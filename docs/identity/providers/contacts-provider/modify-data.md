---
title: https://developer.android.com/identity/providers/contacts-provider/modify-data
url: https://developer.android.com/identity/providers/contacts-provider/modify-data
source: md.txt
---

# Modify contacts using intents

This lesson shows you how to use an[Intent](https://developer.android.com/reference/android/content/Intent)to insert a new contact or modify a contact's data. Instead of accessing the Contacts Provider directly, an[Intent](https://developer.android.com/reference/android/content/Intent)starts the contacts app, which runs the appropriate[Activity](https://developer.android.com/reference/android/app/Activity). For the modification actions described in this lesson, if you send extended data in the[Intent](https://developer.android.com/reference/android/content/Intent)it's entered into the UI of the[Activity](https://developer.android.com/reference/android/app/Activity)that is started.

Using an[Intent](https://developer.android.com/reference/android/content/Intent)to insert or update a single contact is the preferred way of modifying the Contacts Provider, for the following reasons:

- It saves you the time and effort of developing your own UI and code.
- It avoids introducing errors caused by modifications that don't follow the Contacts Provider's rules.
- It reduces the number of permissions you need to request. Your app doesn't need permission to write to the Contacts Provider, because it delegates modifications to the contacts app, which already has that permission.

## Insert a new contact using an intent

You often want to allow the user to insert a new contact when your app receives new data. For example, a restaurant review app can allow users to add the restaurant as a contact as they're reviewing it. To do this using an intent, create the intent using as much data as you have available, and then send the intent to the contacts app.

Inserting a contact using the contacts app inserts a new*raw* contact into the Contacts Provider's[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts)table. If necessary, the contacts app prompts users for the account type and account to use when creating the raw contact. The contacts app also notifies users if the raw contact already exists. Users then have option of canceling the insertion, in which case no contact is created. To learn more about raw contacts, see the[Contacts Provider](https://developer.android.com/guide/topics/providers/contacts-provider)API guide.

### Create an intent

To start, create a new[Intent](https://developer.android.com/reference/android/content/Intent)object with the action[Intents.Insert.ACTION](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert#ACTION). Set the MIME type to[RawContacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts#CONTENT_TYPE). For example:  

### Kotlin

```kotlin
...
// Creates a new Intent to insert a contact
val intent = Intent(ContactsContract.Intents.Insert.ACTION).apply {
    // Sets the MIME type to match the Contacts Provider
    type = ContactsContract.RawContacts.CONTENT_TYPE
}
```

### Java

```java
...
// Creates a new Intent to insert a contact
Intent intent = new Intent(ContactsContract.Intents.Insert.ACTION);
// Sets the MIME type to match the Contacts Provider
intent.setType(ContactsContract.RawContacts.CONTENT_TYPE);
```

If you already have details for the contact, such as a phone number or email address, you can insert them into the intent as extended data. For a key value, use the appropriate constant from[Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert). The contacts app displays the data in its insert screen, allowing users to make further edits and additions.  

### Kotlin

```kotlin
private var emailAddress: EditText? = null
private var phoneNumber: EditText? = null
...
/* Assumes EditText fields in your UI contain an email address
 * and a phone number.
 *
 */
emailAddress = findViewById(R.id.email)
phoneNumber = findViewById(R.id.phone)
...
/*
 * Inserts new data into the Intent. This data is passed to the
 * contacts app's Insert screen
 */
intent.apply {
    // Inserts an email address
    putExtra(ContactsContract.Intents.Insert.EMAIL, emailAddress?.text)
    /*
     * In this example, sets the email type to be a work email.
     * You can set other email types as necessary.
     */
    putExtra(
            ContactsContract.Intents.Insert.EMAIL_TYPE,
            ContactsContract.CommonDataKinds.Email.TYPE_WORK
    )
    // Inserts a phone number
    putExtra(ContactsContract.Intents.Insert.PHONE, phoneNumber?.text)
    /*
     * In this example, sets the phone type to be a work phone.
     * You can set other phone types as necessary.
     */
    putExtra(
            ContactsContract.Intents.Insert.PHONE_TYPE,
            ContactsContract.CommonDataKinds.Phone.TYPE_WORK
    )
}
```

### Java

```java
private EditText emailAddress = null;
private EditText phoneNumber = null;
...
/* Assumes EditText fields in your UI contain an email address
 * and a phone number.
 *
 */
emailAddress = (EditText) findViewById(R.id.email);
phoneNumber = (EditText) findViewById(R.id.phone);
...
/*
 * Inserts new data into the Intent. This data is passed to the
 * contacts app's Insert screen
 */
// Inserts an email address
intent.putExtra(ContactsContract.Intents.Insert.EMAIL, emailAddress.getText())
/*
 * In this example, sets the email type to be a work email.
 * You can set other email types as necessary.
 */
      .putExtra(ContactsContract.Intents.Insert.EMAIL_TYPE,
            ContactsContract.CommonDataKinds.Email.TYPE_WORK)
// Inserts a phone number
      .putExtra(ContactsContract.Intents.Insert.PHONE, phoneNumber.getText())
/*
 * In this example, sets the phone type to be a work phone.
 * You can set other phone types as necessary.
 */
      .putExtra(ContactsContract.Intents.Insert.PHONE_TYPE,
            ContactsContract.CommonDataKinds.Phone.TYPE_WORK);
```

Once you've created the[Intent](https://developer.android.com/reference/android/content/Intent), send it by calling[startActivity()](https://developer.android.com/reference/androidx/fragment/app/Fragment#startActivity(android.content.Intent)).  

### Kotlin

```kotlin
    /* Sends the Intent
     */
    startActivity(intent)
```

### Java

```java
    /* Sends the Intent
     */
    startActivity(intent);
```

This call opens a screen in the contacts app that allows users to enter a new contact. The account type and account name for the contact is listed at the top of the screen. Once users enter the data and click*Done* , the contacts app's contact list appears. Users return to your app by clicking*Back*.

## Edit an existing contact using an intent

Editing an existing contact using an[Intent](https://developer.android.com/reference/android/content/Intent)is useful if the user has already chosen a contact of interest. For example, an app that finds contacts that have postal addresses but lack a postal code could give users the option of looking up the code and then adding it to the contact.

To edit an existing contact using an intent, use a procedure similar to inserting a contact. Create an intent as described in the section[Insert a new contact using an intent](https://developer.android.com/identity/providers/contacts-provider/modify-data#InsertContact), but add the contact's[Contacts.CONTENT_LOOKUP_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_LOOKUP_URI)and the MIME type[Contacts.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_ITEM_TYPE)to the intent. If you want to edit the contact with details you already have, you can put them in the intent's extended data. Notice that some name columns can't be edited using an intent; these columns are listed in the summary section of the API reference for the class[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts)under the heading "Update".

Finally, send the intent. In response, the contacts app displays an edit screen. When the user finishes editing and saves the edits, the contacts app displays a contact list. When the user clicks*Back*, your app is displayed.

### Create the intent

To edit a contact, call[Intent(action)](https://developer.android.com/reference/android/content/Intent#Intent())to create an intent with the action[ACTION_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT). Call[setDataAndType()](https://developer.android.com/reference/android/content/Intent#setDataAndType(android.net.Uri, java.lang.String))to set the data value for the intent to the contact's[Contacts.CONTENT_LOOKUP_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_LOOKUP_URI)and the MIME type to[Contacts.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_ITEM_TYPE)MIME type; because a call to[setType()](https://developer.android.com/reference/android/content/Intent#setType(java.lang.String))overwrites the current data value for the[Intent](https://developer.android.com/reference/android/content/Intent), you must set the data and the MIME type at the same time.

To get a contact's[Contacts.CONTENT_LOOKUP_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_LOOKUP_URI), call[Contacts.getLookupUri(id, lookupkey)](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#getLookupUri(android.content.ContentResolver, android.net.Uri))with the contact's[Contacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)and[Contacts.LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY)values as arguments.

**Note:** A contact's[LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY)value is the identifier that you should use to retrieve a contact. It remains constant, even if the provider changes the contact's row ID to handle internal operations.

The following snippet shows you how to create an intent:  

### Kotlin

```kotlin
    // The Cursor that contains the Contact row
    var mCursor: Cursor? = null
    // The index of the lookup key column in the cursor
    var lookupKeyIndex: Int = 0
    // The index of the contact's _ID value
    var idIndex: Int = 0
    // The lookup key from the Cursor
    var currentLookupKey: String? = null
    // The _ID value from the Cursor
    var currentId: Long = 0
    // A content URI pointing to the contact
    var selectedContactUri: Uri? = null
    ...
    /*
     * Once the user has selected a contact to edit,
     * this gets the contact's lookup key and _ID values from the
     * cursor and creates the necessary URI.
     */
    mCursor?.apply {
        // Gets the lookup key column index
        lookupKeyIndex = getColumnIndex(ContactsContract.Contacts.LOOKUP_KEY)
        // Gets the lookup key value
        currentLookupKey = getString(lookupKeyIndex)
        // Gets the _ID column index
        idIndex = getColumnIndex(ContactsContract.Contacts._ID)
        currentId = getLong(idIndex)
        selectedContactUri = ContactsContract.Contacts.getLookupUri(currentId, mCurrentLookupKey)
    }

    // Creates a new Intent to edit a contact
    val editIntent = Intent(Intent.ACTION_EDIT).apply {
        /*
         * Sets the contact URI to edit, and the data type that the
         * Intent must match
         */
        setDataAndType(selectedContactUri, ContactsContract.Contacts.CONTENT_ITEM_TYPE)
    }
```

### Java

```java
    // The Cursor that contains the Contact row
    public Cursor mCursor;
    // The index of the lookup key column in the cursor
    public int lookupKeyIndex;
    // The index of the contact's _ID value
    public int idIndex;
    // The lookup key from the Cursor
    public String currentLookupKey;
    // The _ID value from the Cursor
    public long currentId;
    // A content URI pointing to the contact
    Uri selectedContactUri;
    ...
    /*
     * Once the user has selected a contact to edit,
     * this gets the contact's lookup key and _ID values from the
     * cursor and creates the necessary URI.
     */
    // Gets the lookup key column index
    lookupKeyIndex = mCursor.getColumnIndex(ContactsContract.Contacts.LOOKUP_KEY);
    // Gets the lookup key value
    currentLookupKey = mCursor.getString(lookupKeyIndex);
    // Gets the _ID column index
    idIndex = mCursor.getColumnIndex(ContactsContract.Contacts._ID);
    currentId = mCursor.getLong(idIndex);
    selectedContactUri =
            Contacts.getLookupUri(currentId, mCurrentLookupKey);
    ...
    // Creates a new Intent to edit a contact
    Intent editIntent = new Intent(Intent.ACTION_EDIT);
    /*
     * Sets the contact URI to edit, and the data type that the
     * Intent must match
     */
    editIntent.setDataAndType(selectedContactUri, ContactsContract.Contacts.CONTENT_ITEM_TYPE);
```

### Add the navigation flag

In Android 4.0 (API version 14) and later, a problem in the contacts app causes incorrect navigation. When your app sends an edit intent to the contacts app, and users edit and save a contact, when they click*Back* they see the contacts list screen. To navigate back to your app, they have to click*Recents*and choose your app.

To work around this problem in Android 4.0.3 (API version 15) and later, add the extended data key`finishActivityOnSaveCompleted`to the intent, with a value of`true`. Android versions prior to Android 4.0 accept this key, but it has no effect. To set the extended data, do the following:  

### Kotlin

```kotlin
    // Sets the special extended data for navigation
    editIntent.putExtra("finishActivityOnSaveCompleted", true)
```

### Java

```java
    // Sets the special extended data for navigation
    editIntent.putExtra("finishActivityOnSaveCompleted", true);
```

### Add other extended data

To add additional extended data to the[Intent](https://developer.android.com/reference/android/content/Intent), call[putExtra()](https://developer.android.com/reference/android/content/Intent#putExtra(java.lang.String, android.os.Bundle))as desired. You can add extended data for common contact fields by using the key values specified in[Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert). Remember that some columns in the[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts)table can't be modified. These columns are listed in the summary section of the API reference for the class[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts)under the heading "Update".

### Send the intent

Finally, send the intent you've constructed. For example:  

### Kotlin

```kotlin
    // Sends the Intent
    startActivity(editIntent)
```

### Java

```java
    // Sends the Intent
    startActivity(editIntent);
```

## Let users choose to insert or edit using an intent

You can allow users to choose whether to insert a contact or edit an existing one by sending an[Intent](https://developer.android.com/reference/android/content/Intent)with the action[ACTION_INSERT_OR_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT_OR_EDIT). For example, an email client app could allow users to add an incoming email address to a new contact, or add it as an additional address for an existing contact. Set the MIME type for this intent to[Contacts.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_ITEM_TYPE), but don't set the data URI.

When you send this intent, the contacts app displays a list of contacts. Users can either insert a new contact or pick an existing contact and edit it. Any extended data fields you add to the intent populates the screen that appears. You can use any of the key values specified in[Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert). The following code snippet shows how to construct and send the intent:  

### Kotlin

```kotlin
    // Creates a new Intent to insert or edit a contact
    val intentInsertEdit = Intent(Intent.ACTION_INSERT_OR_EDIT).apply {
        // Sets the MIME type
        type = ContactsContract.Contacts.CONTENT_ITEM_TYPE
    }
    // Add code here to insert extended data, if desired

    // Sends the Intent with an request ID
    startActivity(intentInsertEdit)
```

### Java

```java
    // Creates a new Intent to insert or edit a contact
    Intent intentInsertEdit = new Intent(Intent.ACTION_INSERT_OR_EDIT);
    // Sets the MIME type
    intentInsertEdit.setType(ContactsContract.Contacts.CONTENT_ITEM_TYPE);
    // Add code here to insert extended data, if desired
    ...
    // Sends the Intent with an request ID
    startActivity(intentInsertEdit);
```