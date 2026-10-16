---
title: https://developer.android.com/health-and-fitness/health-connect/availability
url: https://developer.android.com/health-and-fitness/health-connect/availability
source: md.txt
---

Health Connect requires a mobile device running **Android 9 (API 28)** or higher
with **Google Play services** installed.

Health Connect is exclusive to Android and Google Play. Users can access Health
Connect in two ways, depending on their Android version:

- **On Android 14 and higher,** Health Connect is part of the Android system and is accessible in **Settings**.
- **On Android 13 and lower,** Health Connect is a publicly available app on the Google Play Store.

| **Note:** Health Connect is not supported on devices with work profiles. While users might be able to grant permissions in the work profile, the Health Connect APIs won't be usable, and no data will be written because the work profile is never considered to be in the foreground. Consider this limitation when developing for Google Workspace users.

## Android 14 framework

Health Connect is packaged with Android 14 as part of the Android system, which
means you cannot uninstall it from a device.

### Entry points

On Android 14, users access Health Connect app permissions and data in the
following ways:

- Go to **Settings \> Security \& Privacy \> Privacy \> Health Connect**.
- Go to **Settings \> Security \& Privacy \> Privacy \> Privacy dashboard \>
  (see other permissions) \> Health Connect**.
- Go to **Settings \> Security \& Privacy \> Privacy \> Permission manager \>
  Health Connect**.

## Android 13 APK

The Health Connect app was launched on the Google Play Store on
November 11, 2022.

Once third-party developers [integrate](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started) their apps and
[declare access](https://developer.android.com/health-and-fitness/guides/health-connect/publish/declare-access) to the Health Connect APIs and data types, their apps
can read, write, and share approved data types from the user's on-device store.

Check out the [migration guide](https://developer.android.com/health-and-fitness/guides/health-connect/migrate/migrate-from-android-13-to-14) for guidance on how data is migrated
between the APK and the framework model once users make the switch from
Android 13 to Android 14.