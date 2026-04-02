---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event
source: md.txt
---

# GooglePlayGames.BasicApi.Events.IEvent Interface Reference

# GooglePlayGames.BasicApi.Events.IEvent

Data object representing an Event.

## Summary

Native.PInvoke.EventManager for more.

### Inheritance

Direct Known Subclasses:[GooglePlayGames.BasicApi.Events.Event](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/events/event)

|                                                                                                                                   ### Properties                                                                                                                                   ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [CurrentCount](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event_1a2f225206c85c3a0af7acef980d6d3e2d) | `ulong` The current count for this event.      |
| [Description](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event_1a0d513b9ccc0d868cc34628458a6773e6)  | `string` The description of the event.         |
| [Id](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event_1ae1810c681eccd21137b21260829990b5)           | `string` The ID of the event.                  |
| [ImageUrl](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event_1a525fa65ffcaaf2a14593233eae2bf3a5)     | `string` The URL of the image for the event.   |
| [Name](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event_1a37da68c56f3cecadcfa65b99e7ae9fca)         | `string` The name of the event.                |
| [Visibility](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-event#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_event_1ab36c6750d7fe08e0496f0239e83101e6)   | `EventVisibility` The visibility of the event. |

## Properties

### CurrentCount

```c#
ulong CurrentCount
```  
The current count for this event.  

### Description

```c#
string Description
```  
The description of the event.  

### Id

```c#
string Id
```  
The ID of the event.  

### ImageUrl

```c#
string ImageUrl
```  
The URL of the image for the event.

Empty if there is no image for this event.

The image URL.  

### Name

```c#
string Name
```  
The name of the event.  

### Visibility

```c#
EventVisibility Visibility
```  
The visibility of the event.