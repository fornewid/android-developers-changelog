---
title: https://developer.android.com/privacy-and-security/security-dex
url: https://developer.android.com/privacy-and-security/security-dex
source: md.txt
---

On devices running Android 10 (API level 29) and higher you can tell the platform to run
embedded DEX code directly from your app's APK file. This option can help
prevent an attack if an attacker ever managed to tamper with the locally
compiled code on the device.
| **Note:** Enabling this feature could possibly affect your app's performance because ART must use the [JIT compiler](https://source.android.com/devices/tech/dalvik/jit-compiler) when the app is started (instead of reading native code that was compiled ahead of time). We recommend testing your app's performance before you decide whether or not to enable this feature in your published apps.

If you're using the Gradle build system, to enable this feature do the
following:

- Set the `android::useEmbeddedDex` attribute to
  `true` in the
  [<application>](https://developer.android.com/guide/topics/manifest/application-element)
  element of your app's manifest file.

- Set `useLegacyPackaging` to `false` in the
  module-level `build.gradle.kts` file (`build.gradle`
  file if you're using Groovy).

  **Note:** Don't set the `useLegacyPackaging` option if you're using a version of AGP lower than 4.2.  

  ### Kotlin

  ```kotlin
    packagingOptions {
      dex {
        useLegacyPackaging = false
      }
    }
    
  ```

  ### Groovy

  ```groovy
    packagingOptions {
      dex {
        useLegacyPackaging false
      }
    }
    
  ```

If you're using the Bazel build system, to enable this feature set the
`android:useEmbeddedDex` attribute to `true` in the `<application>` element of
your app's manifest file and leave DEX files uncompressed:  

```
android_binary(
   ...
   nocompress_extensions = [".dex"],
)
```

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Tapjacking](https://developer.android.com/topic/security/risks/tapjacking)
- [android:exported](https://developer.android.com/topic/security/risks/android-exported)
- [# Key management {:#key-management}](https://developer.android.com/topic/security/data)