---
title: https://developer.android.com/privacy-and-security/risks/secure-clipboard-handling
url: https://developer.android.com/privacy-and-security/risks/secure-clipboard-handling
source: md.txt
---

# Secure Clipboard Handling

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

Android offers a powerful framework referred to as the[clipboard](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Clipboard)for copying and pasting data between applications. An improper implementation of this feature could expose user-related data to unauthorized malicious actors or applications.

The specific risk associated with the exposure of clipboard data depends on the nature of the application and the Personal Identifiable Information (PII) it is handling. The impact is especially high for financial applications, as they may expose payment data, or apps that handle two-factor-authentication (2FA) codes.

The attack vectors that could be leveraged in order to exfiltrate clipboard data vary depending on Android version:

- [Android versions older than Android 10 (API level 29)](https://developer.android.com/about/versions/10/privacy/changes#clipboard-data)allow background applications to access foreground app clipboard information, potentially allowing direct access to any copied data by malicious actors.
- From Android 12 onwards (API level 31), every time an application accesses data within the clipboard and pastes it, a toast message is shown to the user, making it more difficult for attacks to go unnoticed. Additionally, in order to protect PII, Android supports the`ClipDescription.EXTRA_IS_SENSITIVE`or`android.content.extra.IS_SENSITIVE`special flag. This allows developers to visually obfuscate the clipboard content preview within the keyboard GUI, preventing copied data from being visually shown in clear-text and potentially stolen by malicious applications. Not implementing one of the aforementioned flags could in fact allow attackers to exfiltrate sensitive data copied to the clipboard by either shoulder surfing or through malicious applications that, while running in background, take screenshots or record videos of a legitimate user's activities.

## Impact

The exploitation of improper clipboard handling could result in user-related sensitive or financial data being exfiltrated by malicious actors. This may aid attackers in conducting further actions such as phishing campaigns or identity theft.

## Mitigations

### Flag Sensitive Data

This solution is employed to visually obfuscate the clipboard content preview within the keyboard GUI. Any sensitive data that can be copied, such as passwords or credit card data, should be flagged with`ClipDescription.EXTRA_IS_SENSITIVE`or`android.content.extra.IS_SENSITIVE`before calling[`ClipboardManager.setPrimaryClip()`](https://developer.android.com/reference/android/content/ClipboardManager#setPrimaryClip(android.content.ClipData)).  

### Kotlin

    // If your app is compiled with the API level 33 SDK or higher.
    clipData.apply {
        description.extras = PersistableBundle().apply {
            putBoolean(ClipDescription.EXTRA_IS_SENSITIVE, true)
        }
    }

    // If your app is compiled with API level 32 SDK or lower.
    clipData.apply {
        description.extras = PersistableBundle().apply {
            putBoolean("android.content.extra.IS_SENSITIVE", true)
        }
    }

### Java

    // If your app is compiled with the API level 33 SDK or higher.
    PersistableBundle extras = new PersistableBundle();
    extras.putBoolean(ClipDescription.EXTRA_IS_SENSITIVE, true);
    clipData.getDescription().setExtras(extras);

    // If your app is compiled with API level 32 SDK or lower.
    PersistableBundle extras = new PersistableBundle();
    extras.putBoolean("android.content.extra.IS_SENSITIVE", true);
    clipData.getDescription().setExtras(extras);

### Enforce Latest Android Versions

Enforcing the app to run on Android versions later or equal to Android 10 (API 29) prevents background processes from accessing clipboard data in the foreground application.

To enforce the app to run only on Android 10 (API 29) or later, set the following values for the version settings in the Gradle build files within your project in Android Studio.  

### Groovy

    android {
          namespace 'com.example.testapp'
          compileSdk [SDK_LATEST_VERSION]

          defaultConfig {
              applicationId "com.example.testapp"
              minSdk 29
              targetSdk [SDK_LATEST_VERSION]
              versionCode 1
              versionName "1.0"
              ...
          }
          ...
        }
        ...

### Kotlin

    android {
          namespace = "com.example.testapp"
          compileSdk = [SDK_LATEST_VERSION]

          defaultConfig {
              applicationId = "com.example.testapp"
              minSdk = 29
              targetSdk = [SDK_LATEST_VERSION]
              versionCode = 1
              versionName = "1.0"
              ...
          }
          ...
        }
        ...

### Delete Clipboard content after a defined period of time

If the application is meant to run on Android versions lower than Android 10 (API level 29), any background application can access clipboard data. In order to reduce this risk, it's useful to implement a function that clears any data copied to the clipboard after a specific period of time. This function is[automatically performed starting with Android 13 (API level 33)](https://blog.google/products/android/android-13/). For older Android versions, this deletion can be performed by including the following snippet within the application's code.  

### Kotlin

    //The Executor makes this task Asynchronous so that the UI continues being responsive
    backgroundExecutor.schedule({
        //Creates a clip object with the content of the Clipboard
        val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
        val clip = clipboard.primaryClip
        //If SDK version is higher or equal to 28, it deletes Clipboard data with clearPrimaryClip()
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            clipboard.clearPrimaryClip()
        } else if (Build.VERSION.SDK_INT < Build.VERSION_CODES.P) {
        //If SDK version is lower than 28, it will replace Clipboard content with an empty value
            val newEmptyClip = ClipData.newPlainText("EmptyClipContent", "")
            clipboard.setPrimaryClip(newEmptyClip)
         }
    //The delay after which the Clipboard is cleared, measured in seconds
    }, 5, TimeUnit.SECONDS)

### Java

    //The Executor makes this task Asynchronous so that the UI continues being responsive

    ScheduledExecutorService backgroundExecutor = Executors.newSingleThreadScheduledExecutor();

    backgroundExecutor.schedule(new Runnable() {
        @Override
        public void run() {
            //Creates a clip object with the content of the Clipboard
            ClipboardManager clipboard = (ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
            ClipData clip = clipboard.getPrimaryClip();
            //If SDK version is higher or equal to 28, it deletes Clipboard data with clearPrimaryClip()
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                clipboard.clearPrimaryClip();
                //If SDK version is lower than 28, it will replace Clipboard content with an empty value
            } else if (Build.VERSION.SDK_INT < Build.VERSION_CODES.P) {
                ClipData newEmptyClip = ClipData.newPlainText("EmptyClipContent", "");
                clipboard.setPrimaryClip(newEmptyClip);
            }
        //The delay after which the Clipboard is cleared, measured in seconds
        }, 5, TimeUnit.SECONDS);

## Resources

- [The clipboard framework](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#Clipboard)
- [System notification shown when your app accesses clipboard data](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#PastingSystemNotifications)
- [Add sensitive content to the clipboard](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#SensitiveContent)
- [Privacy changes in Android 10](https://developer.android.com/about/versions/10/privacy/changes)
- [Set app version information](https://developer.android.com/studio/publish/versioning#appversioning)