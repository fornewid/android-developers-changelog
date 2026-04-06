---
title: Add support for predictive back animations in Views  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/custom-back/support-animations-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Add support for predictive back animations in Views Stay organized with collections Save and categorize content based on your preferences.



You can create custom in-app property animations and transitions, custom
cross-activity animations, and custom cross-fragment animations with predictive
back gestures using Views or Compose. To try the Compose way, see
[Add support for predictive back animations](/guide/navigation/custom-back/support-animations).

## Add custom transitions using the Progress API

With AndroidX Activity 1.8.0-alpha01 or higher, you can use the Predictive Back
Progress APIs to develop custom animations for the predictive back gesture in
your app. Progress APIs are helpful in animating views but have limitations when
animating transitions between fragments. Within [`OnBackPressedCallback`](/reference/kotlin/androidx/activity/OnBackPressedCallback)
we've introduced the [`handleOnBackProgressed`](/reference/androidx/activity/OnBackPressedCallback#handleOnBackPressed()), [`handleOnBackCancelled`](/reference/androidx/activity/OnBackPressedCallback#handleOnBackCancelled())
and [`handleOnBackStarted`](/reference/androidx/activity/OnBackPressedCallback#handleOnBackStarted(androidx.activity.BackEventCompat)) methods to animate objects while the user swipes
back. Use these methods if you need to customize more than the default
animations provided by the system, or the Material Component animations.

We expect most apps to use the backward compatible AndroidX APIs, but there are
also similar platform APIs within the [`OnBackAnimationCallback`](/reference/kotlin/android/window/OnBackAnimationCallback)
interface available to test in Android 14 and higher.

**Note:** Learn how to [design custom in-app transitions and animations.](/design/ui/mobile/guides/patterns/predictive-back).

### Use the Progress APIs with AndroidX Transitions

[

Alas, your browser doesn't support HTML5 video. That's OK! You can still
[download the video](/static/about/versions/14/images/predictive-back-transitions.mp4) and watch it with a video player.
](/static/about/versions/14/images/predictive-back-transitions.mp4)

The Progress APIs can be used with AndroidX Transitions 1.5.0-alpha01 or higher
on Android 14 and higher to create Predictive Back transitions.

1. Use [`TransitionManager#controlDelayedTransition`](/reference/androidx/transition/TransitionManager#controlDelayedTransition(android.view.ViewGroup,androidx.transition.Transition)) instead of
   `beginDelayedTransition` to play transitions as
   the user swipes back.
2. Create the transition within `handleOnBackStarted`.
3. Play the transition with the back event within `handleOnBackProgressed` by
   relating `currentFraction` to `BackEvent.progress` which exposes how far
   the user has swiped back.
4. Finish the transition after the user has committed the back gesture in
   `handleOnBackPressed`.
5. Finally, reset the state of the transition within `handleOnBackCancelled`.

The following video, Kotlin code, and XML demonstrate a custom transition
between two boxes implemented with `OnBackPressedCallback`:

```
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
```

When working with Predictive Back transitions, keep the following in mind:

* Use `isSeekingSupported` to check if the transition supports Predictive Back.
* Override `isSeekingSupported` to return true for your custom transitions.
* Create one controller per animation.
* Predictive Back transitions are supported with AndroidX transitions,
  but not with framework transitions. Migrate away from framework
  transitions and use `Animator` and AndroidX transitions instead.
* Predictive Back transitions are supported on devices running Android 14 and
  higher and are not backward compatible.
* Transitions created with XML scenes are also supported. In
  `handleOnBackStarted`, set your `TransitionSeekController` to the result
  of [`TransitionManager.createSeekController`](/reference/androidx/transition/TransitionManager#createSeekController(androidx.transition.Scene,androidx.transition.Transition)) instead of the result of
  `controlDelayedTransition`.

## Additional Resources

* [Predictive back code samples](https://github.com/android/platform-samples/tree/main/samples/user-interface/predictiveback)
* [Basics for system back video](https://www.youtube.com/watch?v=Elpqr5xpLxQ)
* [Building for the future of Android video](https://www.youtube.com/watch?v=WMMPXayjP8g&t=335s)