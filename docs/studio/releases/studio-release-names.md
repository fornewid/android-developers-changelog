---
title: https://developer.android.com/studio/releases/studio-release-names
url: https://developer.android.com/studio/releases/studio-release-names
source: md.txt
---

# Android Studio release names

Each Android Studio release goes through the following stages of development:

- [**Canary**](https://developer.android.com/studio/preview)- Leading edge features under active development, lightly tested. While you can use Canary builds for development, be aware that features might be added or changed.
- [**Release Candidate (RC)**](https://developer.android.com/studio/preview)- The next version of Android Studio that's almost ready for stable release. The feature set for the next version has been stabilized.
- [**Stable**](https://developer.android.com/studio)- The final version of Android Studio.
- [**Patch n**](https://developer.android.com/studio)- Updates to a version of Android Studio, typically for bug fixes. Might contain new minor features.

There are two types of Android Studio releases:

- **Merge**- Contains the latest updates from the corresponding IntelliJ version. Merge releases might contain limited new Android-Studio-specific features, minor improvements, and bug fixes.

  Merge releases are named`<animal> <IDEA year.major>.1 [stage]`

  For example,`Meerkat 2024.3.1 RC 2`.
- **Feature Drop**- Contains new Android Studio features and bug fixes.

  Feature drops are named`<animal> Feature Drop <IDEA year.major>.2 [stage]`

  For example,`Ladybug Feature Drop 2024.2.2 Patch 2`.

These release names include:

- `<animal>`- the code name for the Android Studio release. These names alphabetically indicate which releases are newer.

- `<IDEA year.major>`- which version of IntelliJ IDEA is the base for this release of Android Studio

- `[stage]`- (optional) indicates patches and pre-release versions. If omitted, this a stable, non-patched release of Android Studio.

For more information on the Android Studio release strategy, See[More frequent, focused updates for Android Studio](https://android-developers.googleblog.com/2024/05/more-frequent-focused-updates-for-android-studio.html).