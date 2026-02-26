---
title: https://developer.android.com/develop/ui/views/launch/splash-screen
url: https://developer.android.com/develop/ui/views/launch/splash-screen
source: md.txt
---

> [!IMPORTANT]
> **Important:** If you implemented a custom splash screen in Android 11 or lower, migrate your app to the [`SplashScreen`](https://developer.android.com/reference/android/window/SplashScreen) API to ensure it displays correctly in Android 12 and higher. For instructions, see [Migrate your existing splash screen implementation to Android
> 12](https://developer.android.com/guide/topics/ui/splash-screen/migrate).

Starting in Android 12, the
[`SplashScreen`](https://developer.android.com/reference/android/window/SplashScreen) API lets apps launch
with animation, including an into-app motion at launch, a splash screen showing
your app icon, and a transition to your app itself. A `SplashScreen` is a
[`Window`](https://developer.android.com/reference/android/view/Window) and
therefore covers an
[`Activity`](https://developer.android.com/reference/android/app/Activity).
**Figure 1.** A splash screen.

The splash screen experience brings standard design elements to every app
launch, but it's also customizable so your app can maintain its unique branding.

In addition to using the `SplashScreen` platform API, you can also use the
[`SplashScreen`](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen)
compat library, which wraps the `SplashScreen` API.

## How the splash screen works

When a user launches an app while the app's process isn't running (a [cold
start](https://developer.android.com/topic/performance/vitals/launch-time#cold)) or the `Activity` isn't
created (a [warm start](https://developer.android.com/topic/performance/vitals/launch-time#warm)), the
following events occur:

1. The system shows the splash screen using themes and any animations that you
   define.

2. When the app is ready, the splash screen is dismissed and the app displays.

The splash screen never shows during a
[hot start](https://developer.android.com/topic/performance/vitals/launch-time#hot).

## Elements and mechanics of the splash screen

The elements of the splash screen are defined by XML resource files in the
Android manifest file. There are light and dark mode versions for each element.

The customizable elements of a splash screen consist of the app icon, icon
background, and window background:
![An image showing the elements contained in a splash screen](https://developer.android.com/static/images/guide/topics/ui/splash-screen/splash-screen-composition.png) **Figure 2.** Customizable elements of a splash screen.

Consider the following elements, shown in figure 2:

1 The **app icon** must be a vector drawable. It
can be static or animated. Although animations can have an unlimited duration,
we recommend not exceeding 1,000 milliseconds. The launcher icon is the default.

2 The **icon background** is optional and useful if
you need more contrast between the icon and the window background. If you use an
[adaptive icon](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive), its
background is displayed if there is enough contrast with the window background.

3 As with adaptive icons, one-third of the
foreground is masked.

4 The **window background** consists of a single
opaque color. If the window background is set and is a plain color, it is used
by default if the attribute isn't set.

### Splash screen dimensions

The splash screen icon uses the same specifications as
[adaptive icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive),
as follows:

- Branded image: this must be 200×80 dp.
- App icon with an icon background: this must be 240×240 dp and fit within a circle 160 dp in diameter.
- App icon without an icon background: this must be 288×288 dp and fit within a circle 192 dp in diameter.

For example, if the full size of an image is 300×300 dp, the icon needs to fit
within a circle with a diameter of 200 dp. Everything outside the circle turns
invisible (masked).
![An image showing different icon dimensions for solid and transparent background](https://developer.android.com/static/images/guide/topics/ui/splash-screen/splash-screen-icon-dimensions.png) **Figure 3.** Splash screen icon dimensions for solid and transparent backgrounds, respectively.

### Splash screen animations and the launch sequence

Additional latency is often associated with launching an app on a cold start.
Adding an animated icon to your splash screen has obvious aesthetic appeal and
provides a more premium experience. User research shows that perceived startup
time is less when viewing an animation.

A splash screen animation is embedded within the launch sequence components, as
shown in figure 4.
![An image showing the launch sequence in twelve consecutive frames, beginning with the launcher icon being tapped and filling the screen as it enlarges](https://developer.android.com/static/images/ui/splash-sequence.png) **Figure 4.** Launch sequence.

1. Enter animation: this consists of the system view to the splash screen. It
   is controlled by the system and isn't customizable.

2. Splash screen (shown during the "wait" portion of the sequence): the splash
   screen can be customized, letting you supply your own logo animation and
   branding. It must meet the [requirements](https://developer.android.com/develop/ui/views/launch/splash-screen#splash-screen-animate-reqs)
   described in this page to work properly.

3. Exit animation: this consists of the animation that hides the splash screen.
   If you want to [customize it](https://developer.android.com/develop/ui/views/launch/splash-screen#customize-animation), use the
   [`SplashScreenView`](https://developer.android.com/reference/android/window/SplashScreenView) and its
   icon. You can run any animation on them, with settings for transform,
   opacity, and color. In this case, manually remove the splash screen when the
   animation is done.

When running the icon animation, app launch gives you the option to skip the
sequence in cases where the app is ready earlier. The app triggers `onResume()`
or the splash screen times out automatically, so make sure the motion can be
comfortably skipped. The splash screen must only be dismissed with `onResume()`
when the app is stable from a visual standpoint, so no additional spinners are
needed. Introducing an incomplete interface can be jarring for users and might
give an impression of unpredictability or lack of polish.

#### Splash screen animation requirements

Your splash screen must adhere to the following specifications:

- Set a single window background color with no transparency. Day and Night
  mode are supported with the
  [`SplashScreen` compat library](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen).

- Make sure the animated icon meets the following specifications:

  - **Format:** the icon must be an [AnimatedVectorDrawable (AVD)](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable) XML.
  - **Dimensions:** an AVD icon must be four times the size of an adaptive icon, as follows:
    - The icon area must be 432 dp---in other words, four times the 108 dp area of an unmasked adaptive icon.
    - The inner two-thirds of the image is visible on the launcher icon, and must be 288 dp---in other words, four times the 72 dp that makes up the inner masked area of an adaptive icon.
  - **Duration:** we recommend not exceeding 1,000 ms on phones. You can use a delayed start, but this can't be longer than 166 ms. If the app startup time is longer than 1,000 ms, consider a looping animation.
- Establish an appropriate time to dismiss the splash screen, which happens as
  your app draws its first frame. You can further customize this as described
  in the section about
  [keeping the splash screen on-screen for longer periods](https://developer.android.com/develop/ui/views/launch/splash-screen#suspend-drawing).

### Splash screen resources

**Figure 5.** Example AVD.

Download the
[](https://developer.android.com/static/resources/splash-screen-news-avd-assets.zip)example starter kit,
which demonstrates how to create, format, and export an animation into an AVD.
It includes the following:

- Adobe After Effects project file of the animation.
- Final exported AVD XML file.
- Example GIF of the animation.

By downloading these files, you agree to the
[Google Terms of Service](https://policies.google.com/terms).

The [Google Privacy Policy](https://policies.google.com/privacy) describes how
data is handled in this service.

## Customize the splash screen in your app

By default, `SplashScreen` uses the `windowBackground` of your theme if
`windowBackground` is a single color. To customize the splash screen, add
attributes to the app theme.

You can customize your app's splash screen by doing any of the following:

- Set theme attributes to change its appearance.

- Keep it on-screen for a longer period.

- Customize the animation for dismissing the splash screen.

### Get started

The core `SplashScreen` library brings the Android 12 splash screen to all
devices from API 23. To add it to your project, add the following snippet to
your `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.core:core-splashscreen:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-splashscreen:1.0.0")
}
```

### Set a theme for the splash screen to change its appearance

You can specify the following attributes in your `Activity` theme to customize
the splash screen for your app. If you already have a legacy splash screen
implementation that uses attributes like `android:windowBackground`, consider
providing an alternate resource file for Android 12 and higher.

1. Use
   [`windowSplashScreenBackground`](https://developer.android.com/reference/android/R.attr#windowSplashScreenBackground)
   to fill the background with a specific single color:

       <item name="android:windowSplashScreenBackground">@color/...</item>

2. Use
   [`windowSplashScreenAnimatedIcon`](https://developer.android.com/reference/android/R.attr#windowSplashScreenAnimatedIcon)
   to replace the icon in the center of the starting window.

   For apps targeting Android 12 (API level 32) only, do the following:

   If the object is animatable and drawable through
   [`AnimationDrawable`](https://developer.android.com/reference/android/graphics/drawable/AnimationDrawable)
   and `AnimatedVectorDrawable`, set `windowSplashScreenAnimationDuration` to
   play the animation while showing the starting window. This isn't required
   for Android 13, because the duration is directly inferred from the
   `AnimatedVectorDrawable`.

       <item name="android:windowSplashScreenAnimatedIcon">@drawable/...</item>

3. Use
   [`windowSplashScreenAnimationDuration`](https://developer.android.com/reference/android/R.attr#windowSplashScreenAnimationDuration)
   to indicate the duration of the splash screen icon animation. Setting this
   doesn't have any effect on the actual time during which the splash screen is
   shown, but you can retrieve it when customizing the splash screen exit
   animation using
   [`SplashScreenView.getIconAnimationDuration`](https://developer.android.com/reference/android/window/SplashScreenView#getIconAnimationDuration()).
   See the following section about
   [keeping the splash screen on-screen for longer periods](https://developer.android.com/develop/ui/views/launch/splash-screen#suspend-drawing)
   for more details.

       <item name="android:windowSplashScreenAnimationDuration">1000</item>

4. Use [`windowSplashScreenIconBackgroundColor`](https://developer.android.com/reference/android/R.attr#windowSplashScreenIconBackgroundColor)
   to set a background behind the splash screen icon. This is useful if there
   isn't enough contrast between the window background and the icon.

       <item name="android:windowSplashScreenIconBackgroundColor">@color/...</item>

5. You can use
   [`windowSplashScreenBrandingImage`](https://developer.android.com/reference/android/R.attr#windowSplashScreenBrandingImage)
   to set an image to be shown at the bottom of the splash screen. However, the
   design guidelines recommend against using a branding image.

       <item name="android:windowSplashScreenBrandingImage">@drawable/...</item>

6. You can use
   [`windowSplashScreenBehavior`](https://developer.android.com/reference/android/R.attr#windowSplashScreenBehavior)
   to specify whether your app always displays the icon on the splash screen in
   Android 13 and higher. The default value is 0, which displays the icon on
   the splash screen if the launching activity sets the `splashScreenStyle` to
   [`SPLASH_SCREEN_STYLE_ICON`](https://developer.android.com/reference/android/window/SplashScreen#SPLASH_SCREEN_STYLE_ICON),
   or follows the system behavior if the launching activity doesn't specify a
   style. If you prefer to never display an empty splash screen and always want
   the animated icon to be displayed, set this to the value `icon_preferred`.

       <item name="android:windowSplashScreenBehavior">icon_preferred</item>

### Keep the splash screen on-screen for longer periods

The splash screen is dismissed as soon as your app draws its first frame. If you
need to load a small amount of data, such as loading in-app settings from a
local disk asynchronously, you can use
[`ViewTreeObserver.OnPreDrawListener`](https://developer.android.com/reference/android/view/ViewTreeObserver.OnPreDrawListener)
to suspend the app to draw its first frame.

If your starting activity finishes before drawing---for example, by not
setting the content view and finishing before `onResume`---the pre-draw
listener isn't needed.

### Kotlin

```kotlin
// Create a new event for the activity.
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Set the layout for the content view.
    setContentView(R.layout.main_activity)

    // Set up an OnPreDrawListener to the root view.
    val content: View = findViewById(android.R.id.content)
    content.viewTreeObserver.addOnPreDrawListener(
        object : ViewTreeObserver.OnPreDrawListener {
            override fun onPreDraw(): Boolean {
                // Check whether the initial data is ready.
                return if (viewModel.isReady) {
                    // The content is ready. Start drawing.
                    content.viewTreeObserver.removeOnPreDrawListener(this)
                    true
                } else {
                    // The content isn't ready. Suspend.
                    false
                }
            }
        }
    )
}
```

### Java

```java
// Create a new event for the activity.
@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // Set the layout for the content view.
    setContentView(R.layout.main_activity);

    // Set up an OnPreDrawListener to the root view.
    final View content = findViewById(android.R.id.content);
    content.getViewTreeObserver().addOnPreDrawListener(
            new ViewTreeObserver.OnPreDrawListener() {
                @Override
                public boolean onPreDraw() {
                    // Check whether the initial data is ready.
                    if (mViewModel.isReady()) {
                        // The content is ready. Start drawing.
                        content.getViewTreeObserver().removeOnPreDrawListener(this);
                        return true;
                    } else {
                        // The content isn't ready. Suspend.
                        return false;
                    }
                }
            });
}
```

### Customize the animation for dismissing the splash screen

You can further customize the animation of the splash screen through
[`Activity.getSplashScreen()`](https://developer.android.com/reference/android/app/Activity#getSplashScreen()).

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // ...

    // Add a callback that's called when the splash screen is animating to the
    // app content.
    splashScreen.setOnExitAnimationListener { splashScreenView ->
        // Create your custom animation.
        val slideUp = ObjectAnimator.ofFloat(
            splashScreenView,
            View.TRANSLATION_Y,
            0f,
            -splashScreenView.height.toFloat()
        )
        slideUp.interpolator = AnticipateInterpolator()
        slideUp.duration = 200L

        // Call SplashScreenView.remove at the end of your custom animation.
        slideUp.doOnEnd { splashScreenView.remove() }

        // Run your animation.
        slideUp.start()
    }
}
```

### Java

```java
@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // ...

    // Add a callback that's called when the splash screen is animating to the
    // app content.
    getSplashScreen().setOnExitAnimationListener(splashScreenView -> {
        final ObjectAnimator slideUp = ObjectAnimator.ofFloat(
                splashScreenView,
                View.TRANSLATION_Y,
                0f,
                -splashScreenView.getHeight()
        );
        slideUp.setInterpolator(new AnticipateInterpolator());
        slideUp.setDuration(200L);

        // Call SplashScreenView.remove at the end of your custom animation.
        slideUp.addListener(new AnimatorListenerAdapter() {
            @Override
            public void onAnimationEnd(Animator animation) {
                splashScreenView.remove();
            }
        });

        // Run your animation.
        slideUp.start();
    });
}
```

By the start of this callback, the
[animated vector drawable](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable)
on the splash screen starts. Depending on the duration of the app launch, the
drawable might be in the middle of its animation. Use
[`SplashScreenView.getIconAnimationStart`](https://developer.android.com/reference/android/window/SplashScreenView#getIconAnimationStart())
to know when the animation started. You can calculate the remaining duration of
the icon animation as follows:

### Kotlin

```kotlin
// Get the duration of the animated vector drawable.
val animationDuration = splashScreenView.iconAnimationDuration
// Get the start time of the animation.
val animationStart = splashScreenView.iconAnimationStart
// Calculate the remaining duration of the animation.
val remainingDuration = if (animationDuration != null && animationStart != null) {
    (animationDuration - Duration.between(animationStart, Instant.now()))
        .toMillis()
        .coerceAtLeast(0L)
} else {
    0L
}
```

### Java

```java
// Get the duration of the animated vector drawable.
Duration animationDuration = splashScreenView.getIconAnimationDuration();
// Get the start time of the animation.
Instant animationStart = splashScreenView.getIconAnimationStart();
// Calculate the remaining duration of the animation.
long remainingDuration;
if (animationDuration != null && animationStart != null) {
    remainingDuration = animationDuration.minus(
            Duration.between(animationStart, Instant.now())
    ).toMillis();
    remainingDuration = Math.max(remainingDuration, 0L);
} else {
    remainingDuration = 0L;
}
```

## Additional resources

- [Migrate your existing splash screen implementation to Android 12 and
  higher](https://developer.android.com/develop/ui/views/launch/splash-screen/migrate)
- [Now in Android](https://github.com/android/nowinandroid) app, which shows a real-world implementation of a splash screen