---
title: https://developer.android.com/guide/topics/resources/providing-resources
url: https://developer.android.com/guide/topics/resources/providing-resources
source: md.txt
---

Resources are the additional files and static content that your code uses, such as bitmaps,
user interface strings, animation instructions, and more.

Always externalize app resources such as images and strings from your
code, so that you can maintain them independently. Also, provide alternative resources for
specific device configurations by grouping them in specially named resource directories. At
runtime, Android uses the appropriate resource based on the current configuration. For
example, you might want to provide different strings depending on the language setting.

Once you externalize your app resources, you can access them
using resource IDs that are generated in your project's `R` class.
This document shows you how to group the resources in your Android project. It also shows you how
to provide alternative resources for specific device configurations and then access them from
your app code or other XML files.

## Group resource types

Place each type of resource in a specific subdirectory of your project's
`res/` directory. For example, here's the file hierarchy for a simple project:

```
MyProject/
    src/
        MyActivity.kt
    res/
        drawable/
            graphic.png
        mipmap/
            icon.png
        values/
            strings.xml
```

The `res/` directory contains all the resources in its
subdirectories: an image resource, a `mipmap/` directory for launcher
icons, and a string resource file. The resource
directory names are important and are described in Table 1.

**Note:** For more information about using the mipmap folders, see
[Put app icons in mipmap directories](https://developer.android.com/training/multiscreen/screendensities#mipmap).

**Table 1.** Resource directories
supported inside project `res/` directory.

| Directory | Resource Type |
|---|---|
| `drawable/` | Bitmap files (PNG, `.9.png`, JPG, or GIF) or XML files that are compiled into the following drawable resource subtypes: - Bitmap files - Nine-patches (re-sizable bitmaps) - State lists - Shapes - Animation drawables - Other drawables For more information, see [Drawable resources](https://developer.android.com/guide/topics/resources/drawable-resource). |
| `mipmap/` | Drawable files for different launcher icon densities. For more information on managing launcher icons with `mipmap/` folders, see [Put app icons in mipmap directories](https://developer.android.com/training/multiscreen/screendensities#mipmap). |
| `raw/` | Arbitrary files to save in their raw form. To open these resources with a raw `https://developer.android.com/reference/java/io/InputStream`, call `https://developer.android.com/reference/kotlin/android/content/res/Resources#openrawresource` with the resource ID, which is `R.raw.filename`. However, if you need access to the original filenames and file hierarchy, consider saving resources in the `assets/` directory instead of `res/raw/`. Files in `assets/` aren't given a resource ID, so you can only read them using `https://developer.android.com/reference/kotlin/android/content/res/AssetManager`. |
| `values/` | XML files that contain simple values, such as strings, integers, and colors. Whereas XML resource files in other `res/` subdirectories define a single resource based on the XML filename, files in the `values/` directory describe multiple resources. For a file in this directory, each child of the `<resources>` element defines a single resource. For example, a `<string>` element creates an `R.string` resource, and a `<color>` element creates an `R.color` resource. Because each resource is defined with its own XML element, you can name the file whatever you want and place different resource types in one file. However, for clarity, you might want to place unique resource types in different files. For example, here are some filename conventions for resources you can create in this directory: - `arrays.xml` for resource arrays ([Typed arrays](https://developer.android.com/guide/topics/resources/more-resources#TypedArray)) - `strings.xml` for [String values](https://developer.android.com/guide/topics/resources/string-resource) For more information, see [String resources](https://developer.android.com/guide/topics/resources/string-resource), [Style resource](https://developer.android.com/guide/topics/resources/style-resource), and [More resource types](https://developer.android.com/guide/topics/resources/more-resources). |
| `xml/` | Arbitrary XML files that can be read at runtime by calling `https://developer.android.com/reference/kotlin/android/content/res/Resources#getxml`. Various XML configuration files must be saved here. |
| `font/` | Font files with extensions such as TTF, OTF, or TTC, or XML files that include a `<font-family>` element. For more information about fonts as resources, see [Add a font as an XML resource](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml). |

**Caution:** Never save resource files directly inside the
`res/` directory. It causes a compiler error.

The resources that you save in the subdirectories defined in Table 1 are your default
resources. That is, these resources define the default design and content for your app.
However, different types of Android-powered devices might call for different types of resources.

For example, you can provide different string resources
that translate the text in your user interface based on the device's language setting.

**Note:** In Compose, UIs, animations, and state-driven colors are declared in Kotlin, so the
`layout/`, `menu/`, `anim/`, `animator/`,
and `color/` directories are obsolete for modern apps. For more
information, see [Animations in
Compose](https://developer.android.com/develop/ui/compose/animation/introduction) and [Anatomy of a theme
in Compose](https://developer.android.com/develop/ui/compose/designsystems/anatomy).

## Provide alternative resources

Most apps provide alternative resources to support specific device
configurations. For instance, include alternative drawable resources for different
screen densities and alternative string resources for different languages. At runtime, Android
detects the current device configuration and loads the appropriate
resources for your app.

To specify configuration-specific alternatives for a set of resources, do the following:

1. Create a new directory in `res/` named in the form `\<resources_name\>-\<qualifier\>`.
   - *`<resources_name>`* is the directory name of the corresponding default resources (defined in Table 1).
   - *`<qualifier>`* is a name that specifies an individual configuration for which these resources are to be used (defined in Table 2).

   You can append more than one *`<qualifier>`*. Separate each
   one with a dash.

   **Caution:** When appending multiple qualifiers, you must
   place them in the same order in which they are listed in Table 2. If the qualifiers are ordered
   incorrectly, the resources are ignored.
2. Save the appropriate alternative resources in this new directory. The resource files must be named exactly the same as the default resource files.

For example, here are some default and alternative resources:

```
res/
    drawable/
        icon.png
        background.png
    drawable-hdpi/
        icon.png
        background.png
```

The `hdpi` qualifier indicates that the resources in that directory are for devices with a
high-density screen. The images in these drawable directories are sized for specific
screen densities, but the filenames are exactly
the same. This way, the resource ID that you use to reference the `icon.png` or
`background.png` image is always the same. Android selects the
version of each resource that best matches the current device by comparing the device
configuration information with the qualifiers in the resource directory name.

**Caution:** When defining an alternative resource, make sure you
also define the resource in a default configuration. Otherwise, your app might encounter runtime
exceptions when the device changes a configuration. For example, if you add a string to only
`values-en` and not `values`, your app might encounter a
`Resource Not Found` exception when the user changes the default system language.

Table 2 lists configuration qualifiers in order of precedence. You can
add multiple qualifiers to one directory name by separating each qualifier with a dash. If you use
multiple qualifiers for a resource directory, you must add them to the directory name in the order they
are listed in the table.

**Table 2.** Configuration qualifier
names.

| Configuration | Qualifier values | Description |
|---|---|---|
| MCC and MNC | Examples: `mcc310` `mcc310-mnc004` `mcc208-mnc00` | The mobile country code (MCC), optionally followed by the mobile network code (MNC) from the SIM card in the device. For example, `mcc310` is U.S. on any carrier, `mcc310-mnc004` is U.S. on Verizon, and `mcc208-mnc00` is France on Orange. If the device uses a radio connection (that is, it's a GSM phone), the MCC and MNC values come from the SIM card. You can also use the MCC alone, for example, to include country-specific legal resources in your app. If you need to specify based on the language only, then use the *language, script (optional), and region (optional)* qualifier instead. If you use the MCC and MNC qualifier, do so with care and test that it works as expected. Also see the configuration fields `https://developer.android.com/reference/kotlin/android/content/res/Configuration#mcc` and `https://developer.android.com/reference/kotlin/android/content/res/Configuration#mnc`, which indicate the current mobile country code and mobile network code, respectively. |
| Language, script (optional), and region (optional) | Examples: `en` `fr` `en-rUS` `fr-rFR` `fr-rCA` `b+en` `b+en+US` `b+es+419` `b+zh+Hant` `b+sr+Latn+RS` | The language is defined by a two-letter [ISO 639-1](http://www.loc.gov/standards/iso639-1/code_list.php) language code, optionally followed by a two-letter [ISO 3166-1-alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) region code (preceded by lowercase `r`). The codes are *not* case-sensitive. The `r` prefix is used to distinguish the region portion. You can't specify a region alone. Android 7.0 (API level 24) introduced support for [BCP 47 language tags](https://tools.ietf.org/html/bcp47), which you can use to qualify language- and region-specific resources. A language tag is composed from a sequence of one or more subtags, each of which refines or narrows the range of language identified by the overall tag. For more information about language tags, see [Tags for Identifying Languages](https://tools.ietf.org/html/rfc5646). To use a BCP 47 language tag, concatenate `b+` and a two-letter [ISO 639-1](http://www.loc.gov/standards/iso639-1/code_list.php) language code, optionally followed by additional subtags separated by `+`. The language tag can change during the life of your app if users change their language in the system settings. For information about how this can affect your app during runtime, see [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes). For a complete guide to localizing your app for other languages, See [Localize your app](https://developer.android.com/guide/topics/resources/localization). Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#getlocales` method, which provides the defined list of locales. This list includes the primary locale. |
| Grammatical gender | `masculine` `feminine` `neuter` | The user's grammatical gender. Used for languages that have grammatical gender. For example, if you need to provide different resources for French speaking users, then you can use directories like the following: `res/` ` values-fr/` ` strings.xml` (default strings with unspecified gender) ` values-fr-masculine/` ` strings.xml` (strings with masculine gender) ` values-fr-feminine/` ` strings.xml` (strings with feminine gender) ` values-fr-neuter/` ` strings.xml` (strings with neutral gender) See [Personalize your app's UI with grammatical gender](https://developer.android.com/about/versions/14/features/grammatical-inflection). Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#getGrammaticalGender()` configuration method, which indicates the grammatical gender. *Added in API level 34.* |
| Wide Color Gamut | `widecg` `nowidecg` | - `widecg`: displays with a wide color gamut such as Display P3 or AdobeRGB - `nowidecg`: displays with a narrow color gamut such as sRGB *Added in API level 26.* Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#isscreenwidecolorgamut` configuration method, which indicates whether the screen has a wide color gamut. |
| High Dynamic Range (HDR) | `highdr` `lowdr` | - `highdr`: displays with a high dynamic range - `lowdr`: displays with a low/standard dynamic range *Added in API level 26.* Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#isscreenhdr` configuration method, which indicates whether the screen has HDR capabilities. |
| UI mode | `car` `desk` `television` `appliance` `watch` `vrheadset` | - `car`: device is displaying in a car dock - `desk`: device is displaying in a desk dock - `television`: device is displaying on a television, providing a "ten-foot" experience where its UI is on a large screen that the user is far away from, and the experience is primarily oriented around D-pad or other non-pointer interaction - `appliance`: device is serving as an appliance, with no display - `watch`: device has a display and is worn on the wrist - `vrheadset`: device is displaying in a virtual reality headset *Added in API level 8; television added in API 13; appliance added in API 16; watch added in API 20; vrheadset added in API 26.* For information about how your app can respond when the device is inserted into or removed from a dock, read [Determine and monitor the docking state and type](https://developer.android.com/training/monitoring-device-state/docking-monitoring). This can change during the life of your app if the user places the device in a dock. You can enable or disable some of these modes using `https://developer.android.com/reference/kotlin/android/app/UiModeManager`. For information about how this affects your app during runtime, see [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes). |
| Night mode | `night` `notnight` | - `night`: night time - `notnight`: day time *Added in API level 8.* This can change during the life of your app if night mode is left in auto mode (default), in which case the mode changes based on the time of day. You can enable or disable this mode using `https://developer.android.com/reference/kotlin/android/app/UiModeManager`. For information about how this affects your app during runtime, see [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes). |
| Screen pixel density (dpi) | `ldpi` `mdpi` `hdpi` `xhdpi` `xxhdpi` `xxxhdpi` `nodpi` `tvdpi` `anydpi` `nnndpi` | - `ldpi`: low-density screens; approximately 120 dpi. - `mdpi`: medium-density (on traditional HVGA) screens; approximately 160 dpi. - `hdpi`: high-density screens; approximately 240 dpi. - `xhdpi`: extra-high-density screens; approximately 320 dpi. *Added in API level 8.* - `xxhdpi`: extra-extra-high-density screens; approximately 480 dpi. *Added in API level 16.* - `xxxhdpi`: extra-extra-extra-high-density uses (launcher icon only---see [Support different pixel densities](https://developer.android.com/training/multiscreen/screendensities)); approximately 640 dpi. *Added in API level 18.* - `nodpi`: used for bitmap resources that you don't want to be scaled to match the device density. - `tvdpi`: screens somewhere between mdpi and hdpi; approximately 213 dpi. This isn't considered a "primary" density group. It is mostly intended for 720p televisions, and most apps don't need it. For 1080p TV panels, use `xhdpi`, and for 4K TV panels, use `xxxhdpi`. *Added in API level 13.* - `anydpi`: matches all screen densities and takes precedence over other qualifiers. This is useful for [vector drawables](https://developer.android.com/develop/ui/views/graphics/vector-drawable-resources). *Added in API level 21.* - `nnndpi`: used to represent non-standard densities, where `nnn` is a positive integer screen density. This isn't used in most cases. Using standard density buckets greatly reduces the overhead of supporting the various device screen densities on the market. There is a 3:4:6:8:12:16 scaling ratio between the six primary densities (ignoring the tvdpi density). So, a 9x9 bitmap in ldpi is 12x12 in mdpi, 18x18 in hdpi, 24x24 in xhdpi, and so on. **Note:** Using a density qualifier doesn't imply that the resources are *only* for screens of that density. If you don't provide alternative resources with qualifiers that better match the current device configuration, the system uses whichever resources are the [best match](https://developer.android.com/guide/topics/resources/providing-resources#BestMatch). For more information about how to handle different screen densities and how Android might scale your bitmaps to fit the current density, see [Screen compatibility overview](https://developer.android.com/guide/practices/screens_support). |
| Touchscreen type | `notouch` `finger` | - `notouch`: device doesn't have a touchscreen. - `finger`: device has a touchscreen that is intended to be used through direct interaction of the user's finger. Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#touchscreen` configuration field, which indicates the type of touchscreen on the device. |
| Keyboard availability | `keysexposed` `keyshidden` `keyssoft` | - `keysexposed`: device has a keyboard available. If the device has a software keyboard enabled (which is likely), this is used even when the hardware keyboard *isn't* exposed to the user or when the device has no hardware keyboard. If no software keyboard is provided or it's disabled, then this is only used when a hardware keyboard is exposed. - `keyshidden`: device has a hardware keyboard available but it is hidden *and* the device does *not* have a software keyboard enabled. - `keyssoft`: device has a software keyboard enabled, whether it's visible or not. If you provide `keysexposed` resources, but not `keyssoft` resources, the system uses the `keysexposed` resources regardless of whether a keyboard is visible, as long as the system has a software keyboard enabled. This can change during the life of your app if the user opens a hardware keyboard. For information about how this affects your app during runtime, see [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes). Also see the configuration fields `https://developer.android.com/reference/kotlin/android/content/res/Configuration#hardkeyboardhidden` and `https://developer.android.com/reference/kotlin/android/content/res/Configuration#keyboardhidden`, which indicate the visibility of a hardware keyboard and the visibility of any kind of keyboard (including software), respectively. |
| Primary text input method | `nokeys` `qwerty` `12key` | - `nokeys`: device has no hardware keys for text input. - `qwerty`: device has a hardware QWERTY keyboard, whether it's visible to the user or not. - `12key`: device has a hardware 12-key keyboard, whether it's visible to the user or not. Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#keyboard` configuration field, which indicates the primary text input method available. |
| Navigation key availability | `navexposed` `navhidden` | - `navexposed`: navigation keys are available to the user. - `navhidden`: navigation keys aren't available (such as behind a closed lid). This can change during the life of your app if the user reveals the navigation keys. For information about how this affects your app during runtime, see [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes). Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#navigationhidden` configuration field, which indicates whether the navigation keys are hidden. |
| Primary non-touch navigation method | `nonav` `dpad` `trackball` `wheel` | - `nonav`: device has no navigation facility other than using the touchscreen. - `dpad`: device has a directional-pad (D-pad) for navigation. - `trackball`: device has a trackball for navigation. - `wheel`: device has a directional wheel(s) for navigation (uncommon). Also see the `https://developer.android.com/reference/kotlin/android/content/res/Configuration#navigation` configuration field, which indicates the type of navigation method available. |
| Platform version (API level) | Examples: `v3` `v4` `v7` etc. | The API level supported by the device. For example, `v1` for API level 1 (devices with Android 1.0 or higher) and `v4` for API level 4 (devices with Android 1.6 or higher). For more information about these values, see the [Android API levels](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels) document. |

**Note:** Not all versions of Android support all the qualifiers. Using a new qualifier implicitly
adds the platform version qualifier so that older devices can ignore it. To avoid any issues, always include a set of
default resources (a set of resources with *no qualifiers* ). For more information, see the
section about [providing the best device compatibility with
resources](https://developer.android.com/guide/topics/resources/providing-resources#Compatibility).

In Compose apps, layout- and dimension-related configuration qualifiers aren't needed. While they
still exist, they are excluded from Table 2. These qualifiers include: layout direction, smallest
width, available width, available height, screen size, screen aspect, round screen, and screen
orientation. For the full table of configuration qualifiers in order of precedence, see
[App resources overview (Views)](https://developer.android.com/topic/architecture/views/resources/providing-resources-views).

### Qualifier name rules

Here are some rules about using configuration qualifier names:

- You can specify multiple qualifiers for a single set of resources, separated by dashes. For example, `drawable-en-rUS-night` applies to US-English devices in night mode.
- The qualifiers must be in the order listed in [Table 2](https://developer.android.com/guide/topics/resources/providing-resources#table2).
  - Wrong: `drawable-hdpi-night/`
  - Correct: `drawable-night-hdpi/`
- Alternative resource directories can't be nested. For example, you can't have `res/drawable/drawable-en/`.
- Values are case-insensitive. The resource compiler converts directory names to lowercase before processing to avoid problems on case-insensitive file systems. Any capitalization in the names is only to benefit readability.
- Only one value for each qualifier type is supported. For example, if you want to use the same drawable files for Spain and France, you *can't* have a directory named `drawable-es-fr/`. Instead, you need two resource directories, such as `drawable-es/` and `drawable-fr/`, which contain the appropriate files.

After you save alternative resources into directories named with
these qualifiers, Android automatically applies the resources in your app based on the
current device configuration. Each time a resource is requested, Android checks for alternative
resource directories that contain the requested resource file, then [finds the
best-matching resource](https://developer.android.com/guide/topics/resources/providing-resources#BestMatch).

If there are no alternative resources that match
a particular device configuration, then Android uses the corresponding default resources---the
set of resources for a particular resource type that doesn't include a configuration
qualifier.

### Create alias resources

When you have a resource that you'd like to use for more than one device
configuration but you don't want to provide it as a default resource, you don't need to put the same
resource in more than one alternative resource directory. Instead, you can create an
alternative
resource that acts as an alias for a resource saved in your default resource directory.

#### Drawables

For example, imagine you have an app icon, `icon.png`, and need a unique version of
it for different locales. However, two locales, English-Canadian and French-Canadian, need to
use the same version. You don't need to copy the same image
into the resource directory for both English-Canadian and French-Canadian.
Instead, you can save the image that's used for both using any name *other than*
`icon.png`, such as `icon_ca.png`, and put
it in the default `res/drawable/` directory. Then create an `icon.xml` file in
`res/drawable-en-rCA/` and `res/drawable-fr-rCA/` that refers to the `icon_ca.png`
resource using the `<bitmap>` element.

```xml
<?xml version="1.0" encoding="utf-8"?>
<bitmap xmlns:android="http://schemas.android.com/apk/res/android" android:src="@drawable/icon_ca" />
```

This lets you store just one version of the
PNG file and two small XML files that point to it.
Then you can use `painterResource(R.drawable.icon)` and the system will pick the
appropriate file once it detects the locale.

#### Strings and other simple values

To create an alias to an existing string, use the resource ID of the desired
string as the value for the new string:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="hello">Hello</string>
    <string name="hi">@string/hello</string>
</resources>
```

The `R.string.hi` resource is now an alias for the `R.string.hello`.

[Other simple values](https://developer.android.com/guide/topics/resources/more-resources) work the
same way, such as colors:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="red">#f00</color>
    <color name="highlight">@color/red</color>
</resources>
```

## Access your app resources

Once you provide a resource in your application, you can apply it by
referencing its resource ID. All resource IDs are defined in your project's `R` class, which
the `aapt` tool automatically generates.

When your application is compiled, `aapt` generates the `R` class, which contains
resource IDs for all the resources in your `res/` directory. For each type of resource,
there is an `R` subclass, such as
`R.drawable` for all drawable resources. And for each resource of that type, there is a
static integer, for example, `R.drawable.icon`. This integer is the resource ID that you can use
to retrieve your resource.

Although the `R` class is where resource IDs are specified, you don't need to
look there to discover a resource ID. A resource ID is always composed of the following:

- The *resource type* : each resource is grouped into a "type," such as `string` or `drawable`.
- The *resource name*, which is the filename excluding the extension.

### Access resources in Compose

Jetpack Compose provides built-in, composable-aware functions to access resources securely.

- **Strings:**

  ```
  stringResource(id = R.string.hello)
  ```
- **Drawables:**

  ```
  painterResource(id = R.drawable.my_icon)
  ```

### Access resources in non-UI code

If you need to access resources outside of your UI hierarchy---such as in a
`ViewModel`, a `Repository`, or a system `Service`---you can
resolve them using the `Context`.

```kotlin
// Retrieve a localized string resource
val greeting = context.getString(R.string.hello_world)
```

You can also retrieve individual resources using methods in `https://developer.android.com/reference/kotlin/android/content/res/Resources`, which you can get an instance of
with `https://developer.android.com/reference/kotlin/android/content/Context#getresources`.

#### Syntax

Here's the syntax to reference a resource in code:

```
[<package_name>.]R.<resource_type>.<resource_name>
```

- *`<package_name>`* is the name of the package in which the resource is located (not required when referencing resources from your own package).
- *`<resource_type>`* is the `R` subclass for the resource type.
- *`<resource_name>`* is either the resource filename without the extension or the `android:name` attribute value in the XML element, for simple values.

For more information about each resource type and how to reference them, see
[Resources in Compose](https://developer.android.com/develop/ui/compose/resources).

### Access original files

While uncommon, you might need to access your original files and directories. If you do, then
saving your files in `res/` won't work for you, because the only way to read a resource from
`res/` is with the resource ID. Instead, you can save your resources in the
`assets/` directory.

Files saved in the `assets/` directory are *not* given a resource
ID, so you can't reference them through the `R` class or from XML resources. Instead, you can
query files in the `assets/` directory like a normal file system and read raw data using
`https://developer.android.com/reference/kotlin/android/content/res/AssetManager`.

However, if all you require is the ability to read raw data (such as a video or audio file),
then save the file in the `res/raw/` directory and read a stream of bytes using
`https://developer.android.com/reference/kotlin/android/content/res/Resources#openrawresource`.

### Access platform resources

Android contains a number of standard resources, such as system styles and themes. To access
these, qualify your resource reference with the `android` package class. For example:
`painterResource(android.R.drawable.ic_menu_info_details)`.

## Provide the best device compatibility with resources

For your app to support multiple device configurations, it's very important that
you always provide default resources for each type of resource that your app uses.

For example, if your app supports several languages, always include a `values/` directory (in which your strings are saved) *without* a [language and region qualifier](https://developer.android.com/guide/topics/resources/providing-resources#LocaleQualifier). If you instead put all your string files
in directories that have a language and region qualifier, then your app crashes when run
on a device set to a language that your strings don't support.

As long as you provide default
`values/` resources, then your app runs properly, even if the user doesn't
understand the language it presents. It's better than crashing.

Providing default resources is important not only because your app might run on a
configuration you hadn't anticipated, but also because new versions of Android sometimes add
configuration qualifiers that lower versions don't support. If you use a new resource qualifier,
but maintain code compatibility with lower versions of Android, then when a lower version of
Android runs your app, it crashes if you don't provide default resources, because it
can't use the resources named with the new qualifier.

For example, if your [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) is set to 4, and you qualify all of your drawable resources using [night mode](https://developer.android.com/guide/topics/resources/providing-resources#NightQualifier) (`night` or `notnight`, which were added in API
level 8), then an API level 4 device can't access your drawable resources and crashes. In this
case, you probably want `notnight` to be your default resources, so exclude that
qualifier and put your drawable resources in either `drawable/` or `drawable-night/`.

In short, to provide the best device compatibility, always provide default
resources for the resources your app needs to perform properly. Then create alternative
resources for specific device configurations using configuration qualifiers.

There is one exception to this rule: If your app's [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) is 4 or
greater, you *don't* need default drawable resources when you provide alternative drawable
resources with the [screen density](https://developer.android.com/guide/topics/resources/providing-resources#DensityQualifier) qualifier. Even without default
drawable resources, Android can find the best match among the alternative screen densities and scale
the bitmaps as necessary. However, for the best experience on all types of devices,
provide alternative drawables for all three types of density.

## How Android finds the best-matching resource

When you request a resource for which you provide alternatives, Android selects which
alternative resource to use at runtime, depending on the current device configuration. To
demonstrate how Android selects an alternative resource, assume the following drawable directories
each contain different versions of the same images:

```
drawable/
drawable-en/
drawable-fr-rCA/
drawable-en-night/
drawable-en-notouch-12key/
drawable-night-ldpi/
drawable-night-notouch-12key/
```

And assume the following is the device configuration:


Locale = `en-GB`   

Night mode = `night`   

Screen pixel density = `hdpi`   

Touchscreen type = `notouch`   

Primary text input method = `12key`

By comparing the device configuration to the available alternative resources, Android selects
drawables from `drawable-en-night`.

The system arrives at its decision for which resources to use with the following
logic:
![](https://developer.android.com/static/images/resources/res-selection-flowchart.png)

**Figure 2.** Flowchart of how Android finds the
best-matching resource.

1. Eliminate resource files that contradict the device configuration. The `drawable-fr-rCA/` directory is eliminated, because it
   contradicts the `en-GB` locale.

   ```
   drawable/
   drawable-en/
   drawable-fr-rCA/
   drawable-en-night/
   drawable-en-notouch-12key/
   drawable-night-ldpi/
   drawable-night-notouch-12key/
   ```

   **Exception:** Screen pixel density is the one qualifier that is not
   eliminated due to a contradiction. Even though the screen density of the device is hdpi,
   `drawable-night-ldpi/` isn't eliminated because every screen density is
   considered to be a match at this point. For information, see [Screen compatibility overview](https://developer.android.com/guide/practices/screens_support).
2. Find the next-highest-precedence qualifier in the list ([Table 2](https://developer.android.com/guide/topics/resources/providing-resources#table2)). (Start with MCC.)
3. Do any of the resource directories include this qualifier?
   - If no, return to step two and look at the next qualifier. In this example, the answer is "no" until the language qualifier is reached.
   - If yes, continue to step four.
4. Eliminate resource directories that don't include this qualifier. In this example, the system next eliminates all the directories that don't include a language qualifier:

   ```
   drawable/
   drawable-en/
   drawable-en-night/
   drawable-en-notouch-12key/
   drawable-night-ldpi/
   drawable-night-notouch-12key/
   ```

   **Exception:** If the qualifier in question is screen pixel density,
   Android selects the option that most closely matches the device screen density.
   In general, Android prefers scaling down a larger original image to scaling up a smaller
   original image. For more information, see [Screen
   compatibility overview](https://developer.android.com/guide/practices/screens_support).
5. Repeat steps two, three, and four until only one directory remains. In this example, night mode is the next qualifier for which there are any matches. So, resources that don't specify night mode are eliminated:

   ```
   drawable-en/
   drawable-en-night/
   drawable-en-notouch-12key/
   ```

   The remaining directory is `drawable-en-night`.

Though this procedure is executed for each resource requested, the system optimizes
some aspects of it. One such optimization is that once the device configuration is known, it might
eliminate alternative resources that can never match. For example, if the configuration
language is English, then any resource directory that has a language qualifier set to
something other than English is never included in the pool of resources checked (though a
resource directory *without* the language qualifier is still included).

When selecting resources based on the screen size qualifiers, the system uses resources
designed for a screen smaller than the current screen if there are no resources that better match.
For example, a large-size screen uses normal-size screen resources if necessary.

However, if
the only available resources are *larger* than the current screen, the system
**doesn't** use them and your app crashes if no other resources match the device
configuration. This happens, for example, if all layout resources are tagged with the `xlarge` qualifier,
but the device is a normal-size screen.

**Note:** The *precedence* of the qualifier (in [Table 2](https://developer.android.com/guide/topics/resources/providing-resources#table2)) is more important
than the number of qualifiers that exactly match the device. In the preceding example, at step four
the last choice on the list includes three qualifiers that exactly match the device (night mode,
touchscreen type, and input method), while `drawable-en` has only one parameter that matches
(language). However, language has a higher precedence than these other qualifiers, so
`drawable-night-notouch-12key` is eliminated.

## Additional resources

To learn more about app resources, see the following additional resources:

### Documentation

- [Resources in Compose](https://developer.android.com/develop/ui/compose/resources)

### Views content

- [App resources overview (Views)](https://developer.android.com/topic/architecture/views/resources/providing-resources-views)