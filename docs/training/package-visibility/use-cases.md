---
title: https://developer.android.com/training/package-visibility/use-cases
url: https://developer.android.com/training/package-visibility/use-cases
source: md.txt
---

This document presents several common use cases in which an app interacts with
other apps. Each section provides guidance on how to accomplish the app's
functionality with limited package visibility, which you need to consider if
your app targets Android 11 (API level 30) or higher.

When an app that targets Android 11 or higher uses an intent to
start an activity in another app, the most straightforward approach is to invoke
the intent and handle the
[`ActivityNotFoundException`](https://developer.android.com/reference/android/content/ActivityNotFoundException)
exception if no app is available.

If part of your app depends on knowing whether the call to
[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent))
can succeed, such as showing a UI, add an element to the
[`<queries>`](https://developer.android.com/guide/topics/manifest/queries-element) element of your app's
manifest. Typically, this is an `<intent>` element.

## Open URLs

This section describes various ways to open URLs in an app that targets
Android 11 or higher.

### Open URLs in a browser or other app

To open a URL, use an intent that contains the
[`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW) intent action, as
described in the guide to [loading a web
URL](https://developer.android.com/guide/components/intents-common#ViewUrl). After you call `startActivity()`
using this intent, one of the following happens:

- The URL opens in a web browser app.
- The URL opens in an app that supports the URL as a [deep
  link](https://developer.android.com/training/app-links/deep-linking).
- A disambiguation dialog appears, which lets the user choose which app opens the URL.
- An `ActivityNotFoundException` occurs because there isn't an app installed on
  the device that can open the URL. (This is unusual.)

  It's recommended that your app catch and handle the
  `ActivityNotFoundException` if it occurs.

Because the `startActivity()` method doesn't require package visibility to
start another application's activity, you don't need to add a `<queries>`
element to your app's manifest or make any changes to an existing `<queries>`
element. This is true for both implicit and explicit intents that open a URL.

#### Check whether a browser is available

In some cases, your app might want to verify that there's at least one browser
available on the device, or that a specific browser is the default browser,
before attempting to open a URL. In those cases, include the following
`<intent>` element as part of the `<queries>` element in your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="https" />
</intent>
```

When you call `queryIntentActivities()` and pass a web intent as an argument,
the returned list includes the available browser apps in some cases. The list
doesn't include browser apps if the user has configured the URL to open in a
non-browser app by default.

### Open URLs in Custom Tabs

[Custom Tabs](https://developers.google.com/web/android/custom-tabs) let an
app customize how the browser looks and feels. You can [open a URL in
a Custom Tab](https://developers.google.com/web/android/custom-tabs/implementation-guide#opening_a_custom_tab)
without needing to add or change the `<queries>` element in your app manifest.

However, you might want to [check whether the device has a browser that supports
Custom Tabs](https://developers.google.com/web/android/custom-tabs/implementation-guide#opening_a_custom_tab)
or select a specific browser to launch with Custom Tabs using
[`CustomTabsClient.getPackageName()`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsClient#getPackageName(android.content.Context,%2520java.util.List%3Cjava.lang.String%3E)).
In those cases, include the following `<intent>` element as part of the
`<queries>` element in your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.support.customtabs.action.CustomTabsService" />
</intent>
```
| **Note:** The `<intent>` element shown in the preceding code snippet isn't necessary if your manifest already includes the `<intent>` element shown in the section about how to [check whether a browser is available](https://developer.android.com/training/package-visibility/use-cases#check-browser-available).

### Let non-browser apps handle URLs

Even if your app can open URLs using Custom Tabs, it's recommended that you
let a non-browser app open a URL if possible. To provide this
capability in your app, attempt a call to `startActivity()` using an intent
that sets the
[`FLAG_ACTIVITY_REQUIRE_NON_BROWSER`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_REQUIRE_NON_BROWSER)
intent flag. If the system throws an `ActivityNotFoundException`, your app can
then open the URL in a Custom Tab.

If an intent includes this flag, a call to `startActivity()` causes an
`ActivityNotFoundException` to be thrown when either of the following
conditions occurs:

- The call would have launched a browser app directly.
- The call would have shown the user a disambiguation dialog where the only options are browser apps.

The following code snippet shows how to update your logic to use the
`FLAG_ACTIVITY_REQUIRE_NON_BROWSER` intent flag:  

### Kotlin

```kotlin
try {
    val intent = Intent(ACTION_VIEW, Uri.parse(url)).apply {
        // The URL should either launch directly in a non-browser app (if it's
        // the default) or in the disambiguation dialog.
        addCategory(CATEGORY_BROWSABLE)
        flags = FLAG_ACTIVITY_NEW_TASK or FLAG_ACTIVITY_REQUIRE_NON_BROWSER
    }
    startActivity(intent)
} catch (e: ActivityNotFoundException) {
    // Only browser apps are available, or a browser is the default.
    // So you can open the URL directly in your app, for example in a
    // Custom Tab.
    openInCustomTabs(url)
}
```

### Java

```java
try {
    Intent intent = new Intent(ACTION_VIEW, Uri.parse(url));
    // The URL should either launch directly in a non-browser app (if it's the
    // default) or in the disambiguation dialog.
    intent.addCategory(CATEGORY_BROWSABLE);
    intent.setFlags(FLAG_ACTIVITY_NEW_TASK | FLAG_ACTIVITY_REQUIRE_NON_BROWSER);
    startActivity(intent);
} catch (ActivityNotFoundException e) {
    // Only browser apps are available, or a browser is the default.
    // So you can open the URL directly in your app, for example in a
    // Custom Tab.
    openInCustomTabs(url);
}
```

### Avoid a disambiguation dialog

If you want to avoid showing the disambiguation dialog that users might see when
they open a URL, and instead prefer to handle the URL yourself in these
situations, you can use an intent that sets the
[`FLAG_ACTIVITY_REQUIRE_DEFAULT`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_REQUIRE_DEFAULT)
intent flag.

If an intent includes this flag, a call to `startActivity()` causes an
`ActivityNotFoundException` to be thrown when the call would have shown a
disambiguation dialog to the user.

If an intent includes both this flag and the
[`FLAG_ACTIVITY_REQUIRE_NON_BROWSER`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_REQUIRE_NON_BROWSER)
intent flag, a call to `startActivity()` causes an `ActivityNotFoundException`
to be thrown when either of the following conditions occurs:

- The call would have launched the browser app directly.
- The call would have shown a disambiguation dialog to the user.

The following code snippet shows how to use the `FLAG_ACTIVITY_REQUIRE_NON_BROWSER`
and `FLAG_ACTIVITY_REQUIRE_DEFAULT` flags together:  

### Kotlin

```kotlin
val url = URL_TO_LOAD
try {
    // For this intent to be invoked, the system must directly launch a
    // non-browser app.
    val intent = Intent(ACTION_VIEW, Uri.parse(url)).apply {
        addCategory(CATEGORY_BROWSABLE)
        flags = FLAG_ACTIVITY_NEW_TASK or FLAG_ACTIVITY_REQUIRE_NON_BROWSER or
                FLAG_ACTIVITY_REQUIRE_DEFAULT
    }
    startActivity(intent)
} catch (e: ActivityNotFoundException) {
    // This code executes in one of the following cases:
    // 1. Only browser apps can handle the intent.
    // 2. The user has set a browser app as the default app.
    // 3. The user hasn't set any app as the default for handling this URL.
    openInCustomTabs(url)
}
```

### Java

```java
String url = URL_TO_LOAD;
try {
    // For this intent to be invoked, the system must directly launch a
    // non-browser app.
    Intent intent = new Intent(ACTION_VIEW, Uri.parse(url));
    intent.addCategory(CATEGORY_BROWSABLE);
    intent.setFlags(FLAG_ACTIVITY_NEW_TASK | FLAG_ACTIVITY_REQUIRE_NON_BROWSER |
            FLAG_ACTIVITY_REQUIRE_DEFAULT);
    startActivity(intent);
} catch (ActivityNotFoundException e) {
    // This code executes in one of the following cases:
    // 1. Only browser apps can handle the intent.
    // 2. The user has set a browser app as the default app.
    // 3. The user hasn't set any app as the default for handling this URL.
    openInCustomTabs(url);
}
```

## Open a file

If your app handles files or attachments, such as checking whether a device can
open a given file, it's usually easiest to try to start an activity that can
handle the file. To do so, use an intent that includes the `ACTION_VIEW` intent
action and the URI that represents the specific file. If no app is available on
the device, your app can catch the `ActivityNotFoundException`. In your
exception-handling logic, you can either show an error or try to handle the file
yourself.

If your app must know in advance whether another app can open a given file,
include the `<intent>` element in the following code snippet as part of the
`<queries>` element in your manifest. Include the file type if you already know
what it is at compile time.  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.intent.action.VIEW" />
  <!-- If you don't know the MIME type in advance, set "mimeType" to "*/*". -->
  <data android:mimeType="application/pdf" />
</intent>
```

You can then check whether an app is available by calling `resolveActivity()`
with your intent.

### Grant URI access

**Note:** Declaring URI access permissions as described in this section
is required for apps that target Android 11 (API level 30) or higher and
recommended for all apps, regardless of their target SDK version and whether
they [export](https://developer.android.com/guide/topics/manifest/provider-element#exported)
their content providers.

For apps that target Android 11 or higher to
access the content URI, your app's intent must declare [URI access
permissions](https://developer.android.com/guide/topics/providers/content-provider-basics#getting-access-with-temporary-permissions)
by setting one or both of the following intent flags:
[`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION)
and
[`FLAG_GRANT_WRITE_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_WRITE_URI_PERMISSION).

On Android 11 and higher, the URI access permissions give the
following capabilities to the app that receives the intent:

- Read from, or write to, the data that the content URI represents, depending on the given URI permissions.
- Gain visibility into the app containing the content provider that matches the URI authority. The app that contains the content provider might be different from the app that sends the intent.

The following code snippet demonstrates how to add a URI permissions intent flag
so that another app that targets Android 11 or higher can view
the data in the content URI:  

### Kotlin

```kotlin
val shareIntent = Intent(Intent.ACTION_VIEW).apply {
    flags = Intent.FLAG_GRANT_READ_URI_PERMISSION
    data = CONTENT_URI_TO_SHARE_WITH_OTHER_APP
}
```

### Java

```java
Intent shareIntent = new Intent(Intent.ACTION_VIEW);
shareIntent.setFlags(FLAG_GRANT_READ_URI_PERMISSION);
shareIntent.setData(CONTENT_URI_TO_SHARE_WITH_OTHER_APP);
```

## Connect to services

If your app needs to interact with a service that isn't [visible
automatically](https://developer.android.com/training/package-visibility/automatic), you can declare the
appropriate intent action within a `<queries>` element. The following sections
give examples using commonly accessed services.

### Connect to a text-to-speech engine

If your app interacts with a text-to-speech (TTS) engine, include the following
`<intent>` element as part of the `<queries>` element in your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.intent.action.TTS_SERVICE" />
</intent>
```

### Connect to a speech recognition service

If your app interacts with a speech recognition service, include the following
`<intent>` element as part of the `<queries>` element in your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.speech.RecognitionService" />
</intent>
```

### Connect to media browser services

If your app is a [client media browser
app](https://developer.android.com/guide/topics/media-apps/audio-app/building-a-mediabrowser-client), include
the following `<intent>` element as part of the `<queries>` element in your
manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.media.browse.MediaBrowserService" />
</intent>
```

## Provide custom functionality

If your app needs to perform customizable actions or show customizable
information based on its interactions with other apps, you can represent that
custom behavior using [intent filter
signatures](https://developer.android.com/training/package-visibility/declaring#intent-filter-signature) as
part of the `<queries>` element in your manifest. The following sections provide
detailed guidance for several common scenarios.

### Query for SMS apps

If your app needs information about the set of SMS apps that are installed on a
device, for example to check which app is the device's default SMS handler,
include the following `<intent>` element as part of the `<queries>` element in
your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.intent.action.SENDTO"/>
  <data android:scheme="smsto" android:host="*" />
</intent>
```

### Create a custom sharesheet

Whenever possible, use a [system-provided
sharesheet](https://developer.android.com/training/sharing/send#why-to-use-system-sharesheet). Alternatively,
include the following `<intent>` element as part of the `<queries>` element in
your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.intent.action.SEND" />
  <!-- Replace with the MIME type that your app works with, if needed. -->
  <data android:mimeType="image/jpeg" />
</intent>
```

The process of building the sharesheet in your app's logic, such as the call to
`queryIntentActivities()`, otherwise remains unchanged compared to
versions of Android earlier than Android 11.

### Show custom text selection actions

When users select text in your app, a [text selection
toolbar](https://material.io/design/platform-guidance/android-text-selection-toolbar)
shows the set of possible operations to perform on the selected text. If this
toolbar shows custom actions from other apps, include the following
`<intent>` element as part of the `<queries>` element in your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<intent>
  <action android:name="android.intent.action.PROCESS_TEXT" />
  <data android:mimeType="text/plain" />
</intent>
```

### Show custom data rows for a contact

Apps can [add custom data
rows](https://developer.android.com/guide/topics/providers/contacts-provider#CustomData) to the Contacts
Provider. For a contacts app to show this custom data, it needs to be
able to do the following:

1. Read the `contacts.xml` file from the other apps.
2. Load an icon corresponding to the custom MIME type.

If your app is a contacts app, include the following `<intent>` elements as part
of the `<queries>` element in your manifest:  

```xml
<!-- Place inside the <queries> element. -->
<!-- Lets the app read the contacts.xml file from other apps. -->
<intent>
  <action android:name="android.accounts.AccountAuthenticator" />
</intent>
<!-- Lets the app load an icon corresponding to the custom MIME type. -->
<intent>
  <action android:name="android.intent.action.VIEW" />
  <data android:scheme="content" android:host="com.android.contacts"
        android:mimeType="vnd.android.cursor.item/*" />
</intent>
```