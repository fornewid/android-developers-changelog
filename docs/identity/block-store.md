---
title: https://developer.android.com/identity/block-store
url: https://developer.android.com/identity/block-store
source: md.txt
---

> [!IMPORTANT]
> **Important:** For an updated user experience and other improvements, consider using [Passkeys with Credential Manager](https://developer.android.com/identity/sign-in/credential-manager) instead.

Many users still manage their own credentials when setting up a new
Android-powered device. This manual process can become challenging and often
results in a poor user experience. The Block Store API, a library powered by
[Google Play services](https://developers.google.com/android), looks to solve this by providing a way for
apps to save user credentials without the complexity or security risk associated
with saving user passwords.

The Block Store API allows your app to store data that it can later
retrieve to re-authenticate users on a new device. This helps provide a more
seamless experience for the user, as they don't need to see a sign-in screen
when launching your app for the first time on the new device.

The benefits to using Block Store include the following:

- Encrypted credential storage solution for developers. Credentials are end-to-end encrypted when possible.
- Save tokens instead of usernames and passwords.
- Eliminate friction from sign-in flows.
- Save users from the burden of managing complex passwords.
- Google verifies the user's identity.

> [!NOTE]
> **Note:** Using Block Store does not limit the user to what type of credentials can be used. Users can sign in with their username and password, their Google Account, or any other federated identity provider, and Block Store still works.

## Before you begin

To prepare your app, complete the steps in the following sections.

### Configure your app

In your project-level `build.gradle` file, include [Google's Maven
repository](https://maven.google.com/web/index.html) in both your `buildscript`
and `allprojects` sections:

    buildscript {
      repositories {
        google()
        mavenCentral()
      }
    }

    allprojects {
      repositories {
        google()
        mavenCentral()
      }
    }

Add the [Google Play services](https://developers.google.com/android) dependency for the Block Store API
to your [module's Gradle build file](https://developer.android.com/studio/build#module-level), which is commonly `app/build.gradle`:

    dependencies {
      implementation 'com.google.android.gms:play-services-auth-blockstore:16.4.0'
    }

## How it works

Block Store allows developers to save and restore up to 16 byte arrays. This
lets you save important information regarding the current user session and
offers the flexibility to save this information however you like. This data can
be end-to-end encrypted and the infrastructure that supports Block Store is
built on top of the Backup and Restore infrastructure.

This guide will cover the use case of saving a user's token to Block Store.
The following steps outline how an app utilizing Block Store would work:

1. During your app's authentication flow, or anytime thereafter, you can store the user's authentication token to Block Store for later retrieval.
2. The token will be stored locally and can also be backed up to the cloud, end-to-end encrypted when possible.
3. Data is transferred when the user initiates a restore flow on a new device.
4. If the user restores your app during the restore flow, your app can then retrieve the saved token from Block Store on the new device.

### Saving the token

When a user signs into your app, you can save the authentication token that you
generate for that user to Block Store. You can store this token using a unique
key pair value that has a maximum 4kb per entry. To store the token, call
[`setBytes()`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/StoreBytesData.Builder#public-storebytesdata.builder-setbytes-byte%5B%5D-bytes) and [`setKey()`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/StoreBytesData.Builder.html#setKey) on an instance of
[`StoreBytesData.Builder`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/StoreBytesData.Builder) to store the user's credentials to the source
device. After you save the token with Block Store, the token is encrypted and
stored locally on the device.

The following sample shows how to save the authentication token to
the local device:

### Java

```java
  BlockstoreClient client = Blockstore.getClient(this);
  byte[] bytes1 = new byte[] { 1, 2, 3, 4 };  // Store one data block.
  String key1 = "com.example.app.key1";
  StoreBytesData storeRequest1 = StoreBytesData.Builder()
          .setBytes(bytes1)
          // Call this method to set the key value pair the data should be associated with.
          .setKeys(Arrays.asList(key1))
          .build();
  client.storeBytes(storeRequest1)
    .addOnSuccessListener(result -> Log.d(TAG, "stored " + result + " bytes"))
    .addOnFailureListener(e -> Log.e(TAG, "Failed to store bytes", e));
```

### Kotlin

```kotlin
  val client = Blockstore.getClient(this)

  val bytes1 = byteArrayOf(1, 2, 3, 4) // Store one data block.
  val key1 = "com.example.app.key1"
  val storeRequest1 = StoreBytesData.Builder()
    .setBytes(bytes1) // Call this method to set the key value with which the data should be associated with.
    .setKeys(Arrays.asList(key1))
    .build()
  client.storeBytes(storeRequest1)
    .addOnSuccessListener { result: Int ->
      Log.d(TAG,
            "Stored $result bytes")
    }
    .addOnFailureListener { e ->
      Log.e(TAG, "Failed to store bytes", e)
    }
```

> [!NOTE]
> **Note:** **Previously stored bytes without a key?** If you have previously used the `StoreBytes()` API to save your data, it is recommended that you start saving your tokens with a key. Data previously saved using StoreBytes is now saved with the key `BlockstoreClient.DEFAULT_BYTES_DATA_KEY`.

#### Use default token

Data saved using StoreBytes without a key uses the default key
`BlockstoreClient.DEFAULT_BYTES_DATA_KEY`.

### Java

```java
  BlockstoreClient client = Blockstore.getClient(this);
  // The default key BlockstoreClient.DEFAULT_BYTES_DATA_KEY.
  byte[] bytes = new byte[] { 9, 10 };
  StoreBytesData storeRequest = StoreBytesData.Builder()
          .setBytes(bytes)
          .build();
  client.storeBytes(storeRequest)
    .addOnSuccessListener(result -> Log.d(TAG, "stored " + result + " bytes"))
    .addOnFailureListener(e -> Log.e(TAG, "Failed to store bytes", e));
```

### Kotlin

```kotlin
  val client = Blockstore.getClient(this);
  // the default key BlockstoreClient.DEFAULT_BYTES_DATA_KEY.
  val bytes = byteArrayOf(1, 2, 3, 4)
  val storeRequest = StoreBytesData.Builder()
    .setBytes(bytes)
    .build();
  client.storeBytes(storeRequest)
    .addOnSuccessListener { result: Int ->
      Log.d(TAG,
            "stored $result bytes")
    }
    .addOnFailureListener { e ->
      Log.e(TAG, "Failed to store bytes", e)
    }
```

> [!NOTE]
> **Note:** On device, Block Store data is stored in Google Play services' local private data directory. No other apps can directly access the data file. They can only access Block Store data using `retrieveBytes()` API, and an app can only retrieve data stored by itself. Google Play services checks both the package name and signature.

### Retrieving the token

Later on, when a user goes through the restore flow on a new device, Google Play
services first verifies the user, then retrieves your Block Store data. The user
has already agreed to restore your app data as a part of the restore flow, so no
additional consents are required. When the user opens your app, you can request
your token from Block Store by calling [`retrieveBytes()`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/BlockstoreClient.html#retrieveBytes()). The retrieved
token can then be used to keep the user signed in on the new device.

The following sample shows how to retrieve multiple tokens based on specific
keys.

### Java

```java
BlockstoreClient client = Blockstore.getClient(this);

// Retrieve data associated with certain keys.
String key1 = "com.example.app.key1";
String key2 = "com.example.app.key2";
String key3 = BlockstoreClient.DEFAULT_BYTES_DATA_KEY; // Used to retrieve data stored without a key

List requestedKeys = Arrays.asList(key1, key2, key3); // Add keys to array
RetrieveBytesRequest retrieveRequest = new RetrieveBytesRequest.Builder()
    .setKeys(requestedKeys)
    .build();

client.retrieveBytes(retrieveRequest)
    .addOnSuccessListener(
        result -> {
          Map<String, BlockstoreData> blockstoreDataMap = result.getBlockstoreDataMap();
          for (Map.Entry<String, BlockstoreData> entry : blockstoreDataMap.entrySet()) {
            Log.d(TAG, String.format(
                "Retrieved bytes %s associated with key %s.",
                new String(entry.getValue().getBytes()), entry.getKey()));
          }
        })
    .addOnFailureListener(e -> Log.e(TAG, "Failed to store bytes", e));
```

### Kotlin

```kotlin
val client = Blockstore.getClient(this)

// Retrieve data associated with certain keys.
val key1 = "com.example.app.key1"
val key2 = "com.example.app.key2"
val key3 = BlockstoreClient.DEFAULT_BYTES_DATA_KEY // Used to retrieve data stored without a key

val requestedKeys = Arrays.asList(key1, key2, key3) // Add keys to array

val retrieveRequest = RetrieveBytesRequest.Builder()
  .setKeys(requestedKeys)
  .build()

client.retrieveBytes(retrieveRequest)
  .addOnSuccessListener { result: RetrieveBytesResponse ->
    val blockstoreDataMap =
      result.blockstoreDataMap
    for ((key, value) in blockstoreDataMap) {
      Log.d(ContentValues.TAG, String.format(
        "Retrieved bytes %s associated with key %s.",
        String(value.bytes), key))
    }
  }
  .addOnFailureListener { e: Exception? ->
    Log.e(ContentValues.TAG,
          "Failed to store bytes",
          e)
  }
```

#### Retrieving all tokens.

Below is an example of how to retrieve all the tokens saved to BlockStore.

### Java

```java
BlockstoreClient client = Blockstore.getClient(this)

// Retrieve all data.
RetrieveBytesRequest retrieveRequest = new RetrieveBytesRequest.Builder()
    .setRetrieveAll(true)
    .build();

client.retrieveBytes(retrieveRequest)
    .addOnSuccessListener(
        result -> {
          Map<String, BlockstoreData> blockstoreDataMap = result.getBlockstoreDataMap();
          for (Map.Entry<String, BlockstoreData> entry : blockstoreDataMap.entrySet()) {
            Log.d(TAG, String.format(
                "Retrieved bytes %s associated with key %s.",
                new String(entry.getValue().getBytes()), entry.getKey()));
          }
        })
    .addOnFailureListener(e -> Log.e(TAG, "Failed to store bytes", e));
```

### Kotlin

```kotlin
val client = Blockstore.getClient(this)

val retrieveRequest = RetrieveBytesRequest.Builder()
  .setRetrieveAll(true)
  .build()

client.retrieveBytes(retrieveRequest)
  .addOnSuccessListener { result: RetrieveBytesResponse ->
    val blockstoreDataMap =
      result.blockstoreDataMap
    for ((key, value) in blockstoreDataMap) {
      Log.d(ContentValues.TAG, String.format(
        "Retrieved bytes %s associated with key %s.",
        String(value.bytes), key))
    }
  }
  .addOnFailureListener { e: Exception? ->
    Log.e(ContentValues.TAG,
          "Failed to store bytes",
          e)
  }
```

> [!NOTE]
> **Note:** **retrieveBytes() deprecation.** `retrieveBytes()` is now deprecated. To retrieve bytes, the key `BlockstoreClient.DEFAULT_BYTES_DATA_KEY` can be used in the `RetrieveBytesRequest` instance in order to get your saved data

Below is an example of how to retrieve the default key.

### Java

```java
BlockStoreClient client = Blockstore.getClient(this);
RetrieveBytesRequest retrieveRequest = new RetrieveBytesRequest.Builder()
    .setKeys(Arrays.asList(BlockstoreClient.DEFAULT_BYTES_DATA_KEY))
    .build();
client.retrieveBytes(retrieveRequest);
```

### Kotlin

```kotlin
val client = Blockstore.getClient(this)

val retrieveRequest = RetrieveBytesRequest.Builder()
  .setKeys(Arrays.asList(BlockstoreClient.DEFAULT_BYTES_DATA_KEY))
  .build()
client.retrieveBytes(retrieveRequest)
```

### Deleting tokens

Deleting tokens from BlockStore may be required for the following reasons:

- User goes through sign out user flow.
- Token has been revoked or is invalid.

Similar to retrieving tokens, you can specify which tokens need deleting by
setting an array of keys which require deletion.

The following example demonstrates how to delete certain keys:

### Java

```java
BlockstoreClient client = Blockstore.getClient(this);

// Delete data associated with certain keys.
String key1 = "com.example.app.key1";
String key2 = "com.example.app.key2";
String key3 = BlockstoreClient.DEFAULT_BYTES_DATA_KEY; // Used to delete data stored without key

List requestedKeys = Arrays.asList(key1, key2, key3) // Add keys to array
DeleteBytesRequest deleteRequest = new DeleteBytesRequest.Builder()
      .setKeys(requestedKeys)
      .build();
client.deleteBytes(deleteRequest)
```

### Kotlin

```kotlin
val client = Blockstore.getClient(this)

// Retrieve data associated with certain keys.
val key1 = "com.example.app.key1"
val key2 = "com.example.app.key2"
val key3 = BlockstoreClient.DEFAULT_BYTES_DATA_KEY // Used to retrieve data stored without a key

val requestedKeys = Arrays.asList(key1, key2, key3) // Add keys to array

val retrieveRequest = DeleteBytesRequest.Builder()
      .setKeys(requestedKeys)
      .build()

client.deleteBytes(retrieveRequest)
```

#### Delete All Tokens

The following example shows how to delete all the tokens currently saved to
BlockStore:

### Java

```java
// Delete all data.
DeleteBytesRequest deleteAllRequest = new DeleteBytesRequest.Builder()
      .setDeleteAll(true)
      .build();
client.deleteBytes(deleteAllRequest)
.addOnSuccessListener(result -> Log.d(TAG, "Any data found and deleted? " + result));
```

### Kotlin

<br />

      val deleteAllRequest = DeleteBytesRequest.Builder()
      .setDeleteAll(true)
      .build()
    retrieve bytes, the key BlockstoreClient.DEFAULT_BYTES_DATA_KEY can be used
    in the RetrieveBytesRequest instance in order to get your saved data

The following example shows how to retrieve the default key.

### Java

### End-to-end encryption

In order for end-to-end encryption to be made available, the device must be
running Android 9 or higher, and the user must have set a screen lock
(PIN, pattern, or password) for their device. You can verify if encryption will
be available on the device by calling [`isEndToEndEncryptionAvailable()`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/BlockstoreClient#isEndToEndEncryptionAvailable()).

The following sample shows how to verify if encryption will be available during
cloud backup:

    client.isEndToEndEncryptionAvailable()
            .addOnSuccessListener { result ->
              Log.d(TAG, "Will Block Store cloud backup be end-to-end encrypted? $result")
            }

> [!NOTE]
> **Note:** It is recommended to verify that end-to-end encryption is available prior to enabling cloud backup.

### Enable cloud backup

To enable cloud backup, add the [`setShouldBackupToCloud()`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/StoreBytesData#shouldBackupToCloud()) method to your
[`StoreBytesData`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/StoreBytesData) object. Block Store will periodically backup to cloud the
bytes stored when `setShouldBackupToCloud()` is set as true.

The following sample shows how to enable cloud backup **only when cloud backup
is end-to-end encrypted**:

    val client = Blockstore.getClient(this)
    val storeBytesDataBuilder = StoreBytesData.Builder()
            .setBytes(/* BYTE_ARRAY */)

    client.isEndToEndEncryptionAvailable()
            .addOnSuccessListener { isE2EEAvailable ->
              if (isE2EEAvailable) {
                storeBytesDataBuilder.setShouldBackupToCloud(true)
                Log.d(TAG, "E2EE is available, enable backing up bytes to the cloud.")

                client.storeBytes(storeBytesDataBuilder.build())
                    .addOnSuccessListener { result ->
                      Log.d(TAG, "stored: ${result.getBytesStored()}")
                    }.addOnFailureListener { e ->
                      Log.e(TAG, "Failed to store bytes", e)
                    }
              } else {
                Log.d(TAG, "E2EE is not available, only store bytes for D2D restore.")
              }
            }

> [!NOTE]
> **Note:** If [`storeBytes`](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/BlockstoreClient#public-abstract-taskinteger-storebytes-storebytesdata-storebytesdata) is called with `shouldBackupToCloud` **unset** or set as **false**, then this device's bytes previously backed up to cloud will be deleted from the cloud upon next periodic sync.

## How to test

Use the following methods during development in order to test the restore
flows.

### Same device uninstall/reinstall

If the user enables Backup services
(it can be checked at **Settings \> Google \> Backup**), Block Store data is
persisted across the app uninstall/reinstall.

You can follow these steps to test:

1. Integrate the Block Store API to your test app.
2. Use the test app to invoke the Block Store API to store your data.
3. Uninstall your test app and then reinstall your app on the same device.
4. Use the test app to invoke the Block Store API to retrieve your data.
5. Verify that the bytes retrieved are the same as what were stored before uninstallation.

> [!NOTE]
> **Note:** Since it takes more steps to test cross-device restore, it's recommended to first verify the integration of your app with the Block Store API using the uninstall/reinstall case.

### Device-to-device

In most cases, this will require a factory reset of the target device. You can
then enter the [Android wireless restore flow](https://developer.android.com/identity/block-store/testing-restore-flows#android_wireless_restore) or [Google cable restore](https://developer.android.com/identity/block-store/testing-restore-flows#google_cable_restore)
(for supported devices).

> [!NOTE]
> **Note:** If the target device is a Samsung Galaxy, you can enter the restore flow by launching [Smart Switch](https://www.samsung.com/us/support/owners/app/smart-switch) outside of setup.

### Cloud restore

1. Integrate the Block Store API to your test app. The test app needs to be submitted to the Play Store.
2. On the source device, use the test app to invoke the Block Store API to store your data, with `shouldBackUpToCloud` set to `true`.
3. For O and above devices, you can manually trigger a Block Store cloud backup: go to **Settings \> Google \> Backup** , click the "Backup Now" button.
   1. To verify that Block Store cloud backup succeeded, you can:
      1. After the backup finishes, search for log lines with tag "CloudSyncBpTkSvc".
      2. You should see lines like this: "......, CloudSyncBpTkSvc: sync result: SUCCESS, ..., uploaded size: XXX bytes ..."
   2. After a Block Store cloud backup, there's a 5-minute "cool down" period. Within that 5 minutes, clicking the "Backup Now" button won't trigger another Block Store cloud backup.
4. Factory reset the target device and go through a cloud restore flow. Select to restore your test app during the restore flow. For more information about cloud restore flows, see [Supported cloud restore flows](https://developer.android.com/identity/block-store/testing-restore-flows#supported_cloud_restore_flow).
5. On the target device, use the test app to invoke the Block store API to retrieve your data.
6. Verify that the bytes retrieved are the same as what were stored in the source device.

## Device Requirements

### End to End Encryption

- End to End encryption is supported on devices running Android 9 (API 29) and above.
- The device must have a screen lock set with a PIN, pattern, or password for end to end encryption to be enabled and correctly encrypt the user's data.

> [!NOTE]
> **Note:** [isEndtoEndEncryptionAvailable()](https://developers.google.com/android/reference/com/google/android/gms/auth/blockstore/StoreBytesData#public-abstract-taskboolean-isendtoendencryptionavailable) will return false if any of these conditions is not met.

### Device to Device Restore Flow

Device to device restore will require you to have a source device and a target
device. These will be the two devices which are transferring data.

**Source** devices must be running Android 6 (API 23) and above to backup.

**Target** devices running Android 9 (API 29) and above to have the ability
to restore.

More information on the device to device restore flow can be found [here](https://developer.android.com/identity/block-store/testing-restore-flows#supported_cloud_restore_flow).

### Cloud Backup and Restore Flow

Cloud backup and restore will require a source device and a target device.

**Source** devices must be running Android 6 (API 23) and above to backup.

**Target** devices are supported based on their vendors. Pixel devices can
use this feature from Android 9 (API 29) and all other devices must be running
Android 12 (API 31) or above.