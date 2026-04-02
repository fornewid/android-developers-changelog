---
title: Adaptive differentiated  |  Large screens  |  Android Developers
url: https://developer.android.com/guide/topics/large-screens/tier-1-overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Large screens](https://developer.android.com/guide/topics/large-screens)
* [Guides](https://developer.android.com/guide/topics/large-screens/tier-3-overview)

# Adaptive differentiated Stay organized with collections Save and categorize content based on your preferences.




![Tier 1 adaptive differentiated icon](/static/images/docs/quality-guidelines/tier-1/tier_1_icon.png)

TIER 1 — The top-quality tier of the [Adaptive app quality guidelines](/docs/quality-guidelines/adaptive-app-quality/tier-1).

![Depiction of three tiers with the top tier, tier 1, highlighted.](/static/images/docs/quality-guidelines/tier-1/tier_1_header.png)

APPS DIFFERENTIATED FOR LARGE SCREENS create a user experience not possible on
small screen devices.

Large screen differentiated apps make multitasking and drag and drop convenient
and simple. Differentiated apps support the unique features of foldable devices,
like tabletop posture, for a user experience other types of devices can't match.

External keyboard, mouse, and trackpad support are on par with desktop
computers. Comprehensive stylus support makes the stylus an integral part of the
device.

## Do's and don'ts

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_do.png)

check\_circle

### Do

* Think big
* Design custom layouts and behaviors
* Make your app different from anything else

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/tier_1_dont.png)

cancel

### Don't

* Settle for less
* Design for just one or two device types
* Let your app be unremarkable

## Guidelines

Differentiate your app by following the Tier 1 guidelines.

---

### Desktop

Deliver a desktop experience on Android by supporting connected displays,
peripheral devices, and desktop functionality.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/user_experience_icon.svg)

#### [User experience](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_user_experience)

A top-quality user experience bridges the gap between mobile convenience and desktop power, enabling users to remain focused and productive.

Guidelines:

* [Scrollbar\_Display](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Scrollbar_Display)
* [Hover\_Parity](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Hover_Parity)
* [Desktop\_Menus](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Desktop_Menus)
* [UI\_Config](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#UI_Config)
* [Request\_Fullscreen\_Mode](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Request_Fullscreen_Mode)

#### What

App has adaptive, user-configurable layouts, including collapsible, reconfigurable panels. The app displays a scrollbar while content is being scrolled by a mouse or trackpad. UI elements display additional content such as previews and tooltips on hover. Users can display apps fullscreen.

#### Why

Expansive, configurable screen space and precision input provide a focused and adaptable workflow. Desktop-style UI elements allow users to stay on task without constant navigation.

#### How

For more about creating refined user experiences, see the [User experience](/guide/topics/large-screens/user-experience) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/pointer_icon.svg)

#### [Keyboard, mouse, and trackpad](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_keyboard_mouse_trackpad)

Provide full support for external input devices.

Guidelines:

* [Keyboard\_Navigation](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Keyboard_Navigation)
* [Keyboard\_Parity](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Keyboard_Parity)
* [Input\_Combinations](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Input_Combinations)
* [Triple\_Click](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Triple_Click)

#### What

App supports efficient navigation with a keyboard, including distinct, consistent focus states and initial focus on appropriate UI elements. The app provides keyboard shortcut parity with web and desktop versions and enhanced selection capabilities using keyboard and mouse or trackpad combinations.

#### Why

Give users all the input capabilities possible with keyboard, mouse, and trackpad.

#### How

To learn how to support advanced input capabilities, see the [Keyboard, mouse, and trackpad](/guide/topics/large-screens/keyboard-mouse-and-trackpad-tier-1) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/multitasking_multi-instance_icon.svg)

#### [Multitasking and multi-instance](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_multitasking_multi-instance)

Make users more productive with multitasking on large screens.

Guidelines:

* [Multitasking\_Scenarios](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multitasking_Scenarios)
* [Multitasking\_PiP](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multitasking_PiP)
* [Multi-Instance](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Multi-Instance)

#### What

App supports all multitasking modes, including multi‑window, multi‑instance, and picture‑in‑picture.

#### Why

Large screens provide plenty of display space for users to work with multiple apps simultaneously.

#### How

Learn how to include your app in multitasking in the [Multi-tasking and multi-instance](/guide/topics/large-screens/multitasking-and-multi-instance) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/drag_and_drop_icon.svg)

#### [Drag and drop](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_drag_drop)

The desktop environment is perfect for drag and drop interactions—within an app or, on Android 7.0 (API level 24) and higher, between apps in multi‑window mode.

Guidelines — [Drag\_Drop\_Support](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Drag_Drop_Support)

#### What

App supports drag and drop within the app and to and from other apps using touch input, mouse, trackpad, and stylus.

#### Why

Increase user productivity and engagement by adding drag and drop capabilities to your app.

#### How

See the [Drag and drop](/guide/topics/large-screens/drag-and-drop) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/printing_and_file_management_icon.svg)

#### [Printing and file management](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_printing_and_file_management)

Desktop users rely on efficient file access and the ability to produce printed or electronic documents.

Guidelines:

