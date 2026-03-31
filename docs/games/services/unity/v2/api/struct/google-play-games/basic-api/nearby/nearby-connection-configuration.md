---
title: GooglePlayGames.BasicApi.Nearby.NearbyConnectionConfiguration Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.NearbyConnectionConfiguration

Defines the configuration for establishing a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) connection.

## Summary

This includes parameters like client ID and initialization callback.

| Constructors and Destructors | |
| --- | --- |
| `NearbyConnectionConfiguration(Action< InitializationStatus > callback, long localClientId)`   Initializes a new instance of the [NearbyConnectionConfiguration](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration) struct. | |

| Public attributes | |
| --- | --- |
| `MaxReliableMessagePayloadLength = 4096` | `const int`  A constant integer representing the maximum payload length for reliable messages. |
| `MaxUnreliableMessagePayloadLength = 1168` | `const int`  A constant integer representing the maximum payload length for unreliable messages. |

| Properties | |
| --- | --- |
| `InitializationCallback` | `Action< InitializationStatus >`  Gets the callback to be invoked upon the completion of initialization. |
| `LocalClientId` | `long`  Gets the unique identifier for the local client. |

## Public attributes

### MaxReliableMessagePayloadLength

```
const int GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::MaxReliableMessagePayloadLength = 4096
```

A constant integer representing the maximum payload length for reliable messages.

### MaxUnreliableMessagePayloadLength

```
const int GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::MaxUnreliableMessagePayloadLength = 1168
```

A constant integer representing the maximum payload length for unreliable messages.

## Properties

### InitializationCallback

```
Action< InitializationStatus > GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::InitializationCallback
```

Gets the callback to be invoked upon the completion of initialization.

### LocalClientId

```
long GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::LocalClientId
```

Gets the unique identifier for the local client.

## Public functions

### NearbyConnectionConfiguration

```
 GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::NearbyConnectionConfiguration(
  Action< InitializationStatus > callback,
  long localClientId
)
```

Initializes a new instance of the [NearbyConnectionConfiguration](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration) struct.

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback that will be invoked when initialization completes. | | `localClientId` | The unique identifier for the local client. | |