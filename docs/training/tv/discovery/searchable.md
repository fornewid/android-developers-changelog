---
title: https://developer.android.com/training/tv/discovery/searchable
url: https://developer.android.com/training/tv/discovery/searchable
source: md.txt
---

# Make TV apps searchable

Android TV uses the Android[search interface](https://developer.android.com/guide/topics/search)to retrieve content data from installed apps and deliver search results to the user. Your app's content data can be included with these results to give the user instant access to the content in your app.

Your app must provide Android TV with the data fields from which Android TV can generate suggested search results as the user enters characters in the search dialog. To do that, your app must implement a[Content Provider](https://developer.android.com/guide/topics/providers/content-providers)that serves up the suggestions along with a[`searchable.xml`](https://developer.android.com/guide/topics/search/searchable-config)configuration file that describes the content provider and other vital information for Android TV. You also need an activity that handles the intent that fires when the user selects a suggested search result. For more detail, see[Add custom search suggestions](https://developer.android.com/guide/topics/search/adding-custom-suggestions). This guide covers the main points specific to Android TV apps.

Before reading this guide, make sure you are familiar with the concepts explained in the[Search API guide](https://developer.android.com/guide/topics/search). Also, review[Add search functionality](https://developer.android.com/training/search).

The sample code in this guide comes from the[Leanback sample app](https://github.com/android/tv-samples/tree/main/Leanback).
| **Note:** Android TV's search interface also retrieves content from Google search servers that has been marked for use with Google*media actions* . If you add your content with media action markup to Google's search index, your content appears in the Android TV search results with a UI that users can use to start viewing the content in your app. For more information about media actions, see[Media Actions](https://developers.google.com/actions/media/).

## Identify columns

The[SearchManager](https://developer.android.com/reference/android/app/SearchManager)describes the data fields it expects by representing them as columns of a local database. Regardless of your data's format, you must map your data fields to these columns, usually in the class that accessess your content data. For information about building a class that maps your existing data to the required fields, see[Building a suggestion table](https://developer.android.com/guide/topics/search/adding-custom-suggestions#SuggestionTable).

The`SearchManager`class includes several columns for Android TV. Some of the more important columns are described in the following table.

|               Value                |                      Description                      |
|------------------------------------|-------------------------------------------------------|
| `SUGGEST_COLUMN_TEXT_1`            | The name of your content (required)                   |
| `SUGGEST_COLUMN_TEXT_2`            | A text description of your content                    |
| `SUGGEST_COLUMN_RESULT_CARD_IMAGE` | An image, poster, or cover for your content           |
| `SUGGEST_COLUMN_CONTENT_TYPE`      | The MIME type of your media                           |
| `SUGGEST_COLUMN_VIDEO_WIDTH`       | The resolution width of your media                    |
| `SUGGEST_COLUMN_VIDEO_HEIGHT`      | The resolution height of your media                   |
| `SUGGEST_COLUMN_PRODUCTION_YEAR`   | The production year of your content (required)        |
| `SUGGEST_COLUMN_DURATION`          | The duration in milliseconds of your media (required) |

The search framework requires the following columns:

- [SUGGEST_COLUMN_TEXT_1](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_TEXT_1)
- [SUGGEST_COLUMN_PRODUCTION_YEAR](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_PRODUCTION_YEAR)
- [SUGGEST_COLUMN_DURATION](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_DURATION)

When the values of these columns for your content match the values for the same content from other providers found by Google servers, the system provides a[deep link](https://developer.android.com/training/app-indexing/deep-linking)to your app in the details view for the content, along with links to the apps of other providers. This is discussed more in the[Deep link to your app in the details screen](https://developer.android.com/training/tv/discovery/searchable#details)section.

Your application's database class might define the columns as follows:  

### Kotlin

```kotlin
class VideoDatabase {
    companion object {
        // The columns we'll include in the video database table
        val KEY_NAME = SearchManager.SUGGEST_COLUMN_TEXT_1
        val KEY_DESCRIPTION = SearchManager.SUGGEST_COLUMN_TEXT_2
        val KEY_ICON = SearchManager.SUGGEST_COLUMN_RESULT_CARD_IMAGE
        val KEY_DATA_TYPE = SearchManager.SUGGEST_COLUMN_CONTENT_TYPE
        val KEY_IS_LIVE = SearchManager.SUGGEST_COLUMN_IS_LIVE
        val KEY_VIDEO_WIDTH = SearchManager.SUGGEST_COLUMN_VIDEO_WIDTH
        val KEY_VIDEO_HEIGHT = SearchManager.SUGGEST_COLUMN_VIDEO_HEIGHT
        val KEY_AUDIO_CHANNEL_CONFIG = SearchManager.SUGGEST_COLUMN_AUDIO_CHANNEL_CONFIG
        val KEY_PURCHASE_PRICE = SearchManager.SUGGEST_COLUMN_PURCHASE_PRICE
        val KEY_RENTAL_PRICE = SearchManager.SUGGEST_COLUMN_RENTAL_PRICE
        val KEY_RATING_STYLE = SearchManager.SUGGEST_COLUMN_RATING_STYLE
        val KEY_RATING_SCORE = SearchManager.SUGGEST_COLUMN_RATING_SCORE
        val KEY_PRODUCTION_YEAR = SearchManager.SUGGEST_COLUMN_PRODUCTION_YEAR
        val KEY_COLUMN_DURATION = SearchManager.SUGGEST_COLUMN_DURATION
        val KEY_ACTION = SearchManager.SUGGEST_COLUMN_INTENT_ACTION
        ...
    }
    ...
}
```

### Java

```java
public class VideoDatabase {
    // The columns we'll include in the video database table
    public static final String KEY_NAME = SearchManager.SUGGEST_COLUMN_TEXT_1;
    public static final String KEY_DESCRIPTION = SearchManager.SUGGEST_COLUMN_TEXT_2;
    public static final String KEY_ICON = SearchManager.SUGGEST_COLUMN_RESULT_CARD_IMAGE;
    public static final String KEY_DATA_TYPE = SearchManager.SUGGEST_COLUMN_CONTENT_TYPE;
    public static final String KEY_IS_LIVE = SearchManager.SUGGEST_COLUMN_IS_LIVE;
    public static final String KEY_VIDEO_WIDTH = SearchManager.SUGGEST_COLUMN_VIDEO_WIDTH;
    public static final String KEY_VIDEO_HEIGHT = SearchManager.SUGGEST_COLUMN_VIDEO_HEIGHT;
    public static final String KEY_AUDIO_CHANNEL_CONFIG =
            SearchManager.SUGGEST_COLUMN_AUDIO_CHANNEL_CONFIG;
    public static final String KEY_PURCHASE_PRICE = SearchManager.SUGGEST_COLUMN_PURCHASE_PRICE;
    public static final String KEY_RENTAL_PRICE = SearchManager.SUGGEST_COLUMN_RENTAL_PRICE;
    public static final String KEY_RATING_STYLE = SearchManager.SUGGEST_COLUMN_RATING_STYLE;
    public static final String KEY_RATING_SCORE = SearchManager.SUGGEST_COLUMN_RATING_SCORE;
    public static final String KEY_PRODUCTION_YEAR = SearchManager.SUGGEST_COLUMN_PRODUCTION_YEAR;
    public static final String KEY_COLUMN_DURATION = SearchManager.SUGGEST_COLUMN_DURATION;
    public static final String KEY_ACTION = SearchManager.SUGGEST_COLUMN_INTENT_ACTION;
...
```

When you build the map from the[SearchManager](https://developer.android.com/reference/android/app/SearchManager)columns to your data fields, you must also specify the[_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)to give each row a unique ID.  

### Kotlin

```kotlin
companion object {
    ....
    private fun buildColumnMap(): Map<String, String> {
        return mapOf(
          KEY_NAME to KEY_NAME,
          KEY_DESCRIPTION to KEY_DESCRIPTION,
          KEY_ICON to KEY_ICON,
          KEY_DATA_TYPE to KEY_DATA_TYPE,
          KEY_IS_LIVE to KEY_IS_LIVE,
          KEY_VIDEO_WIDTH to KEY_VIDEO_WIDTH,
          KEY_VIDEO_HEIGHT to KEY_VIDEO_HEIGHT,
          KEY_AUDIO_CHANNEL_CONFIG to KEY_AUDIO_CHANNEL_CONFIG,
          KEY_PURCHASE_PRICE to KEY_PURCHASE_PRICE,
          KEY_RENTAL_PRICE to KEY_RENTAL_PRICE,
          KEY_RATING_STYLE to KEY_RATING_STYLE,
          KEY_RATING_SCORE to KEY_RATING_SCORE,
          KEY_PRODUCTION_YEAR to KEY_PRODUCTION_YEAR,
          KEY_COLUMN_DURATION to KEY_COLUMN_DURATION,
          KEY_ACTION to KEY_ACTION,
          BaseColumns._ID to ("rowid AS " + BaseColumns._ID),
          SearchManager.SUGGEST_COLUMN_INTENT_DATA_ID to ("rowid AS " + SearchManager.SUGGEST_COLUMN_INTENT_DATA_ID),
          SearchManager.SUGGEST_COLUMN_SHORTCUT_ID to ("rowid AS " + SearchManager.SUGGEST_COLUMN_SHORTCUT_ID)
        )
    }
}
```

### Java

```java
...
  private static HashMap<String, String> buildColumnMap() {
    HashMap<String, String> map = new HashMap<String, String>();
    map.put(KEY_NAME, KEY_NAME);
    map.put(KEY_DESCRIPTION, KEY_DESCRIPTION);
    map.put(KEY_ICON, KEY_ICON);
    map.put(KEY_DATA_TYPE, KEY_DATA_TYPE);
    map.put(KEY_IS_LIVE, KEY_IS_LIVE);
    map.put(KEY_VIDEO_WIDTH, KEY_VIDEO_WIDTH);
    map.put(KEY_VIDEO_HEIGHT, KEY_VIDEO_HEIGHT);
    map.put(KEY_AUDIO_CHANNEL_CONFIG, KEY_AUDIO_CHANNEL_CONFIG);
    map.put(KEY_PURCHASE_PRICE, KEY_PURCHASE_PRICE);
    map.put(KEY_RENTAL_PRICE, KEY_RENTAL_PRICE);
    map.put(KEY_RATING_STYLE, KEY_RATING_STYLE);
    map.put(KEY_RATING_SCORE, KEY_RATING_SCORE);
    map.put(KEY_PRODUCTION_YEAR, KEY_PRODUCTION_YEAR);
    map.put(KEY_COLUMN_DURATION, KEY_COLUMN_DURATION);
    map.put(KEY_ACTION, KEY_ACTION);
    map.put(BaseColumns._ID, "rowid AS " +
            BaseColumns._ID);
    map.put(SearchManager.SUGGEST_COLUMN_INTENT_DATA_ID, "rowid AS " +
            SearchManager.SUGGEST_COLUMN_INTENT_DATA_ID);
    map.put(SearchManager.SUGGEST_COLUMN_SHORTCUT_ID, "rowid AS " +
            SearchManager.SUGGEST_COLUMN_SHORTCUT_ID);
    return map;
  }
...
```

In the previous example, notice the mapping to the[SUGGEST_COLUMN_INTENT_DATA_ID](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA_ID)field. This is the portion of the URI that points to the content unique to the data in this row---the last part of the URI, describing where the content is stored. The first part of the URI, when it is common to all the rows in the table, is set in the[`searchable.xml`](https://developer.android.com/guide/topics/search/searchable-config)file as the[`android:searchSuggestIntentData`](https://developer.android.com/guide/topics/search/searchable-config#searchSuggestIntentData)attribute, as described in the[Handle search suggestions](https://developer.android.com/training/tv/discovery/searchable#suggestions)section.

If the first part of the URI is different for each row in the table, map that value with the[SUGGEST_COLUMN_INTENT_DATA](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA)field. When the user selects this content, the intent that fires provides the intent data from the combination of the`SUGGEST_COLUMN_INTENT_DATA_ID`and either the`android:searchSuggestIntentData`attribute or the`SUGGEST_COLUMN_INTENT_DATA`field value.

## Provide search suggestion data

Implement a[Content Provider](https://developer.android.com/guide/topics/providers/content-providers)to return search term suggestions to the Android TV search dialog. The system queries your content provider for suggestions by calling the[query()](https://developer.android.com/reference/android/content/ContentProvider#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String))method each time a letter is typed. In your implementation of`query()`, your content provider searches your suggestion data and returns a[Cursor](https://developer.android.com/reference/android/database/Cursor)that points to the rows you have designated for suggestions.  

### Kotlin

```kotlin
fun query(uri: Uri, projection: Array<String>, selection: String, selectionArgs: Array<String>,
        sortOrder: String): Cursor {
    // Use the UriMatcher to see what kind of query we have and format the db query accordingly
    when (URI_MATCHER.match(uri)) {
        SEARCH_SUGGEST -> {
            Log.d(TAG, "search suggest: ${selectionArgs[0]} URI: $uri")
            if (selectionArgs == null) {
                throw IllegalArgumentException(
                        "selectionArgs must be provided for the Uri: $uri")
            }
            return getSuggestions(selectionArgs[0])
        }
        else -> throw IllegalArgumentException("Unknown Uri: $uri")
    }
}

private fun getSuggestions(query: String): Cursor {
    val columns = arrayOf<String>(
            BaseColumns._ID,
            VideoDatabase.KEY_NAME,
            VideoDatabase.KEY_DESCRIPTION,
            VideoDatabase.KEY_ICON,
            VideoDatabase.KEY_DATA_TYPE,
            VideoDatabase.KEY_IS_LIVE,
            VideoDatabase.KEY_VIDEO_WIDTH,
            VideoDatabase.KEY_VIDEO_HEIGHT,
            VideoDatabase.KEY_AUDIO_CHANNEL_CONFIG,
            VideoDatabase.KEY_PURCHASE_PRICE,
            VideoDatabase.KEY_RENTAL_PRICE,
            VideoDatabase.KEY_RATING_STYLE,
            VideoDatabase.KEY_RATING_SCORE,
            VideoDatabase.KEY_PRODUCTION_YEAR,
            VideoDatabase.KEY_COLUMN_DURATION,
            VideoDatabase.KEY_ACTION,
            SearchManager.SUGGEST_COLUMN_INTENT_DATA_ID
    )
    return videoDatabase.getWordMatch(query.toLowerCase(), columns)
}
```

### Java

```java
@Override
public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs,
        String sortOrder) {
    // Use the UriMatcher to see what kind of query we have and format the db query accordingly
    switch (URI_MATCHER.match(uri)) {
        case SEARCH_SUGGEST:
            Log.d(TAG, "search suggest: " + selectionArgs[0] + " URI: " + uri);
            if (selectionArgs == null) {
                throw new IllegalArgumentException(
                        "selectionArgs must be provided for the Uri: " + uri);
            }
            return getSuggestions(selectionArgs[0]);
        default:
            throw new IllegalArgumentException("Unknown Uri: " + uri);
    }
}

private Cursor getSuggestions(String query) {
    query = query.toLowerCase();
    String[] columns = new String[]{
        BaseColumns._ID,
        VideoDatabase.KEY_NAME,
        VideoDatabase.KEY_DESCRIPTION,
        VideoDatabase.KEY_ICON,
        VideoDatabase.KEY_DATA_TYPE,
        VideoDatabase.KEY_IS_LIVE,
        VideoDatabase.KEY_VIDEO_WIDTH,
        VideoDatabase.KEY_VIDEO_HEIGHT,
        VideoDatabase.KEY_AUDIO_CHANNEL_CONFIG,
        VideoDatabase.KEY_PURCHASE_PRICE,
        VideoDatabase.KEY_RENTAL_PRICE,
        VideoDatabase.KEY_RATING_STYLE,
        VideoDatabase.KEY_RATING_SCORE,
        VideoDatabase.KEY_PRODUCTION_YEAR,
        VideoDatabase.KEY_COLUMN_DURATION,
        VideoDatabase.KEY_ACTION,
        SearchManager.SUGGEST_COLUMN_INTENT_DATA_ID
    };
    return videoDatabase.getWordMatch(query, columns);
}
...
```

In your manifest file, the content provider receives special treatment. Rather than being tagged as an activity, it is described as a[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element). The provider includes the`android:authorities`attribute to tell the system the namespace of your content provider. Also, you must set its`android:exported`attribute to`"true"`so that the Android global search can use the results returned from it.  

```xml
<provider android:name="com.example.android.tvleanback.VideoContentProvider"
    android:authorities="com.example.android.tvleanback"
    android:exported="true" />
```

## Handle search suggestions

Your app must include a[`res/xml/searchable.xml`](https://developer.android.com/guide/topics/search/searchable-config)file to configure the search suggestions settings.

In the`res/xml/searchable.xml`file, include the[`android:searchSuggestAuthority`](https://developer.android.com/guide/topics/search/searchable-config#searchSuggestAuthority)attribute to tell the system the namespace of your content provider. This must match the string value you specify in the[`android:authorities`](https://developer.android.com/guide/topics/manifest/provider-element#auth)attribute of the[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element)element in your`AndroidManifest.xml`file.

Also include a[label](https://developer.android.com/guide/topics/search/searchable-config#label), which is the name of the application. The system search settings use this label when enumerating searchable apps.

The`searchable.xml`file must also include the[`android:searchSuggestIntentAction`](https://developer.android.com/guide/topics/search/searchable-config#searchSuggestIntentAction)with the value`"android.intent.action.VIEW"`to define the intent action for providing a custom suggestion. This is different from the intent action for providing a[search term](https://developer.android.com/training/tv/discovery/searchable#terms), as described in the following section. For other ways to declare the intent action for suggestions, see[Declaring the intent action](https://developer.android.com/guide/topics/search/adding-custom-suggestions#IntentAction).

Along with the intent action, your app must provide the intent data, which you specify with the[`android:searchSuggestIntentData`](https://developer.android.com/guide/topics/search/searchable-config#searchSuggestIntentData)attribute. This is the first part of the URI that points to the content, which describes the portion of the URI common to all rows in the mapping table for that content. The portion of the URI that is unique to each row is established with the[SUGGEST_COLUMN_INTENT_DATA_ID](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA_ID)field, as described in the[Identify columns](https://developer.android.com/training/tv/discovery/searchable#columns)section. For other ways to declare the intent data for suggestions, see[Declaring the intent data](https://developer.android.com/guide/topics/search/adding-custom-suggestions#IntentData).

The`android:searchSuggestSelection=" ?"`attribute specifies the value passed as the`selection`parameter of the[query()](https://developer.android.com/reference/android/content/ContentProvider#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String))method. The question mark (`?`) value is replaced with the query text.

Finally, you must also include the[`android:includeInGlobalSearch`](https://developer.android.com/guide/topics/search/searchable-config#includeInGlobalSearch)attribute with the value`"true"`. Here is an example`searchable.xml`file:  

```xml
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/search_label"
    android:hint="@string/search_hint"
    android:searchSettingsDescription="@string/settings_description"
    android:searchSuggestAuthority="com.example.android.tvleanback"
    android:searchSuggestIntentAction="android.intent.action.VIEW"
    android:searchSuggestIntentData="content://com.example.android.tvleanback/video_database_leanback"
    android:searchSuggestSelection=" ?"
    android:searchSuggestThreshold="1"
    android:includeInGlobalSearch="true">
</searchable>
```

## Handle search terms

As soon as the search dialog has a word that matches the value in one of your app's columns, as described in the[Identify columns](https://developer.android.com/training/tv/discovery/searchable#identifying)section, the system fires the[ACTION_SEARCH](https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH)intent. The activity in your app that handles that intent searches the repository for columns with the given word in their values and returns a list of content items with those columns. In your`AndroidManifest.xml`file, you designate the activity which handles the[ACTION_SEARCH](https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH)intent as shown in the following example:  

```xml
...
  <activity
      android:name="com.example.android.tvleanback.DetailsActivity"
      android:exported="true">

      <!-- Receives the search request. -->
      <intent-filter>
          <action android:name="android.intent.action.SEARCH" />
          <!-- No category needed, because the Intent will specify this class component -->
      </intent-filter>

      <!-- Points to searchable meta data. -->
      <meta-data android:name="android.app.searchable"
          android:resource="@xml/searchable" />
  </activity>
...
  <!-- Provides search suggestions for keywords against video meta data. -->
  <provider android:name="com.example.android.tvleanback.VideoContentProvider"
      android:authorities="com.example.android.tvleanback"
      android:exported="true" />
...
```

The activity must also describe the searchable configuration with a reference to the[`searchable.xml`](https://developer.android.com/guide/topics/search/searchable-config)file. To[use the global search dialog](https://developer.android.com/guide/topics/search/search-dialog), the manifest must describe which activity should receive search queries. The manifest must also describe the[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element)element, exactly as it is described in the`searchable.xml`file.

## Deep link to your app in the details screen

If you have set up the search configuration as described in the[Handle search suggestions](https://developer.android.com/training/tv/discovery/searchable#suggestions)section and mapped the[SUGGEST_COLUMN_TEXT_1](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_TEXT_1),[SUGGEST_COLUMN_PRODUCTION_YEAR](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_PRODUCTION_YEAR), and[SUGGEST_COLUMN_DURATION](https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_DURATION)fields as described in the[Identify columns](https://developer.android.com/training/tv/discovery/searchable#columns)section, a[deep link](https://developer.android.com/training/app-indexing/deep-linking)to a watch action for your content appears in the details screen that launches when the user selects a search result:
![Deep link in the details screen](https://developer.android.com/static/images/tv/deep-link.png)

When the user selects the link for your app, identified by the \*\*Available On\*\* button in the details screen, the system launches the activity that handles the[ACTION_VIEW](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)set as[`android:searchSuggestIntentAction`](https://developer.android.com/guide/topics/search/searchable-config#searchSuggestIntentAction)with the value`"android.intent.action.VIEW"`in the[`searchable.xml`](https://developer.android.com/guide/topics/search/searchable-config)file.

You can also set up a custom intent to launch your activity. This is demonstrated in the[Leanback sample app](https://github.com/android/tv-samples/tree/main/Leanback). Note that the sample app launches its own`LeanbackDetailsFragment`to show the details for the selected media; in your apps, launch the activity that plays the media immediately to save the user another click or two.

## Search behavior

Search is available in Android TV from the home screen and from inside your app. Search results are different for these two cases.

### Search from the home screen

When the user searches from the home screen, the first result appears in an entity card. If there are apps that can play the content, a link to each one appears at the bottom of the card:
![TV Search Result Playback](https://developer.android.com/static/images/tv/tv-search-playback.png)

You can't programmatically place an app into the entity card. To be included as a playback option, an app's search results must match the title, year, and duration of the searched content.

More search results might be available below the card. To see them, the user must press down on the remote and scroll down. The results for each app appear in a separate row. You can't control the row ordering. Apps that support[watch actions](https://developers.google.com/actions/media/)are listed first.
![TV Search Results](https://developer.android.com/static/images/tv/tv-search-results.gif)

### Search from your app

The user can also start a search from within your app by initiating the microphone from the remote or game pad controller. The search results are displayed in a single row on top of the app's content. Your app generates search results using its own[global search provider](https://developer.android.com/training/tv/discovery/searchable#provide).
![TV In-app Search Results](https://developer.android.com/static/images/tv/tv-search-in-app.png)

## Learn more

To learn more about searching a TV app, read[Integrate Android search features into your app](https://developer.android.com/guide/topics/search)and[Add search functionality](https://developer.android.com/training/search).

For more information on how to customize the in-app search experience with a`SearchFragment`, read[Search within TV apps](https://developer.android.com/training/tv/discovery/in-app-search).