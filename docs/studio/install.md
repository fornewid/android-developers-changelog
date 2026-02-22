---
title: https://developer.android.com/studio/install
url: https://developer.android.com/studio/install
source: md.txt
---

# Install Android Studio

| **Note:** Service integrations, such as Gemini in Android Studio and Firebase Crashlytics, are only available in the latest stable channel version of Android Studio and major versions (including their patches) released in the previous 10 months. If you are using an older version of Android Studio, you will need to update to access Cloud services. For more information, see[Android Studio and Cloud services compatibility](https://developer.android.com/studio/releases#service-compat).

Set up Android Studio in just a few clicks. First, check the system requirements. Then[download the latest version of Android Studio](https://developer.android.com/studio).

The Android Emulator lets you test your apps across a wide range of device configurations and Android API levels without needing a physical device. For this reason, it's the preferred method for testing your Android apps. To learn more, see[Run apps on the Android Emulator](https://developer.android.com/studio/run/emulator).

However, you can also use Android Studio without the Emulator by using a modern physical[Android Device](https://www.android.com/phones/help-me-choose/)or the[Android Device Streaming Service](https://developer.android.com/studio/run/android-device-streaming)to deploy and test apps.

If your system has limited resources, you might consider our cloud-based IDE solution,[Android Studio on IDX](https://idx.google.com/android-studio), which offers a powerful development environment without the need for high-end local hardware.

**Minimum for Android Studio, and Android Studio with the Android Emulator.**

The minimum requirements listed allow you to get started with Android Studio and typically apply to the following use cases:

- Creating and supporting smaller projects and samples.

- Creating a single Android Virtual Device (AVD).

- Deploying an app to a single AVD, to a local physical device, or to[Android Device Streaming](https://developer.android.com/studio/run/android-device-streaming)devices. This doesn't include XR AVDs.

| **Note:** Some minimum requirements differ depending on whether you want to run Android Studio alone or Android Studio with the Android Emulator. In those cases, both requirements are listed and labelled accordingly with either**Studio** or**Studio \& Emulator**.

**Recommended to run Android Studio and the Android Emulator.**

These are the recommended system specifications to run Android Studio and the Android Emulator. This typically covers the following use cases:

- Professional development on larger, more complex codebases.

| **Note:** Larger projects require higher RAM and CPU specs for compilation and loading in the IDE.

- Creating multiple Android Virtual Devices (AVD), including XR devices.

| **Note:** You might need up to 6GB of additional storage for each additional AVD created.

- Running multiple AVDs simultaneously, including XR devices.

| **Note:** Running multiple AVDs simultaneously requires approximately 4GB of memory per AVD. The exact amount might vary depending on your system.

## Windows

| **Note:** Windows machines with ARM-based CPUs aren't currently supported.

Here are the system requirements for Windows:

|    Requirement    |                                                                                                                            Minimum                                                                                                                             |                                                                                                                                                                                            Recommended                                                                                                                                                                                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OS                | 64-bit Microsoft Windows 10                                                                                                                                                                                                                                    | Latest 64-bit version of Windows                                                                                                                                                                                                                                                                                                                                                                  |
| RAM               | **Studio:** 8 GB **Studio \& Emulator:**16GB                                                                                                                                                                                                                   | 32GB                                                                                                                                                                                                                                                                                                                                                                                              |
| CPU               | Virtualization support Required (Intel VT-x or AMD-V, enabled in BIOS). CPU microarchitecture after 2017. [Intel 8th Gen Core](https://www.intel.com/content/www/us/en/processors/processor-numbers.html)i5 / AMD Zen Ryzen (e.g., Intel i5-8xxx, Ryzen 1xxx). | Virtualization support Required (Intel VT-x or AMD-V, enabled in BIOS). Latest CPU microarchitecture. Look for CPUs from the Intel Core i5, i7, or i9 series and or the suffixes H/HK/HX for laptop or suffixes S/F/K for desktop, or the AMD Ryzen 5, 6, 7, or 9 series. Please be aware that Intel® Core™ N-Series and U-Series processors are not recommended due to insufficient performance. |
| Disk space        | **Studio:** 8 GB of free space. **Studio \& Emulator:**16GB of free space                                                                                                                                                                                      | Solid state drive with 32 GB or more                                                                                                                                                                                                                                                                                                                                                              |
| Screen resolution | 1280 x 800                                                                                                                                                                                                                                                     | 1920 x 1080                                                                                                                                                                                                                                                                                                                                                                                       |
| GPU               | **Studio:** None **Studio \& Emulator:**GPU with 4GB VRAM such as Nvidia Geforce 10 series or newer, or AMD Radeon RX 5000 or newer with the latest drivers                                                                                                    | GPU with 8GB VRAM such as Nvidia Geforce 20 series or newer, or AMD Radeon RX6600 or newer with the latest drivers.                                                                                                                                                                                                                                                                               |

To install Android Studio on Windows, follow these steps:

- If you downloaded an`EXE`file (recommended), double-click to launch it.

- If you downloaded a`Zip`file:

  1. Unpack the`Zip`.
  2. Copy the**android-studio** folder into your**Program Files**folder.
  3. Open the**android-studio \> bin**folder.
  4. Launch`studio64.exe`(for 64-bit machines) or`studio.exe`(for 32-bit machines).
  5. Follow the**Setup Wizard**in Android Studio and install any recommended SDK packages.

The following video shows each step of the setup procedure for the recommended`.exe`download:

Android Studio notifies you with a dialog when new tools and other APIs become available. To manually check for updates, click**Help \> Check for Update**.

## Mac

Here are the system requirements for Mac:

|    Requirement    |                                                                               Minimum                                                                               |                     Recommended                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| OS                | macOS 12                                                                                                                                                            | Latest 64-bit version of macOS                      |
| RAM               | **Studio:** 8 GB **Studio \& Emulator:**16GB                                                                                                                        | 32 GB                                               |
| CPU               | Apple M1 chip, or 6th generation Intel Core or newer. e.g. 2016 MacBook Pro with i7-4770HQ processor or higher. We are phasing out support for Mac with Intel chips | Latest Apple Silicon                                |
| Disk space        | **Studio:** 8 GB of free space. **Studio \& Emulator:**16GB of free space.                                                                                          | Solid state drive with 32 GB or more of free space. |
| Screen resolution | 1280 x 800                                                                                                                                                          | 1920 x 1080                                         |
| GPU               | Integrated                                                                                                                                                          | Integrated                                          |

To install Android Studio on your Mac, follow these steps:

1. Launch the Android Studio DMG file.
2. Drag Android Studio into the Applications folder, then launch Android Studio.
3. Choose whether to import previous Android Studio settings, then click**OK**.
4. Complete the Android Studio**Setup Wizard**, which includes downloading the Android SDK components that are required for development.

The following video shows each step of the recommended setup procedure:

Android Studio notifies you with a dialog when new tools and other APIs become available. To manually check for updates, click**Android Studio \> Check for Updates**.

## Linux

| **Note:** Linux machines with ARM-based CPUs aren't currently supported.

Here are the system requirements for Linux:

|    Requirement    |                                                                                                                           Minimum                                                                                                                            |                                                                                                                                                                                          Recommended                                                                                                                                                                                           |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OS                | Any 64-bit Linux distribution that supports Gnome, KDE, or Unity DE; GNU C Library (glibc) 2.31 or later.                                                                                                                                                    | Latest 64-bit version of Linux                                                                                                                                                                                                                                                                                                                                                                 |
| RAM               | **Studio:** 8 GB **Studio \& Emulator:**16GB                                                                                                                                                                                                                 | 32 GB RAM or more                                                                                                                                                                                                                                                                                                                                                                              |
| CPU               | Virtualization support Required (Intel VT-x or AMD-V, enabled in BIOS). CPU microarchitecture after 2017[Intel 8th Gen Core](https://www.intel.com/content/www/us/en/processors/processor-numbers.html)i5 / AMD Zen Ryzen (e.g., Intel i5-8xxx, Ryzen 1xxx). | Virtualization support Required (Intel VT-x or AMD-V, enabled in BIOS). Latest CPU microarchitecture Look for CPUs from the Intel Core i5, i7, or i9 series and or the suffixes H/HK/HX for laptop or suffixes S/F/K for desktop, or the AMD Ryzen 5, 6, 7, or 9 series. Please be aware that Intel Core N-Series and U-Series processors are not recommended due to insufficient performance. |
| Disk space        | **Studio:** 8 GB of free space. **Studio \& Emulator:**16GB of free space.                                                                                                                                                                                   | Solid state drive with 32 GB or more                                                                                                                                                                                                                                                                                                                                                           |
| Screen resolution | 1280 x 800                                                                                                                                                                                                                                                   | 1920 x 1080                                                                                                                                                                                                                                                                                                                                                                                    |
| GPU               | **Studio:** None **Studio \& Emulator:**GPU with 4GB VRAM such as Nvidia Geforce 10 series or newer, or AMD Radeon RX 5000 or newer with the latest drivers                                                                                                  | GPU with 8GB VRAM uch as Nvidia Geforce 20 series or newer, or AMD Radeon RX 6600 or newer with the latest drivers                                                                                                                                                                                                                                                                             |

To install Android Studio on Linux, follow these steps:

1. Unpack the`.tar.gz`file you downloaded to an appropriate location for your applications, such as within`/usr/local/`for your user profile or`/opt/`for shared users.

   For a 64-bit version of Linux, first install the[required libraries for 64-bit machines](https://developer.android.com/studio/install#64bit-libs).
2. To launch Android Studio, open a terminal, navigate to the`android-studio/bin/`directory, and execute`studio`.
3. Select whether you want to import previous Android Studio settings, then click**OK**.
4. Complete the Android Studio**Setup Wizard**, which includes downloading the Android SDK components that are required for development.

**Tip:** To make Android Studio available in your list of applications, select**Tools \> Create Desktop Entry**from the Android Studio menu bar.

### Required libraries for 64-bit machines

If you are running a 64-bit version of Ubuntu, you need to install some 32-bit libraries with the following command:  

```
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386
```

If you are running 64-bit Fedora, the command is:  

```
sudo yum install zlib.i686 ncurses-libs.i686 bzip2-libs.i686
```

The following video shows each step of the recommended setup procedure:

Android Studio notifies you with a dialog when new tools and other APIs become available. To manually check for updates, click**Help \> Check for Update**.

## ChromeOS

For the system requirements to support Android Studio and the Android Emulator, see[Android development](https://chromeos.dev/en/android-environment#install-android-studio-on-chrome-os)in the ChromeOS documentation.

To install Android Studio on ChromeOS, follow these steps:

1. Install[Linux for ChromeOS](https://support.google.com/chromebook/answer/9145439).
2. Open the**Files** app and locate the DEB package in the**Downloads** folder under**My files**.
3. Right-click the DEB package and select**Install with Linux (Beta)**.

   ![The target file location for DEB package on ChromeOS.](https://developer.android.com/static/studio/images/studio-install-chromeos.png)
   - If you have installed Android Studio before, select whether you want to import previous Android Studio settings, then click**OK**.
4. Complete the Android Studio**Setup Wizard**, which includes downloading the Android SDK components that are required for development.

5. Once the installation is complete, launch Android Studio from the Launcher or from the ChromeOS Linux terminal. In the default installation directory`/opt/android-studio/bin`, run`studio`.

Android Studio notifies you with a dialog when new tools and other APIs become available. To manually check for updates, click**Help \> Check for Update**.
| **Note:** Android Studio on ChromeOS currently supports deploying your app only to a connected hardware device. To learn more, read[Run apps on a hardware device](https://developer.android.com/studio/run/device).