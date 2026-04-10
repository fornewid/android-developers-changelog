---
title: https://developer.android.com/privacy-and-security/risks/file-providers
url: https://developer.android.com/privacy-and-security/risks/file-providers
source: md.txt
---

# Improperly Exposed Directories to FileProvider

<br />

**OWASP category:** [MASVS-STORAGE: Storage](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

## Overview

An improperly configured`FileProvider`can unintentionally expose files and directories to an attacker. Depending on the configuration, an attacker can read from or write to these exposed files, which in turn can lead to the exfiltration of sensitive information or, in the worst case, arbitrary code execution. For example, an application with`<root-path>`set in the configuration could enable an attacker to access sensitive information stored in databases or to overwrite the application's native libraries, leading to arbitrary code execution.

## Impact

The impact varies depending on the configuration and file content, but generally leads to data leakage (when reading) or overwriting (when writing) files.

## Mitigations

### Do not use the \<root-path\> path element in the configuration

`<root-path>`corresponds to the root directory of the device (`/`). Allowing this in the configuration provides arbitrary access to files and folders, including the app's sandbox and`/sdcard`directory, which offers a very broad attack surface to an attacker.

### Share narrow path ranges

In the path configuration file, avoid sharing a broad path range like`.`or`/`. Doing so can lead to exposing sensitive files by mistake. Share only a limited/narrower path range and ensure only files you want to share are under this path. This will prevent exposing sensitive files by mistake.

A typical configuration file with safer settings could look like this:  

### Xml

    <paths>
        <files-path name="images" path="images/" />
        <files-path name="docs" path="docs" />
        <cache-path name="cache" path="net-export/" />
    </paths>

### Check and validate the external URIs

Validate the external URIs (using a`content`scheme) and ensure they are not pointing to your application's local files. This prevents any inadvertent information leak.

### Grant minimum access permissions

A[`content URI`](https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs)can have both read and write access permissions. Ensure only the minimum required access permission is granted. For example, if*only* read permission is required, then explicitly grant only[`FLAG_GRANT_READ_URI_PERMISSION`](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION).

### Avoid usage of \<external-path\> for storing/sharing sensitive information

Sensitive data, like personally identifiable information (PII), should not be stored outside of the application container or system credential storage facilities. Thus, avoid the usage of the`<external-path>`element, unless you have explicitly verified that the information being stored/shared is not sensitive.

## Resources

- [FileProvider Documentation](https://developer.android.com/reference/androidx/core/content/FileProvider)

- [Vulnerability on using \<root-path\>](https://hackerone.com/reports/876192)