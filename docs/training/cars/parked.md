---
title: https://developer.android.com/training/cars/parked
url: https://developer.android.com/training/cars/parked
source: md.txt
---

# Build parked apps for cars

In addition to supporting apps built for use while driving,[Android Auto](https://developer.android.com/training/cars/platforms/android-auto)and[Android Automotive OS](https://developer.android.com/training/cars/platforms/automotive-os)support the following categories of apps for use while parked:

|                                Category                                |                Platform                |
|------------------------------------------------------------------------|----------------------------------------|
| [Video](https://developer.android.com/training/cars/parked/video)      | Android Automotive OS                  |
| [Games](https://developer.android.com/training/cars/parked/games)      | Android Auto and Android Automotive OS |
| [Browsers](https://developer.android.com/training/cars/parked/browser) | Android Automotive OS                  |

[![](https://developer.android.com/static/images/picto-icons/code.svg)
Codelab
Build and test a parked app for Android Automotive OS
arrow_forward](https://developer.android.com/codelabs/build-a-parked-app)  
[![](https://developer.android.com/static/images/picto-icons/distribution.svg)
Car ready mobile apps
Learn how your existing mobile app may be eligible for distribution directly to cars
arrow_forward](https://developer.android.com/training/cars/car-ready-mobile-apps)

## Optimize your app for cars

To give your users the best experience possible, keep the following things in mind while building your app for cars.

### Make your app adaptive

The screens present in cars are more similar in size, resolution, and aspect ratio to tablets and foldables than to phones. As such, optimizing your app for large screens benefits your users in cars as well.

In particular, see[Support different display sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes)for details on making the most of large display sizes, as well as the[media](https://developer.android.com/large-screens/gallery/media)and[games](https://developer.android.com/large-screens/gallery/games)galleries for design inspiration and guidance.
| **Note:** While the large screens media gallery contains mocks for both video and audio apps, only video apps can be built for Android Automotive OS as described in this guide. To build audio apps for Android Automotive OS, see[Build media apps for cars](https://developer.android.com/training/cars/media).

Other large screen optimizations such as[input compatibility](https://developer.android.com/guide/topics/large-screens/input-compatibility-large-screens)aren't as directly beneficial for cars, but they can still improve the user experience. For example, keyboard navigation makes use of the same APIs as[rotary navigation](https://developer.android.com/training/cars/testing/emulator#test-rotary), so any optimizations made there can benefit both form factors.

## Distribute your app

After you've tested your app against the[car app quality guidelines for its category](https://developer.android.com/docs/quality-guidelines/car-app-quality#car-app-guidelines)you can use Google Play to distribute it to Android Auto and/or cars with Google built-in. See[Distribute to cars](https://developer.android.com/training/cars/distribute)for more details on the publishing process.
| **Important:** To ensure a good experience when using parked apps, Google works with OEMs to fix system issues that negatively affect parked app experiences on cars with Google built-in. As part of this collaboration, there is additional filtering built into the Play Store to prevent parked apps from being distributed to devices without the necessary fixes. If your app is otherwise compatible with a device, this might be the reason why it is not installable on that device.

## Give feedback on parked apps

If you run into an issue or have a feature request while developing your parked app, you can report it using the[Google Issue Tracker](https://issuetracker.google.com/components/1385294). Be sure to fill out all the requested information in the issue template. Before filing a new issue, check whether it is already reported in the issues list. You can subscribe and vote for issues by clicking the star for an issue in the tracker. For more information, see[Subscribing to an Issue](https://developers.google.com/issue-tracker/guides/subscribe#starring_an_issue).

[Create a new issue](https://issuetracker.google.com/issues/new?component=1385294)