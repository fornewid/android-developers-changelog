---
title: https://developer.android.com/jetpack/androidx/releases/palette
url: https://developer.android.com/jetpack/androidx/releases/palette
source: md.txt
---

# Palette

[Code Sample](https://github.com/android/plaid) Extract representative color palettes from images.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 01, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/palette#1.0.0) | - | - | [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/palette#1.1.0-alpha01) |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460399+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460399&template=1422702)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.1

### Version 1.1.0-alpha01

July 01, 2026

`androidx.palette:palette:1.1.0-alpha01` and `androidx.palette:palette-ktx:1.1.0-alpha01` are released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3392a424178238fa2c15db77b28bb528a3dbf0ea/palette).

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage: -Xjspecify-annotations=strict, -Xtype-enhancement-improvements-strict-mode ([Ideef8](https://android-review.googlesource.com/#/q/Ideef8b4d207f18f08546de9d4c85c93ab7356b64), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Merged public and experimental API files for n- thru t-paths ([I103c7](https://android-review.googlesource.com/#/q/I103c708874e07493c33c4ee76472978faa62ad31), [b/278769092](https://issuetracker.google.com/issues/278769092))

**External Contribution**

- Merge palette-ktx into the palette library. All Kotlin extensions are now part of the main palette artifact. palette-ktx is now an empty artifact for compatibility. ([I3f1df](https://android-review.googlesource.com/#/q/I3f1df19145c7bfd91704c730d2d24aa5a6796359))

There are no release notes for this artifact.