---
title: https://developer.android.com/develop/connectivity/cronet
url: https://developer.android.com/develop/connectivity/cronet
source: md.txt
---

# Perform network operations using Cronet

Cronet is the Chromium network stack made available to Android apps as a library. Cronet takes advantage of multiple technologies that reduce the latency and increase the throughput of the network requests that your app needs to work.

The Cronet Library handles the requests of apps used by millions of people on a daily basis, such as[YouTube](https://play.google.com/store/apps/details?id=com.google.android.youtube),[Google App](https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox),[Google Photos](https://play.google.com/store/apps/details?id=com.google.android.apps.photos), and[Maps - Navigation \& Transit](https://play.google.com/store/apps/details?id=com.google.android.apps.maps).

## Features

**Protocol support**
:   Cronet natively supports the[HTTP](https://tools.ietf.org/html/rfc2616),[HTTP/2](https://tools.ietf.org/html/rfc7540), and[HTTP/3 over QUIC](https://www.chromium.org/quic)protocols.

**Request prioritization**
:   The library allows you to set a priority tag for the requests. The server can use the priority tag to determine the order in which to handle the requests.

**Resource caching**
:   Cronet can use an in-memory or disk cache to store resources retrieved in network requests. Subsequent requests are served from the cache automatically.

**Asynchronous requests**
:   Network requests issued using the Cronet Library are asynchronous by default. Your worker threads aren't blocked while waiting for the request to come back.

**Data compression**
:   Cronet supports data compression using the[Brotli Compressed Data Format](https://tools.ietf.org/html/rfc7932).

To learn how to use the Cronet Library in your app for Android, see[Send a simple request](https://developer.android.com/develop/connectivity/cronet/start). You can also browse the[Cronet Sample](https://github.com/GoogleChromeLabs/cronet-sample)on GitHub.

You can send feedback about the Cronet Library using the[Chromium Issue Tracker](https://crbug.com). Check the list of bugs in the issue tracker to make sure that your issue hasn't already been reported. If your issue hasn't been reported, file a bug with the word*Cronet*in the summary line.