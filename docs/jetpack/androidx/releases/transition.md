---
title: https://developer.android.com/jetpack/androidx/releases/transition
url: https://developer.android.com/jetpack/androidx/releases/transition
source: md.txt
---

# Transition

[User Guide](https://developer.android.com/guide/navigation/navigation-animate-transitions)[Code Sample](https://github.com/android/animation-samples/tree/main/Motion)  
API Reference  
[androidx.transition](https://developer.android.com/reference/kotlin/androidx/transition/package-summary)  
Animate motion in the UI with starting and ending layouts.  

|  Latest Update   |                                  Stable Release                                   | Release Candidate |                                          Beta Release                                           | Alpha Release |
|------------------|-----------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------|---------------|
| December 3, 2025 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/transition#1.6.0) | -                 | [1.7.0-beta01](https://developer.android.com/jetpack/androidx/releases/transition#1.7.0-beta01) | -             |

## Declaring dependencies

To add a dependency on Transition, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Java language implementation
    implementation "androidx.transition:transition:1.6.0"
    // Kotlin
    implementation "androidx.transition:transition-ktx:1.6.0"
}
```

### Kotlin

```kotlin
dependencies {
    // Java language implementation
    implementation("androidx.transition:transition:1.6.0")
    // Kotlin
    implementation("androidx.transition:transition-ktx:1.6.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460400+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460400&template=1422754)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.7

### Version 1.7.0-beta01

December 03, 2025

`androidx.transition:transition:1.7.0-beta01`and`androidx.transition:transition-ktx:1.7.0-beta01`are released. Version 1.7.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fa9d0954ece0376736164b0f7bc2ef33506ab70..d27fe9a65dd5cebd5bfb55f7a88aebe7652fe939/transition).

**Bug Fixes**

- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df),[b/380448311](https://issuetracker.google.com/issues/380448311),[b/435705964](https://issuetracker.google.com/issues/435705964),[b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.7.0-alpha01

July 30, 2025

`androidx.transition:transition:1.7.0-alpha01`and`androidx.transition:transition-ktx:1.7.0-alpha01`are released. Version 1.7.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/184a59d7780ba90e35570b93f6513724b08c2168..5fa9d0954ece0376736164b0f7bc2ef33506ab70/transition).

**Bug Fixes**

- Fixed crash happening when the View is attached to a Window with a null`windowId`. ([I2ddf6](https://android-review.googlesource.com/#/q/I2ddf6129c99f66e0754df39385ecaf7a46cb9d19))

## Version 1.6

### Version 1.6.0

April 23, 2025

`androidx.transition:transition:1.6.0`and`androidx.transition:transition-ktx:1.6.0`are released. Version 1.6.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/07b263a69e6f1671057d7770cf99a0c9811efe10..184a59d7780ba90e35570b93f6513724b08c2168/transition).

### Version 1.6.0-rc01

March 26, 2025

`androidx.transition:transition:1.6.0-rc01`and`androidx.transition:transition-ktx:1.6.0-rc01`are released. Version 1.6.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..07b263a69e6f1671057d7770cf99a0c9811efe10/transition).

### Version 1.6.0-beta01

March 12, 2025

`androidx.transition:transition:1.6.0-beta01`and`androidx.transition:transition-ktx:1.6.0-beta01`are released with no changes since the last alpha. Version 1.6.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..7a145e052ae61e272e91ffe285e9451b8ab71870/transition).

### Version 1.6.0-alpha01

December 11, 2024

`androidx.transition:transition:1.6.0-alpha01`and`androidx.transition:transition-ktx:1.6.0-alpha01`are released. Version 1.6.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d628af7c0127584d10f86a6e0872691a5de4536..46295bc0b75a16f452e8e0090e8de41073d4dbb6/transition).

**New Features**

