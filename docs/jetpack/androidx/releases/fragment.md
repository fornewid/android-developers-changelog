---
title: https://developer.android.com/jetpack/androidx/releases/fragment
url: https://developer.android.com/jetpack/androidx/releases/fragment
source: md.txt
---

# Fragment

[User Guide](https://developer.android.com/guide/components/fragments) [Code Sample](https://github.com/android/user-interface-samples) API Reference  
[androidx.fragment.app](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary)  
[androidx.fragment.app.testing](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary)  
Segment your app into multiple, independent screens that are hosted within an Activity.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| August 13, 2025 | [1.8.9](https://developer.android.com/jetpack/androidx/releases/fragment#1.8.9) | - | - | - |

## Declaring dependencies

To add a dependency on Fragment, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    def fragment_version = "1.8.9"

    // Java language implementation
    implementation "androidx.fragment:fragment:$fragment_version"
    // Kotlin
    implementation "androidx.fragment:fragment-ktx:$fragment_version"
    // Compose
    implementation "androidx.fragment:fragment-compose:$fragment_version"
    // Testing Fragments in Isolation
    debugImplementation "androidx.fragment:fragment-testing-manifest:$fragment_version"
    androidTestImplementation "androidx.fragment:fragment-testing:$fragment_version"
}
```

### Kotlin

```kotlin
dependencies {
    val fragment_version = "1.8.9"

    // Java language implementation
    implementation("androidx.fragment:fragment:$fragment_version")
    // Kotlin
    implementation("androidx.fragment:fragment-ktx:$fragment_version")
    // Compose
    implementation("androidx.fragment:fragment-compose:$fragment_version")
    // Testing Fragments in Isolation
    debugImplementation("androidx.fragment:fragment-testing:$fragment_version")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460964+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460964&template=1182267)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.8

### Version 1.8.9

August 13, 2025

`androidx.fragment:fragment-*:1.8.9` is released. Version 1.8.9 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d008d0faccfc0ad192d2b2df27e3c61227f381f6..f39ca3510efb2347ebfef231e25a3e804922450d/fragment).

**Bug Fixes**

