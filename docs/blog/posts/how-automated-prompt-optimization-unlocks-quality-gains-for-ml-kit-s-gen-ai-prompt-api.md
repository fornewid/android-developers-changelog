---
title: https://developer.android.com/blog/posts/how-automated-prompt-optimization-unlocks-quality-gains-for-ml-kit-s-gen-ai-prompt-api
url: https://developer.android.com/blog/posts/how-automated-prompt-optimization-unlocks-quality-gains-for-ml-kit-s-gen-ai-prompt-api
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# How Automated Prompt Optimization Unlocks Quality Gains for ML Kit's GenAI Prompt API

###### 3-min read

![](https://developer.android.com/static/blog/assets/Prompt_API_Banner_1_ff0c780828_1kyTTw.webp) 28 Jan 2026 4 Authors

##### [Chetan Tekur,](https://developer.android.com/blog/authors/chetan-tekur)
[Chao Zhao,](https://developer.android.com/blog/authors/chao-zhao)
[Paul Zhou,](https://developer.android.com/blog/authors/paul-zhou)
[Caren Chang](https://developer.android.com/blog/authors/caren-chang)

## **Automated Prompt Optimization (APO)**

To further help bring your ML Kit Prompt API use cases to production, we are excited to announce [Automated Prompt Optimization (APO) targeting On-Device models on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/zero-shot-optimizer#optimizing_for_smaller_models). Automated Prompt Optimization is a tool that helps you automatically find the optimal prompt for your use cases.

The era of On-Device AI is no longer a promise---it is a production reality. With the release of **Gemini Nano v3** , we are placing unprecedented language understanding and multimodal capabilities directly into the palms of users. Through the Gemini Nano family of models, we have wide coverage of supported devices across the Android Ecosystem. But for developers building the next generation of intelligent apps, access to a powerful model is only step one. The real challenge lies in **customization**: How do you tailor a foundation model to expert-level performance for your specific use case without breaking the constraints of mobile hardware?

In the server-side world, the larger LLMs tend to be highly capable and require less domain adaptation. Even when needed, more advanced options such as LoRA (Low-Rank Adaptation) fine-tuning can be feasible options. However, the unique architecture of Android AICore prioritizes a **shared, memory-efficient system model**. This means that deploying custom LoRA adapters for every individual app comes with challenges on these shared system services.

But there is an alternate path that can be equally impactful. By leveraging **Automated Prompt Optimization (APO)** on Vertex AI, developers can achieve quality approaching fine-tuning, all while working seamlessly within the native Android execution environment. By focusing on superior system instruction, APO enables developers to tailor model behavior with greater robustness and scalability than traditional fine-tuning solutions.

**Note:** Gemini Nano V3 is a quality optimized version of the highly acclaimed [Gemma 3N](https://developers.googleblog.com/en/introducing-gemma-3n/) model. Any prompt optimizations that are made on the open source Gemma 3N model will apply to Gemini Nano V3 as well. On [supported devices](https://developers.google.com/ml-kit/genai#prompt-device), ML Kit GenAI APIs leverage the nano-v3 model to maximize the quality for Android Developers
![APO block diagram.jpg](https://developer.android.com/static/blog/assets/APO_block_diagram_a8538372af_5sQmK.webp)

APO treats the prompt not as a static text, but as a programmable surface that can be optimized. It leverages server-side models (like Gemini Pro and Flash) to propose prompts, evaluate variations and find the optimal one for your specific task. This process employs three specific technical mechanisms to maximize performance:

1. **Automated Error Analysis:** APO analyzes error patterns from training data to Automatically identify specific weaknesses in the initial prompt.
2. **Semantic Instruction Distillation:** It analyzes massive training examples to distill the "true intent" of a task, creating instructions that more accurately reflect the real data distribution.
3. **Parallel Candidate Testing:** Instead of testing one idea at a time, APO generates and tests numerous prompt candidates in parallel to identify the global maximum for quality.

## Why APO Can Approach Fine Tuning Quality

It is a common misconception that fine-tuning always yields better quality than prompting. For modern foundation models like Gemini Nano v3, prompt engineering can be impactful by itself:

- **Preserving General capabilities:** Fine-tuning ( PEFT/LoRA) forces a model's weights to over-index on a specific distribution of data. This often leads to "catastrophic forgetting," where the model gets better at your specific syntax but worse at general logic and safety. APO leaves the weights untouched, preserving the capabilities of the base model.
- **Instruction Following \& Strategy Discovery:** Gemini Nano v3 has been rigorously trained to follow complex system instructions. APO exploits this by finding the *exact* instruction structure that unlocks the model's latent capabilities, often discovering strategies that might be hard for human engineers to find.

To validate this approach, we evaluated APO across diverse production workloads. Our validation has shown consistent **5-8% accuracy gains** across various use cases.Across multiple deployed on-device features, APO provided significant quality lifts.

|---|---|---|---|---|
| **Use Case** | **Task Type** | **Task Description** | **Metric** | **APO Improvement** |
| **Topic classification** | Text classification | Classify a news article into topics such as finance, sports, etc | Accuracy | **+5%** |
| **Intent classification** | Text classification | Classify a customer service query into intents | Accuracy | **+8.0%** |
| **Webpage translation** | Text translation | Translate a webpage from English to a local language | BLEU | **+8.57%** |

## A Seamless, End-to-End Developer Workflow

It is a common misconception that fine-tuning always yields better quality than prompting. For modern foundation models like Gemini Nano v3, prompt engineering can be impactful by itself:

- **Preserving General capabilities:** Fine-tuning ( PEFT/LoRA) forces a model's weights to over-index on a specific distribution of data. This often leads to "catastrophic forgetting," where the model gets better at your specific syntax but worse at general logic and safety. APO leaves the weights untouched, preserving the capabilities of the base model.
- **Instruction Following \& Strategy Discovery:** Gemini Nano v3 has been rigorously trained to follow complex system instructions. APO exploits this by finding the *exact* instruction structure that unlocks the model's latent capabilities, often discovering strategies that might be hard for human engineers to find.

To validate this approach, we evaluated APO across diverse production workloads. Our validation has shown consistent **5-8% accuracy gains** across various use cases.Across multiple deployed on-device features, APO provided significant quality lifts.

## Conclusion

The release of **Automated Prompt Optimization (APO)** marks a turning point for on-device generative AI. By bridging the gap between foundation models and expert-level performance, we are giving developers the tools to build more robust mobile applications. Whether you are just starting with **Zero-Shot Optimization** or scaling to production with **Data-Driven** refinement, the path to high-quality on-device intelligence is now clearer. Launch your on-device use cases to production today with ML Kit's Prompt API and Vertex AI's Automated Prompt Optimization.

Relevant links:

- [ML Kit Prompt API](https://developers.google.com/ml-kit/genai/prompt/android/get-started),
- [Vertex AI Prompt Optimizer documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer)
- [Gemma 3N Announcement Blog](https://developers.googleblog.com/en/introducing-gemma-3n/)

###### Written by:

-

  ## [Chetan Tekur](https://developer.android.com/blog/authors/chetan-tekur)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/chetan-tekur) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
-

  ## [Chao Zhao](https://developer.android.com/blog/authors/chao-zhao)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/chao-zhao) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
-

  ## [Paul Zhou](https://developer.android.com/blog/authors/paul-zhou)

  ###### Senior Staff Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/paul-zhou) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
-

  ## [Caren Chang](https://developer.android.com/blog/authors/caren-chang)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/caren-chang) ![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp) ![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang)[![](https://developer.android.com/static/blog/assets/David_Chou_226df78370_tqGIk.webp)](https://developer.android.com/blog/authors/david-chou) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/announcing_gemma4_aicore_ce479292b9_Z15e7FP.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Announcing Gemma 4 in the AICore Developer Preview](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview)

  [arrow_forward](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview) At Google, we're committed to bringing the most capable AI models directly to the Android devices in your pocket. Today, we're thrilled to announce the release of our latest state-of-the-art open model: Gemma 4.

  ###### [Caren Chang](https://developer.android.com/blog/authors/caren-chang), [David Chou](https://developer.android.com/blog/authors/david-chou) •
  3 min read

- 3 Authors 30 Oct 2025 30 Oct 2025 ![](https://developer.android.com/static/blog/assets/kakao_8769e675f9_Z1GfWxl.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [ML Kit's Prompt API: Unlock Custom On-Device Gemini Nano Experiences](https://developer.android.com/blog/posts/ml-kit-s-prompt-api-unlock-custom-on-device-gemini-nano-experiences)

  [arrow_forward](https://developer.android.com/blog/posts/ml-kit-s-prompt-api-unlock-custom-on-device-gemini-nano-experiences) AI is making it easier to create personalized app experiences that transform content into the right format for users. We previously enabled developers to integrate with Gemini Nano through ML Kit GenAI APIs tailored for specific use cases like summarization and image description.

  ###### [Caren Chang](https://developer.android.com/blog/authors/caren-chang), [Chengji Yan](https://developer.android.com/blog/authors/chengji-yan), [Penny Li](https://developer.android.com/blog/authors/penny-li) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)