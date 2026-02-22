---
title: https://developer.android.com/ai/custom
url: https://developer.android.com/ai/custom
source: md.txt
---

# Use LiteRT on Android

LiteRT on Android provides essentials for deploying high performance, custom ML features into your Android app.

![Diagram illustrating the architecture of LiteRT, a framework for running machine learning models on Android devices. It shows the components involved, including the ML runtime, hardware acceleration delegates, and Google Play services.](https://developer.android.com/static/images/ml/litert-architecture.svg)

## LiteRT for ML runtime

Use LiteRT with Google Play services, Android's official ML inference runtime, to run high-performance ML inference in your app.[Learn more](https://ai.google.dev/edge/lite/android)

## Hardware Acceleration with LiteRT Delegates

Use LiteRT Delegates distributed using Google Play services to run accelerated ML on specialized hardware such as GPUs or NPUs. This helps you deliver more fluid, lower latency user experiences to your users by accessing advanced on-device compute capabilities.

We provide support for GPU delegates, and we're working with partners to provide access to their custom delegates using Google Play services to support advanced use cases.[Learn more](https://ai.google.dev/edge/lite/android/play_services#hardware-acceleration)

## Enabled by Google Play services

Use Google Play services to access the LiteRT runtime and delegates. This ensures use of the latest stable versions while minimizing impact to your app's binary size.[Learn more](https://ai.google.dev/edge/lite/android/play_services)

## Code samples

Review the LiteRT Android code samples and test ML features on your device.[Learn more](https://github.com/tensorflow/examples/tree/master/lite/examples)

## Get started with LiteRT

Download the example code and get started with LiteRT and Android.[Learn more](https://ai.google.dev/edge/lite/android)

## Acceleration Service

The Acceleration Service API lets you to safely pick the optimal hardware acceleration configuration at runtime without having to worry about the underlying device hardware and drivers.[Learn more](https://ai.google.dev/edge/lite/android/acceleration_service)