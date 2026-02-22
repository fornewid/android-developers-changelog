---
title: https://developer.android.com/studio/emulator_archive
url: https://developer.android.com/studio/emulator_archive
source: md.txt
---

This page provides an archive of Emulator releases. Please review the
[license file](https://cs.android.com/android/platform/superproject/+/master:prebuilts/android-emulator/NOTICE)
in the emulator package for licensing information.

For the best experience, please review the [Emulator system requirements](https://developer.android.com/studio/run/emulator#requirements).

## How to manually install a select version of emulator

To manually install a select version of emulator on Studio, you need to paste the desired
emulator package contents into your SDK installation directory, and change the emulator version
specified in the `package.xml` file. Specifically, follow these steps:

1. Locate your SDK installation directory. The default location of this directory varies by platform:
   - On Windows, it's the `%LocalAppData%\Android\Sdk` directory. This normally expands to `C:\Users\<username>\AppData\Local\Android\Sdk`, although it might vary based on your system.
   - On macOS, it's the `$HOME/Library/Android/sdk` directory.
   - On Linux, it's the `$HOME/Android/Sdk` directory.

   You can check where your SDK installation directory is by opening Studio and clicking
   **Android Studio \> Preferences \> Appearances \& Behavior \> System Settings \>
   Android SDK** . The **Android SDK Location** file path is your SDK installation
   directory location.

   If you're using macOS and browsing using Finder, the `Library` folder might not be
   visible by default. To navigate there, open Finder and click **Go \> Go to Folder**
   and search for "Library."
2. Rename the existing `emulator` directory in the SDK installation directory, because you'll unzip the newly downloaded `emulator` directory here in the next step. For example, call it `emulator_original`.
3. Unzip the emulator zip file you downloaded. Move the contents into the SDK installation directory.
4. On macOS: After unzipping the emulator zip file, clear the quarantine attribute on the
   emulator package by running:

   `
   xattr -dr com.apple.quarantine emulator/
   `

   This should reduce messages about whether the package should be checked or blocked.
5. Paste the `package.xml` file from the `emulator_original` directory into the new `emulator` directory.
6. Change the emulator version specified in the `package.xml` file to the version you
   have downloaded and want to use. To do this, scroll to the bottom of the `package.xml`
   file and find the text that looks like:

   `
   <revision><major>31</major><minor>1</minor><micro>4</micro></revision>
   `

   This is where you should specify the emulator version you downloaded and want to install.

<iframe src="https://android.devsite.google/frame/studio/emulator_archive_dfd3f4671f6af8342f32dcc5fdf8a3f87abcd3f9f3e0b608e7e8820171264c42.frame" class="framebox inherit-locale scroll" allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>