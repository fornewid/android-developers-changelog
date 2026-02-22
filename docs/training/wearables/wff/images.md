---
title: https://developer.android.com/training/wearables/wff/images
url: https://developer.android.com/training/wearables/wff/images
source: md.txt
---

Using images in your watch face can really help bring it to life, from a
full-screen background image to individual detail images to add interest.

Place your image resources in the `res/drawable` folder, for example
`res/drawable/face.png`, and then reference the image as follows:

<br />

```xml
<PartImage x="0" y="0" width="450" height="450">
    <Image resource="watch_face_dial"/>
</PartImage>
```

<br />

The `PartImage` element, as with other containers in Watch Face Format,
can be modified in
many ways, including being scaled, rotated, transformed, tinted, or masked.
See the [`PartImage`](https://developer.android.com/training/wearables/wff/group/part/image/part-image) reference for more information.

### Vary the background

One effect that can provide interest is to change the background every hour.
This can be achieved through the use of the `Images` element, for example:

<br />

```xml
<PartImage x="150" y="150" width="150" height="150">
    <Images change="ON_NEXT_HOUR">
        <Image resource="red"/>
        <Image resource="orange"/>
        <Image resource="green"/>
    </Images>
</PartImage>
```

<br />