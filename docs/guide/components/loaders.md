---
title: https://developer.android.com/guide/components/loaders
url: https://developer.android.com/guide/components/loaders
source: md.txt
---

Loaders are deprecated as of Android 9 (API level 28). The recommended option for
dealing with loading data while handling the `Activity` and `Fragment` lifecycles is to use a
combination of [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) objects
and [`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData).
View models survive configuration changes, like loaders, but with
less boilerplate code. `LiveData` provides a lifecycle-aware way of loading data that you can reuse in
multiple view models. You can also combine `LiveData` using
[`MediatorLiveData`](https://developer.android.com/reference/androidx/lifecycle/MediatorLiveData).
Any observable queries, such as those from a
[Room database](https://developer.android.com/topic/libraries/architecture/room), can be used to observe changes
to the data.  


`ViewModel` and `LiveData` are also available in situations where you don't have access
to the [`LoaderManager`](https://developer.android.com/reference/android/app/LoaderManager), such as in a
[`Service`](https://developer.android.com/reference/android/app/Service). Using the two in
tandem provides an easy way to access the data your app needs without having to deal with the UI
lifecycle. To learn more about `LiveData`, see the
[`LiveData` overview](https://developer.android.com/topic/libraries/architecture/livedata). To learn more about
`ViewModel`, see the [`ViewModel` overview](https://developer.android.com/topic/libraries/architecture/viewmodel).

The Loader API lets you load data from a
[content provider](https://developer.android.com/guide/topics/providers/content-providers)
or other data source for display in a `https://developer.android.com/reference/androidx/fragment/app/FragmentActivity`
or `https://developer.android.com/reference/androidx/fragment/app/Fragment`.

Without loaders, some of the problems you might encounter include the following:

- If you fetch the data directly in the activity or fragment, your users suffer from lack of responsiveness due to performing potentially slow queries from the UI thread.
- If you fetch the data from another thread, perhaps with `https://developer.android.com/reference/android/os/AsyncTask`, then you're responsible for managing both that thread and the UI thread through various activity or fragment lifecycle events, such as `https://developer.android.com/reference/android/app/Activity#onDestroy()` and configuration changes.

Loaders solve these problems and include other benefits:

- Loaders run on separate threads to prevent a slow or unresponsive UI.
- Loaders simplify thread management by providing callback methods when events occur.
- Loaders persist and cache results across configuration changes to prevent duplicate queries.
- Loaders can implement an observer to monitor for changes in the underlying data source. For example, `https://developer.android.com/reference/androidx/loader/content/CursorLoader` automatically registers a `https://developer.android.com/reference/android/database/ContentObserver` to trigger a reload when data changes.

## Loader API summary

There are multiple classes and interfaces that might be involved when using
loaders in an app. They are summarized in the following table:

| Class/Interface | Description |
|---|---|
| `https://developer.android.com/reference/androidx/loader/app/LoaderManager` | An abstract class associated with a `https://developer.android.com/reference/androidx/fragment/app/FragmentActivity` or `https://developer.android.com/reference/androidx/fragment/app/Fragment` for managing one or more `https://developer.android.com/reference/androidx/loader/content/Loader` instances. There is only one `LoaderManager` per activity or fragment, but a `LoaderManager` can manage multiple loaders. To get a `LoaderManager`, call `https://developer.android.com/reference/androidx/fragment/app/FragmentActivity#getSupportLoaderManager()` from the activity or fragment. To start loading data from a loader, call either `https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)` or `https://developer.android.com/reference/androidx/loader/app/LoaderManager#restartLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)`. The system automatically determines whether a loader with the same integer ID already exists and either creates a new loader or reuses an existing loader. |
| `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks` | This interface contains callback methods that are called when loader events occur. The interface defines three callback methods: - `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)`: called when the system needs a new loader to be created. In your code, create a `https://developer.android.com/reference/androidx/loader/content/Loader` object and return it to the system. - `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(androidx.loader.content.Loader%3CD%3E,D)`: called when a loader has finished loading data. You typically display the data to the user in your code. - `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoaderReset(androidx.loader.content.Loader%3CD%3E)`: called when a previously created loader is being reset, when you call `https://developer.android.com/reference/androidx/loader/app/LoaderManager#destroyLoader(int)` or when the activity or fragment is destroyed, making its data unavailable. In your code, remove any references to the loader's data. Your activity or fragment typically implements this interface, and it is registered when you call `https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)` or `https://developer.android.com/reference/androidx/loader/app/LoaderManager#restartLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)`. |
| `https://developer.android.com/reference/androidx/loader/content/Loader` | Loaders perform the loading of data. This class is abstract and serves as the base class for all loaders. You can directly subclass `Loader` or use one of the following built-in subclasses to simplify implementation: - `https://developer.android.com/reference/androidx/loader/content/AsyncTaskLoader`: an abstract loader that provides an `https://developer.android.com/reference/android/os/AsyncTask` to perform load operations on a separate thread. - `https://developer.android.com/reference/androidx/loader/content/CursorLoader`: a concrete subclass of `https://developer.android.com/reference/androidx/loader/content/AsyncTaskLoader` for asynchronously loading data from a `https://developer.android.com/reference/android/content/ContentProvider`. It queries a `https://developer.android.com/reference/android/content/ContentResolver` and returns a `https://developer.android.com/reference/android/database/Cursor`. |

The following sections show you how to use these
classes and interfaces in an application.

## Use loaders in an application

This section describes how to use loaders in an Android application. An
application that uses loaders typically includes the following:

- A `https://developer.android.com/reference/androidx/fragment/app/FragmentActivity` or `https://developer.android.com/reference/androidx/fragment/app/Fragment`.
- An instance of the `https://developer.android.com/reference/androidx/loader/app/LoaderManager`.
- A `https://developer.android.com/reference/androidx/loader/content/CursorLoader` to load data backed by a `https://developer.android.com/reference/android/content/ContentProvider`. Alternatively, you can implement your own subclass of `https://developer.android.com/reference/androidx/loader/content/Loader` or `https://developer.android.com/reference/androidx/loader/content/AsyncTaskLoader` to load data from some other source.
- An implementation for `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks`. This is where you create new loaders and manage your references to existing loaders.
- A way of displaying the loader's data, such as a `https://developer.android.com/reference/android/widget/SimpleCursorAdapter`.
- A data source, such as a `https://developer.android.com/reference/android/content/ContentProvider`, when using a `https://developer.android.com/reference/androidx/loader/content/CursorLoader`.

### Start a loader

The `https://developer.android.com/reference/androidx/loader/app/LoaderManager` manages one or more `https://developer.android.com/reference/androidx/loader/content/Loader` instances within a `https://developer.android.com/reference/androidx/fragment/app/FragmentActivity` or
`https://developer.android.com/reference/androidx/fragment/app/Fragment`. There is only one `LoaderManager` per activity or fragment.

You typically
initialize a `Loader` within the activity's `https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)` method or the fragment's
`https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate(android.os.Bundle)` method. You
do this as follows:

### Kotlin

```kotlin
supportLoaderManager.initLoader(0, null, this)
```

### Java

```java
// Prepare the loader.  Either re-connect with an existing one,
// or start a new one.
getSupportLoaderManager().initLoader(0, null, this);
```

The `https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)` method takes
the following parameters:

- A unique ID that identifies the loader. In this example, the ID is `0`.
- Optional arguments to supply to the loader at construction (`null` in this example).
- A `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks` implementation, which the `LoaderManager` calls to report loader events. In this example, the local class implements the `LoaderManager.LoaderCallbacks` interface, so it passes a reference to itself, `this`.

The `initLoader()` call ensures that a loader
is initialized and active. It has two possible outcomes:

- If the loader specified by the ID already exists, the last created loader is reused.
- If the loader specified by the ID does *not* exist, `initLoader()` triggers the `LoaderManager.LoaderCallbacks` method `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)`. This is where you implement the code to instantiate and return a new loader. For more discussion, see the section about [`onCreateLoader`](https://developer.android.com/guide/components/loaders#onCreateLoader).

In either case, the given `LoaderManager.LoaderCallbacks`
implementation is associated with the loader and is called when the
loader state changes. If, at the point of this call, the caller is in its
started state and the requested loader already exists and has generated its
data, then the system calls `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(androidx.loader.content.Loader%3CD%3E,D)`
immediately, during `initLoader()`. You must be prepared for this to happen. For more discussion of this callback, see the section about [`onLoadFinished`](https://developer.android.com/guide/components/loaders#onLoadFinished).

The `initLoader()` method returns the `Loader` that is created,
but you don't need to capture a reference to it. The `LoaderManager` manages
the life of the loader automatically. The `LoaderManager`
starts and stops loading when necessary and maintains the state of the loader
and its associated content.

As this implies, you rarely interact with loaders
directly.
You most commonly use the `LoaderManager.LoaderCallbacks` methods to intervene in the loading
process when particular events occur. For more discussion of this topic, see the [Using the LoaderManager callbacks](https://developer.android.com/guide/components/loaders#callback) section.

### Restart a loader

When you use `https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)`, as
shown in the preceding section, it uses an existing loader with the specified ID if there is one.
If there isn't, it creates one. But sometimes you want to discard your old data
and start over.

To discard your old data, use `https://developer.android.com/reference/androidx/loader/app/LoaderManager#restartLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)`. For example, the following
implementation of `https://developer.android.com/reference/android/widget/SearchView.OnQueryTextListener` restarts
the loader when the user's query changes. The loader needs to be restarted so
that it can use the revised search filter to do a new query.

### Kotlin

```kotlin
fun onQueryTextChanged(newText: String?): Boolean {
    // Called when the action bar search text has changed.  Update
    // the search filter and restart the loader to do a new query
    // with this filter.
    curFilter = if (newText?.isNotEmpty() == true) newText else null
    supportLoaderManager.restartLoader(0, null, this)
    return true
}
```

### Java

```java
public boolean onQueryTextChanged(String newText) {
    // Called when the action bar search text has changed.  Update
    // the search filter, and restart the loader to do a new query
    // with this filter.
    curFilter = !TextUtils.isEmpty(newText) ? newText : null;
    getSupportLoaderManager().restartLoader(0, null, this);
    return true;
}
```

### Use the LoaderManager callbacks

`https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks` is a callback interface
that lets a client interact with the `https://developer.android.com/reference/androidx/loader/app/LoaderManager`.

Loaders, in particular `https://developer.android.com/reference/androidx/loader/content/CursorLoader`, are expected to
retain their data after being stopped. This lets applications keep their
data across the activity or fragment's `https://developer.android.com/reference/android/app/Activity#onStop()` and `https://developer.android.com/reference/android/app/Activity#onStart()` methods, so that
when users return to an application, they don't have to wait for the data to
reload.

You use the `LoaderManager.LoaderCallbacks` methods to know when to create a new loader and to tell the application when it is
time to stop using a loader's data.

`LoaderManager.LoaderCallbacks` includes these
methods:

- `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)`: instantiates and returns a new `https://developer.android.com/reference/androidx/loader/content/Loader` for the given ID.

<!-- -->

- `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(androidx.loader.content.Loader%3CD%3E,D)`: called when a previously created loader has finished its load.

<!-- -->

- `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoaderReset(androidx.loader.content.Loader%3CD%3E)`: called when a previously created loader is being reset, thus making its data unavailable.

These methods are described in more detail in the following sections.

#### onCreateLoader

When you attempt to access a loader, such as through `https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int,android.os.Bundle,androidx.loader.app.LoaderManager.LoaderCallbacks%3CD%3E)`, it checks to see whether
the loader specified by the ID exists. If it doesn't, it triggers the `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks` method `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)`. This
is where you create a new loader. Typically this is a `https://developer.android.com/reference/androidx/loader/content/CursorLoader`, but you can implement your own `https://developer.android.com/reference/androidx/loader/content/Loader` subclass.

In the following example, the `onCreateLoader()`
callback method creates a `CursorLoader` using its constructor method, which
requires the complete set of information needed to perform a query to the `https://developer.android.com/reference/android/content/ContentProvider`. Specifically, it needs the following:

- *uri*: the URI for the content to retrieve.
- *projection* : a list of which columns to return. Passing `null` returns all columns, which is inefficient.
- *selection* : a filter declaring which rows to return, formatted as a SQL WHERE clause (excluding the WHERE itself). Passing `null` returns all rows for the given URI.
- *selectionArgs* : if you include ?s in the selection, they are replaced by the values from *selectionArgs* in the order that they appear in the selection. The values are bound as strings.
- *sortOrder* : how to order the rows, formatted as a SQL ORDER BY clause (excluding the ORDER BY itself). Passing `null` uses the default sort order, which might be unordered.

### Kotlin

```kotlin
// If non-null, this is the current filter the user has provided.
private var curFilter: String? = null
...
override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
    // This is called when a new Loader needs to be created.  This
    // sample only has one Loader, so we don't care about the ID.
    // First, pick the base URI to use depending on whether we are
    // currently filtering.
    val baseUri: Uri = if (curFilter != null) {
        Uri.withAppendedPath(ContactsContract.Contacts.CONTENT_URI, Uri.encode(curFilter))
    } else {
        ContactsContract.Contacts.CONTENT_URI
    }

    // Now create and return a CursorLoader that will take care of
    // creating a Cursor for the data being displayed.
    val select: String = "((${Contacts.DISPLAY_NAME} NOTNULL) AND (" +
            "${Contacts.HAS_PHONE_NUMBER}=1) AND (" +
            "${Contacts.DISPLAY_NAME} != ''))"
    retu>rn (activity as? Context)?.let { context -
        CursorLoader(
                context,
                baseUri,
                CONTACTS_SUMMARY_PROJECTION,
                select,
                null,
                "${Contacts.DISPLAY_NAME} COLLATE LOCALIZED ASC"
        )
    } ?: throw Exception("Activity cannot be null")
}
```

### Java

```java
// If non-null, this is the current filter the user has provided.
String curFilter;
...
public Loader<Cursor> onCreateLoader(int id, Bundle args) {
    // This is called when a new Loader needs to be created.  This
    // sample only has one Loader, so we don't care about the ID.
    // First, pick the base URI to use depending on whether we are
    // currently filtering.
    Uri baseUri;
    if (curFilter != null) {
        baseUri = Uri.withAppendedPath(Contacts.CONTENT_FILTER_URI,
                  Uri.encode(curFilter));
    } else {
        baseUri = Contacts.CONTENT_URI;
    }

    // Now create and return a CursorLoader that will take care of
    // creating a Cursor for the data being displayed.
    String select = "((" + Contacts.DISPLAY_NAME + " NOTNULL) AND ("
            + Contacts.HAS_PHONE_NUMBER + "=1) AND ("
            + Contacts.DISPLAY_NAME + " != '' ))";
    return new CursorLoader(getActivity(), baseUri,
            CONTACTS_SUMMARY_PROJECTION, select, null,
            Contacts.DISPLAY_NAME + " COLLATE LOCALIZED ASC");
}
```

#### onLoadFinished

This method is called when a previously created loader finishes its load.
This method is guaranteed to be called prior to the release of the last data
that is supplied for this loader. At this point, remove all use of
the old data, since it's going to be released. But don't release the data
yourself---the loader owns it and takes care of that.

The loader releases the data once it knows the application is no longer
using it. For example, if the data is a cursor from a `https://developer.android.com/reference/androidx/loader/content/CursorLoader`,
don't call `https://developer.android.com/reference/android/database/Cursor#close()` on it yourself. If the cursor is being
placed in a `https://developer.android.com/reference/android/widget/CursorAdapter`, use the `https://developer.android.com/reference/android/widget/SimpleCursorAdapter#swapCursor(android.database.Cursor)` method so that the
old `https://developer.android.com/reference/android/database/Cursor` is not closed, as shown in the following example:

### Kotlin

```kotlin
private lateinit var adapter: SimpleCursorAdapter
...
override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor?) {
    // Swap the new cursor in. (The framework will take care of closing the
    // old cursor once we return.)
    adapter.swapCursor(data)
}
```

### Java

```java
// This is the Adapter being used to display the list's data.
SimpleCursorAdapter adapter;
...
public void onLoadFinished(Lo<aderCu>rsor loader, Cursor data) {
    // Swap the new cursor in. (The framework will take care of closing the
    // old cursor once we return.)
    adapter.swapCursor(data);
}
```

#### onLoaderReset

This method is called when a previously created loader is being reset, thus
making its data unavailable. This callback lets you find out when the data is
about to be released so you can remove your reference to it.

This implementation calls
`https://developer.android.com/reference/android/widget/SimpleCursorAdapter#swapCursor(android.database.Cursor)`
with a value of `null`:

### Kotlin

```kotlin
private lateinit var adapter: SimpleCursorAdapter
...
override fun onLoaderReset(loader: Loader<Cursor>) {
    // This is called when the last Cursor provided to onLoadFinished()
    // above is about to be closed.  We need to make sure we are no
    // longer using it.
    adapter.swapCursor(null)
}
```

### Java

```java
// This is the Adapter being used to display the list's data.
SimpleCursorAdapter adapter;
...
public void onLoaderReset(Lo<aderCu>rsor loader) {
    // This is called when the last Cursor provided to onLoadFinished()
    // above is about to be closed.  We need to make sure we are no
    // longer using it.
    adapter.swapCursor(null);
}
```

## Example

As an example, here is the full implementation of a `https://developer.android.com/reference/androidx/fragment/app/Fragment` that displays a `https://developer.android.com/reference/android/widget/ListView` containing
the results of a query against the contacts content provider. It uses a `https://developer.android.com/reference/androidx/loader/content/CursorLoader` to manage the query on the provider.

Because this example is from an application to access a user's contacts, its
manifest must include the permission
`https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS`.

### Kotlin

```kotlin
private val CONTACTS_SUMMARY_PROJECTION: Array<String> = arrayOf(
        Contacts._ID,
        Contacts.DISPLAY_NAME,
        Contacts.CONTACT_STATUS,
        Contacts.CONTACT_PRESENCE,
        Contacts.PHOTO_ID,
        Contacts.LOOKUP_KEY
)


class CursorLoaderListFragment :
        ListFragment(),
        SearchView.OnQueryTextListener,
        LoaderManager.LoaderCallbacks<Cursor> {

    // This is the Adapter being used to display the list's data.
    private lateinit var mAdapter: SimpleCursorAdapter

    // If non-null, this is the current filter the user has provided.
    private var curFilter: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Prepare the loader.  Either re-connect with an existing one,
        // or start a new one.
        loaderManager.initLoader(0, null, this)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Give some text to display if there is no data.  In a real
        // application, this would come from a resource.
        setEmptyText("No phone numbers")

        // We have a menu item to show in action bar.
        setHasOptionsMenu(true)

        // Create an empty adapter we will use to display the loaded data.
        mAdapter = SimpleCursorAdapter(activity,
                android.R.layout.simple_list_item_2,
                null,
                arrayOf(Contacts.DISPLAY_NAME, Contacts.CONTACT_STATUS),
                intArrayOf(android.R.id.text1, android.R.id.text2),
                0
        )
        listAdapter = mAdapter
    }

    override fun onCreateOptionsMenu(menu: Menu, inflater: MenuInflater) {
        // Place an action bar item for searching.
        menu.add("Search").apply {
            setIcon(android.R.drawable.ic_menu_search)
            setShowAsAction(MenuItem.SHOW_AS_ACTION_IF_ROOM)
            actionView = SearchView(activity).apply {
                setOnQueryTextListener(this@CursorLoaderListFragment)
            }
        }
    }

    override fun onQueryTextChange(newText: String?): Boolean {
        // Called when the action bar search text has changed.  Update
        // the search filter, and restart the loader to do a new query
        // with this filter.
        curFilter = if (newText?.isNotEmpty() == true) newText else null
        loaderManager.restartLoader(0, null, this)
        return true
    }

    override fun onQueryTextSubmit(query: String): Boolean {
        // Don't care about this.
        return true
    }

    override fun onListItemClick(l: ListView, v: View, position: Int, id: Long) {
        // Insert desired behavior here.
        Log.i("FragmentComplexList", "Item clicked: $id")
    }

    override fu<n onCr>eateLoader(id: Int, args: Bundle?): LoaderCursor {
        // This is called when a new Loader needs to be created.  This
        // sample only has one Loader, so we don't care about the ID.
        // First, pick the base URI to use depending on whether we are
        // currently filtering.
        val baseUri: Uri = if (curFilter != null) {
            Uri.withAppendedPath(Contacts.CONTENT_URI, Uri.encode(curFilter))
        } else {
            Contacts.CONTENT_URI
        }

        // Now create and return a CursorLoader that will take care of
        // creating a Cursor for the data being displayed.
        val select: String = "((${Contacts.DISPLAY_NAME} NOTNULL) AND (" +
                "${Contacts.HAS_PHONE_NUMBER}=1) AND (" +
                "${Contacts.>DISPLAY_NAME} != ''))"
        return (activity as? Context)?.let { context -
            CursorLoader(
                    context,
                    baseUri,
                    CONTACTS_SUMMARY_PROJECTION,
                    select,
                    null,
                    "${Contacts.DISPLAY_NAME} COLLATE LOCALIZED ASC"
            )
        }< ?: th>row Exception("Activity cannot be null")
    }

    override fun onLoadFinished(loader: LoaderCursor, data: Cursor) {
        // Swap the new cursor in.  (The framework will take care of closing the
        // old <cursor> once we return.)
        mAdapter.swapCursor(data)
    }

    override fun onLoaderReset(loader: LoaderCursor) {
        // This is called when the last Cursor provided to onLoadFinished()
        // above is about to be closed.  We need to make sure we are no
        // longer using it.
        mAdapter.swapCursor(null)
    }
}
```

### Java

```java
public static class CursorLoaderListFragment extends ListFragment
        implements OnQueryTextListener, LoaderManager.LoaderCallbacks<Cursor> {

    // This is the Adapter being used to display the list's data.
    SimpleCursorAdapter mAdapter;

    // If non-null, this is the current filter the user has provided.
    String curFilter;

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Prepare the loader.  Either re-connect with an existing one,
        // or start a new one.
        getLoaderManager().initLoader(0, null, this);
    }

    @Override public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // Give some text to display if there is no data.  In a real
        // application, this would come from a resource.
        setEmptyText("No phone numbers");

        // We have a menu item to show in action bar.
        setHasOptionsMenu(true);

        // Create an empty adapter we will use to display the loaded data.
        mAdapter = new SimpleCursorAdapter(getActivity(),
                android.R.layout.simple_list_item_2, null,
                new String[] { Contacts.DISPLAY_NAME, Contacts.CONTACT_STATUS },
                new int[] { android.R.id.text1, android.R.id.text2 }, 0);
        setListAdapter(mAdapter);
    }

    @Override public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        // Place an action bar item for searching.
        MenuItem item = menu.add("Search");
        item.setIcon(android.R.drawable.ic_menu_search);
        item.setShowAsAction(MenuItem.SHOW_AS_ACTION_IF_ROOM);
        SearchView sv = new SearchView(getActivity());
        sv.setOnQueryTextListener(this);
        item.setActionView(sv);
    }

    public boolean onQueryTextChange(String newText) {
        // Called when the action bar search text has changed.  Update
        // the search filter, and restart the loader to do a new query
        // with this filter.
        curFilter = !TextUtils.isEmpty(newText) ? newText : null;
        getLoaderManager().restartLoader(0, null, this);
        return true;
    }

    @Override public boolean onQueryTextSubmit(String query) {
        // Don't care about this.
        return true;
    }

    @Override public void onListItemClick(ListView l, View v, int position, long id) {
        // Insert desired behavior here.
        Log.i("FragmentComplexList", "Item clicked: " + id);
    }

    // These are the Contacts rows that we will retrieve.
    static final String[] CONTACTS_SUMMARY_PROJECTION = new String[] {
        Contacts._ID,
        Contacts.DISPLAY_NAME,
        Contacts.CONTACT_STATUS,
        Contacts.CONTACT_PRESENCE,
        Contacts.PHOTO_ID,
     <   Con>tacts.LOOKUP_KEY,
    };
    public LoaderCursor onCreateLoader(int id, Bundle args) {
        // This is called when a new Loader needs to be created.  This
        // sample only has one Loader, so we don't care about the ID.
        // First, pick the base URI to use depending on whether we are
        // currently filtering.
        Uri baseUri;
        if (curFilter != null) {
            baseUri = Uri.withAppendedPath(Contacts.CONTENT_FILTER_URI,
                    Uri.encode(curFilter));
        } else {
            baseUri = Contacts.CONTENT_URI;
        }

        // Now create and return a CursorLoader that will take care of
        // creating a Cursor for the data being displayed.
        String select = "((" + Contacts.DISPLAY_NAME + " NOTNULL) AND ("
                + Contacts.HAS_PHONE_NUMBER + "=1) AND ("
                + Contacts.DISPLAY_NAME + " != '' ))";
        return new CursorLoader(getActivity(), baseUri,
                CONTACTS_SUMMARY_PROJECTION, select, null,
           <     C>ontacts.DISPLAY_NAME + " COLLATE LOCALIZED ASC");
    }

    public void onLoadFinished(LoaderCursor loader, Cursor data) {
        // Swap the new cursor in.  (The framework will take care of closing the
       < // ol>d cursor once we return.)
        mAdapter.swapCursor(data);
    }

    public void onLoaderReset(LoaderCursor loader) {
        // This is called when the last Cursor provided to onLoadFinished()
        // above is about to be closed.  We need to make sure we are no
        // longer using it.
        mAdapter.swapCursor(null);
    }
}
```

### More examples

The following examples illustrate how to use loaders:

- [LoaderCursor](https://android.googlesource.com/platform/development/+/master/samples/ApiDemos/src/com/example/android/apis/app/LoaderCursor.java): a complete version of the preceding snippet.
- [Retrieve a list of contacts](https://developer.android.com/training/contacts-provider/retrieve-names): a walkthrough that uses a `https://developer.android.com/reference/androidx/loader/content/CursorLoader` to retrieve data from the contacts provider.
- [LoaderThrottle](https://android.googlesource.com/platform/development/+/master/samples/ApiDemos/src/com/example/android/apis/app/LoaderThrottle.java): an example of how to use throttling to reduce the number of queries a content provider performs when its data changes.