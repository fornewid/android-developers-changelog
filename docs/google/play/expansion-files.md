---
title: https://developer.android.com/google/play/expansion-files
url: https://developer.android.com/google/play/expansion-files
source: md.txt
---

| **Important:** From August 2021, new apps are required to publish with the [Android App Bundle](https://developer.android.com/guide/app-bundle) on Google Play. New apps larger than 200 MB are now supported by either [Play Feature Delivery](https://developer.android.com/guide/app-bundle/dynamic-delivery) or [Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery). From June 2023, new and existing [TV apps are required to
| be published as App Bundles](https://developer.android.com/docs/quality-guidelines/tv-app-quality#SC-E1).

Google Play requires that the compressed APK that users download be no more than 100MB.
For most apps, this is plenty of space for all the app's code and assets.
However, some apps need more space for high-fidelity graphics, media files, or other large assets.
Previously, if your app's compressed download size exceeded 100MB, you had to host and download the
additional resources yourself when the user opens the app. Hosting and serving the extra files can
be costly, and the user experience is often less than ideal. To make this process easier for you
and more pleasant for users, Google Play allows you to attach two large expansion files that
supplement your APK.

Google Play hosts the expansion files for your app and serves them to the device at
no cost to you. The expansion files are saved to the device's shared storage location (the
SD card or USB-mountable partition; also known as the "external" storage) where your app can access
them. On most devices, Google Play downloads the expansion file(s) at the same time it
downloads the APK, so your app has everything it needs when the user opens it for the
first time. In some cases, however, your app must download the files from Google Play
when your app starts.


If you'd like to avoid using expansion files and your app's compressed download size is larger
than 100 MB, you should instead upload your app using [Android App
Bundles](https://developer.android.com/guide/app-bundle) which allows for up to a 200 MB compressed download size. Additionally, because using
app bundles defers APK generation and signing to Google Play, users download optimized APKs with
only the code and resources they need to run your app. You don't have to build, sign, and
manage multiple APKs or expansion files, and users get smaller, more optimized downloads.

## Overview

Each time you upload an APK using the Google Play Console, you have the option to
add one or two expansion files to the APK. Each file can be up to 2GB and it can be any format you
choose, but we recommend you use a compressed file to conserve bandwidth during the download.
Conceptually, each expansion file plays a different role:

- The **main** expansion file is the primary expansion file for additional resources required by your app.
- The **patch** expansion file is optional and intended for small updates to the main expansion file.

While you can use the two expansion files any way you wish, we recommend that the main
expansion file deliver the primary assets and should rarely if ever updated; the patch expansion
file should be smaller and serve as a "patch carrier," getting updated with each major
release or as necessary.

However, even if your app update requires only a new patch expansion file, you still must
upload a new APK with an updated [`versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode) in the manifest. (The
Play Console does not allow you to upload an expansion file to an existing APK.)

**Note:** The patch expansion file is semantically the same as the
main expansion file---you can use each file any way you want.

### File name format

Each expansion file you upload can be any format you choose (ZIP, PDF, MP4, etc.). You can also
use the [JOBB](https://developer.android.com/tools/help/jobb) tool to encapsulate and encrypt a set
of resource files and subsequent patches for that set. Regardless of the file type, Google Play
considers them opaque binary blobs and renames the files using the following scheme:  

```
[main|patch].<expansion-version>.<package-name>.obb
```

There are three components to this scheme:

`main` or `patch`
:   Specifies whether the file is the main or patch expansion file. There can be
    only one main file and one patch file for each APK.

`<expansion-version>`
:   This is an integer that matches the version code of the APK with which the expansion is
    *first* associated (it matches the app's [`android:versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode)
    value).

    "First" is emphasized because although the Play Console allows you to
    re-use an uploaded expansion file with a new APK, the expansion file's name does not change---it
    retains the version applied to it when you first uploaded the file.

`<package-name>`
:   Your app's Java-style package name.

For example, suppose your APK version is 314159 and your package name is com.example.app. If you
upload a main expansion file, the file is renamed to:  

```
main.314159.com.example.app.obb
```

### Storage location

When Google Play downloads your expansion files to a device, it saves them to the system's
shared storage location. To ensure proper behavior, you must not delete, move, or rename the
expansion files. In the event that your app must perform the download from Google Play
itself, you must save the files to the exact same location.

