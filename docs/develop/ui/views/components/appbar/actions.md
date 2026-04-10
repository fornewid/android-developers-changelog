---
title: https://developer.android.com/develop/ui/views/components/appbar/actions
url: https://developer.android.com/develop/ui/views/components/appbar/actions
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose.  
[Dynamic top app bar →](https://developer.android.com/develop/ui/compose/components/app-bars-dynamic)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The app bar lets you add buttons for user actions. This feature lets you put
the most important *actions* for the current context at the top of the app.
For example, a photo browsing app might show *share* and *create
album* buttons at the top when the user is looking at their photo roll. When
the user looks at an individual photo, the app might show *crop* and
*filter* buttons.

Space in the app bar is limited. If an app declares more actions than can fit
in the app bar, the app bar sends the excess actions to an *overflow* menu.
The app can also specify that an action always shows in the overflow menu,
instead of displaying on the app bar.
![An image showing Now in Android app with a action bar icon](https://developer.android.com/static/images/ui/notifications/actions_actionbar.png) **Figure 1.** An action icon in the "Now in Android" app.

## Add action buttons

All action buttons and other items available in the action overflow are
defined in an XML
[menu resource](https://developer.android.com/guide/topics/resources/menu-resource). To add
actions to the action bar, create a new XML file in your project's
`res/menu/` directory.

Add an
[`<item>`](https://developer.android.com/guide/topics/resources/menu-resource#item-element)
element for each item you want to include in the action bar, as shown in the
following sample menu XML file:  

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android" 
xmlns:app="http://schemas.android.com/apk/res-auto">

    <!-- "Mark Favorite", must appear as action button if possible. -->
    <item
        android:id="@+id/action_favorite"
        android:icon="@drawable/ic_favorite_black_48dp"
        android:title="@string/action_favorite"
        app:showAsAction="ifRoom"/>

    <!-- Settings, must always be in the overflow. -->
    <item android:id="@+id/action_settings"
          android:title="@string/action_settings"
          app:showAsAction="never"/>

</menu>
```

The `app:showAsAction` attribute specifies whether the action is
shown as a button on the app bar. If you set
`app:showAsAction="ifRoom"`---as in the example code's
*favorite* action---the action displays as a button if there is room in
the app bar for it. If there isn't enough room, excess actions are sent to the
overflow menu. If you set `app:showAsAction="never"`---as in the
example code's *settings* action---the action is always listed in the
overflow menu and not displayed in the app bar.

The system uses the action's icon as the action button if the action displays
in the app bar. You can find many useful icons in
[Material Icons](https://www.google.com/design/icons/).

## Respond to actions

When the user selects one of the app bar items, the system calls your
activity's
[onOptionsItemSelected()](https://developer.android.com/reference/android/app/Activity#onOptionsItemSelected(android.view.MenuItem))
callback method and passes a
[MenuItem](https://developer.android.com/reference/android/view/MenuItem) object
to indicate which item was tapped. In your implementation of
`onOptionsItemSelected()`, call the
[MenuItem.getItemId()](https://developer.android.com/reference/android/view/MenuItem#getItemId())
method to determine which item was tapped. The ID returned matches the value you
declare in the corresponding `<item>` element's
`android:id` attribute.

For example, the following code snippet checks which action the user selects.
If the method doesn't recognize the user's action, it invokes the superclass
method:  

### Kotlin

```kotlin
override fun onOptionsItemSelected(item: MenuItem) = when (item.itemId) {
    R.id.action_settings -> {
        // User chooses the "Settings" item. Show the app settings UI.
        true
    }

    R.id.action_favorite -> {
        // User chooses the "Favorite" action. Mark the current item as a
        // favorite.
        true
    }

    else -> {
        // The user's action isn't recognized.
        // Invoke the superclass to handle it.
        super.onOptionsItemSelected(item)
    }
}
```

### Java

```java
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    switch (item.getItemId()) {
        case R.id.action_settings:
            // User chooses the "Settings" item. Show the app settings UI.
            return true;

        case R.id.action_favorite:
            // User chooses the "Favorite" action. Mark the current item as a
            // favorite.
            return true;

        default:
            // The user's action isn't recognized.
            // Invoke the superclass to handle it.
            return super.onOptionsItemSelected(item);

    }
}
```