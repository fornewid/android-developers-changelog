---
title: https://developer.android.com/develop/ui/views/notifications/snackbar/showing
url: https://developer.android.com/develop/ui/views/notifications/snackbar/showing
source: md.txt
---

# Build and display a pop-up message

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add notifications in Compose.  
[Snackbar →](https://developer.android.com/develop/ui/compose/components/snackbar)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

You can use a[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)to display a brief message to the user. Unlike[Notifications](https://developer.android.com/guide/topics/ui/notifiers/notifications), the message automatically goes away after a short period. A`Snackbar`is ideal for brief messages that the user doesn't need to act on. For example, an email app can use a`Snackbar`to tell the user that the app successfully sent an email.

## Use a CoordinatorLayout

A`Snackbar`is attached to a view. The`Snackbar`provides basic functionality if it is attached to any object derived from the[View](https://developer.android.com/reference/android/view/View)class, such as any of the common layout objects. However, if the`Snackbar`is attached to a[CoordinatorLayout](https://developer.android.com/reference/androidx/coordinatorlayout/widget/CoordinatorLayout), the`Snackbar`gains additional features:

- The user can dismiss the`Snackbar`by swiping it away.
- The layout moves other UI elements when the`Snackbar`appears. For example, if the layout has a[FloatingActionButton](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton), the layout moves the button up when it shows a`Snackbar`, instead of drawing the`Snackbar`on top of the button. You can see how this looks in figure 1.

The`CoordinatorLayout`class provides a superset of the functionality of[FrameLayout](https://developer.android.com/reference/android/widget/FrameLayout). If your app already uses a`FrameLayout`, you can replace that layout with a`CoordinatorLayout`to enable the full`Snackbar`functionality. If your app uses other layout objects, wrap your existing layout elements in a`CoordinatorLayout`, as shown in the following example:  

```xml
<android.support.design.widget.CoordinatorLayout
    android:id="@+id/myCoordinatorLayout"
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- Here are the existing layout elements, now wrapped in
         a CoordinatorLayout. -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <!-- ...Toolbar, other layouts, other elements... -->

    </LinearLayout>

</android.support.design.widget.CoordinatorLayout>
```

Set an`android:id`tag for your`CoordinatorLayout`. You need the layout's ID when you display the message.
![](https://developer.android.com/static/images/training/snackbar/snackbar_button_move_poster.png)

**Figure 1.** The`CoordinatorLayout`moves the`FloatingActionButton`up when the`Snackbar`appears.

## Display a message

There are two steps to displaying a message. First, you create a`Snackbar`object with the message text. Then, you call that object's[show()](https://developer.android.com/reference/com/google/android/material/snackbar/BaseTransientBottomBar#show())method to display the message to the user.

### Create a Snackbar object

Create a`Snackbar`object by calling the static[Snackbar.make()](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar#make(android.view.View, int, int))method. When you create the`Snackbar`, specify the message it displays and the length of time to show the message:  

### Kotlin

```kotlin
val mySnackbar = Snackbar.make(view, stringId, duration)
```

### Java

```java
Snackbar mySnackbar = Snackbar.make(view, stringId, duration);
```

view
:   The view to attach the`Snackbar`to. The method searches up the view hierarchy from the passed view until it reaches a`CoordinatorLayout`or the window decor's content view. Ordinarily, it's simpler to pass the`CoordinatorLayout`enclosing your content.

stringId
:   The resource ID of the message you want to display. This can be formatted or unformatted text.

duration
:   The length of time to show the message. This can be[LENGTH_SHORT](https://developer.android.com/reference/com/google/android/material/snackbar/BaseTransientBottomBar#LENGTH_SHORT))or[LENGTH_LONG](https://developer.android.com/reference/com/google/android/material/snackbar/BaseTransientBottomBar#LENGTH_LONG).

### Show the message to the user

After you create the`Snackbar`, call its`show()`method to display the`Snackbar`to the user:  

### Kotlin

```kotlin
mySnackbar.show()
```

### Java

```java
mySnackbar.show();
```

The system doesn't show multiple`Snackbar`objects at the same time, so if the view is currently displaying another`Snackbar`, the system queues your`Snackbar`and displays it after the current`Snackbar`expires or is dismissed.

If you want to show a message to the user and don't need to call any of the`Snackbar`object's utility methods, you don't need to keep the reference to the`Snackbar`after you call`show()`. For this reason, it's common to use method chaining to create and show a`Snackbar`in one statement:  

### Kotlin

```kotlin
Snackbar.make(
        findViewById(R.id.myCoordinatorLayout),
        R.string.email_sent,
        Snackbar.LENGTH_SHORT
).show()
```

### Java

```java
Snackbar.make(findViewById(R.id.myCoordinatorLayout), R.string.email_sent,
                        Snackbar.LENGTH_SHORT)
        .show();
```