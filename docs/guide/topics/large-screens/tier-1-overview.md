---
title: https://developer.android.com/guide/topics/large-screens/tier-1-overview
url: https://developer.android.com/guide/topics/large-screens/tier-1-overview
source: md.txt
---

![Tier 1 adaptive differentiated icon](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_icon.png)

TIER 1 --- The top-quality tier of the [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) guidelines.

![Depiction of three tiers with the top tier, tier 1, highlighted.](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_header.png)

APPS DIFFERENTIATED FOR LARGE SCREENS create a user experience not possible on
small screen devices.

Large screen differentiated apps make multitasking and drag and drop convenient
and simple. Differentiated apps support the unique features of foldable devices,
like tabletop posture, for a user experience other types of devices can't match.

External keyboard, mouse, and trackpad support are on par with desktop
computers. Comprehensive stylus support makes the stylus an integral part of the
device.

## Do's and don'ts

![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_do.png)  
check_circle

### Do

- Think big
- Design custom layouts and behaviors
- Make your app different from anything else  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_dont.png)  
cancel

### Don't

- Settle for less
- Design for just one or two device types
- Let your app be unremarkable

## Guidelines

Differentiate your app by following the Tier 1 guidelines.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/multitasking_multi-instance_icon.svg)  

### [Multitasking and multi-instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t1_multitasking_multi-instance)

Make users more productive with multitasking on large screens.

Guidelines --- [Multitasking:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multitasking:Support) and [Multitasking:Multi-Instance](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Multitasking:Multi-Instance)  

#### What

App supports all multitasking modes, including multi‑window, multi‑instance, and picture‑in‑picture.  

#### Why

Large screens provide plenty of display space for users to work with multiple apps simultaneously.  

#### How

Learn how to include your app in multitasking in the [Multi-tasking and multi-instance](https://developer.android.com/guide/topics/large-screens/multitasking-and-multi-instance) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/foldables_icon.svg)  

### [Foldable postures and states](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t1_foldable_postures_states)

Large screen foldable devices are like a phone and tablet in one. Folding features such as tabletop posture and book posture offer new user experience possibilities.

Guidelines --- [Foldables:Postures](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Foldables:Postures) and [Foldables:Camera](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Foldables:Camera)  

#### What

App supports all foldable postures, including tabletop posture, book posture, and dual display. App also supports dual‑screen devices.  

#### Why

Differentiate your app by supporting the unique features of foldable devices.  

#### How

Unfold the facts in the [Foldable postures and states](https://developer.android.com/guide/topics/large-screens/foldable-postures-and-states) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/drag_and_drop_icon.svg)  

### [Drag and drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t1_drag_drop)

Large screens are perfect for drag and drop interactions---within an app or, on Android 7.0 (API level 24) and higher, between apps in multi‑window mode.

Guidelines --- [Drag_Drop:Support](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Drag_Drop:Support)  

#### What

App supports drag and drop within the app and to and from other apps using touch input, mouse, trackpad, and stylus.  

#### Why

Increase user productivity and engagement by adding drag and drop capabilities to your app.  

#### How

See the [Drag and drop](https://developer.android.com/guide/topics/large-screens/drag-and-drop) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/pointer_icon.svg)  

### [Keyboard, mouse, and trackpad](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t1_keyboard_mouse_trackpad)

Provide full support for external input devices.  
Guidelines:

- [Input:Keyboard_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Keyboard_Parity)
- [Input:Combinations](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Combinations)
- [Input:Scrollbar](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Scrollbar)
- [Input:Hover_Parity](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Hover_Parity)
- [Input:Desktop_Menus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Desktop_Menus)
- [Input:Panel_Config](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Panel_Config)
- [Input:Triple_Click](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Input:Triple_Click)  

#### What

App provides keyboard shortcut parity with web and desktop versions, including <kbd>Ctrl</kbd>+click or <kbd>Ctrl</kbd>+tap and <kbd>Shift</kbd>+click or <kbd>Shift</kbd>+tap for enhanced capabilities. App displays a scrollbar for content scrolled using a mouse or trackpad. Users can resize and reconfigure UI panels using a mouse or trackpad. Mouse and trackpad hover activates fly‑out menus or tooltips.  

#### Why

Give users all the input capabilities possible with keyboard, mouse, and trackpad.  

#### How

To learn how to support advanced input capabilities, see the [Keyboard, mouse, and trackpad](https://developer.android.com/guide/topics/large-screens/keyboard-mouse-and-trackpad-tier-1) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/stylus_advanced_icon.svg)  

### [Stylus](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t1_stylus)

Top-tier apps support stylus-equipped devices. A stylus enables users to draw, write, erase, and work with your app using a variety of touch and gesture interactions.  
Guidelines:

- [Stylus:Draw_Write](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Draw_Write)
- [Stylus:Drag_Drop](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Drag_Drop)
- [Stylus:Enhanced](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Stylus:Enhanced)  

#### What

App provides stylus support for drawing, writing, erasing, drag and drop, pressure sensitivity, tilt detection, and palm and finger rejection.  

#### Why

Provide an exceptional user experience on premium devices. Enhance user productivity and satisfaction.  

#### How

For guidance about advanced stylus support, see the [Stylus](https://developer.android.com/guide/topics/large-screens/stylus-tier-1) overview.  
![](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-1/custom_cursors_icon.svg)  

### [Custom cursors](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#t1_custom_cursors)

Provide context for mouse, trackpad, and stylus interactions.

Guidelines --- [Cursors:Custom](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Cursors:Custom)  

#### What

App displays customized cursors such as an I-beam for text, resize handles for resizable panels, processing spinners.  

#### Why

Create a refined user experience that's pleasing as well as productive.  

#### How

See the [Custom cursors](https://developer.android.com/guide/topics/large-screens/custom-cursors) overview.