---
title: https://developer.android.com/topic/architecture/views/resources/localization-views
url: https://developer.android.com/topic/architecture/views/resources/localization-views
source: md.txt
---

[Concepts and Jetpack Compose implementation](https://developer.android.com/guide/topics/resources/localization)

Android runs on many devices in many regions. To reach the most users, make sure
that your app handles text, audio files, numbers, currency, and graphics in
ways appropriate to the locales where your app is used.

This page describes some best practices for localizing Android apps.

You need to have a working knowledge of either Kotlin or the Java programming
language and be familiar with [Android resource loading](https://developer.android.com/guide/topics/resources/providing-resources),
[declaring user interface elements in XML](https://developer.android.com/guide/topics/ui/declaring-layout), development considerations
such as the [activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle),
and general principles of internationalization and localization.

It is good practice to use the Android resource framework to separate the
localized aspects of your app as much as possible from core app functionality.

- Put most or all of the *contents* of your app's user interface into resource files, as described on this page and in the [App resources overview](https://developer.android.com/guide/topics/resources/providing-resources).
- The *behavior* of the user interface, on the other hand, is driven by your Kotlin-based or Java-based code. For example, if users input data that needs to be formatted or sorted differently depending on locale, then you use Kotlin or the Java programming language to handle the data programmatically. This page doesn't cover how to localize your Kotlin-based or Java-based code.

For a short guide to localizing strings in your app, see
[Support different languages and cultures](https://developer.android.com/training/basics/supporting-devices/languages).

## Use resources for localization

This section discusses how to create default resources as well as alternative
resources. It also explains how resources are assigned precedence and how you
refer to your resources in code.

### Create default resources

Put the app's default text in `res/values/strings.xml`. For these strings, use
the default language---the language you expect most of your app's users to speak.

The default resource set also includes any default drawables and layouts
and can include other types of resources such as animations. These resources
go in the following directories:

- `res/drawable/`: required directory holding at least one graphic file, for the app's icon on Google Play
- `res/layout/`: required directory holding an XML file that defines the default layout
- `res/anim/`: required if you have any `res/anim-\<qualifiers\>` folders
- `res/xml/`: required if you have any `res/xml-\<qualifiers\>` folders
- `res/raw/`: required if you have any `res/raw-\<qualifiers\>` folders

**Tip:** In your code, examine each reference to an
Android resource. Make sure that a default resource is defined for each one.
Also make sure that the default string file is complete: a *localized*
string file can contain a subset of the strings, but the *default* string
file must contain them all.

## Localization tips

Follow these tips as you localize your app.

#### Design a flexible layout

If you need to rearrange your layout to fit a certain language,
you can create an alternative layout for that language, such as
`res/layout-de/main.xml` for a German-language layout. However, doing this
can make your app harder to maintain. It is better to create a single
layout that is more flexible.

Another typical situation is a language that requires something different in
its layout. For example, you might have a contact form that includes two
name fields when the app runs in Japanese, but three name fields when
the app runs in some other language. You can handle this in either of
two ways:

- Create one layout with a field that you can programmatically enable or disable, based on the language.
- Have the main layout include another layout that includes the changeable field. The second layout can have different configurations for different languages.

#### Use the Android Context object for manual locale lookup

You can look up the locale using the [`Context`](https://developer.android.com/reference/android/content/Context) object
that Android makes available, as shown in the following example:

### Kotlin

```kotlin
val primaryLocale: Locale = context.resources.configuration.locales[0]
val locale: String = primaryLocale.displayName
```

### Java

```java
Locale primaryLocale = context.getResources().getConfiguration().getLocales().get(0);
String locale = primaryLocale.getDisplayName();
```