---
title: https://developer.android.com/training/app-links/tools
url: https://developer.android.com/training/app-links/tools
source: md.txt
---

You can use these tools to simplify and manage your App Links.

## Android Studio App Links Assistant

The Android Studio App Links Assistant is a plugin within Android Studio that
helps with management, creation and validation of App Links, it includes:

- An overview of all the existing deep links in the app and their validation statuses.
- Detailed view of the misconfiguration for each link and guidance on how to fix the issues.
- Automatically fix the configuration issues in their existing deeplinks.
- Automatic generation of the assetlinks.json file (doesn't support dynamic rules yet)
- Validate the web configuration for each deep link (uses your assetlinks.json file, hosted on your website or domain).
- Wizard to create new App Links.

### How to access the tool?

In Android Studio, click **App Links Assistant** under **Tools**

![Android studio screenshot](https://developer.android.com/static/training/app-links/images/tools_2.png)

## Play Developer Console Deep Link Page

You can also manage and verify deep links through the [Play
Console](https://play.google.com/console). Once you upload your app, the Console provides a
dedicated dashboard (under Grow \> Deep links) to help you create and verify your
App Links:

- Get an overview of existing setup + guidance on how to fix issues
- Surface missing W2AC URLs that should be implemented as DLs
- Push deep links app fixes live without publishing a new app release

![Play console screenshot](https://developer.android.com/static/training/app-links/images/tools_1.png)

It also displays an overview of deep links and configuration errors, with
information on how to fix them.

![Play console gif](https://developer.android.com/static/training/app-links/images/tools_3.gif)

For more information, see [Verify and maintain deep links](https://support.google.com/googleplay/android-developer/answer/12463044).

### How to access the tool?

Visit here: <https://play.google.com/console/about/deeplinks/>

## Flutter Deep Link Validator

The Flutter Deeplinking Validator empowers Flutter developers to:

- Verify the setup of deep links for their Android apps.
- Provides a detailed view of misconfigured deep links and instructions on how to fix them
- Provides code snippets to fix issues in the app file
- Automatically generates assetlinks.json file to fix any issues

For more information, see [Validate deep links](https://docs.flutter.dev/tools/devtools/deep-links).