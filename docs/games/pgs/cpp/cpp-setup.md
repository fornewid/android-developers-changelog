---
title: https://developer.android.com/games/pgs/cpp/cpp-setup
url: https://developer.android.com/games/pgs/cpp/cpp-setup
source: md.txt
---

This document helps you set up your C++ project for
v2 Native C or C++ and verify the authentication service.

## Before you start

You must [set up Play Games Services](https://developer.android.com/games/pgs/console/setup) in
Google Play Console.

### App prerequisites

Make sure that your app's build file uses the following values:

- A `minSdkVersion` of `19` or higher
- A `compileSdkVersion` of `28` or higher

## Set up your game project

Complete the following steps to set up your game project.

### Update build.gradle

In your app-level `build.gradle` file, do the following:

- Make sure the [prefab](https://developer.android.com/reference/tools/gradle-api/4.1/com/android/build/api/dsl/BuildFeatures#prefab) build feature is enabled.

- Add the dependency for the v2 Native SDK (beta):

  - `com.google.android.gms:play-services-games-v2-native-c:21.0.0-beta1`

Here's an example:

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

### Update CMakeLists.txt

In your `CMakeLists.txt` file, add the following code:

      find_package(com.google.android.gms.games.v2.c REQUIRED CONFIG)

      // link games_static for -DANDROID_STL=c++_static or default
      // link games_shared for -DANDROID_STL=c++_shared
      target_link_libraries(
        app PUBLIC com.google.android.gms.games.v2.c::games_static)

### Update AndroidManifest.xml

1. To define your Play Games Services project ID in your `AndroidManifest.xml`
   file, add the following lines:

       <manifest>
         <application>
           <meta-data android:name="com.google.android.gms.games.APP_ID"
                      android:value="@string/game_services_project_id"/>
         </application>
       </manifest>

2. Create a [string resource](https://developer.android.com/guide/topics/resources/string-resource#String)
   for your project ID. This allows your game to access the ID at build time.
   To create the resource, create the file
   `project_root/app/src/main/res/values/games-ids.xml`,
   and add the following:

       <?xml version="1.0" encoding="utf-8"?>
       <resources>
           <string name="game_services_project_id"
                   translatable="false">add your Project ID here</string>
       </resources>

3. Build and test your game. If successful, when you launch your game, the game
   displays a sign-in prompt or a successful sign-in banner.

## Get the player ID

Your game can access player information for an authenticated player by
retrieving their player ID. You can retrieve a player ID by calling the
`GetPlayerId` function, as demonstrated in the following example.

> [!NOTE]
> **Note:** For more information about how Player IDs work, see [Next-generation player IDs](https://developer.android.com/games/pgs/next-gen-player-ids).

    #include <assert.h>
    #include "gni/gni.h"
    #include "gni/gni_task.h"
    #include "pgs/pgs_play_games.h"
    #include "pgs/pgs_players_client.h"

    // A callback for a GniTask returned from PgsPlayersClient_getCurrentPlayerId.
    void OnGetCurrentPlayerIdCompleteCallback(GniTask *task, void *user_data) {

       if (!GniTask_isSuccessful(task)) {
          const char *error_message = nullptr;
          GniTask_getErrorMessage(task, &error_message);

          // Log error message here.

          GniString_destroy(error_message);
          GniTask_destroy(task);
          return;
       }

       const char *result = nullptr;
       PgsPlayersClient_getCurrentPlayerId_getResult(task, &result);

       // Log player ID here.

       GniString_destroy(result);
       GniTask_destroy(task);
    }

    // Gets the player ID.
    void GetPlayerId(jobject main_activity) {
       static const PgsPlayersClient *players_client =
               PgsPlayGames_getPlayersClient(main_activity);

       GniTask *get_current_player_id_task =
               PgsPlayersClient_getCurrentPlayerId(players_client);
       assert(get_current_player_id_task != nullptr);
       GniTask_addOnCompleteCallback(get_current_player_id_task,
                                     OnGetCurrentPlayerIdCompleteCallback,
                                     nullptr);
    }

    // Entry point for our test app
    void TestPGSNative(JNIEnv *env, jobject main_activity) {
       JavaVM *java_vm;
       env->GetJavaVM(&java_vm);

       GniCore_init(java_vm, main_activity);

       GetPlayerId(main_activity);
    }

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
[server access guide](https://developer.android.com/games/pgs/android/server-access).