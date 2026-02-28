---
title: https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat
url: https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to support emoji in Compose. [Support emoji →](https://developer.android.com/develop/ui/compose/text/emoji) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

> [!CAUTION]
> **Caution:** As of late 2021, the `androidx.emoji:emoji`
> library is deprecated in favor of `androidx.emoji2:emoji2`, which
> provides integration into `androidx.appcompat`.
>
> To support modern emoji and simplify backward-compatibility with lower
> versions of Android, it's recommended that you migrate to the
> [`androidx.emoji2:emoji2`](https://developer.android.com/jetpack/androidx/releases/emoji2)
> library. For details on how to implement, see
> [Support modern emoji](https://developer.android.com/guide/topics/ui/look-and-feel/emoji2).


The `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library aims to
keep Android devices up to date with the latest emoji. It prevents your app
from showing missing emoji characters in the form of ☐, which
indicates that your device does not have a font to display the text. By
using the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library,
your app users do not need to wait for Android OS updates to get the latest
emoji.
![Devices showing emoji](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/emoji-compat/emoji-comparison.png) **Figure 1.** Emoji comparison


Refer to the following related resources:

- Emoji Compatibility sample app [Java](https://github.com/android/user-interface-samples/tree/main/EmojiCompat) \| [Kotlin](https://github.com/android/user-interface-samples/tree/main/EmojiCompatKotlin)

## How does EmojiCompat work?


The `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library provides
classes to implement backward-compatible emoji support on devices running
Android 4.4 (API level 19) and higher. You can configure
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` with either bundled or
downloadable fonts. For more information about configuration, refer to the
following sections:

- [Downloadable fonts configuration](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat#downloadable-fonts)
- [Bundled fonts configuration](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat#bundled-fonts)


`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` identifies emoji for a given
`https://developer.android.com/reference/java/lang/CharSequence`, replaces them with
`https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`, if required, and
finally renders the emoji glyphs. Figure 2 demonstrates the process.
![EmojiCompat process](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/emoji-compat/architecture.png) **Figure 2.** EmojiCompat process

## Downloadable fonts configuration

The downloadable fonts configuration uses the Downloadable Fonts support
library feature to download an emoji font. It also updates the necessary
emoji metadata that the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`
support library needs to keep up with the latest versions of the Unicode
specification.

### Adding support library dependency


To use the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library,
you must modify your app project's classpath dependencies within your
development environment.


To add a support library to your application project:

1. Open the `build.gradle` file of your application.
2. Add the support library to the `dependencies` section.

### Groovy

```groovy
dependencies {
    ...
    implementation "androidx.emoji:emoji:28.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("androidx.emoji:emoji:28.0.0")
}
```

### Initializing the downloadable font
configuration


You need to initialize `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` to
load the metadata and the typeface. Since initialization can take some time,
the initialization process runs on a background thread.


To initialize `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` with the
downloadable font configuration, perform the following steps:

1. Create an instance of the `https://developer.android.com/reference/androidx/core/provider/FontRequest` class and provide the font provider authority, the font provider package, the font query, and a list of sets of hashes for the certificate. For more information about `https://developer.android.com/reference/androidx/core/provider/FontRequest`, refer to the [Using Downloadable Fonts programmatically](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts#programmatically) section in the [Downloadable Fonts](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts) documentation.
2. Create an instance of `https://developer.android.com/reference/androidx/emoji/text/FontRequestEmojiCompatConfig` and provide instances of `https://developer.android.com/reference/android/content/Context` and `https://developer.android.com/reference/androidx/core/provider/FontRequest`.
3. Initialize `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` by calling the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#init(android.support.text.emoji.EmojiCompat.Config)` method and pass the instance of `https://developer.android.com/reference/androidx/emoji/text/FontRequestEmojiCompatConfig`.

### Kotlin

```kotlin
class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()
        val fontRequest = FontRequest(
                "com.example.fontprovider",
                "com.example",
                "emoji compat Font Query",
                CERTIFICATES
        )
        val config = FontRequestEmojiCompatConfig(this, fontRequest)
        EmojiCompat.init(config)
    }
}
```

### Java

```java
public class MyApplication extends Application {
  @Override
   public void onCreate() {
     super.onCreate();
     FontRequest fontRequest = new FontRequest(
       "com.example.fontprovider",
       "com.example",
       "emoji compat Font Query",
       CERTIFICATES);
     EmojiCompat.Config config = new FontRequestEmojiCompatConfig(this, fontRequest);
     EmojiCompat.init(config);
   }
}
```
4. Use `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` widgets in layout XMLs. If you are using `https://developer.android.com/reference/android/support/v7/appcompat/package-summary`, refer to the [Using EmojiCompat widgets with AppCompat](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat#using-widgets-with-appcompat) section.

```xml
<android.support.text.emoji.widget.EmojiTextView
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>

<android.support.text.emoji.widget.EmojiEditText
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>

<android.support.text.emoji.widget.EmojiButton
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>
```


For more information about how to configure
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` with the downloadable font
configuration, go to Emoji Compatibility sample app
[Java](https://github.com/android/user-interface-samples/tree/main/EmojiCompat) \| [Kotlin](https://github.com/android/user-interface-samples/tree/main/EmojiCompatKotlin).

## Library components

![Library components in EmojiCompat process](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/emoji-compat/basic-components.png) **Figure 3.** Library components in the EmojiCompat process

Widgets: `https://developer.android.com/reference/androidx/emoji/widget/EmojiEditText`,
`https://developer.android.com/reference/androidx/emoji/widget/EmojiTextView`,
`https://developer.android.com/reference/androidx/emoji/widget/EmojiButton`
:   Default widget implementations to use
    `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` with
    `https://developer.android.com/reference/android/widget/TextView`, `https://developer.android.com/reference/android/widget/EditText`, and
    `https://developer.android.com/reference/android/widget/Button`.

`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`
:   Main public surface for the support library. It performs all the
    external calls and coordinates with the other parts of the system.

`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.Config`
:   Configures the singleton instance to be created.

`https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`
:   A `https://developer.android.com/reference/android/text/style/ReplacementSpan` subclass that replaces the
    character (sequences) and renders the glyph.

`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` Font
:   `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` uses a font to display
    emoji. This font is a modified version of the
    [Android Emoji font](https://www.google.com/get/noto/help/emoji/).
    The font is modified as follows:

    - To provide backward compatibility to render emoji, all emoji characters are represented with a single Unicode code point in Unicode's Supplemental Private Use Area-A starting with U+F0001.
    - Extra emoji metadata is inserted in a binary format into the font and is parsed at runtime by `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`. The data is embedded in the font's `meta` table, with the private tag *Emji*.

## Configuration options


You can use the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` instance to
modify `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` behavior. You can use
the following methods from the base class to set the configuration:

- `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.Config#setReplaceAll(boolean)`: Determines whether `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` should replace all emoji it finds with `https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`. By default, `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` tries its best to understand if the system can render an emoji and does not replace those emoji. When set to `true`, `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` replaces all emoji it finds with `https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`.
- `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.Config#setEmojiSpanIndicatorEnabled(boolean)`: Indicates whether `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` has replaced an emoji with an `https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`. When set to `true`, `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` draws a background for the `https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`. This method is mainly used for debugging purposes.
- `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.Config#setEmojiSpanIndicatorColor(int)`: Sets the color to indicate an `https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`. The default value is `https://developer.android.com/reference/android/graphics/Color#GREEN`.
- `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#registerInitCallback(android.support.text.emoji.EmojiCompat.InitCallback)`: Informs app about the state of the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` initialization.

### Kotlin

```kotlin
val config = FontRequestEmojiCompatConfig(...)
        .setReplaceAll(true)
        .setEmojiSpanIndicatorEnabled(true)
        .setEmojiSpanIndicatorColor(Color.GREEN)
        .registerInitCallback(object: EmojiCompat.InitCallback() {
            ...
        })
```

### Java

```java
EmojiCompat.Config config = new FontRequestEmojiCompatConfig(...)
       .setReplaceAll(true)
       .setEmojiSpanIndicatorEnabled(true)
       .setEmojiSpanIndicatorColor(Color.GREEN)
       .registerInitCallback(new InitCallback() {...})
```

## Adding initialization listeners


`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` and
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` classes
provide
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#registerInitCallback(android.support.text.emoji.EmojiCompat.InitCallback)`
and
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#unregisterInitCallback(android.support.text.emoji.EmojiCompat.InitCallback)`
methods to register an initialization callback. To use these methods, create
an instance of the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.InitCallback` class. Call
these methods and pass the instance of the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.InitCallback` class. When the
initialization of the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support
library is successful, the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`
class calls the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.InitCallback#onInitialized()`
method. If the library
fails to initialize, the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`
class calls the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.InitCallback#onFailed(java.lang.Throwable)`
method.


To check the initialization state at any point, call the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#getLoadState()`
method. It returns one of the following values:
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#LOAD_STATE_LOADING`,
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#LOAD_STATE_SUCCEEDED`,
or `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#LOAD_STATE_FAILED`.

## Using EmojiCompat with AppCompat widgets


If you are using `https://developer.android.com/reference/android/support/v7/widget/package-summary`, you
can use `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` widgets that extend
from `https://developer.android.com/reference/android/support/v7/widget/package-summary`.

1. Add the support library to the dependencies section.

   ### Groovy

   ```groovy
   dependencies {
       ...
       implementation "androidx.emoji:emoji-bundled:$version"
   }
   ```

   ### Kotlin

   ```kotlin
         dependencies {
             implementation("androidx.emoji:emoji-appcompat:$version")
         }
         
   ```

   ### Groovy

   ```groovy
         dependencies {
             implementation "androidx.emoji:emoji-appcompat:$version"
         }
         
   ```
2. Use `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` `https://developer.android.com/reference/android/support/v7/widget/package-summary` widgets in layout XMLs.

```xml
<android.support.text.emoji.widget.EmojiAppCompatTextView
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>

<android.support.text.emoji.widget.EmojiAppCompatEditText
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>

<android.support.text.emoji.widget.EmojiAppCompatButton
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>
```

## Bundled fonts configuration


The `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library is also
available in a bundled font version. This package includes the font with the
embedded metadata. The package also includes a
`https://developer.android.com/reference/androidx/emoji/bundled/BundledEmojiCompatConfig`
that uses the `https://developer.android.com/reference/android/content/res/AssetManager` to load the metadata
and fonts.

**Note:** The size of the font is in multiple
megabytes.

### Adding support library dependency


To use the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library
with bundled font configuration, you *must* modify your app project's
classpath dependencies within your development environment.


To add a support library to your application project:

1. Open the `build.gradle` file of your application.
2. Add the support library to the `dependencies` section.

### Groovy

```groovy
dependencies {
    ...
    implementation "androidx.emoji:emoji:28.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("androidx.emoji:emoji:28.0.0")
}
```

### Using bundled fonts to configure EmojiCompat


To use bundled fonts to configure
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`, perform the following steps:

1. Use `https://developer.android.com/reference/androidx/emoji/bundled/BundledEmojiCompatConfig` to create an instance of `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` and provide an instance of `https://developer.android.com/reference/android/content/Context`.
2. Call the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#init(android.support.text.emoji.EmojiCompat.Config)` method to initialize `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` and pass the instance of `https://developer.android.com/reference/androidx/emoji/bundled/BundledEmojiCompatConfig`.

### Kotlin

```kotlin
class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()
        val config = BundledEmojiCompatConfig(this)
        EmojiCompat.init(config)
    }
}
```

### Java

```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        EmojiCompat.Config config = new BundledEmojiCompatConfig(this);
        EmojiCompat.init(config);
        ...
    }
}
```

## Using EmojiCompat without widgets


`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` uses
`https://developer.android.com/reference/androidx/emoji/text/EmojiSpan` to render correct images.
Therefore, it has to convert any given `https://developer.android.com/reference/java/lang/CharSequence` into
`https://developer.android.com/reference/android/text/Spanned` instances with
`https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`. The
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` class provides a method to
convert `https://developer.android.com/reference/java/lang/CharSequence` into
`https://developer.android.com/reference/android/text/Spanned` instances with
`https://developer.android.com/reference/androidx/emoji/text/EmojiSpan`. Using this method,
you can process and cache the processed instances instead of the raw string,
which improves the performance of your application.

### Kotlin

```kotlin
val processed = EmojiCompat.get().process("neutral face \uD83D\uDE10")
```

### Java

```java
CharSequence processed = EmojiCompat.get().process("neutral face \uD83D\uDE10");
```

## Using EmojiCompat for IMEs


Using the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library,
keyboards can render the emoji supported by the application they are
interacting with. IMEs can use the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#hasEmojiGlyph(java.lang.CharSequence)`
method to check if `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` is capable
of rendering an emoji. This method takes a `https://developer.android.com/reference/java/lang/CharSequence` of
an emoji and returns `true` if
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` can detect and render the
emoji.


The keyboard can also check the version of the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library that the app
supports to determine which emoji to render in the palette. To check the
version, if available, the keyboard needs to check whether the following
keys exist in the
`https://developer.android.com/reference/android/view/inputmethod/EditorInfo#extras`
bundle:

- `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#EDITOR_INFO_METAVERSION_KEY`
- If the key exists in the bundle, the value represents the version of the emoji metadata that the app uses. If this key does not exist, the app is not using `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`.
- `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#EDITOR_INFO_REPLACE_ALL_KEY`
- If the key exists and is set to `true`, this indicates that the app has called the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat.Config#setReplaceAll(boolean)` method. For more information about `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` configuration, refer to the [Configuration options](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat#configuration-options) section.


After receiving the keys in the
`https://developer.android.com/reference/android/view/inputmethod/EditorInfo#extras` bundle,
the keyboard can use the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#hasEmojiGlyph(java.lang.CharSequence, int)`
method, where `metadataVersion` is the value for
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#EDITOR_INFO_METAVERSION_KEY`,
to check whether the app can render a specific emoji.

## Using EmojiCompat with custom widgets


You can always use the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#process(java.lang.CharSequence)`
method to preprocess the `https://developer.android.com/reference/java/lang/CharSequence` in your app and add
it to any widget that can render `https://developer.android.com/reference/android/text/Spanned` instances; for
example, `https://developer.android.com/reference/android/widget/TextView`. In addition,
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` provides the following widget
helper classes to let you enrich your custom widgets with emoji support with
minimum effort.

- `https://developer.android.com/reference/androidx/emoji/widget/EmojiTextViewHelper`
- `https://developer.android.com/reference/androidx/emoji/widget/EmojiEditTextHelper`

**Sample TextView**
**Sample EditText**

## Frequently asked questions

- **How do I initiate the font download?**
- The emoji fonts are downloaded on first request, if they do not exist on the device. The download scheduling is transparent to the app.
- **How much time does it take to initialize?**
- After the font is downloaded, it takes approximately 150 milliseconds to initialize `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`.
- **How much memory does the EmojiCompat support library use?**
- Currently, the data structure to find the emoji is loaded in the app's memory and uses around 200KB.
- **Can I use EmojiCompat for a custom TextView?**
- Yes. EmojiCompat provides helper classes for custom widgets. It is also possible to preprocess a given string and convert it to `https://developer.android.com/reference/android/text/Spanned`. For more information about widget helper classes, refer to the [Using EmojiCompat with custom widgets](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-compat#using-emojicompat-with-custom-widgets) section.
- **What happens if I add widgets in layout XMLs on devices that
  run on Android 4.4 (API level 19) or lower?**
- You can include the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` support library or its widgets in your applications that support devices running Android 4.4 (API level 19) or lower. However, if a device runs on an Android version prior to API level 19, `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` and its widgets are in a "no operation" state. This means that `https://developer.android.com/reference/androidx/emoji/widget/EmojiTextView` behaves exactly like a regular `https://developer.android.com/reference/android/widget/TextView`. `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat` instance; it immediately gets into a `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#LOAD_STATE_SUCCEEDED` state when you call the `https://developer.android.com/reference/androidx/emoji/text/EmojiCompat#init(android.support.text.emoji.EmojiCompat.Config)` method.

## Additional resources


For additional information on using the
`https://developer.android.com/reference/androidx/emoji/text/EmojiCompat`
library, watch [EmojiCompat](https://www.youtube.com/watch?v=sYGKUtM2ga8).