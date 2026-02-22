---
title: https://developer.android.com/work/dpc/logging
url: https://developer.android.com/work/dpc/logging
source: md.txt
---

# Network activity logging

This document explains how a device policy controller (DPC) logs network activity. Continue reading to learn how to add network logging to your DPC.

## Overview

Logging network activity can help enterprises detect and track the spread of malware on their devices. Your DPC can call network logging APIs to report TCP connections and DNS lookups from system networking calls.
| **Note:** Some apps might bypass the logged network APIs by connecting directly to hosts. IT admins can report at the network layer, such as a corporate VPN gateway or firewall, if they need absolute monitoring. While network-layer reporting gives coverage, associating a request's IP address with an app, device, or user is sometimes difficult. These on-device logging APIs can complement network-layer reporting by associating requests with an app, device, or user.

Typically, your DPC delivers logs to a server for presentation to an IT admin. You might want to process the logs further on your server or locally on the device. For example, you could set up DNS denylists to detect and alert IT admins about suspicious behavior.

## Availability

Network logging is supported in Android 8 and higher for a device owner. If enabled, it collects data on network activity of the device. It is also supported in Android 12 and higher for a profile owner of a managed profile and a delegated app with[DELEGATION_NETWORK_LOGGING](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#DELEGATION_NETWORK_LOGGING). When network logging is enabled by the profile owner, the network logs only includes work profile network activity and does not collect data from the personal profile.
| **Caution:** Your DPC can't retrieve network logs if the device has any unaffiliated secondary users or work profiles. While waiting for new users to become affiliated, the system discards logs once the internal buffer is full. We recommend that you affiliate new profiles as soon as your DPC or the device user creates them. Listen for broadcasts or callbacks, such as[`onUserAdded()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onUserAdded(android.content.Context,%20android.content.Intent,%20android.os.UserHandle)), and affiliate the user or work profile.

To learn more, read[Affiliated users](https://developer.android.com/work/dpc/work-profile-on-managed-device#affiliated-users).

## Event logs

When network logging is active, Android records each event from apps using the system networking libraries. Network logging records two types of events:

- DNS lookups
- Network connections

### DNS lookups

Network logging records an event for DNS lookups that are part of system network requests. The logs capture each DNS request that resolves a hostname to an IP address. Other supporting DNS queries, such as name server discovery, aren't recorded.

Network activity logging APIs present each DNS lookup as a[`DnsEvent`](https://developer.android.com/reference/android/app/admin/DnsEvent)instance. Table 1 describes the fields and typical values recorded into a`DnsEvent`.

**Table 1.**DNS event fields

|      Data      |            Example             |                                                                                                       Description                                                                                                       |
|----------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hostname       | *host.example.com*             | The hostname sent in the DNS query.                                                                                                                                                                                     |
| Inet addresses | *203.0.113.9* ,*198.51.100.25* | A list of IPv4 or IPv6 addresses the DNS query resolved for the hostname. To keep the log size manageable, the results might not include all the IP addresses---see address count in the following row.                 |
| Address count  | *4*                            | The number of IP addresses returned from the DNS query resolution. Use this to find out if the IP addresses logged are a subset of the results. A value of 0 (zero) means the hostname didn't resolve to an IP address. |
| Package name   | *com.android.chrome*           | The package name of the app that made the DNS query.                                                                                                                                                                    |
| Timestamp      | *1506297600000*                | A timestamp recording when the DNS lookup happened. The value is the millisecond interval between the DNS lookup and midnight, January 1, 1970 UTC.                                                                     |
| ID             | *25*                           | A monotonically increasing numeric ID. Available in Android 9.0 (API level 28) or higher.                                                                                                                               |

While DNS lookups can help IT admins track[network connections](https://developer.android.com/work/dpc/logging#connections), network logging isn't a general-purpose DNS recording solution. Here are some DNS tasks an app might do that aren't logged:

- Communicating directly with a DNS name server.
- Calling a Java DNS library to make DNS queries.
- Avoiding a DNS query by connecting to a fixed IP address.

### Network connections

Network logging records an event for each attempted connection that's part of a system network request. The logs capture successful and failed TCP connections---UDP transfers aren't recorded.

Network activity logging APIs present each connection as a[`ConnectEvent`](https://developer.android.com/reference/android/app/admin/ConnectEvent)instance. Table 2 describes the fields and typical values recorded into a`ConnectEvent`.

**Table 2.**Connect event fields

|      Data      |       Example        |                                                                         Description                                                                         |
|----------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inet addresses | *2001:db8::2f:abc:0* | The IP address the device connected to. This might be an IPv4 or an IPv6 address.                                                                           |
| Port           | *80*                 | The TCP port number the device connected to.                                                                                                                |
| Package name   | *com.android.chrome* | The package name of the app that connected.                                                                                                                 |
| Timestamp      | *1506297600000*      | A timestamp recording when the network connection happened. The value is the millisecond interval between the connection and midnight, January 1, 1970 UTC. |
| ID             | *26*                 | A monotonically increasing numeric ID. Available in Android 9.0 (API level 28) or higher.                                                                   |

Network logging records an event when an app calls standard network libraries, such as Android's built-in APIs or popular third-party libraries, to connect to a host. Apps issuing system calls directly to communicate aren't logged. Remember, UDP networking isn't logged so some media streaming, messaging, and gaming apps might not appear in the logs.

## Inform users

The system alerts device users that network activity logging is active. Users see the following warnings in the interface:

- A section in the*Device management*dialog explaining your DPC is monitoring network traffic. Users see the dialog by tapping the managed device information label in Quick Settings.
- A dismissible system notification shown while the user is new to network logging. Tapping the notification shows the*Device monitoring*dialog with further explanation in a network monitoring section. The notification disappears when your DPC disables network logging.

## Add network logging to your DPC

To help IT admins review network logs, your DPC needs to be able to complete the following tasks:

- Turn network logging on and off.
- Retrieve any recorded logs when a new batch is ready.
- Send the useful data in the logs to a server.

### Requirements

Network logging is available in Android 8.0 (API level 26) or higher for a device owner and Android 12 (API level 31) or higher for a profile owner of a managed profile. Before logging network activity, your DPC should check if it's a device owner or a profile owner of a managed profile. Network logs in a device owner with a work profile does not include the network activity on the personal profile if it's enabled by the profile owner.

### Enable network logging

To start logging network activity, call the`DevicePolicyManager`method[`setNetworkLoggingEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setNetworkLoggingEnabled(android.content.ComponentName,%20boolean))and pass`true`as the`enabled`argument. Your DPC can call[`isNetworkLoggingEnabled()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isNetworkLoggingEnabled(android.content.ComponentName))to check if network activity is logged.

After your DPC enables network logging, it might be some time before it the first batch of logs is ready. You might want to set delivery expectations for IT admins in your user interface.

To stop logging network activity, call`setNetworkLoggingEnabled()`and pass`false`. When an IT admin turns off network logging, the system deletes any collected and unreported logs.

### Retrieve logs

Your DPC can retrieve logs in batches---the network logging APIs don't provide random access to past individual entries. When a new batch of logs is available, your DPC's[`DeviceAdminReceiver`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver)subclass receives the[`onNetworkLogsAvailable()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onNetworkLogsAvailable(android.content.Context,%20android.content.Intent,%20long,%20int))callback. The callback includes a batch token your DPC can use to retrieve the logs. Your DPC calls the`DevicePolicyManager`method[`retrieveNetworkLogs()`](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#retrieveNetworkLogs(android.content.ComponentName,%20long))to get a list of network events.

The following example shows you could retrieve the logs in your`DeviceAdminReceiver`subclass:  

### Kotlin

```kotlin
fun onNetworkLogsAvailable(
        context: Context, intent: Intent, batchToken: Long, networkLogsCount: Int) {

    val dpm = getManager(context)
    var logs: List<NetworkEvent>? = null

    // Fetch the batch of logs with the batch token from the callback's arguments.
    try {
        logs = dpm.retrieveNetworkLogs(getWho(context), batchToken)
    } catch (e: SecurityException) {
        // Perhaps an unaffiliated user - handle the exception ...
    }

    // Process any logs ...
}
```

### Java

```java
public void onNetworkLogsAvailable(
    Context context, Intent intent, long batchToken, int networkLogsCount) {

  DevicePolicyManager dpm = getManager(context);
  List<NetworkEvent> logs = null;

  // Fetch the next batch of logs using the callback's batch token argument.
  try {
    logs = dpm.retrieveNetworkLogs(getWho(context), batchToken);
  } catch (SecurityException e) {
    // Perhaps an unaffiliated user - handle the exception ...
  }

  // Process any logs ...
}
```

Your DPC should retrieve the logs straightaway because the system deletes the logs to make room for new batches. You might want to keep your local copy of the logs until you're sure your DPC has processed them all without problems.

### Process any logs

A batch of logs typically contain a mix of[`DnsEvent`](https://developer.android.com/reference/android/app/admin/DnsEvent)and[`ConnectEvent`](https://developer.android.com/reference/android/app/admin/ConnectEvent)instances. To learn more about the data fields of DNS lookups and network connections, see[Event logs](https://developer.android.com/work/dpc/logging#log-fields). Events are in chronological order and each batch contains no more than 1200 events.

After your call to retrieve the logs, check the return value isn't`null`. The value might be`null`if one of the following happens:

- The batch represented by the batch token is no longer available. Your DPC can't retrieve the batch and should wait for the next batch.
- The IT admin disabled network logging.

The following simplified example shows how DPC might extract the DNS hostnames resolved. Your DPC needs more sophisticated processing and reporting.  

### Kotlin

```kotlin
// Here, logs might be null. We can't fix because either the token doesn't match
// the current batch or network logging was deactivated.
// Confirm with isNetworkLoggingEnabled().

logs?.forEach {
    // For this example, report the DNS hosts and discard all other data.
    // Because we use the event ID, this example requires API level 28.
    if (it is DnsEvent) {
        reportDnsHostToServer(it.hostname, it.getTimestamp(), it.getId())
    }
}
```

### Java

```java
if (logs == null) {
  // Abandon processing because either the token doesn't match the current batch
  // or network logging was deactivated - confirm with isNetworkLoggingEnabled().
  return;
}

for (NetworkEvent event : logs) {
  // For this example, report the DNS hosts and discard all other data.
  // This example requires API level 28 because we use the event ID.
  if (event instanceof DnsEvent) {
    reportDnsHostToServer(
        ((DnsEvent) event).getHostname(), event.getTimestamp(), event.getId());
  }
}
```

The previous example also shows how you can get the numeric ID for events that are included in Android 9.0 (API level 28) or higher. Because the ID monotonically increases for each event, you can help IT admins spot gaps in their logs. The system resets the ID whenever a DPC enables logging or when the device restarts.

Your DPC can send the entire collection to a server or you might decide to filter the events on the device. For example, you might offer allowlisted reporting for IT admins.

### Development and testing

While you're developing and testing, you might want to receive[`onNetworkLogsAvailable()`](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver#onNetworkLogsAvailable(android.content.Context,%20android.content.Intent,%20long,%20int))callbacks without having to browse hundreds of web pages. In Android 9.0 (API level 28) or higher, you can make a few sample network requests and force the system to send a logs-available callback. Run the following[Android Debug Bridge](https://developer.android.com/studio/command-line/adb)(adb) command in your terminal:  

```
adb shell dpm force-network-logs
```

The system limits how frequently you can use the tool and reports any intentional slowing in the terminal output. If there aren't any logs to retrieve, your DPC doesn't receive a callback.