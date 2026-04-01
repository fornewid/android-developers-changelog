---
title: GooglePlayGames.BasicApi.Nearby.DummyNearbyConnectionClient Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.DummyNearbyConnectionClient

Dummy implementation of [INearbyConnectionClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client).

## Summary

This class can be used for testing purposes. It logs messages indicating that its methods have been called.

### Inheritance

Inherits from: [GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client)

| Public functions | |
| --- | --- |
| `AcceptConnectionRequest(string remoteEndpointId, byte[] payload, IMessageListener listener)` | `void`  Logs the message about accepts a connection request from the specified endpoint. |
| `DisconnectFromEndpoint(string remoteEndpointId)` | `void`  Logs the message about DisconnectFromEndpoint call from dummy implementation. |
| `GetAppBundleId()` | `string`  Returns the app bundle id string. |
| `GetServiceId()` | `string`  Returns the service id string. |
| `LocalDeviceId()` | `string`  Returns the local device id string. |
| `LocalEndpointId()` | `string`  Returns the local endpoint id string. |
| `MaxReliableMessagePayloadLength()` | `int`  The maximum size of a reliable message payload. |
| `MaxUnreliableMessagePayloadLength()` | `int`  The maximum size of an unreliable message payload. |
| `RejectConnectionRequest(string requestingEndpointId)` | `void`  Logs the message about RejectConnectionRequest call from dummy implementation. |
| `SendConnectionRequest(string name, string remoteEndpointId, byte[] payload, System.Action< ConnectionResponse > responseCallback, IMessageListener listener)` | `void`  Sends a connection request to the specified endpoint. |
| `SendReliable(System.Collections.Generic.List< string > recipientEndpointIds, byte[] payload)` | `void`  Logs the message about Reliable call from dummy implementation. |
| `SendUnreliable(System.Collections.Generic.List< string > recipientEndpointIds, byte[] payload)` | `void`  Logs the message about Unreliable call from dummy implementation. |
| `StartAdvertising(string name, System.Collections.Generic.List< string > appIdentifiers, System.TimeSpan? advertisingDuration, System.Action< AdvertisingResult > resultCallback, System.Action< ConnectionRequest > connectionRequestCallback)` | `void`  Starts advertising for a service. |
| `StartDiscovery(string serviceId, System.TimeSpan? advertisingTimeout, IDiscoveryListener listener)` | `void`  Logs the message about StartDiscovery call from dummy implementation. |
| `StopAdvertising()` | `void`  Logs the message about StopAdvertising call from dummy implementation. |
| `StopAllConnections()` | `void`  Logs the message about StopAllConnections call from dummy implementation. |
| `StopDiscovery(string serviceId)` | `void`  Logs the message about StopDiscovery call from dummy implementation. |

## Public functions

### AcceptConnectionRequest

```
void AcceptConnectionRequest(
  string remoteEndpointId,
  byte[] payload,
  IMessageListener listener
)
```

Logs the message about accepts a connection request from the specified endpoint.

### DisconnectFromEndpoint

```
void DisconnectFromEndpoint(
  string remoteEndpointId
)
```

Logs the message about DisconnectFromEndpoint call from dummy implementation.

### GetAppBundleId

```
string GetAppBundleId()
```

Returns the app bundle id string.

### GetServiceId

```
string GetServiceId()
```

Returns the service id string.

### LocalDeviceId

```
string LocalDeviceId()
```

Returns the local device id string.

### LocalEndpointId

```
string LocalEndpointId()
```

Returns the local endpoint id string.

### MaxReliableMessagePayloadLength

```
int MaxReliableMessagePayloadLength()
```

The maximum size of a reliable message payload.

### MaxUnreliableMessagePayloadLength

```
int MaxUnreliableMessagePayloadLength()
```

The maximum size of an unreliable message payload.

### RejectConnectionRequest

```
void RejectConnectionRequest(
  string requestingEndpointId
)
```

Logs the message about RejectConnectionRequest call from dummy implementation.

### SendConnectionRequest

```
void SendConnectionRequest(
  string name,
  string remoteEndpointId,
  byte[] payload,
  System.Action< ConnectionResponse > responseCallback,
  IMessageListener listener
)
```

Sends a connection request to the specified endpoint.

### SendReliable

```
void SendReliable(
  System.Collections.Generic.List< string > recipientEndpointIds,
  byte[] payload
)
```

Logs the message about Reliable call from dummy implementation.

### SendUnreliable

```
void SendUnreliable(
  System.Collections.Generic.List< string > recipientEndpointIds,
  byte[] payload
)
```

Logs the message about Unreliable call from dummy implementation.

### StartAdvertising

```
void StartAdvertising(
  string name,
  System.Collections.Generic.List< string > appIdentifiers,
  System.TimeSpan? advertisingDuration,
  System.Action< AdvertisingResult > resultCallback,
  System.Action< ConnectionRequest > connectionRequestCallback
)
```

Starts advertising for a service.

### StartDiscovery

```
void StartDiscovery(
  string serviceId,
  System.TimeSpan? advertisingTimeout,
  IDiscoveryListener listener
)
```

Logs the message about StartDiscovery call from dummy implementation.

### StopAdvertising

```
void StopAdvertising()
```

Logs the message about StopAdvertising call from dummy implementation.

### StopAllConnections

```
void StopAllConnections()
```

Logs the message about StopAllConnections call from dummy implementation.

### StopDiscovery

```
void StopDiscovery(
  string serviceId
)
```

Logs the message about StopDiscovery call from dummy implementation.