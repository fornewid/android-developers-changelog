---
title: https://developer.android.com/training/wearables/versions/6/changes
url: https://developer.android.com/training/wearables/versions/6/changes
source: md.txt
---

# Test how your app handles behavior changes

Wear OS 6 is based on Android 16 (API level 36). When you prepare your Wear OS app for use on Wear OS 6, handle the system[behavior changes that affect all apps in Android 16](https://developer.android.com/about/versions/16/behavior-changes-all), as well as the[changes for apps that target Android 16](https://developer.android.com/about/versions/16/behavior-changes-16).

Unless otherwise specified, the changes affect all apps that run on Wear OS 6 or higher, regardless of target SDK version.

As a reminder, watches that launch with Wear OS 6 only support watch faces that use the[Watch Face Format](https://developer.android.com/training/wearables/wff). For this reason, we recommend that you migrate to using the Watch Face Format.
| **Caution:** Before you upload your app to the Play Store,[target Android 16](https://developer.android.com/training/wearables/versions/6/setup#update-target-sdk)and[configure an emulator](https://developer.android.com/training/wearables/get-started/creating#configure-emulator)to test your app.

## More consistent always-on behavior

<br />

Wear OS 6 consolidates existing solutions to offer a consistent[always-on](https://developer.android.com/training/wearables/always-on)display experience across devices. As part of this change, the previous top activity remains visible and in the "resumed" state when the device enters system ambient mode.  
![](https://developer.android.com/static/training/wearables/versions/6/images/always-on.png)The current song and media controls remain visible even when the user isn't interacting with the Wear OS device.

<br />

## Default system font for tiles

Wear OS 6 introduces more consistency for tile typography, which helps users navigate through the tile carousel. On a given device, all tiles use the same font. On some devices, this consistent font is a[variable font](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts).
![](https://developer.android.com/static/training/wearables/versions/6/images/tile-water.png)  
![](https://developer.android.com/static/training/wearables/versions/6/images/tile-fitness.png)
All tiles on a given device use the same font.

## More granular health permissions

| **Note:** The following change affects your app only if you[update your target SDK version to Android 16](https://developer.android.com/training/wearables/versions/6/setup#update-target-sdk), the version on which Wear OS 6 is based, or higher.

Starting in Android 16---and, by extension, Wear OS 6---the platform is migrating to the more granular health permissions that Health Connect uses. This affects the following permissions:

| Wear OS 5.1 permission (`android.permission`) |                                                  Wear OS 6 permission (`android.permission.health`)                                                   |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BODY_SENSORS`                                | `READ_HEART_RATE` `READ_OXYGEN_SATURATION`(*sensor available on supported devices* ) `READ_SKIN_TEMPERATURE`(*sensor available on supported devices*) |
| `BODY_SENSORS_BACKGROUND`                     | `READ_HEALTH_DATA_IN_BACKGROUND`                                                                                                                      |

To learn how to update your app for handling these permissions when it targets API level 36 or higher, follow the[migration steps](https://developer.android.com/health-and-fitness/guides/health-services/permissions#migrate-support-api-36)shown in the Health Services for Wear OS guide.

<br />

**Note:**To maintain compatibility for apps that target Wear OS 5.1 (API level 35) and lower, the system offers the following support:

- If the user installs your app on a device that runs Wear OS 6 or higher, the system automatically requests the`READ_HEART_RATE`permission on your app's behalf.
- If the user previously granted the`BODY_SENSORS`and`BODY_SENSORS_BACKGROUND`permissions to your app, and if the user then updates their device to Wear OS 6 or higher, your app maintains the granted permissions.

<br />

## Tile interaction events are batched

| **Note:** The following change affects your app only if you[update your target SDK version to Android 16](https://developer.android.com/training/wearables/versions/6/setup#update-target-sdk), the version on which Wear OS 6 is based, or higher.

Starting in Wear OS 6, events related to users swiping onto and away from your tile---`onTileEnterEvent`and`onTileLeaveEvent`, respectively---are batched. If your app targets Wear OS 6 or higher, call[`onRecentInteractionEventsAsync()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onRecentInteractionEventsAsync(java.util.List%3Candroidx.wear.tiles.EventBuilders.TileInteractionEvent%3E))to monitor these events. Don't rely on real time delivery of these events to update your tiles.