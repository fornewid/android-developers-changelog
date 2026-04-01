---
title: Add an Up action  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/components/appbar/up-action
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add an Up action Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.

[Navigate from top app bar →](https://developer.android.com/develop/ui/compose/components/app-bars-navigate)

![](/static/images/android-compose-ui-logo.png)

Users need an easy way to get back to your app's main screen. To do this, provide an *Up*
button ![](/static/images/guide/navigation/up-button.png) on the app bar
for all activities except the main one. When the user selects the Up button, the app navigates to
the parent activity.

This page shows you how to add an Up button to an app bar using the Jetpack Navigation component.
For a more detailed explanation, see
[Update UI components with NavigationUI](/guide/navigation/navigation-ui).

**Note:** We recommend using the Jetpack Navigation component to handle your app navigation.
This component handles navigating up from the current screen in your app when the user taps the Up
button. To learn more, see the documentation for the
[Jetpack Navigation component](/guide/navigation).

## Configure your app bar

Configure your app bar using an
`AppBarConfiguration`.
From the `AppBarConfiguration`, you can inform the app bar of your top-level
destinations. If the navigation drawer is configured, the drawer menu icon
![](/static/images/guide/navigation/drawer-icon.png) displays on the app
bar on top-level destinations. If the navigation drawer isn't configured, the navigation button is
hidden on top-level destinations.

In both cases, the Up button displays on all other destinations. Pressing the Up button calls
`navigateUp()`.

The following example shows how to configure an app bar using
`AppBarConfiguration`:

### Kotlin

```
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

```
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