---
title: https://developer.android.com/tools/bundletool
url: https://developer.android.com/tools/bundletool
source: md.txt
---

`bundletool`is the underlying tool that Android Studio, the Android Gradle plugin, and Google Play use to build an Android App Bundle.`bundletool`can convert an app bundle into the various APKs that are deployed to devices.

Android SDK Bundles (ASBs) and their APKs are built with`bundletool`. It is also available as a command-line tool, so you can build app bundles and SDK bundles yourself and re-create Google Play's server-side build of your app's APKs or your[runtime-enabled SDK's](https://developer.android.com/design-for-safety/privacy-sandbox/sdk-runtime)APKs.

## Download`bundletool`

If you haven't already, download`bundletool`from the[GitHub repository](https://github.com/google/bundletool/releases).

## Build and test an app bundle

You can use Android Studio or the`bundletool`command-line tool to build your Android App Bundle and then test generating APKs from this app bundle.

### Build an app bundle

Use Android Studio and the Android Gradle plugin to[build and sign an Android App Bundle](https://developer.android.com/studio/publish/app-signing#sign-apk). However, if using the IDE is not an option---for example, because you are using a continuous build server---you can also[build your app bundle from the command line](https://developer.android.com/studio/build/building-cmdline#build_bundle)and sign it using[`jarsigner`](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jarsigner.html).
| **Note:** You can't use`apksigner`to sign your app bundle.

For more information about building app bundles with`bundletool`, see[Build an app bundle using bundletool](https://developer.android.com/studio/build/building-cmdline#bundletool-build).

### Generate a set of APKs from your app bundle

After you build your Android App Bundle, test how Google Play uses it to generate APKs and how those APKs behave when deployed to a device.

There are two ways you can test your app bundle:

- Use the`bundletool`command-line tool locally.
- [Upload your bundle to the Play Console](https://developer.android.com/studio/publish/upload-bundle)through Google Play by using a test track.

This section explains how to use`bundletool`to test your app bundle locally.

When`bundletool`generates APKs from your app bundle, it includes the generated APKs in a container called an*APK set archive* , which uses the`.apks`file extension. To generate an APK set for all device configurations your app supports from your app bundle, use the`bundletool build-apks`command, as shown:  

```
bundletool build-apks --bundle=/MyApp/my_app.aab --output=/MyApp/my_app.apks
```

If you want to deploy the APKs to a device, you also need to include your app's signing information, as shown in the following command. If you don't specify signing information,`bundletool`attempts to sign your APKs with a debug key for you.  

```
bundletool build-apks --bundle=/MyApp/my_app.aab --output=/MyApp/my_app.apks
--ks=<var translate="no">/MyApp/keystore.jks</var>
--ks-pass=file:<var translate="no">/MyApp/keystore.pwd</var>
--ks-key-alias=<var translate="no">MyKeyAlias</var>
--key-pass=file:<var translate="no">/MyApp/key.pwd</var>
```

The following table describes the various flags and options you can set when using the`bundletool build-apks`command in greater detail:

**Table 1.** Options for the`bundletool build-apks`command

|                                                       Flag                                                        |                                                                                                                                                                                                                                                                                                                                                                        Description                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--bundle=`<var translate="no">path</var>                                                                         | **(Required)** Specifies the path to the app bundle you built using Android Studio. To learn more, read[Build your project](https://developer.android.com/studio/run#reference).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `--output=`<var translate="no">path</var>                                                                         | **(Required)** Specifies the name of the output`.apks`file, which contains all the APK artifacts for your app. To test the artifacts in this file on a device, follow the steps in the section about how to[deploy APKs to a connected device](https://developer.android.com/tools/bundletool#deploy_with_bundletool).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--overwrite`                                                                                                     | Overwrites any existing output file with the path you specify using the`--output`option. If you don't include this flag and the output file already exists, you get a build error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `--aapt2=`<var translate="no">path</var>                                                                          | Specifies a custom path to AAPT2. By default,`bundletool`includes its own version of AAPT2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--ks=`<var translate="no">path</var>                                                                             | (Optional) Specifies the path to the deployment keystore used to sign the APKs. If you don't include this flag,`bundletool`attempts to sign your APKs with a debug signing key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--ks-pass=pass:`<var translate="no">password</var> or `--ks-pass=file:`<var translate="no">/path/to/file</var>   | Specifies your keystore password. If you specify a password in plain text, qualify it with`pass:`. If you pass the path to a file that contains the password, qualify it with`file:`. If you specify a keystore using the`--ks`flag without specifying`--ks-pass`,`bundletool`prompts you for a password from the command line.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--ks-key-alias=`<var translate="no">alias</var>                                                                  | Specifies the alias of the signing key you want to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `--key-pass=pass:`<var translate="no">password</var> or `--key-pass=file:`<var translate="no">/path/to/file</var> | Specifies the password for the signing key. If you specify a password in plain text, qualify it with`pass:`. If you pass the path to a file that contains the password, qualify it with`file:`. If this password is identical to the one for the keystore itself, you can omit this flag.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--connected-device`                                                                                              | Instructs`bundletool`to build APKs that target the configuration of a connected device. If you don't include this flag,`bundletool`generates APKs for all device configurations your app supports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `--device-id=`<var translate="no">serial-number</var>                                                             | If you have more than one connected device, use this flag to specify the serial ID of the device to which you want to deploy your app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--device-spec=`<var translate="no">spec_json</var>                                                               | Provides a path to a`.json`file that specifies the device configuration you want to target. To learn more, go to the section about how to[Generate and use device specification JSON files](https://developer.android.com/tools/bundletool#generate_use_json).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--mode=universal`                                                                                                | Sets the mode to`universal`. Use this option if you want`bundletool`to build a single APK that includes all of your app's code and resources, so that the APK is compatible with all device configurations your app supports. **Note:** `bundletool`includes only feature modules that specify`<dist:fusing dist:include="true"/>`in their manifest in a universal APK. To learn more, read about the[feature module manifest](https://developer.android.com/studio/projects/dynamic-delivery#dynamic_feature_manifest). Keep in mind, these APKs are larger than those optimized for a particular device configuration. However, they're easier to share with internal testers who, for example, want to test your app on multiple device configurations. |
| `--local-testing`                                                                                                 | Enables your app bundle for local testing. Local testing allows for quick, iterative testing cycles without the need to upload to Google Play servers. For an example of how to test module installation using the`--local-testing`flag, see[Locally test module installs](https://developer.android.com/guide/app-bundle/test/testing-fakesplitinstallmanager).                                                                                                                                                                                                                                                                                                                                                                                           |

### Deploy APKs to a connected device

After you generate a set of APKs,`bundletool`can deploy the right combination of APKs from that set to a connected device.

For example, if you have a connected device running Android 5.0 (API level 21) or higher,`bundletool`pushes the base APK, feature module APKs, and configuration APKs required to run your app on that device. Alternatively, if your connected device is running Android 4.4 (API level 20) or lower,`bundletool`searches for a compatible multi-APK to deploy to your device.

To deploy your app from an APK set, use the`install-apks`command and specify the path of the APK set using the`--apks=`<var translate="no">/path/to/apks</var>flag, as shown in the following command. If you have multiple devices connected, specify a target device by adding the`--device-id=`<var translate="no">serial-id</var>flag.  

```
bundletool install-apks --apks=/MyApp/my_app.apks
```
| **Note:** If you're using the`--local-testing`flag with the`build-apks`command, use`install-apks`to install your APKs to ensure that local testing works correctly.

### Generate a device-specific set of APKs

If you don't want to build a set of APKs for all device configurations your app supports, you can build APKs that target only the configuration of a connected device using the`--connected-device`option, as shown in the following command. If you have multiple devices connected, specify a target device by including the`--device-id=`<var translate="no">serial-id</var>flag.  

```
bundletool build-apks --connected-device
--bundle=/MyApp/my_app.aab --output=/MyApp/my_app.apks
```

#### Generate and use device specification JSON files

`bundletool`can generate an APK set that targets a device configuration specified by a JSON file. To first generate a JSON file for a connected device, run the following command:  

```
bundletool get-device-spec --output=/tmp/device-spec.json
```

`bundletool`creates a JSON file for your device in the tool's directory. You can then pass the file to`bundletool`to generate a set of APKs that target only the configuration described in that JSON file, as follows:  

```
bundletool build-apks --device-spec=<var translate="no">/MyApp/pixel2.json</var>
--bundle=/MyApp/my_app.aab --output=/MyApp/my_app.apks
```

#### Manually create a device specification JSON

If you don't have access to the device for which you want to build a targeted APK set---for example, if you want to try your app with a device you don't have on hand---you can manually create a JSON file using the following format:  

    {
      "supportedAbis": ["arm64-v8a", "armeabi-v7a"],
      "supportedLocales": ["en", "fr"],
      "screenDensity": 640,
      "sdkVersion": 27
    }

You can then pass this JSON to the`bundle extract-apks`command, as described in the previous section.

### Extract device-specific APKs from an existing APK set

If you have an existing APK set and you want to extract from it a subset of APKs that target a specific device configuration, you can use the`extract-apks`command and specify a device specification JSON, as follows:  

```
bundletool extract-apks
--apks=/MyApp/my_existing_APK_set.apks
--output-dir=/MyApp/my_pixel2_APK_set.apks
--device-spec=/MyApp/bundletool/pixel2.json
```

### Measure the estimated download sizes of APKs in an APK set

To measure the estimated download sizes of APKs in an APK set as they would be served compressed over the wire, use the`get-size total`command:  

```
bundletool get-size total --apks=/MyApp/my_app.apks
```

You can modify the behavior of the`get-size total`command using the following flags:

**Table 2.** Options for the`get-size total`command

|                        Flag                         |                                                                                                                                         Description                                                                                                                                          |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--apks=`<var translate="no">path</var>             | **(Required)**Specifies the path to the existing APK set file whose download size is being measured.                                                                                                                                                                                         |
| `--device-spec=`<var translate="no">path</var>      | Specifies the path to the device spec file (from`get-device-spec`or constructed manually) to use for matching. You can specify a partial path to evaluate a set of configurations.                                                                                                           |
| `--dimensions=`<var translate="no">dimensions</var> | Specifies the dimensions used when computing the size estimates. Accepts a comma-separated list of:`SDK`,`ABI`,`SCREEN_DENSITY`, and`LANGUAGE`. To measure across all dimensions, specify`ALL`.                                                                                              |
| `--instant`                                         | Measures the download size of the instant-enabled APKs instead of the installable APKs. By default,`bundletool`measures the installable APK download sizes.                                                                                                                                  |
| `--modules=`<var translate="no">modules</var>       | Specifies a comma-separated list of modules in the APK set to consider in the measurement. The`bundletool`command automatically includes any dependent modules for the specified set. By default, the command measures the download size of all modules installed during the first download. |

## Additional resources

To learn more about using`bundletool`, watch[App Bundles: Testing bundles with bundletool and the Play Console](https://www.youtube.com/watch?v=vAEAZPU7w-I).