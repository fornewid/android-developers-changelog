---
title: https://developer.android.com/privacy-and-security/risks/untrustworthy-contentprovider-provided-filename
url: https://developer.android.com/privacy-and-security/risks/untrustworthy-contentprovider-provided-filename
source: md.txt
---

# Improperly trusting ContentProvider-provided filename

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

[*FileProvider*](https://developer.android.com/reference/androidx/core/content/FileProvider), a subclass of[*ContentProvider*](https://developer.android.com/reference/android/content/ContentProvider), is intended to provide a secure method for an application ("server application") to[share files with another application](https://developer.android.com/training/secure-file-sharing)("client application"). However, if the client application does not properly handle the filename provided by the server application, an attacker-controlled server application may be able to implement its own malicious*FileProvider*to overwrite files in the client application's app-specific storage.

## Impact

If an attacker can overwrite an application's files, this can lead to malicious code execution (by overwriting the application's code), or allow otherwise modifying the application's behavior (for example, by overwriting the application's shared preferences or other configuration files).

## Mitigations

### Don't Trust User Input

Prefer working without user input when using file system calls by generating a unique filename when writing the received file to storage.

In other words: When the client application writes the received file to storage, it should ignore the filename provided by the server application and instead use its own internally generated unique identifier as the filename.

This example builds upon the code found at[https://developer.android.com/training/secure-file-sharing/request-file](https://developer.android.com/training/secure-file-sharing/request-file#java):  

### Kotlin

    // Code in
    // https://developer.android.com/training/secure-file-sharing/request-file#OpenFile
    // used to obtain file descriptor (fd)

    try {
        val inputStream = FileInputStream(fd)
        val tempFile = File.createTempFile("temp", null, cacheDir)
        val outputStream = FileOutputStream(tempFile)
        val buf = ByteArray(1024)
        var len: Int
        len = inputStream.read(buf)
        while (len > 0) {
            if (len != -1) {
                outputStream.write(buf, 0, len)
                len = inputStream.read(buf)
            }
        }
        inputStream.close()
        outputStream.close()
    } catch (e: IOException) {
        e.printStackTrace()
        Log.e("MainActivity", "File copy error.")
        return
    }

### Java

    // Code in
    // https://developer.android.com/training/secure-file-sharing/request-file#OpenFile
    // used to obtain file descriptor (fd)

    FileInputStream inputStream = new FileInputStream(fd);

    // Create a temporary file
    File tempFile = File.createTempFile("temp", null, getCacheDir());

    // Copy the contents of the file to the temporary file
    try {
        OutputStream outputStream = new FileOutputStream(tempFile))
        byte[] buffer = new byte[1024];
        int length;
        while ((length = inputStream.read(buffer)) > 0) {
            outputStream.write(buffer, 0, length);
        }
    } catch (IOException e) {
        e.printStackTrace();
        Log.e("MainActivity", "File copy error.");
        return;
    }

### Sanitize Provided Filenames

Sanitize the provided filename when writing the received file to storage.

This mitigation is less desirable than the preceding mitigation because it can be challenging to handle all potential cases. Nonetheless: If generating a unique filename is not practical, the client application should sanitize the provided filename. Sanitization includes:

- Sanitizing path traversal characters in the filename
- Performing a canonicalization to confirm there are no path traversals

This example code builds upon the guidance on[retrieving file information](https://developer.android.com/training/secure-file-sharing/retrieve-info):  

### Kotlin

    protected fun sanitizeFilename(displayName: String): String {
        val badCharacters = arrayOf("..", "/")
        val segments = displayName.split("/")
        var fileName = segments[segments.size - 1]
        for (suspString in badCharacters) {
            fileName = fileName.replace(suspString, "_")
        }
        return fileName
    }

    val displayName = returnCursor.getString(nameIndex)
    val fileName = sanitizeFilename(displayName)
    val filePath = File(context.filesDir, fileName).path

    // saferOpenFile defined in Android developer documentation
    val outputFile = saferOpenFile(filePath, context.filesDir.canonicalPath)

    // fd obtained using Requesting a shared file from Android developer
    // documentation

    val inputStream = FileInputStream(fd)

    // Copy the contents of the file to the new file
    try {
        val outputStream = FileOutputStream(outputFile)
        val buffer = ByteArray(1024)
        var length: Int
        while (inputStream.read(buffer).also { length = it } > 0) {
            outputStream.write(buffer, 0, length)
        }
    } catch (e: IOException) {
        // Handle exception
    }

### Java

    protected String sanitizeFilename(String displayName) {
        String[] badCharacters = new String[] { "..", "/" };
        String[] segments = displayName.split("/");
        String fileName = segments[segments.length - 1];
        for (String suspString : badCharacters) {
            fileName = fileName.replace(suspString, "_");
        }
        return fileName;
    }

    String displayName = returnCursor.getString(nameIndex);
    String fileName = sanitizeFilename(displayName);
    String filePath = new File(context.getFilesDir(), fileName).getPath();

    // saferOpenFile defined in Android developer documentation

    File outputFile = saferOpenFile(filePath,
        context.getFilesDir().getCanonicalPath());

    // fd obtained using Requesting a shared file from Android developer
    // documentation

    FileInputStream inputStream = new FileInputStream(fd);

    // Copy the contents of the file to the new file
    try {
        OutputStream outputStream = new FileOutputStream(outputFile))
        byte[] buffer = new byte[1024];
        int length;
        while ((length = inputStream.read(buffer)) > 0) {
            outputStream.write(buffer, 0, length);
        }
    } catch (IOException e) {
        // Handle exception
    }

Contributors: Dimitrios Valsamaras and Michael Peck of Microsoft Threat Intelligence

## Resources

- [Dirty Stream Attack: Turning Android Share Targets Into Attack Vectors](https://i.blackhat.com/Asia-23/AS-23-Valsamaras-Dirty-Stream-Attack-Turning-Android.pdf)
- [Secure File Sharing](https://developer.android.com/training/secure-file-sharing)
- [Request a Shared File documentation](https://developer.android.com/training/secure-file-sharing/request-file)
- [Retrieve Info](https://developer.android.com/training/secure-file-sharing/retrieve-info)
- [FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)
- [Path Traversal](https://developer.android.com/topic/security/risks/path-traversal)
- [CWE-73 External Control of Filename or Path](https://cwe.mitre.org/data/definitions/73)