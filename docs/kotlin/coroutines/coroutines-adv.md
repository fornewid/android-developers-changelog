---
title: https://developer.android.com/kotlin/coroutines/coroutines-adv
url: https://developer.android.com/kotlin/coroutines/coroutines-adv
source: md.txt
---

# Improve app performance with Kotlin coroutines

[Kotlin coroutines](https://kotlinlang.org/docs/reference/coroutines/coroutines-guide.html)enable you to write clean, simplified asynchronous code that keeps your app responsive while managing long-running tasks such as network calls or disk operations.

This topic provides a detailed look at coroutines on Android. If you're unfamiliar with coroutines, be sure to read[Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines)before reading this topic.

## Manage long-running tasks

Coroutines build upon regular functions by adding two operations to handle long-running tasks. In addition to`invoke`(or`call`) and`return`, coroutines add`suspend`and`resume`:

- `suspend`pauses the execution of the current coroutine, saving all local variables.
- `resume`continues execution of a suspended coroutine from the place where it was suspended.

You can call`suspend`functions only from other`suspend`functions or by using a coroutine builder such as`launch`to start a new coroutine.

The following example shows a simple coroutine implementation for a hypothetical long-running task:  

    suspend fun fetchDocs() {                             // Dispatchers.Main
        val result = get("https://developer.android.com") // Dispatchers.IO for `get`
        show(result)                                      // Dispatchers.Main
    }

    suspend fun get(url: String) = withContext(Dispatchers.IO) { /* ... */ }

In this example,`get()`still runs on the main thread, but it suspends the coroutine before it starts the network request. When the network request completes,`get`resumes the suspended coroutine instead of using a callback to notify the main thread.

Kotlin uses a*stack frame*to manage which function is running along with any local variables. When suspending a coroutine, the current stack frame is copied and saved for later. When resuming, the stack frame is copied back from where it was saved, and the function starts running again. Even though the code might look like an ordinary sequential blocking request, the coroutine ensures that the network request avoids blocking the main thread.

## Use coroutines for main-safety

Kotlin coroutines use*dispatchers* to determine which threads are used for coroutine execution. To run code outside of the main thread, you can tell Kotlin coroutines to perform work on either the*Default* or*IO*dispatcher. In Kotlin, all coroutines must run in a dispatcher, even when they're running on the main thread. Coroutines can suspend themselves, and the dispatcher is responsible for resuming them.

To specify where the coroutines should run, Kotlin provides three dispatchers that you can use:

- **Dispatchers.Main** - Use this dispatcher to run a coroutine on the main Android thread. This should be used only for interacting with the UI and performing quick work. Examples include calling`suspend`functions, running Android UI framework operations, and updating[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)objects.
- **Dispatchers.IO** - This dispatcher is optimized to perform disk or network I/O outside of the main thread. Examples include using the[Room component](https://developer.android.com/topic/libraries/architecture/room), reading from or writing to files, and running any network operations.
- **Dispatchers.Default**- This dispatcher is optimized to perform CPU-intensive work outside of the main thread. Example use cases include sorting a list and parsing JSON.

Continuing the previous example, you can use the dispatchers to re-define the`get`function. Inside the body of`get`, call`withContext(Dispatchers.IO)`to create a block that runs on the IO thread pool. Any code you put inside that block always executes via the`IO`dispatcher. Since`withContext`is itself a suspend function, the function`get`is also a suspend function.  

    suspend fun fetchDocs() {                      // Dispatchers.Main
        val result = get("developer.android.com")  // Dispatchers.Main
        show(result)                               // Dispatchers.Main
    }

    suspend fun get(url: String) =                 // Dispatchers.Main
        withContext(Dispatchers.IO) {              // Dispatchers.IO (main-safety block)
            /* perform network IO here */          // Dispatchers.IO (main-safety block)
        }                                          // Dispatchers.Main
    }

With coroutines, you can dispatch threads with fine-grained control. Because`withContext()`lets you control the thread pool of any line of code without introducing callbacks, you can apply it to very small functions like reading from a database or performing a network request. A good practice is to use`withContext()`to make sure every function is*main-safe*, which means that you can call the function from the main thread. This way, the caller never needs to think about which thread should be used to execute the function.

In the previous example,`fetchDocs()`executes on the main thread; however, it can safely call`get`, which performs a network request in the background. Because coroutines support`suspend`and`resume`, the coroutine on the main thread is resumed with the`get`result as soon as the`withContext`block is done.
| **Important:** Using`suspend`doesn't tell Kotlin to run a function on a background thread. It's normal for`suspend`functions to operate on the main thread. It's also common to launch coroutines on the main thread. You should always use`withContext()`inside a`suspend`function when you need main-safety, such as when reading from or writing to disk, performing network operations, or running CPU-intensive operations.

### Performance of withContext()

[`withContext()`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/with-context.html)does not add extra overhead compared to an equivalent callback-based implementation. Furthermore, it's possible to optimize`withContext()`calls beyond an equivalent callback-based implementation in some situations. For example, if a function makes ten calls to a network, you can tell Kotlin to switch threads only once by using an outer`withContext()`. Then, even though the network library uses`withContext()`multiple times, it stays on the same dispatcher and avoids switching threads. In addition, Kotlin optimizes switching between`Dispatchers.Default`and`Dispatchers.IO`to avoid thread switches whenever possible.
| **Important:** Using a dispatcher that uses a thread pool like`Dispatchers.IO`or`Dispatchers.Default`does not guarantee that the block executes on the same thread from top to bottom. In some situations, Kotlin coroutines might move execution to another thread after a`suspend`-and-`resume`. This means thread-local variables might not point to the same value for the entire`withContext()`block.

## Start a coroutine

You can start coroutines in one of two ways:

- [`launch`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/launch.html)starts a new coroutine and doesn't return the result to the caller. Any work that is considered "fire and forget" can be started using`launch`.
- [`async`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/async.html)starts a new coroutine and allows you to return a result with a suspend function called`await`.

Typically, you should`launch`a new coroutine from a regular function, as a regular function cannot call`await`. Use`async`only when inside another coroutine or when inside a suspend function and performing parallel decomposition.
| **Warning:** `launch`and`async`handle exceptions differently. Since`async`expects an eventual call to`await`, it holds exceptions and rethrows them as part of the`await`call. This means if you use`async`to start a new coroutine from a regular function, you might silently drop an exception. These dropped exceptions won't appear in your crash metrics or be noted in logcat. For more information, see[Cancellation and Exceptions in Coroutines](https://medium.com/androiddevelopers/cancellation-in-coroutines-aa6b90163629).

### Parallel decomposition

All coroutines that are started inside a`suspend`function must be stopped when that function returns, so you likely need to guarantee that those coroutines finish before returning. With*structured concurrency* in Kotlin, you can define a`coroutineScope`that starts one or more coroutines. Then, using`await()`(for a single coroutine) or`awaitAll()`(for multiple coroutines), you can guarantee that these coroutines finish before returning from the function.

As an example, let's define a`coroutineScope`that fetches two documents asynchronously. By calling`await()`on each deferred reference, we guarantee that both`async`operations finish before returning a value:  

    suspend fun fetchTwoDocs() =
        coroutineScope {
            val deferredOne = async { fetchDoc(1) }
            val deferredTwo = async { fetchDoc(2) }
            deferredOne.await()
            deferredTwo.await()
        }

You can also use`awaitAll()`on collections, as shown in the following example:  

    suspend fun fetchTwoDocs() =        // called on any Dispatcher (any thread, possibly Main)
        coroutineScope {
            val deferreds = listOf(     // fetch two docs at the same time
                async { fetchDoc(1) },  // async returns a result for the first doc
                async { fetchDoc(2) }   // async returns a result for the second doc
            )
            deferreds.awaitAll()        // use awaitAll to wait for both network requests
        }

Even though`fetchTwoDocs()`launches new coroutines with`async`, the function uses`awaitAll()`to wait for those launched coroutines to finish before returning. Note, however, that even if we had not called`awaitAll()`, the`coroutineScope`builder does not resume the coroutine that called`fetchTwoDocs`until after all of the new coroutines completed.

In addition,`coroutineScope`catches any exceptions that the coroutines throw and routes them back to the caller.

For more information on parallel decomposition, see[Composing suspending functions](https://kotlinlang.org/docs/reference/coroutines/composing-suspending-functions.html).

## Coroutines concepts

### CoroutineScope

A[`CoroutineScope`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)keeps track of any coroutine it creates using`launch`or`async`. The ongoing work (i.e. the running coroutines) can be cancelled by calling`scope.cancel()`at any point in time. In Android, some KTX libraries provide their own`CoroutineScope`for certain lifecycle classes. For example,`ViewModel`has a[`viewModelScope`](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.ViewModel).viewModelScope:kotlinx.coroutines.CoroutineScope), and`Lifecycle`has[`lifecycleScope`](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#lifecyclescope). Unlike a dispatcher, however, a`CoroutineScope`doesn't run the coroutines.
| **Note:** For more information about`viewModelScope`, see[Easy Coroutines in Android: viewModelScope](https://medium.com/androiddevelopers/easy-coroutines-in-android-viewmodelscope-25bffb605471).

`viewModelScope`is also used in the examples found in[Background threading on Android with Coroutines](https://developer.android.com/kotlin/coroutines). However, if you need to create your own`CoroutineScope`to control the lifecycle of coroutines in a particular layer of your app, you can create one as follows:  

    class ExampleClass {

        // Job and Dispatcher are combined into a CoroutineContext which
        // will be discussed shortly
        val scope = CoroutineScope(Job() + Dispatchers.Main)

        fun exampleMethod() {
            // Starts a new coroutine within the scope
            scope.launch {
                // New coroutine that can call suspend functions
                fetchDocs()
            }
        }

        fun cleanUp() {
            // Cancel the scope to cancel ongoing coroutines work
            scope.cancel()
        }
    }

A cancelled scope cannot create more coroutines. Therefore, you should call`scope.cancel()`only when the class that controls its lifecycle is being destroyed. When using`viewModelScope`, the[`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel)class cancels the scope automatically for you in the ViewModel's`onCleared()`method.

### Job

A[`Job`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/index.html)is a handle to a coroutine. Each coroutine that you create with`launch`or`async`returns a`Job`instance that uniquely identifies the coroutine and manages its lifecycle. You can also pass a`Job`to a`CoroutineScope`to further manage its lifecycle, as shown in the following example:  

    class ExampleClass {
        ...
        fun exampleMethod() {
            // Handle to the coroutine, you can control its lifecycle
            val job = scope.launch {
                // New coroutine
            }

            if (...) {
                // Cancel the coroutine started above, this doesn't affect the scope
                // this coroutine was launched in
                job.cancel()
            }
        }
    }

### CoroutineContext

A[`CoroutineContext`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-coroutine-context/index.html)defines the behavior of a coroutine using the following set of elements:

- [`Job`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/index.html): Controls the lifecycle of the coroutine.
- [`CoroutineDispatcher`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/index.html): Dispatches work to the appropriate thread.
- [`CoroutineName`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-name/index.html): The name of the coroutine, useful for debugging.
- [`CoroutineExceptionHandler`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-exception-handler/index.html): Handles uncaught exceptions.

For new coroutines created within a scope, a new`Job`instance is assigned to the new coroutine, and the other`CoroutineContext`elements are inherited from the containing scope. You can override the inherited elements by passing a new`CoroutineContext`to the`launch`or`async`function. Note that passing a`Job`to`launch`or`async`has no effect, as a new instance of`Job`is always assigned to a new coroutine.  

    class ExampleClass {
        val scope = CoroutineScope(Job() + Dispatchers.Main)

        fun exampleMethod() {
            // Starts a new coroutine on Dispatchers.Main as it's the scope's default
            val job1 = scope.launch {
                // New coroutine with CoroutineName = "coroutine" (default)
            }

            // Starts a new coroutine on Dispatchers.Default
            val job2 = scope.launch(Dispatchers.Default + CoroutineName("BackgroundCoroutine")) {
                // New coroutine with CoroutineName = "BackgroundCoroutine" (overridden)
            }
        }
    }

| **Note:** For more information about[`CoroutineExceptionHandler`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-exception-handler/index.html), see[exceptions in coroutines blog post](https://medium.com/androiddevelopers/exceptions-in-coroutines-ce8da1ec060c).

## Additional coroutines resources

For more coroutines resources, see the following links:

- [Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines)
- [Additional resources for Kotlin coroutines and flow](https://developer.android.com/kotlin/coroutines/additional-resources)