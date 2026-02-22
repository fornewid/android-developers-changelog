---
title: https://developer.android.com/training/cars/testing/emulator/configurable
url: https://developer.android.com/training/cars/testing/emulator/configurable
source: md.txt
---

To help emulate some of the configurations seen across OEMs, certain[hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles)support runtime configurability.

These configurations are implemented using[Runtime Resource Overlays](https://source.android.com/docs/core/runtime/rros)(RROs) and can be managed using the`adb shell cmd overlay`command.

Use the following commands to enable or disable a RRO:  

    adb shell cmd overlay enable <var translate="no">NAME</var>
    adb shell cmd overlay disable <var translate="no">NAME</var>

## Modify system bar position

By default, the configurable emulator has two system bars -- a status bar on the top of the screen and a navigation bar at the bottom of the screen. Though many cars share this layout, some don't. Some cars have their system bars on the horizontal sides of the screen instead of the vertical sides, which can break assumptions that you make when developing apps for mobile form factors. See[System bars, immersive mode, and edge-to-edge rendering](https://developer.android.com/training/cars/parked/automotive-os#bars-immersive-edge)for more details and technical guidance.

The following RROs can be used to modify the system bars:

- `com.android.systemui.rro.bottom`
- `com.android.systemui.rro.bottom.rounded`
- `com.android.systemui.rro.left`
- `com.android.systemui.rro.right`

## Emulate display cutouts

Some cars have screens with display cutouts that are very different when compared to those seen on mobile devices. Instead of the notches or pinhole camera cutouts, some Android Automotive OS vehicles have curved screens that make the screen non-rectangular. See[Adapt to irregularly shaped displays](https://developer.android.com/training/cars/parked/automotive-os#irregular-displays)for more details and technical guidance.

The following RROs can be used to emulate display cutouts:

- `com.android.internal.display.cutout.emulation.top_and_right`
- `com.android.internal.display.cutout.emulation.free_form`
- `com.android.internal.emulation.automotive_ultrawide_cutout`

## Recommended testing configurations

Because you can create many configurations by combining these RROs, we recommend that you test your app using the following combinations of[hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles)and RROs. These combinations are similar to some vehicles on the road today.

- *Automotive (1080p landscape)* with`com.android.systemui.rro.left`or`com.android.systemui.rro.right`
- *Automotive Ultrawide* with`com.android.systemui.rro.left`and`com.android.internal.emulation.automotive_ultrawide_cutout`