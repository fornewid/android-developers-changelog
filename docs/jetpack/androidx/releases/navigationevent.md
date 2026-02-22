---
title: https://developer.android.com/jetpack/androidx/releases/navigationevent
url: https://developer.android.com/jetpack/androidx/releases/navigationevent
source: md.txt
---

# navigationevent

API Reference  
[androidx.navigationevent](https://developer.android.com/reference/kotlin/androidx/navigationevent/package-summary)  
The Navigation Event library provides a KMP-first API for handling system back as well as [Predictive Back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture).  

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | [1.0.2](https://developer.android.com/jetpack/androidx/releases/navigationevent#1.0.2) | - | - | - |

## Declaring dependencies

To add a dependency on navigationevent, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.navigationevent:navigationevent:1.0.2"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.navigationevent:navigationevent:1.0.2")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1777955+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1777955&template=2137283)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.2

January 28, 2026

`androidx.navigationevent:navigationevent-*:1.0.2` is released. Version 1.0.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2604e5169fbd9436ac2d09b32572afd4a5bb32ae..a7bd43e4ff5a6c4f70a22b93597ac88425fe5e84/navigationevent).

**Bug Fixes**

- Fix crash when using `NavigationEventHandler` in Android Studio Previews. The handler now detects inspection mode and does nothing, allowing the Preview to render without a provided dispatcher. ([I370f2](https://android-review.googlesource.com/#/q/I370f2b4ece299d9053239739b54b63833ae55c25), [b/454313986](https://issuetracker.google.com/issues/454313986)).

### Version 1.0.1

December 03, 2025

`androidx.navigationevent:navigationevent-*:1.0.1` is released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a336be7aa59aced2a87c402849988939d848fee3..2604e5169fbd9436ac2d09b32572afd4a5bb32ae/navigationevent).

**Bug Fixes**

- Fixes a `ConcurrentModificationException` when disposing a child `NavigationEventDispatcher` such as those created with `rememberNavigationEventDispatcherOwner()`. ([ec68a9](https://android.googlesource.com/platform/frameworks/support/+/ec68a96144221f4d3d2629e08703aa4d5c7cb946), [b/454363524](https://issuetracker.google.com/454363524))

### Version 1.0.0

November 19, 2025

`androidx.navigationevent:navigationevent-*:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..a336be7aa59aced2a87c402849988939d848fee3/navigationevent).

**Major features of 1.0.0:**

The `Navigation Event` library is now stable! `Navigation Event` is the AndroidX library for handling system level interactions such as system-back and predictive back in Android (and other platforms).

- To handle `NavigationEvent`s, you can implement your own `NavigationEventHandler` that overrides the desired functions. You then need to add the handler to a `NavigationEventDispatcher`. Starting with the [Activity `1.12.0`](https://developer.android.com/jetpack/androidxactivity#1.12.0) release, `ComponentActivity` implements the new `NavigationEventDispatcherOwner` interface, which provides a dispatcher that is ready to use :

      // The NavigationEventInfo provides information about a navigation state
      object CurrentInfo : NavigationEventInfo()

      // you can retrieve this from any component that is a NavigationEventDispatcherOwner
      // or you can instantiate your own custom dispatcher
      val dispatcher = myActivity.navigationEventDispatcher

      val myHandler = object : NavigationEventHandler<NavigationEventInfo>(
                  initialInfo = CurrentInfo,
                  isBackEnabled = true
              ) {
                  override fun onBackStarted(event: NavigationEvent) {
                      // Prepare for the back event
                  }

                  override fun onBackProgressed(event: NavigationEvent) {
                      // Use event.progress for predictive animations
                  }

                  // This is the required method for final event handling
                  override fun onBackCompleted() {
                      // Complete the back event
                  }

                  override fun onBackCancelled() {
                      // Cancel the back event
                  }
              }

      dispatcher.addHandler(myHandler)

- The `navigationevent:navigationevent-compose` module provides a convenient compose function `NavigationBackHandler` that automatically hooks up the handler to the closest `LocalNavigationEventDispatcherOwner`'s `NavigationEventDispatcher` and allows developers to provide the desired behavior as parameters:

      object CurrentInfo : NavigationEventInfo()
      object PreviousInfo : NavigationEventInfo()

      val navEventState = rememberNavigationEventState(
        currentInfo = CurrentInfo,
        backInfo = PreviousInfo
      )

      // Inside composition
      NavigationBackHandler(
          State = navEventState,
          isBackEnabled = true,
          // optional
          onBackCancelled = { // Cancel the back event },
          // required
          onBackCompleted = { // Complete the back event } ,
      )

Using this pattern in Compose makes it very easy to hoist the `NavigationEventState` and allow it to be observed by different Composable (i.e. in the case of Navigation3, where you can hoist the state out of the `NavDisplay`).

- Each `NavigationEventDispatcher` has the ability to provide a parent dispatcher, for both the compose and non-compose cases. This allows developers to create a hierarchical structure where several dispatchers can be managed by a single parent. Having a parent makes handling groups of dispatchers that might need to be disabled or disposed, relatively simple:

      // Non-Compose
      val parentDispatcher = NavigationEventDispatcher()
      val childDispatcher = NavigationEventDispatcher(parent = parentDispatcher)

      // Compose
      val composeChildDispatcher = rememberNavigationEventDispatcher(
          // This defaults to `LocalNavigationEventDispatcherOwner.current`
          // Must explicitly provide null to have an unparented dispatcher created here
          parent = NavigationEventDispatch() 
      )

- The library also makes it possible to provide signals directly to the `NavigationEventDispatcher` via a `NavigationEventInput`. `NavigationEventInput`s acts as the "input" side of the navigation system, translating platform-specific events (like system back gestures or button clicks) into standardized events that can be sent to a `NavigationEventDispatcher`. The `navigationevent:navigationevent` module currently provides 2 `NavigationEventInput`s: a more generic `DirectNavigationEventInput` to allow any event to be dispatched and an Android specific `OnBackInvokedInput` that allows a `NavigationEventDispatcher` to support system back and the predictive back gesture. If you implement your own dispatcher (instead of using the one provided by `ComponentActivity`) you must manually add your input:

      val dispatcher = NavigationEventDispatcher()

      dispatcher.addInput(DirectNavigationEventInput())
      dispatcher.addInput(OnBackInvokedDefaultInput(invoker))

### Version 1.0.0-rc01

November 05, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56e97d713c63942b89d95099730e3650408e0321..7cc48474876c19197c67eda0f2d537f62760130e/navigationevent).

### Version 1.0.0-beta01

October 08, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd..56e97d713c63942b89d95099730e3650408e0321/navigationevent).

**API Changes**

- Correct the `FloatRange` annotation for `NavigationEvent.touchX` and `NavigationEvent.touchY`. These values represent absolute pixel coordinates and do not have a `1.0` upper bound. ([I4b205](https://android-review.googlesource.com/#/q/I4b2055b824447deda3abeca459c0ef9a2572ce5d), [b/445989313](https://issuetracker.google.com/issues/445989313))
- Refactor the `NavigationEventDispatcherOwner` composable to `rememberNavigationEventDispatcherOwner`. The function now returns the `NavigationEventDispatcherOwner` directly. To provide this owner to a sub-composition, use `CompositionLocalProvider`. ([I874b2](https://android-review.googlesource.com/#/q/I874b285c7b4592fca533f86f9d57aa676b25b9b2), [b/444446629](https://issuetracker.google.com/issues/444446629))

### Version 1.0.0-alpha09

September 24, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd/navigationevent).

**API Changes**

- Use the `NavigationEventTransitionState.Idle` singleton object directly instead of instantiating `Idle()`. ([Ic7d9e](https://android-review.googlesource.com/#/q/Ic7d9ec5eb9a1c426cd78342a9244df324f3147bd), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Make convenience constructors internal; obtain instances via public `NavigationEventDispatcher.history` instead of direct construction. ([I3b7e0](https://android-review.googlesource.com/#/q/I3b7e077aa3da0494ba56b3b02a257b92e13d65c5), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Require creating `NavigationEventState` via `rememberNavigationEventState`; constructor is now internal. ([Ie143c](https://android-review.googlesource.com/#/q/Ie143c5d25a50ff66f3f22571e4d82bd8dae602c2), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Adopt `onBackCompletedFallback` replace `fallbackOnBackPressed` usages and constructor parameter. Behavior is unchanged; invoked only on completed, unhandled back events. ([Idabe9](https://android-review.googlesource.com/#/q/Idabe94c36cb1cb78fa1770fb90dd02a914456d63), [b/444734264](https://issuetracker.google.com/issues/444734264))
- The primary constructor of `NavigationEventHistory(mergedHistory, currentIndex)` is now `internal`. External consumers must use the public constructors (either the empty constructor or the partition-based constructor) to create instances. ([I1c047](https://android-review.googlesource.com/#/q/I1c0478b0039f8a89b79c4c2b7d655abd4d201722), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Make `View.setViewTreeNavigationEventDispatcherOwner` accept nullable owner ([Ic9eb6](https://android-review.googlesource.com/#/q/Ic9eb6e2b8687caea3d6b852881289c3f0a209cd4), [b/444436762](https://issuetracker.google.com/issues/444436762))
- `NavigationEventInfo` is now an `abstract class` instead of an `interface`. Update all custom implementations to inherit from the class (e.g, `data class MyInfo : NavigationEventInfo()`). ([I1e59c](https://android-review.googlesource.com/#/q/I1e59c844ec7c68a2824d0215af228e47fa6bc4e1), [b/444734264](https://issuetracker.google.com/issues/444734264))
- The legacy `NavigationEventDispatcher.state` property and `getState<T>()` function have been removed. Use the new, separate `dispatcher.transitionState` (for gesture progress) and `dispatcher.history` (for the navigation stack) flows. ([Ic2ceb](https://android-review.googlesource.com/#/q/Ic2cebbcf1eabc3253e4511763896b6cf8d5d45e6), [b/444734264](https://issuetracker.google.com/issues/444734264))
- The `NavigationEventInput.onInfoChanged(...)` callback is replaced. Implement the new `onHistoryChanged(history: NavigationEventHistory)` callback to receive updates as a single `NavigationEventHistory` object. ([I23e0b](https://android-review.googlesource.com/#/q/I23e0b6df2350c0b834af9a478d42dfef7aedeece), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Introduce a new global `NavigationEventDispatcher.history` `StateFlow`. This non-generic flow allows observers to subscribe only to changes to the navigation stack and remains stable during gesture progress. This is the counterpart to `transitionState`. ([I1db10](https://android-review.googlesource.com/#/q/I1db107a184a1b58a55b4dead0b66509761ab100d), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Introduce a new global `NavigationEventDispatcher.transitionState` `StateFlow`. This non-generic flow allows observers to subscribe only to the physical gesture state (Idle/InProgress), separate from history. ([I171fa](https://android-review.googlesource.com/#/q/I171fa229d494eba01aa36f33435c68bc58f10b23), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Introduce the `NavigationEventHistoryState` class. This will serve as the core API for observing navigation information history, separate from gesture state. ([I81ca5](https://android-review.googlesource.com/#/q/I81ca52511003f31e9240b021b011ebaa7dac568f), [b/444734264](https://issuetracker.google.com/issues/444734264))
- `NavigationEvent` is now marked as `@Immutable`, allowing the Compose Compiler to optimize recompositions. ([If78c7](https://android-review.googlesource.com/#/q/If78c70d5fdc0ab87142546f6bbe3c77d9833d7ae), [b/444734264](https://issuetracker.google.com/issues/444734264))
- The `navigationevent-compose` handler APIs are updated. `NavigationEventHandler` and `NavigationBackHandler` (and variants) now support a new overload that accepts a hoisted `NavigationEventState`s. The simple overloads (taking `currentInfo`) are preserved and now use this new state model internally. ([Ic3251](https://android-review.googlesource.com/#/q/Ic32511e845d8b2ca72f9d97aa01d1a3c319f5705), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Add the new `@Stable` `NavigationEventState<T>` state holder to the `navigationevent-compose` library. This object combines local history with local gesture state and will be the primary link between `rememberNavigationEventState` and `NavigationEventHandler`. ([Ifb69f](https://android-review.googlesource.com/#/q/Ifb69f6b7d4cebd1a0020cbacce7dece9c5c38acb), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Add a new public, read-only `transitionState: TransitionState` property to `NavigationEventHandler`. Handlers now maintain their own transition state, which external systems can observe. ([I9acd2](https://android-review.googlesource.com/#/q/I9acd2b09de191f33cb200169fc1b4d3bb74dd17a), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Introduce the new `TransitionState` sealed class. This will serve as the core API for observing gesture state, separate from navigation history. ([Id4beb](https://android-review.googlesource.com/#/q/Id4beb114ebc4ca33b8810de2d1cf9d57f7ec2336), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Expose `currentInfo`, `backInfo`, and `forwardInfo` as public, read-only properties on `NavigationEventHandler`. ([Ia7636](https://android-review.googlesource.com/#/q/Ia76361b27c742a3c84266603067a3e28578f2ec6), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Implementations of `NavigationEventHandler` must now provide an `initialInfo: T` value to the base constructor. ([Idcfea](https://android-review.googlesource.com/#/q/Idcfea61cc16825aa6e78fe19557d604ea874a2d6), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Replace `OnBackInvokedInput` with `OnBackInvokedOverlayInput` or `OnBackInvokedDefaultInput`. ([I5323f](https://android-review.googlesource.com/#/q/I5323ff1b5410c8c42bfa841447ac32bf10ad2a21), [b/428948766](https://issuetracker.google.com/issues/428948766))
- Mark `NavigationEventState` as `@Immutable`. This improves Compose performance by ensuring Composables observing this state can correctly skip recomposition. ([I399c8](https://android-review.googlesource.com/#/q/I399c8aded046b6fcf0bee919210b169f9fd4f7cb))
- Rename `NavigationEventInfo.NotProvided` to `NavigationEventInfo.None;` update references. No behavior change. ([I5e2d4](https://android-review.googlesource.com/#/q/I5e2d4dfb80dc76d86aae55e5fa9fef60e6c9b732))
- `NavigationEventInfo` is now marked as `@Immutable`, allowing the Compose Compiler to optimize recompositions. ([I7c112](https://android-review.googlesource.com/#/q/I7c112c4867cb7dcc926c2e6ff32c4cdad5f16df2))
- Improve Java ergonomics with fun interface for back completion fallback. ([I8a860](https://android-review.googlesource.com/#/q/I8a860e0aa944a9cafd1f22380ba25fe28c0b2c80))
- Rename `onHasEnabledHandlerChanged` to `onHasEnabledHandlersChanged`. This clarifies that the callback reports on the collective enablement state of all handlers, not just one. ([I1af61](https://android-review.googlesource.com/#/q/I1af6102d35775732a52674267d8e29adf5ccd96a), [b/443711297](https://issuetracker.google.com/issues/443711297))
- Remove `hasEnabledHandler()` from `NavigationEventDispatcher;` use `NavigationEventInput.onHasEnabledHandlersChanged` instead. ([Idef72](https://android-review.googlesource.com/#/q/Idef72ed7d18c4d8fe885b264b4a935c6d9ddaba8), [b/443711297](https://issuetracker.google.com/issues/443711297))
- Add `onInfoChanged` callback to `NavigationEventInput` to notify listeners of changes to the navigation history. This provides the full context of the current, back, and forward stacks, enabling Inputs to react to the contextual information. ([I69a8b](https://android-review.googlesource.com/#/q/I69a8bf349e514983b821ab9905d66ac5d9889ac9), [b/443282983](https://issuetracker.google.com/issues/443282983))
- Make `NavigationEvent`'s `swipeEdge` an `@IntDef` ([Icee54](https://android-review.googlesource.com/#/q/Icee542915f6b4c5a37bd663caaec983417498349), [b/443950342](https://issuetracker.google.com/issues/443950342))
- Add a `priority` parameter to `NavigationEventDispatcher.addInput` to scope a dispatcher to one priority; events such as `onHasEnabledCallbacksChanged` now fire only when callbacks at that priority change. ([I3e488](https://android-review.googlesource.com/#/q/I3e488ca02d5707635bafb0680875e2b34f4911ee), [b/443711297](https://issuetracker.google.com/issues/443711297))
- Rename `NavigationEventDispatcher` param from `parentDispatcher` to parent for clarity. ([Id4f1f](https://android-review.googlesource.com/#/q/Id4f1f6f0cd10e3942281d1d0995b96defd1d16bd), [b/443801782](https://issuetracker.google.com/issues/443801782))
- Remove `NavigationEventPriority` in favor of `@IntDef` for Java users ([I10a9f](https://android-review.googlesource.com/#/q/I10a9f6b83a76331a9298fdb57bb1fb6299311ff3), [b/440514265](https://issuetracker.google.com/issues/440514265))
- Enforce navigation handler contract. If your `NavigationEventHandler` sets `isBackEnabled` or `isForwardEnabled` to `true`, you must now override `onBackCompleted` or `onForwardCompleted` respectively. The default implementations now throw an exception to prevent silent failures. ([I17c62](https://android-review.googlesource.com/#/q/I17c62db53c2bf15ac24960be90283e93b7d892c8))
- Enforce valid priority values when adding navigation event handlers. Calling `addHandler` with an unsupported priority will now throw an `IllegalArgumentException`, providing immediate feedback for incorrect usage across all target platforms. ([I3c474](https://android-review.googlesource.com/#/q/I3c4744d651322d23e08e2fb22f33fd04c3a67ee5))

**Bug Fixes**

- Make `addHandler` idempotent; ignore duplicate registrations. ([I052aa](https://android-review.googlesource.com/#/q/I052aafc576e5d75bcbead2987cb75c8c31c98f18), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Keep `NavigationEventState` properties in sync during recomposition. ([Ib3b4d](https://android-review.googlesource.com/#/q/Ib3b4d9a838687fc488f33162c7c8569466bc2cd0), [b/444734264](https://issuetracker.google.com/issues/444734264))
- Ensure `NavigationEventInputs` receive the current contextual info (current, back, forward) immediately upon registration. ([Ie65bf](https://android-review.googlesource.com/#/q/Ie65bf030ad245e76639b46616e37306206cb2f38), [b/443282983](https://issuetracker.google.com/issues/443282983))

### Version 1.0.0-alpha08

September 10, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha08` is released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/navigationevent).

**New Features**

- Introduce a lambda-based `NavigationEventHandler` API that replaces the Flow-based handler. Handle back and forward gestures with simple callbacks instead of collecting flows, reducing boilerplate and avoiding cancellation issues. Provide `NavigationBackHandler` and `NavigationForwardHandler` as targeted convenience APIs. Remove the Flow-based `NavigationEventHandler`; migrate to the new callbacks. ([I23bac](https://android-review.googlesource.com/#/q/I23bac6d64348c368fc9f9019a98f2c6ca25f91be), [b/436248277](https://issuetracker.google.com/issues/436248277))
- Allow passive listeners to access the full navigation back stack through combined back info. Enable UIs to render previews and nested navigation history instead of being limited to the top-most callback. ([I7a510](https://android-review.googlesource.com/#/q/I7a510c5d6a859b41783e4a39252a06da2ed2e01b), [b/436248277](https://issuetracker.google.com/issues/436248277))
- Introduce an explicit back/current/forward model to clarify navigation state and support forward navigation with nested handlers. ([Ib86da](https://android-review.googlesource.com/#/q/Ib86dadd128eafd5776aa23b409eacdce373ecf4a), [b/420443609](https://issuetracker.google.com/issues/420443609))
- Add `onForward*` methods and `isForwardEnabled` to `NavigationEventCallback`. ([Ic100f](https://android-review.googlesource.com/#/q/Ic100f8dcb5f409e36e8a765a5738e033bf11133b), [b/436248290](https://issuetracker.google.com/issues/436248290))
- Add forward navigation support to `NavigationEventInput`. ([I5734b](https://android-review.googlesource.com/#/q/I5734b10639303368931db205739eef542fba37f3))

**API Changes**

- Enable testing of forward navigation events with `TestNavigationEventCallback`. Use `isForwardEnabled` and `onForward*` hooks. ([I21fb5](https://android-review.googlesource.com/#/q/I21fb5ef4d42f2e2efa4bf42506402cd4c6dd4bd8), [b/420443609](https://issuetracker.google.com/issues/420443609))
- Rename `onEvent*` callbacks to `onBack*` in `NavEvent`. ([I228b3](https://android-review.googlesource.com/#/q/I228b3b938b7ac21a58a679ab05d7748bfc71284f), [b/436248290](https://issuetracker.google.com/issues/436248290))
- Convert `SwipeEdge` to an inline class. ([Id5e01](https://android-review.googlesource.com/#/q/Id5e016cb25d1637b307073237822924d58d4f9dc))
- Make the `navigationevent` library interoperable with Java. All public APIs are now fully accessible from Java code, enabling seamless integration into mixed-language or Java-only projects. ([Ibc944](https://android-review.googlesource.com/#/q/Ibc94437d208193d6cb83c70619bf520b09f746ec),[I5465f](https://android-review.googlesource.com/#/q/I5465fba44ca981cbf7d951ff6bdba78d36dd52f6), [I9fb1e](https://android-review.googlesource.com/#/q/I9fb1e8a610dbe79ee012ced6a88354f3590b608d), [b/440532890](https://issuetracker.google.com/issues/440532890)[b/443040294](https://issuetracker.google.com/issues/443040294))
- Clarify API roles by renaming `NavigationEventCallback` to `NavigationEventHandler`. This change better reflects the class's purpose of handling multi-stage navigation gestures. The corresponding `addCallback` method is now `addHandler`. ([I2492a](https://android-review.googlesource.com/#/q/I2492a768cfdc3bfc8dcac1691fbf6ebfe0f44b37), [b/443040331](https://issuetracker.google.com/issues/443040331))

**Bug Fixes**

- Prevent back fallback from running on forward navigation. ([I74814](https://android-review.googlesource.com/#/q/I74814834de47d152973ceb7ec69a53f46d99713a), [b/436248290](https://issuetracker.google.com/issues/436248290))
- Add support for predictive forward navigation. `NavigationEvent` APIs now handle both back and forward gestures, enabling consistent animations for both navigation directions. ([Idc98c](https://android-review.googlesource.com/#/q/Idc98c5057f97e17dba5b22f37f3ff585e9627170), [b/436248290](https://issuetracker.google.com/issues/436248290))
- Prevent an `IllegalStateException` crash during recomposition when a child `NavigationEventDispatcherOwner` is removed. ([Iff50c](https://android-review.googlesource.com/#/q/Iff50cb18253caeb809c1c25dc1cdea11f701a081), [b/412629020](https://issuetracker.google.com/issues/412629020))
- Passive listeners can now access the full navigation back stack through combined back info, enabling UIs to render previews and nested navigation history instead of being limited to the top-most callback. ([I7a510](https://android-review.googlesource.com/#/q/I7a510c5d6a859b41783e4a39252a06da2ed2e01b), [b/436248277](https://issuetracker.google.com/issues/436248277))

### Version 1.0.0-alpha07

August 27, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha07` is released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/navigationevent).

**API Changes**

- Remove `NavigationEventDispatcher.onHasEnabledCallbacksChanged`. ([I50e97](https://android-review.googlesource.com/#/q/I50e97e80900417fc9f5146b848d3c307e1c694d1))
- Make `NavigationEventCallback.onEventCompleted()` abstract. ([I36b38](https://android-review.googlesource.com/#/q/I36b3822adb62fa441b70e88c990f36a4f05cfe4d))
- Change `NavigationEventCallback#on*` methods to `protected`. Update calling code to override them. ([I6b691](https://android-review.googlesource.com/#/q/I6b691b4da8c359af29f1467ba1a894e25f04ecee))
- Rename `DirectNavigationEventInput` functions. ([Iffb62](https://android-review.googlesource.com/#/q/Iffb628a961cd1ce071c2e54d9a5e7e7c922c2cdf))
- Rename `NavigationEventInput.onAttach` to `onAdded`. ([I2d0b8](https://android-review.googlesource.com/#/q/I2d0b8f57e75a444c937c9de36e698c5f3a9c1427))
- Rename `NavigationEventInput.onDetach` to `onRemoved`. ([I2d0b8](https://android-review.googlesource.com/#/q/I2d0b8f57e75a444c937c9de36e698c5f3a9c1427))
- Rename `NavigationEventInputHandler` to `NavigationEventInput`. ([I676a4](https://android-review.googlesource.com/#/q/I676a416c9aab3e04937ffd51d8bfe21eddc5eec5))
- Add `@EmptySuper` to `NavigationEventInput.onHasEnabledCallbacksChanged`. ([If9853](https://android-review.googlesource.com/#/q/If9853409eeb41f613bf26013f19687b45f9b9972))
- Implement `onAttach` in `NavigationEventInputHandler`. ([I03648](https://android-review.googlesource.com/#/q/I036484db882de61e358c5d2d8b1945531766a02e))
- Implement `onDetach` in `NavigationEventInputHandler`. ([I03648](https://android-review.googlesource.com/#/q/I036484db882de61e358c5d2d8b1945531766a02e))
- Default `NavigationEventCallback` to enabled upon creation. ([Ic0188](https://android-review.googlesource.com/#/q/Ic0188530a10913977db57ae6471fdc75d6fa1ba8))
- Replace `NavigationEventInput.addOnHasEnabledCallbacksChangedCallback` with `NavigationEventInput.onHasEnabledCallbacksChanged`. ([I64e93](https://android-review.googlesource.com/#/q/I64e934d5393cfce042a86348c8cd0453d10cd353))
- Require the main thread for `NavigationEventDispatcher.addInput`. ([Ic2930](https://android-review.googlesource.com/#/q/Ic293003eb2a459347cdb599529ee4307a4fb005e))
- Require the main thread for `NavigationEventDispatcher.removeInput`. ([Ic2930](https://android-review.googlesource.com/#/q/Ic293003eb2a459347cdb599529ee4307a4fb005e))
- Remove `Dispatcher.addOnHasEnabledCallbacksChangedCallback`. Replace with `Dispatcher.onHasEnabledCallbacksChanged`. ([Ida3e3](https://android-review.googlesource.com/#/q/Ida3e3883f7b03395351b3e78b4cf9c2e2cb309db), [b/436530096](https://issuetracker.google.com/issues/436530096))

**Bug Fixes**

- Fix bug where adding an already-attached handler or removing an unattached one triggered incorrect lifecycle logic. ([I9e47b](https://android-review.googlesource.com/#/q/I9e47bf34fd73248d8e5514af04638055752997b5))

### Version 1.0.0-alpha06

August 13, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha06` is released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b4562c71af5649ad7262ba4c7925899e6e93bdff..c359e97fece91f3767a7d017e9def23c7caf1f53/navigationevent).

**New Features**

**Passive Listeners API**

You can now pass **custom contextual information** from any navigation host and **passively listen** to gesture state changes from anywhere in your UI. This enables context-aware animations for predictive back and other gesture-driven navigation.

This feature has two parts:

1. **Providing Info** - Use `NavigationEventInfo` to carry custom data.
2. **Consuming State** - Use `dispatcher.state` (`NavigationEventState`) to observe gesture progress and context.

- `NavigationEventCallback` now exposes `setInfo(currentInfo, previousInfo)` method to set gesture context in one call ([I1d5e7](https://android-review.googlesource.com/#/q/I1d5e7e5ce95016448869088b18fd9ac5c775b469), [b/424470518](https://issuetracker.google.com/issues/424470518)).
- `NavigationEventHandler` adds a new overload that accepts `currentInfo` and `previousInfo`, making it the primary API for supplying context in Compose apps ([I6ecd3](https://android-review.googlesource.com/#/q/I6ecd3707a3f521b9e1d828f658b27ffdd856e516), [b/424470518](https://issuetracker.google.com/issues/424470518)).

Example:  

      data class MyScreenInfo(val screenName: String) : NavigationEventInfo

      NavigationEventHandler(
          enabled = true,
          currentInfo = MyScreenInfo("Details Screen"),
          previousInfo = MyScreenInfo("Home Screen")
      ) { /* Handle back completion */ }

- `NavigationEventDispatcher` now exposes `dispatcher.state` and `dispatcher.getState<T>()` ([If7fae](https://android-review.googlesource.com/#/q/If7faebaedefbc51a0dcec6ac7e1e08c858b4014d), [Ia90ca](https://android-review.googlesource.com/#/q/Ia90ca93bf3030c059bf4d63a817e182d59d10c2f), [b/424470518](https://issuetracker.google.com/issues/424470518)). These `StateFlow`-based APIs let any UI observe gesture progress and contextual data without handling the event directly.

Example:  

      val gestureState by LocalNavigationEventDispatcherOwner.current!!
          .navigationEventDispatcher
          .state
          .collectAsState()

      val progress = gestureState.progress // Returns latestEvent.progress or 0F

      when (val state = gestureState) {
          is InProgress -> {
              val toScreen = state.currentInfo as MyScreenInfo
              val fromScreen = state.previousInfo as MyScreenInfo
              println("Navigating from ${fromScreen.screenName} to ${toScreen.screenName}")
          }
          is Idle -> { /* Idle state */ }
      }

- Add `progress` property to `NavigationEventState` ([I7b196](https://android-review.googlesource.com/#/q/I7b196d925d66d6aafbfb4cf7032fab9bc470e41b)) that returns `latestEvent.progress` when in progress, or `0F` otherwise:

      val progress = state.progress

- Add `NavigationEventDispatcherOwner` composable to create, link, and dispose of `NavigationEventDispatcher` instances hierarchically. Enable dynamic control of the dispatcher's enabled state and automatic cleanup.

      @Composable
      fun Sample() {
          NavigationEventDispatcherOwner(enabled = true) {
              val localDispatcherOwner = LocalNavigationEventDispatcherOwner.current
          }
      }

**API Changes**

- The `isPassthrough` parameter has been removed from the `NavigationEventCallback`. ([I99028](https://android-review.googlesource.com/#/q/I99028e7813d04b4cefca5fcae9d17da38514afd3), [b/424470518](https://issuetracker.google.com/issues/424470518))
- `NavigationEventState` constructors are now internal. For testing, update the state (defaults to `Idle`) via the `DirectNavigationEventInputHandler`. Call `handleOnStarted` or `handleOnProgressed` to set state to `InProgress`, and `handleOnCompleted` or `handleOnCancelled` to return it to `Idle`. To update `NavigationEventInfo`, use `NavigationEventCallback.setInfo`. ([I93dca](https://android-review.googlesource.com/#/q/I93dca447718f45cbcceb79367ec422c647660c71), [b/424470518](https://issuetracker.google.com/issues/424470518))
- Added default parameters to `NavigationEvent` to allow for easier instantiation and to simplify testing which should be used in place of `TestNavigationEvent`. ([I5dc49](https://android-review.googlesource.com/#/q/I5dc49bfda688c13287343d711eb30424925b00ff), [I232f4](https://android-review.googlesource.com/#/q/I232f4e164c4fc370dbce5fec7d990de6e0de4daa))
- Added a `TestNavigationEventCallback` for testing navigation events with specific current/previous states. ([Idd22e](https://android-review.googlesource.com/#/q/Idd22eb663641e57e0bbd22a4f6373d81d9c5bd09), [b/424470518](https://issuetracker.google.com/issues/424470518))
- `NavigationEventInputHandler` has been made into an abstract class to replace the previous `AbstractNavigationEventInputHandler` with an implementation in `DirectNavigationEventInputHandler` ([Iadde5](https://android-review.googlesource.com/#/q/Iadde55d642f71285a8887ae4145f36eb801bbb6e), [Ifed40](https://android-review.googlesource.com/#/q/Ifed405ac4658fbfac889bed991266cc04e65cdd0)[I3897c](https://android-review.googlesource.com/#/q/I3897cdedbeabbb22174560595413e215b9237d95), [b/432616296](https://issuetracker.google.com/issues/432616296), [b/435416924](https://issuetracker.google.com/issues/435416924))
- The `send*` functions in `NavigationEventInputHandler` have had their prefixes renamed to `handle*`. ([Iffcaf](https://android-review.googlesource.com/#/q/Iffcaf608654332925a0506698a2b0b2857b267f1))
- `OnBackInvokedInputHandler` now extends the newly `abstract` `NavigationInputHandler`. ([Ib45aa](https://android-review.googlesource.com/#/q/Ib45aa401c332a5414269eacd29277bf10fbd3d82))
- Changed `NavigationEventDispatcherOwner` to require a parent dispatcher where you must explicitly pass `null` to create a root dispatcher. ([Ia6f64](https://android-review.googlesource.com/#/q/Ia6f647f5d4aa22ebf2cf31315084100b90ada6d3), [b/431534103](https://issuetracker.google.com/issues/431534103))

**Bug Fixes**

- Improved efficiency by avoiding collection copies in `NavigationEventDispatcher.dispose()`. ([I4ab09](https://android-review.googlesource.com/#/q/I4ab09c1236714c1d1e81c89bd25b47738ca419dc))
- Fixed an issue where the `NavigationEventHandler` did not correctly respond to changes in its enabled state. ([Ia5268](https://android-review.googlesource.com/#/q/Ia5268cc686cac9eab03fa4d430cf1171d49083f2),[I19bec](https://android-review.googlesource.com/#/q/I19bece87be51a3f34896323f0c8dc0f8e18a3659), [I5be5c](https://android-review.googlesource.com/#/q/I5be5c49bc7b430b16c7a7c9a86b1b18820682be4), [b/431534103](https://issuetracker.google.com/issues/431534103))

**Docs Updates**

- KDocs for `NavigationEvent` expanded to clarify its role as a unified event wrapper and detail property behavior across different navigation types (gestures, clicks). ([I91e8d](https://android-review.googlesource.com/#/q/I91e8d1d7fddb0b2b329422d3344a59c2dc506201))
- Updated documentation for system back handling Compose APIs (`BackHandler`, `PredictiveBackHandler`, `NavigationEventHandler`) to call out behavior specifically around callback order. ([I7ab94](https://android-review.googlesource.com/#/q/I7ab943c77b627402cb2cbfbca4fe790be35934cf), )

**Dependency Update**

- `NavigationEvent` now depends on Compose Runtime 1.9.0-beta03 which allows the `navigationevent-compose` artifact to support all KMP targets. ([Ia1b87](https://android-review.googlesource.com/#/q/Ia1b87ca8925ce4d58de6895853e26b821984ea46))

### Version 1.0.0-alpha05

July 30, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha05` is released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..b4562c71af5649ad7262ba4c7925899e6e93bdff/navigationevent).

**Parent-Child Hierarchy Support:**

A `NavigationEventDispatcher` can now have parent and child dispatchers, forming a hierarchical tree structure. This enables navigation events to propagate and be managed more flexibly across complex Compose UI components by reflecting the UI's structural hierarchy through chained dispatchers. ([I194ac](https://android-review.googlesource.com/#/q/I194acc61f09116048ab048e3f84cb6c58d34bbb6))  

      // Create a parent dispatcher that will manage navigation events at a higher level.
      val parentDispatcher = NavigationEventDispatcher()

      // Create a child dispatcher linked to the parent, forming a hierarchy.
      val childDispatcher = NavigationEventDispatcher(parentDispatcher)

The hierarchical `isEnabled` property allows for top-down control of a dispatcher. When `isEnabled` is set to `false` on a dispatcher, it automatically disables all its descendant dispatchers. This feature enables entire branches of the navigation event system to be toggled off efficiently. ([I9e985](https://android-review.googlesource.com/#/q/I9e985d5571ea07b9e2c0223ad2b4aaeab5266ab8))  

      // Disabling the child dispatcher disables all its callbacks and any of its children recursively.
      childDispatcher.isEnabled = false

Moreover, the `isEnabled` property on `NavigationEventCallback` now respects the enabled state of its associated dispatcher. This means a callback is considered enabled only if both the callback itself and its dispatcher (including its ancestors) are enabled, ensuring consistent hierarchical control over callback activation. ([I1799a](https://android-review.googlesource.com/#/q/I1799a02884a3167abf74e67b35fd10cc02cc9486))  

      // Create a test callback and add it to the child dispatcher.
      val callback1 = TestNavigationEventCallback(isEnabled = true)
      childDispatcher.addCallback(callback1)

      // Since the childDispatcher is disabled, the callback is effectively disabled as well.
      assertThat(callback1.isEnabled).isFalse()

A new `dispose()` method has been introduced for proper cleanup of dispatchers and their children. Calling `dispose()` stops listeners to prevent memory leaks, recursively disposes all child dispatchers, removes all callbacks registered to the dispatcher, and unlinks it from its parent. This guarantees resources are released correctly when dispatchers are no longer needed. ([I9e985](https://android-review.googlesource.com/#/q/I9e985d5571ea07b9e2c0223ad2b4aaeab5266ab8))  

      // Dispose the child dispatcher to clean up resources.
      childDispatcher.dispose()

If any public method is called on a disposed dispatcher, an `IllegalStateException` is thrown immediately. This prevents silent failures and helps developers identify improper usage during development. ([Ic2dc3](https://android-review.googlesource.com/#/q/Ic2dc36f3de36bed58eeef3ff2cfb185bc7f9df59))  

      val callback2 = TestNavigationEventCallback()

      // Attempting to use a disposed dispatcher will throw an exception.
      assertThrows<IllegalStateException> {
          childDispatcher.addCallback(callback2)
      }

**Note:** We will introduce a new `NavigationEventDispatcherOwner` Composable that automatically manages a child dispatcher within Compose UI in [aosp/3692572](https://r.android.com/3692572). However, this change did not make it into the current release cut and is planned for the next one.

**Navigation Testing Library**

- Add `navigationevent-testing` module to provide dedicated testing utilities for the `navigationevent` library. ([0e50b6](https://android-review.googlesource.com/#/q/I8a03eb9822202392f70866b31f9114a8695dbec7))
- Add `TestNavigationEventCallback` fake utility class for testing. It records callback method calls and stores received `NavigationEvent` items to support verification. ([4a0246](https://android-review.googlesource.com/#/q/Id7cf5f541cc80c5760554ed9d4ea933056612eef))
- Add `TestNavigationEvent` fake utility function to create `NavigationEvent` instances with default values, simplifying unit tests for navigation event processing. ([3b63f5](https://android-review.googlesource.com/#/q/Ia292be73ece193a7f64e8edc1c4dd3d05918bd86))
- Add `TestNavigationEventDispatcherOwner` fake utility class for testing. It tracks fallback and enabled-state-changed event counts to support interaction verification in tests. ([c8753e](https://android-review.googlesource.com/#/q/I4bf2258f6e505df6b6f2b2644f0e489047334863))

**API Changes**

- Move `NavigationEventInputHandler` from `androidMain` to `commonMain` to make it available in KMP common code. Add new `public send*` methods for dispatching events. Change dispatch functions on `NavigationEventDispatcher` from `public` to `internal`; users must now use `NavigationEventInputHandler` to send events. ([Ia7114](https://android-review.googlesource.com/#/q/Ia71147cb1e9b3268427965952cb2bedbedc47394))
- Rename `NavigationInputHandler` to `OnBackInvokedInputHandler`. ([I63405](https://android-review.googlesource.com/#/q/I63405b0c1465c2f87a6463c5d88a5b06d870e323))

**Bug Fixes**

- Refactor `NavigationEventDispatcher` to reduce overhead by avoiding intermediate list allocations and improving callback dispatch performance. ([I82702](https://android-review.googlesource.com/#/q/I8270264bf37616837729bf0cb2f3f2e0e5cf1fa7), [I1a9d9](https://android-review.googlesource.com/#/q/I1a9d94ca010cfa6565b294aa95e44afa2d9eac2b))
- Add `@FloatRange` annotations to `touchX`, `touchY`, and `progress` fields in `NavigationEvent` to enforce valid value ranges at compile time and improve API safety. ([Iac0ec](https://android-review.googlesource.com/#/q/Iac0ec1abcf81d854147f35478eb68961bed34bd4))

### Version 1.0.0-alpha04

July 2, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha04` is released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5f155b8946feeab0c4075d645f88769de2577a43..1b437892629a2cdedb46d9b7232575987b2cc6b5/navigationevent).

**Bug Fixes**

- Used `implementedInJetBrainsFork` to `navigationevent-compose` and added a `commonStubs` target to match Compose conventions. Change [requested by JetBrains](https://android-review.googlesource.com/c/platform/frameworks/support/+/3656217/12/navigationevent/navigationevent-compose/src/linuxx64StubsMain/kotlin/androidx/navigationevent/compose/LocalNavigationEventDispatcherOwner.linuxx64Stubs.kt#23). ([f60c79](https://android.googlesource.com/platform/frameworks/support/+/f60c796970d692f0633dbc78362a4937638a2ca8))
- Fixed application of the Compose compiler plugin for Kotlin/Native to ensure correct stub generation. No impact on public APIs or behavior. ([1890c9](https://android.googlesource.com/platform/frameworks/support/+/1890c9b8904ba5d633336bb7f877a8e61591da3b))

### Version 1.0.0-alpha03

June 18, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4fb12d1b1dc4dcae8ca603c7a5db938cc1abe39c..5f155b8946feeab0c4075d645f88769de2577a43/navigationevent).

**New Features**

- Introduced a new `navigationevent-compose` module to support Jetpack Compose features in the `navigationevent` library. ([980d78](https://android.googlesource.com/platform/frameworks/support/+log/4fb12d1b1dc4dcae8ca603c7a5db938cc1abe39c..5f155b8946feeab0c4075d645f88769de2577a43/navigationevent))
- `NavigationEvent` Compose has added a new `LocalNavigationEventDispatcherOwner` local composition. It returns a nullable value to better determine whether it is available in the current composition. `NavigationEventHandler` will now throw an error if the underlying owner is not found. ([62ffda](https://android.googlesource.com/platform/frameworks/support/+/62ffdad22b37dfa8bc2de4cf9bc6914af27d96f6))
- `NavigationEvent` Compose has added a new `NavigationEventHandler` Composable to handle (predictive back gesture) events. It provides a `Flow` of `NavigationEvent` objects that must be collected in the suspending lambda you provide [c42ba6](https://android.googlesource.com/platform/frameworks/support/+/c42ba6444b7080918681fe97cb652d0456308df6) :

    NavigationEventHandler { progress: Flow<NavigationEvent> ->
      // This block is executed when the back gesture begins.
      try {
        progress.collect { backEvent ->
          // Handle gesture progress updates here.
        }
        // This block is executed if the gesture completes successfully.
      } catch (e: CancellationException) {
        // This block is executed if the gesture is cancelled
        throw e
      } finally {
        // This block is executed either the gesture is completed or cancelled
      }
    }

**API Changes**

- Each `NavigationEventCallback` can now be registered with only one `NavigationEventDispatcher` at a time; adding it to multiple dispatchers throws an `IllegalStateException`. Note that this behavior differs from `OnBackPressedDispatcher`, which allows multiple dispatchers. ([e82c19](https://android.googlesource.com/platform/frameworks/support/+/e82c19efe12f6bcb856bbb83522496b02b609bff))
- Made `isPassThrough` a `val` to prevent mutation during navigation, which could break `NavigationEvent`'s dispatching. ([I0b287](https://android-review.googlesource.com/#/q/I0b287fd51b316c9199c8f1ff4a2b8fa6bafd4e94))

### Version 1.0.0-alpha02

June 4, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc..4fb12d1b1dc4dcae8ca603c7a5db938cc1abe39c/navigationevent/navigationevent).

**API Changes**

- Replace `NavigationEventDispatcher`'s secondary constructor with default arguments. ([I716a0](https://android-review.googlesource.com/#/q/I716a05450ebb11d7360f4a9c09a3cd89205d542a))
- Remove priority property from `NavigationEventCallback`. Pass priority to `NavigationEventDispatcher.addCallback()` instead. ([I13cae](https://android-review.googlesource.com/#/q/I13caecd84220bf919549958d79e424d1fc2cd3ab))

**Bug Fixes**

- Fixed a `ConcurrentModificationException` that could occur when `NavigationEventCallback.remove()` was called due to simultaneously modifying the internal list of closeables. ([b/420919815](https://issuetracker.google.com/issues/420919815))

### Version 1.0.0-alpha01

May 20, 2025

`androidx.navigationevent:navigationevent-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd41781824511ce4d5c4a05d2df4aaaee669f0bc/navigationevent/navigationevent).

**New Features**

- The `androidx.navigationevent` library provides a KMP-first API for handling system back as well as [Predictive Back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture). The `NavigationEventDispatcher` serves as a common APIs for registering one or more `NavigationEventCallback` instances for receiving system back events.
- This layer sits below the previously released APIs in `androidx.activity` and aims to be a less opinionated replacement for using the Activity APIs in higher level components or directly using the Android framework `OnBackInvokedDispatcher` APIs. The `androidx.activity` APIs have been rewritten on top of the Navigation Event APIs as part of [Activity 1.12.0-alpha01](https://developer.android.com/jetpack/androidx/releases/activity#1.12.0-alpha01).