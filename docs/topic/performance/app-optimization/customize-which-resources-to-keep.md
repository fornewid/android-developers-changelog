---
title: https://developer.android.com/topic/performance/app-optimization/customize-which-resources-to-keep
url: https://developer.android.com/topic/performance/app-optimization/customize-which-resources-to-keep
source: md.txt
---

# Customize which resources to keep

When you[enable app optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization), the`isShrinkResources = true`setting instructs the optimizer to remove resources that are unused, which helps reduce the size of your app. Resource shrinking works only in conjunction with code shrinking, so if you're optimizing resources, also set`isMinifyEnabled = true`, for example:  

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            ...
        }
    }

If you want to keep or discard specific resources, create an XML*keep* file in your project resources, for example`res/raw/my.package.keep.xml`. The keep file has the following components:

- `<resources>`tag --- Contains all child resource elements and keep/discard attributes.
- `tools:keep`attribute --- Accepts a comma-separated list of resource names that identify resources to keep
- `tools:discard`attribute --- Accepts a comma-separated list of resource names that identify resources to discard

Use the asterisk character as a wildcard to reference multiple resources in the same folder, for example:  

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:keep="@layout/l_used*_c,@layout/l_used_a,@layout/l_used_b*"
        tools:discard="@layout/unused2" />

| **Note:**
|
| - Keep files have global scope. Give your keep files unique filenames that include the file's package name. Unique filenames ensure keep files from different libraries won't conflict, causing potential issues with ignored rules or unneeded kept resources, when different libraries are linked together.
| - The build doesn't package the keep file into your app.
| - You should rarely need to keep resources. The use of[`getIdentifier()`](https://developer.android.com/reference/android/content/res/Resources#getIdentifier(java.lang.String,%20java.lang.String,%20java.lang.String))is an exception; however, retrieving resources by identifier is more efficient than retrieving them by name with`getIdentifier()`.

Specifying which resources to discard might seem superfluous when you could instead delete them, but discarding resources can be useful when using build variants.

## Target specific build variants

To remove resources in only some build variants, put all your resources into the common project directory, then create a different`my.package.build.variant.keep.xml`file for each build variant in the variant's resource directory. In the keep file, manually specify resources to remove when a given resource appears to be used in code (and therefore not removed by the shrinker), but you know it actually won't be used for the given build variant.

## Remove unused alternative resources

The optimizer only removes resources that aren't referenced by your app code, which means the optimizer won't remove[alternative resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)for different device configurations.

Use the Android Gradle`resConfigs`property in your app's module`build.gradle`file to remove alternative resource files that your app does not need.

For example, if you are using a library that includes language resources (such as Google Play Services), then your app includes all translated language strings for the messages in those libraries whether the rest of your app is translated to the same languages or not. To keep only the languages that your app officially supports, specify those languages using the`resConfigs`property. Any resources for languages not specified are removed.

The following snippets show how to limit your language resources to just English and French:  

    android {
        defaultConfig {
            ...
            resourceConfigurations.addAll(listOf("en", "fr"))
        }
    }

or  

    android {
        defaultConfig {
            ...
            resConfigs "en", "fr"
        }
    }

When you publish an app using the Android App Bundle (AAB) format, by default only languages configured on a user's device are downloaded when the user installs the app. Similarly, only resources matching the device's screen density and native libraries matching the device's ABI are included in the download. For more information, see[Re-enable or disable types of configuration APKs](https://developer.android.com/guide/app-bundle/configure-base#disable_config_apks).

For legacy apps releasing with APKs (created before August 2021), you can customize the screen density or ABI resources to include in your APK by[building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits)that target different device configurations.

## Avoid conflicts when merging resources

By default, the Android Gradle plugin (AGP) merges identically named resources, such as drawables with the same name that are in different resource folders. This behavior is not controlled by the`shrinkResources`property and cannot be disabled because the behavior is necessary to avoid errors when multiple resources have the name your code is referencing.

Resource merging occurs only when two or more files share an identical resource name, type, and qualifier. AGP selects the file it identifies to be the best choice among the duplicates (based on a priority order described below) and passes only that one resource to AAPT for distribution in the final build artifact.

AGP looks for duplicate resources in the following locations:

- Main resources, associated with the main source set, generally located in`src/main/res/`
- Variant overlays, from the build type and build flavors
- Library project dependencies

AGP merges duplicate resources in the following cascading priority order:  
Dependencies → Main → Build flavor → Build type

For example, if a duplicate resource appears in both your main resources and a build flavor, Gradle selects the resource in the build flavor.

If identical resources appear in the same source set, Gradle cannot merge them and emits a resource merge error. This can happen if you define multiple source sets in the`sourceSet`property of your module`build.gradle`file, for example, if both`src/main/res/`and`src/main/res2/`contain identical resources.

## Troubleshoot resource shrinking

When you shrink resources, the**Build** window shows a summary of the resources removed from the app. (Click**Toggle view**on the left side of the window to display detailed text output from Gradle.) For example:  

    :android:shrinkDebugResources
    Removed unused resources: Resource data reduced from 2570KB to 1711KB: Removed 33%
    :android:validateDebugSigning

Gradle also creates a diagnostic file named`resources.txt`in`<module-name>/build/outputs/mapping/release/`(the same folder as ProGuard's output files). The file includes details such as which resources reference other resources and which resources are used or removed.

For example, to find out why`@drawable/ic_plus_anim_016`is still in your app, open the`resources.txt`file and search for that filename. You might find that it's referenced from another resource:  

    16:25:48.005 [QUIET] [system.out] @drawable/add_schedule_fab_icon_anim : reachable=true
    16:25:48.009 [QUIET] [system.out] @drawable/ic_plus_anim_016

You now need to know why`@drawable/add_schedule_fab_icon_anim`is reachable; and if you search upwards, you'll find the resource listed under the heading*The root reachable resources are:* in`resources.txt`.

This means there's a code reference to`add_schedule_fab_icon_anim`, that is, its`R.drawable`ID was found in the reachable code.

Unless you're using strict checking, resource IDs can be marked as reachable if there are string constants that look like they might be used to construct resource names for dynamically loaded resources. In that case, if you search the build output for the resource name, you might find a message like this:  

    10:32:50.590 [QUIET] [system.out] Marking drawable:ic_plus_anim_016:2130837506
        used because its format-string matches string pool constant ic_plus_anim_%1$d.

If you see one of these strings and you are certain that the string is not being used to load the given resource dynamically, use the`tools:discard`attribute in your keep file to inform the build system to remove the resource.