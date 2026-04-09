---
title: https://developer.android.com/privacy-and-security/risks/path-traversal
url: https://developer.android.com/privacy-and-security/risks/path-traversal
source: md.txt
---

# Path traversal

<br />

**OWASP category:** [MASVS-STORAGE: Storage](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

## Overview

Path traversal vulnerabilities occur when an attacker can control part of the path that is then passed to the file system APIs without validation. This can lead to unauthorized file system operations. For example, an attacker might use special characters such as`../`to unexpectedly change the resource target, by traversing outside of the targeted directory.

## Impact

The impact varies depending on the operation and file content, but generally leads to a file overwrite (when writing files), data leak (when reading files), or permission changes (when changing file or directory permissions).

## Mitigations

Canonicalize the path using[`File.getCanonicalPath()`](https://developer.android.com/reference/java/io/File#getCanonicalPath())and compare the prefix with the expected directory:  

### Kotlin

    @Throws(IllegalArgumentException::class)
    fun saferOpenFile(path: String, expectedDir: String?): File {
        val f = File(path)
        val canonicalPath = f.canonicalPath
        require(canonicalPath.startsWith(expectedDir!!))
        return f
    }

### Java

    public File saferOpenFile (String path, String expectedDir) throws IllegalArgumentException {
      File f = new File(path);
      String canonicalPath = f.getCanonicalPath();
      if (!canonicalPath.startsWith(expectedDir)) {
        throw new IllegalArgumentException();
      }
      return f;
    }

An additional best practice is to use validation to ensure only expected outcomes occur. Examples include the following:

- Checking if the file already exists to prevent an accidental overwrite.
- Checking if the targeted file is an expected target to prevent leaking data or incorrectly changing permissions.
- Checking if the current directory of the operation is exactly as expected in the return value from the canonical path.
- Ensuring a permissions system is explicitly scoped to the operation, such as checking that it isn't running services as root, and ensuring that the directory permissions are scoped to the service or command specified.