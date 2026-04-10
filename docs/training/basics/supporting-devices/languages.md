---
title: https://developer.android.com/training/basics/supporting-devices/languages
url: https://developer.android.com/training/basics/supporting-devices/languages
source: md.txt
---

Apps include resources that can be specific to a particular culture.
For example, an app can include culture-specific strings that are translated to
the language of the current locale.

It's a good practice to keep
culture-specific resources separated from the rest of your app. Android resolves
language- and culture-specific resources based on the system locale setting. You
can provide support for different locales by using the resources directory in
your Android project.

You can specify resources tailored to the cultures of the people using your
app. You can provide any [resource type](https://developer.android.com/guide/topics/resources/available-resources) that is
appropriate for the language and culture of your users. For example, the
following screenshots show an app displaying string and drawable resources in
the device's default `en_US` locale and the Spanish
`es_ES` locale.
![The app shows a
different text and icon depending on the current locale](https://developer.android.com/static/images/training/languages_01.png)


**Figure 1.** App using different resources depending on the
current locale.

When you create a project using the Android SDK
Tools, the tools generate a `res/` directory in the top level of
the project. Within this `res/` directory are subdirectories for various resource
types. There are also a few default files, such as the `res/values/strings.xml`
file, which holds your string values.

Supporting different languages goes beyond using locale-specific resources.
Some users choose a language that uses right-to-left (RTL) scripts, such as
Arabic or Hebrew, for their UI locale. Other users who set their UI locale to a language that uses
LTR scripts, such as English, might view or generate content
in a language that uses RTL scripts. To support both types of users,
your app needs to do the following:

- Employ an RTL UI layout for RTL locales.
- Detect and declare the direction of text data that's displayed inside formatted messages. Usually, you can [call a method](https://developer.android.com/training/basics/supporting-devices/languages#FormatTextExplanationSolution), as described in this guide, that determines the direction of text data for you.

## Create locale directories and resource files

To add support for more locales, create additional directories inside
`res/`. Each directory's name must adhere to the following format:

```
<resource type>-b+<language code>[+<country code>]
```

For example, `values-b+es/` contains string
resources for locales with the language code `es`. Similarly,
`mipmap-b+es+ES/` contains icons for locales with the `es`
language code and the `ES` country code.


Android loads the appropriate resources according to the locale settings of the
device at runtime. For more information, see
[Provide alternative resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources).

After you decide which locales to support, create the resource subdirectories and
files. For example:

```
MyProject/
    res/
       values/
           strings.xml
       values-b+es/
           strings.xml
       mipmap/
           country_flag.png
       mipmap-b+es+ES/
           country_flag.png
```

Populate the resource files with localized resources.
The following are examples of localized string and image resource files:

English strings (default locale) in `/values/strings.xml`:

```xml
<resources>
    <string name="hello_world">Hello World!</string>
</resources>
```

Spanish strings (`es` locale) in `/values-b+es/strings.xml`:

```xml
<resources>
    <string name="hello_world">¡Hola Mundo!</string>
</resources>
```

US flag icon (default locale) in
`/mipmap/country_flag.png`:
![The icon of flag of the
United States](https://developer.android.com/static/images/training/languages_us_flag.png)


**Figure 2.** Icon used for the default (en_US) locale.

Spanish flag icon (`es_ES` locale) in
`/mipmap-b+es+ES/country_flag.png`:
![The icon of flag of
Spain](https://developer.android.com/static/images/training/languages_es_flag.png)


**Figure 3.** Icon used for the `es_ES` locale.

**Note:** You can use configuration qualifiers,
such as the locale qualifier, on any resource type. For example, you might want to
provide localized versions of your bitmap drawables. For more information, see [Localize your app](https://developer.android.com/guide/topics/resources/localization).

## Use the resources in your app

Reference the resources in your source code and other XML files by using
each resource's `name` attribute:
`R.<resource type>.<resource name>`. There are a variety
of methods that accept a resource this way, as shown in the following examples:

### Kotlin

```kotlin
// Get a string resource
val hello = resources.getString(R.string.hello_world)

// Or supply a string resource to a method that requires a string
TextView(this).apply {
    setText(R.string.hello_world)
}
```

### Java

```java
// Get a string resource
String hello = getResources().getString(R.string.hello_world);

// Or supply a string resource to a method that requires a string
TextView textView = new TextView(this);
textView.setText(R.string.hello_world);
```

In XML files, you can refer to a resource with the syntax
`@<resource type>/<resource name>` whenever the XML
attribute accepts a compatible value, as shown in the following example:

```xml
<ImageView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:src="@mipmap/country_flag" />
```

**Note** : To ensure user language settings are prioritized
correctly, specify the languages your app supports using the `resConfigs` property. For
more information, see
[Specify the languages your app supports](https://developer.android.com/guide/topics/resources/multilingual-support#specify-the-languages-your-app-supports).

## Format text in messages

One of the most common tasks in an app is formatting text. Localized messages
are formatted by inserting text and numeric data into the appropriate positions.
Unfortunately, when dealing with an RTL UI or RTL data, simple formatting can
display incorrect or even unreadable text output.

Languages such as Arabic, Hebrew, Persian, and Urdu are written RTL.
However, some elements, such as numbers and embedded
LTR text, are written LTR within the otherwise RTL text.
Languages that use LTR scripts, including English, are also bidirectional,
because they can contain embedded RTL scripts that need to be displayed RTL.

Apps often generate instances of this kind of embedded opposite-direction text,
such as by inserting text data of an arbitrary
language and an arbitrary text direction into localized messages.
This mixing of directions often doesn't include a clear indication of where
opposite-direction text starts and ends, so app-generated
text can cause poor user experience.

Although the system's default handling of bidirectional text usually renders
text as expected, text might not render properly when your app
inserts it into a localized message. The following are examples of situations
where text is likely to appear incorrectly:

- Text inserted at the start of a message:

  <var translate="no">PERSON_NAME</var> *is calling you*
- Text that starts with a number, such as an address or telephone number:

  *987 654-3210*
- Text that starts with punctuation, such as a phone number:

  *+19876543210*
- Text that ends with punctuation:

  *Are you sure?*
- Text that contains both directions already:

  *The word בננה is Hebrew for banana.*

### Example

Suppose an app sometimes needs to display the message "Did
you mean %s?", with an address inserted in place of the %s at runtime. The app supports different UI locales, so the message comes from a locale-specific
resource and uses the RTL direction when the device is set to an RTL locale. For example, for a Hebrew
UI, the message appears as follows:

*האם התכוונת ל %s?*

However, the suggested address might come from a database that doesn't include text
in the locale's language. For example, if the address is for a place
in California, it appears in the database using English text. If you insert the
address "15 Bay Street, Laurel, CA" into the RTL message without providing any
hints regarding text direction, the result isn't expected or correct:

*האם התכוונת ל 15 Bay Street, Laurel, CA?*

The house number appears to the right of the address, not to the
left as intended. This makes the house number look more like a strange postal
code. The same problem can occur if you include RTL text within a message that
uses the LTR text direction.

#### Explanation and solution

The problem in this example occurs because the text formatter doesn't
specify that "15" is part of the address, so the system can't determine whether
the "15" is part of the RTL text that comes before it or the LTR text that comes
after it.

To solve this problem, use the `https://developer.android.com/reference/android/text/BidiFormatter#unicodeWrap(java.lang.CharSequence)` method from the `https://developer.android.com/reference/android/text/BidiFormatter`
class. This method detects the direction of a string and wraps it in Unicode
formatting characters that declare that direction.

The following code snippet demonstrates how to use
`unicodeWrap()`:

### Kotlin

```kotlin
val mySuggestion = "15 Bay Street, Laurel, CA"
val myBidiFormatter: BidiFormatter = BidiFormatter.getInstance()

// The "did_you_mean" localized string resource includes
// a "%s" placeholder for the suggestion.
String.format(getString(R.string.did_you_mean), myBidiFormatter.unicodeWrap(mySuggestion))
```

### Java

```java
String mySuggestion = "15 Bay Street, Laurel, CA";
BidiFormatter myBidiFormatter = BidiFormatter.getInstance();

// The "did_you_mean" localized string resource includes
// a "%s" placeholder for the suggestion.
String.format(getString(R.string.did_you_mean),
        myBidiFormatter.unicodeWrap(mySuggestion));
```

Because the "15" now appears inside text that is
declared as LTR, it's displayed in the correct position:

*האם התכוונת ל 15 Bay Street, Laurel, CA?*

Use the `unicodeWrap()` method on
every piece of text that you insert into a localized message except when one of the following applies:

- The text is being inserted into a machine-readable string, such as a URI or a SQL query.
- You know the piece of text is already properly wrapped.

**Note:** If your app targets Android 4.3 (API level 18) or
higher, use the version of `https://developer.android.com/reference/android/text/BidiFormatter` found in the
Android Framework. Otherwise, use the version of
`https://developer.android.com/reference/androidx/core/text/BidiFormatter` found in the Support Library.

## Format numbers

Use
[format
strings](https://developer.android.com/guide/topics/resources/string-resource#FormattingAndStyling), not method calls, to convert numbers to strings in your app's
logic:

### Kotlin

```kotlin
var myIntAsString = "$myInt"
```

### Java

```java
String myIntAsString = String.format("%d", myInt);
```

This formats the numbers appropriately for your locale, which might
include using a different set of digits.

When you use
`https://developer.android.com/reference/java/lang/String#format(java.lang.String, java.lang.Object...)` to create a
SQL query on a device set to a locale that uses its own set of digits, such as Persian
and most Arabic locales, problems occur if any of the parameters to the query
are numbers. This is because the number is formatted in the locale's digits, and
these digits are invalid in SQL.

To preserve ASCII-formatted numbers and keep the SQL query valid, you instead need to use
the overloaded version of
`https://developer.android.com/reference/java/lang/String#format(java.util.Locale, java.lang.String, java.lang.Object...)` that
includes a locale as the first parameter. Use the locale argument
`Locale.US`.

## Support layout mirroring

People who use RTL scripts prefer an RTL user interface, which includes
right-aligned menus, right-aligned text, and forward arrows pointing to the
left.

Figure 4 shows the contrast between the LTR version of a screen within the
Settings app and its RTL counterpart:
![The notification area is right-aligned near the top-right corner,
the menu button in the app bar is near the top-left corner, the
content in the main part of the screen is left-aligned and appears
LTR, and the back button is near the bottom-left corner and is
pointing to the left.](https://developer.android.com/static/images/training/basics/ltr-display.png) ![The notification area is left-aligned near the top-left corner, the
menu button in the app bar is near the top-right corner, the content
in the main part of the screen is right-aligned and appears RTL, and
the back button is near the bottom-right corner and is pointing to
the right](https://developer.android.com/static/images/training/basics/rtl-display.png) **Figure 4.** LTR and RTL variants of a settings screen.

When adding RTL support to your app, keep the
following points in mind:

- RTL text mirroring is only supported in apps when used on devices running Android 4.2 (API level 17) or higher. To learn how to support text mirroring on older devices, see [Provide support
  for legacy apps](https://developer.android.com/training/basics/supporting-devices/languages#MirroringSupportLegacyApps) in this guide.
- To test whether your app supports an RTL text direction, [test using developer options](https://developer.android.com/training/basics/supporting-devices/languages#MirroringDevOptions) as described in this guide and invite people who use RTL scripts to use your app.

**Note:** To view additional design guidelines related to
layout mirroring, including a list of elements that are and are not appropriate
to mirror, see the
[Bidirectionality](https://m2.material.io/design/usability/bidirectionality.html)
material design guidelines.

To mirror the UI layout in your app so it appears RTL in an RTL locale,
complete the steps in the following sections.

### Modify the build and manifest files

Modify your app module's `build.gradle` file and app manifest file
as follows:

`build.gradle (Module: app)`

### Groovy

```groovy
android {
    ...
    defaultConfig {
        targetSdkVersion 17 // Or higher
        ...
    }
}
```

### Kotlin

```kotlin
android {
    ...
    defaultConfig {
        targetSdkVersion(17) // Or higher
        ...
    }
}
```

`AndroidManifest.xml`

```xml
<manifest ... >
    ...
    <application ...
        android:supportsRtl="true">
    </application>
</manifest>
```

**Note:** If your app targets Android 4.1.1 (API level 16) or
lower, the `android:supportsRtl` attribute is ignored, along with any
`start` and `end` attribute values that appear in your
app's layout files. In this case, RTL layout mirroring doesn't happen
automatically in your app.

### Update existing resources

Convert `left` and `right` to `start` and
`end`, respectively, in your existing layout resource files.
This lets the framework align your app's UI elements based on
the user's language settings.

**Note:** Before updating your resources, learn how to
[provide support for legacy apps](https://developer.android.com/training/basics/supporting-devices/languages#MirroringSupportLegacyApps), or
apps that target Android 4.1.1 (API level 16) and lower.

To use the framework's RTL alignment capabilities, change the attributes in
your layout files that appear in Table 1.

**Table 1.**Attributes to
use when your app supports multiple text directions

| Attribute supporting LTR only | Attribute supporting LTR and RTL |
|---|---|
| [`android:gravity="left"`](https://developer.android.com/reference/android/R.attr#gravity) | [`android:gravity="start"`](https://developer.android.com/reference/android/R.attr#gravity) |
| [`android:gravity="right"`](https://developer.android.com/reference/android/R.attr#gravity) | [`android:gravity="end"`](https://developer.android.com/reference/android/R.attr#gravity) |
| [`android:layout_gravity="left"`](https://developer.android.com/reference/android/R.attr#layout_gravity) | [`android:layout_gravity="start"`](https://developer.android.com/reference/android/R.attr#layout_gravity) |
| [`android:layout_gravity="right"`](https://developer.android.com/reference/android/R.attr#layout_gravity) | [`android:layout_gravity="end"`](https://developer.android.com/reference/android/R.attr#layout_gravity) |
| [`android:paddingLeft`](https://developer.android.com/reference/android/R.attr#paddingLeft) | [`android:paddingStart`](https://developer.android.com/reference/android/R.attr#paddingStart) |
| [`android:paddingRight`](https://developer.android.com/reference/android/R.attr#paddingRight) | [`android:paddingEnd`](https://developer.android.com/reference/android/R.attr#paddingEnd) |
| [`android:drawableLeft`](https://developer.android.com/reference/android/R.attr#drawableLeft) | [`android:drawableStart`](https://developer.android.com/reference/android/R.attr#drawableStart) |
| [`android:drawableRight`](https://developer.android.com/reference/android/R.attr#drawableRight) | [`android:drawableEnd`](https://developer.android.com/reference/android/R.attr#drawableEnd) |
| [`android:layout_alignLeft`](https://developer.android.com/reference/android/R.attr#layout_alignLeft) | [`android:layout_alignStart`](https://developer.android.com/reference/android/R.attr#layout_alignStart) |
| [`android:layout_alignRight`](https://developer.android.com/reference/android/R.attr#layout_alignRight) | [`android:layout_alignEnd`](https://developer.android.com/reference/android/R.attr#layout_alignEnd) |
| [`android:layout_marginLeft`](https://developer.android.com/reference/android/R.attr#layout_marginLeft) | [`android:layout_marginStart`](https://developer.android.com/reference/android/R.attr#layout_marginStart) |
| [`android:layout_marginRight`](https://developer.android.com/reference/android/R.attr#layout_marginRight) | [`android:layout_marginEnd`](https://developer.android.com/reference/android/R.attr#layout_marginEnd) |
| [`android:layout_alignParentLeft`](https://developer.android.com/reference/android/R.attr#layout_alignParentLeft) | [`android:layout_alignParentStart`](https://developer.android.com/reference/android/R.attr#layout_alignParentStart) |
| [`android:layout_alignParentRight`](https://developer.android.com/reference/android/R.attr#layout_alignParentRight) | [`android:layout_alignParentEnd`](https://developer.android.com/reference/android/R.attr#layout_alignParentEnd) |
| [`android:layout_toLeftOf`](https://developer.android.com/reference/android/R.attr#layout_toLeftOf) | [`android:layout_toStartOf`](https://developer.android.com/reference/android/R.attr#layout_toStartOf) |
| [`android:layout_toRightOf`](https://developer.android.com/reference/android/R.attr#layout_toRightOf) | [`android:layout_toEndOf`](https://developer.android.com/reference/android/R.attr#layout_toEndOf) |

Table 2 shows how the system handles UI alignment attributes based on the
target SDK version, whether `left` and `right` attributes
are defined, and whether `start` and `end` attributes are
defined.

**Table 2.**UI element alignment behavior based
on the target SDK version and defined attributes

| Targeting Android 4.2 (API level 17) or higher? | Left and right defined? | Start and end defined? | Result |
|---|---|---|---|
| Yes | Yes | Yes | `start` and `end` are used, overriding `left` and `right` |
| Yes | Yes | No | `left` and `right` are used |
| Yes | No | Yes | `start` and `end` are used |
| No | Yes | Yes | `left` and `right` are used (`start` and `end` are ignored) |
| No | Yes | No | `left` and `right` are used |
| No | No | Yes | `start` and `end` resolve to `left` and `right` |

### Add direction- and language-specific resources

This step involves adding specific versions of your layout, drawables, and
values resource files that contain customized values for different languages
and text directions.

In Android 4.2 (API level 17) and higher, you can use the `-ldrtl`
(layout-direction-right-to-left) and `-ldltr`
(layout-direction-left-to-right) resource qualifiers. To maintain backward
compatibility with existing resources, older versions of Android use a
resource's language qualifiers to infer the correct text direction.

Suppose you want to add a specific layout file to support RTL scripts,
such as the Hebrew, Arabic, and Persian languages. To do this, add a
`layout-ldrtl/` directory in your `res/` directory, as
shown in the following example:

```
res/
    layout/
        main.xml This layout file is loaded by default.
    layout-ldrtl/
        main.xml This layout file is loaded for languages using an
                 RTL text direction, including Arabic, Persian, and Hebrew.
```

If you want to add a specific version of the layout that is designed for only
Arabic text, your directory structure looks like the following:

```
res/
    layout/
        main.xml This layout file is loaded by default.
    layout-ar/
        main.xml This layout file is loaded for Arabic text.
    layout-ldrtl/
        main.xml This layout file is loaded only for non-Arabic
                 languages that use an RTL text direction.
```

**Note:**Language-specific resources take precedence over
layout-direction-specific resources, which take precedence over the default
resources.

### Use supported widgets

As of Android 4.2 (API level 17), most framework UI elements support the RTL
text direction automatically. However, several framework elements, such as
`https://developer.android.com/reference/androidx/viewpager/widget/ViewPager`, don't support the RTL text
direction.

Home-screen widgets support the RTL text direction as long as their
corresponding manifest files include the attribute assignment
`android:supportsRtl="true"`.

### Provide support for legacy apps

If your app targets Android 4.1.1 (API level 16) or lower, include
`left` and `right` attributes in addition to
`start` and `end`.

To check whether your layout needs to use the RTL text direction, use the
following logic:

### Kotlin

```kotlin
private fun shouldUseLayoutRtl(): Boolean {
    return if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.JELLY_BEAN_MR1) {
        View.LAYOUT_DIRECTION_RTL == layoutDirection
    } else {
        false
    }
}
```

### Java

```java
private boolean shouldUseLayoutRtl() {
    if (android.os.Build.VERSION.SDK_INT >=
            android.os.Build.VERSION_CODES.JELLY_BEAN_MR1) {
        return View.LAYOUT_DIRECTION_RTL == getLayoutDirection();
    } else {
        return false;
    }
}
```

**Note:** To avoid compatibility issues, use version 23.0.1
or higher of the
[Android
SDK Build Tools](https://developer.android.com/studio/releases/build-tools.html).

### Test using developer options

On devices running Android 4.4 (API level 19) or higher, you can enable
**Force RTL layout direction** in the
[on-device developer options](https://developer.android.com/studio/debug/dev-options#drawing). This setting
lets you see text that uses LTR scripts, such as English text, in RTL
mode.

### Update app logic

This section describes specific aspects of your app's logic to
update when adapting your app for handling multiple text directions.

#### Property changes

To handle a change in any RTL-related property---such as layout
direction, layout parameters, padding, text direction, text alignment, or
drawable positioning---use the
`https://developer.android.com/reference/android/view/View#onRtlPropertiesChanged(int)`
callback. This callback lets you get the current layout direction and
update an activity's `https://developer.android.com/reference/android/view/View` objects accordingly.

#### Views

If you are creating a UI widget that is not directly part of an activity's
view hierarchy, such as a dialog or a toast-like UI element, set the correct
layout direction depending on the context. The following code snippet
demonstrates how to complete this process:

### Kotlin

```kotlin
val config: Configuration = context.resources.configuration
view.layoutDirection = config.layoutDirection
```

### Java

```java
final Configuration config =
    getContext().getResources().getConfiguration();
view.setLayoutDirection(config.getLayoutDirection());
```

Several methods of the `https://developer.android.com/reference/android/view/View` class require additional
consideration:

`https://developer.android.com/reference/android/view/View#onMeasure(int, int)`
:   View measurements might vary depending on text direction.

`https://developer.android.com/reference/android/view/View#onLayout(boolean, int, int, int, int)`
:   If you create your own layout implementation, then you need to call
    `super()` in your version of `onLayout()` and adapt
    your custom logic to support RTL scripts.

`https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas)`
:   If you're implementing a custom view or adding advanced functionality to a
    drawing, you need to update your code to support RTL scripts. Use the
    following code to determine if your widget is in RTL mode:

    ### Kotlin

    ```kotlin
    // On devices running Android 4.1.1 (API level 16) and lower,
    // you can call the isLayoutRtl() system method directly.
    fun isLayoutRtl(): Boolean = layoutDirection == LAYOUT_DIRECTION_RTL
    ```

    ### Java

    ```java
    // On devices running Android 4.1.1 (API level 16) and lower,
    // you can call the isLayoutRtl() system method directly.
    public boolean isLayoutRtl() {
        return (getLayoutDirection() == LAYOUT_DIRECTION_RTL);
    }
    ```

#### Drawables

If you have a drawable that needs to be mirrored for an RTL layout, complete
one of these steps based on the version of Android running on the device:

- On devices running Android 4.3 (API level 18) and lower, add and define the `-ldrtl` resource files.
-
  On Android 4.4 (API level 19) and higher, use
  `android:autoMirrored="true"` when defining your drawable,
  which lets the system handle RTL layout mirroring for you.

  **Note:** The `android:autoMirrored`
  attribute only works for simple drawables whose bidirectional mirroring
  is simply a graphical mirroring of the entire drawable. If your drawable
  contains multiple elements, or if reflecting your drawable changes its
  interpretation, you can perform the mirroring yourself. Whenever
  possible, check with a bidirectional expert to determine whether your
  mirrored drawables make sense to users.

#### Gravity

If your app's layout code uses `https://developer.android.com/reference/android/view/Gravity#LEFT` or
`https://developer.android.com/reference/android/view/Gravity#RIGHT`, change these
values to `https://developer.android.com/reference/android/view/Gravity#START` and
`https://developer.android.com/reference/android/view/Gravity#END`, respectively.

If you have Kotlin or Java code that depends on the
`Gravity.LEFT` or `Gravity.RIGHT` properties,
you can adapt it to work with this change by setting the `absoluteGravity` to match the
`layoutDirection`.

For example, if you're using the following code:

### Kotlin

```kotlin
when (gravity and Gravity.HORIZONTAL_GRAVITY_MASK) {
    Gravity.LEFT -> {
        // Handle objects that are left-aligned.
    }
    Gravity.RIGHT -> {
        // Handle objects that are right-aligned.
    }
}
```

### Java

```java
switch (gravity & Gravity.HORIZONTAL_GRAVITY_MASK) {
    case Gravity.LEFT:
        // Handle objects that are left-aligned.
        break;
    case Gravity.RIGHT:
        // Handle objects that are right-aligned.
        break;
}
```

Change it to the following:

### Kotlin

```kotlin
val absoluteGravity: Int = Gravity.getAbsoluteGravity(gravity, layoutDirection)
when (absoluteGravity and Gravity.HORIZONTAL_GRAVITY_MASK) {
    Gravity.LEFT -> {
        // Handle objects that are left-aligned.
    }
    Gravity.RIGHT -> {
        // Handle objects that are right-aligned.
    }
}
```

### Java

```java
final int layoutDirection = getLayoutDirection();
final int absoluteGravity =
        Gravity.getAbsoluteGravity(gravity, layoutDirection);
switch (absoluteGravity & Gravity.HORIZONTAL_GRAVITY_MASK) {
    case Gravity.LEFT:
        // Handle objects that are left-aligned.
        break;
    case Gravity.RIGHT:
        // Handle objects that are right-aligned.
        break;
}
```

This means you can keep your existing code that handles left-aligned and
right-aligned values, even if you are using `start` and
`end` for your gravity values.

**Note:** When applying your gravity settings, use an
overloaded version of `Gravity.apply()` that includes a
`layoutDirection` argument.

#### Margins and padding

To support RTL scripts in your app, follow these best practices related to
margin and padding values:

- Use `https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams#getMarginStart()` and `https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams#getMarginEnd()` instead of the direction-specific attribute equivalents `leftMargin` and `rightMargin`.
- When using `https://developer.android.com/reference/android/view/ViewGroup.MarginLayoutParams#setMargins(int, int, int, int)`, swap the values of the `left` and `right` arguments if your app detects RTL scripts.
- If your app includes custom padding logic, override `https://developer.android.com/reference/android/view/View#setPadding(int, int, int, int)` and `https://developer.android.com/reference/android/view/View#setPaddingRelative(int, int, int, int)`.

## Support per-app language preferences

In many cases, multilingual users set their system language to one language---such as English---but
they want to select other languages for specific apps, such as Dutch, Chinese, or Hindi. To help
apps provide a better experience for these users, Android 13 introduces the following features for
apps that support multiple languages:

- **System settings**: a centralized location where users can select a
  preferred language for each app.

  Your app must declare the `android:localeConfig` attribute in its
  manifest to tell the system that it supports multiple languages. To learn more, see the
  instructions for
  [creating a resource
  file and declaring it in your app's manifest file](https://developer.android.com/guide/topics/resources/app-languages#app-language-settings).
- **Additional APIs** : these public APIs, such as the
  [`setApplicationLocales()`](https://developer.android.com/reference/android/app/LocaleManager#setApplicationLocales\(android.os.LocaleList\))
  and
  [`getApplicationLocales()`](https://developer.android.com/reference/android/app/LocaleManager#getApplicationLocales\(\))
  methods in
  [`LocaleManager`](https://developer.android.com/reference/android/app/LocaleManager),
  let apps set a different language from the system language at
  runtime.

  Apps that use custom in-app language pickers can use these APIs to give users
  a consistent user experience regardless of where they select their language
  preferences. The public APIs also help you reduce the amount of boilerplate code, and
  they support split APKs. They also support [Auto Backup
  for Apps](https://developer.android.com/guide/topics/data/autobackup) to store app-level user language settings.

  For backward compatibility with previous Android versions, equivalent APIs are also available
  in AndroidX. We recommend using
  [Appcompat 1.6.0-beta01](https://developer.android.com/jetpack/androidx/releases/appcompat#1.6.0-beta01) or
  higher.

  To learn more, see the instructions for
  [implementing the new
  APIs](https://developer.android.com/guide/topics/resources/app-languages#api-implementation).

## See also

- [Localize your app](https://developer.android.com/guide/topics/resources/localization)
- [App translation service](https://support.google.com/l10n/answer/6359997)

## Additional resources

To learn more about supporting older devices, view the following resources:

### Blog posts

- [To
  Make Apps Accessible, Make Them Compatible with Different Devices](https://medium.com/google-design/to-make-apps-accessible-make-them-compatible-with-different-devices-11298c6d3f06)
- [Writing for
  global audiences](https://medium.com/google-design/writing-for-global-audiences-d339d23e9612)