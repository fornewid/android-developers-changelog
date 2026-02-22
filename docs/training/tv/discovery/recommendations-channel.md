---
title: https://developer.android.com/training/tv/discovery/recommendations-channel
url: https://developer.android.com/training/tv/discovery/recommendations-channel
source: md.txt
---

# Channels on the home screen

The Android TV home screen, or simply the*home screen* , provides a UI that displays recommended content as a table of*channels* and*programs*. Each row is a channel. A channel contains cards for every program available on that channel:

![TV home screen](https://developer.android.com/training/tv/images/home-screen-4.png)

This document demonstrates how to add channels and programs to the home screen, update content, handle user actions, and provide the best experience for your users. (If you'd like to dig deeper into the API, try the[home screen codelab](https://developer.android.com/codelabs/tv-recommendations-kotlin#0)and watch the[I/O 2017 Android TV session](https://www.youtube.com/watch?v=LMB9B6Z__bM).)

**Note:** Recommendations channels are only available in Android 8.0 (API level 26) and later. You must use them to supply recommendations for apps running in Android 8.0 (API level 26) and later. To supply recommendations for apps running on earlier versions of Android, your app must use the[recommendations row](https://developer.android.com/training/tv/discovery/recommendations-row)instead.

## The home screen UI

Apps can create new channels, add, remove, and update the programs in a channel, and control the order of programs in a channel. For example an app can create a channel called "What's New" and show cards for newly available programs.

Apps cannot control the order in which channels appear in the home screen. When your app creates a new channel, the home screen adds it to the bottom of the channel list. The user can reorder, hide, and show channels.

### The Watch Next channel

The Watch Next channel is the second row that appears in the home screen, after the apps row. The system creates and maintains this channel. Your app can add programs to the Watch Next channel. For more information, see[Add programs to the Watch Next channel](https://developer.android.com/training/tv/discovery/watch-next-add-programs).
| **Note:** On the home screen, the Watch Next channel has the label**Play Next**.

### App channels

The channels that your app creates all follow this life cycle:

1. User discovers a channel in your app and requests to add it to the home screen.
2. App creates the channel and adds it to the`TvProvider`(at this point the channel is not visible).
3. App asks the system to display the channel.
4. System asks user to approve the new channel.
5. New channel appears in the last row of the home screen.

### The default channel

Your app can offer any number of channels for the user to add to the home screen. The user usually has to select and approve each channel before it appears in the home screen. Every app has the option of creating one*default*channel. The default channel is special because it automatically appears in the home screen; the user does not have to explicitly request it.

## Prerequisites

The Android TV home screen uses Android's`TvProvider`APIs to manage the channels and programs that your app creates. To access the provider's data, add the following permission to your app's manifest:  

    <uses-permission android:name="com.android.providers.tv.permission.WRITE_EPG_DATA" />

| **Note:** The`READ_EPG_DATA`permission was deprecated in Android M (API 23) and is no longer needed.

The`TvProvider`support library makes it easier to use the provider. Add it to the dependencies in your`build.gradle`file:  

### Groovy

```groovy
implementation 'androidx.tvprovider:tvprovider:1.0.0'
```

### Kotlin

```kotlin
implementation("androidx.tvprovider:tvprovider:1.0.0")
```

To work with channels and programs, be sure to include these support library imports in your program:  

### Kotlin

```kotlin
import android.support.media.tv.Channel
import android.support.media.tv.TvContractCompat
import android.support.media.tv.ChannelLogoUtils
import android.support.media.tv.PreviewProgram
import android.support.media.tv.WatchNextProgram
```

### Java

```java
import android.support.media.tv.Channel;
import android.support.media.tv.TvContractCompat;
import android.support.media.tv.ChannelLogoUtils;
import android.support.media.tv.PreviewProgram;
import android.support.media.tv.WatchNextProgram;
```

## Channels

The first channel your app creates becomes its default channel. The default channel automatically appears in the home screen. All other channels you create must be selected and accepted by the user before they can appear in the home screen.

### Creating a channel

Your app should ask the system to show newly added channels only when it is running in the foreground. This prevents your app from displaying a dialog requesting approval to add your channel while the user is running a different app. If you try to add a channel while running in the background, the activity's`onActivityResult()`method returns the status code`RESULT_CANCELED`.

To create a channel, follow these steps:

<br />

1. Create a channel builder and set its attributes. Note that the channel type must be`TYPE_PREVIEW`. Add more[attributes](https://developer.android.com/training/tv/discovery/recommendations-channel#attributes)as required.

   ### Kotlin

   ```kotlin
   val builder = Channel.Builder()
   // Every channel you create must have the type `TYPE_PREVIEW`
   builder.setType(TvContractCompat.Channels.TYPE_PREVIEW)
           .setDisplayName("Channel Name")
           .setAppLinkIntentUri(uri)
   ```

   ### Java

   ```java
   Channel.Builder builder = new Channel.Builder();
   // Every channel you create must have the type `TYPE_PREVIEW`
   builder.setType(TvContractCompat.Channels.TYPE_PREVIEW)
           .setDisplayName("Channel Name")
           .setAppLinkIntentUri(uri);
   ```
2. Insert the channel into the provider:

   ### Kotlin

   ```kotlin
   var channelUri = context.contentResolver.insert(
           TvContractCompat.Channels.CONTENT_URI, builder.build().toContentValues())
   ```

   ### Java

   ```java
   Uri channelUri = context.getContentResolver().insert(
           TvContractCompat.Channels.CONTENT_URI, builder.build().toContentValues());
   ```
3. You need to save the channel ID in order to add programs to the channel later. Extract the channel ID from the returned URI:

   ### Kotlin

   ```kotlin
   var channelId = ContentUris.parseId(channelUri)
   ```

   ### Java

   ```java
   long channelId = ContentUris.parseId(channelUri);
   ```
4. You must add a logo for your channel. Use a`Uri`or`Bitmap`. The logo icon should be 80dp x 80dp, and it must be opaque. It is displayed under a circular mask:

   ![TV home screen icon mask](https://developer.android.com/training/tv/images/home-screen-1.png)  

   ### Kotlin

   ```kotlin
   // Choose one or the other
   storeChannelLogo(context: Context, channelId: Long, logoUri: Uri) // also works if logoUri is a URL
   storeChannelLogo(context: Context, channelId: Long, logo: Bitmap)
   ```

   ### Java

   ```java
   // Choose one or the other
   storeChannelLogo(Context context, long channelId, Uri logoUri); // also works if logoUri is a URL
   storeChannelLogo(Context context, long channelId, Bitmap logo);
   ```
5. Create the default channel (optional): When your app creates its first channel, you can make it the[default channel](https://developer.android.com/training/tv/discovery/recommendations-channel#the_default_channel)so it appears in the home screen immediately without any user action. Any other channels you create aren't visible until the user explicitly[selects](https://developer.android.com/training/tv/discovery/recommendations-channel#discovering_and_adding_channels)them.

   <br />

   ### Kotlin

   ```kotlin
   TvContractCompat.requestChannelBrowsable(context, channelId)
   ```

   ### Java

   ```java
   TvContractCompat.requestChannelBrowsable(context, channelId);
   ```

   <br />

6. Make your default channel appear before your app is opened. You can make this behavior happen by adding a`BroadcastReceiver`that listens for the`android.media.tv.action.INITIALIZE_PROGRAMS`action, which the home screen sends after the app is installed:  

   ```xml
   <receiver
     android:name=".RunOnInstallReceiver"
     android:exported="true">
       <intent-filter>
         <action android:name="android.media.tv.action.INITIALIZE_PROGRAMS" />
         <category android:name="android.intent.category.DEFAULT" />
       </intent-filter>
   </receiver>
   ```
   When sideloading your app during development, you can test this step by triggering the intent through adb, where<var translate="no">your.package.name</var>/<var translate="no">.YourReceiverName</var>is your app's`BroadcastReceiver`:

   <br />

   ```
   adb shell am broadcast -a android.media.tv.action.INITIALIZE_PROGRAMS -n \
       your.package.name/.YourReceiverName
   ```

   In rare cases, your app might receive the broadcast at the same time the user starts your app. Make sure your code doesn't try to add the default channel more than once.

   <br />

<br />

### Updating a channel

Updating channels is very similar to creating them.

Use another`Channel.Builder`to set the attributes that need to change.

Use the`ContentResolver`to update the channel. Use the channel ID that you saved when the channel was originally added:  

### Kotlin

```kotlin
context.contentResolver.update(
        TvContractCompat.buildChannelUri(channelId),
        builder.build().toContentValues(),
        null,
        null
)
```

### Java

```java
context.getContentResolver().update(TvContractCompat.buildChannelUri(channelId),
    builder.build().toContentValues(), null, null);
```

To update a channel's logo, use`storeChannelLogo()`.

### Deleting a channel

### Kotlin

```kotlin
context.contentResolver.delete(TvContractCompat.buildChannelUri(channelId), null, null)
```

### Java

```java
context.getContentResolver().delete(TvContractCompat.buildChannelUri(channelId), null, null);
```
| **Note:** You should never delete the default channel. If you do, the user must select it again and ask to add it to the home screen. It cannot reappear automatically. When it's added back it appears at the bottom of the home screen, just like any other newly added channel.

## Programs

### Adding programs to an app channel

Create a`PreviewProgram.Builder`and set its attributes:  

### Kotlin

```kotlin
val builder = PreviewProgram.Builder()
builder.setChannelId(channelId)
        .setType(TvContractCompat.PreviewPrograms.TYPE_CLIP)
        .setTitle("Title")
        .setDescription("Program description")
        .setPosterArtUri(uri)
        .setIntentUri(uri)
        .setInternalProviderId(appProgramId)
```

### Java

```java
PreviewProgram.Builder builder = new PreviewProgram.Builder();
builder.setChannelId(channelId)
        .setType(TvContractCompat.PreviewPrograms.TYPE_CLIP)
        .setTitle("Title")
        .setDescription("Program description")
        .setPosterArtUri(uri)
        .setIntentUri(uri)
        .setInternalProviderId(appProgramId);
```

Add more attributes depending on the type of program. (To see the attributes available for each type of program, refer to the[tables](https://developer.android.com/training/tv/discovery/recommendations-channel#attributes)below.)

Insert the program into the provider:  

### Kotlin

```kotlin
var programUri = context.contentResolver.insert(TvContractCompat.PreviewPrograms.CONTENT_URI,
        builder.build().toContentValues())
```

### Java

```java
Uri programUri = context.getContentResolver().insert(TvContractCompat.PreviewPrograms.CONTENT_URI,
      builder.build().toContentValues());
```

Retrieve the program ID for later reference:  

### Kotlin

```kotlin
val programId = ContentUris.parseId(programUri)
```

### Java

```java
long programId = ContentUris.parseId(programUri);
```

### Adding programs to the Watch Next channel

To insert programs into the Watch Next channel, see[Add programs to the Watch Next channel](https://developer.android.com/training/tv/discovery/watch-next-add-programs).

### Updating a program

You can change a program's information. For example, you may want to update the rental price for a the movie, or update a progress bar showing how much of a program the user has watched.

Use a`PreviewProgram.Builder`to set the attributes you need to change, then call`getContentResolver().update`to update the program. Specify the program ID that you saved when the program was originally added:  

### Kotlin

```kotlin
context.contentResolver.update(
        TvContractCompat.buildPreviewProgramUri(programId),
                builder.build().toContentValues(), null, null
)
```

### Java

```java
context.getContentResolver().update(TvContractCompat.buildPreviewProgramUri(programId),
    builder.build().toContentValues(), null, null);
```

### Deleting a program

### Kotlin

```kotlin
context.contentResolver
        .delete(TvContractCompat.buildPreviewProgramUri(programId), null, null)
```

### Java

```java
context.getContentResolver().delete(TvContractCompat.buildPreviewProgramUri(programId), null, null);
```

## Handling user actions

Your app can help users discover content by providing a UI to display and add channels. Your app should also handle interactions with your channels after they appear in the home screen.

### Discovering and adding channels

Your app can provide a UI element that lets the user select and add its channels (for example, a button that asks to add the channel).

After the user requests a specific channel, execute this code to get the user's permission to add it to the home screen UI:  

### Kotlin

```kotlin
val intent = Intent(TvContractCompat.ACTION_REQUEST_CHANNEL_BROWSABLE)
intent.putExtra(TvContractCompat.EXTRA_CHANNEL_ID, channelId)
try {
  activity.startActivityForResult(intent, 0)
} catch (e: ActivityNotFoundException) {
  // handle error
}
```

### Java

```java
Intent intent = new Intent(TvContractCompat.ACTION_REQUEST_CHANNEL_BROWSABLE);
intent.putExtra(TvContractCompat.EXTRA_CHANNEL_ID, channelId);
try {
   activity.startActivityForResult(intent, 0);
} catch (ActivityNotFoundException e) {
  // handle error
}
```

The system displays a dialog asking the user to approve the channel. Handle the result of the request in the`onActivityResult`method of your activity (`Activity.RESULT_CANCELED`or`Activity.RESULT_OK`).

### Android TV home screen events

When the user interacts with the programs/channels published by the app, the home screen sends intents to the app:

- The home screen sends the`Uri`stored in the APP_LINK_INTENT_URI attribute of a channel to the app when the user selects the channel's logo. The app should just launch its main UI or a view related to the selected channel.
- The home screen sends the`Uri`stored in the INTENT_URI attribute of a program to the app when the user selects a program. The app should play the selected content.
- The user can indicate that they are no longer interested in a program and want it removed from the home screen's UI. The system removes the program from the UI and sends the app that owns the program an intent (android.media.tv.ACTION_PREVIEW_PROGRAM_BROWSABLE_DISABLED or android.media.tv.ACTION_WATCH_NEXT_PROGRAM_BROWSABLE_DISABLED) with the program's ID. The app should remove the program from the provider and should NOT reinsert it.

Make sure to create intent filters for all the[Uris](https://developer.android.com/reference/android/net/Uri)that the home screen sends for user interactions; for example:  

    <receiver
       android:name=".WatchNextProgramRemoved"
       android:enabled="true"
       android:exported="true">
       <intent-filter>
           <action android:name="android.media.tv.ACTION_WATCH_NEXT_PROGRAM_BROWSABLE_DISABLED" />
       </intent-filter>
    </receiver>

## Best practices

- Many TV apps require that users login. In this case the`BroadcastReceiver`that listens for`android.media.tv.action.INITIALIZE_PROGRAMS`should suggest channel content for unauthenticated users. For example, your app can initially show the best content or currently popular content. After the user logs in, it can show personalized content. This is a great chance for apps to up-sell users before they login.
- When your app is not in the foreground and you need to update a channel or a program, use the`JobScheduler`to schedule the work (see:[JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler.html)and[JobService](https://developer.android.com/reference/android/app/job/JobService.html)).
- The system can revoke your app's provider permissions if your app misbehaves (for example: continuously spamming the provider with data). Make sure you wrap the code that accesses the provider with try-catch clauses to handle security exceptions.
- Before updating programs and channels, query the provider for the data you need to update and reconcile the data. For example, there is no need to update a program that the user wants removed from the UI. Use a background job that inserts/updates your data into the provider after querying for the existing data and then requesting approval for your channels. You can run this job when the app starts and whenever the app needs to update its data.

  ### Kotlin

  ```kotlin
  context.contentResolver
    .query(
        TvContractCompat.buildChannelUri(channelId),
            null, null, null, null).use({
                cursor-> if (cursor != null and cursor.moveToNext()) {
                             val channel = Channel.fromCursor(cursor)
                             if (channel.isBrowsable()) {
                                 //update channel's programs
                             }
                         }
            })
  ```

  ### Java

  ```java
  try (Cursor cursor = context.getContentResolver()
        .query(
            TvContractCompat.buildChannelUri(channelId),
            null,
            null,
            null,
            null)) {
                if (cursor != null && cursor.moveToNext()) {
                    Channel channel = Channel.fromCursor(cursor);
                    if (channel.isBrowsable()) {
                        //update channel's programs
                    }
                }
            }
  ```
- Use unique Uris for all images (logos, icons, content images). Be sure to use a different Uri when you update an image. All images are cached. If you do not change the Uri when you change the image, the old image will continue to appear.

- Remember that WHERE clauses are not allowed and calls to the providers with WHERE clauses will throw a security exception.

## Attributes

This section describes the channel and program attributes separately.

### Channel attributes

You must specify these attributes for every channel:

|      Attribute      |                                                                                                       Notes                                                                                                        |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE                | set to`TYPE_PREVIEW`.                                                                                                                                                                                              |
| DISPLAY_NAME        | set to the name of the channel.                                                                                                                                                                                    |
| APP_LINK_INTENT_URI | When the user selects the channel's logo the system sends an intent to start an activity that presents content relevant to the channel. Set this attribute to the Uri used in the intent filter for that activity. |

In addition, a channel also has six fields reserved for internal app usage. These fields can be used to store keys or other values that can help the app map the channel to its internal data structure:

- INTERNAL_PROVIDER_ID
- INTERNAL_PROVIDER_DATA
- INTERNAL_PROVIDER_FLAG1
- INTERNAL_PROVIDER_FLAG2
- INTERNAL_PROVIDER_FLAG3
- INTERNAL_PROVIDER_FLAG4

### Program attributes

See the individual pages for the attributes for each type of program:

- [Video Program Attributes](https://developer.android.com/training/tv/discovery/video-programs)
- [Audio Program Attributes](https://developer.android.com/training/tv/discovery/audio-programs)
- [Game Program Attributes](https://developer.android.com/training/tv/discovery/game-programs)
- [Watch Next Program Attributes](https://developer.android.com/training/tv/discovery/watch-next-programs)

## Sample Code

To learn more about building apps that interact with the home screen and add channels and programs to the Android TV home screen, see our home screen[codelab](https://developer.android.com/codelabs/tv-recommendations-kotlin#0).