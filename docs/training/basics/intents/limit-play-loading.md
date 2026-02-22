---
title: https://developer.android.com/training/basics/intents/limit-play-loading
url: https://developer.android.com/training/basics/intents/limit-play-loading
source: md.txt
---

# Limit loading in on-device Android containers

*On-device Android containers*are apps that simulate the Android OS on an Android-powered device. This includes both apps that simulate the Android OS in its entirety and apps that only simulate portions of the Android OS.

If you don't want on-device Android container apps to load in or proxy your Play Store app, you can add a string to your app manifest that declares this restriction.

Create a[property](https://developer.android.com/guide/topics/manifest/property-element)under the[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)in your Android manifest with`android:name`set to`REQUIRE_SECURE_ENV`and`android:value`set to 1:  

    <property android:name="REQUIRE_SECURE_ENV" android:value="1" />

For this use case, you can use the`REQUIRE_SECURE_ENV`property regardless of the Android version that your app runs on.

On-device Android container apps are[required](https://support.google.com/googleplay/android-developer/answer/9888379)to respect this declaration.

For more information about on-device Android containers, see the[Help Center](https://support.google.com/googleplay/android-developer/answer/13609005).