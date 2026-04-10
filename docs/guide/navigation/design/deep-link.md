---
title: https://developer.android.com/guide/navigation/design/deep-link
url: https://developer.android.com/guide/navigation/design/deep-link
source: md.txt
---

In Android, a deep link is a link that takes you directly to a specific destination within an app.

The Navigation component lets you create two different types of deep links:*explicit* and*implicit*.

## Create an explicit deep link

An[explicit deep link](https://developer.android.com/training/app-links/deep-linking)is a single instance of a deep link that uses a[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent)to take users to a specific location within your app. You might surface an explicit deep link as part of a notification or an app widget, for example.

When a user opens your app via an explicit deep link, the task back stack is cleared and replaced with the deep link destination. When[nesting graphs](https://developer.android.com/guide/navigation/navigation-nested-graphs), the start destination from each level of nesting---that is, the start destination from each`<navigation>`element in the hierarchy---is also added to the stack. This means that when a user presses the Back button from a deep link destination, they navigate back up the navigation stack just as though they entered your app from its entry point.

You can use the[`NavDeepLinkBuilder`](https://developer.android.com/reference/androidx/navigation/NavDeepLinkBuilder)class to construct a[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent), as shown in the example below. Note that if the provided context is not an`Activity`, the constructor uses[`PackageManager.getLaunchIntentForPackage()`](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPackage(java.lang.String))as the default activity to launch, if available.  

### Kotlin

```kotlin
val pendingIntent = NavDeepLinkBuilder(context)
    .setGraph(R.navigation.nav_graph)
    .setDestination(R.id.android)
    .setArguments(args)
    .createPendingIntent()
```

### Java

```java
PendingIntent pendingIntent = new NavDeepLinkBuilder(context)
    .setGraph(R.navigation.nav_graph)
    .setDestination(R.id.android)
    .setArguments(args)
    .createPendingIntent();
```

By default,`NavDeepLinkBuilder`launches your explicit deep link into the default launch`Activity`that is declared in your app's manifest. If your`NavHost`is in another activity, you must specify its component name when creating the deep link builder:  

### Kotlin

```kotlin
val pendingIntent = NavDeepLinkBuilder(context)
    .setGraph(R.navigation.nav_graph)
    .setDestination(R.id.android)
    .setArguments(args)
    .setComponentName(DestinationActivity::class.java)
    .createPendingIntent()
```

### Java

```java
PendingIntent pendingIntent = new NavDeepLinkBuilder(context)
        .setGraph(R.navigation.nav_graph)
        .setDestination(R.id.android)
        .setArguments(args)
        .setComponentName(DestinationActivity.class)
        .createPendingIntent();
```

If you have a[`ComponentName`](https://developer.android.com/reference/android/content/ComponentName), you can pass it directly to the builder:  

### Kotlin

```kotlin
val componentName = ...

val pendingIntent = NavDeepLinkBuilder(context)
    .setGraph(R.navigation.nav_graph)
    .setDestination(R.id.android)
    .setArguments(args)
    .setComponentName(componentName)
    .createPendingIntent()
```

### Java

```java
ComponentName componentName = ...;

PendingIntent pendingIntent = new NavDeepLinkBuilder(context)
        .setGraph(R.navigation.nav_graph)
        .setDestination(R.id.android)
        .setArguments(args)
        .setComponentName(componentName)
        .createPendingIntent();
```

If you have an existing[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController), you can also create a deep link by using[`NavController.createDeepLink()`](https://developer.android.com/reference/androidx/navigation/NavController#createDeepLink()).
| **Note:** If a screen requires that the user perform some action, such as logging in, before they can access that screen, follow the guidance on[Conditional Navigation](https://developer.android.com/guide/navigation/navigation-conditional)to conditionally redirect the user when they reach that screen using a deep link.

## Create an implicit deep link

An[implicit deep link](https://developer.android.com/training/app-links/deep-linking)refers to a specific destination in an app. When the deep link is invoked---for example, when a user clicks a link---Android can then open your app to the corresponding destination.

Deep links can be matched by URI, intent actions, and MIME types. You can specify multiple match types for a single deep link, but note that URI argument matching is prioritized first, followed by action, and then MIME type.

Here's an example deep link that contains a URI, an action, and a MIME type:  

    <fragment android:id="@+id/a"
              android:name="com.example.myapplication.FragmentA"
              tool>s:layout=<"@layout/a"
            deepLink app:uri="www.example.com"
                    app:action="android.intent.action.MY_ACTION&>q<uot;
        >            app:mimeType="type/subtype"/
    /fragment

You can also use the Navigation Editor to create an implicit deep link to a destination as follows:

1. In the**Design**tab of the Navigation Editor, select the destination for the deep link.
2. Click**+** in the**Deep Links** section of the**Attributes**panel.
3. In the**Add Deep Link**dialog that appears, enter the info for your deep link.

   Note the following:
   - URIs without a scheme are assumed as either http or https. For example,`www.google.com`matches both`http://www.google.com`and`https://www.google.com`.
   - Path parameter placeholders in the form of`{placeholder_name}`match one or more characters. For example,`http://www.example.com/users/{id}`matches`http://www.example.com/users/4`. The Navigation component attempts to parse the placeholder values into appropriate types by matching placeholder names to the defined[arguments](https://developer.android.com/guide/navigation/navigation-pass-data#define_destination_arguments)that are defined for the deep link destination. If no argument with the same name is defined, a default`String`type is used for the argument value. You can use the .\* wildcard to match 0 or more characters.
   - Query parameter placeholders can be used instead of or in conjunction with path parameters. For example,`http://www.example.com/users/{id}?myarg={myarg}`matches`http://www.example.com/users/4?myarg=28`.
   - Query parameter placeholders for variables defined with default or nullable values are not required to match. For example,`http://www.example.com/users/{id}?arg1={arg1}&arg2={arg2}`matches`http://www.example.com/users/4?arg2=28`or`http://www.example.com/users/4?arg1=7`. This is not the case with path parameters. For example,`http://www.example.com/users?arg1=7&arg2=28`does not match the above pattern because the required path parameter is not supplied.
   - Extraneous query parameters do not affect deep link URI matching. For example,`http://www.example.com/users/{id}`matches`http://www.example.com/users/4?extraneousParam=7`, even though`extraneousParam`is not defined in the URI pattern.
4. (optional) Check**Auto Verify** to require Google to verify that you are the owner of the URI. For more information, see[Verify Android App Links](https://developer.android.com/training/app-links/verify-android-applinks).

5. Click**Add** . A link icon![](https://developer.android.com/static/studio/images/buttons/navigation-deeplink.png)appears above the selected destination to indicate that destination has a deep link.

6. Click the**Code** tab to toggle to the XML view. A nested`<deepLink>`element has been added to the destination:

       <deepLink app:uri="https://www.google.c>om" /

To enable implicit deep linking, you must also make additions to your app's`manifest.xml`file. Add a single`<nav-graph>`element to an activity that points to an existing navigation graph, as shown in the following example:  

```xml
<?xml version="1.0" encodin>g<="utf-8"?
manifest xmlns:android="http://schemas.android.com/apk/res/android"
    packa>ge=&qu<ot;com.example.m>yapplicati<on"

    application ... 

 >       activity name=".Ma<inActivity" ...
            ...

           > nav-graph android:value=&q<uot;@navi>gatio<n/nav_graph&>q<uot; /

 >           ...

        /activity
    /application
/manifest
```

When building your project, the Navigation component replaces the`<nav-graph>`element with generated`<intent-filter>`elements to match all of the deep links in the navigation graph.

When triggering an implicit deep link, the state of the back stack depends on whether the implicit`Intent`was launched with the[`Intent.FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)flag:

- If the flag is set, the task back stack is cleared and replaced with the deep link destination. As with[explicit deep linking](https://developer.android.com/guide/navigation/design/deep-link#explicit), when[nesting graphs](https://developer.android.com/guide/navigation/navigation-nested-graphs), the start destination from each level of nesting---that is, the start destination from each`<navigation>`element in the hierarchy---is also added to the stack. This means that when a user presses the Back button from a deep link destination, they navigate back up the navigation stack just as though they entered your app from its entry point.
- If the flag is not set, you remain on the task stack of the previous app where the implicit deep link was triggered. In this case, the Back button takes you back to the previous app, while the Up button starts your app's task on the hierarchical parent destination within your navigation graph.

## Handling deep links

It is strongly recommended to always use the default[`launchMode`](https://developer.android.com/guide/topics/manifest/activity-element#lmode)of`standard`when using Navigation. When using`standard`launch mode, Navigation automatically handles deep links by calling[`handleDeepLink()`](https://developer.android.com/reference/androidx/navigation/NavController#handleDeepLink(android.content.Intent))to process any explicit or implicit deep links within the`Intent`. However, this does not happen automatically if the`Activity`is re-used when using an alternate`launchMode`such as`singleTop`. In this case, it is necessary to manually call`handleDeepLink()`in`onNewIntent()`, as shown in the following example:  

### Kotlin

```kotlin
override fun onNewIntent(intent: Intent?) {
    super.onNewIntent(intent)
    navController.handleDeepLink(intent)
}
```

### Java

```java
@Override
protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    navController.handleDeepLink(intent);
}
```

## Additional resources

To learn more about navigation, see the following resources.

### Codelabs

- [Navigation codelab](https://codelabs.developers.google.com/codelabs/android-navigation/index.html?index=../../index#0)

### Videos

- [Android Jetpack: manage UI navigation with Navigation Controller (Google I/O '18)](https://www.youtube.com/watch?v=8GCXtCjtg40)