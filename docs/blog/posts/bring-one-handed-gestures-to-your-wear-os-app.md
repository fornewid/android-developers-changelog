---
title: https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app
url: https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Bring one-handed gestures to your Wear OS app

3 min read ![](https://developer.android.com/static/blog/assets/Bring_one_handed_gestures_Strapi_defff06599_Z1FDx9g.webp) 11 Aug 2026 [![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp)](https://developer.android.com/blog/authors/chiara-chiappini) [Chiara Chiappini](https://developer.android.com/blog/authors/chiara-chiappini) Developer Relation Engineer, Android Developer Relations One-handed gestures offer a convenient and touch-free way for users to interact with their watches, enabling them to perform key actions using only the hand on which the device is worn. First introduced on Pixel Watch with Wear OS 6.1, one-handed gestures made quick interactions effortless, such as starting and stopping a timer, accepting calls, and controlling media.

Now, with Wear OS 7, we're expanding this functionality with a new Gestures framework that allows OEMs to map gestures to primary actions and dismissals, and an API to bring gesture control to the developer community.

Starting with the 1.7[beta release of Compose for Wear OS](https://developer.android.com/jetpack/androidx/releases/wear-compose), you can seamlessly integrate gesture control into your Wear Compose apps. To use this release, upgrade your Wear Compose dependency to:

```
androidx.wear.compose:compose-material3:1.7.0-beta01
```

### Designing for one-handed interaction

The one-handed gestures framework is designed around two primary interaction patterns that allow users to take action without touching the screen:

- **Primary action**, which on Pixel Watch is mapped to a double-pinch gesture: this action should be mapped to the most important task in a given context. For example, users can perform this gesture to take a photo in a camera app, start/stop a timer, or accept an incoming call.
- **Dismiss action**, which on Pixel Watch is mapped to a wrist turn gesture: this action is mapped to system back by default and provides an intuitive way to close interruptive screens or get back to the watch face. It may be overridden for specific use cases, such as silencing an incoming phone call.

These gestures are currently available on Pixel Watch 3 and newer, and the Wear OS gesture framework is available to all Wear OS device manufactures to adopt.

Check out our new [design guidance](https://developer.android.com/design/ui/wear/guides/patterns/gestures) for integrating one-handed gestures into your Wear app.

### Integrating gestures with Compose on Wear OS

To provide seamless gesture support in Wear OS 7, we are introducing a new [Modifier.oneHandedGesture](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/oneHandedGesture.modifier) that you can apply to any existing interactive composable to make it gesture-aware.

Implementing gestures with Compose on Wear OS requires these steps:

1. **Define the gesture configuration.** Start by using rememberOneHandedGestureConfiguration to define the nature of the interaction. This configuration dictates the basic behavior by providing the GestureAction (e.g. tracking a primary pinch or a dismiss wrist flick).
2. **Initialize the indicator state.** Depending on your UI component, initialize a specific state object, such as OneHandedGestureClickIndicatorState for buttons or OneHandedGestureScrollIndicatorState for scrollable lists. This state is used to coordinate visual feedback between the gesture detection modifier and the visual UI indicators, seamlessly managing visibility, timing, and animations.
3. **Apply** [**Modifier.oneHandedGesture**](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/oneHandedGesture.modifier) to your interactive component. You'll pass in your configuration and state, and you'll provide standard callbacks: onGestureAvailable to activate the visual hint when the system prepares the gesture, and onGesture to execute your action when the gesture happens.

The following sample shows how those three steps translate into code when configuring an IconButton:

```kotlin
val gestureConfig = rememberOneHandedGestureConfiguration(action = OneHandedGestureAction.Primary)
val indicatorState = remember { OneHandedGestureClickIndicatorState() }
val coroutineScope = rememberCoroutineScope()

OutlinedIconButton(
    onClick = onPlayPauseButtonClicked,
    modifier = Modifier.touchTargetAwareSize(IconButtonDefaults.LargeButtonSize)
        .oneHandedGesture(
            gestureConfiguration = gestureConfig,
            interactionSource = interactionSource,
            onGestureLabel = "play or pause",
            onGestureAvailable = { 
                coroutineScope.launch { indicatorState.showIndicator() } 
            },
            onGesture = onPlayPauseButtonClicked,
        ),
) {
    // button content goes here
    // See "Guided discovery with gesture indicators" section of this post for recommendations on adding a gesture indicator.
}
```

The GestureAction.Primary can also be used to scroll when the content is the end goal of the user journey, or there is a gesture actionable button off screen that the user can scroll to. Some examples include:

- Scrolling through a notification to view the content and/or initiate a reply (available in TransformingLazyColumn and ScalingLazyColumn).
- Paging through workout metrics or other content that doesn't require the user to tap to continue the user journey (available in HorizontalPager and VerticalPager).

```kotlin
val scrollGestureConfig = rememberOneHandedGestureConfiguration(action = GestureAction.Primary)
val scrollIndicatorState = remember { OneHandedGestureScrollIndicatorState() }
val coroutineScope = rememberCoroutineScope()

TransformingLazyColumn(
    state = scrollState,
    contentPadding = contentPadding,
    modifier = Modifier
        .fillMaxSize()
        .oneHandedGesture(
            gestureConfiguration = scrollGestureConfig,
            onGestureLabel = "scroll",
            onGestureAvailable = { 
                coroutineScope.launch { scrollIndicatorState.showIndicator() } 
            },
            onGesture = { OneHandedGestureDefaults.scrollDown(scrollState) }
        )
) {
    // list content goes here
    // See "Guided discovery with gesture indicators" section of this post for recommendations on adding a gesture indicator.
}
```

### Guided discovery with gesture indicators

To help users learn which gestures are available, gesture indicators work as hints to help discovery about which gestures are available on a screen.

These hints provide animated cues that inform users where they can perform a gesture. The framework manages the cadence and appearance of these hints, ensuring that they are helpful without being intrusive. System settings let users change the cadence to something less frequent if desired.

To integrate with hints, the API provides the following gesture indicator components:

- the [OneHandedGestureClickIndicator](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGestureClickIndicator.composable) for components like a Button
- the [OneHandedGestureScrollIndicator](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGestureScrollIndicator.composable) component for scrolling
- the [OneHandedGestureHorizontalPageIndicator](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGestureHorizontalPageIndicator.composable) for the HorizontalPager
- the [OneHandedGestureVerticalPageIndicator](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGestureVerticalPageIndicator.composable) for the VerticalPager

The following example shows how to use the OneHandedGestureClickIndicator for a Button. See another example for using the [OneHandedGestureScrollIndicator](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/onehandedgesture/OneHandedGestureScrollIndicator.composable) in our [guidance](https://developer.android.com/training/wearables/compose/one-handed-gestures).

```kotlin
val gestureConfig = rememberOneHandedGestureConfiguration(action = GestureAction.Primary)
val indicatorState = remember { OneHandedGestureClickIndicatorState() }
val coroutineScope = rememberCoroutineScope()

OutlinedIconButton(
    onClick = onPlayPauseButtonClicked,
    modifier = Modifier.touchTargetAwareSize(IconButtonDefaults.LargeButtonSize)
        .oneHandedGesture(
            gestureConfiguration = gestureConfig,
            interactionSource = interactionSource,
            onGestureLabel = "play or pause",
            onGestureAvailable = { 
                coroutineScope.launch { indicatorState.showIndicator() } 
            },
            onGesture = onPlayPauseButtonClicked,
        ),
) {
    OneHandedGestureClickIndicator(
        gestureConfiguration = gestureConfig,
        indicatorState = indicatorState,
    ) {
        val icon = if (playerUiModel.playbackState.isPlaying) Icons.Filled.Pause else Icons.Filled.PlayArrow
        Icon(icon, contentDescription = "Play or Pause")
    }
}
```
![sample-app.gif](https://developer.android.com/static/blog/assets/sample_app_38a9b816fe_Z8867z.webp) Sample app showing gesture hint for media controls

We are already seeing early adoption of these APIs from partners like Spotify, who are using one-handed gestures to make music control more seamless on the go. By adopting the Modifier.oneHandedGesture into their Wear OS app, Spotify allows users to play or pause their music with the primary gesture action, which on Pixel Watch devices is the double-pinch gesture. This action triggers the same behavior as the physical play/pause button, and the user doesn't need to touch the screen.
![spotify.gif](https://developer.android.com/static/blog/assets/spotify_97253c677a_Z9cFov.webp) Spotify app with gesture integration

### Bring one-handed gestures to your app

You can begin experimenting with one-handed gestures today in the 1.7 beta release of Compose for Wear OS.

Ensure your app is running on Wear OS 7, which provides the underlying platform support for gesture detection. Check out our new [one-handed gestures developer guide](https://developer.android.com/training/wearables/compose/one-handed-gestures) to see how you can start building more convenient experiences for your users.
- [#Wear OS](https://developer.android.com/blog/topics/wear-os)
- [#made by google](https://developer.android.com/blog/topics/made-by-google)
- [#pixel watch](https://developer.android.com/blog/topics/pixel-watch)
Written by:

-

  ## [Chiara Chiappini](https://developer.android.com/blog/authors/chiara-chiappini)

  ###### Developer Relation Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/chiara-chiappini) ![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp) ![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp)
Continue reading
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_Z1hF7qE.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
- [![View Ataul Munim's profile](https://developer.android.com/static/blog/assets/Ataul_Munim_cf0796f68c_r1HY2.webp)](https://developer.android.com/blog/authors/ataul-munim) 02 Jun 2026 02 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Differentiated_Experiences_Strapi_bbe8e7618b_19k3ww.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building Premium Android Experiences at Google I/O '26](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26) At Google I/O '26, we showcased how the latest advancements in the Android ecosystem can help you elevate your app's quality while maximizing development efficiency.
  [Ataul Munim](https://developer.android.com/blog/authors/ataul-munim) • 3 min read
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - [#Memory](https://developer.android.com/blog/topics/memory)
  - [#Widgets](https://developer.android.com/blog/topics/widgets)
  - [#R8](https://developer.android.com/blog/topics/r8)
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#Automotive OS](https://developer.android.com/blog/topics/automotive-os)
  - +4 ↩
- [![View John Zoeller's profile](https://developer.android.com/static/blog/assets/John_Zoeller_photo_15badd5d35_aN1yx.webp)](https://developer.android.com/blog/authors/john-zoeller) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Developer_Blog_2_1_1440x720_6_64da0326e3_Z1M1YEl.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Wear OS 7](https://developer.android.com/blog/posts/what-s-new-in-wear-os-7)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-wear-os-7) We are excited to introduce Wear OS 7, a major update that brings a new era of power efficiency and intelligence to users and developers alike.
  [John Zoeller](https://developer.android.com/blog/authors/john-zoeller) • 9 min read
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)