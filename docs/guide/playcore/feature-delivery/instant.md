---
title: https://developer.android.com/guide/playcore/feature-delivery/instant
url: https://developer.android.com/guide/playcore/feature-delivery/instant
source: md.txt
---

# Configure instant delivery

[Google Play Instant](https://developer.android.com/topic/google-play-instant/overview)allows users to interact with your app without needing to install APK(s) on their device. Instead, they can experience your app through the "Try Now" button on the Google Play Store or a URL that you create. This form of delivering content makes it easier for you to increase engagement with your app.

You can instant-enable a feature only if you also instant-enable your app's base module. That's because, if a user wants to experience one of your app's instant-enabled feature modules, their device must also download your app's base module for common code and resources. Keep in mind, to support Google Play Instant, the download for your base module and feature must satisfy several criteria:

- **Maximum size:** The combined size of your instant-enabled base module and your instant-enabled feature module must be at most 10 MB. To learn more, read[Enable instant experiences by reducing app or game size](https://developer.android.com/topic/google-play-instant/overview#reduce-size).
- **Background activity:** An instant-enabled module cannot use[background services](https://developer.android.com/training/run-background-service/create-service). Additionally, such a module cannot[send notifications](https://developer.android.com/training/notify-user/build-notification)when running in the background.

If you create an instant-enabled feature module using[Android Studio 3.5](https://developer.android.com/studio)or higher, as described in this section, the IDE automatically instant-enables both the base and feature module for you by including the following in each module's manifest:  

    <manifest xmlns:dist="http://schemas.android.com/apk/distribution"
        ... >
        <dist:module dist:instant="true" />
        ...

Additionally, when downloading and*installing*your app, instant-enabled feature modules are automatically downloaded and installed with your app's base APK. So, the IDE also includes the following in the instant-enabled feature module.  

        <dist:module ...>
            <dist:delivery>
                <dist:install-time />
            </dist:delivery>
        </dist:module>

This behavior means that when you set`dist:instant="true"`, you cannot also include`<dist:on-demand />`. However, you can request instant-enabled modules on demand*within your instant experience* [using the Play Feature Delivery Library](https://developer.android.com/guide/playcore#java-kotlin-asset-delivery).

### Configure a new module for instant delivery

To add an instant-enabled feature module to your app project using Android Studio, proceed as follows:

1. If you haven't already done so, open your app project in the IDE.
2. Select**File \> New \> New Module**from the menu bar.
3. In the**Create New Module** dialog, select**Instant Dynamic Feature Module** and click**Next**.
4. In the**Configure your new module**section, complete the following:

   1. Select the**Base application module**for your app project from the dropdown menu.
   2. Specify a**Module name** . The IDE uses this name to identify the module as a Gradle subproject in your[Gradle settings file](https://developer.android.com/studio/build#settings-file). When you build your app bundle, Gradle uses the last element of the subproject name to inject the`<manifest split>`attribute in the[feature module's manifest](https://developer.android.com/guide/playcore/feature-delivery/instant#dynamic_feature_manifest).
   3. Specify the module's**package name**. By default, Android Studio suggests a package name that combines the root package name of the base module and the module name you specified in the previous step.
   4. Select the**Minimum API level**you want the module to support. This value should match that of the base module.
   5. Specify the**Module title** using up to 50 characters. The platform uses this title to identify the module to users. For this reason, your app's base module must include the module title as a[string resource](https://developer.android.com/guide/topics/resources/string-resource), which you can translate. When creating the module using Android Studio, the IDE adds the string resource to the base module for you and injects the following entry in the feature module's manifest:

          <dist:module
              ...
              dist:title="@string/feature_title">
          </dist:module>

      | **Note:** If you enable resource shrinking, such as for your release builds, the shrinker may remove the module title string resource if code in your base module does not reference it. To make sure the string resource remains in the build output, include the resource in a[custom resource keep file](https://developer.android.com/studio/build/shrink-code#keep-resources).
   6. Check the box next to**Fusing**if you want this module to be available to devices running Android 4.4 (API level 20) and lower and included in multi-APKs. Android Studio injects the following in the module's manifest to reflect your choice.

          <dist:module>
              <dist:fusing dist:include="true" />
          </dist:module>

5. Click**Finish**.

After Android Studio finishes creating your module, inspect its contents yourself from the**Project** pane (select**View \> Tool Windows \> Project**from the menu bar). The default code, resources, and organization should be similar to those of the standard app module.

After you implement a feature that you want to download on demand, learn how to request it[using the Play Feature Delivery Library](https://developer.android.com/guide/playcore#java-kotlin-asset-delivery).

## Deploy your app

While you're developing your app with support for feature modules, you can deploy your app to a connected device like you normally would by selecting**Run \> Run** from the menu bar (or by clicking**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png)in the toolbar).

If your app project includes one or more feature modules, you can choose which features to include when deploying your app by modifying your existing[run/debug configuration](https://developer.android.com/studio/run/rundebugconfig)as follows:

1. Select**Run \> Edit Configurations**from the menu bar.
2. From the left panel of the**Run/Debug Configurations** dialog, select your desired**Android App**configuration.
3. Under**Dynamic features to deploy** in the**General**tab, check the box next to each feature module you want to include when deploying your app.
4. Click**OK**.

By default, Android Studio doesn't deploy your instant-enabled modules as an instant experience or use app bundles to deploy your app. Instead, the IDE builds and installs APKs to your device that are optimized for deployment speed, rather than APK size. To configure Android Studio to instead build and deploy APKs and instant experiences from an app bundle,[modify your run/debug configuration](https://developer.android.com/studio/run/rundebugconfig#android-application).