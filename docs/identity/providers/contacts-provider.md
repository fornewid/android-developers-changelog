---
title: Contacts Provider  |  Identity  |  Android Developers
url: https://developer.android.com/identity/providers/contacts-provider
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Identity](https://developer.android.com/identity)
* [Guides](https://developer.android.com/identity/credential-manager)

# Contacts Provider Stay organized with collections Save and categorize content based on your preferences.




The Contacts Provider is a powerful and flexible Android component that manages the
device's central repository of data about people. The Contacts Provider is the source of data
you see in the device's contacts application, and you can also access its data in your own
application and transfer data between the device and online services. The provider accommodates
a wide range of data sources and tries to manage as much data as possible for each person, with
the result that its organization is complex. Because of this, the provider's API includes an
extensive set of contract classes and interfaces that facilitate both data retrieval and
modification.

This guide describes the following:

* The basic provider structure.
* How to retrieve data from the provider.
* How to modify data in the provider.
* How to write a sync adapter for synchronizing data from your server to the
  Contacts Provider.

This guide assumes that you know the basics of Android content providers. To learn more
about Android content providers, read the
[Content Provider basics](/guide/topics/providers/content-provider-basics) guide.

## Contacts Provider organization

The Contacts Provider is an Android content provider component. It maintains three types of
data about a person, each of which corresponds to a table offered by the provider, as
illustrated in figure 1:

![](/static/images/providers/contacts_structure.png)

**Figure 1.** Contacts Provider table structure.

The three tables are commonly referred to by the names of their contract classes. The classes
define constants for content URIs, column names, and column values used by the tables:

`ContactsContract.Contacts` table
:   Rows representing different people, based on aggregations of raw contact rows.

`ContactsContract.RawContacts` table
:   Rows containing a summary of a person's data, specific to a user account and type.

`ContactsContract.Data` table
:   Rows containing the details for raw contact, such as email addresses or phone numbers.

The other tables represented by contract classes in `ContactsContract`
are auxiliary tables that the Contacts Provider uses to manage its operations or support
specific functions in the device's contacts or telephony applications.

## Raw contacts

A raw contact represents a person's data coming from a single account type and account
name. Because the Contacts Provider allows more than one online service as the source of
data for a person, the Contacts Provider allows multiple raw contacts for the same person.
Multiple raw contacts also allow a user to combine a person's data from more than one account
from the same account type.

Most of the data for a raw contact isn't stored in the
`ContactsContract.RawContacts` table. Instead, it's stored in one or more
rows in the `ContactsContract.Data` table. Each data row has a column
`Data.RAW_CONTACT_ID` that
contains the `RawContacts._ID` value of its
parent `ContactsContract.RawContacts` row.

### Important raw contact columns

The important columns in the `ContactsContract.RawContacts` table are
listed in table 1. Please read the notes that follow after the table:

**Table 1.** Important raw contact columns.

| Column name | Use | Notes |
| --- | --- | --- |
| `ACCOUNT_NAME` | The account name for the account type that's the source of this raw contact. For example, the account name of a Google Account is one of the device owner's Gmail addresses. See the next entry for `ACCOUNT_TYPE` for more information. | The format of this name is specific to its account type. It is not necessarily an email address. |
| `ACCOUNT_TYPE` | The account type that's the source of this raw contact. For example, the account type of a Google Account is `com.google`. Always qualify your account type with a domain identifier for a domain you own or control. This will ensure that your account type is unique. | An account type that offers contacts data usually has an associated sync adapter that synchronizes with the Contacts Provider. |
| `DELETED` | The "deleted" flag for a raw contact. | This flag allows the Contacts Provider to maintain the row internally until sync adapters are able to delete the row from their servers and then finally delete the row from the repository. |

#### Notes

The following are important notes about the
`ContactsContract.RawContacts` table:

* A raw contact's name is not stored in its row in
  `ContactsContract.RawContacts`. Instead, it's stored in
  the `ContactsContract.Data` table, in a
  `ContactsContract.CommonDataKinds.StructuredName` row. A raw contact
  has only one row of this type in the `ContactsContract.Data` table.
* **Caution:** To use your own account data in a raw contact row, it must
  first be registered with the `AccountManager`. To do this, prompt
  users to add the account type and their account name to the list of accounts. If you don't
  do this, the Contacts Provider will automatically delete your raw contact row.

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

* `emily.dickinson@gmail.com`
* `emilyd@gmail.com`
* Twitter account "belle\_of\_amherst"

This user has enabled *Sync Contacts* for all three of these accounts in the
*Accounts* settings.

Suppose Emily Dickinson opens a browser window, logs into Gmail as
`emily.dickinson@gmail.com`, opens
Contacts, and adds "Thomas Higginson". Later on, she logs into Gmail as
`emilyd@gmail.com` and sends an email to "Thomas Higginson", which automatically
adds him as a contact. She also follows "colonel\_tom" (Thomas Higginson's Twitter ID) on
Twitter.

The Contacts Provider creates three raw contacts as a result of this work:

1. A raw contact for "Thomas Higginson" associated with `emily.dickinson@gmail.com`.
   The user account type is Google.
2. A second raw contact for "Thomas Higginson" associated with `emilyd@gmail.com`.
   The user account type is also Google. There is a second raw contact even
   though the name is identical to a previous name, because the person was added for a
   different user account.
3. A third raw contact for "Thomas Higginson" associated with "belle\_of\_amherst". The user
   account type is Twitter.

## Data

As noted previously, the data for a raw contact is stored in a
`ContactsContract.Data` row that is linked to the raw contact's
`_ID` value. This allows a single raw contact to have multiple instances of the same
type of data such as email addresses or phone numbers. For example, if
"Thomas Higginson" for `emilyd@gmail.com` (the raw contact row for Thomas Higginson
associated with the Google Account `emilyd@gmail.com`) has a home email address of
`thigg@gmail.com` and a work email address of
`thomas.higginson@gmail.com`, the Contacts Provider stores the two email address
rows and links them both to the raw contact.

Notice that different types of data are stored in this single table. Display name,
phone number, email, postal address, photo, and website detail rows are all found in the
`ContactsContract.Data` table. To help manage this, the
`ContactsContract.Data` table has some columns with descriptive names,
and others with generic names. The contents of a descriptive-name column have the same meaning
regardless of the type of data in the row, while the contents of a generic-name column have
different meanings depending on the type of data.

### Descriptive column names

Some examples of descriptive column names are:

`RAW_CONTACT_ID`
:   The value of the `_ID` column of the raw contact for this data.

`MIMETYPE`
:   The type of data stored in this row, expressed as a custom MIME type. The Contacts Provider
    uses the MIME types defined in the subclasses of
    `ContactsContract.CommonDataKinds`. These MIME types are open source,
    and can be used by any application or sync adapter that works with the Contacts Provider.

`IS_PRIMARY`
:   If this type of data row can occur more than once for a raw contact, the
    `IS_PRIMARY` column flags
    the data row that contains the primary data for the type. For example, if
    the user long-presses a phone number for a contact and selects **Set default**,
    then the `ContactsContract.Data` row containing that number
    has its `IS_PRIMARY` column set to a
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
`ContactsContract.CommonDataKinds`. The constants simply give a
different constant name to the same column name, which helps you access data in a row of a
particular type.

For example, the `ContactsContract.CommonDataKinds.Email` class defines
type-specific column name constants for a `ContactsContract.Data` row
that has the MIME type
`Email.CONTENT_ITEM_TYPE`. The class contains the constant
`ADDRESS` for the email address
column. The actual value of
`ADDRESS` is "data1", which is
the same as the column's generic name.

**Caution:** Don't add your own custom data to the
`ContactsContract.Data` table using a row that has one of the
provider's pre-defined MIME types. If you do, you may lose the data or cause the provider to
malfunction. For example, you should not add a row with the MIME type
`Email.CONTENT_ITEM_TYPE` that contains a user name instead of an email address in the
column `DATA1`. If you use your own custom MIME type for the row, then you are free
to define your own type-specific column names and use the columns however you wish.

Figure 2 shows how descriptive columns and data columns appear in a
`ContactsContract.Data` row, and how type-specific column names "overlay"
the generic column names

![How type-specific column names map to generic column names](/static/images/providers/data_columns.png)

**Figure 2.** Type-specific column names and generic column names.

### Type-specific column name classes

Table 2 lists the most commonly-used type-specific column name classes:

**Table 2.** Type-specific column name classes

| Mapping class | Type of data | Notes |
| --- | --- | --- |
| `ContactsContract.CommonDataKinds.StructuredName` | The name data for the raw contact associated with this data row. | A raw contact has only one of these rows. |
| `ContactsContract.CommonDataKinds.Photo` | The main photo for the raw contact associated with this data row. | A raw contact has only one of these rows. |
| `ContactsContract.CommonDataKinds.Email` | An email address for the raw contact associated with this data row. | A raw contact can have multiple email addresses. |
| `ContactsContract.CommonDataKinds.StructuredPostal` | A postal address for the raw contact associated with this data row. | A raw contact can have multiple postal addresses. |
| `ContactsContract.CommonDataKinds.GroupMembership` | An identifier that links the raw contact to one of the groups in the Contacts Provider. | Groups are an optional feature of an account type and account name. They're described in more detail in the section [Contact groups](#Groups). |

### Contacts

The Contacts Provider combines the raw contact rows across all account types and account names
to form a **contact**. This facilitates displaying and modifying all the data a
user has collected for a person. The Contacts Provider manages the creation of new contact
rows, and the aggregation of raw contacts with an existing contact row. Neither applications nor
sync adapters are allowed to add contacts, and some columns in a contact row are read-only.

**Note:** If you try to add a contact to the Contacts Provider with an
`insert()`, you'll get
an `UnsupportedOperationException` exception. If you try to update a column
that's listed as "read-only," the update is ignored.

The Contacts Provider creates a new contact in response to the addition of a new raw contact
that doesn't match any existing contacts. The provider also does this if an existing raw
contact's data changes in such a way that it no longer matches the contact to which it was
previously attached. If an application or sync adapter creates a new raw contact that
*does* match an existing contact, the new raw contact is aggregated to the existing
contact.

The Contacts Provider links a contact row to its raw contact rows with the contact row's
`_ID` column in the `Contacts`
table. The `CONTACT_ID` column of the raw contacts table
`ContactsContract.RawContacts` contains `_ID` values for
the contacts row associated with each raw contacts row.

The `ContactsContract.Contacts` table also has the column
`LOOKUP_KEY` that is a
"permanent" link to the contact row. Because the Contacts Provider maintains contacts
automatically, it may change a contact row's `_ID` value
in response to an aggregation or sync. Even If this happens, the content URI
`CONTENT_LOOKUP_URI` combined with
contact's `LOOKUP_KEY` will still
point to the contact row, so you can use
`LOOKUP_KEY`
to maintain links to "favorite" contacts, and so forth. This column has its own format that is
unrelated to the format of the `_ID` column.

Figure 3 shows how the three main tables relate to each other.

![Contacts provider main tables](/static/images/providers/contacts_tables.png)