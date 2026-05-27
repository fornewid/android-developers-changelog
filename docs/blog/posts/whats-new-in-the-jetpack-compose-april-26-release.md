---
title: https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release
url: https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# What's new in the Jetpack Compose April '26 release

###### 5-min read

![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp) 22 Apr 2026 [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) [##### Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta)

###### Developer Advocate, Android

Today, the Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full [BOM mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping)), shared element debug tools, trackpad events, and more. We also have a few experimental APIs that we'd love you to try out and give us feedback on.

To use today's release, upgrade your [Compose BOM](https://developer.android.com/develop/ui/compose/bom) version to:

```kotlin
implementation(platform("androidx.compose:compose-bom:2026.04.01"))
```

## Changes in Compose 1.11.0

### **Coroutine execution in tests**

We're introducing a major update to how Compose handles test timing. Following the opt-in period announced in Compose 1.10, the v2 testing APIs are now the default, and the v1 APIs have been deprecated. The key change is a shift in the default test dispatcher. While the v1 APIs relied on the [`UnconfinedTestDispatcher`](https://developer.android.com/kotlin/coroutines/test#unconfinedtestdispatcher), which executed coroutines immediately, the v2 APIs use the [`StandardTestDispatcher`](https://developer.android.com/kotlin/coroutines/test#standardtestdispatcher). This means that when a coroutine is launched in your tests, it is now queued and does not execute until the virtual clock is advanced.

This better mimics production conditions, effectively flushing out race conditions and making your test suite significantly more robust and less flaky.

