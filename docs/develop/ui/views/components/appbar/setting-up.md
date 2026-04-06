---
title: https://developer.android.com/develop/ui/views/components/appbar/setting-up
url: https://developer.android.com/develop/ui/views/components/appbar/setting-up
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose. [App Bar →](https://developer.android.com/develop/ui/compose/components/app-bars) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

In its most basic form, the action bar displays the title for the activity on one
side and an overflow menu on the other. Even in this basic form, the app bar provides
useful information to users and gives Android apps a consistent look and feel.
![An image showing the app bar in the Now in Android app](https://developer.android.com/static/images/ui/notifications/actions_actionbar.png) **Figure 1.** An app bar with an action icon in the "Now in Android" app.

All activities that use the default theme have an
`https://developer.android.com/reference/android/app/ActionBar` as an app
bar. App bar features are added to the native `ActionBar` over various
Android releases. As a result, the native `ActionBar` behaves differently
depending on what version of Android a device is using.

On the other hand, features are added to the AndroidX AppCompat library's version of
`https://developer.android.com/reference/androidx/appcompat/widget/Toolbar`,
which means those features are available on devices that use the AndroidX libraries.

Use the AndroidX library's `Toolbar` class to implement your activities'
app bars for this reason. Using the AndroidX library's toolbar makes your app's
behavior consistent across the widest range of devices.

## Add a Toolbar to an Activity

These steps describe how to set up a `Toolbar` as your activity's app bar:

1. Add the AndroidX library to your project, as described in [AndroidX overview](https://developer.android.com/jetpack/androidx).
2. Make sure the activity extends `https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity`:

   ### Kotlin

   ```kotlin
   class MyActivity : AppCompatActivity() {
     // ...
   }
   ```

   ### Java

   ```java
   public class MyActivity extends AppCompatActivity {
     // ...
   }
   ```
   | **Note:** Make this change for every activity in your app that uses a `Toolbar` as an app bar.
3. In the app manifest, set the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element to use one of AppCompat's `https://developer.android.com/reference/android/R.style#Theme_DeviceDefault_Light_NoActionBar` themes, as shown in the following example. Using one of these themes prevents the app from using the native `ActionBar` class to provide the app bar.

   ```xml
   <application
       android:theme="@style/Theme.AppCompat.Light.NoActionBar"
       />
   ```
4. Add a `Toolbar` to the activity's layout. For example, the following layout code adds a `Toolbar` and gives it the appearance of floating above the activity:

   ```xml
   <androidx.appcompat.widget.Toolbar
      android:id="@+id/my_toolbar"
      android:layout_width="match_parent"
      android:layout_height="?attr/actionBarSize"
      android:background="?attr/colorPrimary"
      android:elevation="4dp"
      android:theme="@style/ThemeOverlay.AppCompat.ActionBar"
      app:popupTheme="@style/ThemeOverlay.AppCompat.Light"/>
   ```

   See the
   [Material Design specification](https://material.io/design/components/app-bars-bottom.html)
   for recommendations regarding app bar elevation.

   Position the toolbar at the top of the activity's
   [layout](https://developer.android.com/guide/topics/ui/declaring-layout), since you are using
   it as an app bar.
5. In the activity's `https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)` method, call the activity's `https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity#setSupportActionBar(androidx.appcompat.widget.Toolbar)` method and pass the activity's toolbar, as shown in the following example. This method sets the toolbar as the app bar for the activity.

   ### Kotlin

   ```kotlin
   override fun onCreate(savedInstanceState: Bundle?) {
       super.onCreate(savedInstanceState)
       setContentView(R.layout.activity_my)
       // The Toolbar defined in the layout has the id "my_toolbar".
       setSupportActionBar(findViewById(R.id.my_toolbar))
   }
   ```

   ### Java

   ```java
   @Override
   protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       setContentView(R.layout.activity_my);
       Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
       setSupportActionBar(myToolbar);
   }
   ```

Your app now has a basic action bar. By default, the action bar contains the name
of the app and an overflow menu, which initially contains the **Settings** item.
You can add more actions to the action bar and the overflow menu, as described in
[Add and handle actions](https://developer.android.com/develop/ui/views/components/appbar/actions).

## Use app bar utility methods

Once you set the toolbar as an activity's app bar, you have access to the utility
methods provided by the AndroidX library's
`https://developer.android.com/reference/androidx/appcompat/app/ActionBar`
class. This approach lets you do useful things, like hide and show the app bar.

To use the `ActionBar` utility methods, call the activity's
`https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity#getSupportActionBar()`
method. This method returns a reference to an AppCompat `ActionBar` object.
Once you have that reference, you can call any of the `ActionBar` methods
to adjust the app bar. For example, to hide the app bar, call
`https://developer.android.com/reference/androidx/appcompat/app/ActionBar#hide()`.