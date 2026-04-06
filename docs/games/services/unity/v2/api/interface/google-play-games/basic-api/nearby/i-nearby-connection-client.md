---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient Interface Reference

# GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient

Interface for managing connections and communications between devices using[Nearby](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby)Connections.

## Summary

### Inheritance

Direct Known Subclasses:[GooglePlayGames.BasicApi.Nearby.DummyNearbyConnectionClient](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                            ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [AcceptConnectionRequest](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1ae8c08a0da53cbacf1816f4b3ad9d6a36)`(string remoteEndpointId, byte[] payload, `[IMessageListener](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_message_listener)` listener)`                                                                                                                                                                                                                                                                                                   | `void` Accepts a connection request from a remote endpoint.        |
| [DisconnectFromEndpoint](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a86474bce8b63e58b3a99eda1908e1e66)`(string remoteEndpointId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Disconnects from a remote endpoint.                         |
| [GetAppBundleId](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a6d636eb8cd75811bf7afd4f940afbf1d)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `string` Gets the app bundle ID.                                   |
| [GetServiceId](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a5dc7786fcae6e11ff6fc6fecf570c6e2)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string` Gets the service ID used for discovery and connection.    |
| [MaxReliableMessagePayloadLength](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a058a48fc02484a5836cb836aab4d696d)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `int` Gets the maximum length of a reliable message payload.       |
| [MaxUnreliableMessagePayloadLength](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1ac0afaaa4f6df8591613552ff368b0ae3)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `int` Gets the maximum length of an unreliable message payload.    |
| [RejectConnectionRequest](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1aa4132f589df5dacc5de81fa1a85a7017)`(string requestingEndpointId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Rejects a connection request from a remote endpoint.        |
| [SendConnectionRequest](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a497f5a53cac510c894659e27f2402df7)`(string name, string remoteEndpointId, byte[] payload, Action< `[ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response)` > responseCallback, `[IMessageListener](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_message_listener)` listener)`                                  | `void` Sends a connection request to a remote endpoint.            |
| [SendReliable](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1af3550466b493d7c5853309119a8947ef)`(List< string > recipientEndpointIds, byte[] payload)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Sends a reliable message to a list of recipients.           |
| [SendUnreliable](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1ae0cec66a0cf359fff5c06054ed5fe6ff)`(List< string > recipientEndpointIds, byte[] payload)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `void` Sends an unreliable message to a list of recipients.        |
| [StartAdvertising](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a9aa8d47924019960a34c32bad0792eb2)`(string name, List< string > appIdentifiers, TimeSpan? advertisingDuration, Action< `[AdvertisingResult](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result)` > resultCallback, Action< `[ConnectionRequest](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request)` > connectionRequestCallback)` | `void` Starts advertising the local device to nearby devices.      |
| [StartDiscovery](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a7017760f4f7ac4c9d14b96ec7b5a4faa)`(string serviceId, TimeSpan? advertisingTimeout, `[IDiscoveryListener](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_discovery_listener)` listener)`                                                                                                                                                                                                                                                                                               | `void` Starts discovering nearby endpoints for a specific service. |
| [StopAdvertising](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1aa7efbdb100c4b1aaaec19054d2020981)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Stops advertising the local device to nearby devices.       |
| [StopAllConnections](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a84f078280126c83b7ee4f8e49fa8049b)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Stops all connections to nearby endpoints.                  |
| [StopDiscovery](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client_1a8f766be1d34afbc654241271b88300ca)`(string serviceId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Stops discovering endpoints for a specific service.         |

## Public functions

### AcceptConnectionRequest

```c#
void AcceptConnectionRequest(
  string remoteEndpointId,
  byte[] payload,
  IMessageListener listener
)
```  
Accepts a connection request from a remote endpoint.

<br />

|                                                                                                                           Details                                                                                                                           ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|------------------------------------| | `remoteEndpointId` | The ID of the remote endpoint.     | | `payload`          | The connection acceptance payload. | | `listener`         | Listener for message events.       | |

### DisconnectFromEndpoint

```c#
void DisconnectFromEndpoint(
  string remoteEndpointId
)
```  
Disconnects from a remote endpoint.

<br />

|                                                                              Details                                                                              ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|---------------------------------------------------| | `remoteEndpointId` | The ID of the remote endpoint to disconnect from. | |

### GetAppBundleId

```c#
string GetAppBundleId()
```  
Gets the app bundle ID.

<br />

|             Details             ||
|-------------|--------------------|
| **Returns** | The app bundle ID. |

### GetServiceId

```c#
string GetServiceId()
```  
Gets the service ID used for discovery and connection.

<br />

|           Details            ||
|-------------|-----------------|
| **Returns** | The service ID. |

### MaxReliableMessagePayloadLength

```c#
int MaxReliableMessagePayloadLength()
```  
Gets the maximum length of a reliable message payload.

<br />

|                          Details                           ||
|-------------|-----------------------------------------------|
| **Returns** | Maximum length of a reliable message payload. |

### MaxUnreliableMessagePayloadLength

```c#
int MaxUnreliableMessagePayloadLength()
```  
Gets the maximum length of an unreliable message payload.

<br />

|                            Details                            ||
|-------------|--------------------------------------------------|
| **Returns** | Maximum length of an unreliable message payload. |

### RejectConnectionRequest

```c#
void RejectConnectionRequest(
  string requestingEndpointId
)
```  
Rejects a connection request from a remote endpoint.

<br />

|                                                                              Details                                                                              ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|-----------------------------------------------| | `requestingEndpointId` | The ID of the endpoint that sent the request. | |

### SendConnectionRequest

```c#
void SendConnectionRequest(
  string name,
  string remoteEndpointId,
  byte[] payload,
  Action< ConnectionResponse > responseCallback,
  IMessageListener listener
)
```  
Sends a connection request to a remote endpoint.

<br />

|                                                                                                                                                                                                Details                                                                                                                                                                                                ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------------|---------------------------------------| | `name`             | The name of the local device.         | | `remoteEndpointId` | The ID of the remote endpoint.        | | `payload`          | The connection request payload.       | | `responseCallback` | Callback for the connection response. | | `listener`         | Listener for message events.          | |

### SendReliable

```c#
void SendReliable(
  List< string > recipientEndpointIds,
  byte[] payload
)
```  
Sends a reliable message to a list of recipients.

<br />

|                                                                                              Details                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|---------------------------------| | `recipientEndpointIds` | List of recipient endpoint IDs. | | `payload`              | The message payload to send.    | |

### SendUnreliable

```c#
void SendUnreliable(
  List< string > recipientEndpointIds,
  byte[] payload
)
```  
Sends an unreliable message to a list of recipients.

<br />

|                                                                                              Details                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------------|---------------------------------| | `recipientEndpointIds` | List of recipient endpoint IDs. | | `payload`              | The message payload to send.    | |

### StartAdvertising

```c#
void StartAdvertising(
  string name,
  List< string > appIdentifiers,
  TimeSpan? advertisingDuration,
  Action< AdvertisingResult > resultCallback,
  Action< ConnectionRequest > connectionRequestCallback
)
```  
Starts advertising the local device to nearby devices.

<br />

|                                                                                                                                                                                                                                          Details                                                                                                                                                                                                                                          ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------------------|--------------------------------------------| | `name`                      | The name to advertise.                     | | `appIdentifiers`            | List of application identifiers.           | | `advertisingDuration`       | Optional advertising duration.             | | `resultCallback`            | Callback for advertising result.           | | `connectionRequestCallback` | Callback for incoming connection requests. | |

### StartDiscovery

```c#
void StartDiscovery(
  string serviceId,
  TimeSpan? advertisingTimeout,
  IDiscoveryListener listener
)
```  
Starts discovering nearby endpoints for a specific service.

<br />

|                                                                                                                                                 Details                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|---------------------------------------------| | `serviceId`          | The service ID to discover.                 | | `advertisingTimeout` | Optional timeout for advertising discovery. | | `listener`           | Listener for discovery events.              | |

### StopAdvertising

```c#
void StopAdvertising()
```  
Stops advertising the local device to nearby devices.  

### StopAllConnections

```c#
void StopAllConnections()
```  
Stops all connections to nearby endpoints.  

### StopDiscovery

```c#
void StopDiscovery(
  string serviceId
)
```  
Stops discovering endpoints for a specific service.

<br />

|                                                         Details                                                         ||
|------------|-------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|-------------------------------------| | `serviceId` | The service ID to stop discovering. | |