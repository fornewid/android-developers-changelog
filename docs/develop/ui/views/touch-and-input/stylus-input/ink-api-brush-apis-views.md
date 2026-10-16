---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/ink-api-brush-apis-views
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/ink-api-brush-apis-views
source: md.txt
---

The[Ink`Brush`APIs](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush)provide a way to create and customize brushes for drawing on a canvas.

## Create a brush

To create a brush, use the[`Brush`](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush)factory methods with named arguments such as`Brush.createWithColorLong()`. This class lets you set the following properties:

- `family`: The style of the brush, analogous to a typeface or font in text. See[`StockBrushes`](https://developer.android.com/reference/kotlin/androidx/ink/brush/StockBrushes)for available[`BrushFamily`](https://developer.android.com/reference/kotlin/androidx/ink/brush/BrushFamily)values.
- `color`: The color of the brush. You can set the color using a[`ColorLong`](https://developer.android.com/reference/kotlin/androidx/annotation/ColorLong).
- `size`: The base thickness of strokes created with the brush.
- `epsilon`: The smallest distance at which two points in the stroke must be considered distinct, which controls the level of detail or fidelity of the stroke's geometry.
  - Higher values simplify the stroke more, which uses less memory and renders faster, but may result in visible artifacts like jagged edges when zoomed in.
  - Lower values preserve more detail for high-quality zooming, but increase memory usage.
  - For prototyping with a 1 px unit scale, 0.1 is a good starting point. For production apps supporting various screen densities, use density independent units (like dp) and adjust epsilon accordingly.

    val redBrush = Brush.createWithColorLong(
      family = StockBrushes.pressurePen(),
      colorLong = Color.RED.pack(),
      size = 5F,
      epsilon = 0.1F
    )

## Modify brush properties

You can create a copy of an existing brush using the[`copy()`](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush#copy(androidx.ink.brush.BrushFamily,kotlin.Float,kotlin.Float))method. This method lets you change any of the brush's properties.  

    val blueBrush = redBrush.copy(colorLong = Color.BLUE.pack())

## Custom brushes

While[`StockBrushes`](https://developer.android.com/reference/kotlin/androidx/ink/brush/StockBrushes)provides a versatile set of common brushes, Ink API also offers an advanced path for creating entirely new brush behaviors for unique artistic effects or to replicate specific existing brushes for backward compatibility.

A custom`BrushFamily`is loaded from its serialized format. The required format is the gzipped binary encoding of the[BrushFamily protocol buffer](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:ink/ink-storage/src/commonMain/proto/brush_family.proto;l=1?q=brush_family.pr&sq). This lets you load and use custom brush files today. Once deserialized, the custom`BrushFamily`can be used to create a new`Brush`with a specific color and size, just like any of the`StockBrushes`families.
**Note:** This interface is experimental and is subject to change.  

    class CustomBrushes(val context: Context) {

      private const val TAG = "CustomBrushes"

      val brushes by lazy { loadCustomBrushes(context) }

      @OptIn(ExperimentalInkCustomBrushApi::class)
      private fun loadCustomBrushes(): List<CustomBrush> {
        val brushFiles = mapOf(
            "Calligraphy" to (R.raw.calligraphy to R.drawable.draw_24px),
            "Flag Banner" to (R.raw.flag_banner to R.drawable.flag_24px),
            "Graffiti" to (R.raw.graffiti to R.drawable.format_paint_24px),
        // ...
        )

        val loadedBrushes = brushFiles.mapNotNull { (name, pair) ->
          val (resourceId, icon) = pair
          val brushFamily = context.resources.openRawResource(resourceId).use
          { inputStream ->
              BrushFamily.decode(inputStream)
          }
          CustomBrush(name, icon, brushFamily.copy(clientBrushFamilyId = name))     
        }
        return loadedBrushes
      }
    }

    data class CustomBrush(
      val name: String,
      val icon: Int,
      val brushFamily: BrushFamily
    )