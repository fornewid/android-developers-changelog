---
title: https://developer.android.com/identity/providers/contacts-provider/display-contact-badge
url: https://developer.android.com/identity/providers/contacts-provider/display-contact-badge
source: md.txt
---

This page shows you how to add a [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge) to your UI
and how to bind data to it. A `QuickContactBadge` is a widget that
initially appears as a thumbnail image. Although you can use any [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap)
for the thumbnail image, you usually use a `Bitmap` decoded from the
contact's photo thumbnail image.


The small image acts as a control; when users tap the image, the
`QuickContactBadge` expands into a dialog containing the following:

A large image
:
    The large image associated with the contact or, if no image is available, a placeholder
    graphic.


App icons
:
    An app icon for each piece of detail data that can be handled by a built-in app. For
    example, if the contact's details include one or more email addresses, an email icon
    appears. When users tap the icon, all the contact's email addresses appear. When users
    tap one of the addresses, the email app displays a screen for composing a message to the
    selected email address.


The `QuickContactBadge` view provides instant access to a contact's
details and a fast way to communicate with the contact. Users don't have to look up
a contact, find and copy information, and then paste it into the appropriate app. Instead, they
can tap the `QuickContactBadge`, choose the communication method they
want to use, and send the information for that method directly to the appropriate app.

## Add a QuickContactBadge view


To add a [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge), insert a
`<QuickContactBadge>` element in your layout, as shown in the following example:  

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
                android:layout_width="match_parent"
                android:layout_height="match_parent">
...
    <QuickContactBadge
               android:id=@+id/quickbadge
               android:layout_height="wrap_content"
               android:layout_width="wrap_content"
               android:scaleType="centerCrop"/>
    ...
</RelativeLayout>
```

## Retrieve provider data


To display a contact in the [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge), you need a content URI
for the contact and a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) for the small image. You generate
both the content URI and the `Bitmap` from columns retrieved from the
Contacts Provider. Specify these columns as part of the projection you use to load data into
your [Cursor](https://developer.android.com/reference/android/database/Cursor).


For Android 3.0 (API level 11) and higher, include the following columns in your projection:

- [Contacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)
- [Contacts.LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY)
- [Contacts.PHOTO_THUMBNAIL_URI](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#PHOTO_THUMBNAIL_URI)


For Android 2.3.3 (API level 10) and lower, use the following columns:

- [Contacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)
- [Contacts.LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY)


The examples on this page assume that a
`Cursor` that contains these columns and any other selected
columns has been loaded. To learn how to retrieve columns in a `Cursor`, see
[Retrieve a list of contacts](https://developer.android.com/training/contacts-provider/retrieve-names).

## Set the contact URI and thumbnail


Once you have the necessary columns, you can bind data to the
[QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge).

### Set the contact URI


To set the content URI for the contact, call
[getLookupUri(id,lookupKey)](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#getLookupUri(android.content.ContentResolver, android.net.Uri)) to
get a [CONTENT_LOOKUP_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_LOOKUP_URI), then
call [assignContactUri()](https://developer.android.com/reference/android/widget/QuickContactBadge#assignContactUri(android.net.Uri)) to set the
contact. This is shown in the following example:  

### Kotlin

```kotlin
    // The Cursor that contains contact rows
    var cursor: Cursor? = null
    // The index of the _ID column in the Cursor
    var idColumn: Int = 0
    // The index of the LOOKUP_KEY column in the Cursor
    var lookupKeyColumn: Int = 0
    // A content URI for the desired contact
    var contactUri: Uri? = null
    // A handle to the QuickContactBadge view
    ...
    cursor?.let { cursor ->
        /*
         * Insert code here to move to the desired cursor row
         */
        // Gets the _ID column index
        idColumn = cursor.getColumnIndex(ContactsContract.Contacts._ID)
        // Gets the LOOKUP_KEY index
        lookupKeyColumn = cursor.getColumnIndex(ContactsContract.Contacts.LOOKUP_KEY)
        // Gets a content URI for the contact
        contactUri = ContactsContract.Contacts.getLookupUri(
                cursor.getLong(idColumn),
                cursor.getString(lookupKeyColumn)
        )
        binding.badge.assignContactUri(contactUri)
    }
