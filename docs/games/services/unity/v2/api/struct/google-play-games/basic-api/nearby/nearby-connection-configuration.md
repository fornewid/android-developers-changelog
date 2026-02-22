---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration
source: md.txt
---

# GooglePlayGames.BasicApi.Nearby.NearbyConnectionConfiguration Struct Reference

# GooglePlayGames.BasicApi.Nearby.NearbyConnectionConfiguration

Defines the configuration for establishing a[Nearby](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby)connection.

## Summary

This includes parameters like client ID and initialization callback.

| ### Constructors and Destructors ||
|---|---|
| [NearbyConnectionConfiguration](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration_1a61db78849546bf81d18e6c8b71871777)`(Action< `[InitializationStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby_1ac4f721f70ef2577c62ecce26a87807ac)` > callback, long localClientId)` Initializes a new instance of the[NearbyConnectionConfiguration](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration)struct. ||

|                                                                                                                                                                                            ### Public attributes                                                                                                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [MaxReliableMessagePayloadLength](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration_1a7c6955f4214b9616f5d8c98d58cfa6e1)` = 4096`   | `const int` A constant integer representing the maximum payload length for reliable messages.   |
| [MaxUnreliableMessagePayloadLength](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration_1ae9a301681c22bfae8a91e85255138373)` = 1168` | `const int` A constant integer representing the maximum payload length for unreliable messages. |

|                                                                                                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                                                                                                            ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [InitializationCallback](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration_1a91a118d7090dd735f07f0f7581fb011a) | `Action< `[InitializationStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby_1ac4f721f70ef2577c62ecce26a87807ac)` >` Gets the callback to be invoked upon the completion of initialization. |
| [LocalClientId](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration_1ad36b34abfe955964c43111ac9d70e025)          | `long` Gets the unique identifier for the local client.                                                                                                                                                                                                                                                     |

## Public attributes

### MaxReliableMessagePayloadLength

```c#
const int GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::MaxReliableMessagePayloadLength = 4096
```  
A constant integer representing the maximum payload length for reliable messages.  

### MaxUnreliableMessagePayloadLength

```c#
const int GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::MaxUnreliableMessagePayloadLength = 1168
```  
A constant integer representing the maximum payload length for unreliable messages.

## Properties

### InitializationCallback

```c#
Action< InitializationStatus > GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::InitializationCallback
```  
Gets the callback to be invoked upon the completion of initialization.  

### LocalClientId

```c#
long GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::LocalClientId
```  
Gets the unique identifier for the local client.

## Public functions

### NearbyConnectionConfiguration

```c#
 GooglePlayGames::BasicApi::Nearby::NearbyConnectionConfiguration::NearbyConnectionConfiguration(
  Action< InitializationStatus > callback,
  long localClientId
)
```  
Initializes a new instance of the[NearbyConnectionConfiguration](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration#struct_google_play_games_1_1_basic_api_1_1_nearby_1_1_nearby_connection_configuration)struct.

<br />

|                                                                                                                                  Details                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|----------------------------------------------------------------| | `callback`      | A callback that will be invoked when initialization completes. | | `localClientId` | The unique identifier for the local client.                    | |