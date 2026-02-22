---
title: https://developer.android.com/training/wearables/watch-face-push
url: https://developer.android.com/training/wearables/watch-face-push
source: md.txt
---

Wear OS 6 introduces a new API, Watch Face Push, which creates opportunities for
more advanced watch face publishing use cases.

## Identify when to use Watch Face Push

Watch Face Push is an API on Wear OS that allows the developer to add, update,
or remove watch faces directly. It isn't needed for standard watch face
development.

Watch faces used with Watch Face Push must be written using the Watch Face
Format. This can include watch faces designed using Watch Face Designer,
Watch Face Studio, or any other tool that produces watch faces that use the
Watch Face Format.

While the Watch Face Push API can potentially be used in a number of ways, the
following table guides you through the main use cases:

| Use case | Recommended solution | Complexity |
|---|---|---|
| I want to create individual watch faces and publish them. | Use Watch Face Format, either directly or through a tool such as Watch Face Designer or Watch Face Studio, and publish them on Google Play. | Low |
| I want to create a phone app that allows users to select watch faces from a curated collection, or design and customize watch faces for installation directly on their Wear OS watch. | Create an app, for both watch and phone, using the Watch Face Push API on the watch. | High |

## Purpose

The canonical use case for the Watch Face Push API is for creating a
*marketplace* app. From this app, users can select watch faces from a curated
collection on their phone, and directly control the installation of these watch
faces onto their connected watch.

## Considerations

