---
title: https://developer.android.com/training/cars/apps/library/screen-navigation
url: https://developer.android.com/training/cars/apps/library/screen-navigation
source: md.txt
---

Apps often present a number of different screens, each possibly using
different templates the user can navigate through as they interact with
the interface.

The `ScreenManager` class provides a screen stack you can use to push screens
that can be popped automatically when the user selects a **Back** button on the
car screen or uses the hardware **Back** button available in some cars.

This code shows how to add a back action to a message template as well as an
action to push a new screen when selected by the user:  

### Kotlin

    val template = MessageTemplate.Builder("Hello world!")
         .setHeaderAction(Action.BACK)
         .addAction(
             Action.Builder()
                 .setTitle("Next screen")
                 .setOnClickListener { screenManager.push(NextScreen(carContext)) }
                 .build())
         .build()

### Java

    MessageTemplate template = new MessageTemplate.Builder("Hello world!")
        .setHeaderAction(Action.BACK)
        .addAction(
            new Action.Builder()
                .setTitle("Next screen")
                .setOnClickListener(
                    () -> getScreenManager().push(new NextScreen(getCarContext())))
                .build())
        .build();

The [`Action.BACK`](https://developer.android.com/reference/androidx/car/app/model/Action#BACK()) object is a standard [`Action`](https://developer.android.com/reference/androidx/car/app/model/Action) that automatically
invokes [`ScreenManager.pop`](https://developer.android.com/reference/androidx/car/app/ScreenManager#pop()). This behavior can be overridden by using the
[`OnBackPressedDispatcher`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher) instance available from the `CarContext`.

To promote safe driving, the screen stack can consist of no more than five
screens. To learn more, see [Template restrictions](https://developer.android.com/training/cars/apps/library/template-restrictions).