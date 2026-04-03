---
title: Add a splash screen  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/apps/splash-screen
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Add a splash screen Stay organized with collections Save and categorize content based on your preferences.




If your app implements a custom splash screen or uses a launcher theme, migrate
your app to the [`SplashScreen`](/reference/kotlin/androidx/core/splashscreen/SplashScreen) library, available in Jetpack, to ensure it
displays correctly on all Wear OS versions.

See step by step implementation instructions on this page to learn how to add a
splash screen using the `SplashScreen` library such that the screen meets
[design guidelines](/training/wearables/design/launch#branded).

## Add dependencies

Add the following dependency to your app module's `build.gradle` file:

### Groovy

```
dependencies {
    implementation "androidx.core:core-splashscreen:1.2.0"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.core:core-splashscreen:1.2.0")
}
```

Make sure you are using version `1.0.1` or higher, to get support for default
Wear OS dimensions.

## Add a theme

Create a splash screen theme in `res/values/styles.xml`. The parent element
depends on the icon's shape:

* If the icon is round, use `Theme.SplashScreen`.
* If the icon is a different shape, use `Theme.SplashScreen.IconBackground`.

Use `windowSplashScreenBackground` to fill the background with a single black
color. Set the values of `postSplashScreenTheme` to the theme that the Activity
should use and `windowSplashScreenAnimatedIcon` to a drawable or animated
drawable:

```
<resources>
    <style name="Theme.App" parent="@android:style/Theme.DeviceDefault" />

    <style name="Theme.App.Starting" parent="Theme.SplashScreen">
        <!-- Set the splash screen background to black -->
        <item name="windowSplashScreenBackground">@android:color/black</item>
        <!-- Use windowSplashScreenAnimatedIcon to add a drawable or an animated
             drawable. -->
        <item name="windowSplashScreenAnimatedIcon">@drawable/splash_screen</item>
        <!-- Set the theme of the Activity that follows your splash screen. -->
        <item name="postSplashScreenTheme">@style/Theme.App</item>
    </style>
</resources>

styles.xml
```

If you use a non-round icon, you need to set a white background color underneath
your icon. In this case, use the `Theme.SplashScreen.IconBackground` as parent
theme and set the `windowSplashScreenIconBackgroundColor` attribute:

```
<style name="Theme.App.Starting" parent="Theme.SplashScreen">
    <!-- Set a white background behind the splash screen icon. -->
    <item name="windowSplashScreenIconBackgroundColor">@android:color/white</item>
</style>

styles.xml
```

The other attributes are optional.

## Create a drawable for the theme

Splash screen themes requires a drawable to pass into the
`windowSplashScreenAnimatedIcon` attribute. For example, you can create it by
adding a new file `res/drawable/splash_screen.xml` and using app launcher icon
and correct splash screen icon size:

```
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:width="@dimen/splash_screen_icon_size"
        android:height="@dimen/splash_screen_icon_size"
        android:drawable="@mipmap/ic_launcher"
        android:gravity="center" />
</layer-list>

splash_screen.xml
```

The splash screen icon size is defined in `res/values/dimens.xml` and differs
depending whether the icon is round:

```
<resources>
    <!-- Round app icon can take all of default space -->
    <dimen name="splash_screen_icon_size">48dp</dimen>
</resources>

dimens.xml
```

...or non-round and therefore must use the icon background:

```
<resources>
    <!-- Non-round icon with background must use reduced size to fit circle -->
    <dimen name="splash_screen_icon_size">36dp</dimen>
</resources>

dimens.xml
```

## Specify the theme

In your app's manifest file (`AndroidManifest.xml`), replace the theme of the
starting activity -- usually the ones that define a launcher item or are
otherwise exported -- to the theme you created in the previous step:

```
<activity
    android:name=".snippets.SplashScreenActivity"
    android:exported="true"
    android:taskAffinity=""
    android:theme="@style/Theme.App.Starting">
    <!-- ... -->
</activity>

AndroidManifest.xml
```

## Update your starting activity

Install your splash screen in the starting activity before calling
`super.onCreate()`:

```
class SplashScreenActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        installSplashScreen()
        super.onCreate(savedInstanceState)

        setContent {
            WearApp()
        }
    }
}

SplashScreenActivity.kt
```

## Additional resources

[Learn more about splash screens](/develop/ui/views/launch/splash-screen) in general and how you can use them
in your app.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Migrate your splash screen implementation to Android 12 and later](/develop/ui/views/launch/splash-screen/migrate)
* [Splash screens](/develop/ui/views/launch/splash-screen)
* [Integrate App Actions with Android widgets](/develop/devices/assistant/widgets)