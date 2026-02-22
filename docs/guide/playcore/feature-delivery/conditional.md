---
title: https://developer.android.com/guide/playcore/feature-delivery/conditional
url: https://developer.android.com/guide/playcore/feature-delivery/conditional
source: md.txt
---

# Configure conditional delivery

Conditional delivery allows you to set certain device configuration requirements for feature modules to be downloaded automatically during app install. For example, you can configure a feature module that includes functionality for augmented reality (AR) to be available at app install for only devices that support AR.

This delivery mechanism currently supports controlling the download of a module at app install-time based on the following device configurations:

- [Device hardware and software features](https://developer.android.com/guide/playcore/feature-delivery/conditional#new-conditional), including OpenGL ES version
- [User country](https://developer.android.com/guide/playcore/feature-delivery/conditional#country-condition)
- [API level](https://developer.android.com/guide/playcore/feature-delivery/conditional#minapi-condition)
- [Device model](https://developer.android.com/guide/playcore/feature-delivery/conditional#device-targeting-condition)
- [Device RAM](https://developer.android.com/guide/playcore/feature-delivery/conditional#device-targeting-condition)
- [System features](https://developer.android.com/guide/playcore/feature-delivery/conditional#device-targeting-condition)
- [System on Chip](https://developer.android.com/guide/playcore/feature-delivery/conditional#device-targeting-condition)(for devices with API level at least 31)

If a device does not meet all the requirements you specify, the module is not downloaded at app install-time. However, your app may later request to[download the module on demand](https://developer.android.com/guide/app-bundle/playcore)using the Play Core SDK.

Before you get started, make sure you're using Android Studio 3.5 or higher. The following sections show you how to add support for conditional delivery to your feature modules.

## Add a new module with conditional delivery options

The easiest way to create a new feature module with conditional delivery is through the**New Module**wizard, as follows:

1. To open the**New Module** dialog, select**File \> New \> New Module**from the menu bar.
2. In the New Module dialog, select**Dynamic Feature Module** and click**Next**.
3. Configure your module as you normally would and click**Next**.
4. In the**Module Download Options**section, complete the following:

   1. Specify the**Module title** using up to 50 characters. The platform uses this title to identify the module to users when, for example, confirming whether the user wants to download the module. For this reason, your app's base module must include the module title as a[string resource](https://developer.android.com/guide/topics/resources/string-resource), which you can translate. When creating the module using Android Studio, the IDE adds the string resource to the base module for you and injects the following entry in the feature module's manifest:

          <dist:module
              ...
              dist:title="@string/feature_title">
          </dist:module>

      | **Note:** If you enable resource shrinking, such as for your release builds, the shrinker may remove the module title string resource if code in your base module does not reference it. To make sure the string resource remains in the build output, include the resource in a[custom resource keep file](https://developer.android.com/studio/build/shrink-code#keep-resources).
   2. In the dropdown menu under**Install-time inclusion** , select**Only include module at app install for devices with specified features**, which creates a module that's included with your app at app install-time on only devices with certain configurations that you can specify, such as device features or country. Android Studio injects the following in the module's manifest to reflect your choice:

          <dist:module ... >
            <dist:delivery>
                <dist:install-time>
                    <dist:conditions>
                        <!-- If you specify conditions, as described in the steps
                             below, the IDE includes them here. -->
                    </dist:conditions>
                </dist:install-time>
            </dist:delivery>
          </dist:module>

   3. If you want to limit automatic download of the module to certain countries or a minimum API level, click**Finish** to complete creating the module and then read the section about how to[specify conditions based on country](https://developer.android.com/guide/playcore/feature-delivery/conditional#country-condition)or[minimum API level](https://developer.android.com/guide/playcore/feature-delivery/conditional#minapi-condition). Otherwise, click**+ device feature**to add a feature that a device requires in order to download the module at install-time.

   4. Next to**device-feature**, select one of the following options from the dropdown menu and specify its value:

      - **Name:** Allows you to specify a hardware or software feature that a device requires in order to download the module at install-time. The features that conditional delivery supports are the same as those listed as`FEATURE_*`constants by[`PackageManager`](https://developer.android.com/reference/android/content/pm/PackageManager#constants). If you select this option, start typing any part of the constant value of the feature, such as "bluetooth", in the field next to the dropdown, and select one of the suggestions that appear.
      - **OpenGL ES Version:**Allows you to specify a version of OpenGL ES that a device requires in order to download the module at install time. If you select this option, start typing the version, such as "0x00030001", in the field next to the dropdown, and select one of the suggestions that appear.
   5. If you want to add multiple conditions based on available device features, click**+ device feature**for each device feature condition you want to specify.

   6. Check the box next to**Fusing**if you want this module to be available to devices running Android 4.4 (API level 20) and lower and included in multi-APKs. This means you can enable on demand behavior for this module and disable fusing to omit it from devices that don't support downloading and installing split APKs. Android Studio injects the following in the module's manifest to reflect your choice:

          <dist:module ...>
              <dist:fusing dist:include="true | false" />
          </dist:module>

5. When you're done configuring module download options, click**Finish**.

Note that the Android Gradle plugin does not support running[lint](https://developer.android.com/studio/write/lint)from dynamic-feature modules. Running lint from the corresponding application module will run lint on its dynamic-feature modules and include all issues in the app's lint report.

## Add conditional delivery options to an existing feature module

You can easily add conditional delivery options to an existing feature module through the module's manifest. However, you should first read about the[compatibility of conditional delivery options](https://developer.android.com/guide/playcore/feature-delivery/conditional#dist-compat)with other delivery options you may already have enabled.

To get started, you need to first migrate your manifest to the new`<dist:delivery>`element. The code snippet below shows an example of the older syntax:  

    <!-- This is the old syntax. -->
    <dist:module
      dist:title="@string/feature_title" dist:onDemand="true">
      <dist:fusing dist:include="true"/>
    </dist:module>

The delivery options above are now specified as follows.  

    <dist:module
      dist:title="@string/feature_title">
      <dist:delivery>
          <dist:on-demand/>
      </dist:delivery>
      <dist:fusing dist:include="true"/>
    </dist:module>

You can then include conditional delivery options based on device features as follows.  

    <dist:module
        dist:title="@string/feature_title">
        <dist:delivery>
          <dist:on-demand/>
          <dist:install-time>
            <dist:conditions>
              <!-- Requires that the device support AR to download the module at
              app install-time.  -->
              <dist:device-feature dist:name="android.hardware.camera.ar"/>
            </dist:conditions>
          </dist:install-time>
        </dist:delivery>
        <dist:fusing dist:include="true"/>
    </dist:module>

The sections below discuss other options for conditional delivery, such as by country or minimum API level.

## Compatibility with other module download options

Because feature modules offer multiple options to configure how each feature is delivered to a user's device, it's important to understand how conditional delivery options are affected by other settings. The following table summarizes compatibility of conditional delivery with other module download options.

|                 Module download option                 |                                                                                                                                   Compatibility with conditional delivery                                                                                                                                   |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fusing (`<dist:fusing dist:include="true"/>`)          | If a module sets this option to true, Google Play does not respect the conditional delivery options you specify when deploying your app to devices running API level 19 or lower. That is, feature modules that enable fusing are always included at install time for device running API level 19 or lower. |
| Instant-enabled (`<dist:module dist:instant="true"/>`) | Conditional delivery options are not supported for instant-enabled feature modules.                                                                                                                                                                                                                         |
| On demand (`<dist:on-demand/>`)                        | By default, if you specify conditional delivery options, the module is also available on demand.                                                                                                                                                                                                            |

## Specify conditions based on country

Conditional delivery also allows you to specify which countries you want to exclude (or include) from downloading your module at app install-time. Specifying this condition might be useful if, for example, your module implements a payment method that's not available in certain regions.

In this context, the device country is typically determined by the user's billing address registered on their Google Play account.

To specify countries for your module, include the following in the feature module's manifest.  

    <dist:conditions>
       <!-- Set to "true" to specify countries to exclude from downloading
       this module at app install-time. By default, modules are available
       for download to all user countries. -->
      <dist:user-countries dist:exclude="true">
        <!-- Specifies the two-letter  CLDR country code for regions that should
        not download the module at app install-time. -->
        <dist:country dist:code="CN"/>
        <dist:country dist:code="HK"/>
      </dist:user-countries>
    </dist:conditions>

## Specify conditions for API level

Specifying a condition based on a device's API level can be useful if a feature module depends on APIs that are available in only certain versions of the Android platform.

To set a condition based on a minimum or maximum device API level, include the following in your feature module's manifest.  

```xml
<dist:conditions>
    <!-- Specifies the minimum API level that the device must satisfy
         in order to download your module at app install-time. The API level you
         specify must be greater or equal to the module's own minSdkVersion. -->
   <dist:min-sdk dist:value="21"/>
    <!-- Specifies the maximum API level that the device cannot exceed
         in order to download your module at app install-time. The API level you
         specify must be less than or equal to the module's own maxSdkVersion. -->
   <dist:max-sdk dist:value="24"/>
</dist:conditions>
```

## Specify conditions for other device properties (beta)

To specify conditions for other device properties, such as model name, RAM, system features, and system on chip, you can use a device targeting configuration file.

To create a device targeting configuration file, see the[documentation for device targeting](https://developer.android.com/google/play/device-targeting).

Once you have created the configuration file, you can specify device groups for your module by including the following in the feature module's manifest.  

    <dist:conditions>
       <dist:device-groups>
          <dist:device-group dist:name="myCustomGroup1"/>
          <dist:device-group dist:name="myCustomGroup2"/>
       </dist:device-groups>
    </dist:conditions>