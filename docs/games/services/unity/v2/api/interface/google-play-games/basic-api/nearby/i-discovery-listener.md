---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.IDiscoveryListener Interface Reference

# GooglePlayGames.BasicApi.Nearby.IDiscoveryListener

Interface for receiving notifications about discovered endpoints.

## Summary

|                                                                                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                                                                                        ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [OnEndpointFound](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_discovery_listener_1a82dbe486b3388e52517e255c9feded7c)`(`[EndpointDetails](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details)` discoveredEndpoint)` | `void` Called when an endpoint is found during discovery. |
| [OnEndpointLost](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_discovery_listener_1abc2d1177a0c39356406854e18154d1a3)`(string lostEndpointId)`                                                                                                                                                                                                                | `void` Called when an endpoint is lost during discovery.  |

## Public functions

### OnEndpointFound

```c#
void OnEndpointFound(
  EndpointDetails discoveredEndpoint
)
```  
Called when an endpoint is found during discovery.

<br />

|                                                                      Details                                                                      ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|-----------------------------------------| | `discoveredEndpoint` | The details of the discovered endpoint. | |

### OnEndpointLost

```c#
void OnEndpointLost(
  string lostEndpointId
)
```  
Called when an endpoint is lost during discovery.

<br />

|                                                       Details                                                       ||
|------------|---------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|------------------------------| | `lostEndpointId` | The ID of the lost endpoint. | |