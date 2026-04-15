---
title: https://developer.android.com/blog/posts/android-devices-extend-seamlessly-to-connected-displays
url: https://developer.android.com/blog/posts/android-devices-extend-seamlessly-to-connected-displays
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Android devices extend seamlessly to connected displays

###### 7-min read

![](https://developer.android.com/static/blog/assets/android_Connected_34a0ae66a4_1A0pVS.webp) 03 Mar 2026 [![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp)](https://developer.android.com/blog/authors/francesco-romano) [##### Francesco Romano](https://developer.android.com/blog/authors/francesco-romano)

###### Developer Relations Engineer, Android

We are excited to announce a major milestone in bringing mobile and desktop computing closer together on Android: connected display support has reached general availability with the [Android 16 QPR3](https://developer.android.com/about/versions/16/qpr3/release-notes) release!  

As shown at [Google I/O 2025](https://www.youtube.com/watch?v=MmeJSLAnB-M), connected displays allow users to connect their Android devices to an external monitor and instantly access a desktop windowing environment. Apps can be used in free-form or maximized windows and users can multitask just like they would on a desktop OS.

Google and Samsung have collaborated to bring a seamless and powerful desktop windowing experience to devices across the Android ecosystem running Android 16 while connected to an external display.   
This is now generally available on supported devices\* to users who can connect their supported Pixel and Samsung phones to external monitors, enabling new opportunities for building more engaging and more productive app experiences that adapt across form factors.

### **How does it work?**

When a supported Android phone or foldable is connected to an external display, a new desktop session starts on the connected display.

The experience on the connected display is similar to the experience on a desktop, including a taskbar that shows active apps and lets users pin apps for quick access. Users are able to run multiple apps side by side simultaneously in freely resizable windows on the connected display.
![materialDisplay.gif](https://developer.android.com/static/blog/assets/material_Display_6b57bc3b79_ePKt3.webp)

*Phone connected to an external display with a desktop session on the display while the phone maintains its own state.*

When a device that supports desktop windowing (such as a tablet like the Samsung Galaxy Tab S11) is connected to an external display, the desktop session is extended across both displays, unlocking an even more expansive workspace. The two displays then function as one continuous system, allowing app windows, content, and the cursor to move freely between the displays.
![materialDisplay2.gif](https://developer.android.com/static/blog/assets/material_Display2_2c36188b82_1iPoD2.webp)

*Tablet connected to an external display, extending the desktop session across both displays.*

## Why does it matter?

In the Android 16 QPR3 release, we finalized the windowing behaviors, taskbar interactions, and [input compatibility](https://developer.android.com/guide/practices/device-compatibility-mode#override_mouse_to_touch) (mouse and keyboard) that define the connected display experience. We also included [compatibility treatments](https://developer.android.com/guide/practices/device-compatibility-mode#display_compatibility_mode) to scale windows and avoid app restarts when switching displays.

<br />

If your app is built with [adaptive design principles](https://m3.material.io/foundations/adaptive-design), it will automatically have the desktop look and feel, and users will feel right at home. If the app is locked to portrait or assumes a touch-only interface, now is the time to modernize.

In particular, pay attention to these key best practices for optimal app experiences on connected displays:

- **Don't assume a constant** [`Display`](https://developer.android.com/reference/android/view/Display)**object:** The `Display` object associated with your app's context can change when an app window is moved to an external display or if the display configuration changes. Your app should gracefully handle configuration change events and query display metrics dynamically rather than caching them.
- **Account for** [**density configuration changes**](https://developer.android.com/guide/topics/manifest/activity-element#config)**:** External displays can have vastly different pixel densities than the primary device screen. Ensure your layouts and resources adapt correctly to these changes to maintain UI clarity and usability. Use density-independent pixels (dp) for layouts, provide density-specific resources, and ensure your UI scales appropriately.
- **Correctly** [**support external peripherals**](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens): When users connect to an external monitor, they often create a more desktop-like environment. This frequently involves using external keyboards, mice, trackpads, webcams, microphones, and speakers. Improve the support for [keyboard](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands) and [mouse](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#mouse_and_touchpad) interactions.

### **Building for the desktop future with modern tools**

We provide several tools to help you build the desktop experience. Let's recap the latest updates to our core adaptive libraries!

#### **New window size classes: Large and Extra-large**

The biggest update in [Jetpack WindowManager 1.5.0](https://developer.android.com/jetpack/androidx/releases/window#1.5.0) is the addition of two new width window size classes: Large and Extra-large.  

Window size classes are our official, opinionated set of viewport breakpoints that help you design and develop adaptive layouts. With 1.5.0, we're extending this guidance for screens that go beyond the size of typical tablets.  

Here are the new width breakpoints:

- Large: For widths between 1200dp and 1600dp
- Extra-large: For widths ≥1600dp

![windowClasses.png](https://developer.android.com/static/blog/assets/window_Classes_b75579f205_J3qef.webp)

*The different window size classes based on display width.*

On very large surfaces, simply scaling up a tablet's *Expanded* layout isn't always the best user experience. An email client, for example, might comfortably show two panes (a mailbox and a message) in the Expanded window size class. But on an *Extra-large* desktop monitor, the email client could elegantly display three or even four panes, perhaps a mailbox, a message list, the full message content, and a calendar/tasks panel, all at once.

To include the new window size classes in your project, simply call the function from the [WindowSizeClass.BREAKPOINTS_V2](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass#BREAKPOINTS_V2()) set instead of [WindowSizeClass.BREAKPOINTS_V1](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass#BREAKPOINTS_V1()):

```
  val currentWindowMetrics =
    WindowMetricsCalculator.getOrCreate()
    .computeCurrentWindowMetrics(LocalContext.current)

val sizeClass = WindowSizeClass.BREAKPOINTS_V2
    .computeWindowSizeClass(currentWindowMetrics)
```

Then apply the correct layout when you're sure your app has at least that much space:

```
  if(sizeClass.isWidthAtLeastBreakpoint(
    WindowSizeClass.WIDTH_DP_LARGE_LOWER_BOUND)){
    ...
	// Window is at least 1200 dp wide.
}
```

### **Build adaptive layouts with Jetpack Navigation 3**

[Navigation 3](https://developer.android.com/guide/navigation/navigation-3) is the latest addition to the Jetpack collection. Navigation 3, which just reached its first stable release, is a powerful navigation library designed to work with Compose.  

Navigation 3 is also a great tool for building adaptive layouts by allowing multiple destinations to be displayed at the same time and allowing seamless switching between those layouts.  

This system for managing your app's UI flow is based on Scenes. A [Scene](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/Scene) is a layout that displays one or more destinations at the same time. A [SceneStrategy](https://developer.android.com/reference/androidx/navigation3/ui/SceneStrategy) determines whether it can create a Scene. Chaining SceneStrategy instances together allows you to create and display different scenes for different screen sizes and device configurations.  

For out-of-the-box canonical layouts, like list-detail and supporting pane, you can [use the Scenes from the Compose Material 3 Adaptive library](https://developer.android.com/guide/navigation/navigation-3/custom-layouts#display-list-detail) (available in [version 1.3 and above](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#compose_material3_adaptive_version_13_2)).  

It's also easy to build your own custom Scenes by [modifying the Scene recipes](https://github.com/android/nav3-recipes?tab=readme-ov-file#create-custom-scenes) or starting from scratch. For example, let's consider a Scene that displays three panes side by side:

```
  class ThreePaneScene<T : Any>(
    override val key: Any,
    override val previousEntries: List<NavEntry<T>>,
    val firstEntry: NavEntry<T>,
    val secondEntry: NavEntry<T>,
    val thirdEntry: NavEntry<T>
) : Scene<T> {
    override val entries: List<NavEntry<T>> = listOf(firstEntry, secondEntry, thirdEntry)
    override val content: @Composable (() -> Unit) = {
        Row(modifier = Modifier.fillMaxSize()) {
            Column(modifier = Modifier.weight(1f)) {
                firstEntry.Content()
            }
            Column(modifier = Modifier.weight(1f)) {
                secondEntry.Content()
            }
            Column(modifier = Modifier.weight(1f)) {
                thirdEntry.Content()
            }
        }
    }
```

In this scenario, you could define a [SceneStrategy](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/SceneStrategy) to show three panes if the window width is wide enough and the entries from your back stack have declared that they support being displayed in a three-pane scene.

```
  class ThreePaneSceneStrategy<T : Any>(val windowSizeClass: WindowSizeClass) : SceneStrategy<T> {
    override fun SceneStrategyScope<T>.calculateScene(entries: List<NavEntry<T>>): Scene<T>? {
        if (windowSizeClass.isWidthAtLeastBreakpoint(WIDTH_DP_LARGE_LOWER_BOUND)) {
            val lastThree = entries.takeLast(3)
            if (lastThree.size == 3 && lastThree.all { it.metadata.containsKey(MULTI_PANE_KEY) }) {
                val firstEntry = lastThree[0]
                val secondEntry = lastThree[1]
                val thirdEntry = lastThree[2]


                return ThreePaneScene(
                    key = Triple(firstEntry.contentKey, secondEntry.contentKey, thirdEntry.contentKey),
                    previousEntries = entries.dropLast(3),
                    firstEntry = firstEntry,
                    secondEntry = secondEntry,
                    thirdEntry = thirdEntry
                )
            }
        }
        return null
    }
}
```

You can use your ThreePaneSceneStrategy with other strategies when creating your [NavDisplay](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay). For example, we could also add a TwoPaneStrategy to display two panes side by side when there isn't enough space to show three.

```
  val strategy = ThreePaneSceneStrategy() then TwoPaneSceneStrategy()

NavDisplay(..., 
  sceneStrategy = strategy,
  entryProvider = entryProvider { 
    entry<MyScreen>(metadata = mapOf(MULTI_PANE_KEY to true))) { ... }
    ... other entries...
  }
)
```

If there isn't enough space to display three or two panes---both our custom scene strategies return `null`. In this case, `NavDisplay` falls back to displaying the last entry in the back stack in a single pane using `SinglePaneScene`.   

By using scenes and strategies, you can add one, two, and three pane layouts to your app!
![adaptivepane.gif](https://developer.android.com/static/blog/assets/adaptivepane_c2f34f0b31_2qrog2.webp)

*An adaptive app showing three-pane navigation on wide screens.*

Checkout the documentation to learn more on [how to create custom layouts using Scenes in Navigation 3](https://developer.android.com/guide/navigation/navigation-3/custom-layouts).

### Standalone adaptive layouts

If you need a standalone layout, the [Compose Material 3 Adaptive library](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) helps you create adaptive UIs like list-detail and supporting pane layouts that adapt themselves to window configurations automatically based on window size classes or device postures.

The good news is that the library is already up to date with the new breakpoints! Starting from [version 1.2](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#compose_material3_adaptive_version_12_2), the default pane scaffold directive functions support Large and Extra-large width window size classes.

You only need to opt-in by declaring in your Gradle build file that you want to use the new breakpoints:

`currentWindowAdaptiveInfo(supportLargeAndXLargeWidth = true)`

### Getting started

Explore the connected display feature in the latest Android release. Get [Android 16 QPR3](https://developer.android.com/about/versions/16/qpr3/release-notes) on a supported device, then connect it to an external monitor to start testing your app today!

Dive into the updated documentation on [multi-display support](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-connected-displays) and [window management](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-desktop-windowing) to learn more about implementing these best practices.

#### **Feedback**

Your feedback is crucial as we continue to refine the connected display desktop experience. Share your thoughts and report any issues through our [official feedback channels](https://developer.android.com/about/versions/16/qpr3/feedback).

We're committed to making Android a versatile platform that adapts to the many ways users want to interact with their apps and devices. The improvements to connected display support are another step in that direction, and we think your users will love the desktop experiences you'll build!

<br />

**\*Note:** At the time the article is written, connected displays are supported on Pixel 8, 9, 10 series and on a wide array of Samsung devices, including S26, Fold7, Flip7, and Tab S11.

###### Written by:

-

  ## [Francesco Romano](https://developer.android.com/blog/authors/francesco-romano)

  ###### Developer Relations Engineer, Android

  [read_more
  View profile](https://developer.android.com/blog/authors/francesco-romano) ![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp) ![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp)](https://developer.android.com/blog/authors/francesco-romano) 10 Oct 2025 10 Oct 2025 ![](https://developer.android.com/static/blog/assets/jetpack_Window_Manager_931d67ec18_Z20PMAS.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Jetpack WindowManager 1.5 is stable](https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable) We're excited to announce that Jetpack WindowManager 1.5.0 is now stable!

  This release builds on the strong foundation of adaptability in WindowManager, making it even easier to create polished, adaptive UIs that look great on all screen sizes.

  ###### [Francesco Romano](https://developer.android.com/blog/authors/francesco-romano) •
  3 min read

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

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)