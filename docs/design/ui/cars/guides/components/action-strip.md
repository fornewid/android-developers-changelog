---
title: https://developer.android.com/design/ui/cars/guides/components/action-strip
url: https://developer.android.com/design/ui/cars/guides/components/action-strip
source: md.txt
---

# Action strip

The action strip lets users perform secondary or tertiary actions with a quick tap.

## Requirements

- Action strips allow up to two action[buttons](https://developer.android.com/design/ui/cars/guides/components/action-strip)(except for[templates with maps](https://developer.android.com/design/ui/cars/guides/components/action-strip#maps), which allow up to 4).
- Only one label button (with label and optional icon) is allowed per template.
- Button order is specified by the app.

![An action strip including volume and settings buttons](https://developer.android.com/static/images/design/ui/cars/components/action-strip-1.png)In the top right corner of this example, the action strip includes a volume button and a settings button.![Action strip including search and close buttons](https://developer.android.com/static/images/design/ui/cars/components/action-strip-2.png)In the top right corner of this example, the action strip includes a search button and a close button.

<br />

### Guidance

- Use action strips for secondary or tertiary actions, rather than primary actions -- except on the[Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template). For primary actions, use a[floating action button](https://developer.android.com/design/ui/cars/guides/components/fab)or a[button](https://docs.google.com/document/d/1NCMeVXohFZuqhOesvUJN8Z0UheF4_nz0iy90j0JwQ1I/edit?usp=sharing&resourcekey=0-rJNBveypEL9F_M7oxExtIw).
- For details about when the action strip is displayed on the Navigation template and when it's hidden, refer to[Visibility of action strips](https://developer.android.com/design/ui/cars/guides/components/action-strip#visibility).
- Don't include both an action strip and a floating action button at the same time.

| **Note:** Templates for navigation apps can also have a[map action strip](https://developer.android.com/design/ui/cars/guides/components/map-action-strip)with map interactivity buttons.

### Use the action strip on templates with maps

On templates with maps, the action strip can include up to 4 buttons, as shown in the following examples.
![Action strip with two buttons](https://developer.android.com/static/images/design/ui/cars/components/action-strip-3.png)The top right corner of this example shows an action strip with 2 buttons.![Action strip with three buttons](https://developer.android.com/static/images/design/ui/cars/components/action-strip-4.png)The top right corner of this example shows an action strip with 3 buttons.

## Visibility of action strips

The app library generally takes care of showing and hiding the action strip and map action strip in the map-based templates based on user interactions. See these examples:
![Mock-up of pan mode](https://developer.android.com/static/images/design/ui/cars/components/action-strip-5.png)When a map-based template opens, the action strip and map actionstrip are visible. If 10 seconds go by with no user interaction, and if the action strip and map action strip don't have user focus for rotary input, they disappear.![Mock-up of pan mode](https://developer.android.com/static/images/design/ui/cars/components/action-strip-6.png)When the action strip and map action strip are hidden, any user interaction with the screen will cause them to reappear.

<br />

### Exceptions

- Your Apps can flag actions in either action strip as persistent to keep them from disappearing.

- To minimize clutter, Car App Library may hide the action strip on small screens after 10 seconds even when there is rotary focus.