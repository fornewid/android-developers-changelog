---
title: https://developer.android.com/develop/ui/compose/components/divider
url: https://developer.android.com/develop/ui/compose/components/divider
source: md.txt
---

[Dividers](https://m3.material.io/components/divider/overview) are thin lines that separate items in lists or other
containers. You can implement dividers in your app using the `HorizontalDivider`
and `VerticalDivider` composables.

- [`HorizontalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalDivider(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color)): Separate items in a column.
- [`VerticalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#VerticalDivider(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color)): Separate items in a row.

## API surface

Both components provide parameters for modifying their appearance:

- `thickness`: Use this parameter to specify the thickness of the divider line.
- `color`: Use this parameter to specify the color of the divider line.

> [!NOTE]
> **Note:** You can use the `modifier` parameter to control padding.

## Horizontal divider example

The following example demonstrates an implementation of the
`HorizontalDivider` component. It uses the `thickness` parameter to control the
height of the line:


```kotlin
@Composable
fun HorizontalDividerExample() {
    Column(
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        Text("First item in list")
        HorizontalDivider(thickness = 2.dp)
        Text("Second item in list")
    }
}
```

<br />

This implementation renders a thin horizontal line between two text components:
![An Android app screen displaying two text items, 'First item in list' and 'Second item in list,' separated by a thin horizontal line.](https://developer.android.com/static/develop/ui/compose/images/components/divider-horizontal.png) **Figure 1.** A horizontal divider separating two text components.

## Vertical divider example

The following example demonstrates an implementation of the
`VerticalDivider` component. It uses the `color` parameter to provide a custom
color for the line:


```kotlin
@Composable
fun VerticalDividerExample() {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .height(IntrinsicSize.Min),
        horizontalArrangement = Arrangement.SpaceEvenly
    ) {
        Text("First item in row")
        VerticalDivider(color = MaterialTheme.colorScheme.secondary)
        Text("Second item in row")
    }
}
```

<br />

This implementation renders a thin vertical line between two text components:
![An Android app screen displaying two text items, 'First item in row' and 'Second item in row,' separated by a thin vertical line.](https://developer.android.com/static/develop/ui/compose/images/components/divider-vertical.png) **Figure 2.** A vertical divider separating two text components.

## Additional resources

- [`HorizontalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalDivider(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color))
- [`VerticalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#VerticalDivider(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color))
- [Material Design - Dividers](https://m3.material.io/components/divider)