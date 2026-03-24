---
title: https://developer.android.com/docs/quality-guidelines/archive/adaptive/id-map-ls-adaptive
url: https://developer.android.com/docs/quality-guidelines/archive/adaptive/id-map-ls-adaptive
source: md.txt
---

*Created 2026-02-26*

The following table provides a one-to-one mapping between the original guideline
and test IDs in the large screen app quality guidelines and the renamed IDs in
the updated adaptive app quality guidelines.

## Guidelines

### Tier 3

| Large screen app quality || Adaptive app quality ||
| Category | ID | ID | Category |
|---|---|---|---|
| Configuration and continuity | LS-C1 | Config_Changes | Configuration and continuity |
| Configuration and continuity | LS-C2 | Config_Combinations | Configuration and continuity |
| Multi-window mode and multi-resume | LS-M1 | Multi-Window_Functionality | Multi-window mode and multi-resume |
| Multi-window mode and multi-resume | LS-M2 | Multi-Resume | Multi-window mode and multi-resume |
| Camera preview and media projection | LS-CM1 | Camera_Preview | Camera preview and media projection |
| Camera preview and media projection | LS-CM2 | Media_Projection | Camera preview and media projection |
| Keyboard, mouse, and trackpad | LS-I1 | Keyboard_Input | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I2 | Mouse_Trackpad_Basic | Keyboard, mouse, and trackpad |
| Stylus | LS-S1 | Stylus_Basic | Stylus |
| Stylus | LS-S1.1 | Stylus_Text_Input | Stylus |

### Tier 2

| Large screen app quality || Adaptive app quality ||
| Category | ID | ID | Category |
|---|---|---|---|
| UX | LS-U1 | Responsive_adaptive_layouts | User interface |
| UX | LS-U2 | UI_Secondary_Elements | User interface |
| UX | LS-U3 | Touch_Targets | User interface |
| UX | LS-U4 | Drawable_Focus | User interface |
| Keyboard, mouse, and trackpad | LS-I3 | Keyboard_Navigation | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I4 | Keyboard_Shortcuts | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I5 | Keyboard_Media_Playback | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I6 | Keyboard_Send | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I7 | Context_Menus | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I8 | Content_Zoom | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | LS-I9 | Hover_States | Keyboard, mouse, and trackpad |

### Tier 1

| Large screen app quality || Adaptive app quality |||
| Category | ID | ID | Category | Experience |
|---|---|---|---|---|
| Multitasking and multi-instance | LS-M3 | Multitasking_Scenarios | Multitasking and multi-instance | Desktop |
| Multitasking and multi-instance | LS-M4 | Multi-Instance | Multitasking and multi-instance | Desktop |
| Foldable postures and states | LS-F1 | Foldables_Postures | Foldable postures and states | Foldables |
| Foldable postures and states | LS-F2 | Foldables_Camera | Foldable postures and states | Foldables |
| Drag and drop | LS-D1 | Drag_Drop_Support | Drag and drop | Desktop |
| Keyboard, mouse, and trackpad | LS-I10 | Keyboard_Parity | Keyboard, mouse, and trackpad | Desktop |
| Keyboard, mouse, and trackpad | LS-I11 | Input_Combinations | Keyboard, mouse, and trackpad | Desktop |
| Keyboard, mouse, and trackpad | LS-I12 | Scrollbar_Display | User experience | Desktop |
| Keyboard, mouse, and trackpad | LS-I13 | Hover_Parity | User experience | Desktop |
| Keyboard, mouse, and trackpad | LS-I14 | Desktop_Menus | User experience | Desktop |
| Keyboard, mouse, and trackpad | LS-I15 | UI_Config | User experience | Desktop |
| Keyboard, mouse, and trackpad | LS-I16 | Triple_Click | Keyboard, mouse, and trackpad | Desktop |
| Stylus | LS-S2 | Stylus_Draw_Write | Stylus | Stylus |
| Stylus | LS-S3 | Stylus_Drag_Drop | Stylus | Stylus |
| Stylus | LS-S4 | Stylus_Enhanced | Stylus | Stylus |
| Custom cursors | LS-P1 | Custom_Cursors | Cursors | Desktop |
|   |   | Request_Fullscreen_Mode | User experience | Desktop |
|   |   | Printing_Support | Printing and file management | Desktop |
|   |   | File_Management_Basics | Printing and file management | Desktop |
|   |   | File_Picker | Printing and file management | Desktop |
|   |   | File_Handlers | Printing and file management | Desktop |
|   |   | Cursor_Target_Size | Cursors | Desktop |
|   |   | Cross_Device_Handoff | Cross-device | Desktop |
|   |   | Offline_Support | Offline support | Desktop |
|   |   | Web_Transition | App-to-web | Desktop |
|   |   | Foldables_Multitasking_Scenarios | Multitasking and multi-instance | Foldables |
|   |   | Foldables_PiP | Multitasking and multi-instance | Foldables |
|   |   | Foldables_Multi-Instance | Multitasking and multi-instance | Foldables |
|   |   | Camera_Switcher | Camera | Camera • Audio |
|   |   | Audio_Switcher | Audio | Camera • Audio |
|   |   | Audio_Background_Playback | Audio | Camera • Audio |

## Tests

### Tier 3

