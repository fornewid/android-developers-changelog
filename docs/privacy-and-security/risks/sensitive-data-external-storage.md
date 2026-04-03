---
title: https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage
url: https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage
source: md.txt
---

# Sensitive Data Stored in External Storage

<br />

**OWASP category:** [MASVS-STORAGE: Storage](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

## Overview

Applications targeting Android 10 (API 29) or lower don't enforce[scoped storage](https://developer.android.com/training/data-storage#scoped-storage). This means that any data stored on the external storage can be accessed by any other application with the[`READ_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)permission.

## Impact

In applications targeting Android 10 (API 29) or lower, if sensitive data is stored on the external storage, any application on the device with the READ_EXTERNAL_STORAGE permission can access it. This allows malicious applications to silently access sensitive files permanently or temporarily stored on the external storage. Additionally, since content on the external storage can be accessed by any app on the system, any malicious application that also declares the WRITE_EXTERNAL_STORAGE permission can tamper with files stored on the external storage, e.g. to include malicious data. This malicious data, if loaded into the application, could be designed to deceive users or even achieve code execution.

## Mitigations

### Scoped Storage (Android 10 and later)

##### Android 10

For applications targeting Android 10, developers can explicitly opt-in to scoped storage. This can be achieved by setting the[`requestLegacyExternalStorage`](https://developer.android.com/reference/android/R.attr#requestLegacyExternalStorage)flag to**false** in the`AndroidManifest.xml`file. With scoped storage, applications can only access files that they have created themselves on the external storage or files types that were stored using the[MediaStore API](https://developer.android.com/reference/android/provider/MediaStore)such as Audio and Video. This helps protect user privacy and security.

##### Android 11 and later

For applications targeting Android 11 or later versions, the OS[enforces the use of scoped storage](https://developer.android.com/about/versions/11/privacy/storage#scoped-storage), i.e. it ignores the[`requestLegacyExternalStorage`](https://developer.android.com/reference/android/R.attr#requestLegacyExternalStorage)flag and automatically protects applications' external storage from unwanted access.

### Use Internal Storage for Sensitive Data

Regardless of the targeted Android version, an application's sensitive data should always be stored on internal storage. Access to internal storage is automatically restricted to the owning application thanks to Android sandboxing, therefore it can be considered secure, unless the device is rooted.

### Encrypt sensitive data

If the application's use cases require storing sensitive data on the external storage, the data should be encrypted. A strong encryption algorithm is recommended, using the[Android KeyStore](https://developer.android.com/privacy-and-security/keystore)to safely store the key.

In general, encrypting all sensitive data is a recommended security practice, no matter where it is stored.

It is important to note that full disk encryption (or file-based encryption from Android 10) is a measure aimed at protecting data from physical access and other attack vectors. Because of this, to grant the same security measure, sensitive data held on external storage should additionally be encrypted by the application.

### Perform integrity checks

In cases where data or code has to be loaded from the external storage into the application, integrity checks to verify that no other application has tampered with this data or code are recommended. The hashes of the files should be stored in a secure manner, preferably encrypted and in the internal storage.  

### Kotlin

    package com.example.myapplication

    import java.io.BufferedInputStream
    import java.io.FileInputStream
    import java.io.IOException
    import java.security.MessageDigest
    import java.security.NoSuchAlgorithmException

    object FileIntegrityChecker {
        @Throws(IOException::class, NoSuchAlgorithmException::class)
        fun getIntegrityHash(filePath: String?): String {
            val md = MessageDigest.getInstance("SHA-256") // You can choose other algorithms as needed
            val buffer = ByteArray(8192)
            var bytesRead: Int
            BufferedInputStream(FileInputStream(filePath)).use { fis ->
                while (fis.read(buffer).also { bytesRead = it } != -1) {
                    md.update(buffer, 0, bytesRead)
                }

        }

        private fun bytesToHex(bytes: ByteArray): String {
            val sb = StringBuilder()
            for (b in bytes) {
                sb.append(String.format("%02x", b))
            }
            return sb.toString()
        }

        @Throws(IOException::class, NoSuchAlgorithmException::class)
        fun verifyIntegrity(filePath: String?, expectedHash: String): Boolean {
            val actualHash = getIntegrityHash(filePath)
            return actualHash == expectedHash
        }

        @Throws(Exception::class)
        @JvmStatic
        fun main(args: Array<String>) {
            val filePath = "/path/to/your/file"
            val expectedHash = "your_expected_hash_value"
            if (verifyIntegrity(filePath, expectedHash)) {
                println("File integrity is valid!")
            } else {
                println("File integrity is compromised!")
            }
        }
    }

### Java

    package com.example.myapplication;

    import java.io.BufferedInputStream;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.security.MessageDigest;
    import java.security.NoSuchAlgorithmException;

    public class FileIntegrityChecker {

        public static String getIntegrityHash(String filePath) throws IOException, NoSuchAlgorithmException {
            MessageDigest md = MessageDigest.getInstance("SHA-256"); // You can choose other algorithms as needed
            byte[] buffer = new byte[8192];
            int bytesRead;

            try (BufferedInputStream fis = new BufferedInputStream(new FileInputStream(filePath))) {
                while ((bytesRead = fis.read(buffer)) != -1) {
                    md.update(buffer, 0, bytesRead);
                }
            }

            byte[] digest = md.digest();
            return bytesToHex(digest);
        }

        private static String bytesToHex(byte[] bytes) {
            StringBuilder sb = new StringBuilder();
            for (byte b : bytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        }

        public static boolean verifyIntegrity(String filePath, String expectedHash) throws IOException, NoSuchAlgorithmException {
            String actualHash = getIntegrityHash(filePath);
            return actualHash.equals(expectedHash);
        }

        public static void main(String[] args) throws Exception {
            String filePath = "/path/to/your/file";
            String expectedHash = "your_expected_hash_value";

            if (verifyIntegrity(filePath, expectedHash)) {
                System.out.println("File integrity is valid!");
            } else {
                System.out.println("File integrity is compromised!");
            }
        }
    }

## Resources

- [Scoped storage](https://developer.android.com/training/data-storage#scoped-storage)
- [READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)
- [WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)
- [requestLegacyExternalStorage](https://developer.android.com/reference/android/R.attr#requestLegacyExternalStorage)
- [Data and file storage overview](https://developer.android.com/training/data-storage)
- [Data Storage (App Specific)](https://developer.android.com/training/data-storage/app-specific)
- [Cryptography](https://developer.android.com/privacy-and-security/cryptography)
- [Keystore](https://developer.android.com/privacy-and-security/keystore)
- [File-Based encryption](https://source.android.com/docs/security/features/encryption/file-based)
- [Full-Disk encryption](https://source.android.com/docs/security/features/encryption/full-disk)