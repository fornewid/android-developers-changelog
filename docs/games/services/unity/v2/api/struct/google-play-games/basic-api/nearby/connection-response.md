---
title: GooglePlayGames.BasicApi.Nearby.ConnectionResponse Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.ConnectionResponse

Represents a response to a connection request, including status, payload, and identifying information.

## Summary

| Public types | |
| --- | --- |
| `Status{   Accepted,   Rejected,   ErrorInternal,   ErrorNetworkNotConnected,   ErrorEndpointNotConnected,   ErrorAlreadyConnected }` | enum Status codes representing the outcome of a connection request. |

| Properties | |
| --- | --- |
| `LocalClientId` | `long`  Gets the ID of the local client. |
| `Payload` | `byte[]`  Gets the payload sent with the connection response. |
| `RemoteEndpointId` | `string`  Gets the ID of the remote endpoint responding to the connection request. |
| `ResponseStatus` | `Status`  Gets the status of the connection response. |

| Public static functions | |
| --- | --- |
| `Accepted(long localClientId, string remoteEndpointId, byte[] payload)` | `ConnectionResponse`  Creates a response indicating the connection was accepted with a payload. |
| `AlreadyConnected(long localClientId, string remoteEndpointId)` | `ConnectionResponse`  Creates a response indicating the endpoints are already connected. |
| `EndpointNotConnected(long localClientId, string remoteEndpointId)` | `ConnectionResponse`  Creates a response indicating the remote endpoint is not connected. |
| `InternalError(long localClientId, string remoteEndpointId)` | `ConnectionResponse`  Creates a response indicating an internal error occurred. |
| `NetworkNotConnected(long localClientId, string remoteEndpointId)` | `ConnectionResponse`  Creates a response indicating the device is not connected to a network. |
| `Rejected(long localClientId, string remoteEndpointId)` | `ConnectionResponse`  Creates a response indicating the connection was rejected. |

## Public types

### Status

```
 GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Status
```

Status codes representing the outcome of a connection request.

| Properties | |
| --- | --- |
| `Accepted` | Indicates that the connection was accepted. |
| `ErrorAlreadyConnected` | Indicates that the endpoints are already connected. |
| `ErrorEndpointNotConnected` | Indicates that the remote endpoint is not connected. |
| `ErrorInternal` | Indicates that an internal error occurred. |
| `ErrorNetworkNotConnected` | Indicates that the device is not connected to a network. |
| `Rejected` | Indicates that the connection was rejected. |

## Properties

### LocalClientId

```
long GooglePlayGames::BasicApi::Nearby::ConnectionResponse::LocalClientId
```

Gets the ID of the local client.

### Payload

```
byte[] GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Payload
```

Gets the payload sent with the connection response.

### RemoteEndpointId

```
string GooglePlayGames::BasicApi::Nearby::ConnectionResponse::RemoteEndpointId
```

Gets the ID of the remote endpoint responding to the connection request.

### ResponseStatus

```
Status GooglePlayGames::BasicApi::Nearby::ConnectionResponse::ResponseStatus
```

Gets the status of the connection response.

## Public static functions

### Accepted

```
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Accepted(
  long localClientId,
  string remoteEndpointId,
  byte[] payload
)
```

Creates a response indicating the connection was accepted with a payload.

### AlreadyConnected

```
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::AlreadyConnected(
  long localClientId,
  string remoteEndpointId
)
```

Creates a response indicating the endpoints are already connected.

### EndpointNotConnected

```
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::EndpointNotConnected(
  long localClientId,
  string remoteEndpointId
)
```

Creates a response indicating the remote endpoint is not connected.

### InternalError

```
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::InternalError(
  long localClientId,
  string remoteEndpointId
)
```

Creates a response indicating an internal error occurred.

### NetworkNotConnected

```
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::NetworkNotConnected(
  long localClientId,
  string remoteEndpointId
)
```

Creates a response indicating the device is not connected to a network.

### Rejected

```
ConnectionResponse GooglePlayGames::BasicApi::Nearby::ConnectionResponse::Rejected(
  long localClientId,
  string remoteEndpointId
)
```

Creates a response indicating the connection was rejected.