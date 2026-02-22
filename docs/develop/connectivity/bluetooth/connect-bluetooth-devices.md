---
title: https://developer.android.com/develop/connectivity/bluetooth/connect-bluetooth-devices
url: https://developer.android.com/develop/connectivity/bluetooth/connect-bluetooth-devices
source: md.txt
---

To create a connection between two devices, you must implement both the
server-side and client-side mechanisms because one device must open a server
socket, and the other one must initiate the connection using the server device's
MAC address. The server device and the client device each obtain the required
[`BluetoothSocket`](https://developer.android.com/reference/android/bluetooth/BluetoothSocket) in different
ways. The server receives socket information when an incoming connection is
accepted. The client provides socket information when it opens an RFCOMM channel
to the server.

The server and client are considered connected to each other when they each have
a connected `BluetoothSocket` on the same RFCOMM channel. At this point, each
device can obtain input and output streams, and data transfer can begin, which
is discussed in the section about [transferring Bluetooth
data](https://developer.android.com/develop/connectivity/bluetooth/transfer-data). This section
describes how to initiate the connection between two devices.

Make sure you have the appropriate
[Bluetooth permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions) and
[set up your app for Bluetooth](https://developer.android.com/develop/connectivity/bluetooth/setup) before
attempting to find Bluetooth devices.

## Connection techniques

One implementation technique is to automatically prepare each device as a server
so that each device has a server socket open and listening for connections. In
this case, either device can initiate a connection with the other and become the
client. Alternatively, one device can explicitly host the connection and open a
server socket on demand, and the other device initiates the connection.

![](https://developer.android.com/static/images/develop/connectivity/bluetooth/bluetooth-pairing.png)   

**Figure 1.** The Bluetooth pairing dialog.
| **Note:** If the two devices have not been previously paired, then the Android framework automatically shows a pairing request notification or dialog to the user during the connection procedure, as shown in figure 1. Therefore, when your app attempts to connect devices, it doesn't need to be concerned about whether or not the devices are paired. Your RFCOMM connection attempt gets blocked until the user has successfully paired the two devices, and the attempt fails if the user rejects pairing, or if the pairing process fails or times out.

### Connect as a server

When you want to connect two devices, one must act as a server by holding an
open
[`BluetoothServerSocket`](https://developer.android.com/reference/android/bluetooth/BluetoothServerSocket).
The purpose of the server socket is to listen for incoming connection requests
and provide a connected `BluetoothSocket` after a request is accepted. When the
`BluetoothSocket` is acquired from the `BluetoothServerSocket`, the
`BluetoothServerSocket` can---and should---be discarded, unless you want
the device to accept more connections.

To set up a server socket and accept a connection, complete the following
sequence of steps:

1. Get a `BluetoothServerSocket` by calling
   [`listenUsingRfcommWithServiceRecord(String, UUID)`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#listenUsingRfcommWithServiceRecord(java.lang.String,%20java.util.UUID)).

   The string is an identifiable name of your service, which the system
   automatically writes to a new Service Discovery Protocol (SDP) database entry
   on the device. The name is arbitrary and can simply be your app name.
   The Universally Unique Identifier (UUID) is also included in the SDP entry
   and forms the basis for the connection agreement with the client device. That
   is, when the client attempts to connect with this device, it carries a UUID
   that uniquely identifies the service with which it wants to connect. These
   UUIDs must match in order for the connection to be accepted.

   A UUID is a standardized 128-bit format for a string ID used to uniquely
   identify information. A UUID is used to identify information that needs to be
   unique within a system or a network because the probability of a UUID being
   repeated is effectively zero. It is generated independently, without the use
   of a centralized authority. In this case, it's used to uniquely identify your
   app's Bluetooth service. To get a UUID to use with your app, you can use one
   of the many random
   [`UUID`](https://developer.android.com/reference/java/util/UUID) generators on the web, then initialize a
   UUID with
   [`fromString(String)`](https://developer.android.com/reference/java/util/UUID#fromString(java.lang.String)).
2. Start listening for connection requests by calling
   [`accept()`](https://developer.android.com/reference/android/bluetooth/BluetoothServerSocket#accept()).

   This is a blocking call. It returns when either a connection has been
   accepted or an exception has occurred. A connection is accepted only when a
   remote device has sent a connection request containing a UUID that matches
   the one registered with this listening server socket. When successful,
   `accept()` returns a connected `BluetoothSocket`.
3. Unless you want to accept additional connections, call
   [`close()`](https://developer.android.com/reference/android/bluetooth/BluetoothServerSocket#close()).

   This method call releases the server socket and all its resources, but
   doesn't close the connected `BluetoothSocket` that's been returned by
   `accept()`. Unlike TCP/IP, RFCOMM allows only one connected client per
   channel at a time, so in most cases it makes sense to call `close()` on the
   `BluetoothServerSocket` immediately after accepting a connected socket.

Because the `accept()` call is a blocking call, do not execute it in the main
activity UI thread. Executing it in another thread ensures that your app can
still respond to other user interactions. It usually makes sense to do all work
that involves a `BluetoothServerSocket` or `BluetoothSocket` in a new thread
managed by your app. To abort a blocked call such as `accept()`, call `close()`
on the `BluetoothServerSocket` or `BluetoothSocket` from another thread. Note
that all methods on a `BluetoothServerSocket` or `BluetoothSocket` are
thread-safe.

#### Example

The following is a simplified thread for the server component that accepts
incoming connections:  

### Kotlin

```kotlin
private inner class AcceptThread : Thread() {

   private val mmServerSocket: BluetoothServerSocket? by lazy(LazyThreadSafetyMode.NONE) {
       bluetoothAdapter?.listenUsingInsecureRfcommWithServiceRecord(NAME, MY_UUID)
   }

   override fun run() {
       // Keep listening until exception occurs or a socket is returned.
       var shouldLoop = true
       while (shouldLoop) {
           val socket: BluetoothSocket? = try {
               mmServerSocket?.accept()
           } catch (e: IOException) {
               Log.e(TAG, "Socket's accept() method failed", e)
               shouldLoop = false
               null
           }
           socket?.also {
               manageMyConnectedSocket(it)
               mmServerSocket?.close()
               shouldLoop = false
           }
       }
   }

   // Closes the connect socket and causes the thread to finish.
   fun cancel() {
       try {
           mmServerSocket?.close()
       } catch (e: IOException) {
           Log.e(TAG, "Could not close the connect socket", e)
       }
   }
}
```

### Java

```java
private class AcceptThread extends Thread {
   private final BluetoothServerSocket mmServerSocket;

   public AcceptThread() {
       // Use a temporary object that is later assigned to mmServerSocket
       // because mmServerSocket is final.
       BluetoothServerSocket tmp = null;
       try {
           // MY_UUID is the app's UUID string, also used by the client code.
           tmp = bluetoothAdapter.listenUsingRfcommWithServiceRecord(NAME, MY_UUID);
       } catch (IOException e) {
           Log.e(TAG, "Socket's listen() method failed", e);
       }
       mmServerSocket = tmp;
   }

   public void run() {
       BluetoothSocket socket = null;
       // Keep listening until exception occurs or a socket is returned.
       while (true) {
           try {
               socket = mmServerSocket.accept();
           } catch (IOException e) {
               Log.e(TAG, "Socket's accept() method failed", e);
               break;
           }

           if (socket != null) {
               // A connection was accepted. Perform work associated with
               // the connection in a separate thread.
               manageMyConnectedSocket(socket);
               mmServerSocket.close();
               break;
           }
       }
   }

   // Closes the connect socket and causes the thread to finish.
   public void cancel() {
       try {
           mmServerSocket.close();
       } catch (IOException e) {
           Log.e(TAG, "Could not close the connect socket", e);
       }
   }
}
```

In this example, only one incoming connection is desired, so as soon as a
connection is accepted and the `BluetoothSocket` is acquired, the app passes the
acquired `BluetoothSocket` to a separate thread, closes the
`BluetoothServerSocket`, and breaks out of the loop.

Note that when `accept()` returns the `BluetoothSocket`, the socket is already
connected. Therefore, you shouldn't call
[`connect()`](https://developer.android.com/reference/android/bluetooth/BluetoothSocket#connect()), as you do
from the client side.

The app-specific `manageMyConnectedSocket()` method is designed to initiate the
thread for transferring data, which is discussed in the topic about
[transferring Bluetooth
data](https://developer.android.com/develop/connectivity/bluetooth/transfer-data).

Usually, you should close your `BluetoothServerSocket` as soon as you are done
listening for incoming connections. In this example, `close()` is called as soon
as the `BluetoothSocket` is acquired. You may also want to provide a public
method in your thread that can close the private `BluetoothSocket` in the event
that you need to stop listening on that server socket.

### Connect as a client

In order to initiate a connection with a remote device that is accepting
connections on an open server socket, you must first obtain a `BluetoothDevice`
object that represents the remote device. To learn how to create a
`BluetoothDevice`, see [Find Bluetooth
devices](https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices). You must
then use the `BluetoothDevice` to acquire a `BluetoothSocket` and initiate the
connection.

The basic procedure is as follows:

1. Using the `BluetoothDevice`, get a `BluetoothSocket` by calling
   [`createRfcommSocketToServiceRecord(UUID)`](https://developer.android.com/reference/android/bluetooth/BluetoothDevice#createRfcommSocketToServiceRecord(java.util.UUID)).

   This method initializes a `BluetoothSocket` object that allows the client to
   connect to a `BluetoothDevice`. The UUID passed here must match the UUID used
   by the server device when it called
   [`listenUsingRfcommWithServiceRecord(String, UUID)`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#listenUsingRfcommWithServiceRecord(java.lang.String,%20java.util.UUID))
   to open its `BluetoothServerSocket`. To use a matching UUID, hard-code the
   UUID string into your app, and then reference it from both the server
   and client code.
2. Initiate the connection by calling `connect()`. Note that this method is a
   blocking call.

   After a client calls this method, the system performs an SDP lookup to find
   the remote device with the matching UUID. If the lookup is successful and the
   remote device accepts the connection, it shares the RFCOMM channel to use
   during the connection, and the `connect()` method returns. If the connection
   fails, or if the `connect()` method times out (after about 12 seconds), then
   the method throws an [`IOException`](https://developer.android.com/reference/java/io/IOException).

Because `connect()` is a blocking call, you should always perform this
connection procedure in a thread that is separate from the main activity (UI)
thread.

#### Example

The following is a basic example of a client thread that initiates a Bluetooth
connection:  

### Kotlin

```kotlin
private inner class ConnectThread(device: BluetoothDevice) : Thread() {

   private val mmSocket: BluetoothSocket? by lazy(LazyThreadSafetyMode.NONE) {
       device.createRfcommSocketToServiceRecord(MY_UUID)
   }

   public override fun run() {
       // Cancel discovery because it otherwise slows down the connection.
       bluetoothAdapter?.cancelDiscovery()

       mmSocket?.let { socket ->
           // Connect to the remote device through the socket. This call blocks
           // until it succeeds or throws an exception.
           socket.connect()

           // The connection attempt succeeded. Perform work associated with
           // the connection in a separate thread.
           manageMyConnectedSocket(socket)
       }
   }

   // Closes the client socket and causes the thread to finish.
   fun cancel() {
       try {
           mmSocket?.close()
       } catch (e: IOException) {
           Log.e(TAG, "Could not close the client socket", e)
       }
   }
}
```

### Java

```java
private class ConnectThread extends Thread {
   private final BluetoothSocket mmSocket;
   private final BluetoothDevice mmDevice;

   public ConnectThread(BluetoothDevice device) {
       // Use a temporary object that is later assigned to mmSocket
       // because mmSocket is final.
       BluetoothSocket tmp = null;
       mmDevice = device;

       try {
           // Get a BluetoothSocket to connect with the given BluetoothDevice.
           // MY_UUID is the app's UUID string, also used in the server code.
           tmp = device.createRfcommSocketToServiceRecord(MY_UUID);
       } catch (IOException e) {
           Log.e(TAG, "Socket's create() method failed", e);
       }
       mmSocket = tmp;
   }

   public void run() {
       // Cancel discovery because it otherwise slows down the connection.
       bluetoothAdapter.cancelDiscovery();

       try {
           // Connect to the remote device through the socket. This call blocks
           // until it succeeds or throws an exception.
           mmSocket.connect();
       } catch (IOException connectException) {
           // Unable to connect; close the socket and return.
           try {
               mmSocket.close();
           } catch (IOException closeException) {
               Log.e(TAG, "Could not close the client socket", closeException);
           }
           return;
       }

       // The connection attempt succeeded. Perform work associated with
       // the connection in a separate thread.
       manageMyConnectedSocket(mmSocket);
   }

   // Closes the client socket and causes the thread to finish.
   public void cancel() {
       try {
           mmSocket.close();
       } catch (IOException e) {
           Log.e(TAG, "Could not close the client socket", e);
       }
   }
}
```

Notice that in this snippet, `cancelDiscovery()` is called before the connection
attempt occurs. You should always call `cancelDiscovery()` before `connect()`,
especially because `cancelDiscovery()` succeeds regardless of whether device
discovery is currently in progress. If your app needs to determine whether
device discovery is in progress, you can check using
[`isDiscovering()`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#isDiscovering()).

The app-specific `manageMyConnectedSocket()` method is designed to initiate the
thread for transferring data, which is discussed in the section about
[transferring Bluetooth data](https://developer.android.com/develop/connectivity/bluetooth/transfer-data).

When you're done with your `BluetoothSocket`, always call `close()`. Doing so
immediately closes the connected socket and releases all related internal
resources.