---
title: https://developer.android.com/privacy-and-security/risks/content-resolver
url: https://developer.android.com/privacy-and-security/risks/content-resolver
source: md.txt
---

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)


## Overview

According to the [documentation](https://developer.android.com/reference/android/content/ContentResolver), `ContentResolver` is a *"class that provides applications access to the content model"*. ContentResolvers expose methods to interact, fetch, or modify content provided from the following:

- Installed apps (`content://` URI scheme)
- File systems (`file://` URI scheme)
- Supporting APIs as provided by Android (`android.resource://` URI scheme).

To summarize, vulnerabilities related to `ContentResolver` belong to the [confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem) class as the attacker can use a vulnerable application's privileges to access protected content.

## Risk: Abuse based on untrusted file:// URI

The abuse of `ContentResolver` using the `file://` URI vulnerability exploits the capability of `ContentResolver` to return file descriptors described by the URI. This vulnerability affects functions like `openFile()`, `openFileDescriptor()`, `openInputStream()`, `openOutputStream()`, or `openAssetFileDescriptor()` from the `ContentResolver` [API](https://developer.android.com/reference/android/content/ContentResolver). The vulnerability can be abused with a fully or partially attacker-controlled `file://` URI to force the application to access files that weren't intended to be accessible, such as internal databases or shared preferences.

One of the possible attack scenarios would be to create a malicious gallery or file picker that, when used by a vulnerable app, would return a malicious URI.

There are few variants of this attack:

- Fully attacker-controlled `file://` URI that points to an app's internal files
- Part of `file://` URI is attacker-controlled, making it prone to path traversals
- `file://` URI targeting an attacker-controlled symbolic link (symlink) that points to the app's internal files
- Similar to the preceding variant, but here the attacker repeatedly swaps the symlink target from a legitimate target to an app's internal files. The goal is to exploit a race condition between a potential security check and file path usage

### Impact

The impact of exploiting this vulnerability varies depending on what the ContentResolver is used for. In many cases, it can result in an app's protected data being exfiltrated or modifications of protected data by unauthorized parties.

### Mitigations

To mitigate this vulnerability, use the algorithm below to validate the file descriptor. After passing validation, the file descriptor can be used safely.
**Note:** Only the file descriptor is safe. If you decide to reuse the URI, you need to repeat the validation process.  

### Kotlin

    fun isValidFile(ctx: Context, pfd: ParcelFileDescriptor, fileUri: Uri): Boolean {
        // Canonicalize to resolve symlinks and path traversals.
        val fdCanonical = File(fileUri.path!!).canonicalPath

        val pfdStat: StructStat = Os.fstat(pfd.fileDescriptor)

        // Lstat doesn't follow the symlink.
        val canonicalFileStat: StructStat = Os.lstat(fdCanonical)

        // Since we canonicalized (followed the links) the path already,
        // the path shouldn't point to symlink unless it was changed in the
        // meantime.
        if (OsConstants.S_ISLNK(canonicalFileStat.st_mode)) {
            return false
        }

        val sameFile =
            pfdStat.st_dev == canonicalFileStat.st_dev &&
            pfdStat.st_ino == canonicalFileStat.st_ino

        if (!sameFile) {
            return false
        }

        return !isBlockedPath(ctx, fdCanonical)
    }

    fun isBlockedPath(ctx: Context, fdCanonical: String): Boolean {
        // Paths that should rarely be exposed
        if (fdCanonical.startsWith("/proc/") ||
            fdCanonical.startsWith("/data/misc/")) {
            return true
        }

        // Implement logic to block desired directories. For example, specify
        // the entire app data/ directory to block all access.
    }

### Java

    boolean isValidFile(Context ctx, ParcelFileDescriptor pfd, Uri fileUri) {
        // Canonicalize to resolve symlinks and path traversals
        String fdCanonical = new File(fileUri.getPath()).getCanonicalPath();

        StructStat pfdStat = Os.fstat(pfd.getFileDescriptor());

        // Lstat doesn't follow the symlink. 
        StructStat canonicalFileStat = Os.lstat(fdCanonical);

        // Since we canonicalized (followed the links) the path already, 
        // the path shouldn't point to symlink unless it was changed in the meantime
        if (OsConstants.S_ISLNK(canonicalFileStat.st_mode)) {
            return false;
        }

        boolean sameFile =
            pfdStat.stDev == canonicalFileStat.stDev && pfdStat.stIno == canonicalFileStat.stIno;

        if (!sameFile) {
            return false;
        }

        return !isBlockedPath(ctx, fdCanonical);
    } 

    boolean isBlockedPath(Context ctx, String fdCanonical) {
            
            // Paths that should rarely be exposed
            if (fdCanonical.startsWith("/proc/") || fdCanonical.startsWith("/data/misc/")) {
                return true;
            }

            // Implement logic to block desired directories. For example, specify
            // the entire app data/ directory to block all access.
    }

*** ** * ** ***

## Risk: Abuse based on untrusted content:// URI

Abuse of a `ContentResolver` using a `content://` URI vulnerability occurs when a fully or partially attacker controlled URI is passed to `ContentResolver` APIs to operate on content that wasn't intended to be accessible.

There are two main scenarios for this attack:

- The app operates on its own, internal content. For example: after getting a URI from an attacker, the mail app attaches data from its own internal content provider instead of an external photo.
- The app acts as a proxy and then accesses another application's data for the attacker. For example: the mail application attaches data from app X that is protected by a permission that would normally disallow the attacker from seeing that specific attachment. It is available to the application doing the attachment, but not initially thus relaying this content to the attacker.

One possible attack scenario is to create a malicious gallery or file picker that, when used by a vulnerable app, would return a malicious URI.

### Impact

The impact of exploiting this vulnerability varies depending on the context associated with the ContentResolver. This might result in an app's protected data being exfiltrated or modifications by unauthorized parties to protected data.

### Mitigations

#### General

Validate incoming URIs. For example, using an allowlist of expected authorities is considered good practice.

#### URI targets non-exported or permission-protected content provider that belongs to vulnerable app

Check, if URI targets your app:  

### Kotlin

    fun belongsToCurrentApplication(ctx: Context, uri: Uri): Boolean {
        val authority: String = uri.authority.toString()
        val info: ProviderInfo =
            ctx.packageManager.resolveContentProvider(authority, 0)!!

        return ctx.packageName.equals(info.packageName)
    }

### Java

    boolean belongsToCurrentApplication(Context ctx, Uri uri){
        String authority = uri.getAuthority();
        ProviderInfo info = ctx.getPackageManager().resolveContentProvider(authority, 0);

        return ctx.getPackageName().equals(info.packageName);
    }

Or if targeted provider is exported:  

### Kotlin

    fun isExported(ctx: Context, uri: Uri): Boolean {
        val authority = uri.authority.toString()
        val info: ProviderInfo =
                ctx.packageManager.resolveContentProvider(authority, 0)!!

        return info.exported
    }

### Java

    boolean isExported(Context ctx, Uri uri){
        String authority = uri.getAuthority();
        ProviderInfo info = ctx.getPackageManager().resolveContentProvider(authority, 0);       

        return info.exported;
    }

Or if granted explicit permission to the URI - this check is base on assumption that if granted explicit permission to access the data, the URI isn't malicious:  

### Kotlin

    // grantFlag is one of: FLAG_GRANT_READ_URI_PERMISSION or FLAG_GRANT_WRITE_URI_PERMISSION
    fun wasGrantedPermission(ctx: Context, uri: Uri?, grantFlag: Int): Boolean {
        val pid: Int = Process.myPid()
        val uid: Int = Process.myUid()
        return ctx.checkUriPermission(uri, pid, uid, grantFlag) ==
                PackageManager.PERMISSION_GRANTED
    }

### Java

    // grantFlag is one of: FLAG_GRANT_READ_URI_PERMISSION or FLAG_GRANT_WRITE_URI_PERMISSION
    boolean wasGrantedPermission(Context ctx, Uri uri, int grantFlag){
        int pid = Process.myPid();
        int uid = Process.myUid();

        return ctx.checkUriPermission(uri, pid, uid, grantFlag) == PackageManager.PERMISSION_GRANTED;
    }

#### URI targets a permission-protected ContentProvider that belongs to another app which trusts the vulnerable app.

This attack is relevant to the following situations:

- Ecosystems of applications where apps define and use custom permissions or other authentication mechanisms.
- Permission proxy attacks, where an attacker abuses a vulnerable app that's holding a runtime permission, such as READ_CONTACTS, to retrieve data from a system provider.

Test if the URI permission has been granted:  

### Kotlin

    // grantFlag is one of: FLAG_GRANT_READ_URI_PERMISSION or FLAG_GRANT_WRITE_URI_PERMISSION
    fun wasGrantedPermission(ctx: Context, uri: Uri?, grantFlag: Int): Boolean {
        val pid: Int = Process.myPid()
        val uid: Int = Process.myUid()
        return ctx.checkUriPermission(uri, pid, uid, grantFlag) ==
                PackageManager.PERMISSION_GRANTED
    }

### Java

    // grantFlag is one of: FLAG_GRANT_READ_URI_PERMISSION or FLAG_GRANT_WRITE_URI_PERMISSION
    boolean wasGrantedPermission(Context ctx, Uri uri, int grantFlag){
        int pid = Process.myPid();
        int uid = Process.myUid();

        return ctx.checkUriPermission(uri, pid, uid, grantFlag) == PackageManager.PERMISSION_GRANTED;
    }

If usage of other content providers doesn't require a permission grant - such as when the app allows all apps from the ecosystem to access all data - then explicitly forbid usage of these authorities.
| **Note:** Maintaining a denylist is error prone. Denying a package prefix makes this mitigation more robust.

*** ** * ** ***