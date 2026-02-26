---
title: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/visibility
url: https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/visibility
source: md.txt
---

When input focus moves in or out of an editable text field, Android shows or
hides the input ---such as the on-screen keyboard---as
appropriate. The system also decides how your UI and the text field appear above
the input method. For example, when the vertical space on the screen is
constrained, the text field might fill all space above the input method.

For most apps, these default behaviors are all that's needed. In some cases,
though, you might want more control over the visibility of the input method and
how it impacts the layout. This lesson explains how to control and respond to
the input method visibility.

> [!NOTE]
> **Note:** This page refers to the phrase *soft keyboard* throughout, which represents an on-screen keyboard and is the most common type of soft input method. Android supports other types of soft input methods, including image input and ink drawing.

## Show the soft keyboard when the activity starts

Although Android gives focus to the first text field in your layout when the
activity starts, it doesn't show the soft keyboard. This behavior is appropriate
because entering text might not be the primary task in the activity. However, if
entering text is indeed the primary task, such as in a login screen, then you
probably want the soft keyboard to appear by default.

To show the input method when your activity starts, add the
[`android:windowSoftInputMode`](https://developer.android.com/guide/topics/manifest/activity-element#wsoft) attribute to the
`<activity>` element with the `"stateVisible"` value. For example:

    <application ... >
        <activity
            android:windowSoftInputMode="stateVisible" ... >
            ...
        </activity>
       ...
    </application>

> [!NOTE]
> **Note:** If the user's device has an attached hardware keyboard, the soft keyboard does not appear.

### Specify how your UI should respond

When the soft keyboard appears on the screen, it reduces the amount of space
available for your app's UI. The system decides how to adjust the visible
portion of your UI, but it might not get it right. To ensure the best behavior
for your app, specify how you want the system to display your UI in the
remaining space.

To declare your preferred treatment in an activity, use the
`android:windowSoftInputMode` attribute in your manifest's `<activity>` element
with one of the "adjust" values.

For example, to ensure that the system resizes your layout to the available
space---which keeps all of your layout content accessible, even if it
requires scrolling---use `"adjustResize"`:

    <application ... >
       <activity
           android:windowSoftInputMode="adjustResize" ... >
           ...
       </activity>
       ...
    </application>

You can combine the adjustment specification with the [initial soft keyboard
visibility](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/visibility#ShowOnStart) specification from the preceding section:

    <activity
        android:windowSoftInputMode="stateVisible|adjustResize" ... >
        ...
    </activity>

Specifying `"adjustResize"` is important if your UI includes controls that the
user might need to access immediately after or while performing text input. For
example, if you use a relative layout to place a button bar at the bottom of
the screen, using `"adjustResize"` resizes the layout so the button bar appears
above the soft keyboard.

## Show the soft keyboard on demand

If there is a method in your activity's lifecycle where you want to ensure the
input method is visible, you can use the
[`InputMethodManager`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager)
to show it.

For example, the following method takes a
[`View`](https://developer.android.com/reference/android/view/View) in which the user is expected to
type something, calls
[`requestFocus()`](https://developer.android.com/reference/android/view/View#requestFocus()) to give it
focus, then calls [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)) to open the input method:

### Kotlin

```kotlin
fun showSoftKeyboard(view: View) {
   if (view.requestFocus()) {
       val imm = getSystemService(InputMethodManager::class.java)
       imm.showSoftInput(view, InputMethodManager.SHOW_IMPLICIT)
   }
}
```

### Java

```java
public void showSoftKeyboard(View view) {
   if (view.requestFocus()) {
       InputMethodManager imm = getSystemService(InputMethodManager.class);
       imm.showSoftInput(view, InputMethodManager.SHOW_IMPLICIT);
   }
}
```

> [!NOTE]
> **Note:** Once the soft keyboard is visible, don't programmatically hide it. The system hides the input method when the user finishes the task in the text field. Alternatively, the user can hide it with a system control, such as with the Back button.

> [!CAUTION]
> **Caution:** Don't use the [`SHOW_FORCED`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#SHOW_FORCED) flag in [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)) to request the soft keyboard. Otherwise, the software keyboard can remain open even after the app has been closed.

### Show the soft keyboard reliably

There are certain situations, such as when an activity is starting, in which
using [`InputMethodManager.showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)) to display the soft keyboard
may result in the software keyboard not being visible to the user.

The visibility of the soft keyboard when using [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)) is reliant
on the following conditions:

- The view must already be connected to the software keyboard. (This, in turn,
  requires the [window to be focused](https://developer.android.com/reference/android/view/View#onWindowFocusChanged(boolean)) and the editor
  view to request the view focus with
  [`View.requestFocus()`](https://developer.android.com/reference/android/view/View#requestFocus(int))).

- The visibility can also be affected by the `android:windowSoftInputMode`
  attribute and flags used by [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)).

In certain use cases, such as when an activity is starting, some of these
required conditions aren't met. The system doesn't consider the view as
connected to the software keyboard, ignores the [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)) call,
and the soft keyboard isn't visible to the user.

To make sure the software keyboard is reliably shown, you can use the following
alternatives:

- **(Recommended) Use** [`WindowInsetsControllerCompat`](https://developer.android.com/reference/androidx/core/view/WindowInsetsControllerCompat). This object displays the soft keyboard during [`Activity.onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) as shown in the following code snippet. The call is guaranteed to be scheduled after the window is focused.

### Kotlin

```kotlin
editText.requestFocus()
WindowCompat.getInsetsController(window, editText)!!.show(WindowInsetsCompat.Type.ime())
```

### Java

```java
editText.requestFocus();
WindowCompat.getInsetsController(getWindow(), editText).show(WindowInsetsCompat.Type.ime());
```

- **Post a runnable.** This ensures that your app waits until receiving the window focus event from [`View.onWindowFocusChanged()`](https://developer.android.com/reference/android/view/View#onWindowFocusChanged(boolean)) before calling [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)).

### Kotlin

```kotlin
class MyEditText : EditText() {
  ...
  override fun onWindowFocusChanged(hasWindowFocus: Boolean) {
    if (hasWindowFocus) {
      requestFocus()
      post {
        val imm: InputMethodManager = getSystemService(InputMethodManager::class.java)
        imm.showSoftInput(this, 0)
      }
    }
  }
}
```

### Java

```java
public class MyEditText extends EditText {
  ...
  @Override
  public void onWindowFocusChanged(boolean hasWindowFocus) {
    if (hasWindowFocus) {
      requestFocus();
      post(() -> {
        InputMethodManager imm = getSystemService(InputMethodManager.class);
        imm.showSoftInput(this, 0);
      });
    }
  }
}
```

### Handle runtime visibility flags carefully

When toggling soft keyboard visibility at runtime, take care not to pass certain
flag values into these methods. For example, if the application expects the
soft keyboard shows up when calling
`View.getWindowInsetsController().show(ime())` in `Activity.onCreate()` during
the activity starts, the application developers should be careful to not set
[`SOFT_INPUT_STATE_HIDDEN`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#SOFT_INPUT_STATE_HIDDEN) or [`SOFT_INPUT_STATE_ALWAYS_HIDDEN`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#SOFT_INPUT_STATE_ALWAYS_HIDDEN) flags
during the initial launch in case the soft keyboard is hidden unexpectedly.

## System usually hides the soft keyboard automatically

In most situations, the system handles hiding the soft keyboard. This
can be any of the following cases:

- The user finishes the task in the text field.
- The user presses the back key or swipe gestures with the back navigation.
- The user navigate to another app, and that other app has set [`SOFT_INPUT_STATE_HIDDEN`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#SOFT_INPUT_STATE_HIDDEN) or [`SOFT_INPUT_STATE_ALWAYS_HIDDEN`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#SOFT_INPUT_STATE_ALWAYS_HIDDEN) flags when the view gains the focus.

> [!NOTE]
> **Note:** Focusing a view other than a text field doesn't dismiss the soft keyboard on its own.

### Hide the soft keyboard manually based on previous system behavior

Your app must hide the soft keyboard manually in some situations---for
example, when the text field loses focus in
[`View.OnFocusChangeListener.onFocusChange`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener#onFocusChange(android.view.View,%20boolean)). Use this technique judiciously
; closing the soft keyboard unexpectedly impairs the user experience.

If your app manually hides the soft keyboard, you need to know whether
the soft keyboard was shown *explicitly* or *implicitly*:

- The soft keyboard is considered to have been *explicitly* shown after
  a call to [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)).

- Conversely, the soft keyboard is considered to have been implicitly shown in
  either of the following conditions:

  - The system showed the soft keyboard while applying the `android:windowSoftInputMode`.
  - Your app passed [`SHOW_IMPLICIT`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#SHOW_IMPLICIT) to [`showSoftInput()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#showSoftInput(android.view.View,int)).

Normally, [`hideSoftInputFromWindow()`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#hideSoftInputFromWindow(android.os.IBinder,%20int)) hides the soft keyboard regardless of
how it was requested, but with [`HIDE_IMPLICIT_ONLY`](https://developer.android.com/reference/android/view/inputmethod/InputMethodManager#HIDE_IMPLICIT_ONLY)
it can be limited to only dismissing an implicitly requested soft keyboard.

## Show a dialog or overlay view on top of the soft keyboard

In some situations, the editor activity might need to create a non-editable
dialog or overlay window on top of the soft keyboard.

Your app has a few options, which the following sections describe.

In summary, make sure to correctly handle the window flags of the soft keyboard
targeting the window such that it satisfies the following expectations
regarding vertical (z-layer) ordering:

- No flags (normal case): Behind the soft keyboard layer, and can receive text.
- [`FLAG_NOT_FOCUSABLE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_FOCUSABLE) : On top of the soft keyboard layer, but can't receive text.
- [`FLAG_ALT_FOCUSABLE_IM`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_ALT_FOCUSABLE_IM) : On top of the soft keyboard layer, can be focused but isn't connected to the soft keyboard. Also blocks all views underneath it from connecting to the soft keyboard. This is useful for showing an app dialog that doesn't use text input above the soft keyboard layer.
- [`FLAG_NOT_FOCUSABLE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_FOCUSABLE) and [`FLAG_ALT_FOCUSABLE_IM`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_ALT_FOCUSABLE_IM) : Behind the soft keyboard layer, but can't receive text.
- [`FLAG_NOT_FOCUSABLE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_FOCUSABLE) and [`FLAG_NOT_TOUCH_MODAL`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_TOUCH_MODAL) : On top of the soft keyboard, and allow touch events to go "through" the window onto the soft keyboard.

### Create a dialog

Use the [`FLAG_ALT_FOCUSABLE_IM`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_ALT_FOCUSABLE_IM)
dialog window flag to keep the dialog on top of the soft keyboard, and to
prevent the soft keyboard from gaining focus:

### Kotlin

```kotlin
val content = TextView(this)
content.text = "Non-editable dialog on top of soft keyboard"
content.gravity = Gravity.CENTER
val builder = AlertDialog.Builder(this)
  .setTitle("Soft keyboard layering demo")
  .setView(content)
mDialog = builder.create()
mDialog!!.window!!
  .addFlags(WindowManager.LayoutParams.FLAG_ALT_FOCUSABLE_IM)
mDialog!!.show()
```

### Java

```java
TextView content = new TextView(this);
content.setText("Non-editable dialog on top of soft keyboard");
content.setGravity(Gravity.CENTER);
final AlertDialog.Builder builder = new AlertDialog.Builder(this)
    .setTitle("Soft keyboard layering demo")
    .setView(content);
mDialog = builder.create();
mDialog.getWindow().addFlags(FLAG_ALT_FOCUSABLE_IM);
mDialog.show();
```

### Create an overlay view

Create an overlay view specifying [`TYPE_APPLICATION_OVERLAY`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY)
window type and [`FLAG_ALT_FOCUSABLE_IM`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_ALT_FOCUSABLE_IM)
window flag by the soft keyboard targeted activity.

> [!NOTE]
> **Note:** This requires the user to grant the [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW) [special
> permission](https://developer.android.com/training/permissions/requesting-special) to your app.

### Kotlin

```kotlin
val params = WindowManager.LayoutParams(
  width,  /* Overlay window width */
  height,  /* Overlay window height */
  WindowManager.LayoutParams.TYPE_APPLICATION, /* Overlay window type */
  WindowManager.LayoutParams.FLAG_ALT_FOCUSABLE_IM /* No need to allow for text input on top of the soft keyboard */
    or WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL,  /* Allow touch event send to soft keyboard behind the overlay */
  PixelFormat.TRANSLUCENT
)
params.title = "Overlay window"
mOverlayView!!.layoutParams = params
windowManager.addView(mOverlayView, params)
```

### Java

```java
WindowManager.LayoutParams params = new WindowManager.LayoutParams(
    width, /* Overlay window width */
    height, /* Overlay window height */
    TYPE_APPLICATION, /* Overlay window type */
    FLAG_ALT_FOCUSABLE_IM /* No need to allow for text input on top of the soft keyboard */
        | FLAG_NOT_TOUCH_MODAL, /* Allow touch event send to soft keyboard behind the overlay */
    PixelFormat.TRANSLUCENT);
params.setTitle("Overlay window");
mOverlayView.setLayoutParams(params);
getWindowManager().addView(mOverlayView, params);
```

## Show a dialog or view underneath the soft keyboard

Your app might need to create a dialog or a window that has the
following properties:

- Appears underneath the soft keyboard requested by an editor activity such that it's not affected by text input.
- Remains aware of changes to the soft keyboard's inset size changes to adjust the dialog or window's layout.

In this case, your app has several options. The following sections
describe these options.

### Create a dialog

Create a dialog by setting both the [`FLAG_NOT_FOCUSABLE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_FOCUSABLE)
window flag and the [`FLAG_ALT_FOCUSABLE_IM`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_ALT_FOCUSABLE_IM)
window flag:

### Kotlin

```kotlin
val content = TextView(this)
content.text = "Non-editable dialog behind soft keyboard"
content.gravity = Gravity.CENTER
val builder = AlertDialog.Builder(this)
  .setTitle("Soft keyboard layering demo")
  .setView(content)
mDialog = builder.create()
mDialog!!.window!!
  .addFlags(FLAG_NOT_FOCUSABLE or FLAG_ALT_FOCUSABLE_IM)
mDialog!!.show()
```

### Java

```java
TextView content = new TextView(this);
content.setText("Non-editable dialog behind soft keyboard");
content.setGravity(Gravity.CENTER);
final AlertDialog.Builder builder = new AlertDialog.Builder(this)
    .setTitle("Soft keyboard layering demo")
    .setView(content);

mDialog = builder.create();
mDialog.getWindow()
    .addFlags(FLAG_NOT_FOCUSABLE | FLAG_ALT_FOCUSABLE_IM);
mDialog.show();
```

### Create an overlay view

Create an overlay view by setting both the [`FLAG_NOT_FOCUSABLE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_NOT_FOCUSABLE)
window flag and the [`FLAG_ALT_FOCUSABLE_IM`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_ALT_FOCUSABLE_IM)
window flag:

### Kotlin

```kotlin
val params = WindowManager.LayoutParams(
  width,  /* Overlay window width */
  height,  /* Overlay window height */
  WindowManager.LayoutParams.TYPE_APPLICATION,  /* Overlay window type */
  WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
      or WindowManager.LayoutParams.FLAG_ALT_FOCUSABLE_IM,
  PixelFormat.TRANSLUCENT
)
params.title = "Overlay window"
mOverlayView!!.layoutParams = params
windowManager.addView(mOverlayView, params)
```

### Java

```java
WindowManager.LayoutParams params = new WindowManager.LayoutParams(
    width, /* Overlay window width */
    height, /* Overlay window height */
    TYPE_APPLICATION, /* Overlay window type */
    FLAG_NOT_FOCUSABLE | FLAG_ALT_FOCUSABLE_IM,
    PixelFormat.TRANSLUCENT);
params.setTitle("Overlay window");
mOverlayView.setLayoutParams(params);
getWindowManager().addView(mOverlayView, params);
```