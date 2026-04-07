---
title: Rooms  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/rooms
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Rooms Stay organized with collections Save and categorize content based on your preferences.



A resource representing the state of a room with multiple players.

For a list of [methods](#methods) for this resource, see the end of this page.

## Resource representations

There is no persistent data associated with this resource.

## Methods

[reset](/games/services/management/api/rooms/reset)
:   Reset all rooms for the currently authenticated player for your application. This method is only accessible to whitelisted tester accounts for your application.

[resetForAllPlayers](/games/services/management/api/rooms/resetForAllPlayers)
:   Deletes rooms where the only room participants are from whitelisted tester accounts for your application. This method is only available to user accounts for your developer console.