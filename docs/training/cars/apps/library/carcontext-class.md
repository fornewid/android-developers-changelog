---
title: https://developer.android.com/training/cars/apps/library/carcontext-class
url: https://developer.android.com/training/cars/apps/library/carcontext-class
source: md.txt
---

The [`CarContext`](https://developer.android.com/reference/androidx/car/app/CarContext) class extends [`ContextWrapper`](https://developer.android.com/reference/android/content/ContextWrapper), making it accessible
to your `Session` and `Screen` instances. `CarContext` provides access to
essential car services, including the:

- [`ScreenManager`](https://developer.android.com/reference/androidx/car/app/ScreenManager), to manage the [screen stack](https://developer.android.com/training/cars/apps/library/template-restrictions).
- [`AppManager`](https://developer.android.com/reference/androidx/car/app/AppManager), to get general app-related functionality, such as accessing the `Surface` object for [drawing maps](https://developer.android.com/training/cars/apps/library/draw-maps).
- [`NavigationManager`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager), used by turn-by-turn navigation apps to communicate [navigation metadata](https://developer.android.com/training/cars/apps/navigation#navigation-metadata) and other [navigation-related events](https://developer.android.com/training/cars/apps/navigation#starting-ending-stopping-navigation) with the host.

To see a list of library functionality available to navigation apps,
see [Access the navigation templates](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates).

`CarContext` also offers other functionality, such as letting you load drawable
resources by using the configuration from the car screen and signaling that
your app should display its map in [dark theme](https://developer.android.com/training/cars/apps/library/draw-maps#dark-theme).