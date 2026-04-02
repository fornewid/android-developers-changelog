---
title: https://developer.android.com/guide/playcore/feature-delivery/install-time
url: https://developer.android.com/guide/playcore/feature-delivery/install-time
source: md.txt
---

# Configure install-time delivery

Feature modules allow you to separate certain features and resources from the base module of your app and include them in your app bundle. You can then[customize delivery options](https://developer.android.com/guide/playcore/feature-delivery#customize_delivery)to control when and how devices running Android 5.0 (API level 21) or higher download your app's features.

Keep in mind, this type of modularization requires more effort and possibly refactoring your app's existing code, so consider carefully which of your app's features would benefit the most from being available to users on demand.

If you want to gradually modularize app features over time, without changing the behavior of your app or customizing advanced delivery options, you can do so by creating feature modules that are configured for install-time delivery. That is, you can modularize a feature as a feature module, but not enable advanced options so the feature is available when a user installs your app.

Additionally, feature modules that are configured for install-time delivery have the option to later be uninstalled if they're no longer required. For that, they need to be[set up as removable](https://developer.android.com/guide/playcore/feature-delivery/install-time#make-removable).

This section describes how to create a feature module for install-time delivery. Before you begin, make sure you're using[Android Studio 3.5](https://developer.android.com/studio)or higher and Android Gradle Plugin 3.5.0 or higher.

## Configure a new module for install-time delivery

The easiest way to create a new feature module is by using[Android Studio 3.5](https://developer.android.com/studio)or higher. Because feature modules have an inherent dependency on the base app module, you can add them only to existing app projects.

To add a feature module to your app project using Android Studio, proceed as follows:

1. If you haven't already done so, open your app project in the IDE.
2. Select**File \> New \> New Module**from the menu bar.
3. In the**Create New Module** dialog, select**Dynamic Feature Module** and click**Next**.
4. In the**Configure your new module** section, complete the following:
   1. Select the**Base application module**for your app project from the dropdown menu.
   2. Specify a**Module name** . The IDE uses this name to identify the module as a Gradle subproject in your[Gradle settings file](https://developer.android.com/studio/build#settings-file). When you build your app bundle, Gradle uses the last element of the subproject name to inject the`<manifest split>`attribute in the[feature module's manifest](https://developer.android.com/guide/app-bundle/dynamic-delivery#dynamic_feature_manifest).
   3. Specify the module's**package name**. By default, Android Studio suggests a package name that combines the root package name of the base module and the module name you specified in the previous step.
   4. Select the**Minimum API level**you want the module to support. This value should match that of the base module.
5. Click**Next**.
6. In the**Module Download Options**section, complete the following:

   1. Specify the**Module title** using up to 50 characters. Your app's base module must include the module title as a[string resource](https://developer.android.com/guide/topics/resources/string-resource), which you can translate. When creating the module using Android Studio, the IDE adds the string resource to the base module for you and injects the following entry in the feature module's manifest:

          <dist:module
              ...
              dist:title="@string/feature_title">
          </dist:module>

      | **Note:** If you enable resource shrinking, such as for your release builds, the shrinker might remove the module title string resource if code in your base module does not reference it. To make sure the string resource remains in the build output, include the resource in a[custom resource keep file](https://developer.android.com/studio/build/shrink-code#keep-resources).
   2. In the dropdown menu under**Install-time inclusion** , select**Include module at install-time**. Android Studio injects the following in the module's manifest to reflect your choice:

          <dist:module ... >
            <dist:delivery>
                <dist:install-time />
            </dist:delivery>
          </dist:module>

      If you want to learn how to create a feature module that you can download after app install, read[configure on-demand delivery](https://developer.android.com/studio/projects/dynamic-delivery/on-demand-delivery).
   3. Check the box next to**Fusing**if you want this module to be available to devices running Android 4.4 (API level 20) and lower and included in multi-APKs. That means you can omit it from devices that don't support downloading and installing split APKs. Android Studio injects the following in the module's manifest to reflect your choice:

          <dist:module ...>
              <dist:fusing dist:include="true | false" />
          </dist:module>

7. Click**Finish**.

After Android Studio finishes creating your module, inspect its contents yourself from the**Project** pane (select**View \> Tool Windows \> Project**from the menu bar). The default code, resources, and organization should be similar to those of the standard app module.

## Make an install-time module removable

It might be useful to create feature modules for install-time delivery that have the option to be later uninstalled if no longer required. For example, to reduce the installed size of your app, you can modularize content that's required for training or onboarding, and then[uninstall the feature module](https://developer.android.com/guide/playcore/feature-delivery/on-demand#uninstall_modules)using the Play Core API after the user is set up to use your app.

Install-time modules are not removable by default. To mark a module as removable and allow it to be uninstalled, add the`removable`tag and set its value to`true`:  

    <dist:module ... >
      <dist:delivery>
          <dist:install-time>
              <dist:removable dist:value="true"/>
          </dist:install-time>
      </dist:delivery>
    </dist:module>

| **Note:** Configuring too many install-time modules as removable might increase the download and install time for your app. To avoid this issue, keep the number of removable install-time delivery modules under 10.