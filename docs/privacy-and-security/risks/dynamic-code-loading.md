---
title: https://developer.android.com/privacy-and-security/risks/dynamic-code-loading
url: https://developer.android.com/privacy-and-security/risks/dynamic-code-loading
source: md.txt
---

# Dynamic Code Loading

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

Dynamically loading code into an application introduces a risk level that has to be mitigated. Attackers could potentially tamper with or substitute the code to access sensitive data or execute harmful actions.

Many forms of dynamic code loading, especially those that use remote sources,[violate Google Play policies](https://support.google.com/googleplay/android-developer/answer/9888379)and may lead to a suspension of your app from Google Play.

## Impact

If attackers manage to gain access to the code that will be loaded into the application, they could modify it to support their goals. This could lead to data exfiltration and code execution exploits. Even if attackers cannot modify the code to perform arbitrary actions of their choice, it is still possible that they can corrupt or remove the code and thus affect the availability of the application.

## Mitigations

### Avoid using dynamic code loading

Unless there is a business need, avoid dynamic code loading. You should prefer to include all functionalities directly into the application, whenever possible.

### Use trusted sources

Code that will be loaded into the application should be stored in trusted locations. Regarding local storage, the application internal storage or scoped storage (for Android 10 and later) are the recommended places. These locations have measures to avoid direct access from other applications and users.

When loading code from remote locations such as URLs, avoid using third parties when possible, and store the code in your own infrastructure, following security best practices. If you need to load third-party code, ensure that the provider is a trusted one.

### Perform integrity checks

Integrity checks are recommended in order to ensure that the code has not been tampered with. These checks should be performed before loading code into the application.

When loading remote resources, subresource integrity can be used in order to validate the integrity of the accessed resources.

When loading resources from the external storage, use integrity checks to verify that no other application has tampered with this data or code. The hashes of the files should be stored in a secure manner, preferably encrypted and in the internal storage.  

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
            val sb = StringBuilder(bytes.length * 2)
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
            StringBuilder sb = new StringBuilder(bytes.length * 2);
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

### Sign the code

Another option to ensure the integrity of the data is to sign the code and verify its signature before loading it. This method has the advantage of also ensuring the integrity of the hash code, not only the code itself, which provides an additional anti-tampering protection.

Although code signing provides additional security layers, it is important to take into account that it is a more complex process that may require additional effort and resources to be successfully implemented.

Some examples of code signing can be found in the Resources section of this document.

## Resources

- [Subresource Integrity](https://en.wikipedia.org/wiki/Subresource_Integrity)
- [Digitally Sign Data](https://developers.google.com/tink/digitally-sign-data#java)
- [Code Signing](https://en.wikipedia.org/wiki/Code_signing)
- [Sensitive Data Stored in External Storage](https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage)