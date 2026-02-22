---
title: https://developer.android.com/media/camera/camera-extensions
url: https://developer.android.com/media/camera/camera-extensions
source: md.txt
---

[Camera2](https://developer.android.com/training/camera2) and [CameraX](https://developer.android.com/training/camerax) provide an Extensions
API that lets your app access the following extensions that vendors have implemented
on Android devices:

- **Auto:** adjusts the extension mode according to the current scene background, which depends on the vendor library implementation. For example, in low light scenarios, Auto switches to Night to take a picture. For portrait photos, Auto applies Face Retouch or Bokeh.
- **Bokeh:** sharpens the foreground subject and blurs the background. Usually used to take portrait photos of people with a soft, out-of-focus background.
- **Face Retouch:** touches up skin texture, under-eye tone, and more.
- **HDR (High Dynamic Range):** widens exposure range, resulting in more vivid photos. In HDR mode, the camera takes several photos with various exposure values and merges them into one.
- **Night:** brightens photos in low-light situations. The camera takes several photos at various exposure values and merge them into one. This process can take several seconds, and the user should hold the phone still while the camera captures photos.

The [Camera2](https://developer.android.com/training/camera2/extensions-api) and
[CameraX](https://developer.android.com/training/camerax/extensions-api) Extension APIs expose the same set
of extensions, which are available on many
[supported devices](https://developer.android.com/training/camera/supported-devices).
| **Note:** Camera2 and CameraX extensions are only available for the preview and image capture use cases, not video capture.

## Supported devices

Not all devices support extensions, and even if a device has
extensions support, it does not support all extensions.

For a list of known devices that support extensions,
see [Supported devices](https://developer.android.com/training/camera/supported-devices). To check if
an extension is available on your device, see the
[Camera2 Extensions API](https://developer.android.com/training/camera2/extensions-api) and
[CameraX Extensions API](https://developer.android.com/training/camerax/extensions-api)
documentation, respectively.

## Next steps

Learn how to enable camera extensions for your app:

- [Camera2 Extensions API documentation](https://developer.android.com/training/camera2/extensions-api).
- [CameraX Extensions API documentation](https://developer.android.com/training/camerax/extensions-api).