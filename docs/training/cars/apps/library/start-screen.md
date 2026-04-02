---
title: Create your start screen  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/library/start-screen
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Create your start screen Stay organized with collections Save and categorize content based on your preferences.



To create the screens displayed by your app, you define the classes that extend
the `Screen` class and implement its [`onGetTemplate`](/reference/androidx/car/app/Screen#onGetTemplate()) method to return the
[`Template`](/reference/androidx/car/app/model/Template) instance that represents the state of the UI to display in the
car screen.

This code snippet shows how to declare a `Screen` that uses a
[`PaneTemplate`](/reference/androidx/car/app/model/PaneTemplate) template to display a "Hello world!" string:

### Kotlin

```
class HelloWorldScreen(carContext: CarContext) : Screen(carContext) {
    override fun onGetTemplate(): Template {
        val row = Row.Builder().setTitle("Hello world!").build()
        val pane = Pane.Builder().addRow(row).build()
        return PaneTemplate.Builder(pane)
            .setHeaderAction(Action.APP_ICON)
            .build()
    }
}
```

### Java

```
public class HelloWorldScreen extends Screen {
    @NonNull
    @Override
    public Template onGetTemplate() {
        Row row = new Row.Builder().setTitle("Hello world!").build();
        Pane pane = new Pane.Builder().addRow(row).build();
        return new PaneTemplate.Builder(pane)
            .setHeaderAction(Action.APP_ICON)
            .build();
    }
}
```

[Previous

arrow\_back

Create your CarAppService and session](/training/cars/apps/library/carappservice-session)

[Next

Implement screen navigation

arrow\_forward](/training/cars/apps/library/screen-navigation)