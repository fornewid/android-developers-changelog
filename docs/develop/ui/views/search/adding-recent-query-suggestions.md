---
title: Add custom search suggestions  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/search/adding-recent-query-suggestions
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add custom search suggestions Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose.

[Search bar →](https://developer.android.com/develop/ui/compose/components/search-bar)

![](/static/images/android-compose-ui-logo.png)

You can provide search suggestions based on recent search queries in the Android search dialog or
search widget. For example, if a user queries "puppies," the query appears as a suggestion when they
type the same query again. Figure 1 shows an example of a search dialog with recent query
suggestions.

Before you begin, implement the search dialog or a search widget for basic searches
in your application. To learn how, see
[Create a search interface](/develop/ui/views/search/search-dialog).

## The basics

![](/static/images/search/search-suggest-recent-queries.png)

**Figure 1.** Screenshot of a search dialog with recent query
suggestions.

Recent query suggestions are saved searches. When the user selects a suggestion, your searchable
activity receives an
`ACTION_SEARCH` intent
with the suggestion as the search query that your searchable activity already handles.

To provide recent queries suggestions, you need to:

* Implement a searchable activity.
* Create a content provider that extends
  `SearchRecentSuggestionsProvider`
  and declare it in your application manifest.
* Modify the searchable configuration with information about the content provider that provides
  search suggestions.
* Save queries to your content provider each time a search is executed.

Just as the Android system displays the search dialog, it displays the search suggestions below
the dialog or search widget. You provide the source the system retrieves the suggestions from.

When the system identifies that your activity is searchable and provides search suggestions, the
following happens when the user types a query:

1. The system takes the search query text—whatever the user begins typing—and
   performs a query to the content provider that contains your suggestions.
2. Your content provider returns a
   `Cursor` that points to all
   suggestions that match the search query text.
3. The system displays the list of suggestions provided by the `Cursor`.

Once the recent query suggestions are displayed, the following might happen:

* If the user types another key or changes the query in any way, the preceding steps are
  repeated and the suggestion list is updated.
* If the user executes the search, the suggestions are ignored and the search is delivered to
  your searchable activity using the normal `ACTION_SEARCH` intent.
* If the user selects a suggestion, an `ACTION_SEARCH` intent is delivered to your
  searchable activity using the suggested text as the query.

The `SearchRecentSuggestionsProvider` class that you extend for your content provider
automatically does the work in the preceding steps, so there's little code to write.

## Create a content provider

The content provider you need for recent query suggestions is an implementation of
`SearchRecentSuggestionsProvider`. This class does everything for you. You just need to
write a class constructor that executes one line of code.

For example, here's a complete implementation of a content provider for recent query
suggestions:

### Kotlin

```
class MySuggestionProvider : SearchRecentSuggestionsProvider() {
    init {
        setupSuggestions(AUTHORITY, MODE)
    }

    companion object {
        const val AUTHORITY = "com.example.MySuggestionProvider"
        const val MODE: Int = SearchRecentSuggestionsProvider.DATABASE_MODE_QUERIES
    }
}
```

### Java

```
public class MySuggestionProvider extends SearchRecentSuggestionsProvider {
    public final static String AUTHORITY = "com.example.MySuggestionProvider";
    public final static int MODE = DATABASE_MODE_QUERIES;

    public MySuggestionProvider() {
        setupSuggestions(AUTHORITY, MODE);
    }
}
```

The call to
`setupSuggestions()`
passes the name of the search authority and a database mode. The search authority can be any unique
string, but the best practice is to use a fully qualified name for your content provider, such as
the package name followed by the provider's class name. For example,
`"com.example.MySuggestionProvider"`.

The database mode must include
`DATABASE_MODE_QUERIES`
and can optionally include
`DATABASE_MODE_2LINES`,
which adds a column to the suggestions table so you can provide a second line of text with each
suggestion. If you want to provide two lines in each suggestion, see the following example:

### Kotlin

```
const val MODE: Int = DATABASE_MODE_QUERIES or DATABASE_MODE_2LINES
```

### Java

```
public final static int MODE = DATABASE_MODE_QUERIES | DATABASE_MODE_2LINES;
```

Declare the content provider in your application manifest with the same authority string used in
your `SearchRecentSuggestionsProvider` class and in the searchable configuration. For
example:

```
<application>
    <provider android:name=".MySuggestionProvider"
              android:authorities="com.example.MySuggestionProvider" />
    ...
</application>
```

## Modify the searchable configuration

To configure the system to use your suggestions provider, add the
`android:searchSuggestAuthority` and `android:searchSuggestSelection`
attributes to the `<searchable>` element in your searchable configuration file. For
example:

```
<?xml version="1.0" encoding="utf-8"?>
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_label"
    android:hint="@string/search_hint"
    android:searchSuggestAuthority="com.example.MySuggestionProvider"
    android:searchSuggestSelection=" ?" >
</searchable>
```

The value for `android:searchSuggestAuthority` must be a fully qualified name for your
content provider that exactly matches the authority used in the content provider, such as
`"com.example.MySuggestionProvider"` in the preceding examples.

The value for `android:searchSuggestSelection` must be a single question mark preceded
by a space: `" ?"`. This is a placeholder for the SQLite selection argument, and it is
automatically replaced by the query text entered by the user.

## Save queries

To populate your collection of recent queries, add each query received by your searchable
activity to your `SearchRecentSuggestionsProvider`. To do this, create an instance of
`SearchRecentSuggestions`
and call
`saveRecentQuery()`
each time your searchable activity receives a query. For example, here's how you can save the query
during your activity's
`onCreate()`
method:

### Kotlin

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.main)

    if (Intent.ACTION_SEARCH == intent.action) {
        intent.getStringExtra(SearchManager.QUERY)?.also { query ->
            SearchRecentSuggestions(this, MySuggestionProvider.AUTHORITY, MySuggestionProvider.MODE)
                    .saveRecentQuery(query, null)
        }
    }
}
```

### Java

```
@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.main);

    Intent intent  = getIntent();

    if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
        String query = intent.getStringExtra(SearchManager.QUERY);
        SearchRecentSuggestions suggestions = new SearchRecentSuggestions(this,
                MySuggestionProvider.AUTHORITY, MySuggestionProvider.MODE);
        suggestions.saveRecentQuery(query, null);
    }
}
```

The `SearchRecentSuggestionsProvider` constructor requires the
same authority and database mode declared by your content provider.

The `saveRecentQuery()` method takes the search query string as the first parameter
and, optionally, a second string to include as the second line of the suggestion or null. The second
parameter is only used if you enable two-line mode for the search suggestions with
`DATABASE_MODE_2LINES`. If you enable two-line mode, then the query text matches against
the second line when the system looks for matching suggestions.

## Clear the suggestion data

To protect the user's privacy, always provide a way for the user to clear the recent query
suggestions. To clear the query history, call
`clearHistory()`.
For example:

### Kotlin

```
SearchRecentSuggestions(this, HelloSuggestionsProvider.AUTHORITY, HelloSuggestionsProvider.MODE)
        .clearHistory()
```

### Java

```
SearchRecentSuggestions suggestions = new SearchRecentSuggestions(this,
        HelloSuggestionProvider.AUTHORITY, HelloSuggestionProvider.MODE);
suggestions.clearHistory();
```

Execute this from your choice of a "Clear Search History" menu item, preference item, or button.
Provide a confirmation dialog to verify that the user wants to delete their search history.