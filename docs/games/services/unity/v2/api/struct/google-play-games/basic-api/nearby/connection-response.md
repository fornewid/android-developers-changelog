---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.ConnectionResponse Struct Reference

# GooglePlayGames.BasicApi.Nearby.ConnectionResponse

Represents a response to a connection request, including status, payload, and identifying information.

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ### Public types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [Status](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257)`{` ` `[Accepted](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257a382ab522931673c11e398ead1b7b1678)`,` ` `[Rejected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257ad37b1f6c0512e2118cee17fea015b699)`,` ` `[ErrorInternal](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257aa4b8fe38709fba050b2ba197c8805053)`,` ` `[ErrorNetworkNotConnected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257a8b452ed0b72645c7b346ee24165159bb)`,` ` `[ErrorEndpointNotConnected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257aa114b07a3c87d4b0a54d32912e30f84f)`,` ` `[ErrorAlreadyConnected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257ae26cd5b2e9bddc17f3387b438b4c5a3a) `}` | enum Status codes representing the outcome of a connection request. |

|                                                                                                                                                                                                                                                                    ### Properties                                                                                                                                                                                                                                                                    ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LocalClientId](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a73b7c3c474bb04c3f05b67ec0b938d26)    | `long` Gets the ID of the local client.                                                                                                                                                                                                                                                    |
| [Payload](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a0eca0884442ea2db7d30a7effcbbb982)          | `byte[]` Gets the payload sent with the connection response.                                                                                                                                                                                                                               |
| [RemoteEndpointId](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a85f2078d1c67a12529393868d0777373) | `string` Gets the ID of the remote endpoint responding to the connection request.                                                                                                                                                                                                          |
| [ResponseStatus](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a8cc2ea758e4223014ba185e9d14340c2)   | [Status](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a5beaeea278ccd1cc05f781e255daa257) Gets the status of the connection response. |

|                                                                                                                                                                                                                                                                                            ### Public static functions                                                                                                                                                                                                                                                                                             ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Accepted](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1aac84afb9775c06370ad34890512cb3e4)`(long localClientId, string remoteEndpointId, byte[] payload)` | [ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response) Creates a response indicating the connection was accepted with a payload. |
| [AlreadyConnected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1ad1c7d264e7928796253b22d3b28c1283)`(long localClientId, string remoteEndpointId)`         | [ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response) Creates a response indicating the endpoints are already connected.        |
| [EndpointNotConnected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1acc2060260750c6c100045c39aa4a430d)`(long localClientId, string remoteEndpointId)`     | [ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response) Creates a response indicating the remote endpoint is not connected.       |
| [InternalError](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1ac8e4d5623deee6d236472ac93bef8492)`(long localClientId, string remoteEndpointId)`            | [ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response) Creates a response indicating an internal error occurred.                 |
| [NetworkNotConnected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1a44c1b20dbdbae7ec7aea6e4912b09fe7)`(long localClientId, string remoteEndpointId)`      | [ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response) Creates a response indicating the device is not connected to a network.   |
| [Rejected](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response_1ac3fc83ebe1f149efceff7e999fcdf768)`(long localClientId, string remoteEndpointId)`                 | [ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response) Creates a response indicating the connection was rejected.                |

## Public types

### Status

```c#
 GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Status
```  
Status codes representing the outcome of a connection request.

|                                      Properties                                       ||
|-----------------------------|----------------------------------------------------------|
| `Accepted`                  | Indicates that the connection was accepted.              |
| `ErrorAlreadyConnected`     | Indicates that the endpoints are already connected.      |
| `ErrorEndpointNotConnected` | Indicates that the remote endpoint is not connected.     |
| `ErrorInternal`             | Indicates that an internal error occurred.               |
| `ErrorNetworkNotConnected`  | Indicates that the device is not connected to a network. |
| `Rejected`                  | Indicates that the connection was rejected.              |

## Properties

### LocalClientId

```c#
long GooglePlayGames::BasicApi::Nearby::ConnectionResponse::LocalClientId
```  
Gets the ID of the local client.  

### Payload

```c#
byte[] GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Payload
```  
Gets the payload sent with the connection response.  

### RemoteEndpointId

```c#
string GooglePlayGames::BasicApi::Nearby::ConnectionResponse::RemoteEndpointId
```  
Gets the ID of the remote endpoint responding to the connection request.  

### ResponseStatus

```c#
Status GooglePlayGames::BasicApi::Nearby::ConnectionResponse::ResponseStatus
```  
Gets the status of the connection response.

## Public static functions

### Accepted

```c#
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Accepted(
  long localClientId,
  string remoteEndpointId,
  byte[] payload
)
```  
Creates a response indicating the connection was accepted with a payload.  

### AlreadyConnected

```c#
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::AlreadyConnected(
  long localClientId,
  string remoteEndpointId
)
```  
Creates a response indicating the endpoints are already connected.  

### EndpointNotConnected

```c#
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::EndpointNotConnected(
  long localClientId,
  string remoteEndpointId
)
```  
Creates a response indicating the remote endpoint is not connected.  

### InternalError

```c#
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::InternalError(
  long localClientId,
  string remoteEndpointId
)
```  
Creates a response indicating an internal error occurred.  

### NetworkNotConnected

```c#
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::NetworkNotConnected(
  long localClientId,
  string remoteEndpointId
)
```  
Creates a response indicating the device is not connected to a network.  

### Rejected

```c#
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Rejected(
  long localClientId,
  string remoteEndpointId
)
```  
Creates a response indicating the connection was rejected.