---
title: https://developer.android.com/games/engines/defold/defold-export
url: https://developer.android.com/games/engines/defold/defold-export
source: md.txt
---

# Export Defold projects to Android

This guide covers the process of exporting a Defold project as an Android app. Defold can generate both APK files for local device testing and Android App Bundles for submission to the Google Play Store.

To start the export process, choose**Project \> Bundle \> Android Application...** from the Defold menu bar. The**Bundle Application**window opens.
![Defold Bundle Application window](https://developer.android.com/static/images/games/engines/defold/Bundle_settings.png)**Figure 1.** The**Bundle Application**window

## Sign builds

If the**Keystore** and**Keystore Password**fields are empty, Defold automatically generates a debug keystore file and uses it to sign the application. Builds created with a debug keystore may be installed on local devices, but may not be uploaded to the Google Play Store.

To create a build for upload to the Google Play Store, you can use Android Studio to create a release keystore file.

To create a release keystore file for your app:

1. Launch Android Studio.
2. In the**Welcome to Android Studio** window, select**Create New Project**.
3. Select the**No Activity** template, and click**Next**.
4. In the**Configure Your Project** screen, click**Finish**to create the project.
5. Create a keystore file using the instructions at[Generate an upload key and keystore](https://developer.android.com/studio/publish/app-signing#generate-key).
6. After creating the keystore file, quit Android Studio and return to the Defold editor.
7. In the**Bundle Application** window, select the**...** button next to the**Keystore** field and select the newly created`.keystore`file.
8. Enter the keystore password in the**Keystore Password**field.

| **Caution:** When Defold updates to a new version, it generates a new debug keystore file. Before attempting to install a new build, uninstall any build generated using the previous debug keystore. If you don't follow this uninstall step, you'll get an`INSTALL_PARSE_FAILED_INCONSISTENT_CERTIFICATES`error during installation.

## Configure build settings

Use the**Bundle Application**window to configure build settings. These settings are different depending on whether it's for testing on a local device or is a final build for uploading to the Google Play Store.

To configure a build for testing on a local device:

- In the**Architectures** section, select both**32-bit** and**64-bit**.
- In the**Bundle Format** list, select**APK**.
- In the**Variant** list, select**Debug**.

When**Variant** is set to**Debug** , Defold logs engine debug messages to the device`logcat`. This is viewable in the[`logcat`window](https://developer.android.com/studio/debug/am-logcat)in Android Studio or with the`logcat`command in`adb`. For more information on using`adb`to install APK files and view logcat output, see the[Android Debug Bridge](https://developer.android.com/studio/command-line/adb)page.

To configure a build for upload to the Google Play Store:

- In the**Architectures** section, select both**32-bit** and**64-bit**.
- In the**Bundle Format** list, select**AAB**.
- In the**Variant** list, select**Release**.