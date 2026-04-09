---
title: Play Games Services Unity Plugin (v2) Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# Play Games Services Unity Plugin (v2) Reference

These are the reference pages for the games 2.0 Unity plugin.

## [GooglePlayGames](/games/services/unity/v2/api/namespace/google-play-games)

| Classes | |
| --- | --- |
| [PlayGamesLeaderboard](/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard) | Represents a Google Play Games leaderboard. |
| [PlayGamesLocalUser](/games/services/unity/v2/api/class/google-play-games/play-games-local-user) | Represents the Google Play Games local user, providing access to authentication and user-specific functionality. |
| [PlayGamesPlatform](/games/services/unity/v2/api/class/google-play-games/play-games-platform) | Provides access to the Google Play Games platform. |
| [PlayGamesScore](/games/services/unity/v2/api/class/google-play-games/play-games-score) | Represents a score on a Google Play Games leaderboard. |
| [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile) | Represents a Google Play Games user profile. |

## [GooglePlayGames.BasicApi](/games/services/unity/v2/api/namespace/google-play-games/basic-api)

| Classes | |
| --- | --- |
| [Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement) | Data interface for retrieving achievement information. |
| [AuthResponse](/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response) | Represents the response received from Play Games Services when requesting a server-side OAuth 2.0 authorization code for the signed-in player. |
| [AuthScopeExtensions](/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions) | Extensions for the AuthScope enum. |
| [CommonTypesUtil](/games/services/unity/v2/api/class/google-play-games/basic-api/common-types-util) | Utility class for common types. |
| [DummyClient](/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client) | Dummy client used in Editor. |
| [LeaderboardScoreData](/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data) | Leaderboard score data. |
| [Player](/games/services/unity/v2/api/class/google-play-games/basic-api/player) | Represents a player. |
| [PlayerProfile](/games/services/unity/v2/api/class/google-play-games/basic-api/player-profile) | Represents a player, a real-world person (tied to a Games account). |
| [PlayerStats](/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats) | [Player](/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player) stats. |
| [RecallAccess](/games/services/unity/v2/api/class/google-play-games/basic-api/recall-access) | Recall Access data. |
| [ScorePageToken](/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token) | Score page token. |

| Interfaces | |
| --- | --- |
| [IPlayGamesClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client) | Defines an abstract interface for a Play Games Client. |

## [GooglePlayGames.BasicApi.Events](/games/services/unity/v2/api/namespace/google-play-games/basic-api/events)

| Interfaces | |
| --- | --- |
| [IEvent](/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event) | Data object representing an Event. |
| [IEventsClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client) | An interface for interacting with events. |

## [GooglePlayGames.BasicApi.Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby)

| Classes | |
| --- | --- |
| [DummyNearbyConnectionClient](/games/services/unity/v2/api/class/google-play-games/basic-api/nearby/dummy-nearby-connection-client) | Dummy implementation of [INearbyConnectionClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client). |

| Interfaces | |
| --- | --- |
| [IDiscoveryListener](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener) | Interface for receiving notifications about discovered endpoints. |
| [IMessageListener](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-message-listener) | Interface for receiving messages and notifications about remote endpoints. |
| [INearbyConnectionClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client) | Interface for managing connections and communications between devices using [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections. |

| Structs | |
| --- | --- |
| [AdvertisingResult](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/advertising-result) | Represents the result of an attempt to start advertising for nearby connections. |
| [ConnectionRequest](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-request) | Represents a request to establish a connection with a remote endpoint. |
| [ConnectionResponse](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/connection-response) | Represents a response to a connection request, including status, payload, and identifying information. |
| [EndpointDetails](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/endpoint-details) | Represents details of an endpoint involved in a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) Connections operation. |
| [NearbyConnectionConfiguration](/games/services/unity/v2/api/struct/google-play-games/basic-api/nearby/nearby-connection-configuration) | Defines the configuration for establishing a [Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby#namespace_google_play_games_1_1_basic_api_1_1_nearby) connection. |

## [GooglePlayGames.BasicApi.SavedGame](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game)

| Interfaces | |
| --- | --- |
| [IConflictResolver](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver) | An interface that allows developers to resolve metadata conflicts that may be encountered while opening saved games. |
| [ISavedGameClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client) | The main entry point for interacting with saved games. |
| [ISavedGameMetadata](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata) | Interface representing the metadata for a saved game. |

| Structs | |
| --- | --- |
| [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update) | A struct representing the mutation of saved game metadata. |
| [SavedGameMetadataUpdate.Builder](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder) | A builder for constructing instances of [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update). |