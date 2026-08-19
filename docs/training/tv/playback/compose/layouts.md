---
title: https://developer.android.com/training/tv/playback/compose/layouts
url: https://developer.android.com/training/tv/playback/compose/layouts
source: md.txt
---

A TV screen is typically viewed from about 10 feet away, and while it is much
larger than most other Android-powered device displays, a TV screen does not
provide the same level of detail and color as a smaller device screen. These
factors require you to create app layouts with TV devices in mind to create a
useful and enjoyable living-room user experience.

## Basic layout principles

Layouts for TV devices must follow some basic guidelines to help ensure that
they are usable and effective on large screens. Follow these tips to build
layouts optimized for TV screens:

- Build layouts with a landscape orientation. TV screens always display in landscape mode.
- Put on-screen navigation controls on the left or right side of the screen and save the vertical space for content.
- Use responsive and relative sizing (such as `dp` and `sp` units) so that user interfaces scale cleanly across different display resolutions.
- Add sufficient margins and padding between layout controls to avoid a cluttered UI.

## Overscan

Layouts for TV have some unique requirements due to the evolution of TV
standards to present a full-screen picture to viewers. For this reason, TV
devices might clip the outside edge of an app layout to ensure that the entire
display is filled. This behavior is generally referred to as *overscan*.

Position screen elements that must be visible to the user at all times within
the overscan-safe area. Adding a 5% margin of 48 dp on the left and right edges
and 27 dp on the top and bottom edges to a layout helps ensure that screen
elements in the layout are within the overscan-safe area.

Don't adjust background screen elements that the user doesn't directly interact
with, and don't clip the elements to the overscan-safe area. This approach helps
ensure that background screen elements look correct on all screens.

## Build usable text and controls

Follow these tips to make the text and controls in your TV app easier to see
from a distance:

- Break text into small chunks that users can quickly scan.
- Use light text on a dark background. This style is easier to read on a TV.
- Avoid lightweight fonts or fonts that have both very narrow and very broad strokes. Use sans-serif fonts and anti-aliasing to increase readability.
- Make all your view widgets large enough to be clearly visible to someone sitting 10 feet away from the screen. Use density-independent pixel (`dp`) units instead of absolute pixel units, and scalable pixel (`sp`) units for typography.

For more information about density-independent pixels and building layouts to
handle larger screen sizes, see [Screen compatibility overview](https://developer.android.com/guide/practices/screens_support).

## Manage layout resources for TV

Like all other Android devices, TVs have different screen sizes and support
different resolutions, including 720p, 1080p, and 4K. Make sure your app
[supports different screen sizes](https://developer.android.com/training/multiscreen/screensizes).

Different screen sizes and resolutions have different pixel densities. To
preserve the appearance of your UI across screen sizes, resolutions, and pixel
densities, define UI measurements using density-independent pixels (`dp`). The
screen pixel density for different TV panel resolutions is outlined in the
following table:

| Panel resolution | Screen pixel density |
|---|---|
| 720p | `tvdpi` |
| 1080p | `xhdpi` |
| 4K | `xxxhdpi` |

See [Support different pixel densities](https://developer.android.com/training/multiscreen/screendensities) and the
[Screen compatibility overview](https://developer.android.com/training/multiscreen) for more information.

## Layout patterns to avoid

There are a few approaches to building layouts that don't work well on TV
devices. Avoid the following user interface patterns when developing a layout
for TV:

- **Re-using phone or tablet layouts**: Don't reuse layouts from a phone or tablet app without modification. Layouts built for other Android device form factors are not well suited for TV devices and must be simplified for operation on a TV.
- **Using phone action bars or menus**: Top action bars and pull-down menus are not appropriate for a TV interface due to the difficulty in navigating such menus with a remote control.
- **Using swipe-only navigation**: Sliding or swiping between screens can work great on a phone or tablet, but don't try swipe-only gestures on a TV where users rely on a D-pad remote.

For more information about designing layouts that are appropriate to TV, see
[Designing for TV](https://developer.android.com/design/ui/tv).

## Handle large bitmaps

TV devices have limited memory. If your app layout uses very high-resolution
images, it can quickly run into memory limits and cause out-of-memory errors.
Use efficient image loading and decoding libraries (such as [Coil](https://coil-kt.github.io/coil/) or
[Glide](https://github.com/bumptech/glide)) to fetch, decode, and display bitmaps in your app.

For more information about getting the best performance when working with bitmaps,
refer to [Android graphics best practices](https://developer.android.com/topic/performance/graphics).

## Provide effective advertising

For the living-room environment, we recommend using video ad solutions that are
full-screen and dismissable within 30 seconds. Functionality for advertising on
Android TV, such as dismiss buttons and click throughs, must be accessible using
the D-pad rather than touch.

Android TV does not provide a web browser. Your ads must not attempt to launch a
web browser or redirect to Google Play Store content that is not approved for
Android TV devices.

> [!NOTE]
> **Note:** You can use the [`WebView`](https://developer.android.com/reference/android/webkit/WebView) class for logins to social media services.