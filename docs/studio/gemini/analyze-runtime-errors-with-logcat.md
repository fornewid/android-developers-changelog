---
title: https://developer.android.com/studio/gemini/analyze-runtime-errors-with-logcat
url: https://developer.android.com/studio/gemini/analyze-runtime-errors-with-logcat
source: md.txt
---

The agent helps you understand and resolve errors from the
[Logcat](https://developer.android.com/studio/debug/logcat) window, streamlining your debugging process. When
your app throws an error or exception, you can use the "Fix with AI" feature to
get immediate explanations and actionable suggestions without leaving the IDE.

1. Run your app and monitor the Logcat
   ![](https://developer.android.com/static/studio/images/logcat-icon.png)
   window. When an exception or error occurs, Android Studio provides the stack
   trace.

   ![Fix with AI option at the beginning of a Logcat stack trace](https://developer.android.com/static/studio/gemini/images/logcat-fix-with-ai.png) Fix with AI option at the beginning of a Logcat stack trace
2. Click the "Fix with AI" text that appears at the beginning of the stack
   trace. This action sends the relevant information to the agent for analysis.

3. The **Agent** tool window opens with a detailed response, which typically
   includes a summary of the error in plain language, potential causes, and
   suggested fixes.

   ![The agent explains the Logcat error](https://developer.android.com/static/studio/gemini/images/logcat-error-in-gemini-chat.png) The agent explains the Logcat error