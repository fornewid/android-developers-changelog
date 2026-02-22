---
title: https://developer.android.com/training/sharing/direct-share-targets
url: https://developer.android.com/training/sharing/direct-share-targets
source: md.txt
---

![](https://developer.android.com/static/training/sharing/direct-share-targets.png) **Figure 1:** Direct Share row in Sharesheet, as shown by 1

Use Direct Share targets to make it easier and faster for users of other apps
to share URLs, images, or other kinds of data with your app. Direct Share works
by presenting contacts from messaging and social apps directly on the Android
Sharesheet, without users having to select the app then search for the contact.
| **Note:** Starting in Android 11 (API level 30), you may provide Direct Share targets only through the [Sharing Shortcuts](https://developer.android.com/training/sharing/direct-share-targets#sharing-shortcuts-api) API described later on this page.

[`ShortcutManagerCompat`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat)
is an AndroidX API that provides Sharing Shortcuts, and that is backward
compatible with the deprecated `ChooserTargetService` API. This is the preferred
way to publish both Sharing Shortcuts and `ChooserTargets`. For instructions,
see [Use AndroidX to provide both Sharing Shortcuts andChooserTargets](https://developer.android.com/training/sharing/direct-share-targets#androidx-compat-library)
on this page.

## Publish Direct Share targets

The Sharesheet Direct Share row only surfaces dynamic shortcuts provided by the
Sharing Shortcuts API. Complete the following steps to publish Direct Share
targets.

1. In your app's XML resource file, declare `share-target` elements.

       <shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
       <share-target android:targetClass="com.example.android.sharingshortcuts.SendMessageActivity">
           <data android:mimeType="text/plain" />
           <category android:name="com.example.android.sharingshortcuts.category.TEXT_SHARE_TARGET" />
       </share-target>
       </shortcuts>

2. When your app initializes, use [`setDynamicShortcuts`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#setDynamicShortcuts(android.content.Context,java.util.List%3Candroidx.core.content.pm.ShortcutInfoCompat%3E))
   to order dynamic shortcuts by importance.

   A lower index indicates more importance. If you're making a communication
   app, they can be top conversations ordered by recency as they appear in
   your app. Don't publish shortcuts that are stale; a conversation with no
   user activity in the last 30 days is considered stale.  

   ### Kotlin

   ```kotlin
   ShortcutManagerCompat.setDynamicShortcuts(myContext, listOf(shortcut1, shortcut2, ..))
   ```

   ### Java

   ```java
   List<ShortcutInfoCompat> shortcuts = new ArrayList<>();
   shortcuts.add(shortcut1);
   shortcuts.add(shortcut2);
   ...
   ShortcutManagerCompat.setDynamicShortcuts(myContext, shortcuts);
   ```
3. If you're developing a communication app, report shortcut usage through
   [`pushDynamicShortcut`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,androidx.core.content.pm.ShortcutInfoCompat)) immediately every time the user
   receives or sends a message to a contact. See [Report shortcut usage for
   communications apps](https://developer.android.com/training/sharing/direct-share-targets#track-shortcut-usage-comms-apps) on this page for more information. For example, report usage for messages sent by the user by
   specifying capability bindings in the shortcut through
   [`ShortcutInfoCompat.Builder#addCapabilityBinding`](https://developer.android.com/reference/kotlin/androidx/core/content/pm/ShortcutInfoCompat.Builder#addCapabilityBinding(java.lang.String))
   with the `actions.intent.SEND_MESSAGE` capability.

   ### Kotlin

   ```kotlin
   val shortcutInfo = ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
     ...
     .setShortLabel(firstName)
     .setLongLabel(fullName)
     .setCategories(matchedCategories)
     .setLongLived(true)
   .addCapabilityBinding("actions.intent.SEND_MESSAGE").build()
   ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo)
   ```

   ### Java

   ```java
   ShortcutInfoCompat shortcutInfo = new ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
     ...
     .setShortLabel(firstName)
     .setLongLabel(fullName)
     .setCategories(matchedCategories)
     .setLongLived(true)
     .addCapabilityBinding("actions.intent.SEND_MESSAGE")
     .build();

   ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo);
   ```
4. If the user deletes a contact, use
   [`removeLongLivedShortcut`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#removeLongLivedShortcuts(android.content.Context,java.util.List%3Cjava.lang.String%3E)). This is the preferred
   way to remove the shortcut regardless of whether it's cached by system
   services. The following code snippet shows an example of how to do this.

   ### Kotlin

   ```kotlin
   val deleteShortcutId = "..."
   ShortcutManagerCompat.removeLongLivedShortcuts(myContext, listOf(deleteShortcutId))
   ```

   ### Java

   ```java
   String deleteShortcutId = "...";
   ShortcutManagerCompat.removeLongLivedShortcuts(
       myContext, Arrays.asList(deleteShortcutId));
   ```

## Improve rankings of your Direct Share targets

The Android Sharesheet shows a fixed number of Direct Share targets. These
suggestions are sorted by rank. You can potentially improve the ranking of your
shortcuts by doing the following:

- Ensure all `shortcutIds` are unique and never reused for different targets.
- Ensure the shortcut is long-lived by calling [`setLongLived(true)`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLived()).
- For conversation-related shortcuts, report shortcut usage for outgoing and incoming messages by republishing corresponding shortcuts through [`ShortcutManagerCompat.pushDynamicShortcut`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,androidx.core.content.pm.ShortcutInfoCompat)). See [Report shortcut usage for communications apps](https://developer.android.com/training/sharing/direct-share-targets#track-shortcut-usage-comms-apps) on this page for details.
- Avoid providing irrelevant or stale Direct Share targets---for example, contacts the user hasn't messaged within the last 30 days.
- For SMS apps, avoid providing shortcuts for short codes or conversations identified as potential spam. Users are highly unlikely to share to those conversations.
- Call [`setCategories()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setCategories(java.util.Set%3Cjava.lang.String%3E)) to associate the shortcut with the appropriate [`mimeType`
  attributes](https://developer.android.com/training/sharing/receive#supporting-mime-types). For example, for an SMS app, if the contact is not RCS- or MMS-enabled, you wouldn't associate the corresponding shortcut with non-text MIME types such as `image/*` and `video/*`.
- For a given conversation, once a dynamic shortcut is pushed and usage is reported, don't change the shortcut ID. This ensures retention of usage data for ranking.

If the user taps any Direct Share target, your app must take them to a UI where
they can perform an action directly on the subject of the target. Don't present
the user a disambiguation UI, and don't place them in a UI unrelated to the
tapped target. For example, in a messaging app, tapping a Direct Share
target takes the user to a conversation view with the person they selected. The
keyboard is visible and the message is prefilled with the shared data.

## Sharing Shortcuts API

Starting in Android 10 (API level 29),
[`ShortcutInfo.Builder`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder) added methods and enhancements
that provide additional info about the share target:

[`setCategories()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setCategories(java.util.Set%3Cjava.lang.String%3E))
:   Starting with Android 10, categories are also used to filter shortcuts that
    can handle share intents or actions. See [Declare a share
    target](https://developer.android.com/training/sharing/direct-share-targets#declare-share-target) for details. This field is required for shortcuts
    meant to be used as share targets.

[`setLongLived()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLived())

:   Specifies whether or not a shortcut is valid when it has been unpublished or
    made invisible by the app (as a dynamic or pinned shortcut). If a shortcut
    is long lived, it can be cached by various system services even after if has
    been unpublished as a dynamic shortcut.

    Making a shortcut long lived can improve its ranking. See [Get the best
    ranking](https://developer.android.com/training/sharing/direct-share-targets#get-best-ranking) for details.

[`setShortLabel()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setShortLabel(java.lang.CharSequence)), [`setLongLabel()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setLongLabel(java.lang.CharSequence))

:   When publishing a shortcut to an individual person please include their full
    name in `setLongLabel()` and any short name, such as a nickname or a first
    name, in `setShortLabel()`.

Look at an example of [publishing Sharing Shortcuts on GitHub](https://github.com/android/storage-samples/tree/main/SharingShortcuts).

## Provide shortcut imagery

To make a Sharing Shortcut, you'll need to add an image via [`setIcon()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutInfoCompat.Builder#setIcon(androidx.core.graphics.drawable.IconCompat)).

Sharing Shortcuts can appear across system surfaces and might be reshaped.
Additionally, some devices running Android versions 7, 8, or 9 (API levels 25,
26, 27, and 28) might display bitmap‑only icons without a background, which
dramatically decreases contrast. To ensure your shortcut looks as intended,
provide an adaptive bitmap by using [`IconCompat.createWithAdaptiveBitmap()`](https://developer.android.com/reference/androidx/core/graphics/drawable/IconCompat#createWithAdaptiveBitmap(android.graphics.Bitmap)).

Make sure adaptive bitmaps follow the same [guidelines and dimensions set for adaptive icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive).
The most common way to accomplish this is to scale the intended square bitmap to
72x72 dp and center that within a 108x108 dp transparent canvas. If your icon
includes transparent regions, you need to include a background color; otherwise,
transparent regions appear black.

Do not provide imagery masked to a specific shape. For example, prior to
Android 10 (API level 29), it was common to provide user avatars for Direct Share
`ChooserTarget`s that were masked to a circle. The Android Sharesheet and other
system surfaces in Android 10 now shape and theme shortcut imagery.
The preferred method to provide Sharing Shortcuts, through
[`ShortcutManagerCompat`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat),
automatically shape backcompat Direct Share `ChooserTarget` objects to
circles for you.

## Declare a share target

Share targets must be declared in the app's resource file, similar to [static shortcuts definitions](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts). Add share
target definitions inside the `<shortcuts>` root element in the resource file,
along with other static shortcut definitions. Each `<share-targets>` element
contains information about the shared data type, matching categories, and the
target class that will handle the share intent. The XML code looks something
like this:  

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
  <share-target android:targetClass="com.example.android.sharingshortcuts.SendMessageActivity">
    <data android:mimeType="text/plain" />
    <category android:name="com.example.android.sharingshortcuts.category.TEXT_SHARE_TARGET" />
  </share-target>
</shortcuts>
```

The data element in a share target is similar to the [data specification in an intent filter](https://developer.android.com/guide/topics/manifest/data-element). Each share target can have
multiple categories, which are only used to match an app's published shortcuts
with its share target definitions. Categories can have any arbitrary app-defined
values.

In case the user selects the Sharing Shortcut in the Android Sharesheet that
matches with the example target-share above, the app will get the following
share intent:  

```actionscript-3
Action: Intent.ACTION_SEND
ComponentName: {com.example.android.sharingshortcuts /
                com.example.android.sharingshortcuts.SendMessageActivity}
Data: Uri to the shared content
EXTRA_SHORTCUT_ID: <ID of the selected shortcut>
```

If the user opens the share target from the launcher shortcuts, the app will get
the intent that was created when adding the sharing shortcut to the
[ShortcutManagerCompat](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat).
Since it's a different intent, `Intent.EXTRA_SHORTCUT_ID` won't be available,
and you will have to pass the ID manually if you need it.

## Report shortcut usage for communication apps

If you're developing a communication app, you can improve your ranking in the
Android Sharesheet by reporting usage for both outgoing and incoming messages.
To do so, republish the conversation shortcut that represents the contact through
[`ShortcutManagerCompat.pushDynamicShortcut`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,androidx.core.content.pm.ShortcutInfoCompat)).

Shortcut usage and capability bindings are backward compatible to Android 5.0
(API 21).

### Report shortcut usage for outgoing messages

Reporting usage for messages sent by the user is functionally similar to
clicking the "send" button after creating a message.

To trigger usage reporting, specify capability bindings in the shortcut
through [`ShortcutInfoCompat.Builder#addCapabilityBinding`](https://developer.android.com/reference/kotlin/androidx/core/content/pm/ShortcutInfoCompat.Builder#addCapabilityBinding(java.lang.String))
with the `actions.intent.SEND_MESSAGE` capability.  

### Kotlin

```kotlin
val shortcutInfo = ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(firstName)
  .setLongLabel(fullName)
  .setCategories(matchedCategories)
  .setLongLived(true)
.addCapabilityBinding("actions.intent.SEND_MESSAGE").build()
ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo)
```

### Java

```java
ShortcutInfoCompat shortcutInfo = new ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(firstName)
  .setLongLabel(fullName)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.SEND_MESSAGE")
  .build();

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo);
```

If the outgoing message is for a group chat, you must also add the `Audience`
parameter value as the [`recipient`](https://schema.org/recipient)
type is associated with the capability.  

### Kotlin

```kotlin
val shortcutInfo = ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(groupShortTitle)
  .setLongLabel(groupLongTitle)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.SEND_MESSAGE", "message.recipient.@type", listOf("Audience")).build()

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo)
```

### Java

```java
ShortcutInfoCompat shortcutInfo = new ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(groupShortTitle)
  .setLongLabel(groupLongTitle)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.SEND_MESSAGE", "message.recipient.@type", Arrays.asList("Audience"))
  .build();

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo);
```

### Report shortcut usage for incoming messages

To trigger usage reporting when the user receives a message such as an SMS,
chat message, email, or notifications, you must additionally specify capability
bindings in the shortcut through
[`ShortcutInfoCompat.Builder#addCapabilityBinding`](https://developer.android.com/reference/kotlin/androidx/core/content/pm/ShortcutInfoCompat.Builder#addCapabilityBinding(java.lang.String)) with
the `actions.intent.RECEIVE_MESSAGE` capability.  

### Kotlin

```kotlin
val shortcutInfo = ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(firstName)
  .setLongLabel(fullName)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.RECEIVE_MESSAGE").build()

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo)
```

### Java

```java
ShortcutInfoCompat shortcutInfo = new ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(firstName)
  .setLongLabel(fullName)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.RECEIVE_MESSAGE")
  .build();

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo);
```

If the incoming message is from a group chat, you must also add the `Audience`
parameter value as the [`sender`](https://schema.org/sender) type
is associated with the capability.  

### Kotlin

```kotlin
val shortcutInfo = ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(groupShortTitle)
  .setLongLabel(groupLongTitle)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.RECEIVE_MESSAGE", "message.sender.@type", listOf("Audience")).build()

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo)
```

### Java

```java
ShortcutInfoCompat shortcutInfo = new ShortcutInfoCompat.Builder(myContext, staticConversationIdentifier)
  ...
  .setShortLabel(groupShortTitle)
  .setLongLabel(groupLongTitle)
  .setCategories(matchedCategories)
  .setLongLived(true)
  .addCapabilityBinding("actions.intent.RECEIVE_MESSAGE", "message.sender.@type", Arrays.asList("Audience"))
  .build();

ShortcutManagerCompat.pushDynamicShortcut(myContext, shortcutInfo);
```

## Use AndroidX to provide both Sharing Shortcuts and ChooserTargets

To be able to work with the AndroidX compatibility library, the app's manifest
must contain the meta-data chooser-target-service and intent-filters set. See
the current `ChooserTargetService` [Direct Share](https://developer.android.com/about/versions/marshmallow/android-6.0#direct-share) API.

This service is already declared in the compatibility library, so the user does
not need to declare the service in the app's manifest. However, the link from
the share activity to the service must be taken into account as a chooser target
provider.

In the following example, the implementation of `ChooserTargetService` is
`androidx.core.content.pm.ChooserTargetServiceCompat`, which is already defined
in AndroidX:  

```xml
<activity
    android:name=".SendMessageActivity"
    android:label="@string/app_name"
    android:theme="@style/SharingShortcutsDialogTheme">
    <!-- This activity can respond to Intents of type SEND -->
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
    <!-- Only needed if you import the sharetarget AndroidX library that
         provides backwards compatibility with the old DirectShare API.
         The activity that receives the Sharing Shortcut intent needs to be
         taken into account with this chooser target provider. -->
    <meta-data
        android:name="android.service.chooser.chooser_target_service"
        android:value="androidx.sharetarget.ChooserTargetServiceCompat" />
</activity>
```

## Sharing Shortcuts FAQ

**How are the shortcut usage data stored and do they leave the device?**

Shortcuts are stored entirely on-device in the system data directory in an
encrypted disk partition. Information in shortcuts such as the icon, the intent,
and names of people and resources are accessible only by system services and the
same app that publishes the shortcuts.

**What is the history of Direct Share?**

We introduced Direct Share in Android 6.0 (API level 23) to allow apps to
provide `ChooserTarget` objects through a `ChooserTargetService`. Results were
retrieved reactively on demand, leading to a slow loading time for targets.

In Android 10 (API level 29), we replaced the `ChooserTargetService` Direct
Share APIs with the new Sharing Shortcuts API. Instead of retrieving results
reactively on demand, the Sharing Shortcuts API let apps publish Direct Share
targets in advance. This rapidly sped up the process of retrieving Direct Share
targets when preparing the ShareSheet. The `ChooserTargetService` Direct Share
mechanism will continue to work, but the system ranks targets that are provided
this way lower than any target that uses the Sharing Shortcuts API.

Android 11 (API level 30) deprecated the `ChooserTargetService` service, and
Sharing Shortcuts API is the only way to provide Direct Share targets.

**How are published shortcuts for share targets different from launcher
shortcuts (the typical usage of shortcuts when long pressing on app icons in
launcher)?**

Any shortcuts published for a "share target" purpose, is also a launcher
shortcut, and will be shown in the menu when long pressing your app's icon. The
maximum shortcut count limit per activity also applies to the total number of
shortcuts an app is publishing (share targets and legacy launcher shortcuts
combined).

**What is the guidance on the number of sharing shortcuts one should publish.**

The number of sharing shortcuts is constrained to the same limit of dynamic
shortcuts available via
[`getMaxShortcutCountPerActivity(android.content.Context)`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#getMaxShortcutCountPerActivity(android.content.Context)). One can publish any
number to that limit but must keep in mind that sharing shortcuts can be visible
in the app launcher long-press and in the share sheet. Most app launchers on
long-press display a maximum of four or five shortcuts in portrait mode, and
eight in landscape mode. See this
[FAQ](https://github.com/android/user-interface-samples/tree/main/People#shortcuts)
for more details and guidance on sharing shortcuts.