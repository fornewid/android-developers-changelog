---
title: https://developer.android.com/training/cars/media/distraction-safeguards
url: https://developer.android.com/training/cars/media/distraction-safeguards
source: md.txt
---

# Implement distraction safeguards

Because a user's phone is connected to a car's speakers when using Android Auto, you must take additional precautions to prevent driver distraction.

When you develop Android Auto media apps, implement specific safeguards to minimize driver distraction. These safeguards include:

- Preventing your app from automatically playing audio through car speakers, even for user-scheduled alarms.

- Managing how Android Auto displays notifications when your app switches between music and ads.

To achieve this, use the`CarConnection`API to detect if a phone projects to a car screen. If it does, disable alarms or provide an on-phone UI to manage them. For ads, set the`METADATA_KEY_IS_ADVERTISEMENT`metadata key to suppress distracting notifications.

## Suppress alarms in the car

Android Auto media apps must not start playing audio through the car speakers unless the user starts playback by, for example, pressing a**Play**button. Even a user-scheduled alarm from your media app must not start playing music through the car speakers.

To fulfill this requirement, your app can use[`CarConnection`](https://developer.android.com/reference/androidx/car/app/connection/CarConnection)as a signal before playing any audio. Your app can check if the phone is projecting to a car screen. Observe the`LiveData`for the[connection type](https://developer.android.com/reference/androidx/car/app/connection/CarConnection#getType()). Confirm the value is equal to[`CONNECTION_TYPE_PROJECTION`](https://developer.android.com/reference/androidx/car/app/connection/CarConnection#CONNECTION_TYPE_PROJECTION()).

If the user's phone is projecting, media apps that support alarms must perform one of these actions:

- Disable the alarm.

- Re-play the alarm[`STREAM_ALARM`](https://developer.android.com/reference/android/media/AudioManager#STREAM_ALARM)and provide a UI on the phone screen to disable the alarm.

## Handle media advertisements

By default, Android Auto displays a notification when the media metadata changes during an audio playback session. When a media app switches from playing music to running an advertisement, displaying a notification distracts the user. To prevent Android Auto from displaying a notification, set the media metadata key[`METADATA_KEY_IS_ADVERTISEMENT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#METADATA_KEY_IS_ADVERTISEMENT())to[`METADATA_VALUE_ATTRIBUTE_PRESENT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#METADATA_VALUE_ATTRIBUTE_PRESENT()):  

### Kotlin

    import androidx.media.utils.MediaConstants

    override fun onPlayFromMediaId(mediaId: String, extras: Bundle?) {
        MediaMetadataCompat.Builder().apply {
            if (isAd(mediaId)) {
                putLong(
                    MediaConstants.METADATA_KEY_IS_ADVERTISEMENT,
                    MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT)
            }
            // ...add any other properties you normally would.
            mediaSession.setMetadata(build())
        }
    }

### Java

    import androidx.media.utils.MediaConstants;

    @Override
    public void onPlayFromMediaId(String mediaId, Bundle extras) {
        MediaMetadataCompat.Builder builder = new MediaMetadataCompat.Builder();
        if (isAd(mediaId)) {
            builder.putLong(
                MediaConstants.METADATA_KEY_IS_ADVERTISEMENT,
                MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT);
        }
        // ...add any other properties you normally would.
        mediaSession.setMetadata(builder.build());
    }