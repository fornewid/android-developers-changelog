---
title: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/interaction-types
url: https://developer.android.com/design/ui/wear/guides/m2-5/surfaces/interaction-types
source: md.txt
---

# Interaction types

Wear OS lets users quickly glance at information and take action. Apps, tiles, complications, notifications, and voice actions help people get things done with the watch.

## Apps

Developers can create branded, engaging experiences using Wear OS apps. These apps can take full advantage of the watch's hardware capabilities to provide rich and interactive experiences.

The app is a destination where users can interact with content and complete their task. There are many entry-points to an app, including tapping on a complication, a tile, a launcher entry, and a notification.

![watch-face](https://developer.android.com/static/wear/images/design/interaction_4.png "watch face")

**Figure 1.**The Wear OS app launcher.

## Tiles

Tiles provide quick access to glanceable information and actions. Users choose which Tiles they want to see and swipe to them from the watch face.

Tiles are great for use cases in which the user needs more information than can be displayed in a complication.

![tiles](https://developer.android.com/static/wear/images/design/interaction_8.gif "Tiles")

The user can scroll quickly through the Tiles carousel for quick access to information and actions.

## Complications

Watch faces can tell more than time; they can show relevant, timely data. By including a complication, installed apps display useful information and actions, such as upcoming appointments.

People can tap to interact with complications, including tapping to learn more in the app, or tapping to change the state of the complication. For example, imagine a complication that helps track how many glasses of water you are drinking with a quick tap.

![complications](https://developer.android.com/static/wear/images/design/interaction_1.png "complications")

**Figure 2.**A watch face with data complications for an exercise and calendar app.

## Notifications

Notifications provide ambient, contextual data.

Notifications can be expanded to offer more interactions, such as replying to a message, opening a location on a map, or playing a song. Notification templates are available for instant messaging, and calendar events.

![voice-action](https://developer.android.com/static/wear/images/design/interaction_9.png "voice action")

**Figure 3.**A notification in the notification stream.

## Voice actions

Voice actions enable hands-free interactions with Wear OS. These actions help people answer questions and can trigger specific actions on installed apps.

![fits-together](https://developer.android.com/static/wear/images/design/interaction_2.png "how it all fits")

**Figure 4.**After the user has spoken the voice command, "OK Google, show me my agenda," the query appears as text on screen.

## How it all fits together

Consider prioritizing content across surfaces according to how important and frequently users need it, as demonstrated in this example weather app:

<br />

![Complication example](https://developer.android.com/static/wear/images/design/interaction_3.png)

Complication

P1: What's the weather right now?  
![Notification example](https://developer.android.com/static/wear/images/design/interaction_5.png)

Notification

P1: Tell me about a weather advisory

<br />

<br />

![Tile example](https://developer.android.com/static/wear/images/design/interaction_7.png)

Tile

P1: What's the weather right now?

P2: What's the weather today?  
![App example](https://developer.android.com/static/wear/images/design/interaction_6.png)

App

P1: What's the weather right now?

P2: What's the weather today?

P3: What's the hourly breakdown?

P3: Preferences

<br />