---
title: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality
source: md.txt
---

Devices that can run Android apps come in a variety of form
factors---phones, tablets, foldables, desktops, car displays, TVs,
XR---which represent a wide range of display sizes. Android supports
multiple display modes, including multi-window, multi-display, multi-instance,
and picture-in-picture. Foldable devices can be in various folded states, or
postures, such as tabletop posture or book posture.

![Depiction of the three quality tiers as layers stacked vertically.](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/quality_guidelines_header.png)

To ensure your app provides a great user experience regardless of device form
factor, screen size, display mode, or posture, follow the adaptive app
compatibility [checklists](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#adaptive_app_compatibility_checklists) and complete
the compatibility [tests](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#adaptive_app_compatibility_tests).

The checklists and tests define a comprehensive set of quality requirements for
most types of Android apps. Your app probably doesn't need to meet all of the
requirements. Implement the ones that make sense for your app's use cases.

The adaptive app quality guidelines replace and extend the guidance formerly
provided in the
[large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/archive/adaptive/large-screen-app-quality).

As you enhance your app with adaptive capabilities, help users better understand
your app's multi-form-factor experience by updating your app listing on Google
Play. Upload screenshots that show off the app on tablets and foldables. Call
attention to XR features in your app description. For more information and best
practices, see [Google Play Help](https://support.google.com/googleplay/android-developer/answer/9866151).

For examples of optimized and differentiated layouts on screens of all sizes,
see the [adaptive layout gallery](https://developer.android.com/large-screens/gallery).

## Adaptive app compatibility checklists

The compatibility checklists define criteria to help you assess the level of
support your app provides for adaptive design.

Levels of support include the following:

![Icon for Tier 3 Adaptive Ready](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.svg)

### TIER 3 (basic) --- Adaptive ready

Your app runs full screen (or full window in multi-window mode) on all devices,
but app layout might not be ideal. The app is not letterboxed; it does not run
in compatibility mode. Users can complete critical task flows but with a less
than optimal user experience. The app provides basic support for external input
devices, including keyboard, mouse, trackpad, and stylus.

![Icon for Tier 2 Adaptive Optimized](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-2/tier_2_icon.svg)

### TIER 2 (better) --- Adaptive optimized

Your app implements layout optimizations for all screen sizes and device
configurations along with enhanced support for external input devices.

![Icon for Tier 1 Adaptive Differentiated](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_icon.svg)

### TIER 1 (best) --- Adaptive differentiated

Your app provides a user experience designed for the device or display the app
is running on. Where applicable, the app supports multitasking, foldable
postures, drag and drop, and stylus input.

Complete the Tier 2 requirements to enable your app to provide an excellent user
experience on all Android devices. To make your app outstanding on foldables and
large screens such as desktops, complete Tier 1.

*** ** * ** ***

![Icon for Tier 3 Adaptive Ready](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.svg)

TIER 3

### Adaptive ready

Adaptive ready apps must first fulfill the [core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) requirements---in particular, the [User experience](https://developer.android.com/docs/quality-guidelines/core-app-quality#user_experience) requirements.

Apps must meet the following adaptive requirements:

| ID | Tests | Description |
|---|---|---|
| Configuration and continuity |||
| Config:Changes | [T-Config:Orientation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Config:Orientation), [T-Config:State](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Config:State) | App fills the available display area---the entire screen or, in multi-window mode, the app window. App is not [letterboxed](https://developer.android.com/guide/practices/enhanced-letterboxing); it does not run in [compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode). App handles configuration changes and retains or restores its state as the device goes through configuration changes such as device rotation, folding and unfolding, and window resizing in split‑screen and desktop windowing modes, for example: - Scroll position of scrollable fields is maintained - Text typed into text fields is retained and the keyboard state is restored - Media playback resumes where it left off when the configuration change was initiated |
| Config:Combinations | [T-Config:Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Config:Combinations) | App handles combinations of configuration changes, such as window resizing followed by device rotation, or rotation followed by device folding or unfolding. |
| Multi-window mode and multi‑resume |||
| Multi-Window:Functionality | [T-Multi-Window:Functionality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multi-Window:Functionality) | App is fully functional in multi-window mode. See [Support multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode). **Note:** Unity apps should be on Unity Long Term Support (LTS) version 2019 or later. See [Multi-window mode verification](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#testing). |
| Multi-Window:Multi-Resume | [T-Multi-Window:Focus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multi-Window:Focus), [T-Multi-Window:Resources](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multi-Window:Resources) | App fully supports [multi-resume](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-resume). App updates its UI (continues playing media, incorporates new messages, updates download progress, etc.) when the app is not the top focused app. In addition, the app handles the loss of exclusive resources such as cameras and microphones in multi-window scenarios. See [Activity lifecycle in multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#lifecycle). |
| Camera preview and media projection |||
| Media:Camera_Preview | [T-Media:Camera_Preview](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Media:Camera_Preview) | App provides camera preview in landscape and portrait orientations, folded and unfolded device states, and multi-window mode. Preview is properly proportioned and in the correct orientation. |
| Media:Projection | [T-Media:Projection](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Media:Projection) | App supports [media projection](https://developer.android.com/media/grow/media-projection) in landscape and portrait orientations, folded and unfolded device states, and multi-window mode. Projection is properly proportioned and in the correct orientation. |
| Keyboard, mouse, and trackpad |||
| Input:Keyboard | [T-Input:Keyboard](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Keyboard) | App supports text input using external keyboard and switches between physical and virtual keyboards without relaunching the app when an external keyboard is connected or disconnected. |
| Input:Mouse_Trackpad | [T-Input:Mouse_Trackpad](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Mouse_Trackpad) | App supports basic mouse or trackpad interactions: - Click: Any clickable element, including buttons, drop‑down menus, text entry fields, and navigation icons - Select: Any selectable element, including radio buttons, checkboxes, and text (by swiping or double clicking) - Scroll: Any scrollable element, such as lists and pickers, scrollable both vertically and horizontally |
| Stylus |||
| Stylus:Basic | [T-Stylus:Basic](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Stylus:Basic) | App provides basic support for stylus‑equipped tablets, foldables, and desktop devices. The stylus can be used to select and manipulate UI elements, including scrolling through lists, pickers, and other scrollable content. See [Stylus](https://developer.android.com/guide/topics/large-screens/input-compatibility-large-screens#stylus) in [Input compatibility on large screens](https://developer.android.com/guide/topics/large-screens/input-compatibility-large-screens). **Note:** Basic stylus input is the same as touch input, which is fully supported by Android. Basic stylus input is automatically enabled for all apps with no special development required. |
| Stylus:Text_Input | [T-Stylus:Text_Input](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Stylus:Text_Input) | On Android 14 (API level 34) and higher, users can write and edit text in text input fields using a stylus. On ChromeOS M114 and higher, a stylus can be used to write and edit text in text input fields in [`WebView`](https://developer.android.com/reference/kotlin/android/webkit/WebView) components. **Note:** On Android 14 and higher, [`EditText`](https://developer.android.com/reference/kotlin/android/widget/EditText) components support input using a stylus by default; no special development is required. On ChromeOS M114 and higher, `WebView` supports stylus input in text fields by default. |

![Icon for Tier 2 Adaptive Optimized](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-2/tier_2_icon.svg)

TIER 2

### Adaptive optimized

Optimized apps fully support all screen types and device states, including state
transitions.

| ID | Tests | Description |
|---|---|---|
| User interface |||
| UI:Layouts | [T-UI:Flow](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-UI:Flow) | App has responsive and adaptive layouts designed for all screen sizes. All layouts are responsive (see [Migrate your UI to responsive layouts](https://developer.android.com/guide/topics/large-screens/migrate-to-responsive-layouts)). Implementation of adaptive layouts is determined by [window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes). The app UI can include the following: - Leading‑edge navigation rails that expand on larger window sizes into full navigation panels - Grid layouts that scale the number of columns to accommodate window size changes - Columns of text on large screens - Trailing‑edge panels that are open by default on desktop screen sizes; closed, on smaller screens Create two-pane layouts (where appropriate) to take advantage of large screen space. See [Canonical layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts). [Activity embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding) enables activity-based apps to create multi‑pane layouts by displaying activities side by side. |
| UI:Elements | [T-UI:Flow](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-UI:Flow) | Modals, context menus, and other secondary elements are properly formatted on all screen types and device states, for example: - Bottom sheets are not full width on large screens. (Apply a maximum width to avoid stretching.) See [Behavior](https://material.io/components/sheets-bottom#behavior) in [Sheets: bottom](https://material.io/components/sheets-bottom). - Buttons are not full width on large screens. See [Behavior](https://material.io/components/buttons#behavior) in [Buttons](https://material.io/components/buttons). - Text fields and boxes don't stretch to full width on large screens. See [Behavior](https://material.io/components/text-fields#behavior) in [Text fields](https://material.io/components/text-fields). - Small edit menus or modals don't cover the entire screen and maintain context for the user as much as possible. See [Menus](https://material.io/components/menus). - Context menus appear next to the item the user selected. See the "Context menus" topic in [Menus](https://m3.material.io/components/menus/guidelines). - Navigation rails replace navigation bars for better ergonomics on large screens. Rails can also complement other navigation components, such as navigation bars. See [Navigation rail](https://material.io/components/navigation-rail). - Navigation drawers are updated to the latest material component. See [Navigation drawer](https://material.io/components/navigation-drawer). - Dialog boxes are updated to the latest material component. See [Dialogs](https://material.io/components/dialogs). - Images are displayed at a proper resolution and are not stretched or cropped. |
| UI:Touch_Targets | [T-UI:Touch_Targets](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-UI:Touch_Targets) | Touch targets are least 48dp. See the Material Design [Layout and typography](https://material.io/design/usability/accessibility.html#layout-and-typography) guidelines. |
| UI:Focus | [T-UI:Focus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-UI:Focus) | A focused state is created for custom drawables that are interactive. A custom drawable is any visual UI element not provided by the Android framework. If users can interact with a custom drawable, the drawable must be focusable when the device is not in [Touch Mode](https://developer.android.com/reference/kotlin/android/view/View#touch-mode), and a visual indication of the focused state must be apparent. |
| Keyboard, mouse, and trackpad |||
| Input:Keyboard_Navigation | [T-Input:Keyboard_Navigation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Keyboard_Navigation) | The main task flows in the app support keyboard navigation, including <kbd>Tab</kbd> and arrow key navigation. See [Build more accessible apps](https://developer.android.com/guide/topics/ui/accessibility). |
| Input:Keyboard_Shortcuts | [T-Input:Keyboard_Shortcuts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Keyboard_Shortcuts) | App supports keyboard shortcuts for commonly used actions such as select, cut, copy, paste, undo, and redo. See [Input compatibility](https://chromeos.dev/en/android/input-compatibility). |
| Input:Keyboard_Playback | [T-Input:Keyboard_Playback](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Keyboard_Playback) | Keyboard can be used to control media playback; for example, the <kbd>Spacebar</kbd> plays and pauses media. |
| Input:Keyboard_Send | [T-Input:Keyboard_Send](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Keyboard_Send) | Keyboard <kbd>Enter</kbd> key performs a *send* function in communication apps. |
| Input:Context_Menus | [T-Input:Context_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Context_Menus) | Context menus are accessible by typical mouse and trackpad right‑click (secondary mouse button or secondary tap) behavior. |
| Input:Zoom | [T-Input:Zoom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Zoom) | App content can be zoomed using the mouse scroll wheel (in conjunction with pressing the <kbd>Control</kbd>, or <kbd>Ctrl</kbd>, key) and trackpad pinch gestures. |
| Input:Hover | [T-Input:Hover](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Hover) | Actionable UI elements have hover states (where appropriate) to indicate to mouse and trackpad users that the elements are interactive. |

![Icon for Tier 1 Adaptive Differentiated](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_icon.svg)

TIER 1

### Adaptive differentiated

Adaptive differentiated apps use the large screen and foldable form factors to
their full potential. Differentiated apps offer a premium user experience that's
productive and enjoyable.

Because Tier 1 apps are highly differentiated, some of the listed capabilities
are applicable only to specific types of apps. Choose the capabilities that are
appropriate for your application.

| ID | Tests | Description |
|---|---|---|
| Multitasking and multi‑instance |||
| Multitasking:Support | [T-Multitasking:PiP](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multitasking:PiP), [T-Multitasking:Split-Screen](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multitasking:Split-Screen), [T-Multitasking:Attachments](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multitasking:Attachments) | App supports various multitasking scenarios, for example: - Picture-in-picture mode: App is able to enter and exit picture-in-picture mode in portrait and landscape orientations, with the device folded and unfolded, and in multi-window mode. See [Picture-in-picture (PiP) support](https://developer.android.com/guide/topics/ui/picture-in-picture). - Multi-window mode: App can open another application in a separate window from a deep link; for example, a contact management app opens a link to an email message which is displayed in an email app in a new window. See [`FLAG_ACTIVITY_LAUNCH_ADJACENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_launch_adjacent). - Attachments: Messaging apps can open attachments (such as videos) in a separate window. |
| Multitasking:Multi-Instance | [T-Multitasking:Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Multitasking:Multi-Instance) | App is able to launch multiple instances of itself in separate windows. Use cases include document editing, web browsing, file management apps, and product comparisons in shopping apps. See [Multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance) in [Support multi-window mode.](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode) |
| Foldable postures and states |||
| Foldables:Postures | [T-Foldables:Postures](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Foldables:Postures) | App supports all foldable postures and related use cases: - Tabletop posture --- Video calling and video or audio playback. - Book posture --- Reading lengthy text content. - Dual display --- Front and back screen preview for camera apps. Support for dual-screen devices. See [Learn about foldables](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables). |
| Foldables:Camera | [T-Foldables:Camera](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Foldables:Camera) | Camera apps adjust their preview for folded and unfolded states and support front and back screen preview. |
| Drag and drop |||
| Drag_Drop:Support | [T-Drag_Drop:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Drag_Drop:Support) | App supports drag and drop between views within the app and, in multi-window mode, to and from other apps using touch input, mouse, trackpad, and stylus. See [Enable drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop). See also [Stylus:Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Drag_Drop). |
| Keyboard, mouse, and trackpad |||
| Input:Keyboard_Parity | [T-Input:Keyboard_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Keyboard_Parity) | App provides a comprehensive set of keyboard shortcuts while supporting conventional shortcuts such as <kbd>Ctrl-C</kbd> for copy and <kbd>Ctrl-Z</kbd> for undo. App maintains keyboard shortcut parity with equivalent web or desktop versions of the app whenever possible. |
| Input:Combinations | [T-Input:Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Combinations) | Keyboard and mouse or trackpad combinations, such as <kbd>Ctrl</kbd>+click or <kbd>Ctrl</kbd>+tap and <kbd>Shift</kbd>+click or <kbd>Shift</kbd>+tap, provide enhanced capabilities, including the selection of ranges of adjacent items or multiple separated items. |
| Input:Scrollbar | [T-Input:Scrollbar](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Scrollbar) | App displays a scrollbar while content is being scrolled by a mouse or trackpad. |
| Input:Hover_Parity | [T-Input:Hover_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Hover_Parity) | Where applicable, UI elements display additional content such as fly‑out menus or tooltips on mouse or trackpad hover. App maintains hover state parity with equivalent web or desktop versions of the app whenever possible. |
| Input:Desktop_Menus | [T-Input:Desktop_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Desktop_Menus) | Desktop-style menus and context menus are used where appropriate. |
| Input:Panel_Config | [T-Input:Panel_Config](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Panel_Config) | UI panels in multi-panel layouts are reconfigurable using a mouse or trackpad. Reconfigurable panels enable users to adjust the app layout for increased productivity, for example, by changing the size of the detail panel of a [list-detail](https://m3.material.io/foundations/adaptive-design/canonical-layouts#e6337592-71a6-4572-ac5a-15316bb64b8b) layout or by rearranging panels on screen. **Note:** This does not apply to navigation bars, rails, and drawers. |
| Input:Triple_Click | [T-Input:Triple_Click](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Input:Triple_Click) | Triple clicking using a mouse or triple tapping with a trackpad selects entire lines or paragraphs of text. |
| Stylus |||
| Stylus:Draw_Write | [T-Stylus:Draw_Write](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Stylus:Draw_Write) | App supports drawing and writing with a stylus. Drawings and writing can be erased with the stylus. |
| Stylus:Drag_Drop | [T-Stylus:Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Stylus:Drag_Drop) | App provides stylus support for dragging and dropping content between elements within the app and, in multi-window mode, to and from other apps. See [Enable drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop). |
| Stylus:Enhanced | [T-Stylus:Enhanced](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Stylus:Enhanced) | App provides enhanced stylus support, including: - Low latency and motion prediction to improve responsiveness - Pressure sensitivity for drawing strokes of varying width - Tilt detection for creating shading strokes - Palm and finger rejection to prevent stray marks See [Advanced stylus features](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features#low-latency). |
| Custom cursors |||
| Cursors:Custom | [T-Cursors:Custom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Cursors:Custom) | App displays customized cursors to indicate how and when users can interact with UI elements and content, for example: - System cursors provided by the Android framework: - I-beam for text - Resize handles at resizable layer edges - Processing spinners - Specialty cursors that you provide: - Crosshairs when hovering over targets in games - A magnifying glass when hovering over zoomable content - Tools in drawing or illustration apps See [`PointerIcon`](https://developer.android.com/reference/kotlin/android/view/PointerIcon) and [Mouse pointer icons](https://chromeos.dev/en/android/pointer-styling). |

## Adaptive app compatibility tests

The following tests help you discover quality issues in your app. You can
combine the tests or integrate groups of tests together in your own test plans.

For layout and UX purposes, test on at least the following device types:

- Foldable (841x701 dp)
- 8-inch tablet (1024x640 dp)
- 10.5-inch tablet (1280x800 dp)
- 13-inch Chromebook (1600x900 dp)

Use the following Android emulators to test adaptive device compatibility:

- Foldable phone --- 7.6" Fold-in with outer display
- Tablet --- Pixel C 9.94"
- Dual-display foldable --- Microsoft Surface Duo

Use the Android [resizable emulator](https://developer.android.com/about/versions/12/12L/get#resizable-emulator) to test a variety of device
configurations.

*** ** * ** ***

![Tier 3 adaptive ready icon.](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.svg)

TIER 3

### Adaptive ready

| ID | Feature | Description |
|---|---|---|
| Configuration and continuity |||
| T-Config:Orientation | [Config:Changes](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Config:Changes) | Verify that the app is not [letterboxed](https://developer.android.com/guide/practices/enhanced-letterboxing) and is not running in [compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode) in portrait and landscape orientations, in multi-window mode, or when a large screen foldable device is unfolded in portrait or landscape orientation. Resize the app window in multi-window mode, including split-screen and desktop windowing modes. On desktop devices, minimize and restore the app window, maximize and restore the app window. Verify that the app assumes the proper orientation and maintains state in all window sizes. **Note:** Test on a large screen device (sw \>= 600 dp) running Android 12 (API level 31) or higher to ensure the device supports the following: - All device orientations regardless of orientation restrictions set with the [`android:screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen) app manifest element - Multi-window mode, even for apps that have specified [`android:resizeableActivity="false"`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity) in the app manifest |
| T-Config:State | [Config:Changes](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Config:Changes) | From each app screen that has scrollable content, continuous playback content, or text entry fields, do the following: - Scrollable content: Scroll the content - Playback content: Begin playback - Text entry fields: Enter text in multiple fields Rotate the device between landscape and portrait orientations, fold and unfold the device (if applicable), span and unspan your app across two screens (if you have a dual-screen device) and resize the app window in multi-window mode. Minimize and restore the app window on desktop devices; maximize and restore the app window. Verify the following: - Scrollable content: The scroll position remains the same - Playback content: Playback resumes where it left off when the configuration change was initiated - Text entry fields: Previously entered text is retained in input fields |
| T-Config:Combinations | [Config:Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Config:Combinations) | From each app screen, perform combinations of rotating the device between landscape and portrait orientations, folding and unfolding the device (if applicable), and resizing the app window in multi-window mode. |
| Multi-window mode and multi-resume |||
| T-Multi-Window:Functionality | [Multi-Window:Functionality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Functionality) | Open the app in [multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#split-screen_mode_activation). Check whether the app is fully functional in all window sizes, device orientations, and foldable device states. Resize the app window in each orientation. For foldable devices, fold and unfold the device in each orientation. **Unity apps** Open an app other than your Unity app. Go to the **Recents** screen. Select the app icon and put the app in split-screen mode. Open your Unity app, which should launch in split-screen mode beside or below the first app. Go to the **Home** screen to hide the pair of apps. Go to the **Recents** screen. Select the split-screen app pair that includes your Unity app. Verify that the Unity app resumes its activity and the app's layout in the split-screen window is correct with all UI elements accessible. |
| T-Multi-Window:Focus | [Multi-Window:Multi-Resume](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Multi-Resume) | Open the app and initiate a process, such as playing a video, that continuously updates the app. Open another app and make the new app the top focused app. Verify that the non-focused app continues to update its content (for example, a video continues to play). |
| T-Multi-Window:Resources | [Multi-Window:Multi-Resume](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multi-Window:Multi-Resume) | In the app, open the camera or use the microphone. Open another app, and make the new app the top focused app. Verify that the non-focused app has relinquished the camera or mic. Make the original app the top focused app. Verify that the app has regained access to the camera or mic. |
| Camera preview and media projection |||
| T-Media:Camera_Preview | [Media:Camera_Preview](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Media:Camera_Preview) | Open the app full screen and in multi-window mode. Start the camera from within the app. Rotate the device between landscape and portrait orientations. For foldable devices, fold and unfold the device in each orientation. In multi-window mode, resize the app window. Verify that the camera preview is in the proper orientation and proportions in all device states and window sizes. |
| T-Media:Projection | [Media:Projection](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Media:Projection) | Open the app full screen and in multi-window mode. Start a media projection. Rotate the device between landscape and portrait orientations. For foldable devices, fold and unfold the device in each orientation. In multi-window mode, resize the app window. Verify that the media projection is in the proper orientation and proportions in all device states and window sizes. |
| Keyboard, mouse, and trackpad |||
| T-Input:Keyboard | [Input:Keyboard](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard) | For each app screen that has text entry fields, connect an external keyboard to the device and enter text with the external keyboard and the virtual keyboard. Disconnect the external keyboard and enter text with the virtual keyboard. |
| T-Input:Mouse_Trackpad | [Input:Mouse_Trackpad](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Mouse_Trackpad) | For each app screen, connect a mouse and trackpad to the device. Perform basic mouse and trackpad interactions: - Click all clickable elements such as buttons, drop‑down menus, and text entry fields. - Select radio buttons and checkboxes. Select text by swiping and double clicking. - Scroll vertically and horizontally (if applicable) through lists, pickers, and so forth |
| Stylus |||
| T-Stylus:Basic | [Stylus:Basic](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Basic) | Using a stylus, navigate through the app, select UI elements, scroll through lists and pickers, and generally interact with the app. |
| T-Stylus:Text_Input | [Stylus:Text_Input](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Text_Input) | On Android 14 (API level 34) and higher, enter and edit text in text input fields using a stylus. The software keyboard shouldn't appear. On ChromeOS M114 or higher, enter and edit text in text input fields in a `WebView`. |

![Tier 2 adaptive optimized icon.](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-2/tier_2_icon.svg)

TIER 2

### Adaptive optimized

| ID | Feature | Description |
|---|---|---|
| User interface |||
| T-UI:Flow | [UI:Layouts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Layouts), [UI:Elements](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Elements) | Run the app on devices that have a wide variety of screen sizes, including phones, foldable phones, small and large tablets, and desktop devices. Run the app in multi-window mode on the devices. Verify that the app layout responds and adapts to different screen and window sizes. Check whether the app expands and contracts navigation rails, scales the number of columns in grid layouts, flows text into columns, and so forth. Observe whether UI elements are formatted for both aesthetics and function. For apps using activity embedding, test whether activities are displayed side by side on large screens, stacked on small screens. |
| T-UI:Touch_Targets | [UI:Touch_Targets](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Touch_Targets) | Verify that touch targets maintain a consistent, accessible size and position for all display sizes and configurations. For information on accessibility, see the [Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor). |
| T-UI:Focus | [UI:Focus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#UI:Focus) | On each app screen that contains an interactive custom drawable, verify that the drawable can be focused using an external keyboard, D‑pad, or other device that enables UI elements to be focused. Verify that a visual indication of the focused state is apparent. For related information, see [Touch Mode](https://developer.android.com/reference/kotlin/android/view/View#touch-mode). |
| Keyboard, mouse, and trackpad |||
| T-Input:Keyboard_Navigation | [Input:Keyboard_Navigation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard_Navigation) | Navigate through the app's focusable components using the Tab and arrow keys of an external keyboard. |
| T-Input:Keyboard_Shortcuts | [Input:Keyboard_Shortcuts](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard_Shortcuts) | Use keyboard shortcuts on an external keyboard to perform select, cut, copy, paste, undo, and redo actions. |
| T-Input:Keyboard_Playback | [Input:Keyboard_Playback](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard_Playback) | Use an external keyboard to start, stop, pause, rewind, and fast forward media playback. |
| T-Input:Keyboard_Send | [Input:Keyboard_Send](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard_Send) | Use the <kbd>Enter</kbd> key of an external keyboard to send or submit data. |
| T-Input:Context_Menus | [Input:Context_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Context_Menus) | Use the secondary mouse button or trackpad secondary tap capability to access the context menu of interactive elements. |
| T-Input:Zoom | [Input:Zoom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Zoom) | Use the mouse scroll wheel (in conjunction with the <kbd>Control</kbd>, or <kbd>Ctrl</kbd>, key) and trackpad pinch gestures to zoom content in and out. |
| T-Input:Hover | [Input:Hover](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Hover) | Hover the mouse or trackpad cursor over actionable UI elements to activate the element's hover state. |

![Tier 1 adaptive differentiated icon.](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_icon.svg)

TIER 1

### Adaptive differentiated

| ID | Feature | Description |
|---|---|---|
| Multitasking and multi‑instance |||
| T-Multitasking:PiP | [Multitasking:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multitasking:Support) | Enter and exit picture-in-picture mode in portrait and landscape orientations, with the device folded and unfolded, and in multi-window mode. In multi-window mode, change the window size while picture-in-picture mode is active. |
| T-Multitasking:Split-Screen | [Multitasking:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multitasking:Support) | In multi-window mode, open another app from within the app and display both apps side by side. |
| T-Multitasking:Attachments | [Multitasking:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multitasking:Support) | Open and close attachments and notifications in portrait and landscape orientations, with the device folded and unfolded, and in multi-window mode. |
| T-Multitasking:Multi-Instance | [Multitasking:Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multitasking:Multi-Instance) | Launch multiple instances of the app in separate windows in portrait and landscape orientations, with the device folded and unfolded, and in multi-window mode. |
| Foldable postures and states |||
| T-Foldables:Postures | [Foldables:Postures](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Foldables:Postures) | View the app in all foldable postures, including tabletop and book postures. Verify that UI elements transition to the optimal location (for example, media controllers move to the horizontal screen area in tabletop posture). |
| T-Foldables:Camera | [Foldables:Camera](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Foldables:Camera) | Activate the camera from within the app. Verify that the camera preview is correct when the device is folded and unfolded and rotated to portrait and landscape orientations. With the device unfolded, verify that the preview is correct on front and back screens. |
| Drag and drop |||
| T-Drag_Drop:Support | [Drag_Drop:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Drag_Drop:Support) | Drag and drop images and text on drop targets within the app. In multi-window mode, drag and drop images and text between the app and another app (to and from both apps). Drag and drop the content using touch input, mouse, trackpad, and stylus (see also [T-Stylus:Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#T-Stylus:Drag_Drop)). Verify the functionality in portrait and landscape orientations and when the device is in folded and unfolded states. |
| Keyboard, mouse, and trackpad |||
| T-Input:Keyboard_Parity | [Input:Keyboard_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard_Parity) | Change the app's keyboard shortcuts. Test the revised shortcuts using an external keyboard. |
| T-Input:Combinations | [Input:Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Combinations) | Using an external keyboard, mouse, and trackpad, select items in the app's UI. Select multiple separated items and ranges of adjacent items using keyboard/mouse/trackpad actions such as <kbd>Ctrl</kbd>+click, <kbd>Ctrl</kbd>+tap, <kbd>Shift</kbd>+click, and <kbd>Shift</kbd>+tap. |
| T-Input:Scrollbar | [Input:Scrollbar](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Scrollbar) | Scroll app content using a mouse and trackpad. Verify that a scrollbar appears while the content is scrolling. |
| T-Input:Hover_Parity | [Input:Hover_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Hover_Parity) | Using a mouse and trackpad, hover the pointer over UI elements that contain cascading or pop‑up content. Verify that the additional content is revealed. |
| T-Input:Desktop_Menus | [Input:Desktop_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Desktop_Menus) | On desktop and connected displays, verify that desktop-style menus and context menus are used. |
| T-Input:Panel_Config | [Input:Panel_Config](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Panel_Config) | On each app screen, resize and rearrange UI panels using a mouse and trackpad. |
| T-Input:Triple_Click | [Input:Triple_Click](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Triple_Click) | Using a mouse and trackpad, triple click or triple tap to select items in the app, for example, to select full lines of text. |
| Stylus |||
| T-Stylus:Draw_Write | [Stylus:Draw_Write](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Draw_Write) | Draw and write within the app using a stylus. Erase drawings and writing using the stylus. |
| T-Stylus:Drag_Drop | [Stylus:Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Drag_Drop) | Using a stylus, drag and drop content on drop targets within the app. In multi-window mode, drag and drop content between the app and another app (to and from both apps). |
| T-Stylus:Enhanced | [Stylus:Enhanced](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Enhanced) | Interact with the app using a stylus as follows: - As you draw, observe the latency between the current stylus position and the last rendered stroke. - Draw with varying amounts of stylus pressure. Check whether the width of the strokes changes as the pressure changes. More pressure should produce thicker strokes. - Tilt the stylus as you draw; shading strokes should be produced. The more the stylus is tilted, the wider and lighter the shading strokes should be. - Let your fingers and palm touch the screen as you draw. The finger and palm touches shouldn't produce marks. |
| Custom cursors |||
| T-Cursors:Custom | [Cursors:Custom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Cursors:Custom) | Interact with the app using a mouse and trackpad. Verify that custom cursors appear where appropriate, for example: - I-beam for text entry fields - Resize handles at resizable layer edges - Spinners when app is performing long-running tasks |

## Archive

Previous versions of the adaptive app quality guidelines:

- [Large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/archive/adaptive/large-screen-app-quality)