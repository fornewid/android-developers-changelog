---
title: https://developer.android.com/training/wearables/tiles/dynamic
url: https://developer.android.com/training/wearables/tiles/dynamic
source: md.txt
---

Starting in Tiles 1.2, you can stream platform data updates using [dynamic
expressions](https://developer.android.com/training/wearables/data/dynamic). You can then associate these updates with animations in your
tiles. Your app gets updates to this value every second.

Using dynamic expressions, you don't need to refresh the entire tile when its
content changes. To create a more engaging experience in your tiles, animate
those dynamic objects.

## Associate dynamic expressions with data sources

The `androidx.wear.protolayout` and `androidx.wear.protolayout.material`
namespaces contain many classes whose fields accept dynamic expressions. Several
examples include the following:

- Several length values, including the [length of an `Arc` object](https://developer.android.com/reference/androidx/wear/protolayout/LayoutElementBuilders.ArcLine#getLength()) and the [length of a `CircularProgressIndicator`](https://developer.android.com/reference/androidx/wear/protolayout/material/CircularProgressIndicator#getProgress()) object.
- Any color, such as the [content color of a `Button` object](https://developer.android.com/reference/androidx/wear/protolayout/material/ButtonColors#getContentColor()).
- Many string values, including the [content of a `Text` object](https://developer.android.com/reference/androidx/wear/protolayout/material/Text#getText()), the [content of a `LayoutElementsBuilders.Text` object](https://developer.android.com/reference/androidx/wear/protolayout/LayoutElementBuilders.Text#getText()), and the [content
  description of a `CircularProgressIndicator` object](https://developer.android.com/reference/androidx/wear/protolayout/material/CircularProgressIndicator#getContentDescription()).

To use a dynamic expression as a possible value for an element in your tile, use
the element's corresponding `*Prop` dynamic property type and pass in the data
source to the dynamic property type's builder class's `setDynamicValue()`
method.

Tiles support these dynamic property types:

- For linear dimensions, measured in display-independent pixels, use [`DimensionBuilders.DpProp`](https://developer.android.com/reference/androidx/wear/tiles/DimensionBuilders.DpProp).
- For angular dimensions, measured in degrees, use [`DimensionBuilders.DegreesProp`](https://developer.android.com/reference/androidx/wear/tiles/DimensionBuilders.DegreesProp).
- For string values, use [`TypeBuilders.StringProp`](https://developer.android.com/reference/androidx/wear/protolayout/TypeBuilders.StringProp).
- For color values, use [`ColorBuilders.ColorProp`](https://developer.android.com/reference/androidx/wear/protolayout/ColorBuilders.ColorProp).
- For floating-point values, use [`TypeBuilders.FloatProp`](https://developer.android.com/reference/androidx/wear/protolayout/TypeBuilders.FloatProp).

When you use a dynamic expression that affects physical dimensions---any value in
a tile except for color---you must also specify a set of related constraints, such
as a string format. These constraints allow the system renderer to determine the
maximum amount of space that a value could occupy within your tile. Usually, you
specify these constraints at the element level, not at the dynamic expression
level, by calling a method that starts with `setLayoutConstraintsForDynamic*`.

> [!NOTE]
> **Note:** The Material components set these layout constraints automatically.

The following code snippet shows how to display updates to a heart rate using 3
digits, with a fallback value of `--`:

<br />

```kotlin
override fun onTileRequest(requestParams: RequestBuilders.TileRequest) =
    Futures.immediateFuture(
        Tile.Builder()
            .setResourcesVersion(RESOURCES_VERSION)
            .setFreshnessIntervalMillis(60 * 60 * 1000) // 60 minutes
            .setTileTimeline(
                Timeline.fromLayoutElement(
                    Text.Builder(
                        this,
                        TypeBuilders.StringProp.Builder("--")
                            .setDynamicValue(
                                PlatformHealthSources.heartRateBpm()
                                    .format()
                                    .concat(DynamicBuilders.DynamicString.constant(" bpm"))
                            )
                            .build(),
                        TypeBuilders.StringLayoutConstraint.Builder("000").build(),
                    )
                        .build()
                )
            )
            .build()
    )
```

<br />

## Use a small number of expressions within a single tile

Wear OS [places a limit](https://developer.android.com/training/wearables/data/dynamic#use-limited-number-per-screen) on the number of expressions that a single tile can
have. If a tile contains too many total dynamic expressions, dynamic values are
ignored, and the system falls back to the static values that you provide to the
respective dynamic property types.

## Consolidate dynamic data into a state object

You can consolidate the latest set of updates from data sources into a *state*,
which you pass over to your tile for value rendering.

To use state information in your tiles, complete these steps:

1. Establish a set of keys that represent the different values of your tile's
   state. This example creates keys for water intake and a qqq note:

   <br />

   ```kotlin
   companion object {
       val KEY_WATER_INTAKE = intAppDataKey("key_water_intake")
       val KEY_NOTE = stringAppDataKey("key_note")
   }
   ```

   <br />

2. In your implementation of `onTileRequest()`, call `setState()` and establish
   initial mappings from each key to a particular dynamic data value:

   <br />

   ```kotlin
   override fun onTileRequest(
       requestParams: RequestBuilders.TileRequest
   ): ListenableFuture<Tile?> {
       // If the tile hasn't had any state set yet, use the default values
       val state =
           if (requestParams.currentState.keyToValueMapping.isNotEmpty())
               requestParams.currentState
           else
               StateBuilders.State.Builder()
                   .setStateMap(
                       dynamicDataMapOf(
                           KEY_WATER_INTAKE mapTo 200,
                           KEY_NOTE mapTo "Good"
                       )
                   )
                   .build()

       return Futures.immediateFuture(
           Tile.Builder()
               // Set resources, timeline, and other tile properties.
               .setState(state)
               .build()
       )
   }
   ```

   <br />

3. When you create your layout, in a place where you want to show this data
   from state, use a `Dynamic*` type object. You can also call `animate()` to
   show an animation from the previous value to the current value:

   <br />

   ```kotlin
   val waterIntakeValue =
       DynamicBuilders.DynamicInt32.from(KEY_WATER_INTAKE)
   ```

   <br />

4. When needed, you can also update the state with new values. This can be part
   of a tile's [`LoadAction`](https://developer.android.com/reference/androidx/wear/protolayout/ActionBuilders.LoadAction).

   In this example, the water intake value is updated to `400`:

   <br />

   ```kotlin
   val loadAction =
       loadAction(
           dynamicDataMapOf(
               KEY_WATER_INTAKE mapTo 400,
               KEY_NOTE mapTo "Outstanding"
           )
       )
   ```

   <br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate to ProtoLayout namespaces](https://developer.android.com/training/wearables/tiles/migrate-to-protolayout)
- [Get started with tiles](https://developer.android.com/training/wearables/tiles/get_started)
- [Other considerations](https://developer.android.com/develop/ui/compose/migrate/other-considerations)