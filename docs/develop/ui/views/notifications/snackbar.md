---
title: https://developer.android.com/develop/ui/views/notifications/snackbar
url: https://developer.android.com/develop/ui/views/notifications/snackbar
source: md.txt
---

# Pop-up messages overview

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add notifications in Compose.  
[Snackbar →](https://developer.android.com/develop/ui/compose/components/snackbar)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

There are situations where you might want your app to show a quick message to the user, without necessarily waiting for the user to respond. For example, when a user performs an action like sending an email or deleting a file, your app shows a quick confirmation to the user. Often, the user doesn't need to respond to the message. The message needs to be prominent enough that the user can see it, but not so prominent that it prevents the user from working with your app.

Android provides the[Snackbar](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar)widget for this common use case. A`Snackbar`provides a quick pop-up message to the user. The current activity remains visible and interactive while the`Snackbar`is displayed. After a short time, the`Snackbar`automatically dismisses itself.

This documentation shows you how to use`Snackbar`to show pop-up messages.  
![](https://developer.android.com/static/images/training/snackbar/snackbar_drive_2x.png)

**Figure 1.** A`Snackbar`shows a message at the bottom of the activity, and the rest of the activity is still usable.
| **Note:** The`Snackbar`class supersedes[Toast](https://developer.android.com/reference/android/widget/Toast). While`Toast`is supported,`Snackbar`is the preferred way to display brief, transient messages to the user.

## Additional resources

**[Build and display a pop-up message](https://developer.android.com/develop/ui/views/notifications/snackbar/showing)**
:   Learn how to use a`Snackbar`to display a brief message to the user.

**[Add an action to a message](https://developer.android.com/develop/ui/views/notifications/snackbar/action)**
:   Learn how to add an action to a message, letting the user respond to the message.