---
title: Enhance your Android XR app with AI using Gemini  |  Android Developers
url: https://developer.android.com/develop/xr/gemini
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Enhance your Android XR app with AI using Gemini Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

[Android XR](https://www.android.com/xr/) is the first Android platform built in the Gemini
era, and it powers an ecosystem of headsets, glasses, and everything in between.
Gemini makes Android XR headsets easier to use and adds unique capabilities by
helping your users understand what they're seeing and taking actions on their
behalf.

You can access [Gemini APIs using Firebase AI Logic](https://firebase.google.com/docs/ai-logic), which is
available for both native Android apps (with Kotlin) and for Unity. Use these
APIs to build AI-powered features that integrate with cloud-based Gemini and
Imagen models.

## Choose a model

To get started, [compare the capabilities of each model](https://firebase.google.com/docs/ai-logic/models)
available in Firebase. You can then evaluate the results of various prompts for
different models in [AI Studio](https://aistudio.google.com/) to determine which model fits
your use case.

## Explore other ways to enhance your app with Gemini

After you've determined the model that fits your use case, consider these other
ways to enhance your app:

* **Provide a voice interface**: Android XR uses natural inputs like hands,
  gaze, and voice to navigate the system. To let your users navigate your app
  using their voice, use the [Gemini live API](/ai/gemini/live) along with
  [function calling](/ai/gemini/live#function).
* **Generate images with multimodal support**: generate images using Gemini or
  Imagen models with the [Gemini Developer API](/ai/gemini/developer-api).
* **Enrich game interactions in Unity apps**: Generate [structured
  output](https://firebase.google.com/docs/ai-logic/generate-structured-output?api=dev#generate-json-basic) using the [Gemini Developer API](/ai/gemini/developer-api) or [Vertex AI
  Gemini API](/ai/vertex-ai-firebase).