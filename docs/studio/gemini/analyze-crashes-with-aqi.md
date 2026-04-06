---
title: Analyze crashes with App Quality Insights and Gemini  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/gemini/analyze-crashes-with-aqi
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Analyze crashes with App Quality Insights and Gemini Stay organized with collections Save and categorize content based on your preferences.




Use Gemini in Android Studio to analyze your [App Quality Insights](/studio/debug/app-quality-insights) crash
reports, generate insights, provide a crash summary, and (when possible)
recommend next steps, including sample code and links to relevant documentation.

Generate all of this information by clicking **Insights** in the **App Quality
Insights** tool window in Android Studio after you [enable Gemini](/studio/gemini/get-started).

![Show insights from Gemini from the App Quality Insights tool window](/static/studio/gemini/images/android-vitals.gif)

For example, when we click **Insights** in the **App Quality Insights** tool
window for the depicted sample app and click the most common type of error,
Gemini tells us that the app crashed due to a `java.lang` NullPointerException.
It locates the file where the crash originated, shows the relevant code
snippet, and walks through why the crash occurred step by step.

![Insights from Gemini in the App Quality Insights tool window](/static/studio/gemini/images/aqi-crash-analysis.png)

To fix the code that is causing the crash, click **Suggest a fix** and a code
diff opens with Gemini's proposed code changes. You can further refine the
prompt that produced the suggested code changes or edit the code yourself
before accepting the changes.

![Gemini's suggested fix from the App Quality Insights tool window](/static/studio/gemini/images/aqi-suggest-a-fix.png)