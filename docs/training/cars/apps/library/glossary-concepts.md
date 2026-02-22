---
title: https://developer.android.com/training/cars/apps/library/glossary-concepts
url: https://developer.android.com/training/cars/apps/library/glossary-concepts
source: md.txt
---

This terminology and these concepts are used throughout this section.

`CarAppService`
:   [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService) is an abstract [`Service`](https://developer.android.com/reference/android/app/Service) class that your app
    must implement and export to be discovered and managed by the host.
    Your app's `CarAppService` uses [`createHostValidator`](https://developer.android.com/reference/androidx/car/app/CarAppService#createHostValidator()) to validate that
    a host connection can be trusted and, subsequently, uses
    [`onCreateSession`](https://developer.android.com/reference/androidx/car/app/CarAppService#onCreateSession()) to provide [`Session`](https://developer.android.com/reference/androidx/car/app/Session) instances for each
    connection.

Host

:   The host is the backend component that implements the functionality offered
    by the library's APIs so your app can run in the car. The host provides a
    range of services, from discovering your app and managing its lifecycle to
    converting your models into views and notifying your app of user
    interactions.

    On mobile devices, this host is implemented by Android Auto. On Android
    Automotive OS, this host is installed as a system app.

Models and templates

:   The user interface is represented by a graph of model objects you can
    arrange together in different ways, per the template to which they belong.
    Templates are a subset of the models that act as a root in the
    graphs.

    Models include the information to be displayed to the user in the
    form of text and images as well as attributes to configure aspects of the
    visual appearance of such information. For example, text colors or
    image sizes.

    The host converts the models to views that meet driver distraction standards
    and address details such as the variety of car screen factors and input
    modalities.

`Screen`

:   [`Screen`](https://developer.android.com/reference/androidx/car/app/Screen) is a class provided by the library that apps implement to
    manage the user interface visible to the user.

    A `Screen` has a [lifecycle](https://developer.android.com/training/cars/apps/library/lifecycles#screen-lifecycle) and is used by the app to send the template
    to display when the screen is visible. `Screen` instances can also be pushed
    and popped to and from a [`Screen` stack](https://developer.android.com/training/cars/apps/library/template-restrictions) to confirm they meet
    [template flow restrictions](https://developer.android.com/training/cars/apps/library/template-restrictions).

`Session`

:   [`Session`](https://developer.android.com/reference/androidx/car/app/Session) is an abstract class that your app must implement and return
    using `CarAppService.onCreateSession`. A `Session` serves as the entry point
    to display information on the car screen. `Session` has a [lifecycle](https://developer.android.com/training/cars/apps/library/lifecycles)
    that informs the current state of your app on the car screen, such as when
    your app is visible or hidden.

    When a `Session` is started, such as when the app is first launched, the
    host uses the [`onCreateScreen`](https://developer.android.com/reference/androidx/car/app/Session#onCreateScreen(android.content.Intent)) method to ask which initial `Screen`
    to display.

Template restrictions

:   Different templates enforce restrictions in the content of their models. For
    example, list templates impose limits on the number of items that can be
    presented to the user.

    Templates also have restrictions in the way they can be connected to form
    the flow of a task. For example, an app can push up to five templates
    to the screen stack. To learn more, see [Template restrictions](https://developer.android.com/training/cars/apps/library/template-restrictions).