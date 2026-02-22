---
title: https://developer.android.com/work/contacts
url: https://developer.android.com/work/contacts
source: md.txt
---

# Work profile contacts

This developer's guide explains how you can enhance your app to use contact data from the work profile. If you haven't used Android's contacts APIs before, read[Contacts Provider](https://developer.android.com/guide/topics/providers/contacts-provider)to familiarize yourself with the APIs.

## Overview

Devices with[work profiles](https://developer.android.com/work/managed-profiles)store contacts in separate local directories for the work and personal profiles. By default, when an app runs in the personal profile, it doesn't display the work contacts. However, an app can access contact information from the work profile. For example, an app that does this is Google's Android Contacts app which shows both personal and work-directory contacts in search results.

Users often want to use their personal devices and apps for work. By using work-profile contacts, your app can become part of your user's working day.
| **Key Term:** a*personal profile*is another name for the primary user when the device has a work profile. The primary user is the first user set up on the device.

## User experience

Consider how your app might present contact information from the work profile. The best approach depends on the nature of your app and the reason that people use it, but think about the following:

- Should your app include work profile contacts by default or should the user opt-in?
- How will mixing or separating work and personal profile contacts affect the user's flow?
- What is the impact of accidentally tapping a work profile contact?
- What happens to your app's interface when the work profile contacts aren't available?

Your app should clearly indicate a work profile contact. Perhaps you can badge the contact using a familiar work icon---like a briefcase.
![Screenshot showing search results in a list](https://developer.android.com/static/images/work/contacts-app.svg)**Figure 1.**How the Google Contacts app separates work profile contacts

As an example, the Google Contacts app (shown in figure 1) does the following to list a mix of work and personal profile contacts:

1. Inserts a subheader to separate work and personal sections of the list.
2. Badges work contacts with a briefcase icon.
3. Opens a work contact in the work profile when tapped.

If the person using the device turns off the work profile, your app isn't able to look up contact information from the work profile or the organization's remote contact directories. Depending on how you use work-profile contacts, you can silently leave these contacts out or you might need to disable user interface controls.

## Permissions

If your app is already working with the user's contacts, you'll have their[`READ_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)(or possibly[`WRITE_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS)) permission that you requested in your app manifest file. Because the same person uses the personal profile and the work profile, you don't need further permission to access contact data from the work profile.

An IT admin can[block](https://developer.android.com/work/dpc/network-telephony#control_work_contacts_in_the_primary_profile)the work profile sharing contact information with the personal profile. If an IT admin blocks access, your contact searches are returned as empty results. Your app doesn't need to handle specific errors if the user switched off the work profile. The directory content provider continues to return information about the user's work contact directories (see the[Directories](https://developer.android.com/work/contacts#directories)section). To test these permissions, see the[Development and testing](https://developer.android.com/work/contacts#dev-test)section.

## Contact searches

You can get contacts from the work profile using the same APIs and processes that your app uses to get contacts in the personal profile. The enterprise URI for contacts is supported in Android 7.0 (API level 24) or higher. You need to make the following adjustments to the URI:

1. Set the content provider URI to[`Contacts.ENTERPRISE_CONTENT_FILTER_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#ENTERPRISE_CONTENT_FILTER_URI), and supply the contact's name as a query string.
2. Set a contact directory to search. For example,[`ENTERPRISE_DEFAULT`](https://developer.android.com/reference/android/provider/ContactsContract.Directory#ENTERPRISE_DEFAULT)finds contacts in the work profile's local store.

Changing the URI works with any content provider mechanism such as a[`CursorLoader`](https://developer.android.com/reference/androidx/loader/content/CursorLoader)---ideal for loading contact data into user interfaces because data access happens on a worker thread. For simplicity, the examples in this guide call[`ContentResolver.query()`](https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri,%20java.lang.String%5B%5D,%20android.os.Bundle,%20android.os.CancellationSignal)). Here's how you can find contacts in the work profile's local contact directory:  

### Kotlin

```kotlin
// First confirm the device user has given permission for the personal profile.
// There isn't a separate work permission, but an IT admin can block access.
val readContactsPermission =
  ContextCompat.checkSelfPermission(getBaseContext(), Manifest.permission.READ_CONTACTS)
if (readContactsPermission != PackageManager.PERMISSION_GRANTED) {
  return
}

// Fetch Jackie, James, & Jason (and anyone else whose names begin with "ja").
val nameQuery = Uri.encode("ja")

// Build the URI to look up work profile contacts whose name matches. Query
// the default work profile directory which is the locally-stored contacts.
val contentFilterUri =
  ContactsContract.Contacts.ENTERPRISE_CONTENT_FILTER_URI
    .buildUpon()
    .appendPath(nameQuery)
    .appendQueryParameter(
      ContactsContract.DIRECTORY_PARAM_KEY,
      ContactsContract.Directory.ENTERPRISE_DEFAULT.toString()
    )
    .build()

// Query the content provider using the generated URI.
var cursor =
  getContentResolver()
    .query(
      contentFilterUri,
      arrayOf(
        ContactsContract.Contacts._ID,
        ContactsContract.Contacts.LOOKUP_KEY,
        ContactsContract.Contacts.DISPLAY_NAME_PRIMARY
      ),
      null,
      null,
      null
    )

// Print any results found using the work profile contacts' display name.
cursor?.use {
  while (it.moveToNext()) {
    Log.i(TAG, "Work profile contact: ${it.getString(2)}")
  }
}
```

### Java

```java
// First confirm the device user has given permission for the personal profile.
// There isn't a separate work permission, but an IT admin can block access.
int readContactsPermission = ContextCompat.checkSelfPermission(
    getBaseContext(), Manifest.permission.READ_CONTACTS);
if (readContactsPermission != PackageManager.PERMISSION_GRANTED) {
  return;
}

// Fetch Jackie, James, & Jason (and anyone else whose names begin with "ja").
String nameQuery = Uri.encode("ja");

// Build the URI to look up work profile contacts whose name matches. Query
// the default work profile directory which is the locally stored contacts.
Uri contentFilterUri = ContactsContract.Contacts.ENTERPRISE_CONTENT_FILTER_URI
    .buildUpon()
    .appendPath(nameQuery)
    .appendQueryParameter(ContactsContract.DIRECTORY_PARAM_KEY,
        String.valueOf(ContactsContract.Directory.ENTERPRISE_DEFAULT))
    .build();

// Query the content provider using the generated URI.
Cursor cursor = getContentResolver().query(
    contentFilterUri,
    new String[] {
        ContactsContract.Contacts._ID,
        ContactsContract.Contacts.LOOKUP_KEY,
        ContactsContract.Contacts.DISPLAY_NAME_PRIMARY
    },
    null,
    null,
    null);
if (cursor == null) {
  return;
}

// Print any results found using the work profile contacts' display name.
try {
  while (cursor.moveToNext()) {
    Log.i(TAG, "Work profile contact: " + cursor.getString(2));
  }
} finally {
  cursor.close();
}
```

## Directories

Many organizations use remote directories, such as Microsoft Exchange or LDAP, that contain contact information for the entire organization. Your app can help users communicate and share with work colleagues found in their organization's directory. Note that these directories typically contain thousands of contacts, and your app also needs an active network connection to search them. You can use the[`Directory`](https://developer.android.com/reference/android/provider/ContactsContract.Directory)content provider to get the directories used by the user's accounts and find out more about an individual directory.

Query the[`Directory.ENTERPRISE_CONTENT_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Directory#ENTERPRISE_CONTENT_URI)content provider to get directories from the personal profile and the work profile returned together. Searching work-profile directories is supported in Android 7.0 (API level 24) or higher. Your app still needs the user to give[`READ_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)permissions to work with their contact directories.

Because Android stores contact information in different types of local and remote directories, the`Directory`class has methods you can call to find more about a directory:

[`isEnterpriseDirectoryId()`](https://developer.android.com/reference/android/provider/ContactsContract.Directory#isEnterpriseDirectoryId(long))
:   Call this method to find out if the directory is from a work profile account. Remember that the`ENTERPRISE_CONTENT_URI`content provider returns contact directories for the personal and work profile together.

[`isRemoteDirectoryId()`](https://developer.android.com/reference/android/provider/ContactsContract.Directory#isRemoteDirectoryId(long))
:   Call this method to find out if the directory is remote. Remote directories might be enterprise contact stores or could be the user's social networks.

The following example shows how you can use these methods to filter work profile directories:  

### Kotlin

```kotlin
// First, confirm the device user has given READ_CONTACTS permission.
// This permission is still needed for directory listings ...

// Query the content provider to get directories for BOTH the personal and
// work profiles.
val cursor =
  getContentResolver()
    .query(
      ContactsContract.Directory.ENTERPRISE_CONTENT_URI,
      arrayOf(ContactsContract.Directory._ID, ContactsContract.Directory.PACKAGE_NAME),
      null,
      null,
      null
    )

// Print the package name of the work profile's local or remote contact directories.
cursor?.use {
  while (it.moveToNext()) {
    val directoryId = it.getLong(0)
    if (ContactsContract.Directory.isEnterpriseDirectoryId(directoryId)) {
      Log.i(TAG, "Directory: ${it.getString(1)}")
    }
  }
}
```

### Java

```java
// First, confirm the device user has given READ_CONTACTS permission.
// This permission is still needed for directory listings ...

// Query the content provider to get directories for BOTH the personal and
// work profiles.
Cursor cursor = getContentResolver().query(
    ContactsContract.Directory.ENTERPRISE_CONTENT_URI,
    new String[]{
        ContactsContract.Directory._ID,
        ContactsContract.Directory.PACKAGE_NAME
    },
    null,
    null,
    null);
if (cursor == null) {
  return;
}

// Print the package name of the work profile's local or remote contact directories.
try {
  while (cursor.moveToNext()) {
    long directoryId = cursor.getLong(0);

    if (ContactsContract.Directory.isEnterpriseDirectoryId(directoryId)) {
      Log.i(TAG, "Directory: " + cursor.getString(1));
    }
  }
} finally {
  cursor.close();
}
```

The example fetches the ID and package name for the directory. To display a user interface that helps users pick a contact-directory source, you might need to fetch more information about the directory. To see other metadata fields that might be available, read the[`Directory`](https://developer.android.com/reference/android/provider/ContactsContract.Directory)class reference.

## Phone lookups

Apps can query[`PhoneLookup.CONTENT_FILTER_URI`](https://developer.android.com/reference/android/provider/ContactsContract.PhoneLookup#CONTENT_FILTER_URI)to efficiently look up contact data for a telephone number. You can get lookup results from both personal and work profile contacts provider if you replace this URI with[`PhoneLookup.ENTERPRISE_CONTENT_FILTER_URI`](https://developer.android.com/reference/android/provider/ContactsContract.PhoneLookup#ENTERPRISE_CONTENT_FILTER_URI). This work-profile content URI is available in Android 5.0 (API level 21) or higher.

The following example shows an app querying the work-profile content URI to configure the user interface for an incoming call:  

### Kotlin

```kotlin
fun onCreateIncomingConnection(
  connectionManagerPhoneAccount: PhoneAccountHandle,
  request: ConnectionRequest
): Connection {
  var request = request
  // Get the telephone number from the incoming request URI.
  val phoneNumber = this.extractTelephoneNumber(request.address)

  var displayName = "Unknown caller"
  var isCallerInWorkProfile = false

  // Look up contact details for the caller in the personal and work profiles.
  val lookupUri =
    Uri.withAppendedPath(
      ContactsContract.PhoneLookup.ENTERPRISE_CONTENT_FILTER_URI,
      Uri.encode(phoneNumber)
    )
  val cursor =
    getContentResolver()
      .query(
        lookupUri,
        arrayOf(
          ContactsContract.PhoneLookup._ID,
          ContactsContract.PhoneLookup.DISPLAY_NAME,
          ContactsContract.PhoneLookup.CUSTOM_RINGTONE
        ),
        null,
        null,
        null
      )

  // Use the first contact found and check if they're from the work profile.
  cursor?.use {
    if (it.moveToFirst() == true) {
      displayName = it.getString(1)
      isCallerInWorkProfile = ContactsContract.Contacts.isEnterpriseContactId(it.getLong(0))
    }
  }

  // Return a configured connection object for the incoming call.
  val connection = MyAudioConnection()
  connection.setCallerDisplayName(displayName, TelecomManager.PRESENTATION_ALLOWED)

  // Our app's activity uses this value to decide whether to show a work badge.
  connection.setIsCallerInWorkProfile(isCallerInWorkProfile)

  // Configure the connection further ...
  return connection
}
```

### Java

```java
public Connection onCreateIncomingConnection (
    PhoneAccountHandle connectionManagerPhoneAccount, ConnectionRequest request) {
  // Get the telephone number from the incoming request URI.
  String phoneNumber = this.extractTelephoneNumber(request.getAddress());

  String displayName = "Unknown caller";
  boolean isCallerInWorkProfile = false;

  // Look up contact details for the caller in the personal and work profiles.
  Uri lookupUri = Uri.withAppendedPath(
      ContactsContract.PhoneLookup.ENTERPRISE_CONTENT_FILTER_URI,
      Uri.encode(phoneNumber));
  Cursor cursor = getContentResolver().query(
      lookupUri,
      new String[]{
          ContactsContract.PhoneLookup._ID,
          ContactsContract.PhoneLookup.DISPLAY_NAME,
          ContactsContract.PhoneLookup.CUSTOM_RINGTONE
      },
      null,
      null,
      null);

  // Use the first contact found and check if they're from the work profile.
  if (cursor != null) {
    try {
      if (cursor.moveToFirst() == true) {
        displayName = cursor.getString(1);
        isCallerInWorkProfile =
            ContactsContract.Contacts.isEnterpriseContactId(cursor.getLong(0));
      }
    } finally {
      cursor.close();
    }
  }

  // Return a configured connection object for the incoming call.
  MyConnection connection = new MyConnection();
  connection.setCallerDisplayName(displayName, TelecomManager.PRESENTATION_ALLOWED);

  // Our app's activity uses this value to decide whether to show a work badge.
  connection.setIsCallerInWorkProfile(isCallerInWorkProfile);

  // Configure the connection further ...
  return connection;
}
```

## Email lookups

Your app can get personal or work contact data for an email address by querying[`Email.ENTERPRISE_CONTENT_LOOKUP_URI`](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#ENTERPRISE_CONTENT_LOOKUP_URI). Querying this URL first searches the personal contacts for an exact match. If the provider doesn't match any personal contacts, the provider then searches work contacts for a match. This URI is available in Android 6.0 (API level 23) or higher.

Here's how you can look up contact information for an email address:  

### Kotlin

```kotlin
// Build the URI to look up contacts from the personal and work profiles that
// are an exact (case-insensitive) match for the email address.
val emailAddress = "somebody@example.com"
val contentFilterUri =
  Uri.withAppendedPath(
    ContactsContract.CommonDataKinds.Email.ENTERPRISE_CONTENT_LOOKUP_URI,
    Uri.encode(emailAddress)
  )

// Query the content provider to first try to match personal contacts and,
// if none are found, then try to match the work contacts.
val cursor =
  contentResolver.query(
    contentFilterUri,
    arrayOf(
      ContactsContract.CommonDataKinds.Email.CONTACT_ID,
      ContactsContract.CommonDataKinds.Email.ADDRESS,
      ContactsContract.Contacts.DISPLAY_NAME
    ),
    null,
    null,
    null
  )
    ?: return

// Print the name of the matching contact. If we want to work-badge contacts,
// we can call ContactsContract.Contacts.isEnterpriseContactId() with the ID.
cursor.use {
  while (it.moveToNext()) {
    Log.i(TAG, "Matching contact: ${it.getString(2)}")
  }
}
```

### Java

```java
// Build the URI to look up contacts from the personal and work profiles that
// are an exact (case-insensitive) match for the email address.
String emailAddress = "somebody@example.com";
Uri contentFilterUri = Uri.withAppendedPath(
    ContactsContract.CommonDataKinds.Email.ENTERPRISE_CONTENT_LOOKUP_URI,
    Uri.encode(emailAddress));

// Query the content provider to first try to match personal contacts and,
// if none are found, then try to match the work contacts.
Cursor cursor = getContentResolver().query(
    contentFilterUri,
    new String[]{
        ContactsContract.CommonDataKinds.Email.CONTACT_ID,
        ContactsContract.CommonDataKinds.Email.ADDRESS,
        ContactsContract.Contacts.DISPLAY_NAME
    },
    null,
    null,
    null);
if (cursor == null) {
  return;
}

// Print the name of the matching contact. If we want to work-badge contacts,
// we can call ContactsContract.Contacts.isEnterpriseContactId() with the ID.
try {
  while (cursor.moveToNext()) {
    Log.i(TAG, "Matching contact: " + cursor.getString(2));
  }
} finally {
  cursor.close();
}
```

## Show a work contact

Apps running in the personal profile can show a contact card in the work profile. Call[`ContactsContract.QuickContact.showQuickContact()`](https://developer.android.com/reference/android/provider/ContactsContract.QuickContact#showQuickContact(android.content.Context,%20android.graphics.Rect,%20android.net.Uri,%20int,%20java.lang.String%5B%5D))in Android 5.0 or higher to launch the Contacts app in the work profile and show the contact's card.

To generate a correct URI for the work profile, you need to call[`ContactsContract.Contacts.getLookupUri()`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#getLookupUri(long,%20java.lang.String))and pass a contact ID and lookup key. The following example shows how you can get the URI and then show the card:  

### Kotlin

```kotlin
// Query the content provider using the ENTERPRISE_CONTENT_FILTER_URI address.
// We use the _ID and LOOKUP_KEY columns to generate a work-profile URI.
val cursor =
  getContentResolver()
    .query(
      contentFilterUri,
      arrayOf(ContactsContract.Contacts._ID, ContactsContract.Contacts.LOOKUP_KEY),
      null,
      null
    )

// Show the contact details card in the work profile's Contacts app. The URI
// must be created with getLookupUri().
cursor?.use {
  if (it.moveToFirst() == true) {
    val uri = ContactsContract.Contacts.getLookupUri(it.getLong(0), it.getString(1))
    ContactsContract.QuickContact.showQuickContact(
      activity,
      Rect(20, 20, 100, 100),
      uri,
      ContactsContract.QuickContact.MODE_LARGE,
      null
    )
  }
}
```

### Java

```java
// Query the content provider using the ENTERPRISE_CONTENT_FILTER_URI address.
// We use the _ID and LOOKUP_KEY columns to generate a work-profile URI.
Cursor cursor = getContentResolver().query(
    contentFilterUri,
    new String[] {
        ContactsContract.Contacts._ID,
        ContactsContract.Contacts.LOOKUP_KEY,
    },
    null,
    null,
    null);
if (cursor == null) {
  return;
}

// Show the contact details card in the work profile's Contacts app. The URI
// must be created with getLookupUri().
try {
  if (cursor.moveToFirst() == true) {
    Uri uri = ContactsContract.Contacts.getLookupUri(
        cursor.getLong(0), cursor.getString(1));
    ContactsContract.QuickContact.showQuickContact(
        getActivity(),
        new Rect(20, 20, 100, 100),
        uri,
        ContactsContract.QuickContact.MODE_LARGE,
        null);
  }
} finally {
  cursor.close();
}
```

## Availability

The following table summarizes which Android versions support work profile contact data in the personal profile:

|  Android version   |                                                                                                                                                                                                             Support                                                                                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5.0 (API level 21) | Look up work contact names for telephone numbers using[`PhoneLookup.ENTERPRISE_CONTENT_FILTER_URI`](https://developer.android.com/reference/android/provider/ContactsContract.PhoneLookup#ENTERPRISE_CONTENT_FILTER_URI).                                                                                                                                                                                                       |
| 6.0 (API level 23) | Look up work contact names for email addresses using[`Email.ENTERPRISE_CONTENT_LOOKUP_URI`](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#ENTERPRISE_CONTENT_LOOKUP_URI).                                                                                                                                                                                                     |
| 7.0 (API level 24) | Query work contact names from work directories using[`Contacts.ENTERPRISE_CONTENT_FILTER_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#ENTERPRISE_CONTENT_FILTER_URI). List all directories in the work and personal profiles using[`Directory.ENTERPRISE_CONTENT_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Directory#ENTERPRISE_CONTENT_URI). |

## Development and testing

To create a work profile, follow these steps:

1. Install our[Test DPC](https://play.google.com/store/apps/details?id=com.afwsamples.testdpc)app.
2. Open the**Set up Test DPC**app (not the Test DPC app icon).
3. Follow the on-screen instructions to set up a managed profile.
4. In the work profile, open the**Contacts**app and add some sample contacts.

To simulate an IT admin blocking access to work profile contacts, follow these steps:

1. In the work profile, open the**Test DPC**app.
2. Search for the*Disable cross-profile contacts search* setting or the*Disable cross-profile caller ID*setting.
3. Switch the setting to**On**.

To learn more about testing your app with work profiles, read[Test your App for Compatibility with Work Profiles](https://developer.android.com/work/managed-profiles#testing_apps).

## Additional resources

To learn more about contacts or the work profile, see these resources:

- [Work profiles](https://developer.android.com/work/managed-profiles)contains more best practices for work profiles.
- [Retrieve a list of contacts](https://developer.android.com/training/contacts-provider/retrieve-names)walks through the steps needed to list contacts in an app.
- [Contacts Provider](https://developer.android.com/guide/topics/providers/contacts-provider)explains the structure of the contacts database.