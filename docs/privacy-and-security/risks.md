---
title: https://developer.android.com/privacy-and-security/risks
url: https://developer.android.com/privacy-and-security/risks
source: md.txt
---

> Documentation index: https://developer.android.com/privacy-and-security/risks/llms.txt

By making your app more secure, you help preserve user trust and device
integrity.

This page presents a set of common security issues that Android app developers
face. You can use this content in the following ways:

- Learn more about how to proactively secure your apps.
- Understand how to react in the event that one of these issues is discovered in your app.

The following list contains links to dedicated pages for each individual issue,
sorted into categories based on [OWASP MASVS](https://mas.owasp.org/MASVS/) controls. Each
page includes a summary, impact statement, and tips for mitigating the risk to
your app.

### MASVS-STORAGE: Storage

[OWASP category description](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

- [Improperly Exposed Directories to FileProvider](https://developer.android.com/privacy-and-security/risks/file-providers.md.txt)
- [Log Info Disclosure](https://developer.android.com/privacy-and-security/risks/log-info-disclosure.md.txt)
- [Path traversal](https://developer.android.com/privacy-and-security/risks/path-traversal.md.txt)
- [Sensitive Data Stored in External Storage](https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage.md.txt)
- [WebViews -- Unsafe File Inclusion](https://developer.android.com/privacy-and-security/risks/webview-unsafe-file-inclusion.md.txt)
- [Zip Path Traversal](https://developer.android.com/privacy-and-security/risks/zip-path-traversal.md.txt)

### MASVS-CRYPTO: Cryptography

[OWASP category description](https://mas.owasp.org/MASVS/06-MASVS-CRYPTO)

- [Broken or risky cryptographic algorithm](https://developer.android.com/privacy-and-security/risks/broken-cryptographic-algorithm.md.txt)
- [Hardcoded Cryptographic Secrets](https://developer.android.com/privacy-and-security/risks/hardcoded-cryptographic-secrets.md.txt)
- [Weak PRNG](https://developer.android.com/privacy-and-security/risks/weak-prng.md.txt)

### MASVS-NETWORK: Network Communication

[OWASP category description](https://mas.owasp.org/MASVS/08-MASVS-NETWORK)

- [Cleartext communications](https://developer.android.com/privacy-and-security/risks/cleartext-communications.md.txt)
- [Insecure DNS Setup](https://developer.android.com/privacy-and-security/risks/bad-dns.md.txt)
- [Unsafe Download Manager](https://developer.android.com/privacy-and-security/risks/unsafe-download-manager.md.txt)

### MASVS-PLATFORM: Platform Interaction

[OWASP category description](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

- [Content resolvers](https://developer.android.com/privacy-and-security/risks/content-resolver.md.txt)
- [Implicit Intent hijacking](https://developer.android.com/privacy-and-security/risks/implicit-intent-hijacking.md.txt)
- [Insecure API usage](https://developer.android.com/privacy-and-security/risks/insecure-api-usage.md.txt)
- [Insecure broadcast receivers](https://developer.android.com/privacy-and-security/risks/insecure-broadcast-receiver.md.txt)
- [Intent redirection](https://developer.android.com/privacy-and-security/risks/intent-redirection.md.txt)
- [Permission-based access control to exported components](https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components.md.txt)
- [Pending Intents](https://developer.android.com/privacy-and-security/risks/pending-intent.md.txt)
- [Sender of Pending Intents](https://developer.android.com/privacy-and-security/risks/sender-of-pending-intents.md.txt)
- [Sticky Broadcasts](https://developer.android.com/privacy-and-security/risks/sticky-broadcast.md.txt)
- [StrandHogg Attack / Task Affinity Vulnerability](https://developer.android.com/privacy-and-security/risks/strandhogg.md.txt)
- [Tapjacking](https://developer.android.com/privacy-and-security/risks/tapjacking.md.txt)
- [Unsafe use of deep links](https://developer.android.com/privacy-and-security/risks/unsafe-use-of-deeplinks.md.txt)
- [WebView -- Native bridges](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges.md.txt)
- [android:debuggable](https://developer.android.com/privacy-and-security/risks/android-debuggable.md.txt)
- [android:exported](https://developer.android.com/privacy-and-security/risks/android-exported.md.txt)

### MASVS-CODE: Code Quality

[OWASP category description](https://mas.owasp.org/MASVS/10-MASVS-CODE)

- [Cross-App Scripting](https://developer.android.com/privacy-and-security/risks/cross-app-scripting.md.txt)
- [Custom Permissions](https://developer.android.com/privacy-and-security/risks/custom-permissions.md.txt)
- [createPackageContext](https://developer.android.com/privacy-and-security/risks/create-package-context.md.txt)
- [Dynamic code loading](https://developer.android.com/privacy-and-security/risks/dynamic-code-loading.md.txt)
- [Improperly trusting ContentProvider-provided filename](https://developer.android.com/privacy-and-security/risks/untrustworthy-contentprovider-provided-filename.md.txt)
- [Insecure API or Library](https://developer.android.com/privacy-and-security/risks/insecure-library.md.txt)
- [Insecure Machine-to-Machine communication setup](https://developer.android.com/privacy-and-security/risks/insecure-machine-to-machine.md.txt)
- [Security best practices for backups](https://developer.android.com/privacy-and-security/risks/backup-best-practices.md.txt)
- [Secure Clipboard Handling](https://developer.android.com/privacy-and-security/risks/secure-clipboard-handling.md.txt)
- [SQL injection](https://developer.android.com/privacy-and-security/risks/sql-injection.md.txt)
- [Test/Debug Features](https://developer.android.com/privacy-and-security/risks/test-debug.md.txt)
- [Unsafe Deserialization](https://developer.android.com/privacy-and-security/risks/unsafe-deserialization.md.txt)
- [Unsafe HostnameVerifier](https://developer.android.com/privacy-and-security/risks/unsafe-hostname.md.txt)
- [Unsafe X509TrustManager](https://developer.android.com/privacy-and-security/risks/unsafe-trustmanager.md.txt)
- [Use of native code](https://developer.android.com/privacy-and-security/risks/use-of-native-code.md.txt)
- [XML External Entities Injection](https://developer.android.com/privacy-and-security/risks/xml-external-entities-injection.md.txt)
- [Webviews - Unsafe URI Loading](https://developer.android.com/privacy-and-security/risks/unsafe-uri-loading.md.txt)