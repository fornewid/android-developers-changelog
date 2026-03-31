---
title: GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient

Interface for managing connections and communications between devices using [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections.

## Summary

### Inheritance

Direct Known Subclasses:[GooglePlayGames.BasicApi.Nearby.DummyNearbyConnectionClient](/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client)

| Public functions | |
| --- | --- |
| `AcceptConnectionRequest(string remoteEndpointId, byte[] payload, IMessageListener listener)` | `void`  Accepts a connection request from a remote endpoint. |
| `DisconnectFromEndpoint(string remoteEndpointId)` | `void`  Disconnects from a remote endpoint. |
| `GetAppBundleId()` | `string`  Gets the app bundle ID. |
| `GetServiceId()` | `string`  Gets the service ID used for discovery and connection. |
| `MaxReliableMessagePayloadLength()` | `int`  Gets the maximum length of a reliable message payload. |
| `MaxUnreliableMessagePayloadLength()` | `int`  Gets the maximum length of an unreliable message payload. |
| `RejectConnectionRequest(string requestingEndpointId)` | `void`  Rejects a connection request from a remote endpoint. |
| `SendConnectionRequest(string name, string remoteEndpointId, byte[] payload, Action< ConnectionResponse > responseCallback, IMessageListener listener)` | `void`  Sends a connection request to a remote endpoint. |
| `SendReliable(List< string > recipientEndpointIds, byte[] payload)` | `void`  Sends a reliable message to a list of recipients. |
| `SendUnreliable(List< string > recipientEndpointIds, byte[] payload)` | `void`  Sends an unreliable message to a list of recipients. |
| `StartAdvertising(string name, List< string > appIdentifiers, TimeSpan? advertisingDuration, Action< AdvertisingResult > resultCallback, Action< ConnectionRequest > connectionRequestCallback)` | `void`  Starts advertising the local device to nearby devices. |
| `StartDiscovery(string serviceId, TimeSpan? advertisingTimeout, IDiscoveryListener listener)` | `void`  Starts discovering nearby endpoints for a specific service. |
| `StopAdvertising()` | `void`  Stops advertising the local device to nearby devices. |
| `StopAllConnections()` | `void`  Stops all connections to nearby endpoints. |
| `StopDiscovery(string serviceId)` | `void`  Stops discovering endpoints for a specific service. |

## Public functions

### AcceptConnectionRequest

```
void AcceptConnectionRequest(
  string remoteEndpointId,
  byte[] payload,
  IMessageListener listener
)
```

Accepts a connection request from a remote endpoint.

Details | || Parameters | |  |  | | --- | --- | | `remoteEndpointId` | The ID of the remote endpoint. | | `payload` | The connection acceptance payload. | | `listener` | Listener for message events. | |

### DisconnectFromEndpoint

```
void DisconnectFromEndpoint(
  string remoteEndpointId
)
```

Disconnects from a remote endpoint.

Details | || Parameters | |  |  | | --- | --- | | `remoteEndpointId` | The ID of the remote endpoint to disconnect from. | |

### GetAppBundleId

```
string GetAppBundleId()
```

Gets the app bundle ID.

Details | || **Returns** | The app bundle ID. |

### GetServiceId

```
string GetServiceId()
```

Gets the service ID used for discovery and connection.

Details | || **Returns** | The service ID. |

### MaxReliableMessagePayloadLength

```
int MaxReliableMessagePayloadLength()
```

Gets the maximum length of a reliable message payload.

Details | || **Returns** | Maximum length of a reliable message payload. |

### MaxUnreliableMessagePayloadLength

```
int MaxUnreliableMessagePayloadLength()
```

Gets the maximum length of an unreliable message payload.

Details | || **Returns** | Maximum length of an unreliable message payload. |

### RejectConnectionRequest

```
void RejectConnectionRequest(
  string requestingEndpointId
)
```

Rejects a connection request from a remote endpoint.

Details | || Parameters | |  |  | | --- | --- | | `requestingEndpointId` | The ID of the endpoint that sent the request. | |

### SendConnectionRequest

```
void SendConnectionRequest(
  string name,
  string remoteEndpointId,
  byte[] payload,
  Action< ConnectionResponse > responseCallback,
  IMessageListener listener
)
```

Sends a connection request to a remote endpoint.

Details | || Parameters | |  |  | | --- | --- | | `name` | The name of the local device. | | `remoteEndpointId` | The ID of the remote endpoint. | | `payload` | The connection request payload. | | `responseCallback` | Callback for the connection response. | | `listener` | Listener for message events. | |

### SendReliable

```
void SendReliable(
  List< string > recipientEndpointIds,
  byte[] payload
)
```

Sends a reliable message to a list of recipients.

Details | || Parameters | |  |  | | --- | --- | | `recipientEndpointIds` | List of recipient endpoint IDs. | | `payload` | The message payload to send. | |

### SendUnreliable

```
void SendUnreliable(
  List< string > recipientEndpointIds,
  byte[] payload
)
```

Sends an unreliable message to a list of recipients.

Details | || Parameters | |  |  | | --- | --- | | `recipientEndpointIds` | List of recipient endpoint IDs. | | `payload` | The message payload to send. | |

### StartAdvertising

```
void StartAdvertising(
  string name,
  List< string > appIdentifiers,
  TimeSpan? advertisingDuration,
  Action< AdvertisingResult > resultCallback,
  Action< ConnectionRequest > connectionRequestCallback
)
```

Starts advertising the local device to nearby devices.

Details | || Parameters | |  |  | | --- | --- | | `name` | The name to advertise. | | `appIdentifiers` | List of application identifiers. | | `advertisingDuration` | Optional advertising duration. | | `resultCallback` | Callback for advertising result. | | `connectionRequestCallback` | Callback for incoming connection requests. | |

### StartDiscovery

```
void StartDiscovery(
  string serviceId,
  TimeSpan? advertisingTimeout,
  IDiscoveryListener listener
)
```

Starts discovering nearby endpoints for a specific service.

Details | || Parameters | |  |  | | --- | --- | | `serviceId` | The service ID to discover. | | `advertisingTimeout` | Optional timeout for advertising discovery. | | `listener` | Listener for discovery events. | |

### StopAdvertising

```
void StopAdvertising()
```

Stops advertising the local device to nearby devices.

### StopAllConnections

```
void StopAllConnections()
```

Stops all connections to nearby endpoints.

### StopDiscovery

```
void StopDiscovery(
  string serviceId
)
```

Stops discovering endpoints for a specific service.

Details | || Parameters | |  |  | | --- | --- | | `serviceId` | The service ID to stop discovering. | |