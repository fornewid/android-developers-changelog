---
title: https://developer.android.com/training/wearables/wff/groups
url: https://developer.android.com/training/wearables/wff/groups
source: md.txt
---

Groups allow you to separate your watch face design into a logical structure.

This can be useful to help you organize components. You can give each
group a `name` to indicate what it is for.

A further reason that groups are very useful is that you can then treat
everything within that group as a single entity for the purpose of adjusting its
appearance, even dynamically adjusting to changing data sources.

Here are some examples of how this can be useful. The following `Group` contains
various `PartText, PartImage` and `PartDraw` elements that make up a single
logical part of the watch face:

<br />

```xml
<Group name="decorations" x="100" y="100" width="200" height="200">
    <!-- PartText, PartImage, PartDraw elements go here -->
</Group>
```

<br />

## Change ambient behavior

Having defined the `Group`, the visibility of the whole `Group` can be adjusted
for Ambient mode, for example, to hide the `Group`:

<br />

```xml
<Group name="decorations" x="100" y="100" width="200" height="200">
    <Variant mode="AMBIENT" target="alpha" value="0" />
    <!-- PartText, PartImage, PartDraw elements go here -->
</Group>
```

<br />

This avoids the need to add a `Variant` element individually to each child
element.

### Transform a group

Similar to adjusting the ambient behavior, using `Variant`, many of the
properties of `Group` can be adjusted using one or more `Transform` elements.

In this example, the `Group` is rotated based on the second. By specifying
`pivotX` and `pivotY` as `0.5`, the rotation occurs around the center of the
`Group`, irrespective of where each element, such as `PartText` or `PartImage`
sits within that `Group`:

<br />

```xml
<Group name="decorations" x="100" y="100" width="200" height="200">
    <!-- One full rotation per minute -->
    <Transform target="angle" value="[SECOND] * 6" />
    <!-- PartText, PartImage, PartDraw elements go here -->
</Group>
```

<br />