---
title: https://developer.android.com/google/play/asset-country-targeting
url: https://developer.android.com/google/play/asset-country-targeting
source: md.txt
---

# Asset Targeting by Country

| **Warning:** Access to the information on this page is governed by a Google non-disclosure agreement.
| **Note:** The features described on this page are currently only available to select Play Partners.
| **Note:** [Use this form](https://support.google.com/googleplay/android-developer/contact/general_contact)to report any issues to Google Play.

## What is Asset Targeting by Country?

Asset targeting by country allows you to deliver different versions (such as resolutions) of the same asset to devices based on the country where the user is located. For example, you may choose to deliver customized assets to different countries where your app is available - all without incurring any increase in overall game size by only delivering the necessary assets to users' devices. This builds upon the concept of asset packs in Play[Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery). As you'll see below, You can define the targeting criteria with up to 20 country sets. In this context, the device country is typically determined by the user's billing address registered on their Google Play account.

Like Play Asset Delivery, targeting by country supports Android 4.1 (API level 16) and higher. However on devices running Android 4.4 (API level 19) or lower, the default country set is delivered regardless of the user location.

## Developer Journey

At a high level, to integrate targeting by country into your existing game, follow the steps:

1. Integrate targeting by country (and by extension, Play Asset Delivery) within your game
   - Integrate Play Asset Delivery into your game (if you haven't already done so)
   - Divide your assets into*asset packs*
   - Package your code and assets together for the final Android App Bundle artifact you will upload to Play.
2. Create your Device Targeting configuration so that Play knows how to deliver your assets to user devices.
   - Set up the Google Play Developer API (if not already completed), which is what you'll use to send the targeting configs to Play.
   - Go through the steps to create the targeting config.
3. Upload your AAB to Play, and test to make sure everything is configured correctly

Gradle is the recommended build system for Java and native games. For games built using Gradle, follow these steps to configure the build system to build out your AAB with country targeting support.

If you export your game to Gradle then finish your build there, we recommend following these instructions (ex. Unity games[exported to Gradle)](https://docs.unity3d.com/Manual/android-gradle-overview.html)).

## Setting up asset targeting by country within your app

### Integrating Play Asset Delivery into your game (if not already completed)

Play Asset Delivery (PAD) allows you to dynamically deliver your game's assets at install time or runtime, and you can read[an overview about it here](https://developer.android.com/guide/app-bundle/asset-delivery). With targeting by country, Play will deliver the content of your asset packs based on the country set configurations you prescribe for different user locations. It is recommended to follow the guidance below and integrate PAD into your game (i.e. create asset packs, implement retrieval in your game), and then modify the project code to enable targeting by country.
| **Note:** The linked resources below do not have the instructions for configuring targeting by country - as such, all resources for a given asset pack will go to all devices. This is ok for now - in the next step, you will separate out assets for each country set.
| **Note:** To use texture compression format targeting or device tiers targeting on the same folder as country set targeting, you can employ[nested targeting](https://developer.android.com/google/play/nested-targeting).

#### Gradle

For games built with Gradle, use these instructions for[building your asset packs with Gradle](https://developer.android.com/guide/app-bundle/asset-delivery/build-native-java), then follow the instructions for integrating asset pack retrieval within your game:

- [Java](https://developer.android.com/guide/playcore/asset-delivery/integrate-java)
- [Native](https://developer.android.com/guide/playcore/asset-delivery/integrate-native)
- Unity games[exported to Gradle](https://docs.unity3d.com/Manual/android-gradle-overview.html)
  - Use[the Java libraries](https://developer.android.com/guide/playcore/asset-delivery/integrate-java)via the JNI (such as[the one built into Unity](https://docs.unity3d.com/Manual/com.unity.modules.androidjni.html)).

### Creating country-set specific directories

| **Note:** You can have at most 20 distinct country sets, and they must have unique alphanumeric names. All asset packs that use country targeting must target the same set of country sets.

#### If using Gradle

You will now split up your assets between the country sets (max 20) you will define later on. Create your targeted directories by taking the**existing**asset bundle directories created in the last step, and post fixing the appropriate folder (as described below) with #countries_latam, #countries_na, etc. When using the asset packs in your game - you will not need to address folders by postfix (in other words, the postfix is automatically stripped during the build process).

After the previous step, this might look like:  

    ...
    .../level1/src/main/assets/character-textures#countries_latam/
    .../level1/src/main/assets/character-textures#countries_na/
    .../level1/src/main/assets/character-textures/
    ...

When you access the files under the folder, you can just use the same path without post fixing, (in this example - I would reference as`level1/assets/character-textures/`without any postfixes).
| **Note:** Play tries to match the user with any of the country sets you targeted. You should always define a non-targeted folder (`level1/assets/character-textures/`in the example above) to handle users who do not match any targeted country sets.

### Building the Android App Bundle

#### Gradle

In your project's`build.gradle`file, configure your dependencies to have the versions below (or higher) for[Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin)and[bundletool](https://developer.android.com/studio/command-line/bundletool):  

    buildscript {
      dependencies {
        classpath 'com.android.tools.build:gradle:8.1.0-alpha01'
        classpath "com.android.tools.build:bundletool:1.14.0"
        ...
      }
      ...
    }

You will also need to update your gradle version to 8.0 or above. You can update this in`gradle/wrapper/gradle-wrapper.properties`within your project.  

    distributionUrl=https://services.gradle.org/distributions/gradle-8.0-rc-1-all.zip

Finally, you will need to use the Play Asset Delivery Library; if you are still using the monolithic Play Core Library, update it to 1.8.3 or above. We recommend switching to the Play Asset Delivery Library and updating to the latest version if possible.  

    dependencies {
      implementation 'com.google.android.play:asset-delivery:2.0.1'
      ...
    }

In the main app module's`build.gradle`file, enable the country targeting split:  

    android {
      bundle {
        countrySet {
          enableSplit true
        }
        ...
      }
      ...
    }

Finally, you can build your[Android App Bundle](https://developer.android.com/guide/app-bundle)(AAB).

- [Android Studio](https://developer.android.com/studio/run/build-for-release)
- [CLI](https://developer.android.com/studio/build/building-cmdline#bundle_build_gradle)

#### Bundletool

[Build your bundle with bundletool](https://developer.android.com/studio/build/building-cmdline#bundletool-build), and[while at the step to customize your AAB](https://developer.android.com/studio/build/building-cmdline#bundleconfig), add the following to your`BundleConfig.pb`file.  

    {
      ...
      "optimizations": {
        "splitsConfig": {
          "splitDimension": [
          ...
          {
            "value": "COUNTRY_SET",
            "negate": false,
            "suffixStripping": {
              "enabled": true,
            }
          }],
        }
      }
    }

### Local Testing

Before moving on, it is recommended to locally test your app bundle to make sure everything is set up correctly. Using[`bundletool`](https://developer.android.com/studio/command-line/bundletool)(1.14.0 or above), you locally build and test your app, explicitly specifying the correct country. You will first use[`build-apks`](https://developer.android.com/studio/command-line/bundletool#generate_apks)to generate a set of`.apks`files, and then deploy your app to a connected device using[`install-apks`](https://developer.android.com/studio/command-line/bundletool#deploy_with_bundletool). You can also specify which country set you'd like to be installed via the`country-set`flag. You can find more info on this method of local testing[here](https://developer.android.com/guide/playcore/asset-delivery/test#local-testing)(please note that this page hasn't yet been updated for targeting by country and is thus missing the`country-set`flag).  

    bundletool build-apks --bundle=/path/to/app.aab --output=/path/to/app.apks --local-testing
    bundletool install-apks --apks=/path/to/app.apks --country-set=latam

**Alternatively** : You can also use[`extract-apks`](https://developer.android.com/studio/command-line/bundletool#extract_apks)to extract a set of APKs for a specific device. Using[`get-device-spec`](https://developer.android.com/studio/command-line/bundletool#generate_use_json)along with specifying the country for this device, however, will*not work* in conjunction with the`--local-testing`flag, meaning you won't be able to test fast-follow or on-demand asset packs.  

    bundletool get-device-spec --output=/path/to/device-spec.json --country-set=latam
    bundletool extract-apks --apks=/path/to/existing_APK_set.apks --output-dir=/path/to/device_specific_APK_set.apks --device-spec=/path/to/device-spec.json

## Creating a Device Targeting Configuration via Google Play Developer API

### Getting started with the Google Play Developer API (if not already completed)

To configure targeting by country (i.e. defining your country sets) you will need to use the[Android Publisher API](https://developers.google.com/android-publisher)to upload your config to Google Play. You can read more about the API at the link above - there are a few[steps you'll need to follow to get started](https://developers.google.com/android-publisher/getting_started):

1. [Create (if needed) and link your API project to your Google Play Console](https://developers.google.com/android-publisher/getting_started#linking_your_api_project).
2. [Set-up an API Access Client](https://developers.google.com/android-publisher/getting_started#setting_up_api_access_clients).

You can find the API reference[here](https://developers.google.com/android-publisher/api-ref/rest)- later on, if you choose to upload your build via the API, you will be using the[Edits methods](https://developers.google.com/android-publisher/edits). Additionally, it is encouraged to[review this page](https://developers.google.com/android-publisher/api_usage)before using the API.

### Using the Device Targeting Configuration API

You can use the following API call to create your device targeting configuration:

#### Create Device Targeting Config

|-----------------|-----------------------------------------------------------------------------------------------------------------|
| HTTP request    | `POST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/deviceTierConfigs` |
| Path parameters | N/A                                                                                                             |
| Request Body    | [Device Targeting Config](https://developer.android.com/google/play/asset-country-targeting#dtco)               |
| Response Body   | [Device Targeting Config](https://developer.android.com/google/play/asset-country-targeting#dtco)               |

##### Device Targeting Config Object

    {
      "user_country_sets": [
        {
          "name": "latam",
          "country_codes": [
            "AR",
            "BR",
            ...
          ]
        },
        {
          "name": "sea",
          "country_codes": [
            "VN",
            "TW",
            ...
          ]
        }
      ]
    }

Fields:

- **device_confid_id**(integer): ID corresponding to this device targeting configuration.
- **user_country_sets** (object): Country set definitions
  - **name**(string): Name of the country set (a string ID you define).
  - **country_codes** (string): Countries that belong to this country set (format:[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

| **Note:**
| You can have at most 20 country sets.

You can follow the instructions below for[validating your Device Targeting Configuration](https://developer.android.com/google/play/asset-country-targeting#validating-dtc)before uploading it to Google Play.

#### Get Device Targeting Config by ID

You can retrieve a specific device targeting configuration by ID using the following call:

|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| HTTP request    | `GET https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/deviceTierConfigs/{deviceTierConfigId}` |
| Path parameters | N/A                                                                                                                                 |
| Request Body    | N/A                                                                                                                                 |
| Response Body   | [Device Targeting Config](https://developer.android.com/google/play/asset-country-targeting#dtco)                                   |

#### Get list of Device Targeting Configs

You can get the last 10 device targeting configurations given the following call (or optimally specify a set of ten using the*page_token*query parameter):

|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTTP request     | `GET https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/deviceTierConfigs`                                                                                        |
| Path parameters  | N/A                                                                                                                                                                                                   |
| Query parameters | **page_token**(optional) - Used to specify a specific group of 10 DTCs. This is useful if you have created more than 10 DTCs, and would like to see DTCs that were created before the most recent 10. |
| Request Body     | N/A                                                                                                                                                                                                   |
| Response Body    | [List of Device Targeting Configs](https://developer.android.com/google/play/asset-country-targeting#dtco) page_token                                                                                 |

### Validating your Device Targeting Configuration

`bundletool`includes two commands that help you validate that your Device Targeting Configuration works as intended before uploading it to Play.

With`bundletool print-device-targeting-config`, you can validate that your JSON file is syntactically correct.  

    bundletool print-device-targeting-config --config=mydtc.json

With`bundletool evaluate-device-targeting-config`, you can evaluate what country set would match a specific device. You can provide the user country through the`--country-code`flag.  

    bundletool evaluate-device-targeting-config --config=mydtc.json --connected-device --country-code=AR

## Uploading your Android App Bundle to Google Play

| **Note:** At this time, using the API is the only way to link a specific device targeting config to your AAB - otherwise, when uploaded through the console, it will simply apply the latest device targeting config to your AAB.
| **Note:** You must opt-in to Play App Signing in order to upload your Android App Bundle. You can find more info in this here as well.

### Via API

You can use the Google Play Developer API to upload your Android App Bundle to Google Play, and link a specific Device Targeting configuration to your build.
| **Note:** If you wish to start creating the release via the API, but finish via the Play Console, you can use the DRAFT as part of your track update call.

There is a[general overview of the Edits methods here](https://developers.google.com/android-publisher/edits), along with[deeper examples on releasing to the different tracks in Google Play Console](https://developers.google.com/android-publisher/tracks)(for the last link, you'll want to use the[AAB-friendly APIs](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.bundles)instead of the[APK-friendly API](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.apks), which are listed in the page). To specify the device targeting config for your build, you will add the config id to the`deviceTierConfigId`query parameter while calling the[`edits.bundle.upload`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.bundles/upload)method, like this:  

    https://androidpublisher.googleapis.com/upload/androidpublisher/v3/applications/{packageName}/edits/{editId}/bundles?deviceTierConfigId="{deviceTierConfigId}

### Via Google Play Console

You can follow[the instructions here](https://developer.android.com/studio/publish/upload-bundle)to upload your Android App Bundle. The**latest**DTC config will be applied to your App Bundle.

## Verifying the correct assets are being delivered

Use the following method to ensure only the correct assets are being delivered to the device

|-----------------------------------|
| `adb shell pm path {packageName}` |

You should see something like:  

    package:{...}/base.apk
    package:{...}/split_config.en.apk
    package:{...}/split_config.xxhdpi.apk
    package:{...}/split_main_asset.apk
    package:{...}/split_main_asset.config.countries_latam.apk

## Auxiliary

### Quick Start using Curl

Below is an example (using the command line tool curl) of[creating a new device targeting config](https://developer.android.com/google/play/asset-country-targeting#create-device-tier-config), and using the Edits api to create a new edit, upload a new AAB (associating it with a specific device targeting config), set the track/release config, and commit the edit. (thus**making the change public)**. Make sure to have the location of:

- The key corresponding to your[API client](https://developer.android.com/google/play/asset-country-targeting#play-developer-api)
- The package name of your app

First, create a device targeting config, and take note of the`deviceTierConfigId`you'll receive upon a successful call.  

    curl -H "$(oauth2l header --json $HOME/{apiKey} androidpublisher)" -XPOST -H "Content-Type: application/json" -d "{ "user_country_sets": [ { "name": "latam", "country_codes": [ "AR", "BR" ] }, { "name": "sea", "country_codes": [ "VN", "TW" ] } ] }" https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/deviceTierConfigs

[Start an edit](https://developers.google.com/android-publisher/api-ref/rest/v3/edits/insert)- you will get an id and expiry time for the edit. Save the id for the following calls.  

    curl -H "$(oauth2l header --json $HOME/{apiKey} androidpublisher)" -XPOST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/edits

[Upload the AAB](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.apks/upload), specifying the device targeting config as a query parameter - if the call is successful, you will see a version code, sha1 and sha256 of the build. Save the version code for the next call.  

    curl -H "$(oauth2l header --json $HOME/{apiKey} androidpublisher)" --data-binary @$HOME/{aabFile} -H "Content-Type: application/octet-stream" -XPOST https://androidpublisher.googleapis.com/upload/androidpublisher/v3/applications/{packageName}/edits/{editID}/bundles?deviceTierConfigId="{deviceTargetingConfigID}"

[Assign the AAB to the desired track](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks/update)(for testing, it is recommended to use the internal test track, but you can[read more about the different tracks here)](https://developers.google.com/android-publisher/tracks#adding_and_modifying_apks), here we do a simple rollout without release notes, but you can[read this page](https://developers.google.com/android-publisher/tracks)to learn more about how to staged rollouts, draft releases, and release notes.**If this is your first time using the Publisher API, we recommend creating this as a draft release, and completing the release on your Google Play Console to ensure everything was configured correctly**.  

    curl -H "$(oauth2l header --json $HOME/{apiKey} androidpublisher)" -XPUT -H "Content-Type: application/json" -d "{ releases: [{status: '{status}'</code>, <code><strong>versionCodes</strong></code>: <code>['{versionCode}']</code> <code><strong>}]}</strong></code>" <code>https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/edits/{editID}/tracks/{track}

[Commit changes](https://developers.google.com/android-publisher/api-ref/rest/v3/edits/commit)(proceed with caution, as**this will make all changes go live on Play**to the desired track)  

    curl -H "$(oauth2l header --json $HOME/{apiKey} androidpublisher)" -XPOST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/edits/{editID}:commit