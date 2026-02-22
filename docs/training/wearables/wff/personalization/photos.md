---
title: https://developer.android.com/training/wearables/wff/personalization/photos
url: https://developer.android.com/training/wearables/wff/personalization/photos
source: md.txt
---

**Note**: This feature is available on version 4 and higher of Watch Face
Format.

Allowing the user to select photos for inclusion on the watch face can help
bring a personal touch to your watch face experience.

The [working with images](https://developer.android.com/training/wearables/wff/images) section already covers how to display images in
your watch face. If you want to allow the user to choose from a range of
predefined images, then use a `ListConfiguration` as shown in the [define user
configurations](https://developer.android.com/training/wearables/wff/personalization/user-configurations) section.

To use images in your watch face that the user can configure, use the
`<PhotosConfiguration>` element, for example:

<br />

```xml
<!-- Under WatchFace element -->
<UserConfigurations>
    <PhotosConfiguration id="photoConfig" configType="SINGLE"/>
</UserConfigurations>
```

<br />

The `configType` can be either `SINGLE` or `MULTIPLE` indicating whether the
user will be able to select a single image within the companion or a collection
of photos.

## Support a single photo

For the single image case, the photo can be used within a `PartImage` element as
follows:

<br />

```xml
<PartImage x="100" y="50" width="100" height="100">
    <Photos source="[CONFIGURATION.photoConfig]" defaultImageResource="default_image"/>
</PartImage>
```

<br />

Note the `defaultImageResource`, which is shown when the user has not
selected a photo in the companion and is a required attribute.

If the user wishes to select a different photo, then they must use the companion
to replace the existing selection with another.

## Support multiple photos

Using `PhotosConfiguration` with `configType="MULTIPLE"` allows the watch face
to display a photo from a collection, which can be cycled through either through
tapping or automatically after so many views have taken place.

<br />

```xml
<PartImage x="100" y="250" width="100" height="100">
    <Photos change="ON_VISIBLE TAP" changeAfterEvery="5"
        source="[CONFIGURATION.galleryConfig]" defaultImageResource="default_image"/>
</PartImage>
```

<br />

The preceding example shows the two options that are introduced when using
`MULTIPLE`:

1. The `change` attribute allows the developer to specify what events should cause the photo to cycle through the available images.

In the preceding example, both `TAP` and `ON_VISIBLE` are specified, meaning
that the photo changes in response *either* to a user tapping the photo *or*
in response to the photo becoming visible.

1. The `changeAfterEvery` attribute applies only to the `ON_VISIBLE` change event, specifing how many times the photo should have become visible before the photo is changed. For example, you may feel that changing the photo every time the user wakes their watch is too frequent. The default value here is 3.

For more details on working with `PhotosConfiguration`, see the samples on
GitHub.