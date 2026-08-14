---
title: https://developer.android.com/about/versions/11/features/captive-portal
url: https://developer.android.com/about/versions/11/features/captive-portal
source: md.txt
---

Starting in Android 11 Beta 2, the system supports a subset of
functionality described by
[RFC7710bis](https://tools.ietf.org/html/draft-ietf-capport-rfc7710bis)
and the associated [captive portal
API](https://tools.ietf.org/html/draft-ietf-capport-api).

The API provides a reliable way for access points to identify themselves as
captive portals. It also enables new use-cases for access points to publish
information to their users, such as session and venue information.

## Improved captive portal detection

Since Android 5.0 (API level 21), Android devices have detected captive portals
and notified the user that they need to sign in to the network to access the
internet. Captive portals were detected using cleartext HTTP probes to known
destinations (such as `connectivitycheck.gstatic.com`), and if the probe
received an HTTP redirect, the device assumed that the network was a captive
portal. This technique can be unreliable because there is no standard URL to
probe, and such probes could be mistakenly allowed or blocked (instead of
redirected) by captive portal networks. The API allows portals to provide a
positive signal that login is required, along with a URL to log in to.

Android 11 supports DHCP option 114 as described in RFC7710bis.
We may add support for the router advertisement option in a future update. If
the device gets a captive portal API URL through that option during the DHCP
handshake, devices fetch the API contents immediately after connecting and
prompt users to log in if the network is captive, as per the captive portal API.

If the API is not available, or if no portal is advertised, the system will
continue to detect portals and verify internet connectivity using HTTP/HTTPS
probes, as before.

## Venue-published information

Android 11 supports the `venue-info-url` defined in the captive
portal API. This URL allows users to obtain context-specific information about
the access point venue in their browser. By default, users can open this URL if
they choose to do so from a notification after logging in, or from their network
settings.

![Screenshot showing the popup allowing the user to visit the venue
URL](https://developer.android.com/static/images/about/versions/11/captive-portal.png)   

**Figure 1.** If the network provides a venue URL, the system pops up a notice
allowing the user to visit that page

![Screenshot showing how to open the site from the Network details
screen](https://developer.android.com/static/images/about/versions/11/network-details.png)   

**Figure 2.** Button to open the site from the Network details screen

## Future use cases

While at launch Android 11 supports only a basic set of
functionality from the captive portal API, new functionality may be delivered to
devices via Google Play system updates after launch. We encourage network
operators to implement the captive portal API while keeping future possible
improvements in mind:

- Session time (`seconds-remaining`) is currently used in the default **Settings** app to inform users on how much time is left on the portal. The ability to extend the session via the login URL (`can-extend-session`) can also be expressed through the API to allow the system to notify the user about expired or soon-to-expire sessions.
- Data caps (`bytes-remaining`) can be advertised through the API to allow users to keep track of remaining data.