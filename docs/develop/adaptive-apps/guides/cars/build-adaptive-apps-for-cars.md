---
title: https://developer.android.com/develop/adaptive-apps/guides/cars/build-adaptive-apps-for-cars
url: https://developer.android.com/develop/adaptive-apps/guides/cars/build-adaptive-apps-for-cars
source: md.txt
---

[Android Auto](https://developer.android.com/training/cars#auto) and [Android Automotive OS](https://developer.android.com/training/cars#automotive-os) enable users to access apps on
car infotainment systems while cars are parked. Adapt your app for car displays
with just a few implementation changes.

## Key considerations for cars

- **Fixed screen orientation**: Car infotainment screens are in a fixed orientation---either landscape or portrait. Ensure your app supports both to accommodate different vehicle models.
- **Unique system UI and navigation**: Android Automotive OS can include custom system bars and navigation schemes. Gesture navigation is not supported, and back affordances may vary.
- **Irregular screens and cutouts**: Some vehicles have non-rectangular or irregularly shaped screens with unique cutouts. Use appropriate layout parameters to handle these safely.
- **System bars**: Car manufacturers can control whether apps are able to show or hide system bars to enter and exit immersive mode. Manufacturers can also control whether apps can set the color and translucency of system bars.
- **Offline scenarios**: Cars often have intermittent or no internet connectivity. Your app should remain functional in offline scenarios.
- **Safety and parked status**: Apps are primarily accessible when the car is parked. Ensure your UI is optimized for quick, clear interactions that suit a vehicle environment.

## Adaptation strategies

1. **Use window size classes** : Use [window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) to categorize displays as compact, medium, or expanded and adjust your layout accordingly.
2. **Implement multi-pane layouts** : For wider car displays, use [list-detail](https://developer.android.com/develop/adaptive-apps/guides/build-a-list-detail-layout) or other multi-pane patterns to make optimal use of the available width.
3. **Optimize for car resources** : Use the [`car`](https://developer.android.com/guide/topics/resources/providing-resources#UiModeQualifier) resource qualifier to provide layouts or configurations tailored specifically for the Automotive environment.
4. **Test on emulators**: First test your app compatibility on an Android Automotive OS emulator to identify car-specific UI issues.

## Learn more

For complete Android for Cars development guidance, see [Android for Cars
overview](https://developer.android.com/training/cars).