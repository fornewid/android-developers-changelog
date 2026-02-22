---
title: https://developer.android.com/develop/connectivity/telecom/dialer-app/screen-calls
url: https://developer.android.com/develop/connectivity/telecom/dialer-app/screen-calls
source: md.txt
---

# Screen calls

Devices that run Android 10 (API level 29) or higher allow your app to identify calls from numbers that aren't in the user's address book as potential spam calls. Users can choose to have spam calls silently rejected. To provide greater transparency to users when they miss calls, information about these blocked calls is logged in the call log. Using the Android 10 API eliminates the requirement to obtain the[`READ_CALL_LOG`](https://developer.android.com/reference/android/Manifest.permission#READ_CALL_LOG)permission from the user in order to provide call screening and caller ID functionality.

You use a[`CallScreeningService`](https://developer.android.com/reference/android/telecom/CallScreeningService)implementation to screen calls. Call the[`onScreenCall()`](https://developer.android.com/reference/android/telecom/CallScreeningService#onScreenCall(android.telecom.Call.Details))function for any new incoming or outgoing calls when the number is not in the user's contact list. You can check the[`Call.Details`](https://developer.android.com/reference/android/telecom/Call.Details)object for information about the call. Specifically, the[`getCallerNumberVerificationStatus()`](https://developer.android.com/reference/android/telecom/Call.Details#getCallerNumberVerificationStatus())function includes information from the network provider about the other number. If the verification status failed, this is a good indication that the call is from an invalid number or a potential spam call.  

### Kotlin

```kotlin
class ScreeningService : CallScreeningService() {
    // This function is called when an ingoing or outgoing call
    // is from a number not in the user's contacts list
    override fun onScreenCall(callDetails: Call.Details) {
        // Can check the direction of the call
        val isIncoming = callDetails.callDirection == Call.Details.DIRECTION_INCOMING

        if (isIncoming) {
            // the handle (e.g. phone number) that the Call is currently connected to
            val handle: Uri = callDetails.handle

            // determine if you want to allow or reject the call
            when (callDetails.callerNumberVerificationStatus) {
                Connection.VERIFICATION_STATUS_FAILED -> {
                    // Network verification failed, likely an invalid/spam call.
                }
                Connection.VERIFICATION_STATUS_PASSED -> {
                    // Network verification passed, likely a valid call.
                }
                else -> {
                    // Network could not perform verification.
                    // This branch matches Connection.VERIFICATION_STATUS_NOT_VERIFIED.
                }
            }
        }
    }
}
```

### Java

```java
class ScreeningService extends CallScreeningService {
    @Override
    public void onScreenCall(@NonNull Call.Details callDetails) {
        boolean isIncoming = callDetails.getCallDirection() == Call.Details.DIRECTION_INCOMING;

        if (isIncoming) {
            Uri handle = callDetails.getHandle();

            switch (callDetails.getCallerNumberVerificationStatus()) {
                case Connection.VERIFICATION_STATUS_FAILED:
                    // Network verification failed, likely an invalid/spam call.
                    break;
                case Connection.VERIFICATION_STATUS_PASSED:
                    // Network verification passed, likely a valid call.
                    break;
                default:
                    // Network could not perform verification.
                    // This branch matches Connection.VERIFICATION_STATUS_NOT_VERIFIED
            }
        }
    }
}
```

Set the`onScreenCall()`function to call[`respondToCall()`](https://developer.android.com/reference/android/telecom/CallScreeningService#respondToCall(android.telecom.Call.Details,%20android.telecom.CallScreeningService.CallResponse))to tell the system how to respond to the new call. This function takes a[`CallResponse`](https://developer.android.com/reference/android/telecom/CallScreeningService.CallResponse)parameter that you can use to tell the system to block the call, reject it as if the user did, or silence it. You can also tell the system to skip adding this call to the device's call log altogether.  

### Kotlin

```kotlin
// Tell the system how to respond to the incoming call
// and if it should notify the user of the call.
val response = CallResponse.Builder()
    // Sets whether the incoming call should be blocked.
    .setDisallowCall(false)
    // Sets whether the incoming call should be rejected as if the user did so manually.
    .setRejectCall(false)
    // Sets whether ringing should be silenced for the incoming call.
    .setSilenceCall(false)
    // Sets whether the incoming call should not be displayed in the call log.
    .setSkipCallLog(false)
    // Sets whether a missed call notification should not be shown for the incoming call.
    .setSkipNotification(false)
    .build()

// Call this function to provide your screening response.
respondToCall(callDetails, response)
```

### Java

```java
// Tell the system how to respond to the incoming call
// and if it should notify the user of the call.
CallResponse.Builder response = new CallResponse.Builder();
// Sets whether the incoming call should be blocked.
response.setDisallowCall(false);
// Sets whether the incoming call should be rejected as if the user did so manually.
response.setRejectCall(false);
// Sets whether ringing should be silenced for the incoming call.
response.setSilenceCall(false);
// Sets whether the incoming call should not be displayed in the call log.
response.setSkipCallLog(false);
// Sets whether a missed call notification should not be shown for the incoming call.
response.setSkipNotification(false);

// Call this function to provide your screening response.
respondToCall(callDetails, response.build());
```

You must register the`CallScreeningService`implementation in the manifest file with the appropriate intent filter and permission so the system can trigger it correctly.  

    <service
        android:name=".ScreeningService"
        android:permission="android.permission.BIND_SCREENING_SERVICE">
        <intent-filter>
            <action android:name="android.telecom.CallScreeningService" />
        </intent-filter>
    </service>