---
title: https://developer.android.com/training/wearables/data/client-types
url: https://developer.android.com/training/wearables/data/client-types
source: md.txt
---

The Wear OS data layer APIs consist of several different types of clients, which
are useful for different types of data and during different connectivity
conditions.

This page introduces each client type, and it includes a table that compares the
capabilities of the different clients. Using this information, you can select
the set of client types that works best for your app.

## Data client

A [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) object lets you read or write to a [`DataItem`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataItem) or
[`Asset`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Asset):

- Each `DataItem` is a unit of information that's broadcast and synchronized
  across all nearby devices that a user owns. A `DataItem` is stored persistently,
  and your device can read its contents until the data item is deleted.

- An `Asset` is meant for larger data payloads, such as images or media files.

## Message client

A [`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient) object can send messages and is good for remote procedure
calls (RPC), such as using a Wear OS device to control the version of your app
that's installed on a handheld device.

Messages are great for one-way requests using `sendMessage()`, or for a
request-and-response communication model using `sendRequest()`. Unlike with data
clients, message clients need the nodes to be connected to the network in order
to send messages.

The `sendMessage()` method is a best effort to deliver to the remote node, and
it doesn't contain any built-in retry mechanism. If the target device
disconnects before the network transfer starts, the method returns
`TARGET_NODE_NOT_CONNECTED`.

> [!NOTE]
> **Note:** To help preserve power, consider sending messages only to nearby devices.

## Channel client

A [`ChannelClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/ChannelClient) object provides stream-oriented communication between
devices. A *channel* is a bidirectional communication pipe between two nodes,
which is useful for use cases such as the following:

- Transfer data files between two or more connected devices when the internet isn't available. `ChannelClient` saves disk space over `DataClient`, which creates a copy of the assets on the local device before synchronizing with connected devices.
- Reliably send a file that's too large to send using a `MessageClient`.
- Transfer streamed data, such as voice data from the microphone.

After you open a channel, you can send and receive data in a continuous byte
stream, rather than the discrete `DataItem` units that data clients require.

You're responsible for managing the data flow and keeping data consistent.
Channel clients don't offer the same level of automatic data synchronization
that data clients do.

## Client comparison

The following table compares the capabilities of the different clients:

| Client type | Data persistence | Supports data larger than 100 KB? | Network to use | Works offline? |
|---|---|---|---|---|
| **Data client** | Data is persisted indefinitely | Yes (use [`Asset`](https://developers.google.com/android/reference/com/google/android/gms/wearable/Asset) objects) | Bluetooth preferred. Data is backed up to the cloud; if Bluetooth is available, this backup is done asynchronously | Yes, for both read and write |
| **Message client** | No persistence and no retry | No | Bluetooth preferred, but can use Wi-Fi if it's the only type of connection available | No |
| **Channel client** | No persistence (connection-oriented) | Yes | Bluetooth preferred, but can use Wi-Fi if it's the only type of connection available | No |