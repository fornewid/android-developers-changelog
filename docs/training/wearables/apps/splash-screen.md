---
title: https://developer.android.com/training/wearables/apps/splash-screen
url: https://developer.android.com/training/wearables/apps/splash-screen
source: md.txt
---

If your app implements a custom splash screen or uses a launcher theme, migrate
your app to the [`SplashScreen`](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen) library, available in Jetpack, to ensure it
displays correctly on all Wear OS versions.

See step by step implementation instructions on this page to learn how to add a
splash screen using the `SplashScreen` library such that the screen meets
[design guidelines](https://developer.android.com/training/wearables/design/launch#branded).

## Add dependencies

Add the following dependency to your app module's `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-splashscreen:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-splashscreen:1.2.0")
}
```

Make sure you are using version `1.0.1` or higher, to get support for default
Wear OS dimensions.

## Add a theme

Create a splash screen theme in `res/values/styles.xml`. The parent element
depends on the icon's shape:

- If the icon is round, use `Theme.SplashScreen`.
- If the icon is a different shape, use `Theme.SplashScreen.IconBackground`.

Use `windowSplashScreenBackground` to fill the background with a single black
color. Set the values of `postSplashScreenTheme` to the theme that the Activity
should use and `windowSplashScreenAnimatedIcon` to a drawable or animated
drawable:

<br />

```xml
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
```

<br />

If you use a non-round icon, you need to set a white background color underneath
your icon. In this case, use the `Theme.SplashScreen.IconBackground` as parent
theme and set the `windowSplashScreenIconBackgroundColor` attribute:

<br />

```xml
<style name="Theme.App.Starting" parent="Theme.SplashScreen">
    <!-- Set a white background behind the splash screen icon. -->
    <item name="windowSplashScreenIconBackgroundColor">@android:color/white</item>
</style>
```

<br />

The other attributes are optional.

## Create a drawable for the theme

Splash screen themes requires a drawable to pass into the
`windowSplashScreenAnimatedIcon` attribute. For example, you can create it by
adding a new file `res/drawable/splash_screen.xml` and using app launcher icon
and correct splash screen icon size:

<br />

```xml
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:width="@dimen/splash_screen_icon_size"
        android:height="@dimen/splash_screen_icon_size"
        android:drawable="@mipmap/ic_launcher"
        android:gravity="center" />
</layer-list>
```

<br />

The splash screen icon size is defined in `res/values/dimens.xml` and differs
depending whether the icon is round:

<br />

```xml
<resources>
    <!-- Round app icon can take all of default space -->
    <dimen name="splash_screen_icon_size">48dp</dimen>
</resources>
```

<br />

...or non-round and therefore must use the icon background:

<br />

```xml
<resources>
    <!-- Non-round icon with background must use reduced size to fit circle -->
    <dimen name="splash_screen_icon_size">36dp</dimen>
</resources>
```

<br />

## Specify the theme

In your app's manifest file (`AndroidManifest.xml`), replace the theme of the
starting activity -- usually the ones that define a launcher item or are
otherwise exported -- to the theme you created in the previous step:

<br />

```xml
<activity
    android:name=".snippets.SplashScreenActivity"
    android:exported="true"
    android:taskAffinity=""
    android:theme="@style/Theme.App.Starting">
    <!-- ... -->
</activity>
```

<br />

## Update your starting activity

Install your splash screen in the starting activity before calling
`super.onCreate()`:

<br />

```kotlin
class SplashScreenActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        installSplashScreen()
        super.onCreate(savedInstanceState)

        setContent {
            WearApp()
        }
    }
}
```

<br />

## Additional resources

[Learn more about splash screens](https://developer.android.com/develop/ui/views/launch/splash-screen) in general and how you can use them
in your app.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate your splash screen implementation to Android 12 and later](https://developer.android.com/develop/ui/views/launch/splash-screen/migrate)
- [Splash screens](https://developer.android.com/develop/ui/views/launch/splash-screen)
- [Integrate App Actions with Android widgets](https://developer.android.com/develop/devices/assistant/widgets)