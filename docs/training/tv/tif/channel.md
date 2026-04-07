---
title: Work with channel data  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/tif/channel
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Work with channel data Stay organized with collections Save and categorize content based on your preferences.



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

```
<uses-permission android:name="com.android.providers.tv.permission.WRITE_EPG_DATA" />
```

**Note:** The `READ_EPG_DATA` permission was deprecated in Android M (API 23) and is
no longer needed.

## Register channels in the database

The Android TV system database maintains records of channel data for TV inputs. In your setup
activity, for each of your channels, you must map your channel data to the following fields of the
`TvContract.Channels` class:

* `COLUMN_DISPLAY_NAME` - the displayed name of the
  channel
* `COLUMN_DISPLAY_NUMBER` - the displayed channel
  number
* `COLUMN_INPUT_ID` - the ID of the TV input service
* `COLUMN_SERVICE_TYPE` - the channel's service type
* `COLUMN_TYPE` - the channel's broadcast standard
  type
* `COLUMN_VIDEO_FORMAT` - the default video format
  for the channel

Although the TV input framework is generic enough to handle both traditional broadcast and
over-the-top (OTT) content without any distinction, you may want to define the following columns in
addition to those above to better identify traditional broadcast channels:

* `COLUMN_ORIGINAL_NETWORK_ID` - the television
  network ID
* `COLUMN_SERVICE_ID` - the service ID
* `COLUMN_TRANSPORT_STREAM_ID` - the transport stream
  ID

If you want to provide app link details for your channels, you need to
update some additional fields. For more information on app link fields, see
[Add app link information](#applink).

For internet streaming based TV inputs, assign your own values to the above accordingly so that
each channel can be identified uniquely.

Pull your channel metadata (in XML, JSON, or whatever) from your backend server, and in your setup
activity map the values to the system database as follows:

### Kotlin

```
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

```
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

1. **Channel number** (`COLUMN_DISPLAY_NUMBER`)- **Icon**
     ([`android:icon`](/guide/topics/manifest/application-element#icon) in the
     TV input's manifest)
   - **Program description** (`COLUMN_SHORT_DESCRIPTION`)- **Program title** (`COLUMN_TITLE`)
     - **Channel logo** (`TvContract.Channels.Logo`)
       * Use the color #EEEEEE to match the surrounding text
       * Don't include padding
     - **Poster art** (`COLUMN_POSTER_ART_URI`)
       * Aspect ratio between 16:9 and 4:3

![](/static/images/tv/channel-info.png)

**Figure 1.** The system TV app channel and program information presenter.

The system TV app provides the same information through the program guide, including poster art,
as shown in figure 2.

![](/static/images/tv/prog-guide.png)

**Figure 2.** The system TV app program guide.

## Update channel data

When updating existing channel data, use the
`update()`
method instead of deleting and re-adding the data. You can identify the current version of the data
by using `Channels.COLUMN_VERSION_NUMBER`
and `Programs.COLUMN_VERSION_NUMBER`
when choosing the records to update.

**Note:** Adding channel data to the `ContentProvider`
can take time. Add current programs (those within two hours of the current time)
only when you configure your `EpgSyncJobService` to update the rest
of the channel data in the background. See
the [Android TV Live TV Sample App](https://github.com/googlesamples/androidtv-sample-inputs/blob/3853daa98e919393ad9567684a2aac8e9e3741f7/app/src/main/java/com/example/android/sampletvinput/rich/RichSetupFragment.java#L65) for an example.

### Batch loading channel data

When updating the system database with a large amount of channel data, use the `ContentResolver`
`applyBatch()`
or
`bulkInsert()`
method. Here's an example using `applyBatch()`:

### Kotlin

```
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

```
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
not block the UI thread. Using an `AsyncTask` is one
way to perform updates asynchronously. For example, when loading channel info from a backend server,
you can use `AsyncTask` as follows:

### Kotlin

```
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
        context.contentResolver.openInputStream(videoUri).use { inputStream ->
            Xml.newPullParser().also { parser ->
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

```
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
[`WorkManager`](/topic/libraries/architecture/workmanager)
to run the update process during idle time, such as every day at 3:00 a.m.

Other techniques to separate the data update tasks from the UI thread include using the
`HandlerThread` class, or you may implement your own using `Looper`
and `Handler` classes. See [Processes and threads](/guide/components/processes-and-threads) for more information.

## Add app link information

Channels can use *app links* to let users easily launch a related
activity while they are watching channel content. Channel apps use
app links to extend user engagement by launching activities that show
related information or additional content. For example, you can use app links
to do the following:

* Guide the user to discover and purchase related content.
* Provide additional information about currently playing content.
* While viewing episodic content, start viewing the next episode in a
  series.
* Let the user interact with content—for example, rate or review
  content—without interrupting content playback.

App links are displayed when the user presses **Select** to show the
TV menu while watching channel content.

![](/static/images/training/tv/tif/app-link.png)

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
`TvContract.Channels` fields:

* `COLUMN_APP_LINK_COLOR` - The
  accent color of the app link for this channel. For an example accent color,
  see figure 2, callout 3.
* `COLUMN_APP_LINK_ICON_URI` -
  The URI for the app badge icon of the app link for this channel. For an
  example app badge icon, see figure 2, callout 2.
* `COLUMN_APP_LINK_INTENT_URI` -
  The intent URI of the app link for this channel. You can create the URI
  using `toUri(int)` with
  `URI_INTENT_SCHEME` and
  convert the URI back to the original intent with
  `parseUri()`.
* `COLUMN_APP_LINK_POSTER_ART_URI`
  - The URI for the poster art used as the background of the app link
  for this channel. For an example poster image, see figure 2, callout 1.
* `COLUMN_APP_LINK_TEXT` -
  The descriptive link text of the app link for this channel. For an example
  app link description, see the text in figure 2, callout 3.

![](/static/images/training/tv/tif/app-link-diagram.png)

[Previous

arrow\_back

Develop a TV input service](/training/tv/tif/tvinput)

[Next

Manage TV user interaction

arrow\_forward](/training/tv/tif/ui)