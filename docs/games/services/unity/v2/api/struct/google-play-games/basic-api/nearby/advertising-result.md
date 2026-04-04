---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.AdvertisingResult Struct Reference

# GooglePlayGames.BasicApi.Nearby.AdvertisingResult

Represents the result of an attempt to start advertising for nearby connections.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [AdvertisingResult](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result_1a7a7b962142e1c090e12db45d232dfd11)`(`[ResponseStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1afc173c0f78ea77552386c8f699526dea)` status, string localEndpointName)` Constructs a new[AdvertisingResult](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result). ||

|                                                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                                                 ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LocalEndpointName](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result_1af41c66883f19dbfca3be2d309da0309a) | `string` Gets the name of the local endpoint used in the advertising operation.                                                                                                                                                                       |
| [Status](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result_1a28212ae180d3033c1ff444b608f26746)            | [ResponseStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1afc173c0f78ea77552386c8f699526dea) Gets the response status of the advertising operation. |
| [Succeeded](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result_1a3b1c3a80228f13adefa30720c30a810b)         | `bool` Gets a value indicating whether the advertising operation was successful.                                                                                                                                                                      |

## Properties

### LocalEndpointName

```c#
string GooglePlayGames::BasicApi::Nearby::AdvertisingResult::LocalEndpointName
```  
Gets the name of the local endpoint used in the advertising operation.  

### Status

```c#
ResponseStatus GooglePlayGames::BasicApi::Nearby::AdvertisingResult::Status
```  
Gets the response status of the advertising operation.  

### Succeeded

```c#
bool GooglePlayGames::BasicApi::Nearby::AdvertisingResult::Succeeded
```  
Gets a value indicating whether the advertising operation was successful.

## Public functions

### AdvertisingResult

```c#
 GooglePlayGames::BasicApi::Nearby::AdvertisingResult::AdvertisingResult(
  ResponseStatus status,
  string localEndpointName
)
```  
Constructs a new[AdvertisingResult](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result).

<br />

|                                                                                                    Details                                                                                                     ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|----------------------------------------| | `status`            | The result of the advertising attempt. | | `localEndpointName` | The name of the local endpoint.        | |
| Exceptions | |--------------------------------|-------------------------------| | `System.ArgumentNullException` | If localEndpointName is null. |                                                              |