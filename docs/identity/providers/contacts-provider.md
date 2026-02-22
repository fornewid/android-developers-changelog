---
title: https://developer.android.com/identity/providers/contacts-provider
url: https://developer.android.com/identity/providers/contacts-provider
source: md.txt
---

The Contacts Provider is a powerful and flexible Android component that manages the
device's central repository of data about people. The Contacts Provider is the source of data
you see in the device's contacts application, and you can also access its data in your own
application and transfer data between the device and online services. The provider accommodates
a wide range of data sources and tries to manage as much data as possible for each person, with
the result that its organization is complex. Because of this, the provider's API includes an
extensive set of contract classes and interfaces that facilitate both data retrieval and
modification.


This guide describes the following:

- The basic provider structure.
- How to retrieve data from the provider.
- How to modify data in the provider.
- How to write a sync adapter for synchronizing data from your server to the Contacts Provider.


This guide assumes that you know the basics of Android content providers. To learn more
about Android content providers, read the
[Content Provider basics](https://developer.android.com/guide/topics/providers/content-provider-basics) guide.

## Contacts Provider organization


The Contacts Provider is an Android content provider component. It maintains three types of
data about a person, each of which corresponds to a table offered by the provider, as
illustrated in figure 1:
![](https://developer.android.com/static/images/providers/contacts_structure.png)


**Figure 1.** Contacts Provider table structure.


The three tables are commonly referred to by the names of their contract classes. The classes
define constants for content URIs, column names, and column values used by the tables:


[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts) table
:
    Rows representing different people, based on aggregations of raw contact rows.


[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) table
:
    Rows containing a summary of a person's data, specific to a user account and type.


[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table
:
    Rows containing the details for raw contact, such as email addresses or phone numbers.


The other tables represented by contract classes in [ContactsContract](https://developer.android.com/reference/android/provider/ContactsContract)
are auxiliary tables that the Contacts Provider uses to manage its operations or support
specific functions in the device's contacts or telephony applications.

## Raw contacts


A raw contact represents a person's data coming from a single account type and account
name. Because the Contacts Provider allows more than one online service as the source of
data for a person, the Contacts Provider allows multiple raw contacts for the same person.
Multiple raw contacts also allow a user to combine a person's data from more than one account
from the same account type.


Most of the data for a raw contact isn't stored in the
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) table. Instead, it's stored in one or more
rows in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table. Each data row has a column
[Data.RAW_CONTACT_ID](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#RAW_CONTACT_ID) that
contains the [RawContacts._ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) value of its
parent [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row.

### Important raw contact columns


The important columns in the [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) table are
listed in table 1. Please read the notes that follow after the table:


**Table 1.** Important raw contact columns.

| Column name | Use | Notes |
|---|---|---|
| [ACCOUNT_NAME](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#ACCOUNT_NAME) | The account name for the account type that's the source of this raw contact. For example, the account name of a Google Account is one of the device owner's Gmail addresses. See the next entry for [ACCOUNT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#ACCOUNT_TYPE) for more information. | The format of this name is specific to its account type. It is not necessarily an email address. |
| [ACCOUNT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#ACCOUNT_TYPE) | The account type that's the source of this raw contact. For example, the account type of a Google Account is `com.google`. Always qualify your account type with a domain identifier for a domain you own or control. This will ensure that your account type is unique. | An account type that offers contacts data usually has an associated sync adapter that synchronizes with the Contacts Provider. |
| [DELETED](https://developer.android.com/reference/android/provider/ContactsContract.RawContactsColumns#DELETED) | The "deleted" flag for a raw contact. | This flag allows the Contacts Provider to maintain the row internally until sync adapters are able to delete the row from their servers and then finally delete the row from the repository. |

#### Notes


The following are important notes about the
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) table:

- A raw contact's name is not stored in its row in [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts). Instead, it's stored in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table, in a [ContactsContract.CommonDataKinds.StructuredName](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredName) row. A raw contact has only one row of this type in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table.
- **Caution:** To use your own account data in a raw contact row, it must first be registered with the [AccountManager](https://developer.android.com/reference/android/accounts/AccountManager). To do this, prompt users to add the account type and their account name to the list of accounts. If you don't do this, the Contacts Provider will automatically delete your raw contact row.


  For example, if you want your app to maintain contacts data for your web-based service
  with the domain `com.example.dataservice`, and the user's account for your service
  is `becky.sharp@dataservice.example.com`, the user must first add the account
  "type" (`com.example.dataservice`) and account "name"
  (`becky.smart@dataservice.example.com`) before your app can add raw contact rows.
  You can explain this requirement to the user in documentation, or you can prompt the
  user to add the type and name, or both. Account types and account names
  are described in more detail in the next section.

### Sources of raw contacts data


To understand how raw contacts work, consider the user "Emily Dickinson" who has the following
three user accounts defined on her device:

- `emily.dickinson@gmail.com`
- `emilyd@gmail.com`
- Twitter account "belle_of_amherst"


This user has enabled *Sync Contacts* for all three of these accounts in the
*Accounts* settings.


Suppose Emily Dickinson opens a browser window, logs into Gmail as
`emily.dickinson@gmail.com`, opens
Contacts, and adds "Thomas Higginson". Later on, she logs into Gmail as
`emilyd@gmail.com` and sends an email to "Thomas Higginson", which automatically
adds him as a contact. She also follows "colonel_tom" (Thomas Higginson's Twitter ID) on
Twitter.


The Contacts Provider creates three raw contacts as a result of this work:

1. A raw contact for "Thomas Higginson" associated with `emily.dickinson@gmail.com`. The user account type is Google.
2. A second raw contact for "Thomas Higginson" associated with `emilyd@gmail.com`. The user account type is also Google. There is a second raw contact even though the name is identical to a previous name, because the person was added for a different user account.
3. A third raw contact for "Thomas Higginson" associated with "belle_of_amherst". The user account type is Twitter.

## Data


As noted previously, the data for a raw contact is stored in a
[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) row that is linked to the raw contact's
`_ID` value. This allows a single raw contact to have multiple instances of the same
type of data such as email addresses or phone numbers. For example, if
"Thomas Higginson" for `emilyd@gmail.com` (the raw contact row for Thomas Higginson
associated with the Google Account `emilyd@gmail.com`) has a home email address of
`thigg@gmail.com` and a work email address of
`thomas.higginson@gmail.com`, the Contacts Provider stores the two email address
rows and links them both to the raw contact.


Notice that different types of data are stored in this single table. Display name,
phone number, email, postal address, photo, and website detail rows are all found in the
[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table. To help manage this, the
[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table has some columns with descriptive names,
and others with generic names. The contents of a descriptive-name column have the same meaning
regardless of the type of data in the row, while the contents of a generic-name column have
different meanings depending on the type of data.

### Descriptive column names


Some examples of descriptive column names are:


[RAW_CONTACT_ID](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#RAW_CONTACT_ID)
:
    The value of the `_ID` column of the raw contact for this data.


[MIMETYPE](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#MIMETYPE)
:
    The type of data stored in this row, expressed as a custom MIME type. The Contacts Provider
    uses the MIME types defined in the subclasses of
    [ContactsContract.CommonDataKinds](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds). These MIME types are open source,
    and can be used by any application or sync adapter that works with the Contacts Provider.


[IS_PRIMARY](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#IS_PRIMARY)
:
    If this type of data row can occur more than once for a raw contact, the
    [IS_PRIMARY](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#IS_PRIMARY) column flags
    the data row that contains the primary data for the type. For example, if
    the user long-presses a phone number for a contact and selects **Set default** ,
    then the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) row containing that number
    has its [IS_PRIMARY](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#IS_PRIMARY) column set to a
    non-zero value.

### Generic column names


There are 15 generic columns named `DATA1` through
`DATA15` that are generally available and an additional four generic
columns `SYNC1` through `SYNC4` that should only be used by sync
adapters. The generic column name constants always work, regardless of the type of
data the row contains.


The `DATA1` column is indexed. The Contacts Provider always uses this column for
the data that the provider expects will be the most frequent target of a query. For example,
in an email row, this column contains the actual email address.


By convention, the column `DATA15` is reserved for storing Binary Large Object
(BLOB) data such as photo thumbnails.

### Type-specific column names


To facilitate working with the columns for a particular type of row, the Contacts Provider
also provides type-specific column name constants, defined in subclasses of
[ContactsContract.CommonDataKinds](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds). The constants simply give a
different constant name to the same column name, which helps you access data in a row of a
particular type.


For example, the [ContactsContract.CommonDataKinds.Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email) class defines
type-specific column name constants for a [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) row
that has the MIME type
[Email.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_ITEM_TYPE). The class contains the constant
[ADDRESS](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#ADDRESS) for the email address
column. The actual value of
[ADDRESS](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#ADDRESS) is "data1", which is
the same as the column's generic name.


**Caution:** Don't add your own custom data to the
[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table using a row that has one of the
provider's pre-defined MIME types. If you do, you may lose the data or cause the provider to
malfunction. For example, you should not add a row with the MIME type
[Email.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_ITEM_TYPE) that contains a user name instead of an email address in the
column `DATA1`. If you use your own custom MIME type for the row, then you are free
to define your own type-specific column names and use the columns however you wish.


Figure 2 shows how descriptive columns and data columns appear in a
[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) row, and how type-specific column names "overlay"
the generic column names
![How type-specific column names map to generic column names](https://developer.android.com/static/images/providers/data_columns.png)


**Figure 2.** Type-specific column names and generic column names.

### Type-specific column name classes


Table 2 lists the most commonly-used type-specific column name classes:


**Table 2.** Type-specific column name classes

| Mapping class | Type of data | Notes |
|---|---|---|
| [ContactsContract.CommonDataKinds.StructuredName](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredName) | The name data for the raw contact associated with this data row. | A raw contact has only one of these rows. |
| [ContactsContract.CommonDataKinds.Photo](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Photo) | The main photo for the raw contact associated with this data row. | A raw contact has only one of these rows. |
| [ContactsContract.CommonDataKinds.Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email) | An email address for the raw contact associated with this data row. | A raw contact can have multiple email addresses. |
| [ContactsContract.CommonDataKinds.StructuredPostal](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredPostal) | A postal address for the raw contact associated with this data row. | A raw contact can have multiple postal addresses. |
| [ContactsContract.CommonDataKinds.GroupMembership](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.GroupMembership) | An identifier that links the raw contact to one of the groups in the Contacts Provider. | Groups are an optional feature of an account type and account name. They're described in more detail in the section [Contact groups](https://developer.android.com/identity/providers/contacts-provider#Groups). |

### Contacts


The Contacts Provider combines the raw contact rows across all account types and account names
to form a **contact**. This facilitates displaying and modifying all the data a
user has collected for a person. The Contacts Provider manages the creation of new contact
rows, and the aggregation of raw contacts with an existing contact row. Neither applications nor
sync adapters are allowed to add contacts, and some columns in a contact row are read-only.


**Note:** If you try to add a contact to the Contacts Provider with an
[insert()](https://developer.android.com/reference/android/content/ContentResolver#insert(android.net.Uri, android.content.ContentValues)), you'll get
an [UnsupportedOperationException](https://developer.android.com/reference/java/lang/UnsupportedOperationException) exception. If you try to update a column
that's listed as "read-only," the update is ignored.


The Contacts Provider creates a new contact in response to the addition of a new raw contact
that doesn't match any existing contacts. The provider also does this if an existing raw
contact's data changes in such a way that it no longer matches the contact to which it was
previously attached. If an application or sync adapter creates a new raw contact that
*does* match an existing contact, the new raw contact is aggregated to the existing
contact.


The Contacts Provider links a contact row to its raw contact rows with the contact row's
`_ID` column in the [Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts)
table. The `CONTACT_ID` column of the raw contacts table
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) contains `_ID` values for
the contacts row associated with each raw contacts row.


The [ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts) table also has the column
[LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY) that is a
"permanent" link to the contact row. Because the Contacts Provider maintains contacts
automatically, it may change a contact row's [_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) value
in response to an aggregation or sync. Even If this happens, the content URI
[CONTENT_LOOKUP_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_LOOKUP_URI) combined with
contact's [LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY) will still
point to the contact row, so you can use
[LOOKUP_KEY](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#LOOKUP_KEY)
to maintain links to "favorite" contacts, and so forth. This column has its own format that is
unrelated to the format of the [_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) column.


Figure 3 shows how the three main tables relate to each other.
![Contacts provider main tables](https://developer.android.com/static/images/providers/contacts_tables.png)


**Figure 3.** Contacts, Raw Contacts, and Details table relationships.  

**Caution:**If you publish your app to the Google Play Store, or if your
app is on a device running Android 10 (API level 29) or higher, keep in mind
that a limited set of contacts data fields and methods are obsolete.


Under the conditions mentioned, the system periodically clears any values
written to these data fields:

- [`ContactsContract.ContactOptionsColumns.LAST_TIME_CONTACTED`](https://developer.android.com/reference/android/provider/ContactsContract.ContactOptionsColumns#LAST_TIME_CONTACTED)
- [`ContactsContract.ContactOptionsColumns.TIMES_CONTACTED`](https://developer.android.com/reference/android/provider/ContactsContract.ContactOptionsColumns#TIMES_CONTACTED)
- [`ContactsContract.DataUsageStatColumns.LAST_TIME_USED`](https://developer.android.com/reference/android/provider/ContactsContract.DataUsageStatColumns#LAST_TIME_USED)
- [`ContactsContract.DataUsageStatColumns.TIMES_USED`](https://developer.android.com/reference/android/provider/ContactsContract.DataUsageStatColumns#TIMES_USED)


APIs used to set the above data fields are also obsolete:

- [`ContactsContract.Contacts.markAsContacted()`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#markAsContacted(android.content.ContentResolver,%20long))
- [`ContactsContract.DataUsageFeedback`](https://developer.android.com/reference/android/provider/ContactsContract.DataUsageFeedback)


In addition, the following fields no longer return frequent contacts. Note
that some of these fields influence rankings of contacts only when the
contacts are part of a specific
[data
kind](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds).

- [`ContactsContract.Contacts.CONTENT_FREQUENT_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_FREQUENT_URI)
- [`ContactsContract.Contacts.CONTENT_STREQUENT_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_STREQUENT_URI)
- [`ContactsContract.Contacts.CONTENT_STREQUENT_FILTER_URI`](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_STREQUENT_FILTER_URI)
- `CONTENT_FILTER_URI` (affects only [Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_FILTER_URI), [Phone](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Phone#CONTENT_FILTER_URI), [Callable](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Callable#CONTENT_FILTER_URI), and [Contactables](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Contactables#CONTENT_FILTER_URI) data kinds)
- `ENTERPRISE_CONTENT_FILTER_URI` (affects only [Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#ENTERPRISE_CONTENT_FILTER_URI), [Phone](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Phone#ENTERPRISE_CONTENT_FILTER_URI), and [Callable](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Callable#ENTERPRISE_CONTENT_FILTER_URI) data kinds)


If your apps are accessing or updating these fields or APIs, use alternative
methods. For example, you can fulfill certain use cases by using
[private
content providers](https://developer.android.com/guide/topics/providers/content-provider-creating) or other data stored within your app or backend
systems.


To verify that your app's functionality isn't affected by this change, you
can manually clear these data fields. To do so, run the following ADB
command on a device running Android 4.1 (API level 16) or higher:  

```bash
adb shell content delete \
--uri content://com.android.contacts/contacts/delete_usage
```

## Data From sync adapters


Users enter contacts data directly into the device, but data also flows into the Contacts
Provider from web services via **sync adapters** , which automate
the transfer of data between the device and services. Sync adapters run in the background
under the control of the system, and they call [ContentResolver](https://developer.android.com/reference/android/content/ContentResolver) methods
to manage data.


In Android, the web service that a sync adapter works with is identified by an account type.
Each sync adapter works with one account type, but it can support multiple account names for
that type. Account types and account names are described briefly in the section
[Sources of raw contacts data](https://developer.android.com/identity/providers/contacts-provider#RawContactsExample). The following definitions offer
more detail, and describe how account type and name relate to sync adapters and services.


Account type
:
    Identifies a service in which the user has stored data. Most of the time, the user has to
    authenticate with the service. For example, Google Contacts is an account type, identified
    by the code `google.com`. This value corresponds to the account type used by
    [AccountManager](https://developer.android.com/reference/android/accounts/AccountManager).


Account name
:
    Identifies a particular account or login for an account type. Google Contacts accounts
    are the same as Google Accounts, which have an email address as an account name.
    Other services may use a single-word username or numeric id.


Account types don't have to be unique. A user can configure multiple Google Contacts accounts
and download their data to the Contacts Provider; this may happen if the user has one set of
personal contacts for a personal account name, and another set for work. Account names are
usually unique. Together, they identify a specific data flow between the Contacts Provider and
an external service.


If you want to transfer your service's data to the Contacts Provider, you need to write your
own sync adapter. This is described in more detail in the section
[Contacts Provider sync adapters](https://developer.android.com/identity/providers/contacts-provider#SyncAdapters).


Figure 4 shows how the Contacts Provider fits into the flow of data
about people. In the box marked "sync adapters," each adapter is labeled by its account type.
![Flow of data about people](https://developer.android.com/static/images/providers/ContactsDataFlow.png)


**Figure 4.** The Contacts Provider flow of data.

## Required permissions


Applications that want to access the Contacts Provider must request the following
permissions:

Read access to one or more tables
:
    [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS), specified in
    `AndroidManifest.xml` with the
    [<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element) element as
    `<uses-permission android:name="android.permission.READ_CONTACTS">`.

Write access to one or more tables
:
    [WRITE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS), specified in
    `AndroidManifest.xml` with the
    [<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element) element as
    `<uses-permission android:name="android.permission.WRITE_CONTACTS">`.


These permissions do not extend to the user profile data. The user profile and its
required permissions are discussed in the following section,
[The user profile](https://developer.android.com/identity/providers/contacts-provider#UserProfile).


Remember that the user's contacts data is personal and sensitive. Users are concerned about
their privacy, so they don't want applications collecting data about them or their contacts.
If it's not obvious why you need permission to access their contacts data, they may give
your application low ratings or simply refuse to install it.

## The user profile


The [ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts) table has a single row containing
profile data for the device's user. This data describes the device's `user` rather
than one of the user's contacts. The profile contacts row is linked to a raw
contacts row for each system that uses a profile.
Each profile raw contact row can have multiple data rows. Constants for accessing the user
profile are available in the [ContactsContract.Profile](https://developer.android.com/reference/android/provider/ContactsContract.Profile) class.


Access to the user profile requires special permissions. In addition to the
[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) and
[WRITE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS) permissions needed to read and write, access
to the user profile requires the android.Manifest.permission#READ_PROFILE and
android.Manifest.permission#WRITE_PROFILE permissions for read and write access,
respectively.


Remember that you should consider a user's profile to be sensitive. The permission
android.Manifest.permission#READ_PROFILE allows you to access the device user's
personally-identifying data. Make sure to tell the user why
you need user profile access permissions in the description of your application.


To retrieve the contact row that contains the user's profile,
call [ContentResolver.query()](https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String)). Set the content URI to
[CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.Profile#CONTENT_URI) and don't provide any
selection criteria. You can also use this content URI as the base URI for retrieving raw
contacts or data for the profile. For example, this snippet retrieves data for the profile:  

### Kotlin

```kotlin
// Sets the columns to retrieve for the user profile
projection = arrayOf(
        ContactsContract.Profile._ID,
        ContactsContract.Profile.DISPLAY_NAME_PRIMARY,
        ContactsContract.Profile.LOOKUP_KEY,
        ContactsContract.Profile.PHOTO_THUMBNAIL_URI
)

// Retrieves the profile from the Contacts Provider
profileCursor = contentResolver.query(
        ContactsContract.Profile.CONTENT_URI,
        projection,
        null,
        null,
        null
)
```

### Java

```java
// Sets the columns to retrieve for the user profile
projection = new String[]
    {
        Profile._ID,
        Profile.DISPLAY_NAME_PRIMARY,
        Profile.LOOKUP_KEY,
        Profile.PHOTO_THUMBNAIL_URI
    };

// Retrieves the profile from the Contacts Provider
profileCursor =
        getContentResolver().query(
                Profile.CONTENT_URI,
                projection ,
                null,
                null,
                null);
```


**Note:** If you retrieve multiple contact rows, and you want to determine if one of them
is the user profile, test the row's
[IS_USER_PROFILE](https://developer.android.com/reference/android/provider/ContactsContract.ContactsColumns#IS_USER_PROFILE) column. This column
is set to "1" if the contact is the user profile.

## Contacts Provider metadata


The Contacts Provider manages data that keeps track of the state of contacts data in the
repository. This metadata about the repository is stored in various places, including the
Raw Contacts, Data, and Contacts table rows, the
[ContactsContract.Settings](https://developer.android.com/reference/android/provider/ContactsContract.Settings) table, and the
[ContactsContract.SyncState](https://developer.android.com/reference/android/provider/ContactsContract.SyncState) table. The following table shows the
effect of each of these pieces of metadata:


**Table 3.** Metadata in the Contacts Provider

| Table | Column | Values | Meaning |
|---|---|---|---|
| [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) | [DIRTY](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#DIRTY) | "0" - not changed since the last sync. | Marks raw contacts that were changed on the device and have to be synced back to the server. The value is set automatically by the Contacts Provider when Android applications update a row. Sync adapters that modify the raw contact or data tables should always append the string [CALLER_IS_SYNCADAPTER](https://developer.android.com/reference/android/provider/ContactsContract#CALLER_IS_SYNCADAPTER) to the content URI they use. This prevents the provider from marking rows as dirty. Otherwise, sync adapter modifications appear to be local modifications and are sent to the server, even though the server was the source of the modification. |
| [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) | [DIRTY](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#DIRTY) | "1" - changed since last sync, needs to be synced back to the server. | Marks raw contacts that were changed on the device and have to be synced back to the server. The value is set automatically by the Contacts Provider when Android applications update a row. Sync adapters that modify the raw contact or data tables should always append the string [CALLER_IS_SYNCADAPTER](https://developer.android.com/reference/android/provider/ContactsContract#CALLER_IS_SYNCADAPTER) to the content URI they use. This prevents the provider from marking rows as dirty. Otherwise, sync adapter modifications appear to be local modifications and are sent to the server, even though the server was the source of the modification. |
| [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) | [VERSION](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#VERSION) | The version number of this row. | The Contacts Provider automatically increments this value whenever the row or its related data changes. |
| [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) | [DATA_VERSION](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#DATA_VERSION) | The version number of this row. | The Contacts Provider automatically increments this value whenever the data row is changed. |
| [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) | [SOURCE_ID](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#SOURCE_ID) | A string value that uniquely identifies this raw contact to the account in which it was created. | When a sync adapter creates a new raw contact, this column should be set to the server's unique ID for the raw contact. When an Android application creates a new raw contact, the application should leave this column empty. This signals the sync adapter that it should create a new raw contact on the server, and get a value for the [SOURCE_ID](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#SOURCE_ID). In particular, the source id must be **unique** for each account type and should be stable across syncs: - Unique: Each raw contact for an account must have its own source id. If you don't enforce this, you'll cause problems in the contacts application. Notice that two raw contacts for the same account *type* may have the same source id. For example, the raw contact "Thomas Higginson" for the account `emily.dickinson@gmail.com` is allowed to have the same source id as the raw contact "Thomas Higginson" for the account `emilyd@gmail.com`. - Stable: Source ids are a permanent part of the online service's data for the raw contact. For example, if the user clears Contacts Storage from the Apps settings and re-syncs, the restored raw contacts should have the same source ids as before. If you don't enforce this, shortcuts will stop working. |
| [ContactsContract.Groups](https://developer.android.com/reference/android/provider/ContactsContract.Groups) | [GROUP_VISIBLE](https://developer.android.com/reference/android/provider/ContactsContract.GroupsColumns#GROUP_VISIBLE) | "0" - Contacts in this group should not be visible in Android application UIs. | This column is for compatibility with servers that allow a user to hide contacts in certain groups. |
| [ContactsContract.Groups](https://developer.android.com/reference/android/provider/ContactsContract.Groups) | [GROUP_VISIBLE](https://developer.android.com/reference/android/provider/ContactsContract.GroupsColumns#GROUP_VISIBLE) | "1" - Contacts in this group are allowed to be visible in application UIs. | This column is for compatibility with servers that allow a user to hide contacts in certain groups. |
| [ContactsContract.Settings](https://developer.android.com/reference/android/provider/ContactsContract.Settings) | [UNGROUPED_VISIBLE](https://developer.android.com/reference/android/provider/ContactsContract.SettingsColumns#UNGROUPED_VISIBLE) | "0" - For this account and account type, contacts that don't belong to a group are invisible to Android application UIs. | By default, contacts are invisible if none of their raw contacts belongs to a group (Group membership for a raw contact is indicated by one or more [ContactsContract.CommonDataKinds.GroupMembership](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.GroupMembership) rows in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table). By setting this flag in the [ContactsContract.Settings](https://developer.android.com/reference/android/provider/ContactsContract.Settings) table row for an account type and account, you can force contacts without groups to be visible. One use of this flag is to show contacts from servers that don't use groups. |
| [ContactsContract.Settings](https://developer.android.com/reference/android/provider/ContactsContract.Settings) | [UNGROUPED_VISIBLE](https://developer.android.com/reference/android/provider/ContactsContract.SettingsColumns#UNGROUPED_VISIBLE) | "1" - For this account and account type, contacts that don't belong to a group are visible to application UIs. | By default, contacts are invisible if none of their raw contacts belongs to a group (Group membership for a raw contact is indicated by one or more [ContactsContract.CommonDataKinds.GroupMembership](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.GroupMembership) rows in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table). By setting this flag in the [ContactsContract.Settings](https://developer.android.com/reference/android/provider/ContactsContract.Settings) table row for an account type and account, you can force contacts without groups to be visible. One use of this flag is to show contacts from servers that don't use groups. |
| [ContactsContract.SyncState](https://developer.android.com/reference/android/provider/ContactsContract.SyncState) | (all) | Use this table to store metadata for your sync adapter. | With this table you can store sync state and other sync-related data persistently on the device. |

## Contacts Provider access


This section describes guidelines for accessing data from the Contacts Provider, focusing on
the following:

- Entity queries.
- Batch modification.
- Retrieval and modification with intents.
- Data integrity.


Making modifications from a sync adapter is also covered in more detail in the section
[Contacts Provider sync adapters](https://developer.android.com/identity/providers/contacts-provider#SyncAdapters).

### Querying entities


Because the Contacts Provider tables are organized in a hierarchy, it's often useful to
retrieve a row and all of the "child" rows that are linked to it. For example, to display
all the information for a person, you may want to retrieve all the
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) rows for a single
[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts) row, or all the
[ContactsContract.CommonDataKinds.Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email) rows for a single
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row. To facilitate this, the Contacts
Provider offers **entity** constructs, which act like database joins between
tables.


An entity is like a table composed of selected columns from a parent table and its child table.
When you query an entity, you supply a projection and search criteria based on the columns
available from the entity. The result is a [Cursor](https://developer.android.com/reference/android/database/Cursor) that contains
one row for each child table row that was retrieved. For example, if you query
[ContactsContract.Contacts.Entity](https://developer.android.com/reference/android/provider/ContactsContract.Contacts.Entity) for a contact name
and all the [ContactsContract.CommonDataKinds.Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email) rows for all the
raw contacts for that name, you get back a [Cursor](https://developer.android.com/reference/android/database/Cursor) containing one row
for each [ContactsContract.CommonDataKinds.Email](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email) row.


Entities simplify queries. Using an entity, you can retrieve all of the contacts data for a
contact or raw contact at once, instead of having to query the parent table first to get an
ID, and then having to query the child table with that ID. Also, the Contacts Provider processes
a query against an entity in a single transaction, which ensures that the retrieved data is
internally consistent.


**Note:** An entity usually doesn't contain all the columns of the parent and
child table. If you attempt to work with a column name that isn't in the list of column name
constants for the entity, you'll get an [Exception](https://developer.android.com/reference/java/lang/Exception).


The following snippet shows how to retrieve all the raw contact rows for a contact. The snippet
is part of a larger application that has two activities, "main" and "detail". The main activity
shows a list of contact rows; when the user select one, the activity sends its ID to the detail
activity. The detail activity uses the [ContactsContract.Contacts.Entity](https://developer.android.com/reference/android/provider/ContactsContract.Contacts.Entity)
to display all of the data rows from all of the raw contacts associated with the selected
contact.


This snippet is taken from the "detail" activity:  

### Kotlin

```kotlin
...
    /*
     * Appends the entity path to the URI. In the case of the Contacts Provider, the
     * expected URI is content://com.google.contacts/#/entity (# is the ID value).
     */
    contactUri = Uri.withAppendedPath(
            contactUri,
            ContactsContract.Contacts.Entity.CONTENT_DIRECTORY
    )

    // Initializes the loader identified by LOADER_ID.
    loaderManager.initLoader(
            LOADER_ID,  // The identifier of the loader to initialize
            null,       // Arguments for the loader (in this case, none)
            this        // The context of the activity
    )

    // Creates a new cursor adapter to attach to the list view
    cursorAdapter = SimpleCursorAdapter(
            this,                       // the context of the activity
            R.layout.detail_list_item,  // the view item containing the detail widgets
            mCursor,                    // the backing cursor
            fromColumns,               // the columns in the cursor that provide the data
            toViews,                   // the views in the view item that display the data
            0)                          // flags

    // Sets the ListView's backing adapter.
    rawContactList.adapter = cursorAdapter
...
override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
    /*
     * Sets the columns to retrieve.
     * RAW_CONTACT_ID is included to identify the raw contact associated with the data row.
     * DATA1 contains the first column in the data row (usually the most important one).
     * MIMETYPE indicates the type of data in the data row.
     */
    val projection: Array<String> = arrayOf(
            ContactsContract.Contacts.Entity.RAW_CONTACT_ID,
            ContactsContract.Contacts.Entity.DATA1,
            ContactsContract.Contacts.Entity.MIMETYPE
    )

    /*
     * Sorts the retrieved cursor by raw contact id, to keep all data rows for a single raw
     * contact collated together.
     */
    val sortOrder = "${ContactsContract.Contacts.Entity.RAW_CONTACT_ID} ASC"

    /*
     * Returns a new CursorLoader. The arguments are similar to
     * ContentResolver.query(), except for the Context argument, which supplies the location of
     * the ContentResolver to use.
     */
    return CursorLoader(
            applicationContext, // The activity's context
            contactUri,        // The entity content URI for a single contact
            projection,         // The columns to retrieve
            null,               // Retrieve all the raw contacts and their data rows.
            null,               //
            sortOrder           // Sort by the raw contact ID.
    )
}
```

### Java

```java
...
    /*
     * Appends the entity path to the URI. In the case of the Contacts Provider, the
     * expected URI is content://com.google.contacts/#/entity (# is the ID value).
     */
    contactUri = Uri.withAppendedPath(
            contactUri,
            ContactsContract.Contacts.Entity.CONTENT_DIRECTORY);

    // Initializes the loader identified by LOADER_ID.
    getLoaderManager().initLoader(
            LOADER_ID,  // The identifier of the loader to initialize
            null,       // Arguments for the loader (in this case, none)
            this);      // The context of the activity

    // Creates a new cursor adapter to attach to the list view
    cursorAdapter = new SimpleCursorAdapter(
            this,                        // the context of the activity
            R.layout.detail_list_item,   // the view item containing the detail widgets
            mCursor,                     // the backing cursor
            fromColumns,                // the columns in the cursor that provide the data
            toViews,                    // the views in the view item that display the data
            0);                          // flags

    // Sets the ListView's backing adapter.
    rawContactList.setAdapter(cursorAdapter);
...
@Override
public Loader<Cursor> onCreateLoader(int id, Bundle args) {

    /*
     * Sets the columns to retrieve.
     * RAW_CONTACT_ID is included to identify the raw contact associated with the data row.
     * DATA1 contains the first column in the data row (usually the most important one).
     * MIMETYPE indicates the type of data in the data row.
     */
    String[] projection =
        {
            ContactsContract.Contacts.Entity.RAW_CONTACT_ID,
            ContactsContract.Contacts.Entity.DATA1,
            ContactsContract.Contacts.Entity.MIMETYPE
        };

    /*
     * Sorts the retrieved cursor by raw contact id, to keep all data rows for a single raw
     * contact collated together.
     */
    String sortOrder =
            ContactsContract.Contacts.Entity.RAW_CONTACT_ID +
            " ASC";

    /*
     * Returns a new CursorLoader. The arguments are similar to
     * ContentResolver.query(), except for the Context argument, which supplies the location of
     * the ContentResolver to use.
     */
    return new CursorLoader(
            getApplicationContext(),  // The activity's context
            contactUri,              // The entity content URI for a single contact
            projection,               // The columns to retrieve
            null,                     // Retrieve all the raw contacts and their data rows.
            null,                     //
            sortOrder);               // Sort by the raw contact ID.
}
```


When the load is finished, [LoaderManager](https://developer.android.com/reference/android/app/LoaderManager) invokes a callback to
[onLoadFinished()](https://developer.android.com/reference/android/app/LoaderManager.LoaderCallbacks#onLoadFinished(android.content.Loader<D>, D)). One of the incoming arguments to this method is a
[Cursor](https://developer.android.com/reference/android/database/Cursor) with the results of the query. In your own app, you can get the
data from this [Cursor](https://developer.android.com/reference/android/database/Cursor) to display it or work with it further.

### Batch modification


Whenever possible, you should insert, update, and delete data in the Contacts Provider in
"batch mode", by creating an [ArrayList](https://developer.android.com/reference/java/util/ArrayList) of
[ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) objects and calling
[applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)). Because
the Contacts Provider performs all of the operations in an
[applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)) in a single
transaction, your modifications will never leave the contacts repository in an inconsistent
state. A batch modification also facilitates inserting a raw contact and its detail data at
the same time.


**Note:** To modify a *single* raw contact, consider sending an intent to
the device's contacts application rather than handling the modification in your app.
Doing this is described in more detail in the section
[Retrieval and modification with intents](https://developer.android.com/identity/providers/contacts-provider#Intents).

#### Yield points


A batch modification containing a large number of operations can block other processes,
resulting in a bad overall user experience. To organize all the modifications you want to
perform in as few separate lists as possible, and at the same time prevent them from
blocking the system, you should set **yield points** for one or more operations.
A yield point is a [ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) object that has its
[isYieldAllowed()](https://developer.android.com/reference/android/content/ContentProviderOperation#isYieldAllowed()) value set to
`true`. When the Contacts Provider encounters a yield point, it pauses its work to
let other processes run and closes the current transaction. When the provider starts again, it
continues with the next operation in the [ArrayList](https://developer.android.com/reference/java/util/ArrayList) and starts a new
transaction.


Yield points do result in more than one transaction per call to
[applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)). Because of
this, you should set a yield point for the last operation for a set of related rows.
For example, you should set a yield point for the last operation in a set that adds a
raw contact rows and its associated data rows, or the last operation for a set of rows related
to a single contact.


Yield points are also a unit of atomic operation. All accesses between two yield points will
either succeed or fail as a single unit. If you don't set any yield points, the smallest
atomic operation is the entire batch of operations. If you do use yield points, you prevent
operations from degrading system performance, while at the same time ensuring that a subset of
operations is atomic.

#### Modification back references


When you're inserting a new raw contact row and its associated data rows as a set of
[ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) objects, you have to link the data rows to
the raw contact row by inserting the raw contact's
[_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) value as the
[RAW_CONTACT_ID](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#RAW_CONTACT_ID) value. However, this
value isn't available when you're creating the [ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation)
for the data row, because you haven't yet applied the
[ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) for the raw contact row. To work around this,
the [ContentProviderOperation.Builder](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder) class has the method
[withValueBackReference()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withValueBackReference(java.lang.String, int)).
This method allows you to insert or modify a column with the
result of a previous operation.


The [withValueBackReference()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withValueBackReference(java.lang.String, int))
method has two arguments:


`key`
:
    The key of a key-value pair. The value of this argument should be the name of a column
    in the table that you're modifying.


`previousResult`
:
    The 0-based index of a value in the array of
    [ContentProviderResult](https://developer.android.com/reference/android/content/ContentProviderResult) objects from
    [applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)). As
    the batch operations are applied, the result of each operation is stored in an
    intermediate array of results. The `previousResult` value is the index
    of one of these results, which is retrieved and stored with the `key`
    value. This allows you to insert a new raw contact record and get back its
    [_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) value, then make a "back reference" to the
    value when you add a [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) row.


    The entire result array is created when you first call
    [applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)),
    with a size equal to the size of the [ArrayList](https://developer.android.com/reference/java/util/ArrayList) of
    [ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) objects you provide. However, all
    the elements in the result array are set to `null`, and if you try
    to do a back reference to a result for an operation that hasn't yet been applied,
    [withValueBackReference()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withValueBackReference(java.lang.String, int))
    throws an [Exception](https://developer.android.com/reference/java/lang/Exception).


The following snippets show how to insert a new raw contact and data in batch. They
include code that establishes a yield point and uses a back reference.


The first snippet retrieves contact data from the UI. At this point, the user has already
selected the account for which the new raw contact should be added.  

### Kotlin

```kotlin
// Creates a contact entry from the current UI values, using the currently-selected account.
private fun createContactEntry() {
    /*
     * Gets values from the UI
     */
    val name = contactNameEditText.text.toString()
    val phone = contactPhoneEditText.text.toString()
    val email = contactEmailEditText.text.toString()

    val phoneType: String = contactPhoneTypes[mContactPhoneTypeSpinner.selectedItemPosition]

    val emailType: String = contactEmailTypes[mContactEmailTypeSpinner.selectedItemPosition]
```

### Java

```java
// Creates a contact entry from the current UI values, using the currently-selected account.
protected void createContactEntry() {
    /*
     * Gets values from the UI
     */
    String name = contactNameEditText.getText().toString();
    String phone = contactPhoneEditText.getText().toString();
    String email = contactEmailEditText.getText().toString();

    int phoneType = contactPhoneTypes.get(
            contactPhoneTypeSpinner.getSelectedItemPosition());

    int emailType = contactEmailTypes.get(
            contactEmailTypeSpinner.getSelectedItemPosition());
```


The next snippet creates an operation to insert the raw contact row into the
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) table:  

### Kotlin

```kotlin
    /*
     * Prepares the batch operation for inserting a new raw contact and its data. Even if
     * the Contacts Provider does not have any data for this person, you can't add a Contact,
     * only a raw contact. The Contacts Provider will then add a Contact automatically.
     */

    // Creates a new array of ContentProviderOperation objects.
    val ops = arrayListOf<ContentProviderOperation>()

    /*
     * Creates a new raw contact with its account type (server type) and account name
     * (user's account). Remember that the display name is not stored in this row, but in a
     * StructuredName data row. No other data is required.
     */
    var op: ContentProviderOperation.Builder =
            ContentProviderOperation.newInsert(ContactsContract.RawContacts.CONTENT_URI)
                    .withValue(ContactsContract.RawContacts.ACCOUNT_TYPE, selectedAccount.name)
                    .withValue(ContactsContract.RawContacts.ACCOUNT_NAME, selectedAccount.type)

    // Builds the operation and adds it to the array of operations
    ops.add(op.build())
```

### Java

```java
    /*
     * Prepares the batch operation for inserting a new raw contact and its data. Even if
     * the Contacts Provider does not have any data for this person, you can't add a Contact,
     * only a raw contact. The Contacts Provider will then add a Contact automatically.
     */

     // Creates a new array of ContentProviderOperation objects.
    ArrayList<ContentProviderOperation> ops =
            new ArrayList<ContentProviderOperation>();

    /*
     * Creates a new raw contact with its account type (server type) and account name
     * (user's account). Remember that the display name is not stored in this row, but in a
     * StructuredName data row. No other data is required.
     */
    ContentProviderOperation.Builder op =
            ContentProviderOperation.newInsert(ContactsContract.RawContacts.CONTENT_URI)
            .withValue(ContactsContract.RawContacts.ACCOUNT_TYPE, selectedAccount.getType())
            .withValue(ContactsContract.RawContacts.ACCOUNT_NAME, selectedAccount.getName());

    // Builds the operation and adds it to the array of operations
    ops.add(op.build());
```


Next, the code creates data rows for the display name, phone, and email rows.


Each operation builder object uses
[withValueBackReference()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withValueBackReference(java.lang.String, int))
to get the
[RAW_CONTACT_ID](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#RAW_CONTACT_ID). The reference points
back to the [ContentProviderResult](https://developer.android.com/reference/android/content/ContentProviderResult) object from the first operation,
which adds the raw contact row and returns its new [_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID)
value. As a result, each data row is automatically linked by its
[RAW_CONTACT_ID](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#RAW_CONTACT_ID)
to the new [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row to which it belongs.


The [ContentProviderOperation.Builder](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder) object that adds the email row is
flagged with [withYieldAllowed()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withYieldAllowed(boolean)), which sets a yield point:  

### Kotlin

```kotlin
    // Creates the display name for the new raw contact, as a StructuredName data row.
    op = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)
            /*
             * withValueBackReference sets the value of the first argument to the value of
             * the ContentProviderResult indexed by the second argument. In this particular
             * call, the raw contact ID column of the StructuredName data row is set to the
             * value of the result returned by the first operation, which is the one that
             * actually adds the raw contact row.
             */
            .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)

            // Sets the data row's MIME type to StructuredName
            .withValue(ContactsContract.Data.MIMETYPE,
                    ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE)

            // Sets the data row's display name to the name in the UI.
            .withValue(ContactsContract.CommonDataKinds.StructuredName.DISPLAY_NAME, name)

    // Builds the operation and adds it to the array of operations
    ops.add(op.build())

    // Inserts the specified phone number and type as a Phone data row
    op = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)
            /*
             * Sets the value of the raw contact id column to the new raw contact ID returned
             * by the first operation in the batch.
             */
            .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)

            // Sets the data row's MIME type to Phone
            .withValue(ContactsContract.Data.MIMETYPE,
                    ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE)

            // Sets the phone number and type
            .withValue(ContactsContract.CommonDataKinds.Phone.NUMBER, phone)
            .withValue(ContactsContract.CommonDataKinds.Phone.TYPE, phoneType)

    // Builds the operation and adds it to the array of operations
    ops.add(op.build())

    // Inserts the specified email and type as a Phone data row
    op = ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)
            /*
             * Sets the value of the raw contact id column to the new raw contact ID returned
             * by the first operation in the batch.
             */
            .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)

            // Sets the data row's MIME type to Email
            .withValue(ContactsContract.Data.MIMETYPE,
                    ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE)

            // Sets the email address and type
            .withValue(ContactsContract.CommonDataKinds.Email.ADDRESS, email)
            .withValue(ContactsContract.CommonDataKinds.Email.TYPE, emailType)

    /*
     * Demonstrates a yield point. At the end of this insert, the batch operation's thread
     * will yield priority to other threads. Use after every set of operations that affect a
     * single contact, to avoid degrading performance.
     */
    op.withYieldAllowed(true)

    // Builds the operation and adds it to the array of operations
    ops.add(op.build())
```

### Java

```java
    // Creates the display name for the new raw contact, as a StructuredName data row.
    op =
            ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)
            /*
             * withValueBackReference sets the value of the first argument to the value of
             * the ContentProviderResult indexed by the second argument. In this particular
             * call, the raw contact ID column of the StructuredName data row is set to the
             * value of the result returned by the first operation, which is the one that
             * actually adds the raw contact row.
             */
            .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)

            // Sets the data row's MIME type to StructuredName
            .withValue(ContactsContract.Data.MIMETYPE,
                    ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE)

            // Sets the data row's display name to the name in the UI.
            .withValue(ContactsContract.CommonDataKinds.StructuredName.DISPLAY_NAME, name);

    // Builds the operation and adds it to the array of operations
    ops.add(op.build());

    // Inserts the specified phone number and type as a Phone data row
    op =
            ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)
            /*
             * Sets the value of the raw contact id column to the new raw contact ID returned
             * by the first operation in the batch.
             */
            .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)

            // Sets the data row's MIME type to Phone
            .withValue(ContactsContract.Data.MIMETYPE,
                    ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE)

            // Sets the phone number and type
            .withValue(ContactsContract.CommonDataKinds.Phone.NUMBER, phone)
            .withValue(ContactsContract.CommonDataKinds.Phone.TYPE, phoneType);

    // Builds the operation and adds it to the array of operations
    ops.add(op.build());

    // Inserts the specified email and type as a Phone data row
    op =
            ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI)
            /*
             * Sets the value of the raw contact id column to the new raw contact ID returned
             * by the first operation in the batch.
             */
            .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0)

            // Sets the data row's MIME type to Email
            .withValue(ContactsContract.Data.MIMETYPE,
                    ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE)

            // Sets the email address and type
            .withValue(ContactsContract.CommonDataKinds.Email.ADDRESS, email)
            .withValue(ContactsContract.CommonDataKinds.Email.TYPE, emailType);

    /*
     * Demonstrates a yield point. At the end of this insert, the batch operation's thread
     * will yield priority to other threads. Use after every set of operations that affect a
     * single contact, to avoid degrading performance.
     */
    op.withYieldAllowed(true);

    // Builds the operation and adds it to the array of operations
    ops.add(op.build());
```


The last snippet shows the call to
[applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)) that
inserts the new raw contact and data rows.  

### Kotlin

```kotlin
    // Ask the Contacts Provider to create a new contact
    Log.d(TAG, "Selected account: ${mSelectedAccount.name} (${mSelectedAccount.type})")
    Log.d(TAG, "Creating contact: $name")

    /*
     * Applies the array of ContentProviderOperation objects in batch. The results are
     * discarded.
     */
    try {
        contentResolver.applyBatch(ContactsContract.AUTHORITY, ops)
    } catch (e: Exception) {
        // Display a warning
        val txt: String = getString(R.string.contactCreationFailure)
        Toast.makeText(applicationContext, txt, Toast.LENGTH_SHORT).show()

        // Log exception
        Log.e(TAG, "Exception encountered while inserting contact: $e")
    }
}
```

### Java

```java
    // Ask the Contacts Provider to create a new contact
    Log.d(TAG,"Selected account: " + selectedAccount.getName() + " (" +
            selectedAccount.getType() + ")");
    Log.d(TAG,"Creating contact: " + name);

    /*
     * Applies the array of ContentProviderOperation objects in batch. The results are
     * discarded.
     */
    try {

            getContentResolver().applyBatch(ContactsContract.AUTHORITY, ops);
    } catch (Exception e) {

            // Display a warning
            Context ctx = getApplicationContext();

            CharSequence txt = getString(R.string.contactCreationFailure);
            int duration = Toast.LENGTH_SHORT;
            Toast toast = Toast.makeText(ctx, txt, duration);
            toast.show();

            // Log exception
            Log.e(TAG, "Exception encountered while inserting contact: " + e);
    }
}
```


Batch operations also allow you to implement **optimistic concurrency control**,
a method of applying modification transactions without having to lock the underlying repository.
To use this method, you apply the transaction and then check for other modifications that
may have been made at the same time. If you find an inconsistent modification has occurred, you
roll back your transaction and retry it.


Optimistic concurrency control is useful for a mobile device, where there's only one user at
a time, and simultaneous accesses to a data repository are rare. Because locking isn't used,
no time is wasted on setting locks or waiting for other transactions to release their locks.


To use optimistic concurrency control while updating a single
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row, follow these steps:

1. Retrieve the raw contact's [VERSION](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#VERSION) column along with the other data you retrieve.
2. Create a [ContentProviderOperation.Builder](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder) object suitable for enforcing a constraint, using the method [newAssertQuery(Uri)](https://developer.android.com/reference/android/content/ContentProviderOperation#newAssertQuery(android.net.Uri)). For the content URI, use [RawContacts.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts#CONTENT_URI) with the raw contact's [_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) appended to it.
3. For the [ContentProviderOperation.Builder](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder) object, call [withValue()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withValue(java.lang.String, java.lang.Object)) to compare the [VERSION](https://developer.android.com/reference/android/provider/ContactsContract.SyncColumns#VERSION) column to the version number you just retrieved.
4. For the same [ContentProviderOperation.Builder](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder), call [withExpectedCount()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#withExpectedCount(int)) to ensure that only one row is tested by this assertion.
5. Call [build()](https://developer.android.com/reference/android/content/ContentProviderOperation.Builder#build()) to create the [ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) object, then add this object as the first object in the [ArrayList](https://developer.android.com/reference/java/util/ArrayList) that you pass to [applyBatch()](https://developer.android.com/reference/android/content/ContentResolver#applyBatch(java.lang.String, java.util.ArrayList<android.content.ContentProviderOperation>)).
6. Apply the batch transaction.


If the raw contact row is updated by another operation between the time you read the row and
the time you attempt to modify it, the "assert" [ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation)
will fail, and the entire batch of operations will be backed out. You can then choose to retry
the batch or take some other action.


The following snippet demonstrates how to create an "assert"
[ContentProviderOperation](https://developer.android.com/reference/android/content/ContentProviderOperation) after querying for a single raw contact using
a [CursorLoader](https://developer.android.com/reference/android/content/CursorLoader):  

### Kotlin

```kotlin
/*
 * The application uses CursorLoader to query the raw contacts table. The system calls this method
 * when the load is finished.
 */
override fun onLoadFinished(loader: Loader<Cursor>, cursor: Cursor) {
    // Gets the raw contact's _ID and VERSION values
    rawContactID = cursor.getLong(cursor.getColumnIndex(BaseColumns._ID))
    mVersion = cursor.getInt(cursor.getColumnIndex(SyncColumns.VERSION))
}

...

// Sets up a Uri for the assert operation
val rawContactUri: Uri = ContentUris.withAppendedId(
        ContactsContract.RawContacts.CONTENT_URI,
        rawContactID
)

// Creates a builder for the assert operation
val assertOp: ContentProviderOperation.Builder =
        ContentProviderOperation.newAssertQuery(rawContactUri).apply {
            // Adds the assertions to the assert operation: checks the version
            withValue(SyncColumns.VERSION, mVersion)

            // and count of rows tested
            withExpectedCount(1)
        }

// Creates an ArrayList to hold the ContentProviderOperation objects
val ops = arrayListOf<ContentProviderOperation>()

ops.add(assertOp.build())

// You would add the rest of your batch operations to "ops" here

...

// Applies the batch. If the assert fails, an Exception is thrown
try {
    val results: Array<ContentProviderResult> = contentResolver.applyBatch(AUTHORITY, ops)
} catch (e: OperationApplicationException) {
    // Actions you want to take if the assert operation fails go here
}
```

### Java

```java
/*
 * The application uses CursorLoader to query the raw contacts table. The system calls this method
 * when the load is finished.
 */
public void onLoadFinished(Loader<Cursor> loader, Cursor cursor) {

    // Gets the raw contact's _ID and VERSION values
    rawContactID = cursor.getLong(cursor.getColumnIndex(BaseColumns._ID));
    mVersion = cursor.getInt(cursor.getColumnIndex(SyncColumns.VERSION));
}

...

// Sets up a Uri for the assert operation
Uri rawContactUri = ContentUris.withAppendedId(RawContacts.CONTENT_URI, rawContactID);

// Creates a builder for the assert operation
ContentProviderOperation.Builder assertOp = ContentProviderOperation.newAssertQuery(rawContactUri);

// Adds the assertions to the assert operation: checks the version and count of rows tested
assertOp.withValue(SyncColumns.VERSION, mVersion);
assertOp.withExpectedCount(1);

// Creates an ArrayList to hold the ContentProviderOperation objects
ArrayList ops = new ArrayList<ContentProviderOperation>;

ops.add(assertOp.build());

// You would add the rest of your batch operations to "ops" here

...

// Applies the batch. If the assert fails, an Exception is thrown
try
    {
        ContentProviderResult[] results =
                getContentResolver().applyBatch(AUTHORITY, ops);

    } catch (OperationApplicationException e) {

        // Actions you want to take if the assert operation fails go here
    }
```

### Retrieval and modification with intents


Sending an intent to the device's contacts application allows you to access the Contacts
Provider indirectly. The intent starts the device's contacts application UI, in which users can
do contacts-related work. With this type of access, users can:

- Pick a contact from a list and have it returned to your app for further work.
- Edit an existing contact's data.
- Insert a new raw contact for any of their accounts.
- Delete a contact or contacts data.


If the user is inserting or updating data, you can collect the data first and send it as
part of the intent.


When you use intents to access the Contacts Provider via the device's contacts application, you
don't have to write your own UI or code for accessing the provider. You also don't have to
request permission to read or write to the provider. The device's contacts application can
delegate read permission for a contact to you, and because you're making modifications to the
provider through another application, you don't have to have write permissions.


The general process of sending an intent to access a provider is described in detail in the
[Content Provider basics](https://developer.android.com/guide/topics/providers/content-provider-basics) guide in the section "Data access via intents." The action,
MIME type, and data values you use for the available tasks are summarized in Table 4, while the
extras values you can use with
[putExtra()](https://developer.android.com/reference/android/content/Intent#putExtra(java.lang.String, java.lang.String)) are listed in the
reference documentation for [ContactsContract.Intents.Insert](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert):


**Table 4.** Contacts Provider Intents.

| Task | Action | Data | MIME type | Notes |
|---|---|---|---|---|
| **Pick a contact from a list** | [ACTION_PICK](https://developer.android.com/reference/android/content/Intent#ACTION_PICK) | One of: - [Contacts.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_URI), which displays a list of contacts. - [Phone.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Phone#CONTENT_URI), which displays a list of phone numbers for a raw contact. - [StructuredPostal.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredPostal#CONTENT_URI), which displays a list of postal addresses for a raw contact. - [Email.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Email#CONTENT_URI), which displays a list of email addresses for a raw contact. | Not used | Displays a list of raw contacts or a list of data from a raw contact, depending on the content URI type you supply. Call [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)), which returns the content URI of the selected row. The form of the URI is the table's content URI with the row's `LOOKUP_ID` appended to it. The device's contacts app delegates read and write permissions to this content URI for the life of your activity. See the [Content Provider basics](https://developer.android.com/guide/topics/providers/content-provider-basics) guide for more details. |
| **Insert a new raw contact** | [Insert.ACTION](https://developer.android.com/reference/android/provider/ContactsContract.Intents.Insert#ACTION) | N/A | [RawContacts.CONTENT_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts#CONTENT_TYPE), MIME type for a set of raw contacts. | Displays the device's contacts application's **Add Contact** screen. The extras values you add to the intent are displayed. If sent with [startActivityForResult()](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)), the content URI of the newly-added raw contact is passed back to your activity's [onActivityResult()](https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)) callback method in the [Intent](https://developer.android.com/reference/android/content/Intent) argument, in the "data" field. To get the value, call [getData()](https://developer.android.com/reference/android/content/Intent#getData()). |
| **Edit a contact** | [ACTION_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT) | [CONTENT_LOOKUP_URI](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_LOOKUP_URI) for the contact. The editor activity will allow the user to edit any of the data associated with this contact. | [Contacts.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_ITEM_TYPE), a single contact. | Displays the Edit Contact screen in the contacts application. The extras values you add to the intent are displayed. When the user clicks **Done** to save the edits, your activity returns to the foreground. |
| **Display a picker that can also add data.** | [ACTION_INSERT_OR_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT_OR_EDIT) | N/A | [CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.Contacts#CONTENT_ITEM_TYPE) | This intent always displays the contacts app's picker screen. The user can either pick a contact to edit, or add a new contact. Either the edit or the add screen appears, depending on the user's choice, and the extras data you pass in the intent is displayed. If your app displays contact data such as an email or phone number, use this intent to allow the user to add the data to an existing contact. contact, **Note:** There's no need to send a name value in this intent's extras, because the user always picks an existing name or adds a new one. Moreover, if you send a name, and the user chooses to do an edit, the contacts app will display the name you send, overwriting the previous value. If the user doesn't notice this and saves the edit, the old value is lost. |


The device's contacts app doesn't allow you to delete a raw contact or any of its data with an
intent. Instead, to delete a raw contact, use
[ContentResolver.delete()](https://developer.android.com/reference/android/content/ContentResolver#delete(android.net.Uri, java.lang.String, java.lang.String[]))
or [ContentProviderOperation.newDelete()](https://developer.android.com/reference/android/content/ContentProviderOperation#newDelete(android.net.Uri)).


The following snippet shows how to construct and send an intent that inserts a new raw
contact and data:  

### Kotlin

```kotlin
// Gets values from the UI
val name = contactNameEditText.text.toString()
val phone = contactPhoneEditText.text.toString()
val email = contactEmailEditText.text.toString()

val company = companyName.text.toString()
val jobtitle = jobTitle.text.toString()

/*
 * Demonstrates adding data rows as an array list associated with the DATA key
 */

// Defines an array list to contain the ContentValues objects for each row
val contactData = arrayListOf<ContentValues>()

/*
 * Defines the raw contact row
 */

// Sets up the row as a ContentValues object
val rawContactRow = ContentValues().apply {
    // Adds the account type and name to the row
    put(ContactsContract.RawContacts.ACCOUNT_TYPE, selectedAccount.type)
    put(ContactsContract.RawContacts.ACCOUNT_NAME, selectedAccount.name)
}

// Adds the row to the array
contactData.add(rawContactRow)

/*
 * Sets up the phone number data row
 */

// Sets up the row as a ContentValues object
val phoneRow = ContentValues().apply {
    // Specifies the MIME type for this data row (all data rows must be marked by their type)
    put(ContactsContract.Data.MIMETYPE,ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE)

    // Adds the phone number and its type to the row
    put(ContactsContract.CommonDataKinds.Phone.NUMBER, phone)
}

// Adds the row to the array
contactData.add(phoneRow)

/*
 * Sets up the email data row
 */

// Sets up the row as a ContentValues object
val emailRow = ContentValues().apply {
    // Specifies the MIME type for this data row (all data rows must be marked by their type)
    put(ContactsContract.Data.MIMETYPE, ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE)

    // Adds the email address and its type to the row
    put(ContactsContract.CommonDataKinds.Email.ADDRESS, email)
}

// Adds the row to the array
contactData.add(emailRow)

// Creates a new intent for sending to the device's contacts application
val insertIntent = Intent(ContactsContract.Intents.Insert.ACTION).apply {
    // Sets the MIME type to the one expected by the insertion activity
    type = ContactsContract.RawContacts.CONTENT_TYPE

    // Sets the new contact name
    putExtra(ContactsContract.Intents.Insert.NAME, name)

    // Sets the new company and job title
    putExtra(ContactsContract.Intents.Insert.COMPANY, company)
    putExtra(ContactsContract.Intents.Insert.JOB_TITLE, jobtitle)

    /*
    * Adds the array to the intent's extras. It must be a parcelable object in order to
    * travel between processes. The device's contacts app expects its key to be
    * Intents.Insert.DATA
    */
    putParcelableArrayListExtra(ContactsContract.Intents.Insert.DATA, contactData)
}

// Send out the intent to start the device's contacts app in its add contact activity.
startActivity(insertIntent)
```

### Java

```java
// Gets values from the UI
String name = contactNameEditText.getText().toString();
String phone = contactPhoneEditText.getText().toString();
String email = contactEmailEditText.getText().toString();

String company = companyName.getText().toString();
String jobtitle = jobTitle.getText().toString();

// Creates a new intent for sending to the device's contacts application
Intent insertIntent = new Intent(ContactsContract.Intents.Insert.ACTION);

// Sets the MIME type to the one expected by the insertion activity
insertIntent.setType(ContactsContract.RawContacts.CONTENT_TYPE);

// Sets the new contact name
insertIntent.putExtra(ContactsContract.Intents.Insert.NAME, name);

// Sets the new company and job title
insertIntent.putExtra(ContactsContract.Intents.Insert.COMPANY, company);
insertIntent.putExtra(ContactsContract.Intents.Insert.JOB_TITLE, jobtitle);

/*
 * Demonstrates adding data rows as an array list associated with the DATA key
 */

// Defines an array list to contain the ContentValues objects for each row
ArrayList<ContentValues> contactData = new ArrayList<ContentValues>();


/*
 * Defines the raw contact row
 */

// Sets up the row as a ContentValues object
ContentValues rawContactRow = new ContentValues();

// Adds the account type and name to the row
rawContactRow.put(ContactsContract.RawContacts.ACCOUNT_TYPE, selectedAccount.getType());
rawContactRow.put(ContactsContract.RawContacts.ACCOUNT_NAME, selectedAccount.getName());

// Adds the row to the array
contactData.add(rawContactRow);

/*
 * Sets up the phone number data row
 */

// Sets up the row as a ContentValues object
ContentValues phoneRow = new ContentValues();

// Specifies the MIME type for this data row (all data rows must be marked by their type)
phoneRow.put(
        ContactsContract.Data.MIMETYPE,
        ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE
);

// Adds the phone number and its type to the row
phoneRow.put(ContactsContract.CommonDataKinds.Phone.NUMBER, phone);

// Adds the row to the array
contactData.add(phoneRow);

/*
 * Sets up the email data row
 */

// Sets up the row as a ContentValues object
ContentValues emailRow = new ContentValues();

// Specifies the MIME type for this data row (all data rows must be marked by their type)
emailRow.put(
        ContactsContract.Data.MIMETYPE,
        ContactsContract.CommonDataKinds.Email.CONTENT_ITEM_TYPE
);

// Adds the email address and its type to the row
emailRow.put(ContactsContract.CommonDataKinds.Email.ADDRESS, email);

// Adds the row to the array
contactData.add(emailRow);

/*
 * Adds the array to the intent's extras. It must be a parcelable object in order to
 * travel between processes. The device's contacts app expects its key to be
 * Intents.Insert.DATA
 */
insertIntent.putParcelableArrayListExtra(ContactsContract.Intents.Insert.DATA, contactData);

// Send out the intent to start the device's contacts app in its add contact activity.
startActivity(insertIntent);
```

### Data integrity


Because the contacts repository contains important and sensitive data that users expect to be
correct and up-to-date, the Contacts Provider has well-defined rules for data integrity. It's
your responsibility to conform to these rules when you modify contacts data. The important
rules are listed here:


Always add a [ContactsContract.CommonDataKinds.StructuredName](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredName) row
for every [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row you add.
:
    A [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row without a
    [ContactsContract.CommonDataKinds.StructuredName](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.StructuredName) row in the
    [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table may cause problems during
    aggregation.


Always link new [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) rows to their parent
[ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) row.
:
    A [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) row that isn't linked to a
    [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) won't be visible in the device's
    contacts application, and it might cause problems with sync adapters.


Change data only for those raw contacts that you own.
:
    Remember that the Contacts Provider is usually managing data from several different
    account types/online services. You need to ensure that your application only modifies
    or deletes data for rows that belong to you, and that it only inserts data with an
    account type and name that you control.


Always use the constants defined in [ContactsContract](https://developer.android.com/reference/android/provider/ContactsContract) and its
subclasses for authorities, content URIs, URI paths, column names, MIME types, and
[TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.CommonColumns#TYPE) values.
:
    Using these constants helps you to avoid errors. You'll also be notified with compiler
    warnings if any of the constants is deprecated.

### Custom data rows


By creating and using your own custom MIME types, you can insert, edit, delete, and retrieve
your own data rows in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table. Your rows
are limited to using the column defined in
[ContactsContract.DataColumns](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns), although you can map your own
type-specific column names to the default column names. In the device's contacts application,
the data for your rows is displayed but can't be edited or deleted, and users can't add
additional data. To allow users to modify your custom data rows, you must provide an editor
activity in your own application.


To display your custom data, provide a `contacts.xml` file containing a
`<ContactsAccountType>` element and one or more of its
`<ContactsDataKind>` child elements. This is described in more detail in the
section [`<ContactsDataKind> element`](https://developer.android.com/identity/providers/contacts-provider#SocialStreamDataKind).


To learn more about custom MIME types, read the
[Create a Content Provider](https://developer.android.com/guide/topics/providers/content-provider-creating) guide.

## Contacts Provider sync adapters


The Contacts Provider is specifically designed for handling **synchronization**
of contacts data between a device and an online service. This allows users to download
existing data to a new device and upload existing data to a new account.
Synchronization also ensures that users have the latest data at hand, regardless
of the source of additions and changes. Another advantage of synchronization is that it makes
contacts data available even when the device is not connected to the network.


Although you can implement synchronization in a variety of ways, the Android system provides
a plug-in synchronization framework that automates the following tasks:

- Checking network availability.
- Scheduling and executing synchronization, based on user preferences.
- Restarting synchronizations that have stopped.


To use this framework, you supply a sync adapter plug-in. Each sync adapter is unique to a
service and content provider, but can handle multiple account names for the same service. The
framework also allows multiple sync adapters for the same service and provider.

### Sync adapter classes and files


You implement a sync adapter as a subclass of
[AbstractThreadedSyncAdapter](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter) and install it as part of an Android
application. The system learns about the sync adapter from elements in your application
manifest, and from a special XML file pointed to by the manifest. The XML file defines the
account type for the online service and the authority for the content provider, which together
uniquely identify the adapter. The sync adapter does not become active until the user adds an
account for the sync adapter's account type and enables synchronization for the content
provider the sync adapter syncs with. At that point, the system starts managing the adapter,
calling it as necessary to synchronize between the content provider and the server.


**Note:** Using an account type as part of the sync adapter's identification allows
the system to detect and group together sync adapters that access different services from the
same organization. For example, sync adapters for Google online services all have the same
account type `com.google`. When users add a Google Account to their devices, all
of the installed sync adapters for Google services are listed together; each sync adapter
listed syncs with a different content provider on the device.


Because most services require users to verify their identity before accessing
data, the Android system offers an authentication framework that is similar to, and often
used in conjunction with, the sync adapter framework. The authentication framework uses
plug-in authenticators that are subclasses of
[AbstractAccountAuthenticator](https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator). An authenticator verifies
the user's identity in the following steps:

1. Collects the user's name, password or similar information (the user's **credentials**).
2. Sends the credentials to the service
3. Examines the service's reply.


If the service accepts the credentials, the authenticator can
store the credentials for later use. Because of the plug-in authenticator framework, the
[AccountManager](https://developer.android.com/reference/android/accounts/AccountManager) can provide access to any authtokens an authenticator
supports and chooses to expose, such as OAuth2 authtokens.


Although authentication is not required, most contacts services use it.
However, you're not required to use the Android authentication framework to do authentication.

### Sync adapter implementation


To implement a sync adapter for the Contacts Provider, you start by creating an
Android application that contains the following:


A [Service](https://developer.android.com/reference/android/app/Service) component that responds to requests from the system to
bind to the sync adapter.
:
    When the system wants to run a synchronization, it calls the service's
    [onBind()](https://developer.android.com/reference/android/app/Service#onBind(android.content.Intent)) method to get an
    [IBinder](https://developer.android.com/reference/android/os/IBinder) for the sync adapter. This allows the system to do
    cross-process calls to the adapter's methods.


The actual sync adapter, implemented as a concrete subclass of
[AbstractThreadedSyncAdapter](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter).
:
    This class does the work of downloading data from the server, uploading data from the
    device, and resolving conflicts. The main work of the adapter is
    done in the method [onPerformSync()](https://developer.android.com/reference/android/content/AbstractThreadedSyncAdapter#onPerformSync(android.accounts.Account, android.os.Bundle, java.lang.String, android.content.ContentProviderClient, android.content.SyncResult)). This class must be instantiated as a singleton.


A subclass of [Application](https://developer.android.com/reference/android/app/Application).
:
    This class acts as a factory for the sync adapter singleton. Use the
    [onCreate()](https://developer.android.com/reference/android/app/Application#onCreate()) method to instantiate the sync adapter, and
    provide a static "getter" method to return the singleton to the
    [onBind()](https://developer.android.com/reference/android/app/Service#onBind(android.content.Intent)) method of the sync adapter's
    service.


**Optional:** A [Service](https://developer.android.com/reference/android/app/Service) component that responds to
requests from the system for user authentication.
:
    [AccountManager](https://developer.android.com/reference/android/accounts/AccountManager) starts this service to begin the authentication
    process. The service's [onCreate()](https://developer.android.com/reference/android/app/Service#onCreate()) method instantiates an
    authenticator object. When the system wants to authenticate a user account for the
    application's sync adapter, it calls the service's
    [onBind()](https://developer.android.com/reference/android/app/Service#onBind(android.content.Intent)) method to get an
    [IBinder](https://developer.android.com/reference/android/os/IBinder) for the authenticator. This allows the system to do
    cross-process calls to the authenticator's methods..


**Optional:** A concrete subclass of
[AbstractAccountAuthenticator](https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator) that handles requests for
authentication.
:
    This class provides methods that the [AccountManager](https://developer.android.com/reference/android/accounts/AccountManager) invokes
    to authenticate the user's credentials with the server. The details of the
    authentication process vary widely, based on the server technology in use. You should
    refer to the documentation for your server software to learn more about authentication.


XML files that define the sync adapter and authenticator to the system.
:
    The sync adapter and authenticator service components described previously are
    defined in
    `<`[service](https://developer.android.com/guide/topics/manifest/service-element)`>`
    elements in the application manifest. These elements
    contain
    `<`[meta-data](https://developer.android.com/guide/topics/manifest/meta-data-element)`>`
    child elements that provide specific data to the system:

    - The `<`[meta-data](https://developer.android.com/guide/topics/manifest/meta-data-element)`>` element for the sync adapter service points to the XML file `res/xml/syncadapter.xml`. In turn, this file specifies a URI for the web service that will be synchronized with the Contacts Provider, and an account type for the web service.
    - **Optional:** The `<`[meta-data](https://developer.android.com/guide/topics/manifest/meta-data-element)`>` element for the authenticator points to the XML file `res/xml/authenticator.xml`. In turn, this file specifies the account type that this authenticator supports, as well as UI resources that appear during the authentication process. The account type specified in this element must be the same as the account type specified for the sync adapter.

## Social stream data


The android.provider.ContactsContract.StreamItems and
android.provider.ContactsContract.StreamItemPhotos tables
manage incoming data from social networks. You can write a sync adapter that adds stream data
from your own network to these tables, or you can read stream data from these tables and
display it in your own application, or both. With these features, your social networking
services and applications can be integrated into Android's social networking experience.

### Social stream text


Stream items are always associated with a raw contact. The
android.provider.ContactsContract.StreamItemsColumns#RAW_CONTACT_ID links to the
`_ID` value for the raw contact. The account type and account name of the raw
contact are also stored in the stream item row.


Store the data from your stream in the following columns:


android.provider.ContactsContract.StreamItemsColumns#ACCOUNT_TYPE
:
    **Required.** The user's account type for the raw contact associated with this
    stream item. Remember to set this value when you insert a stream item.


android.provider.ContactsContract.StreamItemsColumns#ACCOUNT_NAME
:
    **Required.** The user's account name for the raw contact associated with this
    stream item. Remember to set this value when you insert a stream item.


Identifier columns
:
    **Required.** You must insert the following identifier columns when you
    insert a stream item:

    - android.provider.ContactsContract.StreamItemsColumns#CONTACT_ID: The android.provider.BaseColumns#_ID value of the contact that this stream item is associated with.
    - android.provider.ContactsContract.StreamItemsColumns#CONTACT_LOOKUP_KEY: The android.provider.ContactsContract.ContactsColumns#LOOKUP_KEY value of the contact this stream item is associated with.
    - android.provider.ContactsContract.StreamItemsColumns#RAW_CONTACT_ID: The android.provider.BaseColumns#_ID value of the raw contact that this stream item is associated with.


android.provider.ContactsContract.StreamItemsColumns#COMMENTS
:
    Optional. Stores summary information that you can display at the beginning of a stream item.


android.provider.ContactsContract.StreamItemsColumns#TEXT
:
    The text of the stream item, either the content that was posted by the source of the item,
    or a description of some action that generated the stream item. This column can contain
    any formatting and embedded resource images that can be rendered by
    [fromHtml()](https://developer.android.com/reference/android/text/Html#fromHtml(java.lang.String)). The provider may truncate or
    ellipsize long content, but it will try to avoid breaking tags.


android.provider.ContactsContract.StreamItemsColumns#TIMESTAMP
:
    A text string containing the time the stream item was inserted or updated, in the form
    of *milliseconds* since epoch. Applications that insert or update stream items are
    responsible for maintaining this column; it is not automatically maintained by the
    Contacts Provider.


To display identifying information for your stream items, use the
android.provider.ContactsContract.StreamItemsColumns#RES_ICON,
android.provider.ContactsContract.StreamItemsColumns#RES_LABEL, and
android.provider.ContactsContract.StreamItemsColumns#RES_PACKAGE to link to resources
in your application.


The android.provider.ContactsContract.StreamItems table also contains the columns
android.provider.ContactsContract.StreamItemsColumns#SYNC1 through
android.provider.ContactsContract.StreamItemsColumns#SYNC4 for the exclusive use of
sync adapters.

### Social stream photos


The android.provider.ContactsContract.StreamItemPhotos table stores photos associated
with a stream item. The table's
android.provider.ContactsContract.StreamItemPhotosColumns#STREAM_ITEM_ID column
links to values in the [_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) column of
android.provider.ContactsContract.StreamItems table. Photo references are stored in the
table in these columns:


android.provider.ContactsContract.StreamItemPhotos#PHOTO column (a BLOB).
:
    A binary representation of the photo, resized by the provider for storage and display.
    This column is available for backwards compatibility with previous versions of the Contacts
    Provider that used it for storing photos. However, in the current version
    you should not use this column to store photos. Instead, use
    either android.provider.ContactsContract.StreamItemPhotosColumns#PHOTO_FILE_ID or
    android.provider.ContactsContract.StreamItemPhotosColumns#PHOTO_URI (both of
    which are described in the following points) to store photos in a file. This column now
    contains a thumbnail of the photo, which is available for reading.


android.provider.ContactsContract.StreamItemPhotosColumns#PHOTO_FILE_ID
:
    A numeric identifier of a photo for a raw contact. Append this value to the constant
    [DisplayPhoto.CONTENT_URI](https://developer.android.com/reference/android/provider/ContactsContract.DisplayPhoto#CONTENT_URI)
    to get a content URI pointing to a single photo file, and then call
    [openAssetFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openAssetFileDescriptor(android.net.Uri, java.lang.String)) to get a handle to the photo file.


android.provider.ContactsContract.StreamItemPhotosColumns#PHOTO_URI
:
    A content URI pointing directly to the photo file for the photo represented by this row.
    Call [openAssetFileDescriptor()](https://developer.android.com/reference/android/content/ContentResolver#openAssetFileDescriptor(android.net.Uri, java.lang.String)) with this URI to get a handle to the photo file.

### Using the social stream tables


These tables work the same as the other main tables in the Contacts Provider, except that:

- These tables require additional access permissions. To read from them, your application must have the permission android.Manifest.permission#READ_SOCIAL_STREAM. To modify them, your application must have the permission android.Manifest.permission#WRITE_SOCIAL_STREAM.
- For the android.provider.ContactsContract.StreamItems table, the number of rows stored for each raw contact is limited. Once this limit is reached, the Contacts Provider makes space for new stream item rows by automatically deleting the rows having the oldest android.provider.ContactsContract.StreamItemsColumns#TIMESTAMP. To get the limit, issue a query to the content URI android.provider.ContactsContract.StreamItems#CONTENT_LIMIT_URI. You can leave all the arguments other than the content URI set to `null`. The query returns a Cursor containing a single row, with the single column android.provider.ContactsContract.StreamItems#MAX_ITEMS.


The class android.provider.ContactsContract.StreamItems.StreamItemPhotos defines a
sub-table of android.provider.ContactsContract.StreamItemPhotos containing the photo
rows for a single stream item.

### Social stream interactions


The social stream data managed by the Contacts Provider, in conjunction with the
device's contacts application, offers a powerful way to connect your social networking system
with existing contacts. The following features are available:

- By syncing your social networking service to the Contacts Provider with a sync adapter, you can retrieve recent activity for a user's contacts and store it in the android.provider.ContactsContract.StreamItems and android.provider.ContactsContract.StreamItemPhotos tables for later use.
- Besides regular synchronization, you can trigger your sync adapter to retrieve additional data when the user selects a contact to view. This allows your sync adapter to retrieve high-resolution photos and the most recent stream items for the contact.
- By registering a notification with the device's contacts application and the Contacts Provider, you can *receive* an intent when a contact is viewed, and at that point update the contact's status from your service. This approach may be faster and use less bandwidth than doing a full sync with a sync adapter.
- Users can add a contact to your social networking service while looking at the contact in the device's contacts application. You enable this with the "invite contact" feature, which you enable with a combination of an activity that adds an existing contact to your network, and an XML file that provides the device's contacts application and the Contacts Provider with the details of your application.


Regular synchronization of stream items with the Contacts Provider is the same as
other synchronizations. To learn more about synchronization, see the section
[Contacts Provider sync adapters](https://developer.android.com/identity/providers/contacts-provider#SyncAdapters). Registering notifications and
inviting contacts are covered in the next two sections.

#### Registering to handle social networking views


To register your sync adapter to receive notifications when the user views a contact that's
managed by your sync adapter:

1. Create a file named `contacts.xml` in your project's `res/xml/` directory. If you already have this file, you can skip this step.
2. In this file, add the element `<ContactsAccountType xmlns:android="http://schemas.android.com/apk/res/android">`. If this element already exists, you can skip this step.
3. To register a service that is notified when the user opens a contact's detail page in the device's contacts application, add the attribute `viewContactNotifyService="`*serviceclass*`"` to the element, where *serviceclass* is the fully-qualified classname of the service that should receive the intent from the device's contacts application. For the notifier service, use a class that extends [IntentService](https://developer.android.com/reference/android/app/IntentService), to allow the service to receive intents. The data in the incoming intent contains the content URI of the raw contact the user clicked. From the notifier service, you can bind to and then call your sync adapter to update the data for the raw contact.


To register an activity to be called when the user clicks on a stream item or photo or both:

1. Create a file named `contacts.xml` in your project's `res/xml/` directory. If you already have this file, you can skip this step.
2. In this file, add the element `<ContactsAccountType xmlns:android="http://schemas.android.com/apk/res/android">`. If this element already exists, you can skip this step.
3. To register one of your activities to handle the user clicking on a stream item in the device's contacts application, add the attribute `viewStreamItemActivity="`*activityclass*`"` to the element, where *activityclass* is the fully-qualified classname of the activity that should receive the intent from the device's contacts application.
4. To register one of your activities to handle the user clicking on a stream photo in the device's contacts application, add the attribute `viewStreamItemPhotoActivity="`*activityclass*`"` to the element, where *activityclass* is the fully-qualified classname of the activity that should receive the intent from the device's contacts application.


The `<ContactsAccountType>` element is described in more detail in the
section [\<ContactsAccountType\> element](https://developer.android.com/identity/providers/contacts-provider#SocialStreamAcctType).


The incoming intent contains the content URI of the item or photo that the user clicked.
To have separate activities for text items and for photos, use both attributes in the same file.

#### Interacting with your social networking service


Users don't have to leave the device's contacts application to invite a contact to your social
networking site. Instead, you can have the device's contacts app send an intent for inviting the
contact to one of your activities. To set this up:

1. Create a file named `contacts.xml` in your project's `res/xml/` directory. If you already have this file, you can skip this step.
2. In this file, add the element `<ContactsAccountType xmlns:android="http://schemas.android.com/apk/res/android">`. If this element already exists, you can skip this step.
3. Add the following attributes:
   - `inviteContactActivity="`*activityclass*`"`
   - `inviteContactActionLabel="@string/`*invite_action_label*`"`

   The *activityclass* value is the fully-qualified classname of the activity that should receive the intent. The *invite_action_label* value is a text string that's displayed in the **Add Connection** menu in the device's contacts application.


**Note:** `ContactsSource` is a deprecated tag name for
`ContactsAccountType`.

### contacts.xml reference


The file `contacts.xml` contains XML elements that control the interaction of your
sync adapter and application with the contacts application and the Contacts Provider. These
elements are described in the following sections.

#### \<ContactsAccountType\> element


The `<ContactsAccountType>` element controls the interaction of your
application with the contacts application. It has the following syntax:  

```xml
<ContactsAccountType
        xmlns:android="http://schemas.android.com/apk/res/android"
        inviteContactActivity="activity_name"
        inviteContactActionLabel="invite_command_text"
        viewContactNotifyService="view_notify_service"
        viewGroupActivity="group_view_activity"
        viewGroupActionLabel="group_action_text"
        viewStreamItemActivity="viewstream_activity_name"
        viewStreamItemPhotoActivity="viewphotostream_activity_name">
```


**contained in:**


`res/xml/contacts.xml`


**can contain:**


**`<ContactsDataKind>`**


**Description:**


Declares Android components and UI labels that allow users to invite one of their contacts to
a social network, notify users when one of their social networking streams is updated, and
so forth.


Notice that the attribute prefix `android:` is not necessary for the attributes
of `<ContactsAccountType>`.


**Attributes:**

`inviteContactActivity`
:
    The fully-qualified class name of the activity in your application that you want to
    activate when the user selects **Add connection** from the device's
    contacts application.

`inviteContactActionLabel`
:
    A text string that is displayed for the activity specified in
    `inviteContactActivity`, in the **Add connection** menu.
    For example, you can use the string "Follow in my network". You can use a string resource
    identifier for this label.

`viewContactNotifyService`
:
    The fully-qualified class name of a service in your application that should receive
    notifications when the user views a contact. This notification is sent by the device's
    contacts application; it allows your application to postpone data-intensive operations
    until they're needed. For example, your application can respond to this notification
    by reading in and displaying the contact's high-resolution photo and most recent
    social stream items. This feature is described in more detail in the section
    [Social stream interactions](https://developer.android.com/identity/providers/contacts-provider#SocialStreamInteraction).

`viewGroupActivity`
:
    The fully-qualified class name of an activity in your application that can display
    group information. When the user clicks the group label in the device's contacts
    application, the UI for this activity is displayed.

`viewGroupActionLabel`

:   The label that the contacts application displays for a UI control that allows the user to look at groups in your application.
    A string resource identifier is allowed for this attribute.

`viewStreamItemActivity`
:
    The fully-qualified class name of an activity in your application that the device's
    contacts application launches when the user clicks a stream item for a raw contact.

`viewStreamItemPhotoActivity`
:
    The fully-qualified class name of an activity in your application that the device's
    contacts application launches when the user clicks a photo in the stream item
    for a raw contact.

#### \<ContactsDataKind\> element


The `<ContactsDataKind>` element controls the display of your application's
custom data rows in the contacts application's UI. It has the following syntax:  

```xml
<ContactsDataKind
        android:mimeType="MIMEtype"
        android:icon="icon_resources"
        android:summaryColumn="column_name"
        android:detailColumn="column_name">
```


**contained in:**
`<ContactsAccountType>`


**Description:**


Use this element to have the contacts application display the contents of a custom data row as
part of the details of a raw contact. Each `<ContactsDataKind>` child element
of `<ContactsAccountType>` represents a type of custom data row that your sync
adapter adds to the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table. Add one
`<ContactsDataKind>` element for each custom MIME type you use. You don't have
to add the element if you have a custom data row for which you don't want to display data.


**Attributes:**

`android:mimeType`
:
    The custom MIME type you've defined for one of your custom data row types in the
    [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table. For example, the value
    `vnd.android.cursor.item/vnd.example.locationstatus` could be a custom
    MIME type for a data row that records a contact's last known location.

`android:icon`
:
    An Android
    [drawable resource](https://developer.android.com/guide/topics/resources/drawable-resource)
    that the contacts application displays next to your data. Use this to indicate to the
    user that the data comes from your service.

`android:summaryColumn`
:
    The column name for the first of two values retrieved from the data row. The
    value is displayed as the first line of the entry for this data row. The first line is
    intended to be used as a summary of the data, but that is optional. See also
    [android:detailColumn](https://developer.android.com/identity/providers/contacts-provider#detailColumn).

`android:detailColumn`
:
    The column name for the second of two values retrieved from the data row. The value is
    displayed as the second line of the entry for this data row. See also
    `android:summaryColumn`.

## Additional Contacts Provider features


Besides the main features described in previous sections, the Contacts Provider offers
these useful features for working with contacts data:

- Contact groups
- Photo features

### Contact groups


The Contacts Provider can optionally label collections of related contacts with
**group** data. If the server associated with a user account
wants to maintain groups, the sync adapter for the account's account type should transfer
groups data between the Contacts Provider and the server. When users add a new contact to the
server and then put this contact in a new group, the sync adapter must add the new group
to the [ContactsContract.Groups](https://developer.android.com/reference/android/provider/ContactsContract.Groups) table. The group or groups a raw
contact belongs to are stored in the [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table, using
the [ContactsContract.CommonDataKinds.GroupMembership](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.GroupMembership) MIME type.


If you're designing a sync adapter that will add raw contact data from
server to the Contacts Provider, and you aren't using groups, then you need to tell the
Provider to make your data visible. In the code that is executed when a user adds an account
to the device, update the [ContactsContract.Settings](https://developer.android.com/reference/android/provider/ContactsContract.Settings)
row that the Contacts Provider adds for the account. In this row, set the value of the
[Settings.UNGROUPED_VISIBLE](https://developer.android.com/reference/android/provider/ContactsContract.SettingsColumns#UNGROUPED_VISIBLE) column to 1. When you do this, the Contacts Provider will always
make your contacts data visible, even if you don't use groups.

### Contact photos


The [ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table stores photos as rows with MIME type
[Photo.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Photo#CONTENT_ITEM_TYPE). The row's
[CONTACT_ID](https://developer.android.com/reference/android/provider/ContactsContract.RawContactsColumns#CONTACT_ID) column is linked to the
[_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID) column of the raw contact to which it belongs.
The class [ContactsContract.Contacts.Photo](https://developer.android.com/reference/android/provider/ContactsContract.Contacts.Photo) defines a sub-table of
[ContactsContract.Contacts](https://developer.android.com/reference/android/provider/ContactsContract.Contacts) containing photo information for a contact's
primary photo, which is the primary photo of the contact's primary raw contact. Similarly,
the class [ContactsContract.RawContacts.DisplayPhoto](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts.DisplayPhoto) defines a sub-table
of [ContactsContract.RawContacts](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts) containing photo information for a
raw contact's primary photo.


The reference documentation for [ContactsContract.Contacts.Photo](https://developer.android.com/reference/android/provider/ContactsContract.Contacts.Photo) and
[ContactsContract.RawContacts.DisplayPhoto](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts.DisplayPhoto) contain examples of
retrieving photo information. There is no convenience class for retrieving the primary
thumbnail for a raw contact, but you can send a query to the
[ContactsContract.Data](https://developer.android.com/reference/android/provider/ContactsContract.Data) table, selecting on the raw contact's
[_ID](https://developer.android.com/reference/android/provider/BaseColumns#_ID), the
[Photo.CONTENT_ITEM_TYPE](https://developer.android.com/reference/android/provider/ContactsContract.CommonDataKinds.Photo#CONTENT_ITEM_TYPE), and the [IS_PRIMARY](https://developer.android.com/reference/android/provider/ContactsContract.DataColumns#IS_PRIMARY)
column to find the raw contact's primary photo row.


Social stream data for a person may also include photos. These are stored in the
android.provider.ContactsContract.StreamItemPhotos table, which is described in more
detail in the section [Social stream photos](https://developer.android.com/identity/providers/contacts-provider#StreamPhotos).