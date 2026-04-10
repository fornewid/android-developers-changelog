---
title: https://developer.android.com/training/basics/supporting-devices/platforms
url: https://developer.android.com/training/basics/supporting-devices/platforms
source: md.txt
---

# Support different platform versions

While the latest versions of Android often provide great APIs for your app, you should continue to support older versions of Android until more devices get updated. This lesson shows you how to take advantage of the latest APIs while continuing to support older versions as well.

Use the Android Studio**New Project**wizard to find the distribution of active devices running each version of Android. This distribution is based on the number of devices that visit the Google Play Store. Generally, we recommend supporting about 90% of active devices, while targeting your app to the latest version.

**Tip:** In order to provide the best features and functionality across several Android versions, you should use the[Android Support Library](https://developer.android.com/tools/support-library)in your app, which allows you to use several recent platform APIs on older versions.

## Specify minimum and target API levels

The[AndroidManifest.xml](https://developer.android.com/guide/topics/manifest/manifest-intro)file describes details about your app and identifies which versions of Android it supports. Specifically, the`minSdkVersion`and`targetSdkVersion`attributes for the[`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element)element identify the lowest API level with which your app is compatible and the highest API level against which you've designed and tested your app.

For example:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android" ... >
    <uses-sdk android:minSdkVersion="4" android:targetSdkVersion="15" />
    ...
</manifest>
```

As new versions of Android are released, some style and behaviors may change. To allow your app to take advantage of these changes and ensure that your app fits the style of each user's device, you should set the[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)value to match the latest Android version available.

Since minor SDK versions are not tied to behavior changes, it's not possible to set`targetSdkVersion`to reflect a minor SDK version. If you want to call an API in a minor SDK version that is more recent than your`minSdkVersion`, check the[system version at runtime](https://developer.android.com/training/basics/supporting-devices/$version-codes).

## Check system version at runtime

Android provides a unique code for each platform version in the[Build](https://developer.android.com/reference/android/os/Build)constants class. Use these codes within your app to build conditions that ensure the code that depends on higher API levels is executed only when those APIs are available on the system.  

### Kotlin

```kotlin
private fun setUpActionBar() {
    // Make sure we're running on Honeycomb or higher to use ActionBar APIs
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        actionBar.setDisplayHomeAsUpEnabled(true)
    }
}
```

### Java

```java
private void setUpActionBar() {
    // Make sure we're running on Honeycomb or higher to use ActionBar APIs
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        ActionBar actionBar = getActionBar();
        actionBar.setDisplayHomeAsUpEnabled(true);
    }
}
```

You can use[Build.VERSION.SDK_INT_FULL](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT_FULL)to check for the presence of either a major or minor SDK version.  

### Kotlin

```kotlin
if (SDK_INT_FULL >= VERSION_CODES_FULL.[MAJOR or MINOR RELEASE]) {
  // Use APIs introduced in a major or minor SDK release
}
```

### Java

```java
if (SDK_INT_FULL >= VERSION_CODES_FULL.[MAJOR or MINOR RELEASE]) {
  // Use APIs introduced in a major or minor SDK release
}
```

**Note:** When parsing XML resources, Android ignores XML attributes that aren't supported by the current device. So you can safely use XML attributes that are only supported by newer versions without worrying about older versions breaking when they encounter that code. For example, if you set the`targetSdkVersion="11"`, your app includes the[ActionBar](https://developer.android.com/reference/android/app/ActionBar)by default on Android 3.0 and higher. To then add menu items to the action bar, you need to set`android:showAsAction="ifRoom"`in your menu resource XML. It's safe to do this in a cross-version XML file, because the older versions of Android simply ignore the`showAsAction`attribute (that is, you*do not* need a separate version in`res/menu-v11/`).

## Use platform styles and themes

Android provides user experience themes that give apps the look and feel of the underlying operating system. These themes can be applied to your app within the manifest file. By using these built in styles and themes, your app will naturally follow the latest look and feel of Android with each new release.

To make your activity look like a dialog box:  

```xml
<activity android:theme="@android:style/Theme.Dialog">
```

To make your activity have a transparent background:  

```xml
<activity android:theme="@android:style/Theme.Translucent">
```

To apply your own custom theme defined in`/res/values/styles.xml`:  

```xml
<activity android:theme="@style/CustomTheme">
```

To apply a theme to your entire app (all activities), add the`android:theme`attribute to the[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)element:  

```xml
<application android:theme="@style/CustomTheme">
```

For more about creating and using themes, read the[Styles and Themes](https://developer.android.com/guide/topics/ui/themes)guide.