- Transition now sets the disjoint parent for`ViewOverlays`used to animate its transitions. This allows for the resolution of owners through the disjoint parent, which means you can now correctly resolve`ViewModels`, lifecycles, etc. during a transition. ([I10a16](https://android-review.googlesource.com/#/q/I10a16c84ba1efbf89a503418889ddd56bb711bed),[b/340894487](https://issuetracker.google.com/issues/340894487),[b/287484338](https://issuetracker.google.com/issues/287484338))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([I1f54e](https://android-review.googlesource.com/#/q/I1f54e3f6b2dad0e8bfd2adab7566e1dc4d9d6bc1),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8),[b/345472586](https://issuetracker.google.com/issues/345472586))

## Version 1.5

### Version 1.5.1

July 24, 2024

`androidx.transition:transition:1.5.1`and`androidx.transition:transition-ktx:1.5.1`are released. Version 1.5.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/997511f658e698f2cc9bfbb485bacdefc476ba19..2d628af7c0127584d10f86a6e0872691a5de4536/transition).

**Bug Fixes**

- Fixed an issue where calls to`animateToStart()`or`animateToEnd()`on a seekable transition would be ignored if the transition was not started. ([I44d96](https://android-review.googlesource.com/#/q/I44d9618604c29659e1f6ae7e966cd1533369b18c),[b/338624457](https://issuetracker.google.com/338624457))

### Version 1.5.0

May 1, 2024

`androidx.transition:transition:1.5.0`and`androidx.transition:transition-ktx:1.5.0`are released. Version 1.5.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/725dc97d601fc303e9e87ed447ed24f0bdf7670f..997511f658e698f2cc9bfbb485bacdefc476ba19/transition).

**Important changes since 1.4.0**

- Transitions support seeking on API 34 and above. A new API was added to`TransitionManager`,`controlDelayedTransition()`, which returns a`TransitionSeekController`that allows seeking the`Transition`. This functionality is used by[Fragment 1.7.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.0)to automatically seek transitions when using the Predictive Back Gesture.
- Transitions have a new method,`getRootTransition()`, that returns the Transition containing the current Transition or the current Transition if it isn't contained by any other Transition. This can be useful if the developer needs to have listeners for when the entire Transition starts or ends.
- `TransitionListeners`now have new`onTransitionStart()`and`onTransitionEnd()`listeners that allow the developer to know whether the transition is starting or ending going in reverse or not. This can be important for developing seekable transitions that have`TransitionListeners`.

### Version 1.5.0-rc02

April 17, 2024

`androidx.transition:transition:1.5.0-rc02`and`androidx.transition:transition-ktx:1.5.0-rc02`are released. Version 1.5.0-rc02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/341a818f1f3b41d0af97720246607521510acb14..725dc97d601fc303e9e87ed447ed24f0bdf7670f/transition).

**Dependency Update**

- Updated Fragment dependency to[version 1.7.0-rc02](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.0-rc02)which fixed a bug where if a non-seekable shared element was added to a transaction where all other transitions were seekable, there would be a crash.

### Version 1.5.0-rc01

April 3, 2024

`androidx.transition:transition:1.5.0-rc01`and`androidx.transition:transition-ktx:1.5.0-rc01`are released. Version 1.5.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..341a818f1f3b41d0af97720246607521510acb14/transition).

### Version 1.5.0-beta01

March 20, 2024

`androidx.transition:transition:1.5.0-beta01`and`androidx.transition:transition-ktx:1.5.0-beta01`are released. Version 1.5.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..a57d7d17753695012b58c9ce7ad55a8d39157e62/transition).

**Bug Fixes**

