---
title: https://developer.android.com/training/tv/accessibility
url: https://developer.android.com/training/tv/accessibility
source: md.txt
---

This guide provides best practices for accessibility on Android TV and provides
recommendations for both native and non-native apps.

## Why is accessibility important for my TV app?

Vision impairments are not uncommon among TV viewers. The WHO estimates [2.2
billion people globally](https://www.who.int/health-topics/blindness-and-vision-loss#tab=tab_1) have vision impairments, while about 32 million US
adults experience significant loss ([2018 National Health Interview Survey](https://www.afb.org/research-and-initiatives/statistics/adults)).
In Europe, the EBU estimates [30 million](http://www.euroblind.org/about-blindness-and-partial-sight/facts-and-figures#:%7E:text=Statistics,sighted%20persons%20as%20blind%20persons) are affected.

Visually impaired users enjoy media as much as sighted peers. A Comcast [2017
survey](https://www.afb.org/research-and-initiatives/statistics/adults) found 96% watch TV (81% over an hour daily). Yet, 65% report issues
with finding content. Also, 80% of disabled people in a [UK survey](https://bighack.org/video-on-demand-streaming-and-accessibility-the-big-hack-survey-feedback/) reported
streaming issues.

Assistive technologies help, but TV apps must support accessibility in content
discovery. Pay special attention to navigation guidance and element labels.
Ensure compatibility with features like TalkBack to significantly improve the
experience for users with vision impairments.

The first step toward improving accessibility is awareness. This guide can help
you and your team to uncover accessibility issues with your TV app.

### Android accessibility resources

To learn more about accessibility on Android, see our [accessibility development
resources](https://developer.android.com/guide/topics/ui/accessibility).

## Text scaling

Android TV apps should respect the user's preference for text scaling by
[supporting different pixel densities](https://developer.android.com/training/multiscreen/screendensities#TaskUseDP).

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

On Android 12 and higher, users can alter the text scaling from the device
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

In Android 13 (API level 33) and higher, a new system-wide accessibility
preference lets users enable audio descriptions across all apps. Android TV apps
can check the user's preference by querying it with
[`isAudioDescriptionRequested()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager#isAudioDescriptionRequested()).

### Kotlin

    private lateinit var accessibilityManager: AccessibilityManager

    // In onCreate():
    accessibilityManager = getSystemService(AccessibilityManager::class.java)

    // Where your media player is initialized
    if (am.isAudioDescriptionRequested) {
        // User has requested to enable audio descriptions
    }

### Java

    private AccessibilityManager accessibilityManager;

    // In onCreate():
    accessibilityManager = getSystemService(AccessibilityManager.class);

    // Where your media player is initialized
    if(accessibilityManager.isAudioDescriptionRequested()) {
        // User has requested to enable audio descriptions
    }

Android TV apps can monitor when a user's preference changes by
adding a listener to
[`AccessibilityManager`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager):

### Kotlin

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

### Java

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