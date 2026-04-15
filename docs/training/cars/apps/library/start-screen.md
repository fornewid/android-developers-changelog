---
title: https://developer.android.com/training/cars/apps/library/start-screen
url: https://developer.android.com/training/cars/apps/library/start-screen
source: md.txt
---

To create the screens displayed by your app, you define the classes that extend
the `Screen` class and implement its [`onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate()) method to return the
[`Template`](https://developer.android.com/reference/androidx/car/app/model/Template) instance that represents the state of the UI to display in the
car screen.

This code snippet shows how to declare a `Screen` that uses a
[`PaneTemplate`](https://developer.android.com/reference/androidx/car/app/model/PaneTemplate) template to display a "Hello world!" string:


```kotlin
class MyStartScreen(carContext: CarContext) : Screen(carContext) {
    override fun onGetTemplate(): Template {
        val row = Row.Builder().setTitle("Hello world!").build()
        val pane = Pane.Builder().addRow(row).build()
        val header = Header.Builder()
            .setStartHeaderAction(Action.APP_ICON)
            .build()
        return PaneTemplate.Builder(pane)
            .setHeader(header)
            .build()
    }
}
```

<br />