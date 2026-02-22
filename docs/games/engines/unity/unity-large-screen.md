---
title: https://developer.android.com/games/engines/unity/unity-large-screen
url: https://developer.android.com/games/engines/unity/unity-large-screen
source: md.txt
---

# Make your Unity game great on all form factors

In today's competitive gaming market, it's more important than ever to reach as wide an audience as possible. By developing games for different form factors, such as phones, tablets, foldables, and desktop, you can tap into a larger pool of potential players and increase your chances of success.

## Support screen resizability

To support different form factors, your game must be resizable. Resizability enables your game to support device configurations such as portrait and landscape orientation, multi-window mode, and folded and unfolded states of foldable devices.

If your game doesn't support all window size and orientation configurations, the platform letterboxes your game in[compatibility mode](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode)and, if necessary, prompts the player before changing to an unsupported configuration.
![](https://developer.android.com/static/images/games/multiplatform/configuration_compatibility_dialog.png)**Figure 1.**Configuration compatibility dialog.

For more information see[Support large screen resizability](https://developer.android.com/games/develop/multiplatform/support-large-screen-resizability).

### Multi-window mode

Your browser doesn't support the video tag.**Figure 2.**Different UIs on desktop and foldable in tabletop posture.

[Multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)enables multiple apps to share the same screen simultaneously. Apps can be side by side or one above the other (split-screen mode), one app in a small window overlaying other apps (picture-in-picture mode), or individual apps in separate movable, resizable windows (free-form mode).

To avoid getting into[compatibility mode](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode)when your game runs in multi-window mode, declare that your game is able to handle resizability by enabling the**Resizable Window** option in the[Unity build settings](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html).
![](https://docs.unity3d.com/uploads/Main/PlayerSetAndroidResPres.png)**Figure 3.**Unity's Resolution and Presentation settings for Android.

### Display cutouts

A[*display cutout*](https://developer.android.com/guide/topics/display-cutout)is an area on some devices that extends into the display surface. Cutouts allow for an edge-to-edge experience while providing space for important sensors on the front of the device.
![](https://developer.android.com/static/games/engines/unity/images/cutout-intro.png)**Figure 4.**Display cutout.

To bring an edge-to-edge experience to your game, configure the game to be safe-frame aware. Query the Unity[safeArea API](https://docs.unity3d.com/ScriptReference/Screen-safeArea.html)to get the safe area of the screen in pixels and adjust your game UI and UX accordingly, especially for the elements that users can interact with.

### Foldable postures

Foldable devices can be in various folded states, such as[`FLAT`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#FLAT())(fully open) or[`HALF_OPENED`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED())(somewhere between fully open and completely closed). When a device is in the`HALF_OPENED`state, two postures are possible, depending on the orientation of the fold: tabletop posture (horizontal fold) and book posture (vertical fold). Use tabletop posture to increase player immersion and engagement.
![](https://developer.android.com/static/images/games/multiplatform/foldable_posture_support.png)**Figure 5.**Game in tabletop posture with main view on vertical portion of display, controls on horizontal portion.

To implement tabletop posture,[extend the default Unity activity](https://docs.unity3d.com/2022.1/Documentation/Manual/AndroidUnityPlayerActivity.html)and then use the Jetpack WindowManager layout library to[make your game fold aware](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware).

## Unity sample project

The Unity sample project is based on the Unity 2D demonstration project[Lost Crypt](https://assetstore.unity.com/packages/essentials/tutorial-projects/lost-crypt-2d-sample-project-158673). The sample project demonstrates how to support large screen resizability in Unity. Large screen and foldable device support requires a number of changes to the Unity build options, as well as considerations in the layout of your camera and UI canvases.

The sample project is available to[download now](https://goo.gle/unity_ls_sample). The project contains four different scenes:

- **Original:**Support for basic resizable feature
- **Anchoring:**Same as "Original" scene, but adapts to various aspect ratios and avoids the display cutout
- **HingeAware:**Same as "Anchoring" scene, but supports tabletop posture
- **Mainmenu:**Starting scene, allows navigation to the other scenes and fully supports all device orientations, fold, unfold, and tabletop posture

When building for Android, select all the scenes and set the "Mainmenu" scene as the starting scene.
![](https://developer.android.com/static/games/engines/unity/images/mainmenu.png)**Figure 6.**"Mainmenu" scene lets you to navigate to the other scenes, in tabletop posture.

### Begin with resizable window support

Implement support for various displays sizes and aspect ratios in your Android large screen application to ensure your game or application displays correctly on different devices. Enable your game to resize and change aspect ratio by setting the**Resizable Window** property in the Unity build settings (see the["Multi-window mode"](https://developer.android.com/games/engines/unity/unity-large-screen#multi-window_mode)section). Adjust the camera and canvas aspect ratio to better fit different screens. View project settings in the**Build Settings** and in the`Plugins/Android/AndroidManifest.xml`file. Experience the full screen resizable feature in the project's "Original" scene.
![](https://developer.android.com/static/games/engines/unity/images/full_resizable.png)**Figure 7.**"Original" scene supports Resizable Window feature.

### Go full-screen immersive while handling display cutouts

Enable your game to use the entire screen to make gameplay immersive for an enhanced user experience. Update your game UI anchoring and camera settings to automatically adjust to the screen size. This allows UI elements to maintain their positions relative to the screen size.

The "Anchoring" scene uses the`CameraAspectLock`script to respond to device configuration changes by means of an[extended activity](https://docs.unity3d.com/2022.1/Documentation/Manual/AndroidUnityPlayerActivity.html)(see`Assets/Plugins/Android/LargeScreenPlayableActivity.java`). Unity's[safeArea API](https://docs.unity3d.com/ScriptReference/Screen-safeArea.html)is demonstrated in the`SafeZoneAPI`script, which binds to the`SafeZone`object inside the "Anchoring" scene.
![Game scene full screen on inner and outer displays of a foldable device.](https://developer.android.com/static/games/engines/unity/images/display_cutout.png)**Figure 8.**"Anchoring" scene with display cutout.

### Optimize for foldable devices

The last scene of the Unity sample project, "HingeAware", contains a`ConfigurationManager`object that responds to the different folding states of the target device through[Jetpack library APIs](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware)and an[extended activity](https://docs.unity3d.com/2022.1/Documentation/Manual/AndroidUnityPlayerActivity.html)(see`Assets/Plugins/Android/LargeScreenPlayableActivity.java`). The scene uses the`PanelOnFold`script to control the UI based on the fold status of the device, for example, showing the bottom controller panel when the device is in tabletop posture and adjusting the camera.
![](https://developer.android.com/static/games/engines/unity/images/table_top.png)**Figure 9.**"HingeAware" scene supports tabletop posture.