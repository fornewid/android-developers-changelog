---
title: https://developer.android.com/jetpack/androidx/releases/emoji2
url: https://developer.android.com/jetpack/androidx/releases/emoji2
source: md.txt
---

# Emoji2

[User Guide](https://developer.android.com/guide/topics/ui/look-and-feel/emoji-compat) [Code Sample](https://github.com/android/user-interface-samples) API Reference  
[androidx.emoji2.text](https://developer.android.com/reference/kotlin/androidx/emoji2/text/package-summary)  
[androidx.emoji2.viewshelper](https://developer.android.com/reference/kotlin/androidx/emoji2/viewshelper/package-summary)  
[androidx.emoji2.widget](https://developer.android.com/reference/kotlin/androidx/emoji2/widget/package-summary)  
Display emoji in current and older devices.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| September 10, 2025 | [1.6.0](https://developer.android.com/jetpack/androidx/releases/emoji2#1.6.0) | - | - | - |

## Declaring dependencies

To add a dependency on Emoji2, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    def emoji2_version = "1.6.0"

    implementation "androidx.emoji2:emoji2:$emoji2_version"
    implementation "androidx.emoji2:emoji2-views:$emoji2_version"
    implementation "androidx.emoji2:emoji2-views-helper:$emoji2_version"
}
```

### Kotlin

```kotlin
dependencies {
    val emoji2_version = "1.6.0"

    implementation("androidx.emoji2:emoji2:$emoji2_version")
    implementation("androidx.emoji2:emoji2-views:$emoji2_version")
    implementation("androidx.emoji2:emoji2-views-helper:$emoji2_version")
}
```

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460938+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460938&template=1422574)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Emoji2 Emojipicker Version 1.0

### Version 1.5.0

September 4, 2024

`androidx.emoji2:emoji2-*:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0adbbe89afc8940ce38426fa770f2b800023143f..d54bd534b3505f8abf050634eb0fdd0d7219707b/emoji2).

**Important changes since 1.4.0**

- Support emoji 15.1 and bidirectional emoji selector UI. A simple click on the bidirectional switcher allows users to toggle between left- and right-facing versions of emojis.
- Support multi-skintone emoji selector. Long-pressing couple emojis reveals a multi-person emoji selector for the zero state. When the user taps on the left half of an emoji, the emoji preview on the bottom right will be updated accordingly. When the user selects both halves of an emoji, the emoji preview on the bottom right will show the entire emoji and the user can then input it.

### Version 1.0.0-alpha03

March 8, 2023

`androidx.emoji2:emoji2-emojipicker:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/emoji2/emoji2-emojipicker)

**Bug Fixes**

- Removed unnecessary resources and reduced library size by \~0.3M.

### Version 1.0.0-alpha02

February 22, 2023

`androidx.emoji2:emoji2-emojipicker:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..87533b4ff06971ed59028936cd9b6da988cd4522/emoji2/emoji2-emojipicker)

**API Changes**

- Added new API for java clients to be able to provide recent emojis. ([I39d10](https://android-review.googlesource.com/#/q/I39d1054670ddadeba062810de9b36418843d7c19))

**Bug Fixes**

- Update emoji resources to support emoji 15.0 ([Ib4eb3](https://android-review.googlesource.com/#/q/Ib4eb3565f7cf2f4c4f72268e5b04001b181136e7))
- When picking an emoji from the popup window, update all identical emojis to the newly picked emoji (except the recent emoji row). Also announce the emoji when clicking. ([I892c6](https://android-review.googlesource.com/#/q/I892c6e734ee5be608b2dd632234553bb0d2093f9))
- Wait for emojicompat to load before showing the `EmojiPickerView`. ([I29e03](https://android-review.googlesource.com/#/q/I29e030aa682ddb59add4280d27cac241cbdcdbe2))

### Version 1.0.0-alpha01

January 25, 2023

`androidx.emoji2:emoji2-emojipicker:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/emoji2/emoji2-emojipicker)

**New Features**

- Introduced an emoji picker which provides consistent user experience with the latest emojis across Android OS OEM devices and apps. It provides the latest emoji support and emoji picker UI including skin-tone variants and emoji compat support.

**API Changes**

- Introduced `EmojiPickerView` class that provides up-to-date emojis in a vertical scrollable view with a clickable horizontal header.
- The emoji picker grid columns can be set via XML attribute `emojiGridColumns` or function `setEmojiGridColumns()`.
- The emoji picker grid rows can be set via XML attribute `emojiGridRows` or function `setEmojiGridRows()`.
- The emoji picked listener can be set via `setOnEmojiPickedListener()` and the listener will be notified whenever the user clicked any emoji.
- The recent emoji provider can be provided with `setRecentEmojiProvider()`. This is an optional function. If the recent emoji provider isn't set, a default recent emoji provider will be used by the library. The default behavior is defined as follows: 1) all selected emojis will be saved per-app level in shared preferences. 2) the picker will display at most 3 rows of selected emojis, deduped, in reverse chronological order.
- Introduced `EmojiViewItem` class that holds the displayed emoji and its emoji variants.
- Introduced `RecentEmojiProvider` interface that can be implemented to provide a recent emoji list. The `recentEmojiProvider` is responsible for providing emojis in the "Recently Used" category.

## Version 1.6

### Version 1.6.0

September 10, 2025

`androidx.emoji2:emoji2-*:1.6.0` is released. Version 1.6.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/85d9c24a52883a4d83bebd4f6f3674f47e4d4c9b..9ed4b1acacae02bd637e1932def67751b89244cb/emoji2).

**Important changes since 1.5.0:**

- Supports emoji 16.0
- Add "emoji" suffix to the content description of emojis.

**Bug Fixes**

- Moving the default `minSdk` from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 1.6.0-rc01

August 13, 2025

`androidx.emoji2:emoji2-*:1.6.0-rc01` is released. Version 1.6.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..85d9c24a52883a4d83bebd4f6f3674f47e4d4c9b/emoji2).

**New Features**

- Supported Emoji 16.0 and added "emoji" suffix to the content description.

**API Changes**

- Removing obsolete `@RequiresApi(21)` annotations ([Ic4792](https://android-review.googlesource.com/#/q/Ic47923dcc82f4b7c4638fadb10c2c0268b414fcd))
- Removing obsolete `@RequiresApi(21)` annotations ([I9103b](https://android-review.googlesource.com/#/q/I9103beb2d5f73470f3abfdf034bc2b473be923e6))

### Version 1.6.0-beta01

July 2, 2025

`androidx.emoji2:emoji2-*:1.6.0-beta01` is released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..1b437892629a2cdedb46d9b7232575987b2cc6b5/emoji2).

**New Features**

- Support Emoji 16.0 updates
- Add "emoji" suffix to the content description to make sure that we have a consistent accessibility behavior across all emoji picker apps.

### Version 1.6.0-alpha01

June 4, 2025

`androidx.emoji2:emoji2-*:1.6.0-alpha01` is released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d54bd534b3505f8abf050634eb0fdd0d7219707b..786176dc2284c87a0e620477608e0aca9adeff15/emoji2).

**New Features**

- Emoji 16.0 data updates ([Ifc878](https://android-review.googlesource.com/#/q/Ifc87850ef48d8d2a01f350e6a24cb893e617d222))
- Adding "emoji" suffix to the content description

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage: `-Xjspecify-annotations=strict`, `-Xtype-enhancement-improvements-strict-mode` ([Id07e7](https://android-review.googlesource.com/#/q/Id07e72428528003ad92b9ab1475ec46f877c9bc6), [b/326456246](https://issuetracker.google.com/issues/326456246))

## Version 1.5

### Version 1.5.0

September 4, 2024

`androidx.emoji2:emoji2-*:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0adbbe89afc8940ce38426fa770f2b800023143f..d54bd534b3505f8abf050634eb0fdd0d7219707b/emoji2).

**Important changes since 1.4.0**

- Support emoji 15.1 and bidirectional emoji selector UI. A simple click on the bidirectional switcher allows users to toggle between left- and right-facing versions of emojis.
- Support multi-skintone emoji selector. Long-pressing couple emojis reveals a multi-person emoji selector for the zero state. When the user taps on the left half of an emoji, the emoji preview on the bottom right will be updated accordingly. When the user selects both halves of an emoji, the emoji preview on the bottom right will show the entire emoji and the user can then input it.

### Version 1.5.0-rc01

August 21, 2024

`androidx.emoji2:emoji2-*:1.5.0-rc01` is released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..0adbbe89afc8940ce38426fa770f2b800023143f/emoji2).

**New Features**

- Support emoji 15.1 and bidirectional emoji selector UI. A simple click on the bidirectional switcher allows users to toggle between left and right-facing versions of emojis.
- Support multi-skintone emoji selector. Long-pressing couple emojis reveals a multi-person emoji selector for the zero state. When the user taps on the left half of an emoji, the emoji preview on the bottom right will be updated accordingly. When the user selects both halves of an emoji, the preview will show the entire emoji and the usr can then input it.

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada), [b/345472586](https://issuetracker.google.com/issues/345472586))
- `EmojiPickerView`'s tab selection and indicator updates one click behind. ([146b02](https://android-review.googlesource.com/c/platform/frameworks/support/+/2657077), [b/288261054](https://issuetracker.google.com/issues/288261054))
- `EmojiPickerView`'s tab selection and indicator is broken. ([5e1f14](https://android-review.googlesource.com/c/platform/frameworks/support/+/2970143), [b/273883688](https://issuetracker.google.com/issues/273883688))

### Version 1.5.0-beta01

July 10, 2024

`androidx.emoji2:emoji2-*:1.5.0-beta01` is released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..56579bc30499ce39f0d7a6713a065b00c6194206/emoji2).

**New Features**

- Support emoji 15.1 and bidirectional emoji selection UI.
- Support multi-skintone selection redesign.

**Bug Fixes**

- `EmojiPickerView`'s tab selection and indicator updates one click behind. ([146b02](https://android-review.googlesource.com/#/q/146b021cc44151e8a69e26fc8c7f54bb7a92e892), [b/288261054](https://issuetracker.google.com/issues/288261054))
- `EmojiPickerView`'s tab selection and indicator is broken. ([5e1f14](https://android-review.googlesource.com/#/q/5e1f1404b5689979eeb0cd0b36e509631bd274a1), [b/273883688](https://issuetracker.google.com/issues/273883688))

### Version 1.5.0-alpha01

December 13, 2023

`androidx.emoji2:emoji2-*:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d25c5e925564cf1f52fb6d2f88088d2dd5becfe..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/emoji2)

**New Features**

- `emoji2-bundled` contains an updated emoji font to support Emoji 15.1.

**API Changes**

- Add executors to control the callback thread for `InitCallback`. ([I32b67](https://android-review.googlesource.com/#/q/I32b67d1932dd1b37cbe96d81fea1d1722fc371a2))
- `BundledEmojiCompatConfig` now takes an executor to control loading threads. ([I00e81](https://android-review.googlesource.com/#/q/I00e81d20bde02b82e2af919d182c165080526213))

## Version 1.4

### Version 1.4.0

August 9, 2023

`androidx.emoji2:emoji2-*:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1ecf42715c27ef260259d14b89741160bd9af93c..2d25c5e925564cf1f52fb6d2f88088d2dd5becfe/emoji2)

**Important changes since 1.3.0**

- Introduced emoji picker library. Checkout the [developer doc](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-picker) for more details.

### Version 1.4.0-rc01

July 26, 2023

`androidx.emoji2:emoji2-*:1.4.0-rc01` is released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..1ecf42715c27ef260259d14b89741160bd9af93c/emoji2)

**API Changes**

- Introduce `registerSource` list ([Iae92f](https://android-review.googlesource.com/#/q/Iae92f73b77d4a69b51a7db9e4f355e77d9770491))
- API Council feedback: renamed `TransitionManager.seekTo()` to `createSeekController()`. Please adjust previous comment about adding `TransitionManager.seekTo()` to `TransitionManager.createSeekController()`. ([Idbeb1](https://android-review.googlesource.com/#/q/Idbeb188f4bea286da7f3de7689a023f3cb5e3cb1))
- Added `ExerciseRouteResult`, which is not the superclass for `Data`, `NoData` and `ConsentRequiredStates`. Added `ExerciseRoute` as a standalone class, which holds location data for the route. ([I22eed](https://android-review.googlesource.com/#/q/I22eedcdd68b0842e538c602db058525a556c5ed2))
- Introduced `PagerLayoutInfo` with information collected after a measure pass in Pager. Also introduced PageInfo, the information about a single measured Page in Pager. ([Iad003](https://android-review.googlesource.com/#/q/Iad003bd71d5d26a6b0507f0c6c06751b3969d95c), [b/283098900](https://issuetracker.google.com/issues/283098900))

**Bug Fixes**

- We have updated the colors for `Button`, `IconButton` and `TextButton` in line with Material3 design. The semantic role for `Button`, `IconButton` and `TextButton` can now be overridden using `Modifier.semantics`. ([Ib2495](https://android-review.googlesource.com/#/q/Ib24954145bc5440092cc2ac7dd18d3bc4fd4b756))
- Fixed `EmojiPickerView`'s tab selection and indicator updates one click behind. ([I4db04](https://android-review.googlesource.com/q/I4db044ca9a80fe7076bb92bda035550e034859bb))
- `FileNotFoundException` on showing the emoji picker ([I353e4](https://android-review.googlesource.com/q/I353e467c6dda16276ace15b15921c81012c78d6d))
- Catch the `WindowManager.BadTokenException` when using `EmojiPickerView` ([I0a144](https://android-review.googlesource.com/#/q/I0a1443025e80328fc33f8172612689b3d9017296))

### Version 1.4.0-beta05

June 7, 2023

`androidx.emoji2:emoji2-*:1.4.0-beta05` is released. [Version 1.4.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..73f902dee011bfe400d8a0330bfd8d4bb632065f/emoji2)

**Bug Fixes**

- Fixed a bug introduced in 1.3 that would cause `MetricsAffectingSpans` such as `RelativeSizeSpan` to apply twice. Once during text layout, and again inside of `EmojiSpan.draw`. The result was incorrectly sized draw, visible if any of the text size parameters were changed by the span. ([b/283208650](http://b/283208650))

### Version 1.4.0-beta04

May 24, 2023

`androidx.emoji2:emoji2-*:1.4.0-beta04` is released. [Version 1.4.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/emoji2)

This release fixes a bug present since 1.0 where views with a non-main handler would throw an exception when attempting to update the emoji spans after font load completes. There is no workaround, if you are impacted by this bug please upgrade to this version or later.

**Bug Fixes**

- `EmojiCompat` init callbacks will now use the handler from each view, respecting views not on the main thread. ([Iccbcf](https://android-review.googlesource.com/#/q/Iccbcfb16840662f348cb632cfba9b263fb7ad963))

### Version 1.4.0-beta03

May 10, 2023

`androidx.emoji2:emoji2-*:1.4.0-beta03` is released. [Version 1.4.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/emoji2)

**Bug Fixes**

- Fix emoji picker nested popup view crash. ([0acc8e](https://android.googlesource.com/platform/frameworks/support/+/0acc8ef931befd9306d77bb3560bba030c619e52))
- Throw early exceptions in the `EmojiCompat getEmojiStart/getEmojiEnd`. ([26177f](https://android.googlesource.com/platform/frameworks/support/+/26177ffa93c25fe6bdb5c67ab99c1db2a38f3652))

### Version 1.4.0-beta02

April 19, 2023

`androidx.emoji2:emoji2-*:1.4.0-beta02` is released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/emoji2)

**Bug Fixes**

- Update lint baseline files ([Iaa212](https://android-review.googlesource.com/#/q/Iaa212192c3071141028fcaf7662f6e112c7c0f23))

### Version 1.4.0-beta01

April 5, 2023

`androidx.emoji2:emoji2-*:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/emoji2)

**New Features**

`androidx.emoji2:emoji2-emojipicker`

The Emoji Picker is a UI solution that offers a modern look and feel, up-to-date emojis, and ease of use. Users can browse and select emojis and their variants, or choose from their recently used emojis. With this library, apps across different OEMs can provide an inclusive and unified emoji experience to their users without the developers having to build and maintain their own emoji picker from scratch.

**Up-to-date Emojis**

New emojis are released every year, and we will selectively include them in the Emoji Picker. To ensure backward compatibility, we perform an accurate emoji renderability check internally to eliminate tofu. This will ensure that the library is compatible across multiple Android versions and devices.

**Sticky variants**

Long-pressing an emoji will display a menu of variants, such as different genders or skin tones. The variant you choose will be saved in the emoji picker, and the last selected variant will be used in the main panel. With this feature, users can send their preferred emoji variants with just one tap.

**Recent emoji**

The `RecentEmojiProvider` is responsible for providing emojis in the "Recently Used" category. The library has a default recent emoji provider that satisfies the most common use case:

- All selected emojis are saved per-app level in shared preferences.
- The picker displays at most 3 rows of selected emojis, deduped, in reverse chronological order.

If this default behavior is sufficient, then you don't need to set the `setRecentEmojiProvider()` method.

**Work with EmojiCompat**

If the app has an `EmojiCompat` instance, it will be used in the emoji picker to render as many emojis as possible. If `EmojiCompat` is disabled, the emoji picker will still work fine.

**How to use the library**

To use the library, an app developer should

1. Import `androidx.emoji2:emojipicker:$version` in `build.gradle`.

       dependencies {
         implementation "androidx.emoji2:emojipicker:$version"
       }

2. Inflate the emoji picker view and optionally set `emojiGridRows` and `emojiGridColumns` based on the desired size of each emoji cell

   - You could leave them unset, the default is 9 `emojiGridColumns`, rows will be calculated based on the parent view height and `emojiGridColumns`
   - You could set `emojiGridRows` as a float to indicate there's more emojis if scroll down in XML

        <androidx.emoji2.emojipicker.EmojiPickerView
         android:id="@+id/emoji_picker"
         android:layout_width="match_parent"
         android:layout_height="match_parent"
         app:emojiGridColumns="9" />

in code

        val emojiPickerView = EmojiPickerView(context).apply {
            emojiGridColumns = 15
            layoutParams = ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.MATCH_PARENT
            )
        }
        findViewById<ViewGroup>(R.id.emoji_picker_layout).addView(emojiPickerView)

1. Assuming you would like to append the selected emojis to a EditText, use `setOnEmojiPickedListener()`

         emojiPickerView.setOnEmojiPickedListener {
             findViewById<EditText>(R.id.edit_text).append(it.emoji)
         }

2. Optionally set `RecentEmojiProvider`, see sample app for an example implementation.

3. Optionally customize styles. Create your own style to override common theme attributes and apply the style to the `EmojiPickerView`. For example, overriding `colorControlNormal` will change the category icon color.

         <style name="CustomStyle" >
             <item name="colorControlNormal">#FFC0CB</item>
         </style>
         <androidx.emoji2.emojipicker.EmojiPickerView
             android:id="@+id/emoji_picker"
             android:layout_width="match_parent"
             android:layout_height="match_parent"
             android:theme="@style/CustomStyle"
             app:emojiGridColumns="9" />

See sample app for an example implementation.

A full API surface can be found [here](https://github.com/androidx/androidx/blob/androidx-main/emoji2/emoji2-emojipicker/api/current.txt).

**Sample App**

This [sample](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/emoji2/emoji2-emojipicker/samples) app demonstrate basic use cases plus the following additional scenarios:

- The view re-layouted because `emojiGridRows` and `emojiGridColumns` were reseted.
- The recent emoji provider is overridden to sort by frequency.
- Style customization.

**API Changes**

The Emoji Picker library has been updated with the following new APIs:

- The `EmojiPickerView` class, which provides up-to-date emojis in a vertical scrollable view with a clickable horizontal header.
- The ability to set the number of columns and rows in the emoji picker grid via XML attributes `emojiGridColumns` and `emojiGridRows` or the `setEmojiGridColumns()` and `setEmojiGridRows()` methods.
- The ability to set an emoji picked listener via the `setOnEmojiPickedListener()` method. The listener will be notified whenever the user clicks any emoji.
- The ability to provide a recent emoji provider via the `setRecentEmojiProvider()` method. This is an optional function. If the recent emoji provider is not set, a default recent emoji provider will be used by the library. The default behavior is defined as follows:
  - All selected emojis will be saved per-app level in shared preferences.
  - The picker will display at most 3 rows of selected emojis, deduped, in reverse chronological order.
- The `EmojiViewItem` class, which holds the displayed emoji and its emoji variants.
- The `RecentEmojiProvider` interface, which can be implemented to provide a recent emoji list. The `recentEmojiProvider` is responsible for providing emojis in the "Recently Used" category.
- The `RecentEmojiAsyncProvider` interface, which can be implemented to provide a recent emoji list. The `RecentEmojiAsyncProvider` is responsible for providing emojis in the "Recently Used" category. This interface is equivalent to `RecentEmojiProvider` that allows clients to override the `getRecentEmojiListAsync()` method to provide recent emojis.
- The `RecentEmojiProviderAdapter` class, which is an adapter for the `RecentEmojiAsyncProvider` and implements `RecentEmojiProvider`.

### Version 1.4.0-alpha01

March 22, 2023

`androidx.emoji2:emoji2-*:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4094341e51e18526c3891bf26aee09a8429e107..5e7d256f82fbafb6d059ab7b18fddd87c7531553/emoji2)

**Bug Fixes**

- Fix tests, disable flake tests, and clean ups.

## Version 1.3

### Version 1.3.0

March 22, 2023

`androidx.emoji2:emoji2-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4094341e51e18526c3891bf26aee09a8429e107..a31add952e44ab4aa0fac28de27e3d2f8a7a726b/emoji2)

**Important changes since 1.2.0**

- This release allows [Compose Foundation `1.4.0`](https://developer.android.com/jetpack/androidx/releases/compose-foundation#1.4.0) and higher to enable emoji2 integration.
- It also allows features for replacing `EmojiSpans` with custom drawing code, as well as support for emoji exclusions defined on Android.

### Version 1.3.0-rc01

March 8, 2023

`androidx.emoji2:emoji2-*:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..d4094341e51e18526c3891bf26aee09a8429e107/emoji2)

**New Features**

- This version is to support emoji2 compose integration.

**API Changes**

- Replace spans for custom drawing code.
- Querying system exclusions.

**Bug Fixes**

- And fixed a bug where background spans were not correctly applied behind `EmojiSopans`.

### Version 1.3.0-beta03

February 23, 2023

`androidx.emoji2:emoji2-bundled:1.3.0-beta03`, `androidx.emoji2:emoji2-views:1.3.0-beta03`, and `androidx.emoji2:emoji2-views-helper:1.3.0-beta03` are released.

February 22, 2023

`androidx.emoji2:emoji2:1.3.0-beta03` is released. [Version 1.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..87533b4ff06971ed59028936cd9b6da988cd4522/emoji2/emoji2)

**New Features**

- No changes. This release is to prepare for compose integration.

### Version 1.3.0-beta02

February 8, 2023

`androidx.emoji2:emoji2-*:1.3.0-beta02` is released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..7d3ac1ab1206c01fae3ebb500b5b942636070155/emoji2)

**New Features**

- This release is stabilization to support compose integration.

### Version 1.3.0-beta01

January 25, 2023

`androidx.emoji2:emoji2-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/emoji2)

**New Features**

- Querying system exclusions.
- Replacing the spans for custom drawing code.
- And fixed a bug where background spans were not correctly applied behind `EmojiSopans`.
- This release adds APIs necessary to support `EmojiCompat` in Compose. Expect compose support for emoji compat in a near future release.

### Version 1.3.0-alpha01

January 11, 2023

`androidx.emoji2:emoji2-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65a4875fb9d65b2451610b344113b20cc3c900f5..adf1c279a86ab3886e1666c08e2c3efba783367b/emoji2)

**New APIs for low level interactions**

- Querying system exclusions
- Replacing the spans for custom drawing code
- And fixed a bug where background spans were not correctly applied behind `EmojiSopans`.
- This release adds APIs necessary to support `EmojiCompat` in Compose. Expect compose support for emoji compat in a near future release.

**API Changes**

- Added ability to query system exclusions to `TypefaceEmojiRasterizer`. ([I5653e](https://android-review.googlesource.com/#/q/I5653ecf010b5e676376ae08c4c2c20633dea4696))
- Added new API `EmojiCompat.SpanFactory` for replacing default `EmojiSpan` behavior with custom drawing and sizing code. ([Ib69d9](https://android-review.googlesource.com/#/q/Ib69d907370d8d511ccf416c889834db6de763708))
- Added `EmojiCompat` to Compose ([I96f37](https://android-review.googlesource.com/#/q/I96f37bd992fc8cf305e4cb5e3bbe9ea3be19e52b), [b/139326806](https://issuetracker.google.com/issues/139326806))

**Bug Fixes**

- Emoji2 will now correctly draw backgrounds from `BackgroundSpan`. ([Ide6a8](https://android-review.googlesource.com/#/q/Ide6a8542179a2676cefc16dcf3f3d43e6f376de6), [b/230525134](https://issuetracker.google.com/issues/230525134))
- Finalize AppCompat APIs for 1.5.0-beta01 ([I2a43d](https://android-review.googlesource.com/#/q/I2a43d45452aef36c958e780c0678b2f62738b1f1), [b/236866227](https://issuetracker.google.com/issues/236866227))

## Version 1.2

### Version 1.2.0

August 10, 2022

`androidx.emoji2:emoji2-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/26699d311c26986b4c92aed8ec6b79f7006910ee..65a4875fb9d65b2451610b344113b20cc3c900f5/emoji2)

**Important changes since 1.1.0**

This is a bugfix release. No new features or APIs added since 1.1.0.

However, apps using `PrecomputedText` or `TextView.setText(char[])` should
prioritize bumping to this version.

The following bugs were fixed:

- `Emoji2` will add emoji to `PrecomputedText` by discarding previously precomputed text layout. ([I47d06](https://android-review.googlesource.com/c/platform/frameworks/support/+/2025744), [b/211231958](https://issuetracker.google.com/211231958))
- Backport editor crash fix from Android P to `EditText` that is configured to use emoji2. ([Ifd709](https://android-review.googlesource.com/c/platform/frameworks/support/+/2016855), [b/216891011](https://issuetracker.google.com/211231958))
- Fix crash when emoji2 loads font and `TextView.setText(char[])` was used. ([Id511e](https://android-review.googlesource.com/c/platform/frameworks/support/+/2007316), [b/206859724](https://issuetracker.google.com/211231958))

### Version 1.2.0-rc01

July 27, 2022

`androidx.emoji2:emoji2-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8fda1c7005de1555e6ae9b7a1ae5657c3b91eba7..26699d311c26986b4c92aed8ec6b79f7006910ee/emoji2)

- No changes since the last beta version.

### Version 1.2.0-beta01

July 13, 2022

`androidx.emoji2:emoji2-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..8fda1c7005de1555e6ae9b7a1ae5657c3b91eba7/emoji2)

**New Features**

- No changes from the last version (this release is to support the AppCompat release).

### Version 1.2.0-alpha04

April 20, 2022

`androidx.emoji2:emoji2-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/emoji2)

**New Features**

- No changes in this release.

### Version 1.2.0-alpha03

April 6, 2022

`androidx.emoji2:emoji2-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/emoji2)

**New Features**

- No changes from the last version (this release is to support the appcompat release).

### Version 1.2.0-alpha02

March 23, 2022

`androidx.emoji2:emoji2-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/emoji2)

**Bug Fixes**

- Emoji2 will add emoji to `PrecomputedText` by discarding previously precomputed text layout. ([I47d06](https://android-review.googlesource.com/#/q/I47d066f5cd1f61e0d6338ecc133879fe5bda7e27), [b/211231958](https://issuetracker.google.com/issues/211231958))
- Backport editor crash fix from Android P to EditText that is configured to use emoji2. ([Ifd709](https://android-review.googlesource.com/#/q/Ifd70914816fdb732aae34690666d790a6fc9783a), [b/216891011](https://issuetracker.google.com/issues/216891011))
- Fix crash when emoji2 loads font and `TextView.setText(char[])` was used. ([Id511e](https://android-review.googlesource.com/#/q/Id511e36ce9a9077309855082de88f00c26024c9d), [b/206859724](https://issuetracker.google.com/issues/206859724))

### Version 1.2.0-alpha01

February 23, 2022

`androidx.emoji2:emoji2-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/32e140628dfa9e3cad28b03338027286613fee49..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/emoji2)

No changes since 1.1.0.

## 1.1

### Version 1.1.0

February 23, 2022

`androidx.emoji2:emoji2-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/32e140628dfa9e3cad28b03338027286613fee49..bd4879eba3c19337d1a20342d4564a843dd3e56a/emoji2)

**Important changes since 1.0.0**

- emoji2-bundled contains emoji 14 font
- New `getEmojiMatch` API returns accurate information for keyboards to decide how an emoji will display in the presence of an emojicompat font that's behind the system font
- Bugfix for `NumberKeyListener` that makes digit input correctly filter characters.

### Version 1.1.0-rc01

February 9, 2022

`androidx.emoji2:emoji2-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..32e140628dfa9e3cad28b03338027286613fee49/emoji2)

**New Features**

No changes from beta.

New features compared to emoji2 1.0.0:

- `emoji2-bundled` contains emoji 14 font
- New `getEmojiMatch` API returns accurate information for keyboards to decide how an emoji will display in the presence of an emojicompat font that's behind the system font
- Bugfix for `NumberKeyListener` that makes digit input correctly filter characters

### Version 1.1.0-beta01

January 26, 2022

`androidx.emoji2:emoji2-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..9dceceb54300ed028a7e8fc7a3454f270337ffde/emoji2)

**Bug Fixes**

- androidx-emoji2 beta01 release. No changes from alpha01 ([Ic61d9](https://android-review.googlesource.com/#/q/Ic61d9016bcb136726ac77d3c3013d51b2849610e))

### Version 1.1.0-alpha01

December 15, 2021

`androidx.emoji2:emoji2-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a115796b2e8dbaedf17e2f7ad2eda5c58698b04..301586664b5aad60548f21866cad502d524dbf9f/emoji2)

**New Features**

- `emoji2-bundled` contains emoji 14 font
- New `getEmojiMatch` API returns accurate information for keyboards to decide how an emoji will display in the presence of an emojicompat font that's behind the system font
- Bugfix for `NumberKeyListener` that makes digit input correctly filter characters

**API Changes**

- Add new API `getEmojiMatch` to allow keyboards to more accurately lookup emoji match behavior in emojicompat.
- Deprecate `hasEmojiGlyph`, as its boolean return value is inaccurate when testing against a font that is older than the platform emoji font. Replace with `getEmojiMatch`. ([Ie693d](https://android-review.googlesource.com/#/q/Ie693d9d045954f86d37cae623a72f75aeeea6a9d))

**Bug Fixes**

- Emoji2 will not wrap instances of `NumberKeyListener`, allowing the locale to be configured by `TextView`.
- Appcompat will not wrap instances of `NumberKeyListener` passed to `setKeyListener`, allowing `TextView` to correctly configure the locale on `NumberKeyListeners`. ([Ibf113](https://android-review.googlesource.com/#/q/Ibf113081112d05c75937eec5bc87904ebf450b26), [b/207119921](https://issuetracker.google.com/issues/207119921))

## 1.0

### Version 1.0.1

December 15, 2021

`androidx.emoji2:emoji2-*:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7a115796b2e8dbaedf17e2f7ad2eda5c58698b04..0f6948d84f87951a7b3486d1ab516b9edbfd8f16/emoji2)

**Bug Fixes**

- `Emoji2` will not wrap instances of `NumberKeyListener`, allowing the locale to be configured by `TextView`.
- Appcompat will not wrap instances of `NumberKeyListener` passed to `setKeyListener`, allowing `TextView` to correctly configure the locale on `NumberKeyListeners`. ([Ibf113](https://android-review.googlesource.com/#/q/Ibf113081112d05c75937eec5bc87904ebf450b26), [b/207119921](https://issuetracker.google.com/issues/207119921))

### Version 1.0.0

November 17, 2021

`androidx.emoji2:emoji2-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/23b75a63032c5a1579ccc6a2dd4f60c1153452dd..7a115796b2e8dbaedf17e2f7ad2eda5c58698b04/emoji2)

**Major features of 1.0.0**

androidx.emoji2 replaces androidx.emoji with additional capabilities:

- APK size reduction vs androidx.emoji
- Automatic configuration
- Added as a dependency to appcompat 1.4

For more information about androidx.emoji2 see [Supporting Modern Emoji](https://developer.android.com/guide/topics/ui/look-and-feel/emoji2) and our Android Dev Summit talk [Displaying ALL the emojis in your app Android Dev](https://www.youtube.com/watch?v=QVj2tQm8r58).

### Version 1.0.0-rc01

October 27, 2021

`androidx.emoji2:emoji2-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..23b75a63032c5a1579ccc6a2dd4f60c1153452dd/emoji2)

- No changes since beta02.

### Emoji2 Version 1.0.0-beta01

September 15, 2021

`androidx.emoji2:emoji2-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/emoji2)

**API Changes**

- Added `setLoadingExecutor` to `FontRequestEmojiCompatConfig`,
  which replaces the previous API of `setHandler`. This API allows apps to
  configure `FontRequestEmojiCompatConfig` to use any background executor.

  This change is a breaking change from `androidx.emoji:emoji`, so
  `setHandler` is retained as a no-op Deprecated API to aid in migration. ([I6cd48](https://android-review.googlesource.com/#/q/I6cd48e8f8ad6d8d51c62bd8f2d02c04c77e9db81))
- EmojiCompat correctly sets `EditorInfo.extras` on Android 11

  - Custom widgets that use IME not subclassing EditText may call `EmojiCompat.updateEditorInfo` to inform IME that they support EmojiCompat processing. ([I1ea9b](https://android-review.googlesource.com/#/q/I1ea9bdd579e64139d98bc1298ad2d9c5ade65045))

**Bug Fixes**

- Fix `DefaultEmojiCompatConfig` to correctly lookup emoji font provider on API 19 and 28. This fixes a bug introduced in emoji2 1.0.0-alpha01. ([Ib33d8](https://android-review.googlesource.com/#/q/Ib33d84de2a030f6e57e3d5382a088255a202692a), [b/197906329](https://issuetracker.google.com/issues/197906329))

### Version 1.0.0-alpha03

June 30, 2021

`androidx.emoji2:emoji2-*:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/emoji2)

**New Features**

This release is a bugfix and stabilization release.

1. EmojiEditTextHelper now allows `null` to be passed as a KeyListener. This allows the platform behavior of allowing nulls to be applied to emoji supporting EditText implementations.
2. When using EmojiCompatInitializer initial startup delay is improved to trigger after the first Activity resumes. This allows app startup to happen uncontended, and avoids loading the font for app starts that never show a UI. After a short delay, EmojiCompat will create a thread to load the emoji font.

- A new dependency on `androidx.lifecycle:lifecycle-process` from `androidx.emoji2:emoji2` is added to implement the delay. This will have negligible APK size impact for apps that already include lifecycle (such as apps with appcompat).

**API Changes**

- Allow null KeyListener in AppCompatEditText. This reverses the non-null annotation that was added to AppCompatEditText in 1.4.0-alpha01 and restores the previous behavior when passed null. ([I21482](https://android-review.googlesource.com/#/q/I214824131c0206349b73471a8c22be38bf5dd0d8), [b/189559345](https://issuetracker.google.com/issues/189559345))

**Bug Fixes**

- Change EmojiCompatInitializer to delay font loading until 500ms after the first `Activity.onResume`. This allows an activity to perform `Application.onCreate` and `Activity.onCreate` uncontended, while still ensuring that the emoji font is loaded shortly after app startup. ([I4bff7](https://android-review.googlesource.com/#/q/I4bff7a1b8ae23529be059f5154a8de91ba939861))

### Version 1.0.0-alpha02

June 2, 2021

`androidx.emoji2:emoji2:1.0.0-alpha02`, `androidx.emoji2:emoji2-views:1.0.0-alpha02`, and `androidx.emoji2:emoji2-views-helper:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..86ff5b4bb956431ec884586ce0aea0127e189ec4/emoji2)

**API Changes**

- Renamed package in `emoji2-views-helper` to `androidx.emoji2.viewsintegration`. This is a breaking change for AppCompat `1.4.0-alpha01`, and apps must ensure AppCompat dependency is updated to use the new emoji2 version. ([Ie8397](https://android-review.googlesource.com/#/q/Ie83972affa2281616923620e1642964eead49b4e))

### Version 1.0.0-alpha01

May 18, 2021

`androidx.emoji2:emoji2:1.0.0-alpha01`, `androidx.emoji2:emoji2-views:1.0.0-alpha01`, and `androidx.emoji2:emoji2-views-helper:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61/emoji2)

**Features in this initial release**

Integrating emojicompat is recommended for all apps to support modern emoji from API19. All user generated content in your app contains 🎉.

EmojiCompat has moved from the `androidx.emoji` artifacts to the new `androidx.emoji2`, now in alpha01. The new artifacts replace the previous version.

`emoji2` is added as a dependency to AppCompat starting in [AppCompat `1.4.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.4.0-alpha01) and is enabled by default for AppCompat views.

The `emoji2` artifact introduces a new automatic configuration using the `androidx.startup` library. You no longer need to write any 👨🏽‍💻 code to display 🐻‍❄️.

**Changes in emoji2 from emoji**

- Added new automatic configuration `EmojiCompatInitializer` using `androidx.startup`.
- Added new default configuration that uses service location to find a downloadable fonts provider in `DefaultEmojiCompatConfiguration`.
- Classes moved from `androidx.emoji` package to `androidx.emoji2`.
- Split `EmojiTextView` and related views to a separate artifact `emoji2-views`. This should only be used if your app doesn't use appcompat.
- Extracted helpers for integrating emojicompat into custom views into a separate artifact `emoji2-views-helper`.
- Added nullability annotations.
- Helpers in `emoji2-views-helper` may now be used even when `EmojiCompat` is not initialized (previously they threw an exception).

**What dependency should you add?**

- Apps with AppCompat should upgrade to appcompat version [AppCompat `1.4.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.4.0-alpha01) or higher.
- Apps without AppCompat using `TextView`/`EditText` from platform should use `EmojiTextView` and related classes from `emoji2-views`.

**How to support in custom views**

- Apps with AppCompat should extend `AppCompatTextView`, `AppCompatButton`, etc. instead of platform `TextView`, etc.
- Apps without AppCompat should add `androidx.emoji2:emoji2-views-helper` dependency and use helpers to integrate with custom `TextView` or `EditText` subclasses.

**Configuring automatic initialization**

- Apps can disable the automatic initialization by adding this to the manifest:

       <provider
           android:name="androidx.startup.InitializationProvider"
           android:authorities="${applicationId}.androidx-startup"
           android:exported="false"
           tools:node="merge">
           <meta-data android:name="androidx.emoji2.text.EmojiCompatInitializer"
                     tools:node="remove" />
       </provider>

- This disables automatic configuration, and you can then pass a custom configuration to `EmojiCompat.init`. The default configuration for the system may be retrieved `DefaultEmojiCompatConfig.create(context)` for further configuration before passing to `EmojiCompat.init`.