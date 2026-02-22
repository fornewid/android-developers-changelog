---
title: https://developer.android.com/studio/run/emulator-networking
url: https://developer.android.com/studio/run/emulator-networking
source: md.txt
---

# Set up Android Emulator networking

The emulator provides versatile networking capabilities that you can use to set up complex modeling and testing environments for your app. This page introduces the emulator network architecture and capabilities.

## Network address space

Each instance of the emulator runs behind a virtual router or firewall service that isolates it from your development machine network interfaces and settings and from the internet. An emulated device can't detect your development machine or other emulator instances on the network. It detects only that it is connected through ethernet to a router or firewall.

The virtual router for each instance manages the 10.0.2/24 network address space. All addresses managed by the router are in the form of 10.0.2.<var translate="no">xx</var>, where<var translate="no">xx</var>is a number. Addresses within this space are pre-allocated by the emulator or router as follows:

|        Network Address         |                                      Description                                      |
|--------------------------------|---------------------------------------------------------------------------------------|
| 10.0.2.1                       | Router or gateway address                                                             |
| 10.0.2.2                       | Special alias to your host loopback interface (127.0.0.1 on your development machine) |
| 10.0.2.3                       | First DNS server                                                                      |
| 10.0.2.4 / 10.0.2.5 / 10.0.2.6 | Optional second, third, and fourth DNS servers                                        |
| 10.0.2.15                      | The emulated device network when connected using ethernet                             |
| 10.0.2.16                      | The emulated device network when connected using Wi-Fi                                |
| 127.0.0.1                      | The emulated device loopback interface                                                |

The same address assignments are used by all running emulator instances. That means that if you have two instances running concurrently on your machine, each will have its own router, and behind that, each will have an IP address of 10.0.2.15. The instances are isolated by a router and can't detect each other on the same network. For information about how to let emulator instances communicate over TCP/UDP, see the section about[interconnecting emulator instances](https://developer.android.com/studio/run/emulator-networking#connecting).

The address 127.0.0.1 on your development machine corresponds to the emulator's loopback interface. To access services running on your development machine loopback interface, use the special address 10.0.2.2 instead.

The pre-allocated addresses of an emulated device are specific to the Android Emulator and are likely to be very different on real devices (which are also likely to be network address translated, specifically behind a router or firewall).

## Local networking limitations

Android apps running on an emulator can connect to the network available on your workstation. However, apps connect through the emulator, not directly to hardware, and the emulator acts like a normal app on your workstation. This can cause some limitations:

- Communication with the emulated device may be blocked by a firewall program running on your machine.
- Communication with the emulated device may be blocked by another (physical) firewall or router where your machine is connected.

The emulator's virtual router should be able to handle all outbound TCP and UDP connections and messages on behalf of the emulated device, provided your development machine network environment lets it. There are no built-in limitations on port numbers or ranges, only those imposed by your host operating system and network.

Depending on the environment, the emulator might not be able to support other protocols (such as ICMP, used for "ping"). Currently, the emulator does not support IGMP or multicast.

## Use network redirection

To communicate with an emulator instance behind its virtual router, set up network redirection on the virtual router. Clients can then connect to a specified guest port on the router, while the router directs traffic to and from that port to the emulated device host port.

To set up the network redirection, create a mapping of host and guest ports and addresses on the emulator instance. There are two ways to set up network redirection: using emulator console commands and using the Android Debug Bridge (`adb`) tool, as described in the following sections.

### Set up redirection through the emulator console

Each emulator instance provides a control console that you can connect to and issue commands to that are specific to that instance. Use the`redir`console command to set up redirection as needed for an emulator instance.

First, determine the console port number for the target emulator instance. For example, the console port number for the first emulator instance launched is 5554. Next, connect to the console of the target emulator instance, specifying its console port number, as follows:  

    telnet localhost 5554