```

### Java

```java
    // The Cursor that contains contact rows
    Cursor cursor;
    // The index of the _ID column in the Cursor
    int idColumn;
    // The index of the LOOKUP_KEY column in the Cursor
    int lookupKeyColumn;
    // A content URI for the desired contact
    Uri contactUri;
    ...
    /*
     * Insert code here to move to the desired cursor row
     */
    // Gets the _ID column index
    idColumn = cursor.getColumnIndex(ContactsContract.Contacts._ID);
    // Gets the LOOKUP_KEY index
    lookupKeyColumn = cursor.getColumnIndex(ContactsContract.Contacts.LOOKUP_KEY);
    // Gets a content URI for the contact
    contactUri =
            Contacts.getLookupUri(
                cursor.getLong(idColumn),
                cursor.getString(lookupKeyColumn)
            );
    binding.badge.assignContactUri(contactUri);
```


When users tap the [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge) icon, the contact's
details appear in the dialog.

### Set the photo thumbnail


Setting the contact URI for the [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge) does not automatically
load the contact's thumbnail photo. To load the photo, get a URI for the photo from the
contact's [Cursor](https://developer.android.com/reference/android/database/Cursor) row, use it to open the file containing the compressed
thumbnail photo, and read the file into a [Bitmap](https://developer.android.com/reference/android/graphics/Bitmap).


**Note:** The
[PHOTO_THUMBNAIL_URI](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#PHOTO_THUMBNAIL_URI) column isn't available
in platform versions prior to 3.0. For those versions, you must retrieve the URI
from the [Contacts.Photo](https://developer.android.com/reference/android/provider/ContactsContract.Contacts.Photo) subtable.


First, set up variables to access the `Cursor` containing the
[Contacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) and
[Contacts.LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY) columns:  

### Kotlin

```kotlin
    // The column in which to find the thumbnail ID
    var thumbnailColumn: Int = 0
    /*
     * The thumbnail URI, expressed as a String.
     * Contacts Provider stores URIs as String values.
     */
    var thumbnailUri: String? = null
    ...
    cursor?.let { cursor ->
        /*
         * Gets the photo thumbnail column index if
         * platform version >= Honeycomb
         */
        thumbnailColumn = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            cursor.getColumnIndex(ContactsContract.Contacts.PHOTO_THUMBNAIL_URI)
            // Otherwise, sets the thumbnail column to the _ID column
        } else {
            idColumn
        }
        /*
         * Assuming the current Cursor position is the contact you want,
         * gets the thumbnail ID
         */
        thumbnailUri = cursor.getString(thumbnailColumn)
    }
```

### Java

```java
    // The column in which to find the thumbnail ID
    int thumbnailColumn;
    /*
     * The thumbnail URI, expressed as a String.
     * Contacts Provider stores URIs as String values.
     */
    String thumbnailUri;
    ...
    /*
     * Gets the photo thumbnail column index if
     * platform version >= Honeycomb
     */
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        thumbnailColumn =
                cursor.getColumnIndex(ContactsContract.Contacts.PHOTO_THUMBNAIL_URI);
    // Otherwise, sets the thumbnail column to the _ID column
    } else {
        thumbnailColumn = idColumn;
    }
    /*
     * Assuming the current Cursor position is the contact you want,
     * gets the thumbnail ID
     */
    thumbnailUri = cursor.getString(thumbnailColumn);
    ...
