---
title: GooglePlayGames.BasicApi.Nearby.AdvertisingResult Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.AdvertisingResult

Represents the result of an attempt to start advertising for nearby connections.

## Summary

| Constructors and Destructors | |
| --- | --- |
| `AdvertisingResult(ResponseStatus status, string localEndpointName)`   Constructs a new [AdvertisingResult](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result). | |

| Properties | |
| --- | --- |
| `LocalEndpointName` | `string`  Gets the name of the local endpoint used in the advertising operation. |
| `Status` | `ResponseStatus`  Gets the response status of the advertising operation. |
| `Succeeded` | `bool`  Gets a value indicating whether the advertising operation was successful. |

## Properties

### LocalEndpointName

```
string GooglePlayGames::BasicApi::Nearby::AdvertisingResult::LocalEndpointName
```

Gets the name of the local endpoint used in the advertising operation.

### Status

```
ResponseStatus GooglePlayGames::BasicApi::Nearby::AdvertisingResult::Status
```

Gets the response status of the advertising operation.

### Succeeded

```
bool GooglePlayGames::BasicApi::Nearby::AdvertisingResult::Succeeded
```

Gets a value indicating whether the advertising operation was successful.

## Public functions

### AdvertisingResult

```
 GooglePlayGames::BasicApi::Nearby::AdvertisingResult::AdvertisingResult(
  ResponseStatus status,
  string localEndpointName
)
```

Constructs a new [AdvertisingResult](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_advertising_result).

Details | || Parameters | |  |  | | --- | --- | | `status` | The result of the advertising attempt. | | `localEndpointName` | The name of the local endpoint. | |
| Exceptions | |  |  | | --- | --- | | `System.ArgumentNullException` | If localEndpointName is null. | |