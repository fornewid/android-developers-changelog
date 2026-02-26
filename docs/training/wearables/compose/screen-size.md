---
title: https://developer.android.com/training/wearables/compose/screen-size
url: https://developer.android.com/training/wearables/compose/screen-size
source: md.txt
---

Compose for Wear OS Material version <button value="2.5">2.5</button> <button value="3" default="">3</button>

*** ** * ** ***

Your app should work well on Wear OS devices of all sizes, taking advantage of
additional space where available, and still look great on smaller screens too.
This guide provides recommendations for achieving this user experience.

To learn more about the design principles for adaptive layouts, read the
[design guidance](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-layouts).


## Build responsive layouts using Material 3

Layouts should have [percentage-based margins](https://developer.android.com/design/ui/wear/guides/foundations/canonical-adaptive-layouts#non-scrolling-responsiveness). Because Compose works by default in absolute values instead, use `rememberResponsiveColumnPadding` from the [Horologist Library](https://github.com/google/horologist) to calculate the padding and pass it to the `ScreenScaffold`'s `contentPadding` parameter and the `TransformingLazyColumn`'s `contentPadding` parameter.

<br />

The following code snippet uses a
`TransformingLazyColumn` component to create content that looks great on a variety
of Wear OS screen sizes:

```kotlin
val columnState = rememberTransformingLazyColumnState()
val contentPadding = rememberResponsiveColumnPadding(
    first = ColumnItemType.ListHeader,
    last = ColumnItemType.Button,
)
val transformationSpec = rememberTransformationSpec()
ScreenScaffold(
    scrollState = columnState,
    contentPadding = contentPadding
) { contentPadding ->
    TransformingLazyColumn(
        state = columnState,
        contentPadding = contentPadding
    ) {
        item {
            ListHeader(
                modifier = Modifier.fillMaxWidth().transformedHeight(this, transformationSpec),
                transformation = SurfaceTransformation(transformationSpec)
            ) {
                Text(text = "Header")
            }
        }
        // ... other items
        item {
            Button(
                modifier = Modifier.fillMaxWidth().transformedHeight(this, transformationSpec),
                transformation = SurfaceTransformation(transformationSpec),
                onClick = { /* ... */ },
                icon = {
                    Icon(
                        imageVector = Icons.Default.Build,
                        contentDescription = "build",
                    )
                },
            ) {
                Text(
                    text = "Build",
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis,
                )
            }
        }
    }
}
```

This example also demonstrates `ScreenScaffold` and `AppScaffold`.
These coordinate between the App and individual screens
([navigation routes](https://developer.android.com/training/wearables/compose/navigation)) to ensure the correct scrolling behavior and
`TimeText` positioning.

For the top and bottom padding, also note the following:

- The specification of the first and last `ItemType`, to determine the correct padding.
- The use of `ListHeader` for the first item in the list, because `Text` headers shouldn't have padding.

Full specifications can be found in the [Figma design kits](https://developer.android.com/design/ui/wear/guides/foundations/download). For more
details and examples, see:

- The [Horologist library](https://github.com/google/horologist) - provides helpers to help build optimized and differentiated apps for Wear OS.
- The [ComposeStarter sample](https://github.com/android/wear-os-samples/tree/main/ComposeStarter) - an example showing the principles outlined in this guide.
- The [JetCaster sample](https://github.com/android/compose-samples/tree/main/Jetcaster) - a more complex example of building an app to work with different screen sizes, using the Horologist library.

## Use scrolling layouts in your app

Use a scrolling layout, as shown earlier on this page, as the default choice
when implementing your screens. This lets users reach your app's components
regardless of display preferences or Wear OS device screen size.
![The effect of different device size and font-scaling](https://developer.android.com/static/images/wear/screenshot-test.png)

*The effect of different device sizes
and font-scaling.*

### Dialogs

Dialogs should also be scrollable, unless there is a very good reason not to.

The [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AlertDialog(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.PaddingValues,androidx.compose.ui.window.DialogProperties,kotlin.Function1)) component is responsive and is scrollable by default
if the content exceeds the viewport height.


### Custom screens might require non-scrolling layouts

Some screens may still be suited to non-scrolling layouts. Several examples
include the main player screen in a media app and the workout screen in a
fitness app.

In these cases, look at the canonical guidance provided in the
[Figma design kits](https://developer.android.com/design/ui/wear/guides/foundations/download), and implement a design that is responsive to the size
of the screen, using the correct margins.

## Provide differentiated experiences through breakpoints

With larger displays, you can introduce additional content and features. To
implement this sort of differentiated experience, use *screen size breakpoints*,
showing a different layout when the screen size exceeds 225 dp:

```kotlin
const val LARGE_DISPLAY_BREAKPOINT = 225

@Composable
fun isLargeDisplay() =
    LocalConfiguration.current.screenWidthDp >= LARGE_DISPLAY_BREAKPOINT

// ...
// ... use in your Composables:
    if (isLargeDisplay()) {
        // Show additional content.
    } else {
        // Show content only for smaller displays.
    }
    // ...https://github.com/android/snippets/blob/bbf4e1ff2570641546d50270b121493ef1965774/wear/src/main/java/com/example/wear/snippets/m3/list/List.kt#L140-L158
```

The [design guidance](https://developer.android.com/design/ui/wear/guides/foundations/larger-screens-differentiated) illustrates more of these opportunities.

## Test combinations of screen and font sizes using previews

[Compose previews](https://developer.android.com/develop/ui/compose/tooling/previews) help you develop for a variety of Wear OS screen sizes.
Use both the devices and font-scaling preview definitions to see the following:

- How your screens look at the extremes of sizing, for example, largest font paired with smallest screen.
- How your differentiated experience behaves across breakpoints.

Ensure you implement previews using [`WearPreviewDevices`](https://developer.android.com/reference/kotlin/androidx/wear/compose/ui/tooling/preview/WearPreviewDevices) and
[`WearPreviewFontScales`](https://developer.android.com/reference/kotlin/androidx/wear/compose/ui/tooling/preview/WearPreviewFontScales) for all the screens in your app.

```kotlin
@WearPreviewDevices
@WearPreviewFontScales
@Composable
fun ComposeListPreview() {
    ComposeList()
}
```

## Screenshot testing

Beyond preview testing, screenshot testing lets you test against a range of
existing hardware sizes. This is particularly useful where those devices might
not be immediately available to you, and the issue may not present itself on
other screen sizes.

Screenshot testing also helps you identify regressions at specific locations in
your codebase.

Our samples use [Roborazzi](https://github.com/takahirom/roborazzi) for screenshot testing:

1. Configure your [project](https://github.com/android/wear-os-samples/blob/main/ComposeStarter/build.gradle.kts) and [app](https://github.com/android/wear-os-samples/blob/main/ComposeStarter/app/build.gradle.kts) `build.gradle` files to use Roborazzi.
2. Create a screenshot test for each screen you have in your app. For example, the following code shows a screenshot test for a screen containing a list:

```kotlin
@RunWith(ParameterizedRobolectricTestRunner::class)
class ComposeListScreenTest(
    override val device: WearDevice
) : WearScreenshotTest() {
    override val tolerance = 0.02f

    @Test
    fun myScreenTest() =
        runTest {
            AppScaffold {
                ComposeList()
            }
        }

    companion object {
        @JvmStatic
        @ParameterizedRobolectricTestRunner.Parameters
        fun devices() = WearDevice.entries
    }
}
```

Some important points to note:

- `WearDevice.entries` contains definitions for most popular Wear OS devices so that the tests are run on a representative range of screen sizes.

### Generate golden images

To generate images for your screens, run the following command in a terminal:

    ./gradlew recordRoborazziDebug

### Verify images

To verify changes against existing images, run the following command in a
terminal:

    ./gradlew verifyRoborazziDebug

For a full example of screenshot testing, see the [ComposeStarter](https://github.com/android/wear-os-samples/tree/main/ComposeStarter) sample.