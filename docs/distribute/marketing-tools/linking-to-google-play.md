---
title: https://developer.android.com/distribute/marketing-tools/linking-to-google-play
url: https://developer.android.com/distribute/marketing-tools/linking-to-google-play
source: md.txt
---

Google Play provides several link formats that let you bring users to your
products in the way you want, from Android apps, web pages, ads, reviews,
articles, social media posts, and more.
To link to your app with the Google Play badge, visit the [badge generator](https://developer.android.com/distribute/tools/promote/badges). ![Get it on Google Play](https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png)

The link formats let you link to the following:

- An app's [store listing](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#OpeningDetails).
- A [developer's page](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#OpeningPublisher).
- A [search result](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#PerformingSearch) of your choice.
- A [collection](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#OpeningCollection).
- A [Google Play Instant experience](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#Instant).

## Linking to a store listing

Use the format below to deep-link directly to an app's Store listing page, where
users can see the app description, screenshots, reviews and more, and then
install it.

To create the link, you need to know the app's fully qualified *package name* ,
which is declared in the app's [manifest
file](https://developer.android.com/guide/topics/manifest/manifest-element#package). The package name is
also visible in the Google Play Console.

    https://play.google.com/store/apps/details?id=<package_name>

Here's an example:

```
http://play.google.com/store/apps/details?id=com.google.android.apps.maps
```

For details on how to send the link in an Android app, see [Linking from an
Android App](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#android-app).

## Linking to a developer page

Use the format below to link users to your [developer page](https://support.google.com/googleplay/android-developer/answer/6226441). On this page you can provide more details about your brand,
feature an app, and provide a list of other apps you've published.

To create the link, you need to know your *publisher name*, which is available
from the Play Console.

    https://play.google.com/store/apps/dev?id=<developer_id>

Here's an example:

```
https://play.google.com/store/apps/dev?id=5700313618786177705
```

For details on how to send the link in an Android app, see [Linking from an
Android App](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#android-app).

## Linking to a search result

Use the format below to link users to a search query result on Google Play. The
search result page shows a list of apps (and optionally other content) that
match the query, with ratings, badges, and an install button for each.

To create the link, you just need a search query string. If you want the query
to search beyond the Google Play app listings, remove the `&c=apps` part of the
link URL.

    https://play.google.com/store/search?q=<search_query>&c=apps

Here's an example:

```
https://play.google.com/store/search?q=maps&c=apps
```

For details on how to send the link in an Android app, see [Linking from an
Android App](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#android-app).

## Linking to a collection

If your app is featured or appears in one of the Google Play top charts or
collections, you can use the format below to link users directly to the
collection. The collection shows a ranked list of apps in the collection, with
ratings, short descriptions, and an install button.

    https://play.google.com/store/apps/collection/<collection_name>

Here's an example:

```
https://play.google.com/store/apps/collection/topselling_free
```

For details on how to send the link in an Android app, see [Linking from an
Android App](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#android-app).


**Table 1.** Collections on Google Play.

| Collection | collection_name |
|---|---|
| Staff Picks (Featured) | featured |
| Top Paid | topselling_paid |
| Top Free | topselling_free |
| Top New Free | topselling_new_free |
| Top New Paid | topselling_new_paid |
| Top Grossing | topgrossing |
| Trending | movers_shakers |

## Linking to Editors' Choice Pages

If your app is featured or appears in articles in Editors' Choice, you can use
the format below to link users directly to the Editors' Choice page.

The URL for the main Editors' Choice page is:

```
https://play.google.com/store/apps/topic?id=editors_choice
```

And you can find each page's URL from the Editors' Choice page.

Here are some examples:

- [**Get Motivated With These 5 Fitness Apps**
  `https://play.google.com/store/apps/topic?id=editorial_fitness_apps_us`](https://play.google.com/store/apps/topic?id=editorial_fitness_apps_us)
- [**Map It Out: Navigate Anywhere With These 5 Apps**
  `https://play.google.com/store/apps/topic?id=editorial_navigation_apps_us`](https://play.google.com/store/apps/topic?id=editorial_navigation_apps_us)
- [**Winning Sports Games to Enjoy Any Season**
  `https://play.google.com/store/apps/topic?id=editorial_sports_games_us`](https://play.google.com/store/apps/topic?id=editorial_sports_games_us)

## Linking from an Android App

If you want to link to your products from an Android app, create an
[`Intent`](https://developer.android.com/reference/android/content/Intent) that opens a URL. As you
configure this intent, pass `"com.android.vending"` into `Intent.setPackage()`
so that users see your app's details in the Google Play Store app instead of a
[chooser](https://developer.android.com/training/basics/intents/sending#AppChooser).

The following example directs users to viewing the app containing the package
name `com.example.android` in Google Play:

### Kotlin

```kotlin
val intent = Intent(Intent.ACTION_VIEW).apply {
    data = Uri.parse(
            "https://play.google.com/store/apps/details?id=com.example.android")
    setPackage("com.android.vending")
}
startActivity(intent)
```

### Java

```java
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setData(Uri.parse(
        "https://play.google.com/store/apps/details?id=com.example.android"));
intent.setPackage("com.android.vending");
startActivity(intent);
```

## Launching a Google Play Instant experience

If you have published an instant app using
[Google Play Instant](https://developer.android.com/topic/google-play-instant), you can
launch the app as follows:

### Kotlin

```kotlin
val uriBuilder = Uri.parse("https://play.google.com/store/apps/details")
        .buildUpon()
        .appendQueryParameter("id", "com.example.android")
        .appendQueryParameter("launch", "true")

// Optional parameters, such as referrer, are passed onto the launched
// instant app. You can retrieve these parameters using Activity.intent.data.
uriBuilder.appendQueryParameter("referrer", "exampleCampaignId")

val intent = Intent(Intent.ACTION_VIEW).apply {
    data = uriBuilder.build()
    setPackage("com.android.vending")
}
startActivity(intent)
```

### Java

```java
Intent intent = new Intent(Intent.ACTION_VIEW);
Uri.Builder uriBuilder = Uri.parse("market://launch")
    .buildUpon()
    .appendQueryParameter("id", "com.example.android");

// Optional parameters, such as referrer, are passed onto the launched
// instant app. You can retrieve these parameters using
// Activity.getIntent().getData().
uriBuilder.appendQueryParameter("referrer", "exampleCampaignId");

intent.setData(uriBuilder.build());
intent.setPackage("com.android.vending");
startActivity(intent);
```

> [!NOTE]
> **Note:** If Google Play Instant isn't enabled on the device, the store listing is shown.

## Summary of URL formats

The table below provides a summary of the URIs currently supported by the Google
Play (both on the web and in an Android application), as discussed in the
previous sections.

| For this result | Use this link |
|---|---|
| Show the store listing for a specific app | `https://play.google.com/store/apps/details?id=<package_name>` |
| Show the developer page for a specific publisher | `https://play.google.com/store/apps/dev?id=<developer_id>` |
| Show the result of a search query | `https://play.google.com/store/search?q=<query>` |
| Show an app collection | `https://play.google.com/store/apps/collection/<collection_name>` |
| Launch a Google Play Instant experience | `market://launch?id=<package_name>` |