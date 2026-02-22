---
title: https://developer.android.com/guide/playcore/install-prompt
url: https://developer.android.com/guide/playcore/install-prompt
source: md.txt
---

In-app install prompts are in beta  
Displaying in-app install prompts is limited to early access partners. While this feature is in beta, you can prepare your app for support by following the guidance in this section.  
[Nominate yourself to be an early access partner →](https://goo.gle/)  
![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

When users install your app on multiple devices they own, they can engage with
it more often and in new contexts---on their watch while on the go, on their TV
while relaxing at home, or on their tablet while commuting. This increased
engagement across form factors can lead to a more loyal user base and new
opportunities for your app to provide value. Although some users install apps
across their devices organically, others might appreciate a reminder from one
device to install on another. The in-app install prompt is a Google Play Core
Library feature that lets you prompt your existing phone users to install and
engage with the app on other devices the user owns.

## Installation flow

The in-app install prompt flow includes the following steps:

1. A prompt appears that Play controls.
2. The user taps **See details**, and then Play presents options to select form factors. Play pre-selects relevant devices, displaying screenshots and eligible devices for one-click installation.
3. After tapping **Install**, Play informs the user of pending remote installation.
4. The user can dismiss the prompt and finish their original task within the app.
5. Once the app is successfully installed on the other device, the user gets a confirmation notification on that device.

### Eligibility checks

Play performs a set of asynchronous eligibility checks that gate the prompt UX.
The prompt won't show if any of these checks fail:

- **Age:** Kids accounts cannot use this feature.
- **Compatibility:** Play shows a prompt only if the user has a compatible alternate form factor device for the requested action, for example, installation.
- **Frequency:** Play can show a prompt at most 3 times per month.

## Integrate in-app install prompts in your app

Learn how to integrate in-app install prompts in your app, see:

- [Kotlin or Java](https://developer.android.com/guide/playcore/install-prompt/kotlin-java)

### User privacy

To protect user privacy, Play doesn't inform your app whether the prompt was
shown or not. While we encourage you to integrate the in-app install prompt API
into your app and call it where it makes sense in your user flow, Play controls
when and if the prompt is shown to users using the previously described
eligibility checks.

## Terms of service and data safety

By accessing or using the Play In-App Install Prompts Library, you agree to the
[Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license) and the
[Google Play Terms of Service](https://play.google.com/about/play-terms/index.html). Read and understand all applicable
terms and policies before accessing the library