| Large screen app quality || Adaptive app quality ||
| Category | ID | ID | Category |
|---|---|---|---|
| Configuration and continuity | T3-1 | T-Config_Orientation | Configuration and continuity |
| Configuration and continuity | T3-2 | T-Config_State | Configuration and continuity |
| Configuration and continuity | T3-3 | T-Config_Combinations | Configuration and continuity |
| Multi-window mode and multi-resume | T3-4 | T-Multi-Window_Functionality | Multi-window mode and multi-resume |
| Multi-window mode and multi-resume | T3-5 | T-Multi-Window_Focus | Multi-window mode and multi-resume |
| Multi-window mode and multi-resume | T3-6 | T-Multi-Window_Resources | Multi-window mode and multi-resume |
| Camera preview and media projection | T3-7 | T-Camera_Preview | Camera preview and media projection |
| Camera preview and media projection | T3-8 | T-Media_Projection | Camera preview and media projection |
| Keyboard, mouse, and trackpad | T3-9 | T-Keyboard_Input | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T3-10 | T-Mouse_Trackpad_Basic | Keyboard, mouse, and trackpad |
| Stylus | T3-11 | T-Stylus_Basic | Stylus |
| Stylus | T3-12 | T-Stylus_Text_Input | Stylus |

### Tier 2

| Large screen app quality || Adaptive app quality ||
| Category | ID | ID | Category |
|---|---|---|---|
| UX | T2-1 | T-Layout_Flow | User interface |
| UX | T2-2 | T-Touch_Targets | User interface |
| UX | T2-3 | T-Drawable_Focus | User interface |
| Keyboard, mouse, and trackpad | T2-4 | T-Keyboard_Navigation | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T2-5 | T-Keyboard_Shortcuts | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T2-6 | T-Keyboard_Media_Playback | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T2-7 | T-Keyboard_Send | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T2-8 | T-Context_Menus | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T2-9 | T-Content_Zoom | Keyboard, mouse, and trackpad |
| Keyboard, mouse, and trackpad | T2-10 | T-Hover_States | Keyboard, mouse, and trackpad |

### Tier 1

| Large screen app quality || Adaptive app quality |||
| Category | ID | ID | Category | Experience |
|---|---|---|---|---|
| Multitasking and multi-instance | T1-1 | T-Multitasking_PiP | Multitasking and multi-instance | Desktop |
| Multitasking and multi-instance | T1-2 | T-Multitasking_Split-Screen | Multitasking and multi-instance | Desktop |
| Multitasking and multi-instance | T1-3 | T-Multitasking_Attachments | Multitasking and multi-instance | Desktop |
| Multitasking and multi-instance | T1-4 | T-Multi-Instance | Multitasking and multi-instance | Desktop |
| Foldable postures and states | T1-5 | T-Foldables_Postures | Foldable postures and states | Foldables |
| Foldable postures and states | T1-6 | T-Foldables_Camera | Foldable postures and states | Foldables |
| Drag and drop | T1-7 | T-Drag_Drop_Support | Drag and drop | Desktop |
| Keyboard, mouse, and trackpad | T1-8 | T-Keyboard_Parity | Keyboard, mouse, and trackpad | Desktop |
| Keyboard, mouse, and trackpad | T1-9 | T-Input_Combinations | Keyboard, mouse, and trackpad | Desktop |
| Keyboard, mouse, and trackpad | T1-10 | T-Scrollbar_Display | User experience | Desktop |
| Keyboard, mouse, and trackpad | T1-11 | T-Hover_Parity | User experience | Desktop |
| Keyboard, mouse, and trackpad | T1-12 | T-Desktop_Menus | User experience | Desktop |
| Keyboard, mouse, and trackpad | T1-13 | T-UI_Config | User experience | Desktop |
| Keyboard, mouse, and trackpad | T1-14 | T-Triple_Click | Keyboard, mouse, and trackpad | Desktop |
| Stylus | T1-15 | T-Stylus_Draw_Write | Stylus | Stylus |
| Stylus | T1-16 | T-Stylus_Drag_Drop | Stylus | Stylus |
| Stylus | T1-17 | T-Stylus_Enhanced | Stylus | Stylus |
| Custom cursors | T1-18 | T-Custom_Cursors | Cursors | Desktop |
|   |   | T-Request_Fullscreen_Mode | User experience | Desktop |
|   |   | T-Drag_Drop_Batch | Drag and drop | Desktop |
|   |   | T-Printing_Support | Printing and file management | Desktop |
|   |   | T-File_Picker | Printing and file management | Desktop |
|   |   | T-File_Management_Basics | Printing and file management | Desktop |
|   |   | T-File_Handlers | Printing and file management | Desktop |
|   |   | T-Cursor_Target_Size | Cursors | Desktop |
|   |   | T-Cross_Device_Handoff | Cross-device | Desktop |
|   |   | T-Offline_Support | Offline support | Desktop |
|   |   | T-Web_Transition | App-to-web | Desktop |
|   |   | T-Foldables_PiP | Multitasking and multi-instance | Foldables |
|   |   | T-Foldables_Attachments | Multitasking and multi-instance | Foldables |
|   |   | T-Foldables_Multi-Instance | Multitasking and multi-instance | Foldables |
|   |   | T-Camera_Switcher | Camera | Camera • Audio |
|   |   | T-Audio_Switcher | Audio | Camera • Audio |
|   |   | T-Audio_Background_Playback | Audio | Camera • Audio |