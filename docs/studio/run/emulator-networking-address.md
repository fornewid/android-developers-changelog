---
title: Network address space  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/run/emulator-networking-address
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Network address space Stay organized with collections Save and categorize content based on your preferences.




The emulator provides versatile networking capabilities that you can use to set
up complex modeling and testing environments for your app. This page introduces
the emulator network architecture and capabilities.

The virtual router for each instance manages the `10.0.2/24` network address
space.

* All addresses managed by the router are in the form of `10.0.2.xx`, where
  `xx` is a number.

The following table shows how addresses within this space are pre-allocated by
the emulator or router:

| Network Address | Description |
| --- | --- |
| 10.0.2.1 | Router or gateway address |
| 10.0.2.2 | Special alias to your host loopback interface (127.0.0.1 on your development machine) |
| 10.0.2.3 | First DNS server |
| 10.0.2.4, 10.0.2.5, 10.0.2.6 | Optional second, third, and fourth DNS servers |
| 10.0.2.15 | The emulated device network when connected using ethernet |
| 10.0.2.16 | The emulated device network when connected using Wi-Fi. |
| 127.0.0.1 | The emulated device loopback interface |

**Note:** After Android Emulator version 36.5: When multiple emulated devices are
connected using Wi-Fi, they are assigned addresses starting with `10.0.2.16`,
`10.0.2.17`, and subsequent addresses.**Note:** In Android Emulator versions earlier than 36.5, each instance of the
emulator runs behind a virtual router or firewall service that isolates it from
your development machine network interfaces and settings and from the internet.
An emulated device can't detect your development machine or other emulator
instances on the network. It detects only that it is connected through ethernet
to a router or firewall.

Besides Wi-Fi, the same address assignments are used by all running emulator
instances when connected using ethernet. This means that if you have two
instances running concurrently on your machine, each will have its own router,
and behind that, each will have an IP address of `10.0.2.15`. The instances are
isolated by a router and can't detect each other on the same network. For
information about how to let emulator instances communicate over TCP/UDP, see
[Interconnect emulator instances](/studio/run/emulator-networking-interconnect-ethernet).

The address 127.0.0.1 on your development machine corresponds to the emulator's
loopback interface. To access services running on your development machine
loopback interface, use the special address `10.0.2.2` instead.

The pre-allocated addresses of an emulated device are specific to the Android
Emulator and are likely to be different on real devices (which are also likely
to be network address translated, specifically behind a router or firewall).

## Local networking limitations

Android apps running on an emulator can connect to the network available on your
workstation. However, apps connect through the emulator, not directly to
hardware, and the emulator acts like a normal app on your workstation. This can
cause some limitations:

* Communication with the emulated device might be blocked by a firewall
  program running on your machine.
* Communication with the emulated device might be blocked by another
  (physical) firewall or router where your machine is connected.

The emulator's virtual router can handle all outbound TCP and UDP connections
and messages for the emulated device, provided your development machine's
network environment allows these connections. There are no built-in limitations
on port numbers or ranges, only those imposed by your host operating system and
network.

Depending on the environment, the emulator might not support other protocols,
such as ICMP, which is used for "ping". The emulator does not support IGMP.
For example, users cannot use the ping command to ping the host machine or other
devices on the Local Area Network.