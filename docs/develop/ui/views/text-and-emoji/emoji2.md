---
title: Support modern emoji  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/text-and-emoji/emoji2
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Support modern emoji Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to support emoji in Compose.

[Support emoji →](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2#emoji-compose)

![](/static/images/android-compose-ui-logo.png)

**Important:** This page describes the
[`androidx.emoji2:emoji2`](/jetpack/androidx/releases/emoji2) library, which
replaces the deprecated androidx.emoji:emoji library.

The standard set of emoji is [refreshed annually by
Unicode](https://emojipedia.org/new/), as emoji usage is increasing
rapidly for all types of apps.

If your app displays internet content or provides text input, *we strongly
recommend supporting the latest emoji fonts.* Otherwise, later emoji might be
displayed as a small square box called *tofu* (☐) or other incorrectly rendered
emoji sequences.

Android versions 11 (API level 30) and lower can't update the emoji font, so
apps that display them on those versions must be updated manually.

The following are examples of modern emoji.

| Examples | Version |
| --- | --- |
| 🫩 🪉 🇨🇶 | [16.0](https://emojipedia.org/emoji-16.0/) (September 2024) |
| 🐦‍🔥 🧑‍🧑‍🧒‍🧒 👩🏽‍🦽‍➡️ 🇲🇶 | [15.1](https://emojipedia.org/emoji-15.1/) (September 2023) |
| 🩷 🫸🏼 🐦‍⬛ | [15.0](https://emojipedia.org/emoji-15.0/) (September 2022) |
| 🫠 🫱🏼‍🫲🏿 🫰🏽 | [14.0](https://emojipedia.org/emoji-14.0/) (September 2021) |
| 😶‍🌫️ 🧔🏻‍♀️ 🧑🏿‍❤️‍🧑🏾 | [13.1](https://emojipedia.org/emoji-13.1/) (September 2020) |
| 🥲 🥷🏿 🐻‍❄️ | [13.0](https://emojipedia.org/unicode-13.0/) (March 2020) |
| 🧑🏻‍🦰 🧑🏿‍🦯 👩🏻‍🤝‍👩🏼 | [12.1](https://emojipedia.org/emoji-12.1/) (October 2019) |
| 🦩 🦻🏿 👩🏼‍🤝‍👩🏻 | [12.0](https://emojipedia.org/emoji-12.0/) (February 2019) |

The `androidx.emoji2:emoji2` library provides simpler backward-compatibility
with lower versions of Android. The `emoji2` library is a dependency of the
[`AppCompat`](/jetpack/androidx/releases/appcompat) library and requires no
further configuration to work.

## Emoji support in Compose

[BOM March 2023](/jetpack/compose/bom/bom) ([Compose UI 1.4](/jetpack/androidx/releases/compose-ui#version_14_2))) brings support for the latest emoji
version, including backwards compatibility with older Android versions down to
API 21. This page covers how to configure modern emoji in the View system. See
the [Emoji in Compose](/jetpack/compose/text/emoji) page for more.

## Prerequisites

To confirm that your app properly displays newer emoji, launch it on a device
running Android 10 (API level 29) or lower. This page includes modern emoji you
can display for testing.

## Use AppCompat to support the latest emoji

`AppCompat` 1.4 includes support for emoji.

To use `AppCompat` to support emoji, do the following:

1. Check that your module depends on the `AppCompat` library version
   [1.4.0-alpha01](/jetpack/androidx/releases/appcompat#1.4.0-alpha01) or
   higher.

   ```
   build.gradle

   // Ensure version is 1.4.0-alpha01 or higher.
   implementation "androidx.appcompat:appcompat.$appcompatVersion"
   ```
2. Ensure all activities that display text extend the
   [`AppCompatActivity`](/reference/androidx/appcompat/app/AppCompatActivity)
   class.

   ### Kotlin

   ```
   MyActivity.kt

   class MyActivity: AppCompatActivity {
   ...
   }
   ```

   ### Java

   ```
   MyActivity.java

   class MyActivity extends AppCompatActivity {
   ...
   }
   ```
3. Test your integration by launching your app on a device running Android 10
   or lower and displaying the following test string. Make sure all characters
   render correctly.

   * 16.0: 🫩, 🪉, 🇨🇶
   * 15.1: 🐦‍🔥, 🧑‍🧑‍🧒‍🧒, 👩🏽‍🦽‍➡️, 🇲🇶
   * 15.0: 🩷, 🫸🏼, 🐦‍⬛
   * 14.0: 🫠, 🫱🏼‍🫲🏿, 🫰🏽
   * 13.1: 😶‍🌫️, 🧔🏻‍♀️, 🧑🏿‍❤️‍🧑🏾
   * 13.0: 🥲, 🥷🏿, 🐻‍❄️
   * 12.1: 🧑🏻‍🦰, 🧑🏿‍🦯, 👩🏻‍🤝‍👩🏼
   * 12.0: 🦩, 🦻🏿, 👩🏼‍🤝‍👩🏻

Your app automatically displays backward-compatible emoji on all devices that
provide an `emoji2`-compatible downloadable fonts provider, such as devices
powered by [Google Play services](https://developers.google.com/android).

### If your app is using AppCompat but displays tofu (☐)

In some cases, your app might display tofu instead of the proper emoji, even if
you add the `AppCompat` library. The following are possible explanations and
solutions.

#### You're running the app on a recently flashed device or a new emulator

Clear the app's Google Play services data to clear any font caching that might
happen during startup. This typically resolves the issue after a few hours.

To clear the app data, do the following:

1. Open **Settings** on your Android-powered device.
2. Tap **Apps & notifications**.
3. Tap **See all apps** or **App info**.
4. Scroll through the apps and tap **Google Play services**.
5. Tap **Storage & cache**.
6. Tap **Clear cache**.

#### Your app isn't using an AppCompat text-related class

This can happen if you don't extend `AppCompatActivity` or if you instantiate a
view in code, such as `TextView`. Check for the following:

* The activity extends `AppCompatActivity`.
* If creating the view in code, use the correct [`AppCompat`
  subclass](#custom-views-appcompat).

`AppCompatActivity` automatically inflates `AppCompatTextView` in place of
`TextView` when inflating XML, so you don't need to update your XML.

#### The test phone doesn't support downloadable fonts

Verify that `DefaultEmojiCompatConfig.create` returns a non-null configuration.

#### An emulator on an earlier API level hasn't upgraded Google Play services

When using an emulator on an earlier API level, you might need to update the
bundled Google Play services for `emoji2` to find the font provider. To do this,
log in to the Google Play Store on the emulator.

To verify that a compatible version is installed, do the following:

1. Run the following command:

   ```
   adb shell dumpsys package com.google.android.gms | grep version
   ```
2. Check that the `versionCode` is higher than `211200000`.

## Support emoji without AppCompat

If your app can't include `AppCompat`, it can use `emoji2` directly. This
requires more work, so only use this method if your app *can't* use `AppCompat`.

To support emoji without the `AppCompat` library, do the following:

1. In your app's `build.gradle` file, include `emoji2` and `emoji2-views`.

   ```
   build.gradle

   def emojiVersion = "1.0.0-alpha03"
   implementation "androidx.emoji2:emoji2:$emojiVersion"
   implementation "androidx.emoji2:emoji2-views:$emojiVersion"
   ```

   The `emoji2-views` module provides
   [subclasses](/reference/androidx/emoji2/widget/package-summary) of
   `TextView`, `Button`, and `EditText` that implement
   [`EmojiCompat`](/reference/androidx/emoji2/text/EmojiCompat). Don't use it
   in an app that includes `AppCompat`, because it already implements
   `EmojiCompat`.
2. In XML and code—wherever you use `TextView`, `EditText`, or
   `Button`—use
   [`EmojiTextView`](/reference/androidx/emoji2/widget/EmojiTextView),
   [`EmojiEditText`](/reference/androidx/emoji2/widget/EmojiEditText), or
   [`EmojiButton`](/reference/androidx/emoji2/widget/EmojiButton) instead.

   ```
   activity_main.xml

   <androidx.emoji2.widget.EmojiTextView ... />
   <androidx.emoji2.widget.EmojiEditText ... />
   <androidx.emoji2.widget.EmojiButton ... />
   ```

   By including the `emoji2` module, the system uses the default downloadable
   fonts provider to [load the emoji font
   automatically](#impact-automatic-config) shortly after app startup. No
   further configuration is needed.
3. To test your integration, launch your app on a device running Android 11 or
   lower and displaying the following test strings. Make sure all characters
   render correctly.

   * 16.0: 🫩, 🪉, 🇨🇶
   * 15.1: 🐦‍🔥, 🧑‍🧑‍🧒‍🧒, 👩🏽‍🦽‍➡️, 🇲🇶
   * 15.0: 🩷, 🫸🏼, 🐦‍⬛
   * 14.0: 🫠, 🫱🏼‍🫲🏿, 🫰🏽
   * 13.1: 😶‍🌫️, 🧔🏻‍♀️, 🧑🏿‍❤️‍🧑🏾
   * 13.0: 🥲, 🥷🏿, 🐻‍❄️
   * 12.1: 🧑🏻‍🦰, 🧑🏿‍🦯, 👩🏻‍🤝‍👩🏼
   * 12.0: 🦩, 🦻🏿, 👩🏼‍🤝‍👩🏻

### Use EmojiCompat without widgets

`EmojiCompat` uses [`EmojiSpan`](/reference/androidx/emoji2/text/EmojiSpan) to
render correct images. Therefore, it has to convert any given
[`CharSequence`](/reference/java/lang/CharSequence) object into a
[`Spanned`](/reference/android/text/Spanned) object with `EmojiSpan` objects.
The EmojiCompat class provides the `process()` method to convert `CharSequences`
into `Spanned` instances. Using this method, you can call `process()` in the
background and cache the results, which improves the performance of your app.

### Kotlin

```
val processed = EmojiCompat.get().process("neutral face \uD83D\uDE10")
```

### Java

```
CharSequence processed = EmojiCompat.get().process("neutral face \uD83D\uDE10");
```

### Use EmojiCompat for input method editors

The `EmojiCompat` class lets keyboards render the emoji supported by the app
they are interacting with. [Input method editors
(IMEs)](/guide/topics/text/creating-input-method) can use the
[`getEmojiMatch()`](/reference/androidx/emoji2/text/EmojiCompat#getEmojiMatch(java.lang.CharSequence,int))
method to check whether an instance of `EmojiCompat` is capable of rendering an
emoji. This method takes a [`CharSequence`](/reference/java/lang/CharSequence)
of an emoji and returns `true` if `EmojiCompat` can detect and render the emoji.

The keyboard can also check the version of `EmojiCompat` that the app supports
to determine which emoji to render in the palette. To check the version, if
available, the keyboard can look for the following keys in the
[`EditorInfo.extras`](/reference/android/view/inputmethod/EditorInfo#extras)
bundle:

* [`EDITOR_INFO_METAVERSION_KEY`](/reference/androidx/emoji2/text/EmojiCompat#EDITOR_INFO_METAVERSION_KEY()):
  represents the version of the emoji metadata that the app uses. If this key
  doesn't exist, then the app isn't using `EmojiCompat`.
* [`EDITOR_INFO_REPLACE_ALL_KEY`](/reference/androidx/emoji2/text/EmojiCompat#EDITOR_INFO_REPLACE_ALL_KEY()):
  if the key exists and is set to `true`, then the app configures
  `EmojiCompat` to replace all emoji, even if they are present in the system.

Learn more about how to [configure an instance of
EmojiCompat](#modify-behavior).

## Use emoji in custom views

If your app has [custom views](/training/custom-views/create-view) that are
direct or indirect subclasses of `TextView`—for example, `Button`,
`Switch`, or `EditText`—and those views can display user-generated
content, they must each implement
[`EmojiCompat`](/guide/topics/ui/look-and-feel/emoji-compat).

The process varies depending on whether your app uses the `AppCompat` library.

### Add custom views for apps with AppCompat

If your app uses `AppCompat`, extend the `AppCompat` implementation instead of
the platform implementation. Use the following table as a guide for how to
extend your views in `AppCompat`:

| **Instead of extending...** | **Extend** |
| --- | --- |
| `TextView` | `AppCompatTextView` |
| `EditText` | `AppCompatEditText` |
| `ToggleButton` | `AppCompatToggleButton` |
| `Switch` | `SwitchCompat` |
| `Button` | `AppCompatButton` |
| `CheckedTextView` | `AppCompatCheckedTextView` |
| `RadioButton` | `AppCompatRadioButton` |
| `CheckBox` | `AppCompatCheckBox` |
| `AutoCompleteTextView` | `AppCompatAutoCompleteTextView` |
| `MultiAutoCompleteTextView` | `AppCompatMultiAutoCompleteTextView` |

### Add custom views for apps without AppCompat

If your app doesn't use `AppCompat`, use the view integration helpers in the
`emoji2-views-helper` module that are designed for use in custom views. These
are the helpers that the `AppCompat` library uses to implement emoji support.

Complete the following steps to support custom views for apps that don't use
`AppCompat`.

1. Add the `emoji2-views-helper` library:

   ```
   implementation "androidx.emoji2:emoji2-views-helper:$emojiVersion"
   ```
2. Follow the instructions to include
   [`EmojiTextViewHelper`](/reference/androidx/emoji2/viewsintegration/EmojiTextViewHelper)
   or
   [`EmojiEditTextHelper`](/reference/androidx/emoji2/viewsintegration/EmojiEditTextHelper)
   in your app's custom views.
3. Test your integration by launching your app on a device running Android 10
   or lower and displaying the following test string. Make sure all characters
   render correctly.

   * 16.0: 🫩, 🪉, 🇨🇶
   * 15.1: 🐦‍🔥, 🧑‍🧑‍🧒‍🧒, 👩🏽‍🦽‍➡️, 🇲🇶
   * 15.0: 🩷, 🫸🏼, 🐦‍⬛
   * 14.0: 🫠, 🫱🏼‍🫲🏿, 🫰🏽
   * 13.1: 😶‍🌫️, 🧔🏻‍♀️, 🧑🏿‍❤️‍🧑🏾
   * 13.0: 🥲, 🥷🏿, 🐻‍❄️
   * 12.1: 🧑🏻‍🦰, 🧑🏿‍🦯, 👩🏻‍🤝‍👩🏼
   * 12.0: 🦩, 🦻🏿, 👩🏼‍🤝‍👩🏻

**Note:** For apps not using `AppCompat`, you can either extend the
`EmojiCompat*View` classes or use view helper classes to integrate manually.

## Optional features for handling emoji2

After you include the `emoji2` library in your app, you can add the optional
features that are described in this section.

### Configure emoji2 to use a different font or downloadable font provider

To configure `emoji2` to use a different font or downloadable font provider, do
the following:

1. Disable the
   [`EmojiCompatInitializer`](/reference/androidx/emoji2/text/EmojiCompatInitializer)
   by adding the following to your manifest:

   ```
   <provider
   android:name="androidx.startup.InitializationProvider"
   android:authorities="${applicationId}.androidx-startup"
   android:exported="false"
   tools:node="merge">
   <meta-data android:name="androidx.emoji2.text.EmojiCompatInitializer"
              tools:node="remove" />
   </provider>
   ```
2. Do one of the following:

   * Use the default configuration by calling
     [`DefaultEmojiCompatConfiguration.create(context)`](/reference/androidx/emoji2/text/DefaultEmojiCompatConfig#create(android.content.Context)).
   * Create your own configuration to load fonts from another source using
     [`EmojiCompat.Config`](/reference/androidx/emoji2/text/EmojiCompat.Config).
     This class provides several options to modify your `EmojiCompat`
     behavior, as described in the following section.

**Caution:** If you disable the default configuration, verify that emoji appear
correctly in your app. Call `EmojiCompat.init` shortly after startup. You can
safely call `init()` from `Application.onCreate()`, passing in
[`LOAD_STRATEGY_MANUAL`](/reference/androidx/emoji2/text/EmojiCompat#LOAD_STRATEGY_MANUAL()),
and then later call
[`EmojiCompat.load()`](/reference/androidx/emoji2/text/EmojiCompat#load()) from
a background thread.

#### Modify your EmojiCompat behavior

You can use an instance of `EmojiCompat.Config` to modify `EmojiCompat`
behavior.

The most important configuration option is
[`setMetadataLoadStrategy()`](/reference/androidx/emoji2/text/EmojiCompat.Config#setMetadataLoadStrategy(int)),
which controls when `EmojiCompat` loads the font. Font loading begins as soon as
`EmojiCompat.load()` is called, and this triggers any necessary downloads. The
system creates a thread for font downloading unless your app provides one.

`LOAD_STRATEGY_MANUAL` lets you control when `EmojiCompat.load()` is called, and
[`LOAD_STRATEGY_DEFAULT`](/reference/androidx/emoji2/text/EmojiCompat#LOAD_STRATEGY_DEFAULT())
makes loading start synchronously in the call to
[`EmojiCompat.init()`](/reference/androidx/emoji2/text/EmojiCompat#init(androidx.emoji2.text.EmojiCompat.Config)).

Most apps use `LOAD_STRATEGY_MANUAL` so they can control the thread and timing
of font loading. Your app must defer until after the first screen displays to
avoid introducing startup latency. `EmojiCompatInitializer` follows this
practice and defers loading the emoji font until after the first screen resumes.

Use the following methods from the base class to set other aspects of the
configuration:

* [`setReplaceAll()`](/reference/androidx/emoji2/text/EmojiCompat.Config#setReplaceAll(boolean)):
  determines whether `EmojiCompat` replaces all emoji it finds with instances
  of `EmojiSpan`. By default, when `EmojiCompat` infers that the system can
  render an emoji, it doesn't replace that emoji. When set to `true`,
  `EmojiCompat` replaces all emoji with `EmojiSpan` objects.
* [`setEmojiSpanIndicatorEnabled()`](/reference/androidx/emoji2/text/EmojiCompat.Config#setEmojiSpanIndicatorEnabled(boolean)):
  indicates whether `EmojiCompat` replaces an emoji with an `EmojiSpan`
  object. When set to `true`, `EmojiCompat` draws a background for the
  `EmojiSpan`. This method is mainly used for debugging purposes.
* [`setEmojiSpanIndicatorColor`](/reference/androidx/emoji2/text/EmojiCompat.Config#setEmojiSpanIndicatorColor(int)):
  sets the color to indicate an `EmojiSpan`. The default value is
  [`GREEN`](/reference/android/graphics/Color#GREEN).
* [`registerInitCallback()`](/reference/androidx/emoji2/text/EmojiCompat.Config#registerInitCallback(androidx.emoji2.text.EmojiCompat.InitCallback)):
  informs an app about the state of the `EmojiCompat` initialization.

### Add initialization listeners

`EmojiCompat` and `EmojiCompat.Config` classes provide the
[`registerInitCallback()`](/reference/androidx/emoji2/text/EmojiCompat#registerInitCallback(androidx.emoji2.text.EmojiCompat.InitCallback))
and
[`unregisterInitCallback()`](/reference/androidx/emoji2/text/EmojiCompat#unregisterInitCallback(androidx.emoji2.text.EmojiCompat.InitCallback))
methods to register and unregister initialization callbacks. Your app uses these
callbacks to wait until `EmojiCompat` is initialized before you process emoji on
a background thread or in a custom view.

To use these methods, create an instance of the
[`EmojiCompat.InitCallback`](/reference/androidx/emoji2/text/EmojiCompat.InitCallback)
class. Call these methods and pass in the instance of the
`EmojiCompat.InitCallback` class. When the initialization is successful, the
`EmojiCompat` class calls the
[`onInitialized()`](/reference/androidx/emoji2/text/EmojiCompat.InitCallback#onInitialized())
method. If the library fails to initialize, the `EmojiCompat` class calls the
[`onFailed()`](/reference/androidx/emoji2/text/EmojiCompat.InitCallback#onFailed(java.lang.Throwable))
method.

To check the initialization state at any point, call the
[`getLoadState()`](/reference/androidx/emoji2/text/EmojiCompat#getLoadState())
method. This method returns one of the following values:
[`LOAD_STATE_LOADING`](/reference/androidx/emoji2/text/EmojiCompat#LOAD_STATE_LOADING()),
[`LOAD_STATE_SUCCEEDED`](/reference/androidx/emoji2/text/EmojiCompat#LOAD_STATE_SUCCEEDED()),
or
[`LOAD_STATE_FAILED`](/reference/androidx/emoji2/text/EmojiCompat#LOAD_STATE_FAILED()).

### Support bundled fonts with emoji2

You can use the `emoji2-bundled` artifact to bundle an emoji font into your app.
**However, because the `NotoColorEmoji` font is over 10 MB, we strongly
recommend that your app use downloadable fonts when possible.** The
`emoji2-bundled` artifact is intended for apps on devices that don't support
downloadable fonts.

To use the `emoji2-bundled` artifact, do the following:

1. Include `emoji2-bundled` and `emoji2` artifacts:

   ```
   implementation "androidx.emoji2:emoji2:$emojiVersion"
   implementation "androidx.emoji2:emoji2-bundled:$emojiVersion"
   ```

   **Caution:** Including the `emoji2-bundled` artifact disables the
   `EmojiCompatInitializer`, so your app must call `EmojiCompat.init()`.
2. Configure `emoji2` to use the bundled configuration:

   ### Kotlin

   ```
   EmojiCompat.init(BundledEmojiCompatConfig(context))
   ```

   ### Java

   ```
   EmojiCompat.init(new BundledEmojiCompatConfig(context));
   ```
3. Test the integration by following the preceding steps for including
   `emojicompat` with or without `AppCompat`. Make sure the test string
   displays correctly.

   * 16.0: 🫩, 🪉, 🇨🇶
   * 15.1: 🐦‍🔥, 🧑‍🧑‍🧒‍🧒, 👩🏽‍🦽‍➡️, 🇲🇶
   * 15.0: 🩷, 🫸🏼, 🐦‍⬛
   * 14.0: 🫠, 🫱🏼‍🫲🏿, 🫰🏽
   * 13.1: 😶‍🌫️, 🧔🏻‍♀️, 🧑🏿‍❤️‍🧑🏾
   * 13.0: 🥲, 🥷🏿, 🐻‍❄️
   * 12.1: 🧑🏻‍🦰, 🧑🏿‍🦯, 👩🏻‍🤝‍👩🏼
   * 12.0: 🦩, 🦻🏿, 👩🏼‍🤝‍👩🏻

## Impact of automatic EmojiCompat configuration

The system applies default configuration using the startup library,
`EmojiCompatInitializer`, and
[`DefaultEmojiCompatConfig`](/reference/androidx/emoji2/text/DefaultEmojiCompatConfig).

After the first activity resumes in your app, the initializer schedules emoji
font loading. This brief delay lets your app display its initial content without
any potential latency due to font loading in a background thread.

`DefaultEmojiCompatConfig` looks for a system-installed downloadable font
provider that implements the `EmojiCompat` interface, such as Google Play
services. On devices powered by Google Play services, this loads the font using
Google Play services.

**Note:** The default `emoji2` configuration uses downloadable fonts to fetch a
compatible font file. On devices powered by Google Play services, the app sends
this query at startup to Google Play services. The request for a font is logged
by Google Play services and downloadable fonts.

The initializer creates a background thread to load the emoji font, and font
download can take up to 10 seconds before timing out. After the font is
downloaded, it takes approximately 150 milliseconds on a background thread to
initialize `EmojiCompat`.

Defer the initialization of `EmojiCompat`, even if you disable
`EmojiCompatInitializer`. If you [manually configure
`EmojiCompat`](#modify-behavior), call `EmojiCompat.load()` after it displays
the first screen of your app to avoid background contention with the first
screen load.

After loading, `EmojiCompat` uses about 300 KB of RAM to hold the emoji
metadata.