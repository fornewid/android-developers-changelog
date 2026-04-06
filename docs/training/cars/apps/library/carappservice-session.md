---
title: Create your CarAppService and Session  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/library/carappservice-session
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Create your CarAppService and Session Stay organized with collections Save and categorize content based on your preferences.



Your app must extend the [`CarAppService`](/reference/androidx/car/app/CarAppService) class and implement its
[`onCreateSession`](/reference/androidx/car/app/CarAppService#onCreateSession()) method, which returns a [`Session`](/reference/androidx/car/app/Session) instance that
corresponds to the current connection to the host:

### Kotlin

```
class HelloWorldService : CarAppService() {
  ...
  override fun onCreateSession(): Session {
      return HelloWorldSession()
  }
  ...
}
```

### Java

```
public final class HelloWorldService extends CarAppService {
  ...
  @Override
  @NonNull
  public Session onCreateSession() {
      return new HelloWorldSession();
  }
  ...
}
```

The `Session` instance returns which [`Screen`](/reference/androidx/car/app/Screen) instance to use when the app
is started for the first time:

### Kotlin

```
class HelloWorldSession : Session() {
  ...
  override fun onCreateScreen(intent: Intent): Screen {
      return HelloWorldScreen(carContext)
  }
  ...
}
```

### Java

```
public final class HelloWorldSession extends Session {
  ...
  @Override
  @NonNull
  public Screen onCreateScreen(@NonNull Intent intent) {
      return new HelloWorldScreen(getCarContext());
  }
  ...
}
```

When your car app must start from a screen that isn't the **Home** or
**Landing** screen, such as when handling deep links, you can use
[`ScreenManager.push`](/reference/androidx/car/app/ScreenManager#push(androidx.car.app.Screen)) before returning from [`onCreateScreen`](/reference/androidx/car/app/Session#onCreateScreen(android.content.Intent)) to
pre-seed a back stack of screens. Pre-seeding allows users to navigate back to
previous screens from the first screen displayed by your app.

[Previous

arrow\_back

Set up your project](/training/cars/apps/library/set-up-project)

[Next

Create your start screen

arrow\_forward](/training/cars/apps/library/start-screen)