---
title: https://developer.android.com/training/multiple-apks/screensize
url: https://developer.android.com/training/multiple-apks/screensize
source: md.txt
---

# Create multiple APKs for different screen sizes

If you publish your app to Google Play, you should build and upload an[Android App Bundle](https://developer.android.com/guide/app-bundle). When you do so, Google Play automatically generates and serves optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. Publishing multiple APKs is useful if you are not publishing to Google Play, but you must build, sign, and manage each APK yourself.

When developing your Android application to take advantage of multiple APKs on Google Play, it's important to adopt some good practices from the get-go, and prevent unnecessary headaches further into the development process. This lesson shows you how to create multiple APKs of your app, each covering a different class of screen size. You will also gain some tools necessary to make maintaining a multiple APK codebase as painless as possible.

## Confirm you need multiple APKs

When trying to create an application that works across multiple sizes of Android devices, naturally you want your application to take advantage of all the available space on larger devices, without sacrificing compatibility or usability on the smaller screens. It may seem at the outset as though multiple APK support is the best solution, but this often isn't the case. The[Using Single APK Instead](https://developer.android.com/google/play/publishing/multiple-apks#ApiLevelOptions)section of the multiple APK developer guide includes some useful information on how to accomplish this with a single APK, including use of our support library. You should also read the guide to[supporting multiple screens](https://developer.android.com/guide/practices/screens_support), and there's even a[support library](http://android-developers.blogspot.com/2011/03/fragments-for-all.html)you can download using the Android SDK, which lets you use fragments on pre-Honeycomb devices (making multiple-screen support in a single APK much easier).

If you can manage it, confining your application to a single APK has several advantages, including:

- Publishing and testing are easier
- There's only one codebase to maintain
- Your application can adapt to device configuration changes
- App restore across devices just works
- You don't have to worry about market preference, behavior from "upgrades" from one APK to the next, or which APK goes with which class of devices

The rest of this lesson assumes that you've researched the topic, studiously absorbed the material in the resources linked, and determined that multiple APKs are the right path for your application.

## Chart your requirements

Start off by creating a simple chart to quickly determine how many APKs you need, and what screen size(s) each APK covers. Fortunately, it's easy to chart out your requirements quickly and easily, and have a reference for later. Start out with a row of cells representing the various screen sizes available on the Android platform.

|-------|--------|-------|--------|
| small | normal | large | xlarge |

Now just color in the chart such that each color represents an APK. Here's one example of how you might apply each APK to a certain range of screen sizes.

|-------|--------|-------|--------|
| small | normal | large | xlarge |

Depending on your needs, you could also have two APKs, "small and everything else" or "xlarge and everything else". Coloring in the chart also makes intra-team communication easier---You can now simply refer to each APK as "blue", "green", or "red", no matter how many different screen types it covers.

## Put all common code and resources in a library project

Whether you're modifying an existing Android application or starting one from scratch, this is the first thing that you should do to the codebase, and by the far the most important. Everything that goes into the library project only needs to be updated once (think language-localized strings, color themes, bugs fixed in shared code), which improves your development time and reduces the likelihood of mistakes that could have been easily avoided.

**Note:** While the implementation details of how to create and include library projects are beyond the scope of this lesson, you can get up to speed by reading[Create an Android Library](https://developer.android.com/studio/projects/android-library).

If you're converting an existing application to use multiple APK support, scour your codebase for every localized string file, list of values, theme colors, menu icons and layout that isn't going to change across APKs, and put it all in the library project. Code that isn't going to change much should also go in the library project. You'll likely find yourself extending these classes to add a method or two from APK to APK.

If, on the other hand, you're creating the application from scratch, try as much as possible to write code in the library project*first*, then only move it down to an individual APK if necessary. This is much easier to manage in the long run than adding it to one, then another, then another, then months later trying to figure out whether this blob can be moved up to the library section without screwing anything up.

## Create new APK projects

There should be a separate Android project for each APK you're going to release. For easy organization, place the library project and all related APK projects under the same parent folder. Also remember that each APK needs to have the same package name, although they don't necessarily need to share the package name with the library. If you were to have 3 APKs following the scheme described earlier, your root directory might look like this:  

```
alexlucas:~/code/multi-apks-root$ ls
foo-blue
foo-green
foo-lib
foo-red
```

Once the projects are created, add the library project as a reference to each APK project. If possible, define your starting Activity in the library project, and extend that Activity in your APK project. Having a starting activity defined in the library project gives you a chance to put all your application initialization in one place, so that each individual APK doesn't have to re-implement "universal" tasks like initializing Analytics, running licensing checks, and any other initialization procedures that don't change much from APK to APK.

## Adjust the manifests

When a user downloads an application which uses multiple APKs through Google Play, the correct APK to use is chosen using two simple rules:

- The manifest has to show that particular APK is eligible
- Of the eligible APKs, highest version number wins

By way of example, let's take the set of multiple APKs described earlier, and assume that each APK has been set to support all screen sizes larger than its "target" screen size. Taken individually, the possible range of each APK would look like this:

|-------|--------|-------|--------|
| small | normal | large | xlarge |
| small | normal | large | xlarge |
| small | normal | large | xlarge |

However, by using the "highest version number wins" rule, if we set the versionCode attribute in each APK such that red ≥ green ≥ blue, the chart effectively collapses down to this:

|-------|--------|-------|--------|
| small | normal | large | xlarge |

Now, let's further assume that the Red APK has some requirement on it that the other two don't. The[Filters on Google Play](https://developer.android.com/google/play/filters)page of the Android Developer guide has a whole list of possible culprits. For the sake of example, let's assume that red requires a front-facing camera. In fact, the entire point of the red APK is to use the extra available screen space to do entertaining things with that front-facing camera. But, it turns out, not all xlarge devices even HAVE front-facing cameras! The horror!

Fortunately, if a user is browsing Google Play from one such device, Google Play will look at the manifest, see that Red lists the front-facing camera as a requirement, and quietly ignore it, having determined that Red and that device are not a match made in digital heaven. It will then see that Green is not only compatible with xlarge devices, but also doesn't care whether or not there's a front-facing camera! The app can still be downloaded from Google Play by the user, because despite the whole front-camera mishap, there was still an APK that supported that particular screen size.

In order to keep all your APKs on separate "tracks", it's important to have a good version code scheme. The recommended one can be found on the[Version Codes](https://developer.android.com/google/play/publishing/multiple-apks#VersionCodes)area of our developer guide. Since the example set of APKs is only dealing with one of 3 possible dimensions, it would be sufficient to separate each APK by 1000 and increment from there. This might look like:

Blue: 1001, 1002, 1003, 1004...  
Green: 2001, 2002, 2003, 2004...  
Red:3001, 3002, 3003, 3004...

Putting this all together, your Android Manifests would likely look something like the following:

Blue:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="1001" android:versionName="1.0" package="com.example.foo">
    <supports-screens android:smallScreens="true"
        android:normalScreens="true"
        android:largeScreens="true"
        android:xlargeScreens="true" />
    ...
```

Green:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="2001" android:versionName="1.0" package="com.example.foo">
    <supports-screens android:smallScreens="false"
        android:normalScreens="false"
        android:largeScreens="true"
        android:xlargeScreens="true" />
    ...
```

Red:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="3001" android:versionName="1.0" package="com.example.foo">
    <supports-screens android:smallScreens="false"
        android:normalScreens="false"
        android:largeScreens="false"
        android:xlargeScreens="true" />
    ...
```

Note that technically, multiple APK's will work with either the supports-screens tag, or the compatible-screens tag. Supports-screens is generally preferred, and it's generally a really bad idea to use both tags in the same manifest. It makes things needlessly complicated, and increases the opportunity for errors. Also note that instead of taking advantage of the default values (small and normal are always true by default), the manifests explicitly set the value for each screen size. This can save you headaches down the line. For instance, a manifest with a target SDK of \< 9 will have xlarge automatically set to false, since that size didn't exist yet. So be explicit!

## Review your pre-launch checklist

Before uploading to Google Play, double-check the following items. Remember that these are specifically relevant to multiple APKs, and in no way represent a complete checklist for all applications being uploaded to Google Play.

- All APKs must have the same package name
- All APKs must be signed with the same certificate
- Every screen size you want your APK to support, set to true in the manifest. Every screen size you want it to avoid, set to false
- Double check your manifest filters for conflicting information (an APK that only supports cupcake on XLARGE screens isn't going to be seen by anybody)
- Each APK's manifest must be unique across at least one of supported screen, openGL texture, or platform version
- Try to test each APK on at least one device. Barring that, you have one of the most customizable device emulators in the business sitting on your development machine. Go nuts!

It's also worth inspecting the compiled APK before pushing to market, to make sure there aren't any surprises that could hide your application on Google Play. This is actually quite simple using the "aapt" tool. Aapt (the Android Asset Packaging Tool) is part of the build process for creating and packaging your Android applications, and is also a very handy tool for inspecting them.  

```
>aapt dump badging
package: name='com.example.hello' versionCode='1' versionName='1.0'
sdkVersion:'11'
uses-permission:'android.permission.SEND_SMS'
application-label:'Hello'
application-icon-120:'res/drawable-ldpi/icon.png'
application-icon-160:'res/drawable-mdpi/icon.png'
application-icon-240:'res/drawable-hdpi/icon.png'
application: label='Hello' icon='res/drawable-mdpi/icon.png'
launchable-activity: name='com.example.hello.HelloActivity'  label='Hello' icon=''
uses-feature:'android.hardware.telephony'
uses-feature:'android.hardware.touchscreen'
main
supports-screens: 'xlarge'
supports-any-density: 'true'
locales: '--_--'
densities: '120' '160' '240'
```

When you examine aapt output, be sure to check that you don't have conflicting values for supports-screens and compatible-screens, and that you don't have unintended "uses-feature" values that were added as a result of permissions you set in the manifest. In the example above, the APK will be invisible to most, if not all devices.

Why? By adding the required permission SEND_SMS, the feature requirement of android.hardware.telephony was implicitly added. Since most (if not all) xlarge devices are tablets without telephony hardware in them, Google Play will filter out this APK in these cases, until future devices come along which are both large enough to report as xlarge screen size, and possess telephony hardware.

Fortunately this is easily fixed by adding the following to your manifest:  

```xml
<uses-feature android:name="android.hardware.telephony" android:required="false" />
```

The`android.hardware.touchscreen`requirement is also implicitly added. If you want your APK to be visible on TVs which are non-touchscreen devices you should add the following to your manifest:  

```xml
<uses-feature android:name="android.hardware.touchscreen" android:required="false" />
```

Once you've completed the pre-launch checklist, upload your APKs to Google Play. It may take a bit for the application to show up when browsing Google Play, but when it does, perform one last check. Download the application onto any test devices you may have to make sure that the APKs are targeting the intended devices.

For more information about publishing multiple APKs on Google Play, read[Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks).