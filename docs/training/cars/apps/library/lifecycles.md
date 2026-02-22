---
title: https://developer.android.com/training/cars/apps/library/lifecycles
url: https://developer.android.com/training/cars/apps/library/lifecycles
source: md.txt
---

The [`Session`](https://developer.android.com/reference/androidx/car/app/Session) and [`Screen`](https://developer.android.com/reference/androidx/car/app/Screen) classes implement the [`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)
interface. As the user interacts with the app, lifecycle callbacks of your
`Session` and `Screen` objects are invoked, as illustrated in Figures 1 and 2.

### CarAppService and Session lifecycles

To learn more, see the [`Session.getLifecycle`](https://developer.android.com/reference/androidx/car/app/Session#getLifecycle()) method.
![](https://developer.android.com/static/images/training/cars/carappservice-session-lifecycle.png) **Figure 1**. Session lifecycle.

### Screen lifecycle

To learn more, see [`Screen.getLifecycle`](https://developer.android.com/reference/androidx/car/app/Screen#getLifecycle) method.
![](https://developer.android.com/static/images/training/cars/screen-lifecycle.png) **Figure 2**. Screen lifecycle.