---
title: https://developer.android.com/google/play/integrity/device-recall
url: https://developer.android.com/google/play/integrity/device-recall
source: md.txt
---

# Detect repeat abuse using device recall (beta)

| **Important:** Device recall is a new feature in Play Integrity API that is available in beta and subject to change. [Express interest](https://forms.gle/2d24B4gNyoVrqztG6) in joining the beta program.

This page describes how to use device recall to store and retrieve custom data
with specific devices. You can reliably recall the custom data again later when
your app is installed on the same device, even after the device is reset. This
lets you detect and prevent a device from being re-used based on an action or
behavior that you specify, while preserving user privacy.

## How does device recall work?

Device recall gives apps the ability to store and recall custom data associated
with a specific device in a way that preserves user privacy. The data is stored
on Google's servers, allowing your app to reliably recall your custom data even
after your app is reinstalled or the device is reset. For example, you could use
the feature to recall devices where you found evidence of severe abuse,
devices that already redeemed high-value items (such as a free trial), or
devices that are being used repeatedly to create new accounts for abusive
purposes. Device recall preserves user privacy because the requesting app can
only recall the limited data that it associated with devices, without accessing
any device or user identifiers. After you turn on device recall, you can do the
following:

- **Read per-device data** : You can read three custom values or *bits* for each device when you obtain an integrity verdict. You can define your own meaning to these values; for example, you can treat the values as three separate flags or you could combine them to represent eight custom labels.
- **Modify per-device data**: After you obtain an integrity token, you can use that token to make a server-side call to Google Play's server to modify one or more of the values. You have up to 14 days to use the token. This lets you modify a value if, for example, abuse only becomes evident in the two week period after you first perform an integrity check. When you modify a value, the month and year when the modification was made is also stored.

## Device recall prerequisites and considerations

Device recall may only be used to store and recall information to protect app
security and to mitigate abuse, fraud, and unauthorized access. You may not use
device recall to fingerprint or track individual users or devices and you may
not use device recall to keep track of sensitive user or device characteristics
like gender, age, or location data.

Device recall has the following prerequisites:

- Device recall can be used on phones, tablets, foldables, TV, Auto, and Wear OS. On Wear, device recall is only available on devices that ship with Wear OS 5 or higher. Device recall is not supported on emulators.
- Device recall requires recent versions of both Google Play Store and Google Play services to be installed and enabled on the device.
- Device recall requires the user account to be Play licensed, otherwise the verdict will be unevaluated.

Device recall has the following timing considerations:

- After you verify an integrity token, you have up to 14 days to use it to store custom device recall data.
- Device recall includes timestamps so that you can consider recently modified data as higher priority than data that was modified a long time ago. Consider ignoring or resetting the data after a long enough time period to take into account that devices can change hands or be refurbished and resold.
- The recall bits for a device will be stored for 3 years after the last read or write access.
- If you need to delete all data associated with a device, your app can reset all three values on that device to false. This will automatically reset the time stamps.

For developers with multiple apps and developers transferring apps, device
recall works as follows:

- All the apps in your Google Play developer account have access to the same three values per device. In other words, if one of your apps modifies one of the values, then all of your apps will read the modified value when they're installed on the same device.
- If an app is transferred from one developer account to another, device recall will reflect the new developer account's per-device data, not the old developer account's per-device data.

## Turn on device recall

| **Note:** To turn on device recall, you must first complete the [device recall beta
| interest form](https://forms.gle/2d24B4gNyoVrqztG6). Once approved, you will be able to turn on device recall in the Play Console.

When you are ready, turn on device recall in the Play Console:

1. Sign in to the Play Console.
2. Select the app that will use device recall.
3. In the **Release** section of the left menu, go to **App integrity**.
4. Next to Play Integrity API, click **Settings**.
5. In the Responses section of the page, click **Change responses**.
6. Turn Device recall on.
7. Click Save changes.

When you turn on or off device recall, any [Play Integrity API test
responses](https://developer.android.com/google/play/integrity/additional-tools#test-different) that you've
set up in the Play Console will be deleted and you will need to create them
again.

## Read device recall values

Device recall works in both Play Integrity API classic and standard requests. In
standard requests, device recall is refreshed in the warmup call. In other
words, after you modify per-device data, you will need to perform another warm
up to see the updated value. Once device recall is enabled, you will be able to
[read device recall values](https://developer.android.com/google/play/integrity/verdicts#device-recall) in your integrity verdicts.

## Modify device recall values

You can modify device recall values by making a server-to-server API call
similar to [decoding the integrity
verdict](https://developer.android.com/google/play/integrity/classic#decrypt-verify-google-servers). Setting
a bit to `true` will also update its write date (even if it was already `true`).
Setting a bit to `false` will reset its write date to empty. Any bits that are
unspecified in a request will remain unchanged. There is a small propagation
delay between writing bits and being able to read them back in the verdict. This
delay can be as long as 30 seconds, though it is generally much shorter. Device
recall write requests should be less frequent than your integrity token
requests. They are not counted in your integrity token request quota but are
subject to non-public, defensive rate limits.  

```
playintegrity.googleapis.com/v1/PACKAGE_NAME/deviceRecall:write -d \
'{
  "integrityToken": "INTEGRITY_TOKEN",
  "newValues": {
    "bitFirst": true,
    "bitThird": false
  }
}'
```
| **Note:** The integrity token should be validated during a user action (i.e. you should verify the nonce or request hash) and then used for writing recall bits. It will be valid for up to 14 days.
> **Tip:** If you are using the [Golang library for the Play Integrity API](https://pkg.go.dev/google.golang.org/api/playintegrity/v1), remember to add the field name to [ForceSendFields](https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields) when setting a bit value to false, as in the following snippet.  
>
>     newValues.BitFirst = true // ForceSendFields optional for value true
>     newValues.BitSecond = false // ForceSendFields required for value false
>     newValues.BitThird = nil // do not set ForceSendFields for unspecified bits
>     newValues.ForceSendFields = []string{"BitSecond"}