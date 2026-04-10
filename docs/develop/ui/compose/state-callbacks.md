---
title: https://developer.android.com/develop/ui/compose/state-callbacks
url: https://developer.android.com/develop/ui/compose/state-callbacks
source: md.txt
---

In Jetpack Compose, an object can implement [`RememberObserver`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/RememberObserver) to receive
callbacks when it's used with `remember` to know when it starts and stops being
remembered in the composition hierarchy. Similarly, you can use
[`RetainObserver`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/RetainObserver) to receive information about the state of an object used
with `retain`.

For objects that use this lifecycle information from the composition hierarchy,
we recommend a few best practices to verify that your objects act as good
citizens in the platform and defend against misuse. Specifically, use the
`onRemembered` (or `onRetained`) callbacks to launch work instead of the
constructor, cancel all work when objects stop being remembered or retained, and
avoid leaking implementations of `RememberObserver` and `RetainObserver` to
avoid accidental calls. The next section explains these recommendations in more
depth.

## Initialization and cleanup with `RememberObserver` and `RetainObserver`

The [Thinking in Compose guide](https://developer.android.com/develop/ui/compose/mental-model) describes the mental model behind
composition. When working with `RememberObserver` and `RetainObserver`, it's
important to keep in mind two behaviors of composition:

- Recomposition is optimistic and may be canceled
- All composable functions should have no side-effects

### Run initialization side effects during `onRemembered` or `onRetained`, not construction

When objects are remembered or retained, the calculation lambda runs as part of
composition. For the same reasons that you wouldn't perform a side-effect or
launch a coroutine during composition, you should also not perform side-effects
in the calculation lambda passed to `remember`, `retain`, and their variations.
This includes as part of the constructor for the remembered or retained objects.

Instead, when implementing `RememberObserver`, or `RetainObserver`, verify that
all effects and launched jobs are dispatched in the `onRemembered` callback.
This offers the same timing as the `SideEffect` APIs. It also guarantees that
these effects only execute when the composition is applied, which prevents
orphaned jobs and memory leaks if a recomposition is abandoned or deferred.


```kotlin
class MyComposeObject : RememberObserver {
    private val job = Job()
    private val coroutineScope = CoroutineScope(Dispatchers.Main + job)

    init {
        // Not recommended: This will cause work to begin during composition instead of
        // with other effects. Move this into onRemembered().
        coroutineScope.launch { loadData() }
    }

    override fun onRemembered() {
        // Recommended: Move any cancellable or effect-driven work into the onRemembered
        // callback. If implementing RetainObserver, this should go in onRetained.
        coroutineScope.launch { loadData() }
    }

    private suspend fun loadData() { /* ... */ }

    // ...
}
```

<br />

### Teardown when forgotten, retired, or abandoned

To avoid leaking resources or leaving background jobs orphaned, remembered
objects must also be disposed of. For objects that implement `RememberObserver`,
this means that anything initialized in `onRemembered` must have a matching
release call in `onForgotten`.

Because composition can be canceled, objects that implement `RememberObserver`
must also tidy up after themselves if they are abandoned in compositions. An
object is abandoned when it is returned by `remember` in a composition that gets
canceled or fails. (This happens most commonly when using `PausableComposition`,
and can also occur when using hot reload with Android Studio's composable
preview tooling.)

When a remembered object is abandoned, it receives only the call to
`onAbandoned` (and no call to `onRemembered`). To implement the abandon method,
dispose of anything created between when the object is initialized and when the
object would have received the `onRemembered` callback.


```kotlin
class MyComposeObject : RememberObserver {
    private val job = Job()
    private val coroutineScope = CoroutineScope(Dispatchers.Main + job)

    // ...

    override fun onForgotten() {
        // Cancel work launched from onRemembered. If implementing RetainObserver, onRetired
        // should cancel work launched from onRetained.
        job.cancel()
    }

    override fun onAbandoned() {
        // If any work was launched by the constructor as part of remembering the object,
        // you must cancel that work in this callback. For work done as part of the construction
        // during retain, this code should will appear in onUnused.
        job.cancel()
    }
}
```

<br />

## Keep `RememberObserver` and `RetainObserver` implementations private

When writing public APIs, use caution when extending `RememberObserver` and
`RetainObserver` in creating classes that are returned publicly. A user may not
remember your object when you expect them to, or may remember your object in a
different way than you intended. Because of this, we recommend not exposing
constructors or factory functions for objects that implement `RememberObserver`
or `RetainObserver`. Note that this is dependent on the runtime type of a class,
not the declared type --- remembering an object that implements `RememberObserver`
or `RetainObserver` but is casted to `Any` still causes the object to receive
callbacks.

Not recommended:

    abstract class MyManager

    // Not Recommended: Exposing a public constructor (even implicitly) for an object implementing
    // RememberObserver can cause unexpected invocations if it is remembered multiple times.
    class MyComposeManager : MyManager(), RememberObserver { ... }

    // Not Recommended: The return type may be an implementation of RememberObserver and should be
    // remembered explicitly.
    fun createFoo(): MyManager = MyComposeManager()

Recommended:


```kotlin
abstract class MyManager

class MyComposeManager : MyManager() {
    // Callers that construct this object must manually call initialize and teardown
    fun initialize() { /*...*/ }
    fun teardown() { /*...*/ }
}

@Composable
fun rememberMyManager(): MyManager {
    // Protect the RememberObserver implementation by never exposing it outside the library
    return remember {
        object : RememberObserver {
            val manager = MyComposeManager()
            override fun onRemembered() = manager.initialize()
            override fun onForgotten() = manager.teardown()
            override fun onAbandoned() { /* Nothing to do if manager hasn't initialized */ }
        }
    }.manager
}
```

<br />

## Considerations when remembering objects

In addition to the previous recommendations surrounding `RememberObserver` and
`RetainObserver`, we also recommend being mindful of and avoiding accidentally
re-remembering objects both for performance and correctness. The following
sections go into more depth on specific re-remembering scenarios and why they
should be avoided.

### Only remember objects once

Re-remembering an object can be dangerous. In the best case scenario, you may be
wasting resources remembering a value that's already remembered. But if an
object implements `RememberObserver` and is remembered twice unexpectedly, it
will receive more callbacks than it expects. This can cause issues, as the
`onRemembered` and `onForgotten` logic will execute twice, and most
implementations of `RememberObserver` don't support this case. If a second
remember call happens in a different scope that has a different lifespan from
the original `remember`, many implementations of `RememberObserver.onForgotten`
dispose the object before it is finished being used.

    val first: RememberObserver = rememberFoo()

    // Not Recommended: Re-remembered `Foo` now gets double callbacks
    val second = remember { first }

This advice does not apply to objects that are remembered again transitively (as
in, remembered objects that consume another remembered object). It is common to
write code that looks as follows, which is allowable because a different object
is being remembered and therefore does not cause unexpected callback doubling.


```kotlin
val foo: Foo = rememberFoo()

// Acceptable:
val bar: Bar = remember { Bar(foo) }

// Recommended key usage:
val barWithKey: Bar = remember(foo) { Bar(foo) }
```

<br />

### Assume function arguments are already remembered

A function shouldn't remember any of its parameters both because it can lead to
double callback invocations for `RememberObserver` and because it is
unnecessary. If an input parameter must be remembered, either verify that it
does not implement `RememberObserver`, or require callers to remember their
argument.

    @Composable
    fun MyComposable(
        parameter: Foo
    ) {
        // Not Recommended: Input should be remembered by the caller.
        val rememberedParameter = remember { parameter }
    }

This does not apply to objects remembered transitively. When remembering an
object derived from a function's arguments, consider specifying it as one of the
keys to `remember`:


```kotlin
@Composable
fun MyComposable(
    parameter: Foo
) {
    // Acceptable:
    val derivedValue = remember { Bar(parameter) }

    // Also Acceptable:
    val derivedValueWithKey = remember(parameter) { Bar(parameter) }
}
```

<br />

### Don't retain an object that's already remembered

Similar to re-remembering an object, you should avoid retaining an object that's
remembered to try and extend its lifespan. This is a fallout of the advice in
[State lifespans](https://developer.android.com/develop/ui/compose/state-lifespans): `retain` shouldn't be used with objects that have a
lifespan that doesn't match the lifespan retain offers. Since `remembered`
objects have a shorter lifespan than `retained` objects, you shouldn't retain a
remembered object. Instead, prefer retaining the object at the origin site
instead of remembering it.