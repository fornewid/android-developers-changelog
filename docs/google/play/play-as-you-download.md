---
title: https://developer.android.com/google/play/play-as-you-download
url: https://developer.android.com/google/play/play-as-you-download
source: md.txt
---

# Play as you Download

Built into the core of Android 12+, Play as you Download allows your users to get into the experience quickly after a small download while remaining assets are fetched in the background. To make this happen, Google Play analyzes crowdsourced first use file system access patterns and automatically identifies assets to optimize.

## Prepare your app

Even with the Play as you Download feature enabled, your users only receive the benefit once these prerequisites are met:

- App is distributed using the Android App Bundle format
- App has been updated to the current ads SDKs (if applicable)
- App has enough crowdsourced information about first use experiences
- App has first-use experiences that are suitable for the feature

Learn more about how to[optimize your app for Play as you Download](https://developer.android.com/google/play/play-as-you-download/best-practices).

## Enable your app

If you're using the Android App Bundle format and current ads SDKs, then you've done the work necessary to enable Play as you Download. By default, all apps are enabled. If you don't want to take advantage of this benefit, you can opt-out using the**Play as you Download**tab on the "Advanced settings" page of the Play Console.
| **Note:** Due to device eligibility, not all devices will receive the Play as you Download experience. For example, a device's operating system must be at least Android 12 and there are other technical requirements.

## Improve your results

Learn more about how to[optimize your app for Play as you Download](https://developer.android.com/google/play/play-as-you-download/best-practices).