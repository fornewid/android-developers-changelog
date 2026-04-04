---
title: Implement screen navigation  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/library/screen-navigation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Implement screen navigation Stay organized with collections Save and categorize content based on your preferences.




Apps often present a number of different screens, each possibly using
different templates the user can navigate through as they interact with
the interface.

The `ScreenManager` class provides a screen stack you can use to push screens
that can be popped automatically when the user selects a **Back** button on the
car screen or uses the hardware **Back** button available in some cars.

This code shows how to add a back action to a message template as well as an
action to push a new screen when selected by the user:

### Kotlin

```
val template = MessageTemplate.Builder("Hello world!")
     .setHeaderAction(Action.BACK)
     .addAction(
         Action.Builder()
             .setTitle("Next screen")
             .setOnClickListener { screenManager.push(NextScreen(carContext)) }
             .build())
     .build()
```

### Java

```
MessageTemplate template = new MessageTemplate.Builder("Hello world!")
    .setHeaderAction(Action.BACK)
    .addAction(
        new Action.Builder()
            .setTitle("Next screen")
            .setOnClickListener(
                () -> getScreenManager().push(new NextScreen(getCarContext())))
            .build())
    .build();
```

The [`Action.BACK`](/reference/androidx/car/app/model/Action#BACK()) object is a standard [`Action`](/reference/androidx/car/app/model/Action) that automatically
invokes [`ScreenManager.pop`](/reference/androidx/car/app/ScreenManager#pop()). This behavior can be overridden by using the
[`OnBackPressedDispatcher`](/reference/androidx/activity/OnBackPressedDispatcher) instance available from the `CarContext`.

To promote safe driving, the screen stack can consist of no more than five
screens. To learn more, see [Template restrictions](/training/cars/apps/library/template-restrictions).

[Previous

arrow\_back

Create your start screen](/training/cars/apps/library/start-screen)

[Next

Refresh the contents of a template

arrow\_forward](/training/cars/apps/library/refresh-template)