---
title: https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts
url: https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use text in Compose. [Downloadable Fonts →](https://developer.android.com/jetpack/compose/text/fonts#downloadable-fonts) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The Downloadable Fonts feature lets APIs request fonts from a provider application instead of
bundling files into the app or letting the app download fonts. Downloadable Fonts is available on
devices running Android API versions 14 and higher through the AndroidX Core library.

Downloadable Fonts offers the following benefits:

- Reduces the app size, therefore increasing the app installation success rate.
- Improves the overall system health, as multiple apps can share the same font through a provider. This saves users cellular data, phone memory, and disk space. In this model, the font is fetched over the network when needed.

For hands-on experience with Downloadable Fonts, see the [DownloadableFonts](https://github.com/android/user-interface-samples/tree/main/DownloadableFonts) sample app.

### How does Downloadable Fonts work?

A font provider is an application that retrieves fonts and caches them locally so other apps can
request and share fonts. The following figure illustrates the process.
![An images showing the main components in Emoji compat process](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/downloadable-fonts/downloadable-fonts-process.png) **Figure 1.** Downloadable Fonts process.

### The basics

You can use the Downloadable Fonts feature in the following ways, which are discussed in detail'
in later sections:

- [Using Android Studio and Google Play Services](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#via-android-studio)
- [Programmatically](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#programmatically)
- [Using the AndroidX Core library](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#via-support-lib)

### Use Downloadable Fonts with Android Studio and Google Play services

You can set your application to download fonts by using Android Studio 3.0 or higher. To help you
get started with Downloadable Fonts features, you can use the font provider from Google Play
services.

> [!NOTE]
> **Note:** A device must have Google Play services version 11 or higher to use the Google Fonts provider.

1. In the **Layout Editor** , select a `TextView`. Then, under **Attributes** , select **fontFamily \> More Fonts** . ![An image showing Android Studio Layout Editor](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/downloadable-fonts/layout-editor.png) **Figure 2.** Using the **Layout Editor**. The **Resources** window appears.
2. In the **Source** menu, select **Google Fonts**.
3. In the **Fonts** box, select a font under the "Downloadable" area.
4. Select **Create downloadable font** and click **OK** . ![An image showing how to select fonts from the Resources window](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/downloadable-fonts/resources-window.png) **Figure 3.** Selecting a font from the **Resources** window.
5. Android Studio automatically generates the relevant XML files that are needed to render the font correctly in your app.
![An image showing how to preview fonts](https://developer.android.com/static/guide/topics/ui/images/look-and-feel/downloadable-fonts/preview-fonts.png) **Figure 4.** Previewing the font file.

### Use Downloadable Fonts programmatically

As of Android 8.0 (API level 26), AndroidX Core provides full support for Downloadable Fonts. For
more information about using the AndroidX Core library, see the
[Downloadable Fonts AndroidX Core library section](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#via-support-lib) on this page.

To use the Downloadable Fonts feature programmatically, interact with two key classes:

- **`https://developer.android.com/reference/kotlin/androidx/core/provider/FontRequest`**: this class lets you create a font request.
- **`https://developer.android.com/reference/androidx/core/provider/FontsContractCompat`** : this class lets you create a new `https://developer.android.com/reference/android/graphics/Typeface` object based on the font request.

Your app retrieves fonts from the font provider by using the `FontsContract` API. Each
provider has its own set of restrictions on the Android versions and query language it supports. For
more information on the Android versions and query format, refer to your provider's
documentation.

To download a font, complete the following steps:

1. Create an instance of the `android.graphics.fonts.FontRequest` class to request the font from the provider. To create a request, pass the following parameters:
   - The font provider authority.
   - The font provider package to verify the identity of the provider.
   - The string query of the font. For more information about query formats, see your font provider's documentation, such as [Google Fonts](https://developers.google.com/fonts/docs/android).
   - A list of sets of hashes for the certificates to verify the identity of the provider.

     > [!NOTE]
     > **Note** : It's unnecessary to add a certificate if you request fonts from preinstalled providers. However, always provide a certificate if you request fonts through AndroidX Core library.
     >
     > <br />
     >
   ### Kotlin

   ```kotlin
   val request = FontRequest(
           "com.example.fontprovider.authority",
           "com.example.fontprovider",
           "my font",
           certs
   )
   ```

   ### Java

   ```java
   FontRequest request = new FontRequest("com.example.fontprovider",
                      "com.example.fontprovider", "my font", certs);
   ```

   > [!NOTE]
   > **Note**: You can receive the parameter values from your font provider. Android Studio automatically populates these values for the providers it supports in its UI.

2. Create an instance of the `https://developer.android.com/reference/android/provider/FontsContract.FontRequestCallback` class.
3. Override the `https://developer.android.com/reference/android/provider/FontsContract.FontRequestCallback#onTypefaceRetrieved(android.graphics.Typeface)` method to indicate the font request is complete. Provide the retrieved font as the parameter. You can use this method to set the font as needed. For example, you can set the font on a `https://developer.android.com/reference/android/widget/TextView`.
4. Override the `https://developer.android.com/reference/android/provider/FontsContract.FontRequestCallback#onTypefaceRequestFailed(int)` method to receive information about errors in the font request process. For more information about error codes, refer to the [error code constants](https://developer.android.com/reference/android/provider/FontsContract.FontRequestCallback#FAIL_REASON_FONT_LOAD_ERROR).
5. Call the `FontsContract.requestFont()` method to retrieve the font from the font provider. The method initiates a check to determine whether the font exists in the cache. If the font isn't available locally, it calls the font provider, retrieves the font asynchronously, and passes the result to the callback. Pass the following parameters:
   - An instance of the `https://developer.android.com/reference/android/content/Context` class
   - An instance of the `android.graphics.fonts.FontRequest` class
   - A callback to receive the results of the font request
   - A handler to fetch fonts on a thread

   > [!NOTE]
   > **Note**: Ensure that this handler isn't the user interface thread handler.

The following sample code illustrates the overall Downloadable Fonts process:

### Kotlin

```kotlin
val request = FontRequest(
        "com.example.fontprovider.authority",
        "com.example.fontprovider",
        "my font",
        certs
)
val callback = object : FontsContract.FontRequestCallback() {

    override fun onTypefaceRetrieved(typeface: Typeface) {
        // Your code to use the font goes here.
        ...
    }

    override fun onTypefaceRequestFailed(reason: Int) {
        // Your code to deal with the failure goes here.
        ...
    }
}
FontsContract.requestFonts(context, request, handler, null, callback)
```

### Java

```java
FontRequest request = new FontRequest("com.example.fontprovider.authority",
        "com.example.fontprovider", "my font", certs);
FontsContract.FontRequestCallback callback =
    new FontsContract.FontRequestCallback() {
        @Override
        public void onTypefaceRetrieved(Typeface typeface) {
            // Your code to use the font goes here.
            ...
        }

        @Override
        public void onTypefaceRequestFailed(int reason) {
            // Your code to deal with the failure goes here.
            ...
        }
};
FontsContract.requestFonts(context, request, handler, null, callback);
```

For more information about how to download a font from a font provider, see the
[DownloadableFonts](https://github.com/android/user-interface-samples/tree/main/DownloadableFonts)
sample app.

### Use Downloadable Fonts with AndroidX Core

The AndroidX Core provides support for the Downloadable Fonts feature on devices running Android
API versions 14 or higher. The
`https://developer.android.com/reference/androidx/core/provider/package-summary`
package contains `FontsContractCompat` and `FontRequest` classes to implement
the backward-compatible Downloadable Fonts feature support. The AndroidX classes contain methods
similar to the framework methods, and the process for downloading fonts is similar to the one
described in the section on this page about
[using Downloadable Fonts programmatically](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#programmatically).

To download fonts using AndroidX, import the `FontsContractCompat` and
`FontRequest` classes from the `androidx.core.provider` package. Create
instances of these classes instead of
`https://developer.android.com/reference/android/provider/FontsContract` and
`android.graphics.fonts.FontRequest` framework classes.

> [!NOTE]
> **Note:** You *must* provide a certificate when you request fonts through the AndroidX Core library. This is applicable even for the preinstalled font providers.

#### Add AndroidX Core dependency

To use the `FontsContractCompat` and `FontRequest` classes, you must modify
your app project's classpath dependencies within your development environment.

To add AndroidX Core to your application project, add the following dependency to your app's
`build.gradle` file:

### Groovy

```groovy
dependencies {
    ...
    implementation "androidx.core:core-ktx:1.17.0"
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("androidx.core:core-ktx:1.17.0")
}
```

### Use Downloadable Fonts as resources in XML

Android 8.0 (API level 26) and AndroidX Core offer a faster and more convenient way to declare a
custom font as a resource in the XML layout. This means that there is no need to bundle the font as
an asset. You can define a custom font for your entire theme, which accelerates usability for
multiple weights and styles, such as bold, medium, or light, when provided.

1. Create a new XML file in the `res/font` folder.
2. Add a `<font-family>` root element and set the font-related attributes, as shown in the following sample XML file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
        android:fontProviderAuthority="com.example.fontprovider.authority"
        android:fontProviderPackage="com.example.fontprovider"
        android:fontProviderQuery="example font"
        android:fontProviderCerts="@array/certs">
</font-family>
```
3. Refer to the file as `@font/font_file_name` in the layout XML file. You can also use the `https://developer.android.com/reference/android/content/res/Resources#getFont(int)` method to retrieve the file programmatically, such as `getFont(R.font.font_file_name)`.

### Pre-declare fonts in the manifest

Layout inflation and resource retrieval are synchronous tasks. By default, the first attempt to
retrieve fonts triggers a request to the font provider, and therefore increases the first layout
time. To avoid the delay, you can pre-declare fonts that need to be retrieved in your manifest.
After the system retrieves the font from the provider, it is available immediately. If font
retrieval takes longer than expected, the system aborts the fetching process and uses the default
font.

To pre-declare fonts in the manifest, complete the following steps:

1. Create a resources array in `res/values/arrays.xml` and declare the fonts that you want to prefetch.

```xml
res/values/arrays.xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <array name="preloaded_fonts">
        <item>@font/font1</item>
        <item>@font/font2</item>
    </array>
</resources>
```
2. Use a `meta-data` tag to declare the resource array in your manifest.

```xml
<meta-data android:name="preloaded_fonts" android:resource="@array/preloaded_fonts" />
```

### Add certificates

When a font provider isn't preinstalled, or if you are using the AndroidX Core library, declare
the certificates the font provider is signed with. The system uses the certificates to verify the
font provider's identity.

> [!NOTE]
> **Note** : Android Studio can automatically populate the values for the Google Play services provider if you use the font selector tool in Android Studio. For more information about using Android Studio for downloading fonts, see the [Use Downloadable Fonts with Android Studio and Google Play services](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#via-android-studio) section on this page.

Perform the following steps to add certificates:

1. Create a string array with the certificate details. For more information about certificate details, refer to your font provider's documentation.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="certs">
       <item>MIIEqDCCA5CgAwIBAgIJA071MA0GCSqGSIb3DQEBBAUAMIGUMQsww...</item>
    </string-array>
</resources>
```
2. Set the `fontProviderCerts` attribute to the array.

```xml
android:fontProviderCerts="@array/certs"
```

> [!NOTE]
> **Note**: If the provider has more than one set of certificates, you can define an array of string arrays.

## Downloadable Fonts in Compose