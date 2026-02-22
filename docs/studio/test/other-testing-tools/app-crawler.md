---
title: https://developer.android.com/studio/test/other-testing-tools/app-crawler
url: https://developer.android.com/studio/test/other-testing-tools/app-crawler
source: md.txt
---

# App Crawler

![](https://developer.android.com/static/images/training/testing/robo.png)

Use the App Crawler tool, part of[Jetpack](https://developer.android.com/jetpack), to automatically test your app without the need to write or maintain any code.

The crawler runs alongside your app, automatically issuing actions (tap, swipe, etc.) to explore the state-space of your app. The crawl terminates automatically when there are no more unique actions to perform, the app crashes, or a timeout you designate is reached.

Testing with the crawler is easy because there's no code to write or maintain. Moreover, you can run it on a variety of devices to look for crashes, visual issues, or performance problems. Typically, it's a good idea to use a cloud-based service like[Firebase Test Lab](https://firebase.google.com/docs/test-lab/)to test multiple combinations of screen sizes and hardware configurations more easily and quickly.

## Target audience

App Crawler is targeted at developers who want to ensure their app's basic functionality with minimal configuration. In addition to purely opaque-box testing, the crawler can also be configured to provide specific inputs, such as login credentials or deep links.

## Getting started

Before starting, make sure you have a recent version of the Android SDK. This comes with[Android Studio](https://developer.android.com/studio). If you install a standalone Android SDK, make sure it includes the latest latest build tools and platform tools.

Then,[download the crawler binary archive](https://dl.google.com/appcrawler/beta1/app-crawler.zip).

Next, either start an emulator or connect a physical device using a USB cable. Confirm the device is connected by running the following command:  

```
adb devices
```

To invoke the crawler, first extract the archive to the directory of your choice. From that directory, invoke the crawler using the following command:  

```
java -jar crawl_launcher.jar --apk-file path/to/my/app.apk --android-sdk path/to/my/android/sdk
```

## Crawler options

You can use the following options to invoke the crawler:

|                          Option                           |                                                                                              Description                                                                                               |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--android-sdk `<var translate="no">path</var>            | Specifies the path to your Android SDK. This is a**required**flag.                                                                                                                                     |
| `--apk-file `<var translate="no">file</var>               | Specifies the path to your app APK, which App Crawler then installs and crawls. This is a**required** flag if`--app-package-name`isn't specified.                                                      |
| `--app-package-name `<var translate="no">name</var>       | Specifies the package name of your app. Use this option when your app is already installed on the device and no re-installation is required. This is a**required** flag if`--apk-file`isn't specified. |
| `--key-store `<var translate="no">path</var>              | Specifies the path to the keystore that signs your app and crawler APKs. Use this option when your app requires a specific signature to function properly.                                             |
| `--key-store-password `<var translate="no">password</var> | Specifies the password for the keystore you provided for`--key-store`option. This is a**required** flag if`--key-store`is specified.                                                                   |
| `--timeout-sec `<var translate="no">timeout</var>         | Specifies the timeout for your crawl in seconds. If not specified, the crawl stops after 60 seconds.                                                                                                   |

## Known issues

**Failed to delete original signature files**

Prior to the start of the crawl, JDK 9 users may see this error message:  

```
androidx.test.tools.crawler.launcher.exceptions.ApkSigningException: Failed to delete original signature files
```

If you experience this behavior, we recommend using JDK 8 or 10+. For more information on this issue, see this[JDK 9 bug](https://bugs.openjdk.java.net/browse/JDK-8184940). Some users have fixed the issue by rebuilding their APK using an updated version of Android Studio.

## Additional resources

For more information about using App Crawler, consult the following resources.

- [Firebase Test Lab Robo Test](https://firebase.google.com/docs/test-lab/android/robo-ux-test)contains detailed documentation as well as instructions for how to run crawler tests in the cloud.