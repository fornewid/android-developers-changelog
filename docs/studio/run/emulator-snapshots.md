---
title: https://developer.android.com/studio/run/emulator-snapshots
url: https://developer.android.com/studio/run/emulator-snapshots
source: md.txt
---

# Snapshots

A*snapshot*is a stored image of an Android Virtual Device (AVD) that preserves the entire state of the device at the time that it was saved -- including OS settings, application state, and user data. You can return to a saved system state by loading a snapshot, saving you the time of waiting for the operating system and applications on the virtual device to restart, as well as saving you the effort of bringing your app back to the state at which you want to resume your testing. Starting a virtual device by loading a snapshot is much like waking a physical device from a sleep state, as opposed to booting it from a powered-off state.

For each AVD, you can have one*Quick Boot*snapshot and any number of general snapshots.

The simplest way to take advantage of snapshots is to use a Quick Boot snapshot. By default, each AVD is set to automatically save a Quick Boot snapshot on exit and load from a Quick Boot snapshot on start.

The first time that an AVD starts, it must perform a*cold boot*, just like powering on a device. If Quick Boot is enabled, all subsequent starts load from the specified snapshot, and the system is restored to the state saved in that snapshot.

An AVD can boot up to 10 times faster using a*Quick Boot*snapshot than a Cold boot. That's why we would recommend to use Quick Boot (when possible) after the initial boot on your AVD.

Snapshots are valid for the system image, AVD configuration, and emulator features they are saved with. When you make a change in any of these areas, all snapshots of the affected AVD become invalid. Any update to the Android Emulator, system image, or AVD settings resets the AVD's saved state, so the next time you start the AVD, it must perform a cold boot.

Most controls for saving, loading, and managing snapshots are in the**Snapshots** and**Settings** tabs in the**Snapshots** pane. If you're running the emulator in a tool window in Android Studio, the**Snapshots** pane button is in the emulator toolbar. If you're running the emulator in a standalone window outside of Android Studio, the**Snapshots** pane is in the[Extended controls](https://developer.android.com/studio/run/emulator-snapshots#extended)window.

![](https://developer.android.com/static/studio/images/run/snapshot-examples.png)

You can also control the Quick Boot options when[starting the emulator from the command line](https://developer.android.com/studio/run/emulator-commandline#startup-options).

## Save Quick Boot snapshots

You can specify whether the emulator automatically saves a snapshot when you close. To control this behavior, proceed as follows:

1. Open the snapshots settings. If the emulator is embedded in Android Studio, click on**Snapshots** in the toolbar. If the emulator is in a separate window, open the[Extended controls](https://developer.android.com/studio/run/emulator-snapshots#extended)window.
2. In the**Snapshots** category of controls, navigate to the**Settings**tab.
3. Use the**Auto-save current state to Quickboot**menu to select one of the following options:

   - **Yes**: Always save an AVD snapshot when you close the emulator. This is the default.

     | **Note:** When automatic Quick Boot snapshots are enabled, you can skip saving a Quick Boot snapshot by holding the<kbd>Shift</kbd>key down when you close the emulator.
   - **No**: Don't save an AVD snapshot when you close the emulator.

Your selection applies only to the AVD that is open. You can't save snapshots while ADB is offline (such as while the AVD is still booting).

## Save general snapshots

Whereas you can only have one Quick Boot snapshot for each AVD, you can have multiple general snapshots for each AVD.

To save a general snapshot, open the**Snapshots** pane and click the**Take snapshot**button in its lower-right corner.

To edit the name and description of the selected snapshot, click the edit![](https://developer.android.com/static/studio/images/buttons/edit-snapshot-button.png)button at the bottom of the pane.

## Delete a snapshot

To manually delete a snapshot, open the**Snapshots** pane, select the snapshot, and click the delete![](https://developer.android.com/static/studio/images/buttons/delete-snapshot-button.png)button at the bottom of the pane.

You can also specify whether you would like the emulator to automatically delete snapshots when they become invalid, such as when the AVD settings or emulator version change. By default, the emulator asks you whether you want it to delete invalid snapshots. You can change this setting with the**Delete invalid snapshots** menu in the**Settings** tab of the**Snapshots**pane.

## Load a snapshot

To load a snapshot at any time, open the emulator's**Snapshots** pane, select the**Snapshots** category, choose a snapshot, and click the load![](https://developer.android.com/static/studio/images/buttons/load-snapshot-button.png)button at the bottom of the pane.

In Android Studio 3.2 and higher, each device configuration includes a**Boot option** control in the advanced settings in the[Virtual Device Configuration](https://developer.android.com/studio/run/managing-avds)dialog. You can use the control to specify which snapshot to load when starting that AVD.

### Disable Quick Boot

If you want to disable Quick Boot so your AVD always performs a cold boot, do the following:

1. Select**Tools \> Device Manager** and click**Edit this AVD** ![](https://developer.android.com/static/studio/images/buttons/avd-edit.png).
2. Click**Show Advanced Settings** and scroll down to**Emulated Performance**.
3. Select**Cold boot**.

## Cold boot once

Instead of disabling Quick Boot completely, you can cold boot by clicking**Cold Boot** from the AVD's menu in the**Device Manager**.

![](https://developer.android.com/static/studio/images/run/avd-coldboot-callout_new.png)

## Snapshot requirements and troubleshooting

- Snapshots don't work with Android 4.0.4 (API level 15) or lower.
- Snapshots don't work with ARM system images for Android 8.0 (API level 26).
- If the emulator fails to boot from a snapshot, select**Cold Boot** for the AVD in the Device Manager and[submit a bug report](https://developer.android.com/studio/report-bugs).
- Snapshots are not reliable when software rendering is enabled. If snapshots don't work, click**Edit this AVD** ![](https://developer.android.com/static/studio/images/buttons/avd-edit.png)in the**Device Manager** and change**Graphics** to either**Hardware** or**Automatic**.
- Loading or saving a snapshot is a memory-intensive operation. If you don't have enough RAM free when a load or save operation begins, the operating system may swap the contents of RAM to the hard disk, which can greatly slow the operation. If you experience very slow snapshot loads or saves, you may be able to speed these operations by freeing RAM. Closing applications that are not essential for your work is a good way to free RAM.