---
title: Alternatives to Idling Resources in Compose tests: the waitUntil APIs (updated)  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/alternatives-to-idling-resources-in-compose-tests-the-wait-until-ap-is-updated
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [How-tos](/blog/categories/how-tos)

# Alternatives to Idling Resources in Compose tests: the waitUntil APIs (updated)

###### 3-min read

![](/static/blog/assets/alternativesto_Idiling_13a59b7d0b_Z1sfmFQ.webp)

22

Apr
2022

[![](/static/blog/assets/jose_21a476d0ec_23cCms.webp)](/blog/authors/jose-alcerreca)

[##### Jose Alcérreca](/blog/authors/jose-alcerreca)

###### Developer Relations Engineer

In this article you’ll learn how to use the `waitUntil` test API in Compose to wait for certain conditions to be met. This is a good alternative to using Idling Resources in some situations.

[2023 update] Tldr: use the [new waitUntil APIs](https://gist.github.com/JoseAlcerreca/c5b94db07f04b15255b1637ded3a3bbd) to synchronize in Compose tests (v1.4.0+).

---

## **What is synchronization?**

One way to categorize tests is by their scope. Small tests, or unit tests, focus on small pieces of your app while big tests, or end-to-end, cover a large portion of your app. You can read about this and other types of tests in the newly updated [testing documentation](/training/testing/fundamentals).

Press enter or click to view image in full size

![large_0_9n_Nqkt_HHUTOQ_In_AI_b113b43bcf.png](/static/blog/assets/large_0_9n_Nqkt_HHUTOQ_In_AI_b113b43bcf_b38a7b69b9_1vXHCa.webp)


Different test scopes in an app

**Synchronization** is the mechanism that lets the test know when to run the next operation. The bigger the chunk of code you choose to verify, the harder it is to synchronize with the test. In unit tests it’s easy to have full control of the execution of the code to verify. However, as we grow the scope to include more classes, modules and layers, it gets tricky for the test framework to know if the app is in the middle of an operation or not.

Press enter or click to view image in full size

![large_correct_b1a355f41b.webp](/static/blog/assets/large_correct_b1a355f41b_2af63f11d2_ZC2jIa.webp)


Correct synchronization between test and app

`androidx.test` and, by extension, [Compose Test](/jetpack/compose/testing), use some tricks under the hood so that you don’t have to worry too much about this. For example, if the main thread is busy, the test pauses until it can execute the next line.

However, they can’t know everything. For example, if you load data in a background thread, the test framework might execute the next operation too soon, making your test fail. The worst situation is when this happens only a small percentage of the time, making the test [flaky](/training/testing/fundamentals#flaky).

## **Option 1: Idling Resources**

Idling Resources are an Espresso feature that lets you, the developer, decide when the app is busy. You have two ways to use them:

**1. Installing them in the framework or library that is doing work that the test can’t see.**

A good example of this is [RxIdler](https://github.com/square/RxIdler), which wraps an RxJava scheduler. This is the preferred way to register Idling Resources because it lets you keep your test setup cleanly split from the test code.

**2. Modifying your code under test to explicitly expose information about whether your app is busy or not.**

For example, you could modify your repository (or a [test double](/training/testing/fundamentals/test-doubles)) to indicate that is busy while loading data from a data source:

This is not ideal because you’re polluting your production code, or creating complicated test doubles, and there are some situations when they’re hard to install. For example, how would you use Idling Resources in a Kotlin Flow? Which update is the *final* one?

Instead, we can *wait* for things.

## **Option 2: Waiting for things… the wrong way**

Loading data is usually fast, especially when using fake data, so why waste time with idling resources when you can just make the test sleep for a couple of seconds?

This test will either **run slower than needed or fail**. When you have hundreds or thousands of UI tests, you want tests to be as fast as possible.

Also, sometimes emulators or devices misbehave and jank, making that operation take a bit longer than those 2000ms, breaking your build. When you have hundreds of tests this becomes a huge issue.

![0_DOCdjq-JpPDGV5OB.png](/static/blog/assets/0_DO_Cdjq_Jp_PDGV_5_OB_66574ebe4f_13xFyh.webp)

## **Option 3: Waiting for things the right way!**

If you don’t want to modify your code under test to expose when it’s busy, another option is to wait until a certain condition is met, instead of waiting for an arbitrary amount of time.

![1_jIYFxE4qlHXMi2SwW6JemA.png](/static/blog/assets/1_j_IY_Fx_E4ql_HX_Mi2_Sw_W6_Jem_A_63f8b87010_Z2oBJni.webp)

In Compose, you can leverage the [waitUntil](/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule#waitUntil(kotlin.Long,kotlin.Function0)) function, which takes another function that produces a boolean.

2023/03/22 update: from Compose 1.4.0, we added a new set of waitUntil APIs:

[Before 1.4.0: Use these helpers: [waitUntilExists](https://gist.github.com/JoseAlcerreca/902a0c5a06e02a7411c0518c3f997dbf), [waitUntilNodeCount](https://gist.github.com/JoseAlcerreca/ff5c1f43fe31f1a55ce462bc214cdc83)]

…and use them like this:

Use these APIs only when you need to synchronize your test with the UI. Synchronizing on every test statement pollutes the test code unnecessarily, making it harder to maintain.

When should you use it then? A good use case for it is loading data from an observable (with LiveData, Kotlin Flow or RxJava). When your UI needs to receive multiple updates before you consider it idle, you might want to simplify synchronization using `waitUntil`.

For example, when you collect a Flow from a view:

And you emit multiple items to it:

If `repository` takes an indeterminate amount of time to come back with the first result, the test framework will think “Loading” is the idle state (the initial value assigned in `collectAsState`) and continue with the next statement.

So, you can make the test much more reliable if you make sure the UI is not showing the loading indicator:



---

Happy… wait for it… testing!

---

*Code snippets license:*

```
  Copyright 2022 Google LLC.
SPDX-License-Identifier: Apache-2.0
```

* [#Android](/blog/topics/android)
* [#Compose](/blog/topics/compose)
* [#Idling Resources](/blog/topics/idling-resources)

###### Written by:

* ## [Jose Alcérreca](/blog/authors/jose-alcerreca)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/jose-alcerreca)

  ![](/static/blog/assets/jose_21a476d0ec_23cCms.webp)

  ![](/static/blog/assets/jose_21a476d0ec_23cCms.webp)

## Continue reading

* [![](/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)](/blog/authors/jolanda-verhoef)

  23

  Jan
  2025

  23

  Jan
  2025

  ![](/static/blog/assets/camera_X_Jetpack_09bc5a0414_Z1DttIl.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Create a spotlight effect with CameraX and Jetpack Compose](/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose)

  [arrow\_forward](/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose)

  In this post, we’ll dive into something a bit more visually engaging — implementing a spotlight effect on top of our camera preview, using face detection as the basis for the effect.

  ###### [Jolanda Verhoef](/blog/authors/jolanda-verhoef) • 8 min read

  + [#Android](/blog/topics/android)
  + [#Compose](/blog/topics/compose)
  + [#Mobile App Development](/blog/topics/mobile-app-development)
  + +1
    ↩
* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  04

  Mar
  2026

  04

  Mar
  2026

  ![](/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow\_forward](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 8 min read
* [![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)[![](/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](/blog/authors/ivy-knight)

  02

  Dec
  2025

  02

  Dec
  2025

  ![](/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow\_forward](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](/blog/authors/thomas-ezan), [Ivy Knight](/blog/authors/ivy-knight) • 2 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)