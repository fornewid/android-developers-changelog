---
title: GooglePlayGames.BasicApi.Nearby.EndpointDetails Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi.Nearby.EndpointDetails

Represents details of an endpoint involved in a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections operation.

## Summary

| Constructors and Destructors | |
| --- | --- |
| `EndpointDetails(string endpointId, string name, string serviceId)`   Initializes a new instance of the [EndpointDetails](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details) struct. | |

| Properties | |
| --- | --- |
| `EndpointId` | `string`  Gets the unique identifier of the endpoint. |
| `Name` | `string`  Gets the name of the endpoint. |
| `ServiceId` | `string`  Gets the service ID associated with the endpoint. |

## Properties

### EndpointId

```
string GooglePlayGames::BasicApi::Nearby::EndpointDetails::EndpointId
```

Gets the unique identifier of the endpoint.

### Name

```
string GooglePlayGames::BasicApi::Nearby::EndpointDetails::Name
```

Gets the name of the endpoint.

### ServiceId

```
string GooglePlayGames::BasicApi::Nearby::EndpointDetails::ServiceId
```

Gets the service ID associated with the endpoint.

## Public functions

### EndpointDetails

```
 GooglePlayGames::BasicApi::Nearby::EndpointDetails::EndpointDetails(
  string endpointId,
  string name,
  string serviceId
)
```

Initializes a new instance of the [EndpointDetails](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_endpoint_details) struct.

Details | || Parameters | |  |  | | --- | --- | | `endpointId` | The unique identifier of the endpoint. | | `name` | The name of the endpoint. | | `serviceId` | The service ID associated with the endpoint. | |