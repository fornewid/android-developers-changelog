---
title: https://developer.android.com/about/versions/14/features/predictive-back
url: https://developer.android.com/about/versions/14/features/predictive-back
source: md.txt
---

# Add support for built-in and custom predictive back animations

If you've already[migrated your app to the new system back APIs](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture), you can opt in to predictive back to automatically receive in-app animations and also support custom transitions.

## Add support for built-in in-app animations

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/about/versions/14/images/predictive-back-settings-example.mp4)and watch it with a video player.**Video:**Predictive back animations

After opting in, your app displays animations for back-to-home, cross-activity, and cross-task.

You can also upgrade your material component dependency to v1.10.0 of MDC Android to receive material component animations like the following:

- [Bottom sheets](https://m3.material.io/components/bottom-sheets/guidelines#3d7735e2-73ea-4f3e-bd42-e70161fc1085)
- [Side sheets](https://m3.material.io/components/side-sheets/guidelines#d77245e3-1013-48f8-a9d7-76f484e1be13)
- [Search](https://m3.material.io/components/search/guidelines#3f2d4e47-2cf5-4c33-b6e1-5368ceaade55)

See the[material component developer guidance on GitHub](https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md#predictive-back-material-components)for more information.

The video shows a brief example of predictive back animations for cross-activity and back-to-home using the Android Settings app.

1. In the animation, the user swipes back to return to the previous settings screen---an example of a cross-activity animation.
2. Now on the previous screen, the user begins swiping back a second time, showing a preview of the home screen with its wallpaper---an example of the back-to-home animation.
3. The user continues to swipe right, showing an animation of the window shrinking down to the icon on the home screen.
4. The user has now fully returned to the home screen.

Read more about[supporting predictive back](https://developer.android.com/guide/navigation/predictive-back-gesture#update-default).

## Add custom in-app transitions and animations

You can create custom in-app property animations and transitions using the Progress API and custom cross-activity animations method`overrideActivityTransition`.

### Add custom transitions using the Progress API

With AndroidX Activity 1.8.0-alpha01 or higher, you can use the Predictive Back Progress APIs to develop custom animations for the predictive back gesture in your app. Within[`OnBackPressedCallback`](https://developer.android.com/reference/kotlin/androidx/activity/OnBackPressedCallback)we've introduced the`handleOnBackProgressed`,`handleOnBackCancelled`and`handleOnBackStarted`methods to animate objects while the user swipes back. Use these methods if you need something more custom than the default animations provided by the new system animations or the Material Component animations.

We expect most apps to use the backward compatible AndroidX APIs, but there are also similar platform APIs within the[`OnBackAnimationCallback`](https://developer.android.com/reference/kotlin/android/window/OnBackAnimationCallback)interface available to test in Android 14 Developer Preview 1 and higher.
| **Note:** Learn how to[design custom in-app transitions and animations.](https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back).

#### Use the Progress APIs with AndroidX Transitions

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/about/versions/14/images/predictive-back-transitions.mp4)and watch it with a video player.

The Progress APIs can be used with AndroidX Transitions 1.5.0-alpha01 or higher on Android 14 and above to create Predictive Back transitions.

1. Use[`TransitionManager#controlDelayedTransition`](https://developer.android.com/reference/androidx/transition/TransitionManager#controlDelayedTransition(android.view.ViewGroup,androidx.transition.Transition))instead of`beginDelayedTransition`to play transitions as the user swipes back.
2. Create the transition within`handleOnBackStarted`.
3. Play the transition with the back event within`handleOnBackProgressed`by relating`currentFraction`to`BackEvent.progress`which exposes how far the user has swiped back.
4. Finish the transition after the user has committed the back gesture in`handleOnBackPressed`.
5. Finally, reset the state of the transition within`handleOnBackCancelled`.

The following video, Kotlin code, and XML demonstrate a custom transition between two boxes implemented with`OnBackPressedCallback`:  

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

Note the following when working with Predictive Back transitions:

- Use`isSeekingSupported`to check if the transition supports Predictive Back.
- Override`isSeekingSupported`to return true for your custom transitions.
- Create one controller per animation.
- Predictive Back transitions are supported with AndroidX transitions, but not with framework transitions. We recommend migrating away from framework transitions.
- Predictive Back transitions are supported on Android 14+ devices and are not backward compatible.
- Transitions created with XML scenes are also supported. In`handleOnBackStarted`, set your`TransitionSeekController`to the result of[`TransitionManager.createSeekController`](https://developer.android.com/reference/androidx/transition/TransitionManager#createSeekController(androidx.transition.Scene,androidx.transition.Transition))instead of the result of`controlDelayedTransition`.

### Add custom activity transitions on Android 14 and higher

To ensure that custom Activity transitions support predictive back on Android 14 and higher, you can use[`overrideActivityTransition`](https://developer.android.com/reference/android/app/Activity#overrideActivityTransition(int,%20int,%20int))instead of`overridePendingTransition`. This means that the transition animation plays as the user swipes back.

To provide an example of how this might work, imagine a scenario in which Activity B is on top of Activity A in the back stack. You would handle custom Activity animations in the following way:

- Call either opening or closing transitions within Activity B's`onCreate`method.
- When the user navigates to Activity B, use`OVERRIDE_TRANSITION_OPEN`. When the user swipes to navigate back to Activity A, use`OVERRIDE_TRANSITION_CLOSE`.
- When specifying`OVERRIDE_TRANSITION_CLOSE`, the`enterAnim`is Activity A's enter animation and the`exitAnim`is Activity B's exit animation.

  | **Note:** If`exitAnim`isn't set or is set to`0`, the default cross-activity predictive animation (shown in the preceding video clip) plays instead.