---
title: Google Play Games C++ API Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# Google Play Games C++ API Reference

These are the reference pages for the Play Games services C++ APIs.

| Classes | |
| --- | --- |
| [gpg::Achievement](/games/services/cpp/api/class/gpg/achievement) | A single data structure which allows you to access data about the status of a specific achievement. |
| [gpg::AchievementManager](/games/services/cpp/api/class/gpg/achievement-manager) | Gets and sets various achievement-related data. |
| [gpg::AndroidPlatformConfiguration](/games/services/cpp/api/class/gpg/android-platform-configuration) | The platform configuration used when creating an instance of the [GameServices](/games/services/cpp/api/class/gpg/game-services#classgpg_1_1_game_services) class on Android. |
| [gpg::CaptureOverlayStateListenerHelper](/games/services/cpp/api/class/gpg/capture-overlay-state-listener-helper) | Defines a helper which can be used to provide [ICaptureOverlayStateListener](/games/services/cpp/api/class/gpg/i-capture-overlay-state-listener#classgpg_1_1_i_capture_overlay_state_listener) callbacks to the SDK without defining the full [ICaptureOverlayStateListener](/games/services/cpp/api/class/gpg/i-capture-overlay-state-listener#classgpg_1_1_i_capture_overlay_state_listener) interface. |
| [gpg::EndpointDiscoveryListenerHelper](/games/services/cpp/api/class/gpg/endpoint-discovery-listener-helper) | Defines a helper which can be used to provide [IEndpointDiscoveryListener](/games/services/cpp/api/class/gpg/i-endpoint-discovery-listener#classgpg_1_1_i_endpoint_discovery_listener) callbacks to the SDK without defining the full [IEndpointDiscoveryListener](/games/services/cpp/api/class/gpg/i-endpoint-discovery-listener#classgpg_1_1_i_endpoint_discovery_listener) interface. |
| [gpg::Event](/games/services/cpp/api/class/gpg/event) | A single data structure containing data about the status of a specific event. |
| [gpg::EventManager](/games/services/cpp/api/class/gpg/event-manager) | Gets and sets various event-related data. |
| [gpg::GameServices](/games/services/cpp/api/class/gpg/game-services) | The starting point for interacting with Google Play Games. |
| [gpg::GameServices::Builder](/games/services/cpp/api/class/gpg/game-services/builder) | Used for creating and configuring an instance of the [GameServices](/games/services/cpp/api/class/gpg/game-services#classgpg_1_1_game_services) class. |
| [gpg::ICaptureOverlayStateListener](/games/services/cpp/api/class/gpg/i-capture-overlay-state-listener) | Defines an interface that can deliver events relating to changes in video capture state. |
| [gpg::ICrossAppEndpointDiscoveryListener](/games/services/cpp/api/class/gpg/i-cross-app-endpoint-discovery-listener) | Defines an interface which can be delivered events relating to cross-app remote endpoint discovery. |
| [gpg::IEndpointDiscoveryListener](/games/services/cpp/api/class/gpg/i-endpoint-discovery-listener) | Defines an interface which can be delivered events relating to remote endpoint discovery. |
| [gpg::IMessageListener](/games/services/cpp/api/class/gpg/i-message-listener) | Defines an interface which can be delivered messages from remote endpoints. |
| [gpg::IRealTimeEventListener](/games/services/cpp/api/class/gpg/i-real-time-event-listener) | Defines an interface that can deliver events relating to real-time multiplayer. |
| [gpg::Leaderboard](/games/services/cpp/api/class/gpg/leaderboard) | A single data structure allowing you to access data about the status of a specific leaderboard, such as its name and validity. |
| [gpg::LeaderboardManager](/games/services/cpp/api/class/gpg/leaderboard-manager) | Gets and sets various leaderboard-related data. |
| [gpg::MessageListenerHelper](/games/services/cpp/api/class/gpg/message-listener-helper) | Defines a helper which can be used to provide [IMessageListener](/games/services/cpp/api/class/gpg/i-message-listener#classgpg_1_1_i_message_listener) callbacks to the SDK without defining the full [IMessageListener](/games/services/cpp/api/class/gpg/i-message-listener#classgpg_1_1_i_message_listener) interface. |
| [gpg::MultiplayerInvitation](/games/services/cpp/api/class/gpg/multiplayer-invitation) | A data structure containing data about the current state of an invitation to a turn-based match. |
| [gpg::MultiplayerParticipant](/games/services/cpp/api/class/gpg/multiplayer-participant) | A data structure containing data about a participant in a multiplayer match. |
| [gpg::NearbyConnections](/games/services/cpp/api/class/gpg/nearby-connections) | An API used for creating connections and communicating between apps on the same local network. |
| [gpg::NearbyConnections::Builder](/games/services/cpp/api/class/gpg/nearby-connections/builder) | [Builder](/games/services/cpp/api/class/gpg/nearby-connections/builder#classgpg_1_1_nearby_connections_1_1_builder) class used to construct [NearbyConnections](/games/services/cpp/api/class/gpg/nearby-connections#classgpg_1_1_nearby_connections) objects. |
| [gpg::ParticipantResults](/games/services/cpp/api/class/gpg/participant-results) | A data structure containing data about the per-participant results for a `TurnBasedMatch`. |
| [gpg::Player](/games/services/cpp/api/class/gpg/player) | A data structure that allows you to access data about a specific player. |
| [gpg::PlayerLevel](/games/services/cpp/api/class/gpg/player-level) | A single data structure containing data about player's level. |
| [gpg::PlayerManager](/games/services/cpp/api/class/gpg/player-manager) | Gets and sets various player-related data. |
| [gpg::PlayerStats](/games/services/cpp/api/class/gpg/player-stats) | A data structure that allows you to access data about a specific player. |
| [gpg::RealTimeEventListenerHelper](/games/services/cpp/api/class/gpg/real-time-event-listener-helper) | Defines a helper which can be used to provide [IRealTimeEventListener](/games/services/cpp/api/class/gpg/i-real-time-event-listener#classgpg_1_1_i_real_time_event_listener) callbacks to the SDK without defining the full [IRealTimeEventListener](/games/services/cpp/api/class/gpg/i-real-time-event-listener#classgpg_1_1_i_real_time_event_listener) interface. |
| [gpg::RealTimeMultiplayerManager](/games/services/cpp/api/class/gpg/real-time-multiplayer-manager) | Fetches, modifies, handles messaging for, and creates `RealTimeRoom` objects. |
| [gpg::RealTimeRoom](/games/services/cpp/api/class/gpg/real-time-room) | A data structure containing the current state of a real-time multiplayer room. |
| [gpg::RealTimeRoomConfig](/games/services/cpp/api/class/gpg/real-time-room-config) | A data structure containing the data needed to create a `RealTimeRoom` object. |
| [gpg::RealTimeRoomConfig::Builder](/games/services/cpp/api/class/gpg/real-time-room-config/builder) | Builds one or more [RealTimeRoomConfig](/games/services/cpp/api/class/gpg/real-time-room-config#classgpg_1_1_real_time_room_config) objects. |
| [gpg::Score](/games/services/cpp/api/class/gpg/score) | Single data structure which allows you to access data about a player's score. |
| [gpg::ScorePage](/games/services/cpp/api/class/gpg/score-page) | A single data structure which allows you to access score data. |
| [gpg::ScorePage::Entry](/games/services/cpp/api/class/gpg/score-page/entry) | A class that creates an entry on a score page. |
| [gpg::ScorePage::ScorePageToken](/games/services/cpp/api/class/gpg/score-page/score-page-token) | A data structure that is a nearly-opaque type representing a query for a [ScorePage](/games/services/cpp/api/class/gpg/score-page#classgpg_1_1_score_page) (or is empty). |
| [gpg::ScoreSummary](/games/services/cpp/api/class/gpg/score-summary) | A single data structure which allows you to access a summary of score information. |
| [gpg::SnapshotManager](/games/services/cpp/api/class/gpg/snapshot-manager) | Gets and sets various snapshot-related data. |
| [gpg::SnapshotMetadata](/games/services/cpp/api/class/gpg/snapshot-metadata) | A single data structure that allows you to access data about the status of a specific snapshot metadata. |
| [gpg::SnapshotMetadataChange](/games/services/cpp/api/class/gpg/snapshot-metadata-change) | A single data structure which allows you to access data about the status of a specific snapshot. |
| [gpg::SnapshotMetadataChange::Builder](/games/services/cpp/api/class/gpg/snapshot-metadata-change/builder) | Builds one or more [SnapshotMetadataChange](/games/services/cpp/api/class/gpg/snapshot-metadata-change#classgpg_1_1_snapshot_metadata_change) objects. |
| [gpg::SnapshotMetadataChange::CoverImage](/games/services/cpp/api/class/gpg/snapshot-metadata-change/cover-image) | A single data structure which allows you to access data about the status of a specific cover image. |
| [gpg::StatsManager](/games/services/cpp/api/class/gpg/stats-manager) | Gets and sets various stats-related data. |
| [gpg::TurnBasedMatch](/games/services/cpp/api/class/gpg/turn-based-match) | A data structure containing data about the current state of a `TurnBasedMatch`. |
| [gpg::TurnBasedMatchConfig](/games/services/cpp/api/class/gpg/turn-based-match-config) | A data structure containing the data needed to create a `TurnBasedMatch`. |
| [gpg::TurnBasedMatchConfig::Builder](/games/services/cpp/api/class/gpg/turn-based-match-config/builder) | Builds one or more [TurnBasedMatchConfig](/games/services/cpp/api/class/gpg/turn-based-match-config#classgpg_1_1_turn_based_match_config) objects. |
| [gpg::TurnBasedMultiplayerManager](/games/services/cpp/api/class/gpg/turn-based-multiplayer-manager) | Fetches, modifies and creates `TurnBasedMatch` objects. |
| [gpg::VideoCapabilities](/games/services/cpp/api/class/gpg/video-capabilities) | A data structure which allows access to information on what capabilities the current device has for video recording. |
| [gpg::VideoCaptureState](/games/services/cpp/api/class/gpg/video-capture-state) | A data structure which allows access to the current state of video capture. |
| [gpg::VideoManager](/games/services/cpp/api/class/gpg/video-manager) | Gets and sets various video-related data. |

| Structs | |
| --- | --- |
| [gpg::AchievementManager::FetchAllResponse](/games/services/cpp/api/struct/gpg/achievement-manager/fetch-all-response) | Holds all data for all achievements, along with a response status. |
| [gpg::AchievementManager::FetchResponse](/games/services/cpp/api/struct/gpg/achievement-manager/fetch-response) | Contains data and response status for a single achievement. |
| [gpg::AndroidInitialization](/games/services/cpp/api/struct/gpg/android-initialization) | [AndroidInitialization](/games/services/cpp/api/struct/gpg/android-initialization#structgpg_1_1_android_initialization) includes three initialization functions, exactly one of which must be called. |
| [gpg::AndroidSupport](/games/services/cpp/api/struct/gpg/android-support) | Functions which enable pre- Android 4.0 support. |
| [gpg::AppIdentifier](/games/services/cpp/api/struct/gpg/app-identifier) | An identifier for an application. |
| [gpg::BaseStatus](/games/services/cpp/api/struct/gpg/base-status) | A struct containing all possible status codes that can be returned by our APIs. |
| [gpg::ConnectionRequest](/games/services/cpp/api/struct/gpg/connection-request) | A request to establish a connection. |
| [gpg::ConnectionResponse](/games/services/cpp/api/struct/gpg/connection-response) | A response to a connection request. |
| [gpg::EndpointDetails](/games/services/cpp/api/struct/gpg/endpoint-details) | Details about a remote endpoint that the app has discovered. |
| [gpg::EventManager::FetchAllResponse](/games/services/cpp/api/struct/gpg/event-manager/fetch-all-response) | `Data` and `ResponseStatus` for all events. |
| [gpg::EventManager::FetchResponse](/games/services/cpp/api/struct/gpg/event-manager/fetch-response) | Contains data and response status for a single event. |
| [gpg::LeaderboardManager::FetchAllResponse](/games/services/cpp/api/struct/gpg/leaderboard-manager/fetch-all-response) | Contains data and response statuses for all leaderboards. |
| [gpg::LeaderboardManager::FetchAllScoreSummariesResponse](/games/services/cpp/api/struct/gpg/leaderboard-manager/fetch-all-score-summaries-response) | Contains all data and response statuses for all leaderboard score summaries. |
| [gpg::LeaderboardManager::FetchResponse](/games/services/cpp/api/struct/gpg/leaderboard-manager/fetch-response) | Holds data for a leaderboard, along with a response status. |
| [gpg::LeaderboardManager::FetchScorePageResponse](/games/services/cpp/api/struct/gpg/leaderboard-manager/fetch-score-page-response) | Returns response status and data from the accessed score page. |
| [gpg::LeaderboardManager::FetchScoreSummaryResponse](/games/services/cpp/api/struct/gpg/leaderboard-manager/fetch-score-summary-response) | Data and response status for a specified leaderboard score summary. |
| [gpg::PlayerManager::FetchListResponse](/games/services/cpp/api/struct/gpg/player-manager/fetch-list-response) | A response which contains a vector of players. |
| [gpg::PlayerManager::FetchResponse](/games/services/cpp/api/struct/gpg/player-manager/fetch-response) | `data` and `ResponseStatus` for a specific [Player](/games/services/cpp/api/class/gpg/player#classgpg_1_1_player). |
| [gpg::PlayerManager::FetchSelfResponse](/games/services/cpp/api/struct/gpg/player-manager/fetch-self-response) | Holds all player data, along with a response status. |
| [gpg::RealTimeMultiplayerManager::FetchInvitationsResponse](/games/services/cpp/api/struct/gpg/real-time-multiplayer-manager/fetch-invitations-response) | `Data` and `ResponseStatus` for the `FetchInvitations` operation. |
| [gpg::RealTimeMultiplayerManager::RealTimeRoomResponse](/games/services/cpp/api/struct/gpg/real-time-multiplayer-manager/real-time-room-response) | `Data` and `ResponseStatus` for a specific `RealTimeRoom` object. |
| [gpg::RealTimeMultiplayerManager::RoomInboxUIResponse](/games/services/cpp/api/struct/gpg/real-time-multiplayer-manager/room-inbox-u-i-response) | `Data` and `ResponseStatus` for the `ShowRoomInboxUI` operation. |
| [gpg::RealTimeMultiplayerManager::WaitingRoomUIResponse](/games/services/cpp/api/struct/gpg/real-time-multiplayer-manager/waiting-room-u-i-response) | `Data` and `ResponseStatus` for the `ShowWaitingRoomUI` operation. |
| [gpg::SnapshotManager::CommitResponse](/games/services/cpp/api/struct/gpg/snapshot-manager/commit-response) | Holds the data for an updated snapshot, along with a response status. |
| [gpg::SnapshotManager::FetchAllResponse](/games/services/cpp/api/struct/gpg/snapshot-manager/fetch-all-response) | Holds all data for all snapshots, along with a response status. |
| [gpg::SnapshotManager::MaxSizeResponse](/games/services/cpp/api/struct/gpg/snapshot-manager/max-size-response) | Holds max size for snapshot data and for snapshot cover image. |
| [gpg::SnapshotManager::OpenResponse](/games/services/cpp/api/struct/gpg/snapshot-manager/open-response) | Holds the data for a particular requested snapshot along with a response status. |
| [gpg::SnapshotManager::ReadResponse](/games/services/cpp/api/struct/gpg/snapshot-manager/read-response) | Reads response status and snapshot data returned from a snapshot read operation. |
| [gpg::SnapshotManager::SnapshotSelectUIResponse](/games/services/cpp/api/struct/gpg/snapshot-manager/snapshot-select-u-i-response) | `Data` and `ResponseStatus` for the `ShowSelectUIOperation` operation. |
| [gpg::StartAdvertisingResult](/games/services/cpp/api/struct/gpg/start-advertising-result) | The ID and name of an instance registered on this device. |
| [gpg::StatsManager::FetchForPlayerResponse](/games/services/cpp/api/struct/gpg/stats-manager/fetch-for-player-response) | Holds all [PlayerStats](/games/services/cpp/api/class/gpg/player-stats#classgpg_1_1_player_stats) data, along with a response status. |
| [gpg::TurnBasedMultiplayerManager::MatchInboxUIResponse](/games/services/cpp/api/struct/gpg/turn-based-multiplayer-manager/match-inbox-u-i-response) | `Data` and `ResponseStatus` for the `ShowMatchInboxUI` operation. |
| [gpg::TurnBasedMultiplayerManager::PlayerSelectUIResponse](/games/services/cpp/api/struct/gpg/turn-based-multiplayer-manager/player-select-u-i-response) | `Data` and `ResponseStatus` for the `ShowPlayerSelectUI` operation. |
| [gpg::TurnBasedMultiplayerManager::TurnBasedMatchResponse](/games/services/cpp/api/struct/gpg/turn-based-multiplayer-manager/turn-based-match-response) | `Data` and `ResponseStatus` for a specific `TurnBasedMatch`. |
| [gpg::TurnBasedMultiplayerManager::TurnBasedMatchesResponse](/games/services/cpp/api/struct/gpg/turn-based-multiplayer-manager/turn-based-matches-response) | `Data` and `ResponseStatus` for [TurnBasedMatches](/games/services/cpp/api/class/gpg/turn-based-match#classgpg_1_1_turn_based_match) and [invitations](/games/services/cpp/api/class/gpg/multiplayer-invitation#classgpg_1_1_multiplayer_invitation). |
| [gpg::VideoManager::GetCaptureCapabilitiesResponse](/games/services/cpp/api/struct/gpg/video-manager/get-capture-capabilities-response) | Holds data for video capabilities, along with a response status. |
| [gpg::VideoManager::GetCaptureStateResponse](/games/services/cpp/api/struct/gpg/video-manager/get-capture-state-response) | Holds data for video capture state, along with a response status. |
| [gpg::VideoManager::IsCaptureAvailableResponse](/games/services/cpp/api/struct/gpg/video-manager/is-capture-available-response) | Holds whether or not a capture mode (specified in `IsCaptureAvailable`) is available, along with a response status. |