```


Define a method that takes photo-related data for the contact and dimensions for the
destination view and returns the properly sized thumbnail in a
`Bitmap`. Start by constructing a URI that points to the
thumbnail:


### Kotlin

```kotlin
    /**
     * Load a contact photo thumbnail and return it as a Bitmap,
     * resizing the image to the provided image dimensions as needed.
     * @param photoData photo ID Prior to Honeycomb, the contact's _ID value.
     * For Honeycomb and later, the value of PHOTO_THUMBNAIL_URI.
     * @return A thumbnail Bitmap, sized to the provided width and height.
     * Returns null if the thumbnail is not found.
     */
    private fun loadContactPhotoThumbnail(photoData: String): Bitmap? {
        // Creates an asset file descriptor for the thumbnail file
        var afd: AssetFileDescriptor? = null
        // try-catch block for file not found
        try {
            // Creates a holder for the URI
            val thumbUri: Uri = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
                // If Android 3.0 or later,
                // sets the URI from the incoming PHOTO_THUMBNAIL_URI
                Uri.parse(photoData)
            } else {
                // Prior to Android 3.0, constructs a photo Uri using _ID
                /*
                 * Creates a contact URI from the Contacts content URI
                 * incoming photoData (_ID)
                 */
                val contactUri: Uri =
                        Uri.withAppendedPath(ContactsContract.Contacts.CONTENT_URI, photoData)
                /*
                 * Creates a photo URI by appending the content URI of
                 * Contacts.Photo
                 */
                Uri.withAppendedPath(contactUri, ContactsContract.Contacts.Photo.CONTENT_DIRECTORY)
            }

            /*
             * Retrieves an AssetFileDescriptor object for the thumbnail URI
             * using ContentResolver.openAssetFileDescriptor
             */
            afd = activity?.contentResolver?.openAssetFileDescriptor(thumbUri, "r")
            /*
             * Gets a file descriptor from the asset file descriptor.
             * This object can be used across processes.
             */
            return afd?.fileDescriptor?.let {fileDescriptor ->
                // Decodes the photo file and returns the result as a Bitmap
                // if the file descriptor is valid
                BitmapFactory.decodeFileDescriptor(fileDescriptor, null, null)
            }
        } catch (e: FileNotFoundException) {
            /*
             * Handle file not found errors
             */
            null
        } finally {
            // In all cases, close the asset file descriptor
            try {
                afd?.close()
            } catch (e: IOException) {
            }
        }
    }
```

### Java

```java
    /**
     * Load a contact photo thumbnail and return it as a Bitmap,
     * resizing the image to the provided image dimensions as needed.
     * @param photoData photo ID Prior to Honeycomb, the contact's _ID value.
     * For Honeycomb and later, the value of PHOTO_THUMBNAIL_URI.
     * @return A thumbnail Bitmap, sized to the provided width and height.
     * Returns null if the thumbnail is not found.
     */
    private Bitmap loadContactPhotoThumbnail(String photoData) {
        // Creates an asset file descriptor for the thumbnail file
        AssetFileDescriptor afd = null;
        // try-catch block for file not found
        try {
            // Creates a holder for the URI
            Uri thumbUri;
            // If Android 3.0 or later
            if (Build.VERSION.SDK_INT
                    >=
                Build.VERSION_CODES.HONEYCOMB) {
                // Sets the URI from the incoming PHOTO_THUMBNAIL_URI
                thumbUri = Uri.parse(photoData);
            } else {
            // Prior to Android 3.0, constructs a photo Uri using _ID
                /*
                 * Creates a contact URI from the Contacts content URI
                 * incoming photoData (_ID)
                 */
                final Uri contactUri = Uri.withAppendedPath(
                        ContactsContract.Contacts.CONTENT_URI, photoData);
                /*
                 * Creates a photo URI by appending the content URI of
                 * Contacts.Photo
                 */
                thumbUri =
                        Uri.withAppendedPath(
                                contactUri, ContactsContract.Contacts.Photo.CONTENT_DIRECTORY);
            }

        /*
         * Retrieves an AssetFileDescriptor object for the thumbnail URI
         * using ContentResolver.openAssetFileDescriptor
         */
        afd = getActivity().getContentResolver().
                openAssetFileDescriptor(thumbUri, "r");
        /*
         * Gets a file descriptor from the asset file descriptor.
         * This object can be used across processes.
         */
        FileDescriptor fileDescriptor = afd.getFileDescriptor();
        // Decodes the photo file and returns the result as a Bitmap
        // if the file descriptor is valid
        if (fileDescriptor != null) {
            // Decodes the bitmap
            return BitmapFactory.decodeFileDescriptor(
                    fileDescriptor, null, null);
            }
        // If the file isn't found
        } catch (FileNotFoundException e) {
            /*
             * Handle file not found errors
             */
        // In all cases, close the asset file descriptor
        } finally {
            if (afd != null) {
                try {
                    afd.close();
                } catch (IOException e) {}
            }
        }
        return null;
    }
