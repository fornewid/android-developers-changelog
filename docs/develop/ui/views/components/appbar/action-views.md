---
title: https://developer.android.com/develop/ui/views/components/appbar/action-views
url: https://developer.android.com/develop/ui/views/components/appbar/action-views
source: md.txt
---

# Use action views and action providers

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.  
[App bar →](https://developer.android.com/develop/ui/compose/components/app-bars)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)
| **Note:** For a better approach and user experience, consider gradually migrating your projects to[Jetpack Compose](https://developer.android.com/jetpack/compose/migrate/strategy).

The[AndroidX](https://developer.android.com/jetpack/androidx)library's[Toolbar](https://developer.android.com/reference/androidx/appcompat/widget/Toolbar)provides different ways for users to interact with your app.[Add and handle actions](https://developer.android.com/develop/ui/views/components/appbar/actions)describes how to define an*action*, which can be a button or a menu item. This document describes how to add two versatile components:

- An*action view*is an action that provides rich functionality within the app bar. For example, a search action view lets the user type their search text in the app bar without having to change activities or fragments.
- An*action provider*is an action with its own customized layout. The action initially appears as a button or menu item; when the user taps the action, the action provider controls the action's behavior any way you define. For example, the action provider might respond to a tap by displaying a menu.

AndroidX provides several specialized action view and action provider widgets. For example, the[SearchView](https://developer.android.com/reference/androidx/appcompat/widget/SearchView)widget implements an action view for entering search queries. The[ShareActionProvider](https://developer.android.com/reference/androidx/appcompat/widget/ShareActionProvider)widget implements an action provider for sharing information with other apps. You can also define your own action views and action providers.

## Add an action view

To add an action view, create an[`<item>`](https://developer.android.com/guide/topics/resources/menu-resource#item-element)element in the toolbar's menu resource, as described in[Add and handle actions](https://developer.android.com/develop/ui/views/components/appbar/actions). Add one of the following attributes to the`<item>`element:

- `actionViewClass`: the class of a widget that implements the action
- `actionLayout`: a layout resource describing the action's components

Set the`showAsAction`attribute to`"ifRoom|collapseActionView"`or`"never|collapseActionView"`. The`collapseActionView`flag indicates how to display the widget when the user isn't interacting with it. If the widget is on the app bar, the app displays the widget as an icon. If the widget is in the overflow menu, the app displays the widget as a menu item. When the user interacts with the action view, it expands to fill the app bar.

For example, the following code adds a`SearchView`widget to the app bar:  

```xml
<item android:id="@+id/action_search"
     android:title="@string/action_search"
     android:icon="@drawable/ic_search"
     app:showAsAction="ifRoom|collapseActionView"
     app:actionViewClass="androidx.appcompat.widget.SearchView" />
```

If the user isn't interacting with the widget, the app displays the widget as the icon specified by`android:icon`. If there isn't room in the app bar, the app adds the action to the overflow menu.
![An image showing a search bar with a leading and trailing icons.](https://lh3.googleusercontent.com/zTb1ACT-j6EAGJqu2OEqbkLnLMrdSyHRlRaUYJMwB-vBKc1E6_Bz_bS2rC76Ivyavm7Bs5638cIG0m-aMBux0yovjt2eDxLabF6xm8DxvVU8=s0)**Figure 1.**Search bar with leading and trailing icons.

When the user taps the icon or menu item, the widget expands to fill the toolbar, letting the user interact with it.
![An image showing a search view open once the search bar is focused.](https://lh3.googleusercontent.com/YnYHSwRbp4CE19IxdkgtvlB7oc4R1Tl5T-QY_-9VddsyLIUa6Xd9KY5AMwBclWYY354_v5XEDOjDOsHYe7uAsoF43MAb9Bp-dzlof7ZNecux=s0)**Figure 2.**Search view opens once the search bar is focused.

If you need to configure the action, do so in your activity's[onCreateOptionsMenu()](https://developer.android.com/reference/android/app/Activity#onCreateOptionsMenu(android.view.Menu))callback. You can get the action view's object reference by calling the[getActionView()](https://developer.android.com/reference/android/view/MenuItem#getActionView())method. For example, the following code gets the object reference for the`SearchView`widget defined in the previous code example:  

### Kotlin

```kotlin
override fun onCreateOptionsMenu(menu: Menu?): Boolean {
    menuInflater.inflate(R.menu.main_activity_actions, menu)

    val searchItem = menu?.findItem(R.id.action_search)
    val searchView = searchItem?.actionView as SearchView

    // Configure the search info and add any event listeners.

    return super.onCreateOptionsMenu(menu)
}
```

### Java

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.main_activity_actions, menu);

    MenuItem searchItem = menu.findItem(R.id.action_search);
    SearchView searchView =
            (SearchView) searchItem.getActionView();

    // Configure the search info and add any event listeners.

    return super.onCreateOptionsMenu(menu);
}
```
| **Note:** To improve the look and feel for your`SearchView`, see the[Search component](https://m3.material.io/components/search/overview)in Material Design 3.

### Respond to action view expansion

If the action's`<item>`element has a`collapseActionView`flag, the app displays the action view as an icon until the user interacts with the action view. When the user taps the icon, the built-in handler for[onOptionsItemSelected()](https://developer.android.com/reference/android/app/Activity#onOptionsItemSelected(android.view.MenuItem))expands the action view. If your activity subclass overrides the`onOptionsItemSelected()`method, your override method must call`super.onOptionsItemSelected()`so the superclass can expand the action view.

If you want to do something when the action is expanded or collapsed, you can define a class that implements[MenuItem.OnActionExpandListener](https://developer.android.com/reference/android/view/MenuItem.OnActionExpandListener), and pass a member of that class to[setOnActionExpandListener()](https://developer.android.com/reference/android/view/MenuItem#setOnActionExpandListener(android.view.MenuItem.OnActionExpandListener)). For example, you might want to update the activity based on whether an action view is expanded or collapsed. The following code snippet shows how to define and pass a listener:  

### Kotlin

```kotlin
override fun onCreateOptionsMenu(menu: Menu?): Boolean {
    menuInflater.inflate(R.menu.options, menu)

    // Define the listener.
    val expandListener = object : MenuItem.OnActionExpandListener {
        override fun onMenuItemActionCollapse(item: MenuItem): Boolean {
            // Do something when the action item collapses.
            return true // Return true to collapse the action view.
        }

        override fun onMenuItemActionExpand(item: MenuItem): Boolean {
            // Do something when it expands.
            return true // Return true to expand the action view.
        }
    }

    // Get the MenuItem for the action item.
    val actionMenuItem = menu?.findItem(R.id.myActionItem)

    // Assign the listener to that action item.
    actionMenuItem?.setOnActionExpandListener(expandListener)

    // For anything else you have to do when creating the options menu,
    // do the following:

    return true
}
```

### Java

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.options, menu);

    // Define the listener.
    OnActionExpandListener expandListener = new OnActionExpandListener() {
        @Override
        public boolean onMenuItemActionCollapse(MenuItem item) {
            // Do something when the action item collapses.
            return true;  // Return true to collapse action view.
        }

        @Override
        public boolean onMenuItemActionExpand(MenuItem item) {
            // Do something when it expands.
            return true;  // Return true to expand the action view.
        }
    };

    // Get the MenuItem for the action item.
    MenuItem actionMenuItem = menu.findItem(R.id.myActionItem);

    // Assign the listener to that action item.
    MenuItemCompat.setOnActionExpandListener(actionMenuItem, expandListener);

    // For anything else you have to do when creating the options menu,
    // do the following:

    return true;
}
```

## Add an action provider

To declare an action provider, create an`<item>`element in the toolbar's menu resource, as described in[Add and handle actions](https://developer.android.com/develop/ui/views/components/appbar/actions). Add an`actionProviderClass`attribute, and set it to the fully qualified class name for the action provider class.

For example, the following code declares a`ShareActionProvider`, which is a widget defined in the AndroidX library that lets your app share data with other apps:  

```xml
<item android:id="@+id/action_share"
    android:title="@string/share"
    app:showAsAction="ifRoom"
    app:actionProviderClass="androidx.appcompat.widget.ShareActionProvider"/>
```

In this case, it's unnecessary to declare an icon for the widget, since`ShareActionProvider`provides its own graphics. If you are using a custom action, declare an icon.

## Additional resources

- See[ShareActionProvider](https://developer.android.com/reference/androidx/appcompat/widget/ShareActionProvider)for an example of adding a share action to your top app bar.
- See[ActionProvider](https://developer.android.com/reference/androidx/core/view/ActionProvider)for more information about creating a custom action provider.