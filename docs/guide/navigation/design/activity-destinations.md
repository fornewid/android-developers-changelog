---
title: https://developer.android.com/guide/navigation/design/activity-destinations
url: https://developer.android.com/guide/navigation/design/activity-destinations
source: md.txt
---

# Activity destinations

In your navigation graph, a destination can be an activity. While it is best practice to have a single activity in your app, apps often use separate activities for distinct components or screen within an app. Activity destinations can be useful in such cases.

## Compose and Kotlin DSL

Adding an activity destination to your navigation graph is essentially the same in both Compose and when using the Kotlin DSL with fragments. This is because when passing your`NavGraph`to your`NavHost`composable, you use the same`createGraph()`lambda.

For more information, see[Fragments and the Kotlin DSL](https://developer.android.com/guide/navigation/design/kotlin-dsl#activity).

## XML

Creating an[activity](https://developer.android.com/reference/android/app/Activity)destination is similar to creating a[fragment](https://developer.android.com/reference/androidx/fragment/app/Fragment)destination. However, the nature of an activity destination is quite different.

By default, the[Navigation library](https://developer.android.com/reference/androidx/navigation/package-summary)attaches the[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController)to an`Activity`layout, and the active navigation graph is scoped to the active`Activity`. If a user navigates to a different`Activity`, the current navigation graph is no longer in scope. This means that an`Activity`destination should be considered an endpoint within a navigation graph.

To add an activity destination, specify the destination`Activity`with its fully qualified class name:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/navigation_graph"
    app:startDestination="@id/simpleFragment">

    <activity
        android:id="@+id/sampleActivityDestination"
        android:name="com.example.android.navigation.activity.DestinationActivity"
        android:label="@string/sampleActivityTitle" />
</navigation>
```

This XML is equivalent to the following call to[`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)):  

### Kotlin

    startActivity(Intent(context, DestinationActivity::class.java))

### Java

    startActivity(new Intent(context, DestinationActivity.class));

You might have cases where this approach is not appropriate. For example, you might not have a compile-time dependency on the activity class, or you might prefer the level of indirection of going through an implicit intent. The[`intent-filter`](https://developer.android.com/guide/topics/manifest/intent-filter-element)in the manifest entry for the destination`Activity`dictates how you need to structure the`Activity`destination.

For example, consider the following manifest file:  

    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.android.navigation.activity">
        <application>
            <activity android:name=".DestinationActivity">
                <intent-filter>
                    <action android:name="android.intent.action.VIEW" />
                    <data
                        android:host="example.com"
                        android:scheme="https" />
                    <category android:name="android.intent.category.BROWSABLE" />
                    <category android:name="android.intent.category.DEFAULT" />
                </intent-filter>
            </activity>
        </application>
    </manifest>

The corresponding`Activity`destination needs to be configured with[`action`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator.Destination#setAction(java.lang.String))and[`data`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator.Destination#setData(android.net.Uri))attributes matching those in the manifest entry:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/navigation_graph"
    app:startDestination="@id/simpleFragment">
    <activity
        android:id="@+id/localDestinationActivity"
        android:label="@string/localActivityTitle"
        app:action="android.intent.action.VIEW"
        app:data="https://example.com"
        app:targetPackage="${applicationId}" />
</navigation>
```

Specifying[`targetPackage`](https://developer.android.com/reference/kotlin/androidx/navigation/ActivityNavigator.Destination#setTargetPackage(kotlin.String))to the current[`applicationId`](https://developer.android.com/studio/build/configure-app-module#set_the_application_id)limits the scope to the current application, which includes the main app.

The same mechanism can be used for cases where you want a specific app to be the destination. The following example defines a destination to be an app with an`applicationId`of`com.example.android.another.app`.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/navigation_graph"
    app:startDestination="@id/simpleFragment">
    <activity
        android:id="@+id/localDestinationActivity"
        android:label="@string/localActivityTitle"
        app:action="android.intent.action.VIEW"
        app:data="https://example.com"
        app:targetPackage="com.example.android.another.app" />
</navigation>
```
| **Caution:** An`ActivityNotFoundException`is thrown if you attempt to navigate to this destination and either the specified app is not installed on the device or the destination app does not have an`Activity`defined in its manifest with a matching`intent-filter`.

## Dynamic arguments

The previous examples used fixed URLs to navigate to destinations. You might also need to support dynamic URLs where additional info is sent as part of the URL. For example, you might send a user ID in a URL with a format similar to`https://example.com?userId=<actual user ID>`.

In this case, instead of the[`data`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator.Destination#setData(android.net.Uri))attribute, use[`dataPattern`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator.Destination#setDataPattern(java.lang.String)). You can then supply arguments to be substituted for named placeholders within the`dataPattern`value:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:id="@+id/navigation_graph"
    app:startDestination="@id/simpleFragment">
    <activity
        android:id="@+id/localDestinationActivity"
        android:label="@string/localActivityTitle"
        app:action="android.intent.action.VIEW"
        app:dataPattern="https://example.com?userId={userId}"
        app:targetPackage="com.example.android.another.app">
        <argument
            android:name="userId"
            app:argType="string" />
    </activity>
</navigation>
```

In this example, you can specify a`userId`value using either[Safe Args](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args)or with a`Bundle`:  

### Kotlin

    navController.navigate(
        R.id.localDestinationActivity,
        bundleOf("userId" to "someUser")
    )

### Java

    Bundle args = new Bundle();
    args.putString("userId", "someUser");
    navController.navigate(R.id.localDestinationActivity, args);

This example substitutes`someUser`for`{userId}`and creates a URI value of`https://example.com?userId=someUser`.
| **Caution:** An exception is thrown if any required arguments are missing from the navigation request.