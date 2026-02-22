---
title: https://developer.android.com/studio/run/emulator-use-camera
url: https://developer.android.com/studio/run/emulator-use-camera
source: md.txt
---

# Camera support

The emulator supports the use of basic camera functionality on your virtual device for earlier Android versions. Android 11 and higher supports the following additional Android Emulator camera capabilities:

- RAW capture
- YUV reprocessing
- Level 3 devices
- Logical camera support
- Emulating sensor orientation by using data from the sensor manager
- Applying video stabilization by reducing handshake frequency
- Applying edge enhancement by removing the upscaling usually done in the YUV pipeline
- Concurrent cameras

## Virtual scene camera and ARCore

You can use the virtual scene camera in a virtual environment to experiment with augmented reality (AR) apps made with[ARCore](https://developers.google.com/ar/discover/).

For information on using the virtual scene camera in the emulator, see[Run AR apps in Android Emulator](https://developers.google.com/ar/develop/java/emulator).

When using the emulator with a camera app, you can import an image in PNG or JPEG format to be used within a virtual scene. To choose an image for use in a virtual scene, open the**Extended controls** window, select the**Camera \> Virtual scene images** tab, and click**Add image** . This feature can be used to import custom images such as QR codes for use with any camera-based app. For more information, see[Add Augmented Images to the scene](https://developers.google.com/ar/develop/java/emulator#add_augmented_images_to_the_scene).

## Test common AR actions with macros

You can greatly reduce the time it takes to test common AR actions by using the preset macros in the emulator. For example, you can use a macro to reset all the device's sensors to their default state.

Before using macros, follow the steps in[Run AR apps in Android Emulator](https://developers.google.com/ar/develop/java/emulator)to set up the virtual scene camera for your app, run your app on the emulator, and update ARCore. Then, follow these steps to use emulator macros:

1. With the emulator running and your app connected to ARCore, click**More** ![](https://developer.android.com/static/studio/images/buttons/emulator-extended-controls.png)in the emulator panel.
2. Select**Record and Playback \> Macro Playback**.
3. Choose a macro that you want to use, then click**Play**.

   During playback, you can interrupt a macro by clicking**Stop**.