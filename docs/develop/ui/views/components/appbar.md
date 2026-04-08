---
title: Add the app bar  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/components/appbar
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add the app bar Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.

[App Bar →](https://developer.android.com/develop/ui/compose/components/app-bars)

![](/static/images/android-compose-ui-logo.png)

The *app bar*, also known as the *action bar*, is one of the most important design
elements in your app's activities, because it provides a visual structure and interactive elements
that are familiar to users. Using the app bar makes your app consistent with other Android apps,
letting users quickly understand how to operate your app and have a great experience.

**Note:** With the release of Android 9.0 (API level 28), there is a version of the Support
Library called [AndroidX](/jetpack/androidx) that is part of
[Jetpack](/jetpack). The AndroidX library contains the existing Support Library and
includes Jetpack components.
  
  
You can continue to use the Support Library. Historical artifacts—those versioned 27 and
earlier, and packaged as `android.support.*`—remain available on Google Maven.
However, all newer library development occurs in the AndroidX library.
  
  
We recommend using the AndroidX libraries in all new projects. Consider
[migrating](/jetpack/androidx/migrate) existing projects to AndroidX as well.

The key functions of the app bar are as follows:

* Dedicated space for giving your app an identity and indicating the user's location in the
  app.
* Predictable access to important actions, such as search.
* Support for navigation and view switching, using tabs or menus.

![An image showing a green app bar, with hamburger menu, and three action icons](/static/images/training/appbar/appbar_sheets_2x.png)


**Figure 1.** The app bar from the Google Sheets app.

This documentation section describes how to use the AndroidX
`Toolbar` widget as an
app bar. There are other ways to implement an app bar—for example, some themes set up an
`ActionBar` as an app bar by
default—but using the AppCompat `Toolbar` makes it easier to set up an app bar that
works on the widest range of devices. It also gives you room to customize your app bar later in your
app's development.

## Topics

**[Set up the app bar](/develop/ui/views/components/appbar/setting-up)**
:   Learn how to add a `Toolbar` widget to your activity and set it as the activity's
    app bar.

**[Add and handle actions](/develop/ui/views/components/appbar/actions)**
:   Learn how to add actions to the app bar and its overflow menu, and how to respond when users
    choose those actions.

**[Add an Up action](/develop/ui/views/components/appbar/up-action)**
:   Learn how to add an *Up* button to your app bar so users can navigate back to the app's
    home screen.

**[Use action views and action providers](/develop/ui/views/components/appbar/action-views)**
:   Learn how to use these widgets to provide advanced functionality in your app bar.