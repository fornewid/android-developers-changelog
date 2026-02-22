---
title: https://developer.android.com/about/versions/13/features/qrscanner
url: https://developer.android.com/about/versions/13/features/qrscanner
source: md.txt
---

# Android QR scanner with UPI support

Android 13 (with backwards compatibility for Android 12) supports UPI payment flows by adding a dedicated QR Code scanner that users can access directly from the corresponding Quick Settings tile. Users can launch a UPI payment flow by scanning a QR Code either from the live camera or from a static image.

![](https://developer.android.com/static/images/about/versions/13/upi-1.png)![](https://developer.android.com/static/images/about/versions/13/upi-2.png)![](https://developer.android.com/static/images/about/versions/13/upi-3.png)![](https://developer.android.com/static/images/about/versions/13/upi-4.png)

When multiple UPI apps are installed on a device, the user is presented with a disambiguation dialog. The payment flow then continues in the app selected by the user.

Note that the order of apps is not modified in any manner. Users' most frequently used apps are prioritized by the OS and displayed first, similar to the existing UPI intent dialog.

## Support UPI intents from Android QR scanner

When a payment app is launched via this flow, the calling package ID is set as**com.google.android.gms**. This value cannot be altered.

Payment apps need to**verify this source** and handle all the payment flows initiated from this package ID to be**treated as initiated by QR** and**set the initiation mode to QR when sending data to the payee's PSP**.

To distinguish between payments initiated from scanning a live QR Code (using the camera) and scanning a QR Code image (photo on device), the QR scanner passes an intent**extra**which helps identify the source of the QR Code.

Payment apps need to fetch the value of "intent**extra** " with the key`com.google.android.gms.UPI_QR_SOURCE`, and then compare with the following:

- `STATIC_IMAGE`string indicates that the source is a static image.
- `LIVE_CAMERA`string indicates that the source is the camera.

|--------------------------------------|----------------|----------------------------------------------|
| **Key**                              | **Value**      | **Explanation**                              |
| com.google.android.gms.UPI_QR_SOURCE | `STATIC_IMAGE` | QR code image stored on the device.          |
|                                      | `LIVE_CAMERA`  | QR code image captured live using the camera |