---
title: https://developer.android.com/studio/gemini/attach-file
url: https://developer.android.com/studio/gemini/attach-file
source: md.txt
---

# Attach a file to your query

You can attach your project files as context in chat interactions with Gemini in Android Studio. This lets you quickly reference files in your prompts for Gemini, which helps Gemini identify the files that your query is about.

To attach a file to your query, in the Gemini chat input, type`@`to bring up a file completion menu. Search for the filename you want and select the file to attach it. You can attach multiple files in a single query.
![@File context in Gemini](https://developer.android.com/static/studio/gemini/images/file-context.png)

To un-attach a file, click the**Context** drop-down and press the "x" that appears when you hover over a file. To un-attach all files at once, click**Clear**.

Gemini also automatically suggests files to attach as context. To see which files were suggested by Gemini, click the**Context** drop-down and look under**Gemini suggestions**. To de-select or select a suggested file, use the checkbox next to the file.
![Files attached manually and suggested by Gemini](https://developer.android.com/static/studio/gemini/images/attached-files.png)