For details on building your watch faces, consult the [Watch Face Format](https://developer.android.com/training/wearables/wff)
guidance: Watch faces deployed using Watch Face Push are regular Watch Face
Format watch faces.

When building your watch face, keep the following considerations in mind.

### Package names

Watch faces installed using Watch Face Push must conform to the following
convention:

`<app name>.watchfacepush.<watchface name>`

... where `<app name>` is the package name of the app calling the Watch Face
Push API.

For example, for an app with package name `com.example.mymarketplace`, the
following are valid watch face package names:

- `com.example.mymarketplace.watchfacepush.watchface1`
- `com.example.mymarketplace.watchfacepush.watchface2`
- `com.example.mymarketplace.watchfacepush.another_watchface`

The API rejects watch faces that don't conform with this convention.

### Package contents

The system strictly enforces APK contents. It is technically possible to produce
Watch Face Format APKs that contain innocuous metadata files and other
artifacts, which might be acceptable to Google Play but don't pass the Watch
Face Push validation (see below).

Each watch face APK must contain only the following files/paths:

- `/AndroidManifest.xml`
- `/resources.arsc`
- `/res/**`
- `/META-INF/**`

Additionally, the `AndroidManifest.xml` file must contain only the following
tags:

- `<manifest>`
- `<uses-feature>`
- `<uses-sdk>`
- `<application>`
- `<property>`
- `<meta-data>`

Finally, the package must specify a `minSdk` of at least `33`, and the
`<application>` tag must specify the attribute `android:hasCode="false"`.

### Validation

Unlike regular watch faces distributed through Google Play, the Marketplace app
is responsible for verifying that each Watch Face Push watch face is well formed
and performant.

Watch Face Push uses the following validation checks to verify the quality of
each watch face:

1. All watch faces installed or updated through the Watch Face Push API must pass the Watch Face Push validation tool.
2. Use only the official validation tool to generate *validation tokens* for use with the API.
3. The validation tool must be up-to-date when you run the validation.
4. You don't need to re-validate an APK that has not changed. Tokens don't
   expire, even when the version of the validation tool used is superseded.

   At the same time, we recommend that you re-run the validation once in a
   while, because the validator is updated periodically.

#### Run the validator

The validator is available in three forms:

- A CLI tool
- A library for use with the JVM
- A library for use on Android

#### Command-line validator usage

1. Obtain the validator from Google's [Maven repository](https://maven.google.com/web/index.html#com.google.android.wearable.watchface.validator:validator-push-cli).
2. Run the tool as follows:

       java -jar validator-push-cli-1.0.0-alpha07.jar \
           --apk_path=<your watch face>.apk \
           --package_name=<your marketplace package name>

   If successful, the output includes a *validation token*, which you must
   supply to the Watch Face Push API when adding or updating a watch face.

   If an error occurs, the output includes details about which particular
   check failed.

#### Library validator usage

1. Include the Google and Jitpack repositories. Both are required in order to
   use the validator library.

       repositories {
           ...
           google()
           maven {
               url = uri("https://jitpack.io")
               content {
                   includeGroup("com.github.xgouchet")
               }
           }
       }

2. Include the validator dependency in your project:

       // For use on JVM
       implementation("com.google.android.wearable.watchface.validator:validator-push:1.0.0-alpha07")

       // For use on Android
       implementation("com.google.android.wearable.watchface.validator:validator-push-android:1.0.0-alpha07")

3. Run the validator:

val validator = DwfValidatorFactory.create() val result = validator.validate(watchFaceFile, appPackageName) if (result.failures().isEmpty()) { val token = result.validationToken() println("Validation token: $token") // Validation success - continue with the token // ... } else { // There were failures, handle them accordingly - validation has failed. result.failures().forEach { failure -\> println("FAILURE: ${failure.name()}: ${failure.failureMessage()}") // ... } }[Main.kt](https://github.com/android/snippets/blob/fbed24d5695413cfd86b4b2c6b6faf0a3a2eadb8/watchfacepush/validator/src/main/kotlin/com/example/validator/Main.kt#L39-L54)

For an example of using this library, see the [GitHub sample](https://github.com/android/wear-os-samples/tree/main/WatchFacePush). See also the
[Portable Asset Compiler Kit (Pack)](https://github.com/google/pack) library, which is useful for building
APKs on-device, for use with the Android-based validator.

### APK size

Take particular care with Watch Face Push watch faces to minimize APK size: The
watch face APK is likely to be transmitted from the phone app to the watch app
over Bluetooth, which can be slow.

An overly large APK could take a considerable time to transmit, which is both a
poor user experience and also draining on battery.

- Use appropriate libraries such as [`pngquant`](https://pngquant.org/) to keep image file sizes to a minimum
  - Include this in your watch face collection build process
  - Check dimensions of the image are appropriate for the scale at which you use it.
  - Crop images are appropriately to remove any surrounding background.
- Reduce the size of font files
  - For example, if you use a particular font only to show the time, in the format `HH:MM`, you can use a tool such as [`pyftsubset`](https://fonttools.readthedocs.io/en/stable/subset/) to limit the font file to only contain the necessary glyphs. This can dramatically reduce the size of the resulting font file and APK. [See
    this blog post for details on minimizing font file
    size](https://markoskon.com/creating-font-subsets/), for other cases.

Refer to the [Optimize memory usage guidance](https://developer.android.com/training/wearables/wff/memory-usage#methods) for further suggestions on
keeping APK size to a minimum.

### APK signing

As a regular APK, you must sign all your watch faces. Create a different key
from the key you use with your main app and use the different key for all your
watch faces.

## Architecture

Consider the four main components of the system:

1. **Cloud-based storage** : In the canonical Marketplace app, you build and store your watch faces in the Cloud, ready for your users to use. The watch faces have the following properties:
   1. They are prebuilt as regular Watch Face Format APKs.
   2. Each APK contains only a single Watch Face Format--based watch face.
   3. They are validated with the Watch Face Push validation process and stored with the associated validation token.
   4. Your phone app can retrieve them as needed.
2. **Phone app** : The phone app is the main way in which your users interact with your system. It allows them to:
   1. Browse and search your catalog of watch faces
   2. Install or replace a watch face on the watch
3. **Watch app** : The watch app may typically not have a significant user interface. It is primarily a bridge between the phone app and the Watch Face Push APIs, with the following functionality:
   1. Using the Watch Face Push API to install/update or replace watch faces
   2. Requesting necessary permissions and prompting the user
   3. Providing a default watch face
   4. Providing a minimal cache of watch faces
4. **Phone-watch communications** : The phone and watch app communication is pivotal to the success of the overall experience. Use Wear OS Data Layer APIs, which allow:
   1. **Installation detection** : Using Capabilities and the [`CapabilityClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/CapabilityClient), the phone app can [detect the
      absence of the watch app](https://developer.android.com/training/wearables/apps/standalone-apps#detecting-your-app), and the other way around. You can then launch an intent to the Play store to install the missing form factor.
   2. **State management** : Using the [`DataClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/DataClient) or [`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient) you keep the phone in sync with the state of the watch, for example, synchronizing the state of the active watch face.
   3. **APK transmission** : Using [`ChannelClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/ChannelClient) or [`MessageClient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient), send APKs from the phone to the watch
   4. **Remote invocation** : Using [`Messageclient`](https://developers.google.com/android/reference/com/google/android/gms/wearable/MessageClient), the phone can instruct the watch to call the Watch Face Push API, for example, to install a watch face.

Refer to [the Data Layer API guidance](https://developer.android.com/training/wearables/data/overview) for further details.