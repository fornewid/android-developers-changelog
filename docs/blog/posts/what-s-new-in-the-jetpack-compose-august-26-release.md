---
title: https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release
url: https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# What's new in the Jetpack Compose August '26 release

5 min read ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) 11 Aug 2026 [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) Product Manager Today, the Jetpack Compose August '26 release is stable! This release brings version 1.12 across core Compose modules (see the full [BOM mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping)), introducing rich visual APIs like Mesh Gradients and Wide Color Gamut (WCG) support, structural layout features like named areas in `Grid`, seamless integration with Android's Credential Manager, and significant testing and performance improvements.

To update your project to today's release, upgrade your [Compose BOM](https://developer.android.com/develop/ui/compose/bom) version to `2026.08.00`:

```kotlin
implementation(platform("androidx.compose:compose-bom:2026.08.00"))
```

### **Breaking Changes**

- **AGP \& Compile SDK** : Compose 1.12 updates compileSdk to API 37, requiring a minimum AGP 9.1.2. As a reminder, Compose will always target the latest compileSdk. Learn more about this change [here](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler#agp-compatibility).
- `Modifier.onFirstVisible()`**is deprecated** : Migrate to [Modifier.onVisibilityChanged()](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/onVisibilityChanged.modifier), which provides more precise visibility threshold tracking.

## **Graphics**

### **Mesh Gradients**

Compose 1.12 introduces [`MeshGradientPainter`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/MeshGradientPainter) to help you create multi-point, organic color gradients.
![image.png](https://developer.android.com/static/blog/assets/image_f7fb408503_Z2hoyTa.webp)

```kotlin
val rows = 1
val columns = 1

val gradientPainter = remember {
    MeshGradientPainter(rows, columns) {
        // Parameters: row, column, position, color
        setVertex(0, 0, Offset(0f, 0f), Color.Red)     // Top-Left
        setVertex(0, 1, Offset(1f, 0f), Color.Blue)    // Top-Right
        setVertex(1, 0, Offset(0f, 1f), Color.Green)   // Bottom-Left
        setVertex(1, 1, Offset(1f, 1f), Color.Yellow)  // Bottom-Right
    }
}

Box(
    modifier = modifier
        .aspectRatio(16/9f)
        .fillMaxWidth()
        .paint(gradientPainter)
)
```

For more information and examples, see the [documentation](https://developer.android.com/develop/ui/compose/graphics/draw/mesh-gradient).

### **Wide Color Gamut \& HDR Support**

Modern displays offer extended color fidelity and higher dynamic range. In Compose 1.12, full pipeline support for **Wide Color Gamut (P3)** and **HDR rendering** has been enabled across Compose graphics, paint, and shaders. Colors defined in non-sRGB color spaces (such as Display P3) are preserved through to platform rendering without color clamping. Colors will safely fall back to sRGB if they use an unsupported color space (e.g. CieXyz, CieLab, or Oklab), rely on a color space on an unsupported Android version (e.g Bt2020Hlg on Android 13 and below), or if the app is running on Android 9 (API 28) and below.

Other notable changes:

- [`LayerOutsets`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/LayerOutsets) was added to `GraphicsLayer` \& `Modifier.graphicsLayer`, which you can use to increase the visual bounds of the layer beyond its measured size. Apply `LayerOutsets` to avoid the implicit `clipToBounds` behavior when the layer is promoted to an offscreen buffer.

## **Styles**

At Google I/O, we shared our early vision for the Compose [Styles API](https://developer.android.com/develop/ui/compose/styles)---a unified, performant way to style components. Since then, we have continued building the underlying architecture to guarantee strict type safety and predictable correctness, and to support building custom design systems.

To ensure we get this foundational layer correct, the API will remain experimental, and you can expect breaking changes.

## **Runtime Optimizations**

### **Keyed** SideEffect**Overload**

[`SideEffect`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/SideEffect.composable) now supports key arguments, which lets you fire one-shot side effects whenever specific keys change. This can lead to better performance compared to using a `LaunchedEffect` or `DisposableEffect `when you don't need the coroutine or dispose block. `SideEffect` is up to 90% faster than `LaunchedEffect` and around 20% faster than `DisposableEffect`. Note that `SideEffect` runs its effect before `DisposableEffect` and `LaunchedEffect`, so use caution if migrating existing effects to this API, especially for `LaunchedEffects` that rely on being dispatched to start after the current frame is completed.

```kotlin
@Composable
fun AnalyticsTracker(userId: String, screenName: String) {
    SideEffect(key1 = userId, key2 = screenName) {
        analytics.logScreenView(userId, screenName)
    }
}
```

## **Animation**

- [`DeferredTargetAnimation`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/DeferredTargetAnimation) has graduated out of experimental status.

### **Interactive Two-Stage Transitions**

- **New composables** : [`DeferredAnimatedContent`](https://developer.android.com/reference/kotlin/androidx/compose/animation/DeferredAnimatedContent.composable) and [`DeferredAnimatedVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/animation/DeferredAnimatedVisibility.composable) allow creating delightful two-stage transitions, e.g. for predictive back gesture tracking.
- **Manual animation control**: During a transition's deferred phase, animated properties (like scale or offset) can now be manually manipulated in real-time (e.g., tracking a swipe gesture).
- **Seamless handoff**: Once the deferred phase ends, the transition engine takes over and performs a seamless handoff, including velocity transfer, to the automatic transition.
- **Shared element support** : A new [`permitTransformDuringDeferredTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SharedTransitionScope.SharedContentConfig#permitTransformDuringDeferredTransition()) flag in `SharedContentConfig` controls whether shared elements visually transform along with their parent containers during the deferred transition phase.

```kotlin
val state = remember { DeferredTransitionState(initialScreen) }
val transition = rememberDeferredTransition(state)

if (predictiveBackInProgress) {
    state.defer(targetScreen)
} else {
    state.animateTo(targetScreen)
}

transition.DeferredAnimatedContent(
    targetState = targetScreen,
    mutableTransformSpec = {
       MutableContentTransform {
           // Manually manipulate properties during the deferred phase
           initialContentTransform { scale = swipeProgress }
       }
    }
) { screen ->
    ScreenContent(screen)
}
```

Below are two demos of use cases where a gesture-driven animation is handed off to a triggered animation:
![image.png](https://developer.android.com/static/blog/assets/image_4997083c8b_Z1GXd91.webp)

## **Text, Input \& Platform Integrations**

### **Editable Text Formatting**

New APIs offer rich-text formatting for editable text in [`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicTextField.composable). You can now programmatically apply and manipulate inline character and paragraph formatting using [`SpanStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/SpanStyle) and [`ParagraphStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/ParagraphStyle) via the new `addStyle()` method inside a [`TextFieldBuffer`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer) scope (such as inside `textFieldState.edit { ... }` or an `InputTransformation`). Additionally, `TextFieldBuffer` provides `getSpanStyles()` and `getParagraphStyles()` APIs that return `TrackedRange` objects, allowing you to read, update, or remove applied styles. To complement formatting creation, `TextFieldState` now exposes a read-only `textStyles` property for querying active styles across ranges, while `TextFieldBuffer` provides `originalTextStyles` to inspect formatting state prior to an edit. Text formatting and custom annotations are persisted across configuration changes.

```kotlin
val state = rememberTextFieldState("Formatted text in Compose 1.12")

// Apply bold and color styles to a range of text
state.edit {
    addStyle(
        SpanStyle(fontWeight = FontWeight.Bold, color = Color.Blue),
        start = 0,
        end = 9
    )
}

// Query active styles from TextFieldState
val currentStyles = state.textStyles
```

### **Text Selection**

A new [`SelectionState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/selection/SelectionState) API provides programmatic control and observability over text selection within a [`SelectionContainer`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/selection/SelectionContainer.composable#SelectionContainer(androidx.compose.ui.Modifier,kotlin.Function0)). Hoisting a `SelectionState` object via `rememberSelectionState()` and passing into `SelectionContainer` exposes `selectedTexts` as a reactive list of `AnnotatedStrings` and provides methods like `selectAll()`, `clear()`, `select(TextRange)`, and `extendSelectionByWord()`.

Additionally, use `getSelectableTexts()` to retrieve all selectable text items in layout order and select text across composables in the `SelectionContainer` using a global range.

```kotlin
@Composable
fun ProgrammaticSelectionExample() {
    val selectionState = rememberSelectionState()

    Column {
        Button(
            onClick = { selectionState.selectAll() },
            modifier = Modifier.disableSelectionClearOnTap()
        ) {
            Text("Select All")
        }

        SelectionContainer(state = selectionState) {
            Text("Text content to be selected programmatically.")
        }
    }
}
```

### **Credential Manager Integration**

Compose text fields now natively integrate with Android's Credential Manager (API 34+) via the Autofill framework (below API 34 is handled by [`androidx.credentials library`](https://developer.android.com/jetpack/androidx/releases/credentials)). By attaching the new [`credentialRequest`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).credentialRequest()) semantics property with `CredentialRequestData`, text inputs can prompt passkeys, saved credentials, or sign-in requests directly within the user input flow.

```kotlin
@Composable
fun LoginField(textFieldState: TextFieldState) {
    val credentialData = remember {
        CredentialRequestData(
            // Specify Credential Manager request options
        )
    }

    BasicTextField(
        state = textFieldState,
        modifier = Modifier.semantics {
            credentialRequest = credentialData
        }
    )
}
```

Other notable changes:

- Support for font variation settings in [downloadable fonts](https://developer.android.com/develop/ui/compose/text/fonts?_gl=1*gwqhos*_up*MQ..*_ga*MTQ0MTMzODI2Ny4xNzg0MzAwNjk3*_ga_6HH9YJMN9M*czE3ODQzMDA2OTckbzEkZzAkdDE3ODQzMDA2OTckajYwJGwwJGgxOTczOTM3MzA4#downloadable-fonts).
- Enabled auto-scrolling when dragging text selection beyond the viewport in [`SelectionContainer`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/selection/SelectionContainer.composable).
- Added support for automatic interaction sounds (clicks and focus navigation) to Compose components, with a new [`SoundEffectOnInteraction`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/SoundEffectOnInteraction.composable) composable to allow opt-out. Note that as a consequence of this change, semantics click listeners must now be called from the main thread, which may affect a small number of test cases.
- [`KeyboardType`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/input/KeyboardType) now includes `Date`, `Time`, `DateTime`, and `SignedDecimal`.
- [`BasicSecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicSecureTextField.composable) now uses `TextObfuscationMode.System` by default, while `RevealLastTyped` serves as an absolute override.

## **Layout Enhancements**

### **Named Areas in Grid Layout**

Building complex 2D layouts is now easier with named areas in the `@Experimental` [Grid](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Grid.composable) component. Rather than managing numeric column and row indices across items, you can define semantic regions in your `GridConfigurationScope` and position composables by area name.

```kotlin
@OptIn(ExperimentalGridApi::class)
@Composable
fun DashboardLayout() {
    Grid(
        config = {
            area("header", row = 0, column = 0, rowSpan = 1, columnSpan = 2)
            area("sidebar", row = 1, column = 0)
            area("content", row = 1, column = 1)
            gap(16.dp)
        }
    ) {
        HeaderSection(modifier = Modifier.gridItem(areaId = "header"))
        NavigationSidebar(modifier = Modifier.gridItem(areaId = "sidebar"))
        MainContentView(modifier = Modifier.gridItem(areaId = "content"))
    }
}
```

For more information, see the [documentation](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid/container-properties#named-area).

## **Performance**

As with every release, we continue to invest in Compose's performance to ensure that the framework helps you to build beautiful, performant apps. In this release we've focused on improving startup performance and are now seeing Time to Initial Display (the time it takes for an app to produce its first frame) that is comparable to Views in our [benchmarks](https://developer.android.com/develop/ui/compose/performance/herobenchmark).
![timetoinitialdisplay@2x _v2.png](https://developer.android.com/static/blog/assets/timetoinitialdisplay_2x_v2_26db919929_25qsbc.webp)

## **Testing \& Tooling Upgrades**

### **Test Synchronization**

Compose 1.12 introduces new test APIs designed to reduce test execution times and eliminate flakiness during state sampling:

- [`hasPendingWork`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest#hasPendingWork()): Passively checks if the UI has pending work without advancing the clock, which is ideal for manual animation loops.
- [`runWithoutImplicitWait`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest#runWithoutImplicitWait(kotlin.Function0)): Temporarily disables implicit synchronization when stepping through manual clock frames (e.g. animation tests).

```kotlin
@Test
fun testAnimationStateFast() {

composeTestRule.mainClock.autoAdvance = false
    
    while (composeTestRule.hasPendingWork()) {
        composeTestRule.mainClock.advanceTimeByFrame()
        composeTestRule.waitForIdle()
        
        composeTestRule.runOnUiThread {
            composeTestRule.runWithoutImplicitWait {
                // This is most effective when querying multiple nodes in a single frame. 
                // It prevents the redundant synchronization overhead that would 
                // otherwise occur on every individual query.
                val box1 = composeTestRule.onNodeWithTag("Box1").fetchSemanticsNode()
                val box2 = composeTestRule.onNodeWithTag("Box2").fetchSemanticsNode()
                
                assertThat(box1.boundsInRoot.right).isAtMost(box2.boundsInRoot.left)
            }
        }
    }
}
```

Other notable changes:

- The [`captureToImage`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).captureToImage()) API now allows you to capture a popup or dialog together with its anchor in a single bitmap.
- Added [`onRootWithViewInteraction`](https://developer.android.com/develop/ui/compose/testing/interoperability#viewscoped-semantics) to scope Compose semantic searches to specific Android Views. This simplifies testing hybrid UIs, such as `RecyclerViews`, without requiring unique test tags in production code.
- [`@PreviewWrapper`](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/PreviewWrapper) annotations can now be applied to custom `@MultiPreview` classes, enabling reusable preview setups (such as custom themes) across multiple components.

## **Happy Composing!**

Compose 1.12 makes app development easier and more expressive than ever, with mesh gradients, wide color gamut support, downloadable variable fonts, Credential Manager integration, and faster testing tools. As always, we value your input, so please share your feedback on these changes or what you'd like to see next on our [issue tracker](https://issuetracker.google.com/issues/new?component=612128). Happy composing!
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Written by:

-

  ## [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/nick-butcher) ![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp) ![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)
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
- 3 Authors 28 Jul 2026 28 Jul 2026 ![](https://developer.android.com/static/blog/assets/Jetpack_compose_Strapi_123481f79e_Z1F9b9M.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Celebrating 5 years of Jetpack Compose](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose) Today, we officially celebrate five years since the release of Jetpack Compose 1.0. From version 1.0, announced on July 28th, 2021, to our latest 1.11 release, we've seen the APIs evolve significantly over the years, and we're taking a moment to celebrate.
  [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks), [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Compose_first_Meta_04fd0498ba_1T1vC6.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android UI Development is Compose First](https://developer.android.com/blog/posts/android-ui-development-is-compose-first)

  [arrow_forward](https://developer.android.com/blog/posts/android-ui-development-is-compose-first) In the almost-5-years since Jetpack Compose launched, we've invested in bringing you all the features, performance and tools that you need to build amazing UIs across the variety of Android devices.
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 2 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)