---
title: Advanced emulator usage  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/run/advanced-emulator-usage
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Studio](https://developer.android.com/studio)

# Advanced emulator usage Stay organized with collections Save and categorize content based on your preferences.



You might need to test your app on a virtual device using more than
just basic touch screen gestures and phone movements. For example, you might want to
simulate different locations or network conditions. This page covers advanced
emulator features and different ways to launch the emulator with Android
Studio.

The other pages in this section cover even more advanced ways to use the
emulator, which require you to use the terminal. These more specialized use cases are:

* If you aren’t using Android Studio, you can
  [start the emulator from the command line](/studio/run/emulator-commandline).
* To test features including fingerprint validation, or to change your virtual
  device’s battery state, you can
  [send emulator console commands](/studio/run/emulator-console).
* To have two emulator instances that can communicate to each other,
  or to set up other complex network architectures, you can
  [set up emulator networking](/studio/run/emulator-networking).

For most app developers, the
[basic emulator navigation capabilities](/studio/run/emulator#navigate) and
the features on this page cover your testing needs. For a side-by-side
comparison of what you can do with the emulator depending on how you interact
with it, see [the emulator feature comparison](/studio/run/emulator-comparison).

## Limitations

The Android Emulator doesn't include virtual hardware for the following:

* Bluetooth
* NFC
* SD card insert/eject
* Device-attached headphones
* USB

The watch emulator for Wear OS doesn't provide the Overview (Recent Apps)
button, D-pad, or fingerprint sensor.