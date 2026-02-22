---
title: https://developer.android.com/jetpack/androidx/releases/emoji
url: https://developer.android.com/jetpack/androidx/releases/emoji
source: md.txt
---

# Emoji

# Emoji

[User Guide](https://developer.android.com/guide/topics/ui/look-and-feel/emoji-compat)[Code Sample](https://github.com/android/user-interface-samples)  
API Reference  
[androidx.emoji.bundled](https://developer.android.com/reference/kotlin/androidx/emoji/bundled/package-summary)  
[androidx.emoji.text](https://developer.android.com/reference/kotlin/androidx/emoji/text/package-summary)  
[androidx.emoji.widget](https://developer.android.com/reference/kotlin/androidx/emoji/widget/package-summary)  
Display emoji in current and older devices.  

|   Latest Update   |                                Stable Release                                | Release Candidate |                                        Beta Release                                        | Alpha Release |
|-------------------|------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------|---------------|
| November 19, 2025 | [1.1.0](https://developer.android.com/jetpack/androidx/releases/emoji#1.1.0) | -                 | [1.2.0-beta01](https://developer.android.com/jetpack/androidx/releases/emoji#1.2.0-beta01) | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460938+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460938&template=1422574)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Emoji Version 1.2.0

### Version 1.2.0-beta01

November 19, 2025

`androidx.emoji:emoji:1.2.0-beta01`,`androidx.emoji:emoji-appcompat:1.2.0-beta01`, and`androidx.emoji:emoji-bundled:1.2.0-beta01`are released. Version 1.2.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c432e3c08f7a59f114989dbcefaa1e18fb555df3..e5dc00768ba5e06b850928bd526e1a0a0337c8a2/emoji).

**API Changes**

- `EmojiMetadata`typeface specified as non null. ([Ic727f](https://android-review.googlesource.com/#/q/Ic727f852ab6a1ca1e799eea8b1e2919473613ac5),[b/236341259](https://issuetracker.google.com/issues/236341259))
- `EmojiCompat`correctly sets`EditorInfo.extras`on Android R ([I1ea9b](https://android-review.googlesource.com/#/q/I1ea9bdd579e64139d98bc1298ad2d9c5ade65045),[b/196452690](https://issuetracker.google.com/issues/196452690))
- Custom widgets that use IME not subclassing`EditText`may call`EmojiCompat.updateEditorInfo`to inform IME that they support`EmojiCompat`processing. ([I1ea9b](https://android-review.googlesource.com/#/q/I1ea9bdd579e64139d98bc1298ad2d9c5ade65045),[b/196452690](https://issuetracker.google.com/issues/196452690))

**Bug Fixes**

- Moving the default`minSdk`from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df),[b/380448311](https://issuetracker.google.com/issues/380448311),[b/435705964](https://issuetracker.google.com/issues/435705964),[b/435705223](https://issuetracker.google.com/issues/435705223))
- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage:`-Xjspecify-annotations=strict, -Xtype-enhancement-improvements-strict-mode`([Ibb74c](https://android-review.googlesource.com/#/q/Ibb74cbbb710f914213543cc1c6a8273e0e19c4e4),[b/326456246](https://issuetracker.google.com/issues/326456246))
- `EmojiCompat`init callbacks will now use the handler from each view, respecting views not on the main thread. ([Iccbcf](https://android-review.googlesource.com/#/q/Iccbcfb16840662f348cb632cfba9b263fb7ad963),[b/278897602](https://issuetracker.google.com/issues/278897602))

### Version 1.2.0-alpha03

January 27, 2021

`androidx.emoji:emoji:1.2.0-alpha03`,`androidx.emoji:emoji-appcompat:1.2.0-alpha03`, and`androidx.emoji:emoji-bundled:1.2.0-alpha03`are released.[Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c432e3c08f7a59f114989dbcefaa1e18fb555df3/emoji)

**New Features**

- [Emoji v13.1](https://www.unicode.org/emoji/charts-13.1/emoji-released.html)emoji are added to bundled configuration.

**API Changes**

- Added new API`EmojiCompat.Config#setGlyphChecker`that enables developers to provide custom emoji glyph check behavior. ([Ibc95e](https://android-review.googlesource.com/#/q/Ibc95e158765d392cb8726e53b0f8cac7961f0373),[b/170587912](https://issuetracker.google.com/issues/170587912))

### Version 1.2.0-alpha01

August 19, 2020

`androidx.emoji:emoji:1.2.0-alpha01`,`androidx.emoji:emoji-appcompat:1.2.0-alpha01`, and`androidx.emoji:emoji-bundled:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7df41e99110bc88b2978236027e7643f87c9c03d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/emoji)

**New Features**

- [Emoji v13.0](https://unicode.org/emoji/charts-13.0/emoji-released.html)emoji are added to bundled configuration.

## 1.1.0

### Version 1.1.0

June 24, 2020

`androidx.emoji:emoji:1.1.0`,`androidx.emoji:emoji-appcompat:1.1.0`, and`androidx.emoji:emoji-bundled:1.1.0`are released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b878bf9d7ec27f04fbda7bac038b5e8863b467c4..7df41e99110bc88b2978236027e7643f87c9c03d/emoji)

**Major changes since 1.0.0**

- [Emoji 12](https://www.unicode.org/emoji/charts-12.0/emoji-released.html)and[Emoji 12.1](https://www.unicode.org/emoji/charts-12.1/emoji-released.html)have been added to the bundled EmojiCompat font.

### Version 1.1.0-rc01

April 29, 2020

`androidx.emoji:emoji:1.1.0-rc01`,`androidx.emoji:emoji-appcompat:1.1.0-rc01`, and`androidx.emoji:emoji-bundled:1.1.0-rc01`are released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..b878bf9d7ec27f04fbda7bac038b5e8863b467c4/emoji)

### Version 1.1.0-beta01

April 1, 2020

`androidx.emoji:emoji:1.1.0-beta01`,`androidx.emoji:emoji-appcompat:1.1.0-beta01`, and`androidx.emoji:emoji-bundled:1.1.0-beta01`are released with no changes since`1.1.0-alpha01`.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9cee7f8bcabb66e4b85ebc003b507c4582f9df97..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/emoji)

### Version 1.1.0-alpha01

February 5, 2020

`androidx.emoji:emoji:1.1.0-alpha01`,`androidx.emoji:emoji-appcompat:1.1.0-alpha01`, and`androidx.emoji:emoji-bundled:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits in source](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..15eb802358e0836378e4daba5db3d88cf09b7f03/emoji)and[these commits for Emoji 12 and 12.1](https://android.googlesource.com/platform/external/noto-fonts/+log/f0814148020221620209c31de62a5a207ad7770c..fbf24e9a9b0125391b18f359998614529d07ca6b/emoji-compat/).

**New features**

- [Emoji 12](https://www.unicode.org/emoji/charts-12.0/emoji-released.html)and[Emoji 12.1](https://www.unicode.org/emoji/charts-12.1/emoji-released.html)are added to the bundled EmojiCompat font.