---
title: https://developer.android.com/studio/run/emulator-networking-interconnect
url: https://developer.android.com/studio/run/emulator-networking-interconnect
source: md.txt
---

To test applications that involve multi-device interactions, you can connect
multiple Android Emulator instances so they can communicate with each other.
The method for establishing a connection depends on the version of the emulator
you are using.

## Android Emulators Version 36.5 and Later

Android Emulator Version 36.5 and later offer a simplified networking model that
connects instances over a shared Wi-Fi network.

With this networking stack, multiple emulators appear as distinct devices on the
same virtual Wi-Fi network. This allows them to discover and communicate with
each other automatically using standard Wi-Fi-based protocols.

Emulators can find each other on the virtual network using technologies like
[Network Service Discovery](https://developer.android.com/develop/connectivity/wifi/use-nsd)
(NSD) and
[Wi-Fi Direct](https://developer.android.com/develop/connectivity/wifi/wifip2p).

Because the emulators are on the same Wi-Fi network, you can also find an
emulator's specific IP address and connect to it directly from another emulator
instance. To get the IP address of the virtual Wi-Fi interface (`wlan0`), run
the following command from your host machine:

    adb shell ip addr show wlan0

## Android Emulator Prior to Version 36.5

If you are using an earlier version of the Android Emulator, direct
communication between instances is not possible by default. Each emulator
instance operates behind its own virtual router, isolating it from the local
network and other emulators.

To enable communication, you must manually set up network redirection. This
process involves creating a mapping that forwards traffic from a specific port
on your host machine to a port on the emulated device, bypassing the virtual
router.

You can configure network redirection in two ways:

1. *Emulator Console Commands*: Use the built-in console to set up port mappings for the running emulator instance.
2. *Android Debug Bridge (adb)*: Use adb commands to configure the necessary port forwarding rules.

### Set up redirection through the emulator console

Each emulator instance provides a control console that you can connect to and
issue commands to that are specific to that instance. Use the `redir` console
command to set up redirection as needed for an emulator instance.

First, determine the console port number for the target emulator instance. For
example, the console port number for the first emulator instance launched is
5554. Next, connect to the console of the target emulator instance,
specifying its console port number, as follows:

        telnet localhost 5554

Once connected, you must authenticate before you can set up redirection. See
[Start and stop a console session](https://developer.android.com/studio/run/emulator-console#console-session)
for details about how to do this. Once authenticated, use the `redir` command to
work with redirection.

To add a redirection, use the following command:

        redir add <protocol>:<host-port>:<guest-port>

Where `<protocol>` is either `tcp` or `udp`, and `<host-port>` and `<guest-
port>` set the mapping between your machine and the emulated system.

For example, the following command sets up a redirection that handles all
incoming TCP connections to your host (development) machine on 127.0.0.1:5000
and passes them through to the emulated system on 10.0.2.15:6000:

        redir add tcp:5000:6000

To delete a redirection, use the `redir del` command. To list all redirection
for a specific instance, use `redir list`. For more information about these
and other console commands, see [Send Emulator console
commands](https://developer.android.com/studio/run/emulator-console).

Port numbers are restricted by your local environment. This
typically means that you cannot use host port numbers under 1024 without
special administrator privileges. Also, you won't be able to set up a
redirection for a host port that is already in use by another process on your
machine. In that case, `redir` generates an error message to that effect.

### Set up redirection through adb

The Android Debug Bridge (`adb`) tool provides port forwarding, an alternate
way for you to set up network redirection. For more information, see [Set up
port forwarding](https://developer.android.com/studio/command-line/adb#forwardports) in the `adb`
documentation.

`adb` doesn't currently offer a way to remove a redirection except by stopping
the `adb` server.

### Interconnect emulator instances

To allow one emulator instance to communicate with another, set up network
redirection as described in the following steps.

Assume that your environment is as follows:

- A is your development machine.
- B is your first emulator instance, running on A.
- C is your second emulator instance, also running on A.

If you want to run a server on B to which C will connect, set it up as
follows:

1. Set up the server on B, listening to `10.0.2.15:<serverPort>`.
2. On the B console, set up a redirection from A: `localhost:<localPort>` to B: `10.0.2.15:<serverPort>`.
3. On C, connect the client to `10.0.2.2:<localPort>`.

For example, if you want to run an HTTP server, select `<serverPort>` as `80`
and `<localPort>` as `8080`:

- B listens on `10.0.2.15:80`.
- On the B console, issue `redir add tcp:8080:80`.
- C connects to `10.0.2.2:8080`.