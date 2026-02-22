---
title: https://developer.android.com/studio/gemini/analyze-crashes-with-aqi
url: https://developer.android.com/studio/gemini/analyze-crashes-with-aqi
source: md.txt
---

# Analyze crashes with App Quality Insights and Gemini

Use Gemini in Android Studio to analyze your[App Quality Insights](https://developer.android.com/studio/debug/app-quality-insights)crash reports, generate insights, provide a crash summary, and (when possible) recommend next steps, including sample code and links to relevant documentation.

Generate all of this information by clicking**Insights** in the**App Quality Insights** tool window in Android Studio after you[enable Gemini](https://developer.android.com/studio/gemini/get-started).

![Show insights from Gemini from the App Quality Insights tool window](https://developer.android.com/static/studio/gemini/images/android-vitals.gif)

For example, when we click**Insights** in the**App Quality Insights** tool window for the depicted sample app and click the most common type of error, Gemini tells us that the app crashed due to a`java.lang`NullPointerException. It locates the file where the crash originated, shows the relevant code snippet, and walks through why the crash occurred step by step.
![Insights from Gemini in the App Quality Insights tool window](https://developer.android.com/static/studio/gemini/images/aqi-crash-analysis.png)

To fix the code that is causing the crash, click**Suggest a fix**and a code diff opens with Gemini's proposed code changes. You can further refine the prompt that produced the suggested code changes or edit the code yourself before accepting the changes.
![Gemini's suggested fix from the App Quality Insights tool window](https://developer.android.com/static/studio/gemini/images/aqi-suggest-a-fix.png)