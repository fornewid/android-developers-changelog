---
title: https://developer.android.com/studio/gemini/use-a-local-model
url: https://developer.android.com/studio/gemini/use-a-local-model
source: md.txt
---

Large language models (LLMs) differ in their capabilities. To give you control
and flexibility in AI-assisted software development, Android Studio lets you
choose a local model, running on your personal machine, to power the IDE's AI
functionality.

> [!WARNING]
> **Warning:** By using a third-party model, you agree to send your code and other input data to the provider of the model. Review the model provider's terms to understand how your data will be used. Note that some Android Studio features might not function as expected with external models.

## Choose a model

Using a local model is a great option if you need to work offline, must
adhere to strict company policies on AI tool usage, or are interested in
experimenting with open-source research models.

> [!CAUTION]
> **Caution:** Local models typically offer lower performance compared to cloud-based models. You might experience less accurate responses, higher latency, and limited feature support.

### Try the Gemma 4 model

If you need to use a local model, we recommend trying [Gemma 4](https://android-developers.googleblog.com/2026/04/android-studio-supports-gemma-4-local.html), a
state-of-the-art local model available for agentic coding in Android Studio.

The hardware requirements are as follows. We recommend using the Gemma 26B MoE
model if you have a high-performance machine.

| Model | Total RAM needed | Storage |
|---|---|---|
| Gemma E4B | 12 GB | 4 GB |
| Gemma 26B MoE | 24 GB | 17 GB |

See the [setup guide](https://developer.android.com/studio/gemini/use-a-local-model#set-up-local-model-support) for instructions on how to download and run Gemma 4
locally on your machine.

## Set up local model support

1. Download and install the [latest version of Android Studio](https://developer.android.com/studio/releases).

2. Install an LLM provider such as [LM Studio](https://lmstudio.ai) or
   [Ollama](https://ollama.com) on your local computer.

3. Add the model provider to Android Studio.

   - Go to **Settings \> Tools \> AI \> Model Providers**
   - Select the icon
   - Select **Local Provider**
   - Enter a description of the model provider (typically the model provider's name)
   - Set the port on which the provider is listening
   - Enable a model

   ![Android Studio settings dialog showing Model Providers under Tools > AI.](https://developer.android.com/static/studio/gemini/images/local-model-provider-settings.png) **Figure 1.** Model provider settings.
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

   Open Android Studio. Navigate to the **Agent** tool window. Use the model
   picker to switch from the default model to your configured local
   model.
   ![Android Studio Agent tool window showing the model picker.](https://developer.android.com/static/studio/gemini/images/local-model-picker.png) **Figure 3.** Model picker.

After you've connected Android Studio to your local model, you can use the chat
features within the IDE. All interactions are powered entirely by the model
running on your local machine, giving you a self-contained AI development
environment.

## Consider performance limitations

A local, offline model typically won't be as performant or intelligent as
cloud-based models. Chat responses from local models are usually less
accurate and have higher latency compared to cloud-based models.

Local models are usually not fine-tuned for Android development, and local
models can return responses that are uninformed about the Android Studio user
interface. Some Android Studio AI features and Android development use cases are
nonfunctional with a local model. However, the AI chat feature in Android Studio
is generally supported by local models.