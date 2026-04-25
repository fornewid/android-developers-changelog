---
title: https://developer.android.com/blog/posts/under-the-hood-android-17-lock-free-message-queue
url: https://developer.android.com/blog/posts/under-the-hood-android-17-lock-free-message-queue
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Under the hood: Android 17's lock-free MessageQueue

###### 16-min read

![](https://developer.android.com/static/blog/assets/Android_17_s_Lock_Free_Message_Queue_Blog_2169eab465_1EHW3E.webp) 17 Feb 2026 [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/charles-munger)[![](https://developer.android.com/static/blog/assets/shai_1d2925f4dc_ibtbq.webp)](https://developer.android.com/blog/authors/shai-barack)

##### [Charles Munger](https://developer.android.com/blog/authors/charles-munger)
\&
[Shai Barack](https://developer.android.com/blog/authors/shai-barack)

In Android 17, apps targeting SDK 37 or higher will receive a new implementation of MessageQueue where the implementation is lock-free. The new implementation improves performance and reduces missed frames, but may break clients that reflect on MessageQueue private fields and methods. To learn more about the behavior change and how you can mitigate impact, [check out the MessageQueue behavior change documentation](http://developer.android.com/about/versions/17/changes/messagequeue). This technical blog post provides an overview of the MessageQueue rearchitecture and how you can analyze lock contention issues using Perfetto.

The [Looper](https://developer.android.com/reference/android/os/Looper) drives the UI thread of every Android application. It pulls work from a [MessageQueue](https://developer.android.com/reference/android/os/MessageQueue), dispatches it to a [Handler](https://developer.android.com/reference/android/os/Handler), and repeats. For two decades, `MessageQueue` used a single monitor lock (i.e. a `synchronized` code block) to protect its state.

Android 17 introduces a significant update to this component: a lock-free implementation named **DeliQueue**.

This post explains how locks affect UI performance, how to analyze these issues with Perfetto, and the specific algorithms and optimizations used to improve the Android main thread.

### **The problem: Lock Contention and Priority Inversion**

The legacy `MessageQueue` functioned as a priority queue protected by a single lock. If a background thread posts a message while the main thread performs queue maintenance, the background thread blocks the main thread.

When two or more threads are competing for exclusive use of the same lock, this is called **Lock contention** . This contention can cause **Priority Inversion**, leading to UI jank and other performance problems.

Priority inversion can happen when a high-priority thread (like the UI thread) is made to wait for a low-priority thread. Consider this sequence:

1. A *low priority* background thread acquires the `MessageQueue` lock to post the result of work that it did.
2. A *medium priority* thread becomes runnable and the Kernel's scheduler allocates it CPU time, preempting the low priority thread.
3. The *high priority* UI thread finishes its current task and attempts to read from the queue, but is blocked because the low priority thread holds the lock.

The low-priority thread blocks the UI thread, and the medium-priority work delays it further.
![perfetto1.png](https://developer.android.com/static/blog/assets/perfetto1_441f23086c_22PETm.webp)

#### **Analyzing contention with Perfetto**

You can diagnose these issues using [Perfetto](https://perfetto.dev/). In a standard trace, a thread blocked on a monitor lock enters the sleeping state, and Perfetto shows a slice indicating the lock owner.

When you query trace data, look for slices named "monitor contention with ..." followed by the name of the thread that owns the lock and the code site where the lock was acquired.

#### **Case study: Launcher jank**

To illustrate, let's analyze a trace where a user experienced jank while navigating home on a Pixel phone immediately after taking a photo in the camera app. Below we see a screenshot of Perfetto showing the events leading up to the missed frame:
![launcherJ.png](https://developer.android.com/static/blog/assets/launcher_J_74ad16e6d4_ZRDexG.webp)

- **Symptom:** The Launcher main thread missed its frame deadline. It blocked for 18ms, which exceeds the 16ms deadline required for 60Hz rendering.
- **Diagnosis:** Perfetto showed the main thread blocked on the `MessageQueue` lock. A "BackgroundExecutor" thread owned the lock.
- **Root Cause:** The BackgroundExecutor runs at [Process.THREAD_PRIORITY_BACKGROUND](https://developer.android.com/reference/android/os/Process#THREAD_PRIORITY_BACKGROUND) (very low priority). It performed a non-urgent task (checking [app usage limits](https://www.android.com/digital-wellbeing/)). Simultaneously, medium priority threads were using CPU time to process data from the camera. The OS scheduler preempted the BackgroundExecutor thread to run the camera threads.

This sequence caused the Launcher's UI thread (high priority) to become indirectly blocked by the camera worker thread (medium priority), which was keeping the Launcher's background thread (low priority) from releasing the lock.

#### **Querying traces with PerfettoSQL**

You can use [PerfettoSQL](https://perfetto.dev/docs/analysis/perfetto-sql-getting-started) to [query trace data](https://perfetto.dev/docs/analysis/batch-trace-processor) for specific patterns. This is useful if you have a large bank of traces from user devices or tests, and you're searching for specific traces that demonstrate a problem.

For example, this query finds `MessageQueue` contention coincident with dropped frames (jank):

```
INCLUDE PERFETTO MODULE android.monitor_contention;
INCLUDE PERFETTO MODULE android.frames.jank_type;

SELECT
  process_name,
  -- Convert duration from nanoseconds to milliseconds
  SUM(dur) / 1000000 AS sum_dur_ms,
  COUNT(*) AS count_contention
FROM android_monitor_contention
WHERE is_blocked_thread_main
AND short_blocked_method LIKE "%MessageQueue%" 

-- Only look at app processes that had jank
AND upid IN (
  SELECT DISTINCT(upid)
  FROM actual_frame_timeline_slice
  WHERE android_is_app_jank_type(jank_type) = TRUE
)
GROUP BY process_name
ORDER BY SUM(dur) DESC;
```

In this more complex example, join trace data that spans multiple tables to identify MessageQueue contention during app startup:

```
INCLUDE PERFETTO MODULE android.monitor_contention; 
INCLUDE PERFETTO MODULE android.startup.startups; 

-- Join package and process information for startups
DROP VIEW IF EXISTS startups; 
CREATE VIEW startups AS 
SELECT startup_id, ts, dur, upid 
FROM android_startups 
JOIN android_startup_processes USING(startup_id); 

-- Intersect monitor contention with startups in the same process.
DROP TABLE IF EXISTS monitor_contention_during_startup; 
CREATE VIRTUAL TABLE monitor_contention_during_startup 
USING SPAN_JOIN(android_monitor_contention PARTITIONED upid, startups PARTITIONED upid); 

SELECT 
  process_name, 
  SUM(dur) / 1000000 AS sum_dur_ms, 
  COUNT(*) AS count_contention 
FROM monitor_contention_during_startup 
WHERE is_blocked_thread_main 
AND short_blocked_method LIKE "%MessageQueue%" 
GROUP BY process_name 
ORDER BY SUM(dur) DESC;
```

You can use your favorite LLM to write PerfettoSQL queries to find other patterns.

At Google, we use [BigTrace](https://perfetto.dev/docs/deployment/deploying-bigtrace-on-a-single-machine) to run PerfettoSQL queries across millions of traces. In doing so, we confirmed that what we saw anecdotally was, in fact, a systemic issue. The data revealed that `MessageQueue` lock contention impacts users across the entire ecosystem, substantiating the need for a fundamental architectural change.

### **Solution: lock-free concurrency**

We addressed the `MessageQueue` contention problem by implementing a **lock-free data structure** , using atomic memory operations rather than exclusive locks to synchronize access to shared state. A data structure or algorithm is lock-free if at least one thread can always make progress regardless of the scheduling behavior of the other threads. This property is generally hard to achieve, and is [usually not worth pursuing for most code](https://abseil.io/docs/cpp/atomic_danger).

#### **The atomic primitives**

Lock-free software often relies on atomic Read-Modify-Write primitives that the hardware provides.

On older generation ARM64 CPUs, atomics used a Load-Link/Store-Conditional (LL/SC) loop. The CPU loads a value and marks the address. If another thread writes to that address, the store fails, and the loop retries. Because the threads can keep trying and succeed without waiting for another thread, this operation is lock-free.

```
ARM64 LL/SC loop example
retry:
    ldxr    x0, [x1]        // Load exclusive from address x1 to x0
    add     x0, x0, #1      // Increment value by 1
    stxr    w2, x0, [x1]    // Store exclusive.
                            // w2 gets 0 on success, 1 on failure
    cbnz    w2, retry       // If w2 is non-zero (failed), branch to retr
```

([view in Compiler Explorer](https://godbolt.org/z/GPs9GeGhG))

Newer ARM architectures (ARMv8.1) support **Large System Extensions (LSE)** which include instructions in the form of Compare-And-Swap (CAS) or Load-And-Add (demonstrated below). In Android 17 we added support to the Android Runtime (ART) compiler to detect when LSE is supported and emit optimized instructions:

```
/ ARMv8.1 LSE atomic example
ldadd   x0, x1, [x2]    // Atomic load-add.
                        // Faster, no loop required.
```

In our benchmarks, high-contention code that uses CAS achieves a \~3x speedup over the LL/SC variant.

The Java programming language offers atomic primitives via [java.util.concurrent.atomic](https://developer.android.com/reference/java/util/concurrent/atomic/package-summary) that rely on these and other specialized CPU instructions.

### **The Data Structure: DeliQueue**

To remove lock contention from `MessageQueue`, our engineers designed a novel data structure called **DeliQueue** . DeliQueue separates `Message` insertion from `Message` processing:

1. **The list of** `Messages`**(Treiber stack):** A lock-free stack. Any thread can push new `Messages` here without contention.
2. **The priority queue (Min-heap):** A heap of `Messages` to handle, exclusively owned by the Looper thread (hence no synchronization or locks are needed to access).

#### **Enqueue: pushing to a Treiber stack**

The list of `Messages` is kept in a Treiber stack \[1\], a lock-free stack that uses a CAS loop to update the head pointer.

```
public class TreiberStack <E> {
    AtomicReference<Node<E>> top =
            new AtomicReference<Node<E>>();
    public void push(E item) {
        Node<E> newHead = new Node<E>(item);
        Node<E> oldHead;
        do {
            oldHead = top.get();
            newHead.next = oldHead;
        } while (!top.compareAndSet(oldHead, newHead));
    }

    public E pop() {
        Node<E> oldHead;
        Node<E> newHead;
        do {
            oldHead = top.get();
            if (oldHead == null) return null;
            newHead = oldHead.next;
        } while (!top.compareAndSet(oldHead, newHead));
        return oldHead.item;
    }
}
```

*Source code based on Java Concurrency in Practice \[2\], *[*available online*](https://jcip.net/listings/ConcurrentStack.java) and released to the public domain

Any producer can push new `Message`s to the stack at any time. This is like pulling a ticket at a deli counter - your number is determined by when you showed up, but the order you get your food in doesn't have to match. Because it's a linked stack, every `Message` is a sub-stack - you can see what the `Message` queue was like at any point in time by tracking the head and iterating forwards - you won't see any new `Message`s pushed on top, even if they're being added during your traversal.

#### **Dequeue: bulk transfer to a min-heap**

To find the next `Message` to handle, the `Looper` processes new `Message`s from the Treiber stack by walking the stack starting from the top and iterating until it finds the last `Message` that it previously processed. As the `Looper` traverses down the stack, it inserts `Message`s into the deadline-ordered min-heap. Since the `Looper` exclusively owns the heap, it orders and processes `Message`s without locks or atomics.
![dequeue.png](https://developer.android.com/static/blog/assets/dequeue_17341af975_ZornaQ.webp)

In walking down the stack, the `Looper` also creates links from stacked `Message`s back to their predecessors, thus forming a doubly-linked list. Creating the linked list is safe because links pointing down the stack are added via the Treiber stack algorithm with CAS, and links up the stack are only ever read and modified by the `Looper` thread. These back links are then used to remove `Message`s from arbitrary points in the stack in O(1) time.

This design provides *O*(1) insertion for producers (threads posting work to the queue) and amortized *O*(log N) processing for the consumer (the `Looper`).

Using a min-heap to order `Message`s also addresses a fundamental flaw in the legacy `MessageQueue`, where `Message`s were kept in a singly-linked list (rooted at the top). In the legacy implementation, removal from the head was *O*(1), but insertion had a worst case of *O(N)* -- scaling poorly for overloaded queues! Conversely, insertion to and removal from the min-heap scale logarithmically, delivering competitive average performance but really excelling in tail latencies.

|---|---|---|
|   | Legacy (locked) `MessageQueue` | DeliQueue |
| Insert | *O(N)* | *O*(1) for calling thread *O(logN)* for `Looper` thread |
| Remove from head | *O*(1) | *O(logN)* |

In the legacy queue implementation, producers and the consumer used a lock to coordinate exclusive access to the underlying singly-linked list. In DeliQueue, the Treiber stack handles concurrent access, and the single consumer handles ordering its work queue.

#### **Removal: consistency via tombstones**

DeliQueue is a hybrid data structure, joining a lock-free Treiber stack with a single-threaded min-heap. Keeping these two structures in sync without a global lock presents a unique challenge: a message might be physically present in the stack but logically removed from the queue.

To solve this, DeliQueue uses a technique called "tombstoning." Each `Message` tracks its position in the stack via the backwards and forwards pointers, its index in the heap's array, and a boolean flag indicating whether it has been removed. When a `Message` is ready to run, the `Looper` thread will CAS its removed flag, then remove it from the heap and stack.

When another thread needs to remove a `Message`, it doesn't immediately extract it from the data structure. Instead, it performs the following steps:

1. Logical removal: the thread uses a CAS to atomically set the `Message`'s removal flag from false to true. The `Message` remains in the data structure as evidence of its pending removal, a so-called "tombstone". Once a `Message` is flagged for removal, DeliQueue treats it as if it no longer exists in the queue whenever it's found.
2. Deferred cleanup: The actual removal from the data structure is the responsibility of the `Looper` thread, and is deferred until later. Rather than modifying the stack or heap, the remover thread adds the `Message` to another lock-free freelist stack.
3. Structural removal: Only the `Looper` can interact with the heap or remove elements from the stack. When it wakes up, it clears the freelist and processes the `Message`s it contained. Each `Message` is then unlinked from the stack and removed from the heap.

This approach keeps all management of the heap single-threaded. It minimizes the number of concurrent operations and memory barriers required, making the critical path faster and simpler.

#### **Traversal: benign Java memory model data races**

Most concurrency APIs, such as `Future` in the Java standard library, or Kotlin's `Job` and `Deferred`, include a mechanism to cancel work before it completes. An instance of one of these classes matches 1:1 with a unit of underlying work, and calling `cancel` on an object cancels the specific operations associated with them.

Today's Android devices have multi-core CPUs and concurrent, generational garbage collection. But when Android was first developed, it was too expensive to allocate one object for each unit of work. Consequently, Android's `Handler` supports cancellation via numerous overloads of `removeMessages` - rather than removing a *specific* `Message`, it removes all `Message`s that match the specified criteria. In practice, this requires iterating through all `Message`s inserted before `removeMessages` was called and removing the ones that match.

When iterating forward, a thread only requires one ordered atomic operation, to read the current head of the stack. After that, ordinary field reads are used to find the next `Message`. If the Looper thread modifies the `next` fields while removing `Message`s, the `Looper`'s write and another thread's read are unsynchronized - this is a *data race*. Normally, a data race is a serious bug that can cause huge problems in your app - leaks, infinite loops, crashes, freezes, and more. However, under certain narrow conditions, data races can be benign within the Java Memory Model. Suppose we start with a stack of:
![headMessage.png](https://developer.android.com/static/blog/assets/head_Message_c0bf0dd8c3_mm1mr.webp)

We perform an atomic read of the head, and see A. A's next pointer points to B. At the same time as we process B, the looper might remove B and C, by updating A to point to C and then D.
![headMessage2.png](https://developer.android.com/static/blog/assets/head_Message2_2faa5aad41_ZrmXie.webp)

Even though `B` and `C` are logically removed, `B` retains its next pointer to `C`, and `C` to `D`. The reading thread continues traversing through the detached removed nodes and eventually rejoins the live stack at `D`.

By designing DeliQueue to handle races between traversal and removal, we allow for safe, lock-free iteration.

#### **Quitting: Native refcount**

`Looper` is backed by a native allocation that must be manually freed once the `Looper` has quit. If some other thread is adding `Message`s while the `Looper` is quitting, it could use the native allocation after it's freed, a memory safety violation. We prevent this using a *tagged refcount*, where one bit of the atomic is used to indicate whether the `Looper` is quitting.

Before using the native allocation, a thread reads the refcount atomic. If the quitting bit is set, it returns that the `Looper` is quitting and the native allocation must not be used. If not, it attempts a CAS to increment the number of active threads using the native allocation. After doing what it needs to, it decrements the count. If the quitting bit was set after its increment but before the decrement, and the count is now zero, then it wakes up the `Looper` thread.

When the `Looper` thread is ready to quit, it uses CAS to set the quitting bit in the atomic. If the refcount was 0, it can proceed to free its native allocation. Otherwise, it parks itself, knowing that it will be woken up when the last user of the native allocation decrements the refcount. This approach does mean that the `Looper` thread waits for the progress of other threads, but only when it's quitting. That only happens once and is not performance sensitive, and it keeps the other code for using the native allocation fully lock-free.
![atomicLayout.png](https://developer.android.com/static/blog/assets/atomic_Layout_a0595dfd75_Z1zR6hw.webp)

There's a lot of other tricks and complexity in the implementation. You can learn more about DeliQueue by reviewing the source code.

#### **Optimization: branchless programming**

While developing and testing DeliQueue, the team ran many benchmarks and carefully profiled the new code. One issue identified using the [simpleperf tool](https://developer.android.com/ndk/guides/simpleperf) was pipeline flushes caused by the `Message` comparator code.

A standard comparator uses conditional jumps, with the condition for deciding which `Message` comes first simplified below:

```
static int compareMessages(@NonNull Message m1, @NonNull Message m2) {
    if (m1 == m2) {
        return 0;
    }

    // Primary queue order is by when.
    // Messages with an earlier when should come first in the queue.
    final long whenDiff = m1.when - m2.when;
    if (whenDiff > 0) return 1;
    if (whenDiff < 0) return -1;

    // Secondary queue order is by insert sequence.
    // If two messages were inserted with the same `when`, the one inserted
    // first should come first in the queue.
    final long insertSeqDiff = m1.insertSeq - m2.insertSeq;
    if (insertSeqDiff > 0) return 1;
    if (insertSeqDiff < 0) return -1;

    return 0;
}
```

This code compiles to conditional jumps (`b.le` and `cbnz` instructions). When the CPU encounters a conditional branch, it can't know whether the branch is taken until the condition is computed, so it doesn't know which instruction to read next, and has to guess, using a technique called *branch prediction*. In a case like binary search, the branch direction will be unpredictably different at each step, so it's likely that half the predictions will be wrong. Branch prediction is often ineffective in searching and sorting algorithms (such as the one used in a min-heap), because the cost of guessing wrong is larger than the improvement from guessing correctly. When the branch predictor guesses wrong, it must throw away the work it did after assuming the predicted value, and start again from the path that was actually taken - this is called a *pipeline flush*.

To find this issue, we profiled our benchmarks using the `branch-misses` performance counter, which records stack traces where the branch predictor guesses wrong. We then visualized the results with [Google pprof](https://github.com/google/pprof), as shown below:
![flame2.png](https://developer.android.com/static/blog/assets/flame2_7a4a6d0dfd_LQVaM.webp)

Recall that the original `MessageQueue` code used a singly-linked list for the ordered queue. Insertion would traverse the list in sorted order as a linear search, stopping at the first element that's past the point of insertion and linking the new `Message` ahead of it. Removal from the head simply required unlinking the head. Whereas DeliQueue uses a min-heap, where mutations require reordering some elements (sifting up or down) with logarithmic complexity in a balanced data structure, where any comparison has an even chance of directing the traversal to a left child or to a right child. The new algorithm is asymptotically faster, but exposes a new bottleneck as the search code stalls on branch misses half the time.

Realizing that branch misses were slowing down our heap code, we optimized the code using **branch-free programming**:

```
// Branchless Logic
static int compareMessages(@NonNull Message m1, @NonNull Message m2) {
    final long when1 = m1.when;
    final long when2 = m2.when;
    final long insertSeq1 = m1.insertSeq;
    final long insertSeq2 = m2.insertSeq;

    // signum returns the sign (-1, 0, 1) of the argument,
    // and is implemented as pure arithmetic:
    // ((num >> 63) | (-num >>> 63))
    final int whenSign = Long.signum(when1 - when2);
    final int insertSeqSign = Long.signum(insertSeq1 - insertSeq2);

    // whenSign takes precedence over insertSeqSign,
    // so the formula below is such that insertSeqSign only matters
    // as a tie-breaker if whenSign is 0.
    return whenSign * 2 + insertSeqSign;
}
```

To understand the optimization, [disassemble the two examples in Compiler Explorer](https://godbolt.org/z/bvGh7aadG) and use [LLVM-MCA](https://llvm.org/docs/CommandGuide/llvm-mca.html), a CPU simulator that can generate an [estimated timeline of CPU cycles](https://godbolt.org/z/EYxn6MasE).

```
The original code:
Index     01234567890123
[0,0]     DeER .    .  .   sub  x0, x2, x3
[0,1]     D=eER.    .  .   cmp  x0, #0
[0,2]     D==eER    .  .   cset w0, ne
[0,3]     .D==eER   .  .   cneg w0, w0, lt
[0,4]     .D===eER  .  .   cmp  w0, #0
[0,5]     .D====eER .  .   b.le #12
[0,6]     . DeE---R .  .   mov  w1, #1
[0,7]     . DeE---R .  .   b    #48
[0,8]     . D==eE-R .  .   tbz  w0, #31, #12
[0,9]     .  DeE--R .  .   mov  w1, #-1
[0,10]    .  DeE--R .  .   b    #36
[0,11]    .  D=eE-R .  .   sub  x0, x4, x5
[0,12]    .   D=eER .  .   cmp  x0, #0
[0,13]    .   D==eER.  .   cset w0, ne
[0,14]    .   D===eER  .   cneg w0, w0, lt
[0,15]    .    D===eER .   cmp  w0, #0
[0,16]    .    D====eER.   csetm        w1, lt
[0,17]    .    D===eE-R.   cmp  w0, #0
[0,18]    .    .D===eER.   csinc        w1, w1, wzr, le
[0,19]    .    .D====eER   mov  x0, x1
[0,20]    .    .DeE---R   ret
```

Note the one conditional branch, `b.le`, which avoids comparing the `insertSeq` fields if the result is already known from comparing the `when` fields.

```
The branchless code:
Index     012345678
[0,0]     DeER .  .   sub       x0, x2, x3
[0,1]     DeER .  .   sub       x1, x4, x5
[0,2]     D=eER.  .   cmp       x0, #0
[0,3]     .D=eER  .   cset      w0, ne
[0,4]     .D==eER .   cneg      w0, w0, lt
[0,5]     .DeE--R .   cmp       x1, #0
[0,6]     . DeE-R .   cset      w1, ne
[0,7]     . D=eER .   cneg      w1, w1, lt
[0,8]     . D==eeER   add       w0, w1, w0, lsl #1
[0,9]     .  DeE--R   ret
```

Here, the branchless implementation takes fewer cycles and instructions than even the shortest path through the branchy code - it's better in all cases. The faster implementation plus the elimination of mispredicted branches resulted in a 5x improvement in some of our benchmarks!

<br />

However, this technique is not always applicable. Branchless approaches generally require doing work that will be thrown away, and if the branch is predictable most of the time, that wasted work can slow your code down. In addition, removing a branch often introduces a *data dependency*. Modern CPUs execute multiple operations per cycle, but they can't execute an instruction until its inputs from a previous instruction are ready. In contrast, a CPU can *speculate* about data in branches, and work ahead if a branch is predicted correctly.

#### **Testing and Validation**

Validating the correctness of lock-free algorithms is notoriously difficult!

In addition to standard unit tests for continuous validation during development, we also wrote rigorous **stress tests** to verify queue invariants and to attempt to induce data races if they existed. In our test labs we could run millions of test instances on emulated devices and on real hardware.

With [**Java ThreadSanitizer**](https://github.com/google/java-thread-sanitizer) (JTSan) instrumentation, we could use the same tests to also detect some data races in our code. JTSan did not find any problematic data races in DeliQueue, but - surprisingly -actually detected two concurrency bugs in the Robolectric framework, which we promptly fixed.

To improve our debugging capabilities, we built new **analysis tools** . Below is an example showing an issue in Android platform code where one thread is overloading another thread with `Message`s, causing a large backlog, visible in Perfetto thanks to the `MessageQueue` instrumentation feature that we added.
![workspace.png](https://developer.android.com/static/blog/assets/workspace_9a45a242f0_Z6jExF.webp)

To enable `MessageQueue` tracing in the `system_server` process, include the following in your Perfetto configuration:

```
data_sources {
  config {
    name: "track_event"
    target_buffer: 0  # Change this per your buffers configuration
    track_event_config {
      enabled_categories: "mq"
    }
  }
}
```

#### **Impact**

DeliQueue improves system and app performance by eliminating locks from `MessageQueue`.

- **Synthetic benchmarks:** multi-threaded insertions into busy queues is up to **5,000x faster** than the legacy `MessageQueue`, thanks to improved concurrency (the Treiber stack) and faster insertions (the min-heap).
- In **Perfetto traces acquired from internal beta testers**, we see a reduction of 15% in app main thread time spent in lock contention.
- On the same test devices, the reduced lock contention leads to significant improvements to the user experience, such as:
  - -4% missed frames in apps.
  - -7.7% missed frames in System UI and Launcher interactions.
  - -9.1% in time from app startup to the first frame drawn, at the 95%ile.

### **Next steps**

DeliQueue is rolling out to apps in Android 17. App developers should review preparing your app for the new lock-free `MessageQueue` on the Android Developers blog to learn how to test their apps.

#### **References**

\[1\] Treiber, R.K., 1986. Systems programming: Coping with parallelism. International Business Machines Incorporated, Thomas J. Watson Research Center.

\[2\] Goetz, B., Peierls, T., Bloch, J., Bowbeer, J., Holmes, D., \& Lea, D. (2006). Java Concurrency in Practice. Addison-Wesley Professional.

###### Written by:

-

  ## [Charles Munger](https://developer.android.com/blog/authors/charles-munger)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/charles-munger) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
-

  ## [Shai Barack](https://developer.android.com/blog/authors/shai-barack)

  ###### Android Platform Performance Lead

  [read_more
  View profile](https://developer.android.com/blog/authors/shai-barack) ![](https://developer.android.com/static/blog/assets/shai_1d2925f4dc_ibtbq.webp) ![](https://developer.android.com/static/blog/assets/shai_1d2925f4dc_ibtbq.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose April '26 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) The Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full BOM mapping), shared element debug tools, trackpad events, and more.

  ###### [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)