---
title: https://developer.android.com/studio/debug/device-file-explorer
url: https://developer.android.com/studio/debug/device-file-explorer
source: md.txt
---

# View on-device files with Device Explorer

The Device Explorer lets you view, copy, and delete files on an Android device. It's useful when examining files your app creates or if you want to transfer files to and from a device.
| **Note:** Most device data is not visible unless you are using a rooted device or an emulator with a standard Android (AOSP) system image, not one of the Google APIs or Google Play system images. When using a connected device, be sure to[enable USB debugging](https://developer.android.com/studio/debug/dev-options#enable).

To work with a device's file system, proceed as follows:

1. To open the Device Explorer, select**View \> Tool Windows \> Device Explorer** or click the**Device Explorer** ![](https://developer.android.com/static/studio/images/buttons/device-explorer-icon.png)button in the tool window bar.
2. Select a device from the drop-down list.
3. Interact with the device content in the file explorer window:
   - Right-click a file or directory to create a new file or directory.
   - Save, upload, delete, or synchronize the selected file or directory to your machine.
   - Double-click a file to open it in Android Studio.

![](https://developer.android.com/static/studio/images/debug/device-explorer.png)

**Figure 1.**The Device Explorer tool window.

Android Studio saves files you open in the Device Explorer in a temporary directory outside of your project. If you make modifications to a file opened using the Device Explorer and want to save your changes back to the device, you must manually upload the modified version of the file to the device.

When exploring a device's files, the following directories are particularly useful:

`data/data/`<var translate="no">app_name</var>`/`
:   Contains data files for your app stored on[internal storage](https://developer.android.com/training/data-storage#categories-locations).

`sdcard/`
:   Contains user files stored on[external user storage](https://developer.android.com/training/data-storage#categories-locations)(pictures, etc.).

**Note:** Not all files on a hardware device are visible in the Device Explorer. For example, in the`data/data/`directory, entries corresponding to apps on the device that are not debuggable can't be expanded in the Device Explorer.