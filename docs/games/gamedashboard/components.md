---
title: https://developer.android.com/games/gamedashboard/components
url: https://developer.android.com/games/gamedashboard/components
source: md.txt
---

The Game Dashboard is composed of multiple components that provide quick access
to commonly used features.

## Enabling the Game Dashboard

To enable or disable the Game Dashboard, go to **Settings \> Google \> Game
Dashboard** and turn on or off **Use Game Dashboard** as shown in the following screenshots.

![Game Dashboard Settings - Steps!](https://developer.android.com/static/images/games/game-dashboard/settings.png "Game Dashboard in Settings - Steps")

### Troubleshooting

If the **Game Dashboard** entry is not showing up in **Settings** , make sure that your
Google Play Services has been updated. To update your Google Play Services,
follow the instructions listed in [Keep your device \& apps working with Google
Play Services](https://support.google.com/googleplay/answer/9037938).

## Entrypoint Icon

The *Entrypoint Icon* opens the [Game Dashboard Overlay](https://developer.android.com/games/gamedashboard/components#game-dashboard-overlay).
It is revealed from the top right corner of the screen when the user swipes to
reveal the system UI bar inside of a fullscreen immersive game. Tapping the
Entrypoint Icon opens the Game Dashboard Overlay.

![Entrypoint Icon!](https://developer.android.com/static/images/games/game-dashboard/entrypoint-icon.png "Entrypoint Icon")

## Game Dashboard Overlay

The *Game Dashboard Overlay* is an activity launched on top of the game and provides
access to a suite of in-game features. It consists of two section containers, Toggles and Tiles.

![Game Dashboard Overlay!](https://developer.android.com/static/images/games/game-dashboard/overlay.png "Game Dashboard Overlay")

### Toggles

*Toggle* buttons show or hide their associated features in the
[Shortcut Bar](https://developer.android.com/games/gamedashboard/components#shortcut-bar) or
enable or disable them immediately.

### Tiles

*Tiles* provide the functionalities offered by the Game Dashboard in the context
of the running game. For example:

- The *Optimization Tile* sets the specific [Game
  Mode](https://developer.android.com/games/optimize/adpf/gamemode/about-API-and-interventions) of the running game to [`STANDARD`](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_STANDARD), [`PERFORMANCE`](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_PERFORMANCE), or [`BATTERY`](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_BATTERY).
  - To enable the Optimization Tile, implement [Game Mode API](https://developer.android.com/games/optimize/adpf/gamemode/about-API-and-interventions) in your game.
- The *Achievements Tile* keeps track of the [Achievements](https://developers.google.com/games/services/common/concepts/achievements) in the current game.
  - To enable the Achievements Tile, implement Achievements following the instructions in [Achievements in Android Games](https://developers.google.com/games/services/android/achievements).
- The *Leaderboards Tile* keeps track of the [Leaderboards](https://developers.google.com/games/services/common/concepts/leaderboards) for the current game.

## Shortcut Bar

The *Shortcut Bar* provides easy access to common functionalities such as taking a
screenshot, recording gameplay, or monitoring FPS without leaving the game. The
icons present on the Shortcut Bar are set by the Toggle buttons within the Game
Dashboard Overlay. The Shortcut Bar can be docked on the side of the screen to
minimize its presence over the game.

![Shortcut Bar Docked!](https://developer.android.com/static/images/games/game-dashboard/shortcutbar-docked.png "Shortcut Bar Docked")

![Shortcut Bar Expanded!](https://developer.android.com/static/images/games/game-dashboard/shortcutbar-expanded.png "Shortcut Bar Expanded")