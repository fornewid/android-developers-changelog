---
title: https://developer.android.com/develop/ui/views/search/search-dialog
url: https://developer.android.com/develop/ui/views/search/search-dialog
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose.  
[Search bar →](https://developer.android.com/develop/ui/compose/components/search-bar)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

When you're ready to add search functionality to your app, Android helps you
implement the user interface with either a search dialog that appears at the top
of the activity window or a search widget that you can insert in your layout.
Both the search dialog and the widget can deliver the user's search query to a
specific activity in your app. This way, the user can initiate a search from any
activity where the search dialog or widget is available, and the system starts
the appropriate activity to perform the search and present results.

Other features available for the search dialog and widget include:

- Voice search
- Search suggestions based on recent queries
- Search suggestions that match actual results in your app data

This document shows how to set up your app to provide a search interface
that's assisted by the Android system to deliver search queries, using either
the search dialog or the search widget.

Related resources:

- [Material Design icons](https://material.io/icons/)

## The basics

Before you begin, decide whether you want to implement your search interface
using the search dialog or the search widget. They provide the same search
features, but in slightly different ways:

- The **search dialog** is a UI component that's controlled by the Android system. When activated by the user, the search dialog appears at the top of the activity.

  The Android system controls all events in the search dialog. When the
  user submits a query, the system delivers the query to the activity that
  you specify to handle searches. The dialog can also provide search
  suggestions while the user types.
- The **search widget** is an instance of [SearchView](https://developer.android.com/reference/android/widget/SearchView) that you can place anywhere in your layout. By default, the search widget behaves like a standard [EditText](https://developer.android.com/reference/android/widget/EditText) widget and doesn't do anything, but you can configure it so that the Android system handles all input events, delivers queries to the appropriate activity, and provides search suggestions---just like the search dialog.

| **Note:** This document focuses on how to integrate the search widget with the system for an assisted search implementation. But you can also handle all user input into the search widget yourself, using various callback methods and listeners. If you want to handle user input yourself, read the reference document for `SearchView` and its nested interfaces.

When the user executes a search from the search dialog or a search widget,
the system creates an
[Intent](https://developer.android.com/reference/android/content/Intent) and
stores the user query in it. The system then starts the activity that you
declare to handle searches---the "searchable activity"---and delivers it
the intent. To set up your app for this kind of assisted search, you need the
following:

The rest of this document shows you how to create the search configuration
and searchable activity and how to implement a search interface with either the
search dialog or search widget.

## Create a searchable configuration

The first thing you need is an XML file called a
[search configuration](https://developer.android.com/develop/ui/views/search/searchable-config).
It configures certain UI aspects of the search dialog or widget and defines how
features such as suggestions and voice search behave. This file is traditionally
named `searchable.xml` and must be saved in the `res/xml/`
project directory.
| **Note:** The system uses this file to instantiate a [SearchableInfo](https://developer.android.com/reference/android/app/SearchableInfo) object. You can't create this object yourself at runtime. You must declare the search configuration in XML.

The search configuration file must include the
[`<searchable>`](https://developer.android.com/guide/topics/search/searchable-config#searchable-element)
element as its root node and specify one or more attributes, as shown in the
following example:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_label"
    android:hint="@string/search_hint" >
</searchable>
```

The `android:label` attribute is the only required attribute. It
points to a string resource, which must be the app name. This label isn't
visible to the user until you enable search suggestions for Quick Search Box, at
which point the label is visible in the list of Searchable items in the system
settings.

Although it's not required, we recommend that you always include the
`android:hint` attribute, which provides a hint string in the search
box before users enter a query. The hint is important because it provides
important clues to users about what they can search.
| **Tip:** For consistency with other Android apps, format the string for `android:hint` as "Search \<content-or-product\>". For example, "Search songs and artists" or "Search YouTube."

The `<searchable>` element accepts several other attributes.
However, you don't need most attributes until you add features such as
[search suggestions](https://developer.android.com/develop/ui/views/search/search-dialog#SearchSuggestions) and
[voice search](https://developer.android.com/develop/ui/views/search/search-dialog#VoiceSearch). For detailed information about the
search configuration file, see the
[Search configuration](https://developer.android.com/guide/topics/search/searchable-config)
reference document.

## Create a searchable activity

A searchable activity is the `Activity` in your app that performs
searches based on a query string and presents the search results.

When the user executes a search in the search dialog or widget, the system
starts your searchable activity and delivers it the search query in an
`Intent` with the
[ACTION_SEARCH](https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH)
action. Your searchable activity retrieves the query from the intent's
[QUERY](https://developer.android.com/reference/android/app/SearchManager#QUERY)
extra, then searches your data and presents the results.

Because you can include the search dialog or widget in any other activity in
your app, the system must know which activity is your searchable activity so
that it can properly deliver the search query. So, first declare your searchable
activity in the Android manifest file.

### Declare a searchable activity

If you don't have one already, create an `Activity` that performs
searches and presents results. You don't need to implement the search
functionality yet---just create an activity that you can declare in the
manifest. Inside the manifest's
[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)
element, do the following:

1. Declare the activity to accept the `ACTION_SEARCH` intent in an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) element.
2. Specify the search configuration to use in a [<meta-data>](https://developer.android.com/guide/topics/manifest/meta-data-element) element.

This is shown in the following example:  

```xml
<application ... >
    <activity android:name=".SearchableActivity" >
        <intent-filter>
            <action android:name="android.intent.action.SEARCH" />
        </intent-filter>
        <meta-data android:name="android.app.searchable"
                   android:resource="@xml/searchable"/>
    </activity>
    ...
</application>
```

The `<meta-data>` element must include the
`android:name` attribute with a value of
`"android.app.searchable"` and the `android:resource`
attribute with a reference to the searchable configuration file. In the
preceding example, it refers to the `res/xml/searchable.xml`
file.
| **Note:** The `<intent-filter>` doesn't need a [`<category>`](https://developer.android.com/guide/topics/manifest/category-element) with the `DEFAULT` value---which you usually see in `<activity>` elements---because the system delivers the `ACTION_SEARCH` intent explicitly to your searchable activity using its component name.

### Perform a search

After you declare your searchable activity in the manifest, follow this
procedure to perform a search in your searchable activity:

1. [Receive the query](https://developer.android.com/develop/ui/views/search/search-dialog#ReceivingTheQuery).
2. [Search your data](https://developer.android.com/develop/ui/views/search/search-dialog#SearchingYourData).
3. [Present the results](https://developer.android.com/develop/ui/views/search/search-dialog#PresentingTheResults).

#### Receive the query

When a user executes a search from the search dialog or widget, the system
starts your searchable activity and sends it an `ACTION_SEARCH`
intent. This intent carries the search query in the `QUERY` string
extra. Check for this intent when the activity starts and extract the string.
For example, here's how you can get the search query when your searchable
activity starts:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.search)

    // Verify the action and get the query.
    if (Intent.ACTION_SEARCH == intent.action) {
        intent.getStringExtra(SearchManager.QUERY)?.also { query ->
            doMySearch(query)
        }
    }
}
```

### Java

```java
@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.search);

    // Get the intent, verify the action, and get the query.
    Intent intent = getIntent();
    if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
      String query = intent.getStringExtra(SearchManager.QUERY);
      doMySearch(query);
    }
}
```

The `QUERY` string is always included with the
`ACTION_SEARCH` intent. In the preceding example, the query is
retrieved and passed to a local `doMySearch()` method where the
actual search operation is done.

#### Search your data

The process of storing and searching your data is unique to your app. You can
store and search your data in many ways, and this document doesn't show you how.
Consider how you store and search your data in terms of your needs and your data
format. The following are tips you might be able to apply:

- If your data is stored in a SQLite database on the device, performing a full-text search---using FTS3, rather than a `LIKE` query---can provide a more robust search across text data and can produce results significantly faster. See [sqlite.org](http://sqlite.org/fts3.html) for information about FTS3 and the [SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase) class for information about SQLite on Android.
- If your data is stored online, then the perceived search performance might be inhibited by the user's data connection. You might want to display a progress indicator until your search returns. See [android.net](https://developer.android.com/reference/android/net/package-summary) for a reference of network APIs and [`ProgressBar`](https://developer.android.com/reference/android/widget/ProgressBar) for information about how to display a progress indicator.

| **Note:** If you plan to use a local database, see [Save data in a local database using
| Room](https://developer.android.com/training/data-storage/room).

#### Present the results

Regardless of where your data lives and how you search it, we recommend that
you return search results to your searchable activity with an
[Adapter](https://developer.android.com/reference/android/widget/Adapter). This
way, you can present all the search results in a
[RecyclerView](https://developer.android.com/develop/ui/views/layout/recyclerview).
If your data comes from a SQLite database query, you can apply your results to a
`RecyclerView` using a
[CursorAdapter](https://developer.android.com/reference/android/widget/CursorAdapter).
If your data comes in a different format, then you can create an extension of
[BaseAdapter](https://developer.android.com/reference/android/widget/BaseAdapter).

An `Adapter` binds each item from a set of data into a
[View](https://developer.android.com/reference/android/view/View) object. When
the `Adapter` is applied to a `RecyclerView`, each piece
of data is inserted as an individual view into the list. `Adapter` is
just an interface, so implementations such as
`CursorAdapter`---for binding data from a
[Cursor](https://developer.android.com/reference/android/database/Cursor)---are
needed. If none of the existing implementations work for your data, then you can
implement your own from `BaseAdapter`.

## Use the search dialog

The search dialog provides a floating search box at the top of the screen,
with the app icon on the left. The search dialog can provide search suggestions
as the user types. When the user executes a search, the system sends the search
query to a searchable activity that performs the search.

By default, the search dialog is always hidden until the user activates it.
Your app can activate the search dialog by calling
`onSearchRequested()`. However, this method doesn't work until you
enable the search dialog for the activity.

To enable the search dialog to perform searches, indicate to the system which
searchable activity must receive search queries from the search dialog. For
example, in the preceding section about
[creating a searchable activity](https://developer.android.com/develop/ui/views/search/search-dialog#SearchableActivity), a searchable
activity named `SearchableActivity` is created. If you want a
separate activity, such as one named `OtherActivity`, to show the
search dialog and deliver searches to `SearchableActivity`, declare
in the manifest that `SearchableActivity` is the searchable activity
to use for the search dialog in `OtherActivity`.

To declare the searchable activity for an activity's search dialog, add a
`<meta-data>` element inside the respective activity's
`<activity>` element. The `<meta-data>`
element must include the `android:value` attribute that specifies the
searchable activity's class name and the `android:name` attribute
with a value of `"android.app.default_searchable"`.

For example, here is the declaration for both a searchable activity,
`SearchableActivity`, and another activity,
`OtherActivity`, which uses `SearchableActivity` to
perform searches executed from its search dialog:  

```xml
<application ... >
    <!-- This is the searchable activity; it performs searches. -->
    <activity android:name=".SearchableActivity" >
        <intent-filter>
            <action android:name="android.intent.action.SEARCH" />
        </intent-filter>
        <meta-data android:name="android.app.searchable"
                   android:resource="@xml/searchable"/>
    </activity>

    <!-- This activity enables the search dialog to initiate searches
         in the SearchableActivity. -->
    <activity android:name=".OtherActivity" ... >
        <!-- Enable the search dialog to send searches to SearchableActivity. -->
        <meta-data android:name="android.app.default_searchable"
                   android:value=".SearchableActivity" />
    </activity>
    ...
</application>
```

Because `OtherActivity` now includes a
`<meta-data>` element to declare which searchable activity to
use for searches, the activity enables the search dialog. Although the user is
in this activity, the `onSearchRequested()` method activates the
search dialog. When the user executes the search, the system starts
`SearchableActivity` and delivers it the `ACTION_SEARCH`
intent.
| **Note:** The searchable activity itself provides the search dialog by default, so you don't need to add this declaration to `SearchableActivity`.

If you want every activity in your app to provide the search dialog, insert
the preceding `<meta-data>` element as a child of the
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)
element, instead of each `<activity>`. This way, every activity
inherits the value, provides the search dialog, and delivers searches to the
same searchable activity. If you have multiple searchable activities, you can
override the default searchable activity by placing a different
`<meta-data>` declaration inside individual activities.

With the search dialog now enabled for your activities, your app is ready to
perform searches.

### Invoke the search dialog

Although some devices provide a dedicated search button, the behavior of the
button might vary between devices, and many devices don't provide a search
button at all. So when using the search dialog, you must provide a search button
in your UI that activates the search dialog by calling
`onSearchRequested()`.

For example, add a search button in your
[options menu](https://developer.android.com/guide/topics/ui/menus#options-menu) or UI layout
that calls `onSearchRequested()`.
| **Note:** If your app uses an [app
| bar](https://developer.android.com/training/appbar), then don't use the search dialog for your search interface. Instead, use the [search widget](https://developer.android.com/develop/ui/views/search/search-dialog#UsingSearchWidget) as a collapsible view in the app bar.

You can also enable "type-to-search" functionality, which activates the
search dialog when the user starts typing on the keyboard. The keystrokes are
inserted into the search dialog. You can enable type-to-search in your activity
by calling
[setDefaultKeyMode](https://developer.android.com/reference/android/app/Activity#setDefaultKeyMode(int))---or
[DEFAULT_KEYS_SEARCH_LOCAL](https://developer.android.com/reference/android/app/Activity#DEFAULT_KEYS_SEARCH_LOCAL)---during
your activity's
[onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))
method.

### The impact of the search dialog on your activity lifecycle

The search dialog is a
[Dialog](https://developer.android.com/reference/android/app/Dialog) that floats
at the top of the screen. It doesn't cause any change in the activity stack, so
when the search dialog appears, no lifecycle methods---such as
[onPause()](https://developer.android.com/reference/android/app/Activity#onPause())---are
called. Your activity loses input focus, because input focus is given to the
search dialog.

If you want to be notified when the search dialog is activated, override the
`onSearchRequested()` method. When the system calls this method, it
is an indication that your activity loses input focus to the search dialog, so
you can do any work appropriate for the event, such as pausing a game. Unless
you are [passing search context
data](https://developer.android.com/develop/ui/views/search/search-dialog#SearchContextData)---discussed in another section of this document---end the
method by calling the superclass implementation:  

### Kotlin

```kotlin
override fun onSearchRequested(): Boolean {
    pauseSomeStuff()
    return super.onSearchRequested()
}
```

### Java

```java
@Override
public boolean onSearchRequested() {
    pauseSomeStuff();
    return super.onSearchRequested();
}
```

If the user cancels search by tapping the Back button, the search dialog
closes and the activity regains input focus. You can register to be notified
when the search dialog is closed with
[setOnDismissListener()](https://developer.android.com/reference/android/app/SearchManager#setOnDismissListener(android.app.SearchManager.OnDismissListener)),
[setOnCancelListener()](https://developer.android.com/reference/android/app/SearchManager#setOnCancelListener(android.app.SearchManager.OnCancelListener)),
or both. You only need to register the
[OnDismissListener](https://developer.android.com/reference/android/app/SearchManager.OnDismissListener),
because it is called every time the search dialog closes. The
[OnCancelListener](https://developer.android.com/reference/android/app/SearchManager.OnCancelListener)
only pertains to events in which the user explicitly exits the search dialog, so
it's not called when a search is executed. When the search is executed, the
search dialog automatically disappears.

If the current activity isn't the searchable activity, then the normal
activity lifecycle events are triggered when the user executes a
search---the current activity receives `onPause()`, as described
in [Introduction to
activities](https://developer.android.com/guide/components/activities#Lifecycle). However, if the current activity is the searchable activity,
then one of two things happens:

- By default, the searchable activity receives the `ACTION_SEARCH` intent with a call to `onCreate()`, and a new instance of the activity is brought to the top of the activity stack. There are now two instances of your searchable activity in the activity stack, so tapping the Back button takes you back to the previous instance of the searchable activity, rather than exiting the searchable activity.
- If you set `android:launchMode` to `"singleTop"`, then the searchable activity receives the `ACTION_SEARCH` intent with a call to [onNewIntent(Intent)](https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent)), passing the new `ACTION_SEARCH` intent. For example, here's how you might handle this case, in which the searchable activity's launch mode is `"singleTop"`:  

  ### Kotlin

  ```kotlin
  override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      setContentView(R.layout.search)
      handleIntent(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
      setIntent(intent)
      handleIntent(intent)
  }

  private fun handleIntent(intent: Intent) {
      if (Intent.ACTION_SEARCH == intent.action) {
          intent.getStringExtra(SearchManager.QUERY)?.also { query ->
              doMySearch(query)
          }
      }
  }
  ```

  ### Java

  ```java
  @Override
  public void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.search);
      handleIntent(getIntent());
  }

  @Override
  protected void onNewIntent(Intent intent) {
      super.onNewIntent(intent);
      setIntent(intent);
      handleIntent(intent);
  }

  private void handleIntent(Intent intent) {
      if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
        String query = intent.getStringExtra(SearchManager.QUERY);
        doMySearch(query);
      }
  }
  ```

  Compared to the example code in the section about
  [performing a search](https://developer.android.com/develop/ui/views/search/search-dialog#PerformingSearch), all the code to handle the
  search intent is now in the `handleIntent()` method, so that both
  `onCreate()` and `onNewIntent()` can execute it.

  When the system calls `onNewIntent(Intent)`, the activity isn't
  restarted, so the
  [getIntent()](https://developer.android.com/reference/android/app/Activity#getIntent())
  method returns the same intent that is received with `onCreate()`.
  This is why you must call
  [setIntent(Intent)](https://developer.android.com/reference/android/app/Activity#setIntent(android.content.Intent))
  inside `onNewIntent(Intent)`: so that the intent saved by the
  activity is updated in case you call `getIntent()` in the future.

The second scenario, using `"singleTop"` launch mode, is usually
preferable, because after a search is done, the user might perform additional
searches, and you don't want your app to create multiple instances of the
searchable activity. We recommend that you set your searchable activity to
`"singleTop"` launch mode in the app manifest, as shown in the
following example:  

```xml
<activity android:name=".SearchableActivity"
          android:launchMode="singleTop" >
    <intent-filter>
        <action android:name="android.intent.action.SEARCH" />
    </intent-filter>
    <meta-data
          android:name="android.app.searchable"
          android:resource="@xml/searchable"/>
  </activity>
```

### Pass search context data

In some cases, you can make necessary refinements to the search query inside
the searchable activity for every search made. However, if you want to refine
your search criteria based on the activity from which the user is performing a
search, you can provide additional data in the intent that the system sends to
your searchable activity. You can pass the additional data in the
[APP_DATA](https://developer.android.com/reference/android/app/SearchManager#APP_DATA)
[Bundle](https://developer.android.com/reference/android/os/Bundle), which is
included in the `ACTION_SEARCH` intent.

To pass this kind of data to your searchable activity, override the
`onSearchRequested()` method for the activity from which the user can
perform a search, create a `Bundle` with the additional data, and
call
[startSearch()](https://developer.android.com/reference/android/app/Activity#startSearch(java.lang.String, boolean, android.os.Bundle, boolean))
to activate the search dialog. For example:  

### Kotlin

```kotlin
override fun onSearchRequested(): Boolean {
    val appData = Bundle().apply {
        putBoolean(JARGON, true)
    }
    startSearch(null, false, appData, false)
    return true
}
```

### Java

```java
@Override
public boolean onSearchRequested() {
     Bundle appData = new Bundle();
     appData.putBoolean(SearchableActivity.JARGON, true);
     startSearch(null, false, appData, false);
     return true;
 }
```

Returning true indicates that you successfully handle this callback event and
call `startSearch()` to activate the search dialog. After the user
submits a query, it is delivered to your searchable activity along with the data
you add. You can extract the extra data from the `APP_DATA`
`Bundle` to refine the search, as shown in the following example:  

### Kotlin

```kotlin
val jargon: Boolean = intent.getBundleExtra(SearchManager.APP_DATA)?.getBoolean(JARGON) ?: false
```

### Java

```java
Bundle appData = getIntent().getBundleExtra(SearchManager.APP_DATA);
if (appData != null) {
    boolean jargon = appData.getBoolean(SearchableActivity.JARGON);
}
```
| **Caution:** Never call the `startSearch()` method from outside the `onSearchRequested()` callback method. To activate the search dialog in your activity, always call `onSearchRequested()`. Otherwise, `onSearchRequested()` isn't called and customizations---such as the addition of `appData` in the preceding example---are missed.

## Use the search widget

![An image showing a search view in the app top bar](https://developer.android.com/static/images/ui/search-ui-topbar-33.png)

**Figure 1.** The `SearchView`widget as
an action view in the app bar.

The search widget provides the same functionality as the search dialog. It
starts the appropriate activity when the user executes a search, and it can
provide search suggestions and perform voice search. If it's not an option for
you to put the search widget in the app bar, you can instead put the search
widget somewhere in your activity layout.
| **Note:** When you use the search widget as an action view, you still might need to support using the search dialog for cases when the search widget doesn't fit in the app bar. See the section about [using
| both the widget and the dialog](https://developer.android.com/develop/ui/views/search/search-dialog#UsingBoth).

### Configure the search widget

After you create a
[search configuration](https://developer.android.com/develop/ui/views/search/search-dialog#SearchableConfiguration) and a
[searchable activity](https://developer.android.com/develop/ui/views/search/search-dialog#SearchableActivity), enable assisted search
for each `SearchView` by calling
[setSearchableInfo()](https://developer.android.com/reference/android/widget/SearchView#setSearchableInfo(android.app.SearchableInfo))
and passing it the `SearchableInfo` object that represents your
searchable configuration.

You can get a reference to the `SearchableInfo` by calling
[getSearchableInfo()](https://developer.android.com/reference/android/app/SearchManager#getSearchableInfo(android.content.ComponentName))
on
[SearchManager](https://developer.android.com/reference/android/app/SearchManager).

For example, if you're using a `SearchView` as an action view in
the app bar, enable the widget during the
[onCreateOptionsMenu()](https://developer.android.com/reference/android/app/Activity#onCreateOptionsMenu(android.view.Menu))
callback, as shown in the following example:  

### Kotlin

```kotlin
override fun onCreateOptionsMenu(menu: Menu): Boolean {
    // Inflate the options menu from XML.
    val inflater = menuInflater
    inflater.inflate(R.menu.options_menu, menu)

    // Get the SearchView and set the searchable configuration.
    val searchManager = getSystemService(Context.SEARCH_SERVICE) as SearchManager
    (menu.findItem(R.id.menu_search).actionView as SearchView).apply {
        // Assumes current activity is the searchable activity.
        setSearchableInfo(searchManager.getSearchableInfo(componentName))
        setIconifiedByDefault(false) // Don't iconify the widget. Expand it by default.
    }

    return true
}
```

### Java

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    // Inflate the options menu from XML.
    MenuInflater inflater = getMenuInflater();
    inflater.inflate(R.menu.options_menu, menu);

    // Get the SearchView and set the searchable configuration.
    SearchManager searchManager = (SearchManager) getSystemService(Context.SEARCH_SERVICE);
    SearchView searchView = (SearchView) menu.findItem(R.id.menu_search).getActionView();
    // Assumes current activity is the searchable activity.
    searchView.setSearchableInfo(searchManager.getSearchableInfo(getComponentName()));
    searchView.setIconifiedByDefault(false); // Don't iconify the widget. Expand it by default.

    return true;
}
```

The search widget is now configured, and the system delivers search queries
to your searchable activity. You can also enable
[search suggestions](https://developer.android.com/develop/ui/views/search/search-dialog#SearchSuggestions) for the search widget.
| **Note:** If you want to handle all user input yourself, you can do so with some callback methods and event listeners. For more information, see the reference documentation for `SearchView` and its nested interfaces.

For more information about action views in the app bar, see
[Use action views and action
providers](https://developer.android.com/training/appbar/action-views).

### Other search widget features

The `SearchView` widget provides a few additional features you
might want:

A submit button
:   By default, there's no button to submit a search query, so the user has to
    press the <kbd>Return</kbd> key on the keyboard to initiate a search. You
    can add a "submit" button by calling
    [setSubmitButtonEnabled(true)](https://developer.android.com/reference/android/widget/SearchView#setSubmitButtonEnabled(boolean)).

Query refinement for search suggestions
:   When you enable search suggestions, you usually expect users to select a
    suggestion, but they might also want to refine the suggested search query.
    You can add a button alongside each suggestion that inserts the suggestion
    in the search box for refinement by the user by calling
    [setQueryRefinementEnabled(true)](https://developer.android.com/reference/android/widget/SearchView#setQueryRefinementEnabled(boolean)).

The ability to toggle search box visibility
:   By default, the search widget is "iconified," meaning that it is
    represented only by a search icon---a magnifying glass. It expands to
    show the search box when the user taps the icon. As shown in the preceding
    example, you can show the search box by default by calling
    [setIconifiedByDefault(false)](https://developer.android.com/reference/android/widget/SearchView#setIconifiedByDefault(boolean)).
    You can also toggle the search widget appearance by calling
    [setIconified()](https://developer.android.com/reference/android/widget/SearchView#setIconified(boolean)).

There are several other APIs in the `SearchView` class that let
you customize the search widget. However, most of them are used only when you
handle all user input yourself, instead of using the Android system to deliver
search queries and display search suggestions.

### Use both the widget and the dialog

If you insert the search widget in the app bar as an
[action view](https://developer.android.com/guide/topics/ui/actionbar#ActionView) and enable
it to appear in the app bar if there is room---by setting
`android:showAsAction="ifRoom"`---then the search widget might
not appear as an action view. Instead, a menu item might appear in the overflow
menu. For example, when your app runs on a smaller screen, there might not be
enough room in the app bar to display the search widget along with other action
items or navigation elements, so the menu item instead appears in the overflow
menu. When placed in the overflow menu, the item works like an ordinary menu
item and doesn't display the action view---that is, the search widget.

To handle this situation, the menu item to which you attach the search widget
must activate the search dialog when the user selects it from the overflow menu.
To make this happen, implement
[onOptionsItemSelected()](https://developer.android.com/reference/android/app/Activity#onOptionsItemSelected(android.view.MenuItem))
to handle the "Search" menu item and open the search dialog by calling
`onSearchRequested()`.

For more information about how items in the app bar work and how to handle
this situation, see
[Add the app bar](https://developer.android.com/guide/topics/ui/actionbar).

## Add voice search

You can add voice search functionality to your search dialog or widget by
adding the `android:voiceSearchMode` attribute to your searchable
configuration. This adds a voice search button that launches a voice prompt.
When the user finishes speaking, the transcribed search query is sent to your
searchable activity.

This is shown in the following example:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<searchable xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/search_label"
    android:hint="@string/search_hint"
    android:voiceSearchMode="showVoiceSearchButton|launchRecognizer" >
</searchable>
```

The value `showVoiceSearchButton` is required to enable voice
search. The second value, `launchRecognizer`, specifies that the
voice search button must launch a *recognizer* that returns the
transcribed text to the searchable activity.

You can provide additional attributes to specify the voice search behavior,
such as the expected language and the maximum number of results to return. See
the [Search configuration](https://developer.android.com/develop/ui/views/search/searchable-config) reference for more
information about the available attributes.
| **Note:** Carefully consider whether voice search is appropriate for your app. Searches performed with the voice search button are immediately sent to your searchable activity, without a chance for the user to review the transcribed query. Test the voice recognition and ensure that it understands the types of queries that the user might submit in your app.

## Add search suggestions

Both the search dialog and the search widget can provide search suggestions
as the user types, with assistance from the Android system. The system manages
the list of suggestions and handles the event when the user selects a
suggestion.

You can provide two kinds of search suggestions:

Recent query search suggestions
:   These suggestions are words that the user previously used as search
    queries in your app. See [Add
    custom search suggestions](https://developer.android.com/develop/ui/views/search/adding-recent-query-suggestions) for more information.

Custom search suggestions
:   These are search suggestions that you provide from your own data source to
    help users immediately select the correct spelling or item they are searching
    for. See [Add custom search
    suggestions](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions) for more information.