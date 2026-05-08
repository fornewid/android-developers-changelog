---
title: https://developer.android.com/develop/connectivity/telecom/call-log-integration
url: https://developer.android.com/develop/connectivity/telecom/call-log-integration
source: md.txt
---

VoIP applications can integrate their calls into the system call log. This
lets users see their VoIP call history centrally in the system dialer app
and return calls directly from the dialer app. This guide describes the
required changes to [VoIP calling apps](https://developer.android.com/develop/connectivity/telecom/call-log-integration#changes-calling-app) and
[system dialer apps](https://developer.android.com/develop/connectivity/telecom/call-log-integration#changes-dialer-app).

> [!NOTE]
> **Note:** The features described on this page require [Jetpack Telecom library
> version `1.1.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/core#core-telecom_version_11_2) or higher.

## Changes for the calling app

To integrate your VoIP app with the system call log, follow these steps.

### Register callback intent filter

Register the system-protected intent [`TelecomManager.ACTION_CALL_BACK`](https://developer.android.com/reference/android/telecom/TelecomManager#ACTION_CALL_BACK).

Once this intent filter is properly registered, any calls your app adds using
[`CallsManager.addCall`](https://developer.android.com/reference/androidx/core/telecom/CallsManager#addCall(androidx.core.telecom.CallAttributesCompat,kotlin.coroutines.SuspendFunction1,kotlin.coroutines.SuspendFunction1,kotlin.coroutines.SuspendFunction0,kotlin.coroutines.SuspendFunction0,kotlin.Function1)) or other related Telecom APIs will be automatically
logged by the system. The system uses this registered intent to later send a
callback to your app when a user selects a VoIP call log entry in the dialer
to return the call.


```xml
<!-- Activity to handle the callback intent from the system dialer -->
<activity
    android:name=".VoipCallActivity"
    android:exported="true">

    <!-- Register callback intent -->
    <intent-filter>
        <action android:name="android.telecom.action.CALL_BACK" />
    </intent-filter>
</activity>
```

<br />

### Exclude call logging

Once the callback is registered, all calls are logged to the system
dialer. To exclude calls on a per-call basis, set the [`isLogExcluded`](https://developer.android.com/reference/androidx/core/telecom/CallAttributesCompat#isLogExcluded())
boolean to `true` within [`CallAttributesCompat`](https://developer.android.com/reference/androidx/core/telecom/CallAttributesCompat).


```kotlin
CallAttributesCompat(
    displayName = displayName,
    address = address,
    isLogExcluded = excludeCallLogging, // to exclude call from logging
    direction = if (isIncoming) {
        CallAttributesCompat.DIRECTION_INCOMING
    } else {
        CallAttributesCompat.DIRECTION_OUTGOING
    },
    callType = CallAttributesCompat.CALL_TYPE_AUDIO_CALL,
    callCapabilities = (
        CallAttributesCompat.SUPPORTS_SET_INACTIVE
            or CallAttributesCompat.SUPPORTS_STREAM
            or CallAttributesCompat.SUPPORTS_TRANSFER
        ),
)
```

<br />

### Handle callbacks

Calls added through [`CallsManager.addCall`](https://developer.android.com/reference/androidx/core/telecom/CallsManager#addCall(androidx.core.telecom.CallAttributesCompat,kotlin.coroutines.SuspendFunction1,kotlin.coroutines.SuspendFunction1,kotlin.coroutines.SuspendFunction0,kotlin.coroutines.SuspendFunction0,kotlin.Function1)) get a unique `UUID` through
[`CallControlScope.getCallId`](https://developer.android.com/reference/androidx/core/telecom/CallControlScope#getCallId()).

> [!IMPORTANT]
> **Important:** The calling VoIP app must map the call details to this unique `UUID` and store them. When a user selects a VoIP call log entry in the dialer, the system dialer initiates a callback with the intent action [`TelecomManager.ACTION_CALL_BACK`](https://developer.android.com/reference/android/telecom/TelecomManager#ACTION_CALL_BACK) and an intent extra [`TelecomManager.EXTRA_UUID`](https://developer.android.com/reference/android/telecom/TelecomManager#EXTRA_UUID). The VoIP app uses the stored `UUID` to retrieve the correct call details and handle the return call.


```kotlin
// check the intent action for CALL_BACK
if (intent.action == TelecomManager.ACTION_CALL_BACK) {
    launchCall(
        // fetching stored call details for the UUID to initiate callback
        callDetails = getCallDetails(
            uuid = intent.getStringExtra(TelecomManager.EXTRA_UUID)
        )
    )
}
```

<br />

### Verify call log entries

The system call log maintains a finite number of entries and eventually
purges old call records. Because the app stores a mapping of `UUID`s to call
details for callback handling, it should periodically check which `UUID`s are
still present in the system call log. If a `UUID` is no longer in the system
log, the user cannot initiate a callback for that call, and the app can
safely remove the mapping from its local storage. This practice helps
optimize storage.

To get the current list of `UUID`s attributed to the app within the system
log, use [`CallLog.Calls.CONTENT_VOIP_URI`](https://developer.android.com/reference/android/provider/CallLog.Calls#CONTENT_VOIP_URI).

## Changes for the dialer app

Follow these steps to enable the dialer app to display VoIP call logs and
initiate callbacks to VoIP apps.

### Display VoIP call logs in the dialer app

By default, VoIP apps call logs don't appear in the dialer app. To display
the integrated call logs in the dialer app, do the following:

- On Android 16.1 (API level 36.1), append the query parameter
  `include_voip_calls` to the
  `CallLog.Calls` content provider to display VoIP call logs:


  ```kotlin
  CallLog.Calls.CONTENT_URI.buildUpon()
      .appendQueryParameter("include_voip_calls", "true")
      .build()
  ```

  <br />

- On Android 17 (API level 37) and higher, use the following formalized
  content provider and parameter key:

  - [`CallLog.Calls.CONTENT_URI_WITH_VOIP_CALLS`](https://developer.android.com/reference/android/provider/CallLog.Calls#CONTENT_URI_WITH_VOIP_CALLS)
  - [`CallLog.Calls.INCLUDE_VOIP_CALLS_PARAM_KEY`](https://developer.android.com/reference/android/provider/CallLog.Calls#INCLUDE_VOIP_CALLS_PARAM_KEY)

### Initiate callbacks from dialer app

To initiate a callback from a dialer, use [`TelecomManager.placeCall`](https://developer.android.com/reference/android/telecom/TelecomManager#placeCall(android.net.Uri,%20android.os.Bundle)). The
platform uses the unique `CallLog.Calls._ID` of the call log entry to launch
the correct VoIP app. This launch includes a
[`TelecomManager.ACTION_CALL_BACK`](https://developer.android.com/reference/android/telecom/TelecomManager#ACTION_CALL_BACK) intent, which is a system-defined action
for initiating a return call. This intent contains the call's `UUID` in
intent extra [`TelecomManager.EXTRA_UUID`](https://developer.android.com/reference/android/telecom/TelecomManager#EXTRA_UUID), allowing the VoIP app to identify
which specific call is being called back.


```kotlin
// Uri generated with unique ID of the call log entry to launch the respective VoIP app for callback
val address = ContentUris.withAppendedId(CallLog.Calls.CONTENT_URI, callId)

// extra information required to initiate callback
val extras = Bundle()

telecomManager.placeCall(address, extras)
```

<br />