---
title: https://developer.android.com/about/versions/nougat/android-7.1-samples
url: https://developer.android.com/about/versions/nougat/android-7.1-samples
source: md.txt
---

# Android 7.1 Samples

The following code samples are provided for Android 7.1 (API 25). To download the samples in Android Studio, select the**File \> New \> Import Sample**menu option.

**Note:**These downloadable projects are designed for use with Gradle and Android Studio.

### App shortcuts sample

This sample demonstrates how to use the[app shortcuts API](https://developer.android.com/guide/topics/ui/shortcuts)introduced in Android 7.1 (API level 25). This API allows an application to define a set of intents which are displayed when a user long-presses on the app's launcher icon. Examples are given for registering links both statically in XML, as well as dynamically at runtime.

[App shortcuts sample](https://github.com/android/user-interface-samples/tree/main/AppShortcuts)

### Image keyboard app sample

This sample demonstrates how to implement the[Commit Content API](https://developer.android.com/reference/android/view/inputmethod/InputConnection#commitContent(android.view.inputmethod.InputContentInfo,%20int,%20android.os.Bundle)), using the[Android Support Library](https://developer.android.com/topic/libraries/support-library). This API provides a universal way for IMEs to send images and other rich content directly to a text editor in an app, allowing users to compose content using custom emojis, stickers, or other rich content provided by other applications.

[Image keyboard app sample](https://github.com/android/input-samples/tree/main/CommitContentSampleApp)

### Image keyboard IME sample

This sample demonstrates how to write a[custom image keyboard](https://developer.android.com/preview/image-keyboard)using the[Commit Content API](https://developer.android.com/reference/android/view/inputmethod/InputConnection#commitContent(android.view.inputmethod.InputContentInfo,%20int,%20android.os.Bundle))and the[Android Support Library](https://developer.android.com/topic/libraries/support-library). This keyboard will be displayed inside compatible apps (also using the Commit Content API), allowing users to insert emojis, stickers, or other rich content into text editors.

[Image keyboard IME sample](https://github.com/android/input-samples/tree/main/CommitContentSampleIME)