---
title: https://developer.android.com/training/data-storage/shared/datasets
url: https://developer.android.com/training/data-storage/shared/datasets
source: md.txt
---

Starting in Android 11 (API level 30), the system caches large datasets that
multiple apps might access for use cases like machine learning and media
playback. This functionality helps reduce data redundancy, both over the network
and on disk.

When your app needs access to a shared large dataset, it can first look for
these cached datasets, called *shared data blobs* , before determining whether to
download a new copy. Apps can access these shared datasets functionality using
the APIs in [`BlobStoreManager`](https://developer.android.com/reference/android/app/blob/BlobStoreManager).

The system maintains the shared data blobs and controls which apps can access
them. When your app contributes data blobs, you can indicate which other apps
should have access by calling one of the following methods:

- To grant access to a specific set of apps on a device, pass the package names of these apps into [`allowPackageAccess()`](https://developer.android.com/reference/android/app/blob/BlobStoreManager.Session#allowPackageAccess(java.lang.String,%20byte%5B%5D)).
- To allow only apps whose certificates are signed using the same key as the one used for your app---such as an app suite that you manage---call [`allowSameSignatureAccess()`](https://developer.android.com/reference/android/app/blob/BlobStoreManager.Session#allowSameSignatureAccess()).
- To grant access to all apps on a device, call [`allowPublicAccess()`](https://developer.android.com/reference/android/app/blob/BlobStoreManager.Session#allowPublicAccess()).

## Access shared data blobs

The system represents each shared data blob using a
[`BlobHandle`](https://developer.android.com/reference/android/app/blob/BlobHandle) object. Each instance of `BlobHandle`
contains a cryptographically-secure hash and some identifying details for the
dataset.

To access shared data blobs, download identifying details from the server. Using
these details, check whether the dataset is already available on the system.

The next step depends on whether data is available.

### Dataset available

If the dataset is already available on the device, then access it from the system,
as shown in the following code snippet:  

### Kotlin

```kotlin
val blobStoreManager =
        getSystemService(Context.BLOB_STORE_SERVICE) as BlobStoreManager
// The label "Sample photos" is visible to the user.
val blobHandle = BlobHandle.createWithSha256(sha256DigestBytes,
        "Sample photos",
        System.currentTimeMillis() + TimeUnit.DAYS.toMillis(1),
        "photoTrainingDataset")
try {
    val input = ParcelFileDescriptor.AutoCloseInputStream(
            blobStoreManager.openBlob(blobHandle))
    useDataset(input)
}
```

### Java

```java
BlobStoreManager blobStoreManager =
        ((BlobStoreManager) getSystemService(Context.BLOB_STORE_SERVICE));
if (blobStoreManager != null) {
    // The label "Sample photos" is visible to the user.
    BlobHandle blobHandle = BlobHandle.createWithSha256(
            sha256DigestBytes,
            "Sample photos",
            System.currentTimeMillis() + TimeUnit.DAYS.toMillis(1),
            "photoTrainingDataset");
    try (InputStream input = new ParcelFileDescriptor.AutoCloseInputStream(
            blobStoreManager.openBlob(blobHandle))) {
        useDataset(input);
    }
}
```

### Dataset unavailable

If the dataset isn't available, then download it from the server and contribute it
to the system, as shown in the following code snippet:  

### Kotlin

```kotlin
val sessionId = blobStoreManager.createSession(blobHandle)
try {
    val session = blobStoreManager.openSession(sessionId)
    try {
        // For this example, write 200 MiB at the beginning of the file.
        val output = ParcelFileDescriptor.AutoCloseOutputStream(
                session.openWrite(0, 1024 * 1024 * 200))
        writeDataset(output)

        session.apply {
            allowSameSignatureAccess()
            allowPackageAccess(your-app-package,
                    app-certificate)
            allowPackageAccess(some-other-app-package,
                    app-certificate)
            commit(mainExecutor, callback)
        }
    }
}
```

### Java

```java
long sessionId = blobStoreManager.createSession(blobHandle);
try (BlobStoreManager.Session session =
        blobStoreManager.openSession(sessionId)) {
    // For this example, write 200 MiB at the beginning of the file.
    try (OutputStream output = new ParcelFileDescriptor.AutoCloseOutputStream(
            session.openWrite(0, 1024 * 1024 * 200)))
        writeDataset(output);
        session.allowSameSignatureAccess();
        session.allowPackageAccess(your-app-package,
                    app-certificate);
        session.allowPackageAccess(some-other-app-package,
                    app-certificate);
        session.commit(getMainExecutor(), callback);
    }
}
```