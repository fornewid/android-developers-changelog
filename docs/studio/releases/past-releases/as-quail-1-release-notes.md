---
title: https://developer.android.com/studio/releases/past-releases/as-quail-1-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-quail-1-release-notes
source: md.txt
---

The following are the release notes for Android Studio Quail 1.

## Patch releases

The following is a list of patch releases for Android Studio Quail 1.

### Android Studio Quail 1 \| 2026.1.2 Patch 1 (June 2026)

This minor update includes [these bug
fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2026.1.1#android-studio-quail-1-%7C-2026.1.1-patch-1).

#### Android Studio Quail 1 parallel Gradle Sync execution change

Starting from Android Studio Quail 1, the `org.gradle.parallel=true` property in
the `gradle.properties` file no longer enables parallel model fetching during
Gradle Sync. This will result in a large sync time regression for large
projects.

To enable parallel sync in Android Studio Quail 1, set
`org.gradle.tooling.parallel=true` in your project's `gradle.properties` file.

> [!NOTE]
> **Note:** Adding `org.gradle.tooling.parallel=true` to your project in Android Studio Quail 1 Patch 1 will not enable IDEA parallel model fetching per default, so your project does not have to be compatible with Gradle project isolation in order to enable parallel Gradle Sync.
>
> If you're using a version of Android Studio Quail 1 that is lower than
> Patch 1, then your project needs to be compatible with Gradle project
> isolation to use the `org.gradle.tooling.parallel=true` property.
> For more details, see the
> [known issue](https://developer.android.com/studio/known-issues#android-studio-quail-1-parallel-sync-execution-issue).

The following are new features in Android Studio Quail 1.

## Suggested fixes for crashes with Agent integration in AQI

The [App Quality Insights](https://developer.android.com/studio/debug/app-quality-insights) tool
window is now integrated with the AI agent to analyze crash data along with
your source code to provide detailed explanations and suggest potential fixes.
After selecting a crash in the App Quality Insights tool window, navigate to
the **Insights** tab and click **See more** to see a detailed explanation of
the crash. Click **Fix with AI** to have the agent suggest code changes that
you can review and accept.
![](https://developer.android.com/static/studio/images/agent-integration-aqi.png) New agent integration in AQI with options to "See more" and "Fix with AI"