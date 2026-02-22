---
title: https://developer.android.com/training/cars/testing/emulator/distant-display
url: https://developer.android.com/training/cars/testing/emulator/distant-display
source: md.txt
---

The distant display emulator can be used to emulate the multi-screen hardware found in some vehicles. Specifically, it emulates a device with a touch-enabled center screen and a non-touch dashboard screen. One example scenario for such a setup would be for a user to send a video app to the dashboard screen while continuing to use the center screen to look up a destination in a navigation app.
![The Automotive Distant Display emulator](https://developer.android.com/static/training/cars/images/dd.png)The Automotive Distant Display emulator.

## Move apps using the system UI

The primary way that users move apps to and from the distant display is using a system UI affordance. In the distant display emulator, this can be found in the status bar at the top of the screen.![](https://developer.android.com/static/training/cars/images/to_dd.png)is the button to send the app to the distant display and![](https://developer.android.com/static/training/cars/images/from_dd.png)is the button to return it to the main display. If your app is in immersive mode---that is, it's hidden the system bars---you'll need to reveal the status bar to show these controls.

## Move apps using adb

In addition to the system UI affordance, you can use the following adb commands to move apps to and from the distant display.  

    user_id=$(adb shell am get-current-user)
    adb shell am broadcast -a com.android.systemui.car.intent.action.MOVE_TASK --user $user_id --es move "to_dd"
    adb shell am broadcast -a com.android.systemui.car.intent.action.MOVE_TASK --user $user_id --es move "from_dd"

## Control media playback using adb

For apps that have[integrated with media session](https://developer.android.com/media/media3/session/control-playback), you can use the following command to control playback. For example, you can use this command to control playback of a video app while it's on the distant display.  

    adb shell cmd media_session dispatch <var translate="no">COMMAND</var>

| **Tip:** Run`adb shell cmd media_session`to see full usage information.