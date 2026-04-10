---
title: https://developer.android.com/guide/topics/ui/notifiers/toasts
url: https://developer.android.com/guide/topics/ui/notifiers/toasts
source: md.txt
---

# Toasts overview

A toast provides simple feedback about an operation in a small popup. It only fills the amount of space required for the message and the current activity remains visible and interactive. Toasts automatically disappear after a timeout.

For example, clicking**Send**on an email triggers a "Sending message..." toast, as shown in the following screen capture:
![Image of Android device showing a toast popup reading 'Sending message' next to an app icon](https://developer.android.com/static/images/toast.png)

If your app targets Android 12 (API level 31) or higher, its toast is limited to two lines of text and shows the application icon next to the text. Be aware that the line length of this text varies by screen size, so it's good to make the text as short as possible.

## Alternatives to using toasts

If your app is in the foreground, consider using a[snackbar](https://material.io/components/snackbars)instead of using a toast. Snackbars include user-actionable options, which can provide a better app experience.

If your app is in the background, and you want users to take some action, use a[notification](https://developer.android.com/develop/ui/views/notifications)instead.

## Instantiate a Toast object

Use the[`makeText()`](https://developer.android.com/reference/android/widget/Toast#makeText(android.content.Context,%20int,%20int))method, which takes the following parameters:

1. The activity[`Context`](https://developer.android.com/reference/android/content/Context).
2. The text that should appear to the user.
3. The duration that the toast should remain on the screen.

The`makeText()`method returns a properly initialized`Toast`object.

## Show the toast

To display the toast, call the[`show()`](https://developer.android.com/reference/android/widget/Toast#show())method, as demonstrated in the following example:  

### Kotlin

```kotlin
val text = "Hello toast!"
val duration = Toast.LENGTH_SHORT

val toast = Toast.makeText(this, text, duration) // in Activity
toast.show()
```

### Java

```java
CharSequence text = "Hello toast!";
int duration = Toast.LENGTH_SHORT;

Toast toast = Toast.makeText(this /* MyActivity */, text, duration);
toast.show();
```

## Chain your toast method calls

You can chain your methods to avoid holding on to the`Toast`object, as shown in the following code snippet:  

### Kotlin

```kotlin
Toast.makeText(context, text, duration).show()
```

### Java

```java
Toast.makeText(context, text, duration).show();
```