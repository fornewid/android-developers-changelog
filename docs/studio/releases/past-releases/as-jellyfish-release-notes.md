---
title: https://developer.android.com/studio/releases/past-releases/as-jellyfish-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-jellyfish-release-notes
source: md.txt
---

The following are new features in Android Studio Iguana.

## Patch releases

<br />

The following is a list of the patch releases in Android Studio Jellyfish
and Android Gradle plugin 8.4.

<br />

<br />

### Android Studio Jellyfish \| 2023.3.1 Patch 2 and AGP 8.4.2 (June 2024)

<br />

<br />

| **Important:** This update fixes a critical vulnerability in the GitHub plugin that exists in Android Studio Iguana \| 2023.2.1 and higher.

<br />

<br />

**Important security update:** A
[security vulnerability](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37051)
in the
[GitHub plugin](https://plugins.jetbrains.com/plugin/13115-github)
available in Android Studio Iguana \| 2023.2.1 and higher could expose access
tokens to unauthorized parties.

<br />

<br />

**The fix:** Jetbrains has
[resolved the issue in IntelliJ platform products](https://blog.jetbrains.com/security/2024/06/updates-for-security-issue-affecting-intellij-based-ides-2023-1-and-github-plugin/),
and the fix is now available in
[Android Studio Jellyfish \| 2023.3.1 Patch 2 (2023.3.1.20)](https://developer.android.com/studio).

<br />

<br />

If you already have an Android Studio build on the
[stable channel](https://developer.android.com/studio/intro/update#channels), you can
get the update by clicking **Help \> Check for Updates** (or **Android
Studio \> Check for Updates** on macOS). Otherwise,
[download the latest stable build](https://developer.android.com/studio).

<br />

Furthermore, if you've actively used GitHub pull request functionality in
the IDE, we strongly advise that you revoke any GitHub tokens being used by
the plugin. Given that the plugin can use OAuth integration or personal
access tokens (PATs), please check both and revoke as necessary:

<br />

<br />

- To revoke access for OAuth integration, go to **[Applications](https://github.com/settings/applications)
  \> Authorized OAuth Apps** and revoke access for the **JetBrains IDE Integration** token.
- To revoke access for PATs, go to [Personal access tokens](https://github.com/settings/tokens) and delete the token issued for the GitHub plugin. The default token name is **IntelliJ IDEA GitHub integration plugin**, but you might be using a custom name.

<br />

<br />

After revoking access for the token(s), you need to set up the plugin again
get all the plugin features, including Git operations, to work again.

<br />

<br />

We apologize for any inconvenience and urge all users to update immediately
to safeguard their code and data.

<br />

<br />

This minor update also includes
[these bug fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2023.3.1#android-studio-jellyfish-|-2023.3.1-patch-2).

<br />

<br />

### Android Studio Jellyfish \| 2023.3.1 Patch 1 and AGP 8.4.1 (May 2024)

<br />

<br />

This minor update includes
[these bug fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2023.3.1#android-studio-jellyfish-|-2023.3.1-patch-1).

<br />

## Introducing Gemini in Android Studio

Gemini in Android Studio is your coding companion for Android development. It's
an AI-powered conversational experience in Android Studio that helps you be more
productive by answering Android development queries. To learn more, see
[Meet Gemini in Android Studio](https://developer.android.com/studio/preview/gemini).

## New sign-in flow

When you sign in to Android Studio with your Developer account, you benefit
from Google developer services---such as viewing Firebase Crashlytics and Android
Vitals reports in
[App Quality Insights](https://developer.android.com/studio/debug/app-quality-insights),
accessing real remote devices with
[Device Streaming in Android Studio](https://developer.android.com/studio/preview/android-device-streaming),
and writing higher-quality code with
[Gemini in Android Studio](https://developer.android.com/studio/preview/gemini)---directly from the IDE.

Android Studio Jellyfish makes it easier to add and manage accounts, and provide
the IDE with only the permissions required for each feature. To get started do
one of the following:

- Navigate to one of the features mentioned previously and follow the prompts to sign in and provide necessary permissions
- If you're already signed in, you can manage your accounts and permissions by navigating to **File** (**Android Studio** on macOS) \> **Settings** \> **Tools** \> **Google Accounts**.

## Access real devices with Device Streaming in Android Studio

Device Streaming in Android Studio lets you securely connect to remote physical
Android devices hosted in Google's secure data centers. Powered by Firebase,
it's the fastest and easiest way to test your app against real devices,
including the Google Pixel 8 Pro, Pixel Fold, select Samsung devices, and more.
![Animation of using Device Streaming in Android Studio.](https://developer.android.com/static/studio/releases/assistant/2023.3.1/device-streaming.gif)

After connecting to a device, you can deploy your app, view the display,
interact with the device (including rotating or unfolding the device), and
anything else you might do with a device over a direct ADB over SSL
connection---all without leaving Android Studio. When you're done using the
device, Google wipes all your data and factory resets the device before making
it available to another developer.

During the current beta period, **you can use device streaming at no cost** with
Firebase projects on either a Spark or Blaze plan. To get started sign into your
Developer account from Android Studio and select a Firebase project. If you
don't already have a Firebase project, it's easy to create one. To learn more,
go to
[Device Streaming in Android Studio](https://developer.android.com/studio/run/android-device-streaming).

## App Quality Insights support for ANRs, custom data, and multi-events

Dive deeper into [App Quality Insights (AQI)](https://developer.android.com/studio/debug/app-quality-insights)
crash reports in Android Studio Jellyfish with support for ANR
reports, custom data, and multi-events:

- **Iterate through events:** Now explore multiple events within a Crashlytics report in reverse chronological order, revealing patterns for faster debugging.
- **Explore custom data:** View custom key/values and logs for each crash report (find them in the Keys and Logs tabs after selecting a report).
- **Analyze ANRs:** Access and investigate ANRs directly within both the Android Vitals and Crashlytics tabs.

![Multi-events, ANRs, and custom data in App Quality Insights.](https://developer.android.com/static/studio/images/releases/aqi-jellyfish.png)

## Embedded Layout Inspector

The Layout Inspector is now embedded by default in the **Running Devices** tool
window. This integration saves screen real-estate, centralizes your workflow in
a single tool window, and delivers significant performance gains---with a 50%
improvement in rendering speeds. You can effortlessly toggle between deeply
inspecting and interacting with your app, and use snapshots for 3D
visualizations of your UI. Discover the full range of features at
[Debug your layout with Layout Inspector](https://developer.android.com/studio/debug/layout-inspector).

## App Links Assistant supports web associations file validation

The [App Links Assistant](https://developer.android.com/studio/write/app-link-indexing) now supports
validation of the
[Digital Asset Links JSON file](https://developer.android.com/training/app-links/verify-android-applinks#web-assoc)
that should be published on your website.

This feature extends the existing validation capabilities for the intent filters
that you declare in the app's manifest file. For each domain that's declared in
the manifest file, the Assistant parses the file on your website, performs seven
validation checks, and provides a detailed explanation on how to fix any errors.

To get started:

1. In Android Studio click **Tools \> App Links Assistant**.
2. Double-click **Links** to get a detailed view of the checks the Assistant performed and understand how to fix the misconfigurations.

Ensure a seamless user experience by validating that your JSON file is correctly
formatted for upload to your domain.

## Baseline Profile installation

Android Studio Jellyfish automatically compiles
[Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview) after
installation on device for projects that use AGP 8.4 or higher. This covers
Baseline Profiles that have been generated through a
[Baseline Profile Generator](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile)
module or from libraries like Compose. The automatic installation lets you
experience the performance benefits of Baseline Profiles when installing your
release app locally, and when using low-overhead profiling.

## New colorblind checks in Compose UI Check

[Compose UI Check](https://developer.android.com/guide/topics/ui/accessibility/testing#compose-ui-check)
includes new colorblind simulations and checks, empowering you to craft visually
accessible experiences for all users. Simply enter UI Check mode from Compose
Preview to view your Compose UI in different types of color vision deficiencies
to ensure your designs remain clear and usable.
![Compose UI Check Colorblind example](https://developer.android.com/static/studio/images/design/compose-ui-check-colorblind.png)

## Redirect audio using device mirroring

Starting with Android Studio Jellyfish Canary 5, you can redirect audio from
connected physical devices to your computer speakers or headphones. With audio
redirection, keep your headphones connected to your computer and listen to both
the computer and connected phone without having to manually reconnect to one
device and then another. To enable audio redirection, go to **Android Studio \>
Settings \> Tools \> Device Mirroring** and select **Redirect audio from local
devices**. Note that audio is always redirected, regardless of the settings, for
Firebase Test Lab devices running Android 12 or higher.

## IntelliJ 2023.3 platform updates

Android Studio Jellyfish includes the IntelliJ 2023.3 platform release, which
has many new features such as comprehensive support for the latest Java 21
programing language features, an intuitive floating toolbar with editing
actions, and a **Run to Cursor** inlay option in the debugger to speed up your
workflow. To learn more see the
[IntelliJ release notes](https://www.jetbrains.com/idea/whatsnew/2023-3/).