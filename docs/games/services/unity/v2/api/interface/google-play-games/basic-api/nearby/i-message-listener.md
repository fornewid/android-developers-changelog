---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.IMessageListener Interface Reference

# GooglePlayGames.BasicApi.Nearby.IMessageListener

Interface for receiving messages and notifications about remote endpoints.

## Summary

|                                                                                                                                                                                      ### Public functions                                                                                                                                                                                       ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [OnMessageReceived](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_message_listener_1af0c7c02a3d5569793897da38809ced5c)`(string remoteEndpointId, byte[] data, bool isReliableMessage)` | `void` Called when a message is received from a remote endpoint. |
| [OnRemoteEndpointDisconnected](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_message_listener_1aa320c7dffb2328ac1a56175107d1a57c)`(string remoteEndpointId)`                           | `void` Called when a remote endpoint has disconnected.           |

## Public functions

### OnMessageReceived

```c#
void OnMessageReceived(
  string remoteEndpointId,
  byte[] data,
  bool isReliableMessage
)
```  
Called when a message is received from a remote endpoint.

<br />

|                                                                                                                                             Details                                                                                                                                             ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|--------------------------------------------| | `remoteEndpointId`  | The ID of the remote endpoint.             | | `data`              | The data of the received message.          | | `isReliableMessage` | Indicates whether the message is reliable. | |

### OnRemoteEndpointDisconnected

```c#
void OnRemoteEndpointDisconnected(
  string remoteEndpointId
)
```  
Called when a remote endpoint has disconnected.

<br />

|                                                                 Details                                                                 ||
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|--------------------------------------| | `remoteEndpointId` | The ID of the disconnected endpoint. | |