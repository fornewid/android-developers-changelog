---
title: https://developer.android.com/privacy-and-security/risks/unsafe-trustmanager
url: https://developer.android.com/privacy-and-security/risks/unsafe-trustmanager
source: md.txt
---

# Unsafe X509TrustManager

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

The`X509TrustManager`class is responsible for verifying the authenticity of a remote server. It does this by validating the server's certificate.

An insecure`X509TrustManager`implementation in an Android application is an implementation that does not properly verify the authenticity of the server with which the application is communicating. This can allow an attacker to impersonate a legitimate server and trick the application into sending sensitive data to the attacker.

The vulnerability exists because using the[`X509TrustManager`](https://developer.android.com/reference/javax/net/ssl/X509TrustManager#checkServerTrusted(java.security.cert.X509Certificate%5B%5D,%20java.lang.String))class, Java/Android allows the complete overriding of server verification. The`X509TrustManager`class has two functions of interest:[`checkServerTrusted()`](https://developer.android.com/reference/javax/net/ssl/X509TrustManager#checkServerTrusted(java.security.cert.X509Certificate%5B%5D,%20java.lang.String))and[`getAcceptedIssuers()`](https://developer.android.com/reference/javax/net/ssl/X509TrustManager#getAcceptedIssuers()). These function calls can be configured to trust all X.509 certificates. Finally, custom validation logic may be buggy or incomplete and permit unexpected connections. In all these cases, the purpose of the class has been negated and the network connection established based on the`X509TrustManager`output is not secure.

## Impact

Unsafe X509TrustManager implementations can lead to vulnerabilities which can be used to perform MitM (Man-in-the-Middle) attacks on network traffic from the victim application. The impact of exploiting this insecure code is that a user's application network data can be compromised by network attackers (remotely or locally) if this code is triggered. The impact is dependent on the content of the network traffic being inadvertently exposed (PII, private information, sensitive session values, service credentials, etc).

## Mitigations

Use the[NetworkSecurityConfig.xml](https://developer.android.com/training/articles/security-config)functionality to ensure that all production, testing, debugging, and dev stage connections are properly handled rather than using or implementing custom TLS/SSL certificate validation code. If using a self-signed certificate is needed for test and debug builds, consider using NetworkSecurityConfig instead of implementing a custom`X509TrustManager`.

## Resources

- [Play Warning docs](https://support.google.com/faqs/answer/6346016)
- [Documentation to assist configuring the Network security configuration xml file.](https://developer.android.com/training/articles/security-config)
- [Developer documentation for the TrustManager class.](https://developer.android.com/reference/javax/net/ssl/TrustManager)
- [This check looks for X.509TrustManager implementations whose checkServerTrusted or checkClientTrusted methods do nothing (thus trusting any certificate chain).](https://googlesamples.github.io/android-custom-lint-rules/checks/TrustAllX509TrustManager.md.html)
- [This check looks for custom X.509TrustManager implementations.](https://googlesamples.github.io/android-custom-lint-rules/checks/CustomX509TrustManager.md.html)
- <https://cs.android.com/android-studio/platform/tools/base/+/mirror-goog-studio-main:lint/libs/lint-checks/src/main/java/com/android/tools/lint/checks/X509TrustManagerDetector.java>