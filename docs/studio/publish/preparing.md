---
title: https://developer.android.com/studio/publish/preparing
url: https://developer.android.com/studio/publish/preparing
source: md.txt
---

# Prepare your app for release

| Android developer verification is a new requirement designed to link individuals and organizations to their Android apps. Starting in 2026, Android will require all apps to be registered by verified developers in order to be installed by users on certified Android devices. To learn what you need to do, see[Android developer verification](https://developer.android.com/developer-verification/guides).

To prepare your app for release, you need to configure, build, and test a release version of your app. The configuration tasks involve basic code cleanup and code modification tasks that help optimize your app. The build process is similar to the debug build process and can be done using JDK and Android SDK tools.

Testing tasks serve as a final check, helping ensure that your app performs as expected under real-world conditions. Firebase offers a large set of both physical and virtual test devices through[Firebase Test Lab](https://firebase.google.com/products/test-lab)that you can use to improve your app quality.

When you are finished preparing your app for release, you have a signed APK file, which you can distribute directly to users or distribute through an app marketplace such as[Google Play](https://play.google.com).

This document summarizes the main tasks you need to perform to prepare your app for release. The tasks described on this page apply to all Android apps, regardless of how they are released or distributed to users. If you are releasing your app through Google Play, read[Release with confidence](https://developer.android.com/distribute/best-practices/launch/launch-checklist).

**Note:**As a best practice, make sure your app meets all of your release criteria for functionality, performance, and stability before you perform the tasks outlined on this page.
![Shows how the preparation process fits into the development process](https://developer.android.com/static/images/publishing/publishing_overview_prep.png)

**Figure 1.**Preparing for release is a required development task and is the first step in the publishing process.

## Tasks to prepare for release

To release your app to users, you need to create a release-ready package that users can install and run on their Android-powered devices. The release-ready package contains the same components as the debug APK file---compiled source code, resources, manifest file, and so on---and is built using the same build tools. However, unlike the debug APK file, the release-ready APK file is signed with your own certificate and is optimized with the`zipalign`tool.  
![Shows the five tasks you perform to prepare your app for release](https://developer.android.com/static/images/publishing/publishing_preparing.png)

**Figure 2.**There are five main tasks to prepare your app for release.

The signing and optimization tasks are usually seamless if you are building your app with Android Studio. For example, you can use Android Studio with the Gradle build files to compile, sign, and optimize your app all at once. You can also configure the Gradle build files to do the same when you build from the command line. For more details about using the Gradle build files, see[Configure your build](https://developer.android.com/studio/build).

To prepare your app for release, you typically perform five main tasks, as shown in figure 2. Each main task may include one or more smaller tasks, depending on how you are releasing your app. For example, if you are releasing your app through Google Play, you may want to add special filtering rules to your manifest while you are configuring your app for release. Similarly, to meet Google Play publishing guidelines you may have to prepare screenshots and create promotional text while you are gathering materials for release.

You usually perform the tasks listed in figure 2 after you have throroughly debugged and tested your app. The Android SDK contains several tools to help you test and debug your Android apps. For more information, see[Debug your app](https://developer.android.com/tools/debugging)and[Test your app](https://developer.android.com/tools/testing).

## Gather materials and resources

To prepare your app for release, you need to gather several supporting items. At a minimum, this includes cryptographic keys for signing your app and an app icon. You might also want to include an end-user license agreement.

### Cryptographic keys

Android requires that all APKs are digitally signed with a certificate before they are installed on a device or updated. For[Google Play Store](https://play.google.com), all apps created after August 2021 are required to use[Play App Signing](https://developer.android.com/studio/publish/app-signing#app-signing-google-play). But uploading your AAB to Play Console still requires you to sign it with your developer certificate. Older apps can still self-sign, but whether you're using Play App Signing or you're self-signing, you must sign your app before you can upload it.

To learn about certificate requirements, see[Sign your app](https://developer.android.com/tools/publishing/app-signing).

**Important:**Your app must be signed with a cryptographic key that has a validity period ending after October 22, 2033.

You might also have to obtain other release keys if your app accesses a service or uses a third-party library that requires you to use a key that is based on your private key.

### App icon

Your app's icon helps users identify your app on a device's Home screen and in the Launcher window. It also appears in Manage Applications, My Downloads, and elsewhere. In addition, publishing services such as Google Play display your icon to users. Be sure you have an app icon and that it meets the recommended[icon guidelines](https://material.io/design/iconography/product-icons.html#design-principles).

**Note:** If you are releasing your app on Google Play, you need to create a high-resolution version of your icon. See[Add preview assests to showcase your app](https://www.google.com/support/androidmarket/developer/bin/answer.py?answer=1078870)for more information.

### End-user license agreement

Consider preparing an end-user license agreement (EULA) for your app. A EULA can help protect your person, organization, and intellectual property, and we recommend that you provide one with your app.

### Miscellaneous materials

You might also have to prepare promotional and marketing materials to publicize your app. For example, if you are releasing your app on Google Play, you will need to prepare some promotional text and you will need to create screenshots of your app. For more information, see[Add preview assets to showcase your app](https://www.google.com/support/androidmarket/developer/bin/answer.py?answer=1078870).

## Configure your app for release

After you gather all of your supporting materials, you can start configuring your app for release. This section provides a summary of the configuration changes we recommend that you make to your source code, resource files, and app manifest prior to releasing your app.

Although most of the configuration changes listed in this section are optional, they are considered good coding practices and we encourage you to implement them. In some cases, you might already have made these configuration changes as part of your development process.

### Choose a suitable application ID

Make sure you choose an application ID that is suitable over the life of your app. You can't change the application ID after you distribute your app to users. To set it, use the`applicationId`property in the module-level`build.gradle`or`build.gradle.kts`file. For more information, see[Set the application ID](https://developer.android.com/studio/build/configure-app-module#set-application-id).

### Turn off debugging

To configure whether the APK is debuggable, use the`debuggable`flag for Groovy or the`isDebuggable`flag for Kotlin script:

<br />

### Kotlin

```kotlin
  android {
    ...
    buildTypes {
      release {
        isDebuggable = false
        ...
      }
      debug {
        isDebuggable = true
        ...
      }
    }
    ...
  }
  
```

### Groovy

```groovy
  android {
    ...
    buildTypes {
      release {
        debuggable false
        ...
      }
      debug {
        debuggable true
        ...
      }
    }
    ...
  }
```

### Enable and configure app shrinking

Many of the following optimizations can be automated by enabling[shrinking](https://developer.android.com/studio/build/shrink-code)for your release build. For example, you can add ProGuard rules to remove log statements, and the shrinker will identify and remove unused code and resources. The shrinker can also replace class and variable names with shorter names to further reduce DEX size.

### Turn off logging

Deactivate logging before you build your app for release. You can deactivate logging by removing calls to[Log](https://developer.android.com/reference/android/util/Log)methods in your source files. Also, remove any log files or static test files that were created in your project.

Also, remove all[Debug](https://developer.android.com/reference/android/os/Debug)tracing calls that you added to your code, such as[startMethodTracing()](https://developer.android.com/reference/android/os/Debug#startMethodTracing())and[stopMethodTracing()](https://developer.android.com/reference/android/os/Debug#stopMethodTracing())method calls.

**Important:** Ensure that you disable debugging for your app if using[WebView](https://developer.android.com/reference/android/webkit/WebView)to display paid content or if using JavaScript interfaces, because debugging lets users inject scripts and extract content using Chrome DevTools. To disable debugging, use the[WebView.setWebContentsDebuggingEnabled()](https://developer.android.com/reference/android/webkit/WebView#setWebContentsDebuggingEnabled(boolean))method.

### Clean up your project directories

Clean up your project and make sure it conforms to the directory structure described in[Projects overview](https://developer.android.com/tools/projects#ApplicationProjects). Leaving stray or orphaned files in your project can prevent your app from compiling and cause your app to behave unpredictably. At a minimum, perform the following cleanup tasks:

- Review the contents of your`cpp/`,`lib/`, and`src/`directories. The`cpp/`directory should contain only source files associated with the[Android NDK](https://developer.android.com/tools/sdk/ndk), such as C or C++ source files, header files, or makefiles. The`lib/`directory should contain only third-party library files or private library files, including prebuilt shared and static libraries. The`src/`directory should contain only the source files for your app (Java, Kotlin, and AIDL files). The`src/`directory should not contain any JAR files.
- Check your project for private or proprietary data files that your app doesn't use and remove them. For example, look in your project's`res/`directory for old drawable files, layout files, and values files that you are no longer using and delete them.
- Check your`lib/`directory for test libraries and remove them if they are no longer being used by your app.
- Review the contents of your`assets/`directory and your`res/raw/`directory for raw asset files and static files that you need to update or remove prior to release.

### Review and update your manifest and Gradle build settings

Verify that the following manifest and build files items are set correctly:

- [<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element)element

  Specify only those permissions that are relevant and required for your app.
- `android:icon`and`android:label`attributes

  You must specify values for these attributes, which are located in the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element.
- `versionCode`and`versionName`properties

  We recommend that you specify values for these properties, which are located in the app module-level`build.gradle`or`build.gradle.kts`file. For more information, see[Version your app](https://developer.android.com/tools/publishing/versioning).

There are several additional build file elements that you can set if you are releasing your app on Google Play. For example, the`minSdk`and`targetSdk`attributes, which are located in the app module-level`build.gradle`or`build.gradle.kts`file. For more information about these and other Google Play settings, see[Filters on Google Play](https://developer.android.com/google/play/filters).

### Address compatibility issues

Android provides several tools and techniques to make your app compatible with a wide range of devices. To make your app available to the largest number of users, consider doing the following:

Add support for multiple screen configurations.
:   Make sure you meet the best practices for[supporting multiple screens](https://developer.android.com/guide/practices/screens_support#screen-independence). By supporting multiple screen configurations, you can create an app that functions properly and looks good on any of the screen sizes supported by Android.

Optimize your app for larger displays.
:   You can optimize your app to work well on devices with large displays such as tablets and foldables. For example,[list-detail layouts](https://developer.android.com/guide/topics/large-screens/large-screen-canonical-layouts#list-detail)can improve usability on larger screens.

Consider using Jetpack libraries.
:   Jetpack is a suite of libraries to help developers follow best practices, reduce boilerplate code, and write code that works consistently across Android versions and devices.

### Update URLs for servers and services

If your app accesses remote servers or services, make sure you are using the production URL or path for the server or service and not a test URL or path.

### Implement licensing for Google Play

If you are releasing a paid app through Google Play, consider adding support for Google Play Licensing. Licensing lets you control access to your app based on whether the current user has purchased it. Using Google Play Licensing is optional, even if you are releasing your app through Google Play.

For more information about the Google Play Licensing Service and how to use it in your app, see[App Licensing](https://developer.android.com/google/play/licensing).

## Build your app for release

After you finish configuring your app, you can build it into a release-ready APK file that is signed and optimized. The JDK includes the tools for signing the APK file (Keytool and Jarsigner); the Android SDK includes the tools for compiling and optimizing the APK file. If you are using Android Studio or you are using the Gradle build system from the command line, you can automate the entire build process. For more information about configuring Gradle builds, see[Configure build variants](https://developer.android.com/tools/building/configuring-gradle).

If you are using a[continuous integration system](https://developer.android.com/studio/projects/continuous-integration), you can configure a task to automate your release process. This is not limited to building your release APK or AAB. You can also configure it to automatically upload the build artifact(s) to Play Console.

### Build with Android Studio

You can use the Gradle build system, integrated with Android Studio, to build a release-ready APK file that is signed with your private key and optimized. To learn how to set up and run builds from Android Studio, see[Build and run your app](https://developer.android.com/tools/building/building-studio).

The build process assumes that you have a certificate and private key suitable for signing your app. If you don't have a suitable certificate and private key, Android Studio can help you generate one. For more information about the signing process, see[Sign your app](https://developer.android.com/tools/publishing/app-signing).

## Prepare external servers and resources

If your app relies on a remote server, make sure the server is secure and that it is configured for production use. This is particularly important if you are implementing[in-app billing](https://developer.android.com/google/play/billing)in your app and you are performing the signature verification step on a remote server.

Also, if your app fetches content from a remote server or a real-time service (such as a content feed), be sure the content you are providing is up to date and production ready.

## Test your app for release

Testing the release version of your app helps ensure that your app runs properly under realistic device and network conditions. Ideally, test your app on at least one handset-sized device and one tablet-sized device to verify that your user interface elements are sized correctly and that your app's performance and battery efficiency are acceptable.[Firebase Test Lab](https://firebase.google.com/docs/test-lab)can also be useful for testing across a variety of different devices and Android OS versions.

As a starting point for testing, see[Core app quality](https://developer.android.com/tools/testing/what_to_test). When you are done testing and satisfied that the release version of your app behaves correctly, you can release your app to users. For more information, see[Release your app to users](https://developer.android.com/tools/publishing/publishing_overview#publishing-release).