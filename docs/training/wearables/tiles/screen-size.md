---
title: https://developer.android.com/training/wearables/tiles/screen-size
url: https://developer.android.com/training/wearables/tiles/screen-size
source: md.txt
---

Your app's tiles should work well on Wear OS devices of all sizes, taking
advantage of additional space where available, and still look great on smaller
screens too. This guide provides recommendations for achieving this user
experience.

To learn more about the design principles for adaptive layouts, read the
[design guidance](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design).

## Provide differentiated experiences through breakpoints

Layouts from the [ProtoLayout Material](https://developer.android.com/reference/androidx/wear/protolayout/material/layouts/package-summary) library are responsive and take care
of correct element placement and visibility. However, in some cases you might
want to vary the number of visible elements for best results. For example, you
might want 3 buttons on a smaller display, and 5 on a larger display.

To implement this sort of differentiated experience, use *screen size
breakpoints*. To show a different layout when the screen size exceeds 225 dp:

```kotlin
materialScope(this, requestParams.deviceConfiguration) {
    // ...
    val isLargeScreen = deviceConfiguration.screenWidthDp >= 225
    primaryLayout(
        mainSlot = {
            buttonGroup {
                buttonGroupItem { button1 }
                buttonGroupItem { button2 }
                buttonGroupItem { button3 }
                if (isLargeScreen) {
                    buttonGroupItem { button4 }
                    buttonGroupItem { button5 }
                }
            }
        }
    )
}
```

The [design guidance](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design) illustrates additional opportunities.

## Test tiles on different screen sizes using Previews

It is important to test your layouts on different screen sizes. Use the
Tile Preview annotations, along with the [`TilePreviewHelper`](https://developer.android.com/reference/androidx/wear/tiles/tooling/preview/TilePreviewHelper) and
[`TilePreviewData`](https://developer.android.com/reference/androidx/wear/tiles/tooling/preview/TilePreviewData) classes:

```kotlin
@Preview(device = WearDevices.LARGE_ROUND)
fun smallPreview(context: Context) = TilePreviewData {
    TilePreviewHelper.singleTimelineEntryTileBuilder(
        materialScope(context, it.deviceConfiguration) {
            myAdaptiveLayout() // varies the layout depending on the size of the screen
        }
    )
        .build()
}
```

This lets you preview your Tile layouts directly within Android Studio.

For a full example, see the [timer tiles sample](https://github.com/android/wear-os-samples/blob/main/WearTilesKotlin/app/src/debug/java/com/example/wear/tiles/golden/Timer.kt) on GitHub.