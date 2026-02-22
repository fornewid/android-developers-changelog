---
title: https://developer.android.com/training/wearables/apps/launcher
url: https://developer.android.com/training/wearables/apps/launcher
source: md.txt
---

# Appear in Recents and app resume

The[launcher](https://developer.android.com/training/wearables/user-interfaces#app_launcher_entries)displays a label and icon for any recently resumed[tasks](https://developer.android.com/guide/components/activities/tasks-and-back-stack). If your app package has multiple apps as separate launcher activities, the launcher doesn't know which label and icon to display for non-launcher activities, such as activities launched from a tile or a notification. This might prevent your app from appearing in the**Recents**list in the launcher and cause your app to display incorrectly .

## Label all activities

Verify your activities, including non-launcher activities, are properly labeled in your manifest file, as shown in the following steps.
![An illustration of correctly labeled activities within an Android manifest file.](https://developer.android.com/static/wear/images/activities_1.png)Examples of properly labeled activities.

1. For each activity in your`AndroidManifest.xml`file, determine which launcher activity it belongs to.
2. Copy the icon, round icon, and label from the parent launcher activity into each associated non-launcher activity.
3. For activities that are shared among multiple launcher activities, decide which icon and label to display that represents all of them.

| **Note:** If the launcher cannot determine the correct icon and label, it defaults to the icon and label of your application tag.

## Configure tasks for Recents

To use`RecentTasks`for the**Recents** section in the launcher, verify your`taskAffinity`elements are correctly defined in your`AndroidManifest.xml`file and that you manage your tasks and back stack consistently.

Consider the following when assigning tasks:

- Choose a unique[`taskAffinity`](https://developer.android.com/guide/topics/manifest/activity-element#aff)name for each task in your app. You can consider each launcher activity and its children as one task. Assign that`taskAffinity`to each related activity in your manifest file.
- Avoid calling`startActivity()`with[`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)or[`FLAG_ACTIVITY_CLEAR_TOP`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_CLEAR_TOP).
- Avoid creating*trampoline activities* , which are activities that only launch other activities. Create splash screens using the[SplashScreen API](https://developer.android.com/reference/android/R.attr#windowSplashscreenContent).
- Use`android:excludeFromRecents="true"`and`android:noHistory="true"`flags when you don't want your activity to appear in the**Recents**section.
- Determine the best[launch mode](https://developer.android.com/guide/components/activities/tasks-and-back-stack#TaskLaunchModes)for your activities and develop with that in mind.

## Debug tips

Consider the following when debugging:

- If there are double entries in the**Recents** section for a single app, check if you are using the`NEW_TASK`flag inappropriately.
- If the wrong icon or label appears, verify that each associated non-launcher activity has the same icon, round icon, and label as its parent activity.
- If the system doesn't launch anything after tapping the entry in the launcher, check Logcat (filtered on`launcher`) for errors, because a trampoline activity can cause this issue.

## Recommended resources

- [Building UI with Compose](https://developer.android.com/training/wearables/compose)
- [Wear OS apps](https://developer.android.com/training/wearables/apps)
- [Compose for Wear OS codelab](https://developer.android.com/codelabs/compose-for-wear-os#0)