---
title: GooglePlayGames.BasicApi.Nearby.IMessageListener Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.IMessageListener

Interface for receiving messages and notifications about remote endpoints.

## Summary

| Public functions | |
| --- | --- |
| `OnMessageReceived(string remoteEndpointId, byte[] data, bool isReliableMessage)` | `void`  Called when a message is received from a remote endpoint. |
| `OnRemoteEndpointDisconnected(string remoteEndpointId)` | `void`  Called when a remote endpoint has disconnected. |

## Public functions

### OnMessageReceived

```
void OnMessageReceived(
  string remoteEndpointId,
  byte[] data,
  bool isReliableMessage
)
```

Called when a message is received from a remote endpoint.

Details | || Parameters | |  |  | | --- | --- | | `remoteEndpointId` | The ID of the remote endpoint. | | `data` | The data of the received message. | | `isReliableMessage` | Indicates whether the message is reliable. | |

### OnRemoteEndpointDisconnected

```
void OnRemoteEndpointDisconnected(
  string remoteEndpointId
)
```

Called when a remote endpoint has disconnected.

Details | || Parameters | |  |  | | --- | --- | | `remoteEndpointId` | The ID of the disconnected endpoint. | |