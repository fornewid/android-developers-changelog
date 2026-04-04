---
title: https://developer.android.com/develop/ui/views/search/adding-custom-suggestions
url: https://developer.android.com/develop/ui/views/search/adding-custom-suggestions
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose. [Search bar →](https://developer.android.com/develop/ui/compose/components/search-bar) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

When using the Android search dialog or search widget, you can provide
custom search suggestions that are created from data in your app. For example,
if your app is a dictionary, you can suggest words from the dictionary that
match the text entered in the search field before the user finishes entering
their query. These suggestions are valuable because they can effectively predict
what the user wants and provide instant access to it. Figure 1 shows an example
of a search dialog with custom suggestions.

Once you provide custom suggestions, you can also make them available to the
system-wide Quick Search Box, providing access to your content from outside your
app.

Before you add custom suggestions, implement the Android search dialog or a
search widget for searches in your app. See [Create
a search interface](https://developer.android.com/develop/ui/views/search/search-dialog) and
[Content
providers](https://developer.android.com/guide/topics/providers/content-providers).

## The basics

![](https://developer.android.com/static/images/search/search-suggest-custom.png)

**Figure 1.** Screenshot of a search dialog with
custom search suggestions.

When the user selects a custom suggestion, the system sends an
`https://developer.android.com/reference/android/content/Intent` to your
searchable activity. Unlike a normal search query that sends an intent with the
`https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH`
action, you can instead define your custom suggestions to use
`https://developer.android.com/reference/android/content/Intent#ACTION_VIEW`---or
any other intent action---and also include data that's relevant to the
selected suggestion. In the dictionary example, when the user selects a
suggestion, the app can immediately open the definition for that word, instead
of searching the dictionary for matches.

To provide custom suggestions, perform the following steps:

- Implement a basic searchable activity, as described in [Create a search interface](https://developer.android.com/develop/ui/views/search/search-dialog).
- Modify the searchable configuration with information about the content provider that provides custom suggestions.
- Build a table, such as in a `https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase`, for your suggestions and format the table with required columns.
- Create a [content
  provider](https://developer.android.com/guide/topics/providers/content-providers) that has access to your suggestions table and declare the provider in your manifest.
- Declare the type of `Intent` to be sent when the user selects a suggestion, including a custom action and custom data.

Just as the Android system displays the search dialog, it also displays your
search suggestions. You need a content provider from which the system can
retrieve your suggestions. Read
[Content providers](https://developer.android.com/guide/topics/providers/content-providers)
to learn how to create a content provider.

When the system identifies that your activity is searchable and provides
search suggestions, the following procedure takes place when the user enters a
query:

1. The system takes the search query text---meaning, whatever is entered so far---and performs a query to your content provider that manages your suggestions.
2. Your content provider returns a `https://developer.android.com/reference/android/database/Cursor` that points to all suggestions that are relevant to the search query text.
3. The system displays the list of suggestions provided by the `Cursor`.

Once the custom suggestions are displayed, the following might happen:

- If the user enters another letter or changes the query in any way, the preceding steps repeat and the suggestion list updates accordingly.
- If the user executes the search, the suggestions are ignored and the search is delivered to your searchable activity using the normal `ACTION_SEARCH` intent.
- If the user selects a suggestion, an intent is sent to your searchable activity, carrying a custom action and custom data so that your app can open the suggested content.

## Modify the searchable configuration

To add support for custom suggestions, add the
`android:searchSuggestAuthority` attribute to the
`<searchable>` element in your searchable configuration file,
as shown in the following example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_label"
    android:hint="@string/search_hint"
    android:searchSuggestAuthority="com.example.MyCustomSuggestionProvider">
</searchable>
```

You might need additional attributes, depending on the type of intent you
attach to each suggestion and how you want to format queries to your content
provider. The other optional attributes are discussed in the following
sections.

## Create a content provider

To create a content provider for custom suggestions, first see
[Content providers](https://developer.android.com/guide/topics/providers/content-providers)
to learn how to create a content provider. A content provider for custom
suggestions is similar to any other content provider. However, for each
suggestion you provide, the respective row in the `Cursor` must
include specific columns that the system understands and uses to format the
suggestions.

When the user enters text in the search dialog or search widget, the system
queries your content provider for suggestions by calling
`https://developer.android.com/reference/android/content/ContentProvider#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String)`
each time a letter is entered. In your implementation of `query()`,
your content provider must search your suggestion data and return a
`Cursor` that points to the rows that it determines are good
suggestions.

Details about creating a content provider for custom suggestions are
discussed in the following two sections:

[Handle the suggestion query](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions#HandleSuggestionQuery)
:   How the system sends requests to your content provider and how to handle
    them.

[Build a suggestion table](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions#SuggestionTable)
:   How to define the columns that the system expects in the
    `Cursor` returned with each query.

### Handle the suggestion query

When the system requests suggestions from your content provider, it calls
your content provider's `query()` method. Implement this method to
search your suggestion data and return a `Cursor` pointing to the
suggestions you deem relevant.

Here's a summary of the parameters the system passes to your
`query()` method, listed in order:

The system can send you the search query text in two ways. The default way is
for the query text to be included as the last path of the content URI passed in
the `uri` parameter. However, if you include a selection value in
your searchable configuration's `android:searchSuggestSelection`
attribute, then the query text instead passes as the first element of the
`selectionArgs` string array. These two options are described
next.

#### Get the query in the Uri

By default, the query is appended as the last segment of the `uri`
parameter---a `Uri` object. To retrieve the query text in this
case, use
`https://developer.android.com/reference/android/net/Uri#getLastPathSegment()`,
as shown in the following example:

### Kotlin

```kotlin
val query: String = uri.lastPathSegment.toLowerCase()
```

### Java

```java
String query = uri.getLastPathSegment().toLowerCase();
```

This returns the last segment of the `Uri`, which is the query
text the user enters.

#### Get the query in the selection arguments

Instead of using the URI, it might make more sense for your
`query()` method to receive everything it needs to perform the
look-up, and you might want the `selection` and
`selectionArgs` parameters to carry the appropriate values. In this
case, add the `android:searchSuggestSelection` attribute to your
searchable configuration with your SQLite selection string. In the selection
string, include a question mark (*?*) as a placeholder for the actual
search query. The system calls `query()` with the selection string as
the `selection` parameter and the search query as the first element
in the `selectionArgs` array.

For example, here's how you might form the
`android:searchSuggestSelection` attribute to create a full-text
search statement:

```xml
<?xml version="1.0" encoding="utf-8"?>
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_label"
    android:hint="@string/search_hint"
    android:searchSuggestAuthority="com.example.MyCustomSuggestionProvider"
    android:searchSuggestIntentAction="android.intent.action.VIEW"
    android:searchSuggestSelection="word MATCH ?">
</searchable>
```

With this configuration, your `query()` method delivers the
`selection` parameter as `"word MATCH ?"` and the
`selectionArgs` parameter as the search query. When you pass these to
a SQLite
`https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#query(java.lang.String, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String, java.lang.String, java.lang.String)`
method, as their respective arguments, they are synthesized
together---meaning, the question mark is replaced with the query text. If
you receive suggestion queries this way and need to add wildcards to the query
text, append or prefix them to the `selectionArgs` parameter, because
this value is wrapped in quotes and inserted in place of the question mark.

Another attribute in the preceding example is
`android:searchSuggestIntentAction`, which defines the intent action
sent with each intent when the user selects a suggestion. This is discussed
further in the [Declare an intent for
suggestions](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions#IntentForSuggestions) section.
| **Tip:** If you don't want to define a selection clause in the `android:searchSuggestSelection` attribute, but you still want to receive the query text in the `selectionArgs` parameter, provide a non-null value for the `android:searchSuggestSelection` attribute. This triggers the query to pass in `selectionArgs`, and you can ignore the `selection` parameter. This way, you can instead define the actual selection clause at a lower level so that your content provider doesn't have to handle it.

### Build a suggestion table

When you return suggestions to the system with a `Cursor`, the
system expects specific columns in each row. Regardless of whether you store
your suggestion data in a SQLite database on the device, a database on a web
server, or another format on the device or web, format the suggestions as rows
in a table and present them with a `Cursor`.
| **Note:** If your search suggestions aren't stored in a table format---such as a SQLite table---using the columns required by the system, then you can search your suggestion data for matches and then format them into the necessary table on each request. To do so, create a `https://developer.android.com/reference/android/database/MatrixCursor` using the required column names and then add a row for each suggestion using `https://developer.android.com/reference/android/database/MatrixCursor#addRow(java.lang.Object[])`. Return the final product from your content provider's `query()` method.

The system understands several columns, but only two of them are required:

`https://developer.android.com/reference/android/provider/BaseColumns#_ID`
:   A unique integer row ID for each suggestion. The system requires this to
    present suggestions in a
    `https://developer.android.com/reference/android/widget/ListView`.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_TEXT_1`
:   The string that is presented as a suggestion.

The following columns are all optional. Most are discussed further in the
following sections.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_TEXT_2`
:   A string. If your `Cursor` includes this column, then all
    suggestions are provided in a two-line format. The string in this column is
    displayed as a second, smaller line of text below the primary suggestion
    text. It can be null or empty to indicate no secondary text.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_ICON_1`
:   A drawable resource, content, or file URI string. If your
    `Cursor` includes this column, then all suggestions are provided
    in an icon-plus-text format with the drawable icon on the left side. This
    can be null or zero to indicate no icon in this row.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_ICON_2`
:   A drawable resource, content, or file URI string. If your
    `Cursor` includes this column, then all suggestions are provided
    in an icon-plus-text format with the icon on the right side. This can be
    null or zero to indicate no icon in this row.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_ACTION`
:   An intent action string. If this column exists and contains a value at the
    given row, the action defined here is used when forming the suggestion's
    intent. If the element isn't provided, the action is taken from the
    `android:searchSuggestIntentAction` field in your searchable
    configuration. If your action is the same for all suggestions, it's more
    efficient to specify the action using
    `android:searchSuggestIntentAction` and omit this column.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA`
:   A data URI string. If this column exists and contains a value at the given
    row, this data is used when forming the suggestion's intent. If the element
    isn't provided, the data is taken from the
    `android:searchSuggestIntentData` field in your searchable
    configuration. If neither source is provided, the intent's data field is
    null. If your data is the same for all suggestions, or can be described
    using a constant part and a specific ID, it's more efficient to specify it
    using `android:searchSuggestIntentData` and omit this
    column.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA_ID`
:   A URI path string. If this column exists and contains a value at the given
    row, then "/" and this value is appended to the data field in the intent.
    Only use this if the data field specified by the
    `android:searchSuggestIntentData` attribute in the searchable
    configuration is already set to an appropriate base string.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_EXTRA_DATA`
:   Arbitrary data. If this column exists and contains a value at a given row,
    this is the *extra* data used when forming the suggestion's intent.
    If not provided, the intent's extra data field is null. This column lets
    suggestions provide additional data that is included as an extra in the
    intent's
    `https://developer.android.com/reference/android/app/SearchManager#EXTRA_DATA_KEY`
    key.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_QUERY`
:   If this column exists and this element exists at the given row, this is
    the data that is used when forming the suggestion's query, included as an
    extra in the intent's
    `https://developer.android.com/reference/android/app/SearchManager#QUERY`
    key. It's required if the suggestion's action is `ACTION_SEARCH`,
    but optional otherwise.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_SHORTCUT_ID`
:   Only used when providing suggestions for Quick Search Box. This column
    indicates whether a search suggestion must be stored as a shortcut and
    whether it must be validated. Shortcuts are usually formed when the user
    taps a suggestion from Quick Search Box. If missing, the result is stored as
    a shortcut and never refreshed. If set to
    `https://developer.android.com/reference/android/app/SearchManager#SUGGEST_NEVER_MAKE_SHORTCUT`,
    the result isn't stored as a shortcut. Otherwise, the shortcut ID is used to
    check back for an up-to-date suggestion using
    `https://developer.android.com/reference/android/app/SearchManager#SUGGEST_URI_PATH_SHORTCUT`.

`https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_SPINNER_WHILE_REFRESHING`
:   Only used when providing suggestions for Quick Search Box. This column
    specifies that a spinner must be shown instead of an icon from
    `SUGGEST_COLUMN_ICON_2` while the shortcut of this suggestion is
    refreshing in Quick Search Box.

Most of these columns are discussed further in the following sections.

## Declare an intent for suggestions

When the user selects a suggestion from the list that appears under the
search dialog or widget, the system sends a custom `Intent` to your
searchable activity. You must define the action and data for the intent.

### Declare the intent action

The most common intent action for a custom suggestion is
`ACTION_VIEW`, which is appropriate when you want to open something,
like the definition for a word, a person's contact information, or a web page.
However, the intent action can be any other action and can be different for each
suggestion.

Depending on whether you want all suggestions to use the same intent action,
you can define the action in two ways:

- Use the `android:searchSuggestIntentAction` attribute of your searchable configuration file to define the action for all suggestions, as shown in the following example:

  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <searchable xmlns:android="http://schemas.android.com/apk/res/android"
      android:label="@string/app_label"
      android:hint="@string/search_hint"
      android:searchSuggestAuthority="com.example.MyCustomSuggestionProvider"
      android:searchSuggestIntentAction="android.intent.action.VIEW" >
  </searchable>
  ```
- Use the `SUGGEST_COLUMN_INTENT_ACTION` column to define the action for individual suggestions. To do this, add the `SUGGEST_COLUMN_INTENT_ACTION` column to your suggestions table and, for each suggestion, place in it the action to use---such as `"android.intent.action.VIEW"`.

You can also combine these two techniques. For example, you can include the
`android:searchSuggestIntentAction` attribute with an action to be
used with all suggestions by default, then override this action for some
suggestions by declaring a different action in the
`SUGGEST_COLUMN_INTENT_ACTION` column. If you don't include a value
in the `SUGGEST_COLUMN_INTENT_ACTION` column, then the intent
provided in the `android:searchSuggestIntentAction` attribute is
used.
| **Note:** If you don't include the `android:searchSuggestIntentAction` attribute in your searchable configuration, then you *must* include a value in the `SUGGEST_COLUMN_INTENT_ACTION` column for every suggestion, or else the intent fails.

### Declare intent data

When the user selects a suggestion, your searchable activity receives the
intent with the action you define---as discussed in the previous
section---but the intent must also carry data for your activity to identify
which suggestion is selected. Specifically, the data must be something unique
for each suggestion, such as the row ID for the suggestion in your SQLite table.
When the intent is received, you can retrieve the attached data with
`https://developer.android.com/reference/android/content/Intent#getData()`
or
`https://developer.android.com/reference/android/content/Intent#getDataString()`.

You can define the data included with the intent in two ways:

- Define the data for each suggestion inside the `SUGGEST_COLUMN_INTENT_DATA` column of your suggestions table.

  Provide all necessary data information for each intent in the suggestions
  table by including the `SUGGEST_COLUMN_INTENT_DATA` column and
  then populating it with unique data for each row. The data from this column
  is attached to the intent exactly as you define it in this column. You can
  then retrieve it with `getData()` or
  `getDataString()`.
  | **Tip** : It's usually easier to use the table's row ID as the intent data, because it's always unique. The easiest way to do this is by using the `SUGGEST_COLUMN_INTENT_DATA` column name as an alias for the row ID column.
- Fragment a data URI into two pieces: the portion common to all suggestions and the portion unique to each suggestion. Place these parts into the `android:searchSuggestintentData` attribute of the searchable configuration and the `SUGGEST_COLUMN_INTENT_DATA_ID` column of your suggestions table, respectively.

  The following example shows how to declare the piece of the URI that is
  common to all suggestions in the
  `android:searchSuggestIntentData` attribute of your searchable
  configuration:

  ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <searchable xmlns:android="http://schemas.android.com/apk/res/android"
        android:label="@string/app_label"
        android:hint="@string/search_hint"
        android:searchSuggestAuthority="com.example.MyCustomSuggestionProvider"
        android:searchSuggestIntentAction="android.intent.action.VIEW"
        android:searchSuggestIntentData="content://com.example/datatable" >
    </searchable>
    
  ```

  Include the final path for each suggestion---the unique part---in
  the `SUGGEST_COLUMN_INTENT_DATA_ID` column of your suggestions
  table. When the user selects a suggestion, the system takes the string from
  `android:searchSuggestIntentData`, appends a slash (*/*),
  and then adds the respective value from the
  `SUGGEST_COLUMN_INTENT_DATA_ID` column to form a complete content
  URI. You can then retrieve the `Uri` with
  `getData()`.

#### Add more data

If you need to express more information with your intent, you can add another
table column, such as `SUGGEST_COLUMN_INTENT_EXTRA_DATA`, which can
store additional information about the suggestion. The data saved in this column
is placed in the `EXTRA_DATA_KEY` of the intent's extra bundle.

## Handle the intent

After you provide custom search suggestions with custom intents, you need
your searchable activity to handle these intents when the user selects a
suggestion. This is in addition to handling the `ACTION_SEARCH`
intent, which your searchable activity already does. Here's an example of how
you can handle the intents during your activity's
`https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)`
callback:

### Kotlin

```kotlin
when(intent.action) {
    Intent.ACTION_SEARCH -> {
        // Handle the normal search query case.
        intent.getStringExtra(SearchManager.QUERY)?.also { query ->
            doSearch(query)
        }
    }
    Intent.ACTION_VIEW -> {
        // Handle a suggestions click, because the suggestions all use ACTION_VIEW.
        showResult(intent.data)
    }
}
```

### Java

```java
Intent intent = getIntent();
if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
    // Handle the normal search query case.
    String query = intent.getStringExtra(SearchManager.QUERY);
    doSearch(query);
} else if (Intent.ACTION_VIEW.equals(intent.getAction())) {
    // Handle a suggestions click, because the suggestions all use ACTION_VIEW.
    Uri data = intent.getData();
    showResult(data);
}
```

In this example, the intent action is `ACTION_VIEW` and the data
carries a complete URI pointing to the suggested item, as synthesized by the
`android:searchSuggestIntentData` string and
`SUGGEST_COLUMN_INTENT_DATA_ID` column. The URI then passes to the
local `showResult()` method that queries the content provider for the
item specified by the URI.
| **Note:** You do *not* need to add an intent filter to your Android manifest file for the intent action you defined with the `android:searchSuggestIntentAction` attribute or `SUGGEST_COLUMN_INTENT_ACTION` column. The system opens your searchable activity by name to deliver the suggestion's intent, so the activity doesn't need to declare the accepted action.

## Rewrite the query text

By default, if the user navigates through the suggestions list using
directional controls, such as with a trackball or D-pad, the query text doesn't
update. However, you can temporarily rewrite the user's query text as it appears
in the text box with a query that matches the suggestion in focus. This lets the
user see the query being suggested, and they can select the search box and edit
the query before dispatching it as a search.

You can rewrite the query text in the following ways:

- Add the `android:searchMode` attribute to your searchable configuration with the `"queryRewriteFromText"` value. In this case, the content from the suggestion's `SUGGEST_COLUMN_TEXT_1` column is used to rewrite the query text.
- Add the `android:searchMode` attribute to your searchable\\ configuration with the `"queryRewriteFromData"` value. In this case, the content from the suggestion's `SUGGEST_COLUMN_INTENT_DATA` column is used to rewrite the query text. Only use this with URIs or other data formats that are intended to be user-visible, such as HTTP URLs. Don't use internal URI schemes to rewrite the query in this way.
- Provide a unique query text string in the `SUGGEST_COLUMN_QUERY` column of your suggestions table. If this column is present and contains a value for the current suggestion, it is used to rewrite the query text and override either of the previous implementations.

## Expose search suggestions to Quick Search Box

Once you configure your app to provide custom search suggestions, making them
available to the globally accessible Quick Search Box is as easy as modifying
your searchable configuration to include
`android:includeInGlobalSearch` with the value
`"true"`.

The only scenario in which additional work is necessary is when your content
provider demands a read permission. In that case, you need to add a
`<path-permission>` element for the provider to grant Quick
Search Box read access to your content provider, as shown in the following
example:

```xml
<provider android:name="MySuggestionProvider"
          android:authorities="com.example.MyCustomSuggestionProvider"
          android:readPermission="com.example.provider.READ_MY_DATA"
          android:writePermission="com.example.provider.WRITE_MY_DATA">
  <path-permission android:pathPrefix="/search_suggest_query"
                   android:readPermission="android.permission.GLOBAL_SEARCH" />
</provider>
```

In this example, the provider restricts read and write access to the content.
The `<path-permission>` element amends the restriction by
granting read access to content inside the `"/search_suggest_query"`
path prefix when the `"android.permission.GLOBAL_SEARCH"` permission
exists. This grants access to Quick Search Box so that it can query your content
provider for suggestions.

If your content provider doesn't enforce read permissions, then Quick Search
Box reads it by default.

### Enable suggestions on a device

By default, apps aren't enabled to provide suggestions in Quick Search Box,
even if they are configured to do so. The user chooses whether to include
suggestions from your app in Quick Search Box by opening **Searchable
items** ---located in **Settings \> Search**---and enabling your
app as a searchable item.

Each app that is available to Quick Search Box has an entry in the
**Searchable items** settings page. The entry includes the name of the app
and a short description of what content is searchable from the app and made
available for suggestions in Quick Search Box. To define the description text
for your searchable app, add the `android:searchSettingsDescription`
attribute to your searchable configuration, as shown in the following
example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_label"
    android:hint="@string/search_hint"
    android:searchSuggestAuthority="com.example.MyCustomSuggestionProvider"
    android:searchSuggestIntentAction="android.intent.action.VIEW"
    android:includeInGlobalSearch="true"
    android:searchSettingsDescription="@string/search_description" >
</searchable>
```

Make the string for `android:searchSettingsDescription` as concise
as possible and state the content that is searchable. For example, "Artists,
albums, and tracks" for a music app, or "Saved notes" for a notepad app.
Providing this description is important so that the user knows what kind of
suggestions are provided. Always include this attribute when
`android:includeInGlobalSearch` is true.

Because the user must visit the settings menu to enable search suggestions
for your app, if search is an important aspect of your app consider how to
convey that to your users. For example, you might provide a note the first time
a user launches the app that explains how to enable search suggestions for Quick
Search Box.

### Manage Quick Search Box suggestion shortcuts

Suggestions that the user selects from Quick Search Box can be automatically
made into shortcuts. These are suggestions that the system copies from your
content provider so it can quickly access the suggestion without needing to
re-query your content provider.

By default, this is enabled for all suggestions retrieved by Quick Search
Box, but if your suggestion data changes over time, then you can request that
the shortcuts be refreshed. For example, if your suggestions refer to dynamic
data, such as a contact's presence status, then request that the suggestion
shortcuts be refreshed when shown to the user. To do this, include the
`SUGGEST_COLUMN_SHORTCUT_ID` in your suggestions table. You can use
this column to configure the shortcut behavior for each suggestion in one of the
following ways:

- Make Quick Search Box re-query your content provider for a fresh
  version of the suggestion shortcut.

  Provide a value in the `SUGGEST_COLUMN_SHORTCUT_ID` column for
  the suggestion to be re-queried for a fresh version each time the shortcut
  is displayed. The shortcut quickly displays with whatever data is most
  recently available until the refresh query returns, at which point the
  suggestion is refreshed with the new information. The refresh query is
  sent to your content provider with a URI path of
  `SUGGEST_URI_PATH_SHORTCUT`---instead of
  `SUGGEST_URI_PATH_QUERY`.

  Make the `Cursor` you return contain one suggestion using the
  same columns as the original suggestion or be empty, indicating that the
  shortcut is no longer valid---in which case, the suggestion disappears
  and the shortcut is removed.

  If a suggestion refers to data that can take longer to refresh, such as a
  network-based refresh, you can also add the
  `SUGGEST_COLUMN_SPINNER_WHILE_REFRESHING` column to your
  suggestions table with a value of true to show a progress spinner for the
  right-hand icon until the refresh is complete. Any value other than true
  doesn't show the progress spinner.
- Prevent the suggestion from being copied into a shortcut at all.

  Provide a value of `SUGGEST_NEVER_MAKE_SHORTCUT` in the
  `SUGGEST_COLUMN_SHORTCUT_ID` column. In this case, the
  suggestion is never copied into a shortcut. This is only necessary if you
  absolutely don't want the previously copied suggestion to appear. If you
  provide a normal value for the column, then the suggestion shortcut
  appears only until the refresh query returns.
- Let the default shortcut behavior apply.

  Leave the `SUGGEST_COLUMN_SHORTCUT_ID` empty for each
  suggestion that doesn't change and that can be saved as a
  shortcut.

If none of your suggestions ever change, then you don't need the
`SUGGEST_COLUMN_SHORTCUT_ID` column.
| **Note:** Quick Search Box ultimately decides whether to create a shortcut for a suggestion, considering these values as a strong request from your app. There is no guarantee that the behavior you request for your suggestion shortcuts are fulfilled.

### About Quick Search Box suggestion ranking

Once you make your app's search suggestions available to Quick Search Box,
the Quick Search Box ranking determines how the suggestions are surfaced to the
user for a particular query. This might depend on how many other apps have
results for that query and how often the user selects your results compared to
those from other apps. There is no guarantee regarding how your suggestions are
ranked or whether your app's suggestions show at all for a given query. In
general, providing quality results increases the likelihood that your app's
suggestions are provided in a prominent position, and apps that provide
low-quality suggestions are more likely to be ranked lower or not displayed.