---
title: https://developer.android.com/identity/providers/contacts-provider/retrieve-details
url: https://developer.android.com/identity/providers/contacts-provider/retrieve-details
source: md.txt
---

This lesson shows how to retrieve detail data for a contact, such as email addresses, phone
numbers, and so forth. It's the details that users are looking for when they retrieve a contact.
You can give them all the details for a contact, or only display details of a particular type,
such as email addresses.


The steps in this lesson assume that you already have a
`https://developer.android.com/reference/android/provider/ContactsContract.Contacts` row for a contact the user has picked.
The [Retrieving contact names](https://developer.android.com/identity/providers/contacts-provider/retrieve-names) lesson shows how to
retrieve a list of contacts.

## Retrieve all details for a contact


To retrieve all the details for a contact, search the
`https://developer.android.com/reference/android/provider/ContactsContract.Data` table for any rows that contain the contact's
`https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY`. This column is available in
the `https://developer.android.com/reference/android/provider/ContactsContract.Data` table, because the Contacts
Provider makes an implicit join between the `https://developer.android.com/reference/android/provider/ContactsContract.Contacts`
table and the `https://developer.android.com/reference/android/provider/ContactsContract.Data` table. The
`https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY` column is described
in more detail in the [Retrieving contact names](https://developer.android.com/identity/providers/contacts-provider/retrieve-names) lesson.


**Note:** Retrieving all the details for a contact reduces the performance of a
device, because it needs to retrieve all of the columns in the
`https://developer.android.com/reference/android/provider/ContactsContract.Data` table. Consider the performance impact before
you use this technique.

### Request permissions


To read from the Contacts Provider, your app must have
`https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS` permission.
To request this permission, add the following child element of
`https://developer.android.com/guide/topics/manifest/manifest-element` to your manifest file:

```xml
    <uses-permission android:name="android.permission.READ_CONTACTS" />
```

### Set up a projection


Depending on the data type a row contains, it may use only a few columns or many. In addition,
the data is in different columns depending on the data type.
To ensure you get all the possible columns for all possible data types, you need to add all the
column names to your projection. Always retrieve
`https://developer.android.com/reference/android/provider/BaseColumns#_ID` if you're binding the result
`https://developer.android.com/reference/android/database/Cursor` to a `https://developer.android.com/reference/android/widget/ListView`; otherwise, the binding
won't work. Also retrieve `https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE`
so you can identify the data type of each row you retrieve. For example:

### Kotlin

```kotlin
private val PROJECTION: Array<out String> = arrayOf(
        ContactsContract.Data._ID,
        ContactsContract.Data.MIMETYPE,
        ContactsContract.Data.DATA1,
        ContactsContract.Data.DATA2,
        ContactsContract.Data.DATA3,
        ContactsContract.Data.DATA4,
        ContactsContract.Data.DATA5,
        ContactsContract.Data.DATA6,
        ContactsContract.Data.DATA7,
        ContactsContract.Data.DATA8,
        ContactsContract.Data.DATA9,
        ContactsContract.Data.DATA10,
        ContactsContract.Data.DATA11,
        ContactsContract.Data.DATA12,
        ContactsContract.Data.DATA13,
        ContactsContract.Data.DATA14,
        ContactsContract.Data.DATA15
)
```

### Java

```java
    private static final String[] PROJECTION =
            {
                ContactsContract.Data._ID,
                ContactsContract.Data.MIMETYPE,
                ContactsContract.Data.DATA1,
                ContactsContract.Data.DATA2,
                ContactsContract.Data.DATA3,
                ContactsContract.Data.DATA4,
                ContactsContract.Data.DATA5,
                ContactsContract.Data.DATA6,
                ContactsContract.Data.DATA7,
                ContactsContract.Data.DATA8,
                ContactsContract.Data.DATA9,
                ContactsContract.Data.DATA10,
                ContactsContract.Data.DATA11,
                ContactsContract.Data.DATA12,
                ContactsContract.Data.DATA13,
                ContactsContract.Data.DATA14,
                ContactsContract.Data.DATA15
            };
```


This projection retrieves all the columns for a row in the
`https://developer.android.com/reference/android/provider/ContactsContract.Data` table, using the column names defined in
the `https://developer.android.com/reference/android/provider/ContactsContract.Data` class.


Optionally, you can also use any other column constants defined in or inherited by the
`https://developer.android.com/reference/android/provider/ContactsContract.Data` class. Notice, however, that the columns
`https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#SYNC1` through
`https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#SYNC4` are meant to be used by sync
adapters, so their data is not useful.

### Define the selection criteria


Define a constant for your selection clause, an array to hold selection arguments, and a
variable to hold the selection value. Use
the `https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY` column to
find the contact. For example:

### Kotlin

```kotlin
// Defines the selection clause
private const val SELECTION: String = "${ContactsContract.Data.LOOKUP_KEY} = ?"
...
// Defines the array to hold the search criteria
private val selectionArgs: Array<String> = arrayOf("")
/*
 * Defines a variable to contain the selection value. Once you
 * have the Cursor from the Contacts table, and you've selected
 * the desired row, move the row's LOOKUP_KEY value into this
 * variable.
 */
private var lookupKey: String? = null
```

### Java

```java
    // Defines the selection clause
    private static final String SELECTION = Data.LOOKUP_KEY + " = ?";
    // Defines the array to hold the search criteria
    private String[] selectionArgs = { "" };
    /*
     * Defines a variable to contain the selection value. Once you
     * have the Cursor from the Contacts table, and you've selected
     * the desired row, move the row's LOOKUP_KEY value into this
     * variable.
     */
    private lateinit var lookupKey: String
```


Using "?" as a placeholder in your selection text expression ensures that the resulting search
is generated by binding rather than SQL compilation. This approach eliminates the
possibility of malicious SQL injection.

### Define the sort order


Define the sort order you want in the resulting `https://developer.android.com/reference/android/database/Cursor`. To
keep all rows for a particular data type together, sort by
`https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE`. This query argument
groups all email rows together, all phone rows together, and so forth. For example:

### Kotlin

```kotlin
/*
 * Defines a string that specifies a sort order of MIME type
 */
private const val SORT_ORDER = ContactsContract.Data.MIMETYPE
```

### Java

```java
    /*
     * Defines a string that specifies a sort order of MIME type
     */
    private static final String SORT_ORDER = ContactsContract.Data.MIMETYPE;
```


**Note:** Some data types don't use a subtype, so you can't sort on subtype.
Instead, you have to iterate through the returned `https://developer.android.com/reference/android/database/Cursor`,
determine the data type of the current row, and store data for rows that use a subtype. When
you finish reading the cursor, you can then sort each data type by subtype and display the
results.

### Initialize the Loader


Always do retrievals from the Contacts Provider (and all other content providers) in a
background thread. Use the Loader framework defined by the
`https://developer.android.com/reference/androidx/loader/app/LoaderManager` class and the
`https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks` interface to do background
retrievals.


When you're ready to retrieve the rows, initialize the loader framework by
calling `https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int, android.os.Bundle, android.support.v4.app.LoaderManager.LoaderCallbacks<D>)`. Pass an
integer identifier to the method; this identifier is passed to
`https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks` methods. The identifier helps you
use multiple loaders in an app by allowing you to differentiate between them.


The following snippet shows how to initialize the loader framework:

### Kotlin

```kotlin
// Defines a constant that identifies the loader
private const val DETAILS_QUERY_ID: Int = 0

class DetailsFragment : Fragment(), LoaderManager.LoaderCallbacks<Cursor> {
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Initializes the loader framework
        loaderManager.initLoader(DETAILS_QUERY_ID, null, this)
```

### Java

```java
public class DetailsFragment extends Fragment implements
        LoaderManager.LoaderCallbacks<Cursor> {
    ...
    // Defines a constant that identifies the loader
    static int DETAILS_QUERY_ID = 0;
    ...
    @Override
    public void onCreate(Bundle savedInstanceState) {
        ...
        // Initializes the loader framework
        getLoaderManager().initLoader(DETAILS_QUERY_ID, null, this);
```

### Implement onCreateLoader()


Implement the `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onCreateLoader(int, android.os.Bundle)` method, which is called by the loader framework immediately after you call
`https://developer.android.com/reference/androidx/loader/app/LoaderManager#initLoader(int, android.os.Bundle, android.support.v4.app.LoaderManager.LoaderCallbacks<D>)`. Return a
`https://developer.android.com/reference/androidx/loader/content/CursorLoader` from this method. Since you're searching
the `https://developer.android.com/reference/android/provider/ContactsContract.Data` table, use the constant
`https://developer.android.com/reference/android/provider/ContactsContract.Data#CONTENT_URI` as the content URI.
For example:

### Kotlin

```kotlin
override fun onCreateLoader(loaderId: Int, args: Bundle?): Loader<Cursor> {
    // Choose the proper action
    mLoader = when(loaderId) {
        DETAILS_QUERY_ID -> {
            // Assigns the selection parameter
            selectionArgs[0] = lookupKey
            // Starts the query
            activity?.let {
                CursorLoader(
                        it,
                        ContactsContract.Data.CONTENT_URI,
                        PROJECTION,
                        SELECTION,
                        selectionArgs,
                        SORT_ORDER
                )
            }
        }
        ...
    }
    return mLoader
}
```

### Java

```java
@Override
    public Loader<Cursor> onCreateLoader(int loaderId, Bundle args) {
        // Choose the proper action
        switch (loaderId) {
            case DETAILS_QUERY_ID:
            // Assigns the selection parameter
            selectionArgs[0] = lookupKey;
            // Starts the query
            CursorLoader mLoader =
                    new CursorLoader(
                            getActivity(),
                            ContactsContract.Data.CONTENT_URI,
                            PROJECTION,
                            SELECTION,
                            selectionArgs,
                            SORT_ORDER
                    );
    }
```

### Implement onLoadFinished() and onLoaderReset()


Implement the
`https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(android.support.v4.content.Loader<D>, D)`
method. The loader framework calls
`https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(android.support.v4.content.Loader<D>, D)`
when the Contacts Provider returns the results of the query. For example:

### Kotlin

```kotlin
    override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor) {
        when(loader.id) {
            DETAILS_QUERY_ID -> {
                /*
                 * Process the resulting Cursor here.
                 */
            }
            ...
        }
    }
```

### Java

```java
    @Override
    public void onLoadFinished(Loader<Cursor> loader, Cursor cursor) {
        switch (loader.getId()) {
            case DETAILS_QUERY_ID:
                    /*
                     * Process the resulting Cursor here.
                     */
                }
                break;
            ...
        }
    }
```


The method `https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoaderReset(android.support.v4.content.Loader<D>)` is invoked when the loader framework detects that the data backing the result
`https://developer.android.com/reference/android/database/Cursor` has changed. At this point, remove any existing references
to the `https://developer.android.com/reference/android/database/Cursor` by setting them to null. If you don't, the loader
framework won't destroy the old `https://developer.android.com/reference/android/database/Cursor`, and you'll get a memory
leak. For example:

### Kotlin

```kotlin
    override fun onLoaderReset(loader: Loader<Cursor>) {
        when (loader.id) {
            DETAILS_QUERY_ID -> {
                /*
                 * If you have current references to the Cursor,
                 * remove them here.
                 */
            }
            ...
        }
    }
```

### Java

```java
    @Override
    public void onLoaderReset(Loader<Cursor> loader) {
        switch (loader.getId()) {
            case DETAILS_QUERY_ID:
                /*
                 * If you have current references to the Cursor,
                 * remove them here.
                 */
                }
                break;
    }
```

## Retrieve specific details for a contact


Retrieving a specific data type for a contact, such as all the emails, follows the same pattern
as retrieving all details. These are the only changes you need to make to the code
listed in [Retrieve all details for a contact](https://developer.android.com/identity/providers/contacts-provider/retrieve-details#RetrieveAll):


Projection
:
    Modify your projection to retrieve the columns that are specific to the
    data type. Also modify the projection to use the column name constants defined in the
    `https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds` subclass corresponding to the
    data type.


Selection
:
    Modify the selection text to search for the
    `https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE` value that's specific to
    your data type.


Sort order
:
    Since you're only selecting a single detail type, don't group the returned
    `https://developer.android.com/reference/android/database/Cursor` by `https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE`.


These modifications are described in the following sections.

### Define a projection


Define the columns you want to retrieve, using the column name constants in the subclass
of `https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds` for the data type.
If you plan to bind your `https://developer.android.com/reference/android/database/Cursor` to a `https://developer.android.com/reference/android/widget/ListView`,
be sure to retrieve the `_ID` column. For example, to retrieve email data, define the
following projection:

### Kotlin

```kotlin
private val PROJECTION: Array<String> = arrayOf(
        ContactsContract.CommonDataKinds.Email._ID,
        ContactsContract.CommonDataKinds.Email.ADDRESS,
        ContactsContract.CommonDataKinds.Email.TYPE,
        ContactsContract.CommonDataKinds.Email.LABEL
)
```

### Java

```java
    private static final String[] PROJECTION =
            {
                ContactsContract.CommonDataKinds.Email._ID,
                ContactsContract.CommonDataKinds.Email.ADDRESS,
                ContactsContract.CommonDataKinds.Email.TYPE,
                ContactsContract.CommonDataKinds.Email.LABEL
            };
```


Notice that this projection uses the column names defined in the class
`https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email`, instead of the column names
defined in the class `https://developer.android.com/reference/android/provider/ContactsContract.Data`. Using the email-specific
column names makes the code more readable.


In the projection, you can also use any of the other columns defined in the
`https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds` subclass.

### Define selection criteria


Define a search text expression that retrieves rows for a specific contact's
`https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY` and the
`https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE` of the details you
want. Enclose the `https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE` value in
single quotes by concatenating a "`'`" (single-quote) character to the start and end
of the constant; otherwise, the provider interprets the constant as a variable name rather
than as a string value. You don't need to use a placeholder for this value, because you're
using a constant rather than a user-supplied value. For example:

### Kotlin

```kotlin
/*
 * Defines the selection clause. Search for a lookup key
 * and the Email MIME type
 */
private const val SELECTION =
        "${ContactsContract.Data.LOOKUP_KEY} = ? AND " +
        "${ContactsContract.Data.MIMETYPE} = '${Email.CONTENT_ITEM_TYPE}'"
...
// Defines the array to hold the search criteria
private val selectionArgs: Array<String> = arrayOf("")
```

### Java

```java
    /*
     * Defines the selection clause. Search for a lookup key
     * and the Email MIME type
     */
    private static final String SELECTION =
            Data.LOOKUP_KEY + " = ?" +
            " AND " +
            Data.MIMETYPE + " = " +
            "'" + Email.CONTENT_ITEM_TYPE + "'";
    // Defines the array to hold the search criteria
    private String[] selectionArgs = { "" };
```

### Define a sort order


Define a sort order for the returned `https://developer.android.com/reference/android/database/Cursor`. Since you're retrieving a
specific data type, omit the sort on `https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE`.
Instead, if the type of detail data you're searching includes a subtype, sort on it.
For example, for email data you can sort on
`https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.CommonColumns#TYPE`:

### Kotlin

```kotlin
private const val SORT_ORDER: String = "${Email.TYPE} ASC"
```

### Java

```java
    private static final String SORT_ORDER = Email.TYPE + " ASC ";
```