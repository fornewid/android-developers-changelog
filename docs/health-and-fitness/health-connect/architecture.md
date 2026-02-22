---
title: https://developer.android.com/health-and-fitness/health-connect/architecture
url: https://developer.android.com/health-and-fitness/health-connect/architecture
source: md.txt
---

SDK, client apps, and permissions management.
keywords_public: Health Connect, architecture, Android SDK, client app, APK,
permissions management, data management, CRUD, aggregation

Health Connect is designed to facilitate fast, convenient integration
between client apps and the Health Connect API.

The following diagram shows the integration between a client app and
the Health Connect API through the SDK layer and IPC
(Inter-Process Communication):
![A checkbox appears next to each health feature](https://developer.android.com/static/health-and-fitness/health-connect/images/healthconnectimage1.jpg) **Figure 1.** Health Connect architecture diagram

## SDK support

The SDK allows client apps to determine if the Health Connect API is on a user's
device. If it's not, an availability check is triggered to determine if the
device is compatible.

The Health Connect SDK supports Android 8 (API level 26) at the minimum,
while the Health Connect app is only compatible with Android 9 (API level 28)
or higher. This means that third-party apps can support users with Android 8,
but only users with Android 9 or higher can use Health Connect.

## Release channel availability

Health Connect features are released in **Alpha** and **Stable**
channels. For more information about specific releases, see the
[Health Connect client releases](https://developer.android.com/jetpack/androidx/releases/health-connect).

### Alpha channel

All features documented on the site are available.

### Stable channel

All documented features *except* [Extended device types](https://developer.android.com/health-and-fitness/health-connect/metadata#device-type).

## Architecture components

This section details the key components that make up the Health Connect
architecture, including the SDK, the client app, the Health Connect APK, and
its Permissions and Data Management features.

### 1. Software development kit

The SDK enables the client app to communicate with the Health Connect APK, over
IPC.

### 2. Client app

To integrate with Health Connect, client apps link the SDK into their health
and fitness app. This provides an API surface that facilitates interaction with
the Health Connect API.

### 3. Health Connect APK

The Health Connect APK is the main substance of the Health Connect API, and
contains both its Permissions Management and Data Management components.
The Health Connect APK is made available directly on the user's device.

### 4. Permissions management

Health Connect includes a user interface through which apps request a user's
permission to display data.

It also provides a list of existing user permissions, allowing users to
control access to data across multiple applications.
| **Note:** Health Connect requires you to request the user's permission to read and write their health and fitness data on a per-app basis.

### 5. Data management

Health Connect provides a user interface with an overview of recorded data,
whether it's a user's step count, cycling speed, heart rate, or any other
[supported data types](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/package-summary#classes). Its data management capabilities
include:

- **CRUD Operations and Data Synchronization**: The platform provides standard
  insert, update, and delete functions for data. It also includes functionality
  for client apps to synchronize data, which produces a log of data changes
  showing whether data has been inserted or deleted by other apps.

- **Basic Aggregation Functions**: Clients can apply aggregation functions to
  the data, including:

  - Average, minimum, or maximum values like minimum or maximum heart rate during a session.
  - Sum total like total steps in a day.
  - A count of measurements like number of activity sessions in a week.
  - Total duration on supported data types like time in deep sleep.
- **Reading with Health Connect**: Health Connect allows apps to read a user's
  health and fitness data either when the app is in the foreground or, with the
  user's permission, while running in the background.

  - **Foreground Reading**: You can read data from Health Connect when your app is in the foreground, and for longer operations, it is recommended to use a foreground service to prevent interruptions.
  - **Background Reading**: Your application can be granted permission by the user to read data from Health Connect while running in the background.