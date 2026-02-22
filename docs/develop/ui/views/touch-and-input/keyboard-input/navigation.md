---
title: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/navigation
url: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/navigation
source: md.txt
---

# Support keyboard navigation

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.  
[Focus →](https://developer.android.com/develop/ui/compose/touch-input/focus)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

In addition to soft input methods---such as on-screen keyboards---Android supports physical keyboards attached to the device. A keyboard offers a convenient mode for text input and a way for users to navigate and interact with your app. Although most hand-held devices such as phones use touch as the primary mode of interaction, tablets and similar devices are popular, and many users like to attach keyboard accessories to them.

As more Android-powered devices offer this kind of experience, it's important that you optimize your app to support interaction through a keyboard. This document describes how you can improve navigation with a keyboard.
| **Note:** Supporting directional navigation in your app is also an important part of helping ensure your app is[accessible](https://developer.android.com/guide/topics/ui/accessibility/apps)to users who don't navigate using visual cues. Fully supporting directional navigation in your app can also help you automate[user interface testing](https://developer.android.com/tools/testing/testing_ui)with tools like[UiAutomator](https://developer.android.com/tools/help/uiautomator).

## Test your app

Users might already be able to navigate your app using a keyboard, because the Android system enables most of the necessary behaviors by default.

All interactive widgets provided by the Android framework---such as[Button](https://developer.android.com/reference/android/widget/Button)and[EditText](https://developer.android.com/reference/android/widget/EditText)---are focusable. This means users can navigate with control devices such as a D-pad or keyboard, and each widget glows or otherwise changes its appearance when it gains input focus.

To test your app, perform the following procedure:

1. Install your app on a device that offers a hardware keyboard.If you don't have a hardware device with a keyboard, connect a Bluetooth keyboard or a USB keyboard.

   You can also use the Android emulator:
   1. In the AVD Manager, either click**New Device** or select an existing profile and click**Clone**.
   2. In the window that appears, ensure**Keyboard** and**DPad**are enabled.
2. To test your app, use only the<kbd>Tab</kbd>key to navigate through your UI. Make sure each UI control gets focus as expected.

   Look for any instances in which the focus moves in an unexpected manner.
3. Start again from the beginning of your app and navigate through your UI using direction controls like the arrow keys on the keyboard. From each focusable element in your UI, press<kbd>Up</kbd>,<kbd>Down</kbd>,<kbd>Left</kbd>, and<kbd>Right</kbd>.

   Look for any instances in which the focus moves in an unexpected manner.

If you encounter any instances where navigating with the<kbd>Tab</kbd>key or direction controls doesn't do what you expect, specify where the focus must be in your layout, as discussed in the following sections.

## Handle tab navigation

When a user navigates your app using the keyboard<kbd>Tab</kbd>key, the system passes input focus between elements based on the order in which they appear in the layout. If you use a relative layout, for example, and the order of elements on the screen is different than the order in the file, then you might need to manually specify the focus order.

For example, in the following layout, two buttons are aligned to the right side, and a text field is aligned to the left of the second button. To pass focus from the first button to the text field and then to the second button, the layout needs to explicitly define the focus order for each of the focusable elements with the[`android:nextFocusForward`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusForward)attribute.  

```xml
<androidx.constraintlayout.widget.ConstraintLayout ...>
    <Button
        android:id="@+id/button1"
        android:nextFocusForward="@+id/editText1"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        ... />
    <Button
        android:id="@+id/button2"
        android:nextFocusForward="@+id/button1"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/button1"
        ... />
    <EditText
        android:id="@id/editText1"
        android:nextFocusForward="@+id/button2"
        app:layout_constraintBottom_toBottomOf="@+id/button2"
        app:layout_constraintRight_toLeftOf="@id/button2
        ...  />
    ...
</androidx.constraintlayout.widget.ConstraintLayout>
```

Now, instead of the focus moving from`button1`to`button2`and then`editText1`, it appropriately moves according to the appearance on the screen: from`button1`to`editText1`and then`button2`.

## Handle directional navigation

Users can also navigate your app using the arrow keys on a keyboard, which behaves the same as when navigating with a D-pad or trackball. The system provides a "best guess" for which view to give focus to in a given direction based on the layout of the views on screen. However, sometimes the system guesses wrong.

If the system doesn't pass focus to the appropriate view when navigating in a given direction, specify which view must receive focus with the following attributes:

- [`android:nextFocusUp`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusUp)
- [`android:nextFocusDown`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusDown)
- [`android:nextFocusLeft`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusLeft)
- [`android:nextFocusRight`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusRight)

Each attribute designates the next view to receive focus when the user navigates in that direction, as specified by the view ID. This is shown in the following example:  

```xml
<Button
    android:id="@+id/button1"
 android:nextFocusRight="@+id/button2"
    android:nextFocusDown="@+id/editText1"
    ... />
<Button
    android:id="@id/button2"
    android:nextFocusLeft="@id/button1"
    android:nextFocusDown="@id/editText1"
    ... />
<EditText
    android:id="@id/editText1"
    android:nextFocusUp="@id/button1"
    ...  />
```
| **Note:** Some Android views override the default navigation keys. For example,[`EditText`](https://developer.android.com/reference/android/widget/EditText)overrides the arrow keys to provide navigation within the inserted text.

## Additional resources

Refer to the following related resources:

- [Build accessible apps](https://developer.android.com/training/accessibility)