---
title: https://developer.android.com/guide/playcore/asset-delivery/test
url: https://developer.android.com/guide/playcore/asset-delivery/test
source: md.txt
---

# Test asset delivery

Use the steps in this guide to test how your app integrates Play Asset Delivery to retrieve asset packs.

## Local testing

Play Asset Delivery supports local testing by installing a new version of the game using[`bundletool`](https://developer.android.com/studio/command-line/bundletool). Use local testing for quick, iterative cycles as it avoids the need to upload the game to Google Play servers. The steps you need to take depend on whether you're developing in Java, native, or Unity.

- [Java](https://developer.android.com/guide/playcore/asset-delivery/test#steps-native-java)
- [Native](https://developer.android.com/guide/playcore/asset-delivery/test#steps-native-java)
- [Unity](https://developer.android.com/guide/playcore/asset-delivery/test#steps-unity)

### Java or native

Follow these steps to test your app locally:

1. [Build your app bundle](https://developer.android.com/guide/playcore/asset-delivery#next-step-instructions).

2. Generate APKs with the`--local-testing`flag:

   ```
   java -jar bundletool-all.jar build-apks --bundle=path/to/your/bundle.aab \
     --output=output.apks --local-testing
   ```
3. Connect a device and run`bundletool`to sideload the APKs:

   ```
   java -jar bundletool.jar install-apks --apks=output.apks
   ```

### Unity

In the Unity Editor, select**Google \> Build and Run**.

### Behavior

`install-time`packs will be installed during the app installation process.

`fast-follow`packs behave as`on-demand`packs. That is, they won't be automatically fetched when the game is sideloaded. Developers need to request them manually when the game starts; this does not require any code changes in your app.

### Limitations

The following are limitations of local testing:

- Packs fetch from external storage instead of Play, so you cannot test how your code behaves in the case of network errors.
- Local testing does not cover the wait-for-Wi-Fi scenario.
- Updates are not supported. Before installing a new version of your build, manually uninstall the previous version.

## Testing with internal app sharing

As you get closer to having a release candidate, test your game using as realistic a configuration as possible to make sure that your game will perform well for your users in production. To validate this, you can use[internal app sharing](https://support.google.com/googleplay/android-developer/answer/9303479)to get a sharable link that you can use to download the game from Play while getting the exact same behaviour as your users will once the game is published to the Play Store.

To test Asset Delivery using internal app sharing, do the following:

1. Build your app bundle.
2. Follow the Play Console instructions on how to[share your app internally](https://support.google.com/googleplay/android-developer/answer/9303479).
3. On the test device, click the internal app-sharing link for the version of your app you just uploaded.
4. Install the app from the Google Play Store page you see after clicking the link.