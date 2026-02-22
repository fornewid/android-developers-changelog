---
title: https://developer.android.com/guide/navigation/custom-back/support-animations
url: https://developer.android.com/guide/navigation/custom-back/support-animations
source: md.txt
---

When using the system back APIs, you can opt in to receive in-app animations and
support custom transitions.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/guide/navigation/custom-back/pb-cross-activity-and-back-to-home (1).mp4) and watch it with a video player. **Video 1:**Predictive back animations

After opting in, your app displays animations for back-to-home, cross-activity,
and cross-task.

You can also upgrade your material component dependency to v1.10.0 of MDC
Android to receive material component animations like the following:

- [Bottom sheets](https://m3.material.io/components/bottom-sheets/guidelines#3d7735e2-73ea-4f3e-bd42-e70161fc1085)
- [Side sheets](https://m3.material.io/components/side-sheets/guidelines#d77245e3-1013-48f8-a9d7-76f484e1be13)
- [Search](https://m3.material.io/components/search/guidelines#3f2d4e47-2cf5-4c33-b6e1-5368ceaade55)

See the [material component developer guidance on GitHub](https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md#predictive-back-material-components) for
more information.

The video shows a brief example of predictive back animations for
cross-activity and back-to-home using the Android Settings app.

1. In the animation, the user swipes back to return to the previous settings screen---an example of a cross-activity animation.
2. Now on the previous screen, the user begins swiping back a second time, showing a preview of the home screen with its wallpaper---an example of the back-to-home animation.
3. The user continues to swipe right, showing an animation of the window shrinking down to the icon on the home screen.
4. The user has now fully returned to the home screen.

Learn more about how to [Add support for predictive back gestures](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture).

## Add custom in-app transitions and animations

You can create custom in-app property animations and transitions, custom
cross-activity animations, and custom cross-fragment animations with predictive
back gestures.

### Add custom transitions using the Progress API

With AndroidX Activity 1.8.0-alpha01 or higher, you can use the Predictive Back
Progress APIs to develop custom animations for
the predictive back gesture in your app. Progress APIs are helpful in animating
views but have limitations when animating transitions between fragments. Within
[`OnBackPressedCallback`](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback)
we've introduced the
[`handleOnBackProgressed`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#handleOnBackPressed()),
[`handleOnBackCancelled`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#handleOnBackCancelled())
and
[`handleOnBackStarted`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#handleOnBackStarted(androidx.activity.BackEventCompat))
methods to animate objects while the user swipes back. Use these methods if you
need to customize more than the default animations provided by the system, or
the Material Component animations.

We expect most apps to use the backward compatible AndroidX APIs, but there are
also similar platform APIs within the
[`OnBackAnimationCallback`](https://developer.android.com/reference/kotlin/android/window/OnBackAnimationCallback)
interface available to test in Android 14 Developer Preview 1 and higher.
| **Note:** Learn how to [design custom in-app transitions and animations.](https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back).

#### Use the Progress APIs with AndroidX Transitions

Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/about/versions/14/images/predictive-back-transitions.mp4) and watch it with a video player.

The Progress APIs can be used with AndroidX Transitions 1.5.0-alpha01 or higher
on Android 14 and later to create Predictive Back transitions.

1. Use [`TransitionManager#controlDelayedTransition`](https://developer.android.com/reference/androidx/transition/TransitionManager#controlDelayedTransition(android.view.ViewGroup,androidx.transition.Transition)) instead of `beginDelayedTransition` to play transitions as the user swipes back.
2. Create the transition within `handleOnBackStarted`.
3. Play the transition with the back event within `handleOnBackProgressed` by relating `currentFraction` to `BackEvent.progress` which exposes how far the user has swiped back.
4. Finish the transition after the user has committed the back gesture in `handleOnBackPressed`.
5. Finally, reset the state of the transition within `handleOnBackCancelled`.

The following video, Kotlin code, and XML demonstrate a custom transition
between two boxes implemented with `OnBackPressedCallback`:  

```kotlin
    class MyFragment : Fragment() {

    val transitionSet = TransitionSet().apply {
        addTransition(Fade(Fade.MODE_OUT))
        addTransition(ChangeBounds())
        addTransition(Fade(Fade.MODE_IN))
    }
    ...
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val callback = object : OnBackPressedCallback(enabled = false) {

            var controller: TransitionSeekController? = null

            @RequiresApi(34)
            override fun handleOnBackStarted(backEvent: BackEvent) {
                // Create the transition
                controller = TransitionManager.controlDelayedTransition(
                    binding.card,
                    transitionSet
                )
                changeTextVisibility(ShowText.SHORT)
            }

            @RequiresApi(34)
            override fun handleOnBackProgressed(backEvent: BackEvent) {
                // Play the transition as the user swipes back
                if (controller?.isReady == true) {
                    controller?.currentFraction = backEvent.progress
                }
            }

            override fun handleOnBackPressed() {
                // Finish playing the transition when the user commits back
                controller?.animateToEnd()
                this.isEnabled = false
            }

            @RequiresApi(34)
            override fun handleOnBackCancelled() {
                // If the user cancels the back gesture, reset the state
                transition(ShowText.LONG)
            }
        }

        binding.shortText.setOnClickListener {
            transition(ShowText.LONG)
            callback.isEnabled = true
        }

        this.requireActivity().onBackPressedDispatcher.addCallback(callback)
    }

    private fun transition(showText: ShowText) {
        TransitionManager.beginDelayedTransition(
            binding.card,
            transitionSet
        )
        changeTextVisibility(showText)
    }

    enum class ShowText { SHORT, LONG }
    private fun changeTextVisibility(showText: ShowText) {
        when (showText) {
            ShowText.SHORT -> {
                binding.shortText.isVisible = true
                binding.longText.isVisible = false
            }
            ShowText.LONG -> {
                binding.shortText.isVisible = false
                binding.longText.isVisible = true
            }
        }
    }
}
  
```  

    <?xml version="1.0" encoding="utf-8"?>
    ...
        <androidx.constraintlayout.widget.ConstraintLayout
            android:id="@+id/card"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            ...>

            <TextView
                android:id="@+id/short_text"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                ... />

            <TextView
                android:id="@+id/long_text"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:visibility="gone"
                .../>

        </androidx.constraintlayout.widget.ConstraintLayout>

When working with Predictive Back transitions, keep the following in mind:

- Use `isSeekingSupported` to check if the transition supports Predictive Back.
- Override `isSeekingSupported` to return true for your custom transitions.
- Create one controller per animation.
- Predictive Back transitions are supported with AndroidX transitions, but not with framework transitions. Migrate away from framework transitions and use `Animator` and AndroidX transitions instead.
- Predictive Back transitions are supported on devices running Android 14 and higher and are not backward compatible.
- Transitions created with XML scenes are also supported. In `handleOnBackStarted`, set your `TransitionSeekController` to the result of [`TransitionManager.createSeekController`](https://developer.android.com/reference/androidx/transition/TransitionManager#createSeekController(androidx.transition.Scene,androidx.transition.Transition)) instead of the result of `controlDelayedTransition`.

### Add custom activity transitions on Android 14 and higher

To ensure that custom Activity transitions support Predictive Back on Android 14
and higher, you can use [`overrideActivityTransition`](https://developer.android.com/reference/android/app/Activity#overrideActivityTransition(int,%20int,%20int)) instead of
`overridePendingTransition`. This means that the transition animation plays as
the user swipes back.

To provide an example of how this might work, imagine a scenario in which
Activity B is on top of Activity A in the back stack. You would handle custom
Activity animations in the following way:

- Call either opening or closing transitions within Activity B's `onCreate` method.
- When the user navigates to Activity B, use `OVERRIDE_TRANSITION_OPEN`. When the user swipes to navigate back to Activity A, use `OVERRIDE_TRANSITION_CLOSE`.
- When specifying `OVERRIDE_TRANSITION_CLOSE`, the `enterAnim` is Activity A's
  enter animation and the `exitAnim` is Activity B's exit animation.

  | **Note:** If `exitAnim` isn't set or is set to `0`, the default cross-activity predictive animation, shown in the preceding video, plays instead.

### Add support for Predictive Back with fragments

When implementing Predictive Back with fragments, there are two approaches.

#### Use existing APIs

We recommend that you use existing APIs. These APIs allow you to swipe from the
edge of the screen to manipulate your Animator or Androidx transitions with the
gesture. Whether you move the gesture past a threshold determines whether it is
completed and you return to the previous fragment, or it is cancelled and you
remain on the current fragment. For more information, see
[Navigate between fragments using animations](https://developer.android.com/guide/fragments/animate).

Keep the following factors in mind:

- Import [Transitions 1.5.0](https://developer.android.com/jetpack/androidx/releases/transition#version_150_2) or later and [Fragments 1.7.0](https://developer.android.com/jetpack/androidx/releases/fragment#version_17_2) or later. Much of predictive back support within Fragments relies on Transitions being able to seek animations, which is only possible in Transitions 1.5.0 or later.
- Use Fragments, with either `FragmentManager` or the [Navigation Component](https://developer.android.com/guide/navigation), to handle the back stack. Predictive Back isn't supported if you manage your own back stack. Migrate away from back stacks that `FragmentManager` doesn't know about.
- Some libraries include Predictive Back support. Check the documentation to be sure.
- The [`Animator`](https://developer.android.com/reference/android/animation/Animator) class and [`AndroidX Transition`](https://developer.android.com/jetpack/androidx/releases/transition) library are supported.
- The `Animation` class and framework `Transition` library are not supported.
- Predictive animations only work on devices that run Android 14 or higher.

Use predictive back cross-fragments in the following situations:

- [Animate the navigation component](https://developer.android.com/guide/navigation/use-graph/animate-transitions).
- Animate with [`setCustomAnimations`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setCustomAnimations(int,int,int,int)).
- Animate enter and exit transitions with [`setEnterTransition`](https://developer.android.com/reference/android/app/Fragment#setEnterTransition(android.transition.Transition)), [`setExitTransition`](https://developer.android.com/reference/android/app/Fragment#setExitTransition(android.transition.Transition)), [`setReenterTransition`](https://developer.android.com/reference/android/app/Fragment#setReenterTransition(android.transition.Transition)) and [`setReturnTransition`](https://developer.android.com/reference/android/app/Fragment#setReturnTransition(android.transition.Transition)).
- Animate shared element transitions with [`setSharedElementEnterTransition`](https://developer.android.com/reference/androidx/fragment/app/Fragment#setSharedElementEnterTransition(java.lang.Object)), and [`setSharedElementReturnTransition`](https://developer.android.com/reference/androidx/fragment/app/Fragment#setSharedElementReturnTransition(java.lang.Object)).

Some [material motions](https://m2.material.io/develop/android/theming/motion)
support predictive back as of
[1.12.02-alpha02](https://github.com/material-components/material-components-android/releases/tag/1.12.0-alpha02)
or higher, including `MaterialFadeThrough`, `MaterialSharedAxis` and
`MaterialFade`.

#### Use callbacks

You can create a cross-fragment transition using callbacks, however there is a
known limitation when using callbacks where users cannot see the previous
fragment when swiping back. To create a cross-fragment shared element transition
that corresponds to the predictive back
[design guidance](https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back), do the
following:

Create an `OnBackPressedCallback`. Within `handleOnBackProgressed`, scale and
shift the fragment. Then pop from the back stack. Next, run the shared element
transition using `setSharedElementReturnTransition` outside the callback.

For more information, see [the code sample](https://github.com/android/animation-samples/blob/main/Motion/app/src/main/java/com/example/android/motion/demo/containertransform/CheeseArticleFragment.kt) on GitHub.

## Requirements

Use the following table to understand what is controlled by`targetSdkVersion`
and `compileSdkVersion`, device version, dependencies,
manifest flags, and fragment flags. This table refers to code requirements.
| **Note:** In Android 15 and later, the developer option is no longer available. System animations such as back-to-home, cross-task, and cross-activity now appear for apps that have opted into the predictive back gesture.

| Category | Animation | compileSdk | targetSdk | Device version | android:enableOnBackInvokedCallback | Dependency |
|---|---|---|---|---|---|---|
| System Animations | Back-to-home | 33 | Any | 35 | TRUE | None |
| System Animations | Cross-activity | 34 | Any | 35 | TRUE | None |
| System Animations | Cross-task | 34 | Any | 35 | TRUE | None |
| Platform | Custom cross-activity | 34 | Any | 35 | TRUE | None |
| Platform | Progress API Platform | 34 | Any | 34 | TRUE | None |
| Material Components | Bottom Sheet | 34 | Any | 34 | TRUE | Material Component 1.10.0 |
| Material Components | Side Sheet | 34 | Any | 34 | TRUE | Material Component 1.10.0 |
| Material Components | Navigation Drawer | 34 | Any | 34 | TRUE | Material Component 1.10.0 |
| Material Components | Search | 34 | Any | 34 | TRUE | Material Component 1.10.0 |
| Jetpack Animations | Custom AndroidX cross-fragment | 34 | Any | 34 | TRUE | AndroidX Fragment 1.7 |
| Jetpack Animations | Custom AndroidX Transitions | 34 | Any | 34 | TRUE | AndroidX Transition 1.5 |
| Jetpack Animations | Progress API Jetpack | 34 | Any | 34 | TRUE | AndroidX Activity 1.8 |
| Jetpack Animations |

## Additional Resources

- [Predictive back code samples](https://github.com/android/platform-samples/tree/main/samples/user-interface/predictiveback)
- [Basics for system back video](https://www.youtube.com/watch?v=Elpqr5xpLxQ)
- [Building for the future of Android video](https://www.youtube.com/watch?v=WMMPXayjP8g&t=335s)