---
title: https://developer.android.com/kotlin/coroutines/test
url: https://developer.android.com/kotlin/coroutines/test
source: md.txt
---

Unit testing code that uses [coroutines](https://developer.android.com/kotlin/coroutines) requires some extra attention, as their execution can be asynchronous and happen across multiple threads. This guide covers how suspending functions can be tested, the testing constructs you need to be familiar with, and how to make your code that uses coroutines testable.

The APIs used in this guide are part of the [kotlinx.coroutines.test](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/) library. Make sure to [add the artifact](https://github.com/Kotlin/kotlinx.coroutines/tree/master/kotlinx-coroutines-test#using-in-your-project) as a test dependency to your project to have access to these APIs.

    dependencies {
        testImplementation "org.jetbrains.kotlinx:kotlinx-coroutines-test:$coroutines_version"
    }

> [!NOTE]
> **Note:** This guide uses the coroutine testing APIs introduced in kotlinx.coroutines.test 1.6. If you're looking to migrate from an earlier version, use the [migration guide](https://github.com/Kotlin/kotlinx.coroutines/blob/master/kotlinx-coroutines-test/MIGRATION.md).

## Invoking suspending functions in tests

To call suspending functions in tests, you need to be in a coroutine. As JUnit test functions themselves aren't suspending functions, you need to call a coroutine builder inside your tests to start a new coroutine.

[`runTest`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/run-test.html) is a coroutine builder designed for testing. Use this to wrap any tests that include coroutines. Note that coroutines can be started not only directly in the test body, but also by the objects being used in the test.

```kotlin
suspend fun fetchData(): String {
    delay(1000L)
    return "Hello world"
}

@Test
fun dataShouldBeHelloWorld() = runTest {
    val data = fetchData()
    assertEquals("Hello world", data)
}
```

In general, you should have one invocation of `runTest` per test, and using an [expression body](https://kotlinlang.org/docs/functions.html#single-expression-functions) is recommended.

> [!IMPORTANT]
> **Key Point:** Use [`runTest`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/run-test.html) for tests that use coroutines.

Wrapping your test's code in `runTest` will work for testing basic suspending functions, and it will automatically skip any delays in coroutines, making the test above complete much faster than one second.

However, there are additional considerations to make, depending on what happens in your code under test:

- When your code creates new coroutines other than the top-level test coroutine that `runTest` creates, you'll need to control how those new coroutines are scheduled by [choosing the appropriate `TestDispatcher`](https://developer.android.com/kotlin/coroutines/test#testdispatchers).
- If your code moves the coroutine execution to other dispatchers (for example, by using [`withContext`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/with-context.html)), `runTest` will still generally work, but delays will no longer be skipped, and tests will be less predictable as code runs on multiple threads. For these reasons, in tests you should [inject test dispatchers](https://developer.android.com/kotlin/coroutines/test#injecting-test-dispatchers) to replace real dispatchers.

## TestDispatchers

[`TestDispatchers`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-dispatcher/index.html) are [`CoroutineDispatcher`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-dispatcher/index.html) implementations for testing purposes. You'll need to use `TestDispatchers` if new coroutines are created during the test to make the execution of the new coroutines predictable.

> [!NOTE]
> **Note:** New coroutines can be created directly in the test body, but also in any of the code you're calling in your test (for example, inside the objects you're testing).

There are two available implementations of `TestDispatcher`: [`StandardTestDispatcher`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-standard-test-dispatcher.html) and [`UnconfinedTestDispatcher`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-unconfined-test-dispatcher.html), which perform different scheduling of newly-started coroutines. These both use a [`TestCoroutineScheduler`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-coroutine-scheduler/index.html) to control virtual time and manage running coroutines within a test.

**There should only be one scheduler instance used in a test** , shared between all `TestDispatchers`. See [Injecting TestDispatchers](https://developer.android.com/kotlin/coroutines/test#injecting-test-dispatchers) to learn about sharing schedulers.

To start the top-level test coroutine, `runTest` creates a [`TestScope`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-scope.html), which is an implementation of [`CoroutineScope`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/) that will always use a `TestDispatcher`. If not specified, a `TestScope` will create a `StandardTestDispatcher` by default, and use that to run the top-level test coroutine.

`runTest` keeps track of the coroutines that are queued on the scheduler used by the dispatcher of its `TestScope`, and will not return as long as there's pending work on that scheduler.

> [!IMPORTANT]
> **Key Point:** `runTest` runs the test coroutine in a `TestScope`, using a `TestDispatcher. TestDispatchers` use a `TestCoroutineScheduler` to control virtual time and schedule new coroutines in a test. All `TestDispatchers` in a test must use the same scheduler instance.

### StandardTestDispatcher

When you start new coroutines on a `StandardTestDispatcher`, they are queued up on the underlying scheduler, to be run whenever the test thread is free to use. To let these new coroutines run, you need to *yield* the test thread (free it up for other coroutines to use). This queueing behavior gives you precise control over how new coroutines run during the test, and it resembles the scheduling of coroutines in production code.

> [!NOTE]
> **Note:** For simplicity, the examples here show new coroutines started directly within `runTest`, as `runTest` uses a `StandardTestDispatcher` by default. However, the scheduling behavior shown here applies to any coroutine started on a `StandardTestDispatcher`, including ones [injected](https://developer.android.com/kotlin/coroutines/test#injecting-test-dispatchers) into classes under test.

If the test thread is never yielded during the execution of the top-level test coroutine, any new coroutines will only run after the test coroutine is done (but before `runTest` returns):

```kotlin
@Test
fun standardTest() = runTest {
    val userRepo = UserRepository()

    launch { userRepo.register("Alice") }
    launch { userRepo.register("Bob") }

    assertEquals(listOf("Alice", "Bob"), userRepo.getAllUsers()) // ❌ Fails
}
```

There are several ways to yield the test coroutine to let queued-up coroutines run. All of these calls let other coroutines run on the test thread before returning:

- [`advanceUntilIdle`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-coroutine-scheduler/advance-until-idle.html): Runs all other coroutines on the scheduler until there is nothing left in the queue. This is a good default choice to let all pending coroutines run, and it will work in most test scenarios.
- [`advanceTimeBy`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-coroutine-scheduler/advance-time-by.html): Advances virtual time by the given amount and runs any coroutines scheduled to run before that point in virtual time.
- [`runCurrent`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-coroutine-scheduler/run-current.html): Runs coroutines that are scheduled at the current virtual time.

To fix the previous test, `advanceUntilIdle` can be used to let the two pending coroutines perform their work before continuing to the assertion:

```kotlin
@Test
fun standardTest() = runTest {
    val userRepo = UserRepository()

    launch { userRepo.register("Alice") }
    launch { userRepo.register("Bob") }
    advanceUntilIdle() // Yields to perform the registrations

    assertEquals(listOf("Alice", "Bob"), userRepo.getAllUsers()) // ✅ Passes
}
```

> [!NOTE]
> **Note:** You could also [`join`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/join.html) the [`Job`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/index.html) instances returned by the `launch` calls to make sure that the new coroutines are done before performing the assertion.

> [!IMPORTANT]
> **Key Point:** `StandardTestDispatcher` offers precise control over the execution of coroutines, which is useful in complex test scenarios. `runTest` uses a `StandardTestDispatcher` by default.

### UnconfinedTestDispatcher

When new coroutines are started on an `UnconfinedTestDispatcher`, they are started eagerly on the current thread. This means that they'll start running immediately, without waiting for their coroutine builder to return. In many cases, this dispatching behavior results in simpler test code, as you don't need to manually yield the test thread to let new coroutines run.

However, this behavior is different from what you'll see in production with non-test dispatchers. If your test focuses on concurrency, prefer using `StandardTestDispatcher` instead.

> [!IMPORTANT]
> **Key Point:** `UnconfinedTestDispatcher` executes new coroutines eagerly, and it can be a good choice for simple tests with coroutines.

To use this dispatcher for the top-level test coroutine in `runTest` instead of the default one, create an instance and pass it in as a parameter. This will make new coroutines created within `runTest` execute eagerly, as they inherit the dispatcher from the `TestScope`.

```kotlin
@Test
fun unconfinedTest() = runTest(UnconfinedTestDispatcher()) {
    val userRepo = UserRepository()

    launch { userRepo.register("Alice") }
    launch { userRepo.register("Bob") }

    assertEquals(listOf("Alice", "Bob"), userRepo.getAllUsers()) // ✅ Passes
}
```

In this example, the launch calls will start their new coroutines eagerly on the `UnconfinedTestDispatcher`, which means that each call to launch will only return after the registration is completed.

> [!IMPORTANT]
> **Key Point:** You can pass in a `TestDispatcher` to `runTest` to control the dispatching behavior in the top-level test coroutine.

> [!NOTE]
> **Note:** Using `runTest` with an `UnconfinedTestDispatcher` provides the same scheduling behavior as [`runBlockingTest`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/run-blocking-test.html), which was part of the coroutine testing APIs before version 1.6.

Remember that `UnconfinedTestDispatcher` starts new coroutines eagerly, but this doesn't mean that it'll run them to completion eagerly as well. If the new coroutine suspends, other coroutines will resume executing.

For example, the new coroutine launched within this test will register Alice, but then it suspends when [`delay`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/delay.html) is called. This lets the top-level coroutine proceed with the assertion, and the test fails as Bob is not registered yet:

```kotlin
@Test
fun yieldingTest() = runTest(UnconfinedTestDispatcher()) {
    val userRepo = UserRepository()

    launch {
        userRepo.register("Alice")
        delay(10L)
        userRepo.register("Bob")
    }

    assertEquals(listOf("Alice", "Bob"), userRepo.getAllUsers()) // ❌ Fails
}
```

## Injecting test dispatchers

Code under test might use dispatchers to switch threads (using [`withContext`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/with-context.html)) or to start new coroutines. When code is executed on multiple threads in parallel, tests can become flaky. It can be difficult to perform assertions at the correct time or to wait for tasks to complete if they're running on background threads that you have no control over.

In tests, replace these dispatchers with instances of `TestDispatchers`. This has several benefits:

- The code will run on the single test thread, making tests more deterministic
- You can control how new coroutines are scheduled and executed
- TestDispatchers use a scheduler for virtual time, which skips delays automatically and lets you advance time manually

Using [dependency injection](https://developer.android.com/training/dependency-injection) to provide
dispatchers to your classes makes it easy to replace the real dispatchers in
tests. In these examples, we'll inject a `CoroutineDispatcher`, but you can also
inject the broader
[`CoroutineContext`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-coroutine-context/)
type, which allows for even more flexibility during tests.

For classes that start coroutines, you can also inject a `CoroutineScope`
instead of a dispatcher, as detailed in the [Injecting a scope](https://developer.android.com/kotlin/coroutines/test#inject-scope)
section.

> [!IMPORTANT]
> **Key Point:** In tests, replace real dispatchers with instances of `TestDispatchers` to ensure that all code runs on the single test thread.

> [!NOTE]
> **Note:** See the [Setting the Main dispatcher](https://developer.android.com/kotlin/coroutines/test#setting-main-dispatcher) section to learn how to replace the Main dispatcher in tests.

`TestDispatchers` will, by default, create a new scheduler when they're instantiated. Inside `runTest`, you can access the `testScheduler` property of the `TestScope` and pass it in to any newly created `TestDispatchers`. This will share their understanding of virtual time, and methods like `advanceUntilIdle` will run coroutines on all test dispatchers to completion.

> [!CAUTION]
> **Caution:** You can create and use any number of `TestDispatchers` within a test, however, they must all share the same scheduler. Be careful not to create multiple schedulers.

In the following example, you can see a `Repository` class that creates a new coroutine using the `IO` dispatcher in its `initialize` method and switches the caller to the `IO` dispatcher in its `fetchData` method:

```kotlin
// Example class demonstrating dispatcher use cases
class Repository(private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO) {
    private val scope = CoroutineScope(ioDispatcher)
    val initialized = AtomicBoolean(false)

    // A function that starts a new coroutine on the IO dispatcher
    fun initialize() {
        scope.launch {
            initialized.set(true)
        }
    }

    // A suspending function that switches to the IO dispatcher
    suspend fun fetchData(): String = withContext(ioDispatcher) {
        require(initialized.get()) { "Repository should be initialized first" }
        delay(500L)
        "Hello world"
    }
}
```

In tests, you can inject a `TestDispatcher` implementation to replace the `IO` dispatcher.

In the example below, we inject a `StandardTestDispatcher` into the repository, and use `advanceUntilIdle` to make sure that the new coroutine started in `initialize` completes before proceeding.

> [!CAUTION]
> **Caution:** Advancing until the new coroutine is done is only possible because the new coroutine uses a `TestDispatcher`. Having to do this reveals that the `initialize` method in the example above is not a well-designed API. It starts asynchronous work that callers need to wait for, but has no way to notify callers when that work is done.

`fetchData` will also benefit from running on a `TestDispatcher`, as it will run on the test thread and skip the delay it contains during the test.

```kotlin
class RepositoryTest {
    @Test
    fun repoInitWorksAndDataIsHelloWorld() = runTest {
        val dispatcher = StandardTestDispatcher(testScheduler)
        val repository = Repository(dispatcher)

        repository.initialize()
        advanceUntilIdle() // Runs the new coroutine
        assertEquals(true, repository.initialized.get())

        val data = repository.fetchData() // No thread switch, delay is skipped
        assertEquals("Hello world", data)
    }
}
```

New coroutines started on a `TestDispatcher` can be advanced manually as shown above with `initialize`. Note, however, that this would not be possible or desirable in production code. Instead, this method should be redesigned to be either suspending (for sequential execution), or to return a `Deferred` value (for concurrent execution).

For example, you can use [`async`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/async.html) to start a new coroutine and create a [`Deferred`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-deferred/index.html):

```kotlin
class BetterRepository(private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO) {
    private val scope = CoroutineScope(ioDispatcher)

    fun initialize() = scope.async {
        // ...
    }
}
```

This lets you safely `await` the completion of this code in both tests and production code:

```kotlin
@Test
fun repoInitWorks() = runTest {
    val dispatcher = StandardTestDispatcher(testScheduler)
    val repository = BetterRepository(dispatcher)

    repository.initialize().await() // Suspends until the new coroutine is done
    assertEquals(true, repository.initialized.get())
    // ...
}
```

> [!NOTE]
> **Note:** Similarly, you can create a new coroutine with `launch` and then call [`join`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/join.html) on the [`Job`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-job/index.html) that it returns to wait for its completion.

`runTest` will wait for pending coroutines to complete before returning if the coroutines are on a `TestDispatcher` that it shares a scheduler with. It will also wait for coroutines that are children of the top-level test coroutine, even if they're on other dispatchers (up to a timeout specified by the `dispatchTimeoutMs` parameter, which is 60 seconds by default).

## Setting the Main dispatcher

In [local unit tests](https://developer.android.com/training/testing/local-tests), the `Main` dispatcher that wraps the Android UI thread will be unavailable, as these tests are executed on a local JVM and not an Android device. If your code under test references the main thread, it'll throw an exception during unit tests.

> [!NOTE]
> **Note:** This only applies to local unit tests. You should not replace the `Main` dispatcher in [instrumented tests](https://developer.android.com/training/testing/instrumented-tests) where the real UI thread is available.

In some cases, you can inject the `Main` dispatcher the same way as other dispatchers, as described in [the previous section](https://developer.android.com/kotlin/coroutines/test#injecting-test-dispatchers), allowing you to replace it with a `TestDispatcher` in tests. However, some APIs such as [`viewModelScope`](https://developer.android.com/topic/libraries/architecture/coroutines#viewmodelscope) use a hardcoded `Main` dispatcher under the hood.

Here's an example of a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel) implementation that uses `viewModelScope` to launch a coroutine that loads data:

```kotlin
class HomeViewModel : ViewModel() {
    private val _message = MutableStateFlow("")
    val message: StateFlow<String> get() = _message

    fun loadMessage() {
        viewModelScope.launch {
            _message.value = "Greetings!"
        }
    }
}
```

To replace the `Main` dispatcher with a `TestDispatcher` in all cases, use the [`Dispatchers.setMain`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/set-main.html) and [`Dispatchers.resetMain`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/reset-main.html) functions.

```kotlin
class HomeViewModelTest {
    @Test
    fun settingMainDispatcher() = runTest {
        val testDispatcher = UnconfinedTestDispatcher(testScheduler)
        Dispatchers.setMain(testDispatcher)

        try {
            val viewModel = HomeViewModel()
            viewModel.loadMessage() // Uses testDispatcher, runs its coroutine eagerly
            assertEquals("Greetings!", viewModel.message.value)
        } finally {
            Dispatchers.resetMain()
        }
    }
}
```

**If the `Main` dispatcher has been replaced with a `TestDispatcher`, any newly-created `TestDispatchers` will automatically use the scheduler from the `Main` dispatcher** , including the `StandardTestDispatcher` created by `runTest` if no other dispatcher is passed to it.

This makes it easier to ensure that there is only a single scheduler in use during the test. For this to work, make sure to create all other `TestDispatcher` instances *after* calling `Dispatchers.setMain`.

> [!IMPORTANT]
> **Key Point:** The `Main` dispatcher should be replaced by a `TestDispatcher` in local unit tests. Replacing the `Main` dispatcher also simplifies sharing schedulers between `TestDispatchers`.

A common pattern to avoid duplicating the code that replaces the `Main` dispatcher in each test is to extract it into a JUnit [test rule](https://junit.org/junit4/javadoc/4.12/org/junit/rules/TestRule.html):

```kotlin
// Reusable JUnit4 TestRule to override the Main dispatcher
class MainDispatcherRule(
    val testDispatcher: TestDispatcher = UnconfinedTestDispatcher(),
) : TestWatcher() {
    override fun starting(description: Description) {
        Dispatchers.setMain(testDispatcher)
    }

    override fun finished(description: Description) {
        Dispatchers.resetMain()
    }
}

class HomeViewModelTestUsingRule {
    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    @Test
    fun settingMainDispatcher() = runTest { // Uses Main's scheduler
        val viewModel = HomeViewModel()
        viewModel.loadMessage()
        assertEquals("Greetings!", viewModel.message.value)
    }
}
```

This rule implementation uses an `UnconfinedTestDispatcher` by default, but a `StandardTestDispatcher` can be passed in as a parameter if the `Main` dispatcher shouldn't execute eagerly in a given test class.

When you need a `TestDispatcher` instance in the test body, you can reuse the `testDispatcher` from the rule, as long as it's the desired type. If you want to be explicit about the type of `TestDispatcher` used in the test, or if you need a `TestDispatcher` that's a different type than the one used for `Main`, you can create a new `TestDispatcher` within `runTest`. As the `Main` dispatcher is set to a `TestDispatcher`, any newly created `TestDispatchers` will share its scheduler automatically.

```kotlin
class DispatcherTypesTest {
    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    @Test
    fun injectingTestDispatchers() = runTest { // Uses Main's scheduler
        // Use the UnconfinedTestDispatcher from the Main dispatcher
        val unconfinedRepo = Repository(mainDispatcherRule.testDispatcher)

        // Create a new StandardTestDispatcher (uses Main's scheduler)
        val standardRepo = Repository(StandardTestDispatcher())
    }
}
```

## Creating dispatchers outside a test

In some cases, you might need a `TestDispatcher` to be available outside the test method. For example, during the initialization of a property in the test class:

```kotlin
class ExampleRepository(private val ioDispatcher: CoroutineDispatcher) { /* ... */ }

class RepositoryTestWithRule {
    private val repository = ExampleRepository(/* What TestDispatcher? */)

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    @Test
    fun someRepositoryTest() = runTest {
        // Test the repository...
        // ...
    }
}
```

If you're replacing the `Main` dispatcher as shown in the previous section, `TestDispatchers` created *after* the `Main` dispatcher has been replaced will automatically share its scheduler.

This isn't the case, however, for `TestDispatchers` created as properties of the test class or `TestDispatchers` created during the initialization of properties in the test class. These are initialized before the `Main` dispatcher is replaced. Therefore, they would create new schedulers.

> [!CAUTION]
> **Caution:** If you create a `TestDispatcher` as a property of a test class, it won't take its scheduler from the `Main` dispatcher, as the `Main` dispatcher is only replaced before each test method is executed.

To make sure that there's only one scheduler in your test, create the `MainDispatcherRule` property first. Then reuse its dispatcher (or its scheduler, if you need a `TestDispatcher` of a different type) in the initializers of other class-level properties as needed.

```kotlin
class RepositoryTestWithRule {
    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    private val repository = ExampleRepository(mainDispatcherRule.testDispatcher)

    @Test
    fun someRepositoryTest() = runTest { // Takes scheduler from Main
        // Any TestDispatcher created here also takes the scheduler from Main
        val newTestDispatcher = StandardTestDispatcher()

        // Test the repository...
    }
}
```

Note that both `runTest` and `TestDispatchers` created within the test will still automatically share the scheduler of the `Main` dispatcher.

If you're not replacing the `Main` dispatcher, create your first `TestDispatcher` (which creates a new scheduler) as a property of the class. Then, manually pass that scheduler to each `runTest` invocation and each new `TestDispatcher` created, both as properties and within the test:

```kotlin
class RepositoryTest {
    // Creates the single test scheduler
    private val testDispatcher = UnconfinedTestDispatcher()
    private val repository = ExampleRepository(testDispatcher)

    @Test
    fun someRepositoryTest() = runTest(testDispatcher.scheduler) {
        // Take the scheduler from the TestScope
        val newTestDispatcher = UnconfinedTestDispatcher(this.testScheduler)
        // Or take the scheduler from the first dispatcher, they're the same
        val anotherTestDispatcher = UnconfinedTestDispatcher(testDispatcher.scheduler)

        // Test the repository...
    }
}
```

In this sample, the scheduler from the first dispatcher is passed to `runTest`. This will create a new `StandardTestDispatcher` for the `TestScope` using that scheduler. You could also pass in the dispatcher to `runTest` directly to run the test coroutine on that dispatcher.

## Creating your own TestScope

Like with `TestDispatchers`, you might need to access a `TestScope` outside the test body. While `runTest` creates a `TestScope` under the hood automatically, you can also create your own `TestScope` to use with `runTest`.

When doing this, make sure to call `runTest` on the `TestScope` you've created:

```kotlin
class SimpleExampleTest {
    val testScope = TestScope() // Creates a StandardTestDispatcher

    @Test
    fun someTest() = testScope.runTest {
        // ...
    }
}
```

> [!CAUTION]
> **Caution:** If you create your own `TestScope`, you must call `runTest` on that scope within your test. There can only be one `TestScope` instance in a test.

The code above creates a `StandardTestDispatcher` for the `TestScope` implicitly, as well as a new scheduler. These objects can all also be created explicitly. This can be useful if you need to integrate it with dependency injection setups.

```kotlin
class ExampleTest {
    val testScheduler = TestCoroutineScheduler()
    val testDispatcher = StandardTestDispatcher(testScheduler)
    val testScope = TestScope(testDispatcher)

    @Test
    fun someTest() = testScope.runTest {
        // ...
    }
}
```

> [!IMPORTANT]
> **Key Point:** You can create all the coroutine testing constructs outside of tests if your project setup requires it.

## Injecting a scope

If you have a class that creates coroutines that you need to control during
tests, you can inject a coroutine scope into that class, replacing it with a
`TestScope` in tests.

In the following example, the `UserState` class depends on a `UserRepository`
to register new users and to fetch the list of registered users. As these calls
to `UserRepository` are suspending function calls, `UserState` uses the injected
`CoroutineScope` to start a new coroutine inside its `registerUser` function.

```kotlin
class UserState(
    private val userRepository: UserRepository,
    private val scope: CoroutineScope,
) {
    private val _users = MutableStateFlow(emptyList<String>())
    val users: StateFlow<List<String>> = _users.asStateFlow()

    fun registerUser(name: String) {
        scope.launch {
            userRepository.register(name)
            _users.update { userRepository.getAllUsers() }
        }
    }
}
```

To test this class, you can pass in the `TestScope` from `runTest` when creating
the `UserState` object:

```kotlin
class UserStateTest {
    @Test
    fun addUserTest() = runTest { // this: TestScope
        val repository = FakeUserRepository()
        val userState = UserState(repository, scope = this)

        userState.registerUser("Mona")
        advanceUntilIdle() // Let the coroutine complete and changes propagate

        assertEquals(listOf("Mona"), userState.users.value)
    }
}
```

> [!TIP]
> **Tip:** If your class creates coroutines that don't complete on their own and should be canceled at the end of the test, you can inject [`TestScope.backgroundScope`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-scope/background-scope.html) instead of the `TestScope` itself.

To inject a scope outside of the test function, for example into an object under
test that's created as a property in the test class, see
[Creating your own TestScope](https://developer.android.com/kotlin/coroutines/test#creating-your-own-testscope).

## Additional resources

- [Testing Kotlin flows on Android](https://developer.android.com/kotlin/flow/test)
- [kotlinx.coroutines.test](https://github.com/Kotlin/kotlinx.coroutines/tree/master/kotlinx-coroutines-test) on GitHub