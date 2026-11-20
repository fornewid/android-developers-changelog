---
title: https://developer.android.com/media/grow/hdr-lut
url: https://developer.android.com/media/grow/hdr-lut
source: md.txt
---

> Documentation index: https://developer.android.com/media/grow/llms.txt

Varying HDR capabilities across Android devices can lead to fragmented HDR
display outputs. A look-up table (LUT) is a new color correction solution
designed to resolve this inconsistency. This inconsistency is resolved by
*prescribing* a way to color correct, rather than delegating to an undefined
per-device color correction mechanism.

## SDK prerequisites

To implement LUTs, your SDK version must 36 or higher.

## Implement a LUT

Follow these steps to apply a LUT to a [`SurfaceControl`](https://developer.android.com/reference/android/view/SurfaceControl.md.txt):

1. Create a [`DisplayLuts`](https://developer.android.com/reference/android/hardware/DisplayLuts.md.txt) instance.
2. Create [`DisplayLuts.Entry`](https://developer.android.com/reference/android/hardware/DisplayLuts.Entry.md.txt) instance(s) with the LUT data buffer, LUT dimension, and the sampling key of the LUT. For more information, see [`LutProperties`](https://developer.android.com/reference/android/hardware/LutProperties.md.txt) documentation.
3. Call [`DisplayLuts#set(DisplayLuts.Entry luts)`](https://developer.android.com/reference/android/hardware/DisplayLuts.md.txt#set(android.hardware.DisplayLuts.Entry)) or [`DisplayLuts#set(DisplayLuts.Entry first, DisplayLuts.Entry second)`](https://developer.android.com/reference/android/hardware/DisplayLuts.md.txt#set(android.hardware.DisplayLuts.Entry,%20android.hardware.DisplayLuts.Entry)) to set LUT entries. The framework supports 1D LUT, 3D LUT, or a combination of 1D and 3D LUTs.
4. Call [`SurfaceControl.Transaction#setLuts`](https://developer.android.com/reference/android/view/SurfaceControl.Transaction.md.txt#setLuts(android.view.SurfaceControl,%20android.hardware.DisplayLuts)) to apply the LUTs to the layer.


```kotlin
val sc = SurfaceControl.Builder().build()
val luts = DisplayLuts()
val entry = DisplayLuts.Entry(
    floatArrayOf(0.5f, 0.5f, 0.5f, 0.5f),
    LutProperties.ONE_DIMENSION,
    LutProperties.SAMPLING_KEY_MAX_RGB
)
luts.set(entry)
SurfaceControl.Transaction().setLuts(sc, luts).apply()
```

<br />

You can also use [`OverlayProperties.getLutProperties()`](https://developer.android.com/reference/android/hardware/OverlayProperties.md.txt#getLutProperties()) to understand the
LUT properties of the device, and determine if the Hardware Composer can handle
the selected LUT.