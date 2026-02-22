---
title: https://developer.android.com/training/cars/distribute
url: https://developer.android.com/training/cars/distribute
source: md.txt
---

# Distribute to cars

You've got a great app, and Google Play can help you bring it to users in their vehicles. To get started, review this page to learn how build apps for Android Auto and Android Automotive OS (AAOS) and distribute them through Google Play.

## Understand guidelines and requirements

To prepare for a successful launch, start by reviewing the following table of guidelines and requirements for creating great experiences on Android for Cars.

### All apps

|                                                               General                                                               |                                                                                                            Android Auto                                                                                                            |                                                                                                                        Android Automotive OS                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Meet the[car app quality guidelines](https://developer.android.com/docs/quality-guidelines/car-app-quality)for your app's category. | - Declare`com.google.android.gms.car.application`metadata entry with your app's capabilities in your app manifest. - Deliver your Android Auto experience as part of a new or existing app for phones, tablets, and other devices. | - Use the same package name as your mobile app or create a new one. For details, see[Select an AAOS package name](https://developer.android.com/training/cars/distribute#package-name). - Add Automotive OS-specific screenshots to your Google Play Store listings. |

### Media apps

|                                      General                                       |                                                Android Auto                                                 |                                                                                                                         Android Automotive OS                                                                                                                          |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| See[Build media apps for cars](https://developer.android.com/training/cars/media). | - [Add support for Android Auto to your media app](https://developer.android.com/training/cars/media/auto). | - [Add Android Automotive OS support to your media app](https://developer.android.com/training/cars/media/automotive-os). - Publish your app using a[dedicated Android Automotive OS track](https://developer.android.com/training/cars/distribute#choose-track-aaos). |

### Communication apps

| General |                                               Android Auto                                               |                                                                                                                                                                   Android Automotive OS                                                                                                                                                                   |
|---------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| N/A     | - [Build communication apps for Android Auto](https://developer.android.com/training/cars/communication) | - Communication apps are not supported on Android Automotive OS. Messages and calls from phones are shown on the car head unit using the car's companion app if the car manufacturer has integrated the appropriate libraries. For more information, see[Supported app categories](https://developer.android.com/training/cars#supported-app-categories). |

### Templated apps

|                                                                                                                                                                                                                                                                                                  General                                                                                                                                                                                                                                                                                                  |                                                  Android Auto                                                  |                                                                                                                             Android Automotive OS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - See[Use the Android for Cars App Library](https://developer.android.com/training/cars/apps). - For point of interest apps, see[Build point of interest apps for cars](https://developer.android.com/training/cars/apps/poi). - For internet of things apps, see[Build internet of things apps for cars](https://developer.android.com/training/cars/apps/iot). - For navigation apps, see[Build navigation apps for cars](https://developer.android.com/training/cars/apps/navigation). - For weather apps, see[Build weather apps for cars](https://developer.android.com/training/cars/apps/weather). | - [Add support for Android Auto to your templated app](https://developer.android.com/training/cars/apps/auto). | - [Add support for Android Automotive OS to your templated app](https://developer.android.com/training/cars/apps/automotive-os). - Publish your app using a[dedicated Android Automotive OS track](https://developer.android.com/training/cars/distribute#choose-track-aaos). |

### Parked apps

|                                                                                        General                                                                                         |                                                 Android Auto                                                  |                                                                                                                                                                                                                                                                         Android Automotive OS                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - See[Build parked apps for cars](https://developer.android.com/training/cars/parked) - For games, see[Build games for cars](https://developer.android.com/training/cars/parked/games) | - [Add support for Android Auto to your parked app](https://developer.android.com/training/cars/parked/auto). | - For video apps, see[Build video apps for Android Automotive OS](https://developer.android.com/training/cars/parked/video) - For browsers, see[Build browsers for Android Automotive OS](https://developer.android.com/training/cars/parked/browser) - [Add support for Android Automotive OS to your parked app](https://developer.android.com/training/cars/parked/automotive-os). - Publish your app either using the[mobile release track or a dedicated Android Automotive OS track](https://developer.android.com/training/cars/distribute#choose-track-aaos). |

## Prepare your app for distribution

Before your app can be made available to users in their cars, you must upload your app to the Play Console and update your store listing with Android Auto and AAOS screenshots and other information.

For general information about preparing for launch on Google Play, see the[Launch Checklist](https://developer.android.com/distribute/best-practices/launch/launch-checklist).

### Select an AAOS package name

If you have an existing app on the Google Play Store for Android mobile devices, you can continue to use the same package name for your Android Automotive OS app.**We strongly recommend that you use the same package name for your Android mobile app and AAOS app**for the following reasons:

- Doing so makes it easier for you to manage your store listings and releases for both apps. You can reuse your app description and other assets from your mobile app for your AAOS app. You can use[a dedicated AAOS track](https://support.google.com/googleplay/android-developer/answer/13295490)to control the release of your AAOS app separately from your mobile app.
- If your[parked app](https://developer.android.com/training/cars/parked)is built using[adaptive app principles](https://developer.android.com/adaptive-apps), or should you ever decide to do so in the future, using the same package name for both apps lets you update your app to support different form factors using a single app bundle.

### Declare the AAOS hardware feature

For AAOS apps, depending on which[track type](https://developer.android.com/training/cars/distribute#choose-track-aaos)you choose and your app's category, there are different restrictions for the required automotive hardware[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)element:  

    <manifest ...>
      ...
      <uses-feature android:name="android.hardware.type.automotive" ...>
      ...
    </manifest>

|                                                                            App category                                                                             |         Track type         |                      Restrictions                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------------------------------|
| [Parked apps](https://developer.android.com/training/cars/distribute#parked-apps)                                                                                   | Mobile                     | `android:required`must be`"false"`                     |
| [Parked apps](https://developer.android.com/training/cars/distribute#parked-apps)                                                                                   | Android Automotive OS only | `android:required`must be`"true"`,`"false"`, or unset. |
| [Media](https://developer.android.com/training/cars/distribute#media-apps)and[templated](https://developer.android.com/training/cars/distribute#templated-apps)apps | Android Automotive OS only | `android:required`must be`"true"`or unset.             |

| **Tip:** When supported, using a value of`false`for the`android:required`attribute lets you distribute the same artifact to Android Automotive OS vehicles as to other form factors.

## Opt in to form factors

You must also opt in to the other form factors by completing the following steps in the Google Play Console:  

### Android Auto

1. Navigate to the[Form factors](https://play.google.com/console/developers/app/advanced-distribution?tab=releaseTypes)section of the**Advanced Settings**page.
2. Click**Add form factor** and select**Android Auto**.
3. Complete the requirements for Android Auto:
   - Release an Android Auto app bundle or APK to a testing track.

### Android Automotive OS

1. Navigate to the[Form factors](https://play.google.com/console/developers/app/advanced-distribution?tab=releaseTypes)section of the**Advanced Settings**page.
2. Click**Add form factor** and select**Android Automotive OS**.
3. Complete the requirements for Android Automotive OS:
   - Upload Android Automotive OS screenshots for all store listings.
     - This includes both the[main store listing](https://play.google.com/console/developers/app/main-store-listing)and any[custom store listings](https://play.google.com/console/developers/app/custom-store-listings).
     - To take screenshots of the required resolutions, you can use the*Automotive (1024p landscape)* and*Automotive Portrait* [hardware profiles](https://developer.android.com/training/cars/testing/emulator#bundled-profiles). Your screenshots should not reference any Original Equipment Manufacturer (OEM) in particular.
   - Release an Android Automotive OS app bundle or APK to a testing track.
   - Agree to the review policy to ensure your app follows Android Automotive OS quality guidelines.
     - Select the type of track you'll use to distribute your app to Android Automotive OS devices.**Important:** The default set by the Google Play Console is to use the same tracks as for mobile devices. However, the mobile track is not permitted for some categories of apps on Android Automotive OS. See[Choose a track for Android Automotive OS](https://developer.android.com/training/cars/distribute#choose-track-aaos)for more information.

### Choose a track type for Android Automotive OS

You can always distribute your app to Android Automotive OS vehicles by using the dedicated Android Automotive OS track type. Depending on your app's category, you may also have the alternative to distribute your app to Android Automotive OS devices using the mobile release track.

|                                                                            App category                                                                             |         Supported track types         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| [Parked apps](https://developer.android.com/training/cars/distribute#parked-apps)                                                                                   | - Mobile - Android Automotive OS only |
| [Media](https://developer.android.com/training/cars/distribute#media-apps)and[templated](https://developer.android.com/training/cars/distribute#templated-apps)apps | - Android Automotive OS only          |

All else being equal, we recommend that you use the dedicated track. Doing so makes it possible to:

- Roll out releases independent of the mobile track
- Configure different testers and country targeting for testing tracks

| **Tip:** If you use a dedicated track and you -- or a tool or service you rely on -- upload artifacts to Google Play using the[Google Play Developer API](https://developers.google.com/android-publisher), see[Track name for form factors](https://developers.google.com/android-publisher/tracks#ff-track-name)for details on how to manage releasing to the dedicated track.

## Opt out

If you decide to no longer support one or both form factors, you can opt out from the[Form factors](https://play.google.com/console/developers/app/advanced-distribution?tab=releaseTypes)tab of the**Advanced Settings**page as follows:

- Android Auto: Remove Android Auto support from all of the active artifacts across tracks. You can then click the**Remove**button to remove Android Auto from the list of form factors on the page.
- Android Automotive OS: Opt out of Android Automotive OS by clicking the**Manage** button. You can then click the**Remove**button to remove Android Automotive OS from the list of form factors on the page. Users will no longer be able to find your app on Google Play or receive updates.

## App review depends on release track type

While opted-in for distribution to Android Auto or Android Automotive OS, when you make a submission to Google Play that includes an Android Auto or Android Automotive OS compatible artifact, your app is reviewed for compliance with the[car app quality guidelines](https://developer.android.com/docs/quality-guidelines/car-app-quality). This detailed review process might take more time than you are accustomed to when distributing only to phones and tablets.

Depending on the type of track(s) containing Android Auto or Android Automotive OS compatible artifacts in your submission, the impact of the review result may vary. For example, if a submission contains a non-compliant build in a closed testing track, you will be notified that the build is non-compliant but the submission will still be approved. If the same build was in a production track, the submission would be rejected.

|                                             Track type                                              | Form factor review |
|-----------------------------------------------------------------------------------------------------|--------------------|
| [Internal sharing](https://play.google.com/console/about/internalappsharing/) *(Android Auto only)* | None               |
| [Internal testing](https://play.google.com/console/about/internal-testing/)                         | None               |
| [Closed testing](https://play.google.com/console/about/closed-testing/)                             | Non-blocking       |
| [Open testing](https://play.google.com/console/about/opentesting/)                                  | Blocking           |
| [Production](https://play.google.com/console/about/production/)                                     | Blocking           |

When the review is complete, you receive an email sent to your developer account address that lets you know whether your app was approved or rejected. If your app was not approved, the email has a summary of the areas that you need to address. When you finish the necessary adjustments, including**removal of any rejected artifacts**, you can upload a new version of your app for review.

### Ensure your app can be reviewed

To make the app review process as straightforward as possible, take the following into account as you prepare to submit your app for review:

- If your app requires users to sign in to access all of its features, you must submit test account details in the Google Play Console. See[App Access](https://support.google.com/googleplay/android-developer/answer/9859455#app_access)for instructions on how to do this.
  - If your point of interest app lets users make a booking, this test account must be able to make a booking without being charged funds.
- If your navigation or point of interest app is not available in the United States, you must permit users to use a mock GPS location app so that a reviewer can test the app.