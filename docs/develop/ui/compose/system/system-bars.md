---
title: https://developer.android.com/develop/ui/compose/system/system-bars
url: https://developer.android.com/develop/ui/compose/system/system-bars
source: md.txt
---

Once your app targets SDK 35 or later, [edge-to-edge is enforced](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge). The
system status bar and gesture navigation bars are transparent, but the
three-button navigation bar is translucent. Call `enableEdgeToEdge` to make this
backwards compatible.

However, the system defaults might not work for all use cases. Consult the
[Android system bars design guidance](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars) and [edge-to-edge design
guidance](https://developer.android.com/design/ui/mobile/guides/layout-and-content/edge-to-edge) for an overview of when to consider having transparent or
translucent system bars.

## Create transparent system bars

Create a transparent gesture navigation bar by targeting Android 15 or later or
by calling `enableEdgeToEdge()` with default arguments for earlier versions. For
three-button navigation bar, set [`Window.setNavigationBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#setNavigationBarContrastEnforced(boolean))
to `false` otherwise there will be a translucent scrim applied.

## Create translucent system bars

To create a translucent status bar, create a custom composable that overlaps the
main content and draws a gradient in the area covered by insets.


```kotlin
class SystemBarProtectionSnippets : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // enableEdgeToEdge sets window.isNavigationBarContrastEnforced = true
        // which is used to add a translucent scrim to three-button navigation
        enableEdgeToEdge()

        setContent {
            MyTheme {
                // Main content
                MyContent()

                // After drawing main content, draw status bar protection
                StatusBarProtection()
            }
        }
    }
}

@Composable
private fun StatusBarProtection(
    color: Color = MaterialTheme.colorScheme.surfaceContainer,
) {
    Spacer(
        modifier = Modifier
            .fillMaxWidth()
            .height(
                with(LocalDensity.current) {
                    (WindowInsets.statusBars.getTop(this) * 1.2f).toDp()
                }
            )
            .background(
                brush = Brush.verticalGradient(
                    colors = listOf(
                        color.copy(alpha = 1f),
                        color.copy(alpha = 0.8f),
                        Color.Transparent
                    )
                )
            )
    )
}
```

<br />

**Figure 1.** A translucent status bar.

For adaptive apps, insert a custom composable that matches the colors of each
pane, as seen in the [Edge-to--edge design](https://developer.android.com/design/ui/mobile/guides/layout-and-content/edge-to-edge). To create a translucent
navigation bar, set [`Window.setNavigationBarContrastEnforced`](https://developer.android.com/reference/android/view/Window#setNavigationBarContrastEnforced(boolean)) to true.