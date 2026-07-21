---
title: https://developer.android.com/google/play/age-signals/handle-errors
url: https://developer.android.com/google/play/age-signals/handle-errors
source: md.txt
---

If your app makes a Play Age Signals API request and the call fails, your app
receives an error code. These errors can happen for various reasons, such as the
Play Store app being out of date.

**Retry strategy**: In situations where the user is in session, we recommend
implementing a retry strategy with a maximum number of attempts as an exit
condition so that the error disrupts the user experience as little as possible.

The following table lists error codes for the Play Age Signals API.

| Code | Constant | Description | Retryable |
| -1 | API_NOT_AVAILABLE | The Play Age Signals API is not available. The Play Store app version installed on the device might be old. Ask the user to update the Play Store. | Yes |
| -2 | PLAY_STORE_NOT_FOUND | No Play Store app is found on the device. Ask the user to install or enable the Play Store. | Yes |
| -3 | NETWORK_ERROR | No available network is found. Ask the user to check for a connection. | Yes |
| -4 | PLAY_SERVICES_NOT_FOUND | Play Services is not available or its version is too old. Ask the user to install, update, or enable Play Services. | Yes |
| -5 | CANNOT_BIND_TO_SERVICE | Binding to the service in the Play Store has failed. This can be due to having an old Play Store version installed on the device or device memory is overloaded. Ask the user to update the Play Store app. Retry with an exponential backoff. | Yes |
| -6 | PLAY_STORE_VERSION_OUTDATED | The Play Store app needs to be updated. Ask the user to update the Play Store app. | Yes |
| -7 | PLAY_SERVICES_VERSION_OUTDATED | Play Services needs to be updated. Ask the user to update Play Services. | Yes |
| -8 | CLIENT_TRANSIENT_ERROR | There was a transient error in the client device. Implement a retry strategy with a maximum number of attempts as an exit condition. If the issue still doesn't resolve, ask the user to try again later. | Yes |
| -9 | APP_NOT_OWNED | The app was not installed by Google Play. Ask the user to get your app from Google Play. | No |
| -10 | SDK_VERSION_OUTDATED | The Play Age Signals SDK version is no longer supported. Ask the user to update your app to a later version that uses a recent version of the Play Age Signals SDK. | No |
| -100 | INTERNAL_ERROR | Unknown internal error. Implement a retry strategy with a maximum number of attempts as an exit condition. If the issue still doesn't resolve, ask the user to try again later. If it fails consistently, [contact Google Play Developer support](https://support.google.com/googleplay/android-developer/gethelp), include Play Age Signals API in the subject, and include as much technical detail as possible (such as a bug report). | No |
|---|---|---|---|