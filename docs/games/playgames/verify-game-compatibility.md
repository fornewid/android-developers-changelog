---
title: https://developer.android.com/games/playgames/verify-game-compatibility
url: https://developer.android.com/games/playgames/verify-game-compatibility
source: md.txt
---

This topic describes the troubleshooting steps to take when your game fails to
load in the [developer emulator](https://developer.android.com/games/playgames/pg-emulator) for
Google Play Games on PC. After you complete these steps you can make
another attempt to test your game in the emulator.

## Before you get started

Before you get started, make sure that you've completed the steps in the
following guides:

- The [get started guide](https://developer.android.com/games/playgames/start) for Google Play Games on PC.

- The [developer emulator](https://developer.android.com/games/playgames/pg-emulator) guide.

## Verify Play Console settings

In Google Play Console, verify that the following settings are configured:

### Release

1. **Form Factor** : **Google Play Games on PC only**

   - Go to **Settings \> Advanced settings \> Form factor** and verify that **Google Play Games on PC only** is added.
2. **Closed testing** : **Google Play Games on PC only**

   - Go to the **Closed testing** track and verify that **Google Play Games on PC only** is added. (Only necessary if you choose to create a dedicated track for Google Play Games on PC.)
3. **Countries / regions** : **United States** , **United Kingdom**

   - Go to the **Countries / regions** tab in the **Closed testing** track and verify that **United States** and **United Kingdom** are added.
4. **Google Groups** : `play-multiplatform-test-track@googlegroups.com`

   - Go to **Testers tab \> Google Groups** and verify that `play-multiplatform-test-track@googlegroups.com`
   - You can also grant track access by [creating your own group](https://support.google.com/googleplay/android-developer/answer/9845334#create_additional_track&zippy=%2Ccreate-additional-closed-test-tracks-for-your-development-teams) under this setting.
5. **Build status** : **Release**

   - Verify that you submitted a build on the **Closed testing** track from the previous steps and that the **Build status** is set to **Release**.

### Device compatibility

After you verify your release settings, verify the following settings in
Google Play Console:

1. Go to **Reach and devices \> Device catalog \> All devices** and then type
   `Google Play Games for PC` in the search bar.

2. **Device mode(google vsoc_kiwi_x86_64)** : **Supported**

   1. Verify that **Device mode(google vsoc_kiwi_x86_64)** is labeled as **Supported** .
      - If it is labeled as **Unsupported** , click the arrow icon, and then **Show more** to display to display details about fixing the issue.

### Device integrity

During certification process, do not turn on untrustworthy device exclusion in Play Console. An option in the Google Play Console allows you to
[prevent your app from being available to install](https://developer.android.com/google/play/integrity/additional-tools#prevent-untrustworthy-devices-from-getting-app)
from Google Play on devices that don't pass integrity checks which also prevent Google reviewers from accessing the game.

Check **Reach and devices \> Device catalog \> Device exclusion rules \> Play Integrity**

Don't enable this exclusion rule in the device catalog for
Google Play Games on PC games during the certification process. You can enable it after your game pass certification.