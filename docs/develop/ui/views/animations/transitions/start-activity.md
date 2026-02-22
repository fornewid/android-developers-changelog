---
title: https://developer.android.com/develop/ui/views/animations/transitions/start-activity
url: https://developer.android.com/develop/ui/views/animations/transitions/start-activity
source: md.txt
---

# Start an activity using an animation

<br />

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with animations in Compose.  
[Animate between different types of content in Compose →](https://developer.android.com/develop/ui/compose/animation/quick-guide#switch-different)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Activity transitions in Material Design apps provide visual connections between different states through motion and transformations between common elements. You can specify custom animations for enter and exit transitions and for transitions of shared elements between activities.  

**Figure 1**. A transition with shared elements.

- An*enter* transition determines how views in an activity enter the scene. For example, in the`explode`enter transition, the views enter the scene from the outside and fly inward to the center of the screen.
- An*exit* transition determines how views in an activity exit the scene. For example, in the`explode`exit transition, the views exit the scene away from the center.
- A*shared elements* transition determines how views that are shared between two activities transition between these activities. For example, if two activities have the same image in different positions and sizes, the`changeImageTransform`shared element transition translates and scales the image smoothly between these activities.

Android supports these enter and exit transitions:

- `explode`: moves views in toward or out from the center of the scene.
- `slide`: moves views in or out from one of the edges of the scene.
- `fade`: adds or removes a view from the scene by changing its opacity.

Any transition that extends the[Visibility](https://developer.android.com/reference/android/transition/Visibility)class is supported as an enter or exit transition. For more information, see the API reference for the[Transition](https://developer.android.com/reference/android/transition/Transition)class.

Android also supports these shared elements transitions:

- `changeBounds`: animates the changes in layout bounds of target views.
- `changeClipBounds`: animates the changes in clip bounds of target views.
- `changeTransform`: animates the changes in scale and rotation of target views.
- `changeImageTransform`: animates the changes in size and scale of target images.

When you enable activity transitions in your app, the default cross-fading transition activates between the entering and exiting activities.

![](https://developer.android.com/static/training/material/images/SceneTransition.png)

**Figure 2.**A scene transition with one shared element.

<br />

For sample code that animates between activities using shared elements, see[ActivitySceneTransitionBasic](https://github.com/android/animation/tree/main/ActivitySceneTransitionBasic).

## Check the system version

Activity transition APIs are available on Android 5.0 (API 21) and up. To preserve compatibility with earlier versions of Android, check the system[version](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT)at runtime before you invoke the APIs for any of these features:  

### Kotlin

```kotlin
// Check if we're running on Android 5.0 or higher
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Apply activity transition
} else {
    // Swap without transition
}
```

### Java

```java
// Check if we're running on Android 5.0 or higher
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
    // Apply activity transition
} else {
    // Swap without transition
}
```

## Specify custom transitions

First, enable window content transitions with the`android:windowActivityTransitions`attribute when you define a style that inherits from the Material theme. You can also specify enter, exit, and shared element transitions in your style definition:  

```xml
<style name="BaseAppTheme" parent="android:Theme.Material">
  <!-- enable window content transitions -->
  <item name="android:windowActivityTransitions">true</item>

  <!-- specify enter and exit transitions -->
  <item name="android:windowEnterTransition">@transition/explode</item>
  <item name="android:windowExitTransition">@transition/explode</item>

  <!-- specify shared element transitions -->
  <item name="android:windowSharedElementEnterTransition">
    @transition/change_image_transform</item>
  <item name="android:windowSharedElementExitTransition">
    @transition/change_image_transform</item>
</style>
```

The`change_image_transform`transition in this example is defined as follows:  

```xml
<!-- res/transition/change_image_transform.xml -->
<!-- (see also Shared Transitions below) -->
<transitionSet xmlns:android="http://schemas.android.com/apk/res/android">
  <changeImageTransform/>
</transitionSet>
```

The`changeImageTransform`element corresponds to the[ChangeImageTransform](https://developer.android.com/reference/android/transition/ChangeImageTransform)class. For more information, see the API reference for[Transition](https://developer.android.com/reference/android/transition/Transition).

To enable window content transitions in your code instead, call the[Window.requestFeature()](https://developer.android.com/reference/android/view/Window#requestFeature(int))function:  

### Kotlin

```kotlin
// Inside your activity (if you did not enable transitions in your theme)
with(window) {
    requestFeature(Window.FEATURE_ACTIVITY_TRANSITIONS)

    // Set an exit transition
    exitTransition = Explode()
}
```

### Java

```java
// Inside your activity (if you did not enable transitions in your theme)
getWindow().requestFeature(Window.FEATURE_ACTIVITY_TRANSITIONS);

// Set an exit transition
getWindow().setExitTransition(new Explode());
```

To specify transitions in your code, call these functions with a`Transition`object:

- [Window.setEnterTransition()](https://developer.android.com/reference/android/view/Window#setEnterTransition(android.transition.Transition))
- [Window.setExitTransition()](https://developer.android.com/reference/android/view/Window#setExitTransition(android.transition.Transition))
- [Window.setSharedElementEnterTransition()](https://developer.android.com/reference/android/view/Window#setSharedElementEnterTransition(android.transition.Transition))
- [Window.setSharedElementExitTransition()](https://developer.android.com/reference/android/view/Window#setSharedElementExitTransition(android.transition.Transition))

The`setExitTransition()`and`setSharedElementExitTransition()`functions define the exit transition for the calling activity. The`setEnterTransition()`and`setSharedElementEnterTransition()`functions define the enter transition for the called activity.

To get the full effect of a transition, you must enable window content transitions on both the calling and called activities. Otherwise, the calling activity starts the exit transition, but then you see the window transitions---like scale or fade.

To start an enter transition as soon as possible, use the[Window.setAllowEnterTransitionOverlap()](https://developer.android.com/reference/android/view/Window#setAllowEnterTransitionOverlap(boolean))function on the called activity. This lets you have more dramatic enter transitions.

## Start an activity using transitions

If you enable transitions and set an exit transition for an activity, the transition activates when you launch another activity, as follows:  

### Kotlin

```kotlin
startActivity(intent,
              ActivityOptions.makeSceneTransitionAnimation(this).toBundle())
```

### Java

```java
startActivity(intent,
              ActivityOptions.makeSceneTransitionAnimation(this).toBundle());
```

If you set an enter transition for the second activity, that transition also activates when the activity starts. To disable transitions when you start another activity, provide a`null`options bundle.

## Start an activity with a shared element

| **Note:** See[Shared Element Transitions in Compose](https://developer.android.com/develop/ui/compose/animation/shared-elements)for information on transitioning between composables with consistent content.

To make a screen transition animation between two activities that have a shared element, do the following:

1. Enable window content transitions in your theme.
2. Specify a shared elements transition in your style.
3. Define your transition as an XML resource.
4. Assign a common name to the shared elements in both layouts with the`android:transitionName`attribute.
5. Use the[ActivityOptions.makeSceneTransitionAnimation()](https://developer.android.com/reference/android/app/ActivityOptions#makeSceneTransitionAnimation(android.app.Activity, android.util.Pair<android.view.View, java.lang.String>...))function.

### Kotlin

```kotlin
// Get the element that receives the click event
val imgContainerView = findViewById<View>(R.id.img_container)

// Get the common element for the transition in this activity
val androidRobotView = findViewById<View>(R.id.image_small)

// Define a click listener
imgContainerView.setOnClickListener( {
    val intent = Intent(this, Activity2::class.java)
    // Create the transition animation - the images in the layouts
    // of both activities are defined with android:transitionName="robot"
    val options = ActivityOptions
            .makeSceneTransitionAnimation(this, androidRobotView, "robot")
    // Start the new activity
    startActivity(intent, options.toBundle())
})
```

### Java

```java
// Get the element that receives the click event
final View imgContainerView = findViewById(R.id.img_container);

// Get the common element for the transition in this activity
final View androidRobotView = findViewById(R.id.image_small);

// Define a click listener
imgContainerView.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        Intent intent = new Intent(this, Activity2.class);
        // Create the transition animation - the images in the layouts
        // of both activities are defined with android:transitionName="robot"
        ActivityOptions options = ActivityOptions
            .makeSceneTransitionAnimation(this, androidRobotView, "robot");
        // Start the new activity
        startActivity(intent, options.toBundle());
    }
});
```

For shared dynamic views that you generate in your code, use the[View.setTransitionName()](https://developer.android.com/reference/android/view/View#setTransitionName(java.lang.String))function to specify a common element name in both activities.

To reverse the scene transition animation when you finish the second activity, call the[Activity.finishAfterTransition()](https://developer.android.com/reference/android/app/Activity#finishAfterTransition())function instead of[Activity.finish()](https://developer.android.com/reference/android/app/Activity#finish()).

## Start an activity with multiple shared elements

To make a scene transition animation between two activities that have more than one shared element, define the shared elements in both layouts with the`android:transitionName`attribute---or use the`View.setTransitionName()`function in both activities---and create an[ActivityOptions](https://developer.android.com/reference/android/app/ActivityOptions)object as follows:  

### Kotlin

```kotlin
// Rename the Pair class from the Android framework to avoid a name clash
import android.util.Pair as UtilPair
...
val options = ActivityOptions.makeSceneTransitionAnimation(this,
        UtilPair.create(view1, "agreedName1"),
        UtilPair.create(view2, "agreedName2"))
```

### Java

```java
ActivityOptions options = ActivityOptions.makeSceneTransitionAnimation(this,
        Pair.create(view1, "agreedName1"),
        Pair.create(view2, "agreedName2"));
```