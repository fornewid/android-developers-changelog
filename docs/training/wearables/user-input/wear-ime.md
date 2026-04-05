---
title: https://developer.android.com/training/wearables/user-input/wear-ime
url: https://developer.android.com/training/wearables/user-input/wear-ime
source: md.txt
---

Wear OS supports input methods beyond voice by extending the
Android input method editor (IME) framework. The IME framework provides support
for virtual, on-screen keyboards that let users input text in the form of
keyclicks, handwriting, or gestures.


Wear OS users can choose between various input options from Remote Input. These options include:

- Dictation
- Emoji
- Canned responses
- Smart Reply
- Default IME

![](https://developer.android.com/static/wear/images/new_input_methods.png)

Create an input method for Wear

The Android platform provides a standard framework for creating IMEs. To create
a Wear-OS-specific IME, you need to optimize your IME for a wearable's limited screen size.

### Wear-OS-specific IME filters

To learn how to create an input method for Wear OS, follow the guide to
[create an input method](https://developer.android.com/guide/topics/text/creating-input-method) on handsets.
Then add the Google Play filters in the following sections to your manifest file to make it a Wear-OS-specific IME.

#### API level

If you are developing an IME for Wear OS, remember that the
feature is supported only on Android 6.0 (API level 23) and higher.
To ensure that your IME can be installed only on wearables that support input
methods beyond voice, add the following to your app's manifest:  

```xml
<uses-sdk android:minSdkVersion="23" />
```

#### Device feature sets

To control how your app is filtered from devices that don't support
Wear OS IMEs, such as iPhones, add the following to your app's manifest:  

```xml
<uses-feature android:required="true" android:name="android.hardware.type.watch" />
```

## Invoke an input method

Wear OS provides user settings on the watch that let the user enable multiple
IMEs from the list of installed IMEs. Once the user enables your IME, they
can invoke your IME from the following places:

- A notification or an app using the [RemoteInput](https://developer.android.com/reference/androidx/core/app/RemoteInput) API.
- Wear OS apps with an [`EditText`](https://developer.android.com/reference/android/widget/EditText) field. Touching a text field places the cursor in the field and automatically displays the IME on focus.

## General IME considerations

Here are some things to consider when implementing IME for Wear:

- **Set a default action.**


  [`RemoteInput`](https://developer.android.com/reference/androidx/core/app/RemoteInput)
  and Wear OS apps expect only single-line text entry. Always use the <kbd>Enter</kbd> key to trigger a call
  to
  [`sendDefaultEditorAction`](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#sendDefaultEditorAction(boolean)),
  which causes the app to dismiss the keyboard and continue on to the next step or action.
- **Use a full-screen-mode IME.**

  Input methods on Wear OS cover most of the screen, leaving very little of the
  app visible. Using full-screen mode offers an optimal user experience regardless of the
  app UI. In full-screen mode, an
  [`ExtractedText`](https://developer.android.com/reference/android/view/inputmethod/ExtractedText)
  provides a mirrored view of the text field being edited and can be styled to blend with the
  rest of the input method UI. For more details on full-screen mode, see
  [`InputMethodService`](https://developer.android.com/reference/android/inputmethodservice/InputMethodService).
- **Handle `InputType` flags.**

  At a minimum, for privacy reasons, handle the
  [`InputType`](https://developer.android.com/reference/android/text/InputType)
  flag `TYPE_TEXT_VARIATION_PASSWORD` in your IME. When your IME is in
  password mode, make sure that your keyboard is optimized for single key press,
  meaning that auto spelling correction, auto completion, and gesture input are disabled.
  Most importantly, the keyboard in password mode must support American Standard Code for Information Interchange (ASCII) symbols
  regardless of the input language. For more details, see
  [Specify the input method type](https://developer.android.com/training/keyboard-input/style).
- **Provide a key for switching to the next input method.**

  Android lets users switch between all IMEs supported by the platform.
  In your IME implementation, set the boolean
  [`supportsSwitchingToNextInputMethod`](https://developer.android.com/guide/topics/text/creating-input-method#Switching) to `true`.
  This lets your IME support the switching mechanism so that apps can switch to the next
  platform-supported IME. To learn more about how to implement switching between IMEs, see
  [Switching among IME subtypes](https://developer.android.com/guide/topics/text/creating-input-method#Switching).