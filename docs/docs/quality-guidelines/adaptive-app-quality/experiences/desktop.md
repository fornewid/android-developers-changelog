---
title: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop
source: md.txt
---

The desktop experience---common on Chromebooks and connected
displays---enables precise input and advanced multitasking. The desktop
environment allows users to work across multiple windows and instances,
utilizing keyboard shortcuts and mouse and trackpad interactions. Apps optimized
for desktop provide a productive user experience that bridges the gap between
mobile convenience and desktop power.

## Guidelines

Create an exceptional user experience that takes full advantage of device
capabilities.

### User experience

| Guideline ID | Test IDs | Description |
|---|---|---|
| Scrollbar_Display | [T-Scrollbar_Display](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Scrollbar_Display) | App displays a scrollbar while content is being scrolled by a mouse or trackpad. |
| Hover_Parity | [T-Hover_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Hover_Parity) | Where applicable, UI elements display additional content such as previews, fly‑out menus, and informative tooltips on mouse or trackpad hover. App maintains hover state parity with equivalent web or desktop versions of the app whenever possible. App ensures distinct and consistent hover states with visual contrast that supports accessibility standards on all UI elements. |
| Desktop_Menus | [T-Desktop_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Desktop_Menus) | App has non-intrusive UI elements such as desktop-style menus, context menus, and small modals where appropriate to allow users to remain focused on their primary task without constant navigation. |
| UI_Config | [T-UI_Config](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-UI_Config) | App has adaptive, user-configurable layouts for large screens and cursor-first devices, including: - Adaptive layouts enable users to switch between list, grid, and column presentations. For example, a file or document manager provides a toggle that respects the user's preference to see their files in a list or grid format. - Dockable or movable floating toolbars accommodate user preferences and task requirements. - UI panels in multi-panel layouts are collapsible and reconfigurable using a mouse or trackpad. Reconfigurable panels enable users to adjust the app layout for increased productivity, for example, by changing the size of the detail panel of a [list-detail](https://m3.material.io/foundations/adaptive-design/canonical-layouts#e6337592-71a6-4572-ac5a-15316bb64b8b) layout or by rearranging panels on screen. **Note:** This does not apply to navigation bars, rails, and drawers. |
| Request_Fullscreen_Mode | [T-Request_Fullscreen_Mode](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Request_Fullscreen_Mode) | App implements [`Activity#requestFullscreenMode()`]() to enable smooth transitions from multi-window states, such as split-screen and desktop windowing, to immersive mode. Typically, apps provide a UI element such as a button that activates the fullscreen, immersive experience. |

### Keyboard, mouse, and trackpad

