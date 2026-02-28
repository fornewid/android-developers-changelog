---
title: https://developer.android.com/about/versions/17/features/contact-picker
url: https://developer.android.com/about/versions/17/features/contact-picker
source: md.txt
---

The Android Contact Picker is a standardized, browsable interface for users to
share contacts with your app. Available on devices running
Android 17 or higher, the picker offers a privacy-preserving
alternative to the broad `READ_CONTACTS` permission. Instead of requesting
access to the user's entire address book, your app specifies the data fields it
needs, such as phone numbers or email addresses, and the user selects specific
contacts to share. This grants your app read access to only the selected data,
ensuring granular control while providing a consistent user experience with
built-in search, profile switching, and multi-selection capabilities without
having to build or maintain the UI.

## Integrate the Contact Picker

To integrate the Contact Picker, use the `Intent.ACTION_PICK_CONTACTS` intent.
This intent launches the picker and returns the selected contacts to your app.

Unlike the legacy `ACTION_PICK`, the Contact Picker lets you specify multiple
data fields your app requires at the same time. You do this using
`Intent.EXTRA_REQUESTED_DATA_FIELDS`, passing an `ArrayList<String>` of MIME
types defined in `ContactsContract.CommonDataKinds`.

Common MIME types include:

- `ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE`
- `ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE`
- `ContactsContract.CommonDataKinds.StructuredPostal.CONTENT_ITEM_TYPE`

## Launch the picker

Use `registerForActivityResult` with the `StartActivityForResult` contract to
launch the picker. You can configure the intent to allow single or multiple
selections.

### Select a single contact

In this example, the app requests only phone numbers. The picker will filter the
list to show only contacts with phone numbers and allow the user to select a
specific number.

### Kotlin

    // Define the specific data fields you need
    val requestedFields = arrayListOf(
        ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE
    )

    // Set up the intent
    val pickContactIntent = Intent(Intent.ACTION_PICK_CONTACTS).apply {
        type = ContactsContract.Contacts.CONTENT_TYPE
        putStringArrayListExtra(Intent.EXTRA_REQUESTED_DATA_FIELDS, requestedFields)
    }

    // Launch the picker
    pickContactLauncher.launch(pickContactIntent)

### Java

    // Define the specific data fields you need
    ArrayList<String> requestedFields = new ArrayList<>();
    requestedFields.add(ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE);

    // Set up the intent
    Intent pickContactIntent = new Intent(Intent.ACTION_PICK_CONTACTS);
    pickContactIntent.setType(ContactsContract.Contacts.CONTENT_TYPE);
    pickContactIntent.putStringArrayListExtra(Intent.EXTRA_REQUESTED_DATA_FIELDS,
            requestedFields);

    // Launch the picker
    pickContactLauncher.launch(pickContactIntent);

### Select multiple contacts

To enable multi-selection, add the `Intent.EXTRA_ALLOW_MULTIPLE` extra. You can
optionally limit the number of items a user can select.

### Kotlin

    val requestedFields = arrayListOf(
        ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE,
        ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE
    )

    val pickMultipleIntent = Intent(Intent.ACTION_PICK_CONTACTS).apply {
        type = ContactsContract.Contacts.CONTENT_TYPE
        putStringArrayListExtra(Intent.EXTRA_REQUESTED_DATA_FIELDS, requestedFields)
        // Enable multi-select
        putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true)
        // Optional: Set a custom limit (max 50 recommended)
        putExtra(Intent.EXTRA_SELECTION_LIMIT, 10)
    }

    pickMultipleLauncher.launch(pickMultipleIntent)

## Handle the results

When the user completes the selection, the system returns a `RESULT_OK` and a
Session URI. This URI grants temporary read access to the selected data.

You can query this URI using a standard `ContentResolver`. The resulting
`Cursor` contains the requested data fields and follows the schema of
`ContactsContract.Data`.

### Kotlin

    private val pickContactLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            // The result data contains the Session URI
            val sessionUri = result.data?.data
            sessionUri?.let { uri ->
                processSelectedContacts(uri)
            }
        } else {
            // User cancelled the picker
        }
    }

    private fun processSelectedContacts(sessionUri: Uri) {
        // Define the projection (columns) you want to retrieve
        val projection = arrayOf(
            ContactsContract.Data.CONTACT_ID,
            ContactsContract.Contacts.DISPLAY_NAME_PRIMARY,
            ContactsContract.Data.MIMETYPE,
            ContactsContract.Data.DATA1 // Generic data column (Phone number, Email, etc.)
        )

        contentResolver.query(sessionUri, projection, null, null, null)?.use { cursor ->
            val mimeTypeIdx = cursor.getColumnIndex(ContactsContract.Data.MIMETYPE)
            val dataIdx = cursor.getColumnIndex(ContactsContract.Data.DATA1)
            val nameIdx = cursor.getColumnIndex(ContactsContract.Contacts.DISPLAY_NAME_PRIMARY)

            while (cursor.moveToNext()) {
                val mimeType = cursor.getString(mimeTypeIdx)
                val dataValue = cursor.getString(dataIdx)
                val name = cursor.getString(nameIdx)

                when (mimeType) {
                    ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE -> {
                        Log.d("ContactPicker", "Picked Phone: $dataValue for $name")
                    }
                    ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE -> {
                        Log.d("ContactPicker", "Picked Email: $dataValue for $name")
                    }
                }
            }
        }
    }

## Backward Compatibility

For apps targeting Android 17 and higher, the system
automatically upgrades the existing `Intent.ACTION_PICK` intent to use the new
Contact Picker interface.

If your app already uses `ACTION_PICK`, you don't need to change your code to
receive the new UI. However, to take advantage of new features, such as
receiving a single `Uri` to query contact data, switching between personal \&
work profiles or multiple data field requests, you must update your
implementation to use `Intent.ACTION_PICK_CONTACTS` or the new intent extras.

### Testing on older SDKs

You can test the new picker behavior on devices running Android 17 and
higher even if your app targets a lower SDK version by adding the
`EXTRA_USE_SYSTEM_CONTACTS_PICKER` boolean extra to your `ACTION_PICK` intent.

## Best practices

- **Request only what you need** : If your app only needs to send an SMS, request `Phone.CONTENT_ITEM_TYPE`. The picker will automatically filter out contacts that don't have phone numbers, resulting in a cleaner UI for the user.
- **Persist data immediately**: The Session URI grants temporary read permission. If you need to access this contact information later (after your app process is killed), your app has to persist the contact data.
- **Don't rely on Account Data**: To protect user privacy and prevent fingerprinting, account-specific metadata is stripped from the results.