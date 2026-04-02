---
title: Work with images  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/wff/images
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Work with images Stay organized with collections Save and categorize content based on your preferences.



Using images in your watch face can really help bring it to life, from a
full-screen background image to individual detail images to add interest.

Place your image resources in the `res/drawable` folder, for example
`res/drawable/face.png`, and then reference the image as follows:

```
<PartImage x="0" y="0" width="450" height="450">
    <Image resource="watch_face_dial"/>
</PartImage>

watchface_images.xml
```

The `PartImage` element, as with other containers in Watch Face Format,
can be modified in
many ways, including being scaled, rotated, transformed, tinted, or masked.
See the [`PartImage`](/training/wearables/wff/group/part/image/part-image) reference for more information.

### Vary the background

One effect that can provide interest is to change the background every hour.
This can be achieved through the use of the `Images` element, for example:

```
<PartImage x="150" y="150" width="150" height="150">
    <Images change="ON_NEXT_HOUR">
        <Image resource="red"/>
        <Image resource="orange"/>
        <Image resource="green"/>
    </Images>
</PartImage>

watchface_images.xml
```