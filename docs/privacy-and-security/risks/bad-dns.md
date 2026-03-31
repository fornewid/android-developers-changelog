---
title: Insecure DNS Setup  |  Security  |  Android Developers
url: https://developer.android.com/privacy-and-security/risks/bad-dns
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Guides](https://developer.android.com/privacy-and-security/security-tips)

# Insecure DNS Setup Stay organized with collections Save and categorize content based on your preferences.




**OWASP category:** [MASVS-NETWORK: Network Communication](https://mas.owasp.org/MASVS/08-MASVS-NETWORK)

## Overview

Insecure DNS configurations can occur when developers customize an application's
DNS transport behavior, bypass device defaults, or when a user specifies a
private DNS server in Android 9 and later. Deviation from known good DNS
configurations can leave users vulnerable to attacks like DNS Spoofing or DNS
cache poisoning, allowing attackers to redirect user traffic to malicious sites.

## Impact

If a malicious network attacker is able to spoof DNS, they can discreetly
redirect the user to a website they control, without arousing the user's
suspicion. This malicious website could, for example, phish the user for
personally identifiable information, cause a denial of service for the user, or
redirect the user to websites without notification.

## Risk: Vulnerable DNS Transport Security

Custom DNS configurations may allow apps to bypass Android's built-in transport
security for DNS in Android 9 and higher.

### Mitigations

#### Use the Android OS to handle DNS traffic

Allow the Android OS to handle DNS. Since SDK level 28, Android has added
security to DNS transport through DNS over TLS, and then DNS over HTTP/3 in SDK
level 30.

#### Use SDK level >=28

Update SDK level to at least 28. It should be noted that this mitigation
requires communication with well-known and secure public DNS servers such as can
be found [here](https://dnsprivacy.org/public_resolvers/).

## Resources

* [Resolve DNS queries](/training/basics/network-ops/connecting#lookup-dns)
* [Java reference for DnsResolver Class](/reference/android/net/DnsResolver)
* [Android Security Blog post about DNS-over-HTTP/3](https://security.googleblog.com/2022/07/dns-over-http3-in-android.html)
* [Overview of secure transport for DNS](https://developers.google.com/speed/public-dns/docs/secure-transports)
* [Android Developer Blog post about DNS over TLS](https://android-developers.googleblog.com/2018/04/dns-over-tls-support-in-android-p.html)