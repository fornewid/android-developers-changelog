---
title: https://developer.android.com/health-and-fitness/health-connect/features/native-tracking
url: https://developer.android.com/health-and-fitness/health-connect/features/native-tracking
source: md.txt
---

Health Connect uses device sensors to generate data for certain data types
through **built-in on-device tracking**. With this capability, Health Connect
can record metrics like steps, distance, and active calories burned without
requiring this data from other apps.

This device-level tracking ensures data consistency across all apps connected to
Health Connect and frees your app from needing to implement its own
algorithms, such as deriving distance or active calories from step counts.

## Data types with built-in tracking

Health Connect supports built-in tracking for the following data types:

<br />

| Data Type | Description | Featured Guides |
|---|---|---|
| **Active calories burned** | The estimated calories burned by the user during activity, based on their step count. | [Workouts](https://developer.android.com/health-and-fitness/health-connect/experiences/workouts) guide |
| **Distance** | The estimated distance covered by the user based on their step count. | [Workouts](https://developer.android.com/health-and-fitness/health-connect/experiences/workouts) guide |
| **Steps** | The number of steps taken by the user, detected by device sensors. | [Workouts](https://developer.android.com/health-and-fitness/health-connect/experiences/workouts) guide [Track steps](https://developer.android.com/health-and-fitness/health-connect/features/steps) guide |

<br />

Health Connect only begins tracking a data type when an app requests and
receives permission to read it. If no apps have permission for a given type,
Health Connect doesn't track it.

## User controls

Users can disable built-in tracking for any data type at any time from
Health Connect settings in Android System Settings. If a user disables
tracking, Health Connect stops generating new data of that type but retains
all previously recorded data.

To find Health Connect in Settings, see
[this Android Help article](https://support.google.com/android/answer/13770320).