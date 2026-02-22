---
title: https://developer.android.com/develop/connectivity/cronet/lifecycle
url: https://developer.android.com/develop/connectivity/cronet/lifecycle
source: md.txt
---

# Cronet request lifecycle

Learn about the lifecycle of requests created using Cronet and how to manage them using the callback methods provided by the library.

## Lifecycle overview

Network requests created using the Cronet Library are represented by the[`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)class. The following concepts are important to understand the[`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)lifecycle:

**States**
:   A state is the particular condition that the request is in at a specific time.[UrlRequest](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)objects created using the Cronet Library move through different states in their lifecycle. The request lifecycle includes an initial state, and multiple transitional and final states.

**`UrlRequest`methods**
:   Clients can call specific methods on[`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)objects depending on the state. The methods move the request from one state to another.

**`Callback`methods**
:   By implementing methods of the[`UrlRequest.Callback`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback)class, your app can receive updates about the progress of the request. You can implement the callback methods to call methods of the[`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)object that take the lifecycle from a state to another.

The following list describes the flow of the[`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)lifecycle:

1. The lifecycle is in the**Started** state after your app calls the[`start()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest#start())method.
2. The server could send a redirect response, which takes the flow to the[`onRedirectReceived()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback#onRedirectReceived(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo,%20java.lang.String))method. In this method, you can take one of the following client actions:
   - Follow the redirect using[`followRedirect()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest#followRedirect()). This method takes the request back to the**Started**state.
   - Cancel the request using[`cancel()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest#cancel()). This method takes the request to the[`onCanceled()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback#onCanceled(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo))method where the app can perform additional operations before the request is moved to the**Canceled**final state.
3. After the app follows all the redirects, the server sends the response headers and the[`onResponseStarted()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback#onResponseStarted(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo))method is called. The request is in the**Waiting for read()** state. The app should call the[`read()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest#read(java.nio.ByteBuffer))method to attempt to read part of the response body. After`read()`is called, the request is in the**Reading** state, where there are the following possible outcomes:
   - The reading action was successful, but there is more data available. The[`onReadCompleted()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback#onReadCompleted(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo,%20java.nio.ByteBuffer))is called and the request is in the**Waiting for read()** state again. The app should call the[`read()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest#read(java.nio.ByteBuffer))method again to continue reading the response body. The app could also stop reading the request by using the[`cancel()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest#cancel())method .
   - The reading action was successful, and there is no more data available. The[`onSucceeded()`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback#onSucceeded(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo))method is called and the request is now in the**Succeeded**final state.
   - The reading action failed. The[`onFailed`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest.Callback#onFailed(org.chromium.net.UrlRequest,%20org.chromium.net.UrlResponseInfo,%20org.chromium.net.CronetException))method is called and the final state of the request is now**Failed**.

The following diagram shows the lifecycle of a[`UrlRequest`](https://developer.android.com/develop/connectivity/cronet/reference/org/chromium/net/UrlRequest)object:

![Cronet request lifecycle diagram](https://developer.android.com/static/images/develop/connectivity/cronet-lifecycle.svg)  
The Cronet request lifecycle

|                                                                           Legend                                                                           |                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Cronet initial state legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-initial-state.svg)initial state                | ![Cronet final state legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-final-state.svg)final state               |
| ![Cronet transitional state legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-transitional-state.svg)transitional state | ![Cronet callback methods legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-callback-method.svg)callback methods |
| ![Cronet client action legend icon](https://developer.android.com/static/images/develop/connectivity/cronet-client-action.svg)`UrlRequest`methods          |                                                                                                                                                     |