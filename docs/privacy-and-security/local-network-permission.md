---
title: https://developer.android.com/privacy-and-security/local-network-permission
url: https://developer.android.com/privacy-and-security/local-network-permission
source: md.txt
---

Devices on a Local Area Network (LAN) can be accessed by any app that has the
`INTERNET` permission.
This makes it easy for apps to connect to local devices, but also carries
privacy implications such as forming a fingerprint of the user and being a
proxy for location.

The Local Network Protections project aims to protect the user's privacy by
gating access to the local network behind a new runtime permission.

## Impact

During Android 16, this permission is an opt-in feature which means only the
apps that opt-in will be affected. The goal of the opt-in is for app developers
to understand which parts of their app depend on implicit local network access
such that they can prepare to permission guard them on a future Android release.

Apps will be affected if they access the user's local network using:

- Direct or library use of raw sockets on local network addresses, for example, `Multicast DNS (mDNS)` or `Simple Service Discovery Protocol (SSDP)`.
- Use of framework-level classes that access the local network, for example, `NsdManager`.

### Details of impact

Traffic to and from a local network address requires local network access
permission. The following table lists some common cases:

| App Low Level Network Operation | Local Network Permission Required |
|---|---|
| Making an outgoing TCP connection | yes |
| Accepting an incoming TCP connection | yes |
| Sending a UDP unicast, multicast, broadcast | yes |
| Receiving a incoming UDP unicast, multicast, broadcast | yes |

These restrictions are implemented deep in the networking stack, and thus they
apply to **all networking APIs** . This includes sockets created in the platform
or managed code, networking libraries like Cronet and OkHttp, and any APIs
implemented on top of those. Trying to resolve services on the local network
that have a `.local` suffix requires local network permission.
| **Note:** Traffic originating from Android Webviews that require local network access will inherit permission state from the host app

Exceptions to the preceding rules:

- If a device's DNS server is on a local network, traffic to / from it (at port 53) doesn't require local network access permission.
- Applications using Output Switcher as their in-app picker won't need local network permissions (more guidance to come at a later release).

| **Note:** Many media casting scenarios depend on access to the local network and will be impacted by this change. However, not all apps which offer casting will need to request the new permission. Future APIs and guidance for dealing with casting scenarios will be provided at a later Android Release.

## Guidance

To opt into local network restrictions, do the following:

1. Flash your device to a build with Android 16 Beta 3 or later
2. Install the app to be tested
3. Toggle the Appcompat config by using adb

       adb shell am compat enable RESTRICT_LOCAL_NETWORK <package_name>

4. **Reboot the device**

Now your app's access to the local network is restricted and any attempt to
access the local network will lead to socket errors.
If you are using APIs that perform local network operations outside of your app
process---for example, `NsdManager`---they aren't affected during the opt-in.

To restore access, you must grant your app permission to `NEARBY_WIFI_DEVICES`.

- Make sure the app declares the `NEARBY_WIFI_DEVICES` permission in its `manifest`.
- Go to **Settings** \> **Apps** \> **\[Application Name\]** \> **Permissions** \> **Nearby devices** \> **Allow**

| **Note:** in a future Android release, this feature will be guarded by a new permission in the [`NEARBY_DEVICES`](https://developer.android.com/reference/android/Manifest.permission_group#NEARBY_DEVICES) permission group.

Now your app's access to the local network should be restored and all your
scenarios should work as they did prior to opting the app in. Here is how the
app network traffic will be impacted.

| Permission | Outbound LAN Request | Outbound/Inbound Internet Request | Inbound LAN Request |
|---|---|---|---|
| Granted | Works | Works | Works |
| Not Granted | Fails | Works | Fails |

Use the following command to toggle-off the Appcompat config

    adb shell am compat disable RESTRICT_LOCAL_NETWORK <package_name>

### Errors

If a local network access request fails due to missing permission:

- TCP Connections will typically result in a **timeout error**.
- UDP errors and general permission denials will typically result in an **EPERM** error code

### Bugs

[Submit bugs](https://developer.android.com/about/versions/16/feedback) and feedback for:

- Discrepancies in LAN access (you don't think a certain access should be considered "local network" access)
- Bugs where LAN access should be blocked but isn't
- Bugs where LAN access shouldn't be blocked but is

The following should be unaffected by this change:

- Access to the Internet
- Mobile Network