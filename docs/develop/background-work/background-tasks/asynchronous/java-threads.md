---
title: https://developer.android.com/develop/background-work/background-tasks/asynchronous/java-threads
url: https://developer.android.com/develop/background-work/background-tasks/asynchronous/java-threads
source: md.txt
---

All Android apps use a main thread to handle UI operations. Calling long-running
operations from this main thread can lead to freezes and unresponsiveness. For
example, if your app makes a network request from the main thread, your app's UI
is frozen until it receives the network response. If you use Java, you can
create additional *background threads* to handle long-running operations while
the main thread continues to handle UI updates.

This guide shows how developers using the Java Programming Language can use a
*thread pool* to set up and use multiple threads in an Android app. This guide
also shows you how to define code to run on a thread and how to communicate
between one of these threads and the main thread.

> [!IMPORTANT]
> **Important:** If you're writing your app in Kotlin, we instead recommend [coroutines](https://developer.android.com/kotlin/coroutines) as a lightweight solution for asynchronous background work. Coroutines include features such as structured concurrency, built-in cancellation support, Jetpack integration, and more.

## Concurrency libraries

It's important to understand the basics of threading and its underlying
mechanisms. There are, however, many popular libraries that offer higher-level
abstractions over these concepts and ready-to-use utilities for passing data
between threads. These libraries include [Guava](https://github.com/google/guava/wiki/ListenableFutureExplained) and
[RxJava](https://github.com/ReactiveX/RxJava/wiki) for the Java Programming Language users and [Coroutines](https://developer.android.com/kotlin/coroutines),
which we recommend for Kotlin users.

In practice, you should pick the one that works best for your app and your
development team, though the rules of threading remain the same.

## Examples overview

Based on the [Guide to app architecture](https://developer.android.com/jetpack/docs/guide), the examples in this topic make a
network request and return the result to the main thread, where the app then
might display that result on the screen.

Specifically, the `ViewModel` calls the data layer on the main thread to
trigger the network request. The data layer is in charge of moving the
execution of the network request off the main thread and posting the result back
to the main thread using a callback.

To move the execution of the network request off the main thread, we need to
create other threads in our app.

## Create multiple threads

A [thread pool](https://developer.android.com/reference/java/util/concurrent/ThreadPoolExecutor) is a managed collection of threads that runs tasks in
parallel from a queue. New tasks are executed on existing threads as those
threads become idle. To send a task to a thread pool, use the
[`ExecutorService`](https://developer.android.com/reference/java/util/concurrent/ExecutorService) interface. Note that `ExecutorService` has nothing to do
with [Services](https://developer.android.com/guide/components/services), the Android application component.

Creating threads is expensive, so you should create a thread pool only once as
your app initializes. Be sure to save the instance of the [`ExecutorService`](https://developer.android.com/reference/java/util/concurrent/ExecutorService)
either in your `Application` class or in a [dependency injection container](https://developer.android.com/training/dependency-injection/manual).
The following example creates a thread pool of four threads that we can use to
run background tasks.

    public class MyApplication extends Application {
        ExecutorService executorService = Executors.newFixedThreadPool(4);
    }

There are other ways you can configure a thread pool depending on expected
workload. See [Configuring a thread pool](https://developer.android.com/develop/background-work/background-tasks/asynchronous/java-threads#configuring-a-thread-pool) for more information.

## Execute in a background thread

Making a network request on the main thread causes the thread to wait, or
*block* , until it receives a response. Since the thread is blocked, the OS can't
call `onDraw()`, and your app freezes, potentially leading to an Application Not
Responding (ANR) dialog. Instead, let's run this operation on a background
thread.

### Make the request

First, let's take a look at our `LoginRepository` class and see how it's making
the network request:

    // Result.java
    public abstract class Result<T> {
        private Result() {}

        public static final class Success<T> extends Result<T> {
            public T data;

            public Success(T data) {
                this.data = data;
            }
        }

        public static final class Error<T> extends Result<T> {
            public Exception exception;

            public Error(Exception exception) {
                this.exception = exception;
            }
        }
    }

    // LoginRepository.java
    public class LoginRepository {

        private final String loginUrl = "https://example.com/login";
        private final LoginResponseParser responseParser;

        public LoginRepository(LoginResponseParser responseParser) {
            this.responseParser = responseParser;
        }

        public Result<LoginResponse> makeLoginRequest(String jsonBody) {
            try {
                URL url = new URL(loginUrl);
                HttpURLConnection httpConnection = (HttpURLConnection) url.openConnection();
                httpConnection.setRequestMethod("POST");
                httpConnection.setRequestProperty("Content-Type", "application/json; charset=utf-8");
                httpConnection.setRequestProperty("Accept", "application/json");
                httpConnection.setDoOutput(true);
                httpConnection.getOutputStream().write(jsonBody.getBytes("utf-8"));

                LoginResponse loginResponse = responseParser.parse(httpConnection.getInputStream());
                return new Result.Success<LoginResponse>(loginResponse);
            } catch (Exception e) {
                return new Result.Error<LoginResponse>(e);
            }
        }
    }

`makeLoginRequest()` is synchronous and blocks the calling thread. To model the
response of the network request, we have our own `Result` class.

### Trigger the request

The `ViewModel` triggers the network request when the user taps, for example, on
a button:

    public class LoginViewModel {

        private final LoginRepository loginRepository;

        public LoginViewModel(LoginRepository loginRepository) {
            this.loginRepository = loginRepository;
        }

        public void makeLoginRequest(String username, String token) {
            String jsonBody = "{ username: \"" + username + "\", token: \"" + token + "\" }";
            loginRepository.makeLoginRequest(jsonBody);
        }
    }

With the previous code, `LoginViewModel` is blocking the main thread when making
the network request. We can use the thread pool that we've instantiated to move
the execution to a background thread.

### Handle dependency injection

First, following the [principles of dependency injection](https://developer.android.com/dependency-injection), `LoginRepository`
takes an instance of [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) as opposed to `ExecutorService` because it's
executing code and not managing threads:

    public class LoginRepository {
        ...
        private final Executor executor;

        public LoginRepository(LoginResponseParser responseParser, Executor executor) {
            this.responseParser = responseParser;
            this.executor = executor;
        }
        ...
    }

The Executor's [execute()](https://developer.android.com/reference/java/util/concurrent/Executor#execute(java.lang.Runnable)) method takes a [Runnable](https://developer.android.com/reference/java/lang/Runnable). A `Runnable` is a
Single Abstract Method (SAM) interface with a `run()` method that is executed in
a thread when invoked.

### Execute in the background

Let's create another function called `makeLoginRequest()` that moves the
execution to the background thread and ignores the response for now:

    public class LoginRepository {
        ...
        public void makeLoginRequest(final String jsonBody) {
            executor.execute(new Runnable() {
                @Override
                public void run() {
                    Result<LoginResponse> ignoredResponse = makeSynchronousLoginRequest(jsonBody);
                }
            });
        }

        public Result<LoginResponse> makeSynchronousLoginRequest(String jsonBody) {
            ... // HttpURLConnection logic
        }
        ...
    }

Inside the `execute()` method, we create a new `Runnable` with the block of code
we want to execute in the background thread---in our case, the synchronous network
request method. Internally, the `ExecutorService` manages the `Runnable` and
executes it in an available thread.

> [!NOTE]
> **Note:** In Kotlin, you can use a lambda expression to create an anonymous class that implements the SAM interface.

### Considerations

Any thread in your app can run in parallel to other threads, including the main
thread, so you should ensure that your code is thread-safe. Notice that in our
example that we avoid writing to variables shared between threads, passing
immutable data instead. This is a good practice, because each thread works with
its own instance of data, and we avoid the complexity of synchronization.

If you need to share state between threads, you must be careful to manage access
from threads using synchronization mechanisms such as locks. This is outside of
the scope of this guide. In general you should avoid sharing mutable state
between threads whenever possible.

## Communicate with the main thread

In the previous step, we ignored the network request response. To display the
result on the screen, `LoginViewModel` needs to know about it. We can do that by
using *callbacks*.

The function `makeLoginRequest()` should take a callback as a parameter so that
it can return a value asynchronously. The callback with the result is called
whenever the network request completes or a failure occurs. In Kotlin, we can
use a higher-order function. However, in Java, we have to create a new callback
interface to have the same functionality:

    interface RepositoryCallback<T> {
        void onComplete(Result<T> result);
    }

    public class LoginRepository {
        ...
        public void makeLoginRequest(
            final String jsonBody,
            final RepositoryCallback<LoginResponse> callback
        ) {
            executor.execute(new Runnable() {
                @Override
                public void run() {
                    try {
                        Result<LoginResponse> result = makeSynchronousLoginRequest(jsonBody);
                        callback.onComplete(result);
                    } catch (Exception e) {
                        Result<LoginResponse> errorResult = new Result.Error<>(e);
                        callback.onComplete(errorResult);
                    }
                }
            });
        }
      ...
    }

The `ViewModel` needs to implement the callback now. It can perform different
logic depending on the result:

    public class LoginViewModel {
        ...
        public void makeLoginRequest(String username, String token) {
            String jsonBody = "{ username: \"" + username + "\", token: \"" + token + "\" }";
            loginRepository.makeLoginRequest(jsonBody, new RepositoryCallback<LoginResponse>() {
                @Override
                public void onComplete(Result<LoginResponse> result) {
                    if (result instanceof Result.Success) {
                        // Happy path
                    } else {
                        // Show error in UI
                    }
                }
            });
        }
    }

In this example, the callback is executed in the calling thread, which is a
background thread. This means that you cannot modify or communicate directly
with the UI layer until you switch back to the main thread.

> [!NOTE]
> **Note:** To communicate with the `View` from the `ViewModel` layer, use `LiveData` as recommended in the [Guide to app architecture](https://developer.android.com/jetpack/docs/guide). If the code is being executed on a background thread, you can call `MutableLiveData.postValue()` to communicate with the UI layer.

## Use handlers

You can use a [Handler](https://developer.android.com/reference/android/os/Handler) to enqueue an action to be performed on a different
thread. To specify the thread on which to run the action, construct the
`Handler` using a [Looper](https://developer.android.com/reference/android/os/Looper) for the thread. A `Looper` is an object that runs
the message loop for an associated thread. Once you've created a `Handler`, you
can then use the [post(Runnable)](https://developer.android.com/reference/android/os/Handler#post(java.lang.Runnable)) method to run a block of code in the
corresponding thread.

`Looper` includes a helper function, [getMainLooper()](https://developer.android.com/reference/android/os/Looper#getMainLooper()), which retrieves the
`Looper` of the main thread. You can run code in the main thread by using this
`Looper` to create a `Handler`. As this is something you might do quite often,
you can also save an instance of the `Handler` in the same place you saved the
`ExecutorService`:

    public class MyApplication extends Application {
        ExecutorService executorService = Executors.newFixedThreadPool(4);
        Handler mainThreadHandler = HandlerCompat.createAsync(Looper.getMainLooper());
    }

It's a good practice to inject the handler into the repository, as it gives
you more flexibility. For example, in the future you might want to pass in a
different `Handler` to schedule tasks on a separate thread. If you're always
communicating back to the same thread, you can pass the `Handler` into the
repository constructor, as shown in the following example.

    public class LoginRepository {
        ...
        private final Handler resultHandler;

        public LoginRepository(LoginResponseParser responseParser, Executor executor,
                Handler resultHandler) {
            this.responseParser = responseParser;
            this.executor = executor;
            this.resultHandler = resultHandler;
        }

        public void makeLoginRequest(
            final String jsonBody,
            final RepositoryCallback<LoginResponse> callback
        ) {
            executor.execute(new Runnable() {
                @Override
                public void run() {
                    try {
                        Result<LoginResponse> result = makeSynchronousLoginRequest(jsonBody);
                        notifyResult(result, callback);
                    } catch (Exception e) {
                        Result<LoginResponse> errorResult = new Result.Error<>(e);
                        notifyResult(errorResult, callback);
                    }
                }
            });
        }

        private void notifyResult(
            final Result<LoginResponse> result,
            final RepositoryCallback<LoginResponse> callback,
        ) {
            resultHandler.post(new Runnable() {
                @Override
                public void run() {
                    callback.onComplete(result);
                }
            });
        }
        ...
    }

Alternatively, if you want more flexibility, you can pass in a `Handler` to each
function:

    public class LoginRepository {
        ...

        public void makeLoginRequest(
            final String jsonBody,
            final RepositoryCallback<LoginResponse> callback,
            final Handler resultHandler,
        ) {
            executor.execute(new Runnable() {
                @Override
                public void run() {
                    try {
                        Result<LoginResponse> result = makeSynchronousLoginRequest(jsonBody);
                        notifyResult(result, callback, resultHandler);
                    } catch (Exception e) {
                        Result<LoginResponse> errorResult = new Result.Error<>(e);
                        notifyResult(errorResult, callback, resultHandler);
                    }
                }
            });
        }

        private void notifyResult(
            final Result<LoginResponse> result,
            final RepositoryCallback<LoginResponse> callback,
            final Handler resultHandler
        ) {
            resultHandler.post(new Runnable() {
                @Override
                public void run() {
                    callback.onComplete(result);
                }
            });
        }
    }

In this example, the callback passed into the Repository's `makeLoginRequest`
call is executed on the main thread. That means you can directly modify the UI
from the callback or use `LiveData.setValue()` to communicate with the UI.

## Configure a thread pool

You can create a thread pool using one of the [Executor](https://developer.android.com/reference/java/util/concurrent/Executors) helper functions
with predefined settings, as shown in the previous example code. Alternatively,
if you want to customize the details of the thread pool, you can create an
instance using [ThreadPoolExecutor](https://developer.android.com/reference/java/util/concurrent/ThreadPoolExecutor) directly. You can configure the following
details:

- Initial and maximum pool size.
- *Keep alive time* and time unit. Keep alive time is the maximum duration that a thread can remain idle before it shuts down.
- An input queue that holds `Runnable` tasks. This queue must implement the [BlockingQueue](https://developer.android.com/reference/java/util/concurrent/BlockingQueue) interface. To match the requirements of your app, you can choose from the available queue implementations. To learn more, see the class overview for [ThreadPoolExecutor](https://developer.android.com/reference/java/util/concurrent/ThreadPoolExecutor).

Here's an example that specifies thread pool size based on the total number of
processor cores, a keep alive time of one second, and an input queue.

    public class MyApplication extends Application {
        /*
         * Gets the number of available cores
         * (not always the same as the maximum number of cores)
         */
        private static int NUMBER_OF_CORES = Runtime.getRuntime().availableProcessors();

        // Instantiates the queue of Runnables as a LinkedBlockingQueue
        private final BlockingQueue<Runnable> workQueue = new LinkedBlockingQueue<Runnable>();

        // Sets the amount of time an idle thread waits before terminating
        private static final int KEEP_ALIVE_TIME = 1;
        // Sets the Time Unit to seconds
        private static final TimeUnit KEEP_ALIVE_TIME_UNIT = TimeUnit.SECONDS;

        // Creates a thread pool manager
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(
                NUMBER_OF_CORES,       // Initial pool size
                NUMBER_OF_CORES,       // Max pool size
                KEEP_ALIVE_TIME,
                KEEP_ALIVE_TIME_UNIT,
                workQueue
        );
        ...
    }