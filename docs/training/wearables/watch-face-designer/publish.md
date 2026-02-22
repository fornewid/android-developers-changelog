---
title: https://developer.android.com/training/wearables/watch-face-designer/publish
url: https://developer.android.com/training/wearables/watch-face-designer/publish
source: md.txt
---

This guide explains how to publish your watch face, created using
Watch Face Designer, to Google Play.
| **Note:** Before you begin, [export your watch face using the Google Play option](https://developer.android.com/training/wearables/watch-face-designer/export#google-play) so that you have an Android App Bundle (AAB) file ready.

## Sign into your developer account in Google Play

Sign in to Google Play Console and press 'Create App' on the dashboard.
| **Note:** If you don't have a Google Play Console developer account, [follow the
| official guide to create one](https://support.google.com/googleplay/android-developer/answer/6112435). This includes paying a registration fee.

During the "create app," workflow, **turn off automatic protection when
prompted**; otherwise, you'll have issues signing the bundle later. Automatic
protection isn't relevant to watch faces because they don't have any code.
![](https://developer.android.com/static/wear/images/design/watch-face-designer/play-create.png) **Figure 1** : The **Create app** screen in the Play Console

## Add support for the Wear OS form factor

After you've created your app, navigate to **Test and release \> Testing \>
Internal testing**:
![](https://developer.android.com/static/wear/images/design/watch-face-designer/play-testing.png) **Figure 2** : The **Test and release** screen in the Play Console

In the drop-down in the top right of the page, select **Manage form factors**,
and add Wear OS as a form factor for your app:
![Manage form factors is the 2nd option in the menu](https://developer.android.com/static/wear/images/design/watch-face-designer/play-wear-os.png) ![](https://developer.android.com/static/wear/images/design/watch-face-designer/play-add-form-factor.png) **Figure 3** : Selecting the **Manage form
factors** option (left), then adding Wear OS on the **Form factors** tab on the **Advanced settings** screen (right)

## Create a release on the internal testing track

Return to the internal testing menu and create a Wear OS-only internal testing
track. Then, create a release:
![Button appears near the top-right corner of the screen](https://developer.android.com/static/wear/images/design/watch-face-designer/play-create-track.png) ![Button also appears near the top-right corner of the screen](https://developer.android.com/static/wear/images/design/watch-face-designer/play-create-release.png) **Figure 4** : Select the **Create track** button (left), then on the next screen, select the **Create new release** button (right).

On the **Create closed testing release** screen, select **Choose signing key**.
| **Caution:** In the **Choose signing key** dialog that appears, select **Use Google-generated key**:
![Button is in the 'App Bundles' section on the screen](https://developer.android.com/static/wear/images/design/watch-face-designer/play-signing-key.png) ![Button is on the right](https://developer.android.com/static/wear/images/design/watch-face-designer/play-google-keys.png) **Figure 5** : Select the **Choose signing
key** button (left), then in the dialog that appears, select **Use
Google-generated key** (right).

Drag-and-drop the AAB file from Watch Face Designer into the **Upload** section,
and proceed with creating the release on the testing track.

## Next steps

From here, follow official Google Play documentation on [trying out apps in the
testing track](https://support.google.com/googleplay/answer/7003180) and [promoting releases to production](https://support.google.com/googleplay/android-developer/answer/9859348), which makes your
app visible to everyone on Google Play.