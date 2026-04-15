---
title: https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-december-release
url: https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-december-release
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# What's new in the Jetpack Compose December '25 release

###### 6-min read

![](https://developer.android.com/static/blog/assets/jetpack_Compose_99733114d6_Z2c0xrB.webp) 03 Dec 2025 [![](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) [##### Nick Butcher](https://developer.android.com/blog/authors/nick-butcher)

###### Product Manager

Today, the [Jetpack Compose December '25 release](https://developer.android.com/jetpack/androidx/releases/compose) is stable. This contains version 1.10 of the core Compose modules and version 1.4 of Material 3 (see the full [BOM mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping)), adding new features and major performance improvements.

To use today's release, upgrade your Compose BOM version to `2025.12.00`:

```
  implementation(platform("androidx.compose:compose-bom:2025.12.00"))
```

## **Performance improvements**

We know that the runtime performance of your app is hugely important to you and your users, so performance has been a major priority for the Compose team. This release brings a number of improvements---and you get them all by just upgrading to the latest version. Our internal scroll benchmarks show that Compose now matches the performance you would see if using Views:
![janky.png](https://developer.android.com/static/blog/assets/janky_a31ad00e7e_Z1TjsfD.webp)

*Scroll performance benchmark comparing Views and Jetpack Compose across different versions of Compose*

### **Pausable composition in lazy prefetch**

Pausable composition in lazy prefetch is now enabled by default. This is a fundamental change to how the Compose runtime schedules work, designed to significantly reduce jank during heavy UI workloads.

Previously, once a composition started, it had to run to completion. If a composition was complex, this could block the main thread for longer than a single frame, causing the UI to freeze. With pausable composition, the runtime can now "pause" its work if it's running out of time and resume the work in the next frame. This is particularly effective when used with lazy layout prefetch to prepare frames ahead of time. The Lazy layout [CacheWindow](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#rememberLazyListState(androidx.compose.foundation.lazy.layout.LazyLayoutCacheWindow,kotlin.Int,kotlin.Int)) APIs introduced in Compose 1.9 are a great way to prefetch more content and benefit from pausable composition to produce much smoother UI performance.
![pausable.gif](https://developer.android.com/static/blog/assets/pausable_b582aa09f6_ZPIm6y.webp)

*Pausable composition combined with Lazy prefetch help reduce jank*

We've also optimized performance elsewhere, with improvements to `Modifier.onPlaced`, `Modifier.onVisibilityChanged`, and other modifier implementations. We'll continue to invest in improving the performance of Compose.

## **New features**

### **Retain**

Compose offers a number of APIs to hold and manage state across different lifecycles; for example, `remember` persists state across compositions, and `rememberSavable`/`rememberSerializable` to persist across activity or process recreation. [`retain`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/retain/package-summary#retain(kotlin.Function0)) is a new API that sits between these APIs, enabling you to persist values across configuration changes without being serialized, but not across process death. As `retain` does not serialize your state, you can persist objects like lambda expressions, flows, and large objects like bitmaps, which cannot be easily serialized. For example, you may use `retain` to manage a media player (such as ExoPlayer) to ensure that media playback doesn't get interrupted by a configuration change.

```
  @Composable

fun MediaPlayer() {

    val applicationContext = LocalContext.current.applicationContext

    val exoPlayer = retain { ExoPlayer.Builder(applicationContext).apply { ... }.build() }

    ...

}
```

We want to extend our thanks to the AndroidDev community (especially the [Circuit](https://slackhq.github.io/circuit) team), who have influenced and contributed to the design of this feature.

### **Material 1.4**

Version 1.4.0 of the `material3` library adds a number of new components and enhancements:

- `TextField` now offers an experimental `TextFieldState` based version, which provides a [more robust](https://developer.android.com/develop/ui/compose/text/user-input) method for managing text's state. In addition, new [`SecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedSecureTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.TextObfuscationMode,kotlin.Char,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,kotlin.Function2,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource)) and [`OutlinedSecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedSecureTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.material3.TextFieldLabelPosition,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.foundation.text.input.TextObfuscationMode,kotlin.Char,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,kotlin.Function2,androidx.compose.ui.graphics.Shape,androidx.compose.material3.TextFieldColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource)) variants are now offered. The material `Text` composable now supports autoSize behaviour.
- The carousel component now offers a new [`HorizontalCenteredHeroCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalCenteredHeroCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,kotlin.Boolean,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)) [variant](https://m3.material.io/components/carousel/specs).
- [`TimePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary?_gl=1*1h4dj5y*_up*MQ..*_ga*NDE1MzI0NzAwLjE3NjQ2MTM1MzU.*_ga_6HH9YJMN9M*czE3NjQ2MTM1MzQkbzEkZzAkdDE3NjQ2MTM1MzQkajYwJGwwJGgxODIyOTM4OTMy#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType)) now supports switching between the picker and input modes.
- A [vertical drag handle](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#VerticalDragHandle(androidx.compose.ui.Modifier,androidx.compose.material3.DragHandleSizes,androidx.compose.material3.DragHandleColors,androidx.compose.material3.DragHandleShapes,androidx.compose.foundation.interaction.MutableInteractionSource)) helps users to change an adaptive pane's size and/or position.

![centered-hero-carousel.webp](https://developer.android.com/static/blog/assets/centered_hero_carousel_9ef806cd6e_Z79z7U.webp)

*Horizontal centered hero carousel*

Note that [Material 3 Expressive](https://m3.material.io/blog/building-with-m3-expressive) APIs continue to be developed in the alpha releases of the `material3` library. To learn more, see this recent talk:
[Video](https://www.youtube.com/watch?v=t9rrsqfB2tM)

## **New animation features**

We continue to expand on our animation APIs, including updates for customizing shared element animations.

### **Dynamic shared elements**

By default, `sharedElement()` and `sharedBounds()` animations attempt to animate

layout changes whenever a matching key is found in the target state. However, you may want to disable this animation dynamically based on certain conditions, such as the direction of navigation or the current UI state.

To control whether the shared element transition occurs, you can now customize the `SharedContentConfig` passed to `rememberSharedContentState()`. The `isEnabled` property determines if the shared element is active.

```
  SharedTransitionLayout {

        val transition = updateTransition(currentState)

        transition.AnimatedContent { targetState ->

            // Create the configuration that depends on state changing.

            fun animationConfig() : SharedTransitionScope.SharedContentConfig {

                return object : SharedTransitionScope.SharedContentConfig {

                    override val SharedTransitionScope.SharedContentState.isEnabled: Boolean

                        get() =

                            // determine whether to perform a shared element transition

                }

            }

}
```

See the [documentation](https://developer.android.com/develop/ui/compose/animation/shared-elements/customize#dynamic-enable-disable) for more.

### **Modifier.skipToLookaheadPosition()**

A new modifier, [`Modifier.skipToLookaheadPosition()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope#(androidx.compose.ui.Modifier).skipToLookaheadPosition(kotlin.Function0)), has been added in this release, which keeps the final position of a composable when performing shared element animations. This allows for performing transitions like "reveal" type animation, as can be seen in the Androidify sample with the progressive reveal of the camera. See the video tip here for more information:
[Video](https://www.youtube.com/watch?v=0moEXBqNDZI)

### **Initial velocity in shared element transitions**

This release adds a new shared element transition API, `prepareTransitionWithInitialVelocity`, which lets you pass an initial velocity (e.g. from a gesture) to a shared element transition:

```
  Modifier.fillMaxSize()

    .draggable2D(

        rememberDraggable2DState { offset += it },

        onDragStopped = { velocity ->

            // Set up the initial velocity for the upcoming shared element

            // transition.

            sharedContentStateForDraggableCat

                ?.prepareTransitionWithInitialVelocity(velocity)

            showDetails = false

        },

    )
```
![fling-shared.gif](https://developer.android.com/static/blog/assets/fling_shared_0611ccdf1b_ZpTb5k.webp)

*A shared element transition that starts with an initial velocity from a gesture*

### **Veiled transitions**

[`EnterTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/EnterTransition) and [`ExitTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/ExitTransition?_gl=1*1m00og2*_up*MQ..*_ga*MjU3NDMyNzc5LjE3NjQ2MTE4NjM.*_ga_6HH9YJMN9M*czE3NjQ2MTE4NjMkbzEkZzAkdDE3NjQ2MTE4NjMkajYwJGwwJGgxMTk2NzM1MDk0) define how an [`AnimatedVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#AnimatedVisibility(kotlin.Boolean,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.String,kotlin.Function1))/[`AnimatedContent`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary?_gl=1*18ofha4*_up*MQ..*_ga*MjU3NDMyNzc5LjE3NjQ2MTE4NjM.*_ga_6HH9YJMN9M*czE3NjQ2MTE4NjMkbzEkZzAkdDE3NjQ2MTIyMjEkajYwJGwwJGgxMTk2NzM1MDk0#AnimatedContent(kotlin.Any,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.Alignment,kotlin.String,kotlin.Function1,kotlin.Function2)) composable appears or disappears. A new experimental veil option allows you to specify a color to veil or scrim content; e.g., fading in/out a semi-opaque black layer over content:
![veil_2.gif](https://developer.android.com/static/blog/assets/veil_2_a4f7244888_190Y0O.webp)

*Veiled animated content -- note the semi-opaque veil (or scrim) over the grid content during the animation*

```
  AnimatedContent(

    targetState = page,

    modifier = Modifier.fillMaxSize().weight(1f),

    transitionSpec = {

        if (targetState > initialState) {

            (slideInHorizontally { it } togetherWith

                    slideOutHorizontally { -it / 2 } + veilOut(targetColor = veilColor))

        } else {

            slideInHorizontally { -it / 2 } +

                    unveilIn(initialColor = veilColor) togetherWith slideOutHorizontally { it }

        }

    },

) { targetPage ->

    ...

}
```

## **Upcoming changes**

### **Deprecation of Modifier.onFirstVisible**

Compose 1.9 introduced [`Modifier.onVisibilityChanged`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#%28androidx.compose.ui.Modifier%29.onVisibilityChanged%28kotlin.Long,kotlin.Float,androidx.compose.ui.layout.LayoutBoundsHolder,kotlin.Function1%29) and [`Modifier.onFirstVisible`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#%28androidx.compose.ui.Modifier%29.onFirstVisible%28kotlin.Long,kotlin.Float,androidx.compose.ui.layout.LayoutBoundsHolder,kotlin.Function0%29). After reviewing your feedback, it became apparent that the contract of `Modifier.onFirstVisible` was not possible to honor deterministically; specifically, when an item **first** becomes visible. For example, a Lazy layout may dispose of items that scroll out of the viewport, and then compose them again if they scroll back into view. In this circumstance, the `onFirstVisible` callback would fire again, as it is a newly composed item. Similar behavior would also occur when navigating back to a previously visited screen containing `onFirstVisible`. As such, we have decided to deprecate this modifier in the **next** Compose release (1.11) and recommend migrating to `onVisibilityChanged`. See the [documentation](https://developer.android.com/develop/ui/compose/layouts/visibility-modifiers) for more information.

### **Coroutine dispatch in tests**

We plan to change coroutine dispatch in tests to improve test flakiness and catch more issues. Currently, tests use the `UnconfinedTestDispatcher`, which differs from production behavior; e.g., [effects](https://developer.android.com/develop/ui/compose/side-effects) may run immediately rather than being enqueued. In a future release, we plan to introduce a new API that uses `StandardTestDispatcher` by default to match production behaviours. You can try the new behavior **now** in 1.10:

```
  @get:Rule // also createAndroidComposeRule, createEmptyComposeRule

val rule = createComposeRule(effectContext = StandardTestDispatcher())
```

Using the `StandardTestDispatcher` will queue tasks, so you must use synchronization mechanisms like `composeTestRule.waitForIdle()` or `composeTestRule.runOnIdle()`. If your test uses `runTest`, you must ensure that `runTest` and your Compose rule share the same `StandardTestDispatcher` instance for synchronization.

```
  // 1. Create a SINGLE dispatcher instance

val testDispatcher = StandardTestDispatcher()



// 2. Pass it to your Compose rule

@get:Rule

val composeRule = createComposeRule(effectContext = testDispatcher)



@Test

// 3. Pass the *SAME INSTANCE* to runTest

fun myTest() = runTest(testDispatcher) {

    composeRule.setContent { /* ... */ }

}
```

## **Tools**

Great APIs deserve great tools, and [Android Studio](http://d.android.com/studio) has a number of recent additions for Compose developers:

- [**Transform UI**](https://developer.android.com/studio/preview/features#iterate-ui-agent): Iterate on your designs by right clicking on the `@Preview`, selecting Transform UI, and then describing the change in natural language.
- [**Generate** `@Preview`](https://developer.android.com/studio/preview/features#ui-tools-setup): Right-click on a composable and select **Gemini \> Generate \[Composable name\] Preview**.
- [**Customize Material Symbols**](https://developer.android.com/studio/preview/features#material-symbols-support) with new support for icon variations in the Vector Asset wizard.
- [**Generate code from a screenshot**](https://developer.android.com/studio/preview/features#screen-to-code-agent) or ask Gemini to [match your existing UI to a target image](https://developer.android.com/studio/preview/features#match-ui-agent). This can be combined with remote [MCP support](https://developer.android.com/studio/preview/features#remote-mcp) e.g. to connect to a Figma file and generate Compose UI from designs.
- [**Fix UI quality issues**](https://developer.android.com/studio/preview/features#find-and-fix-ui-quality-issues) audits your UI for common problems, such as accessibility issues, and then proposes fixes.

To see these tools in action, watch this recent demonstration:
[Video](https://www.youtube.com/watch?v=jTlW8JeCClA)

## **Happy Composing**

We continue to invest in Jetpack Compose to provide you with the APIs and tools you need to create beautiful, rich UIs. We value your input, so please share your feedback on these changes or what you'd like to see next in our [issue tracker](https://issuetracker.google.com/issues/new?component=612128).

###### Written by:

-

  ## [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/nick-butcher) ![](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp) ![](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) 13 Apr 2026 13 Apr 2026 ![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Test Multi-Device Interactions with the Android Emulator](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator)

  [arrow_forward](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator) Testing multi-device interactions is now easier than ever with the Android Emulator.

  ###### [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)