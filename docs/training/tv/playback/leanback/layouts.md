---
title: https://developer.android.com/training/tv/playback/leanback/layouts
url: https://developer.android.com/training/tv/playback/leanback/layouts
source: md.txt
---

# Layouts in the Leanback UI toolkit

Build better with Compose  
Create beautiful UIs with minimal code using Jetpack Compose for Android TV OS.  
[Compose for TV →](https://developer.android.com/training/tv/playback/compose)  
![](https://developer.android.com/static/images/android-compose-tv-logo.png)
| **Warning:** The Leanback library is deprecated. Use[Jetpack Compose for Android TV OS](https://developer.android.com/training/tv/playback/compose)instead.

A TV screen is typically viewed from about 10 feet away, and while it is much larger than most other Android-powered device displays, a TV screen does not provide the same level of detail and color as a smaller device screen. These factors require you to create app layouts with TV devices in mind to create a useful and enjoyable user experience.

## Use layout themes for TV

Android[themes](https://developer.android.com/guide/topics/ui/themes)can provide a basis for layouts in your TV apps. Use a theme to modify the display of your app activities that are meant to run on a TV device. This section explains which themes to use.

### Leanback theme

The deprecated[androidx.leanback library](https://developer.android.com/training/tv/get-started/create#leanback)includes`Theme.Leanback`, a theme for TV activities that provides a consistent visual style for Leanback UI toolkit apps. Use this theme for any TV app built with the AndroidX Leanback classes. The following code sample shows how to apply this theme to an activity:  

```xml
<activity
  android:name="com.example.android.TvActivity"
  android:label="@string/app_name"
  android:theme="@style/Theme.Leanback">
```
| **Caution:** The Leanback theme does not include an app bar, since app bars shouldn't be used in Android TV apps. If your app uses support fragments, like[BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment), your activity must extend[FragmentActivity](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity). Do not use[AppCompatActivity](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity), which tries to theme the app bar and produces the following error:  
|
| ```
| java.lang.RuntimeException: Unable to start activity ComponentInfo{...} :
| java.lang.IllegalStateException: You need to use a Theme.AppCompat theme (or descendant) with this activity.
| ```

### NoTitleBar theme

The title bar is a standard user interface element for Android apps on phones and tablets, but it is not appropriate for TV apps. If you are not using AndroidX Leanback classes, apply the`NoTitleBar`theme to your TV activities to suppress the display of a title bar. The following code example from a TV app manifest demonstrates how to apply this theme to remove the display of a title bar:  

```xml
<application>
  ...
  <activity
    android:name="com.example.android.TvActivity"
    android:label="@string/app_name"
    android:theme="@android:style/Theme.NoTitleBar">
    ...
  </activity>
</application>
```

### AppCompat themes

In Android mobile apps, it's very common to use[AppCompatActivity](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity)along with one of the`Theme.AppCompat`themes. This combination lets you use features like drawable tinting without worrying about the version of Android running on the device. If you are developing an app that runs only on Android TV, do not use`AppCompatActivity`, because the features it enables are either already available on Android TV or not relevant.

If you are building an app with a shared codebase between Android mobile and Android TV, you can run into some challenges due to theming.`AppCompatActivity`and the various`AppCompat`widgets require that you use`Theme.AppCompat`, while the Leanback UI toolkit fragments expect you to use[FragmentActivity](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity)and`Theme.Leanback`.

If you need to use the same base activity for Android mobile and Android TV, or if you want to use custom views based on`AppCompat`widgets like[AppCompatImageView](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatImageView), use the`Theme.AppCompat.Leanback`themes. These themes give you all of the theming from`AppCompat`and also provide the Leanback-specific values.

You can customize`Theme.AppCompat.Leanback`themes the same way you do with any other theme. For example, if you want to change values that are specific to the Leanback UI toolkit's[OnboardingSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/OnboardingSupportFragment), do something similar to the following:  

```xml
<style name="MyOnboarding" parent="Theme.AppCompat.Leanback.Onboarding">
    <item name="onboardingLogoStyle">@style/MyOnboardingLogoStyle</item>
    <item name="onboardingPageIndicatorStyle">@style/MyOnboardingPageIndicatorStyle</item>
</style>
```

## Build basic TV layouts

Layouts for TV devices must follow some basic guidelines to help ensure that they are usable and effective on large screens. Follow these tips to build layouts optimized for TV screens:

- Build layouts with a landscape orientation. TV screens always display in landscape mode.
- Put on-screen navigation controls on the left or right side of the screen and save the vertical space for content.
- Create UIs that are divided into sections using[fragments](https://developer.android.com/guide/components/fragments). Use view groups like[GridView](https://developer.android.com/reference/android/widget/GridView)instead of[ListView](https://developer.android.com/reference/android/widget/ListView)to make better use of the horizontal screen space.
- Use view groups like[RelativeLayout](https://developer.android.com/reference/android/widget/RelativeLayout)or[LinearLayout](https://developer.android.com/reference/android/widget/LinearLayout)to arrange views. This approach lets the system adjust the position of the views to the size, alignment, aspect ratio, and pixel density of a TV screen.
- Add sufficient margins between layout controls to avoid a cluttered UI.

### Overscan

Layouts for TV have some unique requirements due to the evolution of TV standards to present a full-screen picture to viewers. For this reason, TV devices might clip the outside edge of an app layout to ensure that the entire display is filled. This behavior is generally referred to as*overscan*.

Position screen elements that must be visible to the user at all times within the overscan-safe area. Adding a 5% margin of 48 dp on the left and right edges and 27 dp on the top and bottom edges to a layout helps ensure that screen elements in the layout are within the overscan-safe area.

Don't adjust background screen elements that the user doesn't directly interact with, and don't clip the elements to the overscan-safe area. This approach helps ensure that background screen elements look correct on all screens.

The following example shows a root layout that can contain background elements and a nested child layout that has a 5% margin and can contain elements within the overscan-safe area:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
   android:layout_width="match_parent"
   android:layout_height="match_parent">

   <!-- Screen elements that can render outside the overscan-safe area go here. -->

   <!-- Nested RelativeLayout with overscan-safe margin. -->
   <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
       android:layout_width="match_parent"
       android:layout_height="match_parent"
       android:layout_marginTop="27dp"
       android:layout_marginBottom="27dp"
       android:layout_marginLeft="48dp"
       android:layout_marginRight="48dp">

      <!-- Screen elements that need to be within the overscan-safe area go here. -->

   </RelativeLayout>

</RelativeLayout>
```

**Caution:** Don't apply overscan margins to your layout if you are using the AndroidX Leanback classes, such as[BrowseSupportFragment](https://developer.android.com/reference/androidx/leanback/app/BrowseSupportFragment)or related widgets, as those layouts already incorporate overscan-safe margins.

## Build usable text and controls

Follow these tips to make the text and controls in your TV app easier to see from a distance:

- Break text into small chunks that users can quickly scan.
- Use light text on a dark background. This style is easier to read on a TV.
- Avoid lightweight fonts or fonts that have both very narrow and very broad strokes. Use simple sans-serif fonts and anti-aliasing to increase readability.
- Use Android's standard font sizes:  

  ```xml
  <TextView
        android:id="@+id/atext"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:singleLine="true"
        android:textAppearance="?android:attr/textAppearanceMedium"/>
  ```
- Make all your view widgets large enough to be clearly visible to someone sitting 10 feet away from the screen. The best way to do this is to use layout-relative sizing rather than absolute sizing, and density-independent pixel (dp) units instead of absolute pixel units. For example, to set the width of a widget, use`wrap_content`instead of a pixel measurement, and to set the margin for a widget, use dp values instead of px values.

For more information about density-independent pixels and building layouts to handle larger screen sizes, see[Screen compatibility overview](https://developer.android.com/guide/practices/screens_support).

## Manage layout resources for TV

Like all other Android devices, TVs have different screen sizes and support different resolutions, including, but not limited to, 720p, 1080p, and 4K. Make sure your app[supports different screen sizes](https://developer.android.com/training/multiscreen/screensizes).

Different screen sizes and resolutions have different pixel densities. To preserve the appearance of your UI across screen sizes, resolution, and pixel densities, define UI measurements using density-independent pixels (dp) rather than pixels. The screen pixel density for different TV panel resolutions is outlined below.

| Panel resolution | Screen pixel density |
|------------------|----------------------|
| 720p             | `tvdpi`              |
| 1080             | `xhdpi`              |
| 4K               | `xxxhdpi`            |

See[Support different pixel densities](https://developer.android.com/training/multiscreen/screendensities)for more information.

<br />

For more information about optimizing layouts and resources for large screens, see[Screen compatibility overview](https://developer.android.com/training/multiscreen).

## Layout patterns to avoid

There are a few approaches to building layouts that don't work well on TV devices. Here are some user interface approaches to avoid when developing a layout for TV.

- **Re-using phone or tablet layouts:**don't reuse layouts from a phone or tablet app without modification. Layouts built for other Android device form factors are not well suited for TV devices and must be simplified for operation on a TV.
- **Using`ActionBar`:**while action bars are recommended for use on phones and tablets, they aren't appropriate for a TV interface. Using an action bar options menu, or any pull-down menu, is strongly discouraged for TV apps due to the difficulty in navigating such a menu with a remote control.
- **Using`ViewPager`:**sliding between screens can work great on a phone or tablet, but don't try this on a TV!

For more information about designing layouts that are appropriate to TV, see the[TV design](https://developer.android.com/design/tv)guide.

## Handle large bitmaps

TV devices, like other Android devices, have a limited amount of memory. If you build your app layout with very high-resolution images or use many high-resolution images in the operation of your app, it can quickly run into memory limits and cause out of memory errors. For most cases, we recommend using the[Glide](https://github.com/bumptech/glide)library to fetch, decode, and display bitmaps in your app. For more information about getting the best performance when working with bitmaps, refer to our general[Android graphics best practices](https://developer.android.com/topic/performance/graphics).

## Provide effective advertising

For the living room environment, we recommend that you use video ad solutions that are full-screen and dismissable within 30 seconds. Functionality for advertising on Android TV, such as dismiss buttons and clickthroughs, must be accessible using the D-pad rather than touch.

Android TV does not provide a web browser. Your ads must not attempt to launch a web browser or redirect to Google Play Store content that is not approved for Android TV devices.

**Note:** You can use the[WebView](https://developer.android.com/reference/android/webkit/WebView)class for logins to social media services.

## Additional resources

[Designing for TV](https://developer.android.com/design/tv)