---
title: https://developer.android.com/training/wearables/wff/effects
url: https://developer.android.com/training/wearables/wff/effects
source: md.txt
---

The `Group` and `Part*` elements also provide `tintColor, renderMode` and
`blendMode` attributes which are powerful ways of adjusting the appearance of
sections of your watch face.

## Use clipping masks with a render mode

`renderMode` was introduced in version 1 of WFF to achieve a clipping mask.

The `renderMode` can be applied to `Group` and `Part*` elements in the scene
hierarchy. The watch face renderer draws the elements in order while traversing
the scene tree.

When `renderMode` is applied to a node, the effect only applies within the
parent `Group` of that node. Other nodes elsewhere in the graph are unaffected.

When no `renderMode` is specified, the default is `SOURCE`, which means that the
element is drawn directly to the screen. However, when one or more
elements are present in the parent node with `MASK` (or `ALL`) specified, then a
different approach is used:

1. An off-screen canvas is created
2. All child elements with `SOURCE` set (which is the default) are drawn
   1. All child elements that are part of the mask (`MASK, ALL`) are applied to the canvas to clip the resulting image.

Note that this means that the order of the elements in the parent node are not
taken into account.

In the following example, the `Scene` parent contains three children:

- The **first and third** elements are `MASK` elements, so they're combined together to form a masking layer
- The **second** element is the only non-masking layer

<br />

```xml
<PartDraw x="175" y="50" width="100" height="100" renderMode="MASK">
    <Ellipse x="0" y="0" width="100" height="100">
        <Fill color="#FFFFFF" />
    </Ellipse>
</PartDraw>

<PartDraw x="0" y="0" width="450" height="450">
    <Rectangle x="0" y="0" width="450" height="450">
        <Fill color="#ff0000">
            <LinearGradient startX="0" startY="0" endX="450" endY="450"
                colors="#FFFF00 #00FFFF #FF00FF" positions="0.25 0.5 0.75" />
        </Fill>
    </Rectangle>
</PartDraw>

<PartText x="75" y="250" width="300" height="80" renderMode="MASK">
    <Text align="CENTER">
        <Font family="pacifico" size="72" weight="BOLD" color="#FFFFFF">Hello!</Font>
    </Text>
</PartText>
```

<br />

The third option for `renderMode` in addition to `SOURCE` and `MASK` is `ALL`.
`ALL` specifies that the element should be treated both as a `SOURCE` and as a
`MASK` which can be useful in some scenarios.

## Use blend mode

**Note**: This capability is available on version 3 and higher of Watch Face
Format.

