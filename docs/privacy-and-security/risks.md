---
title: https://developer.android.com/privacy-and-security/risks
url: https://developer.android.com/privacy-and-security/risks
source: md.txt
---

# Mitigate security risks in your app

By making your app more secure, you help preserve user trust and device integrity.

This page presents a set of common security issues that Android app developers face. You can use this content in the following ways:

- Learn more about how to proactively secure your apps.
- Understand how to react in the event that one of these issues is discovered in your app.

The following list contains links to dedicated pages for each individual issue, sorted into categories based on[OWASP MASVS](https://mas.owasp.org/MASVS/)controls. Each page includes a summary, impact statement, and tips for mitigating the risk to your app.

### MASVS-STORAGE: Storage

[OWASP category description](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

- [Improperly Exposed Directories to FileProvider](https://developer.android.com/privacy-and-security/risks/file-providers)
- [Log Info Disclosure](https://developer.android.com/privacy-and-security/risks/log-info-disclosure)
- [Path traversal](https://developer.android.com/privacy-and-security/risks/path-traversal)
- [Sensitive Data Stored in External Storage](https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage)
- [WebViews -- Unsafe File Inclusion](https://developer.android.com/privacy-and-security/risks/webview-unsafe-file-inclusion)
- [Zip Path Traversal](https://developer.android.com/privacy-and-security/risks/zip-path-traversal)

### MASVS-CRYPTO: Cryptography

[OWASP category description](https://mas.owasp.org/MASVS/06-MASVS-CRYPTO)

- [Broken or risky cryptographic algorithm](https://developer.android.com/privacy-and-security/risks/broken-cryptographic-algorithm)
- [Hardcoded Cryptographic Secrets](https://developer.android.com/privacy-and-security/risks/hardcoded-cryptographic-secrets)
- [Weak PRNG](https://developer.android.com/privacy-and-security/risks/weak-prng)

### MASVS-NETWORK: Network Communication

[OWASP category description](https://mas.owasp.org/MASVS/08-MASVS-NETWORK)

- [Cleartext communications](https://developer.android.com/privacy-and-security/risks/cleartext-communications)
- [Insecure DNS Setup](https://developer.android.com/privacy-and-security/risks/bad-dns)
- [Unsafe Download Manager](https://developer.android.com/privacy-and-security/risks/unsafe-download-manager)

### MASVS-PLATFORM: Platform Interaction

[OWASP category description](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

- [Content resolvers](https://developer.android.com/privacy-and-security/risks/content-resolver)
- [Implicit Intent hijacking](https://developer.android.com/privacy-and-security/risks/implicit-intent-hijacking)
- [Insecure API usage](https://developer.android.com/privacy-and-security/risks/insecure-api-usage)
- [Insecure broadcast receivers](https://developer.android.com/privacy-and-security/risks/insecure-broadcast-receiver)
- [Intent redirection](https://developer.android.com/privacy-and-security/risks/intent-redirection)
- [Permission-based access control to exported components](https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components)
- [Pending Intents](https://developer.android.com/privacy-and-security/risks/pending-intent)
- [Sender of Pending Intents](https://developer.android.com/privacy-and-security/risks/sender-of-pending-intents)
- [Sticky Broadcasts](https://developer.android.com/privacy-and-security/risks/sticky-broadcast)
- [StrandHogg Attack / Task Affinity Vulnerability](https://developer.android.com/privacy-and-security/risks/strandhogg)
- [Tapjacking](https://developer.android.com/privacy-and-security/risks/tapjacking)
- [Unsafe use of deep links](https://developer.android.com/privacy-and-security/risks/unsafe-use-of-deeplinks)
- [WebView -- Native bridges](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges)
- [android:debuggable](https://developer.android.com/privacy-and-security/risks/android-debuggable)
- [android:exported](https://developer.android.com/privacy-and-security/risks/android-exported)

### MASVS-CODE: Code Quality

[OWASP category description](https://mas.owasp.org/MASVS/10-MASVS-CODE)

- [Cross-App Scripting](https://developer.android.com/privacy-and-security/risks/cross-app-scripting)
- [Custom Permissions](https://developer.android.com/privacy-and-security/risks/custom-permissions)
- [createPackageContext](https://developer.android.com/privacy-and-security/risks/create-package-context)
- [Dynamic code loading](https://developer.android.com/privacy-and-security/risks/dynamic-code-loading)
- [Improperly trusting ContentProvider-provided filename](https://developer.android.com/privacy-and-security/risks/untrustworthy-contentprovider-provided-filename)
- [Insecure API or Library](https://developer.android.com/privacy-and-security/risks/insecure-library)
- [Insecure Machine-to-Machine communication setup](https://developer.android.com/privacy-and-security/risks/insecure-machine-to-machine)
- [Security best practices for backups](https://developer.android.com/privacy-and-security/risks/backup-best-practices)
- [Secure Clipboard Handling](https://developer.android.com/privacy-and-security/risks/secure-clipboard-handling)
- [SQL injection](https://developer.android.com/privacy-and-security/risks/sql-injection)
- [Test/Debug Features](https://developer.android.com/privacy-and-security/risks/test-debug)
- [Unsafe Deserialization](https://developer.android.com/privacy-and-security/risks/unsafe-deserialization)
- [Unsafe HostnameVerifier](https://developer.android.com/privacy-and-security/risks/unsafe-hostname)
- [Unsafe X509TrustManager](https://developer.android.com/privacy-and-security/risks/unsafe-trustmanager)
- [Use of native code](https://developer.android.com/privacy-and-security/risks/use-of-native-code)
- [XML External Entities Injection](https://developer.android.com/privacy-and-security/risks/xml-external-entities-injection)
- [Webviews - Unsafe URI Loading](https://developer.android.com/privacy-and-security/risks/unsafe-uri-loading)