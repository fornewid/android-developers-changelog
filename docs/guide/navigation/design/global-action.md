---
title: https://developer.android.com/guide/navigation/design/global-action
url: https://developer.android.com/guide/navigation/design/global-action
source: md.txt
---

# Global actions

You can use a*global action*to create a common action that multiple destinations can use. For example, you might want buttons in different destinations to navigate to the same main app screen.

A global action is represented in the Navigation Editor by a small arrow that points to the associated destination, as shown in figure 1.
![](https://developer.android.com/static/topic/libraries/architecture/images/navigation-global-action.png)**Figure 1.**A global action that leads to a nested graph.

## Create a global action

To create a global action, do the following:

1. From the**Graph Editor**, click on a destination to highlight it.
2. Right-click on the destination to display the context menu.
3. Select**Add Action \> Global** . An arrow (![](https://developer.android.com/static/studio/images/buttons/navigation-globalaction.png)) appears to the left of the destination.
4. Click the**Text**tab to navigate to the XML text view. The XML for the global action looks similar to the following:

       <?xml version="1.0" encoding="utf-8"?>
       <navigation xmlns:app="http://schemas.android.com/apk/res-auto"
                   xmlns:tools="http://schemas.android.com/tools"
                   xmlns:android="http://schemas.android.com/apk/res/android"
                   android:id="@+id/main_nav"
                   app:startDestination="@id/mainFragment">

         ...

         <action android:id="@+id/action_global_mainFragment"
                 app:destination="@id/mainFragment"/>

       </navigation>

## Use a global action

To use a global action in your code, pass the resource ID of the global action to the[`navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(int))method for each UI element, as shown in the following example:  

### Kotlin

```kotlin
viewTransactionButton.setOnClickListener { view ->
    view.findNavController().navigate(R.id.action_global_mainFragment)
}
```

### Java

```java
viewTransactionsButton.setOnClickListener(new View.OnClickListener() {
   @Override
   public void onClick(View view) {
       Navigation.findNavController(view).navigate(R.id.action_global_mainFragment);
   }
});
```

## Use Safe Args with a global action

For information on using Safe Args with global actions, see[Pass data between destinations](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data#safe-args-global).

## Additional resources

To learn more about navigation, consult the following additional resources.

### Codelabs

- [Navigation Codelab](https://codelabs.developers.google.com/codelabs/android-navigation/index.html?index=../../index#0)

### Videos

- [Android Jetpack: manage UI navigation with Navigation Controller (Google I/O '18)](https://www.youtube.com/watch?v=8GCXtCjtg40)