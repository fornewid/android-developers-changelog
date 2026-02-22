---
title: https://developer.android.com/studio/gemini/labs
url: https://developer.android.com/studio/gemini/labs
source: md.txt
---

We've heard feedback that developers want to access AI features in stable channels as soon as possible. You can now discover and try out the latest AI experimental features through the**Studio Labs**menu in the Settings menu starting with Narwhal stable release.

You can get a first look at AI experiments, share your feedback, and help us bring them into the IDE you use everyday. Go to the Studio Labs tab in Settings and enable the features you would like to start using. These AI features are automatically enabled in canary releases and no action is required.
![AI features in Studio Labs](https://developer.android.com/static/studio/gemini/images/studio-labs.png)AI features in Studio Labs

## Studio Labs features

### Compose preview generation with Gemini

Gemini can automatically generate Jetpack Compose preview code saving you time and effort. You can access this feature by right-clicking within a composable and navigating to**Gemini \> Generate Compose Preview** or**Generate Compose Preview for this file**, or by clicking the link in an empty preview panel. The generated preview code is presented in a diff view that lets you to quickly accept, edit, or reject the suggestions, providing a faster way to visualize your composables.
![Compose Preview generation with Gemini](https://developer.android.com/static/studio/gemini/images/compose-preview.png)Compose Preview generation with Gemini

### Transform UI with Gemini

Transform UI code within the Compose Preview environment using natural language directly in the preview. To use it, right-click in the Compose Preview and select**Transform UI With Gemini** . Then enter your natural language requests, such as "Center align these buttons," to guide Gemini in adjusting your layout or styling, or select specific UI elements in the preview for better context. Gemini will then edit your Compose UI code in place, which you can review and approve, speeding up the UI development workflow. To learn more, see[Transform UI](https://developer.android.com/studio/gemini/transform-ui).

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| !['Transform UI with Gemini' in context menu](https://developer.android.com/static/studio/gemini/images/transform-ui1.png)Accessing 'Transform UI with Gemini' menu | !['Transform UI with Gemini' modal dialog](https://developer.android.com/static/studio/gemini/images/transform-ui2.png)Applying a natural language transformation to a Compose preview |

### Journeys for Android Studio

[Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys)helps make end-to-end tests easier to write and maintain by letting you use natural language to describe the steps and assertions for each test---called a journey. By leveraging Gemini's vision and reasoning capabilities, steps written in natural language are converted into actions that Gemini performs on your app, making it both easy to write and understand your journeys. Additionally, you can write and describe more complex assertions, which Gemini evaluates based on what it sees on the device in order to determine whether your journeys pass or fail.  

And because Gemini reasons about which actions to perform to satisfy the goals, journeys are more resilient to subtle changes to your app's layout or behavior, resulting in fewer flaky tests when running against different versions of your app and different device configurations.

Write and run journeys right from Android Studio against any local or remote Android device. The IDE provides a new editor experience for crafting journeys as well as rich results that help you better follow Gemini's reasoning and execution of your journey.
| **Note:** Before you get started, make sure that you're signed into your developer account and have enabled Gemini in Android Studio.