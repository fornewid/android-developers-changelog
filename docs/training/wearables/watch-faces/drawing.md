---
title: https://developer.android.com/training/wearables/watch-faces/drawing
url: https://developer.android.com/training/wearables/watch-faces/drawing
source: md.txt
---

After you configure your project and add a class that implements the
watch face service, you can start writing code to initialize and draw your
custom watch face.

Every watch face creates a custom subclass of a renderer that implements
everything needed to draw the watch face.

The renderer combines the
[`UserStyle`](https://developer.android.com/reference/androidx/wear/watchface/style/UserStyle), the
complication information from
[`ComplicationSlotsManager`](https://developer.android.com/reference/androidx/wear/watchface/ComplicationSlotsManager),
the current time, and other state information to
render the watch face, as shown in the following example:

    class CustomCanvasRenderer(
        private val context: Context,
        surfaceHolder: SurfaceHolder,
        watchState: WatchState,
        private val complicationSlotsManager: ComplicationSlotsManager,
        currentUserStyleRepository: CurrentUserStyleRepository,
        canvasType: Int
    ) : Renderer.CanvasRenderer(
        surfaceHolder = surfaceHolder,
        currentUserStyleRepository = currentUserStyleRepository,
        watchState = watchState,
        canvasType = canvasType,
        interactiveDrawModeUpdateDelayMillis = 16L
    ) {
        override fun render(canvas: Canvas, bounds: Rect, zonedDateTime: ZonedDateTime) {
            // Draw into the canvas
        }

        override fun renderHighlightLayer(canvas: Canvas, bounds: Rect, zonedDateTime: ZonedDateTime) {
            // Draw into the canvas
        }
    }