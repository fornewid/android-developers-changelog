---
title: https://developer.android.com/develop/xr/gemini
url: https://developer.android.com/develop/xr/gemini
source: md.txt
---

<br />


Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses)  
![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

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

- **Provide a voice interface** : Android XR uses natural inputs like hands, gaze, and voice to navigate the system. To let your users navigate your app using their voice, use the [Gemini live API](https://developer.android.com/ai/gemini/live) along with [function calling](https://developer.android.com/ai/gemini/live#function).
- **Generate images with multimodal support** : generate images using Gemini or Imagen models with the [Gemini Developer API](https://developer.android.com/ai/gemini/developer-api).
- **Enrich game interactions in Unity apps** : Generate [structured
  output](https://firebase.google.com/docs/ai-logic/generate-structured-output?api=dev#generate-json-basic) using the [Gemini Developer API](https://developer.android.com/ai/gemini/developer-api) or [Vertex AI
  Gemini API](https://developer.android.com/ai/vertex-ai-firebase).