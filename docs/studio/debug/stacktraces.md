---
title: Analyze a stack trace  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/debug/stacktraces
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Analyze a stack trace Stay organized with collections Save and categorize content based on your preferences.




Debugging an app often requires working with stack traces. A stack trace generates when
your app crashes because of an error or an exception. You can also print a stack trace at any
point in your app code using methods such as
[`Thread.dumpStack()`](/reference/java/lang/Thread#dumpStack()).

While your app is running in debug mode on a connected device, Android Studio prints
and highlights stack traces in the **Logcat** view, as shown in
figure 1. A stack trace shows a list of method calls that lead to the exception being thrown,
together with the filenames and line numbers where the calls happened.

![](/static/studio/images/debug/logcat-stacktrace_2x.png)

**Figure 1.** A stack trace in Logcat.

Click on the highlighted filenames to open the files and examine the source of the method
invocation. Click the **Up the stack trace** ![](/static/studio/images/buttons/logcat-arrow-up.png)

## Open stack traces from external sources

Sometimes you want to analyze stack traces shared in a bug report instead of those you found
while debugging. To analyze data from
[Firebase Crashlytics](https://firebase.google.com/products/crashlytics), use the
[**App Quality Insights**](/studio/debug/app-quality-insights) tool
window. To analyze data from other sources, for example stack traces generated on your users'
devices from the Google Play Console, follow these steps:

1. Open your project in Android Studio.

   **Note:** Make sure the source code you're viewing is from the same
   version of your app that generated the stack trace. If the code is different, you will
   get mismatches between the filenames and line numbers or the order of calls in the stack
   trace and your project.
2. From the **Analyze** menu, click **Analyze Stacktrace**.

   ![Analyze Stack Trace window](/static/studio/images/debug/analyze-stacktrace_2-2_2x.png)

   **Figure 2.** Analyze Stacktrace window.
3. Paste the stack trace text into the **Analyze Stacktrace** window and click
   **OK**.

Android Studio opens a new **<Stacktrace>** tab, shown in figure 3, with the
stack trace you pasted under the **Run** window.

![Stacktrace window](/static/studio/images/debug/stacktrace-window_2x.png)

**Figure 3.** **<Stacktrace>** tab in Android Studio.

## Monitor the clipboard for new stack traces

To improve your productivity if you frequently work with external stack traces, you can let Android
Studio continuously monitor the system clipboard for new stack traces. To do so, follow these
steps:

1. Open the **Analyze Stacktrace** tool.
2. Select the **Automatically detect and analyze thread dumps copied to the clipboard outside
   of IntelliJ IDEA** checkbox.
3. Copy a stack trace in another application, such as a web browser, to the system clipboard.

When you return to the Android Studio window, the stack trace opens automatically under the
**Run** window, so you don't have to paste it into the **Analyze
Stacktrace** window.