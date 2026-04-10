---
title: https://developer.android.com/blog/posts/lets-talk-security-answering-your-top
url: https://developer.android.com/blog/posts/lets-talk-security-answering-your-top
source: md.txt
---

#### [Community](https://developer.android.com/blog/categories/community)

# Let's talk security: Answering your top questions about Android developer verification

###### 2-min read

![](https://developer.android.com/static/blog/assets/lets_Talk_Security_3e0a595955_rfy1m.webp) 30 Sep 2025 [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) [##### Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe)

###### Director, Product Management

Android recently [announced](https://android-developers.googleblog.com/2025/08/elevating-android-security.html) [developer verification](https://developer.android.com/developer-verification), an extra layer of security that deters bad actors and makes it harder for them to spread harm.

Developer feedback is essential as we build this process. One of the most important themes we hear from the developer community is the need for more lead time to adapt to changes, which is why we announced this requirement more than a year before it takes effect. This extended timeline allows you to ask questions, provide feedback that will help shape the final process, and prepare for the new requirement, ensuring a smooth transition for your workflow.

<br />

We're committed to answering your top questions, which you can find regularly updated in our [guides](https://developer.android.com/developer-verification/guides) and [FAQ](https://support.google.com/android-developer-console/answer/16561738), and we've compiled the most frequent answers below. For a deeper discussion on developer identification, check out our conversation on [Android Developer Backstage](https://www.youtube.com/watch?v=A7DEhW-mjdc&feature=youtu.be).

[Video](https://www.youtube.com/watch?v=A7DEhW-mjdc)

### Does this mean sideloading is going away on Android?

Absolutely not. Sideloading is fundamental to Android and it is not going away. Our new developer identity requirements are designed to protect users and developers from bad actors, not to limit choice. We want to make sure that if you download an app, it's truly from the developer it claims to be published from, regardless of where you get the app. Verified developers will have the same freedom to distribute their apps directly to users through sideloading or through any app store they prefer.

### How does developer verification impact my use of Android Studio?

We are working to ensure these changes don't have an impact on your day-to-day workflow so you can continue building your apps as smoothly as possible. Participating in developer verification **will not affect your experience in** [**Android Studio**](https://developer.android.com/studio)**, the official IDE for Android app development.** You will continue to be able to build and run an app even if your identity is not verified. Android Studio is unaffected because deployments performed with [adb](https://developer.android.com/tools/adb), which Android Studio uses behind the scenes to push builds to devices, is unaffected. You can continue to develop, debug, and test your app locally by deploying to both emulators and physical devices, just as you do now.

#### Making APKs available to your test team

If your team's current test process relies on distributing APKs to testers for installation using methods other than [adb](https://developer.android.com/tools/adb), you will need to verify your identity and register the package. This also applies if you make APKs available to your test teams through [Google Play Internal Testing](https://play.google.com/console/about/internal-testing/), [Firebase App Distribution](https://firebase.google.com/docs/app-distribution), or similar solutions through other distribution partners.

### Do I still need to register my apps if I'm only distributing to a limited number of users?

We recommend you register. It's a simple, one-time process that will allow anyone to download and install your app. However, if you prefer not to, we are also introducing a free developer account type that will allow teachers, students, and hobbyists to distribute apps to a limited number of devices without needing to provide a government ID.

If you're interested in a limited distribution account, we want to [hear from you](https://goo.gle/verification-feedback-survey) to shape the experience.

### What can I do to prepare for developer verification?

The best way to get ready and stay updated is to sign up for [early access](https://goo.gle/android-verification-early-access). We'll start sending invitations in October.

We recommend you participate in developer verification because, even though verification is not required to develop apps with Android Studio, you will need it to distribute apps to certified Android devices. Apps installed through enterprise management tools on managed devices will also be installable without being registered.

Please let us know if you have any [feedback or questions](https://goo.gle/Android-verification-feedback) about the verification requirements.
- [#Android](https://developer.android.com/blog/topics/android)
- [#identity](https://developer.android.com/blog/topics/identity)

###### Written by:

-

  ## [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe)

  ###### Director, Product Management

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-forsythe) ![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp) ![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 20 Oct 2025 20 Oct 2025 ![](https://developer.android.com/static/blog/assets/Now_In_Android121_f4ff784252_Z2dFDgg.webp)

  #### [Community](https://developer.android.com/blog/categories/community)

  ## [Now in Android #121](https://developer.android.com/blog/posts/now-in-android-121)

  [arrow_forward](https://developer.android.com/blog/posts/now-in-android-121) Compose 1.9, Media 3 1.8, QPR2 Beta 1, Narwhal Feature Drop, and more!

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  9 min read

  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Now In Android](https://developer.android.com/blog/topics/now-in-android)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Robbie_280bd4586c_2wmcrw.webp)](https://developer.android.com/blog/authors/robbie-mclachlan) 25 Mar 2026 25 Mar 2026 ![](https://developer.android.com/static/blog/assets/Meet_The_Class_2_bb4f1ec5bd_Z1MklPk.webp)

  #### [Community](https://developer.android.com/blog/categories/community)

  ## [Meet the class of 2026 for the Google Play Apps Accelerator](https://developer.android.com/blog/posts/meet-the-class-of-2026-for-the-google-play-apps-accelerator)

  [arrow_forward](https://developer.android.com/blog/posts/meet-the-class-of-2026-for-the-google-play-apps-accelerator) The wait is over! We are incredibly excited to share the Google Play Apps Accelerator class of 2026.

  ###### [Robbie McLachlan](https://developer.android.com/blog/authors/robbie-mclachlan) •
  1 min read

- [![](https://developer.android.com/static/blog/assets/Robbie_280bd4586c_2wmcrw.webp)](https://developer.android.com/blog/authors/robbie-mclachlan) 11 Dec 2025 11 Dec 2025 ![](https://developer.android.com/static/blog/assets/Android_Devs_Google_Devs_Blog_Header_1200x600_79350b0b52_1w8gkH.webp)

  #### [Community](https://developer.android.com/blog/categories/community)

  ## [#WeArePlay: How Matraquina helps non-verbal kids communicate](https://developer.android.com/blog/posts/we-are-play-how-matraquina-helps-non-verbal-kids-communicate)

  [arrow_forward](https://developer.android.com/blog/posts/we-are-play-how-matraquina-helps-non-verbal-kids-communicate) In our latest #WeArePlay film, we meet Adriano, Wagner and Grazyelle. The trio are behind Matraquinha, an app helping thousands of non-verbal children in more than 80 countries communicate.

  ###### [Robbie McLachlan](https://developer.android.com/blog/authors/robbie-mclachlan) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)