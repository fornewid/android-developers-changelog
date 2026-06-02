---
title: Download Android CLI  |  Android Studio  |  Android Developers
url: https://developer.android.com/tools/agents/android-cli/download
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Studio](https://developer.android.com/studio)

# Download Android CLI Stay organized with collections Save and categorize content based on your preferences.





This page provides download links for the latest Android CLI releases. Select
your platform using the tabs, and use the dropdown to choose an installation
method. For the fastest way to download and install, run the curl command for
your operating system in your terminal.

## Linux

Select installer
curl | bash
apt-get
Direct download


* ### Download for Linux using curl | bash

  **Local installation**

  Install the CLI only for your user account. Local installation does not require elevated permissions.

  ```
  curl -fsSL https://dl.google.com/android/cli/latest/linux_x86_64/install.sh | bash
  ```

  **Global installation**

  Install the CLI for all users on this machine. Global installation requires sudo or Admin privileges.

  ```
  curl -fsSL https://dl.google.com/android/cli/latest/linux_x86_64/install_root.sh | bash
  ```
* ### Download for Linux using apt-get

  Configure the repository and install the package:

  ```
  curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | sudo tee /etc/apt/keyrings/google.asc >/dev/null
  sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google.asc] http://dl.google.com/android/cli/latest/debian/ stable main" > /etc/apt/sources.list.d/android-cli.list'
  sudo apt-get update
  sudo apt-get install android-cli
  ```
* ### Download for Linux directly

  [Download Android CLI for Linux
  download](https://dl.google.com/android/cli/latest/linux_x86_64/android)

## Mac with Apple chip

Select installer
curl | bash
homebrew
Direct download


* ### Download for Mac with Apple chip using curl | bash

  **Local installation**

  Install the CLI only for your user account. Local installation does not require elevated permissions.

  ```
  curl -fsSL https://dl.google.com/android/cli/latest/darwin_arm64/install.sh | bash
  ```

  **Global installation**

  Install the CLI for all users on this machine. Global installation requires sudo or Admin privileges.

  ```
  curl -fsSL https://dl.google.com/android/cli/latest/darwin_arm64/install_root.sh | bash
  ```
* ### Download for Mac with Apple chip using homebrew

  We distribute Android CLI through a Homebrew tap. Make sure that you have [Homebrew](https://brew.sh/) installed before proceeding.

  ```
  brew tap android/tap
  brew install android-cli
  ```
* ### Download for Mac with Apple chip directly

  [Download Android CLI for Mac with Apple chip
  download](https://dl.google.com/android/cli/latest/darwin_arm64/android)

## Mac with Intel chip

Select installer
curl | bash
homebrew
Direct download


* ### Download for Mac with Intel chip using curl | bash

  **Local installation**

  Install the CLI only for your user account. Local installation does not require elevated permissions.

  ```
  curl -fsSL https://dl.google.com/android/cli/latest/darwin_x86_64/install.sh | bash
  ```

  **Global installation**

  Install the CLI for all users on this machine. Global installation requires sudo or Admin privileges.

  ```
  curl -fsSL https://dl.google.com/android/cli/latest/darwin_x86_64/install_root.sh | bash
  ```
* ### Download for Mac with Intel chip using homebrew

  We distribute Android CLI through a Homebrew tap. Make sure that you have [Homebrew](https://brew.sh/) installed before proceeding.

  ```
  brew tap android/tap
  brew install android-cli
  ```
* ### Download for Mac with Intel chip directly

  [Download Android CLI for Mac with Intel chip
  download](https://dl.google.com/android/cli/latest/darwin_x86_64/android)

## Windows

Select installer
curl | cmd
winget
Direct download


* ### Download for Windows using curl | cmd

  **Local installation**

  Install the CLI only for your user account. Local installation does not require elevated permissions.

  ```
  curl.exe -fsSL https://dl.google.com/android/cli/latest/windows_x86_64/install.cmd -o "%TEMP%\i.cmd" && "%TEMP%\i.cmd"
  ```

  **Global installation**

  Install the CLI for all users on this machine. Global installation requires sudo or Admin privileges.

  ```
  curl.exe -fsSL https://dl.google.com/android/cli/latest/windows_x86_64/install_admin.cmd -o "%TEMP%\i.cmd" && "%TEMP%\i.cmd"
  ```
* ### Download for Windows using winget

  ```
  winget install --id Google.AndroidCLI
  ```
* ### Download for Windows directly

  [Download Android CLI for Windows
  download](https://dl.google.com/android/cli/latest/windows_x86_64/android.exe)