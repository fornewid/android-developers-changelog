---
title: https://developer.android.com/develop/devices/assistant/dynamic-shortcuts
url: https://developer.android.com/develop/devices/assistant/dynamic-shortcuts
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

[Android shortcuts](https://developer.android.com/guide/topics/ui/shortcuts) provide users with quick
methods to perform an action or access content in an app.
Assistant can proactively suggest your Android dynamic shortcuts to users at
relevant times, enabling users to easily discover and replay your
voice-enabled functionality.

For example, you can push a shortcut for each note a user creates in
your note taking app. You make
dynamic links eligible to display on Google surfaces, like Assistant,
by adding the [Google Shortcuts Integration Jetpack library](https://developer.android.com/jetpack/androidx/releases/core#core-google-shortcuts-1.0.1) to your project.
This library lets Assistant take in dynamic shortcuts you push using the
[`ShortcutManagerCompat`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat) class, which is a Jetpack wrapper for the
[`ShortcutManager`](https://developer.android.com/reference/android/content/pm/ShortcutManager) API.

When you use the Google Shortcuts Integration library in your app, dynamic
shortcuts you push to Google are visible to users as voice shortcut suggestions
in the Assistant app. You can push an unlimited number of dynamic shortcuts to
Assistant using the [`pushDynamicShortcut()`](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,%20androidx.core.content.pm.ShortcutInfoCompat)) method of the
`ShortcutManagerCompat` library.

## Configure your development project

Adding dynamic shortcuts functionality to your app requires the
Google Shortcuts Integration library, which is an Android Jetpack library.
This section describes how to configure your app development project to include
this library.

To add this Jetpack library and configure your project, follow these steps:

1. Update your `gradle.properties` file to handle Jetpack libraries:

   **gradle.properties**

       android.useAndroidX=true
       # Automatically convert third-party libraries to use AndroidX
       android.enableJetifier=true

2. Add the Jetpack library dependencies to your `build.gradle`:

   **app/build.gradle**

       dependencies {
        implementation "androidx.core:core:1.6.0"
        implementation "androidx.core:core-google-shortcuts:1.0.1"
        ...
       }

   In the preceding sample code, you list two Jetpack libraries as
   dependencies. The `androidx.core:core:1.6.0` library contains the
   `ShortcutManagerCompat` class, which you use to push dynamic shortcuts to
   Google.

   The `androidx.core:core-google-shortcuts:1.0.1` is the Google
   Shortcuts Integration library. This library contains no developer-facing
   API. By adding it as a dependency, you enable Assistant to take in the
   dynamic shortcuts you push using the `ShortcutManagerCompat` class.

   > [!NOTE]
   > **Note:** Visit the [Jetpack library explorer](https://developer.android.com/jetpack/androidx/explorer) to find the latest versions of the Core and Google Shortcuts Integration libraries.

## Push dynamic shortcuts

To push dynamic shortcuts that are eligible for display on Assistant,
you first create the shortcut using the `ShortcutInfoCompat.Builder()`
class.

You then push the shortcut using the
`ShortcutManagerCompat.pushDynamicShortcut()` method. Shortcuts are pushed
whenever a user completes a relevant action in your app. The following sample
code pushes a shortcut every time a user creates a list in a notes and lists app.

**ExampleOrderActivity**

### Kotlin

```kotlin
// Define the dynamic shortcut for an item
var intent = Intent(context, DisplayOrderActivity::class.java)
intent.action = Intent.ACTION_VIEW
var shortcutInfo = ShortcutInfoCompat.Builder(context, id)
    .setShortLabel("Running")
    .setLongLabel("Start running")
    .addCapabilityBinding(
        "actions.intent.CREATE_ITEM_LIST", "itemList.name", Arrays.asList("My First List")
    )
    .setIntent(intent) // Push the shortcut
    .build()

// Push the shortcut
ShortcutManagerCompat.pushDynamicShortcut(context, shortcutInfo)
```

### Java

```java
// Define the dynamic shortcut for an item
Intent intent = new Intent(context, DisplayOrderActivity.class);
intent.setAction(Intent.ACTION_VIEW);

ShortcutInfoCompat.Builder shortcutInfo = new ShortcutInfoCompat.Builder(context, id)
    .setShortLabel("Running")
    .setLongLabel("Start running")
    .addCapabilityBinding(
      "actions.intent.CREATE_ITEM_LIST", "itemList.name", Arrays.asList("My First List"))
    .setIntent(intent)
    .build();

// Push the shortcut
ShortcutManagerCompat.pushDynamicShortcut(context, shortcutInfo);
```

The `id` referenced in the `ShortcutInfoCompat.Builder` method in the preceding
sample code defines the `shortcutId` of the resulting shortcut object. This `id`
must be a unique string literal. For details, see the
[Android Shortcuts documentation](https://developer.android.com/reference/android/content/pm/ShortcutInfo#getId()).

In the preceding example, the `addCapabilityBinding` method binds the dynamic
shortcut to a `capability` of the same `android:name` defined in
`shortcuts.xml`. This method lets you associate the shortcut to a
semantic [built-in intent](https://developer.android.com/guide/app-actions/intents) (BII) parameter.

Dynamic shortcuts sometimes are pushed without any particular BII parameter
association. When invoked by the user, Assistant triggers the `intent` defined
in the shortcut to fulfill the action. The following example shows a dynamic
shortcut with no parameter association:

### Kotlin

```kotlin
var intent: Intent = Intent(context, DisplayOrderActivity::class.java)
intent.setPackage(this, "com.sample.app")
intent.setAction(Intent.ACTION_VIEW)

var shortcutInfo: ShortcutInfoCompat = ShortcutInfoCompat.Builder(context, id)
    .setShortLabel("Create a list")
    .setLongLabel("Create a list")
    .addCapabilityBinding("actions.intent.CREATE_ITEM_LIST")
    .setIntent(intent)
    .build()

ShortcutManagerCompat.pushDynamicShortcut(context, shortcutInfo);
```

### Java

```java
Intent intent = new Intent(context, DisplayOrderActivity.class);
intent.setPackage(this, "com.sample.app");
intent.setAction(Intent.ACTION_VIEW);

ShortcutInfoCompat shortcutInfo = new ShortcutInfoCompat.Builder(context, id)
  .setShortLabel("Create a list")
  .setLongLabel("Create a list")
  .addCapabilityBinding("actions.intent.CREATE_ITEM_LIST")
  .setIntent(intent)
  .build();

ShortcutManagerCompat.pushDynamicShortcut(context, shortcutInfo);
```

## Test dynamic shortcuts with Assistant

When Google Assistant successfully takes in a dynamic shortcut from your
application, the shortcut is eligible to appear as a Voice Shortcut suggestion in the
Assistant Android app. The Assistant app suggests the most recent shortcuts
pushed by your app.

To test your dynamic shortcuts with Assistant, follow these steps:

1. Create a preview of your App Actions and prepare your test device or emulator for testing actions by following the same setup requirements as for the [Google Assistant Plugin](https://developer.android.com/guide/app-actions/test-tool).
2. Open your app and define a dynamic shortcut to push. Then complete an action. For example, if you push a shortcut whenever a note is created in your note taking app, then create a new note.
3. Open **Shortcuts** in the **Assistant Settings** app on your device. Your dynamic shortcut appears in the list for your app.