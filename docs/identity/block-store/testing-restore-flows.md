---
title: https://developer.android.com/identity/block-store/testing-restore-flows
url: https://developer.android.com/identity/block-store/testing-restore-flows
source: md.txt
---

# Testing restore flows

## Supported device-to-device restore flows

Some OEMs build custom device-to-device restore flows. Block Store only works for restore flows that include Google's account transfer functionality, since this is how we verify the user's identity. Google Account transfer is available on all Android devices with Google Play services, and can be accessed through the flows described in this document.

### Google cable restore

The Google cable restore is supported on Pixel (and newer models of Motorola and Sharp) devices. During Android setup, tap "Next" on the screen below:
![Initial screen during a cable restore flow](https://developer.android.com/static/identity/block-store/images/cable_restore_figure_1.png)**Figure 1.**Initial screen during a cable restore flow.

Follow the prompts to connect the cable between the source and target devices, and proceed to restore. Make sure you consent to the screen shown to copy your Google Account:
![Copy data to your new phone.](https://developer.android.com/static/identity/block-store/images/cable_restore_figure_2.png)**Figure 2.**Copy data to your new phone.

If the Google Account is not transferred, neither will the Block Store data.

### Samsung Smart Switch

If the target device is a Samsung Galaxy, there are two ways to enter the restore flow: 1) from initial setup or 2) by launching Smart Switch outside of setup.

In order to launch the flow from setup, tap "Next" on the screen shown and follow the instructions to complete the device-to-device restore:
![Samsung Smart Switch app.](https://developer.android.com/static/identity/block-store/images/samsung_smart_switch_figure_1.png)**Figure 1.**Samsung Smart Switch app.

As with the Google cable flow, make sure you consent to the Google Account transfer. Otherwise, Block Store data will not be transferred.

In order to launch the flow from outside the setup, find the Smart Switch app and launch it directly on both devices (if your source device is not a Samsung device, you'll have to install the Smart Switch app on that device from the[Play Store](https://play.google.com/store/apps/details?id=com.sec.android.easyMover)). The Block Store data is transferred as part of the account data, so you need to make sure "Accounts" is selected on the "Select data to transfer" screen during the Smart Switch flow:
![Select data to transfer.](https://developer.android.com/static/identity/block-store/images/samsung_smart_switch_figure_2.png)**Figure 2.**Select data to transfer.

If you run Smart Switch more than once as you test, you might not be able to select "Accounts" in that screen on subsequent transfers (the option is grayed out). That's because the target device will already have all the accounts present on the source device. One workaround is to have 2 Google Accounts on the source device: the account enrolled in the Block Store program (see prerequisites) and another account. Before starting a new Smart Switch transfer, remove the second account on the target device (from**Settings \> Accounts and backup \> Accounts**). You should then be able to select "Accounts" in the "Select data to transfer" screen.

### Android wireless restore

For non-Samsung OEMs that don't support the Google cable flow, tap "Next" on the screen shown:
![Initial screen during a wireless restore flow.](https://developer.android.com/static/identity/block-store/images/cable_restore_figure_1.png)**Figure 1.**Initial screen during a wireless restore flow.

You should then see the screen shown below:
![Select which device to backup from.](https://developer.android.com/static/identity/block-store/images/wireless_figure_2.png)**Figure 2.**Select which device to backup from.

Select "A backup from an Android phone". Follow the instructions to complete the restore flow. As with the other flows, make sure you consent to the Google account transfer.

## Supported cloud restore flow

The following are the steps to perform Google cloud restore during device setup.

### Google cloud restore

During Android setup, tap "Next" on the screen shown:
![Initial screen during cloud restore flow](https://developer.android.com/static/identity/block-store/images/cable_restore_figure_1.png)**Figure 1.**Initial screen during cloud restore flow.

On the next screen(as shown), tap "Can't use old phone" to trigger cloud restore flow. Follow the prompts to go through the cloud restore, including signing to your Google Account (**it needs to be the same as the backup account in your source device**), select the source device to restore from, etc.
![Initiate cloud restore flow](https://developer.android.com/static/identity/block-store/images/cloud_restore_figure_2.png)**Figure 2.**Initiate cloud restore flow.

Make sure your app is selected for restore (in the screen shown) during the restore flow.
![Select your app to restore](https://developer.android.com/static/identity/block-store/images/cloud_restore_figure_3.png)**Figure 3.**Select your app to restore.

## Additional notes

- The restore flow that includes Google's account transfer will always come first before any custom OEM restore flows. When in doubt, choose the first device-to-device restore flow available to you.
- There may be variation in the screens depending on the OEM and Android version.