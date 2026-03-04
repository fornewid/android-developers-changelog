---
title: https://developer.android.com/design/ui/desktop/guides/system/multi-task
url: https://developer.android.com/design/ui/desktop/guides/system/multi-task
source: md.txt
---

Desktop windowing allows users to multitask seamlessly in a free-form
environment.

## Multi-instance

Desktop users often keep multiple windows of the same app open. Android allows
users to quickly switch between them using the keyboard shortcut Alt + Tab.
![Users can switch between app with multi-instance.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_pattern_multi-instance.webp)

If suitable for your app, consider multi-instance support to increase user
productivity on desktop. For developer guides, read more at [multitasking and
multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance).

## Drag-and-drop

On a desktop, users can move data between apps and the OS. Use
drag-and-drop interactions to make this process more intuitive in a multi-window
environment. For design guidance, see Patterns. Learn how to implement with
[drag-and-drop](https://developer.android.com/guide/topics/large-screens/drag-and-drop).
![Drag and drop on laptop.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop-pattern-drag-modal.webp)

## Media playback

Media playback should continue when users minimize the app or move it to the
background. To further enhance the experience, implement picture-in-picture
(PiP) mode, which allows them to watch videos in a floating window while
navigating between apps or browsing content. PiP windows can display controls
for play, pause, previous, and next. For more details, [picture-in-picture](https://developer.android.com/design/ui/mobile/guides/home-screen/picture-in-picture).
![Picture-in-picture modal on tablet.](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_pattern_pip.webp)