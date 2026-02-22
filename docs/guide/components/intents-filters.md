---
title: https://developer.android.com/guide/components/intents-filters
url: https://developer.android.com/guide/components/intents-filters
source: md.txt
---

An [Intent](https://developer.android.com/reference/android/content/Intent) is a messaging object you can use to request an action
from another [app component](https://developer.android.com/guide/components/fundamentals#Components).
Although intents facilitate communication between components in several ways, there are three
fundamental use cases:

<br />

- **Starting an activity**

  An [Activity](https://developer.android.com/reference/android/app/Activity) represents a single screen in an app. You can start a new
  instance of an [Activity](https://developer.android.com/reference/android/app/Activity) by passing an [Intent](https://developer.android.com/reference/android/content/Intent)
  to [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)).
  The [Intent](https://developer.android.com/reference/android/content/Intent)
  describes the activity to start and carries any necessary data.

  If you want to receive a result from the activity when it finishes,
  call [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)). Your activity receives the result
  as a separate [Intent](https://developer.android.com/reference/android/content/Intent) object in your activity's [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)) callback.
  For more information, see the [Activities](https://developer.android.com/guide/components/activities) guide.
- **Starting a service**

  A [Service](https://developer.android.com/reference/android/app/Service) is a component that performs operations in the background
  without a user interface. With Android 5.0 (API level 21) and later, you can start a service
  with [JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler). For more information
  about [JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler), see its
  [API-reference documentation](https://developer.android.com/reference/android/app/job/JobScheduler).

  For versions earlier than Android 5.0 (API level 21), you can start a service by using
  methods of the [Service](https://developer.android.com/reference/android/app/Service) class. You can start a service
  to perform a one-time operation
  (such as downloading a file) by passing an [Intent](https://developer.android.com/reference/android/content/Intent)
  to [startService()](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)). The [Intent](https://developer.android.com/reference/android/content/Intent)
  describes the service to start and carries any necessary data.

  If the service is designed with a client-server interface, you can bind to the service
  from another component by passing an [Intent](https://developer.android.com/reference/android/content/Intent) to [bindService()](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent, android.content.ServiceConnection, int)). For more information, see the [Services](https://developer.android.com/guide/components/services) guide.
- **Delivering a broadcast**

  A broadcast is a message that any app can receive. The system delivers various
  broadcasts for system events, such as when the system boots up or the device starts charging.
  You can deliver a broadcast to other apps by passing an [Intent](https://developer.android.com/reference/android/content/Intent)
  to [sendBroadcast()](https://developer.android.com/reference/android/content/Context#sendBroadcast(android.content.Intent)) or
  [sendOrderedBroadcast()](https://developer.android.com/reference/android/content/Context#sendOrderedBroadcast(android.content.Intent, java.lang.String)).

The rest of this page explains how intents work and how to use them.
For related information, see
[Interacting with Other Apps](https://developer.android.com/training/basics/intents)
and [Sharing Content](https://developer.android.com/training/sharing).

## Intent types

There are two types of intents:

- **Explicit intents** specify which component of which application will satisfy the intent, by specifying a full `ComponentName`. You'll typically use an explicit intent to start a component in your own app, because you know the class name of the activity or service you want to start. For example, you might start a new activity within your app in response to a user action, or start a service to download a file in the background.
- **Implicit intents** do not name a specific component, but instead declare a general action to perform, which allows a component from another app to handle it. For example, if you want to show the user a location on a map, you can use an implicit intent to request that another capable app show a specified location on a map.

Figure 1 shows how an intent is used when starting an activity. When the
[Intent](https://developer.android.com/reference/android/content/Intent) object names a specific activity component explicitly, the system
immediately starts that component.  
![](https://developer.android.com/static/images/components/intent-filters_2x.png)

**Figure 1.** How an implicit intent is
delivered through the system to start another activity: **\[1\]** *Activity A* creates an
[Intent](https://developer.android.com/reference/android/content/Intent) with an action description and passes it to [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)). **\[2\]** The Android System searches all
apps for an intent filter that matches the intent. When a match is found, **\[3\]** the system
starts the matching activity (*Activity B* ) by invoking its [onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) method and passing it the [Intent](https://developer.android.com/reference/android/content/Intent).

When you use an implicit intent, the Android system finds the appropriate component to start
by comparing the contents of the intent to the *intent filters* declared in the [manifest file](https://developer.android.com/guide/topics/manifest/manifest-intro) of other apps on the
device. If the intent matches an intent filter, the system starts that component and delivers it
the [Intent](https://developer.android.com/reference/android/content/Intent) object. If multiple intent filters are compatible, the system
displays a dialog so the user can pick which app to use.

An intent filter is an expression in an app's manifest file that
specifies the type of intents that the component
would like to receive. For instance, by declaring an intent filter for an activity,
you make it possible for other apps to directly start your activity with a certain kind of intent.
Likewise, if you do *not* declare any intent filters for an activity, then it can be started
only with an explicit intent.

**Caution:** To ensure that your app is secure, always
use an explicit
intent when starting a [Service](https://developer.android.com/reference/android/app/Service) and do not
declare intent filters for your services. Using an implicit intent to start a service is a
security hazard because you can't be certain what service will respond to the intent,
and the user can't see which service starts. Beginning with Android 5.0 (API level 21), the system
throws an exception if you call [bindService()](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent, android.content.ServiceConnection, int))
with an implicit intent.

## Building an intent

An [Intent](https://developer.android.com/reference/android/content/Intent) object carries information that the Android system uses
to determine which component to start (such as the exact component name or component
category that should receive the intent), plus information that the recipient component uses in
order to properly perform the action (such as the action to take and the data to act upon).

The primary information contained in an [Intent](https://developer.android.com/reference/android/content/Intent) is the following:

**Component name**

:   The name of the component to start. This is optional, but it's the critical piece of information that makes an intent
    *explicit* , meaning that the intent should be delivered only to the app component
    defined by the component name. Without a component name, the intent is *implicit* and the
    system decides which component should receive the intent based on the other intent information
    (such as the action, data, and category---described below). If you need to start a specific
    component in your app, you should specify the component name.

    **Note:** When starting a [Service](https://developer.android.com/reference/android/app/Service),
    *always specify the component name*. Otherwise, you cannot be certain what service
    will respond to the intent, and the user cannot see which service starts.

    This field of the [Intent](https://developer.android.com/reference/android/content/Intent) is a
    [ComponentName](https://developer.android.com/reference/android/content/ComponentName) object, which you can specify using a fully
    qualified class name of the target component, including the package name of the app, for example,
    `com.example.ExampleActivity`. You can set the component name with [setComponent()](https://developer.android.com/reference/android/content/Intent#setComponent(android.content.ComponentName)), [setClass()](https://developer.android.com/reference/android/content/Intent#setClass(android.content.Context, java.lang.Class<?>)), [setClassName()](https://developer.android.com/reference/android/content/Intent#setClassName(java.lang.String, java.lang.String)),
    or with the
    [Intent](https://developer.android.com/reference/android/content/Intent) constructor.

**Action**
:   A string that specifies the generic action to perform (such as *view* or *pick* ).

    In the case of a broadcast intent, this is the action that took place and is being reported.
    The action largely determines how the rest of the intent is structured---particularly
    the information that is contained in the data and extras.

    You can specify your own actions for use by intents within your app (or for use by other
    apps to invoke components in your app), but you usually specify action constants
    defined by the [Intent](https://developer.android.com/reference/android/content/Intent) class or other framework classes. Here are some
    common actions for starting an activity:


    [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)
    :   Use this action in an intent with [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) when you have some information that
        an activity can show to the user, such as a photo to view in a gallery app, or an address to
        view in a map app.

    [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)
    :   Also known as the *share* intent, you should use this in an intent with [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) when you have some data that the user can
        share through another app, such as an email app or social sharing app.


    See the [Intent](https://developer.android.com/reference/android/content/Intent) class reference for more
    constants that define generic actions. Other actions are defined
    elsewhere in the Android framework, such as in [Settings](https://developer.android.com/reference/android/provider/Settings) for actions
    that open specific screens in the system's Settings app.


    You can specify the action for an intent with [setAction()](https://developer.android.com/reference/android/content/Intent#setAction(java.lang.String)) or with an [Intent](https://developer.android.com/reference/android/content/Intent) constructor.


    If you define your own actions, be sure to include your app's package name
    as a prefix, as shown in the following example:


    ### Kotlin

    ```kotlin
    const val ACTION_TIMETRAVEL = "com.example.action.TIMETRAVEL"
    ```

    ### Java

    ```java
    static final String ACTION_TIMETRAVEL = "com.example.action.TIMETRAVEL";
    ```

**Data**
:   The URI (a [Uri](https://developer.android.com/reference/android/net/Uri) object) that references the data to
    be acted on and/or the
    MIME type of that data. The type of data supplied is generally dictated by the intent's action. For
    example, if the action is [ACTION_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT), the data should contain the
    URI of the document to edit.

    When creating an intent,
    it's often important to specify the type of data (its MIME type) in addition to its URI.
    For example, an activity that's able to display images probably won't be able
    to play an audio file, even though the URI formats could be similar.
    Specifying the MIME type of your data helps the Android
    system find the best component to receive your intent.
    However, the MIME type can sometimes be inferred from the URI---particularly when the data is a
    `content:` URI. A `content:` URI indicates the data is located on the device
    and controlled by a
    [ContentProvider](https://developer.android.com/reference/android/content/ContentProvider), which makes the data MIME type visible to the system.


    To set only the data URI, call [setData()](https://developer.android.com/reference/android/content/Intent#setData(android.net.Uri)).
    To set only the MIME type, call [setType()](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String)). If necessary, you
    can set both explicitly with [setDataAndType()](https://developer.android.com/reference/android/content/Intent#setDataAndType(android.net.Uri, java.lang.String)).


    **Caution:** If you want to set both the URI and MIME type,
    *don't* call [setData()](https://developer.android.com/reference/android/content/Intent#setData(android.net.Uri)) and
    [setType()](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String)) because they each nullify the value of the other.
    Always use [setDataAndType()](https://developer.android.com/reference/android/content/Intent#setDataAndType(android.net.Uri, java.lang.String)) to set both
    URI and MIME type.

**Category**
:   A string containing additional information about the kind of component
    that should handle the intent. Any number of category descriptions can be
    placed in an intent, but most intents do not require a category.
    Here are some common categories:

    [CATEGORY_BROWSABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_BROWSABLE)
    :   The target activity allows itself to be started by a web browser to display data
        referenced by a link, such as an image or an e-mail message.

    [CATEGORY_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)
    :   The activity is the initial activity of a task and is listed in
        the system's application launcher.


    See the [Intent](https://developer.android.com/reference/android/content/Intent) class description for the full list of
    categories.


    You can specify a category with [addCategory()](https://developer.android.com/reference/android/content/Intent#addCategory(java.lang.String)).

These properties listed above (component name, action, data, and category) represent the
defining characteristics of an intent. By reading these properties, the Android system
is able to resolve which app component it should start. However, an intent can carry
additional information that does not affect
how it is resolved to an app component. An intent can also supply the following information:

**Extras**

:   Key-value pairs that carry additional information required to accomplish the requested action. Just as some actions use particular kinds of data URIs, some actions also use particular extras. You can add extra data with various [putExtra()](https://developer.android.com/reference/android/content/Intent#putExtra(java.lang.String, android.os.Bundle)) methods,
    each accepting two parameters: the key name and the value.
    You can also create a [Bundle](https://developer.android.com/reference/android/os/Bundle) object with all the extra data, then insert
    the [Bundle](https://developer.android.com/reference/android/os/Bundle) in the [Intent](https://developer.android.com/reference/android/content/Intent) with [putExtras()](https://developer.android.com/reference/android/content/Intent#putExtras(android.content.Intent)).

    For example, when creating an intent to send an email with
    [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND), you can specify the *to* recipient with the
    [EXTRA_EMAIL](https://developer.android.com/reference/android/content/Intent#EXTRA_EMAIL) key, and specify the *subject* with the
    [EXTRA_SUBJECT](https://developer.android.com/reference/android/content/Intent#EXTRA_SUBJECT) key.

    The [Intent](https://developer.android.com/reference/android/content/Intent) class specifies many `EXTRA_*` constants
    for standardized data types. If you need to declare your own extra keys (for intents that
    your app receives), be sure to include your app's package name
    as a prefix, as shown in the following example:  

    ### Kotlin

    ```kotlin
    const val EXTRA_GIGAWATTS = "com.example.EXTRA_GIGAWATTS"
    ```

    ### Java

    ```java
    static final String EXTRA_GIGAWATTS = "com.example.EXTRA_GIGAWATTS";
    ```


    **Caution** : Do not use [Parcelable](https://developer.android.com/reference/android/os/Parcelable) or
    [Serializable](https://developer.android.com/reference/java/io/Serializable) data when sending an intent that you expect
    another app to receive. If an app
    attempts to access data in a [Bundle](https://developer.android.com/reference/android/os/Bundle) object but does not
    have access to the parceled or serialized class, the system raises a
    [RuntimeException](https://developer.android.com/reference/java/lang/RuntimeException).

**Flags**
:   Flags are defined in the [Intent](https://developer.android.com/reference/android/content/Intent) class that function as metadata for the
    intent. The flags may instruct the Android system how to launch an activity (for example, which
    [task](https://developer.android.com/guide/components/tasks-and-back-stack)
    the activity should belong
    to) and how to treat it after it's launched (for example, whether it belongs in the list of recent
    activities).

    For more information, see the [setFlags()](https://developer.android.com/reference/android/content/Intent#setFlags(int)) method.

### Example explicit intent

An explicit intent is one that you use to launch a specific app component, such as
a particular activity or service in your app. To create an explicit intent, define
the component name for the [Intent](https://developer.android.com/reference/android/content/Intent) object---all
other intent properties are optional.

For example, if you built a service in your app, named `DownloadService`,
designed to download a file from the web, you can start it with the following code:  

### Kotlin

    // Executed in an Activity, so 'this' is the https://developer.android.com/reference/android/content/Context
    // The fileUrl is a string URL, such as "http://www.example.com/image.png"
    val downloadIntent = Intent(this, DownloadService::class.java).apply {
        data = https://developer.android.com/reference/android/net/Uri#parse(java.lang.String)(fileUrl)
    }
    startService(downloadIntent)

### Java

    // Executed in an Activity, so 'this' is the https://developer.android.com/reference/android/content/Context
    // The fileUrl is a string URL, such as "http://www.example.com/image.png"
    Intent downloadIntent = new Intent(this, DownloadService.class);
    downloadIntent.setData(https://developer.android.com/reference/android/net/Uri#parse(java.lang.String)(fileUrl));
    startService(downloadIntent);

The [Intent(Context, Class)](https://developer.android.com/reference/android/content/Intent#Intent(android.content.Context, java.lang.Class<?>))
constructor supplies the app [Context](https://developer.android.com/reference/android/content/Context) and the
component a [Class](https://developer.android.com/reference/java/lang/Class) object. As such,
this intent explicitly starts the `DownloadService` class in the app.

For more information about building and starting a service, see the
[Services](https://developer.android.com/guide/components/services) guide.

### Example implicit intent

An implicit intent specifies an action that can invoke any app on the device able
to perform the action. Using an implicit intent is useful when your app cannot perform the
action, but other apps probably can and you'd like the user to pick which app to use.

For example, if you have content that you want the user to share with other people,
create an intent
with the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) action
and add extras that specify the content to share. When you call
[startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) with that intent, the user can
pick an app through which to share the content.  

### Kotlin

```kotlin
// Create the text message with a string.
val sendIntent = Intent().apply {
    action = Intent.ACTION_SEND
    putExtra(Intent.EXTRA_TEXT, textMessage)
    type = "text/plain"
}

// Try to invoke the intent.
try {
    startActivity(sendIntent)
} catch (e: ActivityNotFoundException) {
    // Define what your app should do if no activity can handle the intent.
}
```

### Java

```java
// Create the text message with a string.
Intent sendIntent = new Intent();
sendIntent.setAction(Intent.ACTION_SEND);
sendIntent.putExtra(Intent.EXTRA_TEXT, textMessage);
sendIntent.setType("text/plain");

// Try to invoke the intent.
try {
    startActivity(sendIntent);
} catch (ActivityNotFoundException e) {
    // Define what your app should do if no activity can handle the intent.
}
```

When [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) is called, the system
examines all of the installed apps to determine which ones can handle this kind of intent (an
intent with the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) action and that carries "text/plain"
data). If there's only one app that can handle it, that app opens immediately and is given the
intent. If no other apps can handle it, your app can catch the
[`ActivityNotFoundException`](https://developer.android.com/reference/android/content/ActivityNotFoundException)
that occurs. If multiple activities accept the intent, the system
displays a dialog such as the one shown in Figure 2, so the user can pick which app to use.

More information about launching other apps is also provided in the guide
about [sending the user to
another app](https://developer.android.com/training/basics/intents/sending).  
![](https://developer.android.com/static/images/training/basics/intent-chooser.png)

**Figure 2.** A chooser dialog.

### Forcing an app chooser

When there is more than one app that responds to your implicit intent,
the user can select which app to use and make that app the default choice for the
action. The ability to select a default is helpful when performing an action for which the user
probably wants to use the same app every time, such as when opening a web page (users
often prefer just one web browser).

However, if multiple apps can respond to the intent and the user might want to use a different
app each time, you should explicitly show a chooser dialog. The chooser dialog asks the
user to select which app to use for the action (the user cannot select a default app for
the action). For example, when your app performs "share" with the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) action, users may want to share using a different app depending
on their current situation, so you should always use the chooser dialog, as shown in Figure 2.

To show the chooser, create an [Intent](https://developer.android.com/reference/android/content/Intent) using [createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser(android.content.Intent, java.lang.CharSequence)) and pass it to [startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)), as shown in the following example.
This example displays a dialog with a list of apps that respond to the intent passed to the [createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser(android.content.Intent, java.lang.CharSequence)) method and uses the supplied text as the
dialog title.  

### Kotlin

```kotlin
val sendIntent = Intent(Intent.ACTION_SEND)
...

// Always use string resources for UI text.
// This says something like "Share this photo with"
val title: String = resources.getString(R.string.chooser_title)
// Create intent to show the chooser dialog
val chooser: Intent = Intent.createChooser(sendIntent, title)

// Verify the original intent will resolve to at least one activity
if (sendIntent.resolveActivity(packageManager) != null) {
    startActivity(chooser)
}
```

### Java

```java
Intent sendIntent = new Intent(Intent.ACTION_SEND);
...

// Always use string resources for UI text.
// This says something like "Share this photo with"
String title = getResources().getString(R.string.chooser_title);
// Create intent to show the chooser dialog
Intent chooser = Intent.createChooser(sendIntent, title);

// Verify the original intent will resolve to at least one activity
if (sendIntent.resolveActivity(getPackageManager()) != null) {
    startActivity(chooser);
}
```

### Detect unsafe intent launches

Your app might launch intents to navigate between components inside of your app,
or to perform an action on behalf of another app. To improve platform security,
Android 12 (API level 31) and higher provide a debugging feature that warns you
if your app performs an unsafe launch of an intent. For example, your app might
perform an unsafe launch of a *nested intent*, which is an intent that is passed
as an extra in another intent.

If your app performs both of the following actions, the system detects an unsafe
intent launch, and a [StrictMode](https://developer.android.com/reference/android/os/StrictMode) violation
occurs:

1. Your app unparcels a nested intent from the extras of a delivered intent.
2. Your app immediately starts an [app
   component](https://developer.android.com/guide/components/fundamentals#Components) using that nested intent, such as passing the intent into [`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)), [`startService()`](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)), or [`bindService()`](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent,%20android.content.ServiceConnection,%20int)).

For more details on how to identify this situation and make changes to your app,
read the blog post about [Android Nesting
Intents](https://medium.com/androiddevelopers/android-nesting-intents-e472fafc1933)
on Medium.

#### Check for unsafe intent launches

To check for unsafe intent launches in your app, call
[`detectUnsafeIntentLaunch()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectUnsafeIntentLaunch())
when you configure your `VmPolicy`, as shown in the following code snippet. If
your app detects a StrictMode violation, you might want to stop app execution to
protect potentially sensitive information.
**Note:** If your app targets Android 12 and uses the [`detectAll()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectAll()) method in its `VmPolicy` definition, the `detectUnsafeIntentLaunch()` method is called automatically.  

### Kotlin

```kotlin
fun onCreate() {
    StrictMode.setVmPolicy(VmPolicy.Builder()
        // Other StrictMode checks that you've previously added.
        // ...
        .detectUnsafeIntentLaunch()
        .penaltyLog()
        // Consider also adding penaltyDeath()
        .build())
}
```

### Java

```java
protected void onCreate() {
    StrictMode.setVmPolicy(new VmPolicy.Builder()
        // Other StrictMode checks that you've previously added.
        // ...
        .detectUnsafeIntentLaunch()
        .penaltyLog()
        // Consider also adding penaltyDeath()
        .build());
}
```

#### Use intents more responsibly

To minimize the chance of an unsafe intent launch, and a StrictMode violation,
follow these best practices.

**Copy only the essential extras within intents, and perform any necessary
sanitation and validation.** Your app might copy the extras from one intent to
another intent that is used to launch a new component. This occurs when your
app calls
[`putExtras(Intent)`](https://developer.android.com/reference/android/content/Intent#putExtras(android.content.Intent))
or
[`putExtras(Bundle)`](https://developer.android.com/reference/android/content/Intent#putExtras(android.os.Bundle)).
If your app performs one of these operations, copy only the extras that the
receiving component expects. If the other intent (that receives the copy)
launches a component that isn't
[exported](https://developer.android.com/guide/topics/manifest/activity-element#exported), sanitize and
validate the extras before copying them to the intent that launches the
component.

**Don't export your app's components unnecessarily.** For example, if you
intend to launch an app component using an internal nested intent, set that
component's `android:exported` attribute to `false`.

**Use a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) instead of a
nested intent.** That way, when another app unparcels the `PendingIntent` of its
containing `Intent`, the other app can launch the `PendingIntent` using the
identity of your app. This configuration allows the other app to safely launch
any component, including a non-exported component, in your app.

The diagram in figure 2 shows how the system passes control from your (client)
app to another (service) app, and back to your app:

1. Your app creates an intent that invokes an activity in another app. Within that intent, you add a `PendingIntent` object as an extra. This pending intent invokes a component in your app; this component isn't exported.
2. Upon receiving your app's intent, the other app extracts the nested `PendingIntent` object.
3. The other app invokes the `send()` method on the `PendingIntent` object.
4. After passing control back to your app, the system invokes the pending intent using your app's context.

![](https://developer.android.com/static/images/guide/components/nested-pending-intent.svg)

**Figure 2.** Diagram of inter-app communication when using a nested pending
intent.

## Receiving an implicit intent

To advertise which implicit intents your app can receive, declare one or more intent filters for
each of your app components with an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element in your [manifest file](https://developer.android.com/guide/topics/manifest/manifest-intro).
Each intent filter specifies the type of intents it accepts based on the intent's action,
data, and category. The system delivers an implicit intent to your app component only if the
intent can pass through one of your intent filters.

**Note:** An explicit intent is always delivered to its target,
regardless of any intent filters the component declares.

An app component should declare separate filters for each unique job it can do.
For example, one activity in an image gallery app may have two filters: one filter
to view an image, and another filter to edit an image. When the activity starts,
it inspects the [Intent](https://developer.android.com/reference/android/content/Intent) and decides how to behave based on the information
in the [Intent](https://developer.android.com/reference/android/content/Intent) (such as to show the editor controls or not).

Each intent filter is defined by an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element in the app's manifest file, nested in the corresponding app component (such
as an [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)
element).

In each app component that includes an `<intent-filter>` element,
explicitly set a value for
[`android:exported`](https://developer.android.com/guide/topics/manifest/activity-element#exported).
This attribute indicates whether the app component is accessible to other apps. In some
situations, such as activities whose intent filters include the
[`LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)
category, it's useful to set this attribute to `true`. Otherwise,
it's safer to set this attribute to `false`.

**Warning:** If an activity, service, or broadcast
receiver in your app uses intent filters and doesn't explicitly set the value
for `android:exported`, your app can't be installed on a device that
runs Android 12 or higher.

Inside the [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element),
you can specify the type of intents to accept using one or more
of these three elements:

[`<action>`](https://developer.android.com/guide/topics/manifest/action-element)
:   Declares the intent action accepted, in the `name` attribute. The value
    must be the literal string value of an action, not the class constant.

[`<data>`](https://developer.android.com/guide/topics/manifest/data-element)
:   Declares the type of data accepted, using one or more attributes that specify various
    aspects of the data URI (`scheme`, `host`, `port`,
    `path`) and MIME type.

[`<category>`](https://developer.android.com/guide/topics/manifest/category-element)
:   Declares the intent category accepted, in the `name` attribute. The value
    must be the literal string value of an action, not the class constant.

    **Note:** To receive implicit intents, you
    *must include* the
    [CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category in the intent filter. The methods
    [startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)) and
    [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)) treat all intents
    as if they declared the [CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category.
    If you do not declare this category in your intent filter, no implicit intents will resolve to
    your activity.

For example, here's an activity declaration with an intent filter to receive an
[ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) intent when the data type is text:  

```xml
<activity android:name="ShareActivity" android:exported="false">
    <intent-filter>
        <action android:name="android.intent.action.SEND"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:mimeType="text/plain"/>
    </intent-filter>
</activity>
```

You can create a filter that includes more than one instance of
[`<action>`](https://developer.android.com/guide/topics/manifest/action-element),
[`<data>`](https://developer.android.com/guide/topics/manifest/data-element), or
[`<category>`](https://developer.android.com/guide/topics/manifest/category-element).
If you do, you need to be certain that the component can handle any and all
combinations of those filter elements.

When you want to handle multiple kinds of intents, but only in specific combinations of
action, data, and category type, then you need to create multiple intent filters.

An implicit intent is tested against a filter by comparing the intent to each of the
three elements. To be delivered to the component, the intent must pass all three tests.
If it fails to match even one of them, the Android system won't deliver the intent to the
component. However, because a component may have multiple intent filters, an intent that does
not pass through one of a component's filters might make it through on another filter.
More information about how the system resolves intents is provided in the section below
about [Intent Resolution](https://developer.android.com/guide/components/intents-filters#Resolution).  
**Caution:** Using an intent filter isn't a secure way to prevent other apps from starting
your components. Although intent filters restrict a component to respond to only
certain kinds of implicit intents, another app can potentially start your app component
by using an explicit intent if the developer determines your component names.
If it's important that *only your own app* is able to start one of your components,
do not declare intent filters in your manifest. Instead, set the
[`exported`](https://developer.android.com/guide/topics/manifest/activity-element#exported) attribute
to `"false"` for that component.

Similarly, to avoid inadvertently running a different app's
[Service](https://developer.android.com/reference/android/app/Service), always use an explicit intent to start your own service.

**Note:**
For all activities, you must declare your intent filters in the manifest file.
However, filters for broadcast receivers can be registered dynamically by calling
[registerReceiver()](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter, java.lang.String, android.os.Handler)). You can then unregister the receiver with [unregisterReceiver()](https://developer.android.com/reference/android/content/Context#unregisterReceiver(android.content.BroadcastReceiver)). Doing so allows your app
to listen for specific broadcasts during only a specified period of time while your app
is running.

### Example filters

To demonstrate some of the intent filter behaviors, here is an example
from the manifest file of a social-sharing app:  

```xml
<activity android:name="MainActivity" android:exported="true">
    <!-- This activity is the main entry, should appear in app launcher -->
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>

<activity android:name="ShareActivity" android:exported="false">
    <!-- This activity handles "SEND" actions with text data -->
    <intent-filter>
        <action android:name="android.intent.action.SEND"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:mimeType="text/plain"/>
    </intent-filter>
    <!-- This activity also handles "SEND" and "SEND_MULTIPLE" with media data -->
    <intent-filter>
        <action android:name="android.intent.action.SEND"/>
        <action android:name="android.intent.action.SEND_MULTIPLE"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:mimeType="application/vnd.google.panorama360+jpg"/>
        <data android:mimeType="image/*"/>
        <data android:mimeType="video/*"/>
    </intent-filter>
</activity>
```

The first activity, `MainActivity`, is the app's main entry point---the activity that
opens when the user initially launches the app with the launcher icon:

- The [ACTION_MAIN](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN) action indicates this is the main entry point and does not expect any intent data.
- The [CATEGORY_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER) category indicates that this activity's icon should be placed in the system's app launcher. If the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) element does not specify an icon with `icon`, then the system uses the icon from the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element.

These two must be paired together in order for the activity to appear in the app launcher.

The second activity, `ShareActivity`, is intended to facilitate sharing text and media
content. Although users might enter this activity by navigating to it from `MainActivity`,
they can also enter `ShareActivity` directly from another app that issues an implicit
intent matching one of the two intent filters.

**Note:** The MIME type,
[`application/vnd.google.panorama360+jpg`](https://developers.google.com/panorama/android/), is a special data type that specifies
panoramic photos, which you can handle with the [Google
panorama](https://developers.google.com/android/reference/com/google/android/gms/panorama/package-summary) APIs.

## Match intents to other apps' intent filters

If another app targets Android 13 (API level 33) or higher, it can handle your
app's intent only if your intent matches the actions and categories of an
`<intent-filter>` element in that other app. If the system doesn't find a
match, it throws an
[`ActivityNotFoundException`](https://developer.android.com/reference/android/content/ActivityNotFoundException).
The sending app must handle
this exception.

Similarly, if you update your app so that it targets Android 13
or higher, all intents originating from external apps are delivered to an
exported component of your app only if that intent matches the actions and
categories of an `<intent-filter>` element that your app declares. This behavior
occurs regardless of the sending app's target SDK version.

In the following cases, intent matching isn't enforced:

- Intents delivered to components that don't declare any intent filters.
- Intents originating from within the same app.
- Intents originating from the system; that is, intents being sent from the "system UID" (uid=1000). System apps include `system_server` and apps that set `android:sharedUserId` to `android.uid.system`.
- Intents originating from root.

Learn more about [intent matching](https://developer.android.com/guide/components/intents-filters#imatch).

## Using a pending intent

A [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) object is a wrapper around an [Intent](https://developer.android.com/reference/android/content/Intent) object. The primary purpose of a [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)
is to grant permission to a foreign application
to use the contained [Intent](https://developer.android.com/reference/android/content/Intent) as if it were executed from your
app's own process.

Major use cases for a pending intent include the following:

- Declaring an intent to be executed when the user performs an action with your [Notification](https://developer.android.com/develop/ui/views/notifications) (the Android system's [NotificationManager](https://developer.android.com/reference/android/app/NotificationManager) executes the [Intent](https://developer.android.com/reference/android/content/Intent)).
- Declaring an intent to be executed when the user performs an action with your [App Widget](https://developer.android.com/guide/topics/appwidgets) (the Home screen app executes the [Intent](https://developer.android.com/reference/android/content/Intent)).
- Declaring an intent to be executed at a specified future time (the Android system's [AlarmManager](https://developer.android.com/reference/android/app/AlarmManager) executes the [Intent](https://developer.android.com/reference/android/content/Intent)).

Just as each [Intent](https://developer.android.com/reference/android/content/Intent) object is designed to be handled by a specific
type of app component (either an [Activity](https://developer.android.com/reference/android/app/Activity), a [Service](https://developer.android.com/reference/android/app/Service), or
a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)), so too must a [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) be
created with the same consideration. When using a pending intent, your app doesn't
execute the intent with a call such as [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)). Instead, you must declare the intended component type when you create the
[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) by calling the respective creator method:

- [PendingIntent.getActivity()](https://developer.android.com/reference/android/app/PendingIntent#getActivity(android.content.Context, int, android.content.Intent, int)) for an [Intent](https://developer.android.com/reference/android/content/Intent) that starts an [Activity](https://developer.android.com/reference/android/app/Activity).
- [PendingIntent.getService()](https://developer.android.com/reference/android/app/PendingIntent#getService(android.content.Context, int, android.content.Intent, int)) for an [Intent](https://developer.android.com/reference/android/content/Intent) that starts a [Service](https://developer.android.com/reference/android/app/Service).
- [PendingIntent.getBroadcast()](https://developer.android.com/reference/android/app/PendingIntent#getBroadcast(android.content.Context, int, android.content.Intent, int)) for an [Intent](https://developer.android.com/reference/android/content/Intent) that starts a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver).

Unless your app is *receiving* pending intents from other apps,
the above methods to create a [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) are probably the only
[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) methods you'll ever need.

Each method takes the current app [Context](https://developer.android.com/reference/android/content/Context), the
[Intent](https://developer.android.com/reference/android/content/Intent) you want to wrap, and one or more flags that specify
how the intent should be used (such as whether the intent can be used more than once).

For more information about using pending intents, see the documentation for each
of the respective use cases, such as in the [Notifications](https://developer.android.com/develop/ui/views/notifications)
and [App Widgets](https://developer.android.com/guide/topics/appwidgets) API guides.

### Specify mutability

If your app targets Android 12 or higher, you must specify the
mutability of each `PendingIntent` object that your app creates. To declare that
a given `PendingIntent` object is mutable or immutable, use the
[`PendingIntent.FLAG_MUTABLE`](https://developer.android.com/reference/android/app/PendingIntent#FLAG_MUTABLE)
or
[`PendingIntent.FLAG_IMMUTABLE`](https://developer.android.com/reference/android/app/PendingIntent#FLAG_IMMUTABLE)
flag, respectively.

If your app attempts to create a `PendingIntent` object
without setting either mutability flag, the system throws an
[`IllegalArgumentException`](https://developer.android.com/reference/java/lang/IllegalArgumentException), and
the following message appears in [Logcat](https://developer.android.com/studio/command-line/logcat):  

    PACKAGE_NAME: Targeting S+ (version 31 and above) requires that one of \
    FLAG_IMMUTABLE or FLAG_MUTABLE be specified when creating a PendingIntent.

    Strongly consider using FLAG_IMMUTABLE, only use FLAG_MUTABLE if \
    some functionality depends on the PendingIntent being mutable, e.g. if \
    it needs to be used with inline replies or bubbles.

#### Create immutable pending intents whenever possible

In most cases, your app should create immutable `PendingIntent` objects, as
shown in the following code snippet. If a `PendingIntent` object is immutable,
then other apps cannot modify the intent to adjust the result of invoking the
intent.  

### Kotlin

```kotlin
val pendingIntent = PendingIntent.getActivity(applicationContext,
        REQUEST_CODE, intent,
        /* flags */ PendingIntent.FLAG_IMMUTABLE)
```

### Java

```java
PendingIntent pendingIntent = PendingIntent.getActivity(getApplicationContext(),
        REQUEST_CODE, intent,
        /* flags */ PendingIntent.FLAG_IMMUTABLE);
```

However, certain use cases require mutable `PendingIntent` objects instead:

- Supporting [direct reply actions in
  notifications](https://developer.android.com/training/notify-user/build-notification#reply-action). The direct reply requires a change to the clip data in the PendingIntent object that's associated with the reply. Usually, you request this change by passing `FILL_IN_CLIP_DATA` as a flag to the [`fillIn()`](https://developer.android.com/reference/android/content/Intent#fillIn(android.content.Intent,%20int)) method.
- Associating notifications with the Android Auto framework, using instances of [`CarAppExtender`](https://developer.android.com/reference/androidx/car/app/notification/CarAppExtender).
- Placing conversations in [bubbles](https://developer.android.com/guide/topics/ui/bubbles) using instances of `PendingIntent`. A mutable `PendingIntent` object allows the system to apply the correct flags, such as [`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_MULTIPLE_TASK) and [`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_DOCUMENT).
- Requesting device location information by calling [`requestLocationUpdates()`](https://developer.android.com/reference/android/location/LocationManager#requestLocationUpdates(java.lang.String,%20long,%20float,%20android.app.PendingIntent)) or similar APIs. The mutable `PendingIntent` object allows the system to add intent extras that represent location lifecycle events. These events include a change in location and a provider becoming available.
- Scheduling alarms using [`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager). The mutable `PendingIntent` object allows the system to add the [`EXTRA_ALARM_COUNT`](https://developer.android.com/reference/android/content/Intent#EXTRA_ALARM_COUNT) intent extra. This extra represents the number of times that a repeating alarm has been triggered. By containing this extra, the intent can accurately notify an app as to whether a repeating alarm was triggered multiple times, such as when the device was asleep.

If your app creates a mutable `PendingIntent` object, it's strongly recommended
that you use an [explicit intent](https://developer.android.com/guide/components/intents-filters#ExampleExplicit) and fill in the
[`ComponentName`](https://developer.android.com/reference/android/content/ComponentName). That way, whenever
another app invokes the `PendingIntent` and passes control back to your app, the
same component in your app always starts.

### Use explicit intents within pending intents

To better define how other apps can use your app's pending intents, always
wrap a pending intent around an [explicit intent](https://developer.android.com/guide/components/intents-filters#ExampleExplicit).
To help follow this best practice, do the following:

1. Check that the action, package, and component fields of the base intent are set.
2. Use [`FLAG_IMMUTABLE`](https://developer.android.com/reference/android/app/PendingIntent#FLAG_IMMUTABLE),
   added in Android 6.0 (API level 23), to create pending intents. This flag
   prevents apps that receive a `PendingIntent` from filling in
   unpopulated properties. If your app's `minSdkVersion` is
   `22` or lower, you can provide safety and compatibility together
   using the following code:

   ```kotlin
   if (Build.VERSION.SDK_INT >= 23) {
     // Create a PendingIntent using FLAG_IMMUTABLE.
   } else {
     // Existing code that creates a PendingIntent.
   }
   ```

## Intent resolution

When the system receives an implicit intent to start an activity, it searches for the
best activity for the intent by comparing it to intent filters based on three aspects:

- Action.
- Data (both URI and data type).
- Category.

The following sections describe how intents are matched to the appropriate components
according to the intent filter declaration in an app's manifest file.

### Action test

To specify accepted intent actions, an intent filter can declare zero or more
[`<action>`](https://developer.android.com/guide/topics/manifest/action-element) elements, as shown in the following example:  

```xml
<intent-filter>
    <action android:name="android.intent.action.EDIT" />
    <action android:name="android.intent.action.VIEW" />
    ...
</intent-filter>
```

To pass this filter, the action specified in the [Intent](https://developer.android.com/reference/android/content/Intent)
must match one of the actions listed in the filter.

If the filter does not list any actions, there is nothing for an
intent to match, so all intents fail the test. However, if an [Intent](https://developer.android.com/reference/android/content/Intent)
does not specify an action, it passes the test as long as the filter
contains at least one action.

### Category test

To specify accepted intent categories, an intent filter can declare zero or more
[`<category>`](https://developer.android.com/guide/topics/manifest/category-element) elements, as shown in the following example:  

```xml
<intent-filter>
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    ...
</intent-filter>
```

For an intent to pass the category test, every category in the [Intent](https://developer.android.com/reference/android/content/Intent)
must match a category in the filter. The reverse is not necessary---the intent filter may
declare more categories than are specified in the [Intent](https://developer.android.com/reference/android/content/Intent) and the
[Intent](https://developer.android.com/reference/android/content/Intent) still passes. Therefore, an intent with no categories
always passes this test, regardless of what categories are declared in the filter.

**Note:**
Android automatically applies the [CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category
to all implicit intents passed to [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)) and [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)).
If you want your activity to receive implicit intents, it must
include a category for `"android.intent.category.DEFAULT"` in its intent filters, as
shown in the previous `<intent-filter>` example.

### Data test

To specify accepted intent data, an intent filter can declare zero or more
[`<data>`](https://developer.android.com/guide/topics/manifest/data-element) elements, as shown in the following example:  

```xml
<intent-filter>
    <data android:mimeType="video/mpeg" android:scheme="http" ... />
    <data android:mimeType="audio/mpeg" android:scheme="http" ... />
    ...
</intent-filter>
```

Each [<data>](https://developer.android.com/guide/topics/manifest/data-element)
element can specify a URI structure and a data type (MIME media type).
Each part of the URI is a separate
attribute: `scheme`, `host`, `port`,
and `path`:

`<scheme>://<host>:<port>/<path>`


The following example shows possible values for these attributes:

`content://com.example.project:200/folder/subfolder/etc`

In this URI, the scheme is `content`, the host is `com.example.project`,
the port is `200`, and the path is `folder/subfolder/etc`.

Each of these attributes is optional in a [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) element,
but there are linear dependencies:

- If a scheme is not specified, the host is ignored.
- If a host is not specified, the port is ignored.
- If both the scheme and host are not specified, the path is ignored.

When the URI in an intent is compared to a URI specification in a filter,
it's compared only to the parts of the URI included in the filter. For example:

- If a filter specifies only a scheme, all URIs with that scheme match the filter.
- If a filter specifies a scheme and an authority but no path, all URIs with the same scheme and authority pass the filter, regardless of their paths.
- If a filter specifies a scheme, an authority, and a path, only URIs with the same scheme, authority, and path pass the filter.

**Note:** A path specification can
contain a wildcard asterisk (\*) to require only a partial match of the path name.

The data test compares both the URI and the MIME type in the intent to a URI
and MIME type specified in the filter. The rules are as follows:

1. An intent that contains neither a URI nor a MIME type passes the test only if the filter does not specify any URIs or MIME types.
2. An intent that contains a URI but no MIME type (neither explicit nor inferable from the URI) passes the test only if its URI matches the filter's URI format and the filter likewise does not specify a MIME type.
3. An intent that contains a MIME type but not a URI passes the test only if the filter lists the same MIME type and does not specify a URI format.
4. An intent that contains both a URI and a MIME type (either explicit or inferable from the URI) passes the MIME type part of the test only if that type matches a type listed in the filter. It passes the URI part of the test either if its URI matches a URI in the filter or if it has a `content:` or `file:` URI and the filter does not specify a URI. In other words, a component is presumed to support `content:` and `file:` data if its filter lists *only* a MIME type.


**Note:** If an intent specifies a URI or MIME type, the data test will
fail if there are no `<data>` elements in the `<intent-filter>`.

This last rule, rule (d), reflects the expectation
that components are able to get local data from a file or content provider.
Therefore, their filters can list just a data type and don't need to explicitly
name the `content:` and `file:` schemes.
The following example shows a typical case in which a [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) element
tells Android that the component can get image data from a content
provider and display it:

<br />

```xml
<intent-filter>
    <data android:mimeType="image/*" />
    ...
</intent-filter>
```


Filters that
specify a data type but not a URI are perhaps the most common because most available
data is dispensed by content providers.


Another common configuration is a filter with a scheme and a data type. For
example, a [`<data>`](https://developer.android.com/guide/topics/manifest/data-element)
element like the following tells Android that
the component can retrieve video data from the network in order to perform the action:  

```xml
<intent-filter>
    <data android:scheme="http" android:mimeType="video/*" />
    ...
</intent-filter>
```

### Intent matching

Intents are matched against intent filters not only to discover a target
component to activate, but also to discover something about the set of
components on the device. For example, the Home app populates the app launcher
by finding all the activities with intent filters that specify the
[ACTION_MAIN](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN) action and
[CATEGORY_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER) category.
A match is only successful if the actions and categories in the Intent match
against the filter, as described in the documentation for the [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)
class.

Your application can use intent matching in a manner similar to what the Home app does.
The [PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager) has a set of `query...()`
methods that return all components that can accept a particular intent and
a similar series of `resolve...()` methods that determine the best
component to respond to an intent. For example,
[queryIntentActivities()](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities(android.content.Intent, int)) returns a list of all activities that can perform
the intent passed as an argument, and [queryIntentServices()](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices(android.content.Intent, int)) returns a similar list of services.
Neither method activates the components; they just list the ones that
can respond. There's a similar method,
[queryBroadcastReceivers()](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers(android.content.Intent, int)), for broadcast receivers.