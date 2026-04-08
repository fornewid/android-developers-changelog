---
title: Retrieve details for a contact  |  Identity  |  Android Developers
url: https://developer.android.com/identity/providers/contacts-provider/retrieve-details
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Identity](https://developer.android.com/identity)
* [Guides](https://developer.android.com/identity/credential-manager)

# Retrieve details for a contact Stay organized with collections Save and categorize content based on your preferences.



This lesson shows how to retrieve detail data for a contact, such as email addresses, phone
numbers, and so forth. It's the details that users are looking for when they retrieve a contact.
You can give them all the details for a contact, or only display details of a particular type,
such as email addresses.

The steps in this lesson assume that you already have a
`ContactsContract.Contacts` row for a contact the user has picked.
The [Retrieving contact names](/identity/providers/contacts-provider/retrieve-names) lesson shows how to
retrieve a list of contacts.

## Retrieve all details for a contact

To retrieve all the details for a contact, search the
`ContactsContract.Data` table for any rows that contain the contact's
`LOOKUP_KEY`. This column is available in
the `ContactsContract.Data` table, because the Contacts
Provider makes an implicit join between the `ContactsContract.Contacts`
table and the `ContactsContract.Data` table. The
`LOOKUP_KEY` column is described
in more detail in the [Retrieving contact names](/identity/providers/contacts-provider/retrieve-names) lesson.

**Note:** Retrieving all the details for a contact reduces the performance of a
device, because it needs to retrieve all of the columns in the
`ContactsContract.Data` table. Consider the performance impact before
you use this technique.

### Request permissions

To read from the Contacts Provider, your app must have
`READ_CONTACTS` permission.
To request this permission, add the following child element of
`<manifest>` to your manifest file:

```
    <uses-permission android:name="android.permission.READ_CONTACTS" />
```

### Set up a projection

Depending on the data type a row contains, it may use only a few columns or many. In addition,
the data is in different columns depending on the data type.
To ensure you get all the possible columns for all possible data types, you need to add all the
column names to your projection. Always retrieve
`Data._ID` if you're binding the result
`Cursor` to a `ListView`; otherwise, the binding
won't work. Also retrieve `Data.MIMETYPE`
so you can identify the data type of each row you retrieve. For example:

### Kotlin

```
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

```
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
`ContactsContract.Data` table, using the column names defined in
the `ContactsContract.Data` class.

Optionally, you can also use any other column constants defined in or inherited by the
`ContactsContract.Data` class. Notice, however, that the columns
`SYNC1` through
`SYNC4` are meant to be used by sync
adapters, so their data is not useful.

### Define the selection criteria

Define a constant for your selection clause, an array to hold selection arguments, and a
variable to hold the selection value. Use
the `Contacts.LOOKUP_KEY` column to
find the contact. For example:

### Kotlin

```
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

```
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

Define the sort order you want in the resulting `Cursor`. To
keep all rows for a particular data type together, sort by
`Data.MIMETYPE`. This query argument
groups all email rows together, all phone rows together, and so forth. For example:

### Kotlin

```
/*
 * Defines a string that specifies a sort order of MIME type
 */
private const val SORT_ORDER = ContactsContract.Data.MIMETYPE
```

### Java

```
    /*
     * Defines a string that specifies a sort order of MIME type
     */
    private static final String SORT_ORDER = ContactsContract.Data.MIMETYPE;
```

**Note:** Some data types don't use a subtype, so you can't sort on subtype.
Instead, you have to iterate through the returned `Cursor`,
determine the data type of the current row, and store data for rows that use a subtype. When
you finish reading the cursor, you can then sort each data type by subtype and display the
results.

### Initialize the Loader

Always do retrievals from the Contacts Provider (and all other content providers) in a
background thread. Use the Loader framework defined by the
`LoaderManager` class and the
`LoaderManager.LoaderCallbacks` interface to do background
retrievals.

When you're ready to retrieve the rows, initialize the loader framework by
calling `initLoader()`. Pass an
integer identifier to the method; this identifier is passed to
`LoaderManager.LoaderCallbacks` methods. The identifier helps you
use multiple loaders in an app by allowing you to differentiate between them.

The following snippet shows how to initialize the loader framework:

### Kotlin

```
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

```
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

Implement the `onCreateLoader()` method, which is called by the loader framework immediately after you call
`initLoader()`. Return a
`CursorLoader` from this method. Since you're searching
the `ContactsContract.Data` table, use the constant
`Data.CONTENT_URI` as the content URI.
For example:

### Kotlin

```
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

```
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
`onLoadFinished()`
method. The loader framework calls
`onLoadFinished()`
when the Contacts Provider returns the results of the query. For example:

### Kotlin

```
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

```
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

The method `onLoaderReset()` is invoked when the loader framework detects that the data backing the result
`Cursor` has changed. At this point, remove any existing references
to the `Cursor` by setting them to null. If you don't, the loader
framework won't destroy the old `Cursor`, and you'll get a memory
leak. For example:

### Kotlin

```
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

```
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
listed in [Retrieve all details for a contact](#RetrieveAll):

Projection
:   Modify your projection to retrieve the columns that are specific to the
    data type. Also modify the projection to use the column name constants defined in the
    `ContactsContract.CommonDataKinds` subclass corresponding to the
    data type.

Selection
:   Modify the selection text to search for the
    `MIMETYPE` value that's specific to
    your data type.

Sort order
:   Since you're only selecting a single detail type, don't group the returned
    `Cursor` by `Data.MIMETYPE`.

These modifications are described in the following sections.

### Define a projection

Define the columns you want to retrieve, using the column name constants in the subclass
of `ContactsContract.CommonDataKinds` for the data type.
If you plan to bind your `Cursor` to a `ListView`,
be sure to retrieve the `_ID` column. For example, to retrieve email data, define the
following projection:

### Kotlin

```
private val PROJECTION: Array<String> = arrayOf(
        ContactsContract.CommonDataKinds.Email._ID,
        ContactsContract.CommonDataKinds.Email.ADDRESS,
        ContactsContract.CommonDataKinds.Email.TYPE,
        ContactsContract.CommonDataKinds.Email.LABEL
)
```

### Java

```
    private static final String[] PROJECTION =
            {
                ContactsContract.CommonDataKinds.Email._ID,
                ContactsContract.CommonDataKinds.Email.ADDRESS,
                ContactsContract.CommonDataKinds.Email.TYPE,
                ContactsContract.CommonDataKinds.Email.LABEL
            };
```

Notice that this projection uses the column names defined in the class
`ContactsContract.CommonDataKinds.Email`, instead of the column names
defined in the class `ContactsContract.Data`. Using the email-specific
column names makes the code more readable.

In the projection, you can also use any of the other columns defined in the
`ContactsContract.CommonDataKinds` subclass.

### Define selection criteria

Define a search text expression that retrieves rows for a specific contact's
`LOOKUP_KEY` and the
`Data.MIMETYPE` of the details you
want. Enclose the `MIMETYPE` value in
single quotes by concatenating a "`'`" (single-quote) character to the start and end
of the constant; otherwise, the provider interprets the constant as a variable name rather
than as a string value. You don't need to use a placeholder for this value, because you're
using a constant rather than a user-supplied value. For example:

### Kotlin

```
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

```
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

Define a sort order for the returned `Cursor`. Since you're retrieving a
specific data type, omit the sort on `MIMETYPE`.
Instead, if the type of detail data you're searching includes a subtype, sort on it.
For example, for email data you can sort on
`Email.TYPE`:

### Kotlin

```
private const val SORT_ORDER: String = "${Email.TYPE} ASC"
```

### Java

```
    private static final String SORT_ORDER = Email.TYPE + " ASC ";
```