---
title: https://developer.android.com/privacy-and-security/risks/zip-path-traversal
url: https://developer.android.com/privacy-and-security/risks/zip-path-traversal
source: md.txt
---

# Zip Path Traversal

<br />

**OWASP category:** [MASVS-STORAGE: Storage](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

## Overview

The Zip Path Traversal vulnerability, also known as ZipSlip, is related to handling compressed archives. On this page, we demonstrate this vulnerability using the ZIP format as an example, but similar problems can arise in libraries handling other formats, like TAR, RAR, or 7z.

The underlying reason for this problem is that inside ZIP archives, each packed file is stored with a fully qualified name, which allows special characters such as slashes and dots. The default library from the`java.util.zip`package doesn't check the names of the archive entries for directory traversal characters (`../`), so special care must be taken when concatenating the name extracted from the archive with the targeted directory path.

It's very important to validate any ZIP-extracting code snippets or libraries from external sources.**Many such libraries are vulnerable to Zip Path Traversals.**

## Impact

The Zip Path Traversal vulnerability can be used to achieve arbitrary file overwrite. Depending on conditions, the impact might vary, but in many cases this vulnerability can lead to major security issues such as code execution.

## Mitigations

To mitigate this issue, before extracting each entry, you should always verify that the target path is a child of the destination directory. The code below assumes that the destination directory is safe -- writable by your app only and not under attacker control -- otherwise your app could be prone to other vulnerabilities such as symlink attacks.  

### Kotlin

    companion object {
        @Throws(IOException::class)
        fun newFile(targetPath: File, zipEntry: ZipEntry): File {
            val name: String = zipEntry.name
            val f = File(targetPath, name)
            val canonicalPath = f.canonicalPath
            if (!canonicalPath.startsWith(
                    targetPath.canonicalPath + File.separator)) {
                throw ZipException("Illegal name: $name")
            }
            return f
        }
    }

### Java

    public static File newFile(File targetPath, ZipEntry zipEntry) throws IOException {
        String name = zipEntry.getName();
        File f = new File(targetPath, name);
        String canonicalPath = f.getCanonicalPath();
        if (!canonicalPath.startsWith(targetPath.getCanonicalPath() + File.separator)) {
          throw new ZipException("Illegal name: " + name);
        }
        return f;
     }

To avoid accidentally overwriting existing files, you should also make sure that the destination directory is empty before starting the extraction process. Otherwise you risk potential app crashes, or in extreme cases, an application compromise.  

### Kotlin

    @Throws(IOException::class)
    fun unzip(inputStream: InputStream?, destinationDir: File) {
        if (!destinationDir.isDirectory) {
            throw IOException("Destination is not a directory.")
        }
        val files = destinationDir.list()
        if (files != null && files.isNotEmpty()) {
            throw IOException("Destination directory is not empty.")
        }
        ZipInputStream(inputStream).use { zipInputStream ->
            var zipEntry: ZipEntry
            while (zipInputStream.nextEntry.also { zipEntry = it } != null) {
                val targetFile = File(destinationDir, zipEntry.name)
                // ...
            }
        }
    }

### Java

    void unzip(final InputStream inputStream, File destinationDir)
          throws IOException {
      if(!destinationDir.isDirectory()) { 
        throw IOException("Destination is not a directory.");
      }

      String[] files = destinationDir.list();
      if(files != null && files.length != 0) { 
        throw IOException("Destination directory is not empty.");
      }

      try (ZipInputStream zipInputStream = new ZipInputStream(inputStream)) {
        ZipEntry zipEntry;
        while ((zipEntry = zipInputStream.getNextEntry()) != null) {
          final File targetFile = new File(destinationDir, zipEntry);
            ...
        }
      }
    }

## Resources

- [Zip Slip Vulnerability](https://snyk.io/research/zip-slip-vulnerability)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Path traversal](https://developer.android.com/topic/security/risks/path-traversal)