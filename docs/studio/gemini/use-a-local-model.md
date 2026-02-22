---
title: https://developer.android.com/studio/gemini/use-a-local-model
url: https://developer.android.com/studio/gemini/use-a-local-model
source: md.txt
---

| **Preview:** Local models are available starting in Android Studio Otter 1 Canary 3. See the [preview release note](https://developer.android.com/studio/preview/features#use-a-local-model).

Large language models (LLMs) differ in their capabilities. To give you control
and flexibility in AI-assisted software development, Android Studio lets you
choose a local model, running on your personal machine, to power the IDE's AI
functionality.
| **Warning:** By using a third-party model, you agree to send your code and other input data to the provider of the model. Review the model provider's terms to understand how your data will be used. Note that some Android Studio features might not function as expected with external models.

## Choose a model

A local model offers an alternative to the LLM support built into Android
Studio; however, [Gemini in Android Studio](https://developer.android.com/gemini-in-android) typically provides the best AI
experience for Android developers because of the powerful [Gemini models](https://deepmind.google/models/gemini/). You
can select from a variety of Gemini models for your Android development tasks,
including the no-cost default model or models accessed with a paid [Gemini API
key](https://developer.android.com/studio/gemini/add-api-key).

Local model capability is a great option if you need to work offline, must
adhere to strict company policies on AI tool usage, or are interested in
experimenting with open-source research models.
| **Caution:** Local models typically offer lower performance compared to cloud-based Gemini models. You might experience less accurate responses, higher latency, and limited feature support. We recommend using [Gemini in Android Studio](https://developer.android.com/gemini-in-android) for the best experience.

## Set up local model support

1. Download and install the [latest canary version of Android Studio](https://developer.android.com/studio/preview).

2. Install an LLM provider such as [LM Studio](https://lmstudio.ai) or
   [Ollama](https://ollama.com) on your local computer.

3. Add the model provider to Android Studio.

   - Go to **Settings \> Tools \> AI \> Model Providers**
   - Select the add icon
   - Select **Local Provider**
   - Enter a description of the model provider (typically the model provider's name)
   - Set the port on which the provider is listening
   - Enable a model

   ![Android Studio settings dialog showing the Gemini section with an option to enable offline mode.](https://developer.android.com/static/studio/gemini/images/local-model-provider-settings.png) **Figure 1.** Model provider settings.
4. Download and install a model of your choice.

   See the [LM Studio](https://lmstudio.ai/models) and
   [Ollama](https://ollama.com/search) model catalogs. For the best experience
   with Agent Mode in Android Studio, select a model that has been trained for
   tool use.
   ![Android Studio settings dialog showing a list of available
   local models.](https://developer.android.com/static/studio/gemini/images/available-local-models.png) **Figure 2.** Available local models.
5. Start your inference environment.

   The inference environment serves your model to local applications. Configure
   a sufficiently large context length token window for optimal performance.
   For detailed instructions on starting and configuring your environment, see
   the [Ollama](https://github.com/ollama/ollama/blob/main/README.md#quickstart) or
   [LM Studio](https://lmstudio.ai/docs/app/basics) documentation.
6. Select a model.

   Open Android Studio. Navigate to the Gemini chat window. Use the model
   picker to switch from the default Gemini model to your configured local
   model.
   ![Android Studio Gemini chat window showing the model picker with options for Gemini and a local model.](https://developer.android.com/static/studio/gemini/images/local-model-picker.png) **Figure 3.** Model picker.

After you've connected Android Studio to your local model, you can use the chat
features within the IDE. All interactions are powered entirely by the model
running on your local machine, giving you a self-contained AI development
environment.

## Consider performance limitations

A local, offline model typically won't be as performant or intelligent as the
cloud-based Gemini models. Chat responses from local models are usually less
accurate and have higher latency compared to cloud-based models.

Local models are usually not fine-tuned for Android development, and local
models can return responses that are uninformed about the Android Studio user
interface. Some Android Studio AI features and Android development use cases are
nonfunctional with a local model. However, the AI chat feature in Android Studio
is generally supported by local models.

For fast, accurate responses on all aspects of Android development and support
for all Android Studio features, [Gemini in Android Studio](https://developer.android.com/gemini-in-android), powered by the
[Gemini models](https://deepmind.google/models/gemini/), is your best solution.