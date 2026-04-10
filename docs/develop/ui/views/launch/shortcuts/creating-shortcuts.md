---
title: https://developer.android.com/develop/ui/views/launch/shortcuts/creating-shortcuts
url: https://developer.android.com/develop/ui/views/launch/shortcuts/creating-shortcuts
source: md.txt
---

Shortcuts deliver specific types of content to your users by helping them
quickly access parts of your app.
![An image showing the contrast between app shortcuts and pinned shortcuts](https://developer.android.com/static/images/guide/topics/ui/shortcuts/pinned-shortcuts.png) **Figure 1.** App shortcuts and pinned shortcuts.

How you deliver content with shortcuts depends on your use case and whether
the shortcut's context is app-driven or user-driven. Although a static
shortcut's context doesn't change and a dynamic shortcut's context constantly
changes, your app drives the context in both cases. In cases where a user
chooses how your app delivers content to them, such as with a pinned shortcut,
the context is defined by the user. The following scenarios describe a few use
cases for each shortcut type:

- **[Static
  shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts#static) are best for apps that link to content using a consistent
  structure throughout the lifetime of a user's interaction with the
  app.** Because most launchers [only display four
  shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/best-practices) at once, static shortcuts are useful for performing a routine task in a consistent way, such as if the user wants to view their calendar or email in a specific way .
- **[Dynamic
  shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts#dynamic) are used for actions in apps that are
  context-sensitive.** Context-sensitive shortcuts are tailored to the actions users perform in an app. For example, if you build a game that lets the user start from their current level on launch, you need to update the shortcut frequently. Using a dynamic shortcut lets you update the shortcut each time the user clears a level.
- **[Pinned
  shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts#pinned) are used for specific user-driven actions.** For example, a user might want to pin a specific website to the launcher. This is beneficial because it lets the user perform a custom action---like navigating to the website in one step, more quickly than using a default instance of a browser.

## Create static shortcuts

Static shortcuts provide links to generic actions within your app, and these
actions must remain consistent over the lifetime of your app's current version.
Good options for static shortcuts include viewing sent messages, setting an
alarm, and displaying a user's exercise activity for the day.

To create a static shortcut, do the following:

1. In your app's `AndroidManifest.xml` file, find the activity whose intent filters are set to the `https://developer.android.com/reference/android/content/Intent#ACTION_MAIN` action and the `https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER` category.

   <br />

2. Add a
   `https://developer.android.com/guide/topics/manifest/meta-data-element`
   element to this activity that references the resource file where the app's
   shortcuts are defined:

   ```xml
     <manifest xmlns:android="http://schemas.android.com/apk/res/android"
               package="com.example.myapplication">
       <application ... >
         <activity android:name="Main">
           <intent-filter>
             <action android:name="android.intent.action.MAIN" />
             <category android:name="android.intent.category.LAUNCHER" />
           </intent-filter>
           
           <meta-data android:name="android.app.shortcuts"
                      android:resource="@xml/shortcuts" /> 
         </activity>
       </application>
     </manifest>
     
   ```
   | **Note:** If using an `https://developer.android.com/guide/topics/manifest/activity-alias-element` define the meta-data in the activity-alias rather than the activity it targets using the `https://developer.android.com/guide/topics/manifest/activity-alias-element#trgt` attribute.
3. Create a new resource file called `res/xml/shortcuts.xml`.

4. In the new resource file, add a `<shortcuts>` root element
   that contains a list of `<shortcut>` elements. In each
   `<shortcut>` element, include information about a static
   shortcut including its icon, description labels, and the intents it launches
   within the app:

   ```xml
     <shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
       <shortcut
         android:shortcutId="compose"
         android:enabled="true"
         android:icon="@drawable/compose_icon"
         android:shortcutShortLabel="@string/compose_shortcut_short_label1"
         android:shortcutLongLabel="@string/compose_shortcut_long_label1"
         android:shortcutDisabledMessage="@string/compose_disabled_message1">
         <intent
           android:action="android.intent.action.VIEW"
           android:targetPackage="com.example.myapplication"
           android:targetClass="com.example.myapplication.ComposeActivity" />
         <!-- If your shortcut is associated with multiple intents, include them
              here. The last intent in the list determines what the user sees when
              they launch this shortcut. -->
         <categories android:name="android.shortcut.conversation" />
         <capability-binding android:key="actions.intent.CREATE_MESSAGE" />
       </shortcut>
       <!-- Specify more shortcuts here. -->
     </shortcuts>
     
   ```

### Customize attribute values

The following list includes descriptions for the different attributes within
a static shortcut. Provide a value for `android:shortcutId` and
`android:shortcutShortLabel`. All other values are optional.


`android:shortcutId`

:   A string literal that represents the shortcut when a
    `https://developer.android.com/reference/android/content/pm/ShortcutManager`
    object performs operations on it.

    | **Note:** You can't set this attribute's value to a resource string, such as `@string/shortcut_id`.


`android:shortcutShortLabel`

:   A concise phrase that describes the shortcut's purpose. When possible,
    limit this short description to 10 characters.

    For more information, see
    `https://developer.android.com/reference/android/content/pm/ShortcutInfo.Builder#setShortLabel(java.lang.CharSequence)`.
    | **Note:** This attribute's value must be a resource string, such as `@string/shortcut_short_label`.


`android:shortcutLongLabel`

:   An extended phrase that describes the shortcut's purpose. If there's enough
    space, the launcher displays this value instead of
    `android:shortcutShortLabel`. When possible, limit this long
    description to 25 characters.

    For more information, see
    `https://developer.android.com/reference/android/content/pm/ShortcutInfo.Builder#setLongLabel(java.lang.CharSequence)`.
    | **Note:** This attribute's value must be a resource string, such as `@string/shortcut_long_label`.


`android:shortcutDisabledMessage`

:   The message that appears in a supported launcher when the user attempts to
    launch a disabled shortcut. The message must explain to the user why the
    shortcut is disabled. This attribute's value has no effect if
    `android:enabled` is `true`.

    | **Note:** This attribute's value must be a resource string, such as `@string/shortcut_disabled_message`.


`android:enabled`

:   Determines whether the user can interact with the shortcut from a supported
    launcher. The default value of `android:enabled` is
    `true`. If you set it to `false`, set an
    `android:shortcutDisabledMessage` that explains why you're
    disabling the shortcut. If you don't think you need to provide such a message,
    remove the shortcut from the XML file entirely.


`android:icon`

:   The [bitmap](https://developer.android.com/topic/performance/graphics) or
    [adaptive
    icon](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive) that the launcher uses when displaying the shortcut to the user. This
    value can be the path to an image or the resource file that contains the
    image. Use adaptive icons whenever possible to improve performance and
    consistency.

    | **Note:** Shortcut icons can't include [tints](https://developer.android.com/guide/topics/graphics/drawables#DrawableTint).

### Configure inner elements

The XML file that lists an app's static shortcuts supports the following
elements inside each `<shortcut>` element. You
**must** include an `intent` inner element for each
static shortcut that you define.


`intent`

:   The action that the system launches when the user selects the shortcut.
    This intent must provide a value for the `android:action`
    attribute.

    | **Note:** This `intent` element can't include string resources.

    You can provide multiple intents for a single shortcut. See
    [Manage
    multiple intents and activities](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts#multiple-intents-activities),
    [Set
    an intent](https://developer.android.com/develop/ui/views/components/settings/customize-your-settings#set-an-intent), and the
    `https://developer.android.com/reference/android/app/TaskStackBuilder`
    class reference for details.


`categories`

:   Provides a grouping for the types of actions that your app's shortcuts
    perform, such as creating new chat messages.

    For a list of supported shortcut categories, see the
    `https://developer.android.com/reference/android/content/pm/ShortcutInfo`
    class reference.


`capability-binding`

:   Declares the [capability](https://developer.android.com/guide/topics/ui/shortcuts/adding-capabilities)
    linked with the shortcut.

    In the previous example, the shortcut is linked to a capability declared
    for
    [`CREATE_MESSAGE`](https://developers.google.com/assistant/app/reference/built-in-intents/communications/create-message),
    which is an [App Actions](https://developers.google.com/assistant/app)
    built-in intent. This capability binding lets users use spoken commands with
    Google Assistant to invoke a shortcut.

## Create dynamic shortcuts

Dynamic shortcuts provide links to specific, context-sensitive actions within
your app. These actions can change between uses of your app and while your app
is running. Good uses for dynamic shortcuts include calling a specific person,
navigating to a specific location, and loading a game from the user's last save
point. You can also use dynamic shortcuts to open a conversation.

The
`https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat`
Jetpack library is a helper for the
`https://developer.android.com/reference/android/content/pm/ShortcutManager`
API, which lets you manage dynamic shortcuts in your app. Using the
`ShortcutManagerCompat` library reduces boilerplate code and helps
ensure that your shortcuts work consistently across Android versions. This
library is also required for pushing dynamic shortcuts so that they are eligible
to appear on Google surfaces---like Assistant---with the
[Google Shortcuts Integration Library](https://developer.android.com/develop/ui/views/launch/shortcuts/creating-shortcuts#gsi-library).

The `ShortcutManagerCompat` API lets your app perform the following
operations with dynamic shortcuts:

- **Push and update:** use `https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#pushDynamicShortcut(android.content.Context,%20androidx.core.content.pm.ShortcutInfoCompat)` to publish and update your dynamic shortcuts. If there are already dynamic or pinned shortcuts with the same ID, each mutable shortcut updates.
- **Remove:** remove a set of dynamic shortcuts using `https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#removeDynamicShortcuts(android.content.Context,%20java.util.List%3Cjava.lang.String%3E)`. Remove all dynamic shortcuts using `https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#removeAllDynamicShortcuts(android.content.Context)`.

For more information about performing operations on shortcuts, see
[Manage shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts)
and the
`https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat`
reference.

Here's an example of creating a dynamic shortcut and associating it with your
app:

### Kotlin

```kotlin
val shortcut = ShortcutInfoCompat.Builder(context, "id1")
        .setShortLabel("Website")
        .setLongLabel("Open the website")
        .setIcon(IconCompat.createWithResource(context, R.drawable.icon_website))
        .setIntent(Intent(Intent.ACTION_VIEW,
                Uri.parse("https://www.mysite.example.com/")))
        .build()

ShortcutManagerCompat.pushDynamicShortcut(context, shortcut)
```

### Java

```java
ShortcutInfoCompat shortcut = new ShortcutInfoCompat.Builder(context, "id1")
    .setShortLabel("Website")
    .setLongLabel("Open the website")
    .setIcon(IconCompat.createWithResource(context, R.drawable.icon_website))
    .setIntent(new Intent(Intent.ACTION_VIEW,
                   Uri.parse("https://www.mysite.example.com/")))
    .build();

ShortcutManagerCompat.pushDynamicShortcut(context, shortcut);
```

### Add the Google Shortcuts Integration Library

The Google Shortcuts Integration Library is an optional Jetpack library. It
lets you push dynamic shortcuts that can be displayed on Android surfaces, such
as the launcher, and Google surfaces, such as Assistant. Using this library
helps users discover your shortcuts to quickly access specific content or replay
actions in your app.

For example, a messaging app might push a dynamic shortcut for a contact
named "Alex" after a user messages that person. After the dynamic shortcut is
pushed, if the user asks Assistant, *"Hey Google, message Alex on ExampleApp,"* Assistant can launch ExampleApp and automatically configure it
to send a message to Alex.


Dynamic shortcuts pushed with this library aren't subject to the
[shortcut limits](https://developer.android.com/guide/topics/ui/shortcuts#shortcut-limitations)
enforced on a per-device basis. This lets your app push a shortcut every time a
user completes an associated action in your app. Pushing frequent shortcuts this
way lets Google understand your user's patterns of use and suggest contextually
relevant shortcuts to them.

For example, Assistant can learn from shortcuts pushed from your
fitness-tracking app that a user typically runs each morning and proactively
suggest a "start a run" shortcut when the user picks up their phone in the
morning.

The Google Shortcuts Integration Library doesn't offer any addressable
functionality itself. Adding this library to your app lets Google surfaces take
in the shortcuts your app pushes using `ShortcutManagerCompat`.

To use this library in your app, follow these steps:

1. Update your `gradle.properties` file to support
   [AndroidX libraries](https://developer.android.com/jetpack/androidx#using_androidx_libraries_in_your_project):

   ```xml
         
         android.useAndroidX=true
         # Automatically convert third-party libraries to use AndroidX
         android.enableJetifier=true
         
         
   ```
2. In `app/build.gradle`, add dependencies for the Google
   Shortcuts Integration Library and `ShortcutManagerCompat`:

   ```xml
         
         dependencies {
           implementation "androidx.core:core:1.6.0"
           implementation 'androidx.core:core-google-shortcuts:1.0.0'
           ...
         }
         
         
   ```

With the library dependencies added to your Android project, your app can use
the `pushDynamicShortcut()` method from
`ShortcutManagerCompat` to push dynamic shortcuts that are eligible
for display on the launcher and participating Google surfaces.
| **Note:** We recommend using `pushDynamicShortcut` to push dynamic shortcuts using the Google Shortcuts Integration Library. Your app can use other methods to publish shortcuts, but those might fail if they reach the maximum shortcut limit.

## Create pinned shortcuts

On Android 8.0 (API level 26) and higher, you can create pinned shortcuts.
Unlike static and dynamic shortcuts, pinned shortcuts appear in supported
launchers as separate icons. Figure 1 shows the distinction between these two
types of shortcuts.
| **Note:** When you attempt to pin a shortcut onto a supported launcher, the user receives a confirmation dialog asking their permission to pin the shortcut. If the user doesn't let the shortcut be pinned, the launcher cancels the request.

To pin a shortcut to a supported launcher using your app, complete the
following steps:

1. Use `https://developer.android.com/reference/android/content/pm/ShortcutManager#isRequestPinShortcutSupported()` to verify that the device's default launcher supports in-app pinning of shortcuts.
2. Create a `ShortcutInfo` object in one of two ways, depending
   on whether the shortcut exists:

   1. If the shortcut exists, create a `ShortcutInfo` object that contains only the existing shortcut's ID. The system finds and pins all other information related to the shortcut automatically.
   2. If you're pinning a new shortcut, create a `ShortcutInfo` object that contains an ID, an intent, and a short label for the new shortcut.

   | **Note:** Because the system performs [backup
   | and restore](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts#backup-restore) on pinned shortcuts automatically, these shortcuts' IDs must contain stable, constant strings or server-side identifiers, rather than identifiers generated locally that might not make sense on other devices.
3. Pin the shortcut to the device's launcher by calling
   `https://developer.android.com/reference/android/content/pm/ShortcutManager#requestPinShortcut(android.content.pm.ShortcutInfo,%20android.content.IntentSender)`.
   During this process, you can pass in a
   `https://developer.android.com/reference/android/app/PendingIntent`
   object, which notifies your app only when the shortcut pins
   successfully.

   | **Note:** If the user doesn't let the shortcut be pinned to the launcher, your app doesn't receive a callback.

   After a shortcut is pinned, your app can update its contents using the
   `https://developer.android.com/reference/android/content/pm/ShortcutManager#updateShortcuts(java.util.List%3Candroid.content.pm.ShortcutInfo%3E)`
   method. For more information, read
   [Update
   shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/managing-shortcuts#update-shortcuts).

The following code snippet demonstrates how to create a pinned shortcut.
| **Note:** Instances of the `ShortcutManager` class must be obtained using `https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.Class%3CT%3E)` with the argument `ShortcutManager.class` or `https://developer.android.com/reference/android/content/Context#getSystemService(java.lang.String)` with the argument `https://developer.android.com/reference/android/content/Context#SHORTCUT_SERVICE`.

### Kotlin

```kotlin
val shortcutManager = getSystemService(ShortcutManager::class.java)

if (shortcutManager!!.isRequestPinShortcutSupported) {
    // Enable the existing shortcut with the ID "my-shortcut".
    val pinShortcutInfo = ShortcutInfo.Builder(context, "my-shortcut").build()

    // Create the PendingIntent object only if your app needs to be notified
    // that the user let the shortcut be pinned. If the pinning operation fails,
    // your app isn't notified. Assume here that the app implements a method
    // called createShortcutResultIntent() that returns a broadcast intent.
    val pinnedShortcutCallbackIntent = shortcutManager.createShortcutResultIntent(pinShortcutInfo)

    // Configure the intent so that your app's broadcast receiver gets the
    // callback successfully. For details, see https://developer.android.com/reference/android/app/PendingIntent#getBroadcast(android.content.Context,%20int,%20android.content.Intent,%20int).
    val successCallback = PendingIntent.getBroadcast(context, /* request code */ 0,
            pinnedShortcutCallbackIntent, /* flags */ 0)

    shortcutManager.requestPinShortcut(pinShortcutInfo,
            successCallback.intentSender)
}
```

### Java

```java
ShortcutManager shortcutManager =
        context.getSystemService(ShortcutManager.class);

if (shortcutManager.isRequestPinShortcutSupported()) {
    // Enable the existing shortcut with the ID "my-shortcut".
    ShortcutInfo pinShortcutInfo =
            new ShortcutInfo.Builder(context, "my-shortcut").build();

    // Create the PendingIntent object only if your app needs to be notified
    // that the user let the shortcut be pinned. If the pinning operation fails,
    // your app isn't notified. Assume here that the app implements a method
    // called createShortcutResultIntent() that returns a broadcast intent.
    Intent pinnedShortcutCallbackIntent =
            shortcutManager.createShortcutResultIntent(pinShortcutInfo);

    // Configure the intent so that your app's broadcast receiver gets the
    // callback successfully. For details, see https://developer.android.com/reference/android/app/PendingIntent#getBroadcast(android.content.Context,%20int,%20android.content.Intent,%20int).
    PendingIntent successCallback = PendingIntent.getBroadcast(context, /* request code */ 0,
            pinnedShortcutCallbackIntent, /* flags */ 0);

    shortcutManager.requestPinShortcut(pinShortcutInfo,
            successCallback.getIntentSender());
}
```
| **Note:** See also the Support Library APIs `https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#isRequestPinShortcutSupported(android.content.Context)` and `https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat#requestPinShortcut(android.content.Context,androidx.core.content.pm.ShortcutInfoCompat,android.content.IntentSender)`, which work on Android 7.1 (API level 25) and lower. The Support Library falls back to the deprecated `https://developer.android.com/reference/android/content/Intent#EXTRA_SHORTCUT_INTENT` extra to attempt the pinning process.

### Create a custom shortcut activity

![An image showing the custom dialog activity that shows the prompt 'Do
you want to add the Gmail launcher icon to your home screen?' The custom
options are 'No thanks' and 'Add icon'.](https://developer.android.com/static/images/guide/topics/ui/shortcuts/pinned-shortcuts-dialog.png) **Figure 2.** Example of a custom app shortcut dialog activity.

You can also create a specialized activity that helps users create shortcuts,
complete with custom options and a confirmation button. Figure 2 shows an
example of this type of activity in the Gmail app.

In your app's manifest file, add
`https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_SHORTCUT`
to the activity's
`https://developer.android.com/guide/topics/manifest/intent-filter-element`
element. This declaration sets up the following behavior when the user attempts
to create a shortcut:

1. The system starts your app's specialized activity.
2. The user sets options for the shortcut.
3. The user selects the confirmation button.
4. Your app creates the shortcut using the `https://developer.android.com/reference/android/content/pm/ShortcutManager#createShortcutResultIntent(android.content.pm.ShortcutInfo)` method. This method returns an `https://developer.android.com/reference/android/content/Intent`, which your app relays back to the previously executing activity using `https://developer.android.com/reference/android/app/Activity#setResult(int)`.
5. Your app calls `https://developer.android.com/reference/android/app/Activity#finish()` on the activity used to create the customized shortcut.

Similarly, your app can prompt users to add pinned shortcuts to the home
screen after installation or the first time the app is launched. This method is
effective because it helps your users create a shortcut as part of their
ordinary workflow.

## Test shortcuts

To test your app's shortcuts, install your app on a device with a launcher
that supports shortcuts. Then, perform the following actions:

- Touch \& hold your app's launcher icon to view the shortcuts that you define for your app.
- Drag a shortcut to pin it to the device's launcher.