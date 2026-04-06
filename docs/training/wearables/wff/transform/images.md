---
title: https://developer.android.com/training/wearables/wff/transform/images
url: https://developer.android.com/training/wearables/wff/transform/images
source: md.txt
---

In addition to static images on the watch face, animated images can bring a
further dimension to the user experience.

Note that this section is specifically about using animated image files. It is
possible to animate components on the watch face using the `Transform` element,
which is covered on the [Dynamically changing the appearance of
elements](https://developer.android.com/training/wearables/wff/transform) page.

Animations can consist of either an animated image file, such as an animated
GIF, or a sequence of `Images`, which combine together to form an animation.

As well as specifying the files to use, you'll need to define how the animation
should behave, for example, whether to loop the playback, or if not, what to do
at the end, among other options. For this, use an [`AnimationController`](https://developer.android.com/training/wearables/wff/group/part/animated-image/animation-controller).

Finally, for all animations, include a [thumbnail
image](https://developer.android.com/training/wearables/wff/group/part/animated-image/thumbnail) in all animations.

Putting this together, a basic animation can be implemented as follows:

<br />

```xml
<PartAnimatedImage x="0" y="0" width="450" height="450">
    <AnimationController play="ON_VISIBLE"/>
    <AnimatedImage resource="animation" format="AGIF"/>
    <Thumbnail resource="animation_thumbnail" />
</PartAnimatedImage>
```

<br />

Consult the [`PartAnimatedImage`](https://developer.android.com/training/wearables/wff/group/part/animated-image/part-animated-image) reference for more details on including a
list of animated images and constructing an animation from still images.