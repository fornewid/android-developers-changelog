---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.DummyNearbyConnectionClient

Dummy implementation of[INearbyConnectionClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client).

## Summary

This class can be used for testing purposes. It logs messages indicating that its methods have been called.

### Inheritance

Inherits from:[GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [AcceptConnectionRequest](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a43c0b85f4c2c482d1e04200fc9537241)`(string remoteEndpointId, byte[] payload, `[IMessageListener](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_message_listener)` listener)`                                                                                                                                                                                                                                                                                                                                                   | `void` Logs the message about accepts a connection request from the specified endpoint. |
| [DisconnectFromEndpoint](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a64e392b03d0602e0c5b4202d9dc1ea3c)`(string remoteEndpointId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Logs the message about DisconnectFromEndpoint call from dummy implementation.    |
| [GetAppBundleId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a18cd24ff7b2b599534585383d60a0db2)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `string` Returns the app bundle id string.                                              |
| [GetServiceId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1aef974fc737f647783bce34f0d475cbd9)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string` Returns the service id string.                                                 |
| [LocalDeviceId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a059e5360d10fbdcff31f09a18f8b44d3)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `string` Returns the local device id string.                                            |
| [LocalEndpointId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a076c3bf43622487ea9a34d36d09cd7dd)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string` Returns the local endpoint id string.                                          |
| [MaxReliableMessagePayloadLength](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a4981a47253fb6906fffe67fa08e3378c)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `int` The maximum size of a reliable message payload.                                   |
| [MaxUnreliableMessagePayloadLength](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a62e34858e8dc0ccb289c514e507ca746)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `int` The maximum size of an unreliable message payload.                                |
| [RejectConnectionRequest](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a4ead60fd1db2f5b76beca3f600040a6c)`(string requestingEndpointId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Logs the message about RejectConnectionRequest call from dummy implementation.   |
| [SendConnectionRequest](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a0ddffcc2f307c9181cb526e4693ce8ea)`(string name, string remoteEndpointId, byte[] payload, System.Action< `[ConnectionResponse](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_response)` > responseCallback, `[IMessageListener](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_message_listener)` listener)`                                                                           | `void` Sends a connection request to the specified endpoint.                            |
| [SendReliable](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a5bb6090842403c5e637aaa80555074c3)`(System.Collections.Generic.List< string > recipientEndpointIds, byte[] payload)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void` Logs the message about Reliable call from dummy implementation.                  |
| [SendUnreliable](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a40ca8db404fd8343d6100f8f75e21681)`(System.Collections.Generic.List< string > recipientEndpointIds, byte[] payload)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `void` Logs the message about Unreliable call from dummy implementation.                |
| [StartAdvertising](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a7e073613c6cb06920e8346a2d9595713)`(string name, System.Collections.Generic.List< string > appIdentifiers, System.TimeSpan? advertisingDuration, System.Action< `[AdvertisingResult](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result)` > resultCallback, System.Action< `[ConnectionRequest](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_connection_request)` > connectionRequestCallback)` | `void` Starts advertising for a service.                                                |
| [StartDiscovery](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a0e7d34415b24c424c4d34849e8903dc6)`(string serviceId, System.TimeSpan? advertisingTimeout, `[IDiscoveryListener](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_discovery_listener)` listener)`                                                                                                                                                                                                                                                                                                                                        | `void` Logs the message about StartDiscovery call from dummy implementation.            |
| [StopAdvertising](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1ad19098bfab802dc241b2d3a662a77521)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Logs the message about StopAdvertising call from dummy implementation.           |
| [StopAllConnections](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1ae3e429da867959eb63efaf749a9daa6c)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Logs the message about StopAllConnections call from dummy implementation.        |
| [StopDiscovery](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client#class_google_play_games_1_1_basic_api_1_1_nearby_1_1_dummy_nearby_connection_client_1a116736313533e06e751828a285312480)`(string serviceId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Logs the message about StopDiscovery call from dummy implementation.             |

## Public functions

### AcceptConnectionRequest

```c#
void AcceptConnectionRequest(
  string remoteEndpointId,
  byte[] payload,
  IMessageListener listener
)
```  
Logs the message about accepts a connection request from the specified endpoint.  

### DisconnectFromEndpoint

```c#
void DisconnectFromEndpoint(
  string remoteEndpointId
)
```  
Logs the message about DisconnectFromEndpoint call from dummy implementation.  

### GetAppBundleId

```c#
string GetAppBundleId()
```  
Returns the app bundle id string.  

### GetServiceId

```c#
string GetServiceId()
```  
Returns the service id string.  

### LocalDeviceId

```c#
string LocalDeviceId()
```  
Returns the local device id string.  

### LocalEndpointId

```c#
string LocalEndpointId()
```  
Returns the local endpoint id string.  

### MaxReliableMessagePayloadLength

```c#
int MaxReliableMessagePayloadLength()
```  
The maximum size of a reliable message payload.  

### MaxUnreliableMessagePayloadLength

```c#
int MaxUnreliableMessagePayloadLength()
```  
The maximum size of an unreliable message payload.  

### RejectConnectionRequest

```c#
void RejectConnectionRequest(
  string requestingEndpointId
)
```  
Logs the message about RejectConnectionRequest call from dummy implementation.  

### SendConnectionRequest

```c#
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

```c#
void SendReliable(
  System.Collections.Generic.List< string > recipientEndpointIds,
  byte[] payload
)
```  
Logs the message about Reliable call from dummy implementation.  

### SendUnreliable

```c#
void SendUnreliable(
  System.Collections.Generic.List< string > recipientEndpointIds,
  byte[] payload
)
```  
Logs the message about Unreliable call from dummy implementation.  

### StartAdvertising

```c#
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

```c#
void StartDiscovery(
  string serviceId,
  System.TimeSpan? advertisingTimeout,
  IDiscoveryListener listener
)
```  
Logs the message about StartDiscovery call from dummy implementation.  

### StopAdvertising

```c#
void StopAdvertising()
```  
Logs the message about StopAdvertising call from dummy implementation.  

### StopAllConnections

```c#
void StopAllConnections()
```  
Logs the message about StopAllConnections call from dummy implementation.  

### StopDiscovery

```c#
void StopDiscovery(
  string serviceId
)
```  
Logs the message about StopDiscovery call from dummy implementation.