From version 3, Watch Face Format offers the ability to apply a [*blend
mode*](https://en.wikipedia.org/wiki/Blend_modes) when composing `Part*` elements.

Unlike `renderMode`, which introduces a special mechanism for constructing the
source and mask respectively, `blendMode` provides general access to all
[Android Graphics blend mode effects](https://developer.android.com/reference/android/graphics/BlendMode), and applies effects in the order that
elements appear in the scene graph.

In normal operation, when a two `Part*` elements are placed in the scene, the
top-most obscures or partially obscures the lower element because the default
`blendMode` is `SRC_OVER`.

<br />

```xml
<PartDraw x="125" y="115" width="150" height="150">
    <Rectangle x="0" y="0" width="150" height="150">
        <Fill color="#ffd3ba" />
    </Rectangle>
</PartDraw>
<PartText x="135" y="160" width="300" height="120">
    <Text align="START">
        <Font family="pacifico" size="96" weight="BOLD" color="#fb5607">Hello!</Font>
    </Text>
</PartText>
```

<br />

As a demonstration of using blend modes, choosing [`SRC_ATOP`](https://developer.android.com/reference/android/graphics/BlendMode#SRC_ATOP), discards
*the source pixels that do not cover destination pixels* . Namely, the
`PartText` is the source, and the destination is the `PartDraw`.

So as a result, text is only drawn over the rectangle, and not elsewhere on the
watch face:

<br />

```xml
<PartDraw x="125" y="115" width="150" height="150">
    <Rectangle x="0" y="0" width="150" height="150">
        <Fill color="#ffd3ba" />
    </Rectangle>
</PartDraw>
<PartText x="135" y="160" width="300" height="120" blendMode="SRC_ATOP">
    <Text align="START">
        <Font family="pacifico" size="96" weight="BOLD" color="#fb5607">Hello!</Font>
    </Text>
</PartText>
```

<br />

More complex effects can be applied, such as using [`COLOR_DODGE`](https://developer.android.com/reference/android/graphics/BlendMode#COLOR_DODGE) instead of
`SRC_ATOP`, which *makes destination brighter to reflect source*.

An example of combining multiple `Part*` elements using [`HUE`](https://developer.android.com/reference/android/graphics/BlendMode#HUE) and
[`COLOR_BURN`](https://developer.android.com/reference/android/graphics/BlendMode#COLOR_BURN) blend modes:

<br />

```xml
<Group name="container" x="75" y="100" width="300" height="300">
    <PartDraw x="25" y="15" width="150" height="150">
        <Rectangle x="0" y="0" width="150" height="150">
            <Fill color="#ffd3ba" />
        </Rectangle>
    </PartDraw>
    <PartDraw x="100" y="15" width="150" height="150" blendMode="HUE">
        <Ellipse x="0" y="0" width="150" height="150">
            <Fill color="#219ebc" />
        </Ellipse>
    </PartDraw>
    <PartText x="35" y="60" width="300" height="120" blendMode="COLOR_BURN">
        <Text align="START">
            <Font family="pacifico" size="96" weight="BOLD" color="#fb5607">Hello!</Font>
        </Text>
    </PartText>
</Group>
```

<br />

## Considerations

The following sections describe some considerations to keep in mind when using
clipping and blend effects.

### Blend mode is applied before render mode

If a node contains both `Part` elements using `blendMode` and `Part` elements
using `renderMode` set to `MASK` (or `ALL`), then the following approach is
taken.

1. The source is composited, including the application of `blendMode` modes
2. The mask is then applied from those elements specifying `rendermode="MASK`"

For example, considering the previous example used before, and adding in a
rectangle mask, noting that the order of the masked element doesn't matter:

<br />

```xml
<Group name="container" x="75" y="100" width="300" height="300">
    <PartDraw x="25" y="15" width="150" height="150">
        <Rectangle x="0" y="0" width="150" height="150">
            <Fill color="#ffd3ba" />
        </Rectangle>
    </PartDraw>
    <PartDraw x="100" y="15" width="150" height="150" blendMode="HUE">
        <Ellipse x="0" y="0" width="150" height="150">
            <Fill color="#219ebc" />
        </Ellipse>
    </PartDraw>
    <PartDraw x="100" y="15" width="150" height="150" renderMode="MASK">
        <Rectangle x="0" y="0" width="150" height="150">
            <Fill color="#ffffff" />
        </Rectangle>
    </PartDraw>
    <PartText x="35" y="60" width="300" height="120" blendMode="COLOR_BURN">
        <Text align="START">
            <Font family="pacifico" size="96" weight="BOLD" color="#fb5607">Hello!</Font>
        </Text>
    </PartText>
</Group>
```

<br />

### Performance

Using either `renderMode` and `blendMode` requires additional computation and
drawing steps. Depending on the device on which the watch face is running, some
of this may be executed efficiently in supported hardware, though this may not
be possible on older devices.

For this reason, use `renderMode` and `blendMode` judiciously and be mindful of
the impact that their use may have on the overall performance of the watch face.

## Use tints

A `tintColor` can be applied to the whole `Part*` element, `Group`, or
individual hands such as `HourHand` and `MinuteHand`, for example:

<br />

```xml
<Group x="75" y="100" width="350" height="350" name="group1" tintColor="#ffd3ba">
    <PartDraw x="25" y="0" width="100" height="100">
        <Rectangle x="0" y="0" width="100" height="100">
            <Fill color="#ffffff" />
        </Rectangle>
    </PartDraw>
    <PartDraw x="150" y="0" width="100" height="100">
        <Ellipse x="25" y="0" width="100" height="100">
            <Fill color="#ffffff" />
        </Ellipse>
    </PartDraw>
    <PartText x="0" y="150" width="300" height="80">
        <Text align="CENTER">
            <Font family="pacifico" size="72" weight="BOLD" color="#ffffff">Hello!</Font>
        </Text>
    </PartText>
</Group>
```

<br />

This can be useful for styling an entire section of the watch face, including
applying the style from the user settings, for example:
`tintcolor="[CONFIGURATION.myThemeColor.0]"`.