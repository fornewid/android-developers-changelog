---
title: https://developer.android.com/studio/preview/install-preview
url: https://developer.android.com/studio/preview/install-preview
source: md.txt
---

# Install a preview version of Android Studio

If you want early access to the next version of Android Studio, you don't have to replace your existing stable version. You can install the Android Studio preview side by side with the stable version and work on the same app projects in both.

This is possible because Android Studio stores its settings for each install in version-specific folders. For example, if you have the stable version of Android Studio 2.3 and a preview version of Android Studio 3.0 installed on Windows, the settings for each are saved in directories such as the following:  

```
C:\Users\Jamie\.AndroidStudio2.3\
C:\Users\Jamie\.AndroidStudioPreview3.0\
```

On Mac, these directories are in`~/Library/Preferences/`and`~/Library/Application Support/`. On Linux, they're in your home directory.

By default, all Android Studio installations share the same Android SDK tools location as specified in the[SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager), so updates to your other SDK tools are available in all versions of Android Studio.
| **Note:** Newer versions of Android Studio might change some configuration data in your projects (such as code style settings in the`.idea`file), which might not be compatible with the older version of Android Studio.

If you don't already have it,[download Android Studio stable here](https://developer.android.com/studio). It's good to have just in case you encounter a new bug in the preview version.

## Install alongside your stable version

After you[download an Android Studio preview](https://developer.android.com/studio/preview), simply save the application alongside any other version of Android Studio as described below.

**Windows:**

1. Unpack the ZIP file.
2. Rename the resulting folder to something unique like "Android Studio Preview."
3. Move it to a permanent location, such as next to your existing Android Studio install in`C:\Program Files\Android\`.
4. Inside`C:\Program Files\Android\Android Studio Preview\bin\`, launch`studio64.exe`(or if you're on a 32-bit machine, launch`studio.exe`).
5. To make the preview version available in your Start menu, right-click`studio64.exe`and click**Pin to Start Menu**.

**Mac:**

1. Unpack the ZIP file.**Note:**If you download version 2.3 or lower, the application name does not include the version number, so you must first rename it before moving the new version into your apps directory. Otherwise, you might override your existing version of Android Studio.

2. Drag the app file into your**Applications**folder.
3. Now launch it.

**Linux:**

1. Unpack the ZIP file.
2. Rename the resulting folder to something unique like "android-studio-preview."
3. Move it to wherever you have your stable version, such as within`/usr/local/`for your user profile, or`/opt/`for shared users.
4. Open a terminal, navigate into`android-studio-preview/bin/`and execute`studio`.