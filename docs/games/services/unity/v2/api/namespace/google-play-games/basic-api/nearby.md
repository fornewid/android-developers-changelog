---
title: GooglePlayGames.BasicApi.Nearby Namespace  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby

## Summary

| Enumerations | |
| --- | --- |
| `InitializationStatus{   Success,   VersionUpdateRequired,   InternalError }` | enum Represents the configuration for a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections operation. |

| Classes | |
| --- | --- |
| [GooglePlayGames.BasicApi.Nearby.DummyNearbyConnectionClient](/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client) | Dummy implementation of [INearbyConnectionClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client). |

| Structs | |
| --- | --- |
| [GooglePlayGames.BasicApi.Nearby.AdvertisingResult](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result) | Represents the result of an attempt to start advertising for nearby connections. |
| [GooglePlayGames.BasicApi.Nearby.ConnectionRequest](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request) | Represents a request to establish a connection with a remote endpoint. |
| [GooglePlayGames.BasicApi.Nearby.ConnectionResponse](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response) | Represents a response to a connection request, including status, payload, and identifying information. |
| [GooglePlayGames.BasicApi.Nearby.EndpointDetails](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details) | Represents details of an endpoint involved in a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections operation. |
| [GooglePlayGames.BasicApi.Nearby.NearbyConnectionConfiguration](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration) | Defines the configuration for establishing a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) connection. |

| Interfaces | |
| --- | --- |
| [GooglePlayGames.BasicApi.Nearby.IDiscoveryListener](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener) | Interface for receiving notifications about discovered endpoints. |
| [GooglePlayGames.BasicApi.Nearby.IMessageListener](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener) | Interface for receiving messages and notifications about remote endpoints. |
| [GooglePlayGames.BasicApi.Nearby.INearbyConnectionClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client) | Interface for managing connections and communications between devices using [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections. |

## Enumerations

### InitializationStatus

```
 InitializationStatus
```

Represents the configuration for a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections operation.

Includes initialization status and client-specific configuration.

| Properties | |
| --- | --- |
| `InternalError` | Denotes that an internal error occurred during initialization. |
| `Success` | Indicates that the initialization was successful. |
| `VersionUpdateRequired` | Signifies that a version update is required for nearby connections. |