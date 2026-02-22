---
title: https://developer.android.com/training/multiple-apks/api
url: https://developer.android.com/training/multiple-apks/api
source: md.txt
---

# Create multiple APKs for different API levels

If you publish your app to Google Play, you should build and upload an[Android App Bundle](https://developer.android.com/guide/app-bundle). When you do so, Google Play automatically generates and serves optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. Publishing multiple APKs is useful if you are not publishing to Google Play, but you must build, sign, and manage each APK yourself.

When developing your Android application to take advantage of multiple APKs on Google Play, it's important to adopt some good practices from the get-go, and prevent unnecessary headaches further into the development process. This lesson shows you how to create multiple APKs of your app, each covering a slightly different range of API levels. You will also gain some tools necessary to make maintaining a multiple APK codebase as painless as possible.

## Confirm you need multiple APKs

When trying to create an application that works across multiple generations of the Android platform, naturally you want your application to take advantage of new features on new devices, without sacrificing backwards compatibility. It may seem at the outset as though multiple APK support is the best solution, but this often isn't the case. The[Using Single APK Instead](https://developer.android.com/google/play/publishing/multiple-apks#ApiLevelOptions)section of the multiple APK developer guide includes some useful information on how to accomplish this with a single APK, including use of our support library. You can also learn how to write code that runs only at certain API levels in a single APK, without resorting to computationally expensive techniques like reflection from[this article](http://android-developers.blogspot.com/2010/07/how-to-have-your-cupcake-and-eat-it-too.html).

If you can manage it, confining your application to a single APK has several advantages, including:

- Publishing and testing are easier
- There's only one codebase to maintain
- Your application can adapt to device configuration changes
- App restore across devices just works
- You don't have to worry about market preference, behavior from "upgrades" from one APK to the next, or which APK goes with which class of devices

The rest of this lesson assumes that you've researched the topic, studiously absorbed the material in the resources linked, and determined that multiple APKs are the right path for your application.

## Chart your requirements

Start off by creating a simple chart to quickly determine how many APKs you need, and what API range each APK covers. For handy reference, the[Platform Versions](https://developer.android.com/about/dashboards)page of the Android Developer website provides data about the relative number of active devices running a given version of the Android platform. Also, although it sounds easy at first, keeping track of which set of API levels each APK is going to target gets difficult rather quickly, especially if there's going to be some overlap (there often is). Fortunately, it's easy to chart out your requirements quickly, easily, and have an easy reference for later.

In order to create your multiple APK chart, start out with a row of cells representing the various API levels of the Android platform. Throw an extra cell at the end to represent future versions of Android.

|---|---|---|---|---|---|---|----|----|----|----|---|
| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | + |

Now just color in the chart such that each color represents an APK. Here's one example of how you might apply each APK to a certain range of API levels.

|---|---|---|---|---|---|---|----|----|----|----|---|
| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | + |

Once you've created this chart, distribute it to your team. Team communication on your project just got immediately simpler, since instead of asking "How's the APK for API levels 3 to 6, er, you know, the Android 1.x one. How's that coming along?" You can simply say "How's the Blue APK coming along?"

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

By way of example, let's take the set of multiple APKs described earlier, and assume that we haven't set a max API level for any of the APKs. Taken individually, the possible range of each APK would look like this:

|---|---|---|---|---|---|---|----|----|----|----|---|
| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | + |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | + |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | + |

Because it is required that an APK with a higher minSdkVersion also have a higher version code, we know that in terms of versionCode values, red ≥ green ≥ blue. Therefore we can effectively collapse the chart to look like this:

|---|---|---|---|---|---|---|----|----|----|----|---|
| 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | + |

Now, let's further assume that the Red APK has some requirement on it that the other two don't.[Filters on Google Play](https://developer.android.com/google/play/filters)page of the Android Developer guide has a whole list of possible culprits. For the sake of example, let's assume that red requires a front-facing camera. In fact, the entire point of the red APK is to combine the front-facing camera with sweet new functionality that was added in API 11. But, it turns out, not all devices that support API 11 even HAVE front-facing cameras! The horror!

Fortunately, if a user is browsing Google Play from one such device, Google Play will look at the manifest, see that Red lists the front-facing camera as a requirement, and quietly ignore it, having determined that Red and that device are not a match made in digital heaven. It will then see that Green is not only forward-compatible with devices with API 11 (since no maxSdkVersion was defined), but also doesn't care whether or not there's a front-facing camera! The app can still be downloaded from Google Play by the user, because despite the whole front-camera mishap, there was still an APK that supported that particular API level.

In order to keep all your APKs on separate "tracks", it's important to have a good version code scheme. The recommended one can be found on the[Version Codes](https://developer.android.com/google/play/publishing/multiple-apks#VersionCodes)area of our developer guide. Since the example set of APKs is only dealing with one of 3 possible dimensions, it would be sufficient to separate each APK by 1000, set the first couple digits to the minSdkVersion for that particular APK, and increment from there. This might look like:

Blue: 03001, 03002, 03003, 03004...  
Green: 07001, 07002, 07003, 07004...  
Red:11001, 11002, 11003, 11004...

Putting this all together, your Android Manifests would likely look something like the following:

Blue:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="03001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="3" />
    ...
```

Green:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="07001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="7" />
    ...
```

Red:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="11001" android:versionName="1.0" package="com.example.foo">
    <uses-sdk android:minSdkVersion="11" />
    ...
```

## Review your pre-launch checklist

Before uploading to Google Play, double-check the following items. Remember that these are specifically relevant to multiple APKs, and in no way represent a complete checklist for all applications being uploaded to Google Play.

- All APKs must have the same package name
- All APKs must be signed with the same certificate
- If the APKs overlap in platform version, the one with the higher minSdkVersion must have a higher version code
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
supports-screens: 'small' 'normal' 'large' 'xlarge'
supports-any-density: 'true'
locales: '--_--'
densities: '120' '160' '240'
```

When you examine aapt output, be sure to check that you don't have conflicting values for supports-screens and compatible-screens, and that you don't have unintended "uses-feature" values that were added as a result of permissions you set in the manifest. In the example above, the APK won't be visible to very many devices.

Why? By adding the required permission SEND_SMS, the feature requirement of android.hardware.telephony was implicitly added. Since API 11 is Honeycomb (the version of Android optimized specifically for tablets), and no Honeycomb devices have telephony hardware in them, Google Play will filter out this APK in all cases, until future devices come along which are higher in API level AND possess telephony hardware.

Fortunately this is easily fixed by adding the following to your manifest:  

```xml
<uses-feature android:name="android.hardware.telephony" android:required="false" />
```

The`android.hardware.touchscreen`requirement is also implicitly added. If you want your APK to be visible on TVs which are non-touchscreen devices you should add the following to your manifest:  

```xml
<uses-feature android:name="android.hardware.touchscreen" android:required="false" />
```

Once you've completed the pre-launch checklist, upload your APKs to Google Play. It may take a bit for the application to show up when browsing Google Play, but when it does, perform one last check. Download the application onto any test devices you may have, to make sure that the APKs are targeting the intended devices. Congratulations, you're done!