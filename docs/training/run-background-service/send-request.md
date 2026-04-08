---
title: Send work requests to the background service  |  Android Developers
url: https://developer.android.com/training/run-background-service/send-request
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Send work requests to the background service Stay organized with collections Save and categorize content based on your preferences.



**Note:** This page is left here as reference for legacy apps only.
See the [guide to background processing on Android](/guide/background)  for recommended
solutions.

The previous lesson showed you how to create a
[`JobIntentService`](/reference/androidx/core/app/JobIntentService) class. This
lesson shows you how to trigger the
[`JobIntentService`](/reference/androidx/core/app/JobIntentService) to run an operation by
enqueuing work with an [`Intent`](/reference/android/content/Intent).
This [`Intent`](/reference/android/content/Intent) can
optionally contain data for the
[`JobIntentService`](/reference/androidx/core/app/JobIntentService) to process.

## Create and send a work request to a JobIntentService

To create a work request and send it to a
[`JobIntentService`](/reference/androidx/core/app/JobIntentService),
create an [`Intent`](/reference/android/content/Intent) and enqueue it to
be executed by calling [`enqueueWork()`](/reference/androidx/core/app/JobIntentService#enqueuework).
Optionally you can add data to the intent (in the form of intent extras) for the
JobIntentService to process. For more information about creating intents, read the Building an
intent section in [Intents and Intent Filters](/guide/components/intents-filters)

The following code snippets demonstrate this process:

1. Create a new [`Intent`](/reference/android/content/Intent) for the
   [`JobIntentService`](/reference/androidx/core/app/JobIntentService) called `RSSPullService`.
     

   ### Kotlin

   ```
   /*
    * Creates a new Intent to start the RSSPullService
    * JobIntentService. Passes a URI in the
    * Intent's "data" field.
    */
   serviceIntent = Intent().apply {
       putExtra("download_url", dataUrl)
   }
   ```

   ### Java

   ```
   /*
    * Creates a new Intent to start the RSSPullService
    * JobIntentService. Passes a URI in the
    * Intent's "data" field.
    */
   serviceIntent = new Intent();
   serviceIntent.putExtra("download_url", dataUrl));
   ```
2. Call [`enqueueWork()`](/reference/androidx/core/app/JobIntentService#enqueuework)
     

   ### Kotlin

   ```
   private const val RSS_JOB_ID = 1000
   RSSPullService.enqueueWork(context, RSSPullService::class.java, RSS_JOB_ID, serviceIntent)
   ```

   ### Java

   ```
   // Starts the JobIntentService
   private static final int RSS_JOB_ID = 1000;
   RSSPullService.enqueueWork(getContext(), RSSPullService.class, RSS_JOB_ID, serviceIntent);
   ```

Notice that you can send the work request from anywhere in an Activity or Fragment.
For example, if you need to get user input first, you can send the request from a callback
that responds to a button click or similar gesture.

Once you call [`enqueueWork()`](/reference/androidx/core/app/JobIntentService#enqueuework),
the [`JobIntentService`](/reference/androidx/core/app/JobIntentService) does the work defined in its
[`onHandleWork()`](/reference/androidx/core/app/JobIntentService#onHandleWork) method, and then stops itself.

The next step is to report the results of the work request back to the originating Activity
or Fragment. The next lesson shows you how to do this with a
`BroadcastReceiver`.