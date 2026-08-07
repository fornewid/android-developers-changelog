---
title: https://developer.android.com/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench
url: https://developer.android.com/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Evolving how LLMs are measured for Android: the next era of Android Bench

3 min read ![](https://developer.android.com/static/blog/assets/Bench_July_releas_V01_Strapi_6ee24bdb6b_1NrCN7.webp) 08 Jul 2026 [![View Zoe Lopez-Latorre 's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_07_07_at_1_15_58_PM_eb87f2f61a_Z1QyLll.webp)](https://developer.android.com/blog/authors/zoe-lopez-latorre) [Zoe Lopez-Latorre](https://developer.android.com/blog/authors/zoe-lopez-latorre) Senior Developer Relations Engineer, Android Back in March, we introduced [Android Bench](http://d.android.com/bench)---our LLM leaderboard for real-world Android development tasks. Our goal was to provide transparency around model capabilities in Android development and to encourage model improvements, to give you more helpful AI options for your everyday workflow. Since then, we have enhanced the benchmark based on your feedback, including evaluating [open-weight models](https://x.com/AndroidDev/status/2064482677500080549) and adding cost and efficiency dimensions to the leaderboard.

But AI capabilities are ever-evolving, and measurement needs to follow suit. As part of our July release, we have adopted the [Harbor framework](https://www.harborframework.com/), which includes an updated version of the benchmarking agent used to evaluate models.

Along with this change to our evaluation, in this July release we're adding 8 new models (**Claude Fable 5, Claude Sonnet 5, Claude Opus 4.8, GLM 5.2, Kimi K2.7 Code, MiniMax M3, Qwen 3.7 Plus and Qwen 3.7 Max**) to the leaderboard. We're also sharing opportunities for you, the Android developer community, to contribute to the benchmark.

**Upgrading our methodology with the Harbor framework**

When we designed Android Bench, we anchored our methodology on leading industry standards available at the time. We used mini-swe-agent v1, a general-purpose benchmarking agent, and adapted it to the nuances of Android development to provide a baseline measurement for the capabilities of models for common Android development tasks.

To continue providing you with state-of-the-art evaluations that accurately measure the latest model capabilities on Android development, we are standardizing our benchmark to the [Harbor framework](https://www.harborframework.com/). Harbor defines standards and integrations that make it easy for anyone to run the benchmark, evaluate their preferred set-up, or share results -- providing you with additional transparency and visibility.

This upgrade enables us to more rigorously evaluate models and their capabilities, and we re-ran the benchmark on all models to establish an updated baseline. This means there is a minor shift in scoring, but you will still be able to view historical scores within [the archive](http://d.android.com/bench/archive) on our website.

We want to ensure Android Bench is helpful for you, so we will continuously update it as our evaluations and the industry mature.

### **Expanding the leaderboard with 8 new models**

As part of our commitment to keeping the leaderboard fresh, we have added Claude Fable 5, Claude Sonnet 5, Claude Opus 4.8, GLM 5.2, Kimi K2.7 Code, MiniMax M3, Qwen 3.7 Plus and Qwen 3.7 Max to the Android Bench leaderboard.

You will see that **Claude Fable 5** is at the top of the leaderboard with a score of 84.5, followed by **GPT 5.5** with 80.2, with **Claude Sonnet 5** in 3rd with a score of 76.2.

When just comparing Open-weight models, **GLM 5.2** is at the top with 72.2, followed by **Kimi K2.7 Code** with a score of 70.4.

You can check out model performance and efficiency metrics on the updated leaderboard to see how these new and previous models navigate Android-specific challenges like Jetpack Compose migrations, wearable networking, and platform API updates.
![image1.png](https://developer.android.com/static/blog/assets/image1_cdb67f52de_Z2bFVId.webp)

### **Opening Android Bench to community contributions**

From the beginning, we've valued an open and transparent approach, which is why we made our original methodology and test harness publicly available on GitHub. You've asked for a way to provide feedback on our dataset, so now we're taking collaboration a step further by giving you, the Android developer community, a chance to shape Android Bench.

Starting today, you can contribute to Android Bench in two ways:

1. Design and [submit your own Android development tasks](https://github.com/android-bench/community-dataset) to evaluate how models handle the scenarios that matter to you.
2. [Run and share benchmark evaluations](https://github.com/android-bench/community-results) firsthand, testing your preferred models against our dataset or your own custom tasks.

We will be reviewing the submitted tasks and will be assessing if they get added to the benchmark. We hope to build a benchmark that truly reflects the diverse, day-to-day realities of the global Android developer community.

### **Looking ahead**

With more and more options for agentic development, maintaining a cutting-edge benchmark ensures that the AI assistance you rely on keeps getting smarter, more helpful, and more effective. Head over to our [GitHub repository](https://github.com/android-bench/android-bench) to check out the tasks. We invite you to submit a task to our team for review, and you can check out [Harbor Hub](https://hub.harborframework.com/datasets/android-bench/android-bench/latest) to explore the dataset or submit evaluations.

As always, you can find the [updated leaderboard](http://d.android.com/bench), or read the [methodology](http://d.android.com/bench/methodology) on our website.
- [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Written by:

-

  ## [Zoe Lopez-Latorre](https://developer.android.com/blog/authors/zoe-lopez-latorre)

  ###### Senior Developer Relations Engineer

  [read_more View profile](https://developer.android.com/blog/authors/zoe-lopez-latorre) ![View Zoe Lopez-Latorre 's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_07_07_at_1_15_58_PM_eb87f2f61a_Z1QyLll.webp) ![View Zoe Lopez-Latorre 's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_07_07_at_1_15_58_PM_eb87f2f61a_Z1QyLll.webp)
Continue reading
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 29 Jul 2026 29 Jul 2026 ![](https://developer.android.com/static/blog/assets/Google_Play_Age_Signals_API_Blog_Strapi_d532f6c0b8_Z298Ads.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Delivering safer, age-appropriate experiences on Google Play](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play) Providing a safe online experience and protecting users from harm is a top priority at Google Play.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 2 min read
- 3 Authors 28 Jul 2026 28 Jul 2026 ![](https://developer.android.com/static/blog/assets/Jetpack_compose_Strapi_123481f79e_Z1F9b9M.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Celebrating 5 years of Jetpack Compose](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose) Today, we officially celebrate five years since the release of Jetpack Compose 1.0. From version 1.0, announced on July 28th, 2021, to our latest 1.11 release, we've seen the APIs evolve significantly over the years, and we're taking a moment to celebrate.
  [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks), [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/MM_Adaptive_and_device_Meta_18e67bafd8_Z1BKgnT.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Optimize your apps for the next generation of Samsung Galaxy devices](https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices)

  [arrow_forward](https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices) Today at Galaxy Unpacked, Samsung unveiled its latest lineup of foldable and wearable devices. For developers, this means that the variety of form factors, screen sizes, and device postures your app needs to support is expanding once again.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) • 3 min read
Stay in the loop

Get the latest Android development insights delivered to your inbox weekly.
[mail Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)