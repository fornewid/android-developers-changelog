---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.EndpointDetails Struct Reference

# GooglePlayGames.BasicApi.Nearby.EndpointDetails

Represents details of an endpoint involved in a[Nearby](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby)Connections operation.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [EndpointDetails](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details_1a749a493a90927c3a05e7ab7cfa29526d)`(string endpointId, string name, string serviceId)` Initializes a new instance of the[EndpointDetails](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details)struct. ||

|                                                                                                                                              ### Properties                                                                                                                                              ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [EndpointId](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details_1a834002742ade2c368fb3785eb11e5528) | `string` Gets the unique identifier of the endpoint.       |
| [Name](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details_1afedfe8047f48755a2d9f99debc17b087)       | `string` Gets the name of the endpoint.                    |
| [ServiceId](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details_1a2a5c19dbce1673b58ee6d32677a6f1f7)  | `string` Gets the service ID associated with the endpoint. |

## Properties

### EndpointId

```c#
string GooglePlayGames::BasicApi::Nearby::EndpointDetails::EndpointId
```  
Gets the unique identifier of the endpoint.  

### Name

```c#
string GooglePlayGames::BasicApi::Nearby::EndpointDetails::Name
```  
Gets the name of the endpoint.  

### ServiceId

```c#
string GooglePlayGames::BasicApi::Nearby::EndpointDetails::ServiceId
```  
Gets the service ID associated with the endpoint.

## Public functions

### EndpointDetails

```c#
 GooglePlayGames::BasicApi::Nearby::EndpointDetails::EndpointDetails(
  string endpointId,
  string name,
  string serviceId
)
```  
Initializes a new instance of the[EndpointDetails](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details)struct.

<br />

|                                                                                                                                   Details                                                                                                                                   ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|----------------------------------------------| | `endpointId` | The unique identifier of the endpoint.       | | `name`       | The name of the endpoint.                    | | `serviceId`  | The service ID associated with the endpoint. | |