The [getObbDir()](https://developer.android.com/reference/android/content/Context#getObbDir()) method returns the specific location
for your expansion files in the following form:  

```
<shared-storage>/Android/obb/<package-name>/
```

- `<shared-storage>` is the path to the shared storage space, available from [getExternalStorageDirectory()](https://developer.android.com/reference/android/os/Environment#getExternalStorageDirectory()).
- `<package-name>` is your app's Java-style package name, available from [getPackageName()](https://developer.android.com/reference/android/content/Context#getPackageName()).

For each app, there are never more than two expansion files in this directory.
One is the main expansion file and the other is the patch expansion file (if necessary). Previous
versions are overwritten when you update your app with new expansion files. Since Android
4.4 (API level 19), apps can read `OBB` expansion files without external storage
permission. However, some implementations of Android 6.0 (API level 23) and later still require
permission, so you will need to declare the
`READ_EXTERNAL_STORAGE` permission in the app manifest and ask for permission at
runtime as follows:  

```xml
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

For Android version 6 and later, external storage permission needs to be requested at runtime.
However, some implementations of Android do not require permission to read OBB files. The
following code snippet shows how to check for read access before asking for external storage
permission:  

### Kotlin

```kotlin
val obb = File(obb_filename)
var open_failed = false

try {
    BufferedReader(FileReader(obb)).also { br ->
        ReadObbFile(br)
    }
} catch (e: IOException) {
    open_failed = true
}

if (open_failed) {
    // request READ_EXTERNAL_STORAGE permission before reading OBB file
    ReadObbFileWithPermission()
}
```

### Java

```java
File obb = new File(obb_filename);
 boolean open_failed = false;

 try {
     BufferedReader br = new BufferedReader(new FileReader(obb));
     open_failed = false;
     ReadObbFile(br);
 } catch (IOException e) {
     open_failed = true;
 }

 if (open_failed) {
     // request READ_EXTERNAL_STORAGE permission before reading OBB file
     ReadObbFileWithPermission();
 }
```

If you must unpack the contents of your expansion files, **do not** delete the
`OBB` expansion files afterwards and **do not** save the unpacked data
in the same directory. You should save your unpacked files in the directory
specified by [getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)). However,
if possible, it's best if you use an expansion file format that allows you to read directly from
the file instead of requiring you to unpack the data. For example, we've provided a library
project called the [APK Expansion Zip Library](https://developer.android.com/google/play/expansion-files#ZipLib) that reads your data directly
from the ZIP file.

**Caution:** Unlike APK files, any files saved
on the shared storage can be read by the user and other apps.

**Tip:** If you're packaging media files into a ZIP, you can use media
playback calls on the files with offset and length controls (such as [MediaPlayer.setDataSource()](https://developer.android.com/reference/android/media/MediaPlayer#setDataSource(java.io.FileDescriptor, long, long)) and
[SoundPool.load()](https://developer.android.com/reference/android/media/SoundPool#load(java.io.FileDescriptor, long, long, int))) without the
need to unpack your ZIP. In order for this to work, you must not perform additional compression on
the media files when creating the ZIP packages. For example, when using the `zip` tool,
you should use the `-n` option to specify the file suffixes that should not be
compressed:   

`zip -n .mp4;.ogg main_expansion media_files`

### Download process

Most of the time, Google Play downloads and saves your expansion files at the same time it
downloads the APK to the device. However, in some cases Google Play
cannot download the expansion files or the user might have deleted previously downloaded expansion
files. To handle these situations, your app must be able to download the files
itself when the main activity starts, using a URL provided by Google Play.

The download process from a high level looks like this:

1. User selects to install your app from Google Play.
2. If Google Play is able to download the expansion files (which is the case for most devices), it downloads them along with the APK. If Google Play is unable to download the expansion files, it downloads the
   APK only.

3. When the user launches your app, your app must check whether the expansion files are already saved on the device.
   1. If yes, your app is ready to go.
   2. If no, your app must download the expansion files over HTTP from Google Play. Your app must send a request to the Google Play client using the Google Play's [app Licensing](https://developer.android.com/google/play/licensing) service, which responds with the name, file size, and URL for each expansion file. With this information, you then download the files and save them to the proper [storage location](https://developer.android.com/google/play/expansion-files#StorageLocation).

**Caution:** It is critical that you include the necessary code to
download the expansion files from Google Play in the event that the files are not already on the
device when your app starts. As discussed in the following section about [Downloading the Expansion Files](https://developer.android.com/google/play/expansion-files#Downloading), we've made a library available to you that
greatly simplifies this process and performs the download from a service with a minimal amount of
code from you.

### Development checklist

Here's a summary of the tasks you should perform to use expansion files with your
app:

1. First determine whether your app's compressed download size needs to be more than 100MB. Space is precious and you should keep your total download size as small as possible. If your app uses more than 100MB in order to provide multiple versions of your graphic assets for multiple screen densities, consider instead publishing [multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks) in which each APK contains only the assets required for the screens that it targets. For the best results when publishing to Google Play, upload an [Android App Bundle](https://developer.android.com/guide/app-bundle), which includes all your app's compiled code and resources, but defers APK generation and signing to Google Play.
2. Determine which app resources to separate from your APK and package them in a file to use as the main expansion file. Normally, you should only use the second patch expansion file when performing updates to
   the main expansion file. However, if your resources exceed the 2GB limit for the main
   expansion file, you can use the patch file for the rest of your assets.

3. Develop your app such that it uses the resources from your expansion files in the device's [shared storage location](https://developer.android.com/google/play/expansion-files#StorageLocation).

   Remember that you must not delete, move, or rename the expansion files.

   If your app doesn't demand a specific format, we suggest you create ZIP files for
   your expansion files, then read them using the [APK Expansion Zip
   Library](https://developer.android.com/google/play/expansion-files#ZipLib).
4. Add logic to your app's main activity that checks whether the expansion files are on the device upon start-up. If the files are not on the device, use Google Play's [app Licensing](https://developer.android.com/google/play/licensing) service to request URLs for the expansion files, then download and save them.

   To greatly reduce the amount of code you must write and ensure a good user experience
   during the download, we recommend you use the [Downloader
   Library](https://developer.android.com/google/play/expansion-files#AboutLibraries) to implement your download behavior.

   If you build your own download service instead of using the library, be aware that you
   must not change the name of the expansion files and must save them to the proper
   [storage location](https://developer.android.com/google/play/expansion-files#StorageLocation).

Once you've finished your app development, follow the guide to [Testing
Your Expansion Files](https://developer.android.com/google/play/expansion-files#Testing).

## Rules and Limitations

Adding APK expansion files is a feature available when you upload your app using the
Play Console. When uploading your app for the first time or updating an
app that uses expansion files, you must be aware of the following rules and limitations:

1. Each expansion file can be no more than 2GB.
2. In order to download your expansion files from Google Play, **the user must have
   acquired your app from Google Play**. Google Play will not provide the URLs for your expansion files if the app was installed by other means.
3. When performing the download from within your app, the URL that Google Play provides for each file is unique for every download and each one expires shortly after it is given to your app.
4. If you update your app with a new APK or upload [multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks) for the same app, you can select expansion files that you've uploaded for a previous APK. **The
   expansion file's name does not change**---it retains the version received by the APK to which the file was originally associated.
5. If you use expansion files in combination with [multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks) in order to provide different expansion files for different devices, you still must upload separate APKs for each device in order to provide a unique [`versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode) value and declare different [filters](https://developer.android.com/google/play/filters) for each APK.
6. You cannot issue an update to your app by changing the expansion files alone---**you must upload a new APK** to update your app. If your changes only concern the assets in your expansion files, you can update your APK simply by changing the [`versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode) (and perhaps also the [`versionName`](https://developer.android.com/guide/topics/manifest/manifest-element#vname)).
7. **Do not save other data into your `obb/`
   directory** . If you must unpack some data, save it into the location specified by [getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)).
8. **Do not delete or rename the `.obb` expansion file** (unless you're performing an update). Doing so will cause Google Play (or your app itself) to repeatedly download the expansion file.
9. When updating an expansion file manually, you must delete the previous expansion file.

## Downloading the Expansion Files

In most cases, Google Play downloads and saves your expansion files to the device at the same
time it installs or updates the APK. This way, the expansion files are available when your
app launches for the first time. However, in some cases your app must download the
expansion files itself by requesting them from a URL provided to you in a response
from Google Play's [app Licensing](https://developer.android.com/google/play/licensing) service.

The basic logic you need to download your expansion files is the following:

1. When your app starts, look for the expansion files on the [shared storage location](https://developer.android.com/google/play/expansion-files#StorageLocation) (in the `Android/obb/<package-name>/` directory).
   1. If the expansion files are there, you're all set and your app can continue.
   2. If the expansion files are *not* there:
      1. Perform a request using Google Play's [app Licensing](https://developer.android.com/google/play/licensing) to get your app's expansion file names, sizes, and URLs.
      2. Use the URLs provided by Google Play to download the expansion files and save the expansion files. You **must** save the files to the [shared storage location](https://developer.android.com/google/play/expansion-files#StorageLocation) (`Android/obb/<package-name>/`) and use the exact file name provided by Google Play's response.

         **Note:** The URL that Google Play provides for your
         expansion files is unique for every download and each one expires shortly after it is given to
         your app.

If your app is free (not a paid app), then you probably haven't used the [app Licensing](https://developer.android.com/google/play/licensing) service. It's primarily
designed for you to enforce
licensing policies for your app and ensure that the user has the right to
use your app (they rightfully paid for it on Google Play). In order to facilitate the
expansion file functionality, the licensing service has been enhanced to provide a response
to your app that includes the URL of your app's expansion files that are hosted
on Google Play. So, even if your app is free for users, you need to include the
License Verification Library (LVL) to use APK expansion files. Of course, if your app
is free, you don't need to enforce license verification---you simply need the
library to perform the request that returns the URL of your expansion files.

**Note:** Whether your app is free or not, Google Play
returns the expansion file URLs only if the user acquired your app from Google Play.

In addition to the LVL, you need a set of code that downloads the expansion files
over an HTTP connection and saves them to the proper location on the device's shared storage.
As you build this procedure into your app, there are several issues you should take into
consideration:

- The device might not have enough space for the expansion files, so you should check before beginning the download and warn the user if there's not enough space.
- File downloads should occur in a background service in order to avoid blocking the user interaction and allow the user to leave your app while the download completes.
- A variety of errors might occur during the request and download that you must gracefully handle.
- Network connectivity can change during the download, so you should handle such changes and if interrupted, resume the download when possible.
- While the download occurs in the background, you should provide a notification that indicates the download progress, notifies the user when it's done, and takes the user back to your app when selected.

To simplify this work for you, we've built the [Downloader Library](https://developer.android.com/google/play/expansion-files#AboutLibraries),
which requests the expansion file URLs through the licensing service, downloads the expansion files,
performs all of the tasks listed above, and even allows your activity to pause and resume the
download. By adding the Downloader Library and a few code hooks to your app, almost all the
work to download the expansion files is already coded for you. As such, in order to provide the best
user experience with minimal effort on your behalf, we recommend you use the Downloader Library to
download your expansion files. The information in the following sections explain how to integrate
the library into your app.

If you'd rather develop your own solution to download the expansion files using the Google
Play URLs, you must follow the [app
Licensing](https://developer.android.com/google/play/licensing) documentation to perform a license request, then retrieve the expansion file names,
sizes, and URLs from the response extras. You should use the [`APKExpansionPolicy`](https://developer.android.com/google/play/expansion-files#ExpansionPolicy) class (included in the License Verification Library) as your licensing
policy, which captures the expansion file names, sizes, and URLs from the licensing service..

### About the Downloader Library

To use APK expansion files with your app and provide the best user experience with
minimal effort on your behalf, we recommend you use the Downloader Library that's included in the
Google Play APK Expansion Library package. This library downloads your expansion files in a
background service, shows a user notification with the download status, handles network
connectivity loss, resumes the download when possible, and more.

To implement expansion file downloads using the Downloader Library, all you need to do is:

- Extend a special [Service](https://developer.android.com/reference/android/app/Service) subclass and [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) subclass that each require just a few lines of code from you.
- Add some logic to your main activity that checks whether the expansion files have already been downloaded and, if not, invokes the download process and displays a progress UI.
- Implement a callback interface with a few methods in your main activity that receives updates about the download progress.

The following sections explain how to set up your app using the Downloader Library.

### Preparing to use the Downloader Library

To use the Downloader Library, you need to
download two packages from the SDK Manager and add the appropriate libraries to your
app.

First, open the [Android SDK Manager](https://developer.android.com/studio/intro/update)
(**Tools \> SDK Manager** ), and under
*Appearance \& Behavior \> System Settings \> Android SDK* , select
the *SDK Tools* tab to select and download:

- *Google Play Licensing Library package*
- *Google Play APK Expansion Library package*

Create a new library module for the License Verification Library and Downloader
Library. For each library:

1. Select **File \> New \> New Module**.
2. In the *Create New Module* window, select **Android Library** , and then select **Next**.
3. Specify an *app/Library name* such as "Google Play License Library" and "Google Play Downloader Library", choose *Minimum SDK level* , then select **Finish**.
4. Select **File \> Project Structure**.
5. Select the *Properties* tab and in *Library
   Repository* , enter the library from the `<sdk>/extras/google/` directory (`play_licensing/` for the License Verification Library or `play_apk_expansion/downloader_library/` for the Downloader Library).
6. Select **OK** to create the new module.

**Note:** The Downloader Library depends on the License
Verification Library. Be sure to add the License
Verification Library to the Downloader Library's project properties.

Or, from a command line, update your project to include the libraries:

1. Change directories to the `<sdk>/tools/` directory.
2. Execute `android update project` with the `--library` option to add both the LVL and the Downloader Library to your project. For example:  

   ```
   android update project --path ~/Android/MyApp \
   --library ~/android_sdk/extras/google/market_licensing \
   --library ~/android_sdk/extras/google/market_apk_expansion/downloader_library
   ```

With both the License Verification Library and Downloader Library added to your
app, you'll be able to quickly integrate the ability to download expansion files from
Google Play. The format that you choose for the expansion files and how you read them
from the shared storage is a separate implementation that you should consider based on your
app needs.

**Tip:** The Apk Expansion package includes a sample
app
that shows how to use the Downloader Library in an app. The sample uses a third library
available in the Apk Expansion package called the APK Expansion Zip Library. If
you plan on
using ZIP files for your expansion files, we suggest you also add the APK Expansion Zip Library to
your app. For more information, see the section below
about [Using the APK Expansion Zip Library](https://developer.android.com/google/play/expansion-files#ZipLib).

### Declaring user permissions

In order to download the expansion files, the Downloader Library
requires several permissions that you must declare in your app's manifest file. They
are:  

```xml
<manifest ...>
    <!-- Required to access Google Play Licensing -->
    <uses-permission android:name="com.android.vending.CHECK_LICENSE" />

    <!-- Required to download files from Google Play -->
    <uses-permission android:name="android.permission.INTERNET" />

    <!-- Required to keep CPU alive while downloading files
        (NOT to keep screen awake) -->
    <uses-permission android:name="android.permission.WAKE_LOCK" />

    <!-- Required to poll the state of the network connection
        and respond to changes -->
    <uses-permission
        android:name="android.permission.ACCESS_NETWORK_STATE" />

    <!-- Required to check whether Wi-Fi is enabled -->
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>

    <!-- Required to read and write the expansion files on shared storage -->
    <uses-permission
        android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    ...
</manifest>
```

**Note:** By default, the Downloader Library requires API
level 4, but the APK Expansion Zip Library requires API level 5.

### Implementing the downloader service

In order to perform downloads in the background, the Downloader Library provides its
own [Service](https://developer.android.com/reference/android/app/Service) subclass called `DownloaderService` that you should extend. In
addition to downloading the expansion files for you, the `DownloaderService` also:

- Registers a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) that listens for changes to the device's network connectivity (the [CONNECTIVITY_ACTION](https://developer.android.com/reference/android/net/ConnectivityManager#CONNECTIVITY_ACTION) broadcast) in order to pause the download when necessary (such as due to connectivity loss) and resume the download when possible (connectivity is acquired).
- Schedules an [RTC_WAKEUP](https://developer.android.com/reference/android/app/AlarmManager#RTC_WAKEUP) alarm to retry the download for cases in which the service gets killed.
- Builds a custom [Notification](https://developer.android.com/reference/android/app/Notification) that displays the download progress and any errors or state changes.
- Allows your app to manually pause and resume the download.
- Verifies that the shared storage is mounted and available, that the files don't already exist, and that there is enough space, all before downloading the expansion files. Then notifies the user if any of these are not true.

All you need to do is create a class in your app that extends the `DownloaderService` class and override three methods to provide specific app details:

`getPublicKey()`
:   This must return a string that is the Base64-encoded RSA public key for your publisher
    account, available from the profile page on the Play Console (see [Setting Up for Licensing](https://developer.android.com/google/play/licensing/setting-up)).

`getSALT()`
:   This must return an array of random bytes that the licensing `Policy` uses to
    create an [`Obfuscator`](https://developer.android.com/google/play/licensing/adding-licensing#impl-Obfuscator). The salt ensures that your obfuscated [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)
    file in which your licensing data is saved will be unique and non-discoverable.

`getAlarmReceiverClassName()`
:   This must return the class name of the [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) in
    your app that should receive the alarm indicating that the download should be
    restarted (which might happen if the downloader service unexpectedly stops).

For example, here's a complete implementation of `DownloaderService`:  

### Kotlin

```kotlin
// You must use the public key belonging to your publisher account
const val BASE64_PUBLIC_KEY = "YourLVLKey"
// You should also modify this salt
val SALT = byteArrayOf(
        1, 42, -12, -1, 54, 98, -100, -12, 43, 2,
        -8, -4, 9, 5, -106, -107, -33, 45, -1, 84
)

class SampleDownloaderService : DownloaderService() {

    override fun getPublicKey(): String = BASE64_PUBLIC_KEY

    override fun getSALT(): ByteArray = SALT

    override fun getAlarmReceiverClassName(): String = SampleAlarmReceiver::class.java.name
}
```

### Java

```java
public class SampleDownloaderService extends DownloaderService {
    // You must use the public key belonging to your publisher account
    public static final String BASE64_PUBLIC_KEY = "YourLVLKey";
    // You should also modify this salt
    public static final byte[] SALT = new byte[] { 1, 42, -12, -1, 54, 98,
            -100, -12, 43, 2, -8, -4, 9, 5, -106, -107, -33, 45, -1, 84
    };

    @Override
    public String getPublicKey() {
        return BASE64_PUBLIC_KEY;
    }

    @Override
    public byte[] getSALT() {
        return SALT;
    }

    @Override
    public String getAlarmReceiverClassName() {
        return SampleAlarmReceiver.class.getName();
    }
}
```

**Notice:** You must update the `BASE64_PUBLIC_KEY` value
to be the public key belonging to your publisher account. You can find the key in the Developer
Console under your profile information. This is necessary even when testing
your downloads.

Remember to declare the service in your manifest file:  

```xml
<app ...>
    <service android:name=".SampleDownloaderService" />
    ...
</app>
```

### Implementing the alarm receiver

In order to monitor the progress of the file downloads and restart the download if necessary, the
`DownloaderService` schedules an [RTC_WAKEUP](https://developer.android.com/reference/android/app/AlarmManager#RTC_WAKEUP) alarm that
delivers an [Intent](https://developer.android.com/reference/android/content/Intent) to a [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) in your
app. You must define the [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver) to call an API
from the Downloader Library that checks the status of the download and restarts
it if necessary.

You simply need to override the [onReceive()](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context, android.content.Intent)) method to call `DownloaderClientMarshaller.startDownloadServiceIfRequired()`.

For example:  

### Kotlin

```kotlin
class SampleAlarmReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        try {
            DownloaderClientMarshaller.startDownloadServiceIfRequired(
                    context,
                    intent,
                    SampleDownloaderService::class.java
            )
        } catch (e: PackageManager.NameNotFoundException) {
            e.printStackTrace()
        }
    }
}
```

### Java

```java
public class SampleAlarmReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        try {
            DownloaderClientMarshaller.startDownloadServiceIfRequired(context,
                intent, SampleDownloaderService.class);
        } catch (NameNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

Notice that this is the class for which you must return the name
in your service's `getAlarmReceiverClassName()` method (see the previous section).

Remember to declare the receiver in your manifest file:  

```xml
<app ...>
    <receiver android:name=".SampleAlarmReceiver" />
    ...
</app>
```

### Starting the download

The main activity in your app (the one started by your launcher icon) is
responsible for verifying whether the expansion files are already on the device and initiating
the download if they are not.

Starting the download using the Downloader Library requires the following
procedures:

1. Check whether the files have been downloaded. The Downloader Library includes some APIs in the `Helper` class to
   help with this process:

   - `getExpansionAPKFileName(Context, c, boolean mainFile, int
     versionCode)`
   - `doesFileExist(Context c, String fileName, long fileSize)`

   For example, the sample app provided in the Apk Expansion package calls the
   following method in the activity's [onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) method to check
   whether the expansion files already exist on the device:  

   ### Kotlin

   ```kotlin
   fun expansionFilesDelivered(): Boolean {
       xAPKS.forEach { xf ->
           Helpers.getExpansionAPKFileName(this, xf.isBase, xf.fileVersion).also { fileName ->
               if (!Helpers.doesFileExist(this, fileName, xf.fileSize, false))
                   return false
           }
       }
       return true
   }
   ```

   ### Java

   ```java
   boolean expansionFilesDelivered() {
       for (XAPKFile xf : xAPKS) {
           String fileName = Helpers.getExpansionAPKFileName(this, xf.isBase,
               xf.fileVersion);
           if (!Helpers.doesFileExist(this, fileName, xf.fileSize, false))
               return false;
       }
       return true;
   }
   ```

   In this case, each `XAPKFile` object holds the version number and file size of a known
   expansion file and a boolean as to whether it's the main expansion file. (See the sample
   app's `SampleDownloaderActivity` class for details.)

   If this method returns false, then the app must begin the download.
2. Start the download by calling the static method `DownloaderClientMarshaller.startDownloadServiceIfRequired(Context c, PendingIntent
   notificationClient, Class<?> serviceClass)`.

   The method takes the following parameters:
   - `context`: Your app's [Context](https://developer.android.com/reference/android/content/Context).
   - `notificationClient`: A [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) to start your main activity. This is used in the [Notification](https://developer.android.com/reference/android/app/Notification) that the `DownloaderService` creates to show the download progress. When the user selects the notification, the system invokes the [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) you supply here and should open the activity that shows the download progress (usually the same activity that started the download).
   - `serviceClass`: The [Class](https://developer.android.com/reference/java/lang/Class) object for your implementation of `DownloaderService`, required to start the service and begin the download if necessary.

   The method returns an integer that indicates
   whether or not the download is required. Possible values are:
   - `NO_DOWNLOAD_REQUIRED`: Returned if the files already exist or a download is already in progress.
   - `LVL_CHECK_REQUIRED`: Returned if a license verification is required in order to acquire the expansion file URLs.
   - `DOWNLOAD_REQUIRED`: Returned if the expansion file URLs are already known, but have not been downloaded.

   The behavior for `LVL_CHECK_REQUIRED` and `DOWNLOAD_REQUIRED` are essentially the
   same and you normally don't need to be concerned about them. In your main activity that calls `startDownloadServiceIfRequired()`, you can simply check whether or not the response is `NO_DOWNLOAD_REQUIRED`. If the response is anything *other than* `NO_DOWNLOAD_REQUIRED`,
   the Downloader Library begins the download and you should update your activity UI to
   display the download progress (see the next step). If the response *is* `NO_DOWNLOAD_REQUIRED`, then the files are available and your app can start.

   For example:  

   ### Kotlin

   ```kotlin
   override fun onCreate(savedInstanceState: Bundle?) {
       super.onCreate(savedInstanceState)

       // Check if expansion files are available before going any further
       if (!expansionFilesDelivered()) {
           val pendingIntent =
                   // Build an Intent to start this activity from the Notification
                   Intent(this, MainActivity::class.java).apply {
                       flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
                   }.let { notifierIntent ->
                       PendingIntent.getActivity(
                               this,
                               0,
                               notifierIntent,
                               PendingIntent.FLAG_UPDATE_CURRENT
                       )
                   }


           // Start the download service (if required)
           val startResult: Int = DownloaderClientMarshaller.startDownloadServiceIfRequired(
                   this,
                   pendingIntent,
                   SampleDownloaderService::class.java
           )
           // If download has started, initialize this activity to show
           // download progress
           if (startResult != DownloaderClientMarshaller.NO_DOWNLOAD_REQUIRED) {
               // This is where you do set up to display the download
               // progress (next step)
               ...
               return
           } // If the download wasn't necessary, fall through to start the app
       }
       startApp() // Expansion files are available, start the app
   }
   ```

   ### Java

   ```java
   @Override
   public void onCreate(Bundle savedInstanceState) {
       // Check if expansion files are available before going any further
       if (!expansionFilesDelivered()) {
           // Build an Intent to start this activity from the Notification
           Intent notifierIntent = new Intent(this, MainActivity.getClass());
           notifierIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK |
                                   Intent.FLAG_ACTIVITY_CLEAR_TOP);
           ...
           PendingIntent pendingIntent = PendingIntent.getActivity(this, 0,
                   notifierIntent, PendingIntent.FLAG_UPDATE_CURRENT);

           // Start the download service (if required)
           int startResult =
               DownloaderClientMarshaller.startDownloadServiceIfRequired(this,
                           pendingIntent, SampleDownloaderService.class);
           // If download has started, initialize this activity to show
           // download progress
           if (startResult != DownloaderClientMarshaller.NO_DOWNLOAD_REQUIRED) {
               // This is where you do set up to display the download
               // progress (next step)
               ...
               return;
           } // If the download wasn't necessary, fall through to start the app
       }
       startApp(); // Expansion files are available, start the app
   }
   ```
3. When the `startDownloadServiceIfRequired()` method returns anything *other
   than* `NO_DOWNLOAD_REQUIRED`, create an instance of `IStub` by calling `DownloaderClientMarshaller.CreateStub(IDownloaderClient client, Class<?>
   downloaderService)`. The `IStub` provides a binding between your activity to the downloader service such that your activity receives callbacks about the download progress.

   In order to instantiate your `IStub` by calling `CreateStub()`, you must pass it
   an implementation of the `IDownloaderClient` interface and your `DownloaderService`
   implementation. The next section about [Receiving download progress](https://developer.android.com/google/play/expansion-files#Progress) discusses
   the `IDownloaderClient` interface, which you should usually implement in your [Activity](https://developer.android.com/reference/android/app/Activity) class so you can update the activity UI when the download state changes.

   We recommend that you call `CreateStub()` to instantiate your `IStub` during your activity's [onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) method, after `startDownloadServiceIfRequired()`
   starts the download.

   For example, in the previous code sample for [onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)), you can respond to the `startDownloadServiceIfRequired()` result like this:  

   ### Kotlin

   ```kotlin
           // Start the download service (if required)
           val startResult = DownloaderClientMarshaller.startDownloadServiceIfRequired(
                   this@MainActivity,
                   pendingIntent,
                   SampleDownloaderService::class.java
           )
           // If download has started, initialize activity to show progress
           if (startResult != DownloaderClientMarshaller.NO_DOWNLOAD_REQUIRED) {
               // Instantiate a member instance of IStub
               downloaderClientStub =
                       DownloaderClientMarshaller.CreateStub(this, SampleDownloaderService::class.java)
               // Inflate layout that shows download progress
               setContentView(R.layout.downloader_ui)
               return
           }
   ```

   ### Java

   ```java
           // Start the download service (if required)
           int startResult =
               DownloaderClientMarshaller.startDownloadServiceIfRequired(this,
                           pendingIntent, SampleDownloaderService.class);
           // If download has started, initialize activity to show progress
           if (startResult != DownloaderClientMarshaller.NO_DOWNLOAD_REQUIRED) {
               // Instantiate a member instance of IStub
               downloaderClientStub = DownloaderClientMarshaller.CreateStub(this,
                       SampleDownloaderService.class);
               // Inflate layout that shows download progress
               setContentView(R.layout.downloader_ui);
               return;
           }
   ```

   After the [onCreate()](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) method returns, your activity
   receives a call to [onResume()](https://developer.android.com/reference/android/app/Activity#onResume()), which is where you should then
   call `connect()` on the `IStub`, passing it your app's [Context](https://developer.android.com/reference/android/content/Context). Conversely, you should call
   `disconnect()` in your activity's [onStop()](https://developer.android.com/reference/android/app/Activity#onStop()) callback.  

   ### Kotlin

   ```kotlin
   override fun onResume() {
       downloaderClientStub?.connect(this)
       super.onResume()
   }

   override fun onStop() {
       downloaderClientStub?.disconnect(this)
       super.onStop()
   }
   ```

   ### Java

   ```java
   @Override
   protected void onResume() {
       if (null != downloaderClientStub) {
           downloaderClientStub.connect(this);
       }
       super.onResume();
   }

   @Override
   protected void onStop() {
       if (null != downloaderClientStub) {
           downloaderClientStub.disconnect(this);
       }
       super.onStop();
   }
   ```

   Calling `connect()` on the `IStub` binds your activity to the `DownloaderService` such that your activity receives callbacks regarding changes to the download
   state through the `IDownloaderClient` interface.

### Receiving download progress

To receive updates regarding the download progress and to interact with the `DownloaderService`, you must implement the Downloader Library's `IDownloaderClient` interface.
Usually, the activity you use to start the download should implement this interface in order to
display the download progress and send requests to the service.

The required interface methods for `IDownloaderClient` are:

`onServiceConnected(Messenger m)`
:   After you instantiate the `IStub` in your activity, you'll receive a call to this
    method, which passes a [Messenger](https://developer.android.com/reference/android/os/Messenger) object that's connected with your instance
    of `DownloaderService`. To send requests to the service, such as to pause and resume
    downloads, you must call `DownloaderServiceMarshaller.CreateProxy()` to receive the `IDownloaderService` interface connected to the service.

    A recommended implementation looks like this:

    ### Kotlin

    ```kotlin
    private var remoteService: IDownloaderService? = null
    ...

    override fun onServiceConnected(m: Messenger) {
        remoteService = DownloaderServiceMarshaller.CreateProxy(m).apply {
            downloaderClientStub?.messenger?.also { messenger ->
                onClientUpdated(messenger)
            }
        }
    }
    ```

    ### Java

    ```java
    private IDownloaderService remoteService;
    ...

    @Override
    public void onServiceConnected(Messenger m) {
        remoteService = DownloaderServiceMarshaller.CreateProxy(m);
        remoteService.onClientUpdated(downloaderClientStub.getMessenger());
    }
    ```

    With the `IDownloaderService` object initialized, you can send commands to the
    downloader service, such as to pause and resume the download (`requestPauseDownload()`
    and `requestContinueDownload()`).

`onDownloadStateChanged(int newState)`

:   The download service calls this when a change in download state occurs, such as the download begins or completes. The `newState` value will be one of several possible values specified in
    by one of the `IDownloaderClient` class's `STATE_*` constants.

    To provide a useful message to your users, you can request a corresponding string
    for each state by calling `Helpers.getDownloaderStringResourceIDFromState()`. This
    returns the resource ID for one of the strings bundled with the Downloader
    Library. For example, the string "Download paused because you are roaming" corresponds to `STATE_PAUSED_ROAMING`.

`onDownloadProgress(DownloadProgressInfo progress)`
:   The download service calls this to deliver a `DownloadProgressInfo` object,
    which describes various information about the download progress, including estimated time remaining,
    current speed, overall progress, and total so you can update the download progress UI.

**Tip:** For examples of these callbacks that update the download
progress UI, see the `SampleDownloaderActivity` in the sample app provided with the
Apk Expansion package.

Some public methods for the `IDownloaderService` interface you might find useful are:

`requestPauseDownload()`
:   Pauses the download.

`requestContinueDownload()`
:   Resumes a paused download.

`setDownloadFlags(int flags)`
:   Sets user preferences for network types on which its OK to download the files. The
    current implementation supports one flag, `FLAGS_DOWNLOAD_OVER_CELLULAR`, but you can add
    others. By default, this flag is *not* enabled, so the user must be on Wi-Fi to download
    expansion files. You might want to provide a user preference to enable downloads over
    the cellular network. In which case, you can call:  

    ### Kotlin

    ```kotlin
    remoteService = DownloaderServiceMarshaller.CreateProxy(m).apply {
        ...
        setDownloadFlags(IDownloaderService.FLAGS_DOWNLOAD_OVER_CELLULAR)
    }
    ```

    ### Java

    ```java
    remoteService
        .setDownloadFlags(IDownloaderService.FLAGS_DOWNLOAD_OVER_CELLULAR);
    ```

## Using APKExpansionPolicy

If you decide to build your own downloader service instead of using the Google Play
[Downloader Library](https://developer.android.com/google/play/expansion-files#AboutLibraries), you should still use the `APKExpansionPolicy` that's provided in the License Verification Library. The `APKExpansionPolicy` class is nearly identical to `ServerManagedPolicy` (available in the
Google Play License Verification Library) but includes additional handling for the APK expansion
file response extras.

**Note:** If you *do use* the [Downloader Library](https://developer.android.com/google/play/expansion-files#AboutLibraries) as discussed in the previous section, the
library performs all interaction with the `APKExpansionPolicy` so you don't have to use
this class directly.

The class includes methods to help you get the necessary information about the available
expansion files:

- `getExpansionURLCount()`
- `getExpansionURL(int index)`
- `getExpansionFileName(int index)`
- `getExpansionFileSize(int index)`

For more information about how to use the `APKExpansionPolicy` when you're *not*
using the [Downloader Library](https://developer.android.com/google/play/expansion-files#AboutLibraries), see the documentation for [Adding Licensing to Your App](https://developer.android.com/google/play/licensing/adding-licensing),
which explains how to implement a license policy such as this one.

## Reading the Expansion File

Once your APK expansion files are saved on the device, how you read your files
depends on the type of file you've used. As discussed in the [overview](https://developer.android.com/google/play/expansion-files#Overview), your
expansion files can be any kind of file you
want, but are renamed using a particular [file name format](https://developer.android.com/google/play/expansion-files#Filename) and are saved to
`<shared-storage>/Android/obb/<package-name>/`.

Regardless of how you read your files, you should always first check that the external
storage is available for reading. There's a chance that the user has the storage mounted to a
computer over USB or has actually removed the SD card.

**Note:** When your app starts, you should always check whether
the external storage space is available and readable by calling [getExternalStorageState()](https://developer.android.com/reference/android/os/Environment#getExternalStorageState()). This returns one of several possible strings
that represent the state of the external storage. In order for it to be readable by your
app, the return value must be [MEDIA_MOUNTED](https://developer.android.com/reference/android/os/Environment#MEDIA_MOUNTED).

### Getting the file names

As described in the [overview](https://developer.android.com/google/play/expansion-files#Overview), your APK expansion files are saved
using a specific file name format:  

```
[main|patch].<expansion-version>.<package-name>.obb
```

To get the location and names of your expansion files, you should use the
[getExternalStorageDirectory()](https://developer.android.com/reference/android/os/Environment#getExternalStorageDirectory()) and [getPackageName()](https://developer.android.com/reference/android/content/Context#getPackageName()) methods to construct the path to your files.

Here's a method you can use in your app to get an array containing the complete path
to both your expansion files:  

### Kotlin

```kotlin
fun getAPKExpansionFiles(ctx: Context, mainVersion: Int, patchVersion: Int): Array<String> {
    val packageName = ctx.packageName
    val ret = mutableListOf<String>()
    if (Environment.getExternalStorageState() == Environment.MEDIA_MOUNTED) {
        // Build the full path to the app's expansion files
        val root = Environment.getExternalStorageDirectory()
        val expPath = File(root.toString() + EXP_PATH + packageName)

        // Check that expansion file path exists
        if (expPath.exists()) {
            if (mainVersion > 0) {
                val strMainPath = "$expPath${File.separator}main.$mainVersion.$packageName.obb"
                val main = File(strMainPath)
                if (main.isFile) {
                    ret += strMainPath
                }
            }
            if (patchVersion > 0) {
                val strPatchPath = "$expPath${File.separator}patch.$mainVersion.$packageName.obb"
                val main = File(strPatchPath)
                if (main.isFile) {
                    ret += strPatchPath
                }
            }
        }
    }
    return ret.toTypedArray()
}
```

### Java

```java
// The shared path to all app expansion files
private final static String EXP_PATH = "/Android/obb/";

static String[] getAPKExpansionFiles(Context ctx, int mainVersion,
      int patchVersion) {
    String packageName = ctx.getPackageName();
    Vector<String> ret = new Vector<String>();
    if (Environment.getExternalStorageState()
          .equals(Environment.MEDIA_MOUNTED)) {
        // Build the full path to the app's expansion files
        File root = Environment.getExternalStorageDirectory();
        File expPath = new File(root.toString() + EXP_PATH + packageName);

        // Check that expansion file path exists
        if (expPath.exists()) {
            if ( mainVersion > 0 ) {
                String strMainPath = expPath + File.separator + "main." +
                        mainVersion + "." + packageName + ".obb";
                File main = new File(strMainPath);
                if ( main.isFile() ) {
                        ret.add(strMainPath);
                }
            }
            if ( patchVersion > 0 ) {
                String strPatchPath = expPath + File.separator + "patch." +
                        mainVersion + "." + packageName + ".obb";
                File main = new File(strPatchPath);
                if ( main.isFile() ) {
                        ret.add(strPatchPath);
                }
            }
        }
    }
    String[] retArray = new String[ret.size()];
    ret.toArray(retArray);
    return retArray;
}
```

You can call this method by passing it your app [Context](https://developer.android.com/reference/android/content/Context)
and the desired expansion file's version.

There are many ways you could determine the expansion file version number. One simple way is to
save the version in a [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences) file when the download begins, by
querying the expansion file name with the `APKExpansionPolicy` class's `getExpansionFileName(int index)` method. You can then get the version code by reading the [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences) file when you want to access the expansion
file.

For more information about reading from the shared storage, see the [Data Storage](https://developer.android.com/guide/topics/data/data-storage#filesExternal)
documentation.

### Using the APK Expansion Zip Library

The Google Market Apk Expansion package includes a library called the APK
Expansion Zip Library (located in `<sdk>/extras/google/google_market_apk_expansion/zip_file/`). This is an optional library that
helps you read your expansion
files when they're saved as ZIP files. Using this library allows you to easily read resources from
your ZIP expansion files as a virtual file system.

The APK Expansion Zip Library includes the following classes and APIs:

`APKExpansionSupport`
:   Provides some methods to access expansion file names and ZIP files:

    `getAPKExpansionFiles()`
    :   The same method shown above that returns the complete file path to both expansion
        files.

    `getAPKExpansionZipFile(Context ctx, int mainVersion, int
    patchVersion)`
    :   Returns a `ZipResourceFile` representing the sum of both the main file and
        patch file. That is, if you specify both the `mainVersion` and the
        `patchVersion`, this returns a `ZipResourceFile` that provides read access to
        all the data, with the patch file's data merged on top of the main file.

`ZipResourceFile`
:   Represents a ZIP file on the shared storage and performs all the work to provide a virtual
    file system based on your ZIP files. You can get an instance using `APKExpansionSupport.getAPKExpansionZipFile()` or with the `ZipResourceFile` by passing it the
    path to your expansion file. This class includes a variety of useful methods, but you generally
    don't need to access most of them. A couple of important methods are:

    `getInputStream(String assetPath)`
    :   Provides an [InputStream](https://developer.android.com/reference/java/io/InputStream) to read a file within the ZIP file. The
        `assetPath` must be the path to the desired file, relative to
        the root of the ZIP file contents.

    `getAssetFileDescriptor(String assetPath)`
    :   Provides an [AssetFileDescriptor](https://developer.android.com/reference/android/content/res/AssetFileDescriptor) for a file within the
        ZIP file. The `assetPath` must be the path to the desired file, relative to
        the root of the ZIP file contents. This is useful for certain Android APIs that require an [AssetFileDescriptor](https://developer.android.com/reference/android/content/res/AssetFileDescriptor), such as some [MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer) APIs.

`APEZProvider`
:   Most apps don't need to use this class. This class defines a [ContentProvider](https://developer.android.com/reference/android/content/ContentProvider) that marshals the data from the ZIP files through a content
    provider [Uri](https://developer.android.com/reference/android/net/Uri) in order to provide file access for certain Android APIs that
    expect [Uri](https://developer.android.com/reference/android/net/Uri) access to media files. For example, this is useful if you want to
    play a video with [VideoView.setVideoURI()](https://developer.android.com/reference/android/widget/VideoView#setVideoURI(android.net.Uri)).

#### Skipping ZIP compression of media files

If you're using your expansion files to store media files, a ZIP file still allows you to
use Android media playback calls that provide offset and length controls (such as [MediaPlayer.setDataSource()](https://developer.android.com/reference/android/media/MediaPlayer#setDataSource(java.io.FileDescriptor, long, long)) and
[SoundPool.load()](https://developer.android.com/reference/android/media/SoundPool#load(java.io.FileDescriptor, long, long, int))). In order for
this to work, you must not perform additional compression on the media files when creating the ZIP
packages. For example, when using the `zip` tool, you should use the `-n`
option to specify the file suffixes that should not be compressed:

`zip -n .mp4;.ogg main_expansion media_files`

#### Reading from a ZIP file

When using the APK Expansion Zip Library, reading a file from your ZIP usually requires the
following:  

### Kotlin

```kotlin
// Get a ZipResourceFile representing a merger of both the main and patch files
val expansionFile =
        APKExpansionSupport.getAPKExpansionZipFile(appContext, mainVersion, patchVersion)

// Get an input stream for a known file inside the expansion file ZIPs
expansionFile.getInputStream(pathToFileInsideZip).use {
    ...
}
```

### Java

```java
// Get a ZipResourceFile representing a merger of both the main and patch files
ZipResourceFile expansionFile =
    APKExpansionSupport.getAPKExpansionZipFile(appContext,
        mainVersion, patchVersion);

// Get an input stream for a known file inside the expansion file ZIPs
InputStream fileStream = expansionFile.getInputStream(pathToFileInsideZip);
```

The above code provides access to any file that exists in either your main expansion file or
patch expansion file, by reading from a merged map of all the files from both files. All you
need to provide the `getAPKExpansionFile()` method is your app `android.content.Context` and the version number for both the main expansion file and patch
expansion file.

If you'd rather read from a specific expansion file, you can use the `ZipResourceFile` constructor with the path to the desired expansion file:  

### Kotlin

```kotlin
// Get a ZipResourceFile representing a specific expansion file
val expansionFile = ZipResourceFile(filePathToMyZip)

// Get an input stream for a known file inside the expansion file ZIPs
expansionFile.getInputStream(pathToFileInsideZip).use {
    ...
}
```

### Java

```java
// Get a ZipResourceFile representing a specific expansion file
ZipResourceFile expansionFile = new ZipResourceFile(filePathToMyZip);

// Get an input stream for a known file inside the expansion file ZIPs
InputStream fileStream = expansionFile.getInputStream(pathToFileInsideZip);
```

For more information about using this library for your expansion files, look at
the sample app's `SampleDownloaderActivity` class, which includes additional code to
verify the downloaded files using CRC. Beware that if you use this sample as the basis for
your own implementation, it requires that you **declare the byte size of your expansion
files** in the `xAPKS` array.

## Testing Your Expansion Files

Before publishing your app, there are two things you should test: Reading the
expansion files and downloading the files.

### Testing file reads

Before you upload your app to Google Play, you
should test your app's ability to read the files from the shared storage. All you need to do
is add the files to the appropriate location on the device shared storage and launch your
app:

1. On your device, create the appropriate directory on the shared storage where Google Play will save your files. For example, if your package name is `com.example.android`, you need to create
   the directory `Android/obb/com.example.android/` on the shared storage space. (Plug in
   your test device to your computer to mount the shared storage and manually create this
   directory.)

2. Manually add the expansion files to that directory. Be sure that you rename your files to match the [file name format](https://developer.android.com/google/play/expansion-files#Filename) that Google Play will use.

   For example, regardless of the file type, the main expansion file for the `com.example.android` app should be `main.0300110.com.example.android.obb`.
   The version code can be whatever value you want. Just remember:
   - The main expansion file always starts with `main` and the patch file starts with `patch`.
   - The package name always matches that of the APK to which the file is attached on Google Play.
3. Now that the expansion file(s) are on the device, you can install and run your app to test your expansion file(s).

Here are some reminders about handling the expansion files:

- **Do not delete or rename** the `.obb` expansion files (even if you unpack the data to a different location). Doing so will cause Google Play (or your app itself) to repeatedly download the expansion file.
- **Do not save other data into your `obb/`
  directory** . If you must unpack some data, save it into the location specified by [getExternalFilesDir()](https://developer.android.com/reference/android/content/Context#getExternalFilesDir(java.lang.String)).

### Testing file downloads

Because your app must sometimes manually download the expansion files when it first
opens, it's important that you test this process to be sure your app can successfully query
for the URLs, download the files, and save them to the device.

To test your app's implementation of the manual download procedure,
you can publish it to the internal test track, so it's only available to
authorized testers. If everything works as expected, your app should
begin downloading the expansion files as soon as the main activity starts.

**Note:** Previously you could test an app by
uploading an unpublished "draft" version. This functionality is no longer
supported. Instead, you must publish it to an internal, closed, or open testing
track. For more information, see
[Draft Apps are No
Longer Supported](https://developer.android.com/google/play/billing/billing_testing#draft_apps).

## Updating Your app

One of the great benefits to using expansion files on Google Play is the ability to
update your app without re-downloading all of the original assets. Because Google Play
allows you to provide two expansion files with each APK, you can use the second file as a "patch"
that provides updates and new assets. Doing so avoids the
need to re-download the main expansion file which could be large and expensive for users.

The patch expansion file is technically the same as the main expansion file and neither
the Android system nor Google Play perform actual patching between your main and patch expansion
files. Your app code must perform any necessary patches itself.

If you use ZIP files as your expansion files, the [APK Expansion Zip
Library](https://developer.android.com/google/play/expansion-files#ZipLib) that's included with the Apk Expansion package includes the ability to merge
your
patch file with the main expansion file.

**Note:** Even if you only need to make changes to the patch
expansion file, you must still update the APK in order for Google Play to perform an update.
If you don't require code changes in the app, you should simply update the [`versionCode`](https://developer.android.com/guide/topics/manifest/manifest-element#vcode) in the
manifest.

As long as you don't change the main expansion file that's associated with the APK
in the Play Console, users who previously installed your app will not
download the main expansion file. Existing users receive only the updated APK and the new patch
expansion file (retaining the previous main expansion file).

Here are a few issues to keep in mind regarding updates to expansion files:

- There can be only two expansion files for your app at a time. One main expansion file and one patch expansion file. During an update to a file, Google Play deletes the previous version (and so must your app when performing manual updates).
- When adding a patch expansion file, the Android system does not actually patch your app or main expansion file. You must design your app to support the patch data. However, the Apk Expansion package includes a library for using ZIP files as expansion files, which merges the data from the patch file into the main expansion file so you can easily read all the expansion file data.