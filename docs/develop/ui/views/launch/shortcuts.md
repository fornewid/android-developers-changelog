---
title: https://developer.android.com/develop/ui/views/launch/shortcuts
url: https://developer.android.com/develop/ui/views/launch/shortcuts
source: md.txt
---

# App shortcuts overview

As a developer, you can define*shortcuts*to perform specific actions in your app. You can display these shortcuts in a supported launcher or assistant---like Google Assistant---and help your users quickly start common or recommended tasks within your app.

This documentation shows you how to[create](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts)and[manage](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts)app shortcuts. You can also learn some[best practices](https://developer.android.com/guide/topics/ui/shortcuts/best-practices)to improve your shortcuts.

## Shortcut types

![app shortcuts](https://developer.android.com/static/images/guide/topics/ui/shortcuts_2023.png)**Figure 1.**Using app shortcuts, you can surface key actions and instantly take users deep into your app.

Each shortcut references one or more[intents](https://developer.android.com/guide/components/intents-filters), each of which launches a specific action in your app when users select the shortcut. The types of shortcuts you create for your app depend on the app's use case. Examples of actions you can express as shortcuts include the following:

- Composing a new email in an email app.
- Navigating users to a particular location in a mapping app.
- Sending messages to a user's contact in a communication app.
- Playing the next episode of a TV show in a media app.
- Loading the last save point in a gaming app.
- Letting the user order a drink in a delivery app using spoken commands.

| **Note:** Only main activities---activities that handle the[Intent.ACTION_MAIN](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN)action and the[Intent.CATEGORY_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)category---can have shortcuts. If an app has multiple main activities, define the set of shortcuts for each activity.

You can publish the following types of shortcuts for your app:

- *Static shortcuts* are defined in a resource file that is packaged into an APK or[app bundle](https://developer.android.com/guide/app-bundle/build).
- *Dynamic shortcuts*can be pushed, updated, and removed by your app only at runtime.
- *Pinned shortcuts* can be added to supported launchers at runtime if the user grants permission.**Note:**Users can also create pinned shortcuts by copying your app's static and dynamic shortcuts onto the launcher.

## Display shortcuts in assistants using capabilities

*Capabilities* in`shortcuts.xml`let you declare the types of actions users can take to launch your app and jump directly to performing a specific task. For example, you can give users voice control of your app through Google Assistant by declaring`capability`elements that extend your in-app functionality to Assistant[App Actions](https://developer.android.com/guide/app-actions/overview#app_actions). For more details, see the documentation about[adding capabilities](https://developer.android.com/guide/topics/ui/shortcuts/adding-capabilities).

## Shortcut limitations

Most supported launchers display up to four shortcuts at a time, including both static and dynamic shortcuts. When pushing dynamic shortcuts for display on Google's surfaces, such as Google Assistant, use the[Google Shortcuts Integration Library](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts#gsi-library)to avoid being subject to the shortcut limit.

If you choose not to use the Google Shortcuts Integration Library, your app is subject to the device's limit for the number of shortcuts it supports at a time. Shortcuts published this way only appear within the Android launchers and aren't discoverable on Google surfaces such as Assistant.
| **Note:** The maximum number of shortcuts a device supports varies. Use the[`getMaxShortcutCountPerActivity()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#getMaxShortcutCountPerActivity(android.content.Context))method to determine how many shortcuts a particular device supports.

There is no limit to the number of pinned shortcuts users can create to your app. Your app can't remove pinned shortcuts, but it can[disable](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts#disable-shortcuts)them.
| **Note:**Although other apps can't access the metadata within your shortcuts, the launcher itself can access this data. Therefore, conceal sensitive user information in this metadata.

To start creating shortcuts for your app, refer to the following documentation:

- [Create shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts)
- [Manage shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts)
- [Best practices for shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/best-practices)

For more details about operations you can perform on shortcuts, see the[ShortcutManager](https://developer.android.com/reference/android/content/pm/ShortcutManager)API reference documentation.