---
title: https://developer.android.com/games/engines/defold/defold-configure
url: https://developer.android.com/games/engines/defold/defold-configure
source: md.txt
---

# Install Defold and configure projects for Android

This guide covers the following steps:

- Selecting a version of Defold
- Downloading and installing Defold
- Creating a new project using the mobile template
- Configuring Android specific Defold project settings

## Select a version

Use the latest stable release of Defold when possible. For Android development, use version 1.2.181 or higher.
| **Note:** Starting in August 2021, Google Play will require all Android apps to be submitted as Android App Bundles, and to use a target API level of 30 or higher. Defold 1.2.181 or higher meets these requirements. For more information, see the[Target API Level](https://developer.android.com/distribute/best-practices/develop/target-sdk)page.

## Download and run Defold

Visit the[Defold download page](https://defold.com/download/)to download the game engine for your preferred environment.

Defold is distributed as a standalone application. It does not require an installation process; after extracting the download archive, you can run it as-is.

## Create a project using the mobile game template

Defold includes a variety of templates you can use when creating a new project. The**Mobile Game** template is useful when making a project for Android. Choosing this template automatically creates placeholder application icon files, and configures size settings, orientation settings, and[input bindings](https://defold.com/manuals/input/#setting-up-input-bindings).

To create a new project using the Mobile Game template, do the following:

1. Launch the[Defold editor](https://defold.com/manuals/editor/).
2. Click**New Project** , and make sure the**From Template**tab is selected.
3. Choose the**Mobile Game**template from the list.
4. Specify a name and location for the new project.
5. Click**Create New Project**.

![Selecting the Mobile Game template from new project](https://developer.android.com/static/images/games/engines/defold/Mobile_template.png)**Figure 1.** Selecting the**Mobile Game**template when creating a new project

## Configure projects for Android

Defold supports a number of Android-specific settings for a Defold project.

- To access these settings: in the Defold editor, open the`game.project`file and scroll down to the**Android**section.

![The Android section of Defold project settings](https://developer.android.com/static/images/games/engines/defold/Project_settings.png)**Figure 2.**Project settings for a Defold project

Important Android specific project settings group into the following categories:

### Application icons

**App icon**fields: Specify the application icon files. Icon files must be in PNG format and match the pixel size denoted in the field name.

### Package information

**Version Code**: Specify the package version code. Google Play requires a unique version code for each package submission. Attempting to use a version code that is lower than a previously submitted version code results in an error.

**Minimum Sdk Version**: Define the minimum Android API level supported by your project.

**Target Sdk Version** : Define the API level of the Android SDK used to build and export the project. Ensure this value is compliant with Google Play[target API requirements](https://developer.android.com/distribute/best-practices/develop/target-sdk).

**Package**: Specify the package identifier of the application. This should match the package identifier created in the Google Play Console.

**Manifest setting** : Specify the`AndroidManifest.xml`file that will be used to create the application manifest. Defold automatically generates a default manifest file for this setting and populates it with values from the project settings.

### Other settings

**Immersive Mode**: If selected, this option hides the navigation and status bars when the application is active.

**Debuggable** : If selected, this option sets the`android:debuggable`field in the Android manifest during export.

## Additional resources

- [Defold manual - Android development](https://defold.com/manuals/android/)
- [Defold manual - Project settings](https://defold.com/manuals/project-settings)