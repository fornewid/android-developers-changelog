---
title: https://developer.android.com/ai/custom
url: https://developer.android.com/ai/custom
source: md.txt
---

LiteRT on Android provides the essentials for deploying high-performance,
custom ML features into your Android app.

![LiteRT architecture on Android: your app and ML model run on the LiteRT
runtime and accelerators, which Google Play services delivers and which run
the model on the device CPU and GPU.](https://developer.android.com/static/images/ml/litert-play-services-architecture.svg)

## LiteRT for ML runtime

Use LiteRT in Google Play services, Android's official ML inference runtime, to
run high-performance ML inference in your app with the `CompiledModel` API.
[Learn more](https://developers.google.com/edge/litert/android/play_services)

## Hardware acceleration with LiteRT accelerators

Use LiteRT accelerators to run your models on the CPU or GPU. The GPU
accelerator runs models up to 1.4 times faster than the previous TensorFlow
Lite GPU delegate, so you can deliver more fluid, lower-latency experiences to
your users. [Learn more](https://developers.google.com/edge/litert/android/compiled_model_java#gpu)

NPU acceleration is available today in standalone LiteRT, and NPU support in
Google Play services is coming soon. [Learn more](https://developers.google.com/edge/litert/next/npu)

## Enabled by Google Play services

Google Play services delivers the LiteRT runtime and accelerators, so you don't
bundle them in your APK. Removing the bundled LiteRT runtime and GPU
accelerator saves up to \~8 MB of app size. Google Play services also keeps the
runtime up to date without an app release. [Learn more](https://developers.google.com/edge/litert/android/play_services#choose-api)

## Build with your AI coding agent

Use the LiteRT runtime skill with your coding agent, such as Agent Mode in
Android Studio, to add LiteRT to your app, run a model on the CPU or GPU, or
migrate an existing TensorFlow Lite app to LiteRT in Google Play services.
[Learn more](https://developer.android.com/agents/skills/device-ai/litert/litert-runtime/skill)

## Code samples

Explore the LiteRT Android code samples and test ML features on your device.
[Learn more](https://github.com/google-ai-edge/litert-samples)

## Get started with LiteRT

Add LiteRT in Google Play services to your app and run your first model.
[Learn more](https://developers.google.com/edge/litert/android/compiled_model_java)