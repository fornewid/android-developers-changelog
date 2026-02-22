---
title: https://developer.android.com/training/articles/smp
url: https://developer.android.com/training/articles/smp
source: md.txt
---

# SMP primer for Android

Android 3.0 and later platform versions are optimized to support multiprocessor architectures. This document introduces issues that can arise when writing multithreaded code for symmetric multiprocessor systems in C, C++, and the Java programming language (hereafter referred to simply as "Java" for the sake of brevity). It's intended as a primer for Android app developers, not as a complete discussion on the subject.

## Introduction

SMP is an acronym for "Symmetric Multi-Processor". It describes a design in which two or more identical CPU cores share access to main memory. Until a few years ago, all Android devices were UP (Uni-Processor).

Most --- if not all --- Android devices always had multiple CPUs, but in the past only one of them was used to run applications while others manage various bits of device hardware (for example, the radio). The CPUs may have had different architectures, and the programs running on them couldn't use main memory to communicate with each other.

Most Android devices sold today are built around SMP designs, making things a bit more complicated for software developers. Race conditions in a multi-threaded program may not cause visible problems on a uniprocessor, but may fail regularly when two or more of your threads are running simultaneously on different cores. What's more, code may be more or less prone to failures when run on different processor architectures, or even on different implementations of the same architecture. Code that has been thoroughly tested on x86 may break badly on ARM. Code may start to fail when recompiled with a more modern compiler.

The rest of this document will explain why, and tell you what you need to do to ensure that your code behaves correctly.

## Memory consistency models: Why SMPs are a bit different

This is a high-speed, glossy overview of a complex subject. Some areas will be incomplete, but none of it should be misleading or wrong. As you will see in the next section, the details here are usually not important.

