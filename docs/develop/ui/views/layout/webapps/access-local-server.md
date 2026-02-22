---
title: https://developer.android.com/develop/ui/views/layout/webapps/access-local-server
url: https://developer.android.com/develop/ui/views/layout/webapps/access-local-server
source: md.txt
---

When developing web content for WebView, it can be helpful to serve content from a local web server on your development machine. If you access this local server from a WebView on a test device or emulator, you can quickly see your changes without deploying to a remote server. This page explains several ways to access a web server running on your host machine from a WebView.

## Set up reverse port forwarding with ADB

You can use the[Android Debug Bridge (adb)](https://developer.android.com/tools/adb), a command-line tool for communicating with your device, to set up reverse port forwarding. This feature lets your device or emulator access a web server running on`localhost`on your development machine.

`adb`has a`reverse`command that can forward requests on a specific port on the device to a different port on the host machine.

To use this feature, run the following command in your terminal:  

    adb reverse tcp:<var translate="no">DEVICE_PORT</var> tcp:<var translate="no">HOST_PORT</var>

Replace the following:

- <var translate="no">DEVICE_PORT</var>: The port on the device that your app's WebView connects to. For example, 8080.
- <var translate="no">HOST_PORT</var>: The port on your development machine where your web server is running. For example, 8080 or 3000.

**Example:**

If your local development server is running on`localhost:8080`on your development machine, you can forward requests from your device to it by running the following command:  

    adb reverse tcp:8080 tcp:8080

After running this command, you can point your app's WebView to`http://localhost:8080`on the device or emulator. The WebView can then connect to the web server running on`localhost:8080`on your development machine. This method works with both physical devices connected using USB and the Android Emulator.

## Use Chrome DevTools port forwarding

Chrome DevTools has its own port forwarding feature that you can use to forward requests from your device to your development machine.

1. Set up your device for debugging as described in[Debug using Chrome DevTools](https://developer.android.com/develop/ui/views/layout/webapps/debug-chrome-devtools).
2. On the`chrome://inspect`page, select**Port forwarding...**.
3. In the**Port**field, enter the port number on the Android device that you want to use to access your development machine.
4. In the**IP address and port**field, enter your development machine's web server address and port number.
5. Select the**Enable port forwarding**checkbox.
6. Select**Done**.

For example, if you enter`3000`in the**Port** field and`localhost:8000`in the**IP address and port** field, then when you point your WebView at`http://localhost:3000`it can access your development machine's web server listening on`localhost:8000`.

You can also use a custom domain name for your local web server. For instructions about how to do this, see[Access local servers and Chrome instances with port forwarding](https://developer.chrome.com/docs/devtools/remote-debugging/local-server#usb-port-forwarding).

## Connect using Android Emulator's pass-through IP address

The Android Emulator provides the special pass-through IP address`10.0.2.2`to connect to your development machine from your app. This method isn't recommended for WebView debugging because your WebView won't treat this IP address as a[secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts). As a result, many web platform features (such as Service Workers, Geolocation, and camera and microphone access) won't be available to your web app. The`adb reverse`and Chrome DevTools port forwarding methods described earlier don't have this problem because they let you point your WebView to the trusted hostname`localhost`.