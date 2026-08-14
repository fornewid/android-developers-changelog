---
title: https://developer.android.com/develop/connectivity/wifi/wifi-easy
url: https://developer.android.com/develop/connectivity/wifi/wifi-easy
source: md.txt
---

On Android 10 (API level 29) and higher devices, you can use Easy Connect to provision
Wi-Fi credentials to a peer device, as a replacement of WPS which was
deprecated in Android 9. Apps can integrate
Easy Connect into their setup and provisioning flow by using the
[`ACTION_PROCESS_WIFI_EASY_CONNECT_URI`](https://developer.android.com/reference/android/provider/Settings#ACTION_PROCESS_WIFI_EASY_CONNECT_URI)
intent. This intent requires a URI. The calling app can retrieve the URI through
various methods, including scanning a QR code from a sticker or display, or
through scanning Bluetooth LE or NFC advertisements.

Once the URI is available, you can provision the peer device's Wi-Fi credentials
with the `ACTION_PROCESS_WIFI_EASY_CONNECT_URI` intent. This allows the
user to select a Wi-Fi network to share and securely transfer the credentials.

Easy Connect does not require Location or Wi-Fi permissions.

> [!NOTE]
> **Note:** Before using this intent, the app *must* verify that Easy Connect is supported on the device by calling [`WifiManager.isEasyConnectSupported()`](https://developer.android.com/reference/android/net/wifi/WifiManager#isEasyConnectSupported()).