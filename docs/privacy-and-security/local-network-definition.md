---
title: Local Network Definition  |  Privacy  |  Android Developers
url: https://developer.android.com/privacy-and-security/local-network-definition
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Privacy](https://developer.android.com/privacy)
* [Guides](https://developer.android.com/privacy-and-security/about)

# Local Network Definition Stay organized with collections Save and categorize content based on your preferences.



A local network in this project refers to an IP network that utilizes a
broadcast-capable network interface, such as Wi-Fi or Ethernet, but excludes
cellular (WWAN) or VPN connections.

The following are considered local networks:

| IPv4 | IPv6 |
| --- | --- |
| - 169.254.0.0/16 //Link Local  - 100.64.0.0/10 // CGNAT  - 10.0.0.0/8 // RFC1918  - 172.16.0.0/12 // RFC1918  - 192.168.0.0/16 // RFC1918 | - Link-local  - Directly-connected routes  - Stub networks like Thread  - Multiple-subnets |

Additionally, both multicast addresses (224.0.0.0/4, ff00::/8) and the IPv4
broadcast address (255.255.255.255) are classified as local network addresses.