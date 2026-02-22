---
title: https://developer.android.com/studio/troubleshoot
url: https://developer.android.com/studio/troubleshoot
source: md.txt
---

# Troubleshoot Android Studio

This page contains guidance for troubleshooting common issues and configuration problems in Android Studio.

## High-density displays

As of version 1.5, Android Studio provides support for high-density displays (like HiDPI and Retina monitors) on all platforms.

### Scaling factor settings

Android Studio determines the scaling factor for your display as follows:

Mac
:   For Retina displays, UI elements are scaled by a factor of 200% and images are rendered in high resolution. There should be no blurriness due to scaling, even in multi-monitor configurations. Note that there is no support for scaling factors other than 100% (for non-Retina displays) and 200% (for Retina displays).

Windows
:   Android Studio uses the primary display's DPI settings to determine the scaling factor of UI elements. For images, if the scaling factor is less than 150%, normal resolution images are scaled up. If the scaling factor is greater than 150%, high resolution images are scaled appropriately.

Linux
:   Android Studio determines the scaling factor by looking at the "Text Scaling Factor," then at the XWindow system DPI Setting.
A DPI setting of 96 corresponds to a scaling factor of 100% (no scaling), and a DPI setting of 192 corresponds to a scaling factor of 200% (the size of UI elements is doubled). Android Studio currently supports DPI settings between 96 (100% scaling) and 288 (300% scaling). If Android Studio does not detect the correct system DPI on your Linux or Windows machine, you can set it manually by setting the`hidpi`property in the`idea.properties`file as described in[Customize your IDE properties](https://developer.android.com/studio/intro/studio-config#customize_ide). Note that this property has no effect on Mac machines. This property functions as follows:

`hidpi=true`
:   Sets the DPI to 192 (200% scaling), ignoring the system settings.

`hidpi=false`
:   Sets the DPI to 96 (100% scaling), ignoring the system settings.

### Blurry or pixelated elements on high-density displays

If one or more elements of Android Studio's UI appear blurry or pixelated on your high-density display, you may be experiencing one of the following issues:

- If most of the Android Studio UI looks fine, but one particular icon is blurry or pixelated, or one particular UI element uses the wrong size font, that particular element probably has not yet been fully updated for HiDPI support. Please file a bug by clicking**Help \> Submit Feedback**. Please include a screenshot and as much information as possible on your system configuration.
- If you are using a Windows or Linux machine and your display uses a scaling factor other than 100% or 200%, images may appear slightly blurred due to the scaling.
- If you are using a Windows machine and you have have changed the Windows font size in the Control Panel, you may experience blurred or pixelated font. You can resolve this issue by signing out of Windows and then signing back in.
- On a multi-monitor setup running Windows 8.1 or later, when you move a window from one display to another display with a different resolution or DPI, you may experience font or image problems (see bug[186007](https://code.google.com/p/android/issues/detail?id=186007)). There is no known workaround at this time.
- Older versions of the JRE 1.8 had an issue for blurry fonts (JRE 1.8.0_25-b18 amd64 in particular, see bug[192316](https://code.google.com/p/android/issues/detail?id=192316).) As of version 2.2, Android studio includes a bundled version of the latest supported JDK, which includes the JDE. To resolve this issue, update Android Studio to version 2.2 or higher and switch to use the bundled JDK by clicking**File \> Project Structure \> SDK Location** and checking the**Use embedded JDK**checkbox.

### Incorrectly-sized elements on high-density displays

If the entire Android Studio UI is the wrong size on your high-density display, see[Scaling factor settings](https://developer.android.com/studio/troubleshoot#scaling-factor). If some elements of the Android Studio UI are the wrong size on your high-density display, but others are correctly-sized, you may be experiencing one of the following issues:

- If you are using a custom editor scheme, the editor font may appear too small or too big compared to the rest of the UI elements on a high-density display. To fix this issue, click**File \> Settings** then click**Editor \> Colors and Fonts \> Font** and change the size of the editor font. Note that when the default scheme is active, the editor font size is scaled automatically (see bug[186920](https://code.google.com/p/android/issues/detail?id=186920)).
- If some UI elements of Android Studio are the right size, but others are too small or too big, you may be experiencing issue[186923](https://code.google.com/p/android/issues/detail?id=186923). Please file a bug by clicking**Help \> Submit Feedback**. Please include a screenshot and as much information as possible on your system configuration.

<br />

## Project sync issues

When attempting to sync your project, you may receive the following error message: "Connection to the Internet denied. ('Permission denied: connect')". You can resolve this error message by adding the system property`-Djava.net.preferIPv4Stack=true`to your`gradle.properties`file in Android Studio as follows:

1. Open your`gradle.properties`file in Android Studio.
2. Add the following line to the file:  

   ```
   org.gradle.jvmargs=-Djava.net.preferIPv4Stack=true
   ```
   Note that if you have already added other Gradle JVM arguments to your`gradle.properties`file, you can add this property to the same line as shown in the following example:  

   ```
   org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m -Djava.net.preferIPv4Stack=true
   ```
3. Restart Android Studio for your changes to take effect.
4. Click**Sync Project with Gradle Files** ![](https://developer.android.com/static/studio/images/buttons/toolbar-sync-gradle.png)to sync your project.

## Problems updating the IDE on Windows

On Windows, files that are in use by a process cannot be deleted. When you attempt to use the built-in update mechanism in the IDE, it sometimes refuses to install the update, usually providing an error message like "Can't delete C:\\some\\path\\file".

To work around this, open the task manager and attempt to kill processes that may be using the file, such as any Gradle daemons.

## minSdkVersion issues

If you are using an obsolete version of the Android Support Libraries, you may receive an error message like the following:  

```
:app:processDebugManifest app/src/main/AndroidManifest.xml:0:0 Error:
uses-sdk:minSdkVersion 19 cannot be smaller than version L declared in library app/build/intermediates/exploded-aar/com.android.support/appcompat-v7/21.0.0-rc1/AndroidManifest.xml
Suggestion: use tools:overrideLibrary="android.support.v7.appcompat" to force usage
```

To resolve this issue, use the SDK manager to update to the latest (non-preview) versions of the Android Support Libraries. For more information about setting up the Support Libraries, see[Support Library setup](https://developer.android.com/topic/libraries/support-library/setup).

## Android Emulator issues

See[Android Emulator troubleshooting](https://developer.android.com/studio/run/emulator-troubleshooting).

## Directories

The following directories are used by Android Studio to store settings, caches, plugins, and logs.  

### Windows

- Configuration (idea.config.path):`%APPDATA%\Google\`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- Plugins (idea.plugins.path):`%APPDATA%\Google\`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>`\plugins`
- System (idea.system.path):`%LOCALAPPDATA%\Google\`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- Logs (idea.log.path):`%LOCALAPPDATA%\Google\`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>`\log`

> - `%APPDATA%`example:`C:\Users\YourUserName\AppData\Roaming`
> - `%LOCALAPPDATA%`example:`C:\Users\YourUserName\AppData\Local`

### macOS

- Configuration (idea.config.path):`~/Library/Application Support/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- Plugins (idea.plugins.path):`~/Library/Application Support/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>`/plugins`
- System (idea.system.path):`~/Library/Caches/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- Logs (idea.log.path):`~/Library/Logs/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>

### Linux

- Configuration (idea.config.path):`~/.config/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- Plugins (idea.plugins.path):`~/.local/share/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- System (idea.system.path):`~/.cache/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>
- Logs (idea.log.path):`~/.cache/Google/`<var class="readonly" scope="AndroidStudio" translate="no">AndroidStudio</var><var class="readonly" scope="VERSION" translate="no">VERSION</var>`/log`

Each directory is listed in the following format:

- `<informal directory name>`([`<IDE property>`](https://developer.android.com/studio/intro/studio-config#customize_ide)):`<default path>`.

Replace:

- <var class="edit" scope="AndroidStudio" translate="no">AndroidStudio</var>with the product name, which is`AndroidStudio`for Stable releases, or`AndroidStudioPreview`for RC and Canary releases.
- <var class="edit" scope="VERSION" translate="no">VERSION</var>with the version. For example:`2023.1`or`2023.3`.