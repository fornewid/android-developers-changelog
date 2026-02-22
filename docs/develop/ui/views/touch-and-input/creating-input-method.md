---
title: https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method
url: https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method
source: md.txt
---

An input method editor (IME) is a user control that lets users enter text. Android provides an
extensible input-method framework that lets applications provide users alternative input methods,
such as on-screen keyboards or speech input. After installing the IMEs, the user can select one from
the system settings and use it across the entire system. Only one IME can be enabled at a time.

To add an IME to the Android system, create an Android application containing a class that
extends
[InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService).
In addition, you usually create a "settings" activity that passes options to the IME service. You
can also define a settings UI that's displayed as part of the system settings.

This page covers the following topics:

- [The IME lifecycle](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#InputMethodLifecycle)
- [Declaring IME components in the application manifest](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#DefiningIME)
- [The IME API](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#IMEAPI)
- [Designing an IME UI](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#IMEUI)
- [Sending text from an IME to an application](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#SendText)
- [Working with IME subtypes](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#IMESubTypes)
- [Other IME considerations](https://developer.android.com/develop/ui/views/touch-and-input/creating-input-method#GeneralDesign)

If you haven't worked with IMEs, read the introductory article
[On-screen Input Methods](http://android-developers.blogspot.com/2009/04/updating-applications-for-on-screen.html)
first.
| **Note:** Beginning with Android 11, the platform lets IMEs display autofill suggestions inline, instead of using a pulldown menu. For more information about how autofill services can support this functionality, read about [how to integrate autofill with your IME](https://developer.android.com/guide/topics/text/ime-autofill).

## The IME lifecycle

The following diagram describes the lifecycle of an IME:
![An image showing the life cycle of an IME.](https://developer.android.com/static/resources/articles/images/inputmethod_lifecycle_image.png) **Figure 1.** The lifecycle of an IME.

The following sections describe how to implement the UI and code associated with an IME that
follows this lifecycle.

## Declare IME components in the manifest

In the Android system, an IME is an Android application that contains a special IME service. The
application's manifest file must declare the service, request the necessary permissions, provide an
intent filter that matches the action `action.view.InputMethod`, and provide metadata
that defines characteristics of the IME. In addition, to provide a settings interface that lets the
user modify the behavior of the IME, you can define a "settings" activity that can be launched from
System Settings.

The following snippet declares an IME service. It requests the permission
[BIND_INPUT_METHOD](https://developer.android.com/reference/android/Manifest.permission#BIND_INPUT_METHOD)
to let the service connect the IME to the system, sets up an intent filter that matches the action
`android.view.InputMethod`, and defines metadata for the IME:  

```xml
<!-- Declares the input method service. -->
<service android:name="FastInputIME"
    android:label="@string/fast_input_label"
    android:permission="android.permission.BIND_INPUT_METHOD">
    <intent-filter>
        <action android:name="android.view.InputMethod" />
    </intent-filter>
    <meta-data android:name="android.view.im"
               android:resource="@xml/method" />
</service>
```

The next snippet declares the settings activity for the IME. It has an intent filter for
[ACTION_MAIN](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN) that
indicates that this activity is the main entry point for the IME application:  

```xml
<!-- Optional: an activity for controlling the IME settings. -->
<activity android:name="FastInputIMESettings"
    android:label="@string/fast_input_settings">
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
    </intent-filter>
</activity>
```

You can also provide access to the IME's settings directly from its UI.

## The input method API

Classes specific to IMEs are found in the
[android.inputmethodservice](https://developer.android.com/reference/android/inputmethodservice/package-summary)
and
[android.view.inputmethod](https://developer.android.com/reference/android/view/inputmethod/package-summary)
packages. The [KeyEvent](https://developer.android.com/reference/android/view/KeyEvent) class is
important for handling keyboard characters.

The central part of an IME is a service component---a class that extends
`InputMethodService`. In addition to implementing the normal service lifecycle, this
class has callbacks for providing your IME's UI, handling user input, and delivering text to the
field that has focus. By default, the `InputMethodService` class provides most of the
implementation for managing the state and visibility of the IME and communicating with the current
input field.

The following classes are also important:

[BaseInputConnection](https://developer.android.com/reference/android/view/inputmethod/BaseInputConnection)
:
    Defines the communication channel from an
    [InputMethod](https://developer.android.com/reference/android/view/inputmethod/InputMethod)
    back to the application that is receiving its input. You use it to read text around the
    cursor, commit text to the text box, and send raw key events to the application.
    Applications must extend this class rather than implementing the base interface
    [InputConnection](https://developer.android.com/reference/android/view/inputmethod/InputConnection).

[KeyboardView](https://developer.android.com/reference/android/inputmethodservice/KeyboardView)
:
    An extension of [View](https://developer.android.com/reference/android/view/View) that
    renders a keyboard and responds to user input events. The keyboard layout is specified by an
    instance of
    [Keyboard](https://developer.android.com/reference/android/inputmethodservice/Keyboard),
    which you can define in an XML file.

## Design the input method UI

There are two main visual elements for an IME: the **input** view and the
**candidates** view. You only have to implement the elements that are relevant to the
input method you're designing.

### Input view

The input view is the UI where the user inputs text in the form of keyclicks, handwriting, or
gestures. When the IME is displayed for the first time, the system calls the
[onCreateInputView()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onCreateInputView())
callback. In your implementation of this method, create the layout you want to display in the IME
window and return the layout to the system. The following snippet shows an example of implementing
the `onCreateInputView()` method:

### Kotlin

```kotlin
override fun onCreateInputView(): View {
    return layoutInflater.inflate(R.layout.input, null).apply {
        if (this is MyKeyboardView) {
            setOnKeyboardActionListener(this@MyInputMethod)
            keyboard = latinKeyboard
        }
    }
}
```

### Java

```java
@Override
public View onCreateInputView() {
    MyKeyboardView inputView =
        (MyKeyboardView) getLayoutInflater().inflate(R.layout.input, null);

    inputView.setOnKeyboardActionListener(this);
    inputView.setKeyboard(latinKeyboard);

    return inputView;
}
```

In this example, `MyKeyboardView` is an instance of a custom implementation of
`KeyboardView` that renders a `Keyboard`.

### Candidates view

The candidates view is the UI where the IME displays potential word corrections or suggestions
for the user to select. In the IME lifecycle, the system calls
[onCreateCandidatesView()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onCreateCandidatesView())
when it's ready to display the candidates view. In your implementation of this method, return a
layout that shows word suggestions, or return null if you don't want to show anything. A null
response is the default behavior, so you don't have to implement this if you don't provide
suggestions.

### UI design considerations

This section describes some UI design considerations for IMEs.

#### Handle multiple screen sizes

The UI for your IME must be able to scale for different screen sizes and handle both landscape
and portrait orientations. In non-fullscreen IME mode, leave sufficient space for the application to
show the text field and any associated context, so that no more than half the screen is occupied by
the IME. In fullscreen IME mode, this isn't an issue.

#### Handle different input types

Android text fields let you set a specific input type, such as free-form text, numbers, URLs,
email addresses, and search strings. When you implement a new IME, detect the input type of each
field and provide the appropriate interface for it. However, you don't have to set up your IME to
check whether the user enters valid text for the input type. This is the responsibility of the
application that owns the text field.

For example, here is the interface that the Latin IME provides for the Android platform text
input:
![An image showing a text input on a Latin IME](https://developer.android.com/static/images/ui/text_input.png) **Figure 2.** Latin IME text input.

And here here is the interface that the Latin IME provides for the Android platform
numeric input:
![An image showing a numeric input on a Latin IME](https://developer.android.com/static/images/ui/numeric_input.png) **Figure 3.** Latin IME numeric input.

When an input field receives focus and your IME starts, the system calls
[onStartInputView()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onStartInputView(android.view.inputmethod.EditorInfo, boolean)),
passing in an
[EditorInfo](https://developer.android.com/reference/android/view/inputmethod/EditorInfo) object
that contains details about the input type and other attributes of the text field. In this object,
the
[inputType](https://developer.android.com/reference/android/view/inputmethod/EditorInfo#inputType)
field contains the text field's input type.

The `inputType` field is an `int` that contains bit patterns for various
input type settings. To test it for the text field's input type, mask it with the constant
[TYPE_MASK_CLASS](https://developer.android.com/reference/android/text/InputType#TYPE_MASK_CLASS),
like this:  

### Kotlin

```kotlin
inputType and InputType.TYPE_MASK_CLASS
```

### Java

```java
inputType & InputType.TYPE_MASK_CLASS
```

The input type bit pattern can have one of several values, including:

[TYPE_CLASS_NUMBER](https://developer.android.com/reference/android/text/InputType#TYPE_CLASS_NUMBER)
:   A text field for entering numbers. As illustrated in figure 3, the Latin IME displays a
    number pad for fields of this type.

[TYPE_CLASS_DATETIME](https://developer.android.com/reference/android/text/InputType#TYPE_CLASS_DATETIME)
:   A text field for entering a date and time.

[TYPE_CLASS_PHONE](https://developer.android.com/reference/android/text/InputType#TYPE_CLASS_PHONE)
:   A text field for entering telephone numbers.

[TYPE_CLASS_TEXT](https://developer.android.com/reference/android/text/InputType#TYPE_CLASS_TEXT)
:   A text field for entering any supported characters.

These constants are described in more detail in the reference documentation for
[InputType](https://developer.android.com/reference/android/text/InputType).

The `inputType` field can contain other bits that indicate a variant of the text field
type, such as:

[TYPE_TEXT_VARIATION_PASSWORD](https://developer.android.com/reference/android/text/InputType#TYPE_TEXT_VARIATION_PASSWORD)
:   A variant of `TYPE_CLASS_TEXT` for entering passwords. The input method displays
    dingbats instead of the actual text.

[TYPE_TEXT_VARIATION_URI](https://developer.android.com/reference/android/text/InputType#TYPE_TEXT_VARIATION_URI)
:   A variant of `TYPE_CLASS_TEXT` for entering web URLs and other Uniform Resource
    Identifiers (URIs).

[TYPE_TEXT_FLAG_AUTO_COMPLETE](https://developer.android.com/reference/android/text/InputType#TYPE_TEXT_FLAG_AUTO_COMPLETE)
:   A variant of `TYPE_CLASS_TEXT` for entering text that the application
    auto-completes from a dictionary, search, or other facility.

Mask `inputType` with the appropriate constant when you test for these variants. The
available mask constants are listed in the reference documentation for `InputType`.
| **Caution:** In your own IME, handle text correctly when you send it to a password field. Hide the password in your UI, both in the input view and in the candidates view. Don't store passwords on a device. To learn more, see [Security tips](https://developer.android.com/guide/practices/security).

## Send text to the application

As the user inputs text with your IME, you can send text to the application by sending individual
key events or by editing the text around the cursor in the application's text field. In either case,
use an instance of `InputConnection` to deliver the text. To get this instance, call
[InputMethodService.getCurrentInputConnection()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#getCurrentInputConnection()).

### Edit the text around the cursor

When you're handling the editing of existing text, some useful methods in
`BaseInputConnection` are the following:


[getTextBeforeCursor()](https://developer.android.com/reference/android/view/inputmethod/BaseInputConnection#getTextBeforeCursor(int, int))
:   Returns a [CharSequence](https://developer.android.com/reference/java/lang/CharSequence)
    containing the number of requested characters before the current cursor position.


[getTextAfterCursor()](https://developer.android.com/reference/android/view/inputmethod/BaseInputConnection#getTextAfterCursor(int, int))
:   Returns a `CharSequence` containing the number of requested characters following
    the current cursor position.


[deleteSurroundingText()](https://developer.android.com/reference/android/view/inputmethod/BaseInputConnection#deleteSurroundingText(int, int))
:   Deletes the specified number of characters before and following the current cursor position.


[commitText()](https://developer.android.com/reference/android/view/inputmethod/BaseInputConnection#commitText(java.lang.CharSequence, int))
:   Commits a `CharSequence` to the text field and sets a new cursor position.

For example, the following snippet shows how to replace the four characters to the left of the
cursor with the text "Hello!":  

### Kotlin

```kotlin
currentInputConnection.also { ic: InputConnection ->
    ic.deleteSurroundingText(4, 0)
    ic.commitText("Hello", 1)
    ic.commitText("!", 1)
}
```

### Java

```java
InputConnection ic = getCurrentInputConnection();
ic.deleteSurroundingText(4, 0);
ic.commitText("Hello", 1);
ic.commitText("!", 1);
```

### Support composing text before committing

If your IME predicts text or requires multiple steps to compose a glyph or word, you can show the
progress in the text field until the user commits the word, and then you can replace the partial
composition with the completed text. You can give special treatment to the text by adding a
*span* to it when you pass it to
[setComposingText()](https://developer.android.com/reference/android/view/inputmethod/InputConnection#setComposingText(java.lang.CharSequence, int)).

The following snippet demonstrates how to show progress in a text field:  

### Kotlin

```kotlin
currentInputConnection.also { ic: InputConnection ->
    ic.setComposingText("Composi", 1)
    ic.setComposingText("Composin", 1)
    ic.commitText("Composing ", 1)
}
```

### Java

```java
InputConnection ic = getCurrentInputConnection();
ic.setComposingText("Composi", 1);
ic.setComposingText("Composin", 1);
ic.commitText("Composing ", 1);
```

### Intercept hardware key events

Even though the input method window doesn't have explicit focus, it receives hardware key events
first and can consume them or forward them to the application. For example, you might want to
consume the directional keys to navigate within your UI for candidate selection during composition.
You might also want to trap the back key to dismiss any dialogs originating from the input method
window.

To intercept hardware keys, override
[onKeyDown()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onKeyDown(int, android.view.KeyEvent))
and
[onKeyUp()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onKeyUp(int, android.view.KeyEvent)).

Call the `super()` method for keys you don't want to handle yourself.

## Create an IME subtype

Subtypes let the IME expose multiple input modes and languages supported by an IME. A subtype can
represent the following:

- A locale, such as en_US or fr_FR
- An input mode, such as voice, keyboard, or handwriting
- Other input styles, forms, or properties specific to the IME, such as 10-key or QWERTY keyboard layouts

The mode can be any text, such as "keyboard" or "voice". A subtype can also expose a combination
of these.

Subtype information is used for an IME switcher dialog that's available from the notification bar
and for IME settings. The information also lets the framework bring up a specific subtype of an IME
directly. When you build an IME, use the subtype facility, because it helps the user identify and
switch between different IME languages and modes.

Define subtypes in one of the input method's XML resource files, using the
`<subtype>` element. The following code snippet defines an IME with two subtypes: a
keyboard subtype for the US English locale and another keyboard subtype for the French language
locale for France:  

```xml
<input-method xmlns:android="http://schemas.android.com/apk/res/android"
        android:settingsActivity="com.example.softkeyboard.Settings"
        android:icon="@drawable/ime_icon">
    <subtype android:name="@string/display_name_english_keyboard_ime"
            android:icon="@drawable/subtype_icon_english_keyboard_ime"
            android:languageTag="en-US"
            android:imeSubtypeMode="keyboard"
            android:imeSubtypeExtraValue="somePrivateOption=true" />
    <subtype android:name="@string/display_name_french_keyboard_ime"
            android:icon="@drawable/subtype_icon_french_keyboard_ime"
            android:languageTag="fr-FR"
            android:imeSubtypeMode="keyboard"
            android:imeSubtypeExtraValue="someVariable=30,someInternalOption=false" />
    <subtype android:name="@string/display_name_german_keyboard_ime" ... />
</input-method>
```

To make sure your subtypes are labeled correctly in the UI, use \`%s\` to get a subtype label that
is the same as the subtype's locale label. This is demonstrated in the next two code snippets. The
first snippet shows part of the input method's XML file:  

```xml
<subtype
    android:label="@string/label_subtype_generic"
    android:imeSubtypeLocale="en_US"
    android:icon="@drawable/icon_en_us"
    android:imeSubtypeMode="keyboard" />
```

The next snippet is part of the IME's `strings.xml` file. The string resource
`label_subtype_generic`, which is used by the input method UI definition to set the
subtype's label, is defined as the following:  

```xml
<string name="label_subtype_generic">%s</string>
```

This setting causes the subtype's display name to match the locale setting. For example, in any
English locale, the display name is "English (United States)."

### Choose IME subtypes from the notification bar

The Android system manages all subtypes exposed by all IMEs. IME subtypes are treated as modes of
the IME they belong to. The user can navigate from the notification bar or the Settings app to a
menu of available IME subtypes, as shown in the following figure:
![An image showing the Languages & input System menu](https://developer.android.com/static/images/ui/languages_and_input.png) **Figure 4.** The **Languages \& input** system menu.

### Choose IME subtypes from System Settings

The user can also control how subtypes are used in the **Language \& input** settings panel
in the system settings:
![An image showing the Languages selection menu](https://developer.android.com/static/images/ui/languages.png) **Figure 5.** The **Languages** system menu

## Switch among IME subtypes

You can let users easily switch among IME subtypes by providing a switching key, such as the
globe-shaped language icon on the keyboard. This improves the keyboard's usability and is convenient
for the user. To enable this switching, perform the following steps:

1. Declare `supportsSwitchingToNextInputMethod = "true"` in the input method's XML resource files. Your declaration must look similar to the following code snippet:  

   ```xml
   <input-method xmlns:android="http://schemas.android.com/apk/res/android"
           android:settingsActivity="com.example.softkeyboard.Settings"
           android:icon="@drawable/ime_icon"
           android:supportsSwitchingToNextInputMethod="true">
   ```
2. Call the [shouldOfferSwitchingToNextInputMethod()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#shouldOfferSwitchingToNextInputMethod()) method.
3. If the method returns true, display a switching key.
4. When the user taps the switching key, call [switchToNextInputMethod()](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#switchToNextInputMethod(boolean)), passing false. A value of false tells the system to treat all subtypes equally, regardless of what IME they belong to. Specifying true requires the system to cycle through subtypes in the current IME.

## General IME considerations

Here are other things to consider as you implement your IME:

- Provide a way for users to set options directly from the IME's UI.
- Provide a way for users to switch to a different IME directly from the input method UI, because multiple IMEs might be installed on the device.
- Bring up the IME's UI quickly. Preload or load on demand any large resources so that users see the IME as soon as they tap a text field. Cache resources and views for subsequent invocations of the input method.
- Release large memory allocations immediately after the input method window is hidden, so that applications have sufficient memory to run. Use a delayed message to release resources if the IME is hidden for a few seconds.
- Make sure users can enter as many characters as possible for the language or locale associated with the IME. Users might use punctuation in passwords or user names, so your IME must provide many different characters to let users enter a password and access the device.