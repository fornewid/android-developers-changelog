---
title: ID map  |  App quality  |  Android Developers
url: https://developer.android.com/docs/quality-guidelines/archive/adaptive/id-map-transitional
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [App quality](https://developer.android.com/quality)

# ID map Stay organized with collections Save and categorize content based on your preferences.




*Created 2026-02-23*

The following table provides a one-to-one mapping between the original IDs in
the large screen app quality guidelines and the renamed IDs in the updated
adaptive app quality guidelines.

## Guidelines

### Tier 3

| Large screen app quality | Transition | Adaptive app quality |
| --- | --- | --- |
| LS-C1 | Config:Changes | Config\_Changes |
| LS-C2 | Config:Combinations | Config\_Combinations |
| LS-M1 | Multi-Window:Functionality | Multi-Window\_Functionality |
| LS-M2 | Multi-Window:Multi-Resume | Multi-Resume |
| LS-CM1 | Media:Camera\_Preview | Camera\_Preview |
| LS-CM2 | Media:Projection | Media\_Projection |
| LS-I1 | Input:Keyboard | Keyboard\_Input |
| LS-I2 | Input:Mouse\_Trackpad | Mouse\_Trackpad\_Basic |
| LS-S1 | Stylus:Basic | Stylus\_Basic |
| LS-S1.1 | Stylus:Text\_Input | Stylus\_Text\_Input |

### Tier 2

| Large screen app quality |  | Adaptive app quality |
| --- | --- | --- |
| LS-U1 | UI:Layouts | Responsive\_adaptive\_layouts |
| LS-U2 | UI:Elements | UI\_Secondary\_Elements |
| LS-U3 | UI:Touch\_Targets | Touch\_Targets |
| LS-U4 | UI:Focus | Drawable\_Focus |
| LS-I3 | Input:Keyboard\_Navigation | Keyboard\_Navigation |
| LS-I4 | Input:Keyboard\_Shortcuts | Keyboard\_Shortcuts |
| LS-I5 | Input:Keyboard\_Playback | Keyboard\_Media\_Playback |
| LS-I6 | Input:Keyboard\_Send | Keyboard\_Send |
| LS-I7 | Input:Context\_Menus | Context\_Menus |
| LS-I8 | Input:Zoom | Content\_Zoom |
| LS-I9 | Input:Hover | Hover\_States |

### Tier 1

| Large screen app quality |  | Adaptive app quality |
| --- | --- | --- |
| LS-M3 | Multitasking:Support | Multitasking\_Scenarios |
| LS-M4 | Multitasking:Multi-Instance | Multi-Instance |
| LS-F1 | Foldables:Postures | Foldables\_Postures |
| LS-F2 | Foldables:Camera | Foldables\_Camera |
| LS-D1 | Drag\_Drop:Support | Drag\_Drop\_Support |
| LS-I10 | Input:Keyboard\_Parity | Keyboard\_Parity |
| LS-I11 | Input:Combinations | Input\_Combinations |
| LS-I12 | Input:Scrollbar | Scrollbar\_Display |
| LS-I13 | Input:Hover\_Parity | Hover\_Parity |
| LS-I14 | Input:Desktop\_Menus | Desktop\_Menus |
| LS-I15 | Input:Panel\_Config | UI\_Config |
| LS-I16 | Input:Triple\_Click | Triple\_Click |
| LS-S2 | Stylus:Draw\_Write | Stylus\_Draw\_Write |
| LS-S3 | Stylus:Drag\_Drop | Stylus\_Drag\_Drop |
| LS-S4 | Stylus:Enhanced | Stylus\_Enhanced |
| LS-P1 | Cursors:Custom | Custom\_Cursors |
|  |  | Camera\_Switcher |
|  |  | Audio\_Switcher |
|  |  | Media\_Background\_Playback |
|  |  | Request\_Fullscreen\_Mode |
|  |  | Multitasking\_PiP |
|  |  | Printing\_Support |
|  |  | File\_Management\_Basics |
|  |  | File\_Picker |
|  |  | File\_Handlers |
|  |  | Cursor\_Target\_Size |
|  |  | Cross\_Device\_Handoff |
|  |  | Offline\_Support |
|  |  | Web\_Transition |

## Tests

### Tier 3

| Large screen app quality |  | Adaptive app quality |
| --- | --- | --- |
| T3-1 | T-Config:Orientation | T-Config\_Orientation |
| T3-2 | T-Config:State | T-Config\_State |
| T3-3 | T-Config:Combinations | T-Config\_Combinations |
| T3-4 | T-Multi-Window:Functionality | T-Multi-Window\_Functionality |
| T3-5 | T-Multi-Window:Focus | T-Multi-Window\_Focus |
| T3-6 | T-Multi-Window:Resources | T-Multi-Window\_Resources |
| T3-7 | T-Media:Camera\_Preview | T-Camera\_Preview |
| T3-8 | T-Media:Projection | T-Media\_Projection |
| T3-9 | T-Input:Keyboard | T-Keyboard\_Input |
| T3-10 | T-Input:Mouse\_Trackpad | T-Mouse\_Trackpad\_Basic |
| T3-11 | T-Stylus:Basic | T-Stylus\_Basic |
| T3-12 | T-Stylus:Text\_Input | T-Stylus\_Text\_Input |

### Tier 2

| Large screen app quality |  | Adaptive app quality |
| --- | --- | --- |
| T2-1 | T-UI:Flow | T-Layout\_Flow |
| T2-2 | T-UI:Touch\_Targets | T-Touch\_Targets |
| T2-3 | T-UI:Focus | T-Drawable\_Focus |
| T2-4 | T-Input:Keyboard\_Navigation | T-Keyboard\_Navigation |
| T2-5 | T-Input:Keyboard\_Shortcuts | T-Keyboard\_Shortcuts |
| T2-6 | T-Input:Keyboard\_Playback | T-Keyboard\_Media\_Playback |
| T2-7 | T-Input:Keyboard\_Send | T-Keyboard\_Send |
| T2-8 | T-Input:Context\_Menus | T-Context\_Menus |
| T2-9 | T-Input:Zoom | T-Content\_Zoom |
| T2-10 | T-Input:Hover | T-Hover\_States |

### Tier 1

| Large screen app quality |  | Adaptive app quality |
| --- | --- | --- |
| T1-1 | T-Multitasking:PiP | T-Multitasking\_PiP |
| T1-2 | T-Multitasking:Split-Screen | T-Multitasking\_Split-Screen |
| T1-3 | T-Multitasking:Attachments | T-Multitasking\_Attachments |
| T1-4 | T-Multitasking:Multi-Instance | T-Multi-Instance |
| T1-5 | T-Foldables:Postures | T-Foldables\_Postures |
| T1-6 | T-Foldables:Camera | T-Foldables\_Camera |
| T1-7 | T-Drag\_Drop:Support | T-Drag\_Drop\_Support |
| T1-8 | T-Input:Keyboard\_Parity | T-Keyboard\_Parity |
| T1-9 | T-Input:Combinations | T-Input\_Combinations |
| T1-10 | T-Input:Scrollbar | T-Scrollbar\_Display |
| T1-11 | T-Input:Hover\_Parity | T-Hover\_Parity |
| T1-12 | T-Input:Desktop\_Menus | T-Desktop\_Menus |
| T1-13 | T-Input:Panel\_Config | T-UI\_Config |
| T1-14 | T-Input:Triple\_Click | Triple\_Click |
| T1-15 | T-Stylus:Draw\_Write | T-Stylus\_Draw\_Write |
| T1-16 | T-Stylus:Drag\_Drop | T-Stylus\_Drag\_Drop |
| T1-17 | T-Stylus:Enhanced | T-Stylus\_Enhanced |
| T1-18 | T-Cursors:Custom | T-Custom\_Cursors |
|  |  | T-Camera\_Switcher |
|  |  | T-Audio\_Switcher |
|  |  | T-Media\_Background\_Playback |
|  |  | T-Request\_Fullscreen\_Mode |
|  |  | T-Printing\_Support |
|  |  | T-File\_Picker |
|  |  | T-File\_Management\_Basics |
|  |  | T-File\_Handlers |
|  |  | T-Cursor\_Target\_Size |
|  |  | T-Cross\_Device\_Handoff |
|  |  | T-Offline\_Support |
|  |  | T-Web\_Transition |