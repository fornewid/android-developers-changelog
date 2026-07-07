---
title: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/ongoing-activities
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/ongoing-activities
source: md.txt
---

# Ongoing activities

Wear OS makes it easier for users to return to activities that run in the background, such as timers, media sessions, and workouts.

## Entry points

Users can return to the ongoing activity from multiple entry-points.

<br />

![Entry point example diagram](https://developer.android.com/static/wear/images/design/ongoing_activity_1.png)

**Figure 1.**Users can return to the ongoing activity from a watch face.  
![Entry point example diagram](https://developer.android.com/static/wear/images/design/ongoing_activity_3.png)

**Figure 2.**Users can return to the ongoing activity from the launcher.  
![Entry point example diagram](https://developer.android.com/static/wear/images/design/ongoing_activity_2.png)

**Figure 3.**Users can return to the ongoing activity from a Tile.

<br />

## Guidelines

Keep the following guidelines in mind when using ongoing activities.

### Display helpful information in the launcher entry

![](https://developer.android.com/static/wear/images/design/ongoing_activity_3.png)  
check_circle

### Do

Show critical information in the launcher entry.

The text string displayed in Recents should help users understand the type of ongoing activity, and the status of that activity.

The text to show in Recents depends on the type of app:

- **Media apps:**Show the track name, such as the song name or podcast name.
- **Fitness apps:**Show either workout duration or workout type.
- **Navigation apps:**Show the journey's ETA, the destination name, or method of navigation.

### Refer to ongoing activities from the Tile

Show a glanceable representation on the Tile to allow the user to return to the ongoing activity while conserving power.
**Note:** To conserve power, try not to update the Tile more than once a minute.  
![](https://developer.android.com/static/wear/images/design/ongoing_activity_2.png)  
check_circle

### Do

Enable the user to tap to see more information in an app.  
![](https://developer.android.com/static/wear/images/design/ongoing_activity_4.png)  
cancel

### Don't

Show detailed information and actions for the ongoing activity on the Tile.