---
title: https://developer.android.com/training/tv/tif/channel
url: https://developer.android.com/training/tv/tif/channel
source: md.txt
---

Your TV input must provide Electronic Program Guide (EPG) data for at least
one channel in its setup activity. You should also periodically update that
data, with consideration for the size of the update and the processing thread
that handles it. Additionally, you can provide app links for channels
that guide the user to related content and activities.
This lesson discusses creating and updating channel and program data on the
system database with these considerations in mind.


Try the [TV Input Service](https://github.com/googlesamples/androidtv-sample-inputs) sample app.

## Get permission

In order for your TV input to work with EPG data, it must declare the
write permission in its Android manifest file as follows:

```xml
<uses-permission android:name="com.android.providers.tv.permission.WRITE_EPG_DA>TA" /
```
| **Note:** The `READ_EPG_DATA` permission was deprecated in Android M (API 23) and is no longer needed.

## Register channels in the database

The Android TV system database maintains records of channel data for TV inputs. In your setup
activity, for each of your channels, you must map your channel data to the following fields of the
`https://developer.android.com/reference/android/media/tv/TvContract.Channels` class:

- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_DISPLAY_NAME` - the displayed name of the channel
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_DISPLAY_NUMBER` - the displayed channel number
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_INPUT_ID` - the ID of the TV input service
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_SERVICE_TYPE` - the channel's service type
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_TYPE` - the channel's broadcast standard type
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_VIDEO_FORMAT` - the default video format for the channel

Although the TV input framework is generic enough to handle both traditional broadcast and
over-the-top (OTT) content without any distinction, you may want to define the following columns in
addition to those above to better identify traditional broadcast channels:

- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_ORIGINAL_NETWORK_ID` - the television network ID
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_SERVICE_ID` - the service ID
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_TRANSPORT_STREAM_ID` - the transport stream ID

If you want to provide app link details for your channels, you need to
update some additional fields. For more information on app link fields, see
[Add app link information](https://developer.android.com/training/tv/tif/channel#applink).

For internet streaming based TV inputs, assign your own values to the above accordingly so that
each channel can be identified uniquely.

Pull your channel metadata (in XML, JSON, or whatever) from your backend server, and in your setup
activity map the values to the system database as follows:

### Kotlin

```kotlin
val values = ContentValues().apply {
    put(TvContract.Channels.COLUMN_DISPLAY_NUMBER, channel.number)
    put(TvContract.Channels.COLUMN_DISPLAY_NAME, channel.name)
    put(TvContract.Channels.COLUMN_ORIGINAL_NETWORK_ID, channel.originalNetworkId)
    put(TvContract.Channels.COLUMN_TRANSPORT_STREAM_ID, channel.transportStreamId)
    put(TvContract.Channels.COLUMN_SERVICE_ID, channel.serviceId)
    put(TvContract.Channels.COLUMN_VIDEO_FORMAT, channel.videoFormat)
}
val uri = context.contentResolver.insert(TvContract.Channels.CONTENT_URI, values)
```

### Java

```java
ContentValues values = new ContentValues();

values.put(Channels.COLUMN_DISPLAY_NUMBER, channel.number);
values.put(Channels.COLUMN_DISPLAY_NAME, channel.name);
values.put(Channels.COLUMN_ORIGINAL_NETWORK_ID, channel.originalNetworkId);
values.put(Channels.COLUMN_TRANSPORT_STREAM_ID, channel.transportStreamId);
values.put(Channels.COLUMN_SERVICE_ID, channel.serviceId);
values.put(Channels.COLUMN_VIDEO_FORMAT, channel.videoFormat);

Uri uri = context.getContentResolver().insert(TvContract.Channels.CONTENT_URI, values);
```

In the example above, `channel` is an object which holds channel metadata from the
backend server.

### Present channel and program information

The system TV app presents channel and program information to users as they flip through channels,
as shown in figure 1. To make sure the channel and program information works with the system TV app's
channel and program information presenter, follow the guidelines below.

1. **Channel number** (`https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_DISPLAY_NUMBER`)
2. **Icon** ([`android:icon`](https://developer.android.com/guide/topics/manifest/application-element#icon) in the TV input's manifest)
3. **Program description** (`https://developer.android.com/reference/android/media/tv/TvContract.Programs#COLUMN_SHORT_DESCRIPTION`)
4. **Program title** (`https://developer.android.com/reference/android/media/tv/TvContract.Programs#COLUMN_TITLE`)
5. **Channel logo** (`https://developer.android.com/reference/android/media/tv/TvContract.Channels.Logo`)
   - Use the color #EEEEEE to match the surrounding text
   - Don't include padding
6. **Poster art** (`https://developer.android.com/reference/android/media/tv/TvContract.Programs#COLUMN_POSTER_ART_URI`)
   - Aspect ratio between 16:9 and 4:3

![](https://developer.android.com/static/images/tv/channel-info.png)


**Figure 1.** The system TV app channel and program information presenter.

The system TV app provides the same information through the program guide, including poster art,
as shown in figure 2.
![](https://developer.android.com/static/images/tv/prog-guide.png)


**Figure 2.** The system TV app program guide.

## Update channel data

When updating existing channel data, use the
`https://developer.android.com/reference/android/content/ContentProvider#update(android.net.Uri, android.content.ContentValues, java.lang.String, java.lang.String[])`
method instead of deleting and re-adding the data. You can identify the current version of the data
by using `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_VERSION_NUMBER`
and `https://developer.android.com/reference/android/media/tv/TvContract.Programs#COLUMN_VERSION_NUMBER`
when choosing the records to update.

**Note:** Adding channel data to the `https://developer.android.com/reference/android/content/ContentProvider`
can take time. Add current programs (those within two hours of the current time)
only when you configure your `EpgSyncJobService` to update the rest
of the channel data in the background. See
the [Android TV Live TV Sample App](https://github.com/googlesamples/androidtv-sample-inputs/blob/3853daa98e919393ad9567684a2aac8e9e3741f7/app/src/main/java/com/example/android/sampletvinput/rich/RichSetupFragment.java#L65) for an example.

### Batch loading channel data

When updating the system database with a large amount of channel data, use the `https://developer.android.com/reference/android/content/ContentResolver`
`https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)`
or
`https://developer.android.com/reference/android/content/ContentResolver#bulkInsert(android.net.Uri, android.content.ContentValues[])`
method. Here's an example using `https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)`:


### Kotlin

```kotlin
val ops = ArrayList<ContentProviderOperation>()
val programsCount = channelInfo.mPrograms.size
channelInfo.mPrograms.forEachIndexed { index, program ->
    ops += ContentProviderOperation.newInsert(
            TvContract.Programs.CONTENT_URI).run {
        withValues(programs[index])
        withValue(TvContract.Programs.COLUMN_START_TIME_UTC_MILLIS, programStartSec * 1000)
        withValue(
                TvContract.Programs.COLUMN_END_TIME_UTC_MILLIS,
                (programStartSec + program.durationSec) * 1000
        )
        build()
    }
    programStartSec += program.durationSec
    if (index % 100 == 99 || index == programsCount - 1) {
        try {
            contentResolver.applyBatch(TvContract.AUTHORITY, ops)
        } catch (e: RemoteException) {
            Log.e(TAG, "Failed to insert programs.", e)
            return
        } catch (e: OperationApplicationException) {
            Log.e(TAG, "Failed to insert programs.", e)
            return
        }
        ops.clear()
    }
}
```

### Java

```java
ArrayList<ContentProviderOperation> ops = new ArrayList<>();
int programsCount = channelInfo.mPrograms.size();
for (int j = 0; j < programsCount; ++j) {
    ProgramInfo program = channelInfo.mPrograms.get(j);
    ops.add(ContentProviderOperation.newInsert(
            TvContract.Programs.CONTENT_URI)
            .withValues(programs.get(j))
            .withValue(Programs.COLUMN_START_TIME_UTC_MILLIS,
                    programStartSec * 1000)
            .withValue(Programs.COLUMN_END_TIME_UTC_MILLIS,
                    (programStartSec + program.durationSec) * 1000)
            .build());
    programStartSec = programStartSec + program.durationSec;
    if (j % 100 == 99 || j == programsCount - 1) {
        try {
            getContentResolver().applyBatch(TvContract.AUTHORITY, ops);
        } catch (RemoteException | OperationApplicationException e) {
            Log.e(TAG, "Failed to insert programs.", e);
            return;
        }
        ops.clear();
    }
}
```

### Process channel data asynchronously

Data manipulation, such as fetching a stream from the server or accessing the database, should
not block the UI thread. Using an `https://developer.android.com/reference/android/os/AsyncTask` is one
way to perform updates asynchronously. For example, when loading channel info from a backend server,
you can use `https://developer.android.com/reference/android/os/AsyncTask` as follows:

### Kotlin

```kotlin
private class LoadTvInputTask(val context: Context) : AsyncTask<Uri, Unit, Unit>() {

    override fun doInBackground(vararg uris: Uri) {
        try {
            fetchUri(uris[0])
        } catch (e: IOException) {
            Log.d("LoadTvInputTask", "fetchUri error")
        }
    }

    @Throws(IOException::class)
    private fun fetchUri(videoUri: Uri) {
        context.contentResolver.openInputStream(videoUri)>.use { inputStream -
            Xml.newPullPars>er().also { parser -
                try {
                    parser.setFeature(XmlPullParser.FEATURE_PROCESS_NAMESPACES, false)
                    parser.setInput(inputStream, null)
                    sTvInput = ChannelXMLParser.parseTvInput(parser)
                    sSampleChannels = ChannelXMLParser.parseChannelXML(parser)
                } catch (e: XmlPullParserException) {
                    e.printStackTrace()
                }
            }
        }
    }
}
```

### Java

```java
private static class LoadTvInputTask extends AsyncTask<Uri, Void, Void> {

    private Context mContext;

    public LoadTvInputTask(Context context) {
        mContext = context;
    }

    @Override
    protected Void doInBackground(Uri... uris) {
        try {
            fetchUri(uris[0]);
        } catch (IOException e) {
          Log.d("LoadTvInputTask", "fetchUri error");
        }
        return null;
    }

    private void fetchUri(Uri videoUri) throws IOException {
        InputStream inputStream = null;
        try {
            inputStream = mContext.getContentResolver().openInputStream(videoUri);
            XmlPullParser parser = Xml.newPullParser();
            try {
                parser.setFeature(XmlPullParser.FEATURE_PROCESS_NAMESPACES, false);
                parser.setInput(inputStream, null);
                sTvInput = ChannelXMLParser.parseTvInput(parser);
                sSampleChannels = ChannelXMLParser.parseChannelXML(parser);
            } catch (XmlPullParserException e) {
                e.printStackTrace();
            }
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
        }
    }
}
```

If you need to update EPG data on a regular basis, consider using
[`WorkManager`](https://developer.android.com/topic/libraries/architecture/workmanager)
to run the update process during idle time, such as every day at 3:00 a.m.

Other techniques to separate the data update tasks from the UI thread include using the
`https://developer.android.com/reference/android/os/HandlerThread` class, or you may implement your own using `https://developer.android.com/reference/android/os/Looper`
and `https://developer.android.com/reference/android/os/Handler` classes. See [Processes and threads](https://developer.android.com/guide/components/processes-and-threads) for more information.

## Add app link information

Channels can use *app links* to let users easily launch a related
activity while they are watching channel content. Channel apps use
app links to extend user engagement by launching activities that show
related information or additional content. For example, you can use app links
to do the following:

- Guide the user to discover and purchase related content.
- Provide additional information about currently playing content.
- While viewing episodic content, start viewing the next episode in a series.
- Let the user interact with content---for example, rate or review content---without interrupting content playback.

App links are displayed when the user presses **Select** to show the
TV menu while watching channel content.
![](https://developer.android.com/static/images/training/tv/tif/app-link.png)

**Figure 1.** An example app link
displayed on the **Channels** row while channel content is shown.

When the user selects the app link, the system starts an activity using
an intent URI specified by the channel app. Channel content continues to play
while the app link activity is active. The user can return to the channel
content by pressing **Back**.

### Provide app link channel data

Android TV automatically creates an app link for each channel,
using information from the channel data. To provide app link information,
specify the following details in your
`https://developer.android.com/reference/android/media/tv/TvContract.Channels` fields:

- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_COLOR` - The accent color of the app link for this channel. For an example accent color, see figure 2, callout 3.
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_ICON_URI` - The URI for the app badge icon of the app link for this channel. For an example app badge icon, see figure 2, callout 2.
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_INTENT_URI` - The intent URI of the app link for this channel. You can create the URI using `https://developer.android.com/reference/android/content/Intent#toUri(int)` with `https://developer.android.com/reference/android/content/Intent#URI_INTENT_SCHEME` and convert the URI back to the original intent with `https://developer.android.com/reference/android/content/Intent#parseUri(java.lang.String, int)`.
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_POSTER_ART_URI` - The URI for the poster art used as the background of the app link for this channel. For an example poster image, see figure 2, callout 1.
- `https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_TEXT` - The descriptive link text of the app link for this channel. For an example app link description, see the text in figure 2, callout 3.

![](https://developer.android.com/static/images/training/tv/tif/app-link-diagram.png)

**Figure 2.** App link details.

If the channel data doesn't specify app link information, the system
creates a default app link. The system chooses default details as follows:

- For the intent URI (`https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_INTENT_URI`), the system uses the `https://developer.android.com/reference/android/content/Intent#ACTION_MAIN` activity for the `https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER` category, typically defined in the app manifest. If this activity is not defined, a non-functioning app link appears---if the user clicks it, nothing happens.
- For the descriptive text (`https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_TEXT`), the system uses "Open <var translate="no">app-name</var>". If no viable app link intent URI is defined, the system uses "No link available".
- For the accent color (`https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_COLOR`), the system uses the default app color.
- For the poster image (`https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_POSTER_ART_URI`), the system uses the app's home screen banner. If the app doesn't provide a banner, the system uses a default TV app image.
- For the badge icon (`https://developer.android.com/reference/android/media/tv/TvContract.Channels#COLUMN_APP_LINK_ICON_URI`), the system uses a badge that shows the app name. If the system is also using the app banner or default app image for the poster image, no app badge is shown.

You specify app link details for your channels in your app's
setup activity. You can update these app link details at any point, so
if an app link needs to match channel changes, update app
link details and call
`https://developer.android.com/reference/android/content/ContentResolver#update(android.net.Uri, android.content.ContentValues, java.lang.String, java.lang.String[])` as needed. For more details on updating
channel data, see [Update channel data](https://developer.android.com/training/tv/tif/channel#update).