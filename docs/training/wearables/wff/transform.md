---
title: Dynamically change element appearance  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/wff/transform
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Dynamically change element appearance Stay organized with collections Save and categorize content based on your preferences.



You may want to change the appearance of parts of the watch face, for example,
change the position, size, visibility, often in response to [input data
sources](/training/wearables/wff/common/attributes/source-type) such as the time of day or the accelerometer.

In Watch Face Format, this is achieved through use of the `Transform` element.
Not all elements can be transformed, but the main *transformable* elements
include: `Group` , `Part*` elements, and drawing primitives such as shapes and
styles.

Attributes of each element that are transformable are marked as such in the
reference documentation.

Specify the transform in the `value` attribute using the Watch Face Format
[expression](/training/wearables/wff/expressions) language, which can include data sources. The `target` attribute
specifies the attribute to change in the parent element.

For example, to change the angle of an `Arc` to reflect step progress:

```
<Arc centerX="225" centerY="225" height="420" width="420" startAngle="0" endAngle="0">
    <Transform target="endAngle" value="[STEP_PERCENT] * 3.6" />
    <Stroke color="#FF00FF" thickness="20" />
</Arc>

watchface_dynamic_appearance.xml
```

As `STEP_PERCENT` changes, `endAngle` is recalculated and the `Arc`
redrawn.

When a Transform element changes a target value, it can be desirable for
this change to be animated over a period of time, as opposed to an immediate
change in value, which could be jarring. Use the `Animation` element to achieve
this:

```
<PartDraw x="100" y="150" width="250" height="120" >
    <Ellipse x="0" y="0" width="50" height="50">
        <Fill color="#ff0000" />
        <!-- Red ball with no animated transition -->
        <Transform target="x" value="[SECOND] % 2 == 0 ? 0 : 200"/>
    </Ellipse>
    <Ellipse x="0" y="100" width="50" height="50">
        <Fill color="#00ff00" />
        <!-- Green ball eases between each position -->
        <Transform target="x" value="[SECOND] % 2 == 0 ? 0 : 200">
            <Animation duration="1" interpolation="EASE_IN_OUT" />
        </Transform>
    </Ellipse>
</PartDraw>

watchface_dynamic_appearance.xml
```

### Transforms using the accelerometer

While it is possible to use the `Transform` element with gyroscopic data
sources such as `ACCELEROMETER_ANGLE_X` to change the position or scale of an
element, Watch Face Format provides a separate element for these: [`Gyro`](/training/wearables/wff/common/transform/gyro).

This lets you simplify the overall picture, separating movement-based
transformation from other transformation such as time based, which might be
applied to the same element.