```


Call the `loadContactPhotoThumbnail()` method in your code to get the
thumbnail `Bitmap`, and use the result to set the photo thumbnail in
your `QuickContactBadge`:  

### Kotlin

```kotlin
    ...
    /*
     * Decodes the thumbnail file to a Bitmap
     */
    mThumbnailUri?.also { thumbnailUri ->
        loadContactPhotoThumbnail(thumbnailUri).also { thumbnail ->
            /*
             * Sets the image in the QuickContactBadge.
             * QuickContactBadge inherits from ImageView.
             */
            badge.setImageBitmap(thumbnail)
        }
    }
```

### Java

```java
    ...
    /*
     * Decodes the thumbnail file to a Bitmap
     */
    Bitmap mThumbnail =
            loadContactPhotoThumbnail(thumbnailUri);
    /*
     * Sets the image in the QuickContactBadge.
     * QuickContactBadge inherits from ImageView.
     */
    badge.setImageBitmap(mThumbnail);
```

## Add a QuickContactBadge to a ListView


A [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge) is a useful addition to a
[ListView](https://developer.android.com/reference/android/widget/ListView) that displays a list of contacts. Use the
`QuickContactBadge` to display a thumbnail photo for each contact; when
users tap the thumbnail, the `QuickContactBadge` dialog appears.

### Add the QuickContactBadge element


To start, add a [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge) view element to your item layout
For example, if you want to display a `QuickContactBadge` and a name for
each contact you retrieve, put the following XML into a layout file:  

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
                android:layout_width="match_parent"
                android:layout_height="wrap_content">
    <QuickContactBadge
        android:id="@+id/quickcontact"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:scaleType="centerCrop"/>
    <TextView android:id="@+id/displayname"
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:layout_toRightOf="@+id/quickcontact"
              android:gravity="center_vertical"
              android:layout_alignParentRight="true"
              android:layout_alignParentTop="true"/>
</RelativeLayout>
```


In the following sections, this file is referred to as `contact_item_layout.xml`.

### Set up a custom CursorAdapter


