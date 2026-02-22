---
title: https://developer.android.com/games/gamedashboard/aboutdashboard
url: https://developer.android.com/games/gamedashboard/aboutdashboard
source: md.txt
---

# About the Game Dashboard

The Game Dashboard is an overlay displayed on top of a running game to provide features to enhance the gaming experience. It provides shortcuts to access features which are frequently used while gaming, such as:

- A live FPS counter
- Screenshots and screen recordings
- Do Not Disturb mode
- [Game Mode](https://developer.android.com/games/optimize/adpf/gamemode/about-API-and-interventions), optimizations which prioritize game[`PERFORMANCE`](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_PERFORMANCE)or saves[`BATTERY`](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_BATTERY)life

To deliver its functionalities without disrupting the game currently in play, it is divided into[Components](https://developer.android.com/games/gamedashboard/components):

- The[Entrypoint Icon](https://developer.android.com/games/gamedashboard/components#entrypoint_icon), the entry point to the Game Dashboard Overlay
- The[Game Dashboard Overlay](https://developer.android.com/games/gamedashboard/components#game-dashboard-overlay), an activity that provides access to all features
- The[Shortcut Bar](https://developer.android.com/games/gamedashboard/components#shortcut-bar), a floating bar that provides quick access to features while playing the game

The Game Dashboard is available on all Pixel devices running Android 12 or higher. On other OEM devices, Game Dashboard might be stripped out or replaced with similar applications.