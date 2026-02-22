---
title: https://developer.android.com/media/camera/lowlight/low-light-boost-gp/concepts
url: https://developer.android.com/media/camera/lowlight/low-light-boost-gp/concepts
source: md.txt
---

# Understand Google Low Light Boost

Google Play services offers the[*Google Low Light Boost library*](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/package-summary). This library allows apps to dynamically adjust the camera's brightness in real time to adapt to low light conditions, even when running on devices that don't support Low Light Boost AE Mode.

We provide several different ways to capture images in low-light conditions. To choose the right approach for your app's needs, see[Choose the best low light option](https://developer.android.com/media/camera/lowlight/choose-option).
| **Note:** Google Low Light Boost does not currently work with HLG10. If the client provides an HLG10 input, Google Low Light Boost outputs an error.

### Key interfaces

There are two main interfaces you need to know about to use Google Low Light Boost:

- [`LowLightBoostClient`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient)lets you confirm that the module is installed from Google Play services, and install the module if necessary. You also use the client to create a`LowLightBoostSession`.
- [`LowLightBoostSession`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostSession)manages the necessary input surfaces and outputs the brightened camera preview to the surface provided by the app. You use`LowLightBoostSession`to turn low light boost on or off.

### Google Low Light Boost workflow

To provide preview images in low light conditions, follow this sequence:

1. [Check whether the device you're on supports Low Light Boost AE Mode](https://developer.android.com/media/camera/lowlight/hw-low-light-boost#check-availability). If the device supports Low Light Boost AE Mode, use it instead of Google Low Light Boost.
2. [Create a Camera2 session](https://developer.android.com/media/camera/camera2). Software LLB works with the Camera2 APIs.
3. [Create a`LowLightBoostClient`](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client#create). This object provides essential utilities you'll need to use Google Low Light Boost.
4. [Check if the low light boost module is installed](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client#check-installed). Google Low Light Boost is provided by Google Play services, so you'll need to check whether it's already installed on the device. If it isn't, you'll need to[install the module](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client#install).
5. [Confirm that the device camera supports Google Low Light Boost](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client#check-supported).
6. [Create a`LowLightBoostSession`](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#create-session). This object lets you turn low light mode on and off.
7. [Preview or record video](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#preview)the way you normally would with Camera2.
8. When the camera is no longer active,[release the session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#release).