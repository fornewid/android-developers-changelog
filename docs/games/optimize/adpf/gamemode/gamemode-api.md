---
title: https://developer.android.com/games/optimize/adpf/gamemode/gamemode-api
url: https://developer.android.com/games/optimize/adpf/gamemode/gamemode-api
source: md.txt
---

The Game Mode API allows you to optimize your game for the best performance or
longest battery life when the user selects the corresponding game mode.

Alternatively, you can submit requests for
[Game Mode interventions](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-interventions) to improve
the performance of games that are no longer being updated by developers.

The Game Mode API and interventions are available on:

- Select [Android 12](https://developer.android.com/about/versions/12/get) devices
- Devices running [Android 13](https://developer.android.com/about/versions/13/get) or higher

Each game may implement the Game Mode API behavior, propose Game Mode
interventions settings to OEMs, or
[opt out of Game Mode interventions](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-interventions#opt-out_from_interventions).

> [!WARNING]
> **Warning:** OEMs may choose to implement Game Mode interventions without developer feedback.

## Setup

To use the Game Mode API in your game, do the following:

1. Download and install the
   [Android 13 SDK](https://developer.android.com/about/versions/13/setup-sdk).

2. In the [`AndroidManifest.xml`](https://developer.android.com/guide/topics/manifest/manifest-intro) file,
   declare your app as a game by setting the
   [`appCategory`](https://developer.android.com/reference/android/R.attr#appCategory) attribute in the
   [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element:

    android:appCategory="game"

1. Query the current game mode by adding this to your main activity:

### Java

    // Only call this for Android 12 and higher devices
    if ( Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ) {
      // Get GameManager from SystemService
      GameManager gameManager = Context.getSystemService(GameManager.class);

      // Returns the selected GameMode
      int gameMode = gameManager.getGameMode();
    }

### Kotlin

    // Only call this for Android 12 and higher devices
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
      // Get GameManager from SystemService
      val gameManager: GameManager? = context.getSystemService(Context.GAME_SERVICE) as GameManager?

      // Returns the selected GameMode
      val gameMode = gameManager?.gameMode
    }

| Supported game mode | Description |
|---|---|
| UNSUPPORTED | The game does not declare support for the Game Mode API and it does not support Game Mode interventions. |
| STANDARD | The user has not selected a game mode or the user selected standard mode. |
| PERFORMANCE | Provides the lowest latency frame rates in exchange for reduced battery life and fidelity. |
| BATTERY | Provides the longest possible battery life in exchange for reduced fidelity or frame rates. |

> [!IMPORTANT]
> **Important:** Battery Saver mode is game-specific and does not impact system level Android Battery Saver behavior.

1. Add code to query the game mode state in the
   [`onResume`](https://developer.android.com/reference/android/app/Activity#onResume()) function:

   ![Example with user setting Battery mode](https://developer.android.com/static/games/optimize/adpf/gamemode/images/set-battery-flow.png)

> [!IMPORTANT]
> **Important:** Your app must always query the `getGameMode()` method when resuming a paused process. See the diagram above for details.

### Best Practices

If your game already supports multiple fidelity and frame rate
targets, you should identify the appropriate settings for performance and
battery saver modes:

- To consistently achieve the maximum device frame rates: consider slight
  reductions in fidelity to achieve higher frame rates.

- To improve battery life: consider choosing a lower display refresh rate (e.g.
  30Hz or 60Hz) and [use frame pacing](https://developer.android.com/games/sdk/frame-pacing) to target the
  reduced rate.

For high-fidelity games such as first-person shooters, multiplayer online
battle arenas (MOBAs), and role-playing games (RPGs), you should focus on
achieving high consistent frame rates to maximize user immersion.

For both high-fidelity and casual games, you should support battery saver mode
to lengthen playtime by reducing your peak frame rates.

## Declare support for Game Modes

To declare support for Game Modes and override any Game Mode interventions by
OEMs, first add the Game Mode configuration to the
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element in your
`AndroidManifest.xml` file:

    <application>
        <meta-data android:name="android.game_mode_config"
                   android:resource="@xml/game_mode_config" />
      ...
    </application>

Then create a `game_mode_config.xml` file in your project's `res/xml/` directory
with the following contents:

    <?xml version="1.0" encoding="UTF-8"?>
    <game-mode-config
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:supportsBatteryGameMode="true"
        android:supportsPerformanceGameMode="true"
    />

> [!IMPORTANT]
> **Important:** If your game declares support for a Game Mode, the game must implement its own optimization. As a result, the platform resets any previously applied Game Mode interventions by OEMs.

## Switch Game Modes

To switch between the game modes, you can use the Game Dashboard (available on
Pixel devices) or similar applications provided by OEMs. Alternatively you can
use the Game Mode shell command during development.

If you are using Game Dashboard and the **optimisation** icon does not display
when your game launches, you may need to upload your app to Google Play Console
and install it through the Play Store. For information about app testing in the
Play Store, see
[Share app bundles and APKs internally](https://support.google.com/googleplay/android-developer/answer/9844679).

![Game Dashboard Activity!](https://developer.android.com/static/images/games/game-mode/gamedashboardactivity.png "Game Dashboard Activity")
**Figure 1.** Game Dashboard shown overlaying the running game on a Pixel
device.

In figure 1, the running game's Game Mode can be changed from the Optimisation
widget. As shown on the widget, the game is currently running on
[`PERFORMANCE`](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_PERFORMANCE)
mode.

During development, if you are using a device without Game Dashboard and the
manufacturer does not provide any way to set Game Mode for each app, you can
change the Game Mode status through [adb](https://developer.android.com/studio/command-line/adb):

    adb shell cmd game mode [standard|performance|battery] <PACKAGE_NAME>

## Sample Application

The [Game Mode API sample](https://github.com/android/games-samples/tree/main/agdk/game_mode)
highlights how you can optimize FPS and render resolution caps to save approximately 25% power in your apps.

## Next

Read [Game Mode Interventions](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-interventions)
to improve a game's performance when it isn't possible to provide game updates.