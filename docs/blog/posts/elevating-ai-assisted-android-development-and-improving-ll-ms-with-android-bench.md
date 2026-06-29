---
title: https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench
url: https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Elevating AI-assisted Android development and improving LLMs with Android Bench

2-min read ![](https://developer.android.com/static/blog/assets/android_Bench_f2e4dd4fda_2816Hg.webp) 05 Mar 2026 [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) Vice President, Product Management, Android Developer We want to make it faster and easier for you to build high-quality Android apps, and one way we're helping you be more productive is by putting AI at your fingertips. We know you want AI that truly understands the nuances of the Android platform, which is why we've been measuring how LLMs perform Android development tasks. Today we released the first version of [**Android Bench**](http://d.android.com/bench), our official leaderboard of LLMs for Android development.

Our goal is to provide model creators with a benchmark to evaluate LLM capabilities for Android development. By establishing a clear, reliable baseline for what high quality Android development looks like, we're helping model creators identify gaps and accelerate improvements---which empowers developers to work more efficiently with a wider range of helpful models to choose for AI assistance---which ultimately will lead to higher quality apps across the Android ecosystem.

#### **Designed with real-world Android development tasks**

We created the benchmark by curating a task set against a range of common Android development areas. It is composed of real challenges of varying difficulty, sourced from public GitHub Android repositories. Scenarios include resolving breaking changes across Android releases, domain-specific tasks like networking on wearables, and migrating to the latest version of Jetpack Compose, to name a few.

Each evaluation attempts to have an LLM fix the issue reported in the task, which we then verify using unit or instrumentation tests. This model-agnostic approach allows us to measure a model's ability to navigate complex codebases, understand dependencies, and solve the kind of problems you encounter every day.

We validated this methodology with several LLM makers, including JetBrains.

"*Measuring AI's impact on Android is a massive challenge, so it's great to see a framework that's this sound and realistic. While we're active in benchmarking ourselves, Android Bench is a unique and welcome addition. This methodology is exactly the kind of rigorous evaluation Android developers need right now."*   
- Kirill Smelov, Head of AI Integrations at JetBrains.

#### **The first Android Bench results**

For this initial release, we wanted to purely measure model performance and not focus on agentic or tool use. The models were able to successfully complete 16-72% of the tasks. This is a wide range that demonstrates some LLMs already have a strong baseline for Android knowledge, while others have more room for improvement. Regardless of where the models are at now, we're anticipating continued improvement as we encourage LLM makers to enhance their models for Android development.

The LLM with the highest average score for this first release is Gemini 3.1 Pro, followed closely by Claude Opus 4.6. You can try all of the models we evaluated for AI assistance for your Android projects by using API keys in the latest stable version of [Android Studio](http://d.android.com/studio).
![androidBench2.png](https://developer.android.com/static/blog/assets/android_Bench2_dd8df6c7df_Z6fYXi.webp)

#### **Providing developers and LLM makers with transparency**

We value an open and transparent approach, so we made [our methodology](http://d.android.com/bench/methodology), dataset, and test harness [publicly available on GitHub](https://github.com/android-bench/android-bench).

One challenge for any public benchmark is the risk of data contamination, where models may have seen evaluation tasks during their training process. We have taken measures to ensure our results reflect genuine reasoning rather than memorization or guessing, including a thorough manual review of agent trajectories, or the integration of a canary string to discourage training.

Looking ahead, we will continue to evolve our methodology to preserve the integrity of the dataset, while also making improvements for future releases of the benchmark---for example, growing the quantity and complexity of tasks.

We're looking forward to how [Android Bench](http://d.android.com/bench) can improve AI assistance long-term. Our vision is to close the gap between concept and quality code. We're building the foundation for a future where no matter what you imagine, you can build it on Android.
Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)
Continue reading
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [17 Things to know for Android developers at Google I/O!](https://developer.android.com/blog/posts/17-things-to-know-for-android-developers-at-google-i-o)

  [arrow_forward](https://developer.android.com/blog/posts/17-things-to-know-for-android-developers-at-google-i-o) Google I/O '26 features 17 key announcements for Android developers focusing on agent-led productivity, Compose First as our UI standard, and high-performance media and adaptive development for the expanding ecosystem.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 8 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 12 May 2026 12 May 2026 ![](https://developer.android.com/static/blog/assets/Tas_Developers_cut_Strapi_3636223c9c_Z2pmmBN.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building for the Intelligence System on Android](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android) Announced today during The Android Show, Android is transitioning from an operating system to an intelligence system, creating more opportunities for engagement with your apps.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android) Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 2 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)