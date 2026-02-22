---
title: https://developer.android.com/training/testing/espresso/idling-resource
url: https://developer.android.com/training/testing/espresso/idling-resource
source: md.txt
---

An *idling resource* represents an asynchronous operation whose results affect
subsequent operations in a UI test. By registering idling resources with
Espresso, you can validate these asynchronous operations more reliably when
testing your app.

## Identify when idling resources are needed

Espresso provides a sophisticated set of
[synchronization capabilities](https://developer.android.com/training/testing/espresso#sync). This
characteristic of the framework, however, applies only to operations that post
messages on the [MessageQueue](https://developer.android.com/reference/android/os/MessageQueue), such as a subclass of
[View](https://developer.android.com/reference/android/view/View) that's drawing its contents on the screen.

Because Espresso isn't aware of any other asynchronous operations, including
those running on a background thread, Espresso can't provide its synchronization
guarantees in those situations. In order to make Espresso aware of your app's
long-running operations, you must register each one as an idling resource.

If you don't use idling resources when testing the results of your app's
asynchronous work, you might find yourself having to use one of the
following bad workarounds to improve your tests' reliability:

- **Adding calls to [Thread.sleep()](https://developer.android.com/reference/java/lang/Thread#sleep(long)).** When you add artificial delays to your tests, it takes longer for your test suite to finish executing, and your tests might still fail sometimes when executed on slower devices. In addition, these delays don't scale well, as your app might have to perform more time-consuming asynchronous work in a future release.
- **Implementing retry wrappers,** which use a loop to repeatedly check whether your app is still performing asynchronous work until a timeout occurs. Even if you specify a maximum retry count in your tests, each re-execution consumes system resources, particularly the CPU.
- **Using instances of [CountDownLatch](https://developer.android.com/reference/java/util/concurrent/CountDownLatch),** which allow one or more threads to wait until a specific number of operations being executed in another thread are complete. These objects require you to specify a timeout length; otherwise, your app might be blocked indefinitely. The latches also add unnecessary complexity to your code, making maintenance more difficult.

Espresso allows you to remove these unreliable workarounds from your tests and
instead register your app's asynchronous work as idling resources.

## Common use cases

When performing operations similar to the following examples in your tests,
consider using an idling resource:

- **Loading data** from the internet or a local data source.
- **Establishing connections** with databases and callbacks.
- **Managing services** , either using a system service or an instance of [IntentService](https://developer.android.com/reference/android/app/IntentService).
- **Performing complex business logic**, such as bitmap transformations.

It's especially important to register idling resources when these operations
update a UI that your tests then validate.
| **Note:** Some third-party libraries use threading schemes that require manual thread management. In these situations, add threading logic to achieve the same functionality benefits as the ones you enjoy by using idling resources directly.

## Example idling resource implementations

The following list describes several example implementations of idling resources
that you can [integrate into your app](https://developer.android.com/training/testing/espresso/idling-resource#integrate-into-app):

[`CountingIdlingResource`](https://developer.android.com/reference/androidx/test/espresso/idling/CountingIdlingResource)
:   Maintains a counter of active tasks. When the counter is zero, the associated
    resource is considered idle. This functionality closely resembles that of a
    [Semaphore](https://developer.android.com/reference/java/util/concurrent/Semaphore). In most cases, this implementation is
    sufficient for managing your app's asynchronous work during testing.

[`UriIdlingResource`](https://developer.android.com/reference/androidx/test/espresso/idling/net/UriIdlingResource)
:   Similar to
    [`CountingIdlingResource`](https://developer.android.com/reference/androidx/test/espresso/idling/CountingIdlingResource),
    but the counter needs to be zero for a specific period of time before the
    resource is considered idle. This additional waiting period takes consecutive
    network requests into account, where an app in your thread might make a new
    request immediately after receiving a response to a previous request.

[`IdlingThreadPoolExecutor`](https://developer.android.com/reference/androidx/test/espresso/idling/concurrent/IdlingThreadPoolExecutor)
:   A custom implementation of [ThreadPoolExecutor](https://developer.android.com/reference/java/util/concurrent/ThreadPoolExecutor)
    that keeps track of the total number of running tasks within the created thread
    pools. This class uses a
    [`CountingIdlingResource`](https://developer.android.com/reference/androidx/test/espresso/idling/CountingIdlingResource) to
    maintain the counter of active tasks.

[`IdlingScheduledThreadPoolExecutor`](https://developer.android.com/reference/androidx/test/espresso/idling/concurrent/IdlingScheduledThreadPoolExecutor)
:   A custom implementation of
    [ScheduledThreadPoolExecutor](https://developer.android.com/reference/java/util/concurrent/ScheduledThreadPoolExecutor). It provides the same
    functionality and capabilities as the
    [`IdlingThreadPoolExecutor`](https://developer.android.com/reference/androidx/test/espresso/idling/concurrent/IdlingThreadPoolExecutor)
    class, but it can also keep track of tasks that are scheduled for the future or
    are scheduled to execute periodically.
| **Note:** The synchronization benefits associated with these implementations of idling resources only take effect following Espresso's first invocation of that resource's [`isIdleNow()`](https://developer.android.com/reference/androidx/test/espresso/IdlingResource#isIdleNow()) method. Therefore, you must register these idling resources **before** you need them.

## Create your own idling resource

As you use idling resources in your app's tests, you might need to provide
custom resource management or logging. In those cases, the implementations
listed in the previous section might not suffice. If that's the case, you can
extend one of these idling resource implementations or create your own.

If you implement your own idling resource functionality, keep the following best
practices in mind, particularly the first one:

**Invoke transitions to the idle state outside idle checks.**
:   After your app becomes idle, call
    [`onTransitionToIdle()`](https://developer.android.com/reference/androidx/test/espresso/IdlingResource.ResourceCallback#onTransitionToIdle())
    outside any implementations of
    [`isIdleNow()`](https://developer.android.com/reference/androidx/test/espresso/IdlingResource#isIdleNow()). That way,
    Espresso doesn't make a second, unnecessary check to determine whether a given
    idling resource is idle.

The following code snippet illustrates this recommendation:  

### Kotlin

```kotlin
fun isIdle() {
    // DON'T call callback.onTransitionToIdle() here!
}

fun backgroundWorkDone() {
    // Background work finished.
    callback.onTransitionToIdle() // Good. Tells Espresso that the app is idle.

    // Don't do any post-processing work beyond this point. Espresso now
    // considers your app to be idle and moves on to the next test action.
}
```

### Java

```java
public void isIdle() {
    // DON'T call callback.onTransitionToIdle() here!
}

public void backgroundWorkDone() {
    // Background work finished.
    callback.onTransitionToIdle() // Good. Tells Espresso that the app is idle.

    // Don't do any post-processing work beyond this point. Espresso now
    // considers your app to be idle and moves on to the next test action.
}
```

**Register idling resources before you need them.**

:   The synchronization benefits associated with idling resources only take effect
    following Espresso's first invocation of that resource's
    [`isIdleNow()`](https://developer.android.com/reference/androidx/test/espresso/IdlingResource#isIdleNow()) method.

    The following list shows several examples of this property:

    - If you register an idling resource in a method annotated with `@Before`, the idling resource takes effect in the first line of each test.
    - If you register an idling resource inside a test, the idling resource takes effect during the next Espresso-based action. This behavior still occurs even if the next action is in the same test as the statement that registers the idling resource.

**Unregister idling resources after you're done using them.**

:   To conserve system resources, you should unregister idling resources as soon
    as you don't need them anymore. For example, if you register an idling resource
    in a method annotated with `@Before`, it's best to unregister this resource in a
    corresponding method that's annotated with `@After`.

**Use an [idling registry](https://developer.android.com/training/testing/espresso/idling-resource#encapsulate-idling-resources) to register and unregister idling resources.**

:   By using this container for your app's idling resources, you can register and
    unregister idling resources repeatedly as needed and still observe consistent
    behavior.

**Maintain only simple app state within idling resources.**

:   For example, the idling resources that you implement and register shouldn't
    contain references to [View](https://developer.android.com/reference/android/view/View) objects.

## Register idling resources

Espresso provides a container class into which you can place your app's idling
resources. This class, called
[`IdlingRegistry`](https://developer.android.com/reference/androidx/test/espresso/IdlingRegistry), is a
self-contained artifact that introduces minimal overhead to your app. The class
also allows you to take the following steps toward improving your app's
maintainability:

- Create a reference to the `IdlingRegistry`, instead of the idling resources that it contains, in your app's tests.
- Maintain differences in the collection of idling resources that you use for each build variant.
- Define idling resources in your app's services, rather than in the UI components that reference those services.

| **Note:** The [`IdlingRegistry`](https://developer.android.com/reference/androidx/test/espresso/IdlingRegistry) class is the only supported method of registering your app's idling resources.

## Integrate idling resources into your app

Although you can add idling resources to an app in several different ways, one
approach in particular maintains encapsulation for your app while still allowing
you to specify a particular operation that a given idling resource represents.

### Recommended approach

When adding idling resources into your app, we **highly** recommend placing the
idling resource logic in the app itself and performing only the registration and
unregistration operations in your tests.

Although you create the unusual situation of using a test-only interface in
production code by following this approach, you can wrap idling resources around
code that you already have, maintaining your app's APK size and method count.

### Alternative approaches

If you'd prefer to not have idling resources logic in your app's production
code, there are several other viable integration strategies:

- Create build variants, such as Gradle's [product
  flavors](https://developer.android.com/studio/build/build-variants#product-flavors), and use idling resources only in your app's debug build.
- Use a dependency injection framework like [Dagger](https://dagger.dev) to inject your app's idling resource dependency graph into your tests. If you're using Dagger 2, the injection itself should originate from a subcomponent.
- Implement an idling resource in your app's tests, and expose the part
  of your app's implementation that needs to be synchronized in those
  tests.

  **Caution:**Although this design decision seems to
  create a self-contained reference to idling resources, it also breaks
  encapsulation in all but the simplest of apps.

## Additional resources

For more information about using Espresso in Android tests, consult the
following resources.

### Samples

- [IdlingResourceSample](https://github.com/android/testing-samples/tree/main/ui/espresso/IdlingResourceSample): Synchronization with background jobs.