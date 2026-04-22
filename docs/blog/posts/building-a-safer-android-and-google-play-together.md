---
title: https://developer.android.com/blog/posts/building-a-safer-android-and-google-play-together
url: https://developer.android.com/blog/posts/building-a-safer-android-and-google-play-together
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Building a safer Android and Google Play, together

###### 3-min read

![](https://developer.android.com/static/blog/assets/251210_Header_v01_de706a19ce_ZIQ3n5.webp) 11 Dec 2025 [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/ron-aquino)

##### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe)
\&
[Ron Aquino](https://developer.android.com/blog/authors/ron-aquino)

Earlier this year, we reiterated our commitment to [keeping Android and Google Play safe](https://android-developers.googleblog.com/2025/03/keeping-google-play-safe.html) for everyone and maintaining a thriving environment where users can trust the apps they download and your business can flourish. We've heard your feedback clearly, from excited conversations at Play events around the world to the honest concerns on social media. You want simpler ways to make sure your apps are compliant and pass review, and need strong protections for your business so you can focus on growth and innovation. We are proud of the steps we've taken together this year, but know this is ongoing work in a complex, ever-changing market.

Here are key actions we've taken this year to simplify your development journey and strengthen protection.

### Simpler ways to build safer apps from the start

This year, we focused on making improvements to the app publishing experience by reducing friction points, from the moment you write code to submitting your app for review.

- **Policy guidance right where you code** : We rolled out [Play Policy Insights](https://developer.android.com/studio/publish/insights) to all developers using Android Studio. This feature provides real-time, in-context guidance and policy warnings as you code, helping you proactively identify and resolve potential issues before you even submit your app for review.
- **Pre-review checks to help prevent app review surprises: Last year, we launched pre-review checks in Play Console so you can identify issues early, like incomplete policy declarations or crashes, and avoid rejections. This year, we expanded these checks for privacy policy links, login credential requirements, data deletion request links, inaccuracies in your Data safety form, and more.**

### Stronger protection for your business and users

We are committed to providing you with powerful ways to protect your apps and users from abuse. Beyond existing [tools](https://support.google.com/googleplay/android-developer/answer/9867159#zippy=%2Cages-and-over), [programs](https://play.google.com/console/about/programs/teacherapproved/), and the performance and security enhancement that comes with every Android [release](https://android-developers.googleblog.com/2025/06/android-16-is-here.html), we've also launched:

- **Advanced abuse and fraud protection** : We made the Play Integrity API [faster and more resilient](https://android-developers.googleblog.com/2024/12/making-play-integrity-api-faster-resilient-private.html), and introduced new features like [Play remediation prompts](https://android-developers.googleblog.com/2025/10/stronger-threat-detection-simpler.html) and [device recall](https://developer.android.com/google/play/integrity/device-recall) in beta. Device recall is a powerful new tool that lets you store and recall limited data associated with a device, even if the device is reset, helping protect your business model from repeat bad actors.
- **Tools to keep kids safe** :
  - We continued to [invest](https://blog.google/technology/safety-security/age-assurance-measures-safer-online-kids-teens-us/) in protecting children across Google products, including Google Play. New Play [policy](https://support.google.com/googleplay/android-developer/answer/16302250?sjid=17958105945234987629-NC) helps keep our youngest users safe globally by requiring apps with dating and gambling features to use Play Console tools to prevent minors from accessing them. Our enhanced Restrict Minor Access feature now blocks the users who we determine to be minors from searching for, downloading, or making purchases in apps that they shouldn't have access to.
  - We've also been [providing tools](https://support.google.com/googleplay/android-developer/answer/16569691) to developers to help meet significant new age verification regulatory requirements in applicable US states.
- **More ways to stop malware from snooping on your app:** Android 16 provides a [new, powerful defense](https://android-developers.googleblog.com/2025/12/enhancing-android-security-stop-malware.html) in a single line of code: `accessibilityDataSensitive`. This flag lets you explicitly mark views in your app as containing sensitive data and block malicious apps from seeing or performing interactions on it. If you already use [`setFilterTouchesWhenObscured(true)`](https://developer.android.com/privacy-and-security/risks/tapjacking#mitigations) to protect your app from tapjacking, your views are automatically treated as sensitive data for accessibility for an instant additional layer of defense with no extra work.

### Smoother policy compliance experience

We're listening to your concerns and proactively working to make the experience of Play policy compliance and Android security requirements more transparent, predictable, and accessible for all developers. You asked for clarity, fairness, and speed, and here is what we launched:

- **More support when you need it** : Beyond the [webinars](https://developersonair.withgoogle.com/google-play-policy-webinars?sjid=2798052899965005772-NA) and [resources](https://support.google.com/googleplay/android-developer/answer/16373081?ref_topic=9877065&sjid=2798052899965005772-NA) that we share, you told us you needed more direct policy help to understand requirements and get answers. Next week, we'll add a direct way for you to reach our team about policy questions in your Play Console. You'll be able to find this new, integrated support experience directly within your Play Console via the ["Help" section](https://play.google.com/console/u/0/developers/help-and-support). We also expanded the [Google Play Developer Help Community](https://support.google.com/googleplay/android-developer/community) to more languages, like Indonesian, Japanese, Korean, and Portuguese.
- **Clearer documentation:** You asked for policy that's easier to understand. To help you quickly grasp essential requirements, we've introduced a new Key Considerations section across several policies (like Permissions and Target API Level) and included concise "Do's \& Don'ts" and easier-to-read summaries.
- **More transparent appeals process:** We introduced a [180-day appeal window](https://support.google.com/googleplay/android-developer/answer/16659089) for account terminations. This allows us to prioritize and make decisions faster for developers who file appeals.
- **Android developer verification design changes** : To support a diverse range of users and developers, we're [taking action](https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html) on your feedback.
  - First, we're creating a dedicated free account type to support students and hobbyists who want to build apps just for a small group, like family and friends. This means that you can share your creations to a limited number of devices without needing to go through the full developer verification process.
  - We're also building a flow for experienced users to be able to install unverified apps. This is being carefully designed to balance providing choice with prioritizing security, including clear warnings so users fully understand the risks before choosing to bypass standard safety checks.

The improvements we made this year are only the beginning. Your feedback helps drive our roadmap, and it will continue to inform future refinements to our policies, tools, experiences, and ensuring Android and Google Play remain the safest and most trusted place for you to innovate and grow your business.

Thank you for being our partner in building the future of Android.

###### Written by:

-

  ## [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe)

  ###### Director, Product Management

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-forsythe) ![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp) ![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)
-

  ## [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino)

  ###### Sr. Director

  [read_more
  View profile](https://developer.android.com/blog/authors/ron-aquino) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 30 Mar 2026 30 Mar 2026 ![](https://developer.android.com/static/blog/assets/android_Verification2_40caaf2e67_NyvEj.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Rolling out to all developers on Play Console and Android Developer Console](https://developer.android.com/blog/posts/android-developer-verification-rolling-out-to-all-developers-on-play-console-and-android-developer-console)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-rolling-out-to-all-developers-on-play-console-and-android-developer-console) Android is for everyone. It's built on a commitment to an open and safe platform. Users should feel confident installing apps, no matter where they get them from.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 19 Mar 2026 19 Mar 2026 ![](https://developer.android.com/static/blog/assets/android_Verification2_b4044e9b89_1tLhzE.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Balancing openness and choice with safety](https://developer.android.com/blog/posts/android-developer-verification-balancing-openness-and-choice-with-safety)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-balancing-openness-and-choice-with-safety) Android proves you don't have to choose between an open ecosystem and a secure one. Since announcing updated verification requirements, we've worked with the community to ensure these protections are robust yet respectful of platform freedom.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  2 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)