---
title: https://developer.android.com/guide/playcore/asset-delivery/device-targeting
url: https://developer.android.com/guide/playcore/asset-delivery/device-targeting
source: md.txt
---

# Device targeting for asset delivery (beta)

Device targeting lets you deliver different versions (e.g. resolutions, etc.) of the same asset to devices based on their hardware. For example, you may choose to deliver low resolution assets to lower end devices to improve performance, and deliver high resolution assets to higher end devices to improve graphic quality - all without incurring any increase in overall game size by only delivering the necessary assets to users' devices. This builds upon the concept of asset packs in Play[Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery). As you'll see later, you have the power to define the group criteria (for now based on RAM, specific device models, available system features, and system on chip).

## Device targeting configuration file

To get started with device targeting, create a device targeting configuration file. Instructions can be found in the[documentation for device targeting](https://developer.android.com/google/play/device-targeting).

## Use device targeting for your asset packs

Once you have created your configuration file, you can subdivide your asset packs by device groups.

The exact steps required are different depending on whether you are building your app with the Android Gradle Plugin or with the Play Unity Plugin. Before proceeding, select your build setup:  
Android Gradle PluginPlay Unity Plugin

Take the**existing** asset pack directories created and post-fix the appropriate folders (as described below) with`#group_myCustomGroup1`,`#group_myCustomGroup2`, etc. When using the asset packs in your app, you won't need to address folders by postfix (in other words, the postfix is automatically stripped during the build process).

After the previous step, this might look like:  

    ...
    .../asset-pack-name/src/main/assets/level#group_myCustomGroup1/
    .../asset-pack-name/src/main/assets/level#group_myCustomGroup2/
    ...

In this example, you would reference`asset-pack-name/assets/level/`without any postfixes.

Devices in`myCustomGroup1`will receive all the assets under`level#group_myCustomGroup1/`, while devices in`myCustomGroup2`will receive all the assets under`level#group_myCustomGroup2/`.

Devices that don't belong to either`myCustomGroup1`or`myCustomGroup2`will receive an empty`asset-pack-name`pack.

This is because devices that don't match any device group will receive the default variant of your asset pack, which includes everything that is either inside the`level#group_other`folder or not inside any directory with a`#group_suffix`.
| **Note:** If a device matches multiple groups, it will be served the content for the group that is defined first in the XML file. The order you define groups in the XML file is your priority order.
| **Important:** It's not possible to prevent**any**variant of your asset pack from being delivered to certain devices. Non-targeted devices will always receive the default variant.