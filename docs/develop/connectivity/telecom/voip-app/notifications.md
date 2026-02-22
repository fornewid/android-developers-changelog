---
title: https://developer.android.com/develop/connectivity/telecom/voip-app/notifications
url: https://developer.android.com/develop/connectivity/telecom/voip-app/notifications
source: md.txt
---

# Add notifications to a media app

When building a media app that processes audio or video, it's important to use the correct notifications and notification channels. This ensures that notifications have the following valuable features:

- Have notification priority
- Are non-dismissable
- Use audio attributes for ringtones

Use`NotificationChannel.Builder`to set up two notification channels: one for incoming calls and the other for active calls.  

    internal companion object {
        const val TELECOM_NOTIFICATION_ID = 200
        const val TELECOM_NOTIFICATION_ACTION = "telecom_action"
        const val TELECOM_NOTIFICATION_INCOMING_CHANNEL_ID = "telecom_incoming_channel"
        const val TELECOM_NOTIFICATION_ONGOING_CHANNEL_ID = "telecom_ongoing_channel"

        private val ringToneUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_RINGTONE)
    }

To display the notification everywhere and allow it to play audio for the ringtone, set the importance of the incoming notification channel to high.  

    val incomingChannel = NotificationChannelCompat.Builder(
            TELECOM_NOTIFICATION_INCOMING_CHANNEL_ID,
            NotificationManagerCompat.IMPORTANCE_HIGH,
        ).setName("Incoming calls")
            .setDescription("Handles the notifications when receiving a call")
            .setVibrationEnabled(true).setSound(
                ringToneUri,
                AudioAttributes.Builder()
                    .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                    .setLegacyStreamType(AudioManager.STREAM_RING)
                    .setUsage(AudioAttributes.USAGE_NOTIFICATION_RINGTONE).build(),
            ).build()

Only active calls requires the importance to be set to default. Use the following incoming call style to allow notifications for incoming calls to be non-dismissable.  

    val ongoingChannel = NotificationChannelCompat.Builder(
            TELECOM_NOTIFICATION_ONGOING_CHANNEL_ID,
            NotificationManagerCompat.IMPORTANCE_DEFAULT,
        )
        .setName("Ongoing calls")
        .setDescription("Displays the ongoing call notifications")
        .build()

To address use cases where the user's device is locked during an incoming call, use a full-screen notification to display an activity to allow the user to answer the call.  

    // on the notification
    val contentIntent = PendingIntent.getActivity(
        /* context = */ context,
        /* requestCode = */ 0,
        /* intent = */ Intent(context, TelecomCallActivity::class.java),
        /* flags = */ PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
    )

Read[Create a call style notification for call apps](https://developer.android.com/develop/ui/views/notifications/call-style)for instructions on using[`CallStyle`](https://developer.android.com/reference/android/app/Notification.CallStyle)to distinguishing call notifications from other types of notifications.