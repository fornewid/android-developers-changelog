---
title: https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox
url: https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox
source: md.txt
---

The Health Connect Toolbox is a companion developer tool to help you test
your app's integration with Health Connect. It can read and write data directly
to Health Connect, allowing you to test your app's operations.
You can download the APK to use it for your test cycle.

[Health Connect Toolbox](https://goo.gle/health-connect-toolbox)

Extract the ZIP file to get the APK files. Then, to install the Toolbox APK on
a connected device, use `adb`. Navigate to the folder where the APK is located
and run the following command:

    $ adb install HealthConnectToolbox-{Version Number}.apk

| **Note:** The Health Connect Toolbox is actively maintained and the `{Version Number}` is expected to be updated with each release. Review the extracted APK from your downloaded ZIP file and make the appropriate changes to the command.

To manage read and write permissions for testing, open the Health
Connect app from either the main screen of the Toolbox app or go directly to
the permission flow.

![The Health Connect Toolbox app is shown as a full user interface.](https://developer.android.com/static/health-and-fitness/health-connect/images/toolbox-homescreen.png)

## Read and write health records

Health Connect Toolbox supports reading and writing all Health Connect data
types.

To insert a new health record:

1. Tap on **Insert Health Record**.
2. Select a category.
3. Select a health record type.
4. Enter the value.
5. Tap the **SAVE** button.

To read the health records from other apps:

1. Tap on **Read Health Record**.
2. Enter the data type.
3. Select the time period for query.
4. Tap the **READ** button.

![One screenshot showing inserting data from toolbox. Another screenshot showing reading data from toolbox.](https://developer.android.com/static/health-and-fitness/health-connect/images/toolbox-read-write-data.png)