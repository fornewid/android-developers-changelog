---
title: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/secure-connection
url: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/secure-connection
source: md.txt
---

# Secure connection API

After discovering a remote device, the `handleIntent` function is called, and
it's time to start passing data between clients. This section covers the
four essential steps of maintaining a secure connection:

- Opening a connection
- Accepting the connection
- Sending and receiving data
- Closing the connection

## Open a connection

To open a connection to receive data from a remote device, use the
previously received participant object and specify `CHANNEL_NAME`:  

### Kotlin

```kotlin
participant
  .openConnection(CHANNEL_HELLO)
  .onFailure { /* handle failure */}
  .getOrNull()
  ?.let { connection ->
    connection.send("Hello, world".toByteArray(UTF_8)).onFailure { /* handle failure */}
  }
```

### Java

```java
public void openConnection(Participant participant) {
  Futures.addCallback(
      participant.openConnectionFuture(CHANNEL_HELLO),
      new FutureCallback<RemoteConnection>() {
        @Override
        public void onSuccess(RemoteConnection remoteConnection) {
          // use remoteConnection object to pass data, e.g.:
          sendDataToRemoteConnection(remoteConnection);
        }

        @Override
        public void onFailure(Throwable t) {
          // handle error opening a remote connection
        }
      },
      mainExecutor);
}

private void sendDataToRemoteConnection(RemoteConnection remoteConnection) {
  Futures.addCallback(
      remoteConnection.sendFuture("Hello, world".getBytes()),
      new FutureCallback<Void>() {
        @Override
        public void onSuccess(Void result) {
          // data sent successfully
        }

        @Override
        public void onFailure(Throwable t) {
          // handle error
        }
      },
      mainExecutor);
}
```

## Accept, send/receive, and close a connection

Secure connections require the receiving device to accept incoming connections
before receiving the data. To accept a remote connection, use the following
snippet:  

### Kotlin

```kotlin
suspend fun acceptIncomingConnection(participant: Participant) {
  val connection = participant.acceptConnection(CHANNEL_HELLO).getOrThrow()
  connection.registerReceiver(
    object : ConnectionReceiver {
      override fun onMessageReceived(remoteConnection: RemoteConnection, payload: ByteArray) {
        displayMessage(payload.toString(UTF_8))
      }

      override fun onConnectionClosed(
        remoteConnection: RemoteConnection,
        error: Throwable?,
        reason: String?
      ) {
        // handle connection closure
      }
    }
  )
}
```

### Java

```java
public void acceptIncomingConnection(Participant participant) {
  // Registers call back to accept incoming remote connection
  Futures.addCallback(
      participant.acceptConnectionFuture(CHANNEL_HELLO),
      new FutureCallback<>() {
        @Override
        public void onSuccess(RemoteConnection result) {
          receiveData(result);
        }

        @Override
        public void onFailure(Throwable t) {
          // handle connection error
        }
      },
      mainExecutor);
}

private void receiveData(RemoteConnection remoteConnection) {
  remoteConnection.registerReceiver(
      new ConnectionReceiver() {
        @Override
        public void onMessageReceived(RemoteConnection remoteConnection, byte[] payload) {
          displayMessage(new String(payload, UTF_8));
        }

        @Override
        public void onConnectionClosed(
            RemoteConnection remoteConnection,
            @Nullable Throwable error,
            @Nullable String reason) {
          // handle connection closure
        }
      });
}
```