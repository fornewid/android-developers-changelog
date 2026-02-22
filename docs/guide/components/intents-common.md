---
title: https://developer.android.com/guide/components/intents-common
url: https://developer.android.com/guide/components/intents-common
source: md.txt
---

An intent lets you start an activity in another app by describing an
action you'd like to perform, such as "view a map" or "take a
picture," in an [Intent](https://developer.android.com/reference/android/content/Intent) object. This type of intent
is called an *implicit* intent because it doesn't specify the app
component to start, but instead specifies an *action* and provides
some *data* with which to perform the action.


When you call [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))
or [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)) and pass it an implicit intent, the system
[resolves
the intent](https://developer.android.com/guide/components/intents-filters#Resolution) to an app that can handle the intent and starts its
corresponding [Activity](https://developer.android.com/reference/android/app/Activity). If there's more than one app
that can handle the intent, the system presents the user with a dialog to
pick which app to use.


This page describes several implicit intents that you can use to perform
common actions, organized by the type of app that handles the intent. Each
section also shows how you can create an [intent
filter](https://developer.android.com/guide/components/intents-filters#Receiving) to advertise your app's ability to perform the action.


**Caution:** If there are no apps on the device that can
receive an implicit intent, an app crashes when it calls [startActivity()](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)). To first verify that
an app exists to receive the intent, call [resolveActivity()](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager)) on your [Intent](https://developer.android.com/reference/android/content/Intent) object. If the result is non-null, there is at least
one app that can handle the intent, and it's safe to call `startActivity()`. If the result is
null, don't use the intent and, if possible, disable the
feature that invokes the intent.


If you're not familiar with how to create intents or intent filters, first read [Intents and Intent
Filters](https://developer.android.com/guide/components/intents-filters).


To learn how to fire the intents listed on this page from your development
host, see the [Verify intents with the Android Debug
Bridge](https://developer.android.com/guide/components/intents-common#AdbIntents) section.

#### Google Voice Actions


[Google Voice
Actions](https://developers.google.com/voice-actions/) fires some of the intents listed on this page in response to
voice commands. For more information, see [Get Started with System Voice Actions](https://developers.google.com/voice-actions/system/#system_actions_reference).

## Alarm clock

The following are common actions for alarm clock apps, including the information you need
to create an intent filter to advertise your app's ability to perform each action.

### Create an alarm

[![](https://developer.android.com/static/guide/components/images/voice-icon.png)](https://developers.google.com/voice-actions/system/#system_actions_reference)


Google Voice Actions

- "set an alarm for 7 am"

To create a new alarm, use the [ACTION_SET_ALARM](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_ALARM)
action and specify alarm details such as the time and message using the following extras.

**Note:** Only the hour, minutes, and message extras are available
in Android 2.3 (API level 9) and lower. The other extras are available in higher versions of the
platform.

**Action**
:   [ACTION_SET_ALARM](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_ALARM)

**Data URI**
:   None

**MIME Type**
:   None

**Extras**
:

    [EXTRA_HOUR](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_HOUR)
    :   The hour for the alarm.

    [EXTRA_MINUTES](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_MINUTES)
    :   The minutes for the alarm.

    [EXTRA_MESSAGE](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_MESSAGE)
    :   A custom message to identify the alarm.

    [EXTRA_DAYS](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_DAYS)
    :   An [ArrayList](https://developer.android.com/reference/java/util/ArrayList) including each week day on which this alarm
        repeats. Each day must be declared with an integer from the [Calendar](https://developer.android.com/reference/java/util/Calendar)
        class, such as [MONDAY](https://developer.android.com/reference/java/util/Calendar#MONDAY).

        For a one-time alarm, don't specify this extra.

    [EXTRA_RINGTONE](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_RINGTONE)
    :   A `content:` URI specifying a ringtone to use with the alarm, or [VALUE_RINGTONE_SILENT](https://developer.android.com/reference/android/provider/AlarmClock#VALUE_RINGTONE_SILENT) for no ringtone.

        To use the default ringtone, don't specify this extra.

    [EXTRA_VIBRATE](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_VIBRATE)
    :   A boolean specifying whether to vibrate for this alarm.

    [EXTRA_SKIP_UI](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_SKIP_UI)
    :   A boolean specifying whether the responding app must skip its UI when setting the alarm.
        If true, the app must bypass any confirmation UI and set the specified alarm.

**Example intent:**  

### Kotlin

```kotlin
fun createAlarm(message: String, hour: Int, minutes: Int) {
    val intent = Intent(AlarmClock.ACTION_SET_ALARM).apply {
        putExtra(AlarmClock.EXTRA_MESSAGE, message)
        putExtra(AlarmClock.EXTRA_HOUR, hour)
        putExtra(AlarmClock.EXTRA_MINUTES, minutes)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void createAlarm(String message, int hour, int minutes) {
    Intent intent = new Intent(AlarmClock.ACTION_SET_ALARM)
            .putExtra(AlarmClock.EXTRA_MESSAGE, message)
            .putExtra(AlarmClock.EXTRA_HOUR, hour)
            .putExtra(AlarmClock.EXTRA_MINUTES, minutes);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```  
**Note:**

To invoke the [ACTION_SET_ALARM](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_ALARM) intent, your app must have the
[SET_ALARM](https://developer.android.com/reference/android/Manifest.permission#SET_ALARM) permission:  

```xml
<uses-permission android:name="com.android.alarm.permission.SET_ALARM" />
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.SET_ALARM" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

### Create a timer

[![](https://developer.android.com/static/guide/components/images/voice-icon.png)](https://developers.google.com/voice-actions/system/#system_actions_reference)


Google Voice Actions

- "set timer for 5 minutes"


To create a countdown timer, use the [ACTION_SET_TIMER](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_TIMER) action and specify timer
details such as the duration using the following extras.

**Note:** This intent is available
in Android 4.4 (API level 19) and higher.

**Action**
:   [ACTION_SET_TIMER](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_TIMER)

**Data URI**
:   None

**MIME Type**
:   None

**Extras**
:

    [EXTRA_LENGTH](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_LENGTH)
    :   The length of the timer in seconds.

    [EXTRA_MESSAGE](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_MESSAGE)
    :   A custom message to identify the timer.

    [EXTRA_SKIP_UI](https://developer.android.com/reference/android/provider/AlarmClock#EXTRA_SKIP_UI)
    :   A boolean specifying whether the responding app must skip its UI when setting the timer.
        If true, the app must bypass any confirmation UI and start the specified timer.

**Example intent:**  

### Kotlin

```kotlin
fun startTimer(message: String, seconds: Int) {
    val intent = Intent(AlarmClock.ACTION_SET_TIMER).apply {
        putExtra(AlarmClock.EXTRA_MESSAGE, message)
        putExtra(AlarmClock.EXTRA_LENGTH, seconds)
        putExtra(AlarmClock.EXTRA_SKIP_UI, true)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void startTimer(String message, int seconds) {
    Intent intent = new Intent(AlarmClock.ACTION_SET_TIMER)
            .putExtra(AlarmClock.EXTRA_MESSAGE, message)
            .putExtra(AlarmClock.EXTRA_LENGTH, seconds)
            .putExtra(AlarmClock.EXTRA_SKIP_UI, true);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```  
**Note:**

To invoke the [ACTION_SET_TIMER](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SET_TIMER) intent, your app must have the
[SET_ALARM](https://developer.android.com/reference/android/Manifest.permission#SET_ALARM) permission:  

```xml
<uses-permission android:name="com.android.alarm.permission.SET_ALARM" />
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.SET_TIMER" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

### Show all alarms

To show the list of alarms, use the [ACTION_SHOW_ALARMS](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SHOW_ALARMS)
action.

Although not many apps invoke this intent, as it's primarily used by system apps,
any app that behaves as an alarm clock can implement
this intent filter and respond by showing the list of current alarms.

**Note:** This intent is available
in Android 4.4 (API level 19) and higher.

**Action**
:   [ACTION_SHOW_ALARMS](https://developer.android.com/reference/android/provider/AlarmClock#ACTION_SHOW_ALARMS)

**Data URI**
:   None

**MIME Type**
:   None

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.SHOW_ALARMS" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## Calendar

Adding an event is a common action for calendar apps.
Create an intent filter to advertise your app's ability to perform this action using the
information in the following section.

### Add a calendar event

To add a new event to the user's calendar, use the
[ACTION_INSERT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT)
action and specify the data URI using
[Events.CONTENT_URI](https://developer.android.com/reference/android/provider/CalendarContract.Events#CONTENT_URI).
You can then specify various event details using the following extras.

**Action**
:   [ACTION_INSERT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT)

**Data URI**
:   [Events.CONTENT_URI](https://developer.android.com/reference/android/provider/CalendarContract.Events#CONTENT_URI)

**MIME Type**
:   `"vnd.android.cursor.dir/event"`

**Extras**
:

    [EXTRA_EVENT_ALL_DAY](https://developer.android.com/reference/android/provider/CalendarContract#EXTRA_EVENT_ALL_DAY)
    :   A boolean specifying whether this is an all-day event.

    [EXTRA_EVENT_BEGIN_TIME](https://developer.android.com/reference/android/provider/CalendarContract#EXTRA_EVENT_BEGIN_TIME)
    :   The start time of the event (milliseconds since epoch).

    [EXTRA_EVENT_END_TIME](https://developer.android.com/reference/android/provider/CalendarContract#EXTRA_EVENT_END_TIME)
    :   The end time of the event (milliseconds since epoch).

    [TITLE](https://developer.android.com/reference/android/provider/CalendarContract.EventsColumns#TITLE)
    :   The event title.

    [DESCRIPTION](https://developer.android.com/reference/android/provider/CalendarContract.EventsColumns#DESCRIPTION)
    :   The event description.

    [EVENT_LOCATION](https://developer.android.com/reference/android/provider/CalendarContract.EventsColumns#EVENT_LOCATION)
    :   The event location.

    [EXTRA_EMAIL](https://developer.android.com/reference/android/content/Intent#EXTRA_EMAIL)
    :   A comma-separated list of email addresses that specify the invitees.

    Many more event details can be specified using the constants defined in the
    [CalendarContract.EventsColumns](https://developer.android.com/reference/android/provider/CalendarContract.EventsColumns) class.

**Example intent:**  

### Kotlin

```kotlin
fun addEvent(title: String, location: String, begin: Long, end: Long) {
    val intent = Intent(Intent.ACTION_INSERT).apply {
        data = Events.CONTENT_URI
        putExtra(Events.TITLE, title)
        putExtra(Events.EVENT_LOCATION, location)
        putExtra(CalendarContract.EXTRA_EVENT_BEGIN_TIME, begin)
        putExtra(CalendarContract.EXTRA_EVENT_END_TIME, end)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void addEvent(String title, String location, long begin, long end) {
    Intent intent = new Intent(Intent.ACTION_INSERT)
            .setData(Events.CONTENT_URI)
            .putExtra(Events.TITLE, title)
            .putExtra(Events.EVENT_LOCATION, location)
            .putExtra(CalendarContract.EXTRA_EVENT_BEGIN_TIME, begin)
            .putExtra(CalendarContract.EXTRA_EVENT_END_TIME, end);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.INSERT" />
        <data android:mimeType="vnd.android.cursor.dir/event" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## Camera

The following are common actions for camera apps, including the information you need
to create an intent filter to advertise your app's ability to perform each action.

### Capture a picture or video and return it

To open a camera app and receive the resulting photo or video, use the [ACTION_IMAGE_CAPTURE](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE) or [ACTION_VIDEO_CAPTURE](https://developer.android.com/reference/android/provider/MediaStore#ACTION_VIDEO_CAPTURE) action. Also specify the URI location where you'd
like the camera to save the photo or video, in the [EXTRA_OUTPUT](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_OUTPUT)
extra.

**Action**
:   [ACTION_IMAGE_CAPTURE](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE) or  

    [ACTION_VIDEO_CAPTURE](https://developer.android.com/reference/android/provider/MediaStore#ACTION_VIDEO_CAPTURE)

**Data URI Scheme**
:   None

**MIME Type**
:   None

**Extras**
:

    [EXTRA_OUTPUT](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_OUTPUT)
    :   The URI location where the camera app saves the photo or
        video file (as a [Uri](https://developer.android.com/reference/android/net/Uri) object).

When the camera app successfully returns
focus to your activity---in other words, your app receives the [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)) callback---you
can access the photo or video at the URI you specified
with the [EXTRA_OUTPUT](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_OUTPUT) value.

**Note:** When you use [ACTION_IMAGE_CAPTURE](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE)
to capture a photo, the camera might also return a
downscaled copy, or thumbnail, of the photo in the result [Intent](https://developer.android.com/reference/android/content/Intent), saved as a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) in an extra field named
`"data"`.

**Example intent:**  

### Kotlin

```kotlin
const val REQUEST_IMAGE_CAPTURE = 1
val locationForPhotos: Uri = ...

fun capturePhoto(targetFilename: String) {
    val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE).apply {
        putExtra(MediaStore.EXTRA_OUTPUT, Uri.withAppendedPath(locationForPhotos, targetFilename))
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_CAPTURE)
    }
}

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
    if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == Activity.RESULT_OK) {
        val thumbnail: Bitmap = data.getParcelableExtra("data")
        // Do other work with full size photo saved in locationForPhotos.
        ...
    }
}
```

### Java

```java
static final int REQUEST_IMAGE_CAPTURE = 1;
static final Uri locationForPhotos;

public void capturePhoto(String targetFilename) {
    Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    intent.putExtra(MediaStore.EXTRA_OUTPUT,
            Uri.withAppendedPath(locationForPhotos, targetFilename));
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_CAPTURE);
    }
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
        Bitmap thumbnail = data.getParcelableExtra("data");
        // Do other work with full size photo saved in locationForPhotos.
        ...
    }
}
```

To do this when working on Android 12 (API level 31) or higher, refer to the following intent example.

**Example intent:**  

### Kotlin

```kotlin
val REQUEST_IMAGE_CAPTURE = 1

private fun dispatchTakePictureIntent() {
    val takePictureIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
    try {
        startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
    } catch (e: ActivityNotFoundException) {
        // Display error state to the user.
    }
}
```

### Java

```java
static final int REQUEST_IMAGE_CAPTURE = 1;

private void dispatchTakePictureIntent() {
    Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    try {
        startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
    } catch (ActivityNotFoundException e) {
        // Display error state to the user.
    }
}
</section></div>
```

For more information about how to use this intent to capture a photo, including
how to create an appropriate [Uri](https://developer.android.com/reference/android/net/Uri) for the output location, read
[Take photos](https://developer.android.com/training/camera-deprecated/photobasics) or
[Take videos](https://developer.android.com/training/camera-deprecated/videobasics).

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.media.action.IMAGE_CAPTURE" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```


When handling this intent, have your activity check for the [EXTRA_OUTPUT](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_OUTPUT) extra in the incoming [Intent](https://developer.android.com/reference/android/content/Intent), then save the captured image or video at the
location specified by that extra and call [setResult()](https://developer.android.com/reference/android/app/Activity#setResult(int, android.content.Intent)) with an `Intent` that includes a compressed thumbnail in an extra
named `"data"`.

### Start a camera app in still image mode

[![](https://developer.android.com/static/guide/components/images/voice-icon.png)](https://developers.google.com/voice-actions/system/#system_actions_reference)


Google Voice Actions

- "take a picture"

To open a camera app in still image mode, use the [INTENT_ACTION_STILL_IMAGE_CAMERA](https://developer.android.com/reference/android/provider/MediaStore#INTENT_ACTION_STILL_IMAGE_CAMERA) action.

**Action**
:   [INTENT_ACTION_STILL_IMAGE_CAMERA](https://developer.android.com/reference/android/provider/MediaStore#INTENT_ACTION_STILL_IMAGE_CAMERA)

**Data URI Scheme**
:   None

**MIME Type**
:   None

**Extras**
:   None

**Example intent:**  

### Kotlin

```kotlin
private fun dispatchTakePictureIntent() {
    val takePictureIntent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
    try {
        startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE)
    } catch (e: ActivityNotFoundException) {
        // Display error state to the user.
    }
}
```

### Java

```java
public void capturePhoto(String targetFilename) {
    Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    intent.putExtra(MediaStore.EXTRA_OUTPUT,
            Uri.withAppendedPath(locationForPhotos, targetFilename));
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_CAPTURE);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.media.action.STILL_IMAGE_CAMERA" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

### Start a camera app in video mode

[![](https://developer.android.com/static/guide/components/images/voice-icon.png)](https://developers.google.com/voice-actions/system/#system_actions_reference)


Google Voice Actions

- "record a video"

To open a camera app in video mode, use the [INTENT_ACTION_VIDEO_CAMERA](https://developer.android.com/reference/android/provider/MediaStore#INTENT_ACTION_VIDEO_CAMERA) action.

**Action**
:   [INTENT_ACTION_VIDEO_CAMERA](https://developer.android.com/reference/android/provider/MediaStore#INTENT_ACTION_VIDEO_CAMERA)

**Data URI Scheme**
:   None

**MIME Type**
:   None

**Extras**
:   None

**Example intent:**  

### Kotlin

```kotlin
fun capturePhoto() {
    val intent = Intent(MediaStore.INTENT_ACTION_VIDEO_CAMERA)
    if (intent.resolveActivity(packageManager) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_CAPTURE)
    }
}
```

### Java

```java
public void capturePhoto() {
    Intent intent = new Intent(MediaStore.INTENT_ACTION_VIDEO_CAMERA);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_CAPTURE);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.media.action.VIDEO_CAMERA" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## Contacts/people app

The following are common actions for contacts management apps, including the information you need
to create an intent filter to advertise your app's ability to perform each action.

### Select a contact

To have the user select a contact and provide your app access to all the contact information,
use the [ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK) action and specify the MIME type to
[Contacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_TYPE).

The result [Intent](https://developer.android.com/reference/android/content/Intent) delivered to your [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)) callback contains the
`content:` URI pointing to the selected contact. The response grants
your app temporary permissions to read that contact using the [Contacts Provider](https://developer.android.com/guide/topics/providers/contacts-provider) API, even if
your app doesn't include the [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permission.

**Tip:** If you need access to only a specific piece of contact
information, such as a phone number or email address, instead see the next section about how to
[select specific contact data](https://developer.android.com/guide/components/intents-common#PickContactData).

**Action**
:   [ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK)

**Data URI Scheme**
:   None

**MIME Type**
:   [Contacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_TYPE)

**Example intent:**  

### Kotlin

```kotlin
const val REQUEST_SELECT_CONTACT = 1

fun selectContact() {
    val intent = Intent(Intent.ACTION_PICK).apply {
        type = ContactsContract.Contacts.CONTENT_TYPE
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivityForResult(intent, REQUEST_SELECT_CONTACT)
    }
}

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
    if (requestCode == REQUEST_SELECT_CONTACT && resultCode == RESULT_OK) {
        val contactUri: Uri = data.data
        // Do something with the selected contact at contactUri.
        //...
    }
}
```

### Java

```java
static final int REQUEST_SELECT_CONTACT = 1;

public void selectContact() {
    Intent intent = new Intent(Intent.ACTION_PICK);
    intent.setType(ContactsContract.Contacts.CONTENT_TYPE);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(intent, REQUEST_SELECT_CONTACT);
    }
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == REQUEST_SELECT_CONTACT && resultCode == RESULT_OK) {
        Uri contactUri = data.getData();
        // Do something with the selected contact at contactUri.
        ...
    }
}
```

For information about how to retrieve contact details once you have the contact URI,
read [Retrieve details
for a contact](https://developer.android.com/training/contacts-provider/retrieve-details).

When you retrieve the contact URI using this intent, you generally don't
need the
[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)
permission to read basic details for that contact, such as display name and
whether the contact is starred. However, if you're trying to
[read more specific data](https://developer.android.com/guide/components/intents-common#PickContactData) about a given contact---such
as their phone number or email address---you need the `READ_CONTACTS`
permission.

### Select specific contact data

To have the user select a specific piece of information from a contact, such as
a phone number, email address, or other data type, use the
[ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK) action and specify the MIME type to one
of the following content types, such as
[CommonDataKinds.Phone.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Phone#CONTENT_TYPE) to get the contact's phone number.

**Note:** In many cases, your app needs to have the
[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)
permission to view specific information about a particular contact.

If you need to retrieve only one type of data from a contact, this technique with a
`CONTENT_TYPE` from the
[ContactsContract.CommonDataKinds](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds) classes is more efficient than
using the [Contacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_TYPE), as shown in the preceding section. The result provides you direct
access to the desired data without requiring you to perform a more complex query to [Contacts Provider](https://developer.android.com/guide/topics/providers/contacts-provider).

The result [Intent](https://developer.android.com/reference/android/content/Intent) delivered to your [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)) callback contains the
`content:` URI pointing to the selected contact data. The response grants
your app temporary permissions to read that contact data even if your app doesn't include the [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permission.

**Action**
:   [ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK)

**Data URI Scheme**
:   None

**MIME Type**
:

    [CommonDataKinds.Phone.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Phone#CONTENT_TYPE)
    :   Pick from contacts with a phone number.

    [CommonDataKinds.Email.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_TYPE)
    :   Pick from contacts with an email address.

    [CommonDataKinds.StructuredPostal.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredPostal#CONTENT_TYPE)
    :   Pick from contacts with a postal address.

    Or one of many other `CONTENT_TYPE` values
    under [ContactsContract](https://developer.android.com/reference/android/provider/ContactsContract).

**Example intent:**  

### Kotlin

```kotlin
const val REQUEST_SELECT_PHONE_NUMBER = 1

fun selectContact() {
    // Start an activity for the user to pick a phone number from contacts.
    val intent = Intent(Intent.ACTION_PICK).apply {
        type = CommonDataKinds.Phone.CONTENT_TYPE
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivityForResult(intent, REQUEST_SELECT_PHONE_NUMBER)
    }
}

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
    if (requestCode == REQUEST_SELECT_PHONE_NUMBER && resultCode == Activity.RESULT_OK) {
        // Get the URI and query the content provider for the phone number.
        val contactUri: Uri = data.data
        val projection: Array<String> = arrayOf(CommonDataKinds.Phone.NUMBER)
        contentResolver.query(contactUri, projection, null, null, null).use { cursor ->
            // If the cursor returned is valid, get the phone number.
            if (cursor.moveToFirst()) {
                val numberIndex = cursor.getColumnIndex(CommonDataKinds.Phone.NUMBER)
                val number = cursor.getString(numberIndex)
                // Do something with the phone number.
                ...
            }
        }
    }
}
```

### Java

```java
static final int REQUEST_SELECT_PHONE_NUMBER = 1;

public void selectContact() {
    // Start an activity for the user to pick a phone number from contacts.
    Intent intent = new Intent(Intent.ACTION_PICK);
    intent.setType(CommonDataKinds.Phone.CONTENT_TYPE);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(intent, REQUEST_SELECT_PHONE_NUMBER);
    }
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == REQUEST_SELECT_PHONE_NUMBER && resultCode == RESULT_OK) {
        // Get the URI and query the content provider for the phone number.
        Uri contactUri = data.getData();
        String[] projection = new String[]{CommonDataKinds.Phone.NUMBER};
        Cursor cursor = getContentResolver().query(contactUri, projection,
                null, null, null);
        // If the cursor returned is valid, get the phone number.
        if (cursor != null && cursor.moveToFirst()) {
            int numberIndex = cursor.getColumnIndex(CommonDataKinds.Phone.NUMBER);
            String number = cursor.getString(numberIndex);
            // Do something with the phone number.
            //...
        }
    }
}
```

### View a contact

To display the details for a known contact, use the [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)
action and specify the contact with a `content:` URI as the intent data.

There are two primary ways to initially retrieve the contact's URI:

- Use the contact URI returned by the [ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK) action shown in the preceding section. This approach doesn't require any app permissions.
- Access the list of all contacts directly, as described in [Retrieve a list of
  contacts](https://developer.android.com/training/contacts-provider/retrieve-names). This approach requires the [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permission.

**Action**
:   [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)

**Data URI Scheme**
:   `content:<URI>`

**MIME Type**
:   None. The type is inferred from the contact URI.

**Example intent:**  

### Kotlin

```kotlin
fun viewContact(contactUri: Uri) {
    val intent = Intent(Intent.ACTION_VIEW, contactUri)
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void viewContact(Uri contactUri) {
    Intent intent = new Intent(Intent.ACTION_VIEW, contactUri);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

### Edit an existing contact

To edit a known contact, use the [ACTION_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT)
action, specify the contact with a `content:` URI
as the intent data, and include any known contact information in extras specified by
constants in [ContactsContract.Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert).

There are two primary ways to initially retrieve the contact URI:

- Use the contact URI returned by the [ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK) action shown in the preceding section. This approach doesn't require any app permissions.
- Access the list of all contacts directly, as described in [Retrieve a list of
  contacts](https://developer.android.com/training/contacts-provider/retrieve-names). This approach requires the [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permission.

**Action**
:   [ACTION_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT)

**Data URI Scheme**
:   `content:<URI>`

**MIME Type**
:   The type is inferred from the contact URI.

**Extras**
:   One or more of the extras defined in [ContactsContract.Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert)
    so you can populate fields of the contact details.

**Example intent:**  

### Kotlin

```kotlin
fun editContact(contactUri: Uri, email: String) {
    val intent = Intent(Intent.ACTION_EDIT).apply {
        data = contactUri
        putExtra(ContactsContract.Intents.Insert.EMAIL, email)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void editContact(Uri contactUri, String email) {
    Intent intent = new Intent(Intent.ACTION_EDIT);
    intent.setData(contactUri);
    intent.putExtra(Intents.Insert.EMAIL, email);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

For more information about how to edit a contact, read [Modify
contacts using intents](https://developer.android.com/training/contacts-provider/modify-data).

### Insert a contact

To insert a new contact, use the [ACTION_INSERT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT) action,
specify [Contacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_TYPE) as
the MIME type, and include any known contact information in extras specified by
constants in [ContactsContract.Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert).

**Action**
:   [ACTION_INSERT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT)

**Data URI Scheme**
:   None

**MIME Type**
:   [Contacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_TYPE)

**Extras**
:   One or more of the extras defined in [ContactsContract.Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert).

**Example intent:**  

### Kotlin

```kotlin
fun insertContact(name: String, email: String) {
    val intent = Intent(Intent.ACTION_INSERT).apply {
        type = ContactsContract.Contacts.CONTENT_TYPE
        putExtra(ContactsContract.Intents.Insert.NAME, name)
        putExtra(ContactsContract.Intents.Insert.EMAIL, email)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void insertContact(String name, String email) {
    Intent intent = new Intent(Intent.ACTION_INSERT);
    intent.setType(Contacts.CONTENT_TYPE);
    intent.putExtra(Intents.Insert.NAME, name);
    intent.putExtra(Intents.Insert.EMAIL, email);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

For more information about how to insert a contact, read [Modify
contacts using intents](https://developer.android.com/training/contacts-provider/modify-data).

## Email

Composing an email with optional attachments is a common action for email apps.
Create an intent filter to advertise your app's ability to perform this action using the
information in the following section.

### Compose an email with optional attachments

To compose an email, use one of the following actions based on whether you'll include attachments or not,
and include email details such as the recipient and subject using the extra keys listed.

**Action**
:   [ACTION_SENDTO](https://developer.android.com/reference/android/content/Intent#ACTION_SENDTO) (for no attachment) or  

    [ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND) (for one attachment) or  

    [ACTION_SEND_MULTIPLE](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE) (for multiple attachments)

**Data URI Scheme**
:   None

**MIME Type**
:

    `"text/plain"`
    `"*/*"`

**Extras**
:

    [Intent.EXTRA_EMAIL](https://developer.android.com/reference/android/content/Intent#EXTRA_EMAIL)
    :   A string array of all "To" recipient email addresses.

    [Intent.EXTRA_CC](https://developer.android.com/reference/android/content/Intent#EXTRA_CC)
    :   A string array of all "CC" recipient email addresses.

    [Intent.EXTRA_BCC](https://developer.android.com/reference/android/content/Intent#EXTRA_BCC)
    :   A string array of all "BCC" recipient email addresses.

    [Intent.EXTRA_SUBJECT](https://developer.android.com/reference/android/content/Intent#EXTRA_SUBJECT)
    :   A string with the email subject.

    [Intent.EXTRA_TEXT](https://developer.android.com/reference/android/content/Intent#EXTRA_TEXT)
    :   A string with the body of the email.

    [Intent.EXTRA_STREAM](https://developer.android.com/reference/android/content/Intent#EXTRA_STREAM)
    :   A [Uri](https://developer.android.com/reference/android/net/Uri) pointing to the attachment.
        If using the
        [ACTION_SEND_MULTIPLE](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE)
        action, this instead is an
        [ArrayList](https://developer.android.com/reference/java/util/ArrayList) containing
        multiple `Uri` objects.

**Example intent:**  

### Kotlin

```kotlin
fun composeEmail(addresses: Array<String>, subject: String, attachment: Uri) {
    val intent = Intent(Intent.ACTION_SEND).apply {
        type = "*/*"
        putExtra(Intent.EXTRA_EMAIL, addresses)
        putExtra(Intent.EXTRA_SUBJECT, subject)
        putExtra(Intent.EXTRA_STREAM, attachment)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void composeEmail(String[] addresses, String subject, Uri attachment) {
    Intent intent = new Intent(Intent.ACTION_SEND);
    intent.setType("*/*");
    intent.putExtra(Intent.EXTRA_EMAIL, addresses);
    intent.putExtra(Intent.EXTRA_SUBJECT, subject);
    intent.putExtra(Intent.EXTRA_STREAM, attachment);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

If you want to make sure that your intent is handled only by an email app, and not a
text messaging or social app, then use the [ACTION_SENDTO](https://developer.android.com/reference/android/content/Intent#ACTION_SENDTO) action
and include the `"mailto:"` data scheme as shown in the following example:  

### Kotlin

```kotlin
fun composeEmail(addresses: Array<String>, subject: String) {
    val intent = Intent(Intent.ACTION_SENDTO).apply {
        data = Uri.parse("mailto:") // Only email apps handle this.
        putExtra(Intent.EXTRA_EMAIL, addresses)
        putExtra(Intent.EXTRA_SUBJECT, subject)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void composeEmail(String[] addresses, String subject) {
    Intent intent = new Intent(Intent.ACTION_SENDTO);
    intent.setData(Uri.parse("mailto:")); // Only email apps handle this.
    intent.putExtra(Intent.EXTRA_EMAIL, addresses);
    intent.putExtra(Intent.EXTRA_SUBJECT, subject);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <data android:type="*/*" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.intent.action.SENDTO" />
        <data android:scheme="mailto" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## File storage

The following are common actions for file storage apps, including the information you need
to create an intent filter to advertise your app's ability to perform each action.

### Retrieve a specific type of file

To request that the user select a file such as a document or photo and return a reference to
your app, use the [ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT) action and specify your desired
MIME type. The file reference returned to your app is transient to your activity's current
lifecycle, so if you want to access it later you must import a copy that you can read later.

This intent also lets the user create a new file in the process. For
example, instead of selecting an existing photo, the user can capture a new photo with the camera.

The result intent delivered to your [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)) method includes data with a URI pointing to the file.
The URI can be anything, such as an `http:` URI, `file:` URI, or `content:`
URI. However, if you'd like to restrict selectable files to only those that are accessible
from a content provider (a `content:` URI) and that are available as a file stream with
[openFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String)),
add
the [CATEGORY_OPENABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE) category to your intent.

On Android 4.3 (API level 18) and higher,
you can also let the user select multiple files by adding
[EXTRA_ALLOW_MULTIPLE](https://developer.android.com/reference/android/content/Intent#EXTRA_ALLOW_MULTIPLE) to the intent, set to `true`.
You can then access each of the selected files in a [ClipData](https://developer.android.com/reference/android/content/ClipData)
object returned by [getClipData()](https://developer.android.com/reference/android/content/Intent#getClipData()).

**Action**
:   [ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT)

**Data URI Scheme**
:   None

**MIME Type**
:   The MIME type corresponding to the file type the user needs to select.

**Extras**
:

    [EXTRA_ALLOW_MULTIPLE](https://developer.android.com/reference/android/content/Intent#EXTRA_ALLOW_MULTIPLE)
    :   A boolean that declares whether the user can select more than one file at a time.

    [EXTRA_LOCAL_ONLY](https://developer.android.com/reference/android/content/Intent#EXTRA_LOCAL_ONLY)
    :   A boolean that declares whether the returned file must be available directly from
        the device, rather than requiring a download from a remote service.

**Category** (optional)
:

    [CATEGORY_OPENABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE)
    :   To return only "openable" files that can be represented as a file stream
        with [openFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String)).

**Example intent to get a photo:**  

### Kotlin

```kotlin
const val REQUEST_IMAGE_GET = 1

fun selectImage() {
    val intent = Intent(Intent.ACTION_GET_CONTENT).apply {
        type = "image/*"
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_GET)
    }
}

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
    if (requestCode == REQUEST_IMAGE_GET && resultCode == Activity.RESULT_OK) {
        val thumbnail: Bitmap = data.getParcelableExtra("data")
        val fullPhotoUri: Uri = data.data
        // Do work with photo saved at fullPhotoUri.
        ...
    }
}
```

### Java

```java
static final int REQUEST_IMAGE_GET = 1;

public void selectImage() {
    Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
    intent.setType("image/*");
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivityForResult(intent, REQUEST_IMAGE_GET);
    }
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == REQUEST_IMAGE_GET && resultCode == RESULT_OK) {
        Bitmap thumbnail = data.getParcelable("data");
        Uri fullPhotoUri = data.getData();
        // Do work with photo saved at fullPhotoUri.
        ...
    }
}
```

**Example intent filter to return a photo:**  

    <activity ...>
        <intent-filter>
            <action android:name="android.intent.action.GET_CONTENT" />
            <data android:type="image/*" />
            <category android:name="android.intent.category.DEFAULT" />
            <!-- The OPENABLE category declares that the returned file is accessible
                 from a content provider that supports https://developer.android.com/reference/android/provider/OpenableColumns
                 and https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String). -->
            <category android:name="android.intent.category.OPENABLE" />
        </intent-filter>
    </activity>

### Open a specific type of file

Instead of retrieving a copy of a file that you must import to your app, by using the [ACTION_GET_CONTENT](https://developer.android.com/reference/android/content/Intent#ACTION_GET_CONTENT) action, when running on Android
4.4 or higher you can instead request to *open* a file that's managed by another app by
using the [ACTION_OPEN_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT) action and specifying a MIME type.
To also let the user create a new document that your app can write to, use the [ACTION_CREATE_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT) action instead.

For example, instead of
selecting from existing PDF documents, the `ACTION_CREATE_DOCUMENT`
intent lets users select where they'd like to create a new document, such as within another app
that manages the document's storage. Your app then receives the URI location of where it
can write the new document.

Whereas the intent delivered to your [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent))
method from the `ACTION_GET_CONTENT` action might
return a URI of any type, the result intent from `ACTION_OPEN_DOCUMENT`
and `ACTION_CREATE_DOCUMENT` always specify the chosen file as a `content:` URI that's backed by a [DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider). You can open the
file with [openFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String)) and
query its details using columns from [DocumentsContract.Document](https://developer.android.com/reference/android/provider/DocumentsContract.Document).

The returned URI grants your app long-term read access to the file, also possibly
with write access. The `ACTION_OPEN_DOCUMENT` action is
particularly useful when you want to read an existing file without making a copy into your app
or when you want to open and edit a file in place.

You can also let the user select multiple files by adding
[EXTRA_ALLOW_MULTIPLE](https://developer.android.com/reference/android/content/Intent#EXTRA_ALLOW_MULTIPLE) to the intent, set to `true`.
If the user selects just one item, then you can retrieve the item from [getData()](https://developer.android.com/reference/android/content/Intent#getData()).
If the user selects more than one item, then `getData()` returns null and you must instead
retrieve each item from a [ClipData](https://developer.android.com/reference/android/content/ClipData)
object that is returned by [getClipData()](https://developer.android.com/reference/android/content/Intent#getClipData()).

**Note:** Your intent **must** specify a MIME type and
**must** declare the [CATEGORY_OPENABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE) category. If
appropriate, you can specify more than one MIME type by adding an array of MIME types with the
[EXTRA_MIME_TYPES](https://developer.android.com/reference/android/content/Intent#EXTRA_MIME_TYPES) extra---if you do so, you must set the
primary MIME type in [setType()](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String)) to `"*/*"`.

**Action**
:   [ACTION_OPEN_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT) or  

    [ACTION_CREATE_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT)

**Data URI Scheme**
:   None

**MIME Type**
:   The MIME type corresponding to the file type the user needs to select.

**Extras**
:

    [EXTRA_MIME_TYPES](https://developer.android.com/reference/android/content/Intent#EXTRA_MIME_TYPES)
    :   An array of MIME types corresponding to the types of files your app is
        requesting. When you use this extra, you must set the primary MIME type in
        [setType()](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String)) to `"*/*"`.

    [EXTRA_ALLOW_MULTIPLE](https://developer.android.com/reference/android/content/Intent#EXTRA_ALLOW_MULTIPLE)
    :   A boolean that declares whether the user can select more than one file at a time.

    [EXTRA_TITLE](https://developer.android.com/reference/android/content/Intent#EXTRA_TITLE)
    :   For use with [ACTION_CREATE_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_DOCUMENT) to specify
        an initial filename.

    [EXTRA_LOCAL_ONLY](https://developer.android.com/reference/android/content/Intent#EXTRA_LOCAL_ONLY)
    :   A boolean that declares whether the returned file must be available directly from
        the device, rather than requiring a download from a remote service.

**Category**
:

    [CATEGORY_OPENABLE](https://developer.android.com/reference/android/content/Intent#CATEGORY_OPENABLE)
    :   To return only "openable" files that can be represented as a file stream
        with [openFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openFileDescriptor(android.net.Uri, java.lang.String)).

**Example intent to get a photo:**  

### Kotlin

```kotlin
const val REQUEST_IMAGE_OPEN = 1

fun selectImage2() {
    val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
        type = "image/*"
        addCategory(Intent.CATEGORY_OPENABLE)
    }
    // Only the system receives the ACTION_OPEN_DOCUMENT, so no need to test.
    startActivityForResult(intent, REQUEST_IMAGE_OPEN)
}

override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent) {
    if (requestCode == REQUEST_IMAGE_OPEN && resultCode == Activity.RESULT_OK) {
        val fullPhotoUri: Uri = data.data
        // Do work with full size photo saved at fullPhotoUri.
        ...
    }
}
```

### Java

```java
static final int REQUEST_IMAGE_OPEN = 1;

public void selectImage() {
    Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
    intent.setType("image/*");
    intent.addCategory(Intent.CATEGORY_OPENABLE);
    // Only the system receives the ACTION_OPEN_DOCUMENT, so no need to test.
    startActivityForResult(intent, REQUEST_IMAGE_OPEN);
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == REQUEST_IMAGE_OPEN && resultCode == RESULT_OK) {
        Uri fullPhotoUri = data.getData();
        // Do work with full size photo saved at fullPhotoUri.
        ...
    }
}
```

Third-party apps can't respond to an intent with the
[ACTION_OPEN_DOCUMENT](https://developer.android.com/reference/android/content/Intent#ACTION_OPEN_DOCUMENT) action. Instead, the system receives this
intent and displays all the files available from various apps in a unified user interface.

To provide your app's files in this UI and let other apps open them, you must implement
a [DocumentsProvider](https://developer.android.com/reference/android/provider/DocumentsProvider) and include an intent filter for
[PROVIDER_INTERFACE](https://developer.android.com/reference/android/provider/DocumentsContract#PROVIDER_INTERFACE)
(`"android.content.action.DOCUMENTS_PROVIDER"`), as shown in the following example:

```xml
<provider ...
    android:grantUriPermissions="true"
    android:exported="true"
    android:permission="android.permission.MANAGE_DOCUMENTS">
    <intent-filter>
        <action android:name="android.content.action.DOCUMENTS_PROVIDER" />
    </intent-filter>
</provider>
```

For more information about how to make the files managed by your app openable from other apps,
read [Open files using storage access framework](https://developer.android.com/guide/topics/providers/document-provider).

## Local actions

Calling a car is a common local action. Create an intent filter to advertise your app's
ability to perform this action using the information in the following section.

### Call a car

[![](https://developer.android.com/static/guide/components/images/voice-icon.png)](https://developers.google.com/voice-actions/system/#system_actions_reference)


Google Voice Actions

- "get me a taxi"
- "call me a car"


(Wear OS only)

To call a taxi, use the
[`ACTION_RESERVE_TAXI_RESERVATION`](https://developers.google.com/android/reference/com/google/android/gms/actions/ReserveIntents#ACTION_RESERVE_TAXI_RESERVATION)
action.

**Note:** Apps must ask for confirmation from the user
before completing this action.

**Action**
:   [`ACTION_RESERVE_TAXI_RESERVATION`](https://developer.android.com/android/reference/com/google/android/gms/actions/ReserveIntents#ACTION_RESERVE_TAXI_RESERVATION)

**Data URI**
:   None

**MIME Type**
:   None

**Extras**
:   None

**Example intent:**  

### Kotlin

```kotlin
fun callCar() {
    val intent = Intent(ReserveIntents.ACTION_RESERVE_TAXI_RESERVATION)
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void callCar() {
    Intent intent = new Intent(ReserveIntents.ACTION_RESERVE_TAXI_RESERVATION);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="com.google.android.gms.actions.RESERVE_TAXI_RESERVATION" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## Maps

Showing a location on a map is a common action for map apps.
Create an intent filter to advertise your app's ability to perform this action using the
information in the following section.

### Show a location on a map

To open a map, use the [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW) action and specify
the location information in the intent data with one of the following schemes.

**Action**
:   [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)

**Data URI Scheme**
:

    `geo:`*latitude* `,`*longitude*

    :   Show the map at the given longitude and latitude. Example: `"geo:47.6,-122.3"`

    `geo:`*latitude* `,`*longitude* `?z=`*zoom*
    :   Show the map at the given longitude and latitude at a certain zoom level. A zoom level of
        1 shows the whole Earth, centered at the given *lat* ,*lng* . The highest
        (closest) zoom level is 23.

        Example: `"geo:47.6,-122.3?z=11"`

    `geo:0,0?q=lat,lng(label)`

    :   Show the map at the given longitude and latitude with a string label. Example: `"geo:0,0?q=34.99,-106.61(Treasure)"`

    `geo:0,0?q=my+street+address`

    :   Show the location for "my street address", which can be a specific address or location query. Example: `"geo:0,0?q=1600+Amphitheatre+Parkway%2C+CA"`

        **Note:** All strings passed in the `geo` URI must
        be encoded. For example, the string `1st & Pike, Seattle` becomes
        `1st%20%26%20Pike%2C%20Seattle`. Spaces in the string are encoded with
        `%20` or replaced with the plus sign (`+`).

**MIME Type**
:   None

**Example intent:**  

### Kotlin

```kotlin
fun showMap(geoLocation: Uri) {
    val intent = Intent(Intent.ACTION_VIEW).apply {
        data = geoLocation
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void showMap(Uri geoLocation) {
    Intent intent = new Intent(Intent.ACTION_VIEW);
    intent.setData(geoLocation);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="geo" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

## Music or video

The following are common actions for music and video apps, including the information you need
to create an intent filter to advertise your app's ability to perform each action.

### Play a media file

To play a music file, use the [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW) action and
specify the URI location of the file in the intent data.

**Action**
:   [ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)

**Data URI Scheme**
:

    `file:`*<URI>*
    `content:`*<URI>*
    `http:`*<URL>*

**MIME Type**
:

    `"audio/*"`
    `"application/ogg"`
    `"application/x-ogg"`
    `"application/itunes"`
    Or any other that your app requires.

**Example intent:**  

### Kotlin

```kotlin
fun playMedia(file: Uri) {
    val intent = Intent(Intent.ACTION_VIEW).apply {
        data = file
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void playMedia(Uri file) {
    Intent intent = new Intent(Intent.ACTION_VIEW);
    intent.setData(file);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <data android:type="audio/*" />
        <data android:type="application/ogg" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

### Play music based on a search query

[![](https://developer.android.com/static/guide/components/images/voice-icon.png)](https://developers.google.com/voice-actions/system/#system_actions_reference)


Google Voice Actions

- "play michael jackson billie jean"

To play music based on a search query, use the
[INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH](https://developer.android.com/reference/android/provider/MediaStore#INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH) intent. An app might fire
this intent in response to the user's voice command to play music. The receiving app for this
intent performs a search within its inventory to match existing content to the given query and
starts playing that content.

In this intent, include the [EXTRA_MEDIA_FOCUS](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_FOCUS) string
extra, which specifies the intended search mode. For example, the search mode can specify whether
the search is for an artist name or song name.

**Action**
:   [INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH](https://developer.android.com/reference/android/provider/MediaStore#INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH)

**Data URI Scheme**
:   None

**MIME Type**
:   None

**Extras**
:

    [MediaStore.EXTRA_MEDIA_FOCUS](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_FOCUS) (required)

    :   Indicates the search mode: whether the user is looking for a particular artist, album, song,
        or playlist. Most search modes take additional extras. For example, if the user
        is interested in listening to a particular song, the intent might have three additional extras:
        the song title, the artist, and the album. This intent supports the following search modes for
        each value of [EXTRA_MEDIA_FOCUS](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_FOCUS):

        *Any* - `"vnd.android.cursor.item/*"`

        :   Play any music. The receiving app plays some music based on a smart choice, such
            as the last playlist the user listened to.

            Additional extras:

            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): an empty string. This extra is always provided for backward compatibility. Existing apps that don't know about search modes can process this intent as an unstructured search.

        *Unstructured* - `"vnd.android.cursor.item/*"`

        :   Play a particular song, album, or genre from an unstructured search query. Apps can generate
            an intent with this search mode when they can't identify the type of content the user wants to
            listen to. Use more specific search modes when possible.

            Additional extras:

            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): a string that contains any combination of the artist, the album, the song name, or the genre.

        *Genre* -
        [Audio.Genres.ENTRY_CONTENT_TYPE](https://developer.android.com/reference/android/provider/MediaStore.Audio.Genres#ENTRY_CONTENT_TYPE)

        :   Play music of a particular genre.

            Additional extras:

            - `"android.intent.extra.genre"` (required) - The genre.
            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): the genre. This extra is always provided for backward compatibility. Existing apps that don't know about search modes can process this intent as an unstructured search.

        *Artist* -
        [Audio.Artists.ENTRY_CONTENT_TYPE](https://developer.android.com/reference/android/provider/MediaStore.Audio.Artists#ENTRY_CONTENT_TYPE)

        :   Play music from a particular artist.

            Additional extras:

            - [EXTRA_MEDIA_ARTIST](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ARTIST) (required): the artist.
            - `"android.intent.extra.genre"`: the genre.
            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): a string that contains any combination of the artist or the genre. This extra is always provided for backward compatibility. Existing apps that don't know about search modes can process this intent as an unstructured search.

        *Album* -
        [Audio.Albums.ENTRY_CONTENT_TYPE](https://developer.android.com/reference/android/provider/MediaStore.Audio.Albums#ENTRY_CONTENT_TYPE)

        :   Play music from a particular album.

            Additional extras:

            - [EXTRA_MEDIA_ALBUM](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ALBUM) (required): the album.
            - [EXTRA_MEDIA_ARTIST](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ARTIST): the artist.
            - `"android.intent.extra.genre"`: the genre.
            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): a string that contains any combination of the album or the artist. This extra is always provided for backward compatibility. Existing apps that don't know about search modes can process this intent as an unstructured search.

        *Song* - `"vnd.android.cursor.item/audio"`

        :   Play a particular song.

            Additional extras:

            - [EXTRA_MEDIA_ALBUM](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ALBUM): the album.
            - [EXTRA_MEDIA_ARTIST](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ARTIST): the artist.
            - `"android.intent.extra.genre"`: the genre.
            - [EXTRA_MEDIA_TITLE](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_TITLE) (required): the song name.
            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): a string that contains any combination of the album, the artist, the genre, or the title. This extra is always provided for backward compatibility. Existing apps that don't know about search modes can process this intent as an unstructured search.

        *Playlist* - [Audio.Playlists.ENTRY_CONTENT_TYPE](https://developer.android.com/reference/android/provider/MediaStore.Audio.Playlists#ENTRY_CONTENT_TYPE)
        :
            | Android playlists are deprecated. The API is no longer maintained, but the current functionality remains for compatibility.

            Play a particular playlist or a playlist that matches some criteria specified
            by additional extras.

            Additional extras:

            - [EXTRA_MEDIA_ALBUM](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ALBUM): the album.
            - [EXTRA_MEDIA_ARTIST](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_ARTIST): the artist.
            - `"android.intent.extra.genre"`: the genre.
            - `"android.intent.extra.playlist"`: the playlist.
            - [EXTRA_MEDIA_TITLE](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_TITLE): the song name that the playlist is based on.
            - [QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY) (required): a string that contains any combination of the album, the artist, the genre, the playlist, or the title. This extra is always provided for backward compatibility. Existing apps that don't know about search modes can process this intent as an unstructured search.


**Example intent:**

If the user wants to listen to music from a particular artist, a search app might generate the
following intent:  

### Kotlin

```kotlin
fun playSearchArtist(artist: String) {
    val intent = Intent(MediaStore.INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH).apply {
        putExtra(MediaStore.EXTRA_MEDIA_FOCUS, MediaStore.Audio.Artists.ENTRY_CONTENT_TYPE)
        putExtra(MediaStore.EXTRA_MEDIA_ARTIST, artist)
        putExtra(SearchManager.QUERY, artist)
    }
    if (intent.resolveActivity(packageManager) != null) {
        startActivity(intent)
    }
}
```

### Java

```java
public void playSearchArtist(String artist) {
    Intent intent = new Intent(MediaStore.INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH);
    intent.putExtra(MediaStore.EXTRA_MEDIA_FOCUS,
                    MediaStore.Audio.Artists.ENTRY_CONTENT_TYPE);
    intent.putExtra(MediaStore.EXTRA_MEDIA_ARTIST, artist);
    intent.putExtra(SearchManager.QUERY, artist);
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(intent);
    }
}
```

**Example intent filter:**  

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.media.action.MEDIA_PLAY_FROM_SEARCH" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

When handling this intent in your activity, check the value of the
[EXTRA_MEDIA_FOCUS](https://developer.android.com/reference/android/provider/MediaStore#EXTRA_MEDIA_FOCUS) extra in the incoming
[Intent](https://developer.android.com/reference/android/content/Intent) to determine the search mode. Once your activity has identified
the search mode, read the values of the additional extras for that particular search mode.
With this information, your app can then perform the search within its inventory to play the
content that matches the search query. This is shown in the following example.  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    ...
    if (intent.action.compareTo(MediaStore.INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH) == 0) {

        val mediaFocus: String? = intent.getStringExtra(MediaStore.EXTRA_MEDIA_FOCUS)
        val query: String? = intent.getStringExtra(SearchManager.QUERY)

        // Some of these extras might not be available depending on the search mode.
        val album: String? = intent.getStringExtra(MediaStore.EXTRA_MEDIA_ALBUM)
        val artist: String? = intent.getStringExtra(MediaStore.EXTRA_MEDIA_ARTIST)
        val genre: String? = intent.getStringExtra("android.intent.extra.genre")
        val playlist: String? = intent.getStringExtra("android.intent.extra.playlist")
        val title: String? = intent.getStringExtra(MediaStore.EXTRA_MEDIA_TITLE)

        // Determine the search mode and use the corresponding extras.
        when {
            mediaFocus == null -> {
                // 'Unstructured' search mode (backward compatible)
                playUnstructuredSearch(query)
            }
            mediaFocus.compareTo("vnd.android.cursor.item/*") == 0 -> {
                if (query?.isNotEmpty() == true) {
                    // 'Unstructured' search mode.
                    playUnstructuredSearch(query)
                } else {
                    // 'Any' search mode.
                    playResumeLastPlaylist()
                }
            }
            mediaFocus.compareTo(MediaStore.Audio.Genres.ENTRY_CONTENT_TYPE) == 0 -> {
                // 'Genre' search mode.
                playGenre(genre)
            }
            mediaFocus.compareTo(MediaStore.Audio.Artists.ENTRY_CONTENT_TYPE) == 0 -> {
                // 'Artist' search mode.
                playArtist(artist, genre)
            }
            mediaFocus.compareTo(MediaStore.Audio.Albums.ENTRY_CONTENT_TYPE) == 0 -> {
                // 'Album' search mode.
                playAlbum(album, artist)
            }
            mediaFocus.compareTo("vnd.android.cursor.item/audio") == 0 -> {
                // 'Song' search mode.
                playSong(album, artist, genre, title)
            }
            mediaFocus.compareTo(MediaStore.Audio.Playlists.ENTRY_CONTENT_TYPE) == 0 -> {
                // 'Playlist' search mode.
                playPlaylist(album, artist, genre, playlist, title)
            }
        }
    }
}
```

### Java

```java
protected void onCreate(Bundle savedInstanceState) {
    //...
    Intent intent = this.getIntent();
    if (intent.getAction().compareTo(MediaStore.INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH) == 0) {

        String mediaFocus = intent.getStringExtra(MediaStore.EXTRA_MEDIA_FOCUS);
        String query = intent.getStringExtra(SearchManager.QUERY);

        // Some of these extras might not be available depending on the search mode.
        String album = intent.getStringExtra(MediaStore.EXTRA_MEDIA_ALBUM);
        String artist = intent.getStringExtra(MediaStore.EXTRA_MEDIA_ARTIST);
        String genre = intent.getStringExtra("android.intent.extra.genre");
        String playlist = intent.getStringExtra("android.intent.extra.playlist");
        String title = intent.getStringExtra(MediaStore.EXTRA_MEDIA_TITLE);

        // Determine the search mode and use the corresponding extras.
        if (mediaFocus == null) {
            // 'Unstructured' search mode (backward compatible).
            playUnstructuredSearch(query);

        } else if (mediaFocus.compareTo("vnd.android.cursor.item/*") == 0) {
            if (query.isEmpty()) {
                // 'Any' search mode.
                playResumeLastPlaylist();
            } else {
                // 'Unstructured' search mode.
                playUnstructuredSearch(query);
            }

        } else if (mediaFocus.compareTo(MediaStore.Audio.Genres.ENTRY_CONTENT_TYPE) == 0) {
            // 'Genre' search mode.
            playGenre(genre);

        } else if (mediaFocus.compareTo(MediaStore.Audio.Artists.ENTRY_CONTENT_TYPE) == 0) {
            // 'Artist' search mode.
            playArtist(artist, genre);

        } else if (mediaFocus.compareTo(MediaStore.Audio.Albums.ENTRY_CONTENT_TYPE) == 0) {
            // 'Album' search mode.
            playAlbum(album, artist);

        } else if (mediaFocus.compareTo("vnd.android.cursor.item/audio") == 0) {
            // 'Song' search mode.
            playSong(album, artist, genre, title);

        } else if (mediaFocus.compareTo(MediaStore.Audio.Playlists.ENTRY_CONTENT_TYPE) == 0) {
            // 'Playlist' search mode.
            playPlaylist(album, artist, genre, playlist, title);
        }
    }
}
```

## New note

Creating a note is a common action for note-taking apps.
Create an intent filter to advertise your app's ability to perform this action using the
information in the following section.

### Create a note

To create a new note, use the
[`ACTION_CREATE_NOTE`](https://developers.google.com/android/reference/com/google/android/gms/actions/NoteIntents#ACTION_CREATE_NOTE) action and specify note details such as the subject and text using following extras.

**Note:** Apps must ask for confirmation from the user
before completing this action.

**Action**
:   [`ACTION_CREATE_NOTE`](https://developers.google.com/android/reference/com/google/android/gms/actions/NoteIntents#ACTION_CREATE_NOTE)

**Data URI Scheme**
:   None

**MIME Type**
:   [`PLAIN_TEXT_TYPE`](https://developer.android.com/reference/org/apache/http/protocol/HTTP.html#PLAIN_TEXT_TYPE)
:   "\*/\*"

**Extras**
:

    [`EXTRA_NAME`](https://developers.google.com/android/reference/com/google/android/gms/actions/NoteIntents#EXTRA_NAME)
    :   A string indicating the title or subject of the note.

    [`EXTRA_TEXT`](https://developers.google.com/android/reference/com/google/android/gms/actions/NoteIntents#EXTRA_TEXT)
    :   A string indicating the text of the note.