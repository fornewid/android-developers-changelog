---
title: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/sessions
url: https://developer.android.com/guide/topics/connectivity/cross-device-sdk/sessions
source: md.txt
---

Building on the[Device Discovery](https://developer.android.com/guide/topics/connectivity/cross-device-sdk/device-discovery)and[Secure Connection](https://developer.android.com/guide/topics/connectivity/cross-device-sdk/secure-connection)APIs, the Sessions API provides a powerful abstraction to build seamless cross-device experiences. A session represents an application user experience that can be transferred and shared across devices.

The Sessions API is also built around the notion of personal and communal experiences represented by session transfer and session share use cases respectively. The following diagram illustrates sessions at a high level:  
![](https://developer.android.com/static/images/develop/connectivity/cross-device-sdk/flow-diagram.png)**Figure 1.**Sessions diagram.

## Create and transfer a session

The Sessions API differentiates between the originating device and the receiving device. The originating device creates the session and searches for a device capable of handling the session. The user of the originating device selects a device from the list provided by the system dialog. Once the user selects the receiving device, the originating session is transferred and removed from the originating device.

To transfer the session, you must first create it using the following parameters:

- An application session tag --- an identifier that allows you to differentiate between multiple sessions in your app.

Then initiate the transfer using the following parameters:

- A[`DeviceFilter`]()to filter devices capable of handling the session
- A callback object implementing`OriginatingSessionStateCallback`

On the originating device, create a session using the example below:  

### Kotlin

```kotlin
private val HELLO_WORLD_TRANSFER_ACTION = "hello_world_transfer"
private lateinit var originatingSession: OriginatingSession
private lateinit var sessions: Sessions

override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  sessions = Sessions.create(context = this)
}

suspend fun transferSession() {
  val sessionId =
    sessions.createSession(
      ApplicationSessionTag("hello_world_transfer"),
    )
  originatingSession =
    sessions.transferSession(
      sessionId,
      StartComponentRequest.Builder()
        .setAction(HELLO_WORLD_TRANSFER_ACTION)
        .setReason("Transfer reason here")
        .build(),
      emptyList(),
      HelloWorldTransferSessionStateCallback()
    )
}
```

### Java

```java
private static final String HELLO_WORLD_TRANSFER_ACTION = "hello_world_transfer";
private OriginatingSession originatingSession;
private Sessions sessions;

@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  sessions = Sessions.create(/* context= */ this);
}

public void transferSession() {
  SessionId sessionId = sessions.createSession(new ApplicationSessionTag("hello_world_transfer"));
  ListenableFuture<OriginatingSession> originatingSessionFuture =
      sessions.transferSessionFuture(
          sessionId,
          new StartComponentRequest.Builder()
              .setAction(HELLO_WORLD_TRANSFER_ACTION)
              .setReason("Transfer reason here")
              .build(),
          Collections.emptyList(),
          new HelloWorldTransferSessionStateCallback());
  Futures.addCallback(
      originatingSessionFuture,
      new FutureCallback<>() {
        @Override
        public void onSuccess(OriginatingSession result) {
          // Do nothing, handled in HelloWorldTransferSessionStateCallback
          originatingSession = result;
        }

        @Override
        public void onFailure(Throwable t) {
          Log.d(TAG, "onFailure called for transferSessionFuture", t);
        }
      },
      mainExecutor);
}
```

Next, define the session callback on the originating device:  

### Kotlin

```kotlin
private inner class HelloWorldTransferSessionStateCallback : OriginatingSessionStateCallback {
  override fun onConnected(sessionId: SessionId) {
    val startupRemoteConnection = originatingSession.getStartupRemoteConnection()
    lifecycleScope.launchWhenResumed {
      startupRemoteConnection.send("hello, world".toByteArray(UTF_8))
      startupRemoteConnection.registerReceiver(
        object : SessionConnectionReceiver {
          override fun onMessageReceived(participant: SessionParticipant, payload: ByteArray) {
            val ok = payload.contentEquals("ok".toByteArray(UTF_8))
            Log.d(TAG, "Session transfer initialized. ok=$ok")
          }
        }
      )
    }
  }

  override fun onSessionTransferred(sessionId: SessionId) {
    Log.d(TAG, "Transfer done.")
  }

  override fun onTransferFailure(sessionId: SessionId, exception: SessionException) {
    // Handle error
  }
}
```

### Java

```java
private class HelloWorldTransferSessionStateCallback implements OriginatingSessionStateCallback {
  @Override
  public void onConnected(SessionId sessionId) {
    SessionRemoteConnection startupRemoteConnection =
        originatingSession.getStartupRemoteConnection();
    Futures.addCallback(
        startupRemoteConnection.sendFuture("hello, world".getBytes()),
        new FutureCallback<>() {
          @Override
          public void onSuccess(Void result) {
            Log.d(TAG, "Successfully sent initialization message");
          }

          @Override
          public void onFailure(Throwable t) {
            Log.d(TAG, "Failed to send initialization message", t);
          }
        },
        mainExecutor);
  }

  @Override
  public void onSessionTransferred(SessionId sessionId) {
    Log.d(TAG, "Transfer done.");
  }

  @Override
  public void onTransferFailure(SessionId sessionId, SessionException exception) {
    // Handle error
  }
}
```

Once the session transfer is initiated, the receiving device receives a callback in the`onNewIntent(intent: Intent)`method. The intent data contains everything necessary to transfer the session.

To complete the transfer on the receiving device:  

### Kotlin

```kotlin
private lateinit var sessions: Sessions

override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  sessions = Sessions.create(context = this)
}

override fun onNewIntent(intent: Intent) {
  super.onNewIntent(intent)
  lifecycleScope.launchWhenResumed {
    val receivingSession =
      sessions.getReceivingSession(intent, HelloWorldReceivingSessionStateCallback())

    // Get info from receiving device and init.
    val startupRemoteConnection = receivingSession.getStartupRemoteConnection()

    startupRemoteConnection.registerReceiver(
      object : SessionConnectionReceiver {
        override fun onMessageReceived(participant: SessionParticipant, payload: ByteArray) {
          lifecycleScope.launchWhenResumed {
            val transferInfo = String(payload)
            startupRemoteConnection.send("ok".toByteArray(UTF_8))
            // Complete transfer.
            Log.d(TAG, "Transfer info: " + transferInfo)
            receivingSession.onComplete()
          }
        }
      }
    )
  }
}

private inner class HelloWorldReceivingSessionStateCallback : ReceivingSessionStateCallback {
  override fun onTransferFailure(sessionId: SessionId, exception: SessionException) {
    // Handle error
  }
}
```

### Java

```java
private Sessions sessions;

@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  sessions = Sessions.create(/* context= */ this);
}

@Override
public void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  ListenableFuture<ReceivingSession> receivingSessionFuture =
      sessions.getReceivingSessionFuture(intent, new HelloWorldReceivingSessionStateCallback());
  ListenableFuture<Void> registerReceiverFuture =
      Futures.transform(
          receivingSessionFuture,
          receivingSession -> {
            SessionRemoteConnection startupRemoteConnection =
                receivingSession.getStartupRemoteConnection();
            SessionConnectionReceiver receiver =
                (participant, payload) -> {
                  Log.d(
                      TAG,
                      "Successfully received initialization message of size: " + payload.length);
                  applicationInitialization(receivingSession, payload);
                };
            startupRemoteConnection.registerReceiver(receiver);
            return null;
          },
          mainExecutor);
  Futures.addCallback(
      registerReceiverFuture,
      new Futu<reCa>llbackVoid() {
        @Override
        public void onSuccess(Void unused) {
          Log.d(TAG, "Connection receiver registerd successfully");
        }

        @Override
        public void onFailure(Throwable t) {
          Log.w(TAG, "Failed to register connection receiver", t);
        }
      },
      mainExecutor);
}

private void applicationInitialization(ReceivingSession receivingSession, byte[] ini<tMessage)> {
  ListenableFutureSessionId disconnectFuture =
      Futures.transform(
          receivingSession.onCompleteF>uture(),
          sessionId - {
            Log.d(TAG, "Succeeded to complete receive transfer for: " + sessionId);
            return sessionId;
          },
          mainExecutor);
  Futures.addCallback(
      di<sconnectF>uture,
      new FutureCallbackSessionId() {
        @Override
        public void onSuccess(SessionId result) {
          Log.d(TAG, "Succeeded to remove the old session: " + result);
        }

        @Override
        public void onFailure(Throwable t) {
          Log.d(TAG, "Failed to remove the old session, which is now orphaned", t);
        }
      },
      mainExecutor);
}

private static class HelloWorldReceivingSessionStateCallback
    implements ReceivingSessionStateCallback {
  @Override
  public void onTransferFailure(SessionId sessionId, SessionException exception) {
    // Handle error
  }
}
```

Now the receiving device can proceed with the user experience.

## Share a session

| **Note:** Sessions sharing is currently only available between two devices.

By sharing a session, you can invite others around you to participate in a group experience, for example:

- Share a map location as a passenger directly with your friend's car.
- Share your Sunday bike route with others that you're biking with.
- Collect items for a group food order without passing your phone around.
- Take a group vote for the next TV show to watch together.

When a user chooses to share a session with another device, the originating device searches for and presents devices capable of joining the session and the user selects the receiving device(s). The application prompts the user on a receiving device to join the session from the originating device. A receiving device is then given a secondary session to interact with the session on the originating device. Applications can also add additional participants to their ongoing shared session.

The process for sharing a session is similar to transferring a session, but instead of calling`transferSession`, call`shareSession`. The other differences are in the session state callback methods.  

### Kotlin

```kotlin
// Originating side.
private val HELLO_WORLD_SHARE_ACTION = "hello_world_share"
private var activePrimarySession: PrimarySession? = null
private lateinit var sessions: Sessions

override fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  sessions = Sessions.create(context = this)
}

suspend fun shareSession() {
  val sessionId = sessions.createSession(ApplicationSessionTag("hello_world_share"))
  activePrimarySession =
    sessions.shareSession(
      sessionId,
      StartComponentRequest.Builder()
        .setAction(HELLO_WORLD_SHARE_ACTION)
        .setReason("Share reason here")
        .build(),
      emptyList(),
      HelloWorldShareSessionStateCallback(),
    )
}

private inner class HelloWorldShareSessionStateCallback : PrimarySessionStateCallback {

  override fun onShareInitiated(sessionId: SessionId, numPotentialParticipants: Int) {
    // Custom logic here for when n devices can potentially join.
    // e.g. if there were 0, cancel/error if desired,
    //      if non-0 maybe spin until numPotentialParticipants join etc.
  }

  override fun onParticipantJoined(sessionId: SessionId, participant: SessionParticipant) {
    // Custom join logic here
    lifecycleScope.launchWhenResumed {
      // Example logic: send only to the participant who just joined.
      val connection =
        checkNotNull(activePrimarySession).getSecondaryRemoteConnectionForParticipant(participant)
      connection.send("Initing hello, world.".toByteArray(UTF_8))
      connection.registerReceiver(
        object : SessionConnectionReceiver {
          override fun onMessageReceived(participant: SessionParticipant, payload: ByteArray) {
            val ok = payload.contentEquals("ok".toByteArray(UTF_8))
            Log.d(TAG, "Session share initialized. ok=$ok")

            // Example logic: broadcast to all participants, including the one
            // that just joined.
            lifecycleScope.launchWhenResumed {
              checkNotNull(activePrimarySession)
                .broadcastToSecondaries("hello, all.".toByteArray(UTF_8))
            }
          }
        }
      )
    }
  }

  override fun onParticipantDeparted(sessionId: SessionId, participant: SessionParticipant) {
    // Custom leave logic here.
  }

  override fun onPrimarySessionCleanup(sessionId: SessionId) {
    // Custom cleanup logic here.
    activePrimarySession = null
  }

  override fun onShareFailureWithParticipant(
    sessionId: SessionId,
    exception: SessionException,
    participant: SessionParticipant
  ) {
    // Handle error
  }
}
```

### Java

```java
// Originating side
private static final String HELLO_WORLD_SHARE_ACTION = "hello_world_share";
@Nullable private PrimarySession activePrimarySession = null;
private Sessions sessions;

@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  sessions = Sessions.create(/* context= */ this);
}

private void shareSession() {
  SessionId sessionId = sessions.createSession(new ApplicationSessionTag("hello_world_share"))<;
  Listenable>FuturePrimarySession shareSessionFuture =
      sessions.shareSessionFuture(
          sessionId,
          new StartComponentRequest.Builder()
              .setAction(HELLO_WORLD_SHARE_ACTION)
              .setReason("Share reason here")
              .build(),
          Collections.emptyList(),
          new HelloWorldShareSessionStateCallback());
  Futures.addCallback(
      shareSessionFu<ture,
      ne>w FutureCallbackPrimarySession() {
        @Override
        public void onSuccess(PrimarySession primarySession) {
          activePrimarySession = primarySession;
        }

        @Override
        public void onFailure(Throwable t) {
          Log.d(TAG, "Failed to share session", t);
        }
      },
      mainExecutor);
}

private class HelloWorldShareSessionStateCallback implements PrimarySessionStateCallback {
  @Override
  public void onShareInitiated(SessionId sessionId, int numPotentialParticipants) {
    // Custom logic here for when n devices can potentially join.
    // e.g. if there were 0, cancel/error if desired,
    //      if non-0 maybe spin until numPotentialParticipants join etc.
  }

  @Override
  public void onParticipantJoined(SessionId sessionId, SessionParticipant participant) {
    PrimarySession joinedSession = activePrimarySession;
    if (joinedSession == null) {
      return;
    }
    SessionRemoteConnection connection =
        joinedSession.getSecondaryRemoteConnectionForParticipant(participant);
    Futures.addCallback(
        connection.sendFuture("Initiating hello, wo<rld.>".getBytes()),
        new FutureCallbackVoid() {
          @Override
          public void onSuccess(Void result) {
            // Send successful.
          }

          @Override
          public void onFailure(Throwable t) {
            // Failed to send.
          }
        },
        mainExecutor);
    connection.registerReceiver(
        new SessionConnectionReceiver() {
          @Override
          public void onMessageReceived(SessionParticipant participant, byte[] payload) {
            boolean ok = new String(payload, UTF_8).equals("ok");
            Log.d(TAG, "Session share initialized. ok=" + ok);

            // Example logic: broadcast to all participants, including the one
            // that just joined.
            Futures.addCallback(
                joinedSession.broadcastToSecondari<esFu>ture("hello, all.".getBytes()),
                new FutureCallbackVoid() {
                  @Override
                  public void onSuccess(Void result) {
                    // Broadcast successful.
                  }

                  @Override
                  public void onFailure(Throwable t) {
                    // Failed to broadcast hello world.
                  }
                },
                mainExecutor);
          }
        });
  }

  @Override
  public void onParticipantDeparted(SessionId sessionId, SessionParticipant participant) {
    // Custom leave logic here.
  }

  @Override
  public void onPrimarySessionCleanup(SessionId sessionId) {
    // Custom cleanup logic here.
    activePrimarySession = null;
  }

  @Override
  public void onShareFailureWithParticipant(
      SessionId sessionId, SessionException exception, SessionParticipant participant) {
    // Custom error handling logic here.
  }
}
```

On the receiving side:  

### Kotlin

```kotlin
// Receiving side.

override fun onNewIntent(intent: Intent) {
  super.onNewIntent(intent)
  lifecycleScope.launchWhenResumed {
    val secondarySession =
      sessions.getSecondarySession(intent, HelloWorldSecondaryShareSessionStateCallback())
    val remoteConnection = secondarySession.getDefaultRemoteConnection()

    remoteConnection.registerReceiver(
      object : SessionConnectionReceiver {
        override fun onMessageReceived(participant: SessionParticipant, payload: ByteArray) {
          Log.d(TAG, "Payload received: ${String(payload)}")
        }
      }
    )
  }
}

private inner class HelloWorldSecondaryShareSessionStateCallback : SecondarySessionStateCallback {
  override fun onSecondarySessionCleanup(sessionId: SessionId) {
    // Custom cleanup logic here.
  }
}
```

### Java

```java
// Receiving side.
@Override
public void onNewIntent(Intent intent) {
  super.onNewIntent(intent);
  sessions = Sessions.create(this);
  ListenableFuture<SecondarySession> secondarySessionFuture =
      sessions.getSecondarySessionFuture(
          intent, new HelloWorldSecondaryShareSessionStateCallback());
  Futures.addCallback(
      secondarySessionFuture,
      new FutureCallback<SecondarySession>() {
        @Override
        public void onSuccess(SecondarySession secondarySession) {
          SessionRemoteConnection remoteConnection =
              secondarySession.getDefaultRemoteConnection();
          remoteConnection.registerReceiver(
              new SessionConnectionReceiver() {
                @Override
                public void onMessageReceived(SessionParticipant participant, byte[] payload) {
                  Log.d(TAG, "Payload received: " + new String(payload, UTF_8));
                }
              });
        }

        @Override
        public void onFailure(Throwable t) {
          // Handle error.
        }
      },
      mainExecutor);
}

private static class HelloWorldSecondaryShareSessionStateCallback
    implements SecondarySessionStateCallback {
  @Override
  public void onSecondarySessionCleanup(SessionId sessionId) {
    // Custom cleanup logic here.
  }
}
```