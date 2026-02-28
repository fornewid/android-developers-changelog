---
title: https://developer.android.com/games/pgs/savedgames
url: https://developer.android.com/games/pgs/savedgames
source: md.txt
---

Players play on multiple devices and install a game on same device multiple
times. As a result, they always need to start their game from their last
progress state. To achieve this, you must implement a cloud save solution in
your game.

To meet the Google Play Games Level Up [user experience guidelines](https://developer.android.com/games/guidelines),
your game needs to implement a cloud save solution which has two parts:

1. **Cloud Save**

   Save your player's game state to the cloud. Retrieve it when they start the
   game. Play Games Services [Saved Games](https://developer.android.com/games/pgs/savedgames#saved-games) provides a service for
   this, but you can use any cloud save solution of your choice.

   > [!NOTE]
   > **Note:** If your game supports guest mode, player progress is not saved or restored. This limitation occurs because guest mode is tied to a single device.

2. **Conflict resolution for multiple game states**

   If a user has multiple accounts or if there's a conflict between saved game
   data on their device and in the cloud, you need a conflict
   resolution policy. Usually, the user decides how to resolve these
   conflicts.
   Your conflict resolution policy should address the following key
   scenarios:
   - **Multiple accounts per user:** Handle instances where a single user interacts with the application using different accounts.
   - **State conflicts:** Resolve discrepancies that arise between the local game state and the cloud-saved game state.

## Saved games

The Saved Games service gives you a convenient way to save
your players' game progression to Google's servers. Your game can retrieve the
saved game data to allow returning players to continue a game at their last
save point from any device.
[Video](https://www.youtube.com/watch?v=iHc2RBZs5T0)

This service offers several key advantages for both players and developers:

- **Synchronize game data across multiple devices.** For example, a player can start a game on an Android phone and seamlessly continue playing on a tablet without losing progress.
- **Ensure data persistence.** Players can resume their game even if their device is lost, destroyed, or traded in for a newer model.

> [!NOTE]
> **Note:** Before using the Saved Games service, you must first [enable it in Google Play Console](https://developer.android.com/games/pgs/console/enable-features#enabling-saved-games).

To learn how to implement saved games for your platform, see
[Client implementations](https://developer.android.com/games/pgs/savedgames#client-implementations).

## Saved Games basics

A saved game consists of two parts:

- An unstructured binary blob - this data can represent whatever you choose, and your game is responsible for parsing and writing to it.
- Structured metadata - additional [properties](https://developer.android.com/games/pgs/savedgames#saved-game-metadata) associated with the binary data that allow Google Play Games Services to visually present Saved Games in the default Saved Games list user interface (UI), and to present useful information in the [Google Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games) (for example, last updated timestamp).

A game can write an arbitrary number of Saved Games for a single player,
subject to [user quota](https://developer.android.com/games/pgs/savedgames#quota), so there is no hard requirement to restrict
players to a single save file.

### Cover images

The Saved Games service provides a visual user experience in addition to
persistence features. You are strongly encouraged to associate representative
images with corresponding save files. If you are using the default Saved Games
list user interface (UI) provided by the Play Games SDK in your game,
the UI will display these cover images. The cover images may also appear in the
[Google Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games).

### Descriptions

You can provide a short text description of the content of a particular saved
game. This description is directly displayed to players and should summarize
the state that the saved game represents; for example, "Fighting the Goblins
in the Dark Woods".

### Quota

Developers are not charged for any saved game data that's stored in the cloud.
Instead, this data is counted against the player's Google Drive quota - you
never have to worry about it. The only quota that game developers need to care
about is their Google Drive API quota.

### Read Write isolation

All Saved Games are stored in your players' Google Drive Application Data
Folder. This folder can only be read and written by your game - it cannot be
viewed or modified by other developers' games, so there is additional protection
against data corruption. In addition, Saved Games are insulated from direct
tampering by players so they cannot modify individual Saved Games.

### Offline support

Your game can still read and write to a saved game when the player's device is
offline, but won't be able to sync with Google Play Games Services until
network connectivity is established. Once reconnected, Google Play Games Services
asynchronously updates the saved game data on Google's servers.

### Conflict resolution

When using the Saved Games service, your game may encounter conflicts when
attempting to save data. These conflicts can occur when a user is running more
than one instance of your application on different devices or computers. Your
application must be able to resolve these conflicts in a way that provides the
best user experience.

Typically, data conflicts occur when an instance of your application is unable
to reach the Saved Games service while attempting to load data or save it. In
general, the best way to avoid data conflicts is to always load the latest data
from the service when your application starts up or resumes, and save data to
the service with reasonable frequency. However, it is not always possible to
avoid data conflicts. Your application should make every effort to handle
conflicts such that your users' data is preserved and that they have a good
experience.

### Limits

Google Play Games Services enforces size limits on binary data and cover
image sizes of 3 MB and 800 KB respectively.

### Saved game metadata

The structured metadata for a saved game contains these these properties:

| Property | Description |
|---|---|
| **ID** | A unique string generated by Google Play Games Services for this saved game. Use this ID to refer to the saved game in your game clients. |
| **Name** | A developer-supplied short name for the saved game, for example "Save slot 1" or "PlayerName_Save1". This is not shown to players. |
| **Description** | A developer-supplied description of the saved game. |
| **Last modified** | Timestamp in milliseconds generated by Google Play Games Services for when the saved game was last updated. |
| **Played time** | A developer-supplied time (in milliseconds) to display on the saved game. This value should represent how long the player has played the corresponding save game. For example, a played time value of 3600000 will be displayed by Google Play Games Services as "1 hr". |
| **Cover image** | This is an optional, developer-supplied property that contains information about the [cover image](https://developer.android.com/games/pgs/savedgames#cover-images). |

## Client implementations

To learn how to implement saved game for your platform, see the following
resources:

- [Android](https://developer.android.com/games/pgs/android/saved-games)
- [Checklist for implementing Cloud save](https://developer.android.com/games/pgs/quality#saved-games)