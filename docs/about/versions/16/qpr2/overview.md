---
title: https://developer.android.com/about/versions/16/qpr2/overview
url: https://developer.android.com/about/versions/16/qpr2/overview
source: md.txt
---

<br />

Android's public Beta program that gives you everything you need to get your
apps ready for the next version of Android.

- **Hardware and emulator system images** - A runtime environment to test your apps on the next version of Android, for Pixel devices and the Android Emulator.
- **Latest platform code and APIs** - We'll provide regular updates, so you'll be testing against the latest platform code.
- **New behaviors and capabilities** - Pinpoint the behavior changes that will affect your apps, and build with the latest platform capabilities.
- **Feedback and support** - Your feedback is critical! [Report issues](https://developer.android.com/about/versions/16/qpr2/feedback) and let us know what you think! Connect with other developers in the \[Developer Community\]\[community\] to share your experiences.

## Milestones and updates

The Android Beta program for developers runs for several months before each
major and minor release. During that time, we'll provide Beta updates for your
development and testing environments, with SDK tools, system images, emulators,
API reference, and API diffs. See the following table to learn more about what
you should focus on during each milestone.

| Milestone | Type | Developer actions |
|:---:|---|---|
| **Beta 1** | Initial beta-quality release, over-the-air update to developers and early adopters who enroll in Android Beta. | - Explore new behavior changes and APIs. - Begin early app compatibility testing. - Give feedback to report any critical issues or requests to us during this time. |
| Platform Stability |||
| **Platform stability** | First **[Platform Stability](https://developer.android.com/about/versions/16/qpr2/overview#platform-stability)** milestone includes final APIs and behaviors. Play publishing also opens. | - Start final compatibility testing for apps, SDKs, and libraries. - Release compatible app versions. - Continue work to target the new API level (for major releases only). - Update SDKs and libraries and notify their developers of any compatibility issues. |
| **Final release** | Platform release to AOSP and ecosystem. | - Release compatible versions for apps, SDKs, and libraries. - Continue work to target the new API level (for major releases only). - Build with new features and APIs. |

## Android release phases

Each phase of the Android's Beta program helps you prepare your apps for the
stable release to AOSP and the Android ecosystem.

### Beta releases

Beta 1 gives you a more complete and stable environment for building and testing
on the next platform release, and it's the first build that we deliver to early
adopters who are enrolled in the Android Beta program. During the Beta releases
period, early adopters will be using your app on Pixel devices, so we recommend
watching for feedback from those users and releasing compatible updates to
address any issues, without changing the app's targeting. For major releases,
it's also a good time to begin preparing for changing your app's targeting
later. Please [give us your feedback](https://developer.android.com/about/versions/16/qpr2/feedback) during this time, to let us know
of any issues or requests.

### Platform stability milestone

Android releases include a milestone called *Platform Stability* to help you
plan your final testing and releases. This milestone means that the platform has
reached final internal and external APIs, final app-facing behaviors, and final
non-SDK API lists. After Platform Stability, you can expect no further changes
affecting your apps. This is the time to begin final testing and development
work needed to ensure that a compatible version of your app will be ready for
users at the final release to the ecosystem. For major releases, Android will
provide a standard API level at this time.

We encourage **all app, game, SDK, library, and game engine developers** to use
the Platform Stability milestone as a target for planning final compatibility
testing and public release. Using Platform Stability instead of final release
gives you several additional weeks before consumers can receive the new platform
on their devices.

From Platform Stability, you'll also be able to **publish apps to devices**
running the Android platform at the official API level. We recommend publishing
into the Google Play [alpha and beta tracks](https://support.google.com/googleplay/android-developer/answer/9845334) first so that you can
test your apps before distributing broadly through the store.
| **Important:** **All SDK, library, tools, and game engine developers** should start testing at Platform Stability and release your compatible updates as soon as possible. Your downstream app and game developers may be blocked until they receive your updates. When you've released a compatible update, be vocal and let your developers know!

### Final release

The stable version of the Android platform is released to AOSP and the greater
Android ecosystem. You should expect that some of your users will update to the
Android platform at this time or shortly thereafter as device manufacturers
start to release updates for their users. Be prepared for new issues that might
be reported as the number of users on the latest version of Android increases.

## What's included in Beta releases?

The Beta program includes everything you need to test your existing apps on a
variety of screen sizes, network technologies, CPU and GPU chipsets, and
hardware architectures.

### SDK \& tools

Using Android Studio, you can download the following components through the SDK
Manager:

- **SDK and tools** for the Beta release
- **Emulator system images for mobile devices** (64-bit only)

We'll provide updates to these development tools at each milestone as needed.

### System images

We provide system images for a variety of Google Pixel devices that you can use
for developing and testing. Visit the Downloads page for the release to get a
system image for development and testing.

If you don't have a Pixel device, you can still develop and test using other
methods, depending on your workflow:

- Emulator system images for mobile devices (64-bit only)
- Generic system images (GSIs)

### OTA updates for Pixel through the Android Beta program

If you have a supported Pixel device, you can enroll the device in the Android
Beta for Pixel program to get updates to the Android platform Beta over-the-air
(OTA).

To learn more and enroll, visit [g.co/androidbeta](https://g.co/androidbeta).

### Beta APIs and publishing

The early Beta builds initially provide a development-only system and Android
library that **doesn't have a standard API level**. If you want to target the
new platform and build with the new APIs during this time, you must target the
Beta version by updating your app's build configuration.

The preview APIs won't be official until the final SDK is released at Platform
Stability. This means that you should expect **API changes** during the Beta,
especially during the initial weeks of the program. We'll provide a summary of
changes with each release.

Later in the preview, developer APIs will be finalized and you'll be able to
download the official SDK into Android Studio and compile against the official
APIs.

Until the Platform Stability milestone, Google Play prevents publishing of apps
that target a preview API level or the future official API level. When the final
SDK is available, you can then target the official API level and publish your
app to Google Play using the alpha, beta, and production release channels.
Meanwhile, if you want to distribute an app to testers that targets the next API
level, you can do so through email or by direct download from your site at any
time.

### API Reference and diff report

The [platform reference documentation](https://developer.android.com/reference/packages)always shows the most recent platform
preview, beta, or final release. While new APIs are under development, they'll
be watermarked for visibility and show the preview codename as the API level.
Note that you can only use these APIs if you are building with the preview SDK.

When the final SDK is available, the API reference will show that the new APIs
were added in the official API level.

## Support resources

As you test and develop with Android Beta builds, use these channels to report
issues and give feedback:

- Visit the [Feedback and issues](https://developer.android.com/about/versions/16/qpr2/feedback) page for complete information on how to report issues and let us know what you think. From the page, you can go to the issue tracker to file bugs or feature requests, and you can take quick surveys on some of the new features and changes.
- [Android Preview issue tracker](https://developer.android.com/about/versions/16/qpr2/feedback#issue_tracker) is our **primary issue
  tracker**. You can report bugs, performance issues, and general feedback through the issue tracker. You can also check for known issues and find workaround steps. We'll keep you updated on your issue as it's triaged and sent to the Android engineering team for review.
- The \[Android Developer Community\]\[community\] is a community where you can **connect with other users and developers** who are working with the Android 16 preview builds. You can share observations and ideas and find answers to questions there.

\[community\]: /about/versions/16/qpr2/dev-community