---
title: Update the IDE and SDK tools  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/intro/update
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Update the IDE and SDK tools Stay organized with collections Save and categorize content based on your preferences.



Once you install Android Studio, you can keep the Android Studio IDE
and Android SDK tools up to date with automatic updates
and the Android SDK Manager.

## Update your IDE using JetBrains Toolbox

If you installed Android Studio using
[JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/), then
Toolbox is responsible for handling updates to Android Studio. Toolbox lets you install canary,
RC, and stable versions of Android Studio in parallel. It also lets you roll back to earlier
versions of each, if required. When an update is available it displays in Toolbox, as
shown in figure 1.

![Jetbrains Toolbox showing updcates available](/static/studio/images/jetbrains-toolbox_2x.png)

**Figure 1.** Jetbrains Toolbox showing available updates.

## Update your IDE and change channels

If you installed Android Studio manually, Android Studio notifies you with a small bubble
dialog when an update is available for the IDE. To manually check for updates,
click **File** >**Settings** >**Appearance & Behavior** >
**System Settings** > **Updates**
(on macOS, **Android Studio** > **Check for Updates**). See figure 2.

Updates for Android Studio are available from the following
release channels:

* **Canary channel:** these bleeding-edge
  releases are updated roughly weekly and are available for download on the
  [Preview release](/studio/preview) page.

  In addition to receiving canary versions of Android Studio, you also receive preview
  versions of other SDK tools, including the Android Emulator.

  Although these builds are subject to more
  bugs, they do get tested and are available so you can try new
  features and provide feedback.

  **Note:** This channel is not recommended for
  production development.
* **RC channel:** these are release candidates based on stable canary builds
  and are available for download on the [Preview release](/studio/preview) page.
  They are released to get feedback before being integrated into the stable channel.
* **Stable channel:** the official, stable release of
  [Android Studio](/studio).

If you'd like to try one of the preview channels (canary or RC)
while still using the stable build for your production projects, you
can [install them side by side](/studio/preview/install-preview).

![](/static/studio/images/preferences-updates_2x.png)