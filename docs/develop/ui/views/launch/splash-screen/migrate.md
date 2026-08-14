---
title: https://developer.android.com/develop/ui/views/launch/splash-screen/migrate
url: https://developer.android.com/develop/ui/views/launch/splash-screen/migrate
source: md.txt
---

If you implement a custom splash screen in Android 11 or earlier, migrate your
app to the [`SplashScreen`](https://developer.android.com/reference/android/window/SplashScreen) API to help
ensure it displays correctly in Android 12 and later.

Starting in Android 12, the system applies the [Android system default splash
screen](https://developer.android.com/about/versions/12/features/splash-screen) on
[cold](https://developer.android.com/topic/performance/vitals/launch-time#cold) and [warm
starts](https://developer.android.com/topic/performance/vitals/launch-time#warm) for all apps. By default,
this system splash screen is constructed using your app's launcher icon element
and the [`windowBackground`](https://developer.android.com/reference/android/R.attr#windowBackground) of your
theme, if it's a single color.

If you don't migrate your app, your app launch experience on Android 12 and
later might be degraded or have unintended results.

- If your existing splash screen is implemented using a
  [custom theme that overrides `android:windowBackground`](https://developer.android.com/develop/ui/views/launch/splash-screen#set-theme),
  the system replaces your custom splash screen with a default Android system
  splash screen on Android 12 and later. This might not be your app's intended
  experience.

- If your existing splash screen is implemented using a dedicated `Activity`,
  launching your app on devices running Android 12 or later results in
  duplicate splash screens:
  [the system splash screen](https://developer.android.com/about/versions/12/features/splash-screen)
  displays, followed by your existing splash screen activity.

You can prevent these degraded or unintended experiences by completing the
migration process described in this document. After you migrate, the API
improves startup time, gives you full control over the splash screen experience,
and creates a more consistent launch experience with other apps on the platform.

## SplashScreen compat library

You can use the `SplashScreen` API directly, but we strongly recommend using the
[Androidx `SplashScreen` compat library](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen)
instead. The compat library uses the `SplashScreen` API, enables
backward-compatibility, and creates a consistent look and feel for splash screen
display across all Android versions. This document is written using the compat
library.

If you migrate using the `SplashScreen` API directly, on Android 11 and earlier
your splash screen looks exactly the same as before the migration. Starting on
Android 12, the splash screen has the Android 12 look and feel.

If you migrate using the `SplashScreen` compat library, the system displays the
same splash screen on all versions of Android.

## Migrate your splash screen implementation

Complete the following steps to migrate your existing splash screen
implementation to Android 12 and later.

This procedure applies to whichever type of implementation you are migrating
from. If you're migrating from a dedicated `Activity`, follow the [best
practices](https://developer.android.com/develop/ui/views/launch/splash-screen/migrate#best-practices) described on this document for adapting your
customized splash screen `Activity`. The `SplashScreen` API also reduces startup
latency that is introduced with a dedicated splash screen activity.

To migrate your splash screen, do the following:

1. In the `build.gradle` file,
   [change your `compileSdkVersion`](https://developer.android.com/about/versions/12/setup-sdk) and include
   the `SplashScreen` compat library in dependencies.

       build.gradle

       android {
          compileSdkVersion 31
          ...
       }
       dependencies {
          ...
          implementation 'androidx.core:core-splashscreen:1.0.0-beta02'
       }

2. Create a theme with a parent of `Theme.SplashScreen`. Set the value of
   `postSplashScreenTheme` to the theme that the `Activity` must use and the
   value of `windowSplashScreenAnimatedIcon` to a drawable or animated
   drawable. The other attributes are optional.

       <style name="Theme.App.Starting" parent="Theme.SplashScreen">
          <!-- Set the splash screen background, animated icon, and animation
          duration. -->
          <item name="windowSplashScreenBackground">@color/...</item>

          <!-- Use windowSplashScreenAnimatedIcon to add a drawable or an animated
               drawable. One of these is required. -->
          <item name="windowSplashScreenAnimatedIcon">@drawable/...</item>
          <!-- Required for animated icons. -->
          <item name="windowSplashScreenAnimationDuration">200</item>

          <!-- Set the theme of the Activity that directly follows your splash
          screen. This is required. -->
          <item name="postSplashScreenTheme">@style/Theme.App</item>
       </style>

   If you want to add a background color underneath your icon, you can use the
   `Theme.SplashScreen.IconBackground` theme and set the
   `windowSplashScreenIconBackground` attribute.
3. In the manifest, replace the theme of the starting activity to the theme you
   create in the previous step.

       <manifest>
          <application android:theme="@style/Theme.App.Starting">
           <!-- or -->
               <activity android:theme="@style/Theme.App.Starting">
       ...

4. Call `installSplashScreen` in the starting activity before calling
   `super.onCreate()`.

   ### Kotlin

   ```kotlin
   class MainActivity : Activity() {

      override fun onCreate(savedInstanceState: Bundle?) {
          // Handle the splash screen transition.
          val splashScreen = installSplashScreen()

          super.onCreate(savedInstanceState)
          setContentView(R.layout.main_activity)
   ...
   ```

   ### Java

   ```java
   public class MainActivity extends Activity {

       @Override
       protected void onCreate(Bundle savedInstanceState) {
            // Handle the splash screen transition.
            SplashScreen splashScreen = SplashScreen.installSplashScreen(this);

            super.onCreate(savedInstanceState);
            setContentView(R.layout.main_activity);
       }
   }
   ```

`installSplashScreen` returns the splash screen object, which you can optionally
use to customize animation or to keep the splash screen on screen for a longer
duration. For more details on customizing the animation, see
[Keep the splash screen on-screen for longer periods](https://developer.android.com/about/versions/12/features/splash-screen#suspend-drawing)
and
[Customize the animation for dismissing the splash screen](https://developer.android.com/about/versions/12/features/splash-screen#customize-animation).

## Adapt your custom splash screen Activity to the splash screen

After you migrate to the splash screen for Android 12 and later, decide what
to do with your previous custom splash screen `Activity`. You have the following
options:

- Keep the custom activity, but prevent it from displaying.
- Keep the custom activity for branding reasons.
- Remove the custom activity and adapt your app as needed.

### Prevent the custom Activity from being displayed

If your previous splash screen `Activity` is primarily used for routing,
consider ways to remove it. For example, you might directly link to the actual
activity or move to a singular activity with subcomponents. If this isn't
feasible, you can use
[`SplashScreen.setKeepOnScreenCondition`](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen#setkeeponscreencondition)
to keep the routing activity in place but stop it from rendering. Doing so
transfers the splash screen to the next activity and supports a smooth
transition.

### Kotlin

```kotlin
  class RoutingActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        val splashScreen = installSplashScreen()
        super.onCreate(savedInstanceState)

        // Keep the splash screen visible for this Activity.
        splashScreen.setKeepOnScreenCondition { true }
        startSomeNextActivity()
        finish()
     }
   ...
  
```

### Java

```java
  public class RoutingActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
      SplashScreen splashScreen = SplashScreen.installSplashScreen(this);

       super.onCreate(savedInstanceState);

       // Keep the splash screen visible for this Activity.
       splashScreen.setKeepOnScreenCondition(() -> true );
       startSomeNextActivity();
       finish();
    }
  ...
  
```

### Keep the custom activity for branding

If you want to use a previous splash screen `Activity` for branding reasons, you
can transition from the system splash screen into your custom splash screen
`Activity` by [customizing the animation for dismissing the splash
screen](https://developer.android.com/about/versions/12/features/splash-screen#customize-animation).
However, it's best to avoid this scenario if possible and use the `SplashScreen`
API to brand your splash screen.

If you need to display a [dialog](https://developer.android.com/develop/ui/views/components/dialogs), we
recommend displaying it over the subsequent custom splash screen activity or
over the main activity after the system splash screen.

### Remove the custom splash screen Activity

Generally, we recommend removing your previous custom splash screen `Activity`
altogether to avoid the duplication of splash screens, to increase efficiency,
and to reduce splash screen loading times. There are different techniques that
you can use to avoid showing redundant splash screen activities.

- **Use lazy loading for your components, modules, or libraries.** Avoid loading
  or initializing components or libraries that aren't required for the app to
  work at launch. Load them later, when the app needs them.

  If your app truly needs a component to work properly, load it only when it's
  really needed and not at launch time, or use a background thread to load it
  after the app starts. Try to keep your `Application.onCreate()` as light as
  possible.

  You can also benefit from using the
  [App Startup library](https://developer.android.com/topic/libraries/app-startup) to initialize components
  at application startup. When doing so, make sure to still load all the
  required modules for the starting activity and don't introduce janks where the
  lazily loaded modules become available.
- **Create a placeholder while loading a small amount of data locally.** Use the
  recommended theming approach and hold back the rendering until the app is
  ready. To implement a splash screen that is backward-compatible, follow the
  steps outlined in
  [Keep the splash screen on-screen for longer periods](https://developer.android.com/about/versions/12/features/splash-screen#suspend-drawing).

- **Show placeholders.** For network-based loads with indeterminate durations,
  dismiss the splash screen and show placeholders for asynchronous loading.
  Consider applying subtle animations to the content area that reflect the
  loading state. Make sure that the loaded content structure matches the
  [skeleton structure](https://m2.material.io/design/communication/launch-screen.html#placeholder-ui)
  as well as possible to support a smooth transition when the content is loaded.

- **Use caching**. When a user opens your app for the first time, you can show
  loading indicators for some UI elements, as shown in the following figure. The
  next time the user returns to your app, you can show this cached content while
  you load more recent content.

**Figure 1.** Showing UI placeholders.