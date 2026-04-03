---
title: Design principles  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/patterns/media/principles
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Design principles Stay organized with collections Save and categorize content based on your preferences.



Design media experiences on Wear OS by applying core principles that prioritize
user control and efficiency.

## Consistent and predictable

Verify that users don't need to relearn interaction basics from one media UI to
another so that users can control media across different contexts.

Align UI patterns and avoid creating new UIs for common interactions.

![](/static/wear/images/design/media-music.png)

## Glanceable and critical

Help users complete tasks quickly by elevating critical controls and showing
correct status.

Display critical controls and content in a clear information hierarchy so that
users can control media browsing and playback on their watch.

Reflect the dynamic status, such as the current device volume or the connected
output device.

![](/static/wear/images/design/media-glanceable.png)

### Quick and consistent

Verify that users can quickly control media on the wrist.

Avoid hidden gestures or interaction patterns that require onboarding and
spatial memory capacity. Provide visual affordances inline that clearly guide
users to additional functionality.

Verify user journeys that involve system and app UI integrate seamlessly to
avoid duplicative screens for users to navigate between surfaces across
contexts.

![](/static/wear/images/design/media-quick-and-easy.png)

## Common design patterns

The following sections describe common design patterns for media experiences on
Wear OS.

### Overflow button

Use the overflow button to provide consistent navigation and more
functionalities.

![](/static/wear/images/design/media-overflow-dont.png)

**Don't**

Rely on hidden gestures that require users to memorize the navigation.

![](/static/wear/images/design/media-overflow-do.png)

**Do**

Provide visible overflow button to guide users to access additional
functionality.

### Consistent access to media options

Provide consistent access to functionality across media surfaces and contexts.

![](/static/wear/images/design/media-consistent-dont.png)

**Don't**

Inconsistent patterns for media controls across media surfaces and contexts
cause user confusion and cognitive load.

![](/static/wear/images/design/media-consistent-do.png)

**Do**

Provide consistent patterns across media surfaces and contexts.

### Volume control

Use the key volume control interaction such as tap affordance, volume bar, and
hardware controls to make sure critical volume tasks can be done.

![](/static/wear/images/design/media-volume-dont.png)

**Don't**

It's confusing when users can't control volume with the hardware.

![](/static/wear/images/design/media-volume-do.png)

**Do**

Let users control the volume with the hardware crown.

### Output device

Use an icon that clearly shows users which device they're using to listen to
media playback.

![](/static/wear/images/design/media-output-dont.png)

**Don't**

Icon doesn't reflect where will the sound come from and where to control volume

![](/static/wear/images/design/media-output-do.png)

**Do**

Reflect the output device status with the indication of volume controls

## Extend across devices

Consider cross-device consistency and use existing patterns for more predictable
and consistent user experience.

[
](/static/wear/images/design/media-better-together-hero.mp4)