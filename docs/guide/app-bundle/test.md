---
title: https://developer.android.com/guide/app-bundle/test
url: https://developer.android.com/guide/app-bundle/test
source: md.txt
---

# Build and test your Android App Bundle

Android App Bundles are the recommended way to build, publish, and distribute your app across multiple device configurations. App bundles also enable advanced features, such as Play Feature Delivery, Play Asset Delivery, and instant experiences. Whether you are just starting to adopt app bundles or are developing for more advanced use cases, this page provides an overview of the various strategies available for you to test your app at each stage of development.

If you are new to app bundles, read[About Android App Bundles](https://developer.android.com/guide/app-bundle).

## Build an app bundle using Android Studio

If you're using Android Studio, you can[build your project](https://developer.android.com/studio/run#reference)as a signed app bundle in just a few clicks. If you're not using the IDE, you can[build an app bundle from the command line](https://developer.android.com/studio/build/building-cmdline#build_bundle). Then,[upload your app bundle](https://developer.android.com/studio/publish/upload-bundle)to the Play Console to test or publish your app.

To build app bundles, follow these steps:

1. [Download Android Studio 3.2 or higher](https://developer.android.com/studio)---it's the easiest way to add feature modules and build app bundles.

2. [Build an Android App Bundle](https://developer.android.com/studio/run#reference)using Android Studio. You can also deploy your app to a connected device from an app bundle by[modifying your run/debug configuration](https://developer.android.com/studio/run/rundebugconfig#android-application)and selecting the option to deploy**APK from app bundle**. Keep in mind, using this option results in longer build times when compared to building and deploying only an APK.

   - If you're not using the IDE, you can instead[build an app bundle from the command line](https://developer.android.com/studio/build/building-cmdline#build_bundle).
3. [Deploy your Android App Bundle](https://developer.android.com/guide/app-bundle/test#deploy-using-studio)by using it to generate APKs that you deploy to a device.

4. [Enroll into app Play App Signing](https://support.google.com/googleplay/android-developer/answer/7384423). Otherwise, you can't upload your app bundle to the Play Console.

5. [Publish your app bundle to Google Play](https://developer.android.com/studio/publish/upload-bundle).

## Deploy using app bundles with Android Studio

You can build your app as an Android App Bundle and deploy it to a connected device right from the IDE. Because the IDE and Google Play use the same tools to extract and install APKs on a device, this local testing strategy helps you to verify the following:

- You can build your app as an app bundle.
- The IDE is able to extract APKs for a target device configuration from the app bundle.
- Features that you separate into feature modules are compatible with your app's base module.
- Your app functions on the target device as you expect.

| **Note:** If you are interested only in building an app bundle using Android Studio, read[Build your project](https://developer.android.com/studio/run#reference).

By default, when you deploy your app from Android Studio to a connected device, the IDE builds and deploys APKs for the target device configuration. That's because building APKs for a particular device configuration is faster than building an app bundle for all device configurations your app supports.

If you want to test building your app as an app bundle, and then deploying APKs from that app bundle to your connected device, you need to[edit the default Run/Debug configuration](https://developer.android.com/studio/run/rundebugconfig)as follows:

1. Select**Run \> Edit Configurations**from the menu bar.
2. Select a run/debug configuration from the left pane.
3. In the right pane, select the**General**tab.
4. Select**APK from app bundle** from the dropdown menu next to**Deploy**.
5. If your app includes an instant app experience that you want to test, check the box next to**Deploy as an instant app**.
6. If your app includes feature modules, you can select which modules you want to deploy by checking the box next to each module. By default, Android Studio deploys all feature modules and always deploys the base app module.
7. Click**Apply** or**OK**.

When you select**Run \> Run**from the menu bar, Android Studio builds an app bundle and uses it to deploy only the APKs required by the connected device and feature modules you selected.

## Build and test from the command line

The tools that Android Studio and Google Play use to build your app bundle and convert it into APKs are available to you from the command line. That is, you can invoke these tools from the command line to locally build and deploy your app from an Android App Bundle.

These local testing tools are useful for the following:

- Integrating configurable builds of app bundles into your Continuous Integration (CI) server or other custom build environment.
- Automating deployment your app from an app bundle to one or more connected test devices.
- Emulating downloads of your app from Google Play onto a connected device.

### Build an app bundle from the command line

If you want to build your app bundle from the command line, you can do so using either`bundletool`or the Android Gradle plugin.

**Android Gradle plugin:** Authored by Google, this plugin comes bundled with Android Studio and is also available as a Maven repository. The plugin defines commands that you can execute from the command line to build an app bundle. While the plugin provides the easiest method of building your app bundle, you'll need to use it via`bundletool`to deploy your app to a test device.

**`bundletool`:** This command-line tool is what both the Android Gradle plugin and Google Play use to build your app as an app bundle, and it's[available from GitHub](https://github.com/google/bundletool). Keep in mind, using`bundletool`to build your app bundle is a lot more complicated than simply running a Gradle task using the plugin. That's because the plugin automates certain prerequisites to building an app bundle. However, this tool is useful for developers who want to generate app bundle artifacts in their CI workflow.

To get started building your app bundle with either approach, read[Build your app from the command line](https://developer.android.com/studio/build/building-cmdline#build_bundle).

### Deploy your app from the command line

Although the Android Gradle plugin is the easiest way to build your app bundle from the command line, you should use`bundletool`to deploy your app from an app bundle to a connected device. That's because`bundletool`provides commands designed specifically to help you test your app bundle and emulate distribution through Google Play.

The following are the different types of scenarios you can test for using`bundletool`:

- [Generate an APK set](https://developer.android.com/studio/command-line/bundletool#generate_apks)that includes split APKs for all device configurations your app supports. Building an APK set is typically required before`bundletool`can deploy your app to a connected device.
  - If you don't want to build a set of all your app's split APKs, you can[generate a device-specific set of APKs](https://developer.android.com/studio/command-line/bundletool#device_specific_apks)based on a connected device or device specification JSON.
- [Deploy your app](https://developer.android.com/studio/command-line/bundletool#deploy_with_bundletool)from an APK set to a connected device.`bundletool`uses adb to determine the split APKs required for each device configuration, and deploys only those APKs to the device. If you have multiple devices, you can also pass the device ID to`bundletool`to target a specific device.
- [Locally test feature delivery options](https://developer.android.com/guide/app-bundle/test/testing-fakesplitinstallmanager). You can use`bundletool`to emulate your device downloading and installing feature modules from Google Play, without actually publishing your app to the Play Console. This is helpful if you want to locally test how your app handles on-demand module download requests and failures.
- [Estimate your app's download size](https://developer.android.com/studio/command-line/bundletool#measure_size)for a given device configuration. This is helpful to better understand the user experience of downloading your app and checking whether your app meets the[compressed download size restriction](https://developer.android.com/guide/app-bundle#size_restrictions)for app bundles or[enabling instant experiences](https://developer.android.com/topic/google-play-instant/overview#reduce-size).

## Test your app bundle on Play

While the other testing strategies described on this page don't require you to upload your app to Play, testing using the Play Console provides the most accurate representation of the user experience. Whether you want to share your app with your internal stakeholders, your internal QA team, a closed group of alpha testers, or a wider audience of beta testers, the Play Console provides you with several testing strategies.

Use the Play Console to test your app for the following reasons:

- You want the most accurate representation of the user experience of downloading your app and, optionally, installing features on demand.
- You want to provide easy access to a group of testers.
- You want to scope tests to QA, alpha, and beta testers.
- You want to access a history of app uploads that you can test on a device. For example, if you want to compare versions for performance regressions.

### Quickly share your app with a URL

While the Play Console test tracks provide a method of progressing your app through formal testing stages, sometimes you want to quickly share your app with trusted testers over less formal channels, such as email or a text message.

By uploading your app bundle to the Play Console[quick sharing](https://play.google.com/console/internal-app-sharing/)page, you can generate a URL that you can easily share with others. Sharing your app this way provides these benefits:

- Authorize anyone on your team to upload test builds, without giving them access to your app in Play Console.
- Testers get access only to the specific test version of your app that was shared with them.
- Test builds can be signed with any key or not signed at all, so uploaders also don't need access to your production or upload key.
- Version codes don't need to be unique, so you can reuse an existing version code and don't need to increment it to upload.
- Test custom delivery options, such as downloading features on demand and[in-app updates](https://developer.android.com/guide/playcore/in-app-updates#internal-app-sharing).
- Capture important data and logs by sharing a debuggable version of your app.

When users click on the URL from their Android device, the device automatically opens the Google Play Store to download the test version of your app. To get started, and learn more about the capabilities and restrictions of this testing strategy, see[Share your app with a URL](https://support.google.com/googleplay/android-developer/answer/9303479)or watch the video below.  

### Download historical versions of your app

You and your testers can also download historical versions of your app that you've uploaded to a production or test track. This can be useful if, for example, you want to quickly test an earlier version of your app to check for performance regressions.

Visit the Play Console**Latest releases and bundles**page and navigate to the download tab of any version you want to download to copy the install link. Alternatively, if you know the package name and version code for the version of your app you want to test, simply visit the following link from your test device:  

```
https://play.google.com/apps/test/package-name/version-code
```
| **Note:** Only authorized users can access historical versions of your app. You can configure the set of authorized users in the Play Console on the quick sharing access tab.

### Upload your app to a test track

When you upload your app and create a release in the Play Console, you can progress your release through multiple testing stages before pushing to production:

- **Internal test:**Create an internal test release to quickly distribute your app for internal testing and quality assurance checks.
- **Closed:**Create a closed release to test pre-release versions of your app with a larger set of testers. Once you've tested with a smaller group of employees or trusted users, you can expand your test to an open release. On your App releases page, an Alpha track will be available as your initial closed test. If needed, you can also create and name additional closed tracks.
- **Open:**Create an open release after you've tested a closed release. Your open release can include a wider range of users for testing, before your app goes live in production.

Progressing your app through each of these testing stages allows you to open your app to wider audiences of testers before releasing your app to production. For more information on Play Console test tracks, go to[Set up an open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/3131213).

### Use pre-launch reports to identify issues

When you upload an APK or app bundle to the open or closed track, you can identify issues for a wide range of devices running different versions of Android.

The pre-launch report on your Play Console helps you identify potential issues with the following:

- Stability
- Android compatibility
- Performance
- Accessibility
- Security vulnerabilities

After you upload your app bundle, test devices automatically launch and crawl your app for several minutes. The crawl performs basic actions every few seconds on your app, such as typing, tapping, and swiping.

After tests are complete, your results will be available in the**pre-launch report** section of your Play Console. To learn more, see the Play Console help topic about how to[Use pre-launch reports to identify issues](https://support.google.com/googleplay/android-developer/answer/7002270).

### Browse and download APKs for specific device configurations

When you upload your app bundle, the Play Console automatically generates split APKs and multi-APKs for all device configurations your app supports. In the Play Console, you can use the**Latest releases and bundles**to see all APK artifacts that Google Play generates, inspect data such as supported devices and your app's delivery configuration, and download the generated APKs to deploy and test locally.

To learn more, read the Play Console help topic about[Reviewing your app bundle details](https://support.google.com/googleplay/android-developer/answer/9006925#review).

## Test your app bundle with Firebase App Distribution

[Firebase App Distribution](https://firebase.google.com/products/app-distribution)makes it easy to distribute pre-release versions of your app to trusted testers so you can get valuable feedback before launch.

App Distribution lets you manage all of your pre-release builds in a central hub, and it gives you the flexibility to distribute these builds right from the console or using the command-line tools that are already part of your workflow.

There are a few steps you need to take to enable your project for Firebase App Distribution. Check out the[Before you begin](https://firebase.google.com/docs/app-distribution/android/distribute-console?apptype=aab#before_you_begin)section of the Firebase documentation. After you've set up your project, choose how you want to integrate App Distribution with your workflow:

- [Using the command line](https://firebase.google.com/docs/app-distribution/android/distribute-cli?apptype=aab)
- [Using Gradle](https://firebase.google.com/docs/app-distribution/android/distribute-gradle?apptype=aab)
- [Using fastlane](https://firebase.google.com/docs/app-distribution/android/distribute-fastlane?apptype=aab)