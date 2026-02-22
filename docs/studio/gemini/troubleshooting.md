---
title: https://developer.android.com/studio/gemini/troubleshooting
url: https://developer.android.com/studio/gemini/troubleshooting
source: md.txt
---

# Troubleshooting

If you encounter an issue with Gemini in Android Studio, go through the troubleshooting steps on this page for ideas on how to fix the issue and get better responses from Gemini.

Other resources:

- Check the[known issues](https://developer.android.com/studio/known-issues)to see if an issue that the Android Studio team is already aware of.
- If the issue persists, consider[filing a bug](https://developer.android.com/studio/report-bugs).

## Can't access any Gemini features

If you're in Android Studio and don't have access to any Gemini features, check the following:

- The Android Studio version you're using supports Gemini. For the most reliable experience, download the[latest stable version of Android Studio](https://developer.android.com/studio). Be aware of the[Android Studio and Cloud services compatibility policy](https://developer.android.com/studio/releases#service-compat).
- You are[logged in to Android Studio](https://developer.android.com/studio/intro#sign-in).

## Responses are low quality

If you find that Gemini's responses aren't as helpful as you'd expect, try the following:

- Help Gemini better understand the context for your question and identify the files that need to be updated by[attaching files to your query](https://developer.android.com/studio/gemini/attach-file).
- If you're using Gemini's standard chat feature, try[agent mode](https://developer.android.com/studio/gemini/agent-mode). Agent mode can tackle tasks that involve multiple files and goes beyond what chat alone can do.
- If you're already using agent mode, expand the context window by[adding an API key](https://developer.android.com/studio/gemini/add-api-key).
- Consider upgrading to the[business tier](https://developer.android.com/studio/gemini/get-started-businesses), which includes the Gemini 2.5 Pro model by default and lets you customize responses to better suit your team needs. For more information, see[Feature comparison](https://developer.android.com/studio/gemini/feature-comparison).

## Responses don't incorporate our team's style guide or policies

To help Gemini better understand your team's practices, such as a coding style guide or third party library preferences, create[rules](https://developer.android.com/studio/gemini/rules)for Gemini to take into account when responding to your prompts.