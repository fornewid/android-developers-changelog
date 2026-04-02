---
title: https://developer.android.com/training/cars/apps/library/interact-map
url: https://developer.android.com/training/cars/apps/library/interact-map
source: md.txt
---

When using the following templates, you can add support for users to interact
with the maps you draw, such as letting them see different parts of a map by
zooming and panning.

| Template | Car App API level support |
|---|---|
| `NavigationTemplate` | 2 |
| `PlaceListNavigationTemplate` *(deprecated)* | 4 |
| `RoutePreviewNavigationTemplate` *(deprecated)* | 4 |
| `MapTemplate` *(deprecated)* | 5 *(template introduced)* |
| `MapWithContentTemplate` | 7 *(template introduced)* |

## Implement interactivity callbacks

The [`SurfaceCallback`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback) interface has several callback methods you can
implement to add interactivity to maps built with the templates in the preceding
section:

| Interaction | Method | Car App API level support |
|---|---|---|
| Tap | [`onClick`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onClick(float,%20float)) | 5 |
| Pinch to zoom | [`onScale`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScale(float,%20float,%20float)) | 2 |
| Single-touch drag | [`onScroll`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScroll(float,%20float)) | 2 |
| Single-touch fling | [`onFling`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onFling(float,%20float)) | 2 |
| Double-tap | [`onScale`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScale(float,%20float,%20float)) *(template host determines scale factor)* | 2 |
| Rotary nudge in pan mode | [`onScroll`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScroll(float,%20float)) *(template host determines distance factor)* | 2 |

## Add a map action strip

These templates can have a map action strip for map-related actions such as
zooming in and out, recentering, displaying a compass, and other actions you
choose to display. The map action strip can contain up to four icon-only buttons
that can be refreshed without affecting task depth. The action strip is
concealed when in the idle state and reappears in the active state.

To receive map [interactivity callbacks](https://developer.android.com/training/cars/apps/library/interact-map#interactivity-callbacks), you **must** add an `Action.PAN`
button in the map action strip. When the user presses the **Pan** button, the
host enters pan mode, as described in [Understand pan mode](https://developer.android.com/training/cars/apps/library/interact-map#pan-mode).

If your app omits the `Action.PAN` button in the map action strip, it doesn't
receive user input from the `SurfaceCallback` methods, and the host closes any
previously activated pan mode.

On a touchscreen, the **Pan** button isn't displayed.

## Understand pan mode

In pan mode, the template host translates user input from non-touch input
devices, such as rotary controllers and touchpads, into the appropriate
`SurfaceCallback` methods. Respond to the user action to enter or exit pan mode
with the [`setPanModeListener`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate.Builder#setPanModeListener(androidx.car.app.navigation.model.PanModeListener)) method in the `NavigationTemplate.Builder`.
The host can hide other UI components in the template while the user is in pan
mode.