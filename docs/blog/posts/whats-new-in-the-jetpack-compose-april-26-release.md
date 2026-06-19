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

- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 18 Jun 2026 18 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2x_325a484212_1BGPPB.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Building a safer ecosystem together](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together) Last year, we introduced Android developer verification to strengthen ecosystem security and stop malicious actors from hiding behind anonymity to release harmful apps.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_D_Android_XR_Strapi_39d27725e6_Zhwmdd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.

  ###### [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) •
  3 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4)
- [![](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_ZDTMlF.webp)](https://developer.android.com/blog/authors/simona-milanovic) 09 Jun 2026 09 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Dev_Productivity_Strapi_b7e79722e6_45umk.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top 3 updates for Android developer productivity](https://developer.android.com/blog/posts/top-3-updates-for-android-developer-productivity)

  [arrow_forward](https://developer.android.com/blog/posts/top-3-updates-for-android-developer-productivity) Every year, Google I/O brings new announcements and resources across ecosystems and products, including Android development. As development shifts toward AI and agent-assisted tooling, we've expanded our offerings to better support you, however you decide to build for Android.

  ###### [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)