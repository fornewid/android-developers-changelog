---
title: https://developer.android.com/blog/posts/jetpack-compose-november-2026-release
url: https://developer.android.com/blog/posts/jetpack-compose-november-2026-release
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# What's new in the Jetpack Compose November '26 release

10 min read ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_812f851abd_WuQ5h.webp) 18 Nov 2026 [![View Meghan Mehta's profile](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z2r6wan.webp)](https://developer.android.com/blog/authors/meghan-mehta.md.txt) [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta.md.txt) Developer Advocate, Android The Jetpack Compose November '26 release is stable! This release brings version 1.13 across core Compose modules (see the full [BOM mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping.md.txt)), introducing updates to text, graphics, layouts, performance, and more---along with a few important deprecations and behavior changes to be aware of.

To update your project to this release, upgrade your Compose BOM version to 2026.11.01. Note that this upgrade requires **Kotlin 2.2** (or newer) and `compileSdk 37.1`.

```kotlin
implementation(platform("androidx.compose:compose-bom:2026.11.01"))
```

## Graphics

We continue to add many new graphics features into Compose. Compose 1.13 introduced polygon shapes, progressive blur, and the ability to configure blur properties directly on Dialogs and Popups.

### **Progressive blur**

Jetpack Compose 1.13 introduces [progressive blur](https://developer.android.com/develop/ui/compose/graphics/blur/overview.md.txt#progressive-blur), letting you transition elements from sharp to blurred seamlessly. Progressive blur is built on a draw-phase lambda using `Modifier.blur { ... }` and [BlurRadiusSpec](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/blur/BlurRadiusSpec.md.txt). You can implement linear gradients (such as vertical or horizontal transitions), radial gradients for focal spotlight effects, or even pass custom AGSL `RuntimeShaders` to drive dynamic, procedural blur maps.

Whether you're blending the bottom edge of a header image into a background using `BlurredEdgeTreatment.Unbounded`, or tracking touch coordinates with a radial spotlight, progressive blurs make premium, tactile depth-of-field effects incredibly straightforward to implement on Android.

```kotlin
Modifier.blur {
    blurRadiusSpec = BlurRadiusSpec.linearGradient(
        start = DpOffset.Zero,
        end = DpOffset(size.width, size.height),
        stops = listOf(
            BlurStop(fraction = 0f, radius = 0.dp),
            BlurStop(fraction = 0.5f, radius = 0.dp),
            BlurStop(fraction = 0.75f, radius = 14.dp),
            BlurStop(fraction = 1f, radius = 28.dp),
        ),
    )
}
```
![image5_size.png](https://developer.android.com/static/blog/assets/image5_size_b0ac4184d7_Z1pAe7O.webp) Linear gradient applied to the bottom 75% of the photo.

### **Polygon shapes and morphing**

Compose 1.13 adds `PolygonShape` and `MorphPolygonShape` to `androidx.compose.foundation:foundation`. Until now, rounded polygons, stars, and shape morphing in Compose required using [`androidx.graphics:graphics-shapes`](https://developer.android.com/jetpack/androidx/releases/graphics.md.txt) directly --- adding the dependency, creating a `RoundedPolygon` at the right pixel size, converting it to a `Path`, and writing your own `Shape` to fit it to the layout bounds.

`PolygonShape` is a regular Compose [Shape](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Shape.md.txt), so it works with `Modifier.clip` or any component's shape parameter, and it resolves to the layout size automatically. `MorphPolygonShape` animates between two polygon shapes by reading a progress lambda at draw time, without recomposition. Use `graphics-shapes` directly only when you're outside Compose UI or need the raw RoundedPolygon geometry. You don't need to add `graphics-shapes` to use `PolygonShape`, as `foundation` already depends on it.

```kotlin
var recording by remember { mutableStateOf(false) }
val progress by animateFloatAsState(if (recording) 1f else 0f)
val shape = remember {
   MorphPolygonShape(
       start = PolygonShape.circle(),
       end = PolygonShape.star(
           numPoints = 9,
           innerRadiusRatio = 0.8f,
           outerRounding = CornerRounding.fraction(0.5f),
       ),
       progress = { progress },
   )
}
Box(
   Modifier
       .size(96.dp)
       .clip(shape)
       .background(MaterialTheme.colorScheme.primary)
       .clickable { recording = !recording }
)
```
![Button morphs from a circle into a star when you interact with it.](https://developer.android.com/static/blog/assets/image9_300w_afbf2d3627_Z10O0hb.webp) Button morphs from a circle into a star when you interact with it.

### **Background blur and pop up properties**

You can now configure `blurBehindRadius`, `backgroundBlurRadius`, `scrimAlpha`, and `windowShape` (to clip dialog background blurs to rounded corners) directly on `DialogProperties` (and `blurBehindRadius/scrimAlpha` on PopupProperties).   
You can also query system cross-window blur state via `WindowInfo.isCrossWindowBlurEnabled`.

### **Graphics performance improvements**

#### **Caching improvements**

In Compose 1.13, rendering static icons is more efficient. `VectorPainter` automatically shares and reuses rasterized draw caches across painters rendering the same static `ImageVector` at the same size and configuration, eliminating redundant bitmap allocations and rasterization. To maximize caching, reuse `ImageVector` instances across composition instead of recreating them. This optimization is enabled by default via `ComposeUiFlags.isVectorDrawCacheSharingEnabled`.

#### **Modifier border improvements**

`Modifier.border` now features a faster, more performant implementation, adds support for runtime shaders (`ShaderBrush` with a `RuntimeShader`) across all shape types, and consistently uses the outline size when rendering borders.

To learn more about all the new graphics features in Compose and on the Android Platform, check out the talk from Android Dev Summit 2026:
[Video](https://www.youtube.com/watch?v=TirZPDPV8Dw)

## Material 3 1.5.0

Compose Material 3 version 1.5.0 is now stable and introduces the following:

- `Slider` and `RangeSlider` have migrated to a stateful model with `SliderState`.
- New expressive components including `ToggleButtons`, `WavyProgressIndicators`, and `TimePickers`.
- APIs including `BottomAppBar`, `TopAppBar variants`, and `BasicAlertDialog` graduated to stable.
- The `material3-ripple` artifact with inset focus rings.

In this release, we cut experimental annotations by 52 percent---dropping from 120 down to 58. We've also graduated almost every new expressive component to stable. As Material 3 enters its sixth year of availability, the Compose Material 2 library is deprecated and no longer actively maintained. We recommend migrating from Material 2 to Material 3 to get the latest bug fixes and design language for Android. Upgrade your dependencies to Material 3 1.5.0 today to bring these new expressive components to your apps. Learn more about all the new components, performance updates, and behavior changes in the [blog post](https://m3.material.io/blog/compose-material-3-is-stable).

## Text

### **Migrate to state-based BasicTextField**

The value-based [`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicTextField.composable.md.txt#BasicTextField(kotlin.String,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.ui.text.input.VisualTransformation,kotlin.Function1,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,kotlin.Function1)) and Material 2 [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/TextField.composable.md.txt#TextField(kotlin.String,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)) are officially deprecated. This shift directs you to transition to the more robust state-based [`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicTextField.composable.md.txt#BasicTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.input.TextFieldDecorator,androidx.compose.foundation.ScrollState)) and [`TextFieldState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState.md.txt) APIs.

If you're using Material 3, your existing value-based `TextField` overloads are not deprecated yet in 1.5.0, but we recommend migrating to the state-based `TextField` and `OutlinedTextField` overloads to take full advantage of synchronous state, improved performance, and upcoming features. If you are still on Material 2, migrate directly to Material 3's state-based text fields.

By migrating to `TextFieldState`, which natively supports saving and restoring formatted styles, you gain improved, out-of-the-box performance and a safer, synchronous state model. This release also removes experimental annotations from [undo/redo history](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/UndoState.md.txt) and [change tracking buffers](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldBuffer.ChangeList.md.txt). Legacy utilities like `VisualTransformation` are deprecated in this release, making way for streamlined alternatives like `OutputTransformation` and `InputTransformation`, including its built-in length-limit filters.

To learn more about how to [migrate to state-based text fields](https://developer.android.com/develop/ui/compose/text/migrate-state-based.md.txt), check out this talk from Android Dev Summit 2026:
[Video](https://www.youtube.com/watch?v=1DvjkRYGs2g)

### **Per-line line height**

When displaying multilingual text or mixed font sizes within a single paragraph, uniform line spacing can cause tall scripts (such as Burmese, Khmer, or Thai) to collide with adjacent lines. Compose 1.13 introduces `LineHeightStyle.Mode.PerLine`, which calculates line height independently for each line. This allows lines with taller glyphs or larger spans to dynamically expand to fit their natural bounds without clipping or disrupting the rest of the paragraph.
![image10.png](https://developer.android.com/static/blog/assets/image10_72df2b2519_Z1FMwHJ.webp) Comparison of Mode.Fixed (default, left) vs. Mode.PerLine (right) preventing text collisions in multilingual layouts.

### **Mergeable FontVariation.Settings**

Compose 1.13 adds merge overloads to `FontVariation.Settings`, making it easy to define base variable font configurations and dynamically override specific axes (like weight, slant, or width) without re-allocating or rebuilding the entire settings list.

```kotlin
// Define a shared base configuration for your variable font
val baseVariation = FontVariation.Settings(FontVariation.weight(400), FontVariation.width(100f))

 
// Easily override or combine specific axes inline
val boldVariation = baseVariation.merge(FontVariation.weight(700))
val condensedVariation = baseVariation.merge(FontVariation.width(85f))
```

## Performance

### **Performance static analysis skill**

We've added a new Jetpack Compose performance [static analysis skill](https://github.com/android/skills/tree/main/jetpack-compose/jetpack-compose-performance) that provides zero-setup code auditing and generation across seven key categories---state and stability, lazy layouts, layouts, graphics, animation, effects and threading, and `Modifier.Node` migrations---allowing you to run standalone checks on any PR, file, or screen to comply with current best practices. Try it out today through the [Android CLI](http://goo.gle/android-cli)!
![Jetpack Compose Performance Skill](https://developer.android.com/static/blog/assets/jetpack_compose_performance_16x9_1_89d03a76f1_2ax0uK.webp)

### **computedStateOf**

A new mechanism for state computation, [`computedStateOf`](https://developer.android.com/agents/skills/jetpack-compose/jetpack-compose-performance/references/state-and-stability.md.txt#d_use_computedstateof_versus_derivedstateof_compose_113), has been introduced in 1.13. It provides a lightweight alternative to `derivedStateOf`, and is intended for condition checks and filtered state calculated from other frequently-changing states (like scroll position and animation thresholds). By not caching calculation results, it has less overhead than `derivedStateOf`---especially when the calculation is invalidated by one of its referenced states changing.

Both state variations invalidate composition when the result of the calculation changes, not when their input states change. They are commonly applied to convert frequently changing states into infrequently changing states, preventing invalidations in your composition hierarchy for unimpactful state changes. You should reserve `derivedStateOf` for heavy calculations or where caching is otherwise necessary. In general, we recommend using `computedStateOf` instead of `derivedStateOf` for state computation.

### **Recomposition tracing in Perfetto**

[Recomposition tracing](https://developer.android.com/develop/ui/compose/tooling/tracing.md.txt#recomposition-tracing) is a new way to augment existing composition tracing with new information about state reads and state writes, providing you with a full overview of the state changes that caused recompositions. For each read and write affecting composition, it records the state's string representation and stack trace to pinpoint the exact line of code where the change occurred.

Note that recording additional data for recomposition tracing adds overhead, so make sure to disable it when investigating your app's performance.

### **Hero benchmarks**

Compose 1.13 matches Compose 1.12.1 across **all our baseline startup and scrolling benchmarks with a 0% jank rate** on Pixel 6. On cold startups, Compose 1.13 still achieves a faster Time to Initial Display (147.65 ms) than Views (152.87 ms)
![image4_size.png](https://developer.android.com/static/blog/assets/image4_size_f52c6c759d_U6FmV.webp)

Views remain faster on Time to Full Display (180.32 ms versus 202.79 ms for Compose) due to differences in data flow starts and GPU shader work. Scrolling frame duration (P50) sits at 3.51 ms for Compose compared to 3.06 ms for Views, with overall performance remaining stable and consistent across valid test runs. We continue to invest heavily in improving performance across all performance metrics, with a focus on startup metrics. For the full results, check out the [documentation](https://developer.android.com/develop/ui/compose/performance/herobenchmark.md.txt).

To learn more about performance, check out the talk from Android Dev Summit 2026:
[Video](https://www.youtube.com/watch?v=t5ujT_o8qj0)

## Layouts

### **Stable FlexBox and Grid**

[`FlexBox`](https://developer.android.com/develop/adaptive-apps/guides/flexbox.md.txt) and [`Grid`](https://developer.android.com/develop/adaptive-apps/guides/grid.md.txt) layouts (announced in [Compose 1.11](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release.md.txt)) are officially graduating from experimental to stable. These APIs are production-ready, highly performant alternatives for wrapped grids and responsive designs. FlexBox also gains a new configuration `maxItemsInEachLine` that lets you limit the number of items in a line when wrapping is enabled.

FlexBox supersedes the Flow layouts (`FlowRow` and `FlowColumn`), and we recommend using `FlexBox` instead of Flow layouts for new code. For a detailed comparison of the layout containers, see [layout containers](https://developer.android.com/develop/ui/compose/layouts/containers.md.txt).
![FlexBox layout responding to screen configuration changes](https://developer.android.com/static/blog/assets/image6_size_again_again_1a7cc74608_Z13Blu6.webp) FlexBox layout responding to screen configuration changes. ![A flexible and adaptive two-dimensional layout with Grid](https://developer.android.com/static/blog/assets/image3_size_again_again_81c5a9c272_fArco.webp) A flexible and adaptive two-dimensional layout with Grid.

### **ConstraintLayout and MotionLayout deprecation**

With the introduction of more modern layout and animation tooling in Compose and new Shared Element APIs---we are officially deprecating `ConstraintLayout` and `MotionLayout` in Compose ([`androidx.constraintlayout:constraintlayout-compose`](https://developer.android.com/jetpack/androidx/releases/constraintlayout.md.txt) artifact).

These newer alternatives provide performant solutions, offering a streamlined approach to building complex user interfaces native to Compose. We recommend migrating your ConstraintLayout Compose usages to the alternatives above.

### **Stable LazyLayoutCacheWindow**

Stabilization of `LazyLayoutCacheWindow` brings robust caching and window-based prefetching directly to all primary lazy collection families---lists, grids, and staggered grids. This functionality improves performance of lazy layouts for off-screen compositions.

Key highlights in this release include:

- **Simplified API configuration** : Cache window settings have moved from the scroll state holder (such as `rememberLazyListState`) directly into the layout composables (`LazyColumn`, LazyVerticalGrid, etc.), making prefetching and caching a direct layout concern.
- **Window-based prefetching**: Replaces legacy item-based prefetching with a default window-based prefetch engine that dynamically calculates an ahead window based on viewport metrics, with the option to customize both ahead and behind windows to retain off-screen compositions.

Learn how Instagram Direct benefited from using `LazyLayoutCacheWindow` in the [case study blog post](https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct.md.txt), and check out the [documentation](https://developer.android.com/develop/ui/compose/lists.md.txt#cache-window) to learn more.

## Animation

Compose 1.13 stabilizes [DeferredTransition](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/DeferredTransition.md.txt) and introduces a new composable, `CapturedAnimatedVisibility`.

### **CapturedAnimatedVisibility**

`AnimatedVisibility` requires the outgoing content and states to be retained during the exit animation, as it continues to compose its content until the exit animation finishes. When the content depends on the state that's already gone, it can cause visible flickering. For example, when closing a details pane sets the selected item to `null`, the existing content has nothing left to show. You either see a blank or a flicker mid-animation, a crash if you used `!!`, or you have to hold on to the old value yourself.

Compose 1.13 introduces `CapturedAnimatedVisibility`. This composable does not require the caller to manage states during the exit because it captures a snapshot of the last frame instead when `visible` becomes false. You can clear your state immediately, and the exit animation still shows what was on screen.

```kotlin
@Composable
fun TrackDetails(track: Track?) {
    // `track` becomes null as soon as the details are closed. CapturedAnimatedVisibility
    // removes the content right away and animates a snapshot of its last frame instead.
    CapturedAnimatedVisibility(
        visible = track != null,
        enter = fadeIn() + expandVertically(),
        exit = fadeOut(tween(800)) + shrinkVertically(tween(800)),
    ) {
        if (track != null) {
            TrackCard(track)
        }
    }
}
```
![Closing the details sets track to null.](https://developer.android.com/static/blog/assets/image2_size_again_7c2d6524d9_Z2tlYvD.webp) Closing the details sets track to null. With AnimatedVisibility (left), the card disappears with nothing to animate. CapturedAnimatedVisibility (right) animates out its last frame.

Releasing state immediately also makes exits cheaper: in our benchmarks, performance during exit is 7--8% faster in terms of frame time than with `AnimatedVisibility`. Keep using `AnimatedVisibility` when the exiting content needs to stay live, or when you need to use `Modifier.animateEnterExit()` on its children, otherwise prefer `CapturedAnimatedVisibility`.

## Custom failure handling in tests

Debugging failing UI tests, especially in CI environments, often requires inspecting the screen state and semantics hierarchy at the exact moment an assertion fails. Compose 1.13 introduces a native failure handling pipeline via [`TestFailurePolicy`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/TestFailurePolicy.md.txt) in [`ComposeUiTestConfig`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTestConfig.md.txt) to automate test diagnostics.

With `TestFailurePolicy`, you can:

- **Capture built-in artifacts:** Set `screenshotCaptureMode` and `uiHierarchyCaptureMode` to `CaptureMode.Enabled` to automatically dump a visual screenshot and the UI semantics tree whenever a test fails.
- **Run custom failure handlers:** Register one or more [`TestFailureHandler`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/TestFailureHandler.md.txt) instances to process the [`FailureContext`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/FailureContext.md.txt), which provides the root `error` and any generated `artifacts`. This allows you to upload screenshots or forward failure telemetry to external reporting tools.
- **Configure captures across an entire test suite:** Enable screenshot and UI hierarchy captures globally in your `build.gradle.kts` via `testInstrumentationRunnerArguments` (`androidx.compose.ui.test.failure.isScreenshotCaptureEnabled` and `androidx.compose.ui.test.failure.isUiHierarchyCaptureEnabled`) without modifying individual test files, while retaining the ability to override them per test.

```kotlin
val customConfig = ComposeUiTestConfig(
   failurePolicy = TestFailurePolicy(
       screenshotCaptureMode = TestFailurePolicy.CaptureMode.Enabled,
       uiHierarchyCaptureMode = TestFailurePolicy.CaptureMode.Enabled,
       failureHandlers = listOf(
           TestFailureHandler { context ->
               val screenshot = context.artifacts.firstOrNull {
                   it.type == FailureArtifact.Type.Screenshot
               }
               // Process or upload the artifact and context.error
           }
       )
   )
)
@Test
fun myTest() = runComposeUiTest(config = customConfig) {
   // Test content
}
```

## Adaptive Skill

Use the updated[Adaptive Skill](https://github.com/android/skills/blob/main/jetpack-compose/adaptive/SKILL.md) to optimize your Compose UI for foldables and desktop!

Build hands-free [tabletop experiences](https://developer.android.com/design/ui/mobile/guides/layout-and-content/postures-and-orientation.md.txt#tabletop) on foldables by rendering content on the upright screen and placing controls on the flat bottom half, keeping fingers off the view.  
The skill will also help to make your app feel native on desktop with keyboard shortcuts, tooltips, and custom cursors, plus proven patterns to prevent state loss when users rotate or unfold their devices. Try it out today through the [Android CLI](http://goo.gle/android-cli)!
![Jetpack Compose Adaptive Skill](https://developer.android.com/static/blog/assets/jetpack_compose_Adaptive_16x9_3_526b1c74fc_22QmJ6.webp)

Watch this Android Dev Summit talk to see how you can level up your foldable and desktop support:
[Video](https://www.youtube.com/watch?v=SGTkTKX7qq4)

## Accurate nested scroll velocity calculation

For apps with hybrid UI architectures, we resolved an issue where fast scrolling in Compose nested inside Android View scroll containers (such as `ScrollView`, `NestedScrollView`, or `CoordinatorLayout`) would sometimes calculate incorrect velocity. Velocity handoffs are now accurately computed, preventing abrupt stops or jumpy scroll physics and ensuring a smooth, fluid fling experience across View and Compose boundaries.

## Behavior change:
Modifier.onFocusedBoundsChanged is now deprecated

[`Modifier.onFocusedBoundsChanged`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/onFocusedBoundsChanged.modifier.md.txt) was deprecated in Compose 1.12, and in 1.13 its implementation has been removed, meaning it has no effect if the modifier is run. The old implementation didn't report focus bounds reliably in many situations and had performance issues.

Built-in scrolling containers such as `LazyColumn` and `Modifier.verticalScroll` already bring focused content into view without this API, so they aren't affected.

To get the focused element's bounds, call[`FocusTargetModifierNode.getFocusedRect()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary.md.txt#(androidx.compose.ui.focus.FocusTargetModifierNode).getFocusedRect()) from a custom `Modifier.Node`. It returns the bounds when you ask for them, rather than reporting every change through a callback. To react to focus changes, use[`Modifier.onFocusChanged`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary.md.txt#(androidx.compose.ui.Modifier).onFocusChanged(kotlin.Function1)). To scroll a focused item into view in a custom container, pair `onFocusChanged` with[`BringIntoViewRequester`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/relocation/BringIntoViewRequester.md.txt).

## Behavior change: Platform interaction sound effects on Android

Clickable elements configured with `Modifier.clickable` (or components built on top of it) now automatically play standard Android interaction sound effects, respecting the user's system sound settings. Previously, Compose clickable elements required manually invoking sound effects to achieve parity with traditional Android Views. This update ensures interactive elements provide immediate audio feedback and feel native to the Android platform out of the box.

## An update on Styles

At Google I/O, we previewed a new way to customize components without forking source code. In Compose 1.13, this foundational architecture has evolved into an unopinionated styling engine. Instead of the framework hardcoding visual properties, property definitions have moved to the design system layer---enabling teams to declare custom brand tokens (`stylePropertyOf / styleLocalOf`) with total autonomy.

Because of this architectural shift, the Styles API remains experimental in Compose 1.13. We are actively working with partners and Material 3 to refine style merging and developer ergonomics before general availability. We've removed the documentation and skill for Styles during this transition.

## New Compose Web library for easier WebView migration (alpha)

Embedding web content inside Compose is one of the final migration friction points for apps. Legacy implementations using `AndroidView` can introduce scroll stutter, state loss during configuration changes or navigation, and interop rendering overhead.

To eliminate this friction, we're launching in two libraries built on two complementary primitives across `androidx.web`:

- `WebContent` (Available now in [`androidx.web:web:1.0.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/web.md.txt)): A state holder that decouples web state (including scroll position, form inputs, navigation history, and JavaScript state) from the view hierarchy so it outlives configuration changes and navigation without leaking your `Activity`.

```kotlin
@Composable
// Assumes `webContent` is already created and retained (e.g., in a ViewModel or via `retain`)
fun WebContentPage(webContent: WebContent, startUrl: String, modifier: Modifier = Modifier) {
   key(webContent) {
       AndroidView(
           factory = { context ->
               webContent.attach(context, ::WebContentView).apply {
                   settings.javaScriptEnabled = true
                   if (url == null) loadUrl(startUrl)
               }
           },
           modifier = modifier,
           onRelease = { view ->
               // The view must leave the hierarchy before WebContent is detached.
               (view.parent as? ViewGroup)?.removeView(view)
               webContent.detach()
           },
       )
   }
}
```

- `WebSurface `(Available soon): A dedicated composable optimized for `WebContent` that bypasses `AndroidView` interop overhead.

Try out the APIs today by importing [`androidx.web:web:1.0.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/web.md.txt), and stay tuned for `WebSurface` alpha release in the near future.

## New Jetpack Compose A2UI renderer

Runtime LLM responses shouldn't be limited to plain text. The new Jetpack Compose A2UI Renderer implements the open [Agent-to-UI (A2UI) protocol](https://a2ui.org/).

```kotlin
implementation("androidx.compose.material3:material3-a2ui:1.0.0-alpha02")
```

AI agents can create rich, interactive UIs at runtime, which render as native Compose components without executing arbitrary code. The renderer handles message parsing and schema validation and feeds agent data into Compose snapshot state. Use the ready-made Basic Catalog, or plug in your own composables and design system. Get started with the documentation, or check out the talk from Android DevSummit.
[Video](https://www.youtube.com/watch?v=qIvsFGvlHdo)

## Documentation updates

We have new documentation available, covering [Anchored draggable](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/drag-composables.md.txt#drag-a-composable-element), [Navigation3 Deep Links](https://developer.android.com/guide/navigation/navigation-3/deep-links.md.txt), and [AppState](https://developer.android.com/topic/libraries/architecture/appstate.md.txt).

## Happy Composing!

Compose 1.13 makes app development easier and more expressive than ever with updates to text, graphics, layouts, performance and more! To see the full set of changes between BOM versions, take a look at the [BOM comparison tool](https://developer.android.com/develop/ui/compose/bom/bom-mapping.md.txt?from=2026.09.00&to=2026.11.01#compare-bom-versions) to see the difference.

To learn more about what's new for Compose, watch the latest talks from the [Android Dev Summit](https://developer.android.com/events/dev-summit.md.txt).

As always, we value your input, so please share your feedback on these changes or what you'd like to see next on our [issue tracker](https://issuetracker.google.com/issues/new?component=612128). Happy composing!
- [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
Written by:

-

  ## [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta.md.txt)

  ###### Developer Advocate, Android

  [read_more
  View profile](https://developer.android.com/blog/authors/meghan-mehta) ![View Meghan Mehta's profile](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z2r6wan.webp) ![View Meghan Mehta's profile](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z2r6wan.webp)
Continue reading
- [![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp)](https://developer.android.com/blog/authors/jan-kleinert.md.txt) 21 Sep 2026 21 Sep 2026 ![](https://developer.android.com/static/blog/assets/Games_for_car_Strapi_1_c55588726e_Z2cIhWx.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Bring your Android game to the car screen today](https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today.md.txt) Today, the games category for Android Auto and cars powered by Android Automotive OS with Google built-in is officially graduating from beta to general availability.
  [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert.md.txt) • 3 min read
  - [#Android Automotive OS](https://developer.android.com/blog/topics/android-automotive-os.md.txt)
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto.md.txt)
  - +1 ↩
- 3 Authors 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_2cdxMf.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in Android for Cars: Unifying platforms and unlocking premium experiences](https://developer.android.com/blog/posts/whats-new-in-android-for-cars-unifying-platforms-and-unlocking-premium-experiences.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-android-for-cars-unifying-platforms-and-unlocking-premium-experiences.md.txt) We're thrilled to see developers continuing to bring their apps and experiences to Android for Cars! Over the past year, we've continued to see strong growth and momentum in the app ecosystem on Android Auto and cars with Google built-in.
  [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert.md.txt), [Noam Gefen](https://developer.android.com/blog/authors/noam-gefen.md.txt), [Thomas Weathers](https://developer.android.com/blog/authors/thomas-weathers.md.txt) • 3 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher.md.txt) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Compose_first_Meta_04fd0498ba_21k6io.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Android UI Development is Compose First](https://developer.android.com/blog/posts/android-ui-development-is-compose-first.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-ui-development-is-compose-first.md.txt) In the almost-5-years since Jetpack Compose launched, we've invested in bringing you all the features, performance and tools that you need to build amazing UIs across the variety of Android devices.
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher.md.txt) • 2 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)