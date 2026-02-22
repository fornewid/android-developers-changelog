---
title: https://developer.android.com/develop/sensors-and-location/sensors/gnss-wear-share-logs
url: https://developer.android.com/develop/sensors-and-location/sensors/gnss-wear-share-logs
source: md.txt
---

# Access and share logs from GnssLogger for Wear OS

GnssLogger for Wear OS v1.0 extends the GnssLogger app from smartphones to watches.

With[GnssLogger for Wear OS](https://play.google.com/store/apps/details?id=com.google.android.apps.location.gps.gnsslogger), you can display real-time[`GnssStatus`](https://developer.android.com/reference/android/location/GnssStatus)information from the GNSS chipset and log to the de facto standard CSV (.txt) and industry standard RINEX file formats.
![GnssLogger for Wear OS](https://developer.android.com/static/images/sensors/gnss-share5.png)**Figure 1.**GnssLogger for Wear OS

## Share logs from GnssLogger for Wear OS

1. If you haven't already,[install GnssLogger](https://play.google.com/store/apps/details?id=com.google.android.apps.location.gps.gnsslogger)on your phone.
2. On your watch, tap**Stop Log**.

Instead of immediately prompting you with sharing options, GnssLogger for Wear OS shows you the following message:
![Message on watch when starting to log](https://developer.android.com/static/images/sensors/gnss-share1.png)**Figure 2.**Message on watch when starting to log

1. On your phone, open GnssLogger and then open the**Log**tab.
2. Tap the**Download \& Delete Watch Log Files**button.

![Download & Delete Watch Log Files button](https://developer.android.com/static/images/sensors/gnss-share-9.png)**Figure 3.**Download \& Delete Watch Log Files button

GnssLogger displays the following message: "Preparing your file. Please wait...":
![Preparing your file message](https://developer.android.com/static/images/sensors/gnss-share-dandd.png)**Figure 4.**Preparing your file message

Depending on the size of the logs on your watch, this might take a while.

After the file is transferred from your watch to your phone, you'll see a*Share*dialog where you can share the files from your watch.
![A dialog showing sharing options](https://developer.android.com/static/images/sensors/gnss-share-2b.png)**Figure 5.**Share dialog

For example, if you choose to share using email, you'll see an attached zip file containing your watch log files:
![Email with attached zip file](https://developer.android.com/static/images/sensors/gnss-share7.png)**Figure 6.**Email with attached zip file

## Use Android Studio or ADB

If you don't have the watch paired with a phone, you can use[Android Studio's Device Explorer](https://developer.android.com/studio/device-explorer)to access the device.

Within Android Studio Device Explorer, check out the path`/sdcard/Android/data/com.google.android.apps.location.gps.gnsslogger/files/gnss_log`to find the log files (.txt file for the[GnssLogger log format](https://github.com/google/gps-measurement-tools/blob/master/LOGGING_FORMAT.md)), and the .24o file for[RINEX](https://files.igs.org/pub/data/format/rinex_4.01.pdf)%7B:.external%7D):
![Android Studio Device Explorer showing log files](https://developer.android.com/static/images/sensors/gnss-share6.png)**Figure 7.**Android Studio Device Explorer

You can select the files, right-click, and then select "Save To..." to save them directly to your computer:
![Dialog to save files to computer](https://developer.android.com/static/images/sensors/gnss-share4.png)**Figure 8.**Save To dialog

If you don't want to install Android Studio on your computer, you can also use[ADB](https://developer.android.com/tools/adb)to pull the files from this directory to your computer:`adb pull /sdcard/Android/data/com.google.android.apps.location.gps.gnsslogger/files/gnss_log`

**Pro tip**: You can also use these two methods (Android Studio and ADB) to retrieve GnssLogger files from phones.

Provide feedback on new features using our[public issue tracker](https://issuetracker.google.com/issues/new?component=313183&template=0).