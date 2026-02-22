---
title: https://developer.android.com/studio/platform/install
url: https://developer.android.com/studio/platform/install
source: md.txt
---

# Install Android Studio for Platform

Set up Android Studio for Platform in just a few clicks. First, check the system requirements. Then[download the latest version of Android Studio](https://developer.android.com/studio/platform).

## Linux

| **Note:** Linux machines with ARM-based CPUs aren't supported.

Here are the system requirements for Linux:

|    Requirement    |                                                               Minimum                                                                |             Recommended              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| OS                | Any 64-bit Linux distribution that supports Gnome, KDE, or Unity DE; GNU C Library (glibc) 2.31 or later.                            | Latest 64-bit version of Linux       |
| RAM               | 8 GB RAM                                                                                                                             | 16 GB RAM or more                    |
| CPU               | x86_64 CPU architecture; 2nd generation Intel Core or newer, or AMD processor with support for AMD Virtualization (AMD-V) and SSSE3. | Latest Intel Core processor          |
| Disk space        | 8 GB (IDE and Android SDK and Emulator)                                                                                              | Solid state drive with 16 GB or more |
| Screen resolution | 1280 x 800                                                                                                                           | 1920 x 1080                          |

## Install on Linux

1. Open a terminal and use the`apt`command to install the downloaded`.deb`file. Using`apt`helps handle any necessary dependencies. Replace`/path/to/your_package.deb`with the actual path to the file you downloaded.

       sudo apt update
       sudo apt install ./asfp-current-linux.deb

   The default installation location is`/opt/android-studio-for-platform/`.
2. Launch ASfP by running the`studio.sh`script located in the`bin`directory of your installation.

       /opt/android-studio-for-platform/bin/studio.sh

3. On the first launch, you'll be prompted to import previous settings (if any) and then guided through the[**setup wizard**](https://developer.android.com/studio/platform/projects/create-project). Follow the prompts to complete the initial configuration.

4. Optional - To create a desktop entry, select**Tools \> Create Desktop Entry**from the ASfP menu bar once the IDE is open.

5. Optional - For easier access from the command line, add the`bin`directory to your system's PATH variable. Add the following line to your shell configuration file (for example the`~/.bashrc`or`~/.zshrc`file):

       export PATH="$PATH:/opt/android-studio-for-platform/bin"

   Remember to source the file by running`source ~/.bashrc`or open a new terminal for the changes to take effect.