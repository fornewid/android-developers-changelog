---
title: GooglePlayGames.BasicApi.Nearby.ConnectionRequest Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi.Nearby.ConnectionRequest

Represents a request to establish a connection with a remote endpoint.

## Summary

Contains information about the remote endpoint and an optional payload.

| Constructors and Destructors | |
| --- | --- |
| `ConnectionRequest(string remoteEndpointId, string remoteEndpointName, string serviceId, byte[] payload)`   Initializes a new instance of the [ConnectionRequest](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request) struct. | |

| Properties | |
| --- | --- |
| `Payload` | `byte[]`  Gets the payload data included with the connection request. |
| `RemoteEndpoint` | `EndpointDetails`  Gets the details of the remote endpoint making the connection request. |

## Properties

### Payload

```
byte[] GooglePlayGames::BasicApi::Nearby::ConnectionRequest::Payload
```

Gets the payload data included with the connection request.

### RemoteEndpoint

```
EndpointDetails GooglePlayGames::BasicApi::Nearby::ConnectionRequest::RemoteEndpoint
```

Gets the details of the remote endpoint making the connection request.

## Public functions

### ConnectionRequest

```
 GooglePlayGames::BasicApi::Nearby::ConnectionRequest::ConnectionRequest(
  string remoteEndpointId,
  string remoteEndpointName,
  string serviceId,
  byte[] payload
)
```

Initializes a new instance of the [ConnectionRequest](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request) struct.

Details | || Parameters | |  |  | | --- | --- | | `remoteEndpointId` | The ID of the remote endpoint requesting the connection. | | `remoteEndpointName` | The name of the remote endpoint. | | `serviceId` | The service ID the connection is targeting. | | `payload` | The payload associated with the connection request. | |