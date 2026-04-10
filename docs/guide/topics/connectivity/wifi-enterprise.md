---
title: https://developer.android.com/guide/topics/connectivity/wifi-enterprise
url: https://developer.android.com/guide/topics/connectivity/wifi-enterprise
source: md.txt
---

# Secure Wi-Fi Enterprise configuration

On Android 11 QPR1 and higher, the system mandates strict security configurations for TLS-based Wi-Fi Enterprise configurations (like PEAP, TLS, or TTLS). When adding a new Enterprise configuration using the methods specified in the[Wi-Fi infrastructure overview](https://developer.android.com/guide/topics/connectivity/wifi-infrastructure)or using[`addNetwork`](https://developer.android.com/reference/android/net/wifi/WifiManager#addNetwork(android.net.wifi.WifiConfiguration)), the caller must configure both a Root CA certificate, and either a domain suffix match or an alternate subject match. If the new configuration isn't set up properly, the system rejects it and it's not added or saved.

This security requirement uses the Root CA provided by the app to cryptographically validate the authentication server's certificate and domain name. This ensures that the user is connected to a trusted network.

An app that needs to create a secure Enterprise configuration must call either[`setCaCertificate`](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setCaCertificate(java.security.cert.X509Certificate))or[`setCaCertificates`](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setCaCertificates(java.security.cert.X509Certificate%5B%5D)). This sets a Root CA certificate or a list of Root CA certificates. The app must then call either[`setAltSubjectMatch`](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setAltSubjectMatch(java.lang.String))or[`setDomainSuffixMatch`](https://developer.android.com/reference/android/net/wifi/WifiEnterpriseConfig#setDomainSuffixMatch(java.lang.String))to set an alternate subject or a domain name suffix.