- Fixed an issue in Fragments where interrupting incoming transitions with a Predictive back gesture would destroy the entering view, potentially leaving a blank screen. ([Id3f22](https://android-review.googlesource.com/#/q/Id3f228dd5f53742c68e6cb16b752022e18e00ec9),[b/319531491](https://issuetracker.google.com/issues/319531491))

### Version 1.5.0-alpha06

January 10, 2024

`androidx.transition:transition:1.5.0-alpha06`and`androidx.transition:transition-ktx:1.5.0-alpha06`are released.[Version 1.5.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/transition)

**Bug Fixes**

- When`TransitionSeekController.animateToStart()`is used, added`TransitionListeners`will now have`onTransitionEnd()`called after the`animateToStart()`'s given`Runnable`. ([Ic6a55](https://android-review.googlesource.com/#/q/Ic6a55916958f85d41c54d7739bde09cfc2352d7c),[b/307624554](https://issuetracker.google.com/issues/307624554))

**Dependency Update**

- The Fragment dependency has been updated to`1.7.0-alpha08`.

### Version 1.5.0-alpha05

November 29, 2023

`androidx.transition:transition:1.5.0-alpha05`and`androidx.transition:transition-ktx:1.5.0-alpha05`are released.[Version 1.5.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e63042bab069a262f0e762d23f5a18152f3bf12a..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/transition)

**Bug Fixes**

- Fixed a`NullPointerException`caused by setting a shared element transition and failing to set an`enter/exitTransition`as well. ([I8472b](https://android-review.googlesource.com/#/q/I8472b865cf93d1d3463f73942c460263f746fef5))
- Fixed issue where`animateToStart()`with`Slide()`failed to move the View back to the start position ([I698f4](https://android-review.googlesource.com/#/q/I698f4dbcef46304f9aa545847d205f7b70c80d63),[b/300157785](https://issuetracker.google.com/issues/300157785))
- Fixed reentrancy problem in Transition which broke cancellation. ([Iddcce](https://android-review.googlesource.com/#/q/Iddcce38e84838ddee22ed6bde72a6adb16cc0112),[b/308379201](https://issuetracker.google.com/issues/308379201))

### Version 1.5.0-alpha04

October 4, 2023

`androidx.transition:transition:1.5.0-alpha04`and \`androidx.transition:transition-ktx:1.5.0-alpha04 are released.[Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..e63042bab069a262f0e762d23f5a18152f3bf12a/transition)

**API Changes**

- **Breaking Change** - The`animateToStart()`method now takes a`Runnable`that should be used to return the transitioning views back to their original state.

### Version 1.5.0-alpha03

September 20, 2023

`androidx.transition:transition:1.5.0-alpha03`and`androidx.transition:transition-ktx:1.5.0-alpha03`are released.[Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/76958258c313f048a95afd97bef633d6c34a75ee..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/transition)

**New Features**

- Transition now provides support for in-app Predictive Back animations on Android 14 devices when used with[Fragment`1.7.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.0-alpha05).

**Bug Fixes**

- Fixed Slide Transition interruption bug. When a Slide Transition interrupted an entering transition to remove a View, it would jump to an incorrect position. ([I946f8](https://android-review.googlesource.com/#/q/I946f826a338304d07e3bd7527e371ee655464e77),[b/297427333](https://issuetracker.google.com/issues/297427333))

### Version 1.5.0-alpha02

September 6, 2023

`androidx.transition:transition:1.5.0-alpha02`and`androidx.transition:transition-ktx:1.5.0-alpha02`are released.[Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91433b3e27791405abd397d20a416c486691ae6e..9446fd1f176bf11de2e1a6a638e2a3f86d0dcc6e/transition)

**New Features**

- `TransitionSeekController`now allows you to set the progress as a fraction of the total duration via`setCurrentFragment()`. ([aosp/2647607](https://android-review.googlesource.com/c/platform/frameworks/support/+/2647607))
- `TransitionSeekController`now allows observing progress when using`animateToStart()`and`animateToEnd()`by calling`addOnProgressChangedListener`. ([aosp/2647607](https://android-review.googlesource.com/c/platform/frameworks/support/+/2647607))
- Added`TransitionManager.seekTo()`to allow using Scenes for seeking Transitions. ([aosp/2647607](https://android-review.googlesource.com/c/platform/frameworks/support/+/2647607))
- Added physics-based animations to seeking transitions. It uses a 1-D velocity tracker to track the progress change with`setCurrentFraction()`or`setCurrentPlayTimeMillis()`and uses it for the initial velocity of`animateToStart`and`animateToEnd`. ([aosp/2647607](https://android-review.googlesource.com/c/platform/frameworks/support/+/2647607))

**Bug Fixes**

- Fixed a flicker when seeking an`AutoTransition`. ([aosp/2643369](https://android-review.googlesource.com/c/platform/frameworks/support/+/2643369))
- Fixed an issue where a`Slide`transition would jump to the wrong starting position when interrupted. ([aosp/2733729](https://android-review.googlesource.com/c/platform/frameworks/support/+/2733729),[b/297427333](https://issuetracker.google.com/issues/297427333))

**Dependency Update**

- Transition now compiles with API 34.

### Version 1.5.0-alpha01

May 10, 2023

`androidx.transition:transition:1.5.0-alpha01`and`androidx.transition:transition-ktx:1.5.0-alpha01`are released. This version is developed in an internal branch.
| **Note:** This version will only compile against the[Android 14 (Upside Down Cake) Beta 2 SDK](https://developer.android.com/about/versions/14#beta-1).

**New Features**

- Transitions support seeking on API 34 and above. A new API was added to`TransitionManager`,`controlDelayedTransition()`, which returns a`TransisionSeekController`that allows seeking the Transition.

**API Changes**

- `TransitionManager`has a new method,`controlDelayedTransition()`, that allows applications to control the progress of transition animations on API 34+. The returned`TransitionSeekController`lets the developer know when the transition is ready for seeking, the duration of the animation, and allows setting the current time of the animation. Only Transitions that override`isSeekable()`to return true are supported by`controlDelayedTransition()`.
- Transitions have a new method,`getRootTransition()`, that returns the Transition containing the current Transition or the current Transition if it isn't contained by any other Transition. This can be useful if the developer needs to have listeners for when the entire Transition starts or ends.
- `TransitionListeners`now have new`onTransitionStart()`and`onTransitionEnd()`listeners that allow the developer to know whether the transition is starting or ending going in reverse or not. This can be important for developing seekable transitions that have`TransitionListeners`.

**Bug Fixes**

- Transitions now copy their`TransitionListeners`when they are cloned. This means that adding new listeners during`createAnimator()`will not affect the root Transition.

## Version 1.4.1

### Version 1.4.1

April 21, 2021

`androidx.transition:transition:1.4.1`and`androidx.transition:transition-ktx:1.4.1`are released.[Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7702878f894128b9f8b9159e3e0a43482d46117e..2ee65abdd1b6cbf649c6b28564c56042e9bac772/transition)

**Bug Fixes**

- Fixed an issue where starting a`Transition`in one container would inadvertently pause other running transitions in separate containers, causing those other transitions to never finish. ([aosp/1664439](https://android-review.googlesource.com/c/platform/frameworks/support/+/1664439),[b/182845041](https://issuetracker.google.com/issues/182845041))

## Version 1.4.0

### Version 1.4.0

January 27, 2021

`androidx.transition:transition:1.4.0`and`androidx.transition:transition-ktx:1.4.0`are released.[Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3b5b2898d67aed2ba70a937b3dec5300b03288..7702878f894128b9f8b9159e3e0a43482d46117e/transition)

**Major changes since 1.3.0**

- The`transition-ktx`artifact introduces Kotlin extensions for adding listeners to AndroidX`Transition`instances. ([b/138870873](https://issuetracker.google.com/138870873))

### Version 1.4.0-rc01

December 2, 2020

`androidx.transition:transition:1.4.0-rc01`and`androidx.transition:transition-ktx:1.4.0-rc01`are released with no changes from`1.4.0-beta01`.[Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..2b3b5b2898d67aed2ba70a937b3dec5300b03288/transition)

### Version 1.4.0-beta01

July 22, 2020

`androidx.transition:transition:1.4.0-beta01`and`androidx.transition:transition-ktx:1.4.0-beta01`are released with no changes since`1.4.0-alpha01`.[Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/transition)

### Version 1.4.0-alpha01

June 24, 2020

`androidx.transition:transition:1.4.0-alpha01`and`androidx.transition:transition-ktx:1.4.0-alpha01`are released.[Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db/transition)

**New Features**

- The`transition-ktx`artifact introduces Kotlin extensions for adding listeners to AndroidX`Transition`instances. ([b/138870873](https://issuetracker.google.com/issues/138870873))

## Version 1.3.1

### Version 1.3.1

February 19, 2020

`androidx.transition:transition:1.3.1`is released.[Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/250921e7515d62adecbbc0083dc133d14dff542d..d9fcad3c5d44e76249fafb1e5e3619c80d0f3a72/transition/transition)

**Bug Fixes**

- Fixed bug when some animated Views were incorrectly clipped when ChangeTransform is used ([b/148798452](https://issuetracker.google.com/issues/148798452))

## Version 1.3.0

### Version 1.3.0

January 22, 2020

`androidx.transition:transition:1.3.0`is released.[Version 1.3.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/80680eca51be5c8483a0ad6f0b9466c99474ad5b..250921e7515d62adecbbc0083dc133d14dff542d/transition/transition).

**Important changes since 1.2.0**

- **Improvements for Fragment 1.2.0** : Improved the integration with[Fragment 1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)to ensure that the Fragment's View is not destroyed before the transition completes and that transitions are cancelled at the appropriate time

### Version 1.3.0-rc02

December 4, 2019

`androidx.transition:transition:1.3.0-rc02`is released.[Version 1.3.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c378b9a2eae63d2701c82b0144af36e33d15c26a..80680eca51be5c8483a0ad6f0b9466c99474ad5b/transition/transition).

**Bug fixes**

- Fixed an issue where Views were incorrectly marked`INVISIBLE`after popping a hidden Fragment. ([b/70793925](https://issuetracker.google.com/issues/70793925))

### Version 1.3.0-rc01

October 23, 2019

`androidx.transition:transition:1.3.0-rc01`is released with no changes since`1.3.0-beta01`.[Version 1.3.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/71bb8aed30b5127486fc7bf88a0b8dfe0b36180e..c378b9a2eae63d2701c82b0144af36e33d15c26a/transition/transition).

### Version 1.3.0-beta01

October 9, 2019

`androidx.transition:transition:1.3.0-beta01`is released.[Version 1.3.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd364edf901d664ab67f9fc20824e7f1fef3f18b..71bb8aed30b5127486fc7bf88a0b8dfe0b36180e/transition/transition).

**New features**

- Improved the integration with[Fragment`1.2.0-beta01`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-beta01)to ensure that the Fragment's View is not destroyed before the transition completes and that transitions are cancelled at the appropriate time. ([aosp/1119841](https://android-review.googlesource.com/1119841))

## Version 1.2.0

### Version 1.2.0

October 9, 2019

`androidx.transition:transition:1.2.0`is released with no changes from 1.2.0-rc01 .[Version 1.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd364edf901d664ab67f9fc20824e7f1fef3f18b..847e7f8df1bf5a7f744b398423b8791bd85e4097/transition).

**Important changes since version 1.1.0**

This version should be used if you're targeting API level 29. Otherwise, some of the transitions will not work properly. Instead of the reflection calls, this version uses the new public methods added in API Level 29. It is a part of our restrictions on non-SDK interfaces effort.

### Version 1.2.0-rc01

September 5, 2019

`androidx.transition:transition:1.2.0-rc01`is released with no changes since version`1.2.0-beta01`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/228b8e37394aecfc5df808b62b34a3455bc747aa..cd364edf901d664ab67f9fc20824e7f1fef3f18b/transition).
| **Note:** This version should be used if you're targeting API level 29.

### Version 1.2.0-beta01

July 2, 2019

`androidx.transition:transition:1.2.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/f584907a42c20e38f68e1b60f1f701db76ca1408..b5043f248cd7bf97c96a596159a075f473375cc1/transition).
| **Note:** This version should be used if you are specifying 29 as a`targetSdkVersion`and will only work with the Q Beta 4 SDK.

**New features**

- This version should be used if you are specifying 29 as a`targetSdkVersion`. Otherwise, some of the transitions will not work properly. Instead of the reflection calls, this version uses the new public methods added in API Level 29. It is a part of our restrictions on non-SDK interfaces effort.

### Version 1.2.0-alpha01

May 7, 2019

`androidx.transition:transition:1.2.0-alpha01`is released.
| **Note:** This version will only work with the Q Beta 3 SDK.

**New features**

- This version should be used if you are specifying Q as a`targetSdkVersion`. Otherwise, some of the transitions will not work properly. Instead of the reflection calls, this version uses the new public methods added in Q. It is a part of our restrictions on non-SDK interfaces effort.

## Version 1.1.0

### Version 1.1.0

July 2, 2019

`androidx.transition:transition:1.1.0`is released with no changes from`1.1.0-rc02`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/946804c1a990b156e5e20a148c8affe71d38c144..d0129b3926300ba2edf0b0fce433c939612425e9/transition).

### Version 1.1.0-rc02

June 5, 2019

`androidx.transition:transition:1.1.0-rc02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/2ee5d826c17d6b538469d85d92745ea43f1ec19e..946804c1a990b156e5e20a148c8affe71d38c144/transition).

**Bug fixes**

- Fix for`TransitionManager.endTransitions()`to correctly work with dependent transitions. ([aosp/946400](https://android-review.googlesource.com/c/platform/frameworks/support/+/946400/))

### Version 1.1.0-rc01

May 7, 2019

`androidx.transition:transition:1.1.0-rc01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/7d0db7338f4fda203216bed530d235f500fa7af3..f584907a42c20e38f68e1b60f1f701db76ca1408/transition).

### Version 1.1.0-beta01

April 3, 2019

`androidx.transition:transition:1.1.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/863462a41d0708ab9044f826e85250cb3d20ffa8..2a481e3fb01ec779d5bc26b7963942e7476ec8a8/transition).

**Bug fixes**

- Fixed`ViewGroupOverlay`caching bug in`Visibility`, occurring on API Level 17 and lower ([aosp/937350](https://android-review.googlesource.com/c/platform/frameworks/support/+/937350))

### Version 1.1.0-alpha02

March 13, 2019

`androidx.transition:transition:1.1.0-alpha02`is released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/3aaf42ac1ab4f795cae10b821da9c9144b361f21..863462a41d0708ab9044f826e85250cb3d20ffa8/transition).

**API changes**

- The method parameter's type of`Scene.getCurrentScene()`was changed from`View`to`ViewGroup`.

**Bug fixes**

- `SidePropagation`doesn't work when an additional delay provided via`setStartDelay()`([b/119839526](https://issuetracker.google.com/issues/119839526)).
- `ChangeImageTransform`applies wrong matrix when interrupted before API 21 ([b/123226255](https://issuetracker.google.com/issues/123226255)).
- `ChangeTransform`works incorrectly in some cases before API 21 ([b/125777978](https://issuetracker.google.com/issues/125777978)).

### Version 1.1.0-alpha01

December 3, 2018

**API changes**

- [aosp/807055](https://android-review.googlesource.com/c/platform/frameworks/support/+/807055/):`Scene.getCurrentScene(View)`method made public. It allows you to write a custom conditional logic depending on a current scene.

**Bug fixes**

- Fixed crash when using`TransitionManager`to collapse/expand item in`RecyclerView`([b/37129527](https://issuetracker.google.com/issues/37129527)).
- Fixed incorrect animation when two Visibility transitions applied ([b/62629600](https://issuetracker.google.com/issues/62629600)).
- Allow override values like duration and interpolator for TransitionSet's children ([b/64644617](https://issuetracker.google.com/issues/64644617)).
- Many other minor bugs fixed.