---
title: https://developer.android.com/develop/connectivity/vpn
url: https://developer.android.com/develop/connectivity/vpn
source: md.txt
---

Android provides APIs for developers to create virtual private network (VPN)
solutions. After reading this guide, you'll know how to develop and test your
own VPN client for Android-powered devices.

## Overview

VPNs allow devices that aren't physically on a network to securely access the
network.

Android includes a built-in (PPTP and L2TP/IPSec) VPN client, which is sometimes
called *legacy VPN*. Android 4.0 (API Level 14) introduced APIs so that app
developers could provide their own VPN solutions. You package your VPN solution
into an app that people install onto the device. Developers normally build a VPN
app for one of the following reasons:

- To offer VPN protocols that the built-in client doesn't support.
- To help people connect to a VPN service without complex configuration.

The rest of this guide explains how to develop VPN apps (including
[always-on](https://developer.android.com/develop/connectivity/vpn#always-on) and [per-app](https://developer.android.com/develop/connectivity/vpn#per-app) VPN) and doesn't cover the
built-in VPN client.

## User experience

Android provides a user interface (UI) to help somebody configure, start, and
stop your VPN solution. The system UI also makes the person using the device
aware of an active VPN connection. Android shows the following UI components for
VPN connections:

- Before a VPN app can become active for the first time, the system displays a connection request dialog. The dialog prompts the person using the device to confirm that they trust the VPN and accept the request.
- The VPN settings screen (Settings \> Network \& Internet \> VPN) shows the VPN apps where a person accepted connection requests. There's a button to configure system options or forget the VPN.
- The Quick Settings tray shows an information panel when a connection is active. Tapping the label displays a dialog with more information and a link to Settings.
- The status bar includes a VPN (key) icon to indicate an active connection.

Your app also needs to provide a UI so that the person using the device can
configure your service's options. For example, your solution might need to
capture the account authentication settings. Apps should show the following UI:

- Controls to manually start and stop a connection. [Always-on VPN](https://developer.android.com/develop/connectivity/vpn#always-on) can connect when needed, but allow people to configure the connection the first time they use your VPN.
- A non-dismissible notification when the service is active. The notification can show the connection status or provide more information---such as network stats. Tapping the notification brings your app to the foreground. Remove the notification after the service becomes inactive.

## VPN service

Your app connects the system networking for a user (or a [work
profile](https://developer.android.com/work/managed-profiles)) to a VPN gateway. Each user (or work profile) can run a
different VPN app. You create a VPN service that the system uses to start and
stop your VPN, and track the connection status. Your VPN service inherits from
[`VpnService`](https://developer.android.com/reference/android/net/VpnService).

The service also acts as your container for the VPN gateway connections and
their local device interfaces. Your service instance call
[`VpnService.Builder`](https://developer.android.com/reference/android/net/VpnService.Builder) methods to establish a new local interface.
**Figure 1.** How `VpnService` connects Android networking to the VPN gateway ![Block-architecture diagram showing how VpnService creates a local TUN
interface in system networking.](https://developer.android.com/static/images/develop/connectivity/vpn-app-arch.svg)

Your app transfers the following data to connect the device to the VPN gateway:

- Reads outgoing IP packets from the local interface's file descriptor, encrypts them, and sends them to the VPN gateway.
- Writes incoming packets (received and decrypted from the VPN gateway) to the local interface's file descriptor.

> [!WARNING]
> **Warning:** Your app must use strong encryption when transferring data to and from the VPN gateway.

There's only one active service per user or profile. Starting a new service,
automatically stops an existing service.

### Add a service

To add a VPN service to your app, create an Android service inheriting from
[`VpnService`](https://developer.android.com/reference/android/net/VpnService). Declare the VPN [service](https://developer.android.com/guide/topics/manifest/service-element) in your app
manifest file with the following additions:

- Protect the service with the [`BIND_VPN_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#BIND_VPN_SERVICE) permission so that only the system can bind to your service.
- Advertise the service with the `"android.net.VpnService"` intent filter so that the system can find your service.

This example shows how you can declare the service in your app manifest file:

    <service android:name=".MyVpnService"
             android:permission="android.permission.BIND_VPN_SERVICE">
         <intent-filter>
             <action android:name="android.net.VpnService"/>
         </intent-filter>
    </service>

Now that your app declares the service, the system can automatically start
and stop your app's VPN service when needed. For example, the system controls
your service when running [always-on VPN](https://developer.android.com/develop/connectivity/vpn#always-on).

### Prepare a service

To prepare the app to become the user's current VPN service, call
[`VpnService.prepare()`](https://developer.android.com/reference/android/net/VpnService#prepare(android.content.Context)). If the person using the device hasn't
already given permission for your app, the method returns an activity intent.
You use this intent to start a system activity that asks for permission. The
system shows a dialog that's similar to other permissions dialogs, such as
camera or contacts access. If your app is already prepared, the method returns
`null`.

Only one app can be the current prepared VPN service. Always call
[`VpnService.prepare()`](https://developer.android.com/reference/android/net/VpnService#prepare(android.content.Context)) because a person might have set a different
app as the VPN service since your app last called the method. To learn more, see
the [Service lifecycle](https://developer.android.com/develop/connectivity/vpn#lifecycle) section.

### Connect a service

Once the service is running, you can establish a new local interface that's
connected to a VPN gateway. To request permission and connect to your service to
the VPN gateway, you need to complete the steps in the following order:

1. Call [`VpnService.prepare()`](https://developer.android.com/reference/android/net/VpnService#prepare(android.content.Context)) to ask for permission (when needed).
2. Call [`VpnService.protect()`](https://developer.android.com/reference/android/net/VpnService#protect(int)) to keep your app's tunnel socket outside of the system VPN and avoid a circular connection.
3. Call [`DatagramSocket.connect()`](https://developer.android.com/reference/java/net/DatagramSocket#connect(java.net.SocketAddress)) to connect your app's tunnel socket to the VPN gateway.
4. Call [`VpnService.Builder`](https://developer.android.com/reference/android/net/VpnService.Builder) methods to configure a new local [TUN](https://en.wikipedia.org/wiki/TUN/TAP) interface on the device for VPN traffic.
5. Call [`VpnService.Builder.establish()`](https://developer.android.com/reference/android/net/VpnService.Builder#establish()) so that the system establishes the local TUN interface and begins routing traffic through the interface.

A VPN gateway normally suggests settings for the local TUN interface during
handshaking. Your app calls [`VpnService.Builder`](https://developer.android.com/reference/android/net/VpnService.Builder) methods to configure a
service as shown in the following sample:

### Kotlin

```kotlin
// Configure a new interface from our VpnService instance. This must be done
// from inside a VpnService.
val builder = Builder()

// Create a local TUN interface using predetermined addresses. In your app,
// you typically use values returned from the VPN gateway during handshaking.
val localTunnel = builder
        .addAddress("192.168.2.2", 24)
        .addRoute("0.0.0.0", 0)
        .addDnsServer("192.168.1.1")
        .establish()
```

### Java

```java
// Configure a new interface from our VpnService instance. This must be done
// from inside a VpnService.
VpnService.Builder builder = new VpnService.Builder();

// Create a local TUN interface using predetermined addresses. In your app,
// you typically use values returned from the VPN gateway during handshaking.
ParcelFileDescriptor localTunnel = builder
    .addAddress("192.168.2.2", 24)
    .addRoute("0.0.0.0", 0)
    .addDnsServer("192.168.1.1")
    .establish();
```

The example in the [Per-app VPN](https://developer.android.com/develop/connectivity/vpn#per-app) section shows an IPv6 config including
more options. You need to add the following [`VpnService.Builder`](https://developer.android.com/reference/android/net/VpnService.Builder) values
before you can establish a new interface:

[`addAddress()`](https://developer.android.com/reference/android/net/VpnService.Builder#addAddress(java.net.InetAddress,%20int))
:   Add at least one IPv4 or IPv6 address along with a subnet mask that the system
    assigns as the local TUN interface address. Your app typically receives the IP
    addresses and subnet masks from a VPN gateway during handshaking.

[`addRoute()`](https://developer.android.com/reference/android/net/VpnService.Builder#addRoute(java.net.InetAddress,%20int))
:   Add at least one route if you want the system to send traffic through the VPN
    interface. Routes filter by destination addresses. To accept all traffic, set an
    open route such as `0.0.0.0/0` or `::/0`.

The [`establish()`](https://developer.android.com/reference/android/net/VpnService.Builder#establish()) method returns a
[`ParcelFileDescriptor`](https://developer.android.com/reference/android/os/ParcelFileDescriptor) instance that your app uses to read and write
packets to and from the interface's buffer. The [`establish()`](https://developer.android.com/reference/android/net/VpnService.Builder#establish())
method returns `null` if your app isn't prepared or somebody revokes the
permission.

### Service lifecycle

Your app should track the status of the system's selected VPN and any active
connections. Update your app's user interface (UI) to keep the person using the
device aware of any changes.

#### Starting a service

Your VPN service can be started in the following ways:

- Your app starts the service---normally because a person tapped a connect button.
- The system starts the service because [always-on VPN](https://developer.android.com/develop/connectivity/vpn#always-on) is on.

Your app starts the VPN service by passing an intent to
[`startService()`](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)). To learn more, read [Starting a
service](https://developer.android.com/guide/components/services#StartingAService).

The system starts your service in the background by calling
[`onStartCommand()`](https://developer.android.com/reference/android/app/Service#onStartCommand(android.content.Intent,%20int,%20int)). However, Android places restrictions on
background apps in version 8.0 (API Level 26) or higher. If you support these
API Levels, you need to transition your service to the foreground by calling
[`Service.startForeground()`](https://developer.android.com/reference/android/app/Service#startForeground(int,%20android.app.Notification)). To learn more, read [Running a
service in the foreground](https://developer.android.com/guide/components/services#Foreground).

#### Stopping a service

A person using the device can stop your service by using your app's UI. Stop the
service instead of just closing the connection. The system also stops an active
connection when the person using the device does the following in the VPN screen
of the Settings app:

- disconnects or forgets the VPN app
- switches off always-on VPN for an active connection

The system calls your service's [`onRevoke()`](https://developer.android.com/reference/android/net/VpnService#onRevoke()) method but this call
might not happen on the main thread. When the system calls this method, an
alternative network interface is already routing traffic. You can safely dispose
of the following resources:

- Close the protected tunnel socket to the VPN gateway by calling [`DatagramSocket.close()`](https://developer.android.com/reference/java/net/DatagramSocket#close()).
- Close the parcel file descriptor (you don't need to drain it) by calling [`ParcelFileDescriptor.close()`](https://developer.android.com/reference/android/os/ParcelFileDescriptor#close()).

## Always-on VPN

Android can start a VPN service when the device boots and keep it running while
the device is on. This feature is called *always-on VPN* and is available in
Android 7.0 (API Level 24) or higher. While Android maintains the service
lifecycle, it's your VPN service that's responsible for the VPN-gateway
connection. Always-on VPN can also block connections that don't use the VPN.

### User experience

In Android 8.0 or higher, the system shows the following dialogs to make the
person using the device aware of always-on VPN:

- When always-on VPN connections disconnect or can't connect, people see a non-dismissible notification. Tapping the notification shows a dialog that explains more. The notification disappears when the VPN reconnects or somebody turns off the always-on VPN option.
- Always-on VPN allows the person using a device to block any network connections that don't use the VPN. When turning on this option, the Settings app warns people that they don't have an internet connection before the VPN connects. The Settings app prompts the person using the device to continue or cancel.

Because the system (and not a person) starts and stops an always-on connection,
you need to adapt your app's behavior and user interface:

1. Disable any UI that disconnects the connection because the system and Settings app control the connection.
2. Save any config between each app start and configure a connection with the latest settings. Because the system starts your app on demand, the person using the device might not always want to configure a connection.

You can also use [managed configurations](https://developer.android.com/work/managed-configurations) to configure a
connection. Managed configurations help an IT admin configure your VPN remotely.

### Detect always-on

Android doesn't include APIs to confirm whether the system started your VPN
service. But, when your app flags any service instances it starts, you can assume
that the system started unflagged services for always-on VPN. Here's an example:

1. Create an [`Intent`](https://developer.android.com/reference/android/content/Intent) instance to start the VPN service.
2. Flag the VPN service by [putting an extra](https://developer.android.com/reference/android/content/Intent#putExtra(java.lang.String,%20java.lang.String)) into the intent.
3. In the service's [`onStartCommand()`](https://developer.android.com/reference/android/app/Service#onStartCommand(android.content.Intent,%20int,%20int)) method, look for the flag in the `intent` argument's extras.

### Blocked connections

A person using the device (or an IT admin) can force all traffic to use the VPN.
The system blocks any network traffic that doesn't use the VPN. People using the
device can find the *Block connections without VPN* switch in the VPN options
panel in Settings.

> [!CAUTION]
> **Caution:** When non-VPN traffic is blocked, apps that aren't in an [allowed
> list](https://developer.android.com/develop/connectivity/vpn#allowed-apps) or in a [disallowed list](https://developer.android.com/develop/connectivity/vpn#disallowed-apps) lose their network connection. Consider warning people when making allowed or disallowed lists. To learn more, see the following [Per-app VPN](https://developer.android.com/develop/connectivity/vpn#per-app) section.

### Opt out of always-on

If your app can't currently support always-on VPN, you can opt out (in Android
8.1 or higher) by setting the
[`SERVICE_META_DATA_SUPPORTS_ALWAYS_ON`](https://developer.android.com/reference/android/net/VpnService#SERVICE_META_DATA_SUPPORTS_ALWAYS_ON)
service metadata to `false`. The following app manifest example shows how to add
the metadata element:

    <service android:name=".MyVpnService"
             android:permission="android.permission.BIND_VPN_SERVICE">
         <intent-filter>
             <action android:name="android.net.VpnService"/>
         </intent-filter>
         <meta-data android:name="android.net.VpnService.SUPPORTS_ALWAYS_ON"
                 android:value=false/>
    </service>

When your app opts out of always-on VPN, the system disables the options UI
controls in Settings.

## Per-app VPN

VPN apps can filter which installed apps are allowed to send traffic through the
VPN connection. You can create either an allowed list, or, a disallowed list,
but not both. If you don't create allowed or disallowed lists, the system sends
all network traffic through the VPN.

Your VPN app must set the lists before the connection is established. If you
need to change the lists, establish a new VPN connection. An app must be
installed on the device when you add it to a list.

### Kotlin

```kotlin
// The apps that will have access to the VPN.
val appPackages = arrayOf(
        "com.android.chrome",
        "com.google.android.youtube",
        "com.example.a.missing.app")

// Loop through the app packages in the array and confirm that the app is
// installed before adding the app to the allowed list.
val builder = Builder()
for (appPackage in appPackages) {
    try {
        packageManager.getPackageInfo(appPackage, 0)
        builder.addAllowedApplication(appPackage)
    } catch (e: PackageManager.NameNotFoundException) {
        // The app isn't installed.
    }
}

// Complete the VPN interface config.
val localTunnel = builder
        .addAddress("2001:db8::1", 64)
        .addRoute("::", 0)
        .establish()
```

### Java

```java
// The apps that will have access to the VPN.
String[] appPackages = {
    "com.android.chrome",
    "com.google.android.youtube",
    "com.example.a.missing.app"};

// Loop through the app packages in the array and confirm that the app is
// installed before adding the app to the allowed list.
VpnService.Builder builder = new VpnService.Builder();
PackageManager packageManager = getPackageManager();
for (String appPackage: appPackages) {
  try {
    packageManager.getPackageInfo(appPackage, 0);
    builder.addAllowedApplication(appPackage);
  } catch (PackageManager.NameNotFoundException e) {
    // The app isn't installed.
  }
}

// Complete the VPN interface config.
ParcelFileDescriptor localTunnel = builder
    .addAddress("2001:db8::1", 64)
    .addRoute("::", 0)
    .establish();
```

### Allowed apps

To add an app to the allowed list, call
[`VpnService.Builder.addAllowedApplication()`](https://developer.android.com/reference/android/net/VpnService.Builder#addAllowedApplication(java.lang.String)). If
the list includes one or more apps, then only the apps in the list use the VPN.
All other apps (that aren't in the list) use the system networks as if the VPN
isn't running. When the allowed list is empty, all apps use the VPN.

### Disallowed apps

To add an app to the disallowed list, call
[`VpnService.Builder.addDisallowedApplication()`](https://developer.android.com/reference/android/net/VpnService.Builder#addDisallowedApplication(java.lang.String)).
Disallowed apps use system networking as if the VPN wasn't running---all other
apps use the VPN.

## Bypass VPN

Your VPN can allow apps to bypass the VPN and select their own network. To
bypass the VPN, call [`VpnService.Builder.allowBypass()`](https://developer.android.com/reference/android/net/VpnService.Builder#allowBypass()) when
establishing a VPN interface. You can't change this value after you start your
VPN service. If an app doesn't bind their process or a socket to a specific
network, the app's network traffic continues through the VPN.

Apps that bind to a specific network don't have a connection when somebody
blocks traffic that doesn't go through the VPN. To send traffic through a specific
network, apps call methods, such as
[`ConnectivityManager.bindProcessToNetwork()`](https://developer.android.com/reference/android/net/ConnectivityManager#bindProcessToNetwork(android.net.Network)) or
[`Network.bindSocket()`](https://developer.android.com/reference/android/net/Network#bindSocket(java.net.Socket)) before connecting the socket.

## Sample code

The Android Open Source Project includes a sample app called [ToyVPN](https://android.googlesource.com/platform/development/+/master/samples/ToyVpn).
This app shows how to set up and connect a VPN service.