---
title: https://developer.android.com/games/pgs/gamestats
url: https://developer.android.com/games/pgs/gamestats
source: md.txt
---

Game Stats are cumulative statistics about your game that players can view on
their [Gamer profile](https://play.google.com/games/profile). These stats let
players track lifetime progress, see highlight moments, and compare with other
players, and power Google Play features such as Quests, Social Challenges and
more in the future.

## Integration steps

Send data using Game Stats API as flexible player events for repetitive stats
and a predefined event `progressUpdate` for the progression stat. You will also
need to configure the logic for calculating the stats that would appear on Gamer
profile and their display information.

**Player Events** represent distinct in-game moments, game loop completions, or
progression milestones.

A player event is defined and modeled as follows:

1. An event is represented by a specific action taken by the player such as completing a match, finishing a run, unlocking a chest, or saving progress in an area.
2. Each action results in certain outcomes or has certain characteristics defining the action. These are modeled as event properties that provide context about the event and its specific outcomes (for example, match type, coins collected during that run, match result, or headshot count).

The integration consists of the following steps:

- **Declare the raw data schema:** Define player events using a CSV upload in the Play Console. See [CSV file guidelines](https://developer.android.com/games/pgs/gamestats#csv-guidelines-events).
- **Integrate with Game Stats API:** Send raw player data in the declared format for flexible player events and `progressUpdate` event.
  - Send all defined events using client side or server side integration. For more information, see examples for [Flexible Events](https://developer.android.com/games/pgs/gamestats#flexible-events-request-body) and [`progressUpdate` event](https://developer.android.com/games/pgs/gamestats#progressupdate-event).
- **Upload a ZIP file:** Provide 3 CSV files and all icon image files that define 5 repetitive stats and 1 player progression level. For more information, see [ZIP file guidelines](https://developer.android.com/games/pgs/gamestats#zip-file-stats-config). Include the following details:
  - **CSV file for repetitive stats:**
    - A unique ID for the stat.
    - Specify the event label to be used for stat calculation. You cannot use the `progressUpdate` event label here.
      - Specify the property label to be used for stat calculation. This must be a property of the specified event.
      - Specify the aggregation type (SUM, MAX, MIN, or COUNT) to determine how to calculate the stat on the selected property label.
      - Specify an optional filter condition to calculate the logic only when the condition is met. Define the property and event label, the operator (=, \<, or \>), and the threshold value.
    - Include a boolean flag to indicate if the stat can be used for competitive features.
    - If the feature can be used for competitive features then minimum and maximum hourly limits for a genuine player. This will be used for us to identify players who might be misusing when participating in features like leagues and social challenges.
    - Provide a unique display name for the stat that players see.
    - Provide unique text describing the stat. This description should provide details into how the player earns it.
    - Provide a unique icon representing the stat by entering the exact icon filename in the CSV file.
    - Provide a sequence order to specify the order in which a player would see the stats in their Gamer profile
    - Provide an optional input whether an increasing value or decreasing value is good for the player. This input will be used for celebrating player movements.
    - Provide an optional unit of measurement for the stat such as km, miles, and seconds.
  - **CSV file for player progression stat:**
    - Provide a unique display name for the player progression that players see.
    - Provide a unique icon representing the stat.
    - Provide a description for the progression stat.
    - Provide an optional input whether an increasing value or decreasing value is good for the player. This input will be used for celebrating player movements only when the `currentProgress` property is of type INT.
    - Provide an optional unit of measurement for the stat such as km, miles, seconds.
  - **CSV file for localization:** Provide localized display names for all stats.
    - Add one row for each localization.
    - Use stat display name string as added in previous CSV to uniquely identify the stat against which the localization is being added.
    - Specify the language from a list of language codes.
    - Add localization for the display name in the specified language.
    - Add localization for the stat description in the specified language.

## CSV file guidelines for events

You can import events using the `PlayerGameEvent.csv` file.

|---|---|
| **Filename** | **Required or Optional** |
| PlayerGameEvent.csv | Required |

#### PlayerGameEvent.csv format

The csv contains declared event and its properties as comma separated values in
the following order:

     Event Name,Property Name,Property Type

If you send the `progressUpdate` event for the `progressionStat`, add a row for
this event. This event must contain at least a `currentProgress` property of
type INT or STRING, plus any other properties you want to send.

##### Example table

| Event Name | Property Name | Property Type |
|---|---|---|
| matchCompleted | duration | DOUBLE |
| matchCompleted | kills | INT |
| matchCompleted | isWinner | BOOLEAN |
| matchCompleted | matchType | STRING (UTF-8) |
| itemCollected | coinsAmount | INT |
| itemCollected | weaponType | STRING (UTF-8) |
| progressUpdate | currentProgress | INT |

## ZIP file guidelines for stats


You can import stats at once using a ZIP file. Refer to the
table for the precise filenames to use in your ZIP file:

| Filename | Required or Optional | Accepted values |
| Filename | Required or Optional | Accepted values |
|---|---|---|
| [`RepetitiveStatsConfig.csv`](https://developer.android.com/games/pgs/gamestats#repetitive-stats-config-format) | Required | Metadata for many events. |
| [`ProgressionStatConfig.csv`](https://developer.android.com/games/pgs/gamestats#progression-stat-config-format) | Required | Declared event and its properties. |
| [`StatLocalizations.csv`](https://developer.android.com/games/pgs/gamestats#statlocalizations-csv-format) | Optional | Provides translations for achievement names and descriptions. |
| [Icon files](https://developer.android.com/games/pgs/gamestats#icon-files) | Required | Icons in 512 x 512 PNG, JPEG, or JPG format. |

### RepetitiveStatsConfig.csv format

The csv contains declared event and its properties as comma separated values in
the following order:

    Stat ID, Event Name,    Property Name,  Aggregation,     Stat Display Name, Stat Description, Filter Property,  Filter Operator,    Filter Value,   Is Competitive, minLimit, maxLimit, Icon File Name, Sequence Number, Good value direction, unit

In case you don't want to use the filter condition, keep the cell as blank.

##### Example table

| Stat ID | Event Name | Property Name | Aggregation | Stat Display Name | Stat Description | Filter Property (optional) | Filter Operator (optional) | Filter Value (optional) | Is Competitive | minLimit | maxLimit | Icon filename | Sequence number | Good value direction | unit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | matchCompleted | duration | MAX | Longest Match Survival | This denotes the survival time of a player in any match | isWinner | = | TRUE | TRUE | 0 | 50 | stat1.png | 1 | Decreasing | seconds |
| 2 | matchCompleted | isWinner | COUNT | Matches Won | This denotes the number of matches a player has won | isWinner | = | TRUE | TRUE | 0 | 50 | stat3.png | 2 | Increasing |   |
| 3 | matchCompleted | kills | SUM | 1-on-1 match kills | Number of kills made across 1-on-1 matches | matchType | = | "1-on-1" | FALSE |   |   | stat4.png | 4 | Increasing |   |
| 4 | itemCollected | coinsAmount | SUM | Total Gold Collected | Player collects coins while playing in a match | weaponType | = | "sword" | FALSE |   |   | stat2.png | 3 | Increasing |   |

### ProgressionStatConfig.csv format

The csv contains declared event and its properties as comma separated values in
the following order:

    Stat ID, Stat Display Name, Stat Description, Icon File Name, Good value direction, unit

The progression stat will be shown as the first stat to a player in their Gamer
Profile.

##### Example table

|---|---|---|---|---|
| **Stat ID** | **Stat Display Name** | **Stat Description** | **Icon File Name** | **Good value direction** |
| 5 | Level | Players accumulate xp by playing matches and level up. | Level.png | increasing |

### StatLocalizations.csv format

The csv contains declared event and its properties as comma separated values in
the following order:

    Stat ID, Stat Display Name, Language Code, Localized Stat Name, Localized Stat Description

##### Example table

|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Stat ID** | **Stat Display Name** | **Language Code** | **Localized Stat Name (UTF-8)** | **Localized Stat Description (UTF-8)** | 1 | Longest Match Survival | es | Supervivencia más larga en partidos | Esto denota el tiempo de supervivencia de una jugadora en cualquier partido. | 1 | Longest Match Survival | fr | Survie du match le plus long | Cela indique la durée de survie d'un joueur dans n'importe quel match. | 4 | Total Gold Collected | es | Oro total recolectado | La jugadora recoge monedas mientras juega en un partido | 4 | Total Gold Collected | fr | Or total collecté | Le joueur collecte des pièces en jouant un match |

## Plan the schema

You can send two types of data using the Game Stats API: flexible player events
and a predefined event for player progression stats. The following examples
illustrate how flexible events look across various game types.

### Flexible Player Events

Player Events are defined by distinct in-game moments, game loop completions, or
progression milestones.

- **Define events** as specific in-game moments, game loop completions, or progression milestones:
  - Game loop completions, such as a completed match or run.
  - Progression milestones, such as saved area exploration progress or a completed level.
- **Add properties** to provide context about the event and its outcomes, such as the level number, match type, weapon type, number of weapons, headshots, coins collected, match result, lap time, or car type.
- **Send events** within the gameplay session as soon as they occur. For example, send a game loop completion event immediately after the loop completes.

##### Examples

| Game type | Event Label | In-game moment / Progression Event Completion / Game Loop Completion | Outcome | Characteristics |
|---|---|---|---|---|
| Linear Progression Indie puzzle game | chapter_completed | Progression event completion | N/A | Chapter Number, Chapter Name, Number of try, number of screens, number of moves, chapter content |
| Linear Progression Indie puzzle game | screen_completed | Progression event completion |   | Chapter Number, Chapter Name, Number of try, number of moves, chapter content |
| 3D Endless runner | run_completed | Game Loop Completion | Coins collected, score | Run duration, coins collected from jetpack, booster used at run start, surfboards used, magnets used, jumper used, jetpack used |
| Open World Action RPG | areaExplorationProgress | Progression event completion | Enemies defeated, potions collected | Area number, Area name, Percentage progress |
| Open World Action RPG | questCompleted | Game loop completion | N/A | Quest name |
| Open World Action RPG | weaponUnlocked | In-game moment | N/A | Weapon Name, Weapon Level |
| Open World Action RPG | chestUnlocked | In-game moment | Enhancement ore collected |   |
| Casual puzzle with decorative meta | puzzleCompleted | Game loop completion / Progression event completion | Coins collected, Boosters collected | Number of moves, Butler's gift used?, Type of level, Level Number, color boosters used, dynamites used |
| Casual puzzle with decorative meta | cardsCollected | In-game moment | 1 star cards, 2 star cards, 3 star cards, total cards | Album number, Album name |
| Arcade Racing | raceCompleted | Game loop completion | Rank, NOS used, race_time | Type of race, rating, car_used |
| Arcade Racing | carUpgraded | In-game moment | Car characteristic that was upgraded, old level / value, new level / value | Type of car, current garage level |
| Third person Battle Royale Shooter | matchCompleted | Game loop completion | Eliminations, Headshots, Honor Value | Match type, survival time |
| eSports Management Simulation | matchCompleted | Game loop completion | Result, goals scored, goals | Opponent team name, playing team name |
| eSports Management Simulation | trainingCompleted | In-game moment | Drills done, teamplay_form_attack, teamplay_form_defense, teamplay_form_possession, teamplay_form_condition |   |

### `progressUpdate` Event

If your game has a primary progression mechanic, use this event to send the
player's current progress. The event has one predefined property called
"currentProgress" of type INT or STRING. Send the value of current progress
using this property, as it is the only value that appears in the Gamer Profile's
Game Stats UI.

Since players could compare their profiles by the current progress within the
game, it is important that there is no delay in getting the current progress
value after the first integration. In order to represent the accurate current
progress to players, you should send the `progressUpdate` event at the start of
each game session as well as whenever there is an update to the current
progress.

##### Examples

| Game type | currentProgress property of \`progressUpdate\` event |
|---|---|
| Linear Progression Puzzle Game | Current Chapter Number Or Level Number |
| 3d Endless Runner | High Score, Current Boosters balance |
| Casual Puzzle | Current Level number, First Try Wins count, Areas Completed count, Number of Collections Completed |
| Arcade Racing | Current Level number, Currency Balance |
| Open World Action RPG | Current Character Rank, Current Level number |
| Third Person Shooter | Current Level number |
| Esports Simulation | Manager Level number, Club Level number |

## Integration details

The API endpoints and SDK are available for early feedback and will be
Generally Available (GA) starting July 2026. See [timeline](https://developer.android.com/games/pgs/gamestats#timeline)

This section shows how to construct events and send them in both client side and
server side integrations.

### When should you send data

**Flexible Events** represent in-game actions related to game loop completions
or specific in-game moments. Submit these events as soon as they occur. For
example, submit the game loop completion event as soon as the loop completes.

**`progressUpdate` Event** represents the current progress level of a player.
The data for progression stat should be sent using this event in the following
situations:

1. Whenever there is an update to current progress send the latest value immediately
2. Whenever a player launches the game so as to ensure the presence of this stat for a player at all times.

#### Integration paths

There are two paths of integration - client and server to server.

### Server to server integration

A public API endpoint lets you send events in the request payload using the
following configurations:

##### Path parameters

| Parameter | Data type | Description |
|---|---|---|
| playerId | String | The PGS ID of the player. |

#### Authorization and Authentication

Server-to-server API calls follow standard [Server-side access to Play Games
Services](https://developer.android.com/games/pgs/android/server-access) guidelines using OAuth 2.0. Requests must include a Bearer token
authorized with the `https://www.googleapis.com/auth/games` scope.

##### Flexible Events: Request Body

**BatchRecordEventsRequest**

```json
{
  "packageName": string,
  "requestTime": string,
  "events": [
    {
      object (PlayerGameEvent)
    }
  ]
}
```

**PlayerGameEvent**

```json
{
  "eventId": string,
  "eventName": string,
  "eventProperties": {
    // keys (e.g., "matchId", "score")
    "": {
       object (PropertyValue)
    }
  },
  "eventTime": string
}
```

**PropertyValue**

```json
// ONE of the following fields will be present:
{
// 64-bit integer formatted as a string to prevent data loss
"intValue": "string",
// Double-precision floating point number.
"doubleValue": number,
// Standard UTF-8 text string.
"stringValue": "string",
// Boolean value (true or false).
"boolValue": boolean,
// RFC 3339 formatted timestamp string (e.g., "2026-01-01T18:00:00Z").
"timestampValue": "string",
// Duration in seconds suffixed with 's' (e.g., "240s" or "3.5s").
"durationValue": "string"
}
```

#### `progressUpdate` event: Request Body

**BatchRecordEventsRequest**

```json
{
  "packageName": string,
  "requestTime": string,
  "events": [
    {
      object (PlayerGameEvent)
    }
  ]
}
```

**PlayerGameEvent - `progressUpdate`**

```json
{
  "eventId": string,
  "eventName": "progressUpdate",
  "eventProperties": {
    "": {
       object (PropertyValue)
// Must have at least one property "currentProgress"  of  type  INT  or  STRING
    }
  },
  "eventTime": string
}
```

#### Response Body

If successful, returns an HTTP 200 OK status with an empty JSON object.

##### Example Request Body

**Flexible event: PlayerGameEvent**

```json
{
  "packageName": "com.example.awesomegame",//Your package name
  "requestTime": "2026-01-01T18:00:00Z",
  "events": [
    {
      "eventId": "123e1234-e29b-41d4-a123-446655440000", // UUID for deduplication //and idempotency
      "eventName": "matchCompleted",
      "eventTime": "2026-01-01T17:00:00Z",
      "eventProperties": {
        "matchId": {
          "stringValue": "Match_A"
        },
        "gameMode": {
          "stringValue": "Battle_B"
        },
        "locationId": {
          "stringValue": "Location_XYZ"
        },
        "playerElimination": {
          "intValue": 2
        },
        "survivalTimeSeconds": {
          "durationValue": "240s"
        },
        "isWinner": {
          "boolValue": true
        }
      }
    }
  ]
}
```

**`progressUpdate` event**

```json
{
  "packageName": "com.example.awesomegame",//Your package name
  "requestTime": "2026-01-01T18:00:00Z",
  "events": [
    {
      "eventId": "123e1234-e29b-41d4-a123-446655440000", // UUID
      "eventName": "progressUpdate",
      "eventTime": "2026-01-01T17:00:00Z",
      "eventProperties": {
        "currentProgress": {
          "intValue": 52
        },
//Add more properties as per your requirement
      }
    }
  ]
}
```

### Client side integration

Client side integration will be made available using Unity, Java and C++ SDKs.

The client side integration for `PlayerGameEvent` would involve you building the
event object in Java or Csharp, depending on the SDK, at the trigger points and
sending them using the upload functions provided by the SDK.

Similarly, for the `progressUpdate` event, record updated progress using the
`currentProgress` property with additional defined properties and send them
using upload functions provided by the SDK.

##### Events

The client side integration for `PlayerGameEvent` are:

##### Build Flexible Player Game Event

### Java


    // Build the PlayerGameEvent
    PlayerGameEvent event = new PlayerGameEvent.Builder("matchCompleted")
      .addProperty("matchId", "Match_A")
      .addProperty("gameMode", "Battle_B")
      .addProperty("mapId", "Location_XYZ")
      .addProperty("isWinner", true)
      .addProperty("survivalTimeSeconds", "240s")
      .addProperty("playerElimination", 2)
      .build();

    List events = new ArrayList<>();
    // ... populate list ...

### Unity


    // Build the PlayerGameEvent
    var playerEvent = new PlayerGameEvent.Builder("matchCompleted")
       .AddProperty("matchId", "Match_A")
       .AddProperty("gameMode", "Battle_B")
       .AddProperty("mapId", "Location_XYZ")
       .AddProperty("isWinner", true)
       .AddProperty("survivalTimeSeconds", "240s")
       .AddProperty("playerElimination", 2)
       .Build();
    var events = new List();
    // ... populate list ...

### C++


    // Build the PlayerGameEvent
    PgsPlayerGameEvent* player_event = PgsPlayerGameEvent_create("matchCompleted");
    if (player_event != nullptr) {
       PgsPlayerGameEvent_putString(player_event, "matchId", "Match_A");
       PgsPlayerGameEvent_putString(player_event, "gameMode", "Battle_B");
       PgsPlayerGameEvent_putString(player_event, "mapId", "Location_XYZ");
       PgsPlayerGameEvent_putBoolean(player_event, "isWinner", true);
       PgsPlayerGameEvent_putString(player_event, "survivalTimeSeconds", "240s");
       PgsPlayerGameEvent_putLong(player_event, "playerElimination", 2);
    }

##### Build `progressUpdate` Player Game Event

### Java


    // Build the PlayerGameEvent
    PlayerGameEvent event = new PlayerGameEvent.Builder("progressUpdate")
      .addProperty("currentProgress", 52)
      // Add other properties if needed
      .build();

    List events = new ArrayList<>();
    // ... populate list ...

### Unity


    // Build the PlayerGameEvent
    var progressEvent = new PlayerGameEvent.Builder("progressUpdate")
       .AddProperty("currentProgress", 52)
       // Add other properties if needed
       .Build();
    var events = new List();
    // ... populate list ...

### C++


    PgsPlayerGameEvent* progress_event = PgsPlayerGameEvent_create("progressUpdate");
    if (progress_event != nullptr) {
       PgsPlayerGameEvent_putLong(progress_event, "currentProgress", 52);
    }

##### Record Event And Upload

### Java


    // Buffers the event locally.
    client.recordEvent(event);

    // Buffers the events locally, (List version)
    client.recordEvents(events);

    // This submits the events to PGS
    client.requestEventsUpload();

### Unity


    // Buffers the event locally.
    PlayGamesPlatform.Instance.RecordEvent(playerEvent);

    // Buffers the events locally, (List version)
    PlayGamesPlatform.Instance.RecordEvents(events);

    // This submits the events to PGS
    PlayGamesPlatform.Instance.RequestEventsUpload();

### C++


    // Record the event
    PgsGameStatsClient_recordEvent(client, player_event);

    // This submits the events to PGS
    PgsGameStatsClient_requestEventsUpload(client);

    // Clean up handle to avoid leaks
    PgsPlayerGameEvent_destroy(player_event);

    // Clean up client handle when PGS operations are finished
    PgsGameStatsClient_destroy(client);

## Timeline

| **Date** | **Game Stats API Integration** | **Game Stats configuration** |
|---|---|---|
| June 2026 | - Developers can start planning data models | Not available |
| July 2026 | - API is Generally Available (GA) to all developers to start the integration - Incoming data is validated against the provided schema and configuration | - Configuration API for providing event schema and stats configuration |
| August 2026 | N/A | - Play Console experience is live with support for CSV uploads |
| September 2026 | N/A | - Players start seeing game stats on their Gamer profile |