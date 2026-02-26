---
title: https://developer.android.com/ai/samples/socialite
url: https://developer.android.com/ai/samples/socialite
source: md.txt
---

![Animated screenshot showing the SociaLite chatbot in
action](https://developer.android.com/static/images/ai/socialite-ai-chat.gif)

The [SociaLite sample app](https://github.com/android/socialite) demonstrates how to use Android
platform APIs to implement features that are commonly deployed in social network
and communications apps. We have integrated the Gemini API using the Firebase AI
Logic SDK to demonstrate how chatbot capabilities can be implemented in your
own Android apps.

This sample code uses Gemini Flash which fast and cost-effective.
[Learn more about the Gemini models](https://firebase.google.com/docs/ai-logic/models). To implement an AI-driven chatbot in
the Socialite demo, we used the [*system instructions*](https://firebase.google.com/docs/ai-logic/system-instructions)
functionality of the Gemini API to modify the behavior of the model. In this
case, we use the prompt "Please respond to this chat conversation like a
friendly cat". This Gemini-infused version of SociaLite also uses the multimodal
capabilities of the model to let the chatbot react to images.

## Implement the Gemini API

The chatbot implementation is primarily located in the `ChatRepository` class.
The `GenerativeModel` class lets you interact with the Gemini API, which is
instantiated as follows:

    val generativeModel = GenerativeModel(
      // Set the model name to the latest Gemini model.
      modelName = "gemini-2.0-flash-lite-001",
      // Set a system instruction to set the behavior of the model.
      systemInstruction = content {
        text("Please respond to this chat conversation like a friendly cat.")
      },
    )

In a coroutine scope, initiate a chat by passing `pastMessages` to `startChat()`
to ensure that the model has access to conversation history. This gives your
chatbot the ability to maintain context and generate coherent responses that
build on previous exchanges.

    val pastMessages = getMessageHistory(chatId)
    val chat = generativeModel.startChat(
      history = pastMessages,
    )

Use the `sendMessage()` method to pass messages to the model.

## Test the AI chatbot

You can test it yourself by following these steps:

1. Check out the code for the [SociaLite sample app](https://github.com/android/socialite) and open it in Android Studio.
2. Set up a Firebase Project, connect your app to the *Gemini Developer API* by following [these steps](https://firebase.google.com/docs/ai-logic/get-started?platform=android&api=dev),
3. Replace google-services.json with your own \& Run `app` configuration,
4. Sync and run your app.
5. In the SociaLite app, tap **Settings** and then tap **AI Chatbot** so that the button label reads "*AI Chatbot: enabled*".

You are now ready to chat!

## Additional resources

[Learn more about the Firebase AI Logic SDK](https://developer.android.com/ai/gemini).