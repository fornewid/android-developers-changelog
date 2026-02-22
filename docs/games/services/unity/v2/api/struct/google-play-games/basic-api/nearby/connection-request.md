---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.ConnectionRequest Struct Reference

# GooglePlayGames.BasicApi.Nearby.ConnectionRequest

Represents a request to establish a connection with a remote endpoint.

## Summary

Contains information about the remote endpoint and an optional payload.

| ### Constructors and Destructors ||
|---|---|
| [ConnectionRequest](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request_1a28b194c478e66e02b6352c3594a43754)`(string remoteEndpointId, string remoteEndpointName, string serviceId, byte[] payload)` Initializes a new instance of the[ConnectionRequest](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request)struct. ||

|                                                                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                                                                ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Payload](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request_1a382433e113d7f29d3133e8cb435d906e)        | `byte[]` Gets the payload data included with the connection request.                                                                                                                                                                                                                  |
| [RemoteEndpoint](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request_1a734e1be5db342df878c6bd153cf4ca12) | [EndpointDetails](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details) Gets the details of the remote endpoint making the connection request. |

## Properties

### Payload

```c#
byte[] GooglePlayGames::BasicApi::Nearby::ConnectionRequest::Payload
```  
Gets the payload data included with the connection request.  

### RemoteEndpoint

```c#
EndpointDetails GooglePlayGames::BasicApi::Nearby::ConnectionRequest::RemoteEndpoint
```  
Gets the details of the remote endpoint making the connection request.

## Public functions

### ConnectionRequest

```c#
 GooglePlayGames::BasicApi::Nearby::ConnectionRequest::ConnectionRequest(
  string remoteEndpointId,
  string remoteEndpointName,
  string serviceId,
  byte[] payload
)
```  
Initializes a new instance of the[ConnectionRequest](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request)struct.

<br />

|                                                                                                                                                                                                                     Details                                                                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|----------------------------------------------------------| | `remoteEndpointId`   | The ID of the remote endpoint requesting the connection. | | `remoteEndpointName` | The name of the remote endpoint.                         | | `serviceId`          | The service ID the connection is targeting.              | | `payload`            | The payload associated with the connection request.      | |