Once connected, you must authenticate before you can set up redirection. See[Start and stop a console session](https://developer.android.com/studio/run/emulator-console#console-session)for details about how to do this. Once authenticated, use the`redir`command to work with redirection.

To add a redirection, use:  

    redir add <protocol>:<host-port>:<guest-port>

Where`<protocol>`is either`tcp`or`udp`, and`<host-port>`and`<guest-port>`set the mapping between your machine and the emulated system.

For example, the following command sets up a redirection that handles all incoming TCP connections to your host (development) machine on 127.0.0.1:5000 and passes them through to the emulated system on 10.0.2.15:6000:  

```
redir add tcp:5000:6000
```

To delete a redirection, use the`redir del`command. To list all redirection for a specific instance, use`redir
list`. For more information about these and other console commands, see[Send Emulator console commands](https://developer.android.com/studio/run/emulator-console).

Note that port numbers are restricted by your local environment. This typically means that you cannot use host port numbers under 1024 without special administrator privileges. Also, you won't be able to set up a redirection for a host port that is already in use by another process on your machine. In that case,`redir`generates an error message to that effect.

### Set up redirection through adb

The Android Debug Bridge (`adb`) tool provides port forwarding, an alternate way for you to set up network redirection. For more information, see[Set up port forwarding](https://developer.android.com/studio/command-line/adb#forwardports)in the`adb`documentation.

Note that`adb`doesn't currently offer a way to remove a redirection except by stopping the`adb`server.

## Configure emulator DNS settings

At startup, the emulator reads the list of DNS servers that your system is currently using. It then stores the IP addresses of up to four servers on this list and sets up aliases to them on the emulated addresses 10.0.2.3, 10.0.2.4, 10.0.2.5, and 10.0.2.6, as needed.

On Linux and macOS, the emulator obtains the DNS server addresses by parsing the file`/etc/resolv.conf`. On Windows, the emulator obtains the addresses by calling the`GetNetworkParams()`API. Note that this usually means that the emulator ignores the content of your "hosts" file (`/etc/hosts`on Linux/macOS,`%WINDOWS%/system32/HOSTS`on Windows).

When starting the emulator from the command line, you can use the`-dns-server <serverList>`option to manually specify the addresses of DNS servers to use, where`<serverList>`is a comma-separated list of server names or IP addresses. You might find this option useful if you encounter DNS resolution problems in the emulated network (for example, an "Unknown Host error" message that appears when using the web browser).

## Use the emulator with a proxy

On many corporate networks, direct connections to the internet are refused by network administrators. Instead, internet connections must pass through a specific proxy. To access the internet on a network with a proxy requirement, the emulator needs to know that there is a proxy and that it needs to connect to it.

Due to the nature of HTTP, a direct web server connection and a connection through a proxy result in different GET requests. The emulator transparently rewrites the GET requests from the virtual device before talking to the proxy so it works.

If your emulator must access the internet through a proxy server, you can configure a custom HTTP proxy.

When using the emulator**within Android Studio** , you can configure a proxy with the settings in the Android Studio Menu (`Settings > Appearance & Behavior > System Settings > HTTP Proxy`). You can find more details at[Set up the Android Studio proxy](https://developer.android.com/studio/intro/studio-config#setup-proxy)in the`Android Studio`documentation.

When using the emulator as standalone (**outside of Android Studio** ), you can configure a proxy from the emulator's**Extended controls**screen:

1. With the emulator open, click**More** ![](https://developer.android.com/static/studio/images/buttons/emulator-extended-controls.png).
2. Click**Settings** and**Proxy**(only available if the emulator was not launched from Android Studio).
3. Define your HTTP proxy settings.

![](https://developer.android.com/static/studio/images/run/emulator-proxy-settings_2x.png)

Alternatively, you can configure a proxy from the command line with the`-http-proxy <proxy>`option when starting the emulator. In this case, specify proxy information in`<proxy>`in one of these formats:  

```
http://<machineName>:<port>
```

or  

```
http://<username>:<password>@<machineName>:<port>
```

The`-http-proxy`option forces the emulator to use the specified HTTP or HTTPS proxy for all outgoing TCP connections. Redirection for UDP is not supported.

Alternatively, you can define the environment variable`http_proxy`with the value you want to use for`<proxy>`. In this case, you do not need to specify a value for`<proxy>`in the`-http-proxy`command---the emulator checks the value of the`http_proxy`environment variable at startup and uses its value automatically, if it is defined.

You can use the`-debug-proxy`option to diagnose proxy connection problems.

## Interconnect emulator instances

To let one emulator instance communicate with another, set up network redirection as described below.

Assume that your environment is represented as follows:

- A is your development machine.
- B is your first emulator instance, running on A.
- C is your second emulator instance, also running on A.

If you want to run a server on B to which C will connect, set it up as follows:

1. Set up the server on B, listening to 10.0.2.15:\<serverPort\>.
2. On the B console, set up a redirection from A:localhost:\<localPort\> to B:10.0.2.15:\<serverPort\>.
3. On C, have the client connect to 10.0.2.2:\<localPort\>.

For example, if you want to run an HTTP server, select`<serverPort>`as 80 and`<localPort>`as 8080:

- B listens on 10.0.2.15:80.
- On the B console, issue`redir add tcp:8080:80.`
- C connects to 10.0.2.2:8080.

## Send a voice call or SMS to another emulator instance

The emulator automatically forwards simulated voice calls and SMS messages from one instance to another. To send a voice call or SMS, use the dialer app or SMS app, respectively, from one of the emulators.

To initiate a simulated voice call to another emulator instance:

1. Launch the dialer app on the originating emulator instance.
2. As the number to dial, enter the console port number of the target instance.

   You can determine the console port number of the target instance by checking its window title, if it is running in a separate window, but not if it is running in a tool window. The console port number is reported as "Android Emulator (\<port\>)".

   Alternatively, the`adb devices`command prints a list of running virtual devices and their console port numbers. For more information, see[Query for devices](https://developer.android.com/studio/command-line/adb#devicestatus).
3. Click the dial button. A new inbound call appears in the target emulator instance.

To send an SMS message to another emulator instance:

1. Launch the SMS app, if available.
2. Specify the console port number of the target emulator instance as as the SMS address.
3. Enter the message text.
4. Send the message. The message is delivered to the target emulator instance.

You can also connect to an emulator console to simulate an incoming voice call or SMS. For more information, see[Telephony emulation](https://developer.android.com/studio/run/emulator-console#telephony)and[SMS emulation](https://developer.android.com/studio/run/emulator-console#sms).