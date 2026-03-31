---
title: Custom WorkManager Configuration and Initialization  |  Background work  |  Android Developers
url: https://developer.android.com/develop/background-work/background-tasks/persistent/configuration/custom-configuration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Background work](https://developer.android.com/develop/background-work)
* [Guides](https://developer.android.com/develop/background-work/background-tasks)

# Custom WorkManager Configuration and Initialization Stay organized with collections Save and categorize content based on your preferences.




By default, WorkManager configures itself automatically when your app starts,
using reasonable options that are suitable for most apps. If you require more
control of how WorkManager manages and schedules work, you can customize the
WorkManager configuration by initializing WorkManager yourself.

## On-Demand Initialization

On-demand initialization lets you create WorkManager only when that component is
needed, instead of every time the app starts up. Doing so moves WorkManager off
your critical startup path, improving app startup performance. To use on-demand
initialization:

### Remove the default initializer

To provide your own configuration, you must first remove the default
initializer. To do so, update
[`AndroidManifest.xml`](/guide/topics/manifest/manifest-intro)
using the merge rule `tools:node="remove"`.

Since WorkManager 2.6, [App Startup](/topic/libraries/app-startup) is used
internally within WorkManager. To provide a custom initializer you need to
remove the `androidx.startup` node.

If you don't use App Startup in your app, you can remove it completely.

```
 <!-- If you want to disable android.startup completely. -->
 <provider
    android:name="androidx.startup.InitializationProvider"
    android:authorities="${applicationId}.androidx-startup"
    tools:node="remove">
 </provider>
```

Otherwise, remove only the `WorkManagerInitializer` node.

```
 <provider
    android:name="androidx.startup.InitializationProvider"
    android:authorities="${applicationId}.androidx-startup"
    android:exported="false"
    tools:node="merge">
    <!-- If you are using androidx.startup to initialize other components -->
    <meta-data
        android:name="androidx.work.WorkManagerInitializer"
        android:value="androidx.startup"
        tools:node="remove" />
 </provider>
```

While using a version of WorkManager older than 2.6, remove
`workmanager-init` instead:

```
<provider
    android:name="androidx.work.impl.WorkManagerInitializer"
    android:authorities="${applicationId}.workmanager-init"
    tools:node="remove" />
```

To learn more about using merge rules in your manifest, see the documentation on
[merging multiple manifest files](/studio/build/manage-manifests#merge-manifests).

### Implement Configuration.Provider

Have your `Application` class implement the
[`Configuration.Provider`](/reference/androidx/work/Configuration.Provider)
interface, and provide your own implementation of
[`Configuration.Provider.getWorkManagerConfiguration`](/reference/androidx/work/Configuration.Provider#getWorkManagerConfiguration()).
When you need to use WorkManager, make sure to call the method
[`WorkManager.getInstance(Context)`](/reference/androidx/work/WorkManager#getInstance(android.content.Context)).
WorkManager calls your app's custom `getWorkManagerConfiguration()` method to
discover its `Configuration`. (You do not need to call
`WorkManager.initialize` yourself.)

**Note:** If you call the deprecated no-parameter `WorkManager.getInstance()` method
before WorkManager has been initialized, the method throws an exception. You
should always use the `WorkManager.getInstance(Context)` method, even if you're
not customizing WorkManager.

Here's an example of a custom `getWorkManagerConfiguration()` implementation:

### Kotlin

```
class MyApplication() : Application(), Configuration.Provider {
     override fun getWorkManagerConfiguration() =
           Configuration.Builder()
                .setMinimumLoggingLevel(android.util.Log.INFO)
                .build()
}
```

### Java

```
class MyApplication extends Application implements Configuration.Provider {
    @Override
    public Configuration getWorkManagerConfiguration() {
        return new Configuration.Builder()
                .setMinimumLoggingLevel(android.util.Log.INFO)
                .build();
    }
}
```

**Note:** You must [remove the default
initializer](/topic/libraries/architecture/workmanager/advanced/custom-configuration#remove-default)
for a custom `getWorkManagerConfiguration()` implementation to take effect.

## Custom initialization before WorkManager 2.1.0

For versions of WorkManager before version 2.1.0, there are two initialization
options. In most cases, the
[default initialization](/topic/libraries/architecture/workmanager/advanced/custom-configuration#default)
is all you need. For more precise control of WorkManager, you can
[specify your own configuration](/topic/libraries/architecture/workmanager/advanced/custom-configuration#custom).

### Default initialization

WorkManager uses a custom `ContentProvider` to initialize itself when your app
starts. This code lives in the internal class
`androidx.work.impl.WorkManagerInitializer` and uses the default
[`Configuration`](/reference/androidx/work/Configuration).
The default initializer is automatically used unless you
[explicitly disable it](/topic/libraries/architecture/workmanager/advanced/custom-configuration#remove-default).
The default initializer is suitable for most apps.

### Custom initialization

If you want to control the initialization process, you must
[disable the default initializer](/topic/libraries/architecture/workmanager/advanced/custom-configuration#remove-default),
then define your own custom configuration.

Once the default initializer is removed, you can manually initialize
WorkManager:

### Kotlin

```
// provide custom configuration
val myConfig = Configuration.Builder()
    .setMinimumLoggingLevel(android.util.Log.INFO)
    .build()

// initialize WorkManager
WorkManager.initialize(this, myConfig)
```

### Java

```
// provide custom configuration
Configuration myConfig = new Configuration.Builder()
    .setMinimumLoggingLevel(android.util.Log.INFO)
    .build();

//initialize WorkManager
WorkManager.initialize(this, myConfig);
```

Make sure the initialization of the
[`WorkManager`](/reference/androidx/work/WorkManager)
singleton runs either in
[`Application.onCreate()`](/reference/android/app/Application#onCreate())
or in a
[`ContentProvider.onCreate()`](/reference/android/content/ContentProvider#onCreate()).

For the complete list of customizations available, see the
[`Configuration.Builder()`](/reference/androidx/work/Configuration.Builder)
reference documentation.