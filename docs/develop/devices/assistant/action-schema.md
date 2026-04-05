---
title: https://developer.android.com/develop/devices/assistant/action-schema
url: https://developer.android.com/develop/devices/assistant/action-schema
source: md.txt
---

Once you identify your in-app functionality and corresponding built-in intent
(BII) to implement, declare the BIIs your functionality supports by defining
a `capability` element in a `shortcuts.xml` resource file. Declaring a BII
as a `capability` registers support for that semantic intent in your app, and
enables voice query fulfillment of the intent using Google Assistant.

Assistant uses natural language processing to extract parameters from a user
query. The [built-in intents reference](https://developer.android.com/reference/app-actions/built-in-intents) lists the fields that each BII is
capable of extracting from an associated user query. For example, if a user
invokes the \[`actions.intent.GET_FOOD_OBSERVATION`\]\[\] capability in your app by
saying, *"Hey Google, Ask ExampleApp what did I eat for Lunch last Friday"*, Assistant
extracts the following BII parameters from the user request:

- `foodObservation.forMeal` = "https://schema.googleapis.com/MealTypeLunch"
- `foodObservation.startTime` = "2024-09-06T00:00:00"
- `foodObservation.endTime` = "2024-09-06T23:59:59"

Assistant passes BII parameters to the fulfillment `intent` defined in the
`capability`. One or more `intent` elements can be defined in a capability to
accommodate the different ways a user might invoke a BII. For instance, you
could define a fulfillment `intent` that requires both BII parameters in the
above example. You could then define a second intent that requires a single BII
parameter, `foodObservation.forMeal`, that reports for all meals on a particular day, like *"Hey Google, Ask ExampleApp what did I eat for Lunch."*

> [!NOTE]
> **Note:** A *fallback* `intent` that does not require a parameter to be present to fulfill a user request is required for each `capability`. These fallback intents improve the user experience by allowing actions to succeed even for vague user queries like *"Hey Google, Ask ExampleApp what did I eat."*

## Overview

You configure App Actions using a `shortcuts.xml` file placed in your app
project's `res/xml` directory, and then creating a reference to `shortcuts.xml`
in your app manifest. Add a reference to `shortcuts.xml` in your app manifest
by following these steps:

1. In your app's manifest file (`AndroidManifest.xml`), find an activity whose
   intent filters are set to the `android.intent.action.MAIN` action and the
   `android.intent.category.LAUNCHER` category.

2. Add a reference to `shortcuts.xml` in `AndroidManifest.xml` using a
   [`<meta-data>`](https://developer.android.com/guide/topics/manifest/meta-data-element) tag in the `Activity` that has intent
   filters for both `MAIN` and `LAUNCHER`, as follows:

       <meta-data
          android:name="android.app.shortcuts"
          android:resource="@xml/shortcuts" />

The above example declares an XML resource for the `xml/shortcuts.xml` file in
the APK. For more details on configuring shortcuts, see
[Create static shortcuts](https://developer.android.com/guide/topics/ui/shortcuts/creating-shortcuts#static) in the Android developer documentation.

> [!NOTE]
> **Note:** If you're using an obfuscation tool for your release APK, disable obfuscation for your app's `shortcuts.xml` file by using an allowlist. If you don't, you're likely to encounter an error when you upload your APK to the Google Play Console.

The Jetpack library [`androidx.core:core:1.6.0`](https://developer.android.com/jetpack/androidx/releases/core)
(or greater) is required in your Android project to avoid compilation errors
when defining App Actions capabilities in `shortcuts.xml`. For details, see
[Getting started with Android Jetpack](https://developer.android.com/jetpack/getting-started).

### Static shortcuts

When defining your `capability`, you can declare static `shortcut` elements in
`shortcuts.xml` to extend the functionality of the capability. Static shortcuts
are ingested by Assistant when you upload a release to Google Play Console.
Since static shortcuts can only be created and updated by creating new releases,
they are most useful to highlight common activities and content in your app.

> [!NOTE]
> **Note:** Assistant can also display dynamic shortcuts to your users. Dynamic shortcuts are customized for your users, and may be created and updated at runtime. For details, see [Push dynamic shortcuts to Assistant](https://developer.android.com/guide/app-actions/dynamic-shortcuts).

You can enable the following App Actions functionality with static shortcuts:

- **Capability shortcuts** . Create shortcuts that launch an instance of your
  `capability` containing predefined `intent` parameter values. For example,
  you could declare an app shortcut "Start a run" which invokes the
  [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII capability in your fitness app.

  These shortcuts contain `intent`, `shortLabel`, and `longLabel` attributes,
  making them eligible to be suggested and fulfilled as [chips](https://material.io/components/chips/android#using-chips) in proactive
  surfaces, such as Assistant or when long-pressing an app icon on Android
  launchers. An action shortcut can also serve as an entity shortcut, detailed
  below, by associating it to a `capability` using a
  [`<capability-binding>`](https://developer.android.com/develop/devices/assistant/action-schema#capability-binding) tag.
- **Entity shortcuts** . Entity shortcuts provide a list of supported parameter
  values for voice query fulfillment of a `capability`. For example, an entity
  shortcut with a list of exercise types ("hike," "run," etc.) bound to the
  `exercise.name` BII parameter of the
  [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise)
  capability. If a user utterance matches an entity, the `shortcutId` ID is
  passed to the intent instead of the raw user query value.

  `Entity` shortcuts don't define `intent`, `shortLabel`, or `longLabel`
  attributes, and as such are not suggested on proactive surfaces. For
  details, see [Inline inventory for App Actions](https://developer.android.com/develop/devices/assistant/action-schema#inline-inventory).

  > [!NOTE]
  > **Note:** Static shortcuts declared as entity shortcuts are dropped by the [`LauncherApps` API](https://developer.android.com/reference/android/content/pm/LauncherApps), meaning they are available to Android launchers.

## Capability Schema

The following table describes the App Actions schema for `capability` elements
in `shortcuts.xml`. When including a tag, all of its attributes are required
unless marked "optional".

| Shortcuts.xml tag | Contained in | Attributes |
|---|---|---|
| [`<capability>`](https://developer.android.com/develop/devices/assistant/action-schema#capability) | `<shortcuts>` | `android:name` `app:queryPatterns` (only applicable for [custom intents](https://developer.android.com/guide/app-actions/custom-intents)) |
| [`<intent>`](https://developer.android.com/develop/devices/assistant/action-schema#intent) | [`<capability>`](https://developer.android.com/develop/devices/assistant/action-schema#capability) | `android:action` (optional) `android:targetClass` (optional) `android:targetPackage` (optional) `android:data` (optional) |
| [`<url-template>`](https://developer.android.com/develop/devices/assistant/action-schema#url-template) | [`<intent>`](https://developer.android.com/develop/devices/assistant/action-schema#intent) | `android:value` |
| [`<extra>`](https://developer.android.com/develop/devices/assistant/action-schema#extra) | [`<intent>`](https://developer.android.com/develop/devices/assistant/action-schema#intent) | `android:key` `android:value` Only applicable for [foreground app invocation](https://developer.android.com/guide/app-actions/foreground-app) |
| [`<parameter>`](https://developer.android.com/develop/devices/assistant/action-schema#parameter) | [`<intent>`](https://developer.android.com/develop/devices/assistant/action-schema#intent) | `android:name` `android:key` `android:mimeType` (only applicable for [custom intents](https://developer.android.com/develop/devices/assistant/action-schema#custom-intents)) `android:required` (optional) `app:shortcutMatchRequired` (optional) |
| [`<shortcut-fulfillment>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut-fulfillment) | [`<capability>`](https://developer.android.com/develop/devices/assistant/action-schema#capability) | Only applicable for [inline inventory](https://developer.android.com/guide/app-actions/inline-inventory) |
| [`<parameter>`](https://developer.android.com/develop/devices/assistant/action-schema#parameter_for_shortcut-fulfillment) | [`<shortcut-fulfillment>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut-fulfillment) | `android:name` |
| [`<slice>`](https://developer.android.com/develop/devices/assistant/action-schema#slice) | [`<capability>`](https://developer.android.com/develop/devices/assistant/action-schema#capability) | Only applicable for [Android Slices](https://developer.android.com/develop/devices/assistant/action-schema#slice) |

### Capability schema description

This section describes the `capability` schema elements.

#### \<capability\>

A `capability` that defines the App Action intent your app supports. Each
`<capability>` element in your `shortcuts.xml` file must provide at least one
[`<intent>`](https://developer.android.com/develop/devices/assistant/action-schema#intent) to handle fulfillment of the action.

Attributes:

- `android:name`: Built-in intent Action ID (for example, \[`actions.intent.GET_FOOD_OBSERVATION`\]\[\]). For a list of supported built-in intents, see the [built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents).
- `app:queryPatterns`: A string array resource of queries expected from the user for this intent. This attribute is only applicable to [custom intents](https://developer.android.com/develop/devices/assistant/action-schema#custom-intents), as BIIs already include models of the common ways users express the tasks they're trying to do, or the information they seek.

> [!NOTE]
> **Note:** App Actions built-in *intents* are distinct from Android *intents* . BIIs model a user query for a task the user wishes to perform in your app. Android intents, by contrast, launch destinations in your app with included context. You declare `capability` tags to map a BII to a corresponding Android intent, enabling users to launch in-app functionality by invoking the BII with Assistant.

#### \<intent\>

Android [`intent`](https://developer.android.com/develop/devices/assistant/action-schema#intent) element defining how a user query should be
fulfilled using in-app functionality. Developers may provide multiple `<intent>`
tags in a `capability`. Assistant attempts to fulfill a user query using the
first `<intent>` in a `capability` for which all required parameters are
provided.

Attributes:

- `android:action`: the intent `Action` type. Defaults to [`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW).
- `android:targetClass`: Target Activity class, for example: `"com.example.exercise.ExerciseActivity"`
- `android:targetPackage`: Package containing the target Activity class, for example: `"com.example.exercise`
- `android:data`: This field is overwritten by [`<url-template>`](https://developer.android.com/develop/devices/assistant/action-schema#url-template) if that tag is declared in the `intent`.

> [!NOTE]
> **Note:** `android:targetClass` and `android:targetPackage` are required for intents that explicitly target an Activity. The `android:data` attribute may also be used to define a target Activity. For details, see [Intent fulfillment options](https://developer.android.com/develop/devices/assistant/action-schema#fulfillment-intents).

#### \<url-template\>

Template for constructing a [deep link](https://developer.android.com/develop/devices/assistant/action-schema#deep-link-fulfillment) URI to
be opened on the device. The template may be expanded with built-in intent
parameters if all required parameters for the template are available. For
examples of the HTTP URL template, see the
[Wikipedia article on URL templates](https://en.wikipedia.org/wiki/URL_Template). The
template format follows the [RFC6570 URI template specification](https://tools.ietf.org/html/rfc6570).

The following are some examples of URL template values:

| Template | Values | Expanded value |
|---|---|---|
| `https://example.com/test{?foo,bar}` | `"foo": "123"` `"bar": "456"` | `https://example.com/test?foo=123&bar=456` |
| `https://example.com/test?utm_campaign=appactions{&foo,bar}` | `"foo": "123"` `"bar": "456"` | `https://example.com/test?utm_campaign=appactions&foo=123&bar=456` |
| `https://example.com/test?utm_campaign=appactions{#foo}` | `"foo": "123"` | `https://example.com/test?utm_campaign=appactions#foo=123` |
| `myapp://example/{foo}` | `"foo": "123"` | `myapp://example/123` |

For more about configuring URL templates, see
[URL templates in fulfillment](https://developer.android.com/develop/devices/assistant/action-schema#url-templates-in-fulfillment).

> [!NOTE]
> **Note:** `<url-template>` is an optional method for targeting an Activity in an `intent`. For details, see [Intent fulfillment options](https://developer.android.com/develop/devices/assistant/action-schema#fulfillment-intents).

#### \<extra\>

Defines extra data for an `intent`. For App Actions, this field is only used to
enable \[foreground app invocation\]\[\] for a `capability`.

#### \<parameter\>

Maps a BII parameter to intent parameter values. For more information, see
[Parameter data and matching](https://developer.android.com/develop/devices/assistant/action-schema#url-templates-in-fulfillment).

Attributes:

- `android:name`: Name of the BII parameter to associate with this `intent` parameter. The name should be a leaf-level field of the BII parameter (for example, `foodObservation.aboutFood.name`).
- `android:key`: Developer-defined key of a BII parameter value. For example, you might define `contact_name` for the `message.recipient.name` BII parameter.
- `android:mimeType`: The mimeType of the parameter, such as `text/*`. This field is only required for parameters of [custom intents](https://developer.android.com/develop/devices/assistant/action-schema#custom-intents).
- `android:required`: Declares whether the user query needs to include this parameter for this intent to be used for fulfillment. If the parameter is not available, Assistant attempts to fulfill the user query using the next `intent` defined for the `capability`.

#### \<shortcut-fulfillment\>

Specifies that an `intent` defined in an [inline inventory](https://developer.android.com/guide/app-actions/inline-inventory) shortcut for a
specified [parameter](https://developer.android.com/develop/devices/assistant/action-schema#parameter_for_shortcut-fulfillment) be used for fulfillment.
For details, see [Fulfillment using shortcut intents](https://developer.android.com/guide/app-actions/inline-inventory#shortcut-fulfillment).

#### \<parameter\> (for `<shortcut-fulfillment>`)

Optional attribute that maps a single BII parameter to inline inventory
shortcut fulfillment. For details, see [Fulfillment using shortcut intents](https://developer.android.com/guide/app-actions/inline-inventory#shortcut-fulfillment).

Attribute:

- `android:name`: Name of the BII parameter to associate to inline inventory shortcut fulfillment. The name should be a leaf-level field of the BII parameter (for example, `menuItem.name`).

#### \<slice\>

Enables Assistant to embed the result of a query matching this `capability` as
an Android Slice. For details, see
[Integrate App Actions with Android Slices](https://developer.android.com/guide/app-actions/legacy/slices).

### Shortcut schema

The following table describes attributes of `shortcut` elements that are used to
enable App Actions functionality. When including a tag, all of its attributes
are required unless marked "optional".

| Shortcuts.xml tag | Contained in | Attributes |
|---|---|---|
| [`<shortcut>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut) | `<shortcuts>` | `android:shortcutId` `android:shortcutShortLabel` `android:shortcutLongLabel` (optional) `android:icon` (optional) |
| [`<intent>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut-intent) | [`<shortcut>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut) | `android:action` `android:targetClass` (optional) `android:targetPackage` (optional) `android:data` (optional) |
| [`<capability-binding>`](https://developer.android.com/develop/devices/assistant/action-schema#capability-binding) | [`` `<shortcut>` ``](https://developer.android.com/develop/devices/assistant/action-schema#shortcut) | `android:key` |
| [`<parameter-binding>`](https://developer.android.com/develop/devices/assistant/action-schema#parameter-binding) | [`<capability-binding>`](https://developer.android.com/develop/devices/assistant/action-schema#capability-binding) | `android:key` (optional) `android:value` |
| [`<extra>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut-extra) | [`<shortcut>`](https://developer.android.com/develop/devices/assistant/action-schema#shortcut) | `android:name` (optional) `android:value` Only applicable for [Enum parameter matching](https://developer.android.com/develop/devices/assistant/action-schema#enum-matching). |

### Shortcut schema description

This section describes the `shortcut` schema elements.

#### \<shortcut\>

An Android [`<shortcut>`](https://developer.android.com/guide/topics/ui/shortcuts) defined in `shortcuts.xml` with certain attributes
that are relevant for App Actions. String values for the `shortcutShortLabel`
and `shortcutLongLabel` fields are referenced via the APK's
[string resources](https://developer.android.com/guide/topics/resources/string-resource#String).

Attributes:

- `android:shortcutId`: Identifier for this shortcut.
- `android:shortcutShortLabel`: String resource representing a brief shortcut phrase. For example, `"@string/callDavidShort"` representing the value "Call David."
- `android:shortcutLongLabel`: String resource representing a long shortcut phrase. For example, `"@string/callDavidLong"` representing the value "Make an audio call to David."

#### \<intent\>

Android intent associated to this shortcut. This `intent` is executed when a
user launches this shortcut using voice or touch.

`shortcut` intent attributes are identical to `capability` [`intent`](https://developer.android.com/develop/devices/assistant/action-schema#intent)
attributes.

#### \<capability-binding\>

Associates a `shortcut` to an App Actions `capability`. Adding this element to
a `shortcut` enables it for voice fulfillment using `Assistant`.

Attributes:

- `android:key`: The `android:name` attribute of the `capability` this `shortcut` is bound to. For example, `actions.intent.START_EXERCISE`.

#### \<parameter-binding\>

Optional attribute that associates a `shortcut` to a single parameter of an App
Actions `capability`. If a `parameter-binding` is defined for a `shortcut`, the
shortcut can be used to provide an inline inventory entity to a BII parameter.
For more details, see [Inline inventory for App Actions](https://developer.android.com/develop/devices/assistant/action-schema#inline-inventory).

Attributes:

- `android:key`: The name of the `capability` BII parameter to associate this shortcut to. For example, `exercise.name`.
- `android:value`: the `entity` value. This can be a single `entity` or a resource list.

#### \<extra\>

The `extra` bundle data for the shortcut. **sameAs** is the only data
relevant to App Actions `shortcut` elements. The **sameAs** URL refers to a
reference web page that unambiguously identifies the entity. Used to specify an
enum value if and only if the intent parameter type is a subtype of
[schema.org/Enumeration](https://schema.org/Enumeration). It is required for parameter fields
whose types are subtypes of `schema.org/Enumeration` (for example:
[`MealTypeBreakfast`](https://schema.googleapis.com/MealTypeBreakfast)).

Attributes:

- `android:key`: The supported value for App Actions is: `sameAs`
- `android:value`: The `sameAs` URL value

For more details, see [Matching enumerated parameter values](https://developer.android.com/develop/devices/assistant/action-schema#enum-matching).

## Intent fulfillment options

You define `intent` elements within a `<capability>` to declare how Assistant
responds to, or fulfills, user voice commands that match that capability. There
are several ways to configure how an `intent` launches a fulfillment destination
in your app, depending on how your app navigation is structured.

The following fulfillment options are available:

- **Explicit intents** : Launch a specific app component by defining the
  `targetClass` and `targetPackage` attributes for the [`intent`](https://developer.android.com/develop/devices/assistant/action-schema#intent).
  This is the recommended App Actions fulfillment method.

- **Deep links** : Launch app destinations using Android deep links by defining
  a [`<url-template>`](https://developer.android.com/develop/devices/assistant/action-schema#url-template) tag within the `intent` element. This
  method is useful if your app navigation already relies on deep links.

- **Intent data** : You can provide a fulfillment URI in the [`intent`](https://developer.android.com/develop/devices/assistant/action-schema#intent)
  `android:data` attribute. This field is overwritten by `<url-template>` data
  if that tag is also defined within the `intent`.

> [!NOTE]
> **Note:** These fulfillment options are mutually exclusive. For example, if you define an explicit [`intent`](https://developer.android.com/develop/devices/assistant/action-schema#intent) by using the `targetClass` and `targetPackage` attributes, you don't need to also define a [`<url-template>`](https://developer.android.com/develop/devices/assistant/action-schema#url-template).

## Parameter data and matching

By default, Assistant sends BII parameters extracted from the user query to your
app as `extra` data of the Android `intent` defined in the `capability`.

Alternately, you can declare a [`<url-template>`](https://developer.android.com/develop/devices/assistant/action-schema#url-template) tag in the
`capability` that contains placeholders for dynamic parameters. This template
maps to one of your Android activities, using an [App Links URL](https://developer.android.com/training/app-links),
a custom scheme, or an [Intent-based URL](https://developer.chrome.com/multidevice/android/intents).

### Using intent Extras

The following example demonstrates an explicit intent defined for a `capability`
fulfillment:

    <capability android:name="actions.intent.START_EXERCISE">
      <intent
        android:targetPackage="com.example.myapp"
        android:targetClass="com.example.myapp.ExerciseActivity">
        <parameter android:name="exercise.name" android:key="exercise" />
      </intent>
    </capability>

Given the above sample, for a user query like, *"Hey Google, start my run,"*
the app receives an `intent` that invokes the component:
`targetPackage`, `targetClass`. The component receives an Extra with
`key = "exercise"`, `value = "Running"`.

### Using a URL template for Android deep links

If your app is already able to handle app-linked URLs, with dynamic parameters,
you can define a `<url-template>` in the `intent` to generate Android
[deep links](https://developer.android.com/training/app-links/deep-linking) for fulfillment. The following sample defines a `<url-template>`:

    <capability android:name="actions.intent.START_EXERCISE">
      <intent>
        <url-template android:value="myapp://start{?exercise}" />
        <parameter android:name="exercise.name" android:key="exercise" />
      </intent>
    </capability>

Given the above sample, for a user query like, *"Hey Google, start my run,"* the
app receives the generated URL: "myapp://start?exercise=Running".

> [!NOTE]
> **Note:** If the generated URL for an `intent` using a `<url-template>` for fulfillment is app-linked, and there are relevant intent-filters added in the `AndroidManifest.xml` resource file, the `targetClass` and `targetActivity` attributes don't need to be defined in the `intent`.

To map the BII parameter to a position in your URL, you use the
`android:name` attribute of the `<parameter>` tag. This attribute
corresponds to the `android:key` value in the URL template that you want to
substitute with information from the user. The `android:key` value must be present
in your `<url-template>` and enclosed by curly braces (`{}`).

### Match enumerated parameter values

Some BII parameters provide enumerated values to your fulfillment intent, for
example, the [supported text values](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/record-food-observation#supported-text-id-values) of the [`RECORD_FOOD_OBSERVATION`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/record-food-observation) BII. For
these parameters, Assistant matches the user's query ("Breakfast") to an
entity whose `sameAs` value matches the enum schema URL
([`https://schema.googleapis.com/MealTypeBreakfast`](https://schema.googleapis.com/MealTypeBreakfast)). To associate enum
values for a supported `entity`, you declare a `sameAs` association in
your `shortcut`. The following sample demonstrates a `sameAs` association for an
inline entity shortcut:

    <shortcut android:shortcutId="meal_breakfast" >
        <capability-binding android:key="actions.intent.RECORD_FOOD_OBSERVATION">
            <parameter-binding android:key="foodObservation.forMeal" />
        </capability-binding>
        <extra
            android:key="sameAs"
            android:value="http://schema.googleapis.com/MealTypeBreakfast" />
    </shortcut>

    <capability android:name="actions.intent.RECORD_FOOD_OBSERVATION">
      <intent targetPackage="com.example.app" targetClass="com.example.app.Class">
        <parameter android:name="foodObservation.forMeal" android:key="for_meal" />
      </intent>
    </capability>

In the above example, if the `RECORD_FOOD_OBSERVATION` capability triggers a
match for the "breakfast" meal type, the following Extra is sent with the
fulfillment `intent`:

- `key = "for_meal"`
- `value = "meal_breakfast"`

## Features

The following App Actions features are available in `shortcuts.xml`.

### Inline inventory for App Actions

For some BII parameters, shortcuts can be used to guide entity
extraction to a set of supported entities specified in `shortcuts.xml`, known as
inline inventory. For details, see [Inline inventory](https://developer.android.com/guide/app-actions/inline-inventory).

### Custom intents

Custom intents can be declared in `shortcuts.xml` to voice enable features in
your app that don't match available BIIs. While similar in
functionality to a BII definition, custom intents require two additional
attributes in `shortcuts.xml`:

- [`app:queryPatterns`](https://developer.android.com/guide/app-actions/custom-intents#query-patterns): Array resource that declares the
  different query patterns for a custom intent.

- `android:mimeType`: Parameter type of a custom intent. This field is
  not required for BIIs, where the parameter type is known. For custom intent
  parameters, a [supported semantic type](https://developer.android.com/guide/app-actions/custom-intents#supported-types) must be declared.

For more details, see [Custom intents](https://developer.android.com/guide/app-actions/custom-intents).