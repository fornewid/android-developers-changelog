---
title: https://developer.android.com/studio/write/tool-attributes
url: https://developer.android.com/studio/write/tool-attributes
source: md.txt
---

While Jetpack Compose handles UI design-time tooling directly in Kotlin, the
`tools:` namespace is still essential for project-level configurations. Standard
Android XML files, like `AndroidManifest.xml` and `res/raw/keep.xml`, use
`tools:` attributes to manage Lint warnings and configure the resource shrinker.

When you build your app, the build tools remove these attributes so
that there is no effect on your APK size or runtime behavior.

To use these attributes, add the `tools` namespace to the root element of each
XML file where you'd like to use them, as shown here:

```xml
<RootTag xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools" >
```

> [!NOTE]
> **Note:** To learn how to render UIs, inject sample data, and test configurations, see [Preview your UI with composable previews](https://developer.android.com/develop/ui/compose/tooling/previews).

## Error-handling attributes

The following attributes help suppress lint warning messages:

### `tools:ignore`

**Intended for:** Any element

**Used by:** [Lint](https://developer.android.com/studio/write/lint#configuring-lint-checking-in-xml)

This attribute accepts a comma-separated list of lint issue IDs that you'd like
the tools to ignore on this element or any of its descendants.

For example, you can tell the tools to ignore the `MissingTranslation` error:

    <string name="show_all_apps" tools:ignore="MissingTranslation">All</string>

### `tools:targetApi`

**Intended for**: Any element

**Used by**: Lint

This attribute works the same as the [`@TargetApi`](https://developer.android.com/reference/android/annotation/TargetApi) annotation in Java code
or the `@RequiresApi` annotation in Kotlin code. It lets you specify the API
level (either as an integer or as a code name) that supports this element.

This tells the lint tools that you believe this element and any children are
used only on the specified API level or higher. This stops lint from warning you
if that element or its attributes are not available on the API level you specify
as your `minSdkVersion`.

For example, you might use this attribute because you are declaring a
`<service>` in your `AndroidManifest.xml` that uses a foreground service type
only available on API level 34 and higher, but your project's `minSdkVersion`
is lower:

    <service
        android:name=".playback.MediaPlaybackService"
        android:foregroundServiceType="mediaPlayback"
        xmlns:tools="http://schemas.android.com/tools"
        tools:targetApi="34" />

### `tools:locale`

**Intended for:** `<resources>`

**Used by:** Lint, Android Studio editor

This tells the tools what the default language or locale is for the resources in
the given `<resources>` element to avoid warnings from the spellchecker.
The tool otherwise assumes the language is English.

The value must be a valid [locale
qualifier](https://developer.android.com/guide/topics/resources/providing-resources#LocaleQualifier).

For example, you can add this to your default `values/strings.xml` file to
indicate that the language used for the default strings is
Spanish rather than English:

    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:locale="es">

## Resource shrinking attributes

The following attributes let you enable strict reference checks and declare
whether to keep or discard certain resources when using
[resource shrinking](https://developer.android.com/studio/build/shrink-code#shrink-resources).

To enable resource shrinking, set the `shrinkResources` property to `true`
in your `build.gradle` file, alongside `minifyEnabled` for code shrinking.

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

**Used by:** Build tools with resource shrinking

This attribute lets you specify whether the build tools should use the
following:

- **Safe mode:** Keep all resources that are explicitly cited and that *might* be referenced dynamically with a call to [`Resources.getIdentifier()`](https://developer.android.com/reference/android/content/res/Resources#getIdentifier(java.lang.String,%20java.lang.String,%20java.lang.String)).
- **Strict mode:** Keep only the resources that are explicitly cited in code or in other resources.

The default is to use safe mode (`shrinkMode="safe"`). To instead use
strict mode, add `shrinkMode="strict"` to the `<resources>` tag as shown here:

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:shrinkMode="strict" />

When you enable strict mode, you might need to use [`tools:keep`](https://developer.android.com/studio/write/tool-attributes#toolskeep)
to keep resources that were removed but that you actually want, and use
[`tools:discard`](https://developer.android.com/studio/write/tool-attributes#toolsdiscard) to explicitly remove even more resources.

For more information, see
[Shrink your resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).

### `tools:keep`

**Intended for:** `<resources>`

**Used by:** Build tools with resource shrinking

When using resource shrinking to remove unused resources, this
attribute lets you specify resources to keep, typically because they are
referenced in an indirect way at runtime, such as by passing a dynamically
generated resource name to
[`Resources.getIdentifier()`](https://developer.android.com/reference/android/content/res/Resources#getIdentifier(java.lang.String,%20java.lang.String,%20java.lang.String)).

To use, create an XML file in your resources directory (for example,
`res/raw/keep.xml`) with a `<resources>` tag
and specify each resource to keep in the `tools:keep` attribute as a
comma-separated list. You can use the asterisk character as a wildcard.

For example:

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:keep="@layout/used_1,@layout/used_2,@layout/*_3" />

For more information, see [Shrink your resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).

### `tools:discard`

**Intended for:** `<resources>`

**Used by:** Build tools with resource shrinking

When using resource shrinking to remove unused resources, this attribute
lets you specify resources you want to manually discard, typically because
the resource is referenced but in a way that does not affect your app or
because the Gradle plugin has incorrectly deduced that the resource is
referenced.

To use, create an XML file in your resources directory (for example,
`res/raw/keep.xml`) with a `<resources>` tag
and specify each resource to discard in the `tools:discard` attribute as a
comma-separated list. You can use the asterisk character as a wildcard.

For example:

    <?xml version="1.0" encoding="utf-8"?>
    <resources xmlns:tools="http://schemas.android.com/tools"
        tools:discard="@layout/unused_1" />

For more information, see
[Shrink your resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).

## Additional resources

### Views content

- [Tools attributes reference (Views)](https://developer.android.com/studio/views/tool-attributes-views)