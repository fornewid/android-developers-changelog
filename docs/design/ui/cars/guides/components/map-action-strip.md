---
title: Map action strip  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/components/map-action-strip
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Map action strip Stay organized with collections Save and categorize content based on your preferences.



The map action strip gives users access to map interactivity features. While
users can access these features through gestures on touchscreens, they also need
buttons to access interactivity features on screens with rotary and touchpad
inputs.

Buttons also add helpful visual clues. The map action strip includes up to 4 buttons:

* [Pan mode](#pan-mode)
  (required for apps that support user panning)
* Recenter
* Zoom-in
* Zoom-out

![Screen capture of the map action strip](/static/images/design/ui/cars/components/map-action-strip-1.png)


From top to bottom, this map action strip includes a pan button, a recenter
button, a zoom out button, and a zoom in button.

## Pan mode

In pan mode, only the full-screen map and map action strip buttons are visible.
Pan mode is used for rotary and touchpad inputs.

For the pan button, apps can provide 2 icons: one for entering pan mode, and one
for exiting. The icon for exiting pan mode should clearly indicate that it
provides a way to exit. For example, this button can show an X. Default icons
will be used if you don't provide any.

![Screen capture of a map showing the pan button](/static/images/design/ui/cars/components/map-action-strip-2.png)


Example of an action strip showing the pan button

**Note:** To enable user panning on all screen types, you must include a pan
button in the map action strip (even though the pan button does not display
on touch screens). Including the pan button causes touch gestures for map
interactivity to be forwarded to the app.

## Template support

All templates that include a map support the map action strip, except the
[Place List (map) template](/design/ui/cars/guides/templates/place-list-map-template), which is not intended for navigation apps.

## Guidance

Like the action strip, the map action strip disappears if 10 seconds go by
without user interaction, as described in [Visibility of action strips](/design/ui/cars/guides/components/action-strip#visibility).

**Note:** When using the map action strip, be sure not to draw other visual elements
away from in the lower-right corner of the map. On short screens, these elements
may cover the map action strip.