---
title: What a great user experience looks like  |  App quality  |  Android Developers
url: https://developer.android.com/quality/user-experience
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# What a great user experience looks like Stay organized with collections Save and categorize content based on your preferences.




![](/static/images/quality/hero-images/ux_highlighted.svg)

High-quality apps and games are intuitive and delightful to use, evoking
positive sentiment through considered and differentiated design. High-quality
apps stand out from the crowd by presenting a strong, unique identity and brand.

To build a high-quality app or game, follow the Android quality guidelines:

* [Core app quality guidelines](/docs/quality-guidelines/core-app-quality): The minimum quality that all apps should
  meet
* [Adaptive app quality guidelines](/docs/quality-guidelines/adaptive-app-quality): The requirements for a great user
  experience regardless of device form factor, display size, or device posture
* Special cases: See the quality guidelines for [widgets](/docs/quality-guidelines/widget-quality),
  [Wear OS](/docs/quality-guidelines/wear-app-quality), [cars](/docs/quality-guidelines/car-app-quality), [TV](/docs/quality-guidelines/tv-app-quality), and [XR](/docs/quality-guidelines/android-xr)

## Usability

Android offers standard components for app layout, interaction patterns, and
user controls. Use these components to provide a consistent and intuitive user
experience. For example:

* Design your app to adapt to a wide variety of device form factors and
  display sizes
* Use [edge-to-edge layouts](/develop/ui/views/layout/edge-to-edge) for an [immersive experience](/design/ui/mobile/guides/layout-and-content/immersive-content)
* If your app has embedded videos, support multitasking with
  [picture-in-picture](/develop/ui/views/picture-in-picture), including [polished transitions](/design/ui/mobile/guides/home-screen/picture-in-picture)
* Enable content sharing with [Android Sharesheets](/training/sharing/send), which has built-in
  support for share targets
* Support [backup and restore](/guide/topics/data/backup) so that user data and settings are preserved
  if users add a new device, replace an existing device, or reinstall your app

**Note:** Follow the recommended [UX design guidelines](/design/ui) and [adaptive app quality
guidelines](/docs/quality-guidelines/adaptive-app-quality) for all the form factors that your app supports.

When needed, provide an engaging way for users to learn how to make the most of
your app or game or any new features that you may add. Design onboarding for
your target audience; for example, consider whether you need to onboard both new
and expert users. Allow users to configure important aspects of the user
experience such as [notifications](/develop/ui/views/notifications), [privacy](/privacy/best-practices) and [security](/topic/security/best-practices).

## Accessibility, localization, and deep links

With billions of potential users, your app or game may need to support a diverse
range of users and environments.

[Localize](https://play.google.com/console/about/translationservices/) your app or game for the markets you distribute in, providing
high-quality translations, culturally and geographically relevant content, and
appropriate measurements, metrics, and currencies.

Follow Android's guidance for [accessibility](/guide/topics/ui/accessibility), and [build for billions](/docs/quality-guidelines/build-for-billions)
where relevant.

If your app accepts traffic from the web or other external sources with [deep
links](/training/app-links), ensure the links resolve directly to relevant content.

## Visual appeal and craftsmanship

Your app or game's design provides an opportunity to delight users and
differentiate your offering, particularly in competitive categories. Develop an
original art style and take a consistent and coherent approach across all of
your product surfaces. Use images, [color](/design/ui/mobile/guides/styles/color), and whitespace to express
hierarchy, state, and brand identity. Transitions and animation, alongside
images, can help to communicate key messages or complex ideas, and make your
user experience more dynamic. Follow relevant best practices in the [Android UI
design hub](/design/ui).

Games depend on emotion and narrative to engage users. To deliver more immersive
experiences, integrate visual aspects like animations and your art style with
your game's audio, storyline, and controls.

## Monetization

There are many ways to monetize your app. A great monetization experience starts
with setting user expectations. Before people install your app or game, tell
them how and when you bill them.

Ensure that any moments where you choose to monetize are properly integrated
into the user experience. For example, don't surprise users with a payment
request immediately after your app has loaded, or distract them with ads in the
middle of a game level.

If your app or game has a paywall, consider offering free trials for any paid
content so that users can make informed decisions on whether to subscribe. If
users must pay to make progress in your app or game, make sure you set this
expectation prior to installation.

The timing, frequency, and placement of ads are important factors in delivering
a high-quality user experience. To ensure that your ads respect users' time,
keep their presentation proportional to the rest of your content in duration,
frequency, and size. Use careful size and placement to minimize the risk of
accidental taps.

Take responsibility for all of the content in your app, including ads, even if
you use a third-party SDK to deliver them. Be aware of ad content your app
presents to your users and ensure it's appropriate for your audience.

## Google Play guidelines

If you distribute on Google Play, follow these additional user-experience
guidelines.

### Monetization

Google Play lets you generate revenue from users in a range of ways including
[subscriptions and in-app purchases](https://play.google.com/console/about/guides/play-commerce/).

### Discovery and featuring

Google Play considers all aspects of the user experience when evaluating what
titles to promote and where. [Learn more](http://g.co/play/featuring)