- Fixed an issue where cancelling a predictive back gesture that pops a hide operation will cause the subsequent gesture not to animate correctly when using animators. ([I0a400](https://android-review.googlesource.com/#/q/I0a4003096caf30f8185e1a9bd2b493f7d1d0c875), [b/384765586](https://issuetracker.google.com/issues/384765586))
- Fixed an error where a combination of `setMaxLifecycle` and `popBackStack` could fail to move the top fragment to RESUMED. ([I3448b](https://android-review.googlesource.com/#/q/I3448b3c372f318b399ce93f74326fbfda87475d9), [b/406127576](https://issuetracker.google.com/issues/406127576))

### Version 1.8.8

June 4, 2025

`androidx.fragment:fragment-*:1.8.8` is released. Version 1.8.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7edaa16f0a4d8d4afbe11d4d62aca84635ff839a..d008d0faccfc0ad192d2b2df27e3c61227f381f6/fragment).

**Bug Fixes**

- Fixed an issue where `FragmentManager` would crash while trying to save the state of Fragments that were added with `setMaxLifecycle(Lifecycle.State.INITIALIZED)`. These fragments, since they never when through `onCreate()`, no longer have any state saved or `onSaveInstanceState()` called. ([I6e37a](https://android-review.googlesource.com/#/q/I6e37a01551008636d6b5ccafa65f03fcbd19321f))

### Version 1.8.7

May 20, 2025

`androidx.fragment:fragment-*:1.8.7` is released. Version 1.8.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e22fa33d22862979c7905e12ed76e74412dc41d2..7edaa16f0a4d8d4afbe11d4d62aca84635ff839a/fragment).

**Bug Fixes**

- Fixed an issue with `FragmentManager` not being in the proper state after pop and replace operations in the same frame that could cause a crash in conjunction with popping the backstack either via `popBackStack` or the predictive back gesture. ([I50ad1](https://android-review.googlesource.com/#/q/I50ad1d46b1bb080b2006883874ee68ae27e98cc7))
- Fixed a crash caused by using AndroidX Transitions and getting into a case where quick consecutive fragment transactions attempt to cancel an unstarted transition and the AndroidX Transition library does not properly clear the transition state. (see [b/414612221](https://issuetracker.google.com/414612221)). ([Ib5235](https://android-review.googlesource.com/#/q/Ib52354b924286b12feda99b49fae09a18b8cb45f))

### Version 1.8.6

February 12, 2025

`androidx.fragment:fragment-*:1.8.6` is released. Version 1.8.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/42d1f9653eafdf921d3f0be1ffadd8905abac21a..e22fa33d22862979c7905e12ed76e74412dc41d2/fragment).

**Bug Fixes**

- `FragmentContainerView`'s `setOnApplyWindowInsetsListener` override now takes a null listener, matching what the framework allows. ([I575f0](https://android-review.googlesource.com/#/q/I575f0b5da72d096b14393afd9819ab66e061b002), [b/282790626](https://issuetracker.google.com/issues/282790626))

### Version 1.8.5

October 30, 2024

`androidx.fragment:fragment-*:1.8.5` is released. Version 1.8.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d20e1de525e7d80ea3b79a4698f86adcb901b66b..42d1f9653eafdf921d3f0be1ffadd8905abac21a/fragment).

**Bug Fixes**

- Fixed an `IllegalStateException` triggered by `saveBackStack` only after a Predictive Back gesture was canceled or interrupted. ([I3387d](https://android-review.googlesource.com/#/q/I3387d9d02495112f211448d7f3c9f862299da697), [b/342419080](https://issuetracker.google.com/issues/342419080))

### Version 1.8.4

October 2, 2024

`androidx.fragment:fragment-*:1.8.4` is released. Version 1.8.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/da5509028c3c40784100283320b83785fbd203c6..d20e1de525e7d80ea3b79a4698f86adcb901b66b/fragment).

**Bug Fixes**

- Fixed an issue where quickly pressing the system back button or quickly doing gesture back will cause Fragments to crash when using Androidx Transitions. ([Ibc038](https://android-review.googlesource.com/#/q/Ibc038d8db7c3e7903a4dc8bfa556883705d27ee8), [b/364804225](https://issuetracker.google.com/issues/364804225))
- Fixed an issue in fragments where interrupting a predictive back gesture would send the fragment manager into an undefined state and even up showing the wrong fragment. ([If82e2](https://android-review.googlesource.com/#/q/If82e2cd540a5319faa2e40d4a28ce31026e2e19d), [b/338624457](https://issuetracker.google.com/issues/338624457))
- Fixed an `UninitializedPropertyAccessException` in `AndroidFragment` when dynamically swapping out the Class your `AndroidFragment` instance is using. ([I12dea](https://android-review.googlesource.com/#/q/I12dea04016d1f68583acb1265ca0a937a7ebd75d))

### Version 1.8.3

September 4, 2024

`androidx.fragment:fragment-*:1.8.3` is released. Version 1.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/539527ae77b888b02a3b0ca85afcaea30a416b4e..558c2142ee7a4d7b67c119563e2c364c4c3a9a08/fragment).

**Bug Fixes**

- `FragmentManager` now correctly takes into account pending operations when handling the Predictive Back gesture. This should ensure that doing a system back no longer causes an `IndexOutOfBoundsException`. ([I9ba32](https://android-review.googlesource.com/#/q/I9ba32fe0583d13618c1eac3f13fdbd8992a3b7ad), [b/342316801](https://issuetracker.google.com/issues/342316801))
- `AndroidFragment` no longer crashes if it is added to composition while the containing activity/fragment's state is already saved. ([I985e9](https://android-review.googlesource.com/#/q/I985e91e6d654815c99e97927154d0fd8f2228c0b), [b/356643968](https://issuetracker.google.com/issues/356643968))

### Version 1.8.2

July 24, 2024

`androidx.fragment:fragment-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c06fe0a3e7c61f31e0734f93bef3899fae9dc0f4..539527ae77b888b02a3b0ca85afcaea30a416b4e/fragment).

**Bug Fixes**

- `AndroidFragment` now properly handles cases where the parent fragment is put on the Fragment back stack, avoiding 'No view found for id' issues when popping back to that fragment. ([I94608](https://android-review.googlesource.com/#/q/I94608fed9ada006e5e601ede8adb8be81fae29a0))
- Fragments added via the `FragmentTransaction.add` method that takes a `ViewGroup` now wait for `onContainerAvailable` before progressing to `onStart()`. This affects users of that API, such as `AndroidFragment`, which now waits for the `AndroidFragment` to re-enter composition before moving it through `onStart()`. ([I94608](https://android-review.googlesource.com/#/q/I94608fed9ada006e5e601ede8adb8be81fae29a0))

### Version 1.8.1

June 26, 2024

`androidx.fragment:fragment-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cb33e7274271da73c61e9231b4d372300cecec4..c06fe0a3e7c61f31e0734f93bef3899fae9dc0f4/fragment).

**Bug Fixes**

- Fixed an issue where fragments without a container were immediately `DESTROYED` when starting a predictive back gesture. Now they are held in the `CREATED` state until after the gesture is complete. ([If6b83](https://android-review.googlesource.com/#/q/If6b83f7dbb655e0bebc99c3c769625626a7c4e8d), [b/345244539](https://issuetracker.google.com/issues/345244539))

### Version 1.8.0

June 12, 2024

`androidx.fragment:fragment-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b9b27a2972eeb4612cbea0f230f514ffb142a5ee..4cb33e7274271da73c61e9231b4d372300cecec4/fragment).

**Important changes since 1.7.0**

- The `fragment-compose` artifact now contains an `AndroidFragment` `Composable` that allows adding fragments into the Compose hierarchy via the fragment class name. It automatically handles the saving and restoring of the Fragment's state. This should be used as a direct replacement for the previously recommended approach of using `AndroidViewBinding` to inflate a Fragment.
- The `onBackStackChangeCancelled` callback on the `FragmentManager`'s `OnBackStackChangedListener` interface now fires as part of executing operations in `FragmentManager`, moving it closer in line with the timing of the `onBackStackChangeCommitted` callback.

### Version 1.8.0-rc01

May 29, 2024

`androidx.fragment:fragment-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..b9b27a2972eeb4612cbea0f230f514ffb142a5ee/fragment).

**Bug Fixes**

- The `onBackStackChangeCancelled` callback on the `FragmentManagers OnBackStackChangedListener` interface now fires as part of executing operations in `FragmentManager`, moving it closer in line with the timing of the `onBackStackChangeCommitted` callback. ([I5ebfb](https://android-review.googlesource.com/#/q/I5ebfb12840173c4e239ff239856c2a05464648f5), [b/332916112](https://issuetracker.google.com/issues/332916112))

### Version 1.8.0-beta01

May 14, 2024

`androidx.fragment:fragment-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5c17ac8d339b80b5f509f83792f5923e337612c7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/fragment).

**Bug Fixes**

- From [Fragment `1.7.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.1): Predictive back will now only run for transactions in which all of the fragments have either a Animator or a Seekable Androidx Transition. This fixes an issue where canceling a partially seekable transaction would cause a black screen. ([I43037](https://android-review.googlesource.com/#/q/I4303795b1cb4f7e58cd4f8efe0baa53d64a51dd8), [b/339169168](https://issuetracker.google.com/issues/339169168))

### Version 1.8.0-alpha02

April 17, 2024

`androidx.fragment:fragment-*:1.8.0-alpha02` is released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..5c17ac8d339b80b5f509f83792f5923e337612c7/fragment).

**Bug Fixes**

- From [Fragment `1.7.0-rc02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.0-rc02): Added logs to indicate why setting a `sharedElement` without any other transitions will fail to run. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48ef375eb1c498bc13da82d5d8355be58ba0ff))
- From [Fragment `1.7.0-rc02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.7.0-rc02): Fixed a bug where if a non-seekable shared element was added to a transactions where all other transitions were seekable, there would be a crash. Now the transaction will correctly be considered non-seekable. ([I18ccd](https://android-review.googlesource.com/#/q/I18ccdbc4f7226f265106435945f8ee4039dc475b))

### Version 1.8.0-alpha01

April 3, 2024

`androidx.fragment:fragment-*:1.8.0-alpha01` is released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55/fragment).

**New Features**

- The new `AndroidFragment` `Composable` allows adding fragments into the Compose hierarchy via the fragment class name. It automatically handles the saving and restoring of the Fragment's state. This can be used as a direct replacement for the [AndroidViewBinding](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidViewBinding(kotlin.Function3,androidx.compose.ui.Modifier,kotlin.Function1)) `Composable`.([b/312895363](https://issuetracker.google.com/issues/312895363), [Icf841](https://android-review.googlesource.com/#/q/Icf84199bbe487b2a2b6a95d2b6e09415f810e77a))

**Documentation Changes**

- Updated documentation for the `OnBackStackChangedListener` APIs to indicate when they are called and how they should be used. ([I0bfd9](https://android-review.googlesource.com/#/q/I0bfd940eea207c7322bce866e8fc585458ec7a85))

**Dependency update**

- Fragment now depends on [Profile Installer 1.3.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.1).

## Version 1.7

### Version 1.7.1

May 14, 2024

`androidx.fragment:fragment-*:1.7.1` is released. Version 1.7.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/88073d6f9c7c7dc2fc11e9ef53a94e12e4ad1495..291ef1e90f03947a872833589ef6e32ba19e9103/fragment).

**Bug Fixes**

- Predictive back will now only run for transactions in which all of the fragments have either a Animator or a Seekable Androidx Transition. This fixes an issue where canceling a partially seekable transaction would cause a blank screen. ([I43037](https://android-review.googlesource.com/#/q/I4303795b1cb4f7e58cd4f8efe0baa53d64a51dd8), [b/339169168](https://issuetracker.google.com/issues/339169168))

### Version 1.7.0

May 1, 2024

`androidx.fragment:fragment-*:1.7.0` is released. Version 1.7.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7c8070cb8775c270c1b0f3b4232c701cec631be4..88073d6f9c7c7dc2fc11e9ef53a94e12e4ad1495/fragment).

**Predictive Back Gesture Support**

- Fragments now provide support for Predictive in-app back when using `Animator` or when using [AndroidX Transition 1.5.0](https://developer.android.com/jetpack/androidx/releases/transition#1.5.0). This allows users to use the back gesture to see the previous fragment by seeking your Animator/Transition before deciding to either commit the transaction via completing the gesture or canceling.

| Transition System | XML Resource | Supports Predictive Back |
|---|---|---|
| [`Animation`](https://developer.android.com/reference/android/view/animation/Animation) | `R.anim` | No |
| [`Animator`](https://developer.android.com/reference/android/animation/Animator) | `R.animator` | Yes |
| Framework [`Transition`](https://developer.android.com/reference/android/transition/Transition) | `R.transition` | No |
| AndroidX [`Transition`](https://developer.android.com/reference/androidx/transition/Transition) with [Transition 1.4.1](https://developer.android.com/jetpack/androidx/releases/transition#1.4.1) or less | `R.transition` | No |
| AndroidX [`Transition`](https://developer.android.com/reference/androidx/transition/Transition) with [Transition 1.5.0](https://developer.android.com/jetpack/androidx/releases/transition#1.5.0) | `R.transition` | Yes |

If you see any issues with Predictive Back support in Fragments after you've [opted into the predictive back gesture](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#opt-predictive), please [file an issue against Fragment](https://issuetracker.google.com/issues/new?component=460964) with a sample project that reproduces your issue. You can disable predictive back by using `FragmentManager.enabledPredictiveBack(false)` in the `onCreate()` of your Activity.

`FragmentManager.OnBackStackChangedListener()` now provides the `onBackStackChangeProgressed()` and `onBackStackChangeCancelled()` for receiving predictive back progress and canceled events respectively.

**Fragment Compose Artifact**

A new `fragment-compose` artifact has been created that focuses on supporting apps that are in the process of moving from a Fragment based architecture to a fully Compose based architecture.

The first feature available in this new artifact is a `content` extension method on `Fragment` that seeks to make it easier to use Compose for the UI of an individual Fragment by creating a `ComposeView` for you and setting the correct `ViewCompositionStrategy`.

      class ExampleFragment : Fragment() {

          override fun onCreateView(
              inflater: LayoutInflater,
              container: ViewGroup?,
              savedInstanceState: Bundle?
          ) = content {
              // Write your @Composable content here
              val viewModel: ExampleViewModel = viewModel()

              // or extract it into a separate, testable method
              ExampleComposable(viewModel)
          }
      }

### Version 1.7.0-rc02

April 17, 2024

`androidx.fragment:fragment-*:1.7.0-rc02` is released. Version 1.7.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bad4645b145a9dff21edd855fd83e097a1a5bcb3..7c8070cb8775c270c1b0f3b4232c701cec631be4/fragment).

**Bug Fixes**

- Added logs to indicate why setting a `sharedElement` without any other transitions will fail to run. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48ef375eb1c498bc13da82d5d8355be58ba0ff))
- Fixed a bug where if a non-seekable shared element was added to a transactions where all other transitions were seekable, there would be a crash. Now the transaction will correctly be considered non-seekable. ([I18ccd](https://android-review.googlesource.com/#/q/I18ccdbc4f7226f265106435945f8ee4039dc475b))

### Version 1.7.0-rc01

April 3, 2024

`androidx.fragment:fragment-*:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..bad4645b145a9dff21edd855fd83e097a1a5bcb3/fragment).

**Dependency update**

- Fragment now depends on [Profile Installer 1.3.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.1).

### Version 1.7.0-beta01

March 20, 2024

`androidx.fragment:fragment-*:1.7.0-beta01` is released. Version 1.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..a57d7d17753695012b58c9ce7ad55a8d39157e62/fragment).

**API Changes**

- `FragmentHostCallback` is now written in Kotlin so that the nullability of the generic type of the Host matches the nullability of the return type of `onGetHost()`. ([I40af5](https://android-review.googlesource.com/#/q/I40af54eac4bb30c0b5e16d55626ef8ce9b033ebb))

**Bug Fixes**

- Fixed an issue where when committing a Predictive Back gesture on a fragment that is not in a container, that fragment would never be destroyed. The Fragment will now be immediately moved to the final state. ([Ida0d9](https://android-review.googlesource.com/#/q/Ida0d901038b60ae42e42942fb16342e443247573))
- Fixed an issue in Fragments where interrupting incoming transitions with a Predictive back gesture would destroy the entering view, and leave a blank screen. ([Id3f22](https://android-review.googlesource.com/#/q/Id3f228dd5f53742c68e6cb16b752022e18e00ec9), [b/319531491](https://issuetracker.google.com/issues/319531491))

### Version 1.7.0-alpha10

February 7, 2024

`androidx.fragment:fragment-*:1.7.0-alpha10` is released. [Version 1.7.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/78ed9a7c8aebd7f55c3219688444fe02ed7798ad..ca2a8cf8da3a3502fccc593974f8085653e38261/fragment)

**Bug Fixes**

- Fixed the known issue in the previous Fragment release where using Fragment's Predictive Back support for `Animator` or AndroidX Transition, Fragments would throw a `NullPointerException` from `handleOnBackProgressed` if no `FragmentManager.OnBackStackChangedListener` has ever been added via [`addOnBackStackChangedListener`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#addOnBackStackChangedListener(androidx.fragment.app.FragmentManager.OnBackStackChangedListener)). ([I7c835](https://android-review.googlesource.com/#/q/I7c835eb5ca4632bc3a3f68a2c1fe70d0e194b8d1))

### Version 1.7.0-alpha09

January 24, 2024

`androidx.fragment:fragment-*:1.7.0-alpha09` is released. [Version 1.7.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..06772614ed2238bb66df7df4d1e239ad0564ba1a/fragment)

**Fragment Compose Artifact**

A new `fragment-compose` artifact has been created that focuses on supporting apps that are in the process of moving from a Fragment based architecture to a fully Compose based architecture.

The first feature available in this new artifact is a `content` extension method on `Fragment` that seeks to make it easier to use Compose for the UI of an individual Fragment by creating a `ComposeView` for you and setting the correct `ViewCompositionStrategy`. ([561cb7](https://android.googlesource.com/platform/frameworks/support/+/561cb75bdf7e971f0ba2dec3cdc3286e1b415ecf), [b/258046948](https://issuetracker.google.com/258046948))

    class ExampleFragment : Fragment() {

        override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
        ) = content {
            // Write your @Composable content here
            val viewModel: ExampleViewModel = viewModel()

            // or extract it into a separate, testable method
            ExampleComposable(viewModel)
        }
    }

**New Features**

- `FragmentManager.OnBackStackChangedListener()` now provides the `onBackStackChangeProgressed()` and `onBackStackChangeCancelled()` for receiving predictive back progress and canceled events respectively. ([214b87](https://android.googlesource.com/platform%2Fframeworks%2Fsupport/+/214b87117035d255d195dc300e95f4f2f5409711))

**Known Issue**

- When using Fragment's Predictive Back support for `Animator` or AndroidX Transition, Fragments will throw a `NullPointerException` from `handleOnBackProgressed` if no `FragmentManager.OnBackStackChangedListener` has ever been added via [`addOnBackStackChangedListener`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#addOnBackStackChangedListener(androidx.fragment.app.FragmentManager.OnBackStackChangedListener)). Manually adding a listener will work around the crash. A fix will be available for this in the next release of Fragments.

### Version 1.7.0-alpha08

January 10, 2024

`androidx.fragment:fragment-*:1.7.0-alpha08` is released. [Version 1.7.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/fragment)

**Clean up**

- Removed workaround for Transition library that has been fixed in [Transition `1.5.0-alpha06`](https://developer.android.com/jetpack/releases/transition#1.5.0-alpha06). ([I04356](https://android-review.googlesource.com/#/q/I04356cee5dcda7c2da3054e7b2b44cc16dbc357d))

### Version 1.7.0-alpha07

November 29, 2023

`androidx.fragment:fragment-*:1.7.0-alpha07` is released. [Version 1.7.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e63042bab069a262f0e762d23f5a18152f3bf12a..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/fragment)

**Bug Fixes**

- Fixed a `NullPointerException` caused by setting a shared element transition and failing to set an enter/exitTransition as well. ([I8472b](https://android-review.googlesource.com/#/q/I8472b865cf93d1d3463f73942c460263f746fef5))
- From [Fragment `1.6.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.6.2): When the Fragment of a `FragmentContainerView` is inflated, its states such as `FragmentManager`, Host, and id are now accessible in the `onInflate` callback. ([I1e44c](https://android-review.googlesource.com/#/q/I1e44c5dbf5f0e0c55be39489f4c973937f6910cd), [b/307427423](https://issuetracker.google.com/issues/307427423))
- From [Fragment `1.6.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.6.2): When using `clearBackStack` to remove a set of fragments, any nested Fragment's `ViewModel` will now be cleared when the parent fragment's `ViewModels` are cleared. ([I6d83c](https://android-review.googlesource.com/#/q/I6d83cd93421837b213d25d2fdbe5405348cd2637), [b/296173018](https://issuetracker.google.com/issues/296173018))

### Version 1.7.0-alpha06

October 4, 2023

`androidx.fragment:fragment-*:1.7.0-alpha06` is released. [Version 1.7.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..e63042bab069a262f0e762d23f5a18152f3bf12a/fragment)

**Dependency Update**

- Fragments has been updated to depend on the new `animateToStart` API added in [Transition `1.5.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/transition#1.5.0-alpha04).

### Version 1.7.0-alpha05

September 20, 2023

`androidx.fragment:fragment-*:1.7.0-alpha05` is released. [Version 1.7.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/fragment)

**New Features**

- Fragments now provide support for Predictive back when using Androidx Transitions. This allows you to use the back gesture to seek to the previous fragment with your custom Androidx Transition before deciding to either commit or cancel the transaction via the completed gesture. You must depend on the [Transition `1.5.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/transition#1.5.0-alpha03) release to enable this feature. ([Ib49b4](https://android-review.googlesource.com/#/q/Ib49b455d0a00d38203de7616fb2be05a3677a548), [b/285175724](https://issuetracker.google.com/issues/285175724))

**Known Issues**

- There is currently an issue where after you cancel a back gesture with a transition once, the next time you start the back gesture it will fail to run the transition, causing a blank screen. This could be caused by an issue in the Transition library. ([b/300157785](https://issuetracker.google.com/300157785)). If you see this issue, please [file an issue against Fragment](https://issuetracker.google.com/issues/new?component=460964) with a sample project that reproduces your issue. You can disable predictive back by using `FragmentManager.enabledPredictiveBack(false)` in the `onCreate()` of your Activity.

### Version 1.7.0-alpha04

September 6, 2023

`androidx.fragment:fragment-*:1.7.0-alpha04` is released. [Version 1.7.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/fragment)

**Bug Fixes**

- Fixed an issue when canceling a predictive back gesture where fragments failed to make it to the correct Lifecycle state. ([I7cffe](https://android-review.googlesource.com/#/q/I7cffe7994cb032c14bec01eac3c4b9dd8c8fbf40), [b/297379023](https://issuetracker.google.com/issues/297379023))
- Fixed a regressions where Animations were allowed to run with Transitions. ([I59f36](https://android-review.googlesource.com/#/q/I59f36ad415c506f20a5cadbd82e209d6ff98dc37))
- Fixed an issue when using Predictive Back with fragments where attempting to go back twice in quick succession on the second to last fragment on the back stack would cause a crash. ([Ifa1a4](https://android-review.googlesource.com/#/q/Ifa1a4c4f7982c76d76094c489ffb39542281af71))

### Version 1.7.0-alpha03

August 23, 2023

`androidx.fragment:fragment-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8f3937053b6b5e938d7576851bef39c829b017ee..3315f1ef094c312203fe26841287902916fbedf5/fragment)

**Bug Fixes**

- Fixed an issue with Fragments when using predictive back that caused the first fragment in the fragment manager's back stack to be skipped and the Activity to finish when using system back via 3 button navigation or the predictive back gesture. ([I0664b](https://android-review.googlesource.com/#/q/I0664b44dd7f6dc49bafb932e3ae47f1aba483fd6), [b/295231788](https://issuetracker.google.com/issues/295231788))

### Version 1.7.0-alpha02

August 9, 2023

`androidx.fragment:fragment-*:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95657d008c8886de1770adf1d52e01e6e952b5b0..5d7dd999525725bd038a00ca4e89e0fef624a6da/fragment)

**Bug Fixes**

- When using Fragments with Predictive Back Gestures from API 34, if you are using a transition system that does not support seeking (`Animations`, `Transitions`) or no transitions at all, Fragments will now wait until the gesture is complete before executing the back action. ([I8100c](https://android-review.googlesource.com/q/2662926+OR+2662927+OR+2663617+OR+2663618+OR+2663620+OR+2679737+OR+2693186+OR+2692848+OR+2692850+OR+2679738+OR+2679739+OR+2679481+OR+2695268))

### Version 1.7.0-alpha01

June 7, 2023

`androidx.fragment:fragment-*:1.7.0-alpha01` is released. This version is developed in an internal branch.
| **Note:** This version will only compile against the Android 14 (Upside Down Cake) Beta 1 SDK or higher.

**New Features**

- Fragments now provide support for Predictive in-app back when using `Animator`. This allows you to use the back gesture to see the previous fragment with your custom Animator before deciding to either commit the transaction via the completed gesture or cancel. You can also disable this new behavior by using the experimental `enablePredictiveBack()`and passing in `false`.

| **Note:** If using the [Navigation Component](https://developer.android.com/guide/navigation), you must upgrade to [Navigation `2.6.0`](https://developer.android.com/jetpack/androidx/releases/navigation#2.6.0) to allow `FragmentManager` to intercept the system back gesture and run the Predictive Back animation.

## Version 1.6

### Version 1.6.2

November 1, 2023

`androidx.fragment:fragment-*:1.6.2` is released. [Version 1.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2c3ed1b7130ae685522386d109f42c2030276ec6..447211941f6898816452f8b591a9f5a3fa3816f8/fragment)

**Bug Fixes**

- When the Fragment of a `FragmentContainerView` is inflated, its states such as `FragmentManager`, Host, and id are now accessible in the `onInflate` callback. ([I1e44c](https://android-review.googlesource.com/#/q/I1e44c5dbf5f0e0c55be39489f4c973937f6910cd), [b/307427423](https://issuetracker.google.com/issues/307427423))
- When using `clearBackStack` to remove a set of fragments, any nested Fragment's `ViewModel` will now be cleared when the parent fragment's `ViewModels` are cleared. ([I6d83c](https://android-review.googlesource.com/#/q/I6d83cd93421837b213d25d2fdbe5405348cd2637), [b/296173018](https://issuetracker.google.com/issues/296173018))

### Version 1.6.1

July 26, 2023

`androidx.fragment:fragment-*:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d0a1cc9311a4f32d38f50c677b3e71d5c971697..2c3ed1b7130ae685522386d109f42c2030276ec6/fragment)

**Bug Fixes**

- Fixed an issue where the saved state stored when the activity was stopped but not destroyed would be incorrectly cached even after the fragment instance was moved back to the `RESUMED` state. This would cause that cached state to be reused if that fragment instance was on the back stack when using the multiple back stacks API to save and restore that fragment. ([I71288](https://android-review.googlesource.com/#/q/I712884633ae73e0784ba0a7fe50bb5a1046e2275), [b/246289075](https://issuetracker.google.com/issues/246289075))

**Dependency Update**

- Fragment now depends on [Activity 1.7.2](https://developer.android.com/jetpack/androidx/releases/activity#1.7.2). This fixes an issue where Kotlin users could not extend `ComponentDialog` without an explicit dependency on Activity. ([b/287509323](https://issuetracker.google.com/287509323))

### Version 1.6.0

June 7, 2023

`androidx.fragment:fragment-*:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/76caddf4220f27dd21aa2da24a43b83340575542..3d0a1cc9311a4f32d38f50c677b3e71d5c971697/fragment)

**Important changes since 1.5.0**

- The saved state of `Fragment`s has been split entirely between private library state (custom `Parcelable` classes) and state provided by the developer, which is now always stored in a `Bundle` that allows determining exactly where a fragment's state is originating.
- The `FragmentManager.OnBackStackChangedListener` interface has been expanded with two additional callbacks of `onBackStackChangeStarted` and `onBackStackChangeCommitted` that are called with each `Fragment` right before they are added/removed from the fragment back stack and right after the transaction is committed, respectively.
- `FragmentStrictMode` added a new `WrongNestedHierarchyViolation` that detects when a child fragment is nested within it's parent's View hierarchy, but not added to the parent's `childFragmentManager`.
- The `Fragment` and `FragmentManager` APIs that take an `Intent` or `IntentSender` are now properly annotated with `@NonNull` to prevent passing in a null value as a null value would always immediately crash the respective android framework APIs these methods call into.
- `DialogFragment` now provides access to underlying `ComponentDialog` via the `requireComponentDialog()` API.
- Fragment now depends on [Lifecycle `2.6.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.1).
- Fragment now depends on [SavedState `1.2.1`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.2.1).
- Fragment now depends on [ProfileInstaller `1.3.0`](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.0).
- The `fragment-testing-manifest` artifact separates out the manifest entries from the rest of the fragment-testing components. This means you can do the following:

      debugImplementation("androidx.fragment:fragment-testing-manifest:X.Y.Z")
      androidTestImplementation("androidx.fragment:fragment-testing:X.Y.Z")

  This avoids conflicts due to version skew between `fragment-testing` and `androidx.test`

### Version 1.6.0-rc01

May 10, 2023

`androidx.fragment:fragment-*:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..76caddf4220f27dd21aa2da24a43b83340575542/fragment)

**Bug Fixes**

- Fixed as issue causing `ActivityResult`s to be sent with the incorrect request code when multiple `startActivityForResult` requests have been made consecutively. ([If0b9d](https://android-review.googlesource.com/#/q/If0b9da0f226144df6c9ce0ef76642cf47184e63c), [b/249519359](https://issuetracker.google.com/issues/249519359))
- Fixed an issue where the `onBackStackChangeListener` callbacks were being dispatched for transactions that did not actually change the back stack if they were mixed in with transactions that do. ([I0eb5c](https://android-review.googlesource.com/#/q/I0eb5c9622f2984232ac106bb975ba72ae9b2435f), [b/279306628](https://issuetracker.google.com/issues/279306628))

### Version 1.6.0-beta01

April 19, 2023

`androidx.fragment:fragment-*:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/fragment)

**Bug Fixes**

- Using `postponeEnterTransition` with a timeout and then replacing the postponed fragment no longer results in leaking the postponed fragment. ([I2ec7d](https://android-review.googlesource.com/#/q/I2ec7d50c9a08be4902dcc3cce4615bc1e19ed47d), [b/276375110](https://issuetracker.google.com/issues/276375110))
- The new `onBackStackChangeStarted` and `onBackStackChangeCommitted` callbacks will now only dispatch a fragment a single time, even if multiple transactions contain the same fragment. ([Ic6b69](https://android-review.googlesource.com/#/q/Ic6b692881ce091c4e73153f60692fe463fb405ca))

### Version 1.6.0-alpha09

April 5, 2023

`androidx.fragment:fragment-*:1.6.0-alpha09` is released. [Version 1.6.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/fragment)

**API Changes**

- `DialogFragment` now provides access to underlying `ComponentDialog` via the `requireComponentDialog()` API. ([I022e3](https://android-review.googlesource.com/#/q/I022e393bb76c0b1b8d4691661662ee59417b5d85), [b/234274777](https://issuetracker.google.com/issues/234274777))
- The fragment `commitNow()`, `executePendingTransactions()`, and `popBackStackImmediate()` APIs have been annotated with `@MainThread` meaning they will now all throw build errors when they are not called from the main thread instead of waiting to fail at runtime. ([Ic9665](https://android-review.googlesource.com/#/q/Ic966543935dd77a4c149cfc4b796bd912c558fb2), [b/236538905](https://issuetracker.google.com/issues/236538905))

**Bug Fixes**

- Fixed a bug in `FragmentManager` where saving and restoring in the same frame could cause a crash. ([Ib36af](https://android-review.googlesource.com/#/q/Ib36aff4a7263e10d7d795b4d8dbd6431d2552e5c), [b/246519668](https://issuetracker.google.com/issues/246519668))
- `OnBackStackChangedListener` `onBackStackChangeStarted` and `onBackStackChangeCommitted` callbacks now only execute when the `FragmentManager` back stack is changed. ([I66055](https://android-review.googlesource.com/#/q/I66055ea52220756aeda717e5208346dcaa611258), [b/274788957](https://issuetracker.google.com/issues/274788957))

### Version 1.6.0-alpha08

March 22, 2023

`androidx.fragment:fragment-*:1.6.0-alpha08` is released. [Version 1.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..5e7d256f82fbafb6d059ab7b18fddd87c7531553/fragment)

**Behavior Change**

- The timing of the `OnBackStackChangedListener.onBackStackChangeCommited` callback has been adjusted to execute before fragment operations are executed. This ensures that the callback will never be passed a fragment that is detached. ([I66a76](https://android-review.googlesource.com/#/q/I66a76810202a9b44b9d4bdffa03be5ed2b28a1e3), [b/273568280](https://issuetracker.google.com/issues/273568280))

**Bug Fixes**

- From [Fragment `1.5.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.6): Fixed an issue where calling `clearFragmentResultListener` inside a `setFragmentResultListener` wouldn't work if the `Lifecycle` was already `STARTED` and a result was already available. ([If7458](https://android-review.googlesource.com/#/q/If7458be3c43ece5a7ee3b1fe5b89bef2cf8b6131))

**Dependency Updates**

- Fragment now depends on [Lifecycle `2.6.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.1). ([586fe7](https://android.googlesource.com/platform/frameworks/support/+/586fe7d84e657d9bbc6d3cb3cbb8954f715df557))
- Fragment now depends on [SavedState `1.2.1`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.2.1). ([078e4e](https://android.googlesource.com/platform/frameworks/support/+/078e4ef4d6b3475ed3a453ea7ba0d03e6bdc02c3))
- Fragment now depends on [ProfileInstaller `1.3.0`](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.0). ([3fc05b](https://android.googlesource.com/platform/frameworks/support/+/3fc05b928c858af7bb318cc5f36a97715c6663a8))

### Version 1.6.0-alpha07

March 8, 2023

`androidx.fragment:fragment-*:1.6.0-alpha07` is released. [Version 1.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/fragment)

**Bug Fixes**

- From [Fragment `1.5.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.6): Fixed an issue where the removal of any Fragment, whether it had added Menu items or not, would invalidate the activity's menu. ([50f098](https://android.googlesource.com/platform/frameworks/support/+/50f098644adc703ae218b0b7e999629f516a0241), [b/244336571](https://issuetracker.google.com/244336571))

### Version 1.6.0-alpha06

February 22, 2023

`androidx.fragment:fragment-*:1.6.0-alpha06` is released. [Version 1.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..87533b4ff06971ed59028936cd9b6da988cd4522/fragment)

**Behavior change**

- The new `onBackStackChangedStarted` callback on `FragmentManager`'s `onBackStackChangedListener` will now be executed before fragments begin to move to their target states. ([I34726](https://android-review.googlesource.com/#/q/I34726bb6bd8bb7e293b2eb605e961e54f313c8bb))

### Version 1.6.0-alpha05

February 8, 2023

`androidx.fragment:fragment-*:1.6.0-alpha05` is released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..7d3ac1ab1206c01fae3ebb500b5b942636070155/fragment)

**New Features**

- The `FragmentManager.OnBackStackChagnedListener` interface now offers two additional callbacks, `onBackStackChangeStarted` and `onBackStackChangeCommitted`, that allow for additional information and control when back stack changes occur in the `FragmentManager`. ([Ib7ce5](https://android-review.googlesource.com/#/q/Ib7ce5958d86ea1701f78e519ff607aa60a439def), [b/238686802](https://issuetracker.google.com/issues/238686802))

**API Changes**

- The `Fragment` and `FragmentManager` APIs that take an `Intent` or `IntentSender` are now properly annotated with `@NonNull` to prevent passing in a null value as a null value would always immediately crash the respective Android framework APIs these methods call into. ([I06fd4](https://android-review.googlesource.com/#/q/I06fd4eed31b985d7b9160430efb2f05d1c451dc1))

### Version 1.6.0-alpha04

December 7, 2022

`androidx.fragment:fragment-*:1.6.0-alpha04` is released. [Version 1.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7/fragment)

**New Features**

- `FragmentStrictMode` added a new `WrongNestedHierarchyViolation` that detects when a child fragment is nested within it's parent's View hierarchy, but not added to the parent's `childFragmentManager`. ([I72521](https://android-review.googlesource.com/#/q/I725210f957b9be5875f7c0eadaaa992deda6614a), [b/249299268](https://issuetracker.google.com/issues/249299268))

**Behavior Changes**

- Fragments now restore their `SavedStateRegistry` state before `onAttach()`, ensuring that it is available from all upward lifecycle methods. ([I1e2b1](https://android-review.googlesource.com/#/q/I1e2b1b1e65900219956c6d9c0d68c175012586b8))

**API Changes**

- The `fragment-testing-manifest` artifact separates out the manifest entries from the rest of the fragment-testing components. This means you can do the following:

    debugImplementation("androidx.fragment:fragment-testing-manifest:X.Y.Z")
    androidTestImplementation("androidx.fragment:fragment-testing:X.Y.Z")

This avoids conflicts due to version skew between `fragment-testing` and `androidx.test`.([I8e534](https://android-review.googlesource.com/#/q/I8e534e2fcab467a43944b6ab4821dc34c1c02cef), [b/128612536](https://issuetracker.google.com/issues/128612536))

**Bug Fixes**

- From [Fragment `1.5.5`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.5): Fragments will no longer incorrectly save the `ViewModel` state as part of the view registry saved state. ([I10d2b](https://android-review.googlesource.com/#/q/I10d2b5363d0abe967e92ad90a578d3bf88a2ca3b), [b/253546214](https://issuetracker.google.com/issues/253546214))

### Version 1.6.0-alpha03

October 5, 2022

`androidx.fragment:fragment:1.6.0-alpha03`, `androidx.fragment:fragment-ktx:1.6.0-alpha03`, and `androidx.fragment:fragment-testing:1.6.0-alpha03` are released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/fragment)

**API Changes**

- Classes extending `DialogFragment` will now be required to call super in their `onDismiss()` overrides. ([I14798](https://android-review.googlesource.com/#/q/I147983f443693b1cafbd996cbbacd726e2dd2130), [b/238928865](https://issuetracker.google.com/issues/238928865))

**Bug Fixes**

- Fixed regressions caused by the integration of the new provider callback interfaces (`OnConfigurationChangedProvider`, `OnMultiWindowModeChangedProvider`, `OnTrimMemoryProvider`, `OnPictureInPictureModeChangedProvider`) to ensure that fragments always get the proper callbacks. ([I9b380](https://android-review.googlesource.com/#/q/I9b380cd13d0fadf4a59be537d22023019f1b7cb4),[I34581](https://android-review.googlesource.com/#/q/I34581e67bb3a81c7a7e162c3e47e51359896a628), ([I8dfe6](https://android-review.googlesource.com/#/q/I8dfe68f7b8700f0c1d3b13a3d5b826fc924b7452), [b/242570955](https://issuetracker.google.com/issues/242570955)),[If9d6b](https://android-review.googlesource.com/#/q/If9d6bc0c4a942287b9e493b073dcb206d881df6d),[Id0096](https://android-review.googlesource.com/#/q/Id0096df0c7c3aed66a832e0c05e81539e1a9ca26),[I690b3](https://android-review.googlesource.com/#/q/I690b3596b4f44a69c4f0b429535d609db94e5a79),[I2cba2](https://android-review.googlesource.com/#/q/I2cba24e9657afa65c08a53cc80756ecd02b9f1e2))

### Version 1.6.0-alpha02

August 24, 2022

`androidx.fragment:fragment:1.6.0-alpha02`, `androidx.fragment:fragment-ktx:1.6.0-alpha02`, and `androidx.fragment:fragment-testing:1.6.0-alpha02` are released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..dd1e45e8550560087f6447a34a9145048b5766f4/fragment)

**Bug Fixes**

- From [Fragment `1.5.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.2): Fixed an issue where executing a `popBackStack()` and a `replace()` transaction at the same time could cause exiting fragments to run the wrong `Animation`/`Animator`. ([Ib1c07](https://android-review.googlesource.com/#/q/Ib1c07bd0e05c0c1a3d785e29456bad9afb183e2d), [b/214835303](https://issuetracker.google.com/issues/214835303))

### Version 1.6.0-alpha01

July 27, 2022

`androidx.fragment:fragment:1.6.0-alpha01`, `androidx.fragment:fragment-ktx:1.6.0-alpha01`, and `androidx.fragment:fragment-testing:1.6.0-alpha01` are released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d5e5f4d57931a05bfd2dc75c09b3537e4d3ec976..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/fragment)

**Behavior Changes**

- The saved state of `Fragment`s has been split entirely between private library state (custom `Parcelable` classes) and state provided by the developer, which is now always stored in a `Bundle` that allows determining exactly where a fragment's state is originating. ([b/207158202](https://issuetracker.google.com/issues/207158202))

**Bug Fixes**

- From [Fragment `1.5.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.1): Fix a regression in the `DialogFragmentCallbacksDetector` where using the lint version bundled with AGP 7.4 would cause lint to crash. ([b/237567009](https://issuetracker.google.com/237567009))

**Dependency update**

- From [Fragment `1.5.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.1): The Fragment library now depends on the [Lifecycle `2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1). ([Id204c](https://android-review.googlesource.com/#/q/Id204c8273a64607e7ee83a452a45a566f5fe0fac))
- From [Fragment `1.5.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.1): The Fragment library now depends on [Activity `1.5.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.1). ([I10f07](https://android-review.googlesource.com/#/q/I10f076fcf8083ff61904604f17a65377b0c7e6b3))

## Version 1.5

### Version 1.5.7

April 19, 2023

`androidx.fragment:fragment:1.5.7`, `androidx.fragment:fragment-ktx:1.5.7`, and `androidx.fragment:fragment-testing:1.5.7` are released. [Version 1.5.7 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/29aa61b8de7b6fc4c40d7853fea944ae84553b19..264a7d28a22c73b74b7b8527075eedd989e8d521/fragment)

**Bug Fixes**

- Using `postponeEnterTransition` with a timeout and then replacing the postponed fragment no longer results in leaking the postponed fragment. ([I2ec7d](https://android-review.googlesource.com/#/q/I2ec7d50c9a08be4902dcc3cce4615bc1e19ed47d), [b/276375110](https://issuetracker.google.com/issues/276375110))

### Version 1.5.6

March 22, 2023

`androidx.fragment:fragment:1.5.6`, `androidx.fragment:fragment-ktx:1.5.6`, and `androidx.fragment:fragment-testing:1.5.6` are released. [Version 1.5.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/81d78b98f8807fb46569ed4c765315088ae8ac7e..29aa61b8de7b6fc4c40d7853fea944ae84553b19/fragment)

**Bug Fixes**

- Fixed an issue where the removal of any Fragment, whether it had added Menu items or not, would invalidate the activity's menu. ([50f098](https://android.googlesource.com/platform/frameworks/support/+/50f098644adc703ae218b0b7e999629f516a0241), [b/244336571](https://issuetracker.google.com/244336571))
- Fixed an issue where calling `clearFragmentResultListener` inside a `setFragmentResultListener` wouldn't work if the `Lifecycle` was already `STARTED` and a result was already available. ([If7458](https://android-review.googlesource.com/#/q/If7458be3c43ece5a7ee3b1fe5b89bef2cf8b6131))

### Version 1.5.5

December 7, 2022

`androidx.fragment:fragment:1.5.5`, `androidx.fragment:fragment-ktx:1.5.5`, and `androidx.fragment:fragment-testing:1.5.5` are released. [Version 1.5.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/16c70a04b803a84c147e758bfce0e6d2051f2fa2..81d78b98f8807fb46569ed4c765315088ae8ac7e/fragment)

**Bug Fixes**

- Fragments will no longer incorrectly save the `ViewModel` state as part of the view registry saved state. ([I10d2b](https://android-review.googlesource.com/#/q/I10d2b5363d0abe967e92ad90a578d3bf88a2ca3b), [b/253546214](https://issuetracker.google.com/issues/253546214))

### Version 1.5.4

October 24, 2022

`androidx.fragment:fragment:1.5.4`, `androidx.fragment:fragment-ktx:1.5.4`, and `androidx.fragment:fragment-testing:1.5.4` are released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a971aa42c5da6841733fedb8cba861c3ad729109..16c70a04b803a84c147e758bfce0e6d2051f2fa2/fragment)

**Bug Fixes**

- Fixed an error where using a custom `FragmentController` with a host that does not implement a provider callback interface (`OnConfigurationChangedProvider`, `OnMultiWindowModeChangedProvider`, `OnTrimMemoryProvider`, `OnPictureInPictureModeChangedProvider`) and calling its deprecated dispatch function would fail to dispatch to child fragments. ([I9b380](https://android-review.googlesource.com/#/q/I9b380cd13d0fadf4a59be537d22023019f1b7cb4))

### Version 1.5.3

September 21, 2022

`androidx.fragment:fragment:1.5.3`, `androidx.fragment:fragment-ktx:1.5.3`, and `androidx.fragment:fragment-testing:1.5.3` are released. [Version 1.5.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/11370054495ad6e38f7904b59d0889da5235b1ce..a971aa42c5da6841733fedb8cba861c3ad729109/fragment)

**Bug Fixes**

- Fixed an error that caused fragments on the back stack to get `onMultiWindowModeChanged()`, `onPictureInPictureModeChanged()`, `onLowMemory()`, and `onConfigurationChanged()` callbacks. ([I34581](https://android-review.googlesource.com/#/q/I34581e67bb3a81c7a7e162c3e47e51359896a628), [I8dfe6](https://android-review.googlesource.com/#/q/I8dfe68f7b8700f0c1d3b13a3d5b826fc924b7452), [b/242570955](https://issuetracker.google.com/issues/242570955))
- Nested child fragments will no longer receive multiple `onMultiWindowModeChanged()`, `onPictureInPictureModeChanged()`, `onLowMemory()`, or `onConfigurationChanged()` callbacks. ([I690b3](https://android-review.googlesource.com/#/q/I690b3596b4f44a69c4f0b429535d609db94e5a79), [Id0096](https://android-review.googlesource.com/#/q/Id0096df0c7c3aed66a832e0c05e81539e1a9ca26), [If9d6b](https://android-review.googlesource.com/#/q/If9d6bc0c4a942287b9e493b073dcb206d881df6d), [I2cba2](https://android-review.googlesource.com/#/q/I2cba24e9657afa65c08a53cc80756ecd02b9f1e2))

### Version 1.5.2

August 10, 2022

`androidx.fragment:fragment:1.5.2`, `androidx.fragment:fragment-ktx:1.5.2`, and `androidx.fragment:fragment-testing:1.5.2` are released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ef17c40272c8b902ee75158214703bea97a7a298..11370054495ad6e38f7904b59d0889da5235b1ce/fragment)

**Bug Fixes**

- Fixed an issue where executing a `popBackStack()` and a `replace()` transaction at the same time could cause exiting fragments to run the wrong `Animation`/`Animator`. ([Ib1c07](https://android-review.googlesource.com/#/q/Ib1c07bd0e05c0c1a3d785e29456bad9afb183e2d), [b/214835303](https://issuetracker.google.com/issues/214835303))

### Version 1.5.1

July 27, 2022

`androidx.fragment:fragment:1.5.1`, `androidx.fragment:fragment-ktx:1.5.1`, and `androidx.fragment:fragment-testing:1.5.1` are released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d5e5f4d57931a05bfd2dc75c09b3537e4d3ec976..ef17c40272c8b902ee75158214703bea97a7a298/fragment)

**Bug Fixes**

- Fix a regression in the `DialogFragmentCallbacksDetector` where using the lint version bundled with AGP 7.4 would cause lint to crash. ([b/237567009](https://issuetracker.google.com/237567009))

**Dependency update**

- The Fragment library now depends on the [Lifecycle `2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1). ([Id204c](https://android-review.googlesource.com/#/q/Id204c8273a64607e7ee83a452a45a566f5fe0fac))
- The Fragment library now depends on [Activity `1.5.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.1). ([I10f07](https://android-review.googlesource.com/#/q/I10f076fcf8083ff61904604f17a65377b0c7e6b3))

### Version 1.5.0

June 29, 2022

`androidx.fragment:fragment:1.5.0`, `androidx.fragment:fragment-ktx:1.5.0`, and `androidx.fragment:fragment-testing:1.5.0` are released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/218ccafb21e861418ebb20936cad034ed012fb70..d5e5f4d57931a05bfd2dc75c09b3537e4d3ec976/fragment)

**Important changes since 1.4.0**

- **CreationExtras Integration** - `Fragment` now has the ability to provide a stateless `ViewModelProvider.Factory` via [Lifecycle `2.5.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0)'s `CreationExtras`.
- **Component Dialog Integration** - `DialogFragment` now uses `ComponentDialog` via [Activity `1.5.0`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.0) as the default dialog returned by `onCreateDialog()`.
- **Saved Instance State Refactoring** - Fragments have begun to change the way they save their instance state. This is an effort to help clearly identify what state has been saved in the fragment and the source of the state. The current changes include the following:
  - `FragmentManager` now saves its saved instance state into a `Bundle` instead of directly in a custom `Parcelable`.
  - Results set via the [`Fragment Result APIs`](https://developer.android.com/guide/fragments/communicate#fragment-result) that have not yet been delivered are now saved separately from the internal state of the `FragmentManager`.
  - The state associated with each individual fragment is now saved separately from the internal state of the `FragmentManager`, thus allowing you to correlate the amount of saved state associated with an individual fragment with the unique IDs present in the `Fragment` debug logging.

**Other Changes**

- `FragmentStrictMode` now offers the ability for private third-party fragments to bypass specific violation penalties by using `allowViolation()` with the class name.
- The Fragment APIs for providing a menu to your activity's `ActionBar` have been deprecated. The `MenuHost` and `MenuProvider` APIs added in [Activity `1.4.0`](https://developer.android.com/jetpack/androidx/releases/activity#1.4.0) provide a testable, lifecycle aware equivalent API surface that fragments should use.

### Version 1.5.0-rc01

May 11, 2022

`androidx.fragment:fragment:1.5.0-rc01`, `androidx.fragment:fragment-ktx:1.5.0-rc01`, and `androidx.fragment:fragment-testing:1.5.0-rc01` are released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..218ccafb21e861418ebb20936cad034ed012fb70/fragment)

**Saved Instance State Refactoring**

- The state associated with each individual fragment is now saved separately from the internal state of the `FragmentManager`, thus allowing you to correlate the amount of saved state associated with an individual fragment with the unique IDs present in the [Fragment debug logging](https://developer.android.com/guide/fragments/debugging#debug-logging). ([a153e0](https://android-review.googlesource.com/#/q/a153e0dc72acb0eb453499bb14d50fd774c4dd93), [b/207158202](https://issuetracker.google.com/issues/207158202))

### Version 1.5.0-beta01

April 20, 2022

`androidx.fragment:fragment:1.5.0-beta01`, `androidx.fragment:fragment-ktx:1.5.0-beta01`, and `androidx.fragment:fragment-testing:1.5.0-beta01` are released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/fragment)

**API Changes**

- `DialogFragment` has added a new `dismissNow` method that uses `commitNow` for parity with the `showNow` function. Note that this will not make the `Dialog` be dismissed immediately, it will only synchronously update the state of the `FragmentManager`. ([I15c36](https://android-review.googlesource.com/#/q/I15c3618ccbea638e8f2125b5c361cce43721b017), [b/72644830](https://issuetracker.google.com/issues/72644830))

**Saved Instance State Refactoring**

- `FragmentManager` now saves its saved instance state into a `Bundle` instead of directly in a custom `Parcelable`. This is the first step in providing additional transparency into what is actually being saved by Fragments. ([I93807](https://android-review.googlesource.com/#/q/I93807d8bebb127fd24d20dee23fc7813cfa0f6ab), [b/207158202](https://issuetracker.google.com/issues/207158202))
- Results set via the [Fragment Result APIs](https://developer.android.com/guide/fragments/communicate#fragment-result) that have not yet been delivered are now saved separately from the internal state of the `FragmentManager`. This will allow for additional transparency into what results are being saved as part of your saved instance state. ([I6ea12](https://android-review.googlesource.com/#/q/I6ea121b1c4a42408de9af44e6cd12a825ec378d1), [b/207158202](https://issuetracker.google.com/issues/207158202))

### Version 1.5.0-alpha05

April 6, 2022

`androidx.fragment:fragment:1.5.0-alpha05`, `androidx.fragment:fragment-ktx:1.5.0-alpha05`, and `androidx.fragment:fragment-testing:1.5.0-alpha05` are released. [Version 1.5.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/fragment)

**API Changes**

- `Fragment`'s `setHasOptionsMenu()` has been deprecated. To manage menus and their menu items, the new menu APIs should be used instead as per the [Fragment `1.5.0-alpha04` release notes](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0-alpha04). ([I7b4b4](https://android-review.googlesource.com/#/q/I7b4b4dd5cfa1922a7ee0d1d4317a52439e780786), [b/226438239](https://issuetracker.google.com/issues/226438239))

### Version 1.5.0-alpha04

March 23, 2022

`androidx.fragment:fragment:1.5.0-alpha04`, `androidx.fragment:fragment-ktx:1.5.0-alpha04`, and `androidx.fragment:fragment-testing:1.5.0-alpha04` are released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/fragment)

**API Changes**

- The Fragment APIs for providing a menu to your activity's `ActionBar` have been deprecated as they tightly couple your fragment to your activity and are not testable in isolation. The `MenuHost` and `MenuProvider` APIs added in [Activity `1.4.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/activity#1.4.0-alpha01) provide a testable, lifecycle aware equivalent API surface that fragments should use. ([I50a59](https://android-review.googlesource.com/#/q/I50a599c9ee85c085e377f74353db72376dcce19a), [I20758](https://android-review.googlesource.com/#/q/I2075845d3598bf3b2635512918fca04abe2e281a))

**Bug Fixes**

- `SavedStateViewFactory` now supports using `CreationExtras` even when it was initialized with a `SavedStateRegistryOwner`. If extras are provided, the initialized arguments are ignored. ([I6c43b](https://android-review.googlesource.com/#/q/I6c43bfd75888cb4b8bdd610cd07d4962aaba37ea), [b/224844583](https://issuetracker.google.com/issues/224844583))

### Version 1.5.0-alpha03

February 23, 2022

`androidx.fragment:fragment:1.5.0-alpha03`, `androidx.fragment:fragment-ktx:1.5.0-alpha03`, and `androidx.fragment:fragment-testing:1.5.0-alpha03` are released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/fragment)

**API Changes**

- You can now pass `CreationExtras` to the `by viewModels()` and `by activityViewModels()` functions. ([Ibefe7](https://android-review.googlesource.com/#/q/Ibefe7e706d2491ee70070b07755c32c5f99cc57a), [b/217601110](https://issuetracker.google.com/issues/217601110))

**Behavior Changes**

- `DialogFragment` now uses [`ComponentDialog`](https://developer.android.com/reference/kotlin/androidx/activity/ComponentDialog) as the default dialog returned by `onCreateDialog()`. ([If3784](https://android-review.googlesource.com/#/q/If3784bbe3d65184c75dd8f3f8e292aa9257297b1), [b/217618170](https://issuetracker.google.com/issues/217618170))

### Version 1.5.0-alpha02

February 9, 2022

`androidx.fragment:fragment:1.5.0-alpha02`, `androidx.fragment:fragment-ktx:1.5.0-alpha02`, and `androidx.fragment:fragment-testing:1.5.0-alpha02` are released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/fragment)

**New Features**

- `FragmentStrictMode` now offers the ability for private third-party fragments to bypass specific violation penalties by using `allowViolation()` with the class name. ([I8f678](https://android-review.googlesource.com/#/q/I8f67856db22fc99b6d06fde7e0cebb753079cc80))

### Version 1.5.0-alpha01

January 26, 2022

`androidx.fragment:fragment:1.5.0-alpha01`, `androidx.fragment:fragment-ktx:1.5.0-alpha01`, and `androidx.fragment:fragment-testing:1.5.0-alpha01` are released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b776acc2f42697fc8a24ca96f38043a133eee415..9dceceb54300ed028a7e8fc7a3454f270337ffde/fragment)

**New Features**

- `Fragment` now integrates with ViewModel CreationExtras, introduced as part of [Lifecycle `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0-alpha01). ([I3060b](https://android-review.googlesource.com/#/q/I3060ba63bae3019489fc54eb116c3b4c1e50d8a1), [b/207012585](https://issuetracker.google.com/issues/207012585))

**Bug Fixes**

- From [Fragment `1.4.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.4.1): `FragmentContainerView` no longer throws an illegal state exception when view IDs generated from xml have negative values. ([Ic185b](https://android-review.googlesource.com/#/q/Ic185b1efe5b48b616881e51b7b892c0f3bfc8e92), [b/213086140](https://issuetracker.google.com/issues/213086140))
- From [Fragment `1.4.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.4.1): When using a custom `ownerProducer` lambda with the `by viewModels()` lazy function, it will now use the `defaultViewModelProviderFactory` from that owner if a custom `ViewModelProvider.Factory` is not provided instead of always using the fragment's factory. ([I56170](https://android-review.googlesource.com/#/q/I561707e21a66afb0540c941bd5b94f834dc3953c), [b/214106513](https://issuetracker.google.com/issues/214106513))
- Fixed a crash when accessing a `ViewModel`for the very first time from a `registerForActivityResult()` callback of a `Fragment`. ([Iea2b3](https://android-review.googlesource.com/#/q/Iea2b30ca03908798474cac9327c4e06e3d4fd09b))

## Version 1.4

### Version 1.4.1

January 26, 2022

`androidx.fragment:fragment:1.4.1`, `androidx.fragment:fragment-ktx:1.4.1`, and `androidx.fragment:fragment-testing:1.4.1` are released. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b776acc2f42697fc8a24ca96f38043a133eee415..70c414acc064e4d3bfd7d0eafbaff50dd8aac5ce/fragment)

**Bug Fixes**

- `FragmentContainerView` no longer throws an illegal state exception when view IDs generated from xml have negative values. ([Ic185b](https://android-review.googlesource.com/#/q/Ic185b1efe5b48b616881e51b7b892c0f3bfc8e92), [b/213086140](https://issuetracker.google.com/issues/213086140))
- When using a custom `ownerProducer` lambda with the `by viewModels()` lazy function, it will now use the `defaultViewModelProviderFactory` from that owner if a custom `ViewModelProvider.Factory` is not provided instead of always using the fragment's factory. ([I56170](https://android-review.googlesource.com/#/q/I561707e21a66afb0540c941bd5b94f834dc3953c), [b/214106513](https://issuetracker.google.com/issues/214106513))

### Version 1.4.0

November 17, 2021

`androidx.fragment:fragment:1.4.0`, `androidx.fragment:fragment-ktx:1.4.0`, and `androidx.fragment:fragment-testing:1.4.0` are released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/02d119fbee4cdfe60f6b1b1a4ee172a726f26963..b776acc2f42697fc8a24ca96f38043a133eee415/fragment)

**Important changes since 1.3.0**

- The `FragmentStrictMode` APIs provide *runtime* checks that allow you to verify that your app or libraries you depend on are not calling deprecated fragment APIs. When a violation is detected, you can choose to print a log message, trigger your own custom listener, or crash your app. The `FragmentStrictMode.Policy` that controls what checks are enabled and what "penalties" are triggered can be set on a `FragmentManager` via the new `setStrictModePolicy()` method. That policy applies to that `FragmentManager` and transitively to any child fragment managers that do not set their own unique policy. See [StrictMode for fragments](https://developer.android.com/guide/fragments/debugging#strictmode).
- `FragmentContainerView` now provides a `getFragment()` method which returns the fragment that was most recently added to the container. This uses the same logic as `findFragmentById()` with the ID of the `FragmentContainerView`, but allows chaining the call.

      val navController = binding.container.getFragment<NavHostFragment>().navController

- `FragmentScenario` now implements `Closeable`, allowing you to use it with Kotlin's [`use`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/use.html) method or [try-with-resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html).

- Added
  `FragmentTransaction#TRANSIT_FRAGMENT_MATCH_ACTIVITY_{OPEN, CLOSE}`
  to specify whether to enable the standard Activity-transition animation taken from your theme in Fragments transition.

- The experimental API of `FragmentManager.enableNewStateManager(boolean)` has been removed and the [new state manager](https://medium.com/androiddevelopers/fragments-rebuilding-the-internals-61913f8bf48e) is now the only option available.

**Multiple back stacks**

The `FragmentManager` maintains a back stack made up of fragment transactions that used [`addToBackStack()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#addToBackStack(java.lang.String)). This allows you to pop those transactions and return to the previous state, using the mechanisms for [Saving state with fragments](https://developer.android.com/guide/fragments/saving-state) to allow your fragments to restore their state appropriately.

This release expands on these mechanisms by providing three new `FragmentManager` APIs: `saveBackStack(String name)`, `restoreBackStack(String name)`, and `clearBackStack(String name)`. These APIs use the same `name` as `addToBackStack()` to save the state of the `FragmentTransaction` and the state of every fragment that was added in those transactions and allow you to later restore those transactions and their fragments with their state in tact. This allows you to effectively 'swap' between multiple back stacks by saving the current back stack and restoring a saved back stack.

`saveBackStack()` operates similarly to [`popBackStack()`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#popBackStack(java.lang.String,%20int)) in that it is asynchronous and results in all the fragment transactions back to that specific name to be reversed ('popped') and any added fragments to be destroyed and removed, but it differs in a few important ways:

- `saveBackStack()` is always inclusive.
- Unlike `popBackStack()` which will pop **all** transactions on the back stack if the specified name is not found on the back stack or if a null name is provided, `saveBackStack()` does nothing if you haven't previously committed a fragment transaction using `addToBackStack()` with that exact, non-null name.
- The state of all fragments added from those transactions is saved. This means that the View state of every fragment is stored, `onSaveInstanceState()` of every fragment is called and that state is restored, and any `ViewModel` instances associated with those fragments are retained (and `onCleared()` is **not** called on them).

The fragment transactions that can be used with `saveBackStack()` must meet certain criteria:

- Every fragment transaction must use [`setReorderingAllowed(true)`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setReorderingAllowed(boolean)) to ensure the transactions can be restored as a single, atomic operation.
- The set of transactions saved must be self-contained (i.e., they must **not** explicitly reference any fragments outside of that set of transactions) to ensure that they can be restored at any later time, no matter what changes have been made to the back stack in the intervening time.
- No fragment that is saved can be a retained fragment or have a retained fragment in their transitive set of child fragments to ensure that the `FragmentManager` does not return any references to saved fragments after the back stack is saved.

Similar to `saveBackStack()`, `restoreBackStack()` and `clearBackStack()`, which would restore a previously saved back stack or clear a previously saved back stack, respectively, both do nothing if you have not previously called `saveBackStack()` with the same name.

For more information, see [Multiple back stacks: A deep dive](https://medium.com/androiddevelopers/multiple-back-stacks-b714d974f134).

### Version 1.4.0-rc01

November 3, 2021

`androidx.fragment:fragment:1.4.0-rc01` released with no changes from Fragment 1.4.0-beta01. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca6054a5e12fcf05ba5e20bf93403afdab093986..02d119fbee4cdfe60f6b1b1a4ee172a726f26963/fragment)

### Version 1.4.0-beta01

October 27, 2021

`androidx.fragment:fragment:1.4.0-beta01`, `androidx.fragment:fragment-ktx:1.4.0-beta01`, and `androidx.fragment:fragment-testing:1.4.0-beta01` are released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..ca6054a5e12fcf05ba5e20bf93403afdab093986/fragment)

**Bug Fixes**

- Parent fragments will now dispatch `onHiddenChanged()` down their entire hierarchy before launching their own callback. ([Iedc20](https://android-review.googlesource.com/#/q/Iedc201ab435cb963e81bc02d203d4d37ff827e01), [b/77504618](https://issuetracker.google.com/issues/77504618))
- The keyboard will now close automatically when going from a fragment with an open keyboard to a fragment with a recycler view. ([I8b842](https://android-review.googlesource.com/#/q/I8b842dd9a421cfbc9189014b802f5e4b6b9c2a47), [b/196852211](https://issuetracker.google.com/issues/196852211))
- `DialogFragment` now uses `setReorderingAllowed(true)` for all transactions it creates when you call `show()`, `showNow()`, or `dismiss()`. ([Ie2c14](https://android-review.googlesource.com/#/q/Ie2c14fb6d11b426ea0b2c26b035a962f08ddc586))
- The extremely long Lint warning of `DetachAndAttachFragmentInSameFragmentTransaction` has been shortened to `DetachAndAttachSameFragment`. ([e9eca3](https://android-review.googlesource.com/#/q/e9eca34ab9edfad6e1b8e9c1a6a26dd26e166998))

### Version 1.4.0-alpha10

September 29, 2021

`androidx.fragment:fragment:1.4.0-alpha10`, `androidx.fragment:fragment-ktx:1.4.0-alpha10`, and `androidx.fragment:fragment-testing:1.4.0-alpha10` are released. [Version 1.4.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/fragment)

**Lint**

- Added the `DetachAndAttachFragmentInSameFragmentTransaction` lint warning for detecting calling both `detach()` and `attach()` on the same `Fragment` in the same `FragmentTransaction` - as these complementary operations cancel each other out when done in the same transaction, they must be split into separate transactions to actually do anything. ([aosp/1832956](https://android-review.googlesource.com/c/platform/frameworks/support/+/1832956/), [b/200867930](https://issuetracker.google.com/issues/200867930))
- Added the `FragmentAddMenuProvider` lint error for correcting usages of the Fragment Lifecycle to the Fragment view Lifecycle when using the `addMenuProvider` API of `MenuHost`. ([aosp/1830457](https://android-review.googlesource.com/c/platform/frameworks/support/+/1830457/), [b/200326272](https://issuetracker.google.com/issues/200326272))

**Documentation Updates**

- The deprecation message for APIs now handled by the [Activity Result APIs](https://developer.android.com/training/basics/intents/result), namely `startActivityForResult`, `startIntentSenderForResult`, `onActivityResult`, `requestPermissions`, and `onRequestPermissionsResult`, have all been expanded with more details. ([cce80f](https://android-review.googlesource.com/#/q/cce80f6e9e1ae0f5b3390b59c5cf1321443ab81f))
- The deprecation message for `onActivityCreated()` for both `Fragment` and `DialogFragment` has all been expanded with more details. ([224db4](https://android-review.googlesource.com/#/q/244db49af2b0fa925892da5860462631d32c114d))

### Version 1.4.0-alpha09

September 15, 2021

`androidx.fragment:fragment:1.4.0-alpha09`, `androidx.fragment:fragment-ktx:1.4.0-alpha09`, and `androidx.fragment:fragment-testing:1.4.0-alpha09` are released. [Version 1.4.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/fragment)

**New Features**

- You can now call `clearBackStack(name)` to clear any state previously saved with `saveBackStack(name)`. ([I70cd7](https://android-review.googlesource.com/#/q/I70cd75a17faffed340424ef0769bd312df9035ae))

**API Changes**

- The `FragmentContainerView` class has been rewritten in Kotlin ensuring that the `getFragment` function will properly respect nullability. ([If694a](https://android-review.googlesource.com/#/q/If694a3b70bf84f03c95d67d20e58485135ab7d86), [b/189629145](https://issuetracker.google.com/issues/189629145))
- FragmentStrictMode is now written in Kotlin ([I11767](https://android-review.googlesource.com/#/q/I117679edc3af067bb0ef901714ace02712c97a40), [b/199183506](https://issuetracker.google.com/issues/199183506))

**Bug Fixes**

- Fixed an issue where the state of a Fragment that was added with `setReorderingAllowed(true)` and then immediately removed before executing pending transactions would not be properly cleaned up. ([I8ccb8](https://android-review.googlesource.com/#/q/I8ccb834a4337dda503e64402dab4aca807d81788))

### Version 1.4.0-alpha08

September 1, 2021

`androidx.fragment:fragment:1.4.0-alpha08`, `androidx.fragment:fragment-ktx:1.4.0-alpha08`, and `androidx.fragment:fragment-testing:1.4.0-alpha08` are released. [Version 1.4.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..47e81d1c497b8a57534a460c277855db1b0257ae/fragment)

**Bug Fixes**

- Improved the `UseRequireInsteadOfGet` Lint check to better handle redundant parenthesis. ([I2d865](https://android-review.googlesource.com/#/q/I2d86527576efa558ea06c270edfd7f34de1a8f5c))
- Improved the `UseGetLayoutInflater` Lint check to handle additional edge cases. ([Ie5423](https://android-review.googlesource.com/#/q/Ie54235d4169c5042441f3e9608296ae4de670850))

### Version 1.4.0-alpha07

August 18, 2021

`androidx.fragment:fragment:1.4.0-alpha07`, `androidx.fragment:fragment-ktx:1.4.0-alpha07`, and `androidx.fragment:fragment-testing:1.4.0-alpha07` are released with no notable changes. [Version 1.4.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/fragment)

### Version 1.4.0-alpha06

August 4, 2021

`androidx.fragment:fragment:1.4.0-alpha06`, `androidx.fragment:fragment-ktx:1.4.0-alpha06`, and `androidx.fragment:fragment-testing:1.4.0-alpha06` are released. [Version 1.4.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/fragment)

**Bug Fixes**

- Fixed an issue with multiple back stacks when rapidly swapping between back stacks that would appear as an `IllegalStateException` while restoring a `FragmentTransaction` or as a second copy of a fragment appearing. ([I9039f](https://android-review.googlesource.com/#/q/I9039f01490dae53cb66ef435161b153b4a0568ff))
- Fixed an issue where `FragmentManager` would hold onto a copy of state previously saved via `saveBackStack()` even after that state was restored. ([Ied212](https://android-review.googlesource.com/#/q/Ied212e256fedc5ba5288d046c023ba1b767a894a))
- The `dismissAllowingStateLoss()` method of `DialogFragment` no longer crashes when you call it after the state is saved when specifically adding the DialogFragment via the `show(FragmentTransaction, String)` method. ([I84422](https://android-review.googlesource.com/#/q/I844222aba9e56d7ae6b0cdb57793ab38f6dbe4c1))

### Version 1.4.0-alpha05

July 21, 2021

`androidx.fragment:fragment:1.4.0-alpha05`, `androidx.fragment:fragment-ktx:1.4.0-alpha05`, and `androidx.fragment:fragment-testing:1.4.0-alpha05` are released. [Version 1.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/fragment)

**Bug Fixes**

- From [Fragment `1.3.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.6): The Fragment's view is now properly set to `GONE` when using `hide()` when the root view has `transitionGroup="true"` set. ([aosp/1766655](https://android-review.googlesource.com/1766655), [b/193603427](https://issuetracker.google.com/issues/193603427))
- From [Fragment `1.3.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.6): `FragmentActivity` now always unlocks the saved state as its first operation in lifecycle callbacks it overrides. ([I6db7a](https://android-review.googlesource.com/#/q/I6db7adb364dfbdd922a376242d54519028d4a9c9))

**Dependency update**

- From [Fragment `1.3.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.6): Fragments now depends on [Activity `1.2.4`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.4) ([I3a66c](https://android-review.googlesource.com/#/q/I3a66c06ec44c43106e6f7fb48ba9b9f964429b45))

### Version 1.4.0-alpha04

June 30, 2021

`androidx.fragment:fragment:1.4.0-alpha04`, `androidx.fragment:fragment-ktx:1.4.0-alpha04`, and `androidx.fragment:fragment-testing:1.4.0-alpha04` are released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..19ae3a88ff0824d615355b492cb56049e16991f2/fragment)

**API Changes**

- `FragmentManager` now uses `SavedStateRegistry` under the hood to save its state. The `saveAllState()` and `restoreSavedState()` methods have also been deprecated in `FragmentController`. If you are using `FragmentController` to host fragments outside of `FragmentActivity`, you should have your `FragmentHostCallbacks` implement `SavedStateRegistryOwner`. ([Iba68e](https://android-review.googlesource.com/#/q/Iba68e71ee9ec0befa79a565a476d25534e86d0e3), [b/188734238](https://issuetracker.google.com/issues/188734238))

**Bug Fixes**

- Fixed an issue where the call to `saveBackStack()` as part of supporting multiple back stacks would fail when done at the same time as running a `FragmentTransaction` that used `replace()`. ([I73137](https://android-review.googlesource.com/#/q/I731372db582f00dc3da4fb05a4f2892378945618))
- Fixed a `NullPointerException` that would occur after manually restoring a saved back stack that contained multiple transactions when using the `restoreBackStack()` API for multiple back stack support. This also fixed an issue where `setReorderingAllowed(true)` was not being checked for all transactions. ([I8c593](https://android-review.googlesource.com/#/q/I8c59355e8899ed86c4e54cccc18af5475a78b319))
- Fixed an issue where `FragmentManager` would incorrectly continue to restore previously saved state of fragments even after those fragments were removed from the `FragmentManager`, thus causing the saved state to continuously grow over time. ([I1fb8e](https://android-review.googlesource.com/#/q/I1fb8eb6942bc385794308bc2056f365472e5a47c))

### Version 1.4.0-alpha03

June 16, 2021

`androidx.fragment:fragment:1.4.0-alpha03`, `androidx.fragment:fragment-ktx:1.4.0-alpha03`, and `androidx.fragment:fragment-testing:1.4.0-alpha03` are released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..ccf79f53033e665475116a4e78ff124df2a52c4b/fragment)

**New Features**

- All Fragment StrictMode [`Violation`](https://developer.android.com/reference/androidx/fragment/app/strictmode/Violation) classes have been updated with more detailed error messages that explain the details of the violation. ([b/187871638](https://issuetracker.google.com/issues/187871638))
  - `FragmentTagUsageViolation` now contains more detailed error message that container the parent container that the fragment would have been added to. ([Ic33a7](https://android-review.googlesource.com/#/q/Ic33a7bfc836a8640b04af915268f5bc9e027bde3))
  - `WrongFragmentContainerViolation` now has more detailed error message that includes the container that the fragment was being added to. ([Ib55f8](https://android-review.googlesource.com/#/q/Ib55f8e4c05e8e2ff6c25916df0749d820ade30d3))
  - The use case classes for `TargetFragmentUsageViolation` now have more detailed error messages to include the fragment causing the violation and any other contained information. ([Icc6ac](https://android-review.googlesource.com/#/q/Icc6aceb7a1fd79894fea1837be43a3090c2af4a6))
  - The classes extending `RetainInstanceUsageViolation` now have more detailed error messages that include the fragment causing the violation. ([I6bd55](https://android-review.googlesource.com/#/q/I6bd559d35f8b4f9aa340efa3f36cb4aab782bc22))
  - `FragmentReuseViolation` now has more detailed error message that includes the previous id of the fragment. ([I28ce2](https://android-review.googlesource.com/#/q/I28ce254ddb61dc3bf4daddfc8cc7eb6985b8b611))
  - `SetUserVisibleHintViolation` now has more detailed error message that includes what the user visible hint was being set to. ([Ib2d5f](https://android-review.googlesource.com/#/q/Ib2d5f91e4ad0575278c04de7721c6f3ad63e5f48))

**Behavior Changes**

- Reverted the restriction on calling `fitsSystemWindows` on a `FragmentContainerView` - this no longer crashes your app. ([6b8ddd](https://android-review.googlesource.com/#/q/6b8ddd6cc0bc6df558c5c0e009708d4fbae10a77), [b/190622202](https://issuetracker.google.com/issues/190622202))

**Bug Fixes**

- From [Fragment `1.3.5`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.5): Fixed a regression in shared element transitions introduced in [Fragment `1.3.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4) by [aosp/1679887](https://android-review.googlesource.com/1679887/). Fragments now correctly handle transition groups (either set directly via `transitionGroup="true"` or indirectly via a `transitionName` or `background`) and shared elements will no longer throw `IndexOutOfBoundsException`s. ([I16484](https://android-review.googlesource.com/#/q/I164845639cae1f64cf54e4e89b2a24d7eb649beb), [b/188679569](https://issuetracker.google.com/issues/188679569), [b/188969304](https://issuetracker.google.com/issues/188969304))
- The `FragmentManager` will no longer crash when you attempt to hide a removing fragment. ([I573dd](https://android-review.googlesource.com/#/q/I573ddcfcd1b9c782b5546dd4643e0e4ed042b277), [b/183634730](https://issuetracker.google.com/issues/183634730))
- The `OnCreateDialogIncorrectCallback` lint check will no longer crash when evaluating a top level variable. ([0a9efa](https://android-review.googlesource.com/#/q/0a9efa914d322810f8dc8d9ba06e79d164c8892d), [b/189967522](https://issuetracker.google.com/issues/189967522))

### Version 1.4.0-alpha02

June 2, 2021

`androidx.fragment:fragment:1.4.0-alpha02`, `androidx.fragment:fragment-ktx:1.4.0-alpha02`, and `androidx.fragment:fragment-testing:1.4.0-alpha02` are released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/fragment)

**New Features**

- `FragmentStrictMode` will now always log violations when logging is enabled via the `FragmentManager`, regardless of the current strict mode policy being used. ([I02df6](https://android-review.googlesource.com/#/q/I02df6361e86124563757d152993aba6468d400f3), [b/187872638](https://issuetracker.google.com/issues/187872638))
- `FragmentStrictMode` now supports exempting particular `Fragment` classes from strict mode `Violation`s allowing that class to bypass any penalties. ([Ib4e5d](https://android-review.googlesource.com/#/q/Ib4e5d6217110d76bcc9ce2a15b12e350ccbc773b), [b/184786736](https://issuetracker.google.com/issues/184786736))

- The `FragmentStrictMode` `Violation` class has been expanded to add structure information based on each violation. This allows you to verify exactly what caused the violation along with the violating fragment ([If5118](https://android-review.googlesource.com/#/q/If5118b1a169e4050620d4aac084d4692393e4e04), [b/187871150](https://issuetracker.google.com/issues/187871150)), each `Violation` contains the following:

  - `WrongFragmentContainerViolation` now contains the `ViewGroup` that the `Fragment` was attempting to be added to. ([I83c75](https://android-review.googlesource.com/#/q/I83c75a2b30f2defef7868e6d1b1d7ea63e576c57), [b/187871150](https://issuetracker.google.com/issues/187871150))
  - `TargetFragmentUsageViolation`has been expanded into, `SetTargetFragmentUsageViolation`, `GetTargetFragmentUsageViolation`, and `GetTargetFragmentRequestCodeUsageViolation`, with `SetTargetFragmentUsageViolation` containing the target fragment and request code. ([I741b4](https://android-review.googlesource.com/#/q/I741b4e0b8aff45babe1a453d41149c7972538789), [b/187871150](https://issuetracker.google.com/issues/187871150))
  - `SetUserVisibleHintViolation` now contains the boolean value passed into `setUserVisibleHint()`. ([I00585](https://android-review.googlesource.com/#/q/I0058552a0176f3e964ceda122b1eb2540490d1a5), [b/187871150](https://issuetracker.google.com/issues/187871150))
  - `FragmentTagUsageViolation` now contains the ViewGroup that the `<fragment>` tag was attempting to inflate a fragment into.([I5dbbc](https://android-review.googlesource.com/#/q/I5dbbc3bc1e318dca326b2d58ad5e9b421e33b072), [b/187871150](https://issuetracker.google.com/issues/187871150))
  - `FragmentReuseViolation` now contains the unique ID of the previous instance of the `Fragment` that caused the viotion. ([I0544d](https://android-review.googlesource.com/#/q/I0544d256d72efc8bfa3e3eaddd5c36189d09e0ae), [b/187871150](https://issuetracker.google.com/issues/187871150))
  - `RetainInstanceUsageViolation` is now abstract and has two subclasses, `SetRetainInstanceUsageViolation` and `GetRetainInstanceUsageViolation`, representing the two cases for the violation type. ([Ic81e5](https://android-review.googlesource.com/#/q/Ic81e5ce6a552f47137cf9d101bc6ce81a3f61db3), [b/187871150](https://issuetracker.google.com/issues/187871150))

**Behavior Changes**

- `FragmentContainerView` now throws an exception when attempting to change the `fitsSystemWindow` attribute programmatically or via XML. Insets should be handled by each individual fragment's view. ([Ie6651](https://android-review.googlesource.com/#/q/Ie6651e5de15e2f99f3a6c9fe1554928f34821782), [b/187304502](https://issuetracker.google.com/issues/187304502))

### Version 1.4.0-alpha01

May 18, 2021

`androidx.fragment:fragment:1.4.0-alpha01`, `androidx.fragment:fragment-ktx:1.4.0-alpha01`, and `androidx.fragment:fragment-testing:1.4.0-alpha01` are released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a12bda4096b6d81e46ecf935fe7140fb80dc61e0..66681ad83c328d0dd821b943bb3d375f02c1db61/fragment)

**New Features**

- `FragmentContainerView` now provides a `getFragment()` method which returns the fragment that was most recently added to the container. This uses the same logic as `findFragmentById()` with the ID of the `FragmentContainerView`, but allows chaining the call. ([Ife17a](https://android-review.googlesource.com/#/q/Ife17ac3a7afe345a8a2e8e1bdf9281fabd63a2d1), [b/162527857](https://issuetracker.google.com/issues/162527857))

      val navController = binding.container.getFragment<NavHostFragment>().navController

- Added
  `FragmentTransaction#TRANSIT_FRAGMENT_MATCH_ACTIVITY_{OPEN, CLOSE}`
  to specify whether to enable the standard Activity-transition animation taken from your theme in Fragments transition. ([I46652](https://android-review.googlesource.com/#/q/I46652ec813b0413a55d6c90efb656f6d9691c211))

**Multiple back stacks**

The `FragmentManager` maintains a back stack made up of fragment transactions that used [`addToBackStack()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#addToBackStack(java.lang.String)). This allows you to pop those transactions and return to the previous state, using the mechanisms for [Saving state with fragments](https://developer.android.com/guide/fragments/saving-state) to allow your fragments to restore their state appropriately.

This release expands on these mechanisms by providing two new `FragmentManager` APIs: `saveBackStack(String name)` and `restoreBackStack(String name)`. These APIs use the same `name` as `addToBackStack()` to save the state of the `FragmentTransaction` and the state of every fragment that was added in those transactions and allow you to later restore those transactions and their fragments with their state in tact. This allows you to effectively 'swap' between multiple back stacks by saving the current back stack and restoring a saved back stack.

`saveBackStack()` operates similarly to [`popBackStack()`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#popBackStack(java.lang.String,%20int)) in that it is asynchronous and results in all the fragment transactions back to that specific name to be reversed ('popped') and any added fragments to be destroyed and removed, but it differs in a few important ways:

- `saveBackStack()` is always inclusive.
- Unlike `popBackStack()` which will pop **all** transactions on the back stack if the specified name is not found on the back stack or if a null name is provided, `saveBackStack()` does nothing if you haven't previously committed a fragment transaction using `addToBackStack()` with that exact, non-null name.
- The state of all fragments added from those transactions is saved. This means that the View state of every fragment is stored, `onSaveInstanceState()` of every fragment is called and that state is restored, and any `ViewModel` instances associated with those fragments are retained (and `onCleared()` is **not** called on them).

The fragment transactions that can be used with `saveBackStack()` must meet certain criteria:

- Every fragment transaction must use [`setReorderingAllowed(true)`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setReorderingAllowed(boolean)) to ensure the transactions can be restored as a single, atomic operation.
- The set of transactions saved must be self-contained (i.e., they must **not** explicitly reference any fragments outside of that set of transactions) to ensure that they can be restored at any later time, no matter what changes have been made to the back stack in the intervening time.
- No fragment that is saved can be a retained fragment or have a retained fragment in their transitive set of child fragments to ensure that the `FragmentManager` does not return any references to saved fragments after the back stack is saved.

Similar to `saveBackStack()`, `restoreBackStack()` does nothing if you have not previously called `saveBackStack()` with the same name. ([b/80029773](https://issuetracker.google.com/80029773))

**Fragment StrictMode**

The `FragmentStrictMode` APIs provide *runtime* checks that allow you to verify that your app or libraries you depend on are not calling deprecated fragment APIs. When a violation is detected, you can choose to print a log message, trigger your own custom listener, or crash your app. The `FragmentStrictMode.Policy` that controls what checks are enabled and what "penalties" are triggered can be set on a `FragmentManager` via the new `setStrictModePolicy()` method. That policy applies to that `FragmentManager` and transitively to any child fragment managers that do not set their own unique policy. ([#123](https://github.com/androidx/androidx/pull/123), [#131](https://github.com/androidx/androidx/pull/131), [#150](https://github.com/androidx/androidx/pull/150), [b/143774122](https://issuetracker.google.com/153737341))

- `detectFragmentReuse()` detects whether a previously removed `Fragment` instance is being re-added to a `FragmentManager`. You should never interact with or keep a reference to a `Fragment` instance after it has been destroyed and removed from a `FragmentManager`. ([#142](https://github.com/androidx/androidx/pull/142), [b/153738653](https://issuetracker.google.com/153738653))
- `detectFragmentTagUsage()` detects when you are using the `<fragment>` tag in your layout XML. You should always use `FragmentContainerView` when inflating fragments as part of your layout. ([#141](https://github.com/androidx/androidx/pull/141), [b/153738235](https://issuetracker.google.com/153738235))
- `detectWrongFragmentContainer()` detects when you add a fragment to a container that is *not* a `FragmentContainerView`. You should always use `FragmentContainerView` as the container for fragments in your layout. ([#146](https://github.com/androidx/androidx/pull/146), [b/181137036](https://issuetracker.google.com/181137036))
- `detectRetainInstanceUsage()` detects when you use the deprecated `setRetainInstance()` or `getRetainInstance()` APIs. ([#140](https://github.com/androidx/androidx/pull/140), [b/153737954](https://issuetracker.google.com/153737954))
- `detectSetUserVisibleHint()` detects when you use the deprecated `setUserVisibleHint()` API. ([#136](https://github.com/androidx/androidx/pull/136), [b/153738974](https://issuetracker.google.com/153738974))
- `detectTargetFragmentUsage()` detects when you use the deprecated `setTargetFragment()`, `getTargetFragment()` or `getTargetRequestCode()` APIs. ([#139](https://github.com/androidx/androidx/pull/139), [b/153737745](https://issuetracker.google.com/153737745))

**API Changes**

- The experimental API of `FragmentManager.enableNewStateManager(boolean)` has been removed and the [new state manager](https://medium.com/androiddevelopers/fragments-rebuilding-the-internals-61913f8bf48e) is now the only option available. ([I90036](https://android-review.googlesource.com/#/q/I9003696ae7abecdd43eece8a20fea8e0657dadc4), [b/162776418](https://issuetracker.google.com/issues/162776418))
- `FragmentScenario` now implements `Closeable`, allowing you to use it with Kotlin's [`use`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/use.html) method or [try-with-resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html). ([#121](https://github.com/androidx/androidx/pull/121), [b/143774122](https://issuetracker.google.com/143774122))

**New Lint checks**

- The `UseGetLayoutInflater` Lint check now warns when using `LayoutInflater.from(Context)` within a `DialogFragment` - you should always use the dialog fragment's `getLayoutInflater()` method to get the appropriate for `LayoutInflater`. ([#156](https://github.com/androidx/androidx/pull/156), [b/170781346](https://issuetracker.google.com/170781346))
- The `DialogFragmentCallbacksDetector` Lint check now warns when calling `setOnCancelListener` or `setOnDismissListener` in the `onCreateDialog()` method of a `DialogFragment` - these listeners are owned by the `DialogFragment` itself and you should override `onCancel()` and `onDismiss()` to receive these callbacks. ([#171](https://github.com/androidx/androidx/pull/171), [b/181780047](https://issuetracker.google.com/181780047), [b/187524311](https://issuetracker.google.com/187524311))

**Bug Fixes**

- From [Fragment 1.3.4](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4): Fixed a regression introduced in [Fragment `1.3.3`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.3) when using the `ViewTreeViewModelStoreOwner.get()` API with `ViewModelProvider` or the Jetpack Compose method of `viewModel()` inside a Fragment. These use cases now correctly use the `ViewModelProvider.Factory` provided by your Fragment if it overrides `getDefaultViewModelProviderFactory()` (as `@AndroidEntryPoint` annotated Fragments do when using Hilt). If you do not override that method, a `SavedStateViewModelFactory` that saves and restores its state alongside the Fragment's view is created as the default factory. ([I5cbfa](https://android-review.googlesource.com/#/q/I5cbfacde2479fb270c0c344c478260f20b3207d5), [b/186097368](https://issuetracker.google.com/issues/186097368))
- From [Fragment 1.3.4](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4): When using `FragmentContainerView` on API 29, insets will no longer dispatch indefinitely, fixing issues with `BottomNavigationBar` and `FloatingActionButton` instances. ([I1bb78](https://android-review.googlesource.com/#/q/I1bb780dffcbbcb6a78fbfb74d288a3c0620a3a40), [b/186012452](https://issuetracker.google.com/issues/186012452))
- From [Fragment 1.3.4](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4): You can now retrieve your Parcelable from the fragment result bundle after process death. ([I65932](https://android-review.googlesource.com/#/q/I6593233191347d9595f81268951d6f8dbb627273), [b/187443158](https://issuetracker.google.com/issues/187443158))
- From [Fragment 1.3.4](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4): When doing a shared element transition on a ViewGroup, if the ViewGroup has `transitionGroup` set to false, it will now properly transition. ([I99675](https://android-review.googlesource.com/#/q/I99675eac030325415789be0762aa666355f27dd8))

**External Contribution**

- Thanks [simonschiller](https://github.com/simonschiller) for making `FragmentScenario` implement `Closeable`. ([#121](https://github.com/androidx/androidx/pull/121), [b/143774122](https://issuetracker.google.com/143774122))
- Thanks [simonschiller](https://github.com/simonschiller) for adding the entirety of the `FragmentStrictMode` API for this release! ([#123](https://github.com/androidx/androidx/pull/123), [#131](https://github.com/androidx/androidx/pull/131), [#150](https://github.com/androidx/androidx/pull/150), [b/143774122](https://issuetracker.google.com/153737341), [#142](https://github.com/androidx/androidx/pull/142), [b/153738653](https://issuetracker.google.com/153738653), [#141](https://github.com/androidx/androidx/pull/141), [b/153738235](https://issuetracker.google.com/153738235), [#146](https://github.com/androidx/androidx/pull/146), [b/181137036](https://issuetracker.google.com/181137036), [#140](https://github.com/androidx/androidx/pull/140), [b/153737954](https://issuetracker.google.com/153737954), [#136](https://github.com/androidx/androidx/pull/136), [b/153738974](https://issuetracker.google.com/153738974), [#139](https://github.com/androidx/androidx/pull/139), [b/153737745](https://issuetracker.google.com/153737745))
- Thanks [tatocaster](https://github.com/tatocaster) for adding the `UseGetLayoutInflater` Lint check. ([#156](https://github.com/androidx/androidx/pull/156), [b/170781346](https://issuetracker.google.com/170781346))
- Thanks [tatocaster](https://github.com/tatocaster) for adding the `DialogFragmentCallbacksDetector` Lint check. ([#171](https://github.com/androidx/androidx/pull/171), [b/181780047](https://issuetracker.google.com/181780047))

## Version 1.3

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.3.6

July 21, 2021

`androidx.fragment:fragment:1.3.6`, `androidx.fragment:fragment-ktx:1.3.6`, and `androidx.fragment:fragment-testing:1.3.6` are released. [Version 1.3.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f7c7f1ee129c30eda48c6e13a4a525ed2c846f6..9bda870a1d83164b81bca5882af8863c0259462f/fragment)

**Bug Fixes**

- From [Fragment `1.4.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/fragment#1.4.0-alpha03): The `FragmentManager` will no longer crash when you attempt to hide a removing fragment. ([I573dd](https://android-review.googlesource.com/#/q/I573ddcfcd1b9c782b5546dd4643e0e4ed042b277), [b/183634730](https://issuetracker.google.com/issues/183634730))
- The Fragment's view is now properly set to `GONE` when using `hide()` when the root view has `transitionGroup="true"` set. ([aosp/1766655](https://android-review.googlesource.com/1766655), [b/193603427](https://issuetracker.google.com/issues/193603427))
- `FragmentActivity` now always unlocks the saved state as its first operation in lifecycle callbacks it overrides. ([I6db7a](https://android-review.googlesource.com/#/q/I6db7adb364dfbdd922a376242d54519028d4a9c9))

**Dependency update**

- From [Fragment `1.3.6`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.6): Fragments now depends on [Activity `1.2.4`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.4) ([I3a66c](https://android-review.googlesource.com/#/q/I3a66c06ec44c43106e6f7fb48ba9b9f964429b45))

### Version 1.3.5

June 16, 2021

`androidx.fragment:fragment:1.3.5`, `androidx.fragment:fragment-ktx:1.3.5`, and `androidx.fragment:fragment-testing:1.3.5` are released. [Version 1.3.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d5122ff6f757cd8287879fdb2712ce745d3c7eb..9f7c7f1ee129c30eda48c6e13a4a525ed2c846f6/fragment)

**Bug Fixes**

- Fixed a regression in shared element transitions introduced in [Fragment `1.3.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.4) by [aosp/1679887](https://android-review.googlesource.com/1679887/). Fragments now correctly handle transition groups (either set directly via `transitionGroup="true"` or indirectly via a `transitionName` or `background`) and shared elements will no longer throw `IndexOutOfBoundsException`s. ([I16484](https://android-review.googlesource.com/#/q/I164845639cae1f64cf54e4e89b2a24d7eb649beb), [b/188679569](https://issuetracker.google.com/issues/188679569), [b/188969304](https://issuetracker.google.com/issues/188969304))

### Version 1.3.4

May 18, 2021

`androidx.fragment:fragment:1.3.4`, `androidx.fragment:fragment-ktx:1.3.4`, and `androidx.fragment:fragment-testing:1.3.4` are released. [Version 1.3.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a12bda4096b6d81e46ecf935fe7140fb80dc61e0..3d5122ff6f757cd8287879fdb2712ce745d3c7eb/fragment)

**Bug Fixes**

- Fixed a regression introduced in [Fragment `1.3.3`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.3) when using the `ViewTreeViewModelStoreOwner.get()` API with `ViewModelProvider` or the Jetpack Compose method of `viewModel()` inside a Fragment when using Hilt. These use cases now correctly use the `ViewModelProvider.Factory` provided by your Fragment if it overrides `getDefaultViewModelProviderFactory()` (as `@AndroidEntryPoint` annotated Fragments do). If you do not override that method, a `SavedStateViewModelFactory` that saves and restores its state alongside the Fragment's view is created as the default factory. ([I5cbfa](https://android-review.googlesource.com/#/q/I5cbfacde2479fb270c0c344c478260f20b3207d5), [b/186097368](https://issuetracker.google.com/issues/186097368))
- When using `FragmentContainerView` on API 29, insets will no longer dispatch indefinitely, fixing issues with `BottomNavigationBar` and `FloatingActionButton` instances. ([I1bb78](https://android-review.googlesource.com/#/q/I1bb780dffcbbcb6a78fbfb74d288a3c0620a3a40), [b/186012452](https://issuetracker.google.com/issues/186012452))
- You can now retrieve your Parcelable from the fragment result bundle after process death. ([I65932](https://android-review.googlesource.com/#/q/I6593233191347d9595f81268951d6f8dbb627273), [b/187443158](https://issuetracker.google.com/issues/187443158))
- When doing a shared element transition on a ViewGroup, if the ViewGroup has `transitionGroup` set to false, it will now properly transition. ([I99675](https://android-review.googlesource.com/#/q/I99675eac030325415789be0762aa666355f27dd8))

### Version 1.3.3

April 21, 2021

`androidx.fragment:fragment:1.3.3`, `androidx.fragment:fragment-ktx:1.3.3`, and `androidx.fragment:fragment-testing:1.3.3` are released. [Version 1.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/359e0b300368007d383fda1172a2813f9126d11f..a12bda4096b6d81e46ecf935fe7140fb80dc61e0/fragment)

**New Features**

- Using `SavedStateViewModelFactory` now works when used with the `SavedStateRegistryOwner` returned by using `ViewTreeSavedStateRegistryOwner.get()` with the Fragment's View. ([I21acf](https://android-review.googlesource.com/#/q/I21acf18f70ab6dcc60f5946d5b0d878e12bc76df), [b/181577191](https://issuetracker.google.com/issues/181577191))

**Bug Fixes**

- Fixed a regression introduced in [Fragment `1.3.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.2) which would cause `popEnter` animations to not run when popping a `FragmentTransaction` that included a `setPrimaryNavFragment` operation, such as those used by `NavHostFragment`. ([I38c87](https://android-review.googlesource.com/#/q/I38c877ae34c825b3a451ab325b6f683de00a2457), [b/183877426](https://issuetracker.google.com/issues/183877426))
- `FragmentContainerView` now ensures that every `Fragment` is dispatched a new set of `WindowInsets`, ensuring that each fragment can now independently consume the insets. ([I63f68](https://android-review.googlesource.com/#/q/I63f685e6715334a77e477180ae94771eeef827c3), [b/172153900](https://issuetracker.google.com/issues/172153900))
- `DialogFragment` now properly handles cases where a child fragment is added to a container that has the same ID as a container in your custom `Dialog` class, fixing view hierarchy issues when reusing IDs that are used internally by dialogs such as `BottomSheetDialog`. ([Ie6279](https://android-review.googlesource.com/#/q/Ie62791677cb8771f22b19bdce5985426c669fba0), [b/180021387](https://issuetracker.google.com/issues/180021387))
- `FragmentManager.dump()` now properly indents the first fragment in the list of active fragments. ([If5c33](https://android-review.googlesource.com/#/q/If5c339c3052a95bf5f1db4f97d460b4969ea31cb), [b/183705451](https://issuetracker.google.com/issues/183705451))

**New State Manager Bug Fixes**

- The new fragment state manager now properly handles exit transitions with hide operations. ([I9e4de](https://android-review.googlesource.com/#/q/I9e4de834e866143295435825c6eba8d5b06011f8), [b/184830265](https://issuetracker.google.com/issues/184830265))

### Version 1.3.2

March 24, 2021

`androidx.fragment:fragment:1.3.2`, `androidx.fragment:fragment-ktx:1.3.2`, and `androidx.fragment:fragment-testing:1.3.2` are released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/587cd19caebfbd63197a766916bf5296b3a6d65e..359e0b300368007d383fda1172a2813f9126d11f/fragment)

**New State Manager Bug Fixes**

- When running both `popBackStack()` and `commit()` operations together, the last operation will now set the direction for all animations rather than running some pop animations and some enter animations. ([I7072e](https://android-review.googlesource.com/#/q/I7072e2c8008318ae812ae461a42ddafbbe6055cd), [b/181142246](https://issuetracker.google.com/issues/181142246))
- Views within in a shared element hierarchy will no longer have their transition name cleared when doing a shared element transition. ([I4d4a6](https://android-review.googlesource.com/#/q/I4d4a6d7770d5c6d54e4c647559d5cabae71f0051), [b/179934757](https://issuetracker.google.com/issues/179934757))

**Dependency Updates**

- Fragment now depends on [Activity 1.2.2](https://developer.android.com/jetpack/androidx/releases/activity#1.2.2), fixing an issue with Activity's `InvalidFragmentVersionForActivityResult` lint check when using Fragment 1.3.1 or higher.
- Fragment now depends on [Lifecycle 2.3.1](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1).

### Version 1.3.1

March 10, 2021

`androidx.fragment:fragment:1.3.1`, `androidx.fragment:fragment-ktx:1.3.1`, and `androidx.fragment:fragment-testing:1.3.1` are released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b4fe1cc9ec5c6d25591e037e4f84316c36d6825a..587cd19caebfbd63197a766916bf5296b3a6d65e/fragment)

**New Features**

- Dialogs within a `DialogFragment` can now get access to ViewTree owners through their DecorView, ensuring that `DialogFragment` can be used with `ComposeView`. ([Ib9290](https://android-review.googlesource.com/#/q/Ib92905306e16dcaee63c985f22b5e36b6718dd39), [b/180691023](https://issuetracker.google.com/issues/180691023))

**Bug Fixes**

- Fragments inflated into an already `RESUMED` activity using FragmentContainerView are now properly shown after a configuration change. ([Ie14c8](https://android-review.googlesource.com/#/q/Ie14c80467b66186862319469f51bbd4d7ebcbbb9), [b/180538371](https://issuetracker.google.com/issues/180538371))
- There is no longer an extra `}` at the end of the fragment `toString()` ([I54705](https://android-review.googlesource.com/#/q/I547053a275afdde0720a63370629af49c1b8cd2e), [b/177761088](https://issuetracker.google.com/issues/177761088))
- Overridden methods in FragmentActivity now properly inherit the base method javaDoc ([I736ce](https://android-review.googlesource.com/#/q/I736ce6ad3c248c093ccb4cdf1f40029451fd1422), [b/139548782](https://issuetracker.google.com/issues/139548782))
- The docs for `setFragmentResult` and `setFragmentResultListener` have updated their parameters docs to reflect that they no longer accept nullables ([I990ba](https://android-review.googlesource.com/#/q/I990baa2e1b71a11b11342c366c284903c247e631), [b/178348386](https://issuetracker.google.com/issues/178348386))

**New State Manager Bug Fixes**

- Fixed a memory leak in fragments caused by `mFocusedView` ([Ib4e9e](https://android-review.googlesource.com/#/q/Ib4e9eddfba3ad925471890ff0078d9a65416f7da), [b/179925887](https://issuetracker.google.com/issues/179925887))
- Fragments now properly call `onCreateOptionsMenu` when using show/hide transactions ([I8bce8](https://android-review.googlesource.com/#/q/I8bce888e4b9757b5f5c3200e8d884e16372b6ec6), [b/180255554](https://issuetracker.google.com/issues/180255554))
- Child fragments with transitions that start prior to the fragment being laid out will now properly reach `RESUMED` ([Ic11e6](https://android-review.googlesource.com/#/q/Ic11e655bd4ed206485c2762a1af4e5bc7aa4cf9c), [b/180825150](https://issuetracker.google.com/issues/180825150))
- Fragments inflated using the `<fragment>` tag will now always make it to `RESUMED` ([I452ac](https://android-review.googlesource.com/#/q/I452acc8016d1be2f4be611cd3affeb33687600ec), ([I9fa49](https://android-review.googlesource.com/#/q/I9fa498952456908a11a257cb3fdedcb89fb083a6))

**Dependency Updates**

- Fragment 1.3.1 depends on [Activity `1.2.1`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.1). ([I557b9](https://android-review.googlesource.com/#/q/I557b913b9c31c7856cd508151e3190c6779c191e))

### Version 1.3.0

February 10, 2021

`androidx.fragment:fragment:1.3.0`, `androidx.fragment:fragment-ktx:1.3.0`, and `androidx.fragment:fragment-testing:1.3.0` are released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fff94654610fc0f34aef14c059a073e6cdd80b10..b4fe1cc9ec5c6d25591e037e4f84316c36d6825a/fragment)

**Major changes since 1.2.0**

- **New State Manager** : A significant [rewrite of the internals](https://medium.com/androiddevelopers/fragments-rebuilding-the-internals-61913f8bf48e) of `FragmentManager` has fixed numerous issues around the dispatch of lifecycle events, animations and transitions, and how postponed fragments are handled.
- **Activity Result API Integration** : Added support for the `ActivityResultRegistry` API introduced in [Activity `1.2.0`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0) to handle `startActivityForResult()`+`onActivityResult()` as well as `requestPermissions()`+`onRequestPermissionsResult()` flows without overriding methods in your Fragment in addition to providing hooks for testing these flows. See the updated [Getting a Result from an Activity](https://developer.android.com/training/basics/intents/result).

  - This release fixes a number of issues around invalid request codes and the dispatch of permission requests that prevent the Activity Result API from working on previous versions of `FragmentActivity`. You must upgrade to Fragment 1.3.0 to use the Activity Result APIs in a `FragmentActivity` or `AppCompatActivity`.
- **Fragment Result API** : Added support for passing results between two Fragments via new APIs on `FragmentManager`. This works for hierarchy fragments (parent/child), DialogFragments, and fragments in Navigation and ensures that results are only sent to your Fragment while it is at least `STARTED`. The target fragment APIs have been deprecated in favor of these new APIs. See [Get Results using the Fragment Result API](https://developer.android.com/guide/fragments/communicate#fragment-result).

- **`FragmentOnAttachListener`** : The `onAttachFragment()` callback on `FragmentActivity` and `Fragment` have been deprecated. A new `FragmentOnAttachListener` has been added to provide a more flexible alternative, allowing delegation of `onAttachFragment()` to separate, testable listeners and support for adding a listener to FragmentManagers other than your direct child FragmentManager.

- **`FragmentScenario` Improvements** : The `FragmentScenario` class from the `fragment-testing` artifact has been rewritten in Kotlin and has received a number of improvements:

  - `FragmentScenario` now uses [`setMaxLifecycle()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setMaxLifecycle(androidx.fragment.app.Fragment,%20androidx.lifecycle.Lifecycle.State)) to implement `moveToState()`, ensuring consistent behavior on all API levels and decoupling the Fragment's state from the underlying Activity.
  - `FragmentScenario` now supports setting an initial `Lifecycle.State` to support asserting the fragment's state before moving to each `Lifecycle.State` for the first time.
  - There is now an alternative to the `FragmentScenario` API of `onFragment` in the form of the Kotlin reified extension method `withFragment` that allows you to return a value. Notably, it rethrows exceptions raised in the given block.
- **`ViewTree` Support** : `Fragment` now supports the `ViewTreeLifecycleOwner.get(View)`, `ViewTreeViewModelStoreOwner.get(View)`, and `ViewTreeSavedStateRegistryOwner` APIs added in [Lifecycle `2.3.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0) and [SavedState `1.1.0`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.1.0) such that it will return the Fragment as the `ViewModelStoreOwner`, and a `SavedStateRegistryOwner` and `LifecycleOwner` tied to the fragment's [view Lifecycle](https://developer.android.com/reference/androidx/fragment/app/Fragment#getViewLifecycleOwner()) when using a `View` within a `Fragment`.

- **`TRANSIT_` animation changes** : The fragment default effects, `TRANSIT_FRAGMENT_OPEN`, `TRANSIT_FRAGMENT_CLOSE`, and `TRANSIT_FRAGMENT_FADE`, now use [`Animator`](https://developer.android.com/reference/android/animation/Animator) instead of [`Animation`](https://developer.android.com/reference/kotlin/android/view/animation/Animation). The resources used to build these animators are now private.

- **`setRetainInstance()` deprecation** : The `setRetainInstance()` method on Fragments has been deprecated. With the introduction of [ViewModels](https://developer.android.com/topic/libraries/architecture/viewmodel), developers have a specific API for retaining state that can be associated with Activities, Fragments, and Navigation graphs. This allows developers to use a normal, not retained Fragment and keep the specific state they want retained separate, avoiding a common source of leaks while maintaining the useful properties of a single creation and destruction of the retained state (namely, the constructor of the `ViewModel` and the `onCleared()` callback it receives).

- **ViewPager 1 adapter deprecation** : With the release of [ViewPager2 `1.0.0`](https://developer.android.com/jetpack/androidx/releases/viewpager2#1.0.0), the `FragmentPagerAdapter` and `FragmentStatePagerAdapter` classes for interacting with `ViewPager` have been deprecated. See [Migrate from ViewPager to ViewPager2](https://developer.android.com/training/animation/vp2-migration).

### Version 1.3.0-rc02

January 27, 2021

`androidx.fragment:fragment:1.3.0-rc02`, `androidx.fragment:fragment-ktx:1.3.0-rc02`, and `androidx.fragment:fragment-testing:1.3.0-rc02` are released. [Version 1.3.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6970bb682fd9f49aa80d74409fd653bad01fe982..fff94654610fc0f34aef14c059a073e6cdd80b10/fragment)

**Bug Fixes**

- Fixed an issue where a parent `DialogFragment` would appear above a child `DialogFragment` after a configuration change; child dialog fragments now always appear above a parent dialog fragment. ([I30806](https://android-review.googlesource.com/#/q/I3080648340b7f05eac35f5ac77f8a7a2c289a104), [b/177439520](https://issuetracker.google.com/issues/177439520))
- Fixed issue where doing a `hide` operation with an `Animation` would cause the hiding fragment to flash at the end of the animation. ([I57e22](https://android-review.googlesource.com/#/q/I57e2282d6c16dcbb403379d67c5e747379db58b1), [b/175417675](https://issuetracker.google.com/issues/175417675))
- Fragments with transitions added before the view hierarchy is attached now properly reach `RESUMED`. ([I1fc1d](https://android-review.googlesource.com/#/q/I1fc1db01450466f9ee012f07e4b608aa3337c838), [b/177154873](https://issuetracker.google.com/issues/177154873))

**New State Manager Bug Fixes**

- The Fragment's view `Lifecycle` now properly handles cases where the Fragment's view is destroyed before the `Lifecycle` reaches `CREATED`, avoiding exceptions stating "no event down from INITIALIZED". ([eda2bd](https://android-review.googlesource.com/#/q/eda2bdb8e41d9fd7280f607b7848b12cc435574c), [b/176138645](https://issuetracker.google.com/issues/176138645))
- Fragments that use an `Animator` now appear in the proper order when using `FragmentContainerView`. ([Id9aa3](https://android-review.googlesource.com/#/q/Id9aa349b180cc2c22912efae3f2c44773ecb7126), [b/176089197](https://issuetracker.google.com/issues/176089197))

### Version 1.3.0-rc01

December 16, 2020

`androidx.fragment:fragment:1.3.0-rc01`, `androidx.fragment:fragment-ktx:1.3.0-rc01`, and `androidx.fragment:fragment-testing:1.3.0-rc01` are released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..6970bb682fd9f49aa80d74409fd653bad01fe982/fragment)

**Bug Fixes**

- `onPrepareOptionsMenu()` now follows the same logic as `onCreateOptionsMenu()` and is no longer called when a parent fragment calls `setMenuVisibility(false)`. ([Id7de8](https://android-review.googlesource.com/#/q/Id7de8156980c09e6ece0d977950b4844eb10d516), [b/173203654](https://issuetracker.google.com/issues/173203654))

**New State Manager Bug Fixes**

- Fixed leak and visual artifact when adding a fragment with an `Animation` to a `FragmentContainerView` and then interrupting that addition with a pop operation. ([I952d8](https://android-review.googlesource.com/#/q/I952d8409bb6afb810fc97b52c14e23f55ba5ab17))
- Fixed an issue where the fragment's view would remain in the view hierarchy if it was replaced during its `onCreate()` or `onViewCreated()` methods. ([I8a7d5](https://android-review.googlesource.com/#/q/I8a7d5aed2c5648d3b898bb1cc1469f90cf5f1abd))
- Focus is now properly restored to Fragment root views when they are resumed. ([Ifc84b](https://android-review.googlesource.com/#/q/Ifc84b33272f17f4be48f603e4826b7c6751fbb2f))
- Combining pop and replace operations in the same fragment transaction will now show the proper animations ([Ifd4e4](https://android-review.googlesource.com/#/q/Ifd4e49cd9874a9ac0673083c27ef3c9765bbfa04), [b/170328691](https://issuetracker.google.com/issues/170328691))

### Version 1.3.0-beta02

December 2, 2020

`androidx.fragment:fragment:1.3.0-beta02`, `androidx.fragment:fragment-ktx:1.3.0-beta02`, and `androidx.fragment:fragment-testing:1.3.0-beta02` are released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/fragment)

**New Features**

- `FragmentScenario` has been fully converted to Kotlin while maintaining source and binary compatibility via usage of Kotlin 1.4's functional interfaces for `FragmentAction`. ([I19d31](https://android-review.googlesource.com/#/q/I19d3175b0d7f1adb0ceaa9c1e907b7f608f86b55))

**Behavior Changes**

- FragmentContainerViews that do not inflate a fragment using the `class` or `android:name` attribute can now be used outside of a `FragmentActivity`. ([Id4397](https://android-review.googlesource.com/#/q/Id4397edf815e6603016e0a7798232c8e9f9f065f), [b/172266337](https://issuetracker.google.com/issues/172266337))
- Attempting to set the max lifecycle of a fragment to `DESTROYED` will now throw an `IllegalArgumentException` ([Ie7651](https://android-review.googlesource.com/#/q/Ie765188cbaf8473b2aac8f171e869c8fec84e212), [b/170765622](https://issuetracker.google.com/issues/170765622))
- Initializing a FragmentScenario with a `DESTROYED` state will now throw an `IllegalArgumentException` ([I73590](https://android-review.googlesource.com/#/q/I7359000183f73a7b2f01eb637655ca8c655e371e), [b/170765622](https://issuetracker.google.com/issues/170765622))

**New State Manager Bug Fixes**

- Fixed an issue where the view would not reach its final state if you interrupt a fragment transition that was using an `Animator` or one of the `TRANSIT_FRAGMENT_` options. ([I92426](https://android-review.googlesource.com/#/q/I92426d8572f9ca71c053945ecc2afd839efbc058), [b/169874632](https://issuetracker.google.com/issues/169874632))
- Fixed an issue that prevented fragments with an exiting `Animation` from being properly destroyed. ([I83d65](https://android-review.googlesource.com/#/q/I83d6584916bb3425f552d73a17e1ab938f00190d))
- Exiting fragments that have their effects reversed now correctly cancel and restart with the proper entering effect. ([I62226](https://android-review.googlesource.com/#/q/I622265e9b4ebb210657aac2a5b97dd47061bfd5c), [b/167092035](https://issuetracker.google.com/issues/167092035))
- Fixed an issue where the exit `Animator` of a `hide()` would not run. ([Id7ffe](https://android-review.googlesource.com/#/q/Id7ffe54e883d9bd22d0759edd190a9d68aba3390))
- Fragments now properly appear when postponed and then immediately started. ([Ie713b](https://android-review.googlesource.com/#/q/Ie713bb4f44c5d2432680f2efbb8cdb38a9d26bf2), [b/170022857](https://issuetracker.google.com/issues/170022857))
- Fragments that remove their focused view during an animation will no longer attempt to restore the focus on the detached view once they reach `RESUMED` ([I38c65](https://android-review.googlesource.com/#/q/I38c65f834e9b85c365952fdb1e84e03a82863063), [b/172925703](https://issuetracker.google.com/issues/172925703))

**External Contribution**

- `FragmentFactory` now caches fragment classes separately for different `ClassLoader` instances. Thanks Simon Schiller! ([#87](https://github.com/androidx/androidx/pull/87), [b/113886460](https://issuetracker.google.com/113886460))

### Version 1.3.0-beta01

October 1, 2020

`androidx.fragment:fragment:1.3.0-beta01`, `androidx.fragment:fragment-ktx:1.3.0-beta01`, and `androidx.fragment:fragment-testing:1.3.0-beta01` are released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/fragment)

**New Features**

- `setMaxLifecycle()` now supports setting the `Lifecycle` state to `INITIALIZING` as long as the fragment has not been moved to `CREATED`. ([b/159662173](https://issuetracker.google.com/issues/159662173))

**API Changes**

- Upgrade androidx to use Kotlin 1.4 ([Id6471](https://android-review.googlesource.com/#/q/Id647100407925c16d734c8c43392b4e2d108d0e3), [b/165307851](https://issuetracker.google.com/issues/165307851), [b/165300826](https://issuetracker.google.com/issues/165300826))

**Behavior Changes**

- Fragment resource files have been correctly made private. ([aosp/1425237](https://android-review.googlesource.com/c/platform/frameworks/support/+/1425237))

**Bug Fixes**

- Fragments inflated using the `<fragment>` tag will now properly wait until their views are added to a container before moving to STARTED ([I02f4c](https://android-review.googlesource.com/#/q/I02f4c2b910a182c580e514765062a649745161fb))
- Fragments that are visible and then `setMaxLifecycle()` to `CREATED` now properly run their exit effects. ([b/165822335](https://issuetracker.google.com/issues/165822335))
- Removing a detached fragment that is not added to the back stack no longer causes a memory leak. Courtesy of Nicklas Ansman Giertz! ([b/166489383](https://issuetracker.google.com/issues/166489383))
- Active fragments will now always have a non-null `FragmentManager` and fragments with a non-null `FragmentManager` will always be considered active. ([aosp/1422346](https://android-review.googlesource.com/c/platform/frameworks/support/+/1422346))
- The fragment default effects, `TRANSIT_FRAGMENT_OPEN`, `TRANSIT_FRAGMENT_CLOSE`, and `TRANSIT_FRAGMENT_FADE`, now use [`Animator`](https://developer.android.com/reference/android/animation/Animator) instead of [`Animation`](https://developer.android.com/reference/kotlin/android/view/animation/Animation). ([b/166155034](https://issuetracker.google.com/issues/1661550343))

**New State Manager Bug Fixes**

- Fragments now properly restore their view focus state from right before they start their animation. ([Icc256](https://android-review.googlesource.com/#/q/Icc2561fb3dc413250153e5e0fcb2d10846791d53))
- Fragments that only have a shared element transition now properly complete their special effects meaning they actually move to their final state ([Iaebc7](https://android-review.googlesource.com/#/q/Iaebc76914b9c24968a2943c18911b183f9dd8a4f), [b/166658128](https://issuetracker.google.com/issues/166658128))
- Fragment views are now always removed from the container before being destroyed. ([Id5876](https://android-review.googlesource.com/#/q/Id587699a6ae9dd696f568f8e0a5304156be1cd82))
- The new state manager now consistently removes the exiting fragment view before adding the entering one. ([I41a6e](https://android-review.googlesource.com/#/q/I41a6ee1a0bc135c0443d8152a8106498241d3862))
- Explicit changes to a fragment view's visibility are now respected by the new state manager. This means that if you set an entering fragment's view to `INVISIBLE` before the animation begins, it will actually stay invisible. ([b/164481490](https://issuetracker.google.com/issues/164481490))
- Fragments now prioritize `Animators` over `Animations`, meaning a fragment with both will only run the `Animator` and ignore the `Animation`. ([b/167579557](https://issuetracker.google.com/issues/167579557))
- The new state manager no longer causes fragments to flash when using entering animations. ([b/163084315](https://issuetracker.google.com/issues/163084315))

**Known Issue**

When using the new state manager, if you press back during an entering special effect instead of returning to the previous fragment, the old fragment is never re-added, resulting in a blank screen. ([b/167259187](https://issuetracker.google.com/issues/167259187), [b/167092035](https://issuetracker.google.com/issues/167092035), [b/168442830](https://issuetracker.google.com/issues/168442830))

### Version 1.3.0-alpha08

August 19, 2020

`androidx.fragment:fragment:1.3.0-alpha08`, `androidx.fragment:fragment-ktx:1.3.0-alpha08`, and `androidx.fragment:fragment-testing:1.3.0-alpha08` are released. [Version 1.3.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/fragment)

**New State Manager**

This release includes a major refactoring of the internal state management of `FragmentManager` which affects the dispatch of lifecycle methods, animations and transitions, and how postponed transactions are handled. This is enabled by default. See the [Fragments: Rebuilding the Internals blog post](https://medium.com/androiddevelopers/fragments-rebuilding-the-internals-61913f8bf48e) for more details. ([b/139536619](https://issuetracker.google.com/139536619), [b/147749580](https://issuetracker.google.com/147749580))

- An *experimental* API in `FragmentManager.enableNewStateManager(boolean)` can be used to control whether FragmentManager uses the new state manager. ([I7b6ee](https://android-review.googlesource.com/#/q/I7b6ee13ea89f3989beafe7c474455e8a04e929a3))

The following issues are fixed only when using the new state manager:

- The previous fragment of a `replace` operation is now correctly stopped before the new fragment is started. ([b/161654580](https://issuetracker.google.com/161654580))
- Fragments now prevent multiple competing animations on the same fragments, avoiding cases where an `Animation` would override all `Transition` effects or an `Animator` and a `Transition` on an individual fragment would both run. ([b/149569323](https://issuetracker.google.com/149569323))
- The `enterTransition` and `exitTranstion` of **all** fragments entering and exiting are now ran rather than only the last entering fragment and the first exiting fragment. ([b/149344150](https://issuetracker.google.com/149344150))
- Postponed fragments no longer get stuck at the `CREATED` state but instead move to `STARTED` with other fragments. ([b/129035555](https://issuetracker.google.com/129035555))
- Fixed an issue where `FragmentManager` would execute operations out of order when mixing a postponed re-ordered transaction and a non-reordered transaction. ([b/147297731](https://issuetracker.google.com/147297731))
- Popping multiple fragments simultaneously will no longer result in intermediate fragments being temporarily visible when postponing fragments. ([b/37140383](https://issuetracker.google.com/37140383))
- `FragmentManager` now returns the correct fragments when calling `findFragmentById()` or `findFragmentByTag()` from within the `onAttachFragment()` callback. ([b/153082833](https://issuetracker.google.com/153082833))
- Fragments no longer call `onCreateView()` on fragments being destroyed when the fragment replacing them is postponed. ([b/143915710](https://issuetracker.google.com/143915710))
- The error message when attempting to combine framework `Transition` and AndroidX `Transition` instances now mentions the fragment with the invalid transition. ([b/155574969](https://issuetracker.google.com/155574969))

**Behavior Changes**

- You can now call `launch()` on an `ActivityResultLauncher` in the `onCreate()` lifecycle method of a fragment. ([b/161464278](https://issuetracker.google.com/issues/161464278))
- Calling `registerForActivityResult()` after `onCreate()` now throws an exception indicating that this is not allowed rather than silently failing to deliver results after a configuration change. ([b/162255449](https://issuetracker.google.com/162255449))
- `FragmentActivity` now uses the `OnContextAvailableListener` API introduced in [Activity `1.2.0-alpha08`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha08) to restore the state of the `FragmentManager`. Any listeners added to subclasses of `FragmentActivity` will run after this listener. ([I513da](https://android-review.googlesource.com/#/q/I513da73bc0862b62af4166be35ba353fc7869a09))

**Bug Fixes**

- `ActivityOptions` passed through when using `startIntentSenderForResult()` are now respected. ([b/162247961](https://issuetracker.google.com/162247961))

**Known Issue**

- When using the new state manager, directly setting the visibility of the fragment's root view after `onViewCreated()` and before `onResume()` results in the visibility you set being overridden by `FragmentManager`, who controls the visibility of the root view. As a workaround, you should always use the `hide()` and `show()` operations to change the visibility of your fragment. ([b/164481490](https://issuetracker.google.com/164481490))

### Version 1.3.0-alpha07

July 22, 2020

`androidx.fragment:fragment:1.3.0-alpha07`, `androidx.fragment:fragment-ktx:1.3.0-alpha07`, and `androidx.fragment:fragment-testing:1.3.0-alpha07` are released. [Version 1.3.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..9f60cc700129e30cee9df020005c317fb39d32ec/fragment)

**New Features**

- `FragmentScenario` now supports setting an initial Lifecycle state of `CREATED`, `STARTED`, or `RESUMED` rather than always moving the Fragment to the `RESUMED` state. ([b/159662750](https://issuetracker.google.com/159662750))
- Added an alternative to the `FragmentScenario` API of `onFragment` in the form of the Kotlin reified extension method `withFragment` that allows you to return a value. Notably, it rethrows exceptions raised in the given block. ([b/158697631](https://issuetracker.google.com/158697631))

**Behavior Changes**

- `FragmentScenario` now uses [`setMaxLifecycle()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setMaxLifecycle(androidx.fragment.app.Fragment,%20androidx.lifecycle.Lifecycle.State)) to implement `moveToState()`, ensuring consistent behavior on all API levels and decoupling the Fragment's state from the underlying Activity. ([b/156527405](https://issuetracker.google.com/156527405))
- The `SavedStateRegistryOwner` returned by `ViewTreeSavedStateRegistryOwner` is now tied to the fragment view's Lifecycle. This ensures that it has its state saved and restore at the same time as the fragment's view. ([b/158503763](https://issuetracker.google.com/158503763))

**Bug Fixes**

- Fragments now wait for the fragment's view to be attached before calling `ViewCompat.requestApplyInsets()`, avoiding cases where the inset request was being dropped. ([b/158095749](https://issuetracker.google.com/158095749))
- Calling `clearFragmentResultListener` now properly clears the lifecycle observer. ([b/159274993](https://issuetracker.google.com/issues/159274993))

### Version 1.3.0-alpha06

June 10, 2020

`androidx.fragment:fragment:1.3.0-alpha06`, `androidx.fragment:fragment-ktx:1.3.0-alpha06`, and `androidx.fragment:fragment-testing:1.3.0-alpha06` are released. [Version 1.3.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/fragment)

**New Features**

- The `onAttachFragment()` callback on `FragmentActivity` and `Fragment` have been deprecated. A new `FragmentOnAttachListener` has been added to provide a more flexible alternative, allowing delegation of `onAttachFragment()` to separate, testable listeners and support for adding a listener to FragmentManagers other than your direct child FragmentManager. ([I06d3d](https://android-review.googlesource.com/#/q/I06d3daa4247914ae363382f7eab920657f23b5fa))

**Bug Fixes**

- Parent fragments now have their view state restored before their child fragments, fixing a visual ordering issue after a configuration change when a `DialogFragment` would show another `DialogFragment` as a child fragment. ([b/157195715](https://issuetracker.google.com/issues/157195715))
- Fixed an issue where the `UseRequireInsteadOfGet` Lint check would not handle chained usages of the `?.` and `!!` operators correctly. ([b/157677616](https://issuetracker.google.com/issues/157677616))

### Version 1.3.0-alpha05

May 20, 2020

`androidx.fragment:fragment:1.3.0-alpha05`, `androidx.fragment:fragment-ktx:1.3.0-alpha05`, and `androidx.fragment:fragment-testing:1.3.0-alpha05` are released. [Version 1.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/942518f415d35ff9f2ff78f312c076c673468877..ccc6e95c574b66563952c33fbe26888b93a0e0cb/fragment)

**New Features**

- Added support for `ViewTreeViewModelStoreOwner` from [Lifecycle `2.3.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha03), and `ViewTreeSavedStateRegistryOwner` from [SavedState `1.1.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.1.0-alpha01) when using a `View` within a `Fragment`. ([aosp/1297993](https://android-review.googlesource.com/1300264), [aosp/1300264](https://android-review.googlesource.com/1298680))

**API Changes**

- The `setFragmentResult()` and `setFragmentResultListener()` APIs now take a non-null `Bundle` and `FragmentResultListener`, respectively. To explicitly clear a previously set result or listener, use the new `clearFragmentResult()` and `clearFragmentResultListener()` methods. ([b/155416778](https://issuetracker.google.com/issues/155416778))
- The `setFragmentResultListener()` Kotlin extensions that take a lambda are now marked as `inline`. ([b/155323404](https://issuetracker.google.com/issues/155323404))

**Behavior Changes**

- The previously deprecated `startActivityForResult()`, `startIntentSenderForResult()`, and `requestPermissions` on `Fragment` now internally use `ActivityResultRegistry`, thus removing the restriction on using only the lower bits (below `0xFFFF`) for your request codes when using those APIs. ([b/155518741](https://issuetracker.google.com/issues/155518741))

**Documentation Updates**

- Expanded the documentation on the `Fragment(@LayoutRes int)` and `DialogFragment(@LayoutRes int)` constructors to clarify that they should be called from your subclasses' no argument constructor when using the default `FragmentFactory`. ([b/153042497](https://issuetracker.google.com/issues/153042497))

### Version 1.3.0-alpha04

April 29, 2020

`androidx.fragment:fragment:1.3.0-alpha04`, `androidx.fragment:fragment-ktx:1.3.0-alpha04`, and `androidx.fragment:fragment-testing:1.3.0-alpha04` are released. [Version 1.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..942518f415d35ff9f2ff78f312c076c673468877/fragment)

**New Features**

- Added support for passing results between two Fragments via new APIs on `FragmentManager`. This works for hierarchy fragments (parent/child), DialogFragments, and fragments in Navigation and ensures that results are only sent to your Fragment while it is at least `STARTED`. ([b/149787344](https://issuetracker.google.com/issues/149787344))

**API Changes**

- The target fragment APIs have been deprecated. To pass data between fragments the new Fragment Result APIs should be used instead. ([b/149787344](https://issuetracker.google.com/issues/149787344))
- The `startActivityForResult()`/`onActivityResult()` and `requestPermissions()`/`onRequestPermissionsResult()` APIs on Fragment have been deprecated. Please use the [Activity Result APIs](https://developer.android.com/training/basics/intents/result). ([aosp/1290887](https://android-review.googlesource.com/1290887))
- **Breaking change** from [Activity `1.2.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha04): the `prepareCall()` method has been renamed to `registerForActivityResult()`. ([aosp/1278717](https://android-review.googlesource.com/1278717))

**Bug Fixes**

- The fragment's `getViewLifecycleOwner()` is now stopped before `onSaveInstanceState()` is called, mirroring the behavior of the fragment's lifecycle. ([b/154645875](https://issuetracker.google.com/issues/154645875))
- Calling `setMenuVisibility(false)` on a fragment now correctly changes the visibility of menus provided by its child fragments. ([b/153593580](https://issuetracker.google.com/issues/153593580))
- Fixed an `illegalStateException` when adding a fragment to a `DialogFragment`'s view hierarchy with `FragmentContainerView`. ([b/154366601](https://issuetracker.google.com/issues/154366601))
- The `getDefaultViewModelProviderFactory()` method on fragments no longer crashes when hosting your fragments outside of an activity. ([b/153762914](https://issuetracker.google.com/issues/153762914))

### Version 1.3.0-alpha03

April 1, 2020

`androidx.fragment:fragment:1.3.0-alpha03`, `androidx.fragment:fragment-ktx:1.3.0-alpha03`, and `androidx.fragment:fragment-testing:1.3.0-alpha03` are released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ba6efec9a86f20ddc75c8c2b132e009cfb6b1..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/fragment)

**API Changes**

- The `prepareCall` methods on `Fragment` are now `final`. ([b/152439361](https://issuetracker.google.com/issues/152439361))

**Bug Fixes**

- Fixed a regression introduced in [Fragment `1.3.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha02) when using `BottomSheetDialogFragment`. ([b/151652127](https://issuetracker.google.com/issues/151652127), [aosp/1263328](https://android-review.googlesource.com/1263328), [aosp/1265163](https://android-review.googlesource.com/1265163))
- Fixed a crash when using `prepareCall` from a fragment after a configuration change. ([b/152137004](https://issuetracker.google.com/issues/152137004))
- Fixed an issue where shared element and exit transitions are ignored when using `setTargetFragment()`. ([b/152023196](https://issuetracker.google.com/issues/152023196))
- From [Fragment `1.2.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.4): Updated the Fragment ProGuard rules to allow obfuscation of kept fragments. ([b/151605338](https://issuetracker.google.com/issues/151605338))
- From [Fragment `1.2.4`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.4): Disabled the `FragmentLiveDataObserve` Lint rule on `DialogFragment` classes as their lifecycle and view lifecycle are always in sync, making it safe to use either `this` or `viewLifecycleOwner` when calling `observe`. ([b/151765086](https://issuetracker.google.com/issues/151765086))

**Dependency Changes**

- Fragments depend on [Activity `1.2.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha03), which had significant improvements to the Activity Result API introduced in Activity `1.2.0-alpha02`.

### Version 1.3.0-alpha02

March 18, 2020

`androidx.fragment:fragment:1.3.0-alpha02`, `androidx.fragment:fragment-ktx:1.3.0-alpha02`, and `androidx.fragment:fragment-testing:1.3.0-alpha02` are released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..1e0ba6efec9a86f20ddc75c8c2b132e009cfb6b1/fragment)

**New Features**

- Added support for the `ActivityResultRegistry` API introduced in [Activity `1.2.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha02) to handle the `startActivityForResult()`+`onActivityResult()` as well as `requestPermissions()`+`onRequestPermissionsResult()` flows without overriding methods in your Fragment in addition to providing hooks for testing these flows. See the updated [Getting a Result from an Activity](https://developer.android.com/training/basics/intents/result). ([b/125158199](https://developer.android.com/issuetracker.google.com/issues/125158199))

**API Changes**

- `DialogFragment` now provides a constructor that takes a `@LayoutRes` that indicates the layout that `onCreateView()` should inflate by default. ([b/150327080](https://issuetracker.google.com/issues/150327080))
- The `onActivityCreated()` method is now deprecated. Code touching the fragment's view should be done in `onViewCreated()` (which is called immediately before `onActivityCreated()`) and other initialization code should be in `onCreate()`. To receive a callback specifically when the activity's `onCreate()` is complete, a `LifeCycleObserver` should be registered on the activity's `Lifecycle` in `onAttach()`, and removed once the `onCreate()` callback is received. ([b/144309266](https://issuetracker.google.com/issues/144309266))

**Bug Fixes**

- From [Fragment `1.2.3`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.3): Fixed a bug in `DialogFragment` that caused a `StackOverflowError` when calling `getLayoutInflater()` from within `onCreateDialog()`. ([b/117894767](https://issuetracker.google.com/issues/117894767), [aosp/1258664](https://android-review.googlesource.com/1258664))
- From [Fragment `1.2.3`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.3): Reduced the scope of Fragment's included ProGuard rules to ensure that unused Fragment classes can be stripped. ([b/149665169](https://issuetracker.google.com/issues/149665169))
- From [Fragment `1.2.3`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.3): Fixed false positives in the `UseRequireInsteadOfGet` Lint check when using a local variable name that shadowed the Kotlin property name. ([b/149891163](https://issuetracker.google.com/issues/149891163))
- From [Fragment `1.2.3`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.3): `FragmentContainerView` no longer throws an `UnsupportedOperationException` for using the incorrect constructor in layout preview. ([b/149707833](https://issuetracker.google.com/issues/149707833))

**Known Issues**

- `BottomSheetDialogFragment` no longer properly positions its dialog on the screen. ([b/151652127](https://issuetracker.google.com/issues/151652127))

### Version 1.3.0-alpha01

March 4, 2020

`androidx.fragment:fragment:1.3.0-alpha01`, `androidx.fragment:fragment-ktx:1.3.0-alpha01`, and `androidx.fragment:fragment-testing:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/905771170a6b905b05c195eb55273e8f0aade92b..666ae665acfcfa2a20eccc18e4494808169742f4/fragment)

**New Features**

- Added support for the `ViewTreeLifecycleOwner.get(View)` API added in [Lifecycle `2.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha01) such that it will return the Fragment's [`viewLifecycleOwner`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getViewLifecycleOwner()) as the `LifecycleOwner` for any Views returned by `onCreateView()`. ([aosp/1182955](https://android-review.googlesource.com/1182955))

**API Changes**

- The `setRetainInstance()` method on Fragments has been deprecated. With the introduction of [ViewModels](https://developer.android.com/topic/libraries/architecture/viewmodel), developers have a specific API for retaining state that can be associated with Activities, Fragments, and Navigation graphs. This allows developers to use a normal, not retained Fragment and keep the specific state they want retained separate, avoiding a common source of leaks while maintaining the useful properties of a single creation and destruction of the retained state (namely, the constructor of the `ViewModel` and the `onCleared()` callback it receives). ([b/143911815](https://issuetracker.google.com/issues/143911815))
- With the release of [ViewPager2 `1.0.0`](https://developer.android.com/jetpack/androidx/releases/viewpager2#1.0.0), the `FragmentPagerAdapter` and `FragmentStatePagerAdapter` classes for interacting with `ViewPager` have been deprecated. See [Migrate from ViewPager to ViewPager2](https://developer.android.com/training/animation/vp2-migration). ([b/145132715](https://issuetracker.google.com/issues/145132715))

**Bug Fixes**

- Fragment ProGuard rules now correctly only keep the default constructors `Fragment` classes that are used rather than for all `Fragment` instances, fixing a regression introduced in [Fragment `1.2.1`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.1). ([b/149665169](https://issuetracker.google.com/issues/149665169)
- The `require___()` Lint rules added in [Fragment `1.2.2`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.2) no longer false positive on local variables that share the same name as the shadowed Kotlin property names (i.e., `view`). ([b/149891163](https://issuetracker.google.com/issues/149891163))
- `FragmentContainerView` no longer throws an `UnsupportedOperationException` when using the layout preview in Android Studio. ([b/149707833](https://issuetracker.google.com/issues/149707833))
- Fixed an issue where retained fragments that were added after the state is saved would not be continually recreated and then destroyed after each configuration change. ([b/145832397](https://issuetracker.google.com/issues/145832397))

## Version 1.2.5

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.5

June 10, 2020

`androidx.fragment:fragment:1.2.5`, `androidx.fragment:fragment-ktx:1.2.5`, and `androidx.fragment:fragment-testing:1.2.5` are released. [Version 1.2.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f1113dbc41d1678cef9a13711434b9640729ccd..1fa73cb2d5a51ba9016a9d7f8cf80e04ad50f528/fragment)

**Bug Fixes**

- The fragment's `getViewLifecycleOwner()` is now stopped before `onSaveInstanceState()` is called, mirroring the behavior of the fragment's lifecycle. This was previously released in [Fragment `1.3.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha04). ([b/154645875](https://issuetracker.google.com/issues/154645875))
- Calling `setMenuVisibility(false)` on a fragment now correctly changes the visibility of menus provided by its child fragments. This was previously released in [Fragment `1.3.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha04). ([b/153593580](https://issuetracker.google.com/issues/153593580))

## Version 1.2.4

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.4

April 1, 2020

`androidx.fragment:fragment:1.2.4`, `androidx.fragment:fragment-ktx:1.2.4`, and `androidx.fragment:fragment-testing:1.2.4` are released. [Version 1.2.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bb33dc2112f153d6d7ae15a267d2acd7ac53dabb..1f1113dbc41d1678cef9a13711434b9640729ccd/fragment)

**Bug Fixes**

- Updated the Fragment ProGuard rules to allow obfuscation of kept fragments. ([b/151605338](https://issuetracker.google.com/issues/151605338))
- Disabled the `FragmentLiveDataObserve` Lint rule on `DialogFragment` classes as their lifecycle and view lifecycle are always in sync, making it safe to use either `this` or `viewLifecycleOwner` when calling `observe`. ([b/151765086](https://issuetracker.google.com/issues/151765086))

## Version 1.2.3

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.3

March 18, 2020

`androidx.fragment:fragment:1.2.3`, `androidx.fragment:fragment-ktx:1.2.3`, and `androidx.fragment:fragment-testing:1.2.3` are released. [Version 1.2.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9598eb9e7eaf8411e0433c8b5fc5a5bc8abc096a..bb33dc2112f153d6d7ae15a267d2acd7ac53dabb/fragment)

**Bug Fixes**

- Fixed a bug in `DialogFragment` that caused a `StackOverflowError` when calling `getLayoutInflater()` from within `onCreateDialog()`. ([b/117894767](https://issuetracker.google.com/issues/117894767), [aosp/1258665](https://android-review.googlesource.com/1258665))
- Reduced the scope of Fragment's included ProGuard rules to ensure that unused Fragment classes can be stripped. ([b/149665169](https://issuetracker.google.com/issues/149665169))
- Fixed false positives in the `UseRequireInsteadOfGet` Lint check when using a local variable name that shadowed the Kotlin property name. ([b/149891163](https://issuetracker.google.com/issues/149891163))
- `FragmentContainerView` no longer throws an `UnsupportedOperationException` for using the incorrect constructor in layout preview. ([b/149707833](https://issuetracker.google.com/issues/149707833))

## Version 1.2.2

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.2

February 19, 2020

`androidx.fragment:fragment:1.2.2`, `androidx.fragment:fragment-ktx:1.2.2`, and `androidx.fragment:fragment-testing:1.2.2` are released. [Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b27fe92ff55203b778e3201a949a85c7c6c1bf76..9598eb9e7eaf8411e0433c8b5fc5a5bc8abc096a/fragment)

**New Lint checks**

- Lint suggests using the `viewLifecycleOwner` as the `LifecycleOwner` to calls into `OnBackPressedDispatcher` in `onCreateView()`, `onViewCreated()`, and `onActivityCreated()`. ([b/142117657](https://issuetracker.google.com/issues/142117657))
- Added a new Lint check that confirms that you are using the correct `debugImplementation` when using the `fragment-testing` artifact. ([b/141500106](https://issuetracker.google.com/issues/141500106))
- Fragments now suggest using the associated `require___()` methods for more descriptive error messages instead of `checkNotNull(get___())`, `requireNonNull(get___())`, or `get___()!!` for all of the Fragment APIs that include both a `get` and `require` equivalent. ([aosp/1202883](https://android-review.googlesource.com/1202883))

**Bug Fixes**

- Fixed the Fragment ProGuard files to avoid R8 warnings ([b/148963981](https://issuetracker.google.com/issues/148963981))
- Improved the existing Lint check suggesting using `viewLifecycleOwner` when using `observe` to also handle the `livedata-ktx` extension method version of `observe`. ([b/148996309](https://issuetracker.google.com/issues/148996309))
- Fixed the formatting for many of the Lint checks ([aosp/1157012](https://android-review.googlesource.com/1157012))

**External contributions**

- Thanks to Zac Sweers for contributing the `require___()` Lint checks on behalf of Slack! ([aosp/1202883](https://android-review.googlesource.com/1202883))

## Version 1.2.1

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.1

February 5, 2020

`androidx.fragment:fragment:1.2.1`, `androidx.fragment:fragment-ktx:1.2.1`, and `androidx.fragment:fragment-testing:1.2.1` are released. [Version 1.2.1 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/905771170a6b905b05c195eb55273e8f0aade92b..b27fe92ff55203b778e3201a949a85c7c6c1bf76/fragment).

**Bug fixes**

- Fragments added via the `add` and `replace` methods that take a `Class` instance (or the Kotlin reified versions) now have their default constructor kept by ProGuard. ([b/148181315](https://issuetracker.google.com/issues/148181315))
- `FragmentStatePagerAdapter` and `FragmentPagerAdapter` no longer catch exceptions thrown by `FragmentManager` when running `finishUpdate()`. ([aosp/1208711](https://android-review.googlesource.com/1208711/))
- Fixed an issue where `FragmentManager.findFragment()` did not work with fragments added via the `<fragment>` tag. ([b/147784323](https://issuetracker.google.com/issues/147784323))
- Fragments inflated using the `<fragment>` tag now always receive a call to `onInflate()` before `onCreate()` when in the layout. ([aosp/1215856](https://android-review.googlesource.com/1215856/))
- Calling `toString()` on a `FragmentManager` instance no longer throws a `NullPointerException` when the Activity is already destroyed. ([b/148189412](https://issuetracker.google.com/issues/148189412))

**Dependency changes**

- Fragments `1.2.1` now depends on [Lifecycle ViewModel SavedState `2.2.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#viewmodel-savedstate-2.2.0).

## Version 1.2.0

| **Note:** The Kotlin dependant libraries of this version (`fragment-ktx`,`fragment-testing`) target Java 8 programming language bytecode. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

### Version 1.2.0

January 22, 2020

`androidx.fragment:fragment:1.2.0`, `androidx.fragment:fragment-ktx:1.2.0`, and `androidx.fragment:fragment-testing:1.2.0` are released. [Version 1.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/52c5cbd1c318a40cad51528d31aa6535f1ab38fe..905771170a6b905b05c195eb55273e8f0aade92b/fragment).

**Important changes since 1.1.0**

- **FragmentContainerView** : The `FragmentContainerView` is the strongly recommended container for dynamically added Fragments, replacing usage of `FrameLayout` or other layouts. It also supports the same `class`, `android:name`, and optional `android:tag` as the `<fragment>` tag, but uses a normal `FragmentTransaction` to add this initial fragment, instead of the custom code path used by `<fragment>`.
- **`onDestroyView()` timing** : Fragments now wait for exit animations, exit framework transitions, and exit AndroidX transitions (when using [Transition `1.3.0`](https://developer.android.com/jetpack/androidx/releases/transition#version_130_2)) to complete before calling `onDestroyView()`.
- **Class based `add()` and `replace()`** : Added new overloads of `add()` and `replace()` on `FragmentTransaction` that take a `Class<? extends Fragment>` and optional `Bundle` of arguments. These methods use your `FragmentFactory` to construct an instance of the Fragment to add. Kotlin extensions that use reified types (i.e, `fragmentTransaction.replace<YourFragment>(R.id.container)`) have also been added to `fragment-ktx`.
- **Lifecycle ViewModel SavedState Integration** : `SavedStateViewModelFactory` is now the default factory used when using `by viewModels()`, `by activityViewModels()`, the `ViewModelProvider` constructor, or `ViewModelProviders.of()` with a Fragment.
- **New Lint checks** : Added a new Lint check that ensures you are using `getViewLifecycleOwner()` when observing `LiveData` from `onCreateView()`, `onViewCreated()`, or `onActivityCreated()`.
- **`getFragmentManager()` deprecation** : The `getFragmentManager()` and `requireFragmentManager()` methods on Fragment have been deprecated and replaced with a single `getParentFragmentManager()` method, which returns the non-null `FragmentManager` the Fragment is added to (you can use `isAdded()` to determine if it is safe to call).
- **`FragmentManager.enableDebugLogging()` deprecation** : The static `FragmentManager.enableDebugLogging` method has been deprecated. FragmentManager now respects [`Log.isLoggable()`](https://developer.android.com/reference/android/util/Log#isLoggable(java.lang.String,%20int)) for the tag `FragmentManager`, allowing you to enable either `DEBUG` or `VERBOSE` logging without re-compiling your app.

**Known Issues**

- Fragments referenced only via the `class` or `android:name` attribute on a `FragmentContainerView` are not kept by ProGuard automatically, requiring that you manually add a keep rule for each fragment class. ([b/142601969](https://issuetracker.google.com/issues/142601969))
- When adding a `NavHostFragment` using `class` or `android:name` in XML with `FragmentContainerView`, you cannot use `findNavController()` in `onCreate()` of your Activity. ([b/142847973](https://issuetracker.google.com/issues/142847973))

### Version 1.2.0-rc05

January 8, 2020

`androidx.fragment:fragment:1.2.0-rc05`, `androidx.fragment:fragment-ktx:1.2.0-rc05`, and `androidx.fragment:fragment-testing:1.2.0-rc05` are released. [Version 1.2.0-rc05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/51813e9145ac8b1ed7f01f3b8dc6741abc937079..52c5cbd1c318a40cad51528d31aa6535f1ab38fe/fragment).

**Bug fixes**

- Fixed a regression in Fragment `1.2.0-rc04` when using the `<fragment>` tag which caused `onViewCreated()` to be called incorrectly during activity destruction. ([b/146290333](https://issuetracker.google.com/issues/146290333))
- Fragments added with the `<fragment>` tag now properly have their non-config cleared even when they are only sometimes in the layout (i.e., only in your landscape layout). As a consequence, these Fragments are now correctly moved to `CREATED` even when not in your layout instead of being instantiated but never moving through any lifecycle methods. ([b/145769287](https://issuetracker.google.com/issues/145769287))

### Version 1.2.0-rc04

December 18, 2019

`androidx.fragment:fragment:1.2.0-rc04`, `androidx.fragment:fragment-ktx:1.2.0-rc04`, and `androidx.fragment:fragment-testing:1.2.0-rc04` are released. [Version 1.2.0-rc04 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0754f64b25856c50be34974ca8081be31c1b8b2f..51813e9145ac8b1ed7f01f3b8dc6741abc937079/fragment).

**Bug fixes**

- Adjusted the animations for `TRANSIT_FRAGMENT_OPEN`, `TRANSIT_FRAGMENT_CLOSE`, and `TRANSIT_FRAGMENT_FADE` to avoid visual issues. ([b/145468417](https://issuetracker.google.com/issues/145468417))

### Version 1.2.0-rc03

December 4, 2019

`androidx.fragment:fragment:1.2.0-rc03`, `androidx.fragment:fragment-ktx:1.2.0-rc03`, and `androidx.fragment:fragment-testing:1.2.0-rc03` are released. [Version 1.2.0-rc03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/daa892ee7bce89afe2ab151da444916753225de8..0754f64b25856c50be34974ca8081be31c1b8b2f/fragment).

**Bug fixes**

- Fixed an unintentional behavior change where Fragments who have been removed are still returned by `findFragmentById()` / `findFragmentByTag()` while their exit animations/transitions run. ([b/143982969](https://issuetracker.google.com/issues/143982969), [aosp/1167585](https://android-review.googlesource.com/c/platform/frameworks/support/+/1167585))
- Child fragments are now correctly stopped before their parents when the containing activity calls `onSaveInstanceState()`. ([b/144380645](https://issuetracker.google.com/issues/144380645))
- Fixed an issue where Views were incorrectly marked `INVISIBLE` after popping a hidden Fragment. ([b/70793925](https://issuetracker.google.com/issues/70793925))
- Fragment shared element transitions now handle Views that have been rotated, scaled, etc. ([b/142835261](https://issuetracker.google.com/issues/142835261))

**Documentation Updates**

- Clarified the deprecation documentation around `setUserVisibleHint()`. ([b/143897055](https://issuetracker.google.com/issues/143897055))
- Improved the documentation on `setFragmentFactory()` and `getFragmentFactory()` to better indicate that setting a `FragmentFactory` will also affect child FragmentManagers. ([aosp/1170095](https://android-review.googlesource.com/c/platform/frameworks/support/+/1170095))

**Dependency changes**

- Fragments now depends on Lifecycle `2.2.0-rc03`, Lifecycle ViewModel SavedState `1.0.0-rc03`, and Activity `1.1.0-rc03`.

### Version 1.2.0-rc02

November 7, 2019

`androidx.fragment:fragment:1.2.0-rc02`, `androidx.fragment:fragment-ktx:1.2.0-rc02`, and `androidx.fragment:fragment-testing:1.2.0-rc02` are released. [Version 1.2.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b36efec9f0fbc815605584732e6e2b59b7fd0575..daa892ee7bce89afe2ab151da444916753225de8/fragment).

**Bug fixes**

- When in Kotlin, the LintFix for using `getViewLifecycleOwner()` when observing `LiveData` from `onCreateView()`, `onViewCreated()`, or `onActivityCreated()` (introduced in [Fragment `1.2.0-rc01`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-rc01)) now uses the Kotlin property access syntax `viewLifecycleOwner` instead of `getViewLifecycleOwner()`. ([aosp/1143821](https://android-review.googlesource.com/1143821))

### Version 1.2.0-rc01

October 23, 2019

`androidx.fragment:fragment:1.2.0-rc01`, `androidx.fragment:fragment-ktx:1.2.0-rc01`, and `androidx.fragment:fragment-testing:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/50959249335066aab14331fa93c0fa132cc00deb..b36efec9f0fbc815605584732e6e2b59b7fd0575/fragment).

**New features**

- `FragmentContainerView` now supports the `class` attribute in addition to `android:name`, mirroring the functionality of the `<fragment>` tag. ([b/142722242](https://issuetracker.google.com/issues/142722242))
- Added a new Lint check that ensures you are using `getViewLifecycleOwner()` when observing `LiveData` from `onCreateView()`, `onViewCreated()`, or `onActivityCreated()`. ([b/137122478](https://issuetracker.google.com/issues/137122478))

**Bug fixes**

- The `onDismiss` and `onCancel` callbacks on `DialogFragment` now guarantee that the `DialogInterface` passed to them is non-null and that `getDialog()` returns non-null when they are executed. ([b/141974033](https://issuetracker.google.com/issues/141974033))
- `FragmentContainerView` now adds the Fragment defined by `class` or `android:name` as part of inflation, ensuring that `findFragmentById()` and `findFragmentByTag()` work immediately afterwards. ([b/142520327](https://issuetracker.google.com/issues/142520327))
- Fixed an `IllegalStateException` in `FragmentContainerView` due to the state being saved. ([b/142580713](https://issuetracker.google.com/issues/142580713))
- Fixed an `UnsupportedOperationException` in `FragmentContainerView` when the `FragmentContainerView` class is obfuscated. ([b/142657034](https://issuetracker.google.com/issues/142657034))

**Known issues**

- Fragments referenced only via the `class` or `android:name` attribute on a `FragmentContainerView` are not kept by ProGuard automatically, requiring that you manually add a keep rule for each fragment class. We have disabled the Lint rule suggesting moving to `FragmentContainerView` until this is fixed via `aapt2`. ([b/142601969](https://issuetracker.google.com/issues/142601969))

### Version 1.2.0-beta02

October 11, 2019

`androidx.fragment:fragment:1.2.0-beta02`, `androidx.fragment:fragment-ktx:1.2.0-beta02`, and `androidx.fragment:fragment-testing:1.2.0-beta02` are released. [Version 1.2.0-beta02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/20f7c62349217f2b3f79a3c7548b2331235de42c..50959249335066aab14331fa93c0fa132cc00deb/fragment).

**Bug fixes**

- Fixed an issue where Fragment's `onInflate()` did not receive proper attributes from `FragmentContainerView`, breaking cases such as `NavHostFragment`. ([b/142421837](https://issuetracker.google.com/issues/142421837))

### Version 1.2.0-beta01

October 9, 2019

`androidx.fragment:fragment:1.2.0-beta01`, `androidx.fragment:fragment-ktx:1.2.0-beta01`, and `androidx.fragment:fragment-testing:1.2.0-beta01` are released. [Version 1.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/1d4e6911dcf86c2b56d96037e56d0bbe4552732f..20f7c62349217f2b3f79a3c7548b2331235de42c/fragment).

**New features**

- `FragmentContainerView` adds support for adding an initial fragment with added support for the `android:name` and optional `android:tag` XML attributes. Unlike the `<fragment>` tag, `FragmentContainerView` uses a normal `FragmentTransaction` under the hood to add the initial fragment, allowing further `FragmentTransaction` operations on the `FragmentContainerView` and enables the usage of View Binding for the layout. ([b/139830628](https://issuetracker.google.com/issues/139830628), [b/141177981](https://issuetracker.google.com/issues/141177981))
- Fragments now contains a Lint warning offering a quick fix to replace `<fragment>` with `FragmentContainerView`. ([b/139830056](https://issuetracker.google.com/issues/139830056))

**Bug fixes**

- Fixed a `ClassCastException` when using `androidx.transition`. ([b/140680619](https://issuetracker.google.com/issues/140680619))
- When using [Transition `1.3.0-beta01`](https://developer.android.com/jetpack/androidx/releases/transition#1.3.0-beta01), Fragments now wait for `androidx.transition` transitions (in addition to framework transitions and animations, which were fixed in [Fragment `1.2.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-alpha03) and [Fragment `1.2.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-alpha02), respectively) to finish before dispatching `onDestroyView()`. ([aosp/1119841](https://android-review.googlesource.com/1119841))
- When using [Transition `1.3.0-beta01`](https://developer.android.com/jetpack/androidx/releases/transition#1.3.0-beta01), Fragments now properly cancel `androidx.transition` transitions before starting new transitions / animations on the same container. ([aosp/1119841](https://android-review.googlesource.com/1119841))
- Fixed an issue on API 17 and lower when using `androidx.transition` transitions on the root view of your Fragment when using `FragmentContainerView`. ([b/140361893](https://issuetracker.google.com/issues/140361893))
- The `fragment-testing` artifact now depends on AndroidX Test `1.2.0`, fixing an incompatibility with the latest Espresso 3.2.0. ([b/139100149](https://issuetracker.google.com/issues/139100149))
- Removed usage of `Log.w` in FragmentManager. ([aosp/1126468](https://android-review.googlesource.com/1126468))

**Known issues**

- Fragment's `onInflate()` do not receive proper attributes from `FragmentContainerView`, breaking cases such as `NavHostFragment`. ([b/142421837](https://issuetracker.google.com/issues/142421837))

### Version 1.2.0-alpha04

September 18, 2019

`androidx.fragment:fragment:1.2.0-alpha04`, `androidx.fragment-ktx:example:1.2.0-alpha04`, and `androidx.fragment:fragment-testing:1.2.0-alpha04` are released. [Version 1.2.0-alpha04 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/8e4aaeee0302e90400b8aa995dbbc220aa5dfe21..6e3bf267861f1dffb15c0ceff82f553a658c9972/fragment).

**API changes**

- The `getFragmentManager()` and `requireFragmentManager()` methods on `Fragment` have been deprecated and replaced with a single `getParentFragmentManager()` method, which returns the non-null `FragmentManager` the Fragment is added to (you can use `isAdded()` to determine if it is safe to call). ([b/140574496](https://issuetracker.google.com/issues/140574496))
- The static `FragmentManager.enableDebugLogging` method has been deprecated. FragmentManager now respects [`Log.isLoggable()`](https://developer.android.com/reference/android/util/Log#isLoggable(java.lang.String,%20int)) for the tag `FragmentManager`, allowing you to enable either `DEBUG` or `VERBOSE` logging without re-compiling your app. ([aosp/1116591](https://android-review.googlesource.com/1116591))

**Bug fixes**

- Fragments are now properly destroyed while exit animations on other fragments are running. ([b/140574199](https://issuetracker.google.com/issues/140574199))
- Fixed an issue where Fragments would call `Activity.findViewById()` where before it did not. ([aosp/1116431](https://android-review.googlesource.com/1116431))

### Version 1.2.0-alpha03

September 5, 2019

`androidx.fragment:fragment:1.2.0-alpha03`, `androidx.fragment:fragment-ktx:1.2.0-alpha03`, and `androidx.fragment:fragment-testing:1.2.0-alpha03` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/b4eddfd7b427a4a334dceb6e0fb600de38ccdd4f..8e4aaeee0302e90400b8aa995dbbc220aa5dfe21/fragment).

**API changes**

- `FragmentContainerView` is now `final`. ([b/140133091](https://issuetracker.google.com/issues/140133091))

**Bug fixes**

- `FragmentContainerView` now properly reverses the draw order when popping fragments off the back stack. ([b/139104187](https://issuetracker.google.com/issues/139104187))
- Fixed an issue where the wrong animation would run when both popping a fragment and adding a new fragment at the same time. ([b/111659726](https://issuetracker.google.com/issues/111659726))
- Fragments now wait for transitions (in addition to animations, which was fixed in [Fragment `1.2.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-alpha02)) to finish before dispatching `onDestroyView()`. ([b/138741697](https://issuetracker.google.com/issues/138741697))

### Version 1.2.0-alpha02

August 7, 2019

`androidx.fragment:fragment:1.2.0-alpha02`, `androidx.fragment:fragment-ktx:1.2.0-alpha02`, and `androidx.fragment:fragment-testing:11.2.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/588801999e8e8ea9ec080a796f72fefa17f3cd3b..ece690f1fdb4481b47c5128fd21d88da7d6850a6/fragment).

**New features**

- `SavedStateViewModelFactory` is now the default factory used when using `by viewModels()`, `by activityViewModels()`, the `ViewModelProvider` constructor, or `ViewModelProviders.of()` with a `Fragment`. ([b/135716331](https://issuetracker.google.com/issues/135716331))
- The default animations when using `TRANSIT_FRAGMENT_OPEN`, `TRANSIT_FRAGMENT_CLOSE`, `TRANSIT_FRAGMENT_FADE` with `setTransition` on a `FragmentTransaction` have been updated to match the animations used by activities on Android 10 devices. ([aosp/1012812](https://android-review.googlesource.com/1012812), [aosp/1014730](https://android-review.googlesource.com/1014730))

**API changes**

- Introduces `FragmentContainerView` as the strongly recommended container for dynamically added Fragments, replacing usage of `FrameLayout`, etc. as it fixes animation z-ordering issues and window insets dispatching to Fragments. ([b/37036000](https://issuetracker.google.com/issues/37036000), [aosp/985243](https://android-review.googlesource.com/985243), [b/136494650](https://issuetracker.google.com/issues/136494650))
- Added a static `FragmentManager.findFragment(View)` method to retrieve the containing Fragment from a view inflated by a fragment. A Kotlin extension is also available in `fragment-ktx`. ([aosp/1090757](https://android-review.googlesource.com/1090757))
- Added new overloads of `add()` and `replace()` on `FragmentTransaction` that take a `Class<? extends Fragment>` and optional `Bundle` of arguments. These methods use your `FragmentFactory` to construct an instance of the Fragment to add. Kotlin extension that use reified types (i.e, `fragmentTransaction.replace<YourFragment>(R.id.container)`) have also been added to `fragment-ktx`. ([b/126124987](https://issuetracker.google.com/issues/126124987))
- `@MainThread` annotations have been added to `Fragment` lifecycle callbacks. ([b/127272564](https://issuetracker.google.com/issues/127272564))
- The breadcrumb title related APIs on `FragmentTransaction` and `FragmentManager.BackStackEntry` have been deprecated. ([b/138252944](https://issuetracker.google.com/issues/138252944))
- The `setTransitionStyle` method on `FragmentTransaction` has been deprecated. ([aosp/1011537](https://android-review.googlesource.com/1011537))
- Many of the methods in `FragmentManager` are no longer `abstract`. `FragmentManager` itself remains `abstract` and should not be directly instantiated or extended; you should continue to only get an existing instance from `getSupportFragmentManager()`, `getChildFragmentManager()`, etc.

**Bug fixes**

- From [Fragment `1.1.0-rc04`](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0-rc04): Fragments now correctly cancel postponed transitions on Fragments have been popped. ([b/138251858](https://issuetracker.google.com/issues/138251858))
- From [Fragment `1.1.0-rc03`](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0-rc03): Fixed an issue where calling `postponeEnterTransition()` with a timeout more than once would not cancel previous timeouts. ([b/137797118](https://issuetracker.google.com/issues/137797118))
- From [Fragment `1.1.0-rc02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0-rc02): Fixed a crash in `FragmentPagerAdapter` and `FragmentStatePagerAdapter` when removing the current item. ([b/137209870](https://issuetracker.google.com/issues/137209870))
- Fragments now wait for animations to finish before dispatching `onDestroyView()`. ([b/136110528](https://developer.android.com/issuetracker.google.com/issues/136110528))
- Fragment animations from child fragments and their descendants are now properly handled when animating the parent Fragment. ([b/116675313](https://developer.android.com/issuetracker.google.com/issues/116675313))
- Fixed a `NullPointerException` when using shared element transitions and combining a pop and add operation. ([b/120507394](https://issuetracker.google.com/issues/120507394))
- Added a workaround to `IllegalStateException`s when using `FragmentPagerAdapter` and `FragmentStatePagerAdapter` in Robolectric tests. ([b/137201343](https://issuetracker.google.com/issues/137201343))

### Version 1.2.0-alpha01

July 2, 2019

`androidx.fragment:fragment:1.2.0-alpha01`, `androidx.fragment:fragment-ktx:1.2.0-alpha01`, and `androidx.fragment:fragment-testing:1.2.0-alpha01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0491995874ce17bcaf19ad9864f5ec6a0ae1b46d..588801999e8e8ea9ec080a796f72fefa17f3cd3b/fragment).

**New features**

- FragmentManager now calls `requestApplyInsets()` after attaching the Fragment's view and directly before calling `onViewCreated()`, ensuring that your view always has the correct insets. ([b/135945162](https://issuetracker.google.com/issues/135945162))

**Bug fixes**

- Fixed a `NullPointerException` when popping a `FragmentTransaction` that used `setPrimaryNavigationFragment()` before `replace()`. ([b/134673465](https://issuetracker.google.com/issues/134673465))

## Version 1.1.0

### Version 1.1.0

September 5, 2019

`androidx.fragment:fragment:1.1.0`, `androidx.fragment:fragment-ktx:1.1.0`, and `androidx.fragment:fragment-testing:1.1.0` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/f8b89aff336c926d3e9a661f497fa07db93e4283..0a0b85c233fab9c76d9bb2cd9e9b59bc0ffbe6c5/fragment).

**Important Changes since 1.0.0**

- **fragment-testing** : The `fragment-testing` artifact provides a `FragmentScenario` class for testing a fragment in isolation. See [Test your app's fragments documentation](https://developer.android.com/training/basics/fragments/testing) for more details.
- **FragmentFactory** : You can now set a `FragmentFactory` on a `FragmentManager` to manage the creation of fragment instances, removing the strict requirement to have a no-argument constructor.
- **Kotlin Property Delegates for ViewModels** : The `fragment-ktx` artifact now contains two Kotlin property delegates: `by viewModels()` for accessing ViewModels associated with the individual fragment and `by activityViewModels()` for accessing ViewModels scoped to the activity.
- **Max Lifecycle** : You can now set a max Lifecycle state for a Fragment by calling `setMaxLifecycle()` on a `FragmentTransaction`. This replaces the now deprecated `setUserVisibleHint()`. `FragmentPagerAdapter` and `FragmentStatePagerAdapter` have a new constructor that allows you to switch to the new behavior.
- **FragmentActivity LayoutId constructor** : Subclasses of `FragmentActivity` can now optionally call into a constructor on `FragmentActivity` that takes an `R.layout` ID, indicating the layout that should be set as the content view as an alternative to calling `setContentView()` in `onCreate()`. This does not change the requirement that your subclass have a no-argument constructor.
- **Fragment LayoutId constructor** : Subclasses of `Fragment` can now optionally call into a constructor on `Fragment` that takes an `R.layout` ID, indicating the layout that should be used for this fragment as an alternative to overriding `onCreateView()`. The inflated layout can be configured in `onViewCreated()`.
- **Postpone with a timeout** : A new overload of `postponeEnterTransition()` has been added that takes a timeout.

### Version 1.1.0-rc04

August 7, 2019

`androidx.fragment:fragment:1.1.0-rc04`, `androidx.fragment:fragment-ktx:1.1.0-rc04`, and `androidx.fragment:fragment-testing:1.1.0-rc04` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/fb2e8b50c7c18c54f770ad7544287ef9a260ec01..f8b89aff336c926d3e9a661f497fa07db93e4283/fragment).

**Bug fixes**

- Fragments now correctly cancel postponed transitions on Fragments have been popped. ([b/138251858](https://issuetracker.google.com/issues/138251858))

### Version 1.1.0-rc03

July 19, 2019

`androidx.fragment:fragment:1.1.0-rc03`, `androidx.fragment:fragment-ktx:1.1.0-rc03`, and `androidx.fragment:fragment-testing:1.1.0-rc03` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/16e3ea9c8519ff086ea5f0bbc4d6fa84743e87f1..fb2e8b50c7c18c54f770ad7544287ef9a260ec01/fragment).

**Bug fixes**

- Fixed an issue where calling `postponeEnterTransition()` with a timeout more than once would not cancel previous timeouts. ([b/137797118](https://issuetracker.google.com/issues/137797118))

### Version 1.1.0-rc02

July 17, 2019

`androidx.fragment:fragment:1.1.0-rc02`, `androidx.fragment:fragment-ktx:1.1.0-rc02`, and `androidx.fragment-testing:fragment:1.1.0-rc02` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/31e072b23ddd65615efc5f3fbece2276b6b5cae4..16e3ea9c8519ff086ea5f0bbc4d6fa84743e87f1/fragment).

**Bug fixes**

- Fixed a crash in `FragmentPagerAdapter` and `FragmentStatePagerAdapter` when removing the current item. ([b/137209870](https://issuetracker.google.com/issues/137209870))

### Version 1.1.0-rc01

July 2, 2019

`androidx.fragment:fragment:1.1.0-rc01`, `androidx.fragment:fragment-ktx:1.1.0-rc01`, and `androidx.fragment:fragment-testing:1.1.0-rc01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0491995874ce17bcaf19ad9864f5ec6a0ae1b46d..31e072b23ddd65615efc5f3fbece2276b6b5cae4/fragment).

**Bug fixes**

- Fragments now properly update their visibility when using `show()` or `hide()` operations while the transition is running. ([b/133385058](https://issuetracker.google.com/issues/133385058))
- Fixed a `NullPointerException` when popping a `FragmentTransaction` that used `setPrimaryNavigationFragment()` before `replace()`. ([b/134673465](https://issuetracker.google.com/issues/134673465))

### Version 1.1.0-beta01

June 5, 2019

`androidx.fragment:fragment:1.1.0-beta01`, `androidx.fragment:fragment-ktx:1.1.0-beta01`, and `androidx.fragment:fragment-testing:1.1.0-beta01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/ff4d74c16caf828426d4e6dd8e2d22db9f1be303..b74c465a858f50f5733ec376b2817d240e619b16/fragment).

**Bug fixes**

- `androidx.lifecycle.Lifecycle` callbacks (specifically related to `STARTED`, `RESUMED`, `PAUSED`, `STOPPED`, and `DESTROYED`) for nested Fragments are now properly nested. ([b/133497591](https://issuetracker.google.com/issues/133497591))
- `OnBackPressedCallback` instances registered in a Fragment's `onCreate()` now properly take precedence over the child FragmentManager. ([b/133175997](https://issuetracker.google.com/issues/133175997))
- Child fragments are no longer animated when their parent fragment is being replaced. ([b/121017790](https://issuetracker.google.com/issues/121017790))
- Fragments animations and transitions are now ignored when using `animateLayoutChanges="true"`, fixing an issue where Fragments were not properly destroyed. ([b/116257087](https://issuetracker.google.com/issues/116257087))

### Version 1.1.0-alpha09

May 16, 2019

`androidx.fragment:fragment:1.1.0-alpha09`, `androidx.fragment:fragment-ktx:1.1.0-alpha09`, and `androidx.fragment:fragment-testing:1.1.0-alpha09` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/948d2294e7ae482dffa9641ec0fb0cbb3412481a..ff4d74c16caf828426d4e6dd8e2d22db9f1be303/fragment).

**API changes**

- Fragments now receive a callback to a new `onPrimaryNavigationFragmentChanged(boolean)` method when the primary navigation fragment changes. [aosp/960857](https://android-review.googlesource.com/960857)

**Bug fixes**

- Menu Items inflated by a child Fragment are now correctly removed when the Parent Fragment is removed. [b/131581013](https://issuetracker.google.com/issues/131581013)

### Version 1.1.0-alpha08

May 7, 2019

`androidx.fragment:fragment:1.1.0-alpha08`, `androidx.fragment:fragment-ktx:1.1.0-alpha08`, and `androidx.fragment:fragment-testing:1.1.0-alpha08` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0fe6b4168055f8da37c439dc82fbc535a9e1987a..948d2294e7ae482dffa9641ec0fb0cbb3412481a/fragment).

This release is incompatible with Preferences 1.1.0-alpha01 through 1.1.0-alpha04. Please upgrade to Preferences 1.1.0-alpha05 when using this version of Fragments.

**New features**

- Added a new overload of `postponeEnterTransition()` that takes a timeout, after which the Fragment will automatically call `startPostponedEnterTransition()` [b/120803208](https://issuetracker.google.com/issues/120803208)

**API changes**

- Breaking change: the previously deprecated `FragmentFactory` `instantiate` method that took a `Bundle` has been removed. [aosp/953856](https://android-review.googlesource.com/953856)
- Breaking change: The `RESUME_ONLY_CURRENT_FRAGMENT` and `USE_SET_USER_VISIBLE_HINT` constants in `FragmentPagerAdapter` and `FragmentStatePagerAdapter` have been renamed to `BEHAVIOR_RESUME_ONLY_CURRENT_FRAGMENT` and `BEHAVIOR_SET_USER_VISIBLE_HINT`, respectively. [aosp/954782](https://android-review.googlesource.com/954782)

**Bug fixes**

- Fragments that have had their lifecycle capped via `setMaxLifecycle()` no longer get resumed before reaching their final state. [b/131557151](https://issuetracker.google.com/issues/131557151)
- When using `setMaxLifecycle(Lifecycle.State.CREATED)`, Fragments will properly have their view destroyed. [aosp/954180](https://android-review.googlesource.com/954180)

### Version 1.1.0-alpha07

April 25, 2019

`androidx.fragment:fragment:1.1.0-alpha07`, `androidx.fragment:fragment-ktx:1.1.0-alpha07`, and `androidx.fragment:fragment-testing:1.1.0-alpha07` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/ea6ef7b3e86be09ad7380887c0ddada0064cdee5..1d1a928881b4a7a75a85ab5b723cc81c829f1c83/fragment).

**New features**

- You can now set a max Lifecycle state for a Fragment by calling `setMaxLifecycle()` on a `FragmentTransaction`. This replaces the now deprecated `setUserVisibleHint()`. `FragmentPagerAdapter` and `FragmentStatePagerAdapter` have a new constructor that allows you to switch to the new behavior. ([b/129780800](https://issuetracker.google.com/issues/129780800))

**API Changes**

- `moveToState(STARTED)` on `FragmentScenario` can now only be called on API 24+ devices. ([b/129880016](https://issuetracker.google.com/issues/129880016))

**Behavior Changes**

- As a consequence of ([b/129907905](https://issuetracker.google.com/issues/129907905)), fragments on the back stack will **not** get a callback to `onCreateView()` when the hosting activity is recreated. `onCreateView()` will now only be called when the fragment becomes visible (i.e., the back stack is popped).

**Bug fixes**

- Fixed an issue when using a `<fragment>` tag in XML and the `contentLayoutId` constructor of `FragmentActivity` or `AppCompatActivity`. ([b/129907905](https://issuetracker.google.com/issues/129907905))
- Corrected an issue where fragments on the back stack would not be moved to at least `CREATED` after a configuration change, causing ViewModels and child retained fragments to not be properly disposed. ([b/129593351](https://issuetracker.google.com/issues/129593351))
- Fixed a crash in `restoreSaveState` caused by a desync of the retained fragments after the instance state is saved. ([b/130433793](https://issuetracker.google.com/issues/130433793)) ([aosp/947824](https://android-review.googlesource.com/947824))
- Fixed issues where an `OnBackPressedCallback` added with a fragment lifecycle would not be called if the `FragmentManager` had a back stack. See [androidx.activity 1.0.0-alpha07](https://developer.android.com/jetpack/androidx/releases/activity#1.0.0-alpha07) for more details. ([aosp/948209](https://android-review.googlesource.com/948209))
- Fragments no longer enforce `LAYER_TYPE_HARDWARE` for animations. If you specifically need a hardware layer animation, please set it as part of your animation. ([b/129486478](https://issuetracker.google.com/issues/129486478))

### Version 1.1.0-alpha06

April 3, 2019

`androidx.fragment:fragment:1.1.0-alpha06`, `androidx.fragment:fragment-ktx:1.1.0-alpha06`, and `androidx.fragment:fragment-testing:1.1.0-alpha06` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/4c34c957abe3a1cec4eb2342bb41a88c838999f7..ea6ef7b3e86be09ad7380887c0ddada0064cdee5/fragment).

**New features**

- Exceptions thrown by FragmentManager now include the Fragment's name in the message. ([b/67759402](https://issuetracker.google.com/issues/67759402))

**API Changes**

- `Fragment` and `FragmentActivity` now contain a second constructor that takes a `@LayoutRes int`, which replaces the previous behavior of annotating your class with `@ContentView`. This approach works in both app and library modules. ([b/128352521](https://issuetracker.google.com/issues/128352521))
- FragmentActivity's `onActivityResult()` is now properly marked as `@CallSuper`. ([b/127971684](https://issuetracker.google.com/issues/127971684))
- The FragmentFactory's `instantiate` method that takes an argument Bundle has been deprecated and apps should use the new `instantiate` overload that does not take a Bundle. ([b/128836103](https://issuetracker.google.com/issues/128836103))
- `FragmentScenario` methods are now properly annotated with `@StyleRes`. ([aosp/924193](https://android-review.googlesource.com/924193))
- `FragmentTabHost` has been deprecated. ([b/127971835](https://issuetracker.google.com/issues/127971835))
- FragmentActivity's `getThemedContext()` has been removed. ([aosp/934078](https://android-review.googlesource.com/934078))

**Bug fixes**

- Fixed a regression in 1.1.0-alpha05 that caused the incoming Fragment to flash on the screen. ([b/129405432](https://issuetracker.google.com/issues/129405432))
- Fixed an issue where the primary navigation fragment would be lost after a popBackStack+replace+popBackStack series of operations. ([b/124332597](https://issuetracker.google.com/issues/124332597))
- Fixed an issue when using `@ContentView` constructors on your Activity when restoring Fragment state. ([b/127313094](https://issuetracker.google.com/issues/127313094))
- Corrected the logic of `setTargetFragment()` when replacing an existing target Fragment with a Fragment not yet attached to the FragmentManager. ([aosp/932156](https://android-review.googlesource.com/932156/))

### Version 1.1.0-alpha05

March 13, 2019

`androidx.fragment:fragment:1.1.0-alpha05`, `androidx.fragment:fragment-ktx:1.1.0-alpha05`, and `androidx.fragment:fragment-testing:1.1.0-alpha05` are released. The full list of commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/e3951615d7fc9e64177ce46599a36fe1c26ac918..4c34c957abe3a1cec4eb2342bb41a88c838999f7/fragment).

**New features**

- `@ContentView` annotation lookups are now cached ([b/123709449](https://issuetracker.google.com/issues/123709449))

**Behavior changes**

- Calling `remove()`, `hide()`, `show()`, `detach()`, and `setPrimaryNavigationFragment()` with a Fragment attached to a different FragmentManager now throws an `IllegalStateException` rather than silently failing ([aosp/904301](https://android-review.googlesource.com/904301))

**Bug fixes**

- `onNewIntent` for `FragmentActivity` is now correctly marked with `@CallSuper` ([b/124120586](https://issuetracker.google.com/issues/124120586))
- Fixed an issue where `DialogFragment`'s `onDismiss()` could be called twice when using `getDialog().dismiss()` or `getDialog().cancel()` ([b/126563750](https://issuetracker.google.com/issues/126563750))

### Version 1.1.0-alpha04

February 7, 2019

`androidx.fragment:fragment 1.1.0-alpha04`, `androidx.fragment:fragment-ktx 1.1.0-alpha04`, and `androidx.fragment:fragment-testing 1.1.0-alpha04` are released.

**New features**

- Added support for the `@ContentView` class annotation that allows you to indicate which layout XML file should be inflated as an alternative to overriding `onCreateView()`. It is recommended to do view related work in `onViewCreated()`. ([aosp/837619](https://android-review.googlesource.com/837619))
- `fragment-testing` now depends on `androidx.test:core-ktx` 1.1.0 stable ([b/121209673](https://issuetracker.google.com/issues/121209673))
- You can now use `openActionBarOverflowOrOptionsMenu` with `FragmentScenario` to test Fragment hosted options menus ([b/121126668](https://issuetracker.google.com/issues/121126668))

**API changes**

- Added a `requireArguments()` method which returns a `@NonNull Bundle` or throws an `IllegalStateException` ([b/121196360](https://issuetracker.google.com/issues/121196360))
- Added a note that `getLifecycle()`, `getViewLifecycleOwner()`, and `getViewLifecycleOwnerLiveData()` should not be overridden and will be made final in a future release. Please [file a feature request](https://issuetracker.google.com/issues/new?component=460964) if you are currently overriding this method. ([aosp/880714](https://android-review.googlesource.com/880714))
- Added a note that `getViewModelStore()` should not be overridden and will be made final in a future release. Please [file a feature request](https://issuetracker.google.com/issues/new?component=460964) if you are currently overriding this method. ([aosp/880713](https://android-review.googlesource.com/880713))
- Fixed an issue with binary compatibility with previous releases of Fragments. ([aosp/887877](https://android-review.googlesource.com/887877)) ([aosp/889834](https://android-review.googlesource.com/889834))

**Bug fixes**

- Target fragments are correctly cleared out when you pass `null` to `setTargetFragment()`. ([aosp/849969](https://android-review.googlesource.com/849969))
- Fixed an issue where target Fragments were sometimes unavailable in or after `onDestroy()`. ([b/122312935](https://issuetracker.google.com/issues/122312935))
- DialogFragment's onDismiss() is now called before `onDestroy()`. ([aosp/874133](https://android-review.googlesource.com/874133)) ([aosp/890734](https://android-review.googlesource.com/890734))

### Version 1.1.0-alpha03

December 17, 2018

**New features**

- Fragment now implements `BundleSavedStateRegistryOwner` and depends on the newly released SavedState library \[[aosp/824380](https://android-review.googlesource.com/824380)\]
- A `by activityViewModels` Kotlin property delegate has been added to retrieve ViewModels associated with the containing Activity \[[b/119050253](https://issuetracker.google.com/issues/119050253)\]
- The `by viewModels` Kotlin property delegate has been expanded to take an optional lambda method for getting the `ViewModelStoreOwner`, allowing you to pass in the parent Fragment or other custom `ViewModelStoreOwner` with code such as `val viewModel: MyViewModel by viewModels(::requireParentFragment)` \[[b/119050253](https://issuetracker.google.com/issues/119050253)\]

**API changes**

- `FragmentScenario` now allows you to specify a theme such as `Theme.AppCompat` \[[b/119054431](https://issuetracker.google.com/issues/119054431)\]. This is a breaking change.
- Added a `requireView()` method which returns a `@NonNull View` or throws an `IllegalStateException` \[[b/120241368](https://issuetracker.google.com/issues/120241368)\]
- Added a `requireParentFragment()` method which returns a `@NonNull Fragment` or throws an `IllegalStateException` \[[b/112103783](https://issuetracker.google.com/issues/112103783)\]

**Bug fixes**

- Fixed IllegalStateException: Failure saving state [b/120814739](https://issuetracker.google.com/issues/120814739)
- Fragments being restored from saved instance state will now always receive a non-null `Bundle` \[[b/119794496](https://issuetracker.google.com/issues/119794496)\]
- Removed Fragments no longer reuse their `Lifecycle` object if re-added \[[b/118880674](https://issuetracker.google.com/issues/118880674)\]

### Version 1.1.0-alpha02

December 3, 2018

**New features**

- FragmentScenario's Kotlin extensions now let you use a lambda for Fragment construction as an alternative to passing in a `FragmentFactory` instance. ([aosp/812913](https://android-review.googlesource.com/c/platform/frameworks/support/+/812913))

**Bug fixes**

- Fixed an IllegalStateException when using nested Fragments on the back stack ([b/119256498](https://issuetracker.google.com/issues/119256498))
- Fixed crash when using `FragmentScenario.recreate()` with a `FragmentFactory` ([aosp/820540](https://android-review.googlesource.com/c/platform/frameworks/support/+/820540))
- Fixed an issue where target Fragments were not accessible after the Fragment was removed ([aosp/807634](https://android-review.googlesource.com/c/platform/frameworks/support/+/807634/))

### Version 1.1.0-alpha01

November 5, 2018

This is the first release of the
`fragment-testing` artifact and `FragmentScenario` which is built on top of the
androidx.test:core APIs. See the [Fragment testing documentation](https://developer.android.com/training/basics/fragments/testing) for more details.

**New features**

- New FragmentScenario class for testing Fragments in isolation.
- You can now set a `FragmentFactory` on any `FragmentManager` to control how new Fragment instances are instantiated.
- Added a new `by viewModels()` Kotlin property delegate for retrieving ViewModels from a Fragment.
- Pending input events (such as clicks) are now canceled in a Fragment's `onStop()`.

**API changes**

- Significantly expanded the nullability annotations across the Fragment API surface.

**Bug fixes**

- Fix an issue which caused Fragment operations to fail from within LiveData [(b/77944637)](https://issuetracker.google.com/issues/77944637)

**Known issues**

- Target Fragments cannot be accessed after a Fragment has been removed from the FragmentManager.
- `fragment-testing` depends on `androidx.test:core:1.0.0-beta01` instead of the correct `androidx.test:core:1.0.0`.