---
title: https://developer.android.com/training/tv/discovery/recommendations-row
url: https://developer.android.com/training/tv/discovery/recommendations-row
source: md.txt
---

# Recommendations in Android N and earlier

When interacting with TVs, users generally prefer to give minimal input before watching content. An ideal scenario for many TV users is: sit down, turn on, and watch. The fewest steps to get users to content they enjoy is generally the path they prefer.

**Note:** Use the APIs described here for making recommendations in apps running in Android versions up to and including Android 7.1 (API level 25) only. To supply recommendations for apps running in Android 8.0 (API level 26) and later, your app must use[recommendations channels](https://developer.android.com/training/tv/discovery/recommendations-channel).

The Android framework assists with minimum-input interaction by providing a recommendations row on the home screen. Content recommendations appear as the first row of the TV home screen after the first use of the device. Contributing recommendations from your app's content catalog can help bring users back to your app.
![](https://developer.android.com/static/images/tv/home-recommendations.png)

**Figure 1.**An example of the recommendations row.

This guide teaches you how to create recommendations and provide them to the Android framework so users can easily discover and enjoy your app content. See also the sample implementation in the[Leanback sample app](https://github.com/android/tv-samples/tree/main/Leanback).

## Best practices for recommendations

Recommendations help users quickly find the content and apps they enjoy. Creating recommendations that are high-quality and relevant to users is an important factor in creating a great user experience with your TV app. For this reason, you should carefully consider what recommendations you present to the user and manage them closely.

### Types of recommendations

When you create recommendations, you should link users back to incomplete viewing activities or suggest activities that extend that to related content. Here are some specific type of recommendations you should consider:

- **Continuation content**recommendations for the next episode for users to resume watching a series. Or, use continuation recommendations for paused movies, TV shows, or podcasts so users can get back to watching paused content in just a few clicks.
- **New content**recommendations, such as for a new first-run episode, if the user finished watching another series. Also, if your app lets users subscribe to, follow, or track content, use new content recommendations for unwatched items in their list of tracked content.
- **Related content**recommendations based on the users' historic viewing behavior.

For more information on how to design recommendation cards for the best user experience, see[Recommendation Row](https://www.google.com/design/spec-tv/system-overview/recommendation-row.html#recommendation-row-types-of-recommendations)in the Android TV Design Spec.

### Refresh recommendations

When refreshing recommendations, don't just remove and repost them, because doing so causes the recommendations to appear at the end of the recommendations row. Once a content item, such as a movie, has been played,[remove it](https://developer.android.com/guide/topics/ui/notifiers/notifications#Removing)from the recommendations.

### Customize recommendations

You can customize recommendation cards to convey branding information, by setting user interface elements such as the card's foreground and background image, color, app icon, title, and subtitle. To learn more, see[Recommendation Row](https://www.google.com/design/spec-tv/system-overview/recommendation-row.html#recommendation-row-card-customization)in the Android TV Design Spec.

### Group recommendations

You can optionally group recommendations based on recommendation source. For example, your app might provide two groups of recommendations: recommendations for content the user is subscribed to, and recommendations for new trending content the user might not be aware of.

The system ranks and orders recommendations for each group separately when creating or updating the recommendation row. By providing group information for your recommendations, you can ensure that your recommendations don't get ordered below unrelated recommendations.

Use[NotificationCompat.Builder.setGroup()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setGroup(java.lang.String))to set the group key string of a recommendation. For example, to mark a recommendation as belonging to a group that contains new trending content, you might call`setGroup("trending")`.

## Create a recommendations service

Content recommendations are created with background processing. In order for your application to contribute to recommendations, create a service that periodically adds listings from your app's catalog to the system's list of recommendations.

The following code example illustrates how to extend[IntentService](https://developer.android.com/reference/android/app/IntentService)to create a recommendation service for your application:  

### Kotlin

```kotlin
class UpdateRecommendationsService : IntentService("RecommendationService") {
    override protected fun onHandleIntent(intent: Intent) {
        Log.d(TAG, "Updating recommendation cards")
        val recommendations = VideoProvider.getMovieList()
        if (recommendations == null) return

        var count = 0

        try {
            val builder = RecommendationBuilder()
                    .setContext(applicationContext)
                    .setSmallIcon(R.drawable.videos_by_google_icon)

            for (entry in recommendations.entrySet()) {
                for (movie in entry.getValue()) {
                    Log.d(TAG, "Recommendation - " + movie.getTitle())

                    builder.setBackground(movie.getCardImageUrl())
                            .setId(count + 1)
                            .setPriority(MAX_RECOMMENDATIONS - count)
                            .setTitle(movie.getTitle())
                            .setDescription(getString(R.string.popular_header))
                            .setImage(movie.getCardImageUrl())
                            .setIntent(buildPendingIntent(movie))
                            .build()
                    if (++count >= MAX_RECOMMENDATIONS) {
                        break
                    }
                }
                if (++count >= MAX_RECOMMENDATIONS) {
                    break
                }
            }
        } catch (e: IOException) {
            Log.e(TAG, "Unable to update recommendation", e)
        }
    }

    private fun buildPendingIntent(movie: Movie): PendingIntent {
        val detailsIntent = Intent(this, DetailsActivity::class.java)
        detailsIntent.putExtra("Movie", movie)

        val stackBuilder = TaskStackBuilder.create(this)
        stackBuilder.addParentStack(DetailsActivity::class.java)
        stackBuilder.addNextIntent(detailsIntent)

        // Ensure a unique PendingIntents, otherwise all
        // recommendations end up with the same PendingIntent
        detailsIntent.setAction(movie.getId().toString())

        val intent = stackBuilder.getPendingIntent(0, PendingIntent.FLAG_UPDATE_CURRENT)
        return intent
    }

    companion object {
        private val TAG = "UpdateRecommendationsService"
        private val MAX_RECOMMENDATIONS = 3
    }
}
```

### Java

```java
public class UpdateRecommendationsService extends IntentService {
    private static final String TAG = "UpdateRecommendationsService";
    private static final int MAX_RECOMMENDATIONS = 3;

    public UpdateRecommendationsService() {
        super("RecommendationService");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        Log.d(TAG, "Updating recommendation cards");
        HashMap<String, List<Movie>> recommendations = VideoProvider.getMovieList();
        if (recommendations == null) return;

        int count = 0;

        try {
            RecommendationBuilder builder = new RecommendationBuilder()
                    .setContext(getApplicationContext())
                    .setSmallIcon(R.drawable.videos_by_google_icon);

            for (Map.Entry<String, List<Movie>> entry : recommendations.entrySet()) {
                for (Movie movie : entry.getValue()) {
                    Log.d(TAG, "Recommendation - " + movie.getTitle());

                    builder.setBackground(movie.getCardImageUrl())
                            .setId(count + 1)
                            .setPriority(MAX_RECOMMENDATIONS - count)
                            .setTitle(movie.getTitle())
                            .setDescription(getString(R.string.popular_header))
                            .setImage(movie.getCardImageUrl())
                            .setIntent(buildPendingIntent(movie))
                            .build();

                    if (++count >= MAX_RECOMMENDATIONS) {
                        break;
                    }
                }
                if (++count >= MAX_RECOMMENDATIONS) {
                    break;
                }
            }
        } catch (IOException e) {
            Log.e(TAG, "Unable to update recommendation", e);
        }
    }

    private PendingIntent buildPendingIntent(Movie movie) {
        Intent detailsIntent = new Intent(this, DetailsActivity.class);
        detailsIntent.putExtra("Movie", movie);

        TaskStackBuilder stackBuilder = TaskStackBuilder.create(this);
        stackBuilder.addParentStack(DetailsActivity.class);
        stackBuilder.addNextIntent(detailsIntent);
        // Ensure a unique PendingIntents, otherwise all
        // recommendations end up with the same PendingIntent
        detailsIntent.setAction(Long.toString(movie.getId()));

        PendingIntent intent = stackBuilder.getPendingIntent(0, PendingIntent.FLAG_UPDATE_CURRENT);
        return intent;
    }
}
```

In order for this service to be recognized by the system and run, register it using your app manifest. The following code snippet illustrates how to declare this class as a service:  

```xml
<manifest ... >
  <application ... >
    ...

    <service
            android:name="com.example.android.tvleanback.UpdateRecommendationsService"
            android:enabled="true" />
  </application>
</manifest>
```

## Build recommendations

Once your recommendation service starts running, it must create recommendations and pass them to the Android framework. The framework receives the recommendations as[Notification](https://developer.android.com/reference/android/app/Notification)objects that use a specific template and are marked with a specific category.

### Setting the values

To set the UI element values for the recommendation card, you create a builder class that follows the builder pattern described as follows. First, you set the values of the recommendation card elements.  

### Kotlin

```kotlin
class RecommendationBuilder {
    ...

    fun setTitle(title: String): RecommendationBuilder {
        this.title = title
        return this
    }

    fun setDescription(description: String): RecommendationBuilder {
        this.description = description
        return this
    }

    fun setImage(uri: String): RecommendationBuilder {
        imageUri = uri
        return this
    }

    fun setBackground(uri: String): RecommendationBuilder {
        backgroundUri = uri
        return this
    }

...
```

### Java

```java
public class RecommendationBuilder {
    ...

    public RecommendationBuilder setTitle(String title) {
            this.title = title;
            return this;
        }

        public RecommendationBuilder setDescription(String description) {
            this.description = description;
            return this;
        }

        public RecommendationBuilder setImage(String uri) {
            imageUri = uri;
            return this;
        }

        public RecommendationBuilder setBackground(String uri) {
            backgroundUri = uri;
            return this;
        }
...
```

### Create the notification

Once you've set the values, you then build the notification, assigning the values from the builder class to the notification, and calling[NotificationCompat.Builder.build()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#build()).

Also, be sure to call[setLocalOnly()](https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder#setLocalOnly(boolean))so the[NotificationCompat.BigPictureStyle](https://developer.android.com/reference/androidx/core/app/NotificationCompat.BigPictureStyle)notification won't show up on other devices.

The following code example demonstrates how to build a recommendation.  

### Kotlin

```kotlin
class RecommendationBuilder {
    ...

    @Throws(IOException::class)
    fun build(): Notification {
        ...

        val notification = NotificationCompat.BigPictureStyle(
        NotificationCompat.Builder(context)
                .setContentTitle(title)
                .setContentText(description)
                .setPriority(priority)
                .setLocalOnly(true)
                .setOngoing(true)
                .setColor(context.resources.getColor(R.color.fastlane_background))
                .setCategory(Notification.CATEGORY_RECOMMENDATION)
                .setLargeIcon(image)
                .setSmallIcon(smallIcon)
                .setContentIntent(intent)
                .setExtras(extras))
                .build()

        return notification
    }
}
```

### Java

```java
public class RecommendationBuilder {
    ...

    public Notification build() throws IOException {
        ...

        Notification notification = new NotificationCompat.BigPictureStyle(
                new NotificationCompat.Builder(context)
                        .setContentTitle(title)
                        .setContentText(description)
                        .setPriority(priority)
                        .setLocalOnly(true)
                        .setOngoing(true)
                        .setColor(context.getResources().getColor(R.color.fastlane_background))
                        .setCategory(Notification.CATEGORY_RECOMMENDATION)
                        .setLargeIcon(image)
                        .setSmallIcon(smallIcon)
                        .setContentIntent(intent)
                        .setExtras(extras))
                .build();

        return notification;
    }
}
```

## Run recommendations service

Your app's recommendation service must run periodically in order to create current recommendations. To run your service, create a class that runs a timer and invokes it at regular intervals. The following code example extends the[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)class to start periodic execution of a recommendation service every half hour:  

### Kotlin

```kotlin
class BootupActivity : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        Log.d(TAG, "BootupActivity initiated")
        if (intent.action.endsWith(Intent.ACTION_BOOT_COMPLETED)) {
            scheduleRecommendationUpdate(context)
        }
    }

    private fun scheduleRecommendationUpdate(context: Context) {
        Log.d(TAG, "Scheduling recommendations update")
        val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        val recommendationIntent = Intent(context, UpdateRecommendationsService::class.java)
        val alarmIntent = PendingIntent.getService(context, 0, recommendationIntent, 0)
        alarmManager.setInexactRepeating(AlarmManager.ELAPSED_REALTIME_WAKEUP,
                INITIAL_DELAY,
                AlarmManager.INTERVAL_HALF_HOUR,
                alarmIntent
        )
    }

    companion object {
        private val TAG = "BootupActivity"
        private val INITIAL_DELAY:Long = 5000
    }
}
```

### Java

```java
public class BootupActivity extends BroadcastReceiver {
    private static final String TAG = "BootupActivity";

    private static final long INITIAL_DELAY = 5000;

    @Override
    public void onReceive(Context context, Intent intent) {
        Log.d(TAG, "BootupActivity initiated");
        if (intent.getAction().endsWith(Intent.ACTION_BOOT_COMPLETED)) {
            scheduleRecommendationUpdate(context);
        }
    }

    private void scheduleRecommendationUpdate(Context context) {
        Log.d(TAG, "Scheduling recommendations update");

        AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
        Intent recommendationIntent = new Intent(context, UpdateRecommendationsService.class);
        PendingIntent alarmIntent = PendingIntent.getService(context, 0, recommendationIntent, 0);

        alarmManager.setInexactRepeating(AlarmManager.ELAPSED_REALTIME_WAKEUP,
                INITIAL_DELAY,
                AlarmManager.INTERVAL_HALF_HOUR,
                alarmIntent);
    }
}
```

This implementation of the[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)class must run after start up of the TV device where it is installed. To accomplish this, register this class in your app manifest with an intent filter that listens for the completion of the device boot process. The following sample code demonstrates how to add this configuration to the manifest:  

```xml
<manifest ... >
  <application ... >
    <receiver android:name="com.example.android.tvleanback.BootupActivity"
              android:enabled="true"
              android:exported="false">
      <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED"/>
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

**Important:** Receiving a boot completed notification requires that your app requests the[RECEIVE_BOOT_COMPLETED](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_BOOT_COMPLETED)permission. For more information, see[ACTION_BOOT_COMPLETED](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED).

In your recommendation service class'[onHandleIntent()](https://developer.android.com/reference/android/app/IntentService#onHandleIntent(android.content.Intent))method, post the recommendation to the manager as follows:  

### Kotlin

```kotlin
val notification = notificationBuilder.build()
notificationManager.notify(id, notification)
```

### Java

```java
Notification notification = notificationBuilder.build();
notificationManager.notify(id, notification);
```