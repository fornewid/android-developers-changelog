---
title: https://developer.android.com/identity/providers/contacts-provider/contacts-storage-locations
url: https://developer.android.com/identity/providers/contacts-provider/contacts-storage-locations
source: md.txt
---

Apps may allow users to create and store contacts. These contacts can typically
be saved in two locations:

1. **Cloud account**: Save contacts to an account associated with a cloud service (such as Google Cloud) to allow synchronization and backup of contacts.
2. **Local account**: Contacts can be stored locally on the device.

Users can set their preferred storage location in the device settings. This
preferred location is known as the **default account**, and is used when
creating contacts. Apps should respect this preference. This document explains
how to work with different contact storage locations, including cloud accounts
and the local accounts, and implement best practices for managing user
preferences. The local account refers to storing contacts directly on the
device.

### Retrieve the default account

To determine the default account for new contacts, use the
[`ContactsContract.RawContacts.DefaultAccount`](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts.DefaultAccount)

Call [`getDefaultAccountForNewContacts()`](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts.DefaultAccount#getDefaultAccountForNewContacts(android.content.ContentResolver)) to get the
[`ContactsContrast.RawContacts.DefaultAccount.DefaultAccountAndState`](https://developer.android.com/reference/android/provider/ContactsContract.RawContacts.DefaultAccount.DefaultAccountAndState)
object. This object contains information about the default account setting.  

### Kotlin

    import ContactsContrast.RawContacts
    import ContactsContrast.RawContacts.DefaultAccount
    import ContactsContrast.RawContacts.DefaultAccount.DefaultAccountAndState

    val defaultAccountAndState: DefaultAccountAndState =
      DefaultAccount.getDefaultAccountForNewContacts(
          getContentResolver()
      )

### Java

    import ContactsContrast.RawContacts;
    import ContactsContrast.RawContacts.DefaultAccount;
    import ContactsContrast.RawContacts.DefaultAccount.DefaultAccountAndState;

    DefaultAccountAndState defaultAccountAndState =
      DefaultAccount.getDefaultAccountForNewContacts(
        getContentResolver()
      );

The `DefaultAccountAndState` object contains:

- State: Indicates whether a default account is set and, if so, the category of that account (cloud, local, or SIM).
- Account: Provides the specific account details (name and type) if the state is `DEFAULT_ACCOUNT_STATE_CLOUD or DEFAULT_ACCOUNT_STATE_SIM`. It will be null for other states, including `DEFAULT_ACCOUNT_STATE_LOCAL`.

| **Note:** For the local account (`DEFAULT_ACCOUNT_STATE_LOCAL`), you can retrieve the account information using `RawContacts.getLocalAccountName()` and `RawContacts.getLocalAccountType()`.

Here's an example of how to parse the `DefaultAccountAndState` object:  

### Kotlin

    // Retrieves the state of default account.
    val defaultAccountState = defaultAccountAndState.state
    var defaultAccountName: String? = null
    var defaultAccountType: String? = null

    when (defaultAccountState) {
        // Default account is set to a cloud or a SIM account.
        DefaultAccountState.DEFAULT_ACCOUNT_STATE_CLOUD,
        DefaultAccountState.DEFAULT_ACCOUNT_STATE_SIM -> {
            defaultAccountName = defaultAccountAndState.account?.name
            defaultAccountType = defaultAccountAndState.account?.type
        }
        // Default account is set to the local account on the device.
        DefaultAccountState.DEFAULT_ACCOUNT_STATE_LOCAL -> {
            defaultAccountName = RawContacts.getLocalAccountType()
            defaultAccountType = RawContacts.getLocalAccountName()
        }
        // Default account is not set.
        DefaultAccountState.DEFAULT_ACCOUNT_STATE_NOT_SET -> {
        }
    }

### Java

    // Retrieves the state of default account.
    var defaultAccountState = defaultAccountAndState.getState();
    String defaultAccountName = null;
    String defaultAccountType = null;

    switch (defaultAccountState) {
      // Default account is set to a cloud or a SIM account.
      case DefaultAccountState.DEFAULT_ACCOUNT_STATE_CLOUD:
      case DefaultAccountState.DEFAULT_ACCOUNT_STATE_SIM:
        defaultAccountName = defaultAccountAndState.getAccount().name;
        defaultAccountType = defaultAccountAndState.getAccount().type;
        break;
      // Default account is set to the local account on the device.
      case  DefaultAccountState.DEFAULT_ACCOUNT_STATE_LOCAL:
        defaultAccountName = RawContacts.getLocalAccountType();
        defaultAccountType = RawContacts.getLocalAccountName();
        break;

      // Default account is not set.
      case DefaultAccountState.DEFAULT_ACCOUNT_STATE_NOT_SET:
        break;
    }

### Create contacts without specifying an account

If the default account is set, your app usually doesn't need to explicitly
specify an account when creating contacts. The system automatically saves
the new contact to the default account. Here's how to create a contact without
specifying an account.

Create a new `ArrayList` of `ContentProviderOperation` objects. This list
holds the operations to insert the raw contact and its associated data.  

### Kotlin

    val ops = ArrayList<ContentProviderOperation>()

### Java

    ArrayList<ContentProviderOperation> ops =
            new ArrayList<ContentProviderOperation>();

Create a new `ContentProviderOperation` to insert the raw contact. Since you're
not specifying an account, you don't need to include the `ACCOUNT_TYPE` and
`ACCOUNT_NAME`.  

### Kotlin

    val op = ContentProviderOperation.newInsert(
        ContactsContract.RawContacts.CONTENT_URI
    )
    ops.add(op.build())

### Java

    ContentProviderOperation.Builder op =
        ContentProviderOperation.newInsert(
            ContactsContract.RawContacts.CONTENT_URI
        );
    ops.add(op.build());

Add other `ContentProviderOperation` objects to the ops list to include the
contact fields (like name, phone number, email). Then execute the batch
operation to create the contact.  

### Kotlin

    try {
        getContentResolver().applyBatch(
            ContactsContract.AUTHORITY, ops
        )
    } catch (e: Exception) {
        // Handle exceptions
    }

### Java

    try {
        getContentResolver().applyBatch(
            ContactsContract.AUTHORITY, ops
        );
    } catch (Exception e) {
        // Handle exceptions
    }

### Create contacts in a cloud account

To create a contact in a cloud account, insert the raw contact row into the
`ContactsContract.RawContacts` table and specify the cloud account. Here's how:

Create a new `ArrayList` of `ContentProviderOperation` objects.  

### Kotlin

    val ops = ArrayList<ContentProviderOperation>()

### Java

    ArrayList<ContentProviderOperation> ops =
        new ArrayList<ContentProviderOperation>();

Create a new `ContentProviderOperation` to insert the raw contact. Use the
`withValue()` method to specify the account type and account name of the
selected cloud account.  

### Kotlin

    val op = ContentProviderOperation.newInsert(
        ContactsContract.RawContacts.CONTENT_URI
    )
        .withValue(
            ContactsContract.RawContacts.ACCOUNT_TYPE,
            selectedAccount.type
        )
        .withValue(
            ContactsContract.RawContacts.ACCOUNT_NAME,
            selectedAccount.name
        )
    ops.add(op.build())

### Java

    ContentProviderOperation.Builder op =
        ContentProviderOperation.newInsert(
            ContactsContract.RawContacts.CONTENT_URI
        )
            .withValue(
                ContactsContract.RawContacts.ACCOUNT_TYPE,
                selectedAccount.getType()
            )
            .withValue(
                ContactsContract.RawContacts.ACCOUNT_NAME,
                selectedAccount.getName()
            );
    ops.add(op.build());

Add other `ContentProviderOperation` objects to the ops list to include the
contact fields and execute the batch operation to create the contact.

### Create contacts in the local account

| **Caution:** When the default account is set to a cloud account (`DEFAULT_ACCOUNT_STATE_CLOUD`), contacts should only be created in the cloud account. Avoid creating contacts in the local account or any SIM accounts in this scenario.

To create a contact in the local account, insert a new raw contact row into the
`ContactsContract.RawContacts` table and specify the account information for the
local account:

Create a new `ArrayList` of `ContentProviderOperation` objects.  

### Kotlin

    val ops = ArrayList<ContentProviderOperation>()

### Java

    ArrayList<ContentProviderOperation> ops =
        new ArrayList<ContentProviderOperation>();

Create a new `ContentProviderOperation` to insert the raw contact. Use
`ContactsContract.RawContacts.getLocalAccountName()` and
`ContactsContract.RawContacts.getLocalAccountType()` to specify the account
information for the local account.  

### Kotlin

    val op = ContentProviderOperation.newInsert(
        ContactsContract.RawContacts.CONTENT_URI
    )
        .withValue(
            ContactsContract.RawContacts.ACCOUNT_TYPE,
            ContactsContract.RawContacts.getLocalAccountType()
        )
        .withValue(
            ContactsContract.RawContacts.ACCOUNT_NAME,
            ContactsContract.RawContacts.getLocalAccountName()
        )
    ops.add(op.build())

### Java

    ContentProviderOperation.Builder op =
        ContentProviderOperation.newInsert(
            ContactsContract.RawContacts.CONTENT_URI
        )
            .withValue(
                ContactsContract.RawContacts.ACCOUNT_TYPE,
                ContactsContract.RawContacts.getLocalAccountType()
            )
            .withValue(
                ContactsContract.RawContacts.ACCOUNT_NAME,
                ContactsContract.RawContacts.getLocalAccountName()
            );
    ops.add(op.build());

Add other `ContentProviderOperation` objects to the ops list to include the
contact fields, and execute the batch operations to create the contact.