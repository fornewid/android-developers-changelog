---
title: https://developer.android.com/studio/gemini/add-api-key
url: https://developer.android.com/studio/gemini/add-api-key
source: md.txt
---

| **Note:** The ability to add your own API key is only applicable if you're using Gemini's free tier. Business users have access to Gemini 2.5 Pro by default.

The default Agent Mode in Android Studio has a no-cost daily quota with a limited context window. To expand the context window, you can add your own Gemini API key to take advantage of up to 1 million tokens with Gemini 3 Pro. To learn how to add an API key when using third-party models, see[Use a remote model](https://developer.android.com/studio/gemini/use-a-remote-model).

A larger context window lets you send more instructions, code, and attachments to Gemini, leading to even higher quality responses. This is especially useful when working with agents because the larger context provides Gemini 3 with the ability to reason about complex or long-running tasks.

To get a Gemini API key:

1. In Android Studio, go to**File (Android Studio** on macOS)**\> Settings \> Tools \> Gemini \> Model Providers** and click**Gemini**.
2. Click**Get a Gemini API key** to open[Google AI Studio](https://aistudio.google.com/)and retrieve or create your API key.
3. Enter your Gemini API key in the**API key** field. A list of models appears in**Available models**.
4. Select the models you want to enable. You can choose from the enabled models when you send a prompt.
5. Select**Apply** to apply the updates (click**OK**to apply the updates and immediately exit the settings).

![Add your own API key in the Gemini settings.](https://developer.android.com/static/studio/gemini/images/gemini-3-add-api-key-settings.png)

Be sure to safeguard your Gemini API key because[additional charges](https://aistudio.google.com/)apply for Gemini API usage associated with a personal API key. You can monitor your Gemini API key usage in AI Studio through**Usage and Limits**.