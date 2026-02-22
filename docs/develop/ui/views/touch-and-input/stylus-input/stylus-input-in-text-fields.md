---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/stylus-input-in-text-fields
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/stylus-input-in-text-fields
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with a stylus in Compose. [Stylus input in text fields →](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/stylus-input-in-text-fields) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

Android 14 (API level 34) and higher enable users to write into any text input
field in any app using a stylus. Android text entry fields, including
[`EditText`](https://developer.android.com/reference/kotlin/android/widget/EditText) components and
[`WebView`](https://developer.android.com/reference/kotlin/android/webkit/WebView) text widgets, support
stylus input by default.

However, if your app requires custom text input fields (see [Custom text
editors](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors)) or
has a complex layout with text entry fields overlaying a drawing surface, you'll
need to customize your app.
Your browser doesn't support the video tag. **Figure 1.** Handwritten input with a stylus.

## `EditText`

Stylus handwriting is enabled for all `EditText` fields by default on Android 14
and higher. Handwriting mode is started for an `EditText` when a stylus motion
event is detected within the handwriting bounds of the view.

The handwriting bounds include 40 dp of vertical padding and 10 dp of horizontal
padding around the view. Adjust the handwriting bounds with
[`setHandwritingBoundsOffsets()`](https://developer.android.com/reference/kotlin/android/view/View#sethandwritingboundsoffsets).
Disable handwriting with
[`setAutoHandwritingEnabled(false)`](https://developer.android.com/reference/kotlin/android/view/View#setautohandwritingenabled).
![Input field with surrounding rectangle indicating the bounds for detection of stylus motion events.](https://developer.android.com/static/images/develop/ui/compose/touch-input/stylus-input/shared/edittext_handwriting_bounds.png) **Figure 2.** Handwriting bounds of `EditText` fields. **Note:** Stylus handwriting is not supported for `EditText` fields that have the password input type, for example:
|
| ```xml
| <EditText
|     ...
|     android:inputType="textPassword"
|     ... />
| ```
|
| See [`android:inputType`](https://developer.android.com/reference/android/widget/TextView#attr_android:inputType).

## Input delegation

Apps can display placeholder UI elements that appear to be text input fields but
are actually just static UI elements with no text input capability. Search
fields are a common example. Tapping the static UI element triggers a transition
to a new UI that contains a functional text input field focused for input.
Your browser doesn't support the video tag. **Figure 3.** Input delegation from static UI element to text input field.

### Stylus input delegation

Use the handwriting delegation APIs to support stylus handwriting input for
placeholder input fields (see
[`setHandwritingDelegatorCallback()`](https://developer.android.com/reference/kotlin/android/view/View#sethandwritingdelegatorcallback)
and
[`setIsHandwritingDelegate()`](https://developer.android.com/reference/kotlin/android/view/View#setishandwritingdelegate)).
The placeholder UI element is configured to delegate handwriting to a functional
input field, for example:

### Kotlin

```kotlin
if (Build.VERSION.SDK_INT >= 34) {
    placeholderInputField.setHandwritingDelegatorCallback {
        showAndFocusDelegateInputField()
    }
    delegateInputField.setIsHandwritingDelegate(true)
}
```

### Java

```java
if (Build.VERSION.SDK_INT >= 34) {
    placeholderInputField.setHandwritingDelegatorCallback(this::showAndFocusInputFieldDelegate);
    delegateInputField.setIsHandwritingDelegate(true);
}
```

Stylus motion over the placeholder text input field view invokes the callback.
The callback triggers the UI transition to show and focus the functional input
field. The callback implementation is typically the same as the implementation
for a click listener on the placeholder element. When the functional input field
creates an
[`InputConnection`](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputConnection),
stylus handwriting mode starts.
Your browser doesn't support the video tag. **Figure 4.** Stylus input delegation from static UI element to text input field.

### Material Design

The
[`com.google.android.material.search`](https://developer.android.com/reference/com/google/android/material/search/package-summary)
library provides the
[`SearchBar`](https://developer.android.com/reference/com/google/android/material/search/SearchBar) and
[`SearchView`](https://developer.android.com/reference/com/google/android/material/search/SearchView) classes
to facilitate implementation of the placeholder UI pattern.

Placeholder and functional search views are linked with
[`setUpWithSearchBar()`](https://developer.android.com/reference/com/google/android/material/search/SearchView#setupWithSearchBar(com.google.android.material.search.SearchBar)).

Handwriting delegation is configured in the Material library with no additional
development required in your app.

## Overlap with drawing surfaces

If your app has a drawing surface with a text field overlaying the surface, you
may need to disable stylus handwriting to allow the user to draw. See
[`setAutoHandwritingEnabled()`](https://developer.android.com/reference/kotlin/android/view/View#setautohandwritingenabled).

## Testing

Stylus handwriting is supported on Android 14 and higher devices with a
compatible stylus input device and an [input method
editor](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method) (IME) that
supports the Android 14 stylus handwriting APIs.

If you don't have a stylus input device, simulate stylus input on any device
with root access (including emulators) using the following Android Debug Bridge
(adb) commands:


    // Android 14
    adb shell setprop persist.debug.input.simulate_stylus_with_touch true && adb shell stop && adb shell start

    // Android 15 and higher
    // Property takes effect after screen reconfiguration such as orientation change.
    adb shell setprop debug.input.simulate_stylus_with_touch true

Use the Gboard beta for testing if you are using a device that doesn't support
stylus.

## Additional resources

- Material Design --- [Text fields](https://m3.material.io/components/text-fields/overview)
- [Custom text editors](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors)