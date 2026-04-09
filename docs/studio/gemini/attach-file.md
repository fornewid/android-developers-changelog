---
title: Attach a file to your query  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/gemini/attach-file
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Attach a file to your query Stay organized with collections Save and categorize content based on your preferences.



You can attach your project files as context in chat interactions with Gemini in
Android Studio. This lets you quickly reference files in your prompts for
Gemini, which helps Gemini identify the files that your query is about.

To attach a file to your query, in the Gemini chat input, type `@` to bring up a
file completion menu. Search for the filename you want and select the file to
attach it. You can attach multiple files in a single query.

![@File context in Gemini](/static/studio/gemini/images/file-context.png)

To un-attach a file, click the **Context** drop-down and press the "x" that
appears when you hover over a file. To un-attach all files at once, click
**Clear**.

Gemini also automatically suggests files to attach as context. To see which
files were suggested by Gemini, click the **Context** drop-down and look under
**Gemini suggestions**. To de-select or select a suggested file, use the
checkbox next to the file.

![Files attached manually and suggested by Gemini](/static/studio/gemini/images/attached-files.png)