---
title: https://developer.android.com/guide/navigation/design/add-new
url: https://developer.android.com/guide/navigation/design/add-new
source: md.txt
---

# Add support for new destination types

The[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController)type relies on one or more[`Navigator`](https://developer.android.com/reference/androidx/navigation/Navigator)objects to perform the navigation operation. By default,`NavController`supports leaving the navigation graph by navigating to another activity using the[`ActivityNavigator`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator)class and its nested[`ActivityNavigator.Destination`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator.Destination)class.

To navigate to any other type of destination, one or more additional`Navigator`objects must be added to the`NavController`. For example, when using fragments as destinations, the[`NavHostFragment`](https://developer.android.com/reference/androidx/navigation/fragment/NavHostFragment)automatically adds the[`FragmentNavigator`](https://developer.android.com/reference/androidx/navigation/fragment/FragmentNavigator)class to its`NavController`.

To add a new`Navigator`object to a`NavController`, use the[`getNavigatorProvider()`](https://developer.android.com/reference/androidx/navigation/NavController#getNavigatorProvider())method, followed by the[`addNavigator()`](https://developer.android.com/reference/androidx/navigation/NavigatorProvider#addNavigator(androidx.navigation.Navigator))method.

The following code shows an example of adding a`CustomNavigator`object to a`NavController`:  

### Kotlin

```kotlin
val customNavigator = CustomNavigator()
navController.navigatorProvider += customNavigator
```

### Java

```java
CustomNavigator customNavigator = new CustomNavigator();
navController.getNavigatorProvider().addNavigator(customNavigator);
```

Most`Navigator`classes have a nested destination subclass. This subclass can be used to specify additional attributes unique to your destination. For more information about destination subclasses, see the reference documentation for the appropriate[`Navigator`](https://developer.android.com/reference/androidx/navigation/Navigator)class.

## Additional resources

To learn more about navigation, see the following additional resources.

<br />

### Codelabs

<br />

- [Learn Jetpack Navigation codelab](https://codelabs.developers.google.com/codelabs/android-navigation/index.html?index=../../index#0)

<br />

### Videos

<br />

- [Android Jetpack: Manage UI navigation with Navigation Controller](https://www.youtube.com/watch?v=8GCXtCjtg40)