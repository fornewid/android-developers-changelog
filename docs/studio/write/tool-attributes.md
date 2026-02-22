---
title: https://developer.android.com/studio/write/tool-attributes
url: https://developer.android.com/studio/write/tool-attributes
source: md.txt
---

# Tools attributes reference

Android Studio supports a variety of XML attributes in the`tools`namespace that enable design-time features, such as which layout to show in a fragment, or compile-time behaviors, such as which shrinking mode to apply to your XML resources. When you build your app, the build tools remove these attributes so that there is no effect on your APK size or runtime behavior.

To use these attributes, add the`tools`namespace to the root element of each XML file where you'd like to use them, as shown here:  

```xml
<RootTag xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools" >
```

## Error-handling attributes

The following attributes help suppress lint warning messages:

### `tools:ignore`

**Intended for:**Any element

**Used by:** [Lint](https://developer.android.com/studio/write/lint#configuring-lint-checking-in-xml)

This attribute accepts a comma-separated list of lint issue IDs that you'd like the tools to ignore on this element or any of its descendants.

For example, you can tell the tools to ignore the`MissingTranslation`error:  

    <string name="show_all_apps" tools:ignore="MissingTranslation">All</string>

### `tools:targetApi`

**Intended for**: Any element

**Used by**: Lint

This attribute works the same as the[`@TargetApi`](https://developer.android.com/reference/android/annotation/TargetApi)annotation in Java code. It lets you specify the API level (either as an integer or as a code name) that supports this element.

This tells the tools that you believe this element and any children are used only on the specified API level or higher. This stops lint from warning you if that element or its attributes are not available on the API level you specify as your`minSdkVersion`.

For example, you might use this attribute because[`GridLayout`](https://developer.android.com/reference/android/widget/GridLayout)is only available on API level 14 and higher, but you know this layout is not used in your code for any lower versions:  

    <GridLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        tools:targetApi="14" >

(However, note that we recommend that you use[`GridLayout`](https://developer.android.com/reference/androidx/gridlayout/widget/GridLayout)from the support library instead.)

### `tools:locale`

**Intended for:** `<resources>`

**Used by:**Lint, Android Studio editor

This tells the tools what the default language or locale is for the resources in the given`<resources>`element to avoid warnings from the spellchecker. The tool otherwise assumes the language is English.

The value must be a valid[locale qualifier](https://developer.android.com/guide/topics/resources/providing-resources#LocaleQualifier).

For example, you can add this to your default`values/strings.xml`file to indicate that the language used for the default strings is Spanish rather than English:  

    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:locale="es">

## Design-time view attributes

The following attributes define layout characteristics that are visible only in the Android Studio layout preview.

### `tools:`instead of`android:`

**Intended for:** `<View>`

**Used by:**Android Studio layout editor

You can insert sample data in your layout preview by using the`tools:`prefix instead of`android:`with any`<View>`attribute from the Android framework. This is useful when the attribute's value isn't populated until runtime and you want to see the effect in the layout preview.

For example, if the`android:text`attribute value is set at runtime, or you want to see the layout with a value different than the default, you can add`tools:text`to specify some text for the layout preview only.
![The tools:text attribute sets Google Voice as the value for the layout preview](https://developer.android.com/static/studio/images/write/tools-attribute-text_2x.png)**Figure 1.** The`tools:text`attribute sets "Google Voice" as the value for the layout preview.

You can add both the`android:`namespace attribute, which is used at runtime, and the matching`tools:`attribute, which overrides the runtime attribute in the layout preview only.

You can also use a`tools:`attribute to undo an attribute setting for the layout preview only. For example, if you have a`FrameLayout`with two children but you want to see only one child in the layout preview, you can set one of them to be invisible in the layout preview, as shown here:  

```xml
<Button
    android:id="@+id/button"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="First" />

<Button
    android:id="@+id/button2"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Second"
    tools:visibility="invisible"  />
```

When using the[Layout Editor](https://developer.android.com/studio/write/layout-editor)in design view, the**Properties** window lets you edit some design-time view attributes. Each design-time attribute is indicated with a wrench icon![The Wrench icon](https://developer.android.com/static/studio/images/buttons/layout-tools-attr.png)next to the attribute name to distinguish it from the real attribute of the same name.

### `tools:context`

**Intended for:** Any root`<View>`

**Used by:** Lint,[Android Studio Layout Editor](https://developer.android.com/studio/write/layout-editor#sample-data)

This attribute declares which activity this layout is associated with by default. This enables features in the editor or layout preview that require knowledge of the activity, such as what the layout theme is in the preview and where to insert`onClick`handlers generated from a quickfix, as shown in figure 2.
![Quickfix for the onClick attribute works only if you've set tools:context](https://developer.android.com/static/studio/images/write/tools-attribute-context_2x.png)**Figure 2.** Quickfix for the`onClick`attribute works only if you've set`tools:context`.

You can specify the activity class name using the same dot prefix as in the manifest file (excluding the full package name).

For example:  

    <android.support.constraint.ConstraintLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        tools:context=".MainActivity" >

| **Tip:** You can also select the theme for the layout preview from the[Layout Editor toolbar](https://developer.android.com/studio/write/layout-editor#change-appearance).

### `tools:itemCount`

**Intended for:** `<RecyclerView>`

**Used by:** [Android Studio Layout Editor](https://developer.android.com/studio/write/layout-editor#sample-data)

For a given[RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView), this attribute specifies the number of items the Layout Editor should render in the**Preview**window.

For example:  

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:itemCount="3"/>

### `tools:layout`

**Intended for:** `<fragment>`

**Used by:**Android Studio Layout Editor

This attribute declares which layout you want the layout preview to draw inside the fragment because the layout preview can't execute the activity code that normally applies the layout.

For example:  

    <fragment android:name="com.example.main.ItemListFragment"
        tools:layout="@layout/list_content" />

### `tools:listitem`,`tools:listheader`,`tools:listfooter`

**Intended for:** `<AdapterView>`(and subclasses like`<ListView>`)

**Used by:**Android Studio Layout Editor

These attributes specify which layout to show in the layout preview for a list's items, header, and footer. Any data fields in the layout are filled with numeric contents, such as "Item 1," so that the list items are not repetitive.

For example:  

    <ListView xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@android:id/list"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:listitem="@layout/sample_list_item"
        tools:listheader="@layout/sample_list_header"
        tools:listfooter="@layout/sample_list_footer" />

### `tools:showIn`

**Intended for:** Any root`<View>`in a layout that's referred to by an`<include>`

**Used by:**Android Studio Layout Editor

This attribute lets you point to a layout that uses this layout using[`<include>`](https://developer.android.com/training/improving-layouts/reusing-layouts), so you can preview and edit this file as it appears while embedded in its parent layout.

For example:  

    <TextView xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:text="@string/hello_world"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        tools:showIn="@layout/activity_main" />

Now the layout preview shows this`TextView`layout as it appears inside the`activity_main`layout.

### `tools:menu`

**Intended for:** Any root`<View>`

**Used by:**Android Studio Layout Editor

This attribute specifies which menu the layout preview shows in the[app bar](https://developer.android.com/training/appbar). The value is one or more menu IDs, separated by commas, without`@menu/`or any such ID prefix and without the`.xml`extension.

For example:  

    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:menu="menu1,menu2" />

### `tools:minValue`,`tools:maxValue`

**Intended for:** `<NumberPicker>`

**Used by:**Android Studio Layout Editor

These attributes set minimum and maximum values for a[NumberPicker](https://developer.android.com/reference/android/widget/NumberPicker)view.

For example:  

    <NumberPicker xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/numberPicker"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        tools:minValue="0"
        tools:maxValue="10" />

### `tools:openDrawer`

**Intended for:** `<DrawerLayout>`

**Used by:**Android Studio Layout Editor

This attribute lets you open a[DrawerLayout](https://developer.android.com/reference/androidx/drawerlayout/widget/DrawerLayout)in the preview.

You can also modify how the Layout Editor renders the layout by passing one of the following values:

**Table 1.** Values to modify how the Layout Editor renders a`DrawerLayout`

| Constant | Value  |                              Description                              |
|----------|--------|-----------------------------------------------------------------------|
| `end`    | 800005 | Push object to the end of its container, not changing its size.       |
| `left`   | 3      | Push object to the left of its container, not changing its size.      |
| `right`  | 5      | Push object to the right of its container, not changing its size.     |
| `start`  | 800003 | Push object to the beginning of its container, not changing its size. |

For example:  

    <androidx.drawerlayout.widget.DrawerLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/drawer_layout"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:openDrawer="start" />

### `"@tools:sample/*"`resources

**Intended for:**Any view that supports UI text or images

**Used by:** [Android Studio Layout Editor](https://developer.android.com/studio/write/layout-editor#sample-data)

This attribute lets you inject placeholder data or images into your view. For example, to test how your layout behaves with text before you have finalized UI text for your app, you can use placeholder text as follows:  

    <TextView xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        tools:text="@tools:sample/lorem" />

The following table describes the types of placeholder data you can inject into your layouts:

**Table 2.**Placeholder data for layouts

|          Attribute value           |                                        Description of placeholder data                                        |
|------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `@tools:sample/full_names`         | Full names randomly generated from the combination of`@tools:sample/first_names`and`@tools:sample/last_names` |
| `@tools:sample/first_names`        | Common first names                                                                                            |
| `@tools:sample/last_names`         | Common last names                                                                                             |
| `@tools:sample/cities`             | Names of cities from around the world                                                                         |
| `@tools:sample/us_zipcodes`        | Randomly generated US ZIP codes                                                                               |
| `@tools:sample/us_phones`          | Randomly generated phone numbers with the following format:`(800) 555-xxxx`                                   |
| `@tools:sample/lorem`              | Placeholder text in Latin                                                                                     |
| `@tools:sample/date/day_of_week`   | Randomized dates and times for the specified format                                                           |
| `@tools:sample/date/ddmmyy`        | Randomized dates and times for the specified format                                                           |
| `@tools:sample/date/mmddyy`        | Randomized dates and times for the specified format                                                           |
| `@tools:sample/date/hhmm`          | Randomized dates and times for the specified format                                                           |
| `@tools:sample/date/hhmmss`        | Randomized dates and times for the specified format                                                           |
| `@tools:sample/avatars`            | Vector drawables that you can use as profile avatars                                                          |
| `@tools:sample/backgrounds/scenic` | Images that you can use as backgrounds                                                                        |

## Resource shrinking attributes

The following attributes let you enable strict reference checks and declare whether to keep or discard certain resources when using[resource shrinking](https://developer.android.com/studio/build/shrink-code#shrink-resources).

To enable resource shrinking, set the`shrinkResources`property to`true`in your`build.gradle`file, alongside`minifyEnabled`for code shrinking.

For example:  

### Groovy

```groovy
android {
    ...
    buildTypes {
        release {
            shrinkResources true
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'),
                    'proguard-rules.pro'
        }
    }
}
```

### Kotlin

```kotlin
android {
    ...
    buildTypes {
        getByName("release") {
            isShrinkResources = true
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

### `tools:shrinkMode`

**Intended for:** `<resources>`

**Used by:**Build tools with resource shrinking

This attribute lets you specify whether the build tools should use the following:

- **Safe mode:** Keep all resources that are explicitly cited and that*might* be referenced dynamically with a call to[`Resources.getIdentifier()`](https://developer.android.com/reference/android/content/res/Resources#getIdentifier(java.lang.String,%20java.lang.String,%20java.lang.String)).
- **Strict mode:**Keep only the resources that are explicitly cited in code or in other resources.

The default is to use safe mode (`shrinkMode="safe"`). To instead use strict mode, add`shrinkMode="strict"`to the`<resources>`tag as shown here:  

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:shrinkMode="strict" />

When you enable strict mode, you might need to use[`tools:keep`](https://developer.android.com/studio/write/tool-attributes#toolskeep)to keep resources that were removed but that you actually want, and use[`tools:discard`](https://developer.android.com/studio/write/tool-attributes#toolsdiscard)to explicitly remove even more resources.

For more information, see[Shrink your resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).

### `tools:keep`

**Intended for:** `<resources>`

**Used by:**Build tools with resource shrinking

When using resource shrinking to remove unused resources, this attribute lets you specify resources to keep, typically because they are referenced in an indirect way at runtime, such as by passing a dynamically generated resource name to[`Resources.getIdentifier()`](https://developer.android.com/reference/android/content/res/Resources#getIdentifier(java.lang.String,%20java.lang.String,%20java.lang.String)).

To use, create an XML file in your resources directory (for example,`res/raw/keep.xml`) with a`<resources>`tag and specify each resource to keep in the`tools:keep`attribute as a comma-separated list. You can use the asterisk character as a wild card.

For example:  

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:keep="@layout/used_1,@layout/used_2,@layout/*_3" />

For more information, see[Shrink your resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).

### `tools:discard`

**Intended for:** `<resources>`

**Used by:**Build tools with resource shrinking

When using resource shrinking to remove unused resources, this attribute lets you specify resources you want to manually discard, typically because the resource is referenced but in a way that does not affect your app or because the Gradle plugin has incorrectly deduced that the resource is referenced.

To use, create an XML file in your resources directory (for example,`res/raw/keep.xml`) with a`<resources>`tag and specify each resource to discard in the`tools:discard`attribute as a comma-separated list. You can use the asterisk character as a wild card.

For example:  

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:discard="@layout/unused_1" />

For more information, see[Shrink your resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).