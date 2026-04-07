---
title: https://developer.android.com/privacy-and-security/risks/sticky-broadcast
url: https://developer.android.com/privacy-and-security/risks/sticky-broadcast
source: md.txt
---

# Sticky Broadcasts

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

Android apps and the Android system can use broadcasts as a messaging system to notify other apps of events that they might be interested in.*Sticky broadcasts*are a special type of broadcast for which the sent intent object(s) remains in the cache after the broadcast is complete. The system may re-broadcast sticky intents to later registrations of receivers. Unfortunately, the sticky broadcasts API suffers from a number of security-related shortcomings, which is why it was deprecated in Android 5.0 (API level 21).

### Anyone can access sticky broadcasts

Sticky broadcasts cannot be restricted to receivers that hold certain permissions. Therefore, they aren't suitable for broadcasting sensitive information. It might be tempting to think that specifying the[application package name](https://developer.android.com/reference/android/content/Intent#setPackage(java.lang.String))on the broadcast`Intent`limits the set of`BroadcastReceivers`:  

### Kotlin

    val intent = Intent("com.example.NOTIFY").apply {
        setPackage("com.example.myapp")
    }
    applicationContext.sendBroadcast(intent)

### Java

    Intent intent = new Intent("com.example.NOTIFY");
    intent.setPackage("com.example.myapp");
    getApplicationContext().sendBroadcast(intent);

In the example, only receivers in the`com.example.myapp`package receive the intent when the broadcast is sent. However, the package name filter isn't applied when the Intent is re-broadcast from the sticky cache. When registering a receiver using the[`registerReceiver()`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter))method, all intents in the sticky cache that match the specified filter are re-broadcast to the receiver regardless of the package name in which the receiver resides.

### Anyone can send sticky broadcasts

To send sticky broadcasts, an app only requires the`android.permission.BROADCAST_STICKY`permission, which is granted automatically when the app is installed. Therefore, attackers can send any intent to any receiver, potentially gaining unauthorized access to another app. Broadcast receivers can restrict the senders to those holding a certain permission. However, by doing so, the receiver can't receive broadcasts from the sticky cache because those are not sent in the context of any app's identity and aren't broadcast with any permissions.

### Anyone can modify sticky broadcasts

When an intent is part of a sticky broadcast, that intent replaces any previous instance that has the same action, data, type, identifier, class, and categories in the sticky cache. Therefore, an attacker can trivially overwrite the extra data in a sticky intent from a legitimate app, which might then get re-broadcast to other receivers.

Broadcasts sent using the[`sendStickyOrderedBroadcast()`](https://developer.android.com/reference/android/content/Context#sendStickyOrderedBroadcast(android.content.Intent,%20android.content.BroadcastReceiver,%20android.os.Handler,%20int,%20java.lang.String,%20android.os.Bundle))method are delivered to one receiver at a time to allow receivers with higher priority to consume the broadcast before it's delivered to receivers with lower priority. As each receiver executes in turn, it can propagate a result to the next receiver, such as by calling[`setResultData()`](https://developer.android.com/reference/android/content/BroadcastReceiver#setResultData(java.lang.String)), or it can[abort the broadcast](https://developer.android.com/reference/android/content/BroadcastReceiver#abortBroadcast()), preventing subsequent receivers from receiving the broadcast. An attacker that can receive sticky ordered broadcasts from a legitimate app can create a high-priority receiver to tamper with the broadcast result data or drop broadcasts completely.

## Impact

Impact varies depending on how sticky broadcasts are used and what data is passed to the broadcast receivers. Generally speaking, use of sticky broadcasts can lead to sensitive data exposure, data tampering, unauthorized access to execute behavior in another app, and denial of service.

## Mitigations

Sticky broadcasts shouldn't be used. The recommended pattern is to use non-sticky broadcasts with another mechanism, such as a local database, to retrieve the current value whenever desired.

Developers can control who can receive non-sticky broadcasts using[permissions](https://developer.android.com/guide/components/broadcasts#restrict-broadcasts-permissions)or by setting the[application package name](https://developer.android.com/reference/android/content/Intent#setPackage(java.lang.String))on the intent. Furthermore, if a broadcast doesn't need to be sent to components outside of an app, use[`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData), which implements the[observer pattern](https://en.wikipedia.org/wiki/Observer_pattern).

More information about securing broadcasts can be found on the[broadcasts overview](https://developer.android.com/guide/components/broadcasts#security-and-best-practices)page.