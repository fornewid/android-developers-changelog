---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/surfaces
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/surfaces
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In Jetpack Compose Glimmer, the [`surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/surface.composable) component is a fundamental
building block that represents a distinct visual area or a physical boundary for
components such as buttons and cards.

A surface is responsible for the following visual and physical properties:

- **Clipping**: Clips its children to a specified shape.
- **Border**: Draws an inner border to emphasize the component boundary. When focused, it draws a wider border with a focused highlight.
- **Background**: Applies a background color to the surface area.
- **Depth effects** : Renders `DepthEffect` shadows based on the component's state (such as default versus focused).
- **Content Color**: Provides a color for text and icons inside the surface, calculated by default from the background color.
- **Interaction States**: Draws a pressed overlay when the surface is pressed and a wider border with a highlight when focused.

## Example: Create a surface

The following code creates a surface with clipping, a background, and default
borders:

    @Composable
    fun SurfaceSample() {
        Box(Modifier.surface().padding(horizontal = 24.dp, vertical = 20.dp)) {
            Text("This is a surface")
        }
    }

> [!NOTE]
> **Note:** This example provides a non-focusable element. Use a surface like this only when you don't want the element to be interactable.

## Interaction and focus

Surfaces aren't focusable by default, so users can't interact with them. In most
cases, surfaces should be interactive to let users consistently move focus and
navigate between components. You can use the Compose [`focusable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/focusable.modifier) modifier
for surfaces that are only intended to be focusable. Similarly, you can create a
clickable surface using the Compose [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/clickable.modifier) modifier. You can also use
other modifiers for surfaces that require actions.

The following code shows examples of both focusable and clickable surfaces:


```kotlin
@Composable
fun FocusableSurfaceSample() {
    val interactionSource = remember { MutableInteractionSource() }
    Box(
        modifier = Modifier
            .size(100.dp)
            .surface(interactionSource = interactionSource)
            .focusable(interactionSource = interactionSource),
        contentAlignment = Alignment.Center
    ) {
        Text("Focusable")
    }
}

@Composable
fun ClickableSurfaceSample() {
    val interactionSource = remember { MutableInteractionSource() }
    Box(
        modifier = Modifier
            .size(100.dp)
            .surface(interactionSource = interactionSource)
            .focusable(interactionSource = interactionSource)
            .clickable(
                interactionSource = interactionSource,
                indication = null
            ) { /* Handle click action */ },
        contentAlignment = Alignment.Center
    ) {
        Text("Clickable")
    }
}
```

<br />

### Key points about the code

- **Shared interaction source for focusable surfaces** : Both `.surface()` and
  `.focusable()` must share the same `interactionSource`. This lets the
  surface react to focus changes.

- **Shared interaction source for clickable surfaces** : Both `.surface()` and
  `.clickable()` must share the same `interactionSource`. This ensures that
  visual states (like press or focus) are synchronized, letting surface react
  visually to user input.

- **Modifier ordering** : The sequence of modifiers is critical. Because
  `.surface()` clips a layout, placing it *before* `.clickable()` ensures the
  touch target is constrained to the surface's shape. If `.clickable()` comes
  first, the interaction area might extend beyond the visible, clipped
  boundaries of the component.

### SurfaceDepthEffect

The [`SurfaceDepthEffect`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/SurfaceDepthEffect) class manages the transition of shadows between
interaction states:

- `depthEffect`: The shadow effect used when the surface is in its default state.
- `focusedDepthEffect`: The shadow effect used when the surface is focused.