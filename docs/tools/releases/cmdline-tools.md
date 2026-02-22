---
title: https://developer.android.com/tools/releases/cmdline-tools
url: https://developer.android.com/tools/releases/cmdline-tools
source: md.txt
---

# Android SDK Command-Line Tools release notes

The Android SDK Command-Line Tools package contains various tools for building and debugging Android apps. It is released concurrently with Android Studio and is installed in the<var translate="no">android_sdk</var>`/cmdline-tools/`<var translate="no">version</var>`/bin/`directory.

For a complete description of the tools included in this package, see[Command line tools](https://developer.android.com/studio/command-line#tools-sdk)in the user guide.

To install the latest version, check the[SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager)for updates. Alternatively, you can[download the latest stable version](https://developer.android.com/studio#command-tools)directly.

In Android Studio, the latest version available in the SDK Manager dialog depends on which update channel you've selected. To use a preview version of this package,[set your update channel](https://developer.android.com/studio/preview/install-preview#change_your_update_channel)to either Beta or Canary.

To update using`sdkmanager`from the command line, use either of the following:  

    // Beta channel
    sdkmanager 'cmdline-tools;latest' --channel=1

    // Canary channel
    sdkmanager 'cmdline-tools;latest' --channel=3

| **Note:** The Android SDK Command-Line Tools package replaces the deprecated[SDK Tools](https://developer.android.com/studio/releases/sdk-tools)package. For information about the deprecated SDK Tools package, see the[Android SDK Tools release notes](https://developer.android.com/studio/releases/sdk-tools).

## Android SDK Command-Line Tools 5.0 (canary)

Updated in December 2020.

## Android SDK Command-Line Tools 4.0 (beta)

Updated in December 2020. Adds the[`retrace`](https://developer.android.com/studio/command-line/retrace)tool.

## Android SDK Command-Line Tools 3.0

Released in July 2020.

## Android SDK Command-Line Tools 2.1

Released in June 2020.

## Android SDK Command-Line Tools 2.0

Released in May 2020.

## Android SDK Command-Line Tools 1.0

Released in February 2020.