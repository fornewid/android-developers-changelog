---
title: Tier 3 — Adaptive ready  |  App quality  |  Android Developers
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [User experience](https://developer.android.com/quality/user-experience)

# Tier 3 — Adaptive ready Stay organized with collections Save and categorize content based on your preferences.



Apps that are Adaptive ready run full screen on all form factors and provide basic support for external input devices, enabling users to complete critical task flows on any device.

![Depiction of the three quality tiers as layers stacked vertically with the bottom tier highlighted.](/static/images/docs/quality-guidelines/tier-3/tier_3_header.png)

Adaptive ready apps must first fulfill the [core app quality](/docs/quality-guidelines/core-app-quality) requirements—in particular, the [User experience](/docs/quality-guidelines/core-app-quality#user_experience) requirements.

## Guidelines

Provide a stable and functional experience on all form factors.

### Configuration and continuity

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Config\_Changes | [T-Config\_Orientation](#T-Config_Orientation), [T-Config\_State](#T-Config_State) | App fills the available display area—the entire screen or, in multi-window mode, the app window. Content does not overflow the available display area. App is not [letterboxed](/guide/practices/enhanced-letterboxing); it does not run in [compatibility mode](/guide/topics/manifest/supports-screens-element#compat-mode).  App handles configuration changes and retains or restores its state as the device goes through configuration changes such as device rotation, folding and unfolding, and window resizing in split‑screen and desktop windowing modes, for example:   * Scroll position of scrollable fields is maintained * Text typed into text fields is retained and the keyboard state is restored * Media playback resumes where it left off when the configuration change was initiated |
| Config\_Combinations | [T-Config\_Combinations](#T-Config_Combinations) | App handles combinations of configuration changes, such as window resizing followed by device rotation, or rotation followed by device folding or unfolding. |

### Multi-window mode and multi-resume

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Multi-Window\_Functionality | [T-Multi-Window\_Functionality](#T-Multi-Window_Functionality) | App is fully functional in multi-window mode. See [Support multi-window mode](/develop/ui/compose/layouts/adaptive/support-multi-window-mode).  **Note:** Unity apps should be on Unity Long Term Support (LTS) version 2019 or later. See [Multi-window mode verification](/develop/ui/compose/layouts/adaptive/support-multi-window-mode#testing). |
| Multi-Resume | [T-Multi-Window\_Focus](#T-Multi-Window_Focus), [T-Multi-Window\_Resources](#T-Multi-Window_Resources) | App fully supports [multi-resume](/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-resume). App updates its UI (continues playing media, incorporates new messages, updates download progress, etc.) when the app is not the top focused app. In addition, the app handles the loss of exclusive resources such as cameras and microphones in multi-window scenarios. See [Activity lifecycle in multi-window mode](/develop/ui/compose/layouts/adaptive/support-multi-window-mode#lifecycle). |

### Camera preview and media projection

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Camera\_Preview | [T-Camera\_Preview](#T-Camera_Preview) | App provides camera preview in landscape and portrait orientations, folded and unfolded device states, and multi-window mode. Preview is properly proportioned and in the correct orientation. |
| Media\_Projection | [T-Media\_Projection](#T-Media_Projection) | App supports [media projection](/media/grow/media-projection) in landscape and portrait orientations, folded and unfolded device states, and multi-window mode. Projection is properly proportioned and in the correct orientation. |

### Keyboard, mouse, and trackpad

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Keyboard\_Input | [T-Keyboard\_Input](#T-Keyboard_Input) | App supports text input using external keyboard and switches between physical and virtual keyboards without relaunching the app when an external keyboard is connected or disconnected. |
| Mouse\_Trackpad\_Basic | [T-Mouse\_Trackpad\_Basic](#T-Mouse_Trackpad_Basic) | App supports basic mouse or trackpad interactions:   * Click: Any clickable element, including buttons, drop‑down menus, text entry fields, and navigation icons * Select: Any selectable element, including radio buttons, checkboxes, and text (by swiping or double clicking) * Scroll: Any scrollable element, such as lists and pickers, scrollable both vertically and horizontally |

### Stylus

| Guideline ID | Test IDs | Description |
| --- | --- | --- |
| Stylus\_Basic | [T-Stylus\_Basic](#T-Stylus_Basic) | App provides basic support for stylus‑equipped tablets, foldables, and desktop devices. The stylus can be used to select and manipulate UI elements, including scrolling through lists, pickers, and other scrollable content.  See [Stylus](/guide/topics/large-screens/input-compatibility-large-screens#stylus) in [Input compatibility on large screens](/guide/topics/large-screens/input-compatibility-large-screens).  **Note:** Basic stylus input is the same as touch input, which is fully supported by Android. Basic stylus input is automatically enabled for all apps with no special development required. |
| Stylus\_Text\_Input | [T-Stylus\_Text\_Input](#T-Stylus_Text_Input) | On Android 14 (API level 34) and higher, users can write and edit text in text input fields using a stylus. On ChromeOS M114 and higher, a stylus can be used to write and edit text in text input fields in [`WebView`](/reference/kotlin/android/webkit/WebView) components.  **Note:** On Android 14 and higher, [`EditText`](/reference/kotlin/android/widget/EditText) components support input using a stylus by default; no special development is required. On ChromeOS M114 and higher, `WebView` supports stylus input in text fields by default. |

## Tests

To confirm that your app is functional on all form factors, run the following tests.

### Configuration and continuity

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Config\_Orientation | [Config\_Changes](#Config_Changes) | Verify that the app is not [letterboxed](/guide/practices/enhanced-letterboxing) and is not running in [compatibility mode](/guide/topics/manifest/supports-screens-element#compat-mode) in portrait orientation, landscape orientation, multi-window mode, or when a large screen foldable device is unfolded in portrait or landscape orientation. Verify that all content fits within the available display space. Resize the app window in multi-window mode, including split-screen and desktop windowing modes. On desktop devices, minimize and restore the app window, maximize and restore the app window. Verify that the app assumes the proper orientation and maintains state in all window sizes.  **Note:** Test on a large screen device (sw >= 600 dp) running Android 12 (API level 31) or higher to ensure the device supports the following:   * All device orientations regardless of orientation restrictions set with the [`android:screenOrientation`](/guide/topics/manifest/activity-element#screen) app manifest element * Multi-window mode, even for apps that have specified [`android:resizeableActivity="false"`](/guide/topics/manifest/application-element#resizeableActivity) in the app manifest |
| T-Config\_State | [Config\_Changes](#Config_Changes) | From each app screen that has scrollable content, continuous playback content, or text entry fields, do the following:   * Scrollable content: Scroll the content * Playback content: Begin playback * Text entry fields: Enter text in multiple fields   Rotate the device between landscape and portrait orientations, fold and unfold the device (if applicable), and resize the app window in multi-window mode. Minimize and restore the app window on desktop devices; maximize and restore the app window. Verify the following:   * Scrollable content: The scroll position remains the same * Playback content: Playback resumes where it left off when the configuration change was initiated * Text entry fields: Previously entered text is retained in input fields |
| T-Config\_Combinations | [Config\_Combinations](#Config_Combinations) | From each app screen, perform combinations of rotating the device between landscape and portrait orientations, folding and unfolding the device (if applicable), and resizing the app window in multi-window mode. |

### Multi-window mode and multi-resume

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Multi-Window\_Functionality | [Multi-Window\_Functionality](#Multi-Window_Functionality) | Open the app in [multi-window mode](/develop/ui/compose/layouts/adaptive/support-multi-window-mode#split-screen_mode_activation). Check whether the app is fully functional in all window sizes, device orientations, and foldable device states. Resize the app window in each orientation. For foldable devices, fold and unfold the device in each orientation.  **Unity apps**  Open an app other than your Unity app. Go to the **Recents** screen. Select the app icon and put the app in split-screen mode. Open your Unity app, which should launch in split-screen mode beside or below the first app. Go to the **Home** screen to hide the pair of apps. Go to the **Recents** screen. Select the split-screen app pair that includes your Unity app. Verify that the Unity app resumes its activity and the app's layout in the split-screen window is correct with all UI elements accessible. |
| T-Multi-Window\_Focus | [Multi-Resume](#Multi-Resume) | Open the app and initiate a process, such as playing a video, that continuously updates the app. Open another app and make the new app the top focused app. Verify that the non-focused app continues to update its content (for example, a video continues to play). |
| T-Multi-Window\_Resources | [Multi-Resume](#Multi-Resume) | In the app, open the camera or use the microphone. Open another app, and make the new app the top focused app. Verify that the non-focused app has relinquished the camera or mic. Make the original app the top focused app. Verify that the app has regained access to the camera or mic. |

### Camera preview and media projection

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Camera\_Preview | [Camera\_Preview](#Camera_Preview) | Open the app full screen and in multi-window mode. Start the camera from within the app. Rotate the device between landscape and portrait orientations. For foldable devices, fold and unfold the device in each orientation. In multi-window mode, resize the app window. Verify that the camera preview is in the proper orientation and proportions in all device states and window sizes. |
| T-Media\_Projection | [Media\_Projection](#Media_Projection) | Open the app full screen and in multi-window mode. Start a media projection. Rotate the device between landscape and portrait orientations. For foldable devices, fold and unfold the device in each orientation. In multi-window mode, resize the app window. Verify that the media projection is in the proper orientation and proportions in all device states and window sizes. |

### Keyboard, mouse, and trackpad

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Keyboard\_Input | [Keyboard\_Input](#Keyboard_Input) | For each app screen that has text entry fields, connect an external keyboard to the device and enter text with the external keyboard and the virtual keyboard. Disconnect the external keyboard and enter text with the virtual keyboard. |
| T-Mouse\_Trackpad\_Basic | [Mouse\_Trackpad\_Basic](#Mouse_Trackpad_Basic) | For each app screen, connect a mouse and trackpad to the device. Perform basic mouse and trackpad interactions:   * Click all clickable elements such as buttons, drop‑down menus, and text entry fields. * Select radio buttons and checkboxes. Select text by swiping and double clicking. * Scroll vertically and horizontally (if applicable) through lists, pickers, and other scrollable UI elements. |

### Stylus

| Test ID | Guideline IDs | Description |
| --- | --- | --- |
| T-Stylus\_Basic | [Stylus\_Basic](#Stylus_Basic) | Using a stylus, navigate through the app, select UI elements, scroll through lists and pickers, and generally interact with the app. |
| T-Stylus\_Text\_Input | [Stylus\_Text\_Input](#Stylus_Text_Input) | On Android 14 (API level 34) and higher, enter and edit text in text input fields using a stylus. The software keyboard shouldn't appear. On ChromeOS M114 or higher, enter and edit text in text input fields in a [`WebView`](/reference/kotlin/android/webkit/WebView). |