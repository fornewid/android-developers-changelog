---
title: CarAppService, Session, and Screen lifecycles  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/library/lifecycles
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# CarAppService, Session, and Screen lifecycles Stay organized with collections Save and categorize content based on your preferences.




The [`Session`](/reference/androidx/car/app/Session) and [`Screen`](/reference/androidx/car/app/Screen) classes implement the [`LifecycleOwner`](/reference/androidx/lifecycle/LifecycleOwner)
interface. As the user interacts with the app, lifecycle callbacks of your
`Session` and `Screen` objects are invoked, as illustrated in Figures 1 and 2.

### CarAppService and Session lifecycles

To learn more, see the [`Session.getLifecycle`](/reference/androidx/car/app/Session#getLifecycle()) method.

![](/static/images/training/cars/carappservice-session-lifecycle.png)


**Figure 1**. Session lifecycle.

### Screen lifecycle

To learn more, see [`Screen.getLifecycle`](/reference/androidx/car/app/Screen#getLifecycle) method.

![](/static/images/training/cars/screen-lifecycle.png)


**Figure 2**. Screen lifecycle.

[Previous

arrow\_back

CarContext class](/training/cars/apps/library/carcontext-class)