---
title: https://developer.android.com/training/tv/discovery/watch-next-add-programs
url: https://developer.android.com/training/tv/discovery/watch-next-add-programs
source: md.txt
---

# Add programs to the Watch Next channel

The Watch Next channel is the second row that appears in the home screen, after the apps row. The system creates and maintains this channel. Your app can add programs to the Watch Next channel: programs that the user marked as interesting, stopped watching in the middle, or that are related to the content the user is watching (like the next episode in a series or next season of a show).
| **Note:** On the home screen, the Watch Next channel has the label**Play Next** . However, the Android classes used to manage the Watch Next channel are[`WatchNextProgram`](https://developer.android.com/reference/androidx/tvprovider/media/tv/WatchNextProgram)and[`WatchNextPrograms`](https://developer.android.com/reference/android/media/tv/TvContract.WatchNextPrograms). They have methods and constants with the stem "watchnext".

The Watch Next channel has some constraints: your app cannot move, remove, or hide the Watch Next channel's row.

## Steps

Inserting programs into the Watch Next channel is similar to[inserting programs into your own channel](https://developer.android.com/training/tv/discovery/recommendations-channel#add-programs). See the following sections for details specific to Watch Next.

Publishing to the Watch Next channel on Google TV (displayed as "Continue watching") requires prior approval by Google through a certification process and uses server-side processing to sort programs based on their attributes. To start the certification process, please submit this[linked form](https://docs.google.com/forms/d/e/1FAIpQLSeaNhHjDNM8osXPgkXeUQMSl5CntaEw0EeGYHIAc5jxUhQuHg/viewform).

When inserting content into the Watch Next channel, you must follow these guidelines:

- [Watch Next guidelines for app developers](https://developer.android.com/training/tv/discovery/guidelines-app-developers)
- [Watch Next guidelines for TV providers](https://developer.android.com/training/tv/discovery/guidelines-tv-providers)

### Select a type of program

There are four types of Watch Next programs. Select the appropriate type:

|            Type             |                                                                                            Notes                                                                                            |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WATCH_NEXT_TYPE_CONTINUE`  | The user stopped while watching content.                                                                                                                                                    |
| `WATCH_NEXT_TYPE_NEXT`      | The next available program in a series the user is watching is available. For example, if the user is watching episode 3 of a series, the app can suggest that they watch episode 4 next.   |
| `WATCH_NEXT_TYPE_NEW`       | New content that clearly follows what the user is watching is now available. For example, the user is watching episode number 5 from a series and episode 6 becomes available for watching. |
| `WATCH_NEXT_TYPE_WATCHLIST` | Inserted by the system or the app when the user saves a program.                                                                                                                            |

For more information, see[Watch Next attributes](https://developer.android.com/training/tv/discovery/watch-next-programs).

### Use the WatchNextProgram builder

Use a`WatchNextProgram.Builder`. For more information, see[Watch Next attributes](https://developer.android.com/training/tv/discovery/watch-next-programs).  

### Kotlin

```kotlin
val builder = WatchNextProgram.Builder()
builder.setType(TvContractCompat.WatchNextPrograms.TYPE_MOVIE)
        .setWatchNextType(TvContractCompat.WatchNextPrograms.WATCH_NEXT_TYPE_CONTINUE)
        .setLastEngagementTimeUtcMillis(time)
        .setTitle("Title")
        .setDescription("Program description")
        .setPosterArtUri(uri)
        .setIntentUri(uri)
        .setInternalProviderId(appProgramId)

val watchNextProgramUri = context.contentResolver
        .insert(TvContractCompat.WatchNextPrograms.CONTENT_URI,
                builder.build().toContentValues())
```

### Java

```java
WatchNextProgram.Builder builder = new WatchNextProgram.Builder();
builder.setType(TvContractCompat.WatchNextPrograms.TYPE_MOVIE)
        .setWatchNextType(TvContractCompat.WatchNextPrograms.WATCH_NEXT_TYPE_CONTINUE)
        .setLastEngagementTimeUtcMillis(time)
        .setTitle("Title")
        .setDescription("Program description")
        .setPosterArtUri(uri)
        .setIntentUri(uri)
        .setInternalProviderId(appProgramId);

Uri watchNextProgramUri = context.getContentResolver()
        .insert(TvContractCompat.WatchNextPrograms.CONTENT_URI, builder.build().toContentValues());
```

Use`TvContractCompat.buildWatchNextProgramUri(long watchNextProgramId)`to create the`Uri`you need to update a Watch Next program.

When the user adds a program to the Watch Next channel, the system copies the program to the row. It sends the intent`TvContractCompat.ACTION_PREVIEW_PROGRAM_ADDED_TO_WATCH_NEXT`to notify the app that the program has been added. The intent includes two extras: the program ID that was copied and the program ID created for the program in the Watch Next channel.