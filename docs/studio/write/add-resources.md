---
title: https://developer.android.com/studio/write/add-resources
url: https://developer.android.com/studio/write/add-resources
source: md.txt
---

# Add app resources

App resources, such as bitmaps and layouts, are organized into type-specific directories inside each module's`res/`directory. You can also add alternative versions of each file that are optimized for different device configurations, such as a high-res version of a bitmap for high-density screens.

Android Studio helps you add new resources and alternative resources in several ways, depending on the type of resource you want to add. This page describes how to add basic resource files, how to change the location of your resources, and how resource merging works.

See the following pages for details about how to create specific resource types:

- To add layout files, see[Build a UI with Layout Editor](https://developer.android.com/studio/write/layout-editor).
- To add string files, see[Localize the UI with Translations Editor](https://developer.android.com/studio/write/translations-editor).
- To add bitmaps, see[Create app icons with Image Asset Studio](https://developer.android.com/studio/write/image-asset-studio).
- To add SVG files, see[Add multi-density vector graphics](https://developer.android.com/studio/write/vector-asset-studio).

For information about how to reference the resources from your app code, see[App resources overview](https://developer.android.com/guide/topics/resources/providing-resources).

## Add an XML resource file

Although the preceding page links describe workflows that are customized to each type of resource, you can add any XML resource file by following these steps:

1. Click the target app module in the**Project** window in either the**Android** or**Project**view.

2. Select**File \> New \> Android resource file** .

   <br />

   ![](https://developer.android.com/static/studio/images/write/new-resource_2-2_2x.png)

   **Figure 1.** **New Resource File**dialog.
3. Fill out the details in the dialog:
   - **File name** : Enter the name for the XML file (this doesn't require the`.xml`suffix).
   - **Resource type**: Select the type of resource you want to create.
   - **Root element**: If applicable, select the root XML element for the file. Some resource types support only one type of root element. Depending on the resource type selected, this might not be editable.
   - **Source set** : Select the[source set](https://developer.android.com/studio/build#sourcesets)where you want to save the file.
   - **Directory name** : The directory must be named in a way that's specific to the resource type and configuration qualifiers. Don't edit this unless you want to add configuration qualifiers to the directory name manually (use**Available qualifiers**instead).
   - **Available qualifiers** : Instead of manually including configuration qualifiers in your directory name, you can add them by selecting a qualifier from the list and clicking**Add** ![](https://developer.android.com/static/studio/images/buttons/ic_add-arrows.png).
4. Once you've added all the qualifiers you want, click**OK**.

**Tip:** To open a simplified version of the**New Resource File** dialog that's specific to the resource type you want to add, right-click an existing resource directory within the**res** folder and select**New \><var translate="no">type-name</var>resource file**.

### Inline complex XML resources

Some complex resources require multiple XML resource files. For example, an animated vector drawable has a vector drawable object and an animation object and requires at least three XML files.

In this example, you can create and keep the three separate XML files if you need to reuse one or more of them. But if the XML files are used only for this animated vector drawable, you can instead use the inline resource format provided in the Android Asset Packaging Tool (AAPT). With AAPT, you can define all three resources in one XML file. For more information, see[Inline complex XML resources](https://developer.android.com/guide/topics/resources/complex-xml-resources).
| **Note:** Autocompletion isn't supported for inline resources. When developing new complex resources it can be easier to create them using separate resources and combine them into a single inline file once the resource is working as intended.

## Add a resource directory

To add a new resource directory, follow these steps:

1. Click the target app module in the**Project**window.

2. Select**File \> New \> Android resource directory** .

   <br />

   ![](https://developer.android.com/static/studio/images/write/new-resource-dir_2-2_2x.png)

   **Figure 2.** **New Resource Directory**dialog.
3. Fill in the details in the dialog:
   - **Directory name** : The directory must be named in a way that's specific to the resource type and combination of configuration qualifiers. Don't edit this unless you want to add configuration qualifiers to the directory name manually (use**Available qualifiers**instead).
   - **Resource type:**Select the type of resource you want the directory to contain.
   - **Source set:**Select the source set where you want the directory.
   - **Available qualifiers:** Instead of manually including configuration qualifiers in your directory name, you can add them by selecting a qualifier from the list and clicking**Add** ![](https://developer.android.com/static/studio/images/buttons/ic_add-arrows.png).
4. Once you've added all the qualifiers you want, click**OK**.

## Change your resource directory

By default, your resources are located in<var translate="no">module-name</var>`/src/`<var translate="no">source-set-name</var>`/res/`. For example, resources for your module's main source set are in`src/main/res/`, and resources for the debug source set are in`src/debug/res/`.

However, you can change these paths to any other location (relative to the`build.gradle`file) with the`res.srcDirs`property in the`sourceSets`block. For example:  

### Groovy

```groovy
android {
    sourceSets {
        main {
            res.srcDirs = ['resources/main']
        }
        debug {
            res.srcDirs = ['resources/debug']
        }
    }
}
```

### Kotlin

```kotlin
android {
    sourceSets {
        getByName("main") {
            res.srcDirs("resources/main")
        }
        getByName("debug") {
            res.srcDirs("resources/debug")
        }
    }
}
```

You can also specify multiple resource directories for one source set, and then the build tools merge them together. For example:  

### Groovy

```groovy
android {
    sourceSets {
        main {
            res.srcDirs = ['res1', 'res2']
        }
    }
}
```

### Kotlin

```kotlin
android {
    sourceSets {
        main {
            res.srcDirs("res1", "res2")
        }
    }
}
```
| **Note:** If two or more resource directories contain the same resource file, an error occurs during resource merging.

For more information, read about[source sets](https://developer.android.com/studio/build/build-variants#sourcesets).

## Resource merging

Resources in your final app file can come from three sources:

- The main source set (generally located in`src/main/res/`)
- [Build variant](https://developer.android.com/studio/build/build-variants)source sets
- Android libraries (AARs)

When all resources from each source set or library are unique, they're all added into the final app. A resource is considered unique if its filename is unique within both its[resource type](https://developer.android.com/guide/topics/resources/available-resources)directory and the[resource qualifier](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources)(if defined).

If there are two or more matching versions of the same resource, then only one version is included in the final app. The build tools select which version to keep based on the following priority order (highest priority on the left):
> build variant \> build type \> product flavor \> main source set \> library dependencies

For example, if the main source set contains:

- `res/layout/example.xml`
- `res/layout-land/example.xml`

And the debug build type contains:

- `res/layout/example.xml`

Then the final app includes`res/layout/example.xml`from the debug build type and`res/layout-land/example.xml`from the main source set.

However, if your build configuration specifies[multiple resource folders](https://developer.android.com/studio/write/add-resources#change_your_resource_directory)for a given source set and there are conflicts between those sources, an error occurs and the merge fails because each resource directory has the same priority.