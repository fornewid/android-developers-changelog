---
title: https://developer.android.com/topic/libraries/support-library
url: https://developer.android.com/topic/libraries/support-library
source: md.txt
---

# Support Library

**Note:** With the release of Android 9.0 (API level 28) there is a new version of the support library called[AndroidX](https://developer.android.com/jetpack/androidx)which is part of[Jetpack](https://developer.android.com/jetpack). The AndroidX library contains the existing support library and also includes the latest Jetpack components.  

You can continue to use the support library. Historical artifacts (those versioned 27 and earlier, and packaged as`android.support.*`) will remain available on Google Maven. However, all new library development will occur in the[AndroidX](https://developer.android.com/jetpack/androidx)library.  

We recommend using the AndroidX libraries in all new projects. You should also consider[migrating](https://developer.android.com/jetpack/androidx/migrate)existing projects to AndroidX as well.

When developing apps that support multiple API versions, you may want a standard way to provide newer features on earlier versions of Android or gracefully fall back to equivalent functionality. Rather than building code to handle earlier versions of the platform, you can leverage these libraries to provide that compatibility layer. In addition, the Support Libraries provide additional convenience classes and features not available in the standard Framework API for easier development and support across more devices.

Originally a single binary library for apps, the Android Support Library has evolved into a suite of libraries for app development. Many of these libraries are now a strongly recommended, if not essential, part of app development.

This document provides an overview of the support library to help you understand its components and how to use it effectively in your app.

**Caution:** Starting with Support Library release 26.0.0 (July 2017), the minimum supported API level across most support libraries has increased to Android 4.0 (API level 14) for most library packages. For more information, see[Version Support and Package Names](https://developer.android.com/topic/libraries/support-library#api-versions)on this page.

## Uses for the Support Libraries

There are a few distinct uses for the support libraries. Backward compatibility classes for earlier versions of the platform is just one of them. Here is a more complete list of ways you can use the support libraries in your app:

- **Backward Compatibility for newer APIs** - A large amount of the support libraries provide backward compatibility for newer framework classes and methods. For example, the[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)support class provides support for fragments on devices running versions earlier than Android 3.0 (API level 11).
- **Convenience and Helper Classes** - The support libraries provides a number of helper classes, particularly for user interface development. For example the[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)class provides a user interface widget for displaying and managing very long lists, useable on versions of Android from API level 7 and up.
- **Debugging and Utilities** - There are a number of features that provide utility beyond code you incorporate into your app, including the[`support-annotations`](https://developer.android.com/studio/write/annotations)library for improved code lint checks on method inputs and[Multidex support](https://developer.android.com/studio/build/multidex)for configuring and distributing apps with over 65,536 methods.

## Using Support versus Framework APIs

Support Libraries provide classes and methods that closely resemble APIs in the Android Framework. Upon discovering this, you may wonder if you should use the framework version of the API or the support library equivalent. Here are the guidelines for when you should use support library classes in place of Framework APIs:

- **Compatibility for a Specific Feature**- If you want to support a recent platform feature on devices that are running earlier versions of the platform, use the equivalent classes and methods from the support library.
- **Compatibility for Related Library Features** - More sophisticated support library classes may depend on one or more additional support library classes, so you should use support library classes for those dependencies. For example, the[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)support class should be used with[FragmentPagerAdapter](https://developer.android.com/reference/androidx/fragment/app/FragmentPagerAdapter)or the[FragmentStatePagerAdapter](https://developer.android.com/reference/androidx/fragment/app/FragmentStatePagerAdapter)support classes.
- **General Device Compatibility** - If you do not have a specific platform feature you intend to use with your app in a backward compatible way, it is still a good idea to use support library classes in your app. For example, you may want to use[ActivityCompat](https://developer.android.com/reference/androidx/core/app/ActivityCompat)in place of the framework[Activity](https://developer.android.com/reference/android/app/Activity)class, so you can take advantage of newer features later on, such as incorporating the new permissions model introduced in Android 6.0 (API level 23).

Support Library classes that provide a compatible implementation of platform API classes may not be able to provide the full set of functionality available in the latest release, due to the limitations of the host device platform version. In these cases, Support Library classes are designed to degrade gracefully, and may not provide the all the functionality or data of the current, platform API. For this reason, you should review the reference documentation for the library classes and methods you use, and thoroughly test on devices running the earliest version of the platform supported by your app.

**Note:** The support libraries do not provide equivalent classes and methods for each framework API. In some cases, you may need to wrap a framework method call with an explicit SDK version check and provide alternative code to handle methods not available on a device. For more information on using version checks in your code, see[Supporting Different Platform Versions](https://developer.android.com/training/basics/supporting-devices/platforms).

## Version Support and Package Names

Some of the Support Library packages have package names to indicate the minimum level of the API they originally supported, using a v# notation, such as the support-v4 package. Starting with Support Library version 26.0.0 (released in July 2017), the minimum supported API level has changed to Android 4.0 (API level 14) for all support library packages. For this reason, when working with any recent release of the support library, you should not assume that the the*v#*package notation indicates a minimum API support level. This change in recent releases also means that library packages with the v4 and v7 are essentially equivalent in the minimum level of API they support. For example, the support-v4 and the support-v7 package both support a minimum API level of 14, for releases of the Support Library from 26.0.0 and higher.

### Support Library Release Versions

The[release version](https://developer.android.com/topic/libraries/support-library/revisions)of the Support Library, such as 24.2.0 or 25.0.1, is different from the minimum API level supported by any library in that release.The release version number indicates which version of the platform API it was built against, and therefore, what the most recent APIs*may be included*in this version of the libraries.

Specifically, the first section of the release version number, for example the 24 in version 24.2.0, generally corresponds with the version of the platform API available when it was released. The release version level of the support library indicates it incorporates*some* features of that API level, but you should not assume it provides compatibility with*all*features released in the new platform API version.

## Library Dependencies

Most libraries in the Android Support Library suite have some dependency on one or more libraries. For example, nearly all support libraries have a dependency on the`support-compat`package. In general, you do not need to worry about support library dependencies, because the gradle build tool manages library dependencies for you, by automatically including dependent libraries.

If you want to see what libraries and library dependencies are included in your app, run the following command at the build root of your app development project to get a report of the dependencies for that project, including Android Support Libraries and other libraries:  

```
gradle -q dependencies your-app-project:dependencies
```

For more information about adding support libraries to your development project using Gradle, see[Support Library Setup](https://developer.android.com/topic/libraries/support-library/setup). For more information about working with Gradle, see[Configure Your Build](https://developer.android.com/studio/build).

Note that*all*Android Support Libraries also depend on some base level of the platform, for recent releases, that is Android 4.0 (API level 14) or higher.