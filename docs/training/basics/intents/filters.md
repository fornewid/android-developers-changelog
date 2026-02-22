---
title: https://developer.android.com/training/basics/intents/filters
url: https://developer.android.com/training/basics/intents/filters
source: md.txt
---

If your app can perform an action that might be useful to another app,
prepare it to respond to action requests by specifying
the appropriate intent filter in your activity.

For example, if you
build a social app that can share messages or photos with the user's friends,
support the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) intent.
Then, when users initiate a "share" action from another app, your app appears as an option in the
chooser dialog (also known as the *disambiguation dialog*), as shown in figure 1.
![](https://developer.android.com/static/images/training/basics/intent-chooser.png)

**Figure 1.** The chooser dialog.

To let other apps start your activity in this way, you need to add an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element in your manifest file for the corresponding [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) element.

When your app is installed on a device, the system identifies your intent
filters and adds the information to an internal catalog of intents supported by all installed apps.
When an app calls [startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)) or [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int))
with an implicit intent, the system checks for activities that can respond to the
intent.

## Add an intent filter

To properly define which intents your activity can handle, make each intent filter you add
as specific as possible in terms of the type of action and data the activity
accepts.

The system might send a given [Intent](https://developer.android.com/reference/android/content/Intent) to an activity if that activity has
an intent filter that fulfills the following criteria of the `Intent` object:

Action
:   A string naming the action to perform. Usually one of the platform-defined values, such
    as [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) or [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW).

    Specify this in your intent filter with the [`<action>`](https://developer.android.com/guide/topics/manifest/action-element) element.
    The value you specify in this element must be the full string name for the action, instead of the
    API constant, as shown in the examples on this page.

Data

:   A description of the data associated with the intent.<br />

    Specify this in your intent filter with the [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) element. Using one
    or more attributes in this element, you can specify the MIME type, a URI prefix,
    a URI scheme, or a combination of these and others that indicate the data type
    accepted.

    **Note:** If you don't need to declare specifics about the data
    [Uri](https://developer.android.com/reference/android/net/Uri), such as when your activity handles
    other kind of "extra" data, instead of a URI, specify only the `android:mimeType` attribute to declare the type of
    data your activity handles, such as `text/plain` or `image/jpeg`.

Category
:   Provides an additional way to characterize the activity handling the intent, usually related
    to the user gesture or location from which it's started. There are several different categories
    supported by the system, but most are rarely used. However, all implicit intents are defined with
    [CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) by default.

    Specify this in your intent filter with the [`<category>`](https://developer.android.com/guide/topics/manifest/category-element)
    element.

In your intent filter, you can declare which criteria your activity accepts
by declaring each of them with corresponding XML elements nested in the [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element.

For example, here's an activity with an intent filter that handles the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) intent when the data type is either text or an image:  

```xml
<activity android:name="ShareActivity">
    <intent-filter>
        <action android:name="android.intent.action.SEND"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:mimeType="text/plain"/>
        <data android:mimeType="image/*"/>
    </intent-filter>
</activity>
```

**Tip:** If you want the icon in the chooser dialog to be different
from your activity's default icon, add `android:icon` in the [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element.

Each incoming intent specifies only one action and one data type, but it's OK to declare multiple
instances of the [`<action>`](https://developer.android.com/guide/topics/manifest/action-element), [`<category>`](https://developer.android.com/guide/topics/manifest/category-element), and [`<data>`](https://developer.android.com/guide/topics/manifest/data-element) elements in each
[`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element).

If any two pairs of action and data are mutually exclusive in
their behaviors, create separate intent filters to specify which actions are acceptable
when paired with which data types.

For example, suppose your activity handles both text and images for both the [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) and [ACTION_SENDTO](https://developer.android.com/reference/android/content/Intent#ACTION_SENDTO) intents. In this case, you must define two separate
intent filters for the two actions, because an `ACTION_SENDTO` intent must use the data [Uri](https://developer.android.com/reference/android/net/Uri) to specify
the recipient's address using the `send` or `sendto` URI scheme. This is shown in the following example:  

```xml
<activity android:name="ShareActivity">
    <!-- Filter for sending text; accepts SENDTO action with sms URI schemes -->
    <intent-filter>
        <action android:name="android.intent.action.SENDTO"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:scheme="sms" />
        <data android:scheme="smsto" />
    </intent-filter>
    <!-- Filter for sending text or images; accepts SEND action and text or image data -->
    <intent-filter>
        <action android:name="android.intent.action.SEND"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:mimeType="image/*"/>
        <data android:mimeType="text/plain"/>
    </intent-filter>
</activity>
```

**Note:** To receive implicit intents, you must include the
[CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT) category in the intent filter. The methods [startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)) and [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)) treat all intents as if they
declared the `CATEGORY_DEFAULT` category. If you don't declare it
in your intent filter, no implicit intents resolve to your activity.

For more information about sending and receiving [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)
intents that perform social sharing behaviors, see [Receiving simple data from other apps](https://developer.android.com/training/sharing/receive).
You can also find useful information about sharing data in
[Sharing simple data](https://developer.android.com/training/sharing) and
[Sharing files](https://developer.android.com/training/secure-file-sharing).

## Handle the intent in your activity

To decide what action to take in your activity, read the
[Intent](https://developer.android.com/reference/android/content/Intent) that is used to start it.

As your activity starts, call [getIntent()](https://developer.android.com/reference/android/app/Activity#getIntent()) to retrieve the
`Intent` that started the activity. You can do so at any time during the
lifecycle of the activity, but you generally do so during early callbacks, such as
[onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) or [onStart()](https://developer.android.com/reference/android/app/Activity#onStart()).

This is shown in the following example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    setContentView(R.layout.main)

    val data: Uri? = intent?.data

    // Figure out what to do based on the intent type
    if (intent?.type?.startsWith("image/") == true) {
        // Handle intents with image data
    } else if (intent?.type == "text/plain") {
        // Handle intents with text
    }
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    setContentView(R.layout.main);

    // Get the intent that started this activity
    Intent intent = getIntent();
    Uri data = intent.getData();

    // Figure out what to do based on the intent type
    if (intent.getType().indexOf("image/") != -1) {
        // Handle intents with image data
    } else if (intent.getType().equals("text/plain")) {
        // Handle intents with text
    }
}
```

## Return a result

If you want to return a result to the activity that invoked yours, call [setResult()](https://developer.android.com/reference/android/app/Activity#setResult(int, android.content.Intent)) to specify the result code and result [Intent](https://developer.android.com/reference/android/content/Intent). When your operation is done and the user returns to the original
activity, call [finish()](https://developer.android.com/reference/android/app/Activity#finish()) to
close and destroy your activity. This is shown in the following example:  

### Kotlin

```kotlin
// Create intent to deliver some kind of result data
Intent("com.example.RESULT_ACTION", Uri.parse("content://result_uri")).also { result ->
    setResult(Activity.RESULT_OK, result)
}
finish()
```

### Java

```java
// Create intent to deliver some kind of result data
Intent result = new Intent("com.example.RESULT_ACTION", Uri.parse("content://result_uri"));
setResult(Activity.RESULT_OK, result);
finish();
```

You must always specify a result code with the result. Generally, it's either [RESULT_OK](https://developer.android.com/reference/android/app/Activity#RESULT_OK) or [RESULT_CANCELED](https://developer.android.com/reference/android/app/Activity#RESULT_CANCELED). You can then
provide additional data with an [Intent](https://developer.android.com/reference/android/content/Intent), as necessary.

**Note:** The result is set to
[RESULT_CANCELED](https://developer.android.com/reference/android/app/Activity#RESULT_CANCELED)
by default. So, if the user taps the Back
button before completing the action and before you set the result, the original activity receives
the "canceled" result.

If you simply need to return an integer that indicates one of several result options, you can set
the result code to any value higher than 0. If you use the result code to deliver an integer and you
have no need to include the [Intent](https://developer.android.com/reference/android/content/Intent),
you can call [setResult()](https://developer.android.com/reference/android/app/Activity#setResult(int))
and pass only a result code:  

### Kotlin

```kotlin
setResult(RESULT_COLOR_RED)
finish()
```

### Java

```java
setResult(RESULT_COLOR_RED);
finish();
```

In this case, there might be only a handful of possible results, so the result code is a locally
defined integer (greater than 0). This works well when you're returning a result to an activity
in your own app, because the activity that receives the result can reference the public
constant to determine the value of the result code.

**Note:** There's no need to check whether your activity was started
with [startActivity()](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)) or [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)). Simply call [setResult()](https://developer.android.com/reference/android/app/Activity#setResult(int, android.content.Intent)) if the intent that started your activity
might expect a result. If the originating activity called `startActivityForResult()`, then the system delivers it
the result you supply to `setResult()`; otherwise, the result is ignored.