See[Further reading](https://developer.android.com/training/articles/smp#more)at the end of the document for pointers to more thorough treatments of the subject.

Memory consistency models, or often just "memory models", describe the guarantees the programming language or hardware architecture makes about memory accesses. For example, if you write a value to address A, and then write a value to address B, the model might guarantee that every CPU core sees those writes happen in that order.

The model most programmers are accustomed to is*sequential consistency* , which is described like this([Adve \& Gharachorloo](https://developer.android.com/training/articles/smp#more)):

- All memory operations appear to execute one at a time
- All operations in a single thread appear to execute in the order described by that processor's program.

Let's assume temporarily that we have a very simple compiler or interpreter that introduces no surprises: It translates assignments in the source code to load and store instructions in exactly the corresponding order, one instruction per access. We'll also assume for simplicity that each thread executes on its own processor.

If you look at a bit of code and see that it does some reads and writes from memory, on a sequentially-consistent CPU architecture you know that the code will do those reads and writes in the expected order. It's possible that the CPU is actually reordering instructions and delaying reads and writes, but there is no way for code running on the device to tell that the CPU is doing anything other than execute instructions in a straightforward manner. (We'll ignore memory-mapped device driver I/O.)

To illustrate these points it's useful to consider small snippets of code, commonly referred to as*litmus tests*.

Here's a simple example, with code running on two threads:

|     Thread 1     |        Thread 2        |
|------------------|------------------------|
| `A = 3` ` B = 5` | `reg0 = B` ` reg1 = A` |

In this and all future litmus examples, memory locations are represented by capital letters (A, B, C) and CPU registers start with "reg". All memory is initially zero. Instructions are executed from top to bottom. Here, thread 1 stores the value 3 at location A, and then the value 5 at location B. Thread 2 loads the value from location B into reg0, and then loads the value from location A into reg1. (Note that we're writing in one order and reading in another.)

Thread 1 and thread 2 are assumed to execute on different CPU cores. You should**always**make this assumption when thinking about multi-threaded code.

Sequential consistency guarantees that, after both threads have finished executing, the registers will be in one of the following states:

|   Registers    |             States              |
|----------------|---------------------------------|
| reg0=5, reg1=3 | possible (thread 1 ran first)   |
| reg0=0, reg1=0 | possible (thread 2 ran first)   |
| reg0=0, reg1=3 | possible (concurrent execution) |
| reg0=5, reg1=0 | never                           |

To get into a situation where we see B=5 before we see the store to A, either the reads or the writes would have to happen out of order. On a sequentially-consistent machine, that can't happen.

Uni-processors, including x86 and ARM, are normally sequentially consistent. Threads appear to execute in interleaved fashion, as the OS kernel switches between them. Most SMP systems, including x86 and ARM, are not sequentially consistent. For example, it is common for hardware to buffer stores on their way to memory, so that they don't immediately reach memory and become visible to other cores.

The details vary substantially. For example, x86, though not sequentially consistent, still guarantees that reg0 = 5 and reg1 = 0 remains impossible. Stores are buffered, but their order is maintained. ARM, on the other hand, does not. The order of buffered stores is not maintained, and stores may not reach all other cores at the same time. These differences are important to assembly programmers. However, as we will see below, C, C++, or Java programmers can and should program in a way that hides such architectural differences.

So far, we've unrealistically assumed that it is only the hardware that reorders instructions. In reality, the compiler also reorders instructions to improve performance. In our example, the compiler might decide that some later code in Thread 2 needed the value of reg1 before it needed reg0, and thus load reg1 first. Or some prior code may already have loaded A, and the compiler might decide to reuse that value instead of loading A again. In either case, the loads to reg0 and reg1 might be reordered.

Reordering accesses to different memory locations, either in the hardware, or in the compiler, is allowed, since it doesn't affect the execution of a single thread, and it can significantly improve performance. As we will see, with a bit of care, we can also prevent it from affecting the results of multithreaded programs.

Since compilers can also reorder memory accesses, this problem is actually not new to SMPs. Even on a uniprocessor, a compiler could reorder the loads to reg0 and reg1 in our example, and Thread 1 could be scheduled between the reordered instructions. But if our compiler happened to not reorder, we might never observe this problem. On most ARM SMPs, even without compiler reordering, the reordering will probably be seen, possibly after a very large number of successful executions. Unless you're programming in assembly language, SMPs generally just make it more likely you'll see problems that were there all along.

## Data-race-free programming

Fortunately, there is usually an easy way to avoid thinking about any of these details. If you follow some straightforward rules, it's usually safe to forget all of the preceding section except the "sequential consistency" part. Unfortunately, the other complications may become visible if you accidentally violate those rules.

Modern programming languages encourage what's known as a "data-race-free" programming style. So long as you promise not to introduce "data races", and avoid a handful of constructs that tell the compiler otherwise, the compiler and hardware promise to provide sequentially consistent results. This doesn't really mean they avoid memory access reordering. It does mean that if you follow the rules you won't be able to tell that memory accesses are being reordered. It's a lot like telling you that sausage is a delicious and appetizing food, so long as you promise not to visit the sausage factory. Data races are what expose the ugly truth about memory reordering.

### What's a "data race"?

A*data race*occurs when at least two threads simultaneously access the same ordinary data, and at least one of them modifies it. By "ordinary data" we mean something that's not specifically a synchronization object intended for thread communication. Mutexes, condition variables, Java volatiles, or C++ atomic objects are not ordinary data, and their accesses are allowed to race. In fact they are used to prevent data races on other objects.

In order to determine whether two threads simultaneously access the same memory location, we can ignore the memory-reordering discussion from above, and assume sequential consistency. The following program doesn't have a data race if`A`and`B`are ordinary boolean variables that are initially false:

|     Thread 1      |     Thread 2      |
|-------------------|-------------------|
| `if (A) B = true` | `if (B) A = true` |

Since operations are not reordered, both conditions will evaluate to false, and neither variable is ever updated. Thus there cannot be a data race. There is no need to think about what might happen if the load from`A`and store to`B`in Thread 1 were somehow reordered. The compiler is not allowed to reorder Thread 1 by rewriting it as "`B = true; if (!A) B = false`". That would be like making sausage in the middle of town in broad daylight.

Data races are officially defined on basic built-in types like integers and references or pointers. Assigning to an`int`while simultaneously reading it in another thread is clearly a data race. But both the C++ standard library and the Java Collections libraries are written to allow you to also reason about data races at the library level. They promise to not introduce data races unless there are concurrent accesses to the same container, at least one of which updates it. Updating a`set<T>`in one thread while simultaneously reading it in another allows the library to introduce a data race, and can thus be thought of informally as a "library-level data race". Conversely, updating one`set<T>`in one thread, while reading a different one in another, does not result in a data race, because the library promises not to introduce a (low-level) data race in that case.

Normally concurrent accesses to different fields in a data structure cannot introduce a data race. However there is one important exception to this rule: Contiguous sequences of bit-fields in C or C++ are treated as a single "memory location". Accessing any bit-field in such a sequence is treated as accessing all of them for purposes of determining the existence of a data race. This reflects the inability of common hardware to update individual bits without also reading and re-writing adjacent bits. Java programmers have no analogous concerns.

### Avoiding data races

Modern programming languages provide a number of synchronization mechanisms to avoid data races. The most basic tools are:

Locks or Mutexes
:   Mutexes (C++11`std::mutex`, or`pthread_mutex_t`), or`synchronized`blocks in Java can be used to ensure that certain section of code do not run concurrently with other sections of code accessing the same data. We'll refer to these and other similar facilities generically as "locks." Consistently acquiring a specific lock before accessing a shared data structure and releasing it afterwards, prevents data races when accessing the data structure. It also ensures that updates and accesses are atomic, i.e. no other update to the data structure can run in the middle. This is deservedly by far the most common tool for preventing data races. The use of Java`synchronized`blocks or C++`lock_guard`or`unique_lock`ensure that locks are properly released in the event of an exception.

Volatile/atomic variables
:   Java provides`volatile`fields that support concurrent access without introducing data races. Since 2011, C and C++ support`atomic`variables and fields with similar semantics. These are typically more difficult to use than locks, since they only ensure that individual accesses to a single variable are atomic. (In C++ this normally extends to simple read-modify-write operations, like increments. Java requires special method calls for that.) Unlike locks,`volatile`or`atomic`variables can't be used directly to prevent other threads from interfering with longer code sequences.

It's important to note that`volatile`has very different meanings in C++ and Java. In C++,`volatile`does not prevent data races, though older code often uses it as a workaround for the lack of`atomic`objects. This is no longer recommended; in C++, use`atomic<T>`for variables that can be concurrently accessed by multiple threads. C++`volatile`is meant for device registers and the like.

C/C++`atomic`variables or Java`volatile`variables can be used to prevent data races on other variables. If`flag`is declared to have type`atomic<bool>`or`atomic_bool`(C/C++) or`volatile boolean`(Java), and is initially false then the following snippet is data-race-free:

|         Thread 1         |           Thread 2            |
|--------------------------|-------------------------------|
| `A = ...` ` flag = true` | `while (!flag) {}` ` ... = A` |

Since Thread 2 waits for`flag`to be set, the access to`A`in Thread 2 must happen after, and not concurrently with, the assignment to`A`in Thread 1. Thus there is no data race on`A`. The race on`flag`doesn't count as a data race, since volatile/atomic accesses are not "ordinary memory accesses".

The implementation is required to prevent or hide memory reordering sufficiently to make code like the preceding litmus test behave as expected. This normally makes volatile/atomic memory accesses substantially more expensive than ordinary accesses.

Although the preceding example is data-race-free, locks together with`Object.wait()`in Java or condition variables in C/C++ usually provide a better solution that does not involve waiting in a loop while draining battery power.

### When memory reordering becomes visible

Data-race-free programming normally saves us from having to explicitly deal with memory access reordering issues. However, there are several cases in which reordering does become visible:

1. If your program has a bug resulting in an unintentional data race, compiler and hardware transformations can become visible, and the behavior of your program may be surprising. For example, if we forgot to declare`flag`volatile in the preceding example, Thread 2 may see an uninitialized`A`. Or the compiler may decide that flag can't possibly change during Thread 2's loop and transform the program to

   |         Thread 1         |               Thread 2                |
   |--------------------------|---------------------------------------|
   | `A = ...` ` flag = true` | reg0 = flag; while (!reg0) {} ... = A |

   When you debug, you may well see the loop continuing forever in spite of the fact that`flag`is true.
2. C++ provides facilities for explicitly relaxing sequential consistency even if there are no races. Atomic operations can take explicit`memory_order_`... arguments. Similarly, the`java.util.concurrent.atomic`package provides a more restricted set of similar facilities, notably`lazySet()`. And Java programmers occasionally use intentional data races for similar effect. All of these provide performance improvements at a large cost in programming complexity. We discuss them only briefly[below](https://developer.android.com/training/articles/smp#weak).
3. Some C and C++ code is written in an older style, not entirely consistent with current language standards, in which`volatile`variables are used instead of`atomic`ones, and memory ordering is explicitly disallowed by inserting so called*fences* or*barriers*. This requires explicit reasoning about access reordering and understanding of hardware memory models. A coding style along these lines is still used in the Linux kernel. It should not be used in new Android applications, and is also not further discussed here.

## Practice

Debugging memory consistency problems can be very difficult. If a missing lock,`atomic`or`volatile`declaration causes some code to read stale data, you may not be able to figure out why by examining memory dumps with a debugger. By the time you can issue a debugger query, the CPU cores may have all observed the full set of accesses, and the contents of memory and the CPU registers will appear to be in an "impossible" state.

### What not to do in C

Here we present some examples of incorrect code, along with simple ways to fix them. Before we do that, we need to discuss the use of a basic language feature.

#### C/C++ and "volatile"

C and C++`volatile`declarations are a very special purpose tool. They prevent*the compiler* from reordering or removing*volatile* accesses. This can be helpful for code accessing hardware device registers, memory mapped to more than one location, or in connection with`setjmp`. But C and C++`volatile`, unlike Java`volatile`, is not designed for thread communication.

In C and C++, accesses to`volatile`data may be reordered with accessed to non-volatile data, and there are no atomicity guarantees. Thus`volatile`can't be used for sharing data between threads in portable code, even on a uniprocessor. C`volatile`usually does not prevent access reordering by the hardware, so by itself it is even less useful in multi-threaded SMP environments. This is the reason C11 and C++11 support`atomic`objects. You should use those instead.

A lot of older C and C++ code still abuses`volatile`for thread communication. This often works correctly for data that fits in a machine register, provided it is used with either explicit fences or in cases in which memory ordering is not important. But it is not guaranteed to work correctly with future compilers.

#### Examples

In most cases you'd be better off with a lock (like a`pthread_mutex_t`or C++11`std::mutex`) rather than an atomic operation, but we will employ the latter to illustrate how they would be used in a practical situation.  

```c++
MyThing* gGlobalThing = NULL;  // Wrong!  See below.
void initGlobalThing()    // runs in Thread 1
{
    MyStruct* thing = malloc(sizeof(*thing));
    memset(thing, 0, sizeof(*thing));
    thing->x = 5;
    thing->y = 10;
    /* initialization complete, publish */
    gGlobalThing = thing;
}
void useGlobalThing()    // runs in Thread 2
{
    if (gGlobalThing != NULL) {
        int i = gGlobalThing->x;    // could be 5, 0, or uninitialized data
        ...
    }
}
```

The idea here is that we allocate a structure, initialize its fields, and at the very end we "publish" it by storing it in a global variable. At that point, any other thread can see it, but that's fine since it's fully initialized, right?

The problem is that the store to`gGlobalThing`could be observed before the fields are initialized, typically because either the compiler or the processor reordered the stores to`gGlobalThing`and`thing->x`. Another thread reading from`thing->x`could see 5, 0, or even uninitialized data.

The core problem here is a data race on`gGlobalThing`. If Thread 1 calls`initGlobalThing()`while Thread 2 calls`useGlobalThing()`,`gGlobalThing`can be read while being written.

This can be fixed by declaring`gGlobalThing`as atomic. In C++11:  

```c++
atomic<MyThing*> gGlobalThing(NULL);
```

This ensures that the writes will become visible to other threads in the proper order. It also guarantees to prevent some other failure modes that are otherwise allowed, but unlikely to occur on real Android hardware. For example, it ensures that we cannot see a`gGlobalThing`pointer that has only been partially written.

### What not to do in Java

We haven't discussed some relevant Java language features, so we'll take a quick look at those first.

Java technically does not require code to be data-race-free. And there is a small amount of very-carefully-written Java code that works correctly in the presence of data races. However, writing such code is extremely tricky, and we discuss it only briefly below. To make matters worse, the experts who specified the meaning of such code no longer believe the specification is correct. (The specification is fine for data-race-free code.)

For now we will adhere to the data-race-free model, for which Java provides essentially the same guarantees as C and C++. Again, the language provides some primitives that explicitly relax sequential consistency, notably the`lazySet()`and`weakCompareAndSet()`calls in`java.util.concurrent.atomic`. As with C and C++, we will ignore these for now.

#### Java's "synchronized" and "volatile" keywords

The "synchronized" keyword provides the Java language's in-built locking mechanism. Every object has an associated "monitor" that can be used to provide mutually exclusive access. If two threads try to "synchronize" on the same object, one of them will wait until the other completes.

As we mentioned above, Java's`volatile T`is the analog of C++11's`atomic<T>`. Concurrent accesses to`volatile`fields are allowed, and don't result in data races. Ignoring`lazySet()`et al. and data races, it is the Java VM's job to make sure that the result still appears sequentially consistent.

In particular, if thread 1 writes to a`volatile`field, and thread 2 subsequently reads from that same field and sees the newly written value, then thread 2 is also guaranteed to see all writes previously made by thread 1. In terms of memory effect, writing to a volatile is analogous to a monitor release, and reading from a volatile is like a monitor acquire.

There is one notable difference from C++'s`atomic`: If we write`volatile int x;`in Java, then`x++`is the same as`x = x + 1`; it performs an atomic load, increments the result, and then performs an atomic store. Unlike C++, the increment as a whole is not atomic. Atomic increment operations are instead provided by the`java.util.concurrent.atomic`.

#### Examples

Here's a simple,*incorrect* implementation of a monotonic counter:(*[Java theory and practice: Managing volatility](https://developer.android.com/training/articles/smp#more)*).  

```c++
class Counter {
    private int mValue;
    public int get() {
        return mValue;
    }
    public void incr() {
        mValue++;
    }
}
```

Assume`get()`and`incr()`are called from multiple threads, and we want to be sure that every thread sees the current count when`get()`is called. The most glaring problem is that`mValue++`is actually three operations:

1. `reg = mValue`
2. `reg = reg + 1`
3. `mValue = reg`

If two threads execute in`incr()`simultaneously, one of the updates could be lost. To make the increment atomic, we need to declare`incr()`"synchronized".

It's still broken however, especially on SMP. There is still a data race, in that`get()`can access`mValue`concurrently with`incr()`. Under Java rules, the`get()`call can be appear to be reordered with respect to other code. For example, if we read two counters in a row, the results might appear to be inconsistent because the`get()`calls we reordered, either by the hardware or compiler. We can correct the problem by declaring`get()`to be synchronized. With this change, the code is obviously correct.

Unfortunately, we've introduced the possibility of lock contention, which could hamper performance. Instead of declaring`get()`to be synchronized, we could declare`mValue`with "volatile". (Note`incr()`must still use`synchronize`since`mValue++`is otherwise not a single atomic operation.) This also avoids all data races, so sequential consistency is preserved.`incr()`will be somewhat slower, since it incurs both monitor entry/exit overhead, and the overhead associated with a volatile store, but`get()`will be faster, so even in the absence of contention this is a win if reads greatly outnumber writes. (See also[AtomicInteger](https://developer.android.com/reference/java/util/concurrent/atomic/AtomicInteger)for a way to completely remove the synchronized block.)

Here's another example, similar in form to the earlier C examples:  

```c++
class MyGoodies {
    public int x, y;
}
class MyClass {
    static MyGoodies sGoodies;
    void initGoodies() {    // runs in thread 1
        MyGoodies goods = new MyGoodies();
        goods.x = 5;
        goods.y = 10;
        sGoodies = goods;
    }
    void useGoodies() {    // runs in thread 2
        if (sGoodies != null) {
            int i = sGoodies.x;    // could be 5 or 0
            ....
        }
    }
}
```

This has the same problem as the C code, namely that there is a data race on`sGoodies`. Thus the assignment`sGoodies = goods`might be observed before the initialization of the fields in`goods`. If you declare`sGoodies`with the`volatile`keyword, sequential consistency is restored, and things will work as expected.

Note that only the`sGoodies`reference itself is volatile. The accesses to the fields inside it are not. Once`sGoodies`is`volatile`, and memory ordering is properly preserved, the fields cannot be concurrently accessed. The statement`z =
sGoodies.x`will perform a volatile load of`MyClass.sGoodies`followed by a non-volatile load of`sGoodies.x`. If you make a local reference`MyGoodies localGoods = sGoodies`, then a subsequent`z =
localGoods.x`will not perform any volatile loads.

A more common idiom in Java programming is the infamous "double-checked locking":  

```c++
class MyClass {
    private Helper helper = null;
    public Helper getHelper() {
        if (helper == null) {
            synchronized (this) {
                if (helper == null) {
                    helper = new Helper();
                }
            }
        }
        return helper;
    }
}
```

The idea is that we want to have a single instance of a`Helper`object associated with an instance of`MyClass`. We must only create it once, so we create and return it through a dedicated`getHelper()`function. To avoid a race in which two threads create the instance, we need to synchronize the object creation. However, we don't want to pay the overhead for the "synchronized" block on every call, so we only do that part if`helper`is currently null.

This has a data race on the`helper`field. It can be set concurrently with the`helper == null`in another thread.

To see how this can fail, consider the same code rewritten slightly, as if it were compiled into a C-like language (I've added a couple of integer fields to represent`Helper's`constructor activity):  

```c++
if (helper == null) {
    synchronized() {
        if (helper == null) {
            newHelper = malloc(sizeof(Helper));
            newHelper->x = 5;
            newHelper->y = 10;
            helper = newHelper;
        }
    }
    return helper;
}
```

There is nothing to prevent either the hardware or the compiler from reordering the store to`helper`with those to the`x`/`y`fields. Another thread could find`helper`non-null but its fields not yet set and ready to use. For more details and more failure modes, see the "'Double Checked Locking is Broken' Declaration" link in the appendix for more details, or Item 71 ("Use lazy initialization judiciously") in Josh Bloch's*Effective Java, 2nd Edition.*.

There are two ways to fix this:

1. Do the simple thing and delete the outer check. This ensures that we never examine the value of`helper`outside a synchronized block.
2. Declare`helper`volatile. With this one small change, the code in Example J-3 will work correctly on Java 1.5 and later. (You may want to take a minute to convince yourself that this is true.)

Here is another illustration of`volatile`behavior:  

```c++
class MyClass {
    int data1, data2;
    volatile int vol1, vol2;
    void setValues() {    // runs in Thread 1
        data1 = 1;
        vol1 = 2;
        data2 = 3;
    }
    void useValues() {    // runs in Thread 2
        if (vol1 == 2) {
            int l1 = data1;    // okay
            int l2 = data2;    // wrong
        }
    }
}
```

Looking at`useValues()`, if Thread 2 hasn't yet observed the update to`vol1`, then it can't know if`data1`or`data2`has been set yet. Once it sees the update to`vol1`, it knows that`data1`can be safely accessed and correctly read without introducing a data race. However, it can't make any assumptions about`data2`, because that store was performed after the volatile store.

Note that`volatile`cannot be used to prevent reordering of other memory accesses that race with each other. It is not guaranteed to generate a machine memory fence instruction. It can be used to prevent data races by executing code only when another thread has satisfied a certain condition.

### What to do

In C/C++, prefer C++11 synchronization classes, such as`std::mutex`. If not, use the corresponding`pthread`operations. These include the proper memory fences, providing correct (sequentially consistent unless otherwise specified) and efficient behavior on all Android platform versions. Be sure to use them correctly. For example, remember that condition variable waits may spuriously return without being signaled, and should thus appear in a loop.

It's best to avoid using atomic functions directly, unless the data structure you are implementing is extremely simple, like a counter. Locking and unlocking a pthread mutex require a single atomic operation each, and often cost less than a single cache miss, if there's no contention, so you're not going to save much by replacing mutex calls with atomic ops. Lock-free designs for non-trivial data structures require much more care to ensure that higher level operations on the data structure appear atomic (as a whole, not just their explicitly atomic pieces).

If you do use atomic operations, relaxing ordering with`memory_order`... or`lazySet()`may provide performance advantages, but requires deeper understanding than we have conveyed so far. A large fraction of existing code using these is discovered to have bugs after the fact. Avoid these if possible. If your use cases doesn't exactly fit one of those in the next section, make sure you either are an expert, or have consulted one.

Avoid using`volatile`for thread communication in C/C++.

In Java, concurrency problems are often best solved by using an appropriate utility class from the[java.util.concurrent](https://developer.android.com/reference/java/util/concurrent/package-summary)package. The code is well written and well tested on SMP.

Perhaps the safest thing you can do is make your objects immutable. Objects from classes like Java's String and Integer hold data that cannot be changed once an object is created, avoiding all potential for data races on those objects. The book*Effective Java, 2nd Ed.* has specific instructions in "Item 15: Minimize Mutability". Note in particular the importance of declaring Java fields "final"([Bloch](https://developer.android.com/training/articles/smp#more)).

Even if an object is immutable, remember that communicating it to another thread without any kind of synchronization is a data race. This can occasionally be acceptable in Java (see below), but requires great care, and is likely to result in brittle code. If it's not extremely performance critical, add a`volatile`declaration. In C++, communicating a pointer or reference to an immutable object without proper synchronization, like any data race, is a bug. In this case, it is reasonably likely to result in intermittent crashes since, for example, the receiving thread may see an uninitialized method table pointer due to store reordering.

If neither an existing library class, nor an immutable class is appropriate, the Java`synchronized`statement or C++`lock_guard`/`unique_lock`should be used to guard accesses to any field that can be accessed by more than one thread. If mutexes won't work for your situation, you should declare shared fields`volatile`or`atomic`, but you must take great care to understand the interactions between threads. These declarations won't save you from common concurrent programming mistakes, but they will help you avoid the mysterious failures associated with optimizing compilers and SMP mishaps.

You should avoid "publishing" a reference to an object, i.e. making it available to other threads, in its constructor. This is less critical in C++ or if you stick to our "no data races" advice in Java. But it's always good advice, and becomes critical if your Java code is run in other contexts in which the Java security model matters, and untrusted code may introduce a data race by accessing that "leaked" object reference. It's also critical if you choose to ignore our warnings and use some of the techniques in the next section. See([Safe Construction Techniques in Java](https://developer.android.com/training/articles/smp#more))for details

## A little more about weak memory orders

C++11 and later provide explicit mechanisms for relaxing the sequential consistency guarantees for data-race-free programs. Explicit`memory_order_relaxed`,`memory_order_acquire`(loads only), and`memory_order_release`(stores only) arguments for atomic operations each provide strictly weaker guarantees than the default, typically implicit,`memory_order_seq_cst`.`memory_order_acq_rel`provides both`memory_order_acquire`and`memory_order_release`guarantees for atomic read-modify write operations.`memory_order_consume`is not yet sufficiently well specified or implemented to be useful, and should be ignored for now.

The`lazySet`methods in`Java.util.concurrent.atomic`are similar to C++`memory_order_release`stores. Java's ordinary variables are sometimes used as a replacement for`memory_order_relaxed`accesses, though they are actually even weaker. Unlike C++, there is no real mechanism for unordered accesses to variables that are declared as`volatile`.

You should generally avoid these unless there are pressing performance reasons to use them. On weakly ordered machine architectures like ARM, using them will commonly save on the order of a few dozen machine cycles for each atomic operation. On x86, the performance win is limited to stores, and likely to be less noticeable. Somewhat counter-intuitively, the benefit may decrease with larger core counts, as the memory system becomes more of a limiting factor.

The full semantics of weakly ordered atomics are complicated. In general they require precise understanding of the language rules, which we will not go into here. For example:

- The compiler or hardware can move`memory_order_relaxed`accesses into (but not out of) a critical section bounded by a lock acquisition and release. This means that two`memory_order_relaxed`stores may become visible out of order, even if they are separated by a critical section.
- An ordinary Java variable, when abused as a shared counter, may appear to another thread to decrease, even though it is only incremented by a single other thread. But this is not true for C++ atomic`memory_order_relaxed`.

With that as a warning, here we give a small number of idioms that seem to cover many of the use cases for weakly ordered atomics. Many of these are applicable only to C++.

### Non-racing accesses

It is fairly common that a variable is atomic because it is*sometimes* read concurrently with a write, but not all accesses have this issue. For example a variable may need to be atomic because it is read outside a critical section, but all updates are protected by a lock. In that case, a read that happens to be protected by the same lock cannot race, since there cannot be concurrent writes. In such a case, the non-racing access (load in this case), can be annotated with`memory_order_relaxed`without changing the correctness of C++ code. The lock implementation already enforces the required memory ordering with respect to access by other threads, and`memory_order_relaxed`specifies that essentially no additional ordering constraints need to be enforced for the atomic access.

There is no real analog to this in Java.

### Result is not relied upon for correctness

When we use a racing load only to generate a hint, it's generally also OK to not enforce any memory ordering for the load. If the value is not reliable, we also can't reliably use the result to infer anything about other variables. Thus it's OK if memory ordering is not guaranteed, and the load is supplied with a`memory_order_relaxed`argument.

A common instance of this is the use of C++`compare_exchange`to atomically replace`x`by`f(x)`. The initial load of`x`to compute`f(x)`does not need to be reliable. If we get it wrong, the`compare_exchange`will fail and we will retry. It is fine for the initial load of`x`to use a`memory_order_relaxed`argument; only memory ordering for the actual`compare_exchange`matters.

### Atomically modified but unread data

Occasionally data is modified in parallel by multiple threads, but not examined until the parallel computation is complete. A good example of this is a counter that is atomically incremented (e.g. using`fetch_add()`in C++ or`atomic_fetch_add_explicit()`in C) by multiple threads in parallel, but the result of these calls is always ignored. The resulting value is only read at the end, after all updates are complete.

In this case, there is no way to tell whether accesses to this data was reordered, and hence C++ code may use a`memory_order_relaxed`argument.

<br />

Simple event counters are a common example of this. Since it is so common, it is worth making some observations about this case:

- Use of`memory_order_relaxed`improves performance, but may not address the most important performance issue: Every update requires exclusive access to the cache line holding the counter. This results in a cache miss every time a new thread accesses the counter. If updates are frequent and alternate between threads, it is much faster to avoid updating the shared counter every time by, for example, using thread-local counters and summing them at the end.
- This technique is combinable with the previous section: It is possible to concurrently read approximate and unreliable values while they are being updated, with all operations using`memory_order_relaxed`. But it is important to treat the resulting values as completely unreliable. Just because the count appears to have been incremented once does not mean another thread can be counted on to have reached the point at which the increment has been performed. The increment may instead have been reordered with earlier code. (As for the similar case we mentioned earlier, C++ does guarantee that a second load of such a counter will not return a value less than an earlier load in the same thread. Unless of course the counter overflowed.)
- It is common to find code that tries to compute approximate counter values by performing individual atomic (or not) reads and writes, but not making the increment as a whole atomic. The usual argument is that this is "close enough" for performance counters or the like. It's typically not. When updates are sufficiently frequent (a case you probably care about), a large fraction of the counts are typically lost. On a quad core device, more than half the counts may commonly be lost. (Easy exercise: construct a two thread scenario in which the counter is updated a million times, but the final counter value is one.)

### Simple flag communication

A`memory_order_release`store (or read-modify-write operation) ensures that if subsequently a`memory_order_acquire`load (or read-modify-write operation) reads the written value, then it will also observe any stores (ordinary or atomic) that preceded the A`memory_order_release`store. Conversely, any loads preceding the`memory_order_release`will not observe any stores that followed the`memory_order_acquire`load. Unlike`memory_order_relaxed`, this allows such atomic operations to be used to communicate the progress of one thread to another.

For example, we can rewrite the double-checked locking example from above in C++ as  

```c++
class MyClass {
  private:
    atomic<Helper*> helper {nullptr};
    mutex mtx;
  public:
    Helper* getHelper() {
      Helper* myHelper = helper.load(memory_order_acquire);
      if (myHelper == nullptr) {
        lock_guard<mutex> lg(mtx);
        myHelper = helper.load(memory_order_relaxed);
        if (myHelper == nullptr) {
          myHelper = new Helper();
          helper.store(myHelper, memory_order_release);
        }
      }
      return myHelper;
    }
};
```

The acquire load and release store ensure that if we see a non-null`helper`, then we will also see its fields correctly initialized. We've also incorporated the prior observation that non-racing loads can use`memory_order_relaxed`.

A Java programmer could conceivably represent`helper`as a`java.util.concurrent.atomic.AtomicReference<Helper>`and use`lazySet()`as the release store. The load operations would continue to use plain`get()`calls.

In both cases, our performance tweaking concentrated on the initialization path, which is unlikely to be performance critical. A more readable compromise might be:  

```c++
    Helper* getHelper() {
      Helper* myHelper = helper.load(memory_order_acquire);
      if (myHelper != nullptr) {
        return myHelper;
      }
      lock_guard&ltmutex> lg(mtx);
      if (helper == nullptr) {
        helper = new Helper();
      }
      return helper;
    }
```

This provides the same fast path, but resorts to default, sequentially-consistent, operations on the non-performance-critical slow path.

Even here,`helper.load(memory_order_acquire)`is likely to generate the same code on current Android-supported architectures as a plain (sequentially-consistent) reference to`helper`. Really the most beneficial optimization here may be the introduction of`myHelper`to eliminate a second load, though a future compiler might do that automatically.

Acquire/release ordering does not prevent stores from getting visibly delayed, and does not ensure that stores become visible to other threads in a consistent order. As a result, it does not support a tricky, but fairly common coding pattern exemplified by Dekker's mutual exclusion algorithm: All threads first set a flag indicating that they want to do something; if a thread*t* then notices that no other thread is trying to do something, it can safely proceed, knowing that there will be no interference. No other thread will be able to proceed, since*t* 's flag is still set. This fails if the flag is accessed using acquire/release ordering, since that doesn't prevent making a thread's flag visible to others late, after they have erroneously proceeded. Default`memory_order_seq_cst`does prevent it.

### Immutable fields

If an object field is initialized on first use and then never changed, it may be possible to initialize and subsequently read it using weakly ordered accesses. In C++, it could be declared as`atomic`and accessed using`memory_order_relaxed`or in Java, it could be declared without`volatile`and accessed without special measures. This requires that all of the following hold:

- It should be possible to tell from the value of the field itself whether it has already been initialized. To access the field, the fast path test-and-return value should read the field only once. In Java the latter is essential. Even if the field tests as initialized, a second load may read the earlier uninitialized value. In C++ the "read once" rule is merely good practice.
- Both initialization and subsequent loads must be atomic, in that partial updates should not be visible. For Java, the field should not be a`long`or`double`. For C++, an atomic assignment is required; constructing it in place will not work, since construction of an`atomic`is not atomic.
- Repeated initializations must be safe, since multiple threads may read the uninitialized value concurrently. In C++, this generally follows from the "trivially copyable" requirement imposed for all atomic types; types with nested owned pointers would require deallocation in the copy constructor, and would not be trivially copyable. For Java, certain reference types are acceptable:
- Java references are limited to immutable types containing only final fields. The constructor of the immutable type should not publish a reference to the object. In this case the Java final field rules ensure that if a reader sees the reference, it will also see the initialized final fields. C++ has no analog to these rules and pointers to owned objects are unacceptable for this reason as well (in addition to violating the "trivially copyable" requirements).

## Closing notes

While this document does more than merely scratch the surface, it doesn't manage more than a shallow gouge. This is a very broad and deep topic. Some areas for further exploration:

- The actual Java and C++ memory models are expressed in terms of a*happens-before* relation that specifies when two actions are guaranteed to occur in a certain order. When we defined a data race, we informally talked about two memory accesses happening "simultaneously". Officially this is defined as neither one happening before the other. It is instructive to learn the actual definitions of*happens-before* and*synchronizes-with* in the Java or C++ Memory Model. Although the intuitive notion of "simultaneously" is generally good enough, these definitions are instructive, particularly if you are contemplating using weakly ordered atomic operations in C++. (The current Java specification only defines`lazySet()`very informally.)
- Explore what compilers are and aren't allowed to do when reordering code. (The JSR-133 spec has some great examples of legal transformations that lead to unexpected results.)
- Find out how to write immutable classes in Java and C++. (There's more to it than just "don't change anything after construction".)
- Internalize the recommendations in the Concurrency section of*Effective Java, 2nd Edition.*(For example, you should avoid calling methods that are meant to be overridden while inside a synchronized block.)
- Read through the[java.util.concurrent](https://developer.android.com/reference/java/util/concurrent/package-summary)and[java.util.concurrent.atomic](https://developer.android.com/reference/java/util/concurrent/atomic/package-summary)APIs to see what's available. Consider using concurrency annotations like`@ThreadSafe`and`@GuardedBy`(from net.jcip.annotations).

The[Further Reading](https://developer.android.com/training/articles/smp#more)section in the appendix has links to documents and web sites that will better illuminate these topics.

## Appendix

### Implementing synchronization stores

*(This isn't something most programmers will find themselves implementing, but the discussion is illuminating.)*

For small built-in types like`int`, and hardware supported by Android, ordinary load and store instructions ensure that a store will be made visible either in its entirety, or not at all, to another processor loading the same location. Thus some basic notion of "atomicity" is provided for free.

As we saw before, this does not suffice. In order to ensure sequential consistency we also need to prevent reordering of operations, and to ensure that memory operations become visible to other processes in a consistent order. It turns out that the latter is automatic on Android-supported hardware, provided we make judicious choices for enforcing the former, so we largely ignore it here.

Order of memory operations is preserved by both preventing reordering by the compiler, and preventing reordering by the hardware. Here we focus on the latter.

Memory ordering on ARMv7, x86, and MIPS is enforced with "fence" instructions that roughly prevent instructions following the fence from becoming visible before instructions preceding the fence. (These are also commonly called "barrier" instructions, but that risks confusion with`pthread_barrier`-style barriers, which do much more than this.) The precise meaning of fence instructions is a fairly complicated topic that has to address the way in which guarantees provided by multiple different kinds of fences interact, and how these combine with other ordering guarantees usually provided by the hardware. This is a high level overview, so we will gloss over these details.

The most basic kind of ordering guarantee is that provided by C++`memory_order_acquire`and`memory_order_release`atomic operations: Memory operations preceding a release store should be visible following an acquire load. On ARMv7, this is enforced by:

- Preceding the store instruction with a suitable fence instruction. This prevents all prior memory accesses from being reordered with the store instruction. (It also unnecessarily prevents reordering with later store instruction.)
- Following the load instruction with a suitable fence instruction, preventing the load from being reordered with subsequent accesses. (And once again providing unneeded ordering with at least earlier loads.)

Together these suffice for C++ acquire/release ordering. They are necessary, but not sufficient, for Java`volatile`or C++ sequentially consistent`atomic`.

To see what else we need, consider the fragment of Dekker's algorithm we briefly mentioned earlier.`flag1`and`flag2`are C++`atomic`or Java`volatile`variables, both initially false.

|                         Thread 1                          |                         Thread 2                          |
|-----------------------------------------------------------|-----------------------------------------------------------|
| `flag1 = true` ` if (flag2 == false)` ` `*critical-stuff* | `flag2 = true` ` if (flag1 == false)` ` `*critical-stuff* |

Sequential consistency implies that one of the assignments to`flag`*n*must be executed first, and be seen by the test in the other thread. Thus, we will never see these threads executing the "critical-stuff" simultaneously.

But the fencing required for acquire-release ordering only adds fences at the beginning and end of each thread, which doesn't help here. We additionally need to ensure that if a`volatile`/`atomic`store is followed by a`volatile`/`atomic`load, the two are not reordered. This is normally enforced by adding a fence not just before a sequentially consistent store, but also after it. (This is again much stronger than required, since this fence typically orders all earlier memory accesses with respect to all later ones.)

We could instead associate the extra fence with sequentially consistent loads. Since stores are less frequent, the convention we described is more common and used on Android.

As we saw in an earlier section, we need to insert a store/load barrier between the two operations. The code executed in the VM for a volatile access will look something like this:

|             volatile load              |                              volatile store                               |
|----------------------------------------|---------------------------------------------------------------------------|
| `reg = A` ` `*fence for "acquire" (1)* | *fence for "release" (2)* ` A = reg` ` `*fence for later atomic load (3)* |

Real machine architectures commonly provide multiple types of fences, which order different types of accesses and may have different cost. The choice between these is subtle, and influenced by the need to ensure that stores are made visible to other cores in a consistent order, and that the memory ordering imposed by the combination of multiple fences composes correctly. For more details, please see the University of Cambridge page with[collected mappings of atomics to actual processors](https://developer.android.com/training/articles/smp#more).

On some architectures, notably x86, the "acquire" and "release" barriers are unnecessary, since the hardware always implicitly enforces sufficient ordering. Thus on x86 only the last fence (3) is really generated. Similarly on x86, atomic read-modify-write operations implicitly include a strong fence. Thus these never require any fences. On ARMv7 all fences we discussed above are required.

ARMv8 provides LDAR and STLR instructions that directly enforce the requirements of Java volatile or C++ sequentially consistent loads and stores. These avoid the unnecessary reordering constraints we mentioned above. 64-bit Android code on ARM uses these; we chose to focus on ARMv7 fence placement here because it sheds more light on the actual requirements.

### Further reading

Web pages and documents that provide greater depth or breadth. The more generally useful articles are nearer the top of the list.

Shared Memory Consistency Models: A Tutorial
:   Written in 1995 by Adve \& Gharachorloo, this is a good place to start if you want to dive more deeply into memory consistency models.  
    <http://www.hpl.hp.com/techreports/Compaq-DEC/WRL-95-7.pdf>

Memory Barriers
:   Nice little article summarizing the issues.  
    <https://en.wikipedia.org/wiki/Memory_barrier>

Threads Basics
:   An introduction to multi-threaded programming in C++ and Java, by Hans Boehm. Discussion of data races and basic synchronization methods.  
    <http://www.hboehm.info/c++mm/threadsintro.html>

Java Concurrency In Practice
:   Published in 2006, this book covers a wide range of topics in great detail. Highly recommended for anyone writing multi-threaded code in Java.  
    <http://www.javaconcurrencyinpractice.com>

JSR-133 (Java Memory Model) FAQ
:   A gentle introduction to the Java memory model, including an explanation of synchronization, volatile variables, and construction of final fields. (A bit dated, particularly when it discusses other languages.)  
    [http://www.cs.umd.edu/\~pugh/java/memoryModel/jsr-133-faq.html](http://www.cs.umd.edu/~pugh/java/memoryModel/jsr-133-faq.html)

Validity of Program Transformations in the Java Memory Model
:   A rather technical explanation of remaining problems with the Java memory model. These issues do not apply to data-race-free programs.  
    [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.1790\&rep=rep1\&type=pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.1790&rep=rep1&type=pdf)

Overview of package java.util.concurrent
:   The documentation for the`java.util.concurrent`package. Near the bottom of the page is a section entitled "Memory Consistency Properties" that explains the guarantees made by the various classes.  
    [java.util.concurrent](https://developer.android.com/reference/java/util/concurrent/package-summary)Package Summary

Java Theory and Practice: Safe Construction Techniques in Java
:   This article examines in detail the perils of references escaping during object construction, and provides guidelines for thread-safe constructors.  
    <http://www.ibm.com/developerworks/java/library/j-jtp0618.html>

Java Theory and Practice: Managing Volatility
:   A nice article describing what you can and can't accomplish with volatile fields in Java.  
    <http://www.ibm.com/developerworks/java/library/j-jtp06197.html>

The "Double-Checked Locking is Broken" Declaration
:   Bill Pugh's detailed explanation of the various ways in which double-checked locking is broken without`volatile`or`atomic`. Includes C/C++ and Java.  
    [http://www.cs.umd.edu/\~pugh/java/memoryModel/DoubleCheckedLocking.html](http://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html)

\[ARM\] Barrier Litmus Tests and Cookbook
:   A discussion of ARM SMP issues, illuminated with short snippets of ARM code. If you found the examples on this page too un-specific, or want to read the formal description of the DMB instruction, read this. Also describes the instructions used for memory barriers on executable code (possibly useful if you're generating code on the fly). Note that this predates ARMv8, which also supports additional memory ordering instructions and moved to a somewhat stronger memory model. (See the "ARM® Architecture Reference Manual ARMv8, for ARMv8-A architecture profile" for details.)  
    <http://infocenter.arm.com/help/topic/com.arm.doc.genc007826/Barrier_Litmus_Tests_and_Cookbook_A08.pdf>

Linux Kernel Memory Barriers
:   Documentation for Linux kernel memory barriers. Includes some useful examples and ASCII art.  
    <http://www.kernel.org/doc/Documentation/memory-barriers.txt>

ISO/IEC JTC1 SC22 WG21 (C++ standards) 14882 (C++ programming language), section 1.10 and clause 29 ("Atomic operations library")
:   Draft standard for C++ atomic operation features. This version is close to the C++14 standard, which includes minor changes in this area from C++11.  
    <http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2015/n4527.pdf>  
    (intro:<http://www.hpl.hp.com/techreports/2008/HPL-2008-56.pdf>)

ISO/IEC JTC1 SC22 WG14 (C standards) 9899 (C programming language) chapter 7.16 ("Atomics \<stdatomic.h\>")
:   Draft standard for ISO/IEC 9899-201x C atomic operation features. For details, also check later defect reports.  
    <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf>

C/C++11 mappings to processors (University of Cambridge)
:   Jaroslav Sevcik and Peter Sewell's collection of translations of C++ atomics to various common processor instruction sets.  
    [http://www.cl.cam.ac.uk/\~pes20/cpp/cpp0xmappings.html](http://www.cl.cam.ac.uk/~pes20/cpp/cpp0xmappings.html)

Dekker's algorithm
:   The "first known correct solution to the mutual exclusion problem in concurrent programming". The wikipedia article has the full algorithm, with a discussion about how it would need to be updated to work with modern optimizing compilers and SMP hardware.  
    <https://en.wikipedia.org/wiki/Dekker's_algorithm>

Comments on ARM vs. Alpha and address dependencies
:   An e-mail on the arm-kernel mailing list from Catalin Marinas. Includes a nice summary of address and control dependencies.  
    <http://linux.derkeiler.com/Mailing-Lists/Kernel/2009-05/msg11811.html>

What Every Programmer Should Know About Memory
:   A very long and detailed article about different types of memory, particularly CPU caches, by Ulrich Drepper.  
    <http://www.akkadia.org/drepper/cpumemory.pdf>

Reasoning about the ARM weakly consistent memory model
:   This paper was written by Chong \& Ishtiaq of ARM, Ltd. It attempts to describe the ARM SMP memory model in a rigorous but accessible fashion. The definition of "observability" used here comes from this paper. Again, this predates ARMv8.  
    [http://portal.acm.org/ft_gateway.cfm?id=1353528\&type=pdf\&coll=\&dl=\&CFID=96099715\&CFTOKEN=57505711](http://portal.acm.org/ft_gateway.cfm?id=1353528&type=pdf&coll&dl&CFID=96099715&CFTOKEN=57505711)

The JSR-133 Cookbook for Compiler Writers
:   Doug Lea wrote this as a companion to the JSR-133 (Java Memory Model) documentation. It contains the initial set of implementation guidelines for the Java memory model that was used by many compiler writers, and is still widely cited and likely to provide insight. Unfortunately, the four fence varieties discussed here are not a good match for Android-supported architectures, and the above C++11 mappings are now a better source of precise recipes, even for Java.  
    <http://g.oswego.edu/dl/jmm/cookbook.html>

x86-TSO: A Rigorous and Usable Programmer's Model for x86 Multiprocessors
:   A precise description of the x86 memory model. Precise descriptions of the ARM memory model are unfortunately significantly more complicated.  
    [http://www.cl.cam.ac.uk/\~pes20/weakmemory/cacm.pdf](http://www.cl.cam.ac.uk/~pes20/weakmemory/cacm.pdf)