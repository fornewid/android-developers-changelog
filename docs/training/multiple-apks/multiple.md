---
title: https://developer.android.com/training/multiple-apks/multiple
url: https://developer.android.com/training/multiple-apks/multiple
source: md.txt
---

# Creating multiple APKs with several dimensions

If you publish your app to Google Play, you should build and upload an[Android App Bundle](https://developer.android.com/guide/app-bundle). When you do so, Google Play automatically generates and serves optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. Publishing multiple APKs is useful if you are not publishing to Google Play, but you must build, sign, and manage each APK yourself.

When developing your Android application to take advantage of multiple APKs on Google Play, it's important to adopt some good practices from the get-go, and prevent unnecessary headaches further into the development process. This lesson shows you how to create multiple APKs of your app, each covering a different class of screen size. You will also gain some tools necessary to make maintaining a multiple APK codebase as painless as possible.

## Confirm you need multiple APKs

When trying to create an application that works across the huge range of available Android devices, naturally you want your application look its best on each individual device. You want to take advantage of the space of large screens but still work on small ones, to use new Android API features or visual textures available on cutting edge devices but not abandon older ones. It may seem at the outset as though multiple APK support is the best solution, but this often isn't the case. The[Using Single APK Instead](https://developer.android.com/google/play/publishing/multiple-apks#ApiLevelOptions)section of the multiple APK guide includes some useful information on how to accomplish all of this with a single APK, including use of our[support library](http://android-developers.blogspot.com/2011/03/fragments-for-all.html), and links to resources throughout the Android Developer guide.

If you can manage it, confining your application to a single APK has several advantages, including:

- Publishing and Testing are easier
- There's only one codebase to maintain
- Your application can adapt to device configuration changes
- App restore across devices just works
- You don't have to worry about market preference, behavior from "upgrades" from one APK to the next, or which APK goes with which class of devices

The rest of this lesson assumes that you've researched the topic, studiously absorbed the material in the resources linked, and determined that multiple APKs are the right path for your application.

## Chart your requirements

Start off by creating a simple chart to quickly determine how many APKs you need, and what screen size(s) each APK covers. Fortunately, it's easy to chart out your requirements quickly, easily, and have an easy reference for later. Let's say you want to split your APKs across two dimensions, API and screen size. Create a table with a row and column for each possible pair of values, and color in some "blobs", each color representing one APK.

|--------|---|---|---|---|---|---|---|----|----|----|---|
|        | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | + |
| small  |   |   |   |   |   |   |   |    |    |    |   |
| normal |   |   |   |   |   |   |   |    |    |    |   |
| large  |   |   |   |   |   |   |   |    |    |    |   |
| xlarge |   |   |   |   |   |   |   |    |    |    |   |

Above is an example with four APKs. Blue is for all small/normal screen devices, Green is for large screen devices, and Red is for xlarge screen devices, all with an API range of 3-10. Purple is a special case, as it's for all screen sizes, but only for API 11 and up. More importantly, just by glancing at this chart, you immediately know which APK covers any given API/screen-size combo. To boot, you also have swanky codenames for each one, since "Have we tested red on the ?" is a lot easier to ask your cubie than "Have we tested the 3-to-10 xlarge APK against the Xoom?" Print this chart out and hand it to every person working on your codebase. Life just got a lot easier.

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
foo-purple
foo-red
```

Once the projects are created, add the library project as a reference to each APK project. If possible, define your starting Activity in the library project, and extend that Activity in your APK project. Having a starting activity defined in the library project gives you a chance to put all your application initialization in one place, so that each individual APK doesn't have to re-implement "universal" tasks like initializing Analytics, running licensing checks, and any other initialization procedures that don't change much from APK to APK.

## Adjust the manifests

When a user downloads an application which uses multiple APKs through Google Play, the correct APK to use is chosen using two simple rules:

- The manifest has to show that particular APK is eligible
- Of the eligible APKs, highest version number wins.

By way of example, let's take the set of multiple APKs described earlier, and assume that each APK has been set to support all screen sizes larger than its "target" screen size. Let's look at the sample chart from earlier:

|--------|---|---|---|---|---|---|---|----|----|----|---|
|        | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | + |
| small  |   |   |   |   |   |   |   |    |    |    |   |
| normal |   |   |   |   |   |   |   |    |    |    |   |
| large  |   |   |   |   |   |   |   |    |    |    |   |
| xlarge |   |   |   |   |   |   |   |    |    |    |   |

Since it's okay for coverage to overlap, we can describe the area covered by each APK like so:

- Blue covers all screens, minSDK 3.
- Green covers Large screens and higher, minSDK 3.
- Red covers XLarge screens (generally tablets), minSDK of 9.
- Purple covers all screens, minSDK of 11.

Note that there's a*lot*of overlap in those rules. For instance, an XLarge device with API 11 can conceivably run any one of the 4 APKs specified. However, by using the "highest version number wins" rule, we can set an order of preference as follows:

Purple ≥ Red ≥ Green ≥ Blue

Why allow all the overlap? Let's pretend that the Purple APK has some requirement on it that the other two don't. The[Filters on Google Play](https://developer.android.com/google/play/filters)page of the Android Developer guide has a whole list of possible culprits. For the sake of example, let's assume that Purple requires a front-facing camera. In fact, the entire point of Purple is to use entertaining things with the front-facing camera! But, it turns out, not all API 11+ devices even HAVE front-facing cameras! The horror!

Fortunately, if a user is browsing Google Play from one such device, Google Play will look at the manifest, see that Purple lists the front-facing camera as a requirement, and quietly ignore it, having determined that Purple and that device are not a match made in digital heaven. It will then see that Red is not only compatible with xlarge devices, but also doesn't care whether or not there's a front-facing camera! The app can still be downloaded from Google Play by the user, because despite the whole front-camera mishap, there was still an APK that supported that particular API level.

In order to keep all your APKs on separate "tracks", it's important to have a good version code scheme. The recommended one can be found on the[Version Codes](https://developer.android.com/google/play/publishing/multiple-apks#VersionCodes)area of our developer guide. It's worth reading the whole section, but the basic gist is for this set of APKs, we'd use two digits to represent the minSDK, two to represent the min/max screen size, and 3 to represent the build number. That way, when the device upgraded to a new version of Android, (say, from 10 to 11), any APKs that are now eligible and preferred over the currently installed one would be seen by the device as an "upgrade". The version number scheme, when applied to the example set of APKs, might look like:

Blue: 0304001, 0304002, 0304003...  
Green: 0334001, 0334002, 0334003  
Red: 0344001, 0344002, 0344003...  
Purple: 1104001, 1104002, 1104003...  

Putting this all together, your Android Manifests would likely look something like the following:

Blue:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="0304001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="3" />
    <supports-screens android:smallScreens="true"
        android:normalScreens="true"
        android:largeScreens="true"
        android:xlargeScreens="true" />
    ...
```

Green:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="0334001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="3" />
    <supports-screens android:smallScreens="false"
        android:normalScreens="false"
        android:largeScreens="true"
        android:xlargeScreens="true" />
    ...
```

Red:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="0344001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="3" />
    <supports-screens android:smallScreens="false"
        android:normalScreens="false"
        android:largeScreens="false"
        android:xlargeScreens="true" />
    ...
```

Purple:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="1104001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="11" />
    <supports-screens android:smallScreens="true"
        android:normalScreens="true"
        android:largeScreens="true"
        android:xlargeScreens="true" />
    ...
```

Note that technically, multiple APK's will work with either the supports-screens tag, or the compatible-screens tag. Supports-screens is generally preferred, and it's generally a really bad idea to use both- It makes things needlessly complicated, and increases the opportunity for errors. Also note that instead of taking advantage of the default values (small and normal are always true by default), the manifests explicitly set the value for each screen size. This can save you headaches down the line - By way of example, a manifest with a target SDK of \< 9 will have xlarge automatically set to false, since that size didn't exist yet. So be explicit!

## Review your pre-launch checklist

Before uploading to Google Play, double-check the following items. Remember that these are specifically relevant to multiple APKs, and in no way represent a complete checklist for all applications being uploaded to Google Play.

- All APKs must have the same package name.
- All APKs must be signed with the same certificate.
- If the APKs overlap in platform version, the one with the higher minSdkVersion must have a higher version code.
- Every screen size you want your APK to support, set to true in the manifest. Every screen size you want it to avoid, set to false.
- Double check your manifest filters for conflicting information (an APK that only supports cupcake on XLARGE screens isn't going to be seen by anybody)
- Each APK's manifest must be unique across at least one of supported screen, OpenGL texture, or platform version.
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

<br />

```xml
<uses-feature android:name="android.hardware.telephony" android:required="false" />
```

The`android.hardware.touchscreen`requirement is also implicitly added. If you want your APK to be visible on TVs which are non-touchscreen devices you should add the following to your manifest:  

```xml
<uses-feature android:name="android.hardware.touchscreen" android:required="false" />
```

Once you've completed the pre-launch checklist, upload your APKs to Google Play. It may take a bit for the application to show up when browsing Google Play, but when it does, perform one last check. Download the application onto any test devices you may have to make sure that the APKs are targeting the intended devices. Congratulations, you're done!