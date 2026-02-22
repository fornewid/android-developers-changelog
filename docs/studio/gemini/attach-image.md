---
title: https://developer.android.com/studio/gemini/attach-image
url: https://developer.android.com/studio/gemini/attach-image
source: md.txt
---

# Attach an image to your query

| **Note:** Image attachment is available in Gemini's no-cost tier.

Attach an image to your query for Gemini in Android Studio to better understand an app's architecture and accelerate the UI development process.

To attach an image to your prompt, click**Attach Image File** ![Attach Image File icon](https://developer.android.com/static/studio/images/attach-image-file.png)and upload the image.

Here are just a few ways Gemini can help with images:

- If you have a mock-up of the UI you'd like, Gemini can provide the code that creates it. For example, if you provide Gemini a screenshot of the[Now in Android](https://github.com/android/nowinandroid)app, it can provide the Compose code to create it. This example shows a screenshot of the app's feed (left) and Gemini's generated Jetpack Compose code (right) for that UI. To learn more, see[Generate UI with image attachments](https://developer.android.com/studio/gemini/generate-ui-with-images).

  ![The 'Now in Android' app, showing a feed of articles with titles, topics, and bookmark icons.](https://developer.android.com/static/studio/images/nia-screenshot-2.png)![Gemini's code response displaying Jetpack Compose code that recreates the UI from the 'Now in Android' screenshot.](https://developer.android.com/static/studio/images/gias-response-2.png)Gemini generates Jetpack Compose code from a UI screenshot of the Now in Android app.
- If you want to learn how an app is constructed, Gemini can explain how the UI works in terms of its component parts. For example, you can ask Gemini to explain the composables and data flow behind another Now in Android screenshot. The left image shows a detail screen with a news item, and the right image displays Gemini's explanation of the Compose structure and data flow for that screen.

  ![A single news article detail in the 'Now in Android' app, showing a title, author, and description.](https://developer.android.com/static/studio/images/nia-screenshot-1.png)![Gemini's explanation of the Jetpack Compose composables and data flow for the news article detail screen.](https://developer.android.com/static/studio/images/gias-response-1.png)Gemini explains the UI composition and data flow of a specific app screen.
- If you have an app architecture diagram, Gemini can suggest code to create the app based on the diagram, serving as a full stack development assistant. Gemini can also help document the diagram and explain the construction of the app, which helps when writing a design doc for your teammates to review. For instance, the following image shows a simplified architecture diagram depicting data flow between various app components like UI, ViewModel, Repository, and Data Source.

  ![A simplified app architecture diagram showing UI, ViewModel, Repository, and Data Source components with arrows indicating data flow.](https://developer.android.com/static/studio/gemini/images/architecture-diagram.png)Gemini can generate code and documentation from an app architecture diagram.
- If you notice a UI bug, take a screenshot and ask Gemini to brainstorm solutions. You can help point out what's wrong by circling the area that has the error. The following example shows a screenshot of a mobile app with a red circle highlighting a misaligned UI element.

  ![A mobile app screenshot showing a UI bug where a text element is overlapping or misaligned, highlighted with a red circle.](https://developer.android.com/static/studio/gemini/images/ui-bug.png)Gemini can help brainstorm solutions for UI bugs from a screenshot.