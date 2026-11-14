---
title: https://developer.android.com/develop/connectivity/cronet/lifecycle
url: https://developer.android.com/develop/connectivity/cronet/lifecycle
source: md.txt
---

> Documentation index: https://developer.android.com/develop/connectivity/cronet/llms.txt

Learn about the lifecycle of requests created using Cronet and how to manage
them using the callback methods provided by the library.

## Lifecycle overview

The [`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt) class represents network requests created using the Cronet
Library. The following concepts are important to understand the `UrlRequest`
lifecycle:

**States**
:   A state is the particular condition that the request is in at a specific time.
    `UrlRequest` objects created using the Cronet Library move through different
    states in their lifecycle. The request lifecycle includes an initial state,
    and multiple transitional and final states.

**`UrlRequest` methods**
:   Clients can call specific methods on `UrlRequest` objects depending on the
    state. The methods move the request from one state to another.

**`Callback` methods**
:   By implementing methods of the [`UrlRequest.Callback`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt) class, your app can
    receive updates about the progress of the request. You can implement the
    callback methods to call methods of the `UrlRequest` object that take the
    lifecycle from one state to another.

The following list describes the flow of the `UrlRequest` lifecycle:

1. The lifecycle is in the **Started** state after your app calls the [`start()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt#start()) method.
2. The server might send a redirect response, which takes the flow to the [`onRedirectReceived()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt#onRedirectReceived(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo,%20java.lang.String)) method. In this method, you can take one of the following client actions:
   - Follow the redirect using [`followRedirect()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt#followRedirect()). This method takes the request back to the **Started** state.
   - Cancel the request using [`cancel()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt#cancel()). This method takes the request to the [`onCanceled()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt#onCanceled(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo)) method where the app can perform additional operations before the request moves to the **Canceled** final state.
3. After the app follows all the redirects, the server sends the response headers and Cronet calls the [`onResponseStarted()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt#onResponseStarted(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo)) method. The request is in the **Waiting for read()** state. The app must call the [`read()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt#read(java.nio.ByteBuffer)) method to attempt to read part of the response body. After your app calls `read()`, the request is in the **Reading** state, where there are the following possible outcomes:
   - The reading action succeeds, and there is more data available. Cronet calls the [`onReadCompleted()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt#onReadCompleted(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo,%20java.nio.ByteBuffer)) method and the request is in the **Waiting for read()** state again. The app can call the [`read()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt#read(java.nio.ByteBuffer)) method again to continue reading the response body. The app can also stop reading the request by using the [`cancel()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.md.txt#cancel()) method.
   - The reading action succeeds, and there is no more data available. Cronet calls the [`onSucceeded()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt#onSucceeded(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo)) method and the request is in the **Succeeded** final state.
   - The reading action fails. Cronet calls the [`onFailed()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback.md.txt#onFailed(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo,%20org.chromium.net.CronetException)) method and the final state of the request is **Failed**.

The following diagram shows the lifecycle of a `UrlRequest` object:

![Cronet request lifecycle
diagram](https://developer.android.com/static/images/develop/connectivity/cronet-lifecycle.svg)  

The Cronet request lifecycle

| Legend |   |
|---|---|
| ![Cronet initial state legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-initial-state.svg) initial state | ![Cronet final state legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-final-state.svg) final state |
| ![Cronet transitional state legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-transitional-state.svg) transitional state | ![Cronet callback methods legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-callback-method.svg) callback methods |
| ![Cronet client action legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-client-action.svg) `UrlRequest` methods |   |