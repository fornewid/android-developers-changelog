---
title: https://developer.android.com/training/wearables/wff/ambient
url: https://developer.android.com/training/wearables/wff/ambient
source: md.txt
---

All watch faces should have not only an interactive mode, but also ambient mode.
The Wear OS App Quality guidelines specify that only [15% of pixels are
illuminated in ambient mode](https://developer.android.com/docs/quality-guidelines/wear-app-quality#wff).

Typically, the watch spends much more time in ambient mode, and during this
time, conserving power is a priority.

Well designed ambient displays contain only essential information, and they
minimize the number of pixels that are illuminated.

The recommended approach for implementing a component that alters in appearance
between ambient and interactive modes is to add two elements, each with a
`Variant`. Adding this at the `Part*` or `Group` level makes it possible keep
the number of `Variant` elements to a minimum.

<br />

```xml
<Group name="logo_interactive" x="100" y="100" width="200" height="200">
    <!-- Hide these elements in ambient mode -->
    <Variant mode="AMBIENT" target="alpha" value="0" />
    <!-- Components to show in interactive mode -->
</Group>
<Group name="logo_ambient" x="100" y="100" width="200" height="200" alpha="0">
    <Variant mode="AMBIENT" target="alpha" value="255" />
    <!-- Components to show in ambient mode -->
</Group>
```

<br />