To ensure your tests align with standard coroutine behavior and to avoid future compatibility issues, we strongly recommend migrating your test suite. Check out our comprehensive [migration guide](https://developer.android.com/develop/ui/compose/testing/migrate-v2) for API mappings and common fixes.

### **Shared element improvements and animation tooling**

We've also added some handy visual debugging tools for shared elements and `Modifier.animatedBounds`. You can now see exactly what's happening under the hood---like target bounds, animation trajectories, and how many matches are found---making it much easier to spot why a transition might not be behaving as expected. To use the new tooling, simply surround your SharedTransitionLayout with the [`LookaheadAnimationVisualDebugging`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#LookaheadAnimationVisualDebugging(kotlin.Boolean,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Boolean,kotlin.Function0)) composable.

```kotlin
LookaheadAnimationVisualDebugging(
    overlayColor = Color(0x4AE91E63),
    isEnabled = true,
    multipleMatchesColor = Color.Green,
    isShowKeylabelEnabled = false,
    unmatchedElementColor = Color.Red,
) {
    SharedTransitionLayout {
        CompositionLocalProvider(
            LocalSharedTransitionScope provides this,
        ) {
            // your content
        }
    }
}
```

### **Trackpad events**

We've revamped Compose support for trackpads, like built-in laptop trackpads, attachable trackpads for tablets, or external/virtual trackpads. Basic trackpad events will now generally be considered PointerType.Mouse events, aligning mouse and trackpad behavior to better match user expectations. Previously, these trackpad events were interpreted as fake touchscreen fingers of `PointerType.Touch`, which led to confusing user experiences. For example, clicking and dragging with a trackpad would scroll instead of selecting. By changing the pointer type these events have in the latest release of Compose, clicking and dragging with a trackpad will no longer scroll.

We also added support for more complicated trackpad gestures as recognized by the platform since API 34, including [two finger swipes](https://developer.android.com/reference/android/view/MotionEvent#CLASSIFICATION_TWO_FINGER_SWIPE) and [pinches](https://developer.android.com/reference/android/view/MotionEvent#CLASSIFICATION_PINCH). These gestures are automatically recognized by components like `Modifier.scrollable` and `Modifier.transformable` to have better behavior with trackpads.

These changes improve behavior for trackpads across built-in components, with redundant touch slop removed, a more intuitive drag-and-drop starting gesture, double-click and triple-click selection in text fields, and desktop-styled context menus in text fields.

To test trackpad behavior, there are new testing APIs with [`performTrackpadInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteraction#(androidx.compose.ui.test.SemanticsNodeInteraction).performTrackpadInput(kotlin.Function1))`,` which allow validating the behavior of your apps when being used with a trackpad. If you have custom gesture detectors, validate behavior across input types, including touchscreens, mice, trackpads, and styluses, and ensure support for mouse scroll wheels and trackpad gestures.
![beforeAndAfter.webp](https://developer.android.com/static/blog/assets/before_And_After_9a75e8a0d1_Zx1J0g.webp)

**Composition host defaults (Compose runtime)**

We introduced [`HostDefaultProvider`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/HostDefaultProvider), `LocalHostDefaultProvider`, `HostDefaultKey`, and `ViewTreeHostDefaultKey` to supply host-level services directly through compose-runtime. This removes the need for libraries to depend on `compose-ui` for lookups, better supporting Kotlin Multiplatform. To link these values to the composition tree, library authors can use `compositionLocalWithHostDefaultOf` to create a `CompositionLocal` that resolves defaults from the host.

### **Preview wrappers**

**Android Studio custom previews** is a new feature that allows you to define exactly how the contents of a Compose preview are displayed.

By implementing the `PreviewWrapperProvider` interface and applying the new `@PreviewWrapper` annotation, you can easily inject custom logic, such as applying a specific `Theme`. The annotation can be applied to a function annotated with `@Composable` and `@Preview` or `@MultiPreview`, offering a generic, easy-to-use solution that works across preview features and significantly reduces repetitive code.

```kotlin
class ThemeWrapper: PreviewWrapper {
    @Composable
    override fun Wrap(content: @Composable (() -> Unit)) {
        JetsnackTheme {
            content()
        }
    }
}

@PreviewWrapperProvider(ThemeWrapper::class)
@Preview
@Composable
private fun ButtonPreview() {
    // JetsnackTheme in effect
    Button(onClick = {}) {
        Text(text = "Demo")
    }
}
```

## Deprecations and removals

- As announced in the [Compose 1.10 blog post](https://android-developers.googleblog.com/2025/12/whats-new-in-jetpack-compose-december.html), we're deprecating `Modifier.onFirstVisible()`. Its name often led to misconceptions, particularly within lazy layouts, where it would trigger multiple times during scrolling. We recommend migrating to [`Modifier.onVisibilityChanged()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/package-summary#(androidx.compose.ui.Modifier).onVisibilityChanged(kotlin.Long,kotlin.Float,androidx.compose.ui.layout.LayoutBoundsHolder,kotlin.Function1)), which allows for more precise manual tracking of visibility states tailored to your specific use case requirements.
- The `ComposeFoundationFlags.isTextFieldDpadNavigationEnabled` flag was removed because D-pad navigation for `TextFields` is now always enabled by default. The new behavior ensures that the D-pad events from a gamepad or a TV remote first move the cursor in the given direction. The focus can move to another element only when the cursor reaches the end of the text.

## Upcoming APIs

In the upcoming Compose 1.12.0 release, the `compileSdk` will be upgraded to `compileSdk 37`, with AGP 9 and all apps and libraries that depend on Compose inheriting this requirement. We recommend keeping up to date with the latest released versions, as Compose aims to promptly adopt new `compileSdks` to provide access to the latest Android features. Be sure to check out the [documentation here](https://developer.android.com/build/releases/about-agp#api-level-support) for more information on which version of AGP is supported for different API levels.

In Compose 1.11.0, the following APIs are introduced as `@Experimental`, and we look forward to hearing your feedback as you explore them in your apps. Note that `@Experimental APIs` are provided for early evaluation and feedback and may undergo significant changes or removal in future releases.

### **Styles (Experimental)**

We are introducing a new experimental foundation API for [styling](https://developer.android.com/develop/ui/compose/styles). The Style API is a new paradigm for customizing visual elements of components, which has traditionally been performed with modifiers. It is designed to unlock deeper, easier customization by exposing a standard set of styleable properties with simple state-based styling and animated transitions. With this new API, we're already seeing promising [performance benefits](https://developer.android.com/develop/ui/compose/styles/performance). We plan to adopt Styles in Material components once the Style API stabilizes.

A basic example of overriding a pressed state style background:

```kotlin
@Composable
fun LoginButton(modifier: Modifier = Modifier) {
    Button(
        onClick = {
            // Login logic
        },
        modifier = modifier,
        style = {
            background(
                Brush.linearGradient(
                    listOf(lightPurple, lightBlue)
                )
            )
            width(75.dp)
            height(50.dp)
            textAlign(TextAlign.Center)
            externalPadding(16.dp)

            pressed {
                background(
                    Brush.linearGradient(
                        listOf(Color.Magenta, Color.Red)
                    )
                )
            }
        }
    ){
        Text(
            text = "Login",
        )
    }
}
```
![styles.webp](https://developer.android.com/static/blog/assets/styles_dccbb26cfe_Z3sMfB.webp)

Check out the [documentation](https://developer.android.com/develop/ui/compose/styles) and file any bugs [here](https://issuetracker.google.com/issues/new?component=612128).

### **MediaQuery (Experimental)**

The new [mediaQuery](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery) API provides a declarative and performant way to adapt your UI to its environment. It abstracts complex information retrieval into simple conditions within a [`UiMediaScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/UiMediaScope), ensuring recomposition only happens when needed.

With support for a wide range of environmental signals---from device capabilities like keyboard types and pointer precision, to contextual states like window size and posture---you can build deeply responsive experiences. Performance is baked in with [`derivedMediaQuery`](https://developer.android.com/reference/kotlin/androidx/compose/ui/package-summary#derivedMediaQuery(kotlin.Function1)) to handle high-frequency updates, while the ability to override scopes makes testing and previews seamless across hardware configurations. Previously, to get access to certain device properties --- like if a device was in [tabletop mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware#features_of_foldable_displays) --- you'd need to write a lot of boilerplate to do so:

```kotlin
@Composable
fun isTabletopPosture(
    context: Context = LocalContext.current
): Boolean {
    val windowLayoutInfo by
        WindowInfoTracker
            .getOrCreate(context)
            .windowLayoutInfo(context)
            .collectAsStateWithLifecycle(null)

    return windowLayoutInfo.displayFeatures.any { displayFeature ->
        displayFeature is FoldingFeature &&
            displayFeature.state == FoldingFeature.State.HALF_OPENED &&
            displayFeature.orientation == FoldingFeature.Orientation.HORIZONTAL
    }
}

@Composable
fun VideoPlayer() {
    if(isTabletopPosture()) {
        TabletopLayout()
    } else {
        FlatLayout()
    }
}
```

Now, with `UIMediaQuery`, you can add the `mediaQuery` syntax to query device properties, such as if a device is in tabletop mode:

```kotlin
@OptIn(ExperimentalMediaQueryApi::class)
@Composable
fun VideoPlayer() {
    if (mediaQuery { windowPosture == UiMediaScope.Posture.Tabletop }) {
        TabletopLayout()
    } else {
        FlatLayout()
    }
}
```

Check out the [documentation](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery) and file any bugs [here](https://issuetracker.google.com/issues?q=componentid:1876021).

### **Grid (Experimental)**

[`Grid`](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) is a powerful new API for building complex, two-dimensional layouts in Jetpack Compose. While `Row` and `Column` are great for linear designs, `Grid` gives you the structural control needed for screen-level architecture and intricate components without the overhead of a scrollable list. `Grid` allows you to define your layout using tracks, gaps, and cells, offering familiar sizing options like `Dp`, percentages, intrinsic content sizes, and flexible "Fr" units.

```kotlin
@OptIn(ExperimentalGridApi::class)
@Composable
fun GridExample() {
    Grid(
        config = {
            repeat(4) { column(0.25f) }
            repeat(2) { row(0.5f) }
            gap(16.dp)
        }
    ) {
        Card1(modifier = Modifier.gridItem(rowSpan = 2)
        Card2(modifier = Modifier.gridItem(colmnSpan = 3)
        Card3(modifier = Modifier.gridItem(columnSpan = 2)
        Card4()
    }
}
```

You can place items automatically or explicitly span them across multiple rows and columns for precision. Best of all, it's highly adaptive---you can dynamically reconfigure your grid tracks and spans to respond to device states like tabletop mode or orientation changes, ensuring your UI looks great across form factors.
![Grid.gif](https://developer.android.com/static/blog/assets/Grid_eb3d39af12_18MCYj.webp)

Check out the [documentation](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) and file any bugs [here](https://issuetracker.google.com/issues/new?component=1876021&template=1424126).

### **FlexBox (Experimental)**

[FlexBox](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#FlexBox(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.FlexBoxConfig,kotlin.Function1)) is a layout container designed for high performance, adaptive UIs. It manages item sizing and space distribution based on available container dimensions. It handles complex tasks like wrapping (`wrap`) and multi-axis alignment of items (`justifyContent, alignItems, alignContent`). It allows items to grow (`grow`) or shrink (`shrink`) to fill the container.

```kotlin
@OptIn(ExperimentalFlexBoxApi::class)
fun FlexBoxWrapping(){
    FlexBox(
        config = {
            wrap(FlexWrap.Wrap)
            gap(8.dp)
        }
    ) {
        RedRoundedBox()
        BlueRoundedBox()
        GreenRoundedBox(modifier = Modifier.width(350.dp).flex { grow(1.0f) })
        OrangeRoundedBox(modifier = Modifier.width(200.dp).flex { grow(0.7f) })
        PinkRoundedBox(modifier = Modifier.width(200.dp).flex { grow(0.3f) })
    }
}
```
![AnimationGif.gif](https://developer.android.com/static/blog/assets/Animation_Gif_9b060dce28_1i16ER.webp)

Check out the [documentation](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox) and file any bugs [here](https://b.corp.google.com/issues/new?component=1876021&title=%5BFlexBox%5D&pli=1&template=0).

### **New SlotTable implementation (Experimental)**

We've introduced a new implementation of the `SlotTable`, which is disabled by default in this release. `SlotTable` is the internal data structure that the Compose runtime uses to track the state of your composition hierarchy, track invalidations/recompositions, store remembered values, and track all metadata of the composition at runtime. This new implementation is designed to improve performance, primarily around random edits.

To try the new `SlotTable`, enable [`ComposeRuntimeFlags.isLinkBufferComposerEnabled`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/ComposeRuntimeFlags#isLinkBufferComposerEnabled()).

## Start coding today!

With so many exciting new APIs in Jetpack Compose, and many more coming up, it's never been a better time to [migrate to Jetpack Compose](https://developer.android.com/develop/ui/compose/migrate/migrate-xml-views-to-jetpack-compose). As always, we value your feedback and feature requests (especially on `@Experimental` features that are still baking) --- please file them [here](https://goo.gle/compose-feedback). Happy composing!

###### Written by:

-

  ## [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta)

  ###### Developer Advocate, Android

  [read_more
  View profile](https://developer.android.com/blog/authors/meghan-mehta) ![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp) ![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.

  ###### [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) •
  2 min read

  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  4 min read

  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)