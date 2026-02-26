---
title: https://developer.android.com/ai/overview
url: https://developer.android.com/ai/overview
source: md.txt
---

This guide is designed to help you integrate Google's generative artificial
intelligence and machine learning (AI/ML) solutions into your applications. It
provides guidance to help you navigate the various artificial intelligence and
machine learning solutions available and choose the one that best fits your
needs. The goal of this document is to help you determine which tool to use and
why, by focusing on your needs and use cases.

To assist you in selecting the most suitable AI/ML solution for your specific
requirements, [this document includes a solutions guide](https://developer.android.com/ai/overview#ai-solution-guide). By answering a
series of questions about your project's goals and constraints, the guide
directs you towards the most appropriate tools and technologies.

This guide helps you choose the best AI solution for your app. Consider these
factors: the type of data (text, images, audio, video), the task's complexity
(simple summarization to complex tasks needing specialized knowledge), and the
data size (short inputs versus large documents). This will help you decide
between using Gemini Nano on your device or Firebase's cloud-based AI (Gemini
Flash, Gemini Pro, or Imagen).
[![Decision flowchart for GenAI use cases. Criteria include Modality
(text, image versus audio, video, image generation), Complexity
(summarize, rewrite versus domain knowledge), and Context Window
(short input/output versus extensive documents/media), leading to
either On-device GenAI (Gemini Nano) or Firebase AI Logic (Gemini
Flash, Pro, Imagen).](https://developer.android.com/static/ai/assets/images/genai-use-cases.svg)](https://developer.android.com/ai/overview#ai-solution-guide) **Figure 1** : This illustration represents a high-level solutions guide to help you find the right AI/ML solution for your Android app. For a more detailed breakdown of your AI and ML options, refer to the [solutions guide](https://developer.android.com/ai/overview#ai-solution-guide) found later in this document.

## Harness the power of on-device inference

When you're adding AI and ML features to your Android app, you can choose
different ways to deliver them -- either on the device or using the cloud.

On-device solutions like Gemini Nano deliver results with no additional cost,
provide enhanced user privacy, and provide reliable offline functionality
because input data is processed locally. These benefits can be critical for
certain use cases, like message summarization, making on-device a priority when
choosing the right solutions.

**Gemini Nano** lets you run inference directly on an Android-powered
device. If you're working with text, images, or audio, start with [**ML Kit's
GenAI APIs**](https://developers.google.com/ml-kit/genai) for out-of-the-box solutions. The ML Kit GenAI APIs are
powered by Gemini Nano and fine-tuned for specific on-device tasks. The ML Kit
GenAI APIs are an ideal path to production for your apps due to their
higher-level interface and scalability. These APIs allow you to implement
use-cases to **summarize, proofread** , and **rewrite** text, generate
**image descriptions** , and perform **speech recognition**.

To move beyond the fundamental use cases provided by the ML Kit GenAI APIs,
consider [**Gemini Nano Experimental Access**](https://developer.android.com/ai/gemini-nano/experimental). Gemini Nano Experimental
Access gives you more direct access to custom prompting with Gemini Nano.

For traditional machine learning tasks, you have the flexibility to implement
your own custom models. We provide robust tools like [ML Kit](https://developer.android.com/ai/overview#ml-kit),
[MediaPipe](https://developer.android.com/ai/overview#mediapipe), [LiteRT](https://developer.android.com/ai/overview#litert), and [Google Play](https://developer.android.com/google/play/on-device-ai) delivery features to
streamline your development process.

For applications that require highly specialized solutions, you can use your own
custom model, such as [Gemma](https://ai.google.dev/gemma) or another model that is tailored
to your specific use case. Run your model directly on the user's device with
LiteRT, which provides pre-designed model architectures for optimized
performance.

You can also consider building a hybrid solution by leveraging both on-device
and cloud models.

Mobile apps commonly utilize local models for small text data, such as chat
conversations or blog articles. However, for larger data sources (like PDFs) or
when additional knowledge is required, a cloud-based solution with more powerful
Gemini models may be necessary.

## Integrate advanced Gemini models

Android developers can integrate Google's advanced generative AI capabilities,
including the powerful Gemini Pro, Gemini Flash, and Imagen models, into their
applications using the [Firebase AI Logic SDK](https://developer.android.com/ai/vertex-ai-firebase). This SDK is designed for
larger data needs and provides expanded capabilities and adaptability by
enabling access to these high-performing, multimodal AI models.

With the Firebase AI Logic SDK, developers can make client-side calls to
Google's AI models with minimal effort. These models, such as Gemini Pro and
Gemini Flash, run inference in the cloud and empower Android apps to process a
variety of inputs including image, audio, video, and text. Gemini Pro excels at
reasoning over complex problems and analyzing extensive data, while the Gemini
Flash series offers superior speed and a context window large enough for most
tasks.

## When to use traditional machine learning

While generative AI is useful for creating and editing content like text,
images, and code, many real-world problems are better solved using traditional
Machine Learning (ML) techniques. These established methods excel at tasks
involving prediction, classification, detection, and understanding patterns
within existing data, often with greater efficiency, lower computational cost,
and simpler implementation than generative models.

Traditional ML frameworks offer robust, optimized, and often more practical
solutions for applications focused on analyzing input, identifying features, or
making predictions based on learned patterns---rather than generating entirely new
output. Tools like Google's ML Kit, LiteRT, and MediaPipe provide powerful
capabilities tailored for these non-generative use cases, particularly in mobile
and edge computing environments.

### Kickstart your machine learning integration with ML Kit

ML Kit offers production-ready, mobile-optimized solutions for common machine
learning tasks, requiring no prior ML expertise. This easy-to-use mobile SDK
brings Google's ML expertise directly to your Android and iOS apps, allowing you
to focus on feature development instead of model training and optimization. ML
Kit provides prebuilt APIs and ready-to-use models for features like barcode
scanning, text recognition (OCR), face detection, image labeling, object
detection and tracking, language identification, and smart reply.

These models are typically optimized for on-device execution, ensuring low
latency, offline functionality, and enhanced user privacy as data often remains
on the device. Choose ML Kit to quickly add established ML features to your
mobile app without needing to train models or require generative output. It's
ideal for efficiently enhancing apps with "smart" capabilities using Google's
optimized models or by deploying custom TensorFlow Lite models.

Get started with our comprehensive guides and documentation at the [ML Kit
developer site](https://developers.google.com/ml-kit).

### Custom ML deployment with LiteRT

For greater control or to deploy your own ML models, use a custom ML stack
built on LiteRT and Google Play services. This stack provides the essentials for
deploying high-performance ML features. LiteRT is a toolkit optimized for
running TensorFlow models efficiently on resource-constrained mobile, embedded,
and edge devices, giving you the ability to run significantly smaller and faster
models that consume less memory, power, and storage. The LiteRT runtime is
highly optimized for various hardware accelerators (GPUs, DSPs, NPUs) on edge
devices, enabling low-latency inference.

Choose LiteRT when you need to efficiently deploy trained ML models (commonly
for classification, regression, or detection) on devices with limited
computational power or battery life, such as smartphones, IoT devices, or
microcontrollers. It's the preferred solution for deploying custom or standard
predictive models at the edge where speed and resource conservation are
paramount.

Learn more about [ML deployment with LiteRT](https://ai.google.dev/edge/litert).

### Build real-time perception into your apps with MediaPipe

MediaPipe provides open-source, cross-platform, and customizable machine
learning solutions designed for live and streaming media. Benefit from
optimized, prebuilt tools for complex tasks like hand tracking, pose
estimation, face mesh detection, and object detection, all enabling
high-performance, real-time interaction even on mobile devices.

MediaPipe's graph-based pipelines are highly customizable, allowing you to
tailor solutions for Android, iOS, web, desktop, and backend applications.
Choose MediaPipe when your application needs to understand and react instantly
to live sensor data, especially video streams, for use cases such as gesture
recognition, AR effects, fitness tracking, or avatar control---all focused on
analyzing and interpreting input.

Explore the solutions and start building with [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/guide.md).

## Choose an approach: On-device or cloud

When integrating AI/ML features into your Android app, a crucial early decision
is whether to perform processing directly on the user's device or in the cloud.
Tools like ML Kit, Gemini Nano, and TensorFlow Lite enable on-device
capabilities, while the Gemini cloud APIs with Firebase AI Logic can provide
powerful cloud-based processing. Making the right choice depends on a variety of
factors specific to your use case and user needs.

Consider the following aspects to guide your decision:

- **Connectivity and offline functionality**: If your application needs to function reliably without an internet connection, on-device solutions like Gemini Nano are ideal. Cloud-based processing, by its nature, requires network access.
- **Data privacy**: For use cases where user data must remain on the device for privacy reasons, on-device processing offers a distinct advantage by keeping sensitive information local.
- **Model capabilities and task complexity**: Cloud-based models are often significantly larger, more powerful, and updated more frequently, making them suitable for highly complex AI tasks or when processing larger inputs where higher output quality and extensive capabilities are paramount. Simpler tasks might be well-handled by on-device models.
- **Cost considerations**: Cloud APIs typically involve usage-based pricing, meaning costs can scale with the number of inferences or amount of data processed. On-device inference, while generally free from direct per-use charges, incurs development costs and can impact device resources like battery life and overall performance.
- **Device resources**: On-device models consume storage space on the user's device. It's also important to be aware of the device compatibility of specific on-device models, such as Gemini Nano, to ensure your target audience can use the features.
- **Fine-tuning and customization**: If you require the ability to fine-tune models for your specific use case, cloud-based solutions generally offer greater flexibility and more extensive options for customization.
- **Cross-platform consistency**: If consistent AI features across multiple platforms, including iOS, are critical, be mindful that some on-device solutions, like Gemini Nano, may not yet be available on all operating systems.

By carefully considering your use case requirements and the available options,
you can find the perfect AI/ML solution to enhance your Android app and deliver
intelligent and personalized experiences to your users.

*** ** * ** ***

## Guide to AI/ML solutions

This solutions guide can help you identify the appropriate developer tools for
integrating AI/ML technologies into your Android projects.

**What is the primary goal of the AI feature?**

- **A) Generating new content (text, image descriptions), or performing
  simple text processing (summarizing, proofreading, or rewriting text)?** → Go to [**Generative AI**](https://developer.android.com/ai/overview#g)
- **B) Analyzing existing data/input for prediction, classification,
  detection, understanding patterns, or processing real-time streams (like
  video/audio)?** → Go to [**Traditional ML \& Perception**](https://developer.android.com/ai/overview#t)

*** ** * ** ***

### Traditional ML and perception

You need to analyze input, identify features, or make predictions based on
learned patterns, rather than generating entirely new output.

**What specific task are you performing?**

- **A) Need quick integration of pre-built, common mobile ML features?** (e.g., barcode scanning, text recognition (OCR), face detection, image labeling, object detection and tracking, language ID, basic smart reply)
  - **→ Use: [ML Kit](https://developers.google.com/ml-kit)** (Traditional APIs)
  - *Why*: Easiest integration for established mobile ML tasks, often optimized for on-device use (low latency, offline, privacy).
- **B) Need to process *real-time streaming data* (like video or audio) for
  perception tasks?** (e.g., hand tracking, pose estimation, face mesh, Real-time object detection and segmentation in video)
  - **→ Use: [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/guide)**
  - *Why*: Framework specialized for high-performance, real-time perception pipelines on various platforms.
- **C) Need to efficiently run your *own custom-trained* ML model (e.g., for
  classification, regression, detection) on the device, prioritizing
  performance and low resource usage?**
  - **→ Use: [LiteRT](https://developer.android.com/ai/custom)** (TensorFlow Lite Runtime)
  - *Why*: Optimized runtime for deploying custom models efficiently on mobile and edge devices (small size, fast inference, hardware acceleration).
- **D) Need to *train your own custom ML model* for a specific task?**
  - **→ Use: [LiteRT](https://developer.android.com/ai/custom)** (TensorFlow Lite Runtime) + custom model training
  - *Why*: Provides the tools to train and deploy custom models, optimized for mobile and edge devices.
- **E) Need advanced content classification, sentiment analysis, or
  translation of *many* languages with high nuance?**
  - Consider if traditional ML models (potentially deployed using LiteRT or cloud) fit, or if advanced NLU requires generative models (return to Start, choose A). For cloud-based classification, sentiment, or translation:
  - **→ Use: Cloud-based solutions (e.g.,** [**Google Cloud Natural Language
    API**](https://cloud.google.com/natural-language), [**Google Cloud Translation
    API**](https://cloud.google.com/translate), **potentially accessed using a custom backend or
    [Vertex AI](https://cloud.google.com/vertex-ai))**. (Lower priority than on-device options if offline or privacy is key).
  - *Why*: Cloud solutions offer powerful models and extensive language support, but require connectivity and may incur costs.

*** ** * ** ***

### Generative AI

You need to create new content, summarize, rewrite, or perform complex
understanding or interaction tasks.

**Do you require the AI to function *offline* , need maximum *data privacy*
(keeping user data on-device), or want to *avoid cloud inference costs?***

- **A) Yes** , offline, maximum privacy, or no cloud cost is critical.
  - → Go to [**On-device generative AI**](https://developer.android.com/ai/overview#go)
- **B) No** , connectivity is available and acceptable, cloud capabilities and scalability are more important, or specific features require cloud.
  - → Go to [**Cloud generative AI**](https://developer.android.com/ai/overview#gc)

*** ** * ** ***

#### On-device generative AI (Using Gemini Nano)

*Caveats*: Requires compatible Android devices, limited iOS support, specific
token limits (1024 prompt, 4096 context), models are less powerful than cloud
counterparts.

**Does your use case *specifically* match the streamlined tasks offered by
the ML Kit GenAI APIs? (summarize text, proofread text, rewrite text,
generate image descriptions, or perform speech recognition) AND are the token
limits sufficient?**

- **A) Yes** :
  - **→ Use: ML Kit GenAI APIs (powered by Gemini Nano)**
  - *Why*: Easiest way to integrate specific, common generative tasks on-device, highest priority on-device solution.
- **B) No** (You need more flexible prompting or tasks beyond the specific ML Kit GenAI APIs, but still want on-device execution within Nano's capabilities):
  - **→ Use: Gemini Nano Experimental Access**
  - *Why*: Provides open prompting capabilities on-device for use cases beyond the structured ML Kit GenAI APIs, respecting Nano's limitations.

*** ** * ** ***

#### Cloud generative AI

Uses more powerful models, requires connectivity, usually involves
inference costs, offers wider device reach and easier cross-platform (Android
and iOS) consistency.

**What is your priority: Ease of integration within Firebase OR maximum
flexibility/control?**

- **A) Prefer easier integration, a managed API experience, and are likely
  using Firebase already?**
  - **→ Use: Firebase AI Logic SDK** → Go to [**Firebase AI Logic**](https://developer.android.com/ai/overview?tab=t.466um8gk14b7#bookmark=kix.lga3yghibwcu)
- **B) Need maximum flexibility, access to the widest range of models
  (including third-party/custom), advanced fine-tuning, and are willing to
  manage your own backend integration (more complex)?**
  - **→ Use: Gemini API with a Custom Cloud Backend (using Google Cloud
    Platform)**
  - *Why*: Offers the most control, broadest model access, and custom training options but requires significant backend development effort. Suitable for complex, large-scale, or highly customized needs.

(**You chose Firebase AI Logic SDK) What kind
of generative task and performance profile do you need?**

- **A) Need a balance of performance and cost, suitable for general text
  generation, summarization, or chat applications where speed is important?**
  - **→ Use: [Firebase AI Logic SDK with Gemini Flash](https://developer.android.com/ai/vertex-ai-firebase)**
  - *Why*: Optimized for speed and efficiency within the Vertex AI managed environment.
- **B) Need higher quality and capability for complex text generation,
  reasoning, advanced NLU, or instruction following?**
  - **→ Use: [Firebase AI Logic SDK with Gemini Pro](https://developer.android.com/ai/vertex-ai-firebase)**
  - *Why*: More powerful text model for demanding tasks, accessed through Firebase.
- **C) Need sophisticated *image generation* or advanced image
  understanding or manipulation based on text prompts?**
  - **→ Use: [Firebase AI Logic SDK with Imagen 3](https://developer.android.com/ai/imagen)**
  - *Why*: State-of-the-art image generation model accessed using the managed Firebase environment.