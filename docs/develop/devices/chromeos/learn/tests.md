---
title: https://developer.android.com/develop/devices/chromeos/learn/tests
url: https://developer.android.com/develop/devices/chromeos/learn/tests
source: md.txt
---

The following table includes a set of test cases you can use in your
test plan. The test cases cover a wide array of common scenarios that Android
apps can experience when running on ChromeOS devices.

| Test type | Test case | App scenario | Success case |
|---|---|---|---|
|   | Find app in Play Store | All | App exists in Play Store, accessed from a Chromebook (no issue if working as intended). **NOTE:** [Flags in your manifest](https://developer.android.com/guide/topics/manifest/uses-feature-element) can cause the app to be unavailable, depending on the hardware in the ChromeOS device. This test is best run on clamshell devices, as they most accurately represent the hardware profile of most devices. |
|   | Install app | All | App installs on the Chromebook with no issues. |
|   | Clamshell: Launch app | All | App opens without crashing, not responding, or throwing ANR (app not responding). App content is upright. |
| Window Management | Clamshell: Resize window | All | If the window resize button is available, resize the window. App doesn't crash, stop responding, or ANR. App content scales. Try this in various pages of the app. The active cursor stays in place and page content doesn't change, except to adjust to larger screen layout. |
| Window Management | Clamshell: Free-form resizing | All | Try dragging the corner of the window to resize the window. App doesn't crash, stop responding, or ANR. App content scales. Try this in various pages of the app. The active cursor stays in place and page content doesn't change, except to adjust to larger screen layout. |
| Window Management | Clamshell: Reopen app | All | If the window resize button is available, resize the window and close the app, then reopen. App launches with the same window size and orientation it had when it was closed. |
| Window Management | Clamshell: Minimize and restore | All | Minimize and restore the app. App doesn't crash, stop responding, or ANR, and content reappears unchanged. |
| Window Management | Clamshell: Fullscreen app | All | The full-screen key on the ChromeOS keyboard puts the app in full screen, with no top bar. App doesn't crash, stop responding, or ANR. App content scales. |
| Mouse + Trackpad | Clamshell: Trackpad click | All | Use trackpad to click a touch control. App responds like there's a touch in that location, with no lag. |
| Mouse + Trackpad | Clamshell: Trackpad right-click | All | Use trackpad to right-click (two-finger tap) a touch control. App responds like there's a touch in that location, with no lag. |
| Mouse + Trackpad | Clamshell: Trackpad scroll | All | In a scrollable area of the app, like a list, use two-finger scroll action on trackpad. App content scrolls. |
| Mouse + Trackpad | Clamshell: Trackpad zoom | All | In a zoomable area of the app, like an image or a map, use the trackpad to zoom. App content zooms. |
| Mouse + Trackpad | Clamshell: Mouse click | All | Using a mouse device, click a touch control. App responds like there's a touch in that location, with no lag. |
| Mouse + Trackpad | Clamshell: Mouse right-click | All | Using a mouse device, right-click a touch control. App responds likes there's a touch in that location, with no lag. |
| Mouse + Trackpad | Clamshell: Mouse scroll | All | In a scrollable area of the app, like a list, use the scroll wheel. App content scrolls. |
| Mouse + Trackpad | Clamshell: Mouse scroll to zoom | All | In a zoomable area of the app, such as an image or a map, use the scroll wheel. App content zooms. |
| Mouse + Trackpad | Clamshell: Touchscreen click | All | Using your finger, push on a touch control. App responds like there's a touch in that location, with no lag. |
| Mouse + Trackpad | Clamshell: Touchscreen right-click | All | Using your finger, touch \& hold a touch control. App responds like there's a touch in that location, with no lag. |
| Mouse + Trackpad | Clamshell: Touchscreen scroll | All | In a scrollable area of the app, like a list, use the one- or two-finger scroll action. App content scrolls. |
| Mouse + Trackpad | Clamshell: Touchscreen zoom | All | In a zoomable area of the app, such as an image or a map, use fingers to zoom on touchscreen. App content zooms. |
| Stylus | Clamshell: Stylus click | All | Using a stylus, click a touch control. App responds like there's a touch in that location, with no lag. |
| Stylus | Clamshell: Stylus scroll | All | In a scrollable area of the app, such as a list, use the stylus swipe or scroll action. App content scrolls. |
| Input | Clamshell: Physical keyboard | All | While in clamshell mode, click a text input box and type text with the keyboard. Onscreen keyboard doesn't show. Typed text shows in the input box with no lag. |
|   | Buy in-app content | IAP enabled | While signed in, try to purchase some in-app content. Content appears in app as appropriate. Purchase appears in Play purchase history. |
|   | Suspend/resume | All | While app is running, close Chromebook. After 5-10 seconds, reopen Chromebook. App connects back in the same state. |
|   | Wi-Fi connectivity | All | Turn the Wi-Fi off. The app complains about lack of internet connection. Turn Wi-Fi back on. The app connects back to internet and is functional. |
| Window Management | Transition between clamshell and touchview | All | Open app in clamshell mode, then change the device to touchview mode. The window size and orientation update as expected. |
|   | Touchview: Launch app | All | App opens without crashing, not responding, or throwing ANR. App content is upright. Try this in portrait and landscape modes. |
| Window Management | Touchview: Resize window | All | If the window resize button is available, resize the window. App doesn't crash, stop responding, or ANR. App content scales. Try this in various pages of the app. The active cursor stays in place and page content doesn't change, except to adjust to larger screen layout. Try this in portrait and landscape modes. |
| Window Management | Touchview: Reopen app | All | If the window resize button is available, resize the window and close the app, then reopen. App launches with the same window size and orientation it had when it was closed. Try this in portrait and landscape modes. |
| Window Management | Touchview: Minimize and restore | All | Minimize and restore the app. App doesn't crash, stop responding, or ANR, and content reappears unchanged. |
| Window Management | Touchview: Rotate device | All | While in tablet mode, rotate the device 90 degrees. App either doesn't rotate OR it does rotate and window and content resize appropriately. The active cursor or page stays in place. |
| Input | Touchview: Touchscreen click | All | Using your finger, push on a touch control. App responds like there's a touch in that location, with no lag. |
| Input | Touchview: Touchscreen right-click | All | Using your finger, touch \& hold on a touch control. App responds like there's a touch in that location, with no lag. |
| Input | Touchview: Touchscreen scroll | All | In a scrollable area of the app, like a list, use the one- or two-finger scroll action. App content scrolls. |
| Input | Touchview: Touchscreen zoom | All | In a zoomable area of the app, such as an image or a map, use fingers to zoom content. App content zooms. |
| Input | Touchview: Stylus click | All | Using a stylus, click a touch control. App responds like there's a touch in that location, with no lag. |
| Input | Touchview: Stylus scroll | All | In a scrollable area of the app, like a list, use the stylus swipe or scroll action. App content scrolls. |
| Input | Touchview: Virtual keyboard | All | While in tablet mode, tap an area in the app that takes text input and type text. Onscreen keyboard and text show as expected. Try this in portrait and landscape modes as well as the transitions between them. |
| Camera | Touchview: Take photo | Communication | App opens the camera and the preview images are scaled and oriented correctly. The resulting picture taken is scaled and oriented correctly. Try this in portrait and landscape modes. |
|   | Touchview: Record video | Communication | App opens the camera and the preview images are scaled and oriented correctly. Starting the recording, the preview is scaled and oriented correctly. Playback is smooth and performs as expected, with no lag in audio or video, and the video is at its recorded speed. Try this in portrait and landscape modes. |
| Window Management | Touchview: Change orientation while camera is on | Communication | Open the app's camera. Rotate the device 90 degrees. App doesn't crash, stop responding, or ANR. App either doesn't rotate OR it does rotate and window and content resize appropriately. |
|   | Create content | Content creation | Output, like drawing, text, or audio, records in the app as expected, with no lags. |
|   | Save content | Content creation | App saves the content, either locally or in the cloud, and content is recreated faithfully when reopened. |
|   | Share content |   | App shares content with third party. Third party can receive and open content. |
|   | 1:1 communication | Communication | Send one of every possible message type to another user, like an email, text message, phone call, or video call. Verify transmission. |
|   | 1:many communication | Communication | Post one of every possible post type to a group, like a newsfeed post, forum post, or chat group. Verify transmission. |
| Camera | Clamshell: Take photo | Communication | App opens the camera and the preview images are scaled and oriented correctly. The resulting picture taken is scaled and oriented correctly. |
| Camera | Clamshell: Record video | Communication | App opens the camera and the preview images are scaled and oriented correctly. Starting the recording, the preview is scaled and oriented correctly. Playback is smooth and performs as expected, with no lag in audio or video, and the video is at its recorded speed. |
| Camera | Clamshell: Camera retries after app resumes | Communication | Open the app's camera. Close the lid of the device. Open the lid of the device. App continues to let the user take a photo or lets the user retry taking a photo without restarting the app. |
| Input | Touch to draw | Drawing or Handwriting | Use a finger to input drawing strokes into the app. Strokes appear on canvas as expected, with no lag. |
| Stylus | Stylus to draw | Drawing or Handwriting | Use the stylus to input drawing strokes into the app. Strokes appear on canvas as expected, with no lag. |
|   | Video playback | Communication or Social \& Media | Play a video within the app. The playback is smooth with no lags. Sound is clear. |
|   | Sound volume | Communication or Social \& Media | If the app has volume controls, try changing the volume while media with sound plays. The volume adjusts accordingly. |
|   | Tilt motion | Games | Tilt the device while playing a motion-sensing game. App responds accordingly. |
|   | Location finding | Weather or Maps or Navigation | App finds the general location of the user, even without GPS hardware. |
|   | Other app-specific functionality not captured | All | Use this only if one of the preceding actions test cases doesn't fit. |
| UI | Large screen layout | All | If the app's UI takes advantage of the extra real estate of the screen, content takes up the full width of the screen on the device, or content is appropriately sized. |
| Mouse + Trackpad | Clamshell: Trackpad drag | All | Drop a piece of content, like an image, into an area of the app where this might make sense using trackpad. The dropped object executes. |
| Mouse + Trackpad | Clamshell: Mouse drag | All | Using a mouse, drop a piece of content, like an image, into an area of the app where this might make sense. The dropped object executes. |
| Input | Clamshell: Touchscreen drag | All | Using your finger, drop a piece of content, like an image, into an area of the app where this might make sense. The dropped object executes. |
| Stylus | Clamshell: Stylus drag | All | Using the stylus, drop a piece of content, like an image, into an area of the app where this might make sense. The dropped object executes. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: arrow | All | The arrow keys on the ChromeOS keyboard work as expected within the app. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: <kbd>Tab</kbd> | All | The <kbd>Tab</kbd> key on the ChromeOS keyboard works as expected. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: Cut and copy | All | In a text input box, such as a message input or high-score name, select some existing text. Cut with <kbd>Control</kbd>+<kbd>X</kbd>. Paste into another app with <kbd>Control</kbd>+<kbd>V</kbd>. Retest with <kbd>Control</kbd>+<kbd>C</kbd> instead of <kbd>Control</kbd>+<kbd>X</kbd>. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: <kbd>Escape</kbd> key | All | The <kbd>Escape</kbd> key corresponds to closing the active window or going back to the previous page. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: <kbd>Enter</kbd> key | All | Pressing <kbd>Enter</kbd> triggers the selected button, and pressing <kbd>Enter</kbd> while editing an input field in a form with multiple fields submits the form. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: <kbd>Enter</kbd> to send | All | In a text input box, like a message input or high-score name, input some text, then press <kbd>Enter</kbd>. The text submits to the app. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: App hot keys | All | Try pressing any commonly used keyboard shortcuts for the app. App responds as expected. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: Back | All | The back key on the ChromeOS keyboard works like the back button on Android. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: Refresh | All | In an area of the app with live or perishable content, the refresh key on the ChromeOS keyboard refreshes the view. |
| Keyboard Shortcuts + Nav | Clamshell: Special keys: Dock window | All | Use <kbd>Alt</kbd>+<kbd>[</kbd> or <kbd>Alt</kbd>+<kbd>]</kbd> to dock the app to one side of the screen. App docks, similar to the behavior of the Chrome browser. |
| Desktop Functionality | Offline mode | All | Turn the Wi-Fi off from the settings menu. Try to use a feature of the app that is available offline. The offline feature is functional. |
| Input | Touchview: Touchscreen drag | All | Using your finger, drop a piece of content, like an image, into an area of the app where this might make sense. The dropped object executes. |
| Stylus | Touchview: Stylus drag | All | Using the stylus, drop a piece of content, like an image, into an area of the app where this might make sense. The dropped object executes. |
| Stylus | Stylus pressure | Drawing or Handwriting | Use the stylus to input drawing strokes or erase drawing strokes using various pressures. Strokes appear on canvas with variable weight as expected. |
| Stylus | Stylus erase | Drawing or Handwriting | Select the erase option and use the stylus to erase parts of a drawing. Markings disappears as expected. This is important for drawing apps; note-taking apps are typically exempt from this. |
| Stylus | Stylus only (reject finger) | Drawing or Handwriting | Select the option to be in stylus-only mode. Try drawing using the stylus and then using the finger. The canvas has markings when using the stylus, and not when using the finger. |
| Stylus | Stylus touch cancel | Drawing or Handwriting | While using stylus to draw, place palm against the touchscreen. No additional markings appear on the canvas (called "palm rejection"). |
| Desktop Functionality | Multitasking function | Background apps | Open app, engage function, and open any other app. App continues background function, such as background audio or a stopwatch. |