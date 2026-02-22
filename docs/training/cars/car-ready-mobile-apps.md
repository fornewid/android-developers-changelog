---
title: https://developer.android.com/training/cars/car-ready-mobile-apps
url: https://developer.android.com/training/cars/car-ready-mobile-apps
source: md.txt
---

# Car ready mobile apps

The*Car ready mobile apps* program distributes eligible mobile apps in the[video](https://developer.android.com/training/cars#video),[games](https://developer.android.com/training/cars#games), and[browsers](https://developer.android.com/training/cars#browser)categories to cars with little to no additional development work. Starting in February 2025, eligible apps will be available for download from the Google Play Store in cars that run Android Automotive OS with Google built-in.
| **Note:** At a later date, Android Auto will add support for these apps.

## Eligibility

To be eligible for distribution through this program, your app must meet all of the[Car ready](https://developer.android.com/docs/quality-guidelines/car-app-quality#car-quality-tiers)quality guidelines for your app's category. If your app does not already meet some of these guidelines --[`AN-1`](https://developer.android.com/docs/quality-guidelines/car-app-quality#AN-1), for example -- they might still be met when run in the[compatibility mode](https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode)used to run apps distributed through the program.

### Address common eligibility issues

To increase the chances that your app will be selected for distribution through the program, test your app to validate that it doesn't have any of the following common eligibility issues.

#### Feature requirements preventing distribution

To make your app eligible for distribution to any compatible car with Google built-in, it must[meet Google Play feature requirements](https://developer.android.com/training/cars/platforms/automotive-os#play-feature-requirements).

#### Dependency on an unavailable Google Play service

If your app has a breaking dependency on a Google Play service that is not[available on Cars with Google built-in](https://developer.android.com/training/cars/platforms/automotive-os/google-play/google-services), you'll need to implement an alternative or remove the dependency.

## Test your app

To test your app on Android Automotive OS, you can use the[generic system images with compatibility mode](https://developer.android.com/training/cars/testing/emulator?filter=compatibility-mode#generic-images).

These emulator system images include the compatibility mode that is required for cars to receive apps distributed through the*Car ready mobile apps*program, so they give the most accurate representation of how your app performs. If you test with other system images, your app's behavior may differ.

## Participate in the program

Participation in the program is by invite only. You can nominate your app for consideration by submitting the[interest form](https://forms.gle/uBF9nyFdABnLh7wQ7).

If your app is not accepted into the program, you can still bring your app to cars. See[Build parked apps](https://developer.android.com/training/cars/parked)for more details.

### How will I know if my app has been selected for the program?

If your app is selected for the program, you will receive a message in your[Play Console Inbox](https://play.google.com/console/developers/inbox)as well as an email to the[contact email address](https://support.google.com/googleplay/android-developer/answer/10840893)associated with your Google Play account. After a period of time specified in these notifications, your app is automatically opted in to the program unless you choose to opt out.

## Opt out of the program

During the notification period, you can opt out of the program by submitting the[opt-out form](https://forms.gle/yMYKZUmT2vVmJkKd6).

After the notification period has passed and your app has been opted in to the program, you can opt out through the Google Play Console by following the steps detailed in[Distribute to cars](https://developer.android.com/training/cars/distribute#opt-out).

## Analyze usage in cars

If your app is made available through the*Car ready mobile apps*program, you can do the following to understand how it is being installed and used in cars.

|       Platform        |                                                                                                       Play Console                                                                                                       |                                                                                                                                                                              On device                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Android Automotive OS | In the Google Play Console, you can filter by the "Car" form factor to get information about your app's performance in Cars with Google built-in on the*Reach and devices* ,*Statistics* , and*Rating and reviews*pages. | You can use the[`hasSystemFeature`](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String))API to detect whether your app is running on Android Automotive OS by checking for the[`FEATURE_AUTOMOTIVE`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUTOMOTIVE)feature. |

## Frequently asked questions

### Will my app be usable while the user is driving?

No, apps distributed through the*Car ready mobile apps*program are not usable while driving. If a user begins driving while your app is open, the OS handles hiding your app from the user and stopping it.

### Why should I make my app available in cars?

By making your app available in cars, you can increase user engagement during down time, such as when charging electric vehicles or waiting to pick someone up. In the future, apps will also be available for use on passenger displays while driving.

### Which devices support apps distributed through the*Car ready mobile apps*program?

Apps distributed through the*Car ready mobile apps*program will be available on a variety of Cars with Google built-in that have been certified by Google to meet the program requirements. Google is working with OEMs to certify more new and existing devices in the coming months and years.

### How can I test my app's experience in cars?

See the[Test your app](https://developer.android.com/training/cars/car-ready-mobile-apps#test)section of this page.

### If I choose to participate, what happens if I want to opt-out at a later date?

Your app remains installed on any devices it has been installed on, but it doesn't receive updates on those devices and isn't discoverable for installation on other devices.

### If I choose not to participate now, can I change my mind and distribute my app to cars at a later date?

Yes, opting out doesn't prevent you from distributing your app to cars at a later date.

### My app wasn't chosen for inclusion in the program. Can I still distribute it to cars?

Yes, you can still distribute your app to cars. See[Distribute to cars](https://developer.android.com/training/cars/distribute)for more details.

### When will Android Auto be supported?

Stay tuned to this page for more details on Android Auto support.