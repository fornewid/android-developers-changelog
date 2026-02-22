---
title: https://developer.android.com/training/tv/accessibility
url: https://developer.android.com/training/tv/accessibility
source: md.txt
---

This guide provides best practices for accessibility on Android TV and provides
recommendations for both native and non-native apps.

## Why is accessibility important for my TV app?

Vision impairments are not uncommon among the TV-watching population.
An estimated [2.2 billion people globally](https://www.who.int/health-topics/blindness-and-vision-loss#tab=tab_1)
have a vision impairment, according
to the World Health Organization (WHO). In the US, 32 million Americans age 18 and older have experienced
significant vision loss,
according to the [2018 National Health Interview Survey](https://www.afb.org/research-and-initiatives/statistics/adults).
In Europe, the estimates
point to [30 million](http://www.euroblind.org/about-blindness-and-partial-sight/facts-and-figures#:%7E:text=Statistics,sighted%20persons%20as%20blind%20persons)
blind and partially sighted persons, according to the European Blind Union (EBU).

Most importantly, users with vision impairments enjoy media content
just as much as their fully sighted peers. A [2017 survey](https://www.afb.org/research-and-initiatives/statistics/adults) commissioned by Comcast
showed that 96% of users who are blind or have low vision regularly watch
TV, with 81% watching more than an hour per day. However, 65% also reported
encountering problems with looking up what's on TV. And in a [2020 survey in the
UK](https://bighack.org/video-on-demand-streaming-and-accessibility-the-big-hack-survey-feedback/),
80% of disabled people said they had experienced accessibility issues with video
on-demand streaming services.

While assistive technologies can and do help users with low vision, it's
important to support accessibility in content discovery journeys for TV apps.
For example, pay extra attention to providing navigation guidance and
properly labeling elements, and ensure that TV apps work well with accessibility
features like TalkBack. These steps can significantly improve the experience for
users with vision impairments.

The first step toward improving accessibility is awareness. This guide can
help you and your team to uncover accessibility issues with your TV app.

### Android accessibility resources

To learn more about accessibility on Android, see our [accessibility development resources](https://developer.android.com/guide/topics/ui/accessibility).

## Text scaling

Android TV apps should respect the user's preference for text scaling by [supporting different pixel densities](https://developer.android.com/training/multiscreen/screendensities#TaskUseDP).

Take special care to:

- Use `wrap_content` for dimensions in UI components.
- Ensure that layouts rearrange components as their dimensions change depending on the text scale.
- Ensure that components still fit on the screen at larger text scales.
- Don't use sp text size units for components that are not flexible.
- Check the value of `FONT_SCALE` for adjustment in custom views:

      // Checking font scale with Context
      val scale = resources.configuration.fontScale
      Log.d(TAG, "Text scale is: " + scale)

The text scale can be changed with the following command:  

    adb shell settings put system font_scale 1.2f

On Android 12 and above, users can alter the text scaling from the device
settings.

## Keyboard layouts

In Android 13 (API level 33) and higher, you can use
[`getKeyCodeForKeyLocation()`](https://developer.android.com/reference/android/view/InputDevice#getKeyCodeForKeyLocation(int))
to
[look up the keycodes](https://developer.android.com/training/tv/games#keyboard-layouts) for
expected key locations.
This might be necessary if the user has re-mapped some key locations or if they
are using a keyboard that does not have a typical layout.

## Audio description

In Android 13 (API level 33) and higher, a new system-wide accessibility preference
lets users enable audio descriptions across all apps. Android TV apps can
check the user's preference by querying it with
[`isAudioDescriptionRequested()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager#isAudioDescriptionRequested()).  

### Kotlin

```kotlin
private lateinit var accessibilityManager: AccessibilityManager

// In onCreate():
accessibilityManager = getSystemService(AccessibilityManager::class.java)

// Where your media player is initialized
if (am.isAudioDescriptionRequested) {
    // User has requested to enable audio descriptions
}
```

### Java

```java
private AccessibilityManager accessibilityManager;

// In onCreate():
accessibilityManager = getSystemService(AccessibilityManager.class);

// Where your media player is initialized
if(accessibilityManager.isAudioDescriptionRequested()) {
    // User has requested to enable audio descriptions
}
```

Android TV apps can monitor when a user's preference changes by
adding a listener to
[`AccessibilityManager`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager):  

### Kotlin

```kotlin
private val listener =
    AccessibilityManager.AudioDescriptionRequestedChangeListener { enabled ->
        // Preference changed; reflect its state in your media player
    }

override fun onStart() {
    super.onStart()

    accessibilityManager.addAudioDescriptionRequestedChangeListener(mainExecutor, listener)
}

override fun onStop() {
    super.onStop()

    accessibilityManager.removeAudioDescriptionRequestedChangeListener(listener)
}
```

### Java

```java
private AccessibilityManager.AudioDescriptionRequestedChangeListener listener = enabled -> {
    // Preference changed; reflect its state in your media player
};

@Override
protected void onStart() {
    super.onStart();

    accessibilityManager.addAudioDescriptionRequestedChangeListener(getMainExecutor(), listener);
}

@Override
protected void onStop() {
    super.onStop();

    accessibilityManager.removeAudioDescriptionRequestedChangeListener(listener);
}
```