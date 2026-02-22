---
title: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input
url: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn about touch and input in Compose.  
[Touch and input →](https://developer.android.com/develop/ui/compose/touch-input)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

The Android system shows an on-screen keyboard---known as a
*soft input method*---when a text field in your UI receives focus.
To provide the best user experience, you can specify characteristics
about the type of input you expect, such as a
phone number or email address, and how the input method must behave, such as
performing autocorrect for spelling mistakes.

In addition to the on-screen input methods, Android supports hardware keyboards, so it's
also important to optimize your app to support attached keyboards.

These topics and more are discussed in the following documentation.

## Lessons

**[Specify the input method type](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/style)**
:   Learn how to show certain soft input methods, such as those designed for phone numbers, web
    addresses, or other formats. Also, learn how to specify characteristics such
    as spelling suggestion behavior and action buttons such as **Done** or **Next**.

**[Handle input method visibility](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/visibility)**
:   Learn how to specify when to show the soft input method and how
    your layout must adjust to the reduced screen space.

**[Support keyboard navigation](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/navigation)**
:   Learn how to verify that users can navigate your app using a keyboard
    and how to make any necessary changes to the navigation order.

**[Handle keyboard actions](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/commands)**
:   Learn how to respond directly to keyboard input for user actions.