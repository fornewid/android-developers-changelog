---
title: https://developer.android.com/develop/ui/compose/accessibility/scalable-content
url: https://developer.android.com/develop/ui/compose/accessibility/scalable-content
source: md.txt
---

Implement **pinch-to-zoom** gestures to support scalable content in your app.
This is the standard, platform-consistent method for improving accessibility,
allowing users to intuitively adjust the size of text and UI elements to fit
their needs. Your app can define custom scaling behavior with granular control
and contextual behavior that offers an experience that users often discover more
quickly than a system-level feature like screen magnification.

## Choose a scaling strategy

The strategies covered in this guide cause the UI to reflow and reorganize to
fit the screen's width. This provides a significant accessibility benefit by
eliminating the need for horizontal panning and the frustrating "zig-zag" motion
that would otherwise be required to read long lines of text.

**Further Reading** : Research confirms that for users with low vision, reflowing
content is significantly more readable and easier to navigate than interfaces
that require two-dimensional panning. For more details, see [A Comparison of
Pan-and-Scan and Reflowable Content on Mobile Devices](https://link.springer.com/chapter/10.1007/978-3-319-20612-7_18).

### Scale either all elements or only text elements

The following table demonstrates the visual effect of each scaling strategy.

| Strategy | Density scaling | Font scaling |
|---|---|---|
| **Behavior** | Scales everything proportionally. The content reflows to fit its container, so the user doesn't need to pan horizontally to see all content. | Only affects text elements. The overall layout and non-text components stay the same size. |
| **What Scales** | **All visual elements**: Text, components (buttons, icons), images, and layout spacing (padding, margins) | **Text only** |
| **Demonstration** |   |   |

### Recommendations

Now that you've seen the visual differences, the following table helps you weigh
the trade-offs and choose the best strategy for your content.

|---|---|---|
| **UI type** | **Recommended strategy** | **Reasoning** |
| **Reading-intensive layouts** Examples: News articles, messaging apps | **Density or font scaling** | Density scaling is preferred to scale the entire content area, including inline images. Font scaling is a straightforward alternative if only text needs to be scaled. |
| **Visually structured layouts** Examples: App stores, social media feeds | **Density scaling** | Preserves the visual relationships between images and text in carousels or grids. The reflowing nature avoids horizontal panning, which would conflict with nested scrolling elements. |

## Detect scaling gestures in Jetpack Compose

To support user-scalable content, you must first detect multi-touch gestures. In
Jetpack Compose, you can do this using the [`Modifier.transformable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).transformable(androidx.compose.foundation.gestures.TransformableState,kotlin.Boolean,kotlin.Boolean)).

> [!IMPORTANT]
> **Important:** It's critical to understand that this modifier is **purely a
> gesture detector**; it doesn't apply scaling. You must use the data it provides to update your own state.

The `transformable` modifier is a high-level API that provides the `zoomChange`
delta since the last gesture event. This simplifies the state update logic to
direct accumulation (for example, `scale *= zoomChange`), making it ideal for
the adaptive scaling strategies covered in this guide.

## Example implementations

The following examples show how to implement the density scaling and font
scaling strategies.

> [!TIP]
> **Tip:** To further enhance the user experience and accommodate the user's preference, consider keeping the chosen scale factor. When the user returns to the screen or relaunches the app, their preferred scale is already applied. For a modern, Jetpack-recommended solution for storing preferences, see [Jetpack DataStore](https://developer.android.com/topic/libraries/architecture/datastore).

### Density scaling

This approach scales the base `density` of a UI area. As a result, all
layout-based measurements---including padding, spacing, and component sizes---are
scaled, as if the screen size or resolution had changed. Because text size
also relies on density, it also scales proportionally. This strategy is
effective when you want to uniformly enlarge all elements within a specific
area, maintaining the overall visual rhythm and proportions of your UI.


```kotlin
private class DensityScalingState(
    // Note: For accessibility, typical min/max values are ~0.75x and ~3.5x.
    private val minScale: Float = 0.75f,
    private val maxScale: Float = 3.5f,
    private val currentDensity: Density
) {
    val transformableState = TransformableState { zoomChange, _, _ ->
        scaleFactor.floatValue =
            (scaleFactor.floatValue * zoomChange).coerceIn(minScale, maxScale)
    }
    val scaleFactor = mutableFloatStateOf(1f)
    fun scaledDensity(): Density {
        return Density(
            currentDensity.density * scaleFactor.floatValue,
            currentDensity.fontScale
        )
    }
}
```

<br />

### Font scaling

This strategy is more targeted, modifying only the `fontScale` factor. The
result is that only text elements grow or shrink, while all other layout
components---such as containers, padding, and icons---remain a fixed size. This
strategy is well-suited for improving text legibility in reading-intensive
apps.

> [!NOTE]
> **Note:** This approach leverages Android's underlying font scaling system, which applies a **non-linear scale** for better readability. Therefore, a `zoomChange` of 2.0 might not result in text that appears exactly twice as large, but it creates scaling behavior that is consistent with the user's system-wide accessibility settings.


```kotlin
class FontScaleState(
    // Note: For accessibility, typical min/max values are ~0.75x and ~3.5x.
    private val minScale: Float = 0.75f,
    private val maxScale: Float = 3.5f,
    private val currentDensity: Density
) {
    val transformableState = TransformableState { zoomChange, _, _ ->
        scaleFactor.floatValue =
            (scaleFactor.floatValue * zoomChange).coerceIn(minScale, maxScale)
    }
    val scaleFactor = mutableFloatStateOf(1f)
    fun scaledFont(): Density {
        return Density(
            currentDensity.density,
            currentDensity.fontScale * scaleFactor.floatValue
        )
    }
}
```

<br />

### Shared demo UI

This is the shared `DemoCard` composable used by both of the preceding examples
to highlight the different scaling behaviors.


```kotlin
@Composable
private fun DemoCard() {
    Card(
        modifier = Modifier
            .width(360.dp)
            .padding(16.dp),
        shape = RoundedCornerShape(12.dp)
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Text("Demo Card", style = MaterialTheme.typography.headlineMedium)
            var isChecked by remember { mutableStateOf(true) }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("Demo Switch", Modifier.weight(1f), style = MaterialTheme.typography.bodyLarge)
                Switch(checked = isChecked, onCheckedChange = { isChecked = it })
            }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Icon(Icons.Filled.Person, "Icon", Modifier.size(32.dp))
                Spacer(Modifier.width(8.dp))
                Text("Demo Icon", style = MaterialTheme.typography.bodyLarge)
            }
            Row(
                Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Box(
                    Modifier
                        .width(100.dp)
                        .weight(1f)
                        .height(80.dp)
                        .background(Color.Blue)
                )
                Box(
                    Modifier
                        .width(100.dp)
                        .weight(1f)
                        .height(80.dp)
                        .background(Color.Red)
                )
            }
            Text(
                "Demo Text: Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                    " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                style = MaterialTheme.typography.bodyMedium,
                textAlign = TextAlign.Justify
            )
        }
    }
}
```

<br />

## Tips and considerations

To create a more polished and accessible experience, consider the following
recommendations:

- **Consider offering non-gesture scale controls**: Some users may have difficulty with gestures. To support these users, consider providing an alternative way to adjust or reset the scale that doesn't rely on gestures.
- **Build for all scales** : Test your UI against both in-app scaling and system-wide font or display settings. Check that your app's layouts adapt correctly without breaking, overlapping, or hiding content. Learn more about how to build [adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive).