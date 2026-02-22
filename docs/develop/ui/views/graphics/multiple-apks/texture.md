---
title: https://developer.android.com/develop/ui/views/graphics/multiple-apks/texture
url: https://developer.android.com/develop/ui/views/graphics/multiple-apks/texture
source: md.txt
---

# Creating multiple APKs for different GL textures

If you publish your app to Google Play, you should build and upload an[Android App Bundle](https://developer.android.com/guide/app-bundle). When you do so, Google Play automatically generates and serves optimized APKs for each user's device configuration, so they download only the code and resources they need to run your app. Publishing multiple APKs is useful if you are not publishing to Google Play, but you must build, sign, and manage each APK yourself.

When developing your Android application to take advantage of multiple APKs on Google Play, it's important to adopt some good practices from the get-go, and prevent unnecessary headaches further into the development process. This lesson shows you how to create multiple APKs of your app, each supporting a different subset of OpenGL texture formats. You will also gain some tools necessary to make maintaining a multiple APK codebase as painless as possible.

## Confirm you need multiple APKs

When trying to create an application that works across all available Android-powered devices, naturally you want your application look its best on each individual device, regardless of the fact they don't all support the same set of GL textures. It may seem at the outset as though multiple APK support is the best solution, but this often isn't the case. The[Using Single APK Instead](https://developer.android.com/google/play/publishing/multiple-apks#ApiLevelOptions)section of the multiple APK developer guide includes some useful information on how to accomplish this with a single APK, including how to[detect supported texture formats at runtime](https://developer.android.com/google/play/publishing/multiple-apks#TextureOptions). Depending on your situation, it might be easier to bundle all formats with your application, and simply pick which one to use at runtime.

If you can manage it, confining your application to a single APK has several advantages, including:

- Publishing and Testing are easier
- There's only one codebase to maintain
- Your application can adapt to device configuration changes
- App restore across devices just works
- You don't have to worry about market preference, behavior from "upgrades" from one APK to the next, or which APK goes with which class of devices

The rest of this lesson assumes that you've researched the topic, studiously absorbed the material in the resources linked, and determined that multiple APKs are the right path for your application.

## Chart your requirements

The Android Developer Guide provides a handy reference of some of common supported textures on the[supports-gl-texture page](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element). This page also contains some hints as to which phones (or families of phones) support particular texture formats. Note that it's generally a good idea for one of your APKs to support ETC1, as that texture format is supported by all Android-powered devices that support the OpenGL ES 2.0 spec.

Since most Android-powered devices support more than one texture format, you need to establish an order of preference. Create a chart including all the formats that your application is going to support. The left-most cell is going to be the lowest priority (It will probably be ETC1, a really solid default in terms of performance and compatibility). Then color in the chart such that each cell represents an APK.

|------|-----|---------|
| ETC1 | ATI | PowerVR |

Coloring in the chart does more than just make this guide less monochromatic - It also has a way of making intra-team communication easier- You can now simply refer to each APK as "blue", "green", or "red", instead of "The one that supports ETC1 texture formats", etc.

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

When a user downloads an application which uses multiple APKs through Google Play, the correct APK to use is chosen using some simple rules:

- The manifest has to show that particular APK is eligible
- Of the eligible APKs, highest version number wins
- If*any*of the texture formats listed in your APK are supported by the device on market, that device is considered eligible

With regards to GL Textures, that last rule is important. It means that you should, for instance, be*very* careful about using different GL formats in the same application. If you were to use PowerVR 99% of the time, but use ETC1 for, say, your splash screen... Then your manifest would necessarily indicate support for both formats. A device that*only*supported ETC1 would be deemed compatible, your app would download, and the user would see some thrilling crash messages. The common case is going to be that if you're using multiple APKs specifically to target different devices based on GL texture support, it's going to be one texture format per APK.

This actually makes texture support a little bit different than the other two multiple APK dimensions, API level and screen size. Any given device only has one API level, and one screen size, and it's up to the APK to support a range of them. With textures, the APK will generally support one texture, and the device will support many. There will often be overlap in terms of one device supporting many APKs, but the solution is the same: Version codes.

By way of example, take a few devices, and see how many of the APKs defined earlier fit each device.

|----------|---------|--------|
| FooPhone | Nexus S | Evo    |
| ETC1     | ETC1    | ETC1   |
|          | PowerVR | ATI TC |

Assuming that PowerVR and ATI formats are both preferred over ETC1 when available, than according to the "highest version number wins" rule, if we set the versionCode attribute in each APK such that red ≥ green ≥ blue, then both Red and Green will always be chosen over Blue on devices which support them, and should a device ever come along which supports both Red and Green, red will be chosen.

In order to keep all your APKs on separate "tracks," it's important to have a good version code scheme. The recommended one can be found on the Version Codes area of our developer guide. Since the example set of APKs is only dealing with one of 3 possible dimensions, it would be sufficient to separate each APK by 1000 and increment from there. This might look like:

Blue: 1001, 1002, 1003, 1004...  
Green: 2001, 2002, 2003, 2004...  
Red:3001, 3002, 3003, 3004...

Putting this all together, your Android Manifests would likely look something like the following:

Blue:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="1001" android:versionName="1.0" package="com.example.foo">
    <supports-gl-texture android:name="GL_OES_compressed_ETC1_RGB8_texture" />
    ...
```

Green:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="2001" android:versionName="1.0" package="com.example.foo">
    <supports-gl-texture android:name="GL_AMD_compressed_ATC_texture" />
    ...
```

Red:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="3001" android:versionName="1.0" package="com.example.foo">
    <supports-gl-texture android:name="GL_IMG_texture_compression_pvrtc" />
    ...
```

## Review your pre-launch checklist

Before uploading to Google Play, double-check the following items. Remember that these are specifically relevant to multiple APKs, and in no way represent a complete checklist for all applications being uploaded to Google Play.

- All APKs must have the same package name
- All APKs must be signed with the same certificate
- Double check your manifest filters for conflicting information (an APK that only supports cupcake on XLARGE screens isn't going to be seen by anybody)
- Each APK's manifest must be unique across at least one of supported screen, OpenGL texture, or platform version
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

Once you've completed the pre-launch checklist, upload your APKs to Google Play. It may take a bit for the application to show up when browsing Google Play, but when it does, perform one last check. Download the application onto any test devices you may have to make sure that the APKs are targeting the intended devices. Congratulations, you're done!