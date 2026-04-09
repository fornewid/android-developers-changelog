---
title: https://developer.android.com/privacy-and-security/risks/unsafe-hostname
url: https://developer.android.com/privacy-and-security/risks/unsafe-hostname
source: md.txt
---

# Unsafe HostnameVerifier

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

The[`HostnameVerifier`](https://developer.android.com/reference/javax/net/ssl/HostnameVerifier#verify(java.lang.String,%20javax.net.ssl.SSLSession))implementation is responsible for verifying that the hostname in the server's certificate matches the hostname of the server that the client is trying to connect to.

An unsafe HostnameVerifier implementation in an Android application is an implementation that does not properly verify the hostname of the server with which the application is communicating. This can allow an attacker to impersonate a legitimate server and trick the application into sending sensitive data to the attacker.

This vulnerability exists because the`HostnameVerifier`class has function calls that can skip X.509 certificate hostname validation and, instead, only verify the hash of the certificate. A common misconception is that the[`SSLSession#isValid`](https://developer.android.com/reference/javax/net/ssl/SSLSession#isValid())function performs a security-related operation, when in reality its purpose is only to check if a session is valid and available for resuming or joining; neither of which validate the*security* of a session. The HostnameVerifier class has been superseded by[NetworkSecurityConfig](https://developer.android.com/training/articles/security-config).

## Impact

Unsafe HostnameVerifier implementations can lead to vulnerabilities which can be used to perform MiTM (Man-in-The-Middle) attacks on network traffic from the victim application. The impact of exploiting this insecure code is that a user's application network data can be compromised by network attackers (remotely or locally) if this code is triggered. The impact is dependent on the content of the network traffic being inadvertently exposed (PII, private information, sensitive session values, service credentials, etc).

## Mitigations

Use the[NetworkSecurityConfig.xml](https://developer.android.com/training/articles/security-config)to ensure that all production, testing, debugging, and dev stage connections are properly handled rather than using or implementing custom TLS/SSL certificate validation code.

## Resources

- [Network Security Configuration Documentation](https://developer.android.com/training/articles/security-config)
- [This check looks for implementations of HostnameVerifier whose verify method always returns true (thus trusting any hostname)](https://googlesamples.github.io/android-custom-lint-rules/checks/BadHostnameVerifier.md.html)
- [Developer documentation for the HostnameVerifier class](https://developer.android.com/reference/javax/net/ssl/HostnameVerifier#verify(java.lang.String,%20javax.net.ssl.SSLSession))
- [AllowAllHostnameVerifierDetector class in Android](https://cs.android.com/android-studio/platform/tools/base/+/mirror-goog-studio-main:lint/libs/lint-checks/src/main/java/com/android/tools/lint/checks/AllowAllHostnameVerifierDetector.java)