To bind a [CursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter) to a [ListView](https://developer.android.com/reference/android/widget/ListView)
containing a [QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge), define a custom adapter that
extends `CursorAdapter`. This approach lets you process the
data in the [Cursor](https://developer.android.com/reference/android/database/Cursor) before you bind it to the
`QuickContactBadge`. This approach also lets you bind multiple
`Cursor` columns to the `QuickContactBadge`. Neither
of these operations is possible in a regular `CursorAdapter`.


The subclass of `CursorAdapter` that you define must
override the following methods:

[CursorAdapter.newView()](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter#newView(android.content.Context, android.database.Cursor, android.view.ViewGroup))
:
    Inflates a new [View](https://developer.android.com/reference/android/view/View) object to hold the item layout. In the override
    of this method, store handles to the child `View` objects of the layout,
    including the child `QuickContactBadge`. By taking this approach, you
    avoid having to get handles to the child `View` objects each time you
    inflate a new layout.


    You must override this method so you can get handles to the individual child
    `View` objects. This technique lets you control their binding in
    `CursorAdapter.bindView()`.

[CursorAdapter.bindView()](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter#bindView(android.view.View, android.content.Context, android.database.Cursor))
:
    Moves data from the current `Cursor` row to the child
    `View` objects of the item layout. You must override this method so
    you can bind both the contact's URI and thumbnail to the
    `QuickContactBadge`. The default implementation only permits a one-to-one
    mapping between a column and a `View`.


The following code snippet contains an example of a custom subclass of
`CursorAdapter`:

### Define the custom list adapter


Define the subclass of
[CursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter),
including its constructor, and override
[newView()](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter#newView(android.content.Context, android.database.Cursor, android.view.ViewGroup)) and
[bindView()](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter#bindView(android.view.View, android.content.Context, android.database.Cursor)):  

### Kotlin

```kotlin
    /**
     * Defines a class that holds resource IDs of each item layout
     * row to prevent having to look them up each time data is
     * bound to a row
     */
    private data class ViewHolder(
            internal var displayname: TextView? = null,
            internal var quickcontact: QuickContactBadge? = null
    )

    /**
     *
     *
     */
    private inner class ContactsAdapter(
            context: Context,
            val inflater: LayoutInflater = LayoutInflater.from(context)
    ) : CursorAdapter(context, null, 0) {
        ...
        override fun newView(
                context: Context,
                cursor: Cursor,
                viewGroup: ViewGroup
        ): View {
            /* Inflates the item layout. Stores view references
             * in a ViewHolder class to prevent having to look
             * them up each time bindView() is called.
             */
            return ContactListLayoutBinding.inflate(inflater,
                    viewGroup,
                    false).also { binding ->
                view.tag = ViewHolder().apply {
                    displayname = binding.displayname
                    quickcontact = binding.quickcontact
                }
            }.root
        }
        ...
        override fun bindView(view: View?, context: Context?, cursor: Cursor?) {
            (view?.tag as? ViewHolder)?.also { holder ->
                cursor?.apply {
                    ...
                    // Sets the display name in the layout
                    holder.displayname?.text = getString(displayNameIndex)
                    ...
                    /*
                     * Generates a contact URI for the QuickContactBadge
                     */
                    ContactsContract.Contacts.getLookupUri(
                            getLong(idIndex),
                            cursor.getString(lookupKeyIndex)
                    ).also { contactUri ->
                        holder.quickcontact?.assignContactUri(contactUri)
                    }

                    getString(photoDataIndex)?.also {photoData ->
                        /*
                         * Decodes the thumbnail file to a Bitmap.
                         * The method loadContactPhotoThumbnail() is defined
                         * in the section "Set the contact URI and thumbnail."
                         */
                        loadContactPhotoThumbnail(photoData)?.also { thumbnailBitmap ->
                            /*
                             * Sets the image in the QuickContactBadge.
                             * QuickContactBadge inherits from ImageView.
                             */
                            holder.quickcontact?.setImageBitmap(thumbnailBitmap)
                        }
                    }
                }
            }

        }
    }
```

### Java

```java
    private class ContactsAdapter extends CursorAdapter {
        private LayoutInflater inflater;
        ...
        public ContactsAdapter(Context context) {
            super(context, null, 0);

            /*
             * Gets an inflater that can instantiate
             * the ListView layout from the file
             */
            inflater = LayoutInflater.from(context);
            ...
        }
        ...
        /**
         * Defines a class that holds resource IDs of each item layout
         * row to prevent having to look them up each time data is
         * bound to a row
         */
        private class ViewHolder {
            TextView displayname;
            QuickContactBadge quickcontact;
        }
        ...
        @Override
        public View newView(
                Context context,
                Cursor cursor,
                ViewGroup viewGroup) {
            /* Inflates the item layout. Stores view references
             * in a ViewHolder class to prevent having to look
             * them up each time bindView() is called.
             */
            final ContactListLayoutBinding binding =
            ContactListLayoutBinding.inflate(inflater, 
                viewGroup,
                false);
            final ViewHolder holder = new ViewHolder();
            holder.displayname =
                    binding.displayName;
            holder.quickcontact =
                    binding.quickContact;
            view.setTag(holder);
            return binding.root;
        }
        ...
        @Override
        public void bindView(
                View view,
                Context context,
                Cursor cursor) {
            final ViewHolder holder = (ViewHolder) view.getTag();
            final String photoData =
                    cursor.getString(photoDataIndex);
            final String displayName =
                    cursor.getString(displayNameIndex);
            ...
            // Sets the display name in the layout
            holder.displayname = cursor.getString(displayNameIndex);
            ...
            /*
             * Generates a contact URI for the QuickContactBadge
             */
            final Uri contactUri = Contacts.getLookupUri(
                    cursor.getLong(idIndex),
                    cursor.getString(lookupKeyIndex));
            holder.quickcontact.assignContactUri(contactUri);
            String photoData = cursor.getString(photoDataIndex);
            /*
             * Decodes the thumbnail file to a Bitmap.
             * The method loadContactPhotoThumbnail() is defined
             * in the section "Set the contact URI and thumbnail."
             */
            Bitmap thumbnailBitmap =
                    loadContactPhotoThumbnail(photoData);
            /*
             * Sets the image in the QuickContactBadge.
             * QuickContactBadge inherits from ImageView.
             */
            holder.quickcontact.setImageBitmap(thumbnailBitmap);
    }
```

### Set up variables


In your code, set up variables including a [Cursor](https://developer.android.com/reference/android/database/Cursor) projection that
includes the necessary columns, as shown in the following example.


**Note:** The following code snippets use the method
`loadContactPhotoThumbnail()`, which is defined in the
[Set the contact URI and thumbnail](https://developer.android.com/identity/providers/contacts-provider/display-contact-badge#SetURIThumbnail) section.  

### Kotlin

```kotlin
/*
 * Defines a projection based on platform version. This ensures
 * that you retrieve the correct columns.
 */
private val PROJECTION: Array<out String> = arrayOf(
        ContactsContract.Contacts._ID,
        ContactsContract.Contacts.LOOKUP_KEY,
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            ContactsContract.Contacts.DISPLAY_NAME_PRIMARY
        } else {
            ContactsContract.Contacts.DISPLAY_NAME
        },
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            ContactsContract.Contacts.PHOTO_FILE_ID
        } else {
            /*
             * Although it's not necessary to include the
             * column twice, this keeps the number of
             * columns the same regardless of version
             */
            ContactsContract.Contacts._ID
        }
)
...
class ContactsFragment : Fragment(), LoaderManager.LoaderCallbacks<Cursor> {
    ...
    // Defines a ListView
    private val listView: ListView? = null
    // Defines a ContactsAdapter
    private val adapter: ContactsAdapter? = null
    ...
    // Defines a Cursor to contain the retrieved data
    private val cursor: Cursor? = null
    /*
     * As a shortcut, defines constants for the
     * column indexes in the Cursor. The index is
     * 0-based and always matches the column order
     * in the projection.
     */
    // Column index of the _ID column
    private val idIndex = 0
    // Column index of the LOOKUP_KEY column
    private val lookupKeyIndex = 1
    // Column index of the display name column
    private val displayNameIndex = 3
    /*
     * Column index of the photo data column.
     * It's PHOTO_THUMBNAIL_URI for Honeycomb and later,
     * and _ID for previous versions.
     */
    private val photoDataIndex: Int =
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) 3 else 0
    ...
```

### Java

```java
public class ContactsFragment extends Fragment implements
        LoaderManager.LoaderCallbacks<Cursor> {
...
    // Defines a ListView
    private ListView listView;
    // Defines a ContactsAdapter
    private ContactsAdapter adapter;
    ...
    // Defines a Cursor to contain the retrieved data
    private Cursor cursor;
    /*
     * Defines a projection based on platform version. This ensures
     * that you retrieve the correct columns.
     */
    private static final String[] PROJECTION =
            {
                ContactsContract.Contacts._ID,
                ContactsContract.Contacts.LOOKUP_KEY,
                (Build.VERSION.SDK_INT >=
                 Build.VERSION_CODES.HONEYCOMB) ?
                        ContactsContract.Contacts.DISPLAY_NAME_PRIMARY :
                        ContactsContract.Contacts.DISPLAY_NAME
                (Build.VERSION.SDK_INT >=
                 Build.VERSION_CODES.HONEYCOMB) ?
                        ContactsContract.Contacts.PHOTO_FILE_ID :
                        /*
                         * Although it's not necessary to include the
                         * column twice, this keeps the number of
                         * columns the same regardless of version
                         */
                        ContactsContract.Contacts._ID
            };
    /*
     * As a shortcut, defines constants for the
     * column indexes in the Cursor. The index is
     * 0-based and always matches the column order
     * in the projection.
     */
    // Column index of the _ID column
    private int idIndex = 0;
    // Column index of the LOOKUP_KEY column
    private int lookupKeyIndex = 1;
    // Column index of the display name column
    private int displayNameIndex = 3;
    /*
     * Column index of the photo data column.
     * It's PHOTO_THUMBNAIL_URI for Honeycomb and later,
     * and _ID for previous versions.
     */
    private int photoDataIndex =
            Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB ?
            3 :
            0;
    ...
```

### Set up the ListView


In [Fragment.onCreate()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate(android.os.Bundle)), instantiate the custom
cursor adapter and get a handle to the [ListView](https://developer.android.com/reference/android/widget/ListView):  

### Kotlin

```kotlin
    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        return FragmentListViewBinding.inflate(...).let { binding ->
            ...
            /*
             * Gets a handle to the ListView in the file
             * contact_list_layout.xml
             */
            listView = binding.contactList
            mAdapter?.also {
                listView?.adapter = it
            }
            ...
        }.root
    }
    ...
```

### Java

```java
    @Override
    public View onCreateView(LayoutInflater inflater,
            ViewGroup container, Bundle savedInstanceState) {
        FragmentListViewBinding binding = FragmentListViewBinding.inflate(...)
        ...
        /*
         * Gets a handle to the ListView in the file
         * contact_list_layout.xml
         */
        if (binding.contactListView != null && adapter != null) {
            binding.contactListView.setAdapter(adapter);
        }
        ...
    }
    ...
```


In [onViewCreated()](https://developer.android.com/reference/androidx/fragment/app/Fragment#onViewCreated(android.view.View,%20android.os.Bundle)), bind the
`ContactsAdapter` to the `ListView`:  

### Kotlin

```kotlin
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)
    /*
     * Instantiates the subclass of
     * CursorAdapter
     */
    mAdapter = activity?.let {
        ContactsAdapter(it).also { adapter ->
            // Sets up the adapter for the ListView
            listView?.adapter = adapter
        }
    }
}
```

### Java

```java
@Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        ...
        /*
         * Instantiates the subclass of
         * CursorAdapter
         */
        mAdapter = new ContactsAdapter(getActivity());
        // Sets up the adapter for the ListView
        if (listView != null && mAdapter != null) {
            listView.setAdapter(mAdapter);
        }
        ...
    }
    ...
```


When you get back a [Cursor](https://developer.android.com/reference/android/database/Cursor) containing the contacts data, usually in
[onLoadFinished()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoadFinished(androidx.loader.content.Loader%3CD%3E,D)),
call [swapCursor()](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter#swapCursor(android.database.Cursor)) to move the
`Cursor` data to the `ListView`. This displays the
[QuickContactBadge](https://developer.android.com/reference/android/widget/QuickContactBadge) for each entry in the list of contacts.  

### Kotlin

```kotlin
override fun onLoadFinished(loader: Loader<Cursor>, cursor: Cursor) {
    // When the loader has completed, swap the cursor into the adapter
    mAdapter?.swapCursor(cursor)
}
```

### Java

```java
public void onLoadFinished(Loader<Cursor> loader, Cursor cursor) {
        // When the loader has completed, swap the cursor into the adapter
        mAdapter.swapCursor(cursor);
    }
```


When you bind a `Cursor` to a
`ListView` with a [CursorAdapter](https://developer.android.com/reference/androidx/cursoradapter/widget/CursorAdapter)
(or subclass), and you use a [CursorLoader](https://developer.android.com/reference/androidx/loader/content/CursorLoader) to load the
`Cursor`, always clear references to the `Cursor`
in your implementation of
[onLoaderReset()](https://developer.android.com/reference/androidx/loader/app/LoaderManager.LoaderCallbacks#onLoaderReset(androidx.loader.content.Loader%3CD%3E)).
This is shown in the following example:  

### Kotlin

```kotlin
    override fun onLoaderReset(loader: Loader<Cursor>) {
        // Removes remaining reference to the previous Cursor
        adapter?.swapCursor(null)
    }
```

### Java

```java
    @Override
    public void onLoaderReset(Loader<Cursor> loader) {
        // Removes remaining reference to the previous Cursor
        adapter.swapCursor(null);
    }
```