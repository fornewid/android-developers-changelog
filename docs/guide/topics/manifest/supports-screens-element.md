---
title: https://developer.android.com/guide/topics/manifest/supports-screens-element
url: https://developer.android.com/guide/topics/manifest/supports-screens-element
source: md.txt
---

# &lt;supports-screens>

syntax:
:

    ```xml
    <supports-screens android:resizeable=["true"| "false"]
                      android:smallScreens=["true" | "false"]
                      android:normalScreens=["true" | "false"]
                      android:largeScreens=["true" | "false"]
                      android:xlargeScreens=["true" | "false"]
                      android:anyDensity=["true" | "false"]
                      android:requiresSmallestWidthDp="integer"
                      android:compatibleWidthLimitDp="integer"
                      android:largestWidthLimitDp="integer"/>
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Lets you specify the screen sizes your application supports and enable screen compatibility mode for screens larger than what your application supports. It's important that you always use this element in your application to specify the screen sizes your application supports.

    **Note:** Screen compatibility mode**isn't** a mode you want your application to run in. It causes pixelation and blurring in your UI due to zooming. The proper way to make your application work well on large screens is to follow the[Screen compatibility overview](https://developer.android.com/guide/practices/screens_support)and provide alternative layouts for different screen sizes.

    An application "supports" a given screen size if it resizes properly to fill the entire screen. Normal resizing applied by the system works well for most applications, and you don't have to do any extra work to make your application work on screens larger than a handset device.

    However, it's often important that you optimize your application's UI for different screen sizes by providing[alternative layout resources](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources). For instance, you might want to modify the layout of an activity when it is on a tablet compared to when running on a handset device.

    However, if your application doesn't work well when resized to fit different screen sizes, you can use the attributes of the`<supports-screens>`element to control whether your application is distributed only to smaller screens or has its UI scaled up, or "zoomed," to fit larger screens using the system's[screen compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode).

    If you don't design for larger screen sizes and the normal resizing doesn't achieve the appropriate results, screen compatibility mode scales your UI by emulating a*normal*size screen and medium density. It then zooms in so that it fills the entire screen. Be aware that this causes pixelation and blurring of your UI, so it's better if you optimize your UI for large screens.

    **Note:** Android 3.2 introduced new attributes:`android:requiresSmallestWidthDp`,`android:compatibleWidthLimitDp`, and`android:largestWidthLimitDp`. If you're developing your application for Android 3.2 and higher, use these attributes to declare your screen size support instead of the attributes based on generalized screen sizes.

    ##### About screen compatibility mode

    Screen compatibility mode is a last resort for apps that aren't properly designed to take advantage of larger screen sizes. This is not a mode you want your app to run in, because it can offer a poor user experience. There are two versions of screen compatibility mode based on the device version the app runs on.

    On Android versions 1.6 to 3.1, the system runs your application in a "postage stamp" window. It emulates a 320dp x 480dp screen with a black border that fills the remaining area of the screen.

    On Android 3.2 and up, the system draws the layout as it does on a 320dp x 480dp screen, then scales it up to fill the screen. This often causes artifacts such as blurring and pixelation in your UI.

    For more information about how to properly support different screen sizes so that you can avoid using screen compatibility mode with your application, read[Screen compatibility overview](https://developer.android.com/guide/practices/screens_support).

attributes:
:

    `android:resizeable`
    :   Indicates whether the application is resizeable for different screen sizes. This attribute is`"true"`by default. If set to`"false"`, the system runs your application in[screen compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode)on large screens.

        <br />

        **This attribute is deprecated**. It was introduced to help applications transition from Android 1.5 to 1.6, when support for multiple screens was first introduced. Don't use it.

    `android:smallScreens`
    :   Indicates whether the application supports "small" screen form-factors. A small screen is defined as one with a smaller aspect ratio than the "normal" screen, or traditional HVGA screen. An application that doesn't support small screens*isn't available* for small screen devices from external services, such as Google Play, because there is little the platform can do to make such an application work on a smaller screen. This is`"true"`by default.

    `android:normalScreens`
    :   Indicates whether an application supports the "normal" screen form-factors. Traditionally this is an HVGA medium density screen, but WQVGA low density and WVGA high density are also considered to be normal. This attribute is`"true"`by default.

    `android:largeScreens`

    :   Indicates whether the application supports "large" screen form-factors. A large screen is defined as a screen that is significantly larger than a "normal" handset screen. Thus it might require some special care on the application's part to make good use of it, though it might rely on resizing by the system to fill the screen.The default value for this varies between some versions, so it's better if you explicitly declare this attribute. Beware that setting it to`"false"`generally enables[screen compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode).

    `android:xlargeScreens`

    :   Indicates whether the application supports "extra-large" screen form-factors. An extra-large screen is defined as a screen that is significantly larger than a "large" screen, such as a tablet or something even larger. It might require special care on the application's part to make good use of it, though it might rely on resizing by the system to fill the screen.The default value for this varies between some versions, so it's better if you explicitly declare this attribute. Beware that setting it to`"false"`generally enables[screen compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode).

        This attribute was introduced in API level 9.

    `android:anyDensity`

    :   Indicates whether the application includes resources to accommodate any screen density.For applications that support Android 1.6 (API level 4) and higher, this is`"true"`by default.*Don't* set it to`"false"`unless you're absolutely certain that it's necessary for your application to work. The only time it might be necessary to disable this is if your app directly manipulates bitmaps. For more information, see the[Screen compatibility overview](https://developer.android.com/guide/practices/screens_support#DensityConsiderations).

    `android:requiresSmallestWidthDp`
    :   Specifies the minimum`smallestWidth`required for the app. The`smallestWidth`is the shortest dimension of the screen space, in`dp`units, that must be available to your application UI. That is, it is the shortest of the available screen's two dimensions.

        <br />

        For a device to be considered compatible with your application, the device's`smallestWidth`must be equal to or greater than this value. Usually, the value you supply for this is the "smallest width" that your layout supports, regardless of the screen's current orientation.

        For example, a typical handset screen has a`smallestWidth`of 320dp, a 7-inch tablet has a`smallestWidth`of 600dp, and a 10-inch tablet has a`smallestWidth`of 720dp. These values are generally the`smallestWidth`because they are the shortest dimension of the screen's available space.

        The size against which your value is compared takes into account screen decorations and system UI. For example, if the device has some persistent UI elements on the display, the system declares the device's`smallestWidth`as one that is smaller than the actual screen size, because those are screen pixels not available for your UI.

        If your application properly resizes for smaller screen sizes, down to the "small" size or a minimum width of 320dp, you don't need to use this attribute. Otherwise, use a value for this attribute that matches the smallest value used by your application for the[smallest screen width qualifier](https://developer.android.com/guide/topics/resources/providing-resources#SmallestScreenWidthQualifier)(`sw<N>dp`).

        **Caution:**The Android system doesn't pay attention to this attribute, so it doesn't affect how your application behaves at runtime. Instead, it is used to enable filtering for your application on services such as Google Play. However, Google Play currently doesn't support this attribute for filtering on Android 3.2, so continue using the other size attributes if your application doesn't support small screens.

        This attribute was introduced in API level 13.

    `android:compatibleWidthLimitDp`
    :   This attribute lets you enable[screen compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode)as a user-optional feature by specifying the maximum "smallest screen width" for which your application is designed. If the smallest side of a device's available screen is greater than your value here, users can still install your application but are offered to run it in screen compatibility mode.

        <br />

        By default, screen compatibility mode is disabled, and your layout resizes to fit the screen as usual. A button is available in the system bar that lets the user toggle screen compatibility mode.

        If your application is compatible with all screen sizes and its layout properly resizes, you don't need to use this attribute.

        **Note:** Currently, screen compatibility mode emulates only handset screens with a 320dp width, so screen compatibility mode isn't applied if your value for`android:compatibleWidthLimitDp`is larger than`320`.

        This attribute was introduced in API level 13.

    `android:largestWidthLimitDp`
    :   This attribute lets you force-enable[screen compatibility mode](https://developer.android.com/guide/topics/manifest/supports-screens-element#compat-mode)by specifying the maximum "smallest screen width" for which your application is designed. If the smallest side of a device's available screen is greater than your value here, the application runs in screen compatibility mode, with no way for the user to disable it.

        If your application is compatible with all screen sizes and its layout properly resizes, you don't need to use this attribute. Otherwise, first consider using the[`android:compatibleWidthLimitDp`](https://developer.android.com/guide/topics/manifest/supports-screens-element#compatibleWidth)attribute. Use the`android:largestWidthLimitDp`attribute only when your application is functionally broken when resized for larger screens, and screen compatibility mode is the only way that your application can be used.

        **Note:** Currently, screen compatibility mode emulates only handset screens with a 320dp width, so screen compatibility mode isn't applied if your value for`android:largestWidthLimitDp`is larger than`320`.

        This attribute was introduced in API level 13.

introduced in:
:   API level 4

see also:
:
    - [Screen compatibility overview](https://developer.android.com/guide/practices/screens_support)
    - [DisplayMetrics](https://developer.android.com/reference/android/util/DisplayMetrics)