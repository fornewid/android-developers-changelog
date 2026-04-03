---
title: https://developer.android.com/develop/ui/views/components/appbar/up-action
url: https://developer.android.com/develop/ui/views/components/appbar/up-action
source: md.txt
---

# Add an Up action

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.  
[Navigate from top app bar →](https://developer.android.com/develop/ui/compose/components/app-bars-navigate)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Users need an easy way to get back to your app's main screen. To do this, provide an*Up* button![](https://developer.android.com/static/images/guide/navigation/up-button.png)on the app bar for all activities except the main one. When the user selects the Up button, the app navigates to the parent activity.

This page shows you how to add an Up button to an app bar using the Jetpack Navigation component. For a more detailed explanation, see[Update UI components with NavigationUI](https://developer.android.com/guide/navigation/navigation-ui).
| **Note:** We recommend using the Jetpack Navigation component to handle your app navigation. This component handles navigating up from the current screen in your app when the user taps the Up button. To learn more, see the documentation for the[Jetpack Navigation component](https://developer.android.com/guide/navigation).

## Configure your app bar

Configure your app bar using an[AppBarConfiguration](https://developer.android.com/reference/androidx/navigation/ui/AppBarConfiguration). From the`AppBarConfiguration`, you can inform the app bar of your top-level destinations. If the navigation drawer is configured, the drawer menu icon![](https://developer.android.com/static/images/guide/navigation/drawer-icon.png)displays on the app bar on top-level destinations. If the navigation drawer isn't configured, the navigation button is hidden on top-level destinations.

In both cases, the Up button displays on all other destinations. Pressing the Up button calls[navigateUp()](https://developer.android.com/reference/androidx/navigation/NavController#navigateUp()).

The following example shows how to configure an app bar using`AppBarConfiguration`:  

### Kotlin

```kotlin
  override fun onCreate(savedInstanceState: Bundle?) {
    ...
    val navController = findNavController(R.id.nav_host_fragment_activity_main)
    
    val appBarConfiguration = AppBarConfiguration(
        setOf(
            R.id.navigation_home, R.id.navigation_dashboard, R.id.navigation_notifications
        )
    )
    binding.myToolbar.setupWithNavController(navController, appBarConfiguration)
  }
  
```

### Java

```java
  @Override
  protected void onCreate(Bundle savedInstanceState) {
      ...
      NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_activity_main);

      AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
              R.id.navigation_home, R.id.navigation_dashboard, R.id.navigation_notifications)
              .build();
      NavigationUI.setupWithNavController(binding.myToolbar, navController, appBarConfiguration);
  }
  
```