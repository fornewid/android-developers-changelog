---
title: https://developer.android.com/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated
url: https://developer.android.com/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Alternatives to Idling Resources in Compose tests: the waitUntil APIs (updated)

###### 3-min read

![](https://developer.android.com/static/blog/assets/alternativesto_Idiling_13a59b7d0b_Z1sfmFQ.webp) 22 Apr 2022 [![](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp)](https://developer.android.com/blog/authors/jose-alcerreca) [##### Jose Alcérreca](https://developer.android.com/blog/authors/jose-alcerreca)

###### Developer Relations Engineer

In this article you'll learn how to use the `waitUntil` test API in Compose to wait for certain conditions to be met. This is a good alternative to using Idling Resources in some situations.

\[2023 update\] Tldr: use the [new waitUntil APIs](https://gist.github.com/JoseAlcerreca/c5b94db07f04b15255b1637ded3a3bbd) to synchronize in Compose tests (v1.4.0+).

*** ** * ** ***

## **What is synchronization?**

One way to categorize tests is by their scope. Small tests, or unit tests, focus on small pieces of your app while big tests, or end-to-end, cover a large portion of your app. You can read about this and other types of tests in the newly updated [testing documentation](https://developer.android.com/training/testing/fundamentals).

Press enter or click to view image in full size
![large_0_9n_Nqkt_HHUTOQ_In_AI_b113b43bcf.png](https://developer.android.com/static/blog/assets/large_0_9n_Nqkt_HHUTOQ_In_AI_b113b43bcf_b38a7b69b9_1vXHCa.webp) Different test scopes in an app

**Synchronization** is the mechanism that lets the test know when to run the next operation. The bigger the chunk of code you choose to verify, the harder it is to synchronize with the test. In unit tests it's easy to have full control of the execution of the code to verify. However, as we grow the scope to include more classes, modules and layers, it gets tricky for the test framework to know if the app is in the middle of an operation or not.

Press enter or click to view image in full size
![large_correct_b1a355f41b.webp](https://developer.android.com/static/blog/assets/large_correct_b1a355f41b_2af63f11d2_ZC2jIa.webp) Correct synchronization between test and app

`androidx.test` and, by extension, [Compose Test](https://developer.android.com/jetpack/compose/testing), use some tricks under the hood so that you don't have to worry too much about this. For example, if the main thread is busy, the test pauses until it can execute the next line.

However, they can't know everything. For example, if you load data in a background thread, the test framework might execute the next operation too soon, making your test fail. The worst situation is when this happens only a small percentage of the time, making the test [flaky](https://developer.android.com/training/testing/fundamentals#flaky).

## **Option 1: Idling Resources**

Idling Resources are an Espresso feature that lets you, the developer, decide when the app is busy. You have two ways to use them:

**1. Installing them in the framework or library that is doing work that the test can't see.**

A good example of this is [RxIdler](https://github.com/square/RxIdler), which wraps an RxJava scheduler. This is the preferred way to register Idling Resources because it lets you keep your test setup cleanly split from the test code.
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_e3ac1334f360f4c6c4f0bbaaec895e591e15fc9d0c0b8fbd0268270dfe5bc796.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

**2. Modifying your code under test to explicitly expose information about whether your app is busy or not.**

For example, you could modify your repository (or a [test double](https://developer.android.com/training/testing/fundamentals/test-doubles)) to indicate that is busy while loading data from a data source:
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_bbed89de23a03697da61c2cc641fc9c8f411c43574e0d16391a2b9851b40c08b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

This is not ideal because you're polluting your production code, or creating complicated test doubles, and there are some situations when they're hard to install. For example, how would you use Idling Resources in a Kotlin Flow? Which update is the *final* one?

Instead, we can *wait* for things.

## **Option 2: Waiting for things... the wrong way**

Loading data is usually fast, especially when using fake data, so why waste time with idling resources when you can just make the test sleep for a couple of seconds?
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_a90eadd192ea72a5eeda558e2d209e1371ff4a3dcd713d1b3a44f0f1fdacfe90.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

This test will either **run slower than needed or fail**. When you have hundreds or thousands of UI tests, you want tests to be as fast as possible.

Also, sometimes emulators or devices misbehave and jank, making that operation take a bit longer than those 2000ms, breaking your build. When you have hundreds of tests this becomes a huge issue.
![0_DOCdjq-JpPDGV5OB.png](https://developer.android.com/static/blog/assets/0_DO_Cdjq_Jp_PDGV_5_OB_66574ebe4f_13xFyh.webp)

## **Option 3: Waiting for things the right way!**

If you don't want to modify your code under test to expose when it's busy, another option is to wait until a certain condition is met, instead of waiting for an arbitrary amount of time.
![1_jIYFxE4qlHXMi2SwW6JemA.png](https://developer.android.com/static/blog/assets/1_j_IY_Fx_E4ql_HX_Mi2_Sw_W6_Jem_A_63f8b87010_Z2oBJni.webp)

In Compose, you can leverage the [waitUntil](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule#waitUntil(kotlin.Long,kotlin.Function0)) function, which takes another function that produces a boolean.
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_222b0225e82515be85f29ddf15b41c1651a1addb2c1a415f5c37e2c79ee861b0.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

2023/03/22 update: from Compose 1.4.0, we added a new set of waitUntil APIs:
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_9f8e46acb0f74e41a541bdbc7600959d3368cae2101dd8d8843341ece9e22ce2.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

\[Before 1.4.0: Use these helpers: [waitUntilExists](https://gist.github.com/JoseAlcerreca/902a0c5a06e02a7411c0518c3f997dbf), [waitUntilNodeCount](https://gist.github.com/JoseAlcerreca/ff5c1f43fe31f1a55ce462bc214cdc83)\]

...and use them like this:
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_ef05993ed4878dd1ed2c32a53984050ed0ded34cd19546966d10de6abad0b249.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

Use these APIs only when you need to synchronize your test with the UI. Synchronizing on every test statement pollutes the test code unnecessarily, making it harder to maintain.

When should you use it then? A good use case for it is loading data from an observable (with LiveData, Kotlin Flow or RxJava). When your UI needs to receive multiple updates before you consider it idle, you might want to simplify synchronization using `waitUntil`.

For example, when you collect a Flow from a view:
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_4c928e0fcf6e9c2e384dc4120283cb4fd37b90e6263445ea2ca039684a7b6074.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

And you emit multiple items to it:
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_2be6d9ae439d54226b5c2c1122ad96557c97a754ece7d4440a78976378a9c19f.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

If `repository` takes an indeterminate amount of time to come back with the first result, the test framework will think "Loading" is the idle state (the initial value assigned in `collectAsState`) and continue with the next statement.
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_b35d485b00e8402d9d158770410b4e1bb2115281089d66fea58206260e7c76ef.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

So, you can make the test much more reliable if you make sure the UI is not showing the loading indicator:
<iframe src="https://android.devsite.google/frame/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated/index_8525ae2a0a7be13740c3dfd518aa246dac97031a68aecc61d89bbe29913ec02b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

*** ** * ** ***

Happy... wait for it... testing!

*** ** * ** ***

*Code snippets license:*

```
Copyright 2022 Google LLC.
SPDX-License-Identifier: Apache-2.0
```
- [#Android](https://developer.android.com/blog/topics/android)
- [#Compose](https://developer.android.com/blog/topics/compose)
- [#Idling Resources](https://developer.android.com/blog/topics/idling-resources)

###### Written by:

-

  ## [Jose Alcérreca](https://developer.android.com/blog/authors/jose-alcerreca)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jose-alcerreca) ![](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp) ![](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)](https://developer.android.com/blog/authors/jolanda-verhoef) 23 Jan 2025 23 Jan 2025 ![](https://developer.android.com/static/blog/assets/camera_X_Jetpack_09bc5a0414_Z1DttIl.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Create a spotlight effect with CameraX and Jetpack Compose](https://developer.android.com/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose)

  [arrow_forward](https://developer.android.com/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose) In this post, we'll dive into something a bit more visually engaging --- implementing a spotlight effect on top of our camera preview, using face detection as the basis for the effect.

  ###### [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef) •
  8 min read

  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#Mobile App Development](https://developer.android.com/blog/topics/mobile-app-development)
  - +1 ↩
- [![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](https://developer.android.com/blog/authors/adarsh-fernando)[![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](https://developer.android.com/blog/authors/esteban-de-la-canal) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Android CLI and skills: Build Android apps 3x faster using any agent](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent) Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

  ###### [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando), [Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)