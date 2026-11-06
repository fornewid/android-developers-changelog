---
title: https://developer.android.com/studio/gemini/troubleshooting
url: https://developer.android.com/studio/gemini/troubleshooting
source: md.txt
---

If you encounter an issue with AI in Android Studio, go through the
troubleshooting steps on this page for ideas on how to fix the issue and get
better responses from the agent.

Other resources:

- Check the [known issues](https://developer.android.com/studio/known-issues) to see if an issue that the Android Studio team is already aware of.
- If the issue persists, consider [filing a bug](https://developer.android.com/studio/report-bugs).

## Can't access any AI features

If you're in Android Studio and don't have access to any AI features,
check the following:

- The Android Studio version you're using supports agentic development. For the most reliable experience, download the [latest stable version of Android
  Studio](https://developer.android.com/studio). Be aware of the [Android Studio and Cloud services compatibility
  policy](https://developer.android.com/studio/releases#service-compat).
- You are [logged in to Android Studio](https://developer.android.com/studio/intro#sign-in).

## Responses are low quality

If you find that the agent's responses aren't as helpful as you'd expect, try
the following:

- Help the agent better understand the context for your question and identify the files that need to be updated by [attaching files to your query](https://developer.android.com/studio/gemini/attach-file).
- Expand the context window by [adding an API key](https://developer.android.com/studio/gemini/add-api-key).
- If you're using Gemini models, consider upgrading to [Gemini Enterprise](https://developer.android.com/studio/gemini/get-started-businesses), which includes access to premium models by default and lets you customize responses to better suit your team needs. For more information, see [Feature
  comparison](https://developer.android.com/studio/gemini/feature-comparison).

## Responses don't incorporate our team's style guide or policies

To help the agent better understand your team's practices, such as a coding
style guide or third party library preferences, create [rules](https://developer.android.com/studio/gemini/rules) for the agent
to take into account when responding to your prompts.