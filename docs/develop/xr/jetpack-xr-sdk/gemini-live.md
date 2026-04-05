---
title: Integrate with the Gemini Live API for AI glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/gemini-live
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Integrate with the Gemini Live API for AI glasses Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

The [Gemini Live API](https://firebase.google.com/docs/ai-logic/live-api/) provides a comprehensive solution for
implementing conversational interfaces with your user. When building for Android
XR, you can integrate with the Gemini Live API through [Firebase AI
Logic](https://firebase.google.com/products/firebase-ai-logic). Unlike using [Text to Speech (TTS)](/develop/xr/jetpack-xr-sdk/asr) and [Automatic
Speech Recognition (ASR)](/develop/xr/jetpack-xr-sdk/asr), the Gemini Live API handles both audio input and
output in a seamless way. The Gemini Live API does require a persistent internet
connection, incur cost, supports a [limited number of concurrent connections per
project](https://firebase.google.com/docs/ai-logic/live-api/limits-and-specs)
and might not be ideal for handling error conditions or other critical user
communication, especially on AI glasses with no display.

In addition to supporting audio interfaces, you can also use the Gemini Live API
to build agentic experiences.

To get started with the Gemini Live API, follow along the steps outlined in the
[Gemini Live API guide](/ai/gemini/live). It walks you through instantiating and configuring a
[`LiveGenerativeModel`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel), establishing a
[`LiveSession`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) and creating custom
[`FunctionDeclaration`](https://firebase.google.com/docs/ai-logic/live-api?api=dev#function-calling) instances that allow your app to process
requests from Gemini.

[Previous

arrow\_back

Handle audio output using Text to Speech](/develop/xr/jetpack-xr-sdk/tts)