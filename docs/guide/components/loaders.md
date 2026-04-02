---
title: Loaders  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/components/loaders
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Loaders Stay organized with collections Save and categorize content based on your preferences.



Loaders are deprecated as of Android 9 (API level 28). The recommended option for
dealing with loading data while handling the `Activity` and `Fragment` lifecycles is to use a
combination of [`ViewModel`](/reference/androidx/lifecycle/ViewModel) objects
and [`LiveData`](/reference/androidx/lifecycle/LiveData).
View models survive configuration changes, like loaders, but with
less boilerplate code. `LiveData` provides a lifecycle-aware way of loading data that you can reuse in
multiple view models. You can also combine `LiveData` using
[`MediatorLiveData`](/reference/androidx/lifecycle/MediatorLiveData).
Any observable queries, such as those from a
[Room database](/topic/libraries/architecture/room), can be used to observe changes
to the data.  
  
`ViewModel` and `LiveData` are also available in situations where you don't have access
to the [`LoaderManager`](/reference/android/app/LoaderManager), such as in a
[`Service`](/reference/android/app/Service). Using the two in
tandem provides an easy way to access the data your app needs without having to deal with the UI
lifecycle. To learn more about `LiveData`, see the
[`LiveData` overview](/topic/libraries/architecture/livedata). To learn more about
`ViewModel`, see the [`ViewModel` overview](/topic/libraries/architecture/viewmodel).

The Loader API lets you load data from a
[content provider](/guide/topics/providers/content-providers)
or other data source for display in a `FragmentActivity`
or `Fragment`.

Without loaders, some of the problems you might encounter include the following:

* If you fetch the data directly in the activity or fragment, your users
  suffer from lack of responsiveness due to performing potentially slow
  queries from the UI thread.
* If you fetch the data from another thread, perhaps with `AsyncTask`,
  then you're responsible for managing both that thread
  and the UI thread through various activity or fragment lifecycle events, such as
  `onDestroy()` and configuration changes.

Loaders solve these problems and include other benefits:

* Loaders run on separate threads to prevent a slow or unresponsive UI.
* Loaders simplify thread management by providing callback methods when events
  occur.
* Loaders persist and cache results across configuration changes to prevent
  duplicate queries.
* Loaders can implement an observer to monitor for changes in the underlying
  data source. For example, `CursorLoader` automatically
  registers a `ContentObserver` to trigger a reload
  when data changes.

## Loader API summary

There are multiple classes and interfaces that might be involved when using
loaders in an app. They are summarized in the following table:

| Class/Interface | Description |
| --- | --- |
| `LoaderManager` | An abstract class associated with a `FragmentActivity` or `Fragment` for managing one or more `Loader` instances. There is only one `LoaderManager` per activity or fragment, but a `LoaderManager` can manage multiple loaders. To get a `LoaderManager`, call `getSupportLoaderManager()` from the activity or fragment. To start loading data from a loader, call either `initLoader()` or `restartLoader()`. The system automatically determines whether a loader with the same integer ID already exists and either creates a new loader or reuses an existing loader. |
| `LoaderManager.LoaderCallbacks` | This interface contains callback methods that are called when loader events occur. The interface defines three callback methods:  * `onCreateLoader(int, Bundle)`:   called when the system needs a new loader to be created. In your code,   create a `Loader` object and return it to   the system. * `onLoadFinished(Loader<D>, D)`:   called when a loader has finished loading data. You typically   display the data to the user in your code. * `onLoaderReset(Loader<D>)`:   called when a previously created loader is being reset, when you call   `destroyLoader(int)` or when the activity   or fragment is destroyed, making its data unavailable. In your code,   remove any references to the loader's data.  Your activity or fragment typically implements this interface, and it is registered when you call `initLoader()` or `restartLoader()`. |
| `Loader` | Loaders perform the loading of data. This class is abstract and serves as the base class for all loaders. You can directly subclass `Loader` or use one of the following built-in subclasses to simplify implementation:  * `AsyncTaskLoader`: an abstract loader that   provides an `AsyncTask` to perform load operations on a separate   thread. * `CursorLoader`: a concrete subclass of   `AsyncTaskLoader` for asynchronously loading data   from a `ContentProvider`. It queries a   `ContentResolver` and returns a   `Cursor`. |

The following sections show you how to use these
classes and interfaces in an application.

## Use loaders in an application

This section describes how to use loaders in an Android application. An
application that uses loaders typically includes the following:

* A `FragmentActivity` or `Fragment`.
* An instance of the `LoaderManager`.
* A `CursorLoader` to load data backed by a `ContentProvider`. Alternatively, you can implement your own subclass
  of `Loader` or `AsyncTaskLoader` to
  load data from some other source.
* An implementation for `LoaderManager.LoaderCallbacks`.
  This is where you create new loaders and manage your references to existing
  loaders.
* A way of displaying the loader's data, such as a `SimpleCursorAdapter`.
* A data source, such as a `ContentProvider`, when using a
  `CursorLoader`.

### Start a loader

The `LoaderManager` manages one or more `Loader` instances within a `FragmentActivity` or
`Fragment`. There is only one `LoaderManager` per activity or fragment.

You typically
initialize a `Loader` within the activity's `onCreate()` method or the fragment's
`onCreate()` method. You
do this as follows:

### Kotlin

```
supportLoaderManager.initLoader(0, null, this)
```

### Java

```
// Prepare the loader.  Either re-connect with an existing one,
// or start a new one.
getSupportLoaderManager().initLoader(0, null, this);
```

The `initLoader()` method takes
the following parameters:

* A unique ID that identifies the loader. In this example, the ID is `0`.
* Optional arguments to supply to the loader at
  construction (`null` in this example).
* A `LoaderManager.LoaderCallbacks` implementation, which
  the `LoaderManager` calls to report loader events. In this
  example, the local class implements the `LoaderManager.LoaderCallbacks` interface, so it passes a reference
  to itself, `this`.

The `initLoader()` call ensures that a loader
is initialized and active. It has two possible outcomes:

* If the loader specified by the ID already exists, the last created loader
  is reused.
* If the loader specified by the ID does *not* exist,
  `initLoader()` triggers the
  `LoaderManager.LoaderCallbacks` method `onCreateLoader()`.
  This is where you implement the code to instantiate and return a new loader.
  For more discussion, see the section about [`onCreateLoader`](#onCreateLoader).

In either case, the given `LoaderManager.LoaderCallbacks`
implementation is associated with the loader and is called when the
loader state changes. If, at the point of this call, the caller is in its
started state and the requested loader already exists and has generated its
data, then the system calls `onLoadFinished()`
immediately, during `initLoader()`. You must be prepared for this to happen. For more discussion of this callback, see the section about [`onLoadFinished`](#onLoadFinished).

The `initLoader()` method returns the `Loader` that is created,
but you don't need to capture a reference to it. The `LoaderManager` manages
the life of the loader automatically. The `LoaderManager`
starts and stops loading when necessary and maintains the state of the loader
and its associated content.

As this implies, you rarely interact with loaders
directly.
You most commonly use the `LoaderManager.LoaderCallbacks` methods to intervene in the loading
process when particular events occur. For more discussion of this topic, see the [Using the LoaderManager callbacks](#callback) section.

### Restart a loader

When you use `initLoader()`, as
shown in the preceding section, it uses an existing loader with the specified ID if there is one.
If there isn't, it creates one. But sometimes you want to discard your old data
and start over.

To discard your old data, use `restartLoader()`. For example, the following
implementation of `SearchView.OnQueryTextListener` restarts
the loader when the user's query changes. The loader needs to be restarted so
that it can use the revised search filter to do a new query.

### Kotlin

```
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

```
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

`LoaderManager.LoaderCallbacks` is a callback interface
that lets a client interact with the `LoaderManager`.

Loaders, in particular `CursorLoader`, are expected to
retain their data after being stopped. This lets applications keep their
data across the activity or fragment's `onStop()` and `onStart()` methods, so that
when users return to an application, they don't have to wait for the data to
reload.

You use the `LoaderManager.LoaderCallbacks` methods to know when to create a new loader and to tell the application when it is
time to stop using a loader's data.

`LoaderManager.LoaderCallbacks` includes these
methods:

* `onCreateLoader()`:
  instantiates and returns a new `Loader` for the given ID.

* `onLoadFinished()`:
  called when a previously created loader has finished its load.

* `onLoaderReset()`:
  called when a previously created loader is being reset, thus making its
  data unavailable.

These methods are described in more detail in the following sections.

#### onCreateLoader

When you attempt to access a loader, such as through `initLoader()`, it checks to see whether
the loader specified by the ID exists. If it doesn't, it triggers the `LoaderManager.LoaderCallbacks` method `onCreateLoader()`. This
is where you create a new loader. Typically this is a `CursorLoader`, but you can implement your own `Loader` subclass.

In the following example, the `onCreateLoader()`
callback method creates a `CursorLoader` using its constructor method, which
requires the complete set of information needed to perform a query to the `ContentProvider`. Specifically, it needs the following:

* *uri*: the URI for the content to retrieve.
* *projection*: a list of which columns to return. Passing
  `null` returns all columns, which is inefficient.
* *selection*: a filter declaring which rows to return,
  formatted as a SQL WHERE clause (excluding the WHERE itself). Passing
  `null` returns all rows for the given URI.
* *selectionArgs*: if you include ?s in the selection, they
  are replaced by the values from *selectionArgs* in the order that they appear in
  the selection. The values are bound as strings.
* *sortOrder*: how to order the rows, formatted as a SQL
  ORDER BY clause (excluding the ORDER BY itself). Passing `null`
  uses the default sort order, which might be unordered.

### Kotlin

```
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
    return (activity as? Context)?.let { context ->
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

```
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
yourself—the loader owns it and takes care of that.

The loader releases the data once it knows the application is no longer
using it. For example, if the data is a cursor from a `CursorLoader`,
don’t call `close()` on it yourself. If the cursor is being
placed in a `CursorAdapter`, use the `swapCursor()` method so that the
old `Cursor` is not closed, as shown in the following example:

### Kotlin

```
private lateinit var adapter: SimpleCursorAdapter
...
override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor?) {
    // Swap the new cursor in. (The framework will take care of closing the
    // old cursor once we return.)
    adapter.swapCursor(data)
}
```

### Java

```
// This is the Adapter being used to display the list's data.
SimpleCursorAdapter adapter;
...
public void onLoadFinished(Loader<Cursor> loader, Cursor data) {
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
`swapCursor()`
with a value of `null`:

### Kotlin

```
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

```
// This is the Adapter being used to display the list's data.
SimpleCursorAdapter adapter;
...
public void onLoaderReset(Loader<Cursor> loader) {
    // This is called when the last Cursor provided to onLoadFinished()
    // above is about to be closed.  We need to make sure we are no
    // longer using it.
    adapter.swapCursor(null);
}
```

## Example

As an example, here is the full implementation of a `Fragment` that displays a `ListView` containing
the results of a query against the contacts content provider. It uses a `CursorLoader` to manage the query on the provider.

Because this example is from an application to access a user's contacts, its
manifest must include the permission
`READ_CONTACTS`.

### Kotlin

```
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

    override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
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
                "${Contacts.DISPLAY_NAME} != ''))"
        return (activity as? Context)?.let { context ->
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

    override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor) {
        // Swap the new cursor in.  (The framework will take care of closing the
        // old cursor once we return.)
        mAdapter.swapCursor(data)
    }

    override fun onLoaderReset(loader: Loader<Cursor>) {
        // This is called when the last Cursor provided to onLoadFinished()
        // above is about to be closed.  We need to make sure we are no
        // longer using it.
        mAdapter.swapCursor(null)
    }
}
```

### Java

```
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
        Contacts.LOOKUP_KEY,
    };
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

    public void onLoadFinished(Loader<Cursor> loader, Cursor data) {
        // Swap the new cursor in.  (The framework will take care of closing the
        // old cursor once we return.)
        mAdapter.swapCursor(data);
    }

    public void onLoaderReset(Loader<Cursor> loader) {
        // This is called when the last Cursor provided to onLoadFinished()
        // above is about to be closed.  We need to make sure we are no
        // longer using it.
        mAdapter.swapCursor(null);
    }
}
```

### More examples

The following examples illustrate how to use loaders:

* [LoaderCursor](https://android.googlesource.com/platform/development/+/master/samples/ApiDemos/src/com/example/android/apis/app/LoaderCursor.java): a complete version of the preceding snippet.
* [Retrieve a list of contacts](/training/contacts-provider/retrieve-names):
  a walkthrough that uses a `CursorLoader` to retrieve
  data from the contacts provider.
* [LoaderThrottle](https://android.googlesource.com/platform/development/+/master/samples/ApiDemos/src/com/example/android/apis/app/LoaderThrottle.java): an example of how to use throttling to reduce the number
  of queries a content provider performs when its data changes.