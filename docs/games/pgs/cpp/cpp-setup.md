---
title: Set up v2 Native C or C++  |  Android game development  |  Android Developers
url: https://developer.android.com/games/pgs/cpp/cpp-setup
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Set up v2 Native C or C++ Stay organized with collections Save and categorize content based on your preferences.




This document helps you set up your C++ project for
v2 Native C or C++ and verify the authentication service.

## Before you start

You must [set up Play Games Services](/games/pgs/console/setup) in
Google Play Console.

### App prerequisites

Make sure that your app's build file uses the following values:

* A `minSdkVersion` of `19` or higher
* A `compileSdkVersion` of `28` or higher

## Set up your game project

Complete the following steps to set up your game project.

### Update build.gradle

In your app-level `build.gradle` file, do the following:

* Make sure the [prefab](/reference/tools/gradle-api/4.1/com/android/build/api/dsl/BuildFeatures#prefab) build feature is enabled.
* Add the dependency for the v2 Native SDK (beta):

  + `com.google.android.gms:play-services-games-v2-native-c:21.0.0-beta1`

Here's an example:

```
  android {
    ...
    buildFeatures {
      prefab true
    }
    ...
  }
  dependencies {
    ...
    implementation "com.google.android.gms:play-services-games-v2-native-c:21.0.0-beta1"
  }
```

### Update CMakeLists.txt

In your `CMakeLists.txt` file, add the following code:

```
  find_package(com.google.android.gms.games.v2.c REQUIRED CONFIG)

  // link games_static for -DANDROID_STL=c++_static or default
  // link games_shared for -DANDROID_STL=c++_shared
  target_link_libraries(
    app PUBLIC com.google.android.gms.games.v2.c::games_static)
```

### Update AndroidManifest.xml

1. To define your Play Games Services project ID in your `AndroidManifest.xml`
   file, add the following lines:

   ```
   <manifest>
     <application>
       <meta-data android:name="com.google.android.gms.games.APP_ID"
                  android:value="@string/game_services_project_id"/>
     </application>
   </manifest>
   ```
2. Create a [string resource](/guide/topics/resources/string-resource#String)
   for your project ID. This allows your game to access the ID at build time.
   To create the resource, create the file
   `project_root/app/src/main/res/values/games-ids.xml`,
   and add the following:

   ```
   <?xml version="1.0" encoding="utf-8"?>
   <resources>
       <string name="game_services_project_id"
               translatable="false">add your Project ID here</string>
   </resources>
   ```
3. Build and test your game. If successful, when you launch your game, the game
   displays a sign-in prompt or a successful sign-in banner.

## Re-launch the sign-in prompt

If a player declines the initial Play Games Services sign-in prompt that is
automatically displayed when your game launches, they may change their mind
during the game session. You can re-launch the sign-in prompt by calling
`PgsGamesSignInClient_signIn` as long as no players are authenticated.

## Game server authorization

Once a player successfully authenticates to Play Games Services, your game
client can request a server authorization code that your backend game server can
use to securely communicate with Play Games Services. This allows your game
server to retrieve, update, and store data for the authenticated player. You can
retrieve the server authorization code by calling the
`PgsGamesSignInClient_requestServerSideAccess` function.

For more information, see the
[server access guide](/games/pgs/android/server-access).






Send feedback