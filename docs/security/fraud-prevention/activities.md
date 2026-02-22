---
title: https://developer.android.com/security/fraud-prevention/activities
url: https://developer.android.com/security/fraud-prevention/activities
source: md.txt
---

# Secure sensitive activities

This document details ways to monitor sensitive activities, such as user logins and online purchases.

## FLAG_SECURE

`FLAG_SECURE`is a[Window flag](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)that tells Android not to allow screenshots or to display the window view on a non-secure display (such as Casting the screen). This is useful for applications that need to protect sensitive information, like banking apps or password managers. When a window is flagged with`FLAG_SECURE`, Android prevents screenshots from being taken and prevents the window from being displayed on a non-secure display, such as a TV or projector. This helps to protect the information that is being displayed in the window from being accessed by unauthorized people.

### How this helps mitigate fraud

A malicious app or entity might retrieve background screenshots. When the state of your app changes to the background,`FLAG_SECURE`can be used. When the screenshot is taken the resulting image is blank.

`FLAG_SECURE`also helps with remote screen sharing use cases. It isn't always a malicious app that will retrieve screenshots, legitimate screen sharing apps are also commonly found used in fraudulent situations.

### Implementation

For views with the information you want protected, add the following:  

### Kotlin

```kotlin
window?.setFlags(
    WindowManager.LayoutParams.FLAG_SECURE,
    WindowManager.LayoutParams.FLAG_SECURE
)
```

### Java

```java
window.setFlags(
  WindowManager.LayoutParams.FLAG_SECURE,
  WindowManager.LayoutParams.FLAG_SECURE
);
```

### Best practices

It is important to note that this approach isn't reliable in preventing overlay attacks. In some cases it does not correctly predict if screen recording is active, however it does cover most use cases. To mitigate overlay attacks, read the next section about`HIDE_OVERLAY_WINDOWS`permissions.
| **Note:** For Android 11 (API 30) and lower`FLAG_SECURE`is able to help around 70% of the devices reliably. This is because on certain devices keyboard taps can be recorded.

## HIDE_OVERLAY_WINDOWS

`HIDE_OVERLAY_WINDOWS`is a permission added in Android 12 where your app can opt-out of having application overlays drawn over it. In Android 12 we have made it harder to acquire the[`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)permission, essentially allowing your app to block overlays from third-party apps.

### How this helps mitigate fraud

When you enable the`HIDE_OVERLAY_WINDOWS`permission you are opting out of having application overlays drawn on top of your app. This permission provides a protection mechanism against[cloak and dagger](https://cloak-and-dagger.org/)attacks.

### Implementation

To enable this permission, add[`HIDE_OVERLAY_WINDOWS`](https://developer.android.com/reference/android/Manifest.permission#HIDE_OVERLAY_WINDOWS)to your project's manifest.

### Best practices

As with any permission, you should trust any overlay app at least as much as you trust any other app on the device. In other words, your app shouldn't allow other apps to draw overlays over it unless you know the other app is trustworthy. Allowing an app to draw over other apps can be dangerous because it can steal passwords or read messages.