| Guideline ID | Test IDs | Description |
|---|---|---|
| Keyboard_Navigation | [T-Keyboard_Navigation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Keyboard_Navigation) | App supports seamless and efficient navigation with a keyboard. The app ensures distinct and consistent focus states with visual contrast that supports accessibility standards for all UI elements. Initial focus is set for appropriate UI elements; for example, when users draft a message in an email app, focus is initially on the *To* text field. Users should be able to start typing right away in the first text input field when a page loads. See [Keyboard interaction](https://developer.android.com/design/ui/desktop/guides/interaction/keyboard). |
| Keyboard_Parity | [T-Keyboard_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Keyboard_Parity) | App provides a comprehensive set of keyboard shortcuts while supporting conventional shortcuts such as <kbd>Ctrl-C</kbd> for copy and <kbd>Ctrl-Z</kbd> for undo. App maintains keyboard shortcut parity with equivalent web and desktop versions of the app whenever possible. |
| Input_Combinations | [T-Input_Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Input_Combinations) | Keyboard and mouse or trackpad combinations, such as <kbd>Ctrl</kbd>+click or <kbd>Ctrl</kbd>+tap and <kbd>Shift</kbd>+click or <kbd>Shift</kbd>+tap, provide enhanced capabilities, including the selection of ranges of adjacent items or multiple separated items. |
| Triple_Click | [T-Triple_Click](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Triple_Click) | Triple clicking using a mouse or triple tapping with a trackpad selects entire lines or paragraphs of text. |

### Multitasking and multi-instance

| Guideline ID | Test IDs | Description |
|---|---|---|
| Multitasking_Scenarios | [T-Multitasking_PiP](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Multitasking_PiP), [T-Multitasking_Split-Screen](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Multitasking_Split-Screen), [T-Multitasking_Attachments](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Multitasking_Attachments) | App supports various multitasking scenarios, for example: - Picture-in-picture mode: App is able to enter and exit picture-in-picture mode in portrait and landscape orientations and in multi-window mode. Use cases include media playback and video calls. See [Picture-in-picture (PiP) support](https://developer.android.com/guide/topics/ui/picture-in-picture). - Multi-window mode: App can open another application in a separate window from a deep link; for example, a contact management app opens a link to an email message which is displayed in an email app in a new window. See [`FLAG_ACTIVITY_LAUNCH_ADJACENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_launch_adjacent). - Attachments: Messaging apps can open attachments (such as videos) in a separate window. |
| Multitasking_PiP | [T-Multitasking_PiP](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Multitasking_PiP) | App supports interactive picture‑in‑picture functionality that enables custom controls and user interaction in media and non‑media applications. |
| Multi-Instance | [T-Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Multi-Instance) | App is able to launch multiple instances of itself in separate windows. Use cases include document editing, web browsing, file management apps, and product comparisons in shopping apps. See [Multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance) in [Support multi-window mode.](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode) |

### Drag and drop

| Guideline ID | Test IDs | Description |
|---|---|---|
| Drag_Drop_Support | [T-Drag_Drop_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Drag_Drop_Support) | App supports drag and drop between presentations within the app and, in multi-window mode, to and from other apps using touch input, mouse, trackpad, and stylus. See [Enable drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop). See also [Stylus_Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#Stylus_Drag_Drop). |
| Drag_Drop_Support | [T-Drag_Drop_Batch](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Drag_Drop_Batch) | App supports drag and drop of multiple elements into the app to be processed as a group. See [DropHelper for simplified drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/drophelper). |

### Printing and file management

| Guideline ID | Test IDs | Description |
|---|---|---|
| Printing_Support | [T-Printing_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Printing_Support) | App supports document printing or exporting to a printable format. |
| File_Management_Basics | [T-File_Management_Basics](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-File_Management_Basics) | App implements common file management functionality, including: - **Naming and saving:** File names and locations are prominently visible. - **Downloading:** Users can save files to their preferred location on the local storage device. - **Uploading:** Users can upload files from local storage and prioritize using the OS file picker. |
| File_Picker | [T-File_Picker](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-File_Picker) | App integrates with the OS file picker, ensuring seamless import and export experiences. Desktop and productivity users rely heavily on file managers for broad content access. |
| File_Handlers | [T-File_Handlers](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-File_Handlers) | App designates itself as a file handler by declaring support for relevant file types. This enables users to open files with specific applications directly from the system's Files app. |

### Cursors

| Guideline ID | Test IDs | Description |
|---|---|---|
| Custom_Cursors | [T-Custom_Cursors](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Custom_Cursors) | App displays customized cursors to indicate how and when users can interact with UI elements and content, for example: - System cursors provided by the Android framework: - I-beam for text - Resize handles at resizable layer edges - Processing spinners - Specialty cursors that you provide: - Crosshairs when hovering over targets in games - A magnifying glass when hovering over zoomable content - Tools in drawing or illustration apps For more information, see: <!-- --> - [Cursors](https://developer.android.com/design/ui/desktop/guides/interaction/cursors) - [`PointerIcon`](https://developer.android.com/reference/kotlin/android/view/PointerIcon) - [Mouse pointer icons](https://chromeos.dev/en/android/pointer-styling) |
| Cursor_Target_Size | [T-Cursor_Target_Size](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Cursor_Target_Size) | App prioritizes precision in cursor interactions by implementing cursor target sizes that match visual target sizes to reduce perceived target. |

### Cross-device

| Guideline ID | Test IDs | Description |
|---|---|---|
| Cross_Device_Handoff | [T-Cross_Device_Handoff](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Cross_Device_Handoff) | Apps that work on multiple types of Android devices allow users to start a task on one Android device and seamlessly transition to another. The app restores a near‑equivalent state for the same task so the user can continue where they left off. |

### Offline support

| Guideline ID | Test IDs | Description |
|---|---|---|
| Offline_Support | [T-Offline_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Offline_Support) | App enables offline functionality for the full or partial feature set, allowing users to remain productive. The app provides graceful degradation to notify users of connection requirements. |

### App-to-web

| Guideline ID | Test IDs | Description |
|---|---|---|
| Web_Transition | [T-Web_Transition](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#T-Web_Transition) | App ensures smooth and intelligent transitions between app and web content (and vice versa) where appropriate, avoiding fragmented user experiences. |

## Tests

To verify that your app provides a premium, differentiated experience, complete
the following tests.

### User experience

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Scrollbar_Display | [Scrollbar_Display](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Scrollbar_Display) | Scroll app content using a mouse and trackpad. Verify that a scrollbar appears while the content is scrolling. |
| T-Hover_Parity | [Hover_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Hover_Parity) | Using a mouse and trackpad, hover the pointer over UI elements that contain cascading or pop‑up content. Verify that the additional content is revealed. |
| T-Desktop_Menus | [Desktop_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Desktop_Menus) | On desktop and connected displays, verify that desktop-style menus and context menus are used. |
| T-UI_Config | [UI_Config](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#UI_Config) | Verify that the app provides user-configurable layout options: - Layout presentation --- If the app supports multiple presentation formats (such as list, grid, or column views), verify that users can switch between the formats. - Floating toolbars --- If the app provides dockable or movable floating toolbars, verify that users can move or dock the toolbars. - Panel reconfiguration --- On screen layouts that have multiple content panels (such as list‑detail), resize the panels by dragging dividers. Rearrange the panels if the app supports rearrangement. In all cases, verify that the app correctly reconfigures its layout and the content remains accessible and properly formatted. |
| T-Request_Fullscreen_Mode | [Request_Fullscreen_Mode](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Request_Fullscreen_Mode) | Place the app window in a multi-window state, such as split-screen or desktop windowing mode. Trigger the app's fullscreen UI element. Verify that the app smoothly transitions to immersive fullscreen mode. |

### Keyboard, mouse, and trackpad

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Keyboard_Navigation | [Keyboard_Navigation](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Keyboard_Navigation) | Using an external keyboard, navigate through the app's UI using the <kbd>Tab</kbd> and arrow keys. Verify that focus states are distinct and consistent for all interactive elements. Also verify that appropriate UI elements, such as text input fields, receive initial focus when a screen is first displayed and users are able to enter data. |
| T-Keyboard_Parity | [Keyboard_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Keyboard_Parity) | Verify that the app supports conventional keyboard shortcuts and maintains keyboard shortcut parity with the web and desktop versions of the app whenever possible. |
| T-Input_Combinations | [Input_Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Input_Combinations) | Using an external keyboard, mouse, and trackpad, select items in the app's UI. Select multiple separated items and ranges of adjacent items using keyboard/mouse/trackpad actions such as <kbd>Ctrl</kbd>+click, <kbd>Ctrl</kbd>+tap, <kbd>Shift</kbd>+click, and <kbd>Shift</kbd>+tap. |
| T-Triple_Click | [Triple_Click](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Triple_Click) | Using a mouse and trackpad, triple click or triple tap to select items in the app, for example, to select full lines of text. |

### Multitasking and multi-instance

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Multitasking_PiP | [Multitasking_Scenarios](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multitasking_Scenarios) | Enter and exit picture-in-picture mode in portrait and landscape orientations and in multi‑window mode. In multi‑window mode, change the window size while picture‑in‑picture mode is active. In picture-in-picture mode, interact with any custom controls and verify their functionality. |
| T-Multitasking_Split-Screen | [Multitasking_Scenarios](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multitasking_Scenarios) | In multi-window mode, open another app from within the app and display both apps side by side. |
| T-Multitasking_Attachments | [Multitasking_Scenarios](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multitasking_Scenarios) | Open and close attachments and notifications in portrait and landscape orientations and in multi-window mode. |
| T-Multi-Instance | [Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multi-Instance) | Launch multiple instances of the app in separate windows in portrait and landscape orientations and in multi-window mode. |

### Drag and drop

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Drag_Drop_Support | [Drag_Drop_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Drag_Drop_Support) | Drag and drop images and text on drop targets within the app. In multi-window mode, drag and drop images and text between the app and another app (to and from both apps). Drag and drop the content using touch input, mouse, trackpad, and stylus (see also [T-Stylus_Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#T-Stylus_Drag_Drop)). Verify the functionality in portrait and landscape orientations. |
| T-Drag_Drop_Batch | [Drag_Drop_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Drag_Drop_Support) | Drag and drop multiple elements, such as images and text, as a group within the app. In multi-window mode, drag and drop groups of elements between the app and another app (to and from both apps). Drag and drop the content using touch input, mouse, trackpad, and stylus (see also [T-Stylus_Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#T-Stylus_Drag_Drop)). Verify the functionality in portrait and landscape orientations. |

### Printing and file management

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Printing_Support | [Printing_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Printing_Support) | Verify that the app can print documents or export them to a printable format such as PDF. |
| T-File_Management_Basics | [File_Management_Basics](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#File_Management_Basics) | Verify that file names and locations are visible, and that users can choose save locations when downloading or uploading files. |
| T-File_Picker | [File_Picker](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#File_Picker) | Verify that the app uses the system file picker for importing and exporting files. |
| T-File_Handlers | [File_Handlers](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#File_Handlers) | From the system Files app, verify that the app is listed as an option to open relevant file types. |

### Cursors

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Custom_Cursors | [Custom_Cursors](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Custom_Cursors) | Interact with the app using a mouse and trackpad. Verify that custom cursors appear where appropriate, for example: - I-beam for text entry fields - Resize handles at resizable layer edges - Spinners when app is performing long-running tasks |
| T-Cursor_Target_Size | [Cursor_Target_Size](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Cursor_Target_Size) | Using a mouse and trackpad, interact with small UI elements such as icons, buttons, and handles. Verify that the interactive area of each element accurately reflects its visual boundaries, allowing for precise selection. |

### Cross-device

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Cross_Device_Handoff | [Cross_Device_Handoff](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Cross_Device_Handoff) | Start a task on one device, then switch to another device where the app is installed. Verify that you can continue the task from a near‑equivalent state. |

### Offline support

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Offline_Support | [Offline_Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Offline_Support) | Disable network connectivity and verify that core app functionality remains available or that the app provides clear notification of connection requirements. |

### App-to-web

| Test ID | Guideline IDs | Description |
|---|---|---|
| T-Web_Transition | [Web_Transition](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Web_Transition) | Interact with deep links or web content within the app. Verify that transitions between the app and related web content are seamless. |