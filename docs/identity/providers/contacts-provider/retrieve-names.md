---
title: https://developer.android.com/identity/providers/contacts-provider/retrieve-names
url: https://developer.android.com/identity/providers/contacts-provider/retrieve-names
source: md.txt
---

# Retrieve a list of contacts

This lesson shows you how to retrieve a list of contacts whose data matches all or part of a search string, using the following techniques:

Match contact names
:   Retrieve a list of contacts by matching the search string to all or part of the contact name data. The Contacts Provider allows multiple instances of the same name, so this technique can return a list of matches.

Match a specific type of data, such as a phone number
:   Retrieve a list of contacts by matching the search string to a particular type of detail data such as an email address. For example, this technique allows you to list all of the contacts whose email address matches the search string.

Match any type of data
:   Retrieve a list of contacts by matching the search string to any type of detail data, including name, phone number, street address, email address, and so forth. For example, this technique allows you to accept any type of data for a search string and then list the contacts for which the data matches the string.

**Note:** All the examples in this lesson use a[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader)to retrieve data from the Contacts Provider. A[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader)runs its query on a thread that's separate from the UI thread. This ensures that the query doesn't slow down UI response times and cause a poor user experience. For more information, see the Android training class[Loading Data in the Background](https://developer.android.com/training/load-data-background).

## Request permission to read the provider

To do any type of search of the Contacts Provider, your app must have[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)permission. To request this, add this[<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element)element to your manifest file as a child element of[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element):  

```xml
    <uses-permission android:name="android.permission.READ_CONTACTS" />
```

## Match a contact by name and list the results

This technique tries to match a search string to the name of a contact or contacts in the Contact Provider's[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts)table. You usually want to display the results in a[ListView](https://developer.android.com/reference/android/widget/ListView), to allow the user to choose among the matched contacts.

### Define ListView and item layouts

To display the search results in a[ListView](https://developer.android.com/reference/android/widget/ListView), you need a main layout file that defines the entire UI including the[ListView](https://developer.android.com/reference/android/widget/ListView), and an item layout file that defines one line of the[ListView](https://developer.android.com/reference/android/widget/ListView). For example, you could create the main layout file`res/layout/contacts_list_view.xml`with the following XML:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<ListView xmlns:android="http://schemas.android.com/apk/res/android"
          android:id="@android:id/list"
          android:layout_width="match_parent"
          android:layout_height="match_parent"/>
```

This XML uses the built-in Android[ListView](https://developer.android.com/reference/android/widget/ListView)widget[android:id/list](https://developer.android.com/reference/android/R.id#list).

Define the item layout file`contacts_list_item.xml`with the following XML:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android"
          android:id="@android:id/text1"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:clickable="true"/>
```

This XML uses the built-in Android[TextView](https://developer.android.com/reference/android/widget/TextView)widget[android:text1](https://developer.android.com/reference/android/R.id#text1).

**Note:**This lesson doesn't describe the UI for getting a search string from the user, because you may want to get the string indirectly. For example, you can give the user an option to search for contacts whose name matches a string in an incoming text message.

The two layout files you've written define a user interface that shows a[ListView](https://developer.android.com/reference/android/widget/ListView). The next step is to write code that uses this UI to display a list of contacts.

### Define a Fragment that displays the list of contacts

To display the list of contacts, start by defining a[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)that's loaded by an[Activity](https://developer.android.com/reference/android/app/Activity). Using a[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)is a more flexible technique, because you can use one[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)to display the list and a second[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)to display the details for a contact that the user chooses from the list. Using this approach, you can combine one of the techniques presented in this lesson with one from the lesson[Retrieve details for a contact](https://developer.android.com/training/contacts-provider/retrieve-details).

To learn how to use one or more[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)objects from an an[Activity](https://developer.android.com/reference/android/app/Activity), read the training class[Build a dynamic UI with Fragments](https://developer.android.com/training/basics/fragments).

To help you write queries against the Contacts Provider, the Android framework provides a contracts class called[ContactsContract](https://developer.android.com/reference/android/provider/ContactsContract), which defines useful constants and methods for accessing the provider. When you use this class, you don't have to define your own constants for content URIs, table names, or columns. To use this class, include the following statement:  

### Kotlin

```kotlin
import android.provider.ContactsContract
```

### Java

```java
import android.provider.ContactsContract;
```

Since the code uses a[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader)to retrieve data from the provider, you must specify that it implements the loader interface[LoaderManager.LoaderCallbacks](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks). Also, to help detect which contact the user selects from the list of search results, implement the adapter interface[AdapterView.OnItemClickListener](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener). For example:  

### Kotlin

```kotlin
...
import android.support.v4.app.Fragment
import android.support.v4.app.LoaderManager
import android.widget.AdapterView
...
class ContactsFragment :
        Fragment(),
        LoaderManager.LoaderCallbacks<Cursor>,
        AdapterView.OnItemClickListener {
```

### Java

```java
...
import android.support.v4.app.Fragment;
import android.support.v4.app.LoaderManager.LoaderCallbacks;
import android.widget.AdapterView;
...
public class ContactsFragment extends Fragment implements
        LoaderManager.LoaderCallbacks<Cursor>,
        AdapterView.OnItemClickListener {
```

### Define global variables

Define global variables that are used in other parts of the code:  

### Kotlin

```kotlin
...
/*
 * Defines an array that contains column names to move from
 * the Cursor to the ListView.
 */
@SuppressLint("InlinedApi")
private val FROM_COLUMNS: Array<String> = arrayOf(
        if ((Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB)) {
            ContactsContract.Contacts.DISPLAY_NAME_PRIMARY
        } else {
            ContactsContract.Contacts.DISPLAY_NAME
        }
)
/*
 * Defines an array that contains resource ids for the layout views
 * that get the Cursor column contents. The id is pre-defined in
 * the Android framework, so it is prefaced with "android.R.id"
 */
private val TO_IDS: IntArray = intArrayOf(android.R.id.text1)
...
class ContactsFragment :
        Fragment(),
        LoaderManager.LoaderCallbacks<Cursor>,
        AdapterView.OnItemClickListener {
    ...
    // Define global mutable variables
    // Define a ListView object
    lateinit var contactsList: ListView
    // Define variables for the contact the user selects
    // The contact's _ID value
    var contactId: Long = 0
    // The contact's LOOKUP_KEY
    var contactKey: String? = null
    // A content URI for the selected contact
    var contactUri: Uri? = null
    // An adapter that binds the result Cursor to the ListView
    private val cursorAdapter: SimpleCursorAdapter? = null
```

### Java

```java
    ...
    /*
     * Defines an array that contains column names to move from
     * the Cursor to the ListView.
     */
    @SuppressLint("InlinedApi")
    private final static String[] FROM_COLUMNS = {
            Build.VERSION.SDK_INT
                    >= Build.VERSION_CODES.HONEYCOMB ?
                    ContactsContract.Contacts.DISPLAY_NAME_PRIMARY :
                    ContactsContract.Contacts.DISPLAY_NAME
    };
    /*
     * Defines an array that contains resource ids for the layout views
     * that get the Cursor column contents. The id is pre-defined in
     * the Android framework, so it is prefaced with "android.R.id"
     */
    private final static int[] TO_IDS = {
           android.R.id.text1
    };
    // Define global mutable variables
    // Define a ListView object
    ListView contactsList;
    // Define variables for the contact the user selects
    // The contact's _ID value
    long contactId;
    // The contact's LOOKUP_KEY
    String contactKey;
    // A content URI for the selected contact
    Uri contactUri;
    // An adapter that binds the result Cursor to the ListView
    private SimpleCursorAdapter cursorAdapter;
    ...
```

**Note:** Since[Contacts.DISPLAY_NAME_PRIMARY](https://developer.android.com/reference/android/provider/ContactsContract.ContactNameColumns#DISPLAY_NAME_PRIMARY)requires Android 3.0 (API version 11) or later, setting your app's`minSdkVersion`to 10 or below generates an Android Lint warning in Android Studio. To turn off this warning, add the annotation`@SuppressLint("InlinedApi")`before the definition of`FROM_COLUMNS`.

### Initialize the Fragment

Initialize the[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment). Add the empty, public constructor required by the Android system, and inflate the[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)object's UI in the callback method[onCreateView()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater, android.view.ViewGroup, android.os.Bundle)). For example:  

### Kotlin

```kotlin
    // A UI Fragment must inflate its View
    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        // Inflate the fragment layout
        return inflater.inflate(R.layout.contact_list_fragment, container, false)
    }
```

### Java

```java
    // Empty public constructor, required by the system
    public ContactsFragment() {}

    // A UI Fragment must inflate its View
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        // Inflate the fragment layout
        return inflater.inflate(R.layout.contact_list_fragment,
            container, false);
    }
```

### Set up the CursorAdapter for the ListView

Set up the[SimpleCursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/SimpleCursorAdapter)that binds the results of the search to the[ListView](https://developer.android.com/reference/android/widget/ListView). To get the[ListView](https://developer.android.com/reference/android/widget/ListView)object that displays the contacts, you need to call[Activity.findViewById()](https://developer.android.com/reference/android/app/Activity#findViewById(int))using the parent activity of the[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment). Use the[Context](https://developer.android.com/reference/android/content/Context)of the parent activity when you call[setAdapter()](https://developer.android.com/reference/android/widget/AdapterView#setAdapter(T)). For example:  

### Kotlin

```kotlin
    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        ...
        // Gets the ListView from the View list of the parent activity
        activity?.also {
            contactsList = it.findViewById<ListView>(R.id.contact_list_view)
            // Gets a CursorAdapter
            cursorAdapter = SimpleCursorAdapter(
                    it,
                    R.layout.contact_list_item,
                    null,
                    FROM_COLUMNS, TO_IDS,
                    0
            )
            // Sets the adapter for the ListView
            contactsList.adapter = cursorAdapter
        }
    }
```

### Java

```java
    public void onActivityCreated(Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        ...
        // Gets the ListView from the View list of the parent activity
        contactsList =
            (ListView) getActivity().findViewById(R.layout.contact_list_view);
        // Gets a CursorAdapter
        cursorAdapter = new SimpleCursorAdapter(
                getActivity(),
                R.layout.contact_list_item,
                null,
                FROM_COLUMNS, TO_IDS,
                0);
        // Sets the adapter for the ListView
        contactsList.setAdapter(cursorAdapter);
    }
```

### Set the selected contact listener

When you display the results of a search, you usually want to allow the user to select a single contact for further processing. For example, when the user clicks a contact you can display the contact's address on a map. To provide this feature, you first defined the current[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)as the click listener by specifying that the class implements[AdapterView.OnItemClickListener](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener), as shown in the section[Define a Fragment that displays the list of contacts](https://developer.android.com/identity/providers/contacts-provider/retrieve-names#Fragment).

To continue setting up the listener, bind it to the[ListView](https://developer.android.com/reference/android/widget/ListView)by calling the method[setOnItemClickListener()](https://developer.android.com/reference/android/widget/AdapterView#setOnItemClickListener(android.widget.AdapterView.OnItemClickListener))in[onActivityCreated()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onActivityCreated(android.os.Bundle)). For example:  

### Kotlin

```kotlin
    fun onActivityCreated(savedInstanceState:Bundle) {
        ...
        // Set the item click listener to be the current fragment.
        contactsList.onItemClickListener = this
        ...
    }
```

### Java

```java
    public void onActivityCreated(Bundle savedInstanceState) {
        ...
        // Set the item click listener to be the current fragment.
        contactsList.setOnItemClickListener(this);
        ...
    }
```

Since you specified that the current[Fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)is the[OnItemClickListener](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener)for the[ListView](https://developer.android.com/reference/android/widget/ListView), you now need to implement its required method[onItemClick()](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener#onItemClick(android.widget.AdapterView<?>, android.view.View, int, long)), which handles the click event. This is described in a succeeding section.

### Define a projection

Define a constant that contains the columns you want to return from your query. Each item in the[ListView](https://developer.android.com/reference/android/widget/ListView)displays the contact's display name, which contains the main form of the contact's name. In Android 3.0 (API version 11) and later, the name of this column is[Contacts.DISPLAY_NAME_PRIMARY](https://developer.android.com/reference/android/provider/ContactsContract.ContactNameColumns#DISPLAY_NAME_PRIMARY); in versions previous to that, its name is[Contacts.DISPLAY_NAME](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#DISPLAY_NAME).

The column[Contacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)is used by the[SimpleCursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/SimpleCursorAdapter)binding process.[Contacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)and[LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY)are used together to construct a content URI for the contact the user selects.  

### Kotlin

```kotlin
...
@SuppressLint("InlinedApi")
private val PROJECTION: Array<out String> = arrayOf(
        ContactsContract.Contacts._ID,
        ContactsContract.Contacts.LOOKUP_KEY,
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB)
            ContactsContract.Contacts.DISPLAY_NAME_PRIMARY
        else
            ContactsContract.Contacts.DISPLAY_NAME
)
```

### Java

```java
...
@SuppressLint("InlinedApi")
private static final String[] PROJECTION =
        {
            Contacts._ID,
            Contacts.LOOKUP_KEY,
            Build.VERSION.SDK_INT
                    >= Build.VERSION_CODES.HONEYCOMB ?
                    ContactsContract.Contacts.DISPLAY_NAME_PRIMARY :
                    ContactsContract.Contacts.DISPLAY_NAME

        };
```

### Define constants for the Cursor column indexes

To get data from an individual column in a[Cursor](https://developer.android.com/reference/android/database/Cursor), you need the column's index within the[Cursor](https://developer.android.com/reference/android/database/Cursor). You can define constants for the indexes of the[Cursor](https://developer.android.com/reference/android/database/Cursor)columns, because the indexes are the same as the order of the column names in your projection. For example:  

### Kotlin

```kotlin
// The column index for the _ID column
private const val CONTACT_ID_INDEX: Int = 0
// The column index for the CONTACT_KEY column
private const val CONTACT_KEY_INDEX: Int = 1
```

### Java

```java
// The column index for the _ID column
private static final int CONTACT_ID_INDEX = 0;
// The column index for the CONTACT_KEY column
private static final int CONTACT_KEY_INDEX = 1;
```

### Specify the selection criteria

To specify the data you want, create a combination of text expressions and variables that tell the provider the data columns to search and the values to find.

For the text expression, define a constant that lists the search columns. Although this expression can contain values as well, the preferred practice is to represent the values with a "?" placeholder. During retrieval, the placeholder is replaced with values from an array. Using "?" as a placeholder ensures that the search specification is generated by binding rather than by SQL compilation. This practice eliminates the possibility of malicious SQL injection. For example:  

### Kotlin

```kotlin
// Defines the text expression
@SuppressLint("InlinedApi")
private val SELECTION: String =
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB)
            "${ContactsContract.Contacts.DISPLAY_NAME_PRIMARY} LIKE ?"
        else
            "${ContactsContract.Contacts.DISPLAY_NAME} LIKE ?"
...
    // Defines a variable for the search string
    private val searchString: String = ...
    // Defines the array to hold values that replace the ?
    private val selectionArgs = arrayOf<String>(searchString)
```

### Java

```java
    // Defines the text expression
    @SuppressLint("InlinedApi")
    private static final String SELECTION =
            Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB ?
            Contacts.DISPLAY_NAME_PRIMARY + " LIKE ?" :
            Contacts.DISPLAY_NAME + " LIKE ?";
    // Defines a variable for the search string
    private String searchString;
    // Defines the array to hold values that replace the ?
    private String[] selectionArgs = { searchString };
```

### Define the onItemClick() method

In a previous section, you set the item click listener for the[ListView](https://developer.android.com/reference/android/widget/ListView). Now implement the action for the listener by defining the method[AdapterView.OnItemClickListener.onItemClick()](https://developer.android.com/reference/android/widget/AdapterView.OnItemClickListener#onItemClick(android.widget.AdapterView<?>, android.view.View, int, long)):  

### Kotlin

```kotlin
    override fun onItemClick(parent: AdapterView<*>, view: View?, position: Int, id: Long) {
        // Get the Cursor
        val cursor: Cursor? = (parent.adapter as? CursorAdapter)?.cursor?.apply {
            // Move to the selected contact
            moveToPosition(position)
            // Get the _ID value
            contactId = getLong(CONTACT_ID_INDEX)
            // Get the selected LOOKUP KEY
            contactKey = getString(CONTACT_KEY_INDEX)
            // Create the contact's content Uri
            contactUri = ContactsContract.Contacts.getLookupUri(contactId, mContactKey)
            /*
             * You can use contactUri as the content URI for retrieving
             * the details for a contact.
             */
        }
    }
```

### Java

```java
    @Override
    public void onItemClick(
        AdapterView<?> parent, View item, int position, long rowID) {
        // Get the Cursor
        Cursor cursor = parent.getAdapter().getCursor();
        // Move to the selected contact
        cursor.moveToPosition(position);
        // Get the _ID value
        contactId = cursor.getLong(CONTACT_ID_INDEX);
        // Get the selected LOOKUP KEY
        contactKey = cursor.getString(CONTACT_KEY_INDEX);
        // Create the contact's content Uri
        contactUri = Contacts.getLookupUri(contactId, mContactKey);
        /*
         * You can use contactUri as the content URI for retrieving
         * the details for a contact.
         */
    }
```

### Initialize the loader

Since you're using a[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader)to retrieve data, you must initialize the background thread and other variables that control asynchronous retrieval. Do the initialization in[onCreate()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate(android.os.Bundle))as shown in the following example:  

### Kotlin

```kotlin
class ContactsFragment :
        Fragment(),
        LoaderManager.LoaderCallbacks<Cursor> {
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        // Always call the super method first
        super.onCreate(savedInstanceState)
        ...
        // Initializes the loader
        loaderManager.initLoader(0, null, this)
```

### Java

```java
public class ContactsFragment extends Fragment implements
        LoaderManager.LoaderCallbacks<Cursor> {
    ...
    // Called just before the Fragment displays its UI
    @Override
    public void onCreate(Bundle savedInstanceState) {
        // Always call the super method first
        super.onCreate(savedInstanceState);
        ...
        // Initializes the loader
        getLoaderManager().initLoader(0, null, this);
```

### Implement onCreateLoader()

Implement the method[onCreateLoader()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)), which is called by the loader framework immediately after you call[initLoader()](https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int, android.os.Bundle, android.support.v4.app.LoaderManager.LoaderCallbacks<D>)).

In[onCreateLoader()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)), set up the search string pattern. To make a string into a pattern, insert "%" (percent) characters to represent a sequence of zero or more characters, or "_" (underscore) characters to represent a single character, or both. For example, the pattern "%Jefferson%" would match both "Thomas Jefferson" and "Jefferson Davis".

Return a new[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader)from the method. For the content URI, use[Contacts.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_URI). This URI refers to the entire table, as shown in the following example:  

### Kotlin

```kotlin
    ...
    override fun onCreateLoader(loaderId: Int, args: Bundle?): Loader<Cursor> {
        /*
         * Makes search string into pattern and
         * stores it in the selection array
         */
        selectionArgs[0] = "%$mSearchString%"
        // Starts the query
        return activity?.let {
            return CursorLoader(
                    it,
                    ContactsContract.Contacts.CONTENT_URI,
                    PROJECTION,
                    SELECTION,
                    selectionArgs,
                    null
            )
        } ?: throw IllegalStateException()
    }
```

### Java

```java
    ...
    @Override
    public Loader<Cursor> onCreateLoader(int loaderId, Bundle args) {
        /*
         * Makes search string into pattern and
         * stores it in the selection array
         */
        selectionArgs[0] = "%" + searchString + "%";
        // Starts the query
        return new CursorLoader(
                getActivity(),
                ContactsContract.Contacts.CONTENT_URI,
                PROJECTION,
                SELECTION,
                selectionArgs,
                null
        );
    }
```

### Implement onLoadFinished() and onLoaderReset()

Implement the[onLoadFinished()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(android.support.v4.content.Loader<D>, D))method. The loader framework calls[onLoadFinished()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(android.support.v4.content.Loader<D>, D))when the Contacts Provider returns the results of the query. In this method, put the result[Cursor](https://developer.android.com/reference/android/database/Cursor)in the[SimpleCursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/SimpleCursorAdapter). This automatically updates the[ListView](https://developer.android.com/reference/android/widget/ListView)with the search results:  

### Kotlin

```kotlin
    override fun onLoadFinished(loader: Loader<Cursor>, cursor: Cursor) {
        // Put the result Cursor in the adapter for the ListView
        cursorAdapter?.swapCursor(cursor)
    }
```

### Java

```java
    @Override
    public void onLoadFinished(Loader<Cursor> loader, Cursor cursor) {
        // Put the result Cursor in the adapter for the ListView
        cursorAdapter.swapCursor(cursor);
    }
```

The method[onLoaderReset()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoaderReset(android.support.v4.content.Loader<D>))is invoked when the loader framework detects that the result[Cursor](https://developer.android.com/reference/android/database/Cursor)contains stale data. Delete the[SimpleCursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/SimpleCursorAdapter)reference to the existing[Cursor](https://developer.android.com/reference/android/database/Cursor). If you don't, the loader framework will not recycle the[Cursor](https://developer.android.com/reference/android/database/Cursor), which causes a memory leak. For example:  

### Kotlin

```kotlin
    override fun onLoaderReset(loader: Loader<Cursor>) {
        // Delete the reference to the existing Cursor
        cursorAdapter?.swapCursor(null)
    }
```

### Java

```java
    @Override
    public void onLoaderReset(Loader<Cursor> loader) {
        // Delete the reference to the existing Cursor
        cursorAdapter.swapCursor(null);

    }
```

You now have the key pieces of an app that matches a search string to contact names and returns the result in a[ListView](https://developer.android.com/reference/android/widget/ListView). The user can click a contact name to select it. This triggers a listener, in which you can work further with the contact's data. For example, you can retrieve the contact's details. To learn how to do this, continue with the next lesson,[Retrieve details for a contact](https://developer.android.com/training/contacts-provider/retrieve-details).

To learn more about search user interfaces, read the API guide[Create a search interface](https://developer.android.com/guide/topics/search/search-dialog).

The remaining sections in this lesson demonstrate other ways of finding contacts in the Contacts Provider.

## Match a contact by a specific type of data

This technique allows you to specify the type of data you want to match. Retrieving by name is a specific example of this type of query, but you can also do it for any of the types of detail data associated with a contact. For example, you can retrieve contacts that have a specific postal code; in this case, the search string has to match data stored in a postal code row.

To implement this type of retrieval, first implement the following code, as listed in previous sections:

- Request Permission to Read the Provider.
- Define ListView and item layouts.
- Define a Fragment that displays the list of contacts.
- Define global variables.
- Initialize the Fragment.
- Set up the CursorAdapter for the ListView.
- Set the selected contact listener.
- Define constants for the Cursor column indexes.Although you're retrieving data from a different table, the order of the columns in the projection is the same, so you can use the same indexes for the Cursor.

- Define the onItemClick() method.
- Initialize the loader.
- Implement onLoadFinished() and onLoaderReset().

The following steps show you the additional code you need to match a search string to a particular type of detail data and display the results.

### Choose the data type and table

To search for a particular type of detail data, you have to know the custom MIME type value for the data type. Each data type has a unique MIME type value defined by a constant`CONTENT_ITEM_TYPE`in the subclass of[ContactsContract.CommonDataKinds](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds)associated with the data type. The subclasses have names that indicate their data type; for example, the subclass for email data is[ContactsContract.CommonDataKinds.Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email), and the custom MIME type for email data is defined by the constant[Email.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_ITEM_TYPE).

Use the[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data)table for your search. All of the constants you need for your projection, selection clause, and sort order are defined in or inherited by this table.

### Define a projection

To define a projection, choose one or more of the columns defined in[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data)or the classes from which it inherits. The Contacts Provider does an implicit join between[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data)and other tables before it returns rows. For example:  

### Kotlin

```kotlin
@SuppressLint("InlinedApi")
private val PROJECTION: Array<out String> = arrayOf(
        /*
         * The detail data row ID. To make a ListView work,
         * this column is required.
         */
        ContactsContract.Data._ID,
        // The primary display name
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB)
            ContactsContract.Data.DISPLAY_NAME_PRIMARY
        else
            ContactsContract.Data.DISPLAY_NAME,
        // The contact's _ID, to construct a content URI
        ContactsContract.Data.CONTACT_ID,
        // The contact's LOOKUP_KEY, to construct a content URI
        ContactsContract.Data.LOOKUP_KEY
)
```

### Java

```java
    @SuppressLint("InlinedApi")
    private static final String[] PROJECTION =
        {
            /*
             * The detail data row ID. To make a ListView work,
             * this column is required.
             */
            ContactsContract.Data._ID,
            // The primary display name
            Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB ?
                    ContactsContract.Data.DISPLAY_NAME_PRIMARY :
                    ContactsContract.Data.DISPLAY_NAME,
            // The contact's _ID, to construct a content URI
            ContactsContract.Data.CONTACT_ID,
            // The contact's LOOKUP_KEY, to construct a content URI
            ContactsContract.Data.LOOKUP_KEY // A permanent link to the contact
        };
```

### Define search criteria

To search for a string within a particular type of data, construct a selection clause from the following:

- The name of the column that contains your search string. This name varies by data type, so you need to find the subclass of[ContactsContract.CommonDataKinds](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds)that corresponds to the data type and then choose the column name from that subclass. For example, to search for email addresses, use the column[Email.ADDRESS](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#ADDRESS).
- The search string itself, represented as the "?" character in the selection clause.
- The name of the column that contains the custom MIME type value. This name is always[Data.MIMETYPE](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE).
- The custom MIME type value for the data type. As described previously, this is the constant`CONTENT_ITEM_TYPE`in the[ContactsContract.CommonDataKinds](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds)subclass. For example, the MIME type value for email data is[Email.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_ITEM_TYPE). Enclose the value in single quotes by concatenating a "`'`" (single quote) character to the start and end of the constant; otherwise, the provider interprets the value as a variable name rather than as a string value. You don't need to use a placeholder for this value, because you're using a constant rather than a user-supplied value.

For example:  

### Kotlin

```kotlin
/*
 * Constructs search criteria from the search string
 * and email MIME type
 */
private val SELECTION: String =
        /*
         * Searches for an email address
         * that matches the search string
         */
        "${Email.ADDRESS} LIKE ? AND " +
        /*
         * Searches for a MIME type that matches
         * the value of the constant
         * Email.CONTENT_ITEM_TYPE. Note the
         * single quotes surrounding Email.CONTENT_ITEM_TYPE.
         */
        "${ContactsContract.Data.MIMETYPE } = '${Email.CONTENT_ITEM_TYPE}'"
```

### Java

```java
    /*
     * Constructs search criteria from the search string
     * and email MIME type
     */
    private static final String SELECTION =
            /*
             * Searches for an email address
             * that matches the search string
             */
            Email.ADDRESS + " LIKE ? " + "AND " +
            /*
             * Searches for a MIME type that matches
             * the value of the constant
             * Email.CONTENT_ITEM_TYPE. Note the
             * single quotes surrounding Email.CONTENT_ITEM_TYPE.
             */
            ContactsContract.Data.MIMETYPE + " = '" + Email.CONTENT_ITEM_TYPE + "'";
```

Next, define variables to contain the selection argument:  

### Kotlin

```kotlin
    private var searchString: String? = null
    private val selectionArgs: Array<String> = arrayOf("")
```

### Java

```java
    String searchString;
    String[] selectionArgs = { "" };
```

### Implement onCreateLoader()

Now that you've specified the data you want and how to find it, define a query in your implementation of[onCreateLoader()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)). Return a new[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader)from this method, using your projection, selection text expression, and selection array as arguments. For a content URI, use[Data.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.Data#CONTENT_URI). For example:  

### Kotlin

```kotlin
    override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
        // OPTIONAL: Makes search string into pattern
        searchString = "%$mSearchString%"

        searchString?.also {
            // Puts the search string into the selection criteria
            selectionArgs[0] = it
        }
        // Starts the query
        return activity?.let {
            CursorLoader(
                    it,
                    ContactsContract.Data.CONTENT_URI,
                    PROJECTION,
                    SELECTION,
                    selectionArgs,
                    null
            )
        } ?: throw IllegalStateException()
    }
```

### Java

```java
@Override
    public Loader<Cursor> onCreateLoader(int loaderId, Bundle args) {
        // OPTIONAL: Makes search string into pattern
        searchString = "%" + searchString + "%";
        // Puts the search string into the selection criteria
        selectionArgs[0] = searchString;
        // Starts the query
        return new CursorLoader(
                getActivity(),
                Data.CONTENT_URI,
                PROJECTION,
                SELECTION,
                selectionArgs,
                null
        );
    }
```

These code snippets are the basis of a simple reverse lookup based on a specific type of detail data. This is the best technique to use if your app focuses on a particular type of data, such as emails, and you want allow users to get the names associated with a piece of data.

## Match a contact by any type of data

Retrieving a contact based on any type of data returns contacts if any of their data matches a the search string, including name, email address, postal address, phone number, and so forth. This results in a broad set of search results. For example, if the search string is "Doe", then searching for any data type returns the contact "John Doe"; it also returns contacts who live on "Doe Street".

To implement this type of retrieval, first implement the following code, as listed in previous sections:

- Request Permission to Read the Provider.
- Define ListView and item layouts.
- Define a Fragment that displays the list of contacts.
- Define global variables.
- Initialize the Fragment.
- Set up the CursorAdapter for the ListView.
- Set the selected contact listener.
- Define a projection.
- Define constants for the Cursor column indexes.For this type of retrieval, you're using the same table you used in the section[Match a contact by name and list the results](https://developer.android.com/identity/providers/contacts-provider/retrieve-names#NameMatch). Use the same column indexes as well.

- Define the onItemClick() method.
- Initialize the loader.
- Implement onLoadFinished() and onLoaderReset().

The following steps show you the additional code you need to match a search string to any type of data and display the results.

### Remove selection criteria

Don't define the`SELECTION`constants or the`mSelectionArgs`variable. These aren't used in this type of retrieval.

### Implement onCreateLoader()

Implement the[onCreateLoader()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle))method, returning a new[CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader). You don't need to convert the search string into a pattern, because the Contacts Provider does that automatically. Use[Contacts.CONTENT_FILTER_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_FILTER_URI)as the base URI, and append your search string to it by calling[Uri.withAppendedPath()](https://developer.android.com/reference/android/net/Uri#withAppendedPath(android.net.Uri, java.lang.String)). Using this URI automatically triggers searching for any data type, as shown in the following example:  

### Kotlin

```kotlin
    override fun onCreateLoader(loaderId: Int, args: Bundle?): Loader<Cursor> {
        /*
         * Appends the search string to the base URI. Always
         * encode search strings to ensure they're in proper
         * format.
         */
        val contentUri: Uri = Uri.withAppendedPath(
                ContactsContract.Contacts.CONTENT_FILTER_URI,
                Uri.encode(searchString)
        )
        // Starts the query
        return activity?.let {
            CursorLoader(
                    it,
                    contentUri,
                    PROJECTION2,
                    null,
                    null,
                    null
            )
        } ?: throw IllegalStateException()
    }
```

### Java

```java
    @Override
    public Loader<Cursor> onCreateLoader(int loaderId, Bundle args) {
        /*
         * Appends the search string to the base URI. Always
         * encode search strings to ensure they're in proper
         * format.
         */
        Uri contentUri = Uri.withAppendedPath(
                Contacts.CONTENT_FILTER_URI,
                Uri.encode(searchString));
        // Starts the query
        return new CursorLoader(
                getActivity(),
                contentUri,
                PROJECTION,
                null,
                null,
                null
        );
    }
```

These code snippets are the basis of an app that does a broad search of the Contacts Provider. The technique is useful for apps that want to implement functionality similar to the People app's contact list screen.