---
title: https://developer.android.com/studio/projects/add-app-module
url: https://developer.android.com/studio/projects/add-app-module
source: md.txt
---

# Add a module for a new device

Modules provide a container for your app's source code, resource files, and app level settings, such as the module-level build file and Android manifest file. Each module can be independently built, tested, and debugged.

Android Studio uses modules to make it easy to add new devices to your project. By following a few simple steps in Android Studio, you can create a module to contain code that's specific to a device type, such as Wear OS or Android TV. Android Studio automatically creates module directories, such as source and resource directories, and a default`build.gradle`file appropriate for the device type. Also, Android Studio creates device modules with recommended build configurations, such as using the Leanback library for Android TV modules.

This page describes how to add a new module for a specific device.

Android Studio also makes it easy to add a library or Google Cloud module to your project. For details on creating a library module, see[Create a Library Module](https://developer.android.com/studio/projects/android-library#CreateLibrary).

## Create a new module

To add a new module to your project for a new device, proceed as follows:

1. Click**File** \>**New** \>**New Module**.
2. In the**Create New Module** window that appears, Android Studio offers the following device modules:
   - Phone \& Tablet Module
   - Wear OS Module
   - Android TV Module
   - Glass Module

   Select the module for the device you want, and then click**Next**.
3. In the**Configure your new module** form, enter the following details:
   - **Application Name**: This name is used as the title of your app launcher icon for the new module.
   - **Module Name**: This text is used as the name of the folder where your source code and resources files are visible.
   - **Package Name** : This is the Java namespace for the code in your module. It is added as the[`package`](https://developer.android.com/guide/topics/manifest/manifest-element#package)attribute in the module's[Android manifest file](https://developer.android.com/guide/topics/manifest/manifest-intro).**Important:**Module package names must be globally unique. You can't have two modules with the same package name in the same project.
   - **Minimum SDK** : This setting indicates the lowest version of the Android platform that the app module supports. This value sets the`minSdkVersion`attribute in the`build.gradle`file, which you can edit later.

   Then click**Next**.
4. Depending on which device module you selected, the following page displays a selection of appropriate code templates you can select to use as your main activity. Click an activity template with which you want to start, and then click**Next** . If you don't need an activity, click**Add No Activity** , click**Finish**, and then you're done.
5. If you chose an activity template, enter the settings for your activity on the**Customize the Activity** page. Most templates ask for an**Activity Name** ,**Layout Name** ,**Title** , and**Source Language** , but each template has activity-specific settings. Click**Finish**. When you create an app module with an activity template, you can immediately run and test the module on your device.

Android Studio creates all the necessary files for the new module and syncs the project with the new module gradle files. Adding a module for a new device also adds any required dependencies for the target device to the module's build file.

Once the Gradle project sync completes, the new module appears in the**Project** window on the left. If you don't see the new module folder, make sure the window is displaying the[Android view](https://developer.android.com/studio/projects#ProjectFiles).

## Import a module

To import an existing module into your project, proceed as follows:

1. Click**File \> New \> Import Module**.
2. In the**Source directory** box, type or select the directory of the module(s) that you want to import:
   - If you are importing one module, indicate its root directory.
   - If you are importing multiple modules from a project, indicate the project folder. For each module inside the folder, a box appears and indicates the**Source location** and**Module name** . Make sure the**Import**box is checked for each module that you want to import.

   If your module(s) have other dependencies, they will be listed to import under**Additional required modules**.
3. Type your desired module name(s) in the**Module name**field(s).
4. Click**Finish.**

Once the module is imported, it appears in the[**Project**window](https://developer.android.com/studio/projects/index.html#ProjectFiles)on the left.

## Next steps

Once you've added a new module, you can modify the module code and resources, configure module build settings, and build the module. You can also run and debug the module like any other app.

- To learn about build settings for a module, see[The Module-level Build File](https://developer.android.com/studio/build#module-level).
- To build and run a specific module, see[Select and build a different module](https://developer.android.com/studio/run#build-module).

You'll also want to add code and resources to properly support the new device. For more information about how to develop app modules for different device types, see the corresponding documentation:

- For Wear OS modules:[Creating and Running a Wearable App](https://developer.android.com/training/wearables/apps/creating.html)
- For Android TV modules:[Get Started with TV Apps](https://developer.android.com/training/tv/start/start.html)
- For Glass modules:[GDK Quick Start](https://developers.google.com/glass/develop/gdk/quick-start#for_android_experts)

As you develop your new module, you might create device independent code that is already duplicated in a different app module. Instead of maintaining duplicate code, consider moving the shared code to a library module and adding the library as a dependency to your app modules. For more information on creating a library module and adding it as a dependency, see[Create an Android Library](https://developer.android.com/studio/projects/android-library).