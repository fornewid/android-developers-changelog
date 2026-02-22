---
title: https://developer.android.com/guide/navigation/integrations/feature-modules
url: https://developer.android.com/guide/navigation/integrations/feature-modules
source: md.txt
---

The Dynamic Navigator library extends the functionality of the
[Jetpack Navigation component](https://developer.android.com/guide/navigation) to work with destinations
that are defined in
[feature modules](https://developer.android.com/guide/app-bundle/dynamic-delivery#customize_delivery).
This library also provides seamless installation of on-demand feature
modules when navigating to these destinations.
| **Note:** If you are not familiar with Play Feature Delivery, review the [feature module guide](https://developer.android.com/guide/app-bundle/dynamic-delivery#customize_delivery) and [additional resources](https://developer.android.com/guide/app-bundle/dynamic-delivery#additional_resources) before continuing.

## Setup

To support feature modules, use the following dependencies in your app module's `build.gradle` file:  

### Groovy

```groovy
dependencies {
    def nav_version = "2.9.7"

    api "androidx.navigation:navigation-fragment-ktx:$nav_version"
    api "androidx.navigation:navigation-ui-ktx:$nav_version"
    api "androidx.navigation:navigation-dynamic-features-fragment:$nav_version"
}
```

### Kotlin

```kotlin
dependencies {
    val nav_version = "2.9.7"

    api("androidx.navigation:navigation-fragment-ktx:$nav_version")
    api("androidx.navigation:navigation-ui-ktx:$nav_version")
    api("androidx.navigation:navigation-dynamic-features-fragment:$nav_version")
}
```

Note that the other Navigation dependencies should use [api configurations](https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_separation)
so that they are available to your feature modules.

## Basic usage

To support feature modules, first change all instances of
`NavHostFragment` in your app to
`androidx.navigation.dynamicfeatures.fragment.DynamicNavHostFragment`:  

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/nav_host_fragment"
        android:name="androidx.navigation.dynamicfeatures.fragment.DynamicNavHostFragment"
        app:navGraph="@navigation/nav_graph"
        ... />

Next, add an `app:moduleName` attribute to any `<activity>`, `<fragment>`, or
`<navigation>` destinations in your `com.android.dynamic-feature` module's
navigation graphs that are associated with a `DynamicNavHostFragment`.
This attribute tells the Dynamic Navigator library that the destination
belongs to a feature module with the name that you specify.
**Note:** The `moduleName` needs to match your app's `dynamicFeatures` property as declared in the `build.gradle` file.  

    <fragment
        app:moduleName="myDynamicFeature"
        android:id="@+id/featureFragment"
        android:name="com.google.android.samples.feature.FeatureFragment"
        ... />

When you navigate to one of these destinations, the Dynamic Navigator library
first checks if the feature module is installed. If the feature
module is already present, your app navigates to the destination as expected.
If the module isn't present, your app shows an intermediate progress fragment
destination as it installs the module. The default implementation of the
progress fragment shows a basic UI with a progress bar and handles any
installation errors.
![two loading screens that show UI with a progress bar when navigating
to a feature module for the first time](https://developer.android.com/static/images/guide/navigation/dfm-nav-loading.png) **Figure 1.** UI showing a progress bar when a user navigates to an on-demand feature for the first time. The app displays this screen as the corresponding module downloads.

To customize this UI, or to manually handle installation
progress from within your own app screen, see the
[Customize the progress fragment](https://developer.android.com/guide/navigation/integrations/feature-modules#customize) and
[Monitor the request state](https://developer.android.com/guide/navigation/integrations/feature-modules#monitor) sections in this topic.

Destinations that don't specify `app:moduleName` continue to work without
changes and behave as though your app uses a regular `NavHostFragment`.

## Customize the progress fragment

You can override the progress fragment implementation for each navigation graph
by setting the `app:progressDestination` attribute to the ID of the destination
you want to use for handling installation progress. Your custom progress
destination should be a
[`Fragment`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) that derives from
[`AbstractProgressFragment`](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/AbstractProgressFragment).
You must override the abstract methods for notifications about installation
progress, errors, and other events. You can then show installation progress in a
UI of your choice.

The default implementation's
[`DefaultProgressFragment`](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/navigation/navigation-dynamic-features-fragment/src/main/java/androidx/navigation/dynamicfeatures/fragment/ui/DefaultProgressFragment.kt)
class uses this API to show installation progress.

## Monitor the request state

The Dynamic Navigator library enables you to implement a UX flow similar to the
one in
[UX best practices for on-demand delivery](https://developer.android.com/studio/projects/dynamic-delivery/ux-guidelines),
in which a user stays in the context of a previous screen while waiting for
installation to finish. This means that you don't need to show an intermediate
UI or progress fragment at all.
![screen that shows a bottom nav bar with an icon that indicates
that a feature module is downloading](https://developer.android.com/static/images/guide/navigation/nav-dfm-ui.png) **Figure 2.** Screen that shows download progress from a bottom navigation bar.

In this scenario, you are responsible for
monitoring and handling all installation states, progress changes, errors, and
so on.

To initiate this non-blocking navigation flow, pass a
[`DynamicExtras`](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/DynamicExtras)
object that contains a
[`DynamicInstallMonitor`](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/DynamicInstallMonitor)
to
[`NavController.navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(int,%20android.os.Bundle,%20androidx.navigation.NavOptions,%20androidx.navigation.Navigator.Extras)),
as shown in the following example:  

### Kotlin

```kotlin
val navController = ...
val installMonitor = DynamicInstallMonitor()

navController.navigate(
    destinationId,
    null,
    null,
    DynamicExtras(installMonitor)
)
```

### Java

```java
NavController navController = ...
DynamicInstallMonitor installMonitor = new DynamicInstallMonitor();

navController.navigate(
    destinationId,
    null,
    null,
    new DynamicExtras(installMonitor);
)
```

Immediately after calling `navigate()`, you should check the value of
`installMonitor.isInstallRequired` to see if the attempted navigation resulted
in a feature module installation.

- If the value is `false`, you're navigating to a normal destination and don't need to do anything else.
- If the value is `true`, you should start observing the `LiveData` object that
  is now in `installMonitor.status`. This `LiveData` object emits
  [`SplitInstallSessionState`](https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallSessionState)
  updates from the Play Core library. These updates contain installation
  progress events that you can use to update the UI. Remember to handle all
  relevant statuses as outlined in the
  [Play Core guide](https://developer.android.com/guide/app-bundle/playcore),
  including
  [asking for user confirmation](https://developer.android.com/guide/playcore/dynamic-delivery#obtain_confirmation)
  if necessary.

  ### Kotlin

  ```kotlin
  val navController = ...
  val installMonitor = DynamicInstallMonitor()

  navController.navigate(
    destinationId,
    null,
    null,
    DynamicExtras(installMonitor)
  )

  if (installMonitor.isInstallRequired) {
    installMonitor.status.observe(this, object : Observer<SplitInstallSessionState> {
        override fun onChanged(sessionState: SplitInstallSessionState) {
            when (sessionState.status()) {
                SplitInstallSessionStatus.INSTALLED -> {
                    // Call navigate again here or after user taps again in the UI:
                    // navController.navigate(destinationId, destinationArgs, null, null)
                }
                SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION -> {
                    SplitInstallManager.startConfirmationDialogForResult(...)
                }

                // Handle all remaining states:
                SplitInstallSessionStatus.FAILED -> {}
                SplitInstallSessionStatus.CANCELED -> {}
            }

            if (sessionState.hasTerminalStatus()) {
                installMonitor.status.removeObserver(this);
            }
        }
    });
  }
  ```

  ### Java

  ```java
  NavController navController = ...
  DynamicInstallMonitor installMonitor = new DynamicInstallMonitor();

  navController.navigate(
    destinationId,
    null,
    null,
    new DynamicExtras(installMonitor);
  )

  if (installMonitor.isInstallRequired()) {
    installMonitor.getStatus().observe(this, new Observer<SplitInstallSessionState>() {
        @Override
        public void onChanged(SplitInstallSessionState sessionState) {
            switch (sessionState.status()) {
                case SplitInstallSessionStatus.INSTALLED:
                    // Call navigate again here or after user taps again in the UI:
                    // navController.navigate(mDestinationId, mDestinationArgs, null, null);
                    break;
                case SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION:
                    SplitInstallManager.startConfirmationDialogForResult(...)
                    break;

                // Handle all remaining states:
                case SplitInstallSessionStatus.FAILED:
                    break;
                case SplitInstallSessionStatus.CANCELED:
                    break;
            }

            if (sessionState.hasTerminalStatus()) {
                installMonitor.getStatus().removeObserver(this);
            }
        }
    });
  }
  ```

When the installation finishes, the `LiveData` object emits a
`SplitInstallSessionStatus.INSTALLED` status. You should then call
`NavController.navigate()` again. Since the module is now installed, the call
now succeeds, and the app navigates to the destination as expected.

After reaching a terminal state, such as when installation completes or when
installation fails, you should remove your `LiveData` observer to avoid memory
leaks. You can check if the status represents a terminal state by using
`SplitInstallSessionStatus.hasTerminalStatus()`.

See [`AbstractProgressFragment`](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/AbstractProgressFragment)
for an example implementation of this observer.

## Included graphs

The Dynamic Navigator library supports including graphs that are defined in
feature modules. To include a graph that is defined in a feature
module, do the following:

1. Use `<include-dynamic/>` instead of `<include/>`, as shown in the following
   example:

       <include-dynamic
           android:id="@+id/includedGraph"
           app:moduleName="includedgraphfeature"
           app:graphResName="included_feature_nav"
           app:graphPackage="com.google.android.samples.dynamic_navigator.included_graph_feature" />

2. Inside `<include-dynamic ... />`, you must specify the following attributes:

   - `app:graphResName`: the name of the navigation graph resource file. The name is derived from the graph's file name. For example, if the graph is in `res/navigation/nav_graph.xml`, the resource name is `nav_graph`.
   - `android:id` - the graph destination ID. The Dynamic Navigator library ignores any `android:id` values that are found in the root element of the included graph.
   - `app:moduleName`: the package name of the module.

### Use the correct graphPackage

It is important to get the `app:graphPackage` correct as the Navigation
component will not be able to include the specified `navGraph` from the feature
module, otherwise.
| **Caution:** The package name of the dynamic feature module is generated automatically by the build toolchain, and any values in the `AndroidManifest.xml` or `build.gradle` in your dynamic module will be ignored.

The package name of a dynamic feature module is constructed by appending the
name of the module to the `applicationId` of the base app module. So if the
base app module has an `applicationId` of `com.example.dynamicfeatureapp` and
the dynamic feature module is named `DynamicFeatureModule`, then the package
name of the dynamic module will be
`com.example.dynamicfeatureapp.DynamicFeatureModule`. This package name is
case-sensitive.

If you're in any doubt, you can confirm the package name of the feature module
by checking the generated `AndroidManifest.xml`. After building the project go
to `<DynamicFeatureModule>/build/intermediates/merged_manifest/debug/AndroidManifest.xml`,
which should look something like this:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:dist="http://schemas.android.com/apk/distribution"
    featureSplit="DynamicFeatureModule"
    package="com.example.dynamicfeatureapp"
    android:versionCode="1"
    android:versionName="1.0" >

    <uses-sdk
        android:minSdkVersion="21"
        android:targetSdkVersion="30" />

    <dist:module
        dist:instant="false"
        dist:title="@string/title_dynamicfeaturemodule" >
        <dist:delivery>
            <dist:install-time />
        </dist:delivery>

        <dist:fusing dist:include="true" />
    </dist:module>

    <application />

</manifest>
```

The `featureSplit` value should match the name of the dynamic feature module, and the package will match the `applicationId` of the base app module. The `app:graphPackage` is the combination of these: `com.example.dynamicfeatureapp.DynamicFeatureModule`.

### Navigating to an include-dynamic navigation graph

It is only possible to navigate to the `startDestination` of an
`include-dynamic` navigation graph. The dynamic module is responsible for its
own navigation graph and the base app has no knowledge of that.

The include-dynamic mechanism enables the base app module to include a
[nested navigation graph](https://developer.android.com/guide/navigation/navigation-nested-graphs)
that is defined within the dynamic module. This nested navigation graph behaves
like any nested navigation graph. The root navigation graph (that is, the parent
of the nested graph) can only define the nested navigation graph itself as a
destination and not its children. Thus, the `startDestination` is used when
the include-dynamicnavigation graph is the destination.

## Limitations

- Dynamically-included graphs don't currently support deep links.
- Dynamically-loaded nested graphs (that is, a `<navigation>` element with an `app:moduleName`) don't currently support deep links.