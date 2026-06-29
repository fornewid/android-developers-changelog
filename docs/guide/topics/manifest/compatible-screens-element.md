---
title: https://developer.android.com/guide/topics/manifest/compatible-screens-element
url: https://developer.android.com/guide/topics/manifest/compatible-screens-element
source: md.txt
---

# &lt;compatible-screens>

syntax:
:

    ```xml
    <compatible-screens>
        <screen android:screenSize=["small" | "normal" | "large" | "xlarge"]
                android:screenDensity=["ldpi" | "mdpi" | "hdpi" | "xhdpi"
                                       | "280" | "360" | "420" | "480" | "560" ] />
        ...
    </compatible-screens>
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:
:   Specifies each screen configuration with which the application is compatible. Only one instance of the`<compatible-screens>`element is allowed in the manifest, but it can contain multiple`<screen>`elements. Each`<screen>`element specifies a specific screen size-density combination with which the application is compatible.

    The Android system*doesn't* read the`<compatible-screens>`manifest element at any point. This element is informational only and is used by external services, such as Google Play, to better understand the application's compatibility with specific screen configurations and to enable filtering for users.

    Any screen configuration that*isn't* declared in this element is a screen with which the application*isn't*compatible. External services, such as Google Play, don't provide the application to devices with such screens.

    **Caution:** Normally,*you don't use this manifest element* . Using this element can dramatically reduce the potential user base for your application by preventing users from installing your application if they have a device with a screen configuration that you don't list. Use it only as a last resort, when the application absolutely doesn't work with specific screen configurations. Instead of using this element, follow the guide to[supporting multiple screens](https://developer.android.com/guide/practices/screens_support)to provide scalable support for multiple screens using alternative layouts and bitmaps for different screen sizes and densities.

    If you want to set a minimum screen size for your your application, use the[`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element)element. For example, if you want your application to be available only for large and extra-large screen devices, the`<supports-screens>`element lets you declare that your application doesn't support small and normal screen sizes. Then, external services like Google Play filter your application accordingly. You can also use the`<supports-screens>`element to declare whether the system can resize your application for different screen sizes.

    For more information about how Google Play filters applications using this and other manifest elements, see[Filters on Google Play](https://developer.android.com/google/play/filters).

child elements:
:

    `<screen>`

    :   Specifies a single screen configuration with which the application is compatible.

        At least one instance of this element must be placed inside the`<compatible-screens>`element. This element must include both the`android:screenSize`and`android:screenDensity`attributes. If you don't declare both attributes, then the element is ignored.

        Attributes:

        `android:screenSize`
        :   **Required.** Specifies the screen size for this screen configuration.

            Accepted values:

            - `small`
            - `normal`
            - `large`
            - `xlarge`

            For information about the different screen sizes, see[Screen compatibility overview](https://developer.android.com/guide/practices/screens_support#sizes).

        `android:screenDensity`
        :   **Required.** Specifies the screen density for this screen configuration.

            Accepted values:

            - `"ldpi"`(approximately 120 dpi)
            - `"mdpi"`(approximately 160 dpi)
            - `"hdpi"`(approximately 240 dpi)
            - `"xhdpi"`(approximately 320 dpi)
            - `"280"`
            - `"360"`
            - `"420"`
            - `"480"`
            - `"560"`

            For information about the different screen densities, see[Screen compatibility overview](https://developer.android.com/guide/practices/screens_support#density).

example

:   If your application is compatible with only small and normal screens, regardless of screen density, then you must specify 12`<screen>`elements, because each screen size has six different density configurations.

    You must declare each one of these. Any combination of size and density that you*don't* specify is considered a screen configuration with which your application*isn't*compatible. Here's what the manifest entry looks like if your application is compatible with only small and normal screens:  

    ```xml
    <manifest ... >
        ...
        <compatible-screens>
            <!-- all small size screens -->
            <screen android:screenSize="small" android:screenDensity="ldpi" />
            <screen android:screenSize="small" android:screenDensity="mdpi" />
            <screen android:screenSize="small" android:screenDensity="hdpi" />
            <screen android:screenSize="small" android:screenDensity="xhdpi" />
            <screen android:screenSize="small" android:screenDensity="xxhdpi" />
            <screen android:screenSize="small" android:screenDensity="xxxhdpi" />
            <!-- all normal size screens -->
            <screen android:screenSize="normal" android:screenDensity="ldpi" />
            <screen android:screenSize="normal" android:screenDensity="mdpi" />
            <screen android:screenSize="normal" android:screenDensity="hdpi" />
            <screen android:screenSize="normal" android:screenDensity="xhdpi" />
            <screen android:screenSize="normal" android:screenDensity="xxhdpi" />
            <screen android:screenSize="normal" android:screenDensity="xxxhdpi" />
        </compatible-screens>
        <application ... >
            ...
        <application>
    </manifest>
    ```

introduced in:
:   API level 9

see also:
:   [Screen compatibility overview](https://developer.android.com/guide/practices/screens_support)
:   [Filters on Google Play](https://developer.android.com/google/play/filters)