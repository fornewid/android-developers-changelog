---
title: https://developer.android.com/training/wearables/wff/complications
url: https://developer.android.com/training/wearables/wff/complications
source: md.txt
---

[Complications](https://developer.android.com/design/ui/wear/guides/surfaces/complications) are a feature of both physical and smartwatch watch faces
that show additional information. Typically the user selects what information is
shown in a complication.

Typically complications come in a number of shapes:

1. Rectangular
2. Circular
3. Arcs, along the edge of the watch face
4. Background, covering the whole of the watch face

In Wear OS, the Complication system can be broken down into two parts:

1. The Complication [**data source**](https://developer.android.com/training/wearables/complications#data-source)
2. The Complication **rendering**

For example, a health and fitness app might implement a Daily Steps complication
data source. This could be rendered by the WFF watch face.

## Data sources in complications

Complication data sources specify only the data to be rendered, and the type of
complication. The data source plays no part in determining how the data should
be represented on the watch face.

For example, the health and fitness Daily Steps complication data source may
produce the following data to indicate the user has taken 2400 of their target
10000 steps today:

- Type: [`GOAL_PROGRESS`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/GoalProgressComplicationData.Builder)
- Value: `2400`
- TargetValue: `10000`

Note that there is nothing in this data that indicates how this should be
rendered.

The watch face specifies what types of complication it is capable of rendering.
This determines which data sources are then available for the user to select
from.

In the case of the Daily Steps example, you decide in your watch face
definition how to render the `Value` and `TargetValue`: would it be as text, or as
a progress indicator? That is for you as the watch face designer to decide.

## Define complications

Offering the ability to show complications on your watch face can be valuable to
users, as it allows them to have a greater range of information at a glance and
customized to their needs.

Decide if and how many complications to support on your watch face,
what their shapes and positioning will be, and what types of data they
support.

Each space on the watch face for a complication is defined as a
`ComplicationSlot` within which a bounding area is defined for the rendering of
the complication:

<br />

```xml
<ComplicationSlot slotId="1" supportedTypes="SHORT_TEXT SMALL_IMAGE EMPTY"
    x="100" y="100" width="100" height="100">
    <BoundingOval x="0"  y="0" width="100" height="100" />
    <Complication type="SHORT_TEXT">
        <!-- Complication content for rendering SHORT_TEXT data goes here -->
    </Complication>
    <Complication type="SMALL_IMAGE">
        <!-- Complication content for rendering SMALL_IMAGE data goes here -->
    </Complication>
</ComplicationSlot>
```

<br />

A similar approach can be applied to the other bounding shapes such as rectangle
and ellipse.

## Set the complication type and defaults

The complication system provides a number of different types, which
allows the watch face to express what type of data it can represent on the
screen. For example, an Arc complication, as shown previously, isn't a great fit
for an image-based complication data type such as `SMALL_IMAGE`, but could work
very well for numeric data such as `RANGED_VALUE`.

In your `ComplicationSlot` declaration, set `supportedTypes` to the
space-separated list of the types that can be rendered in this slot.

You must also set the default source for the `ComplicationSlot` unless you
allow the `EMPTY` type, in which case setting a default is optional:

<br />

```xml
<ComplicationSlot slotId="2" supportedTypes="SHORT_TEXT SMALL_IMAGE EMPTY"
    x="250" y="100" width="100" height="100">
    <DefaultProviderPolicy
        defaultSystemProvider="STEP_COUNT"
        defaultSystemProviderType="SHORT_TEXT" />
    <!-- ... -->
</ComplicationSlot>
```

<br />

In addition to having to specify system providers, [you can optionally specify
non-system providers](https://developer.android.com/training/wearables/wff/complication/default-provider-policy?version=2#bounding-arc-optional-attributes), such as third-party providers to use by default, if
they are already installed.

## Render complication data

Having defined the `ComplicationSlot`, bounds, and containing `Complication`
element, use standard WFF components, such as `PartDraw, PartImage` and
`PartText` to display the Complication data.

Elements within the `Complication` data have access to a special data source:
`COMPLICATION`, which provides the various data properties set by the
complication data source.

For example, a `SMALL_IMAGE` complication can set the `COMPLICATION.SMALL_IMAGE`
and `COMPLICATION.SMALL_IMAGE_AMBIENT` values. These can be used instead of
resource in an `Image` element:

<br />

```xml
<Complication type="SMALL_IMAGE">
    <PartImage x="0" y="0" width="100" height="100">
        <Image resource="[COMPLICATION.SMALL_IMAGE]" />
    </PartImage>
</Complication>
```

<br />

Each different complication type has a different set of available properties
that can be set; for a full list of each, see the [`Complication`](https://developer.android.com/training/wearables/wff/complication/complication) reference.
This example displays the text from a `SHORT_TEXT` complication:

<br />

```xml
<Complication type="SHORT_TEXT">
    <PartText x="0" y="0" width="100" height="100">
        <Text>
            <Font size="32">
                <Template>
                    <![CDATA[%s]]><Parameter expression="[COMPLICATION.TEXT]" />
                </Template>
            </Font>
        </Text>
    </PartText>
</Complication>
```

<br />

### Maximize usefulness when rendering complications

There are a number of challenges when adding `ComplicationSlots` to your watch
face:

1. There are numerous Complication data types. Different apps may provide one or many of these.
2. Each Complication data type, as well as having mandatory properties also has many optional properties. Check that the most useful rendering is made from the available properties, taking into account the different combinations.

To address these issues, some strategies include:

1. Support multiple complication types for each slot. For example, `SHORT_TEXT` is quite widely supported by complication data sources, so supporting a number of different types, such as `SHORT_TEXT RANGED_VALUE` for a small circular complication, increases compatibility.
2. Offer different complication types across the watch face. For example, you could support `RANGED_VALUE` and `GOAL_PROGRESS` on edge-positioned Arc complications, and `SHORT_TEXT` and `SMALL_IMAGE` on circular complications in the body of the watch face.
3. Check for optional elements for each data type. For example, `SHORT_TEXT` optionally supports a title property and an image. Your layout for rendering the available data might differ depending on whether an image or title is available or not.