* [Printing\_Support](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Printing_Support)
* [File\_Management\_Basics](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#File_Management_Basics)
* [File\_Picker](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#File_Picker)
* [File\_Handlers](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#File_Handlers)

#### What

App provides support for document printing and exporting to PDF format. The app also implements file management functionality, integration with the OS file picker, and file handler declarations.

#### Why

Desktop productivity requires powerful, convenient file access and management along with the ability to output digital content to a variety of formats.

#### How

Learn how to work with files in the [Printing and file management](/guide/topics/large-screens/printing-file-management) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/cursors_icon.svg)

#### [Cursors](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_cursors)

Provide context and precision control for mouse, trackpad, and stylus interactions.

Guidelines — [Custom\_Cursors](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Custom_Cursors) and [Cursor\_Target\_Size](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Cursor_Target_Size)

#### What

App displays differentiating cursors such as an I-beam for text and resize handles for panels. Cursor target sizes match visual boundaries of UI components for high interactive precision.

#### Why

Differentiated cursors provide immediate feedback on how users can interact with UI elements, creating a refined and productive user experience.

#### How

See the [Cursors](/guide/topics/large-screens/custom-cursors) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/cross-device_icon.svg)

#### [Cross device](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_cross-device)

Continuity from device to device allows users to work seamlessly across their Android ecosystem.

Guidelines — [Cross\_Device\_Handoff](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Cross_Device_Handoff)

#### What

App allows users to start a task on one Android device and seamlessly transition to another by restoring a near-equivalent state.

#### Why

Users often work with multiple devices and expect a continuous, uninterrupted workflow.

#### How

Learn about cross-device development in the [Cross device](/guide/topics/large-screens/cross-device) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/offline_support_icon.svg)

#### [Offline support](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_offline_support)

Reliable offline functionality ensures productivity regardless of network availability.

Guidelines — [Offline\_Support](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Offline_Support)

#### What

App enables core functionality while offline and provides clear notifications of connection requirements and graceful degradation when online connectivity is limited or unavailable.

#### Why

Users expect to remain productive regardless of the quality or availability of their network connection.

#### How

Learn about building for app usage offline in the [Offline support](/guide/topics/large-screens/offline-support) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/app_to_web_icon.svg)

#### [App to web](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#t1_app_to_web)

Smooth transitions between app and web content maintain user flow and application context.

Guidelines — [Web\_Transition](/docs/quality-guidelines/adaptive-app-quality/experiences/desktop#Web_Transition)

#### What

App transitions smoothly between app content and related web content (and vice versa).

#### Why

Proper handling of deep links and web content avoids a fragmented user experience and maintains user focus.

#### How

Learn about handling web content in the [App to web](/guide/topics/large-screens/app-to-web) overview.

---

### Foldables

Differentiate your app by supporting the unique features of premium foldable
devices.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/foldables_icon.svg)

#### [Foldable postures and states](/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#t1_postures_states)

Large screen foldable devices are like a phone and tablet in one. Folding features such as tabletop posture and book posture offer new user experience possibilities.

Guidelines — [Foldables\_Postures](/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#Foldables_Postures) and [Foldables\_Camera](/docs/quality-guidelines/adaptive-app-quality/experiences/foldables#Foldables_Camera)

#### What

App supports all foldable postures, including tabletop posture, book posture, and dual display. App also supports dual‑screen devices.

#### Why

Differentiate your app by supporting the unique features of foldable devices.

#### How

Unfold the facts in the [Foldables](/guide/topics/large-screens/foldables) overview.

---

### Camera • audio

Enable engaging media experiences.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/camera_icon.svg)

#### [Camera](/docs/quality-guidelines/adaptive-app-quality/experiences/camera-audio#t1_camera)

Support for external cameras enables a professional photography and video experience.

Guidelines — [Camera\_Switcher](/docs/quality-guidelines/adaptive-app-quality/experiences/camera-audio#Camera_Switcher)

#### What

App includes switchers to toggle between the device's built-in cameras and external devices.

#### Why

Large screen users often connect cameras for meetings or content production.

#### How

Learn more about camera support in the [Camera • audio](/guide/topics/large-screens/camera-audio) overview.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/speaker_icon.svg)

#### [Audio](/docs/quality-guidelines/adaptive-app-quality/experiences/camera-audio#t1_audio)

Premium listening experiences are defined by a choice of available devices and uninterrupted playback and control across all windowing and device states.

Guidelines — [Audio\_Switcher](/docs/quality-guidelines/adaptive-app-quality/experiences/camera-audio#Audio_Switcher) and [Audio\_Background\_Playback](/docs/quality-guidelines/adaptive-app-quality/experiences/camera-audio#Audio_Background_Playback)

#### What

App supports switching between built‑in audio devices, such as a speaker or microphone, and connected devices. The app also supports background playback when minimized or behind other windows or the device screen is locked.

#### Why

Users expect audio apps to support peripheral devices and continue playing as users manage other windowing tasks.

#### How

See the [Camera • audio](/guide/topics/large-screens/camera-audio) overview.

---

### Stylus

Support the natural feel of stylus interactions for creativity and productivity
tasks.

![](/static/images/guide/topics/large-screens/quality-guidelines/tier-1/stylus_advanced_icon.svg)

#### [Stylus support](/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#t1_stylus)

Top-tier apps support stylus-equipped devices. A stylus enables users to draw, write, erase, and work with your app using a variety of touch and gesture interactions.

Guidelines:

* [Stylus\_Draw\_Write](/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#Stylus_Draw_Write)
* [Stylus\_Drag\_Drop](/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#Stylus_Drag_Drop)
* [Stylus\_Enhanced](/docs/quality-guidelines/adaptive-app-quality/experiences/stylus#Stylus_Enhanced)

#### What

App provides stylus support for drawing, writing, erasing, drag and drop, pressure sensitivity, tilt detection, and palm and finger rejection.

#### Why

Provide an exceptional user experience on premium devices. Enhance user productivity and satisfaction.

#### How

For guidance about advanced stylus support, see the [Stylus](/guide/topics/large-screens/stylus-tier-1) overview.