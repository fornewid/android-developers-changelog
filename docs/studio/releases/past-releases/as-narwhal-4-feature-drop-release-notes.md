---
title: https://developer.android.com/studio/releases/past-releases/as-narwhal-4-feature-drop-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-narwhal-4-feature-drop-release-notes
source: md.txt
---

# Android Studio Narwhal 4 Feature Drop | 2025.1.4 (October 2025)

The following are new features in Android Studio Narwhal 4 Feature Drop.

## New setting to open new projects with the Project view

There is a new setting to have new projects open in Project view by default. To enable the setting go to**File** (**Android Studio** on macOS)**\> Settings \> Advanced Settings \> Project View** and select**Set Project view as the default**.

## Gemini in Android Studio updates

Android Studio Narwhal 4 Feature Drop updates Gemini in Android Studio in the following ways:

- [Agent Mode](https://developer.android.com/studio/gemini/agent-mode)is stable and the default when you invoke Gemini.
- The**Chat** mode is now called**Ask**.
- You can drag or paste images from your clipboard into the chat field, making it easier to work with visuals.
- We support instructions in[`AGENTS.MD`files](https://developer.android.com/studio/gemini/agent-files)(in addition to`AGENT.md`files, an older standard).

## Android SDK Upgrade Assistant now supports Android 16 / API 36

The migration from Android 15 / API 35 to Android 16 / API 36 has been added to the Android SDK Upgrade Assistant. To get help migrating, go to**Tools \> Android SDK Upgrade Assistant**.

## Watch Face Format support in Android Studio

Android Studio Narwhal 4 Feature Drop improves the workflow for creating[watch faces](https://developer.android.com/training/wearables/watch-faces)by introducing editor support for the[Watch Face XML Format](https://developer.android.com/training/wearables/wff)to write, debug, and fine-tune your watch face designs directly within the IDE.
![](https://developer.android.com/static/studio/preview/features/images/declarative-watch-faces-support.gif)Android Studio added support for the Watch Face Format.

Android Studio lets you directly edit the XML files used in Watch Face Format. It now provides code completion for tags and attributes based on the official Watch Face Format schemas and live error validation that helps identify issues like missing required attributes. Android Studio also includes resource linking to quickly navigate to drawable resources and other referenced XML elements along with advanced syntax support for handling arithmetic expressions and data source references embedded in the XML. Finally, you can deploy watch faces directly from Android Studio.