---
title: https://developer.android.com/develop/ui/views/quicksettings-tiles/qr-code
url: https://developer.android.com/develop/ui/views/quicksettings-tiles/qr-code
source: md.txt
---

Quick Settings are tiles displayed in the [Quick Settings panel](https://support.google.com/android/answer/9083864).
Users can tap these tiles to quickly complete recurring tasks.
This document shows you how to create a custom Quick Settings tile for QR Code
payments.

Before continuing, be sure you're familiar with general instructions and best
practices for [creating custom Quick Settings tiles for your app](https://developer.android.com/develop/ui/views/quicksettings-tiles).

To [create your tile](https://developer.android.com/develop/ui/views/quicksettings-tiles#create-tile), follow these steps:

1. [Create your custom icon](https://developer.android.com/develop/ui/views/quicksettings-tiles#create-custom).
2. [Create and declare your `TileService`](https://developer.android.com/develop/ui/views/quicksettings-tiles#create-declare-tileservice).

   > [!NOTE]
   > **Note:** At this point, your custom tile service will appear in the Quick Settings menu. In order to see your custom tile upon pull down, [edit and
   > rearrange your tiles](https://support.google.com/android/answer/9083864).

3. To launch the QR Code payment, fill in the `onClick()` method. Long-tapping
   a tile prompts the App Info screen for the user. To override this behavior
   and instead launch an activity for setting preferences, add an
   `<intent-filter>` to one of your activities with
   [`ACTION_QS_TILE_PREFERENCES`](https://developer.android.com/reference/android/service/quicksettings/TileService.html?utm_campaign=adp_series_quicksettingstiles_092916&utm_source=medium&utm_medium=blog#ACTION_QS_TILE_PREFERENCES).

   ### Kotlin

   ```kotlin
   import android.service.quicksettings.TileService

   // Called when the user taps on your tile in an active or inactive state.
   override fun onClick() {
      // Create Intent, replace MainActivity::class.java with QR Code Activity
      val intent = Intent(this, MainActivity::class.java)
      // Create PendingIntent
      val pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE)
      if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.UPSIDE_DOWN_CAKE) {
        startActivityAndCollapse(pendingIntent)
      } else {
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        startActivityAndCollapse(intent)
      }
   }
   ```

   ### Java

   ```java
   import android.service.quicksettings.TileService;

   // Called when the user taps on your tile in an active or inactive state.
   @Override
   public void onClick() {
    // Create Intent, replace MainActivity.class with QR Code Activity
    Intent intent = new Intent(MyQSTileService.this, MainActivity.class);
    // Create PendingIntent
    PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE);
    if (VERSION.SDK_INT >= VERSION_CODES.UPSIDE_DOWN_CAKE) {
      startActivityAndCollapse(pendingIntent);
    } else {
      intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
      startActivityAndCollapse(intent);
    }
   }
   ```
4. To protect users' sensitive payment information, [perform only safe actions
   on securely-locked devices](https://developer.android.com/develop/ui/views/quicksettings-tiles#perform-only).

   ### Kotlin

   ```kotlin
   import android.service.quicksettings.TileService

   override fun onClick() {
      val intent = Intent(this, MainActivity::class.java)
      val pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE)

      // ...

      if (isSecure()) {
          startActivityAndCollapse(pendingIntent)
      } else {
          unlockAndRun {
              startActivityAndCollapse(pendingIntent)
          }
      }
      // ...
   }
   ```

   ### Java

   ```java
   import android.service.quicksettings.TileService;

   @Override
   public void onClick() {
    Intent intent = new Intent(MyQSTileService.this, MainActivity.class);
    PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_IMMUTABLE);
    ...
    if (isSecure()) {
      startActivityAndCollapse(pendingIntent);
    } else {
      unlockAndRun(new Runnable() {
        @Override
        public void run() {
          startActivityAndCollapse(pendingIntent);
        }
      });
     }
    ...
   }
   ```
5. When first introducing this feature, [prompt the user to add your
   tile](https://developer.android.com/develop/ui/views/quicksettings-tiles#prompt-user).