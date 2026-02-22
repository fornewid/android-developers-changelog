---
title: https://developer.android.com/studio/preview/android-studio-cloud
url: https://developer.android.com/studio/preview/android-studio-cloud
source: md.txt
---

# Android Studio Cloud

![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/try-asc-card.png)[Try Android Studio Cloud](https://studio.firebase.google.com/new/android-studio)
| **Note:** **Android Studio Cloud**is in the experimental phase. Its features and capabilities are subject to change substantially.

[Android Studio Cloud](https://studio.firebase.google.com/new/android-studio), accessed through[Firebase Studio](https://studio.firebase.google.com/), enables developers to conveniently open Android Studio projects anywhere with an internet connection. While we're experimenting with streaming technologies, you'll be interacting with a remotely streamed Linux virtual machine (VM) running Android Studio on the web. Expect a user experience similar to running the Linux version of Android Studio.

Whether it's exploring sample projects or accessing existing Android app projects on GitHub, our goal is that this feature can streamline your development workflow by eliminating the need for local installations.

You can expect:

- Dedicated workspaces in which we have pre-downloaded the necessary Android SDK components and Android Studio IDE for you to explore and build your Android app
- Access to your Android Studio Cloud from anywhere
- The ability to create multiple workspaces at once

See the current[known limitations and workarounds](https://developer.android.com/studio/preview/android-studio-cloud#known-issues-and-workarounds). We wish to learn more about your feedback and gradually add more capabilities as Android Studio Cloud progresses through the experimental stage. Please report any feedback and issues through the[issue tracker](https://developer.android.com/studio/report-bugs)and this[survey](https://forms.gle/QEjcFbZJCNjcRde58).

*** ** * ** ***

## Get started

|                                                                                                                                                                                                                                                                                                                                               Steps                                                                                                                                                                                                                                                                                                                                               ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [Try Android Studio Cloud](https://studio.firebase.google.com/new/android-studio)and name your workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | ![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/try-asc.png)           |
| Click**Create**and wait for the workspace to be initialized.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/set-up-workspace.png)  |
| Once loaded, you will land in the VM linux environment where Android Studio launches. Choose whether or not you would like to send analytics to Google.                                                                                                                                                                                                                                                                                                                                                                                                                               | ![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/send-analytics.png)    |
| To start a new project or open a project for the first time, either create a**New Project, Get from VCS** , or click**More Actions** and select**Import an Android Code Sample**to get started with an Android project.                                                                                                                                                                                                                                                                                                                                                               | ![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/start-new-project.png) |
| As an example, you can select**New Project** and open an**Empty Activity**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/new-project.png)       |
| You will then land in Android Studio, and you can try development tasks that you would usually do: - Create a new project - Import projects from Git or GitHub - Edit code - Create previews - Deploy to an emulator - Use the debugger, layout inspector, profiler, and more - Leverage AI in your development workflow with[Gemini in Android Studio](https://developer.android.com/gemini-in-android) When you're working, be aware of current[known limitations and workarounds](https://developer.android.com/studio/preview/android-studio-cloud#known-issues-and-workarounds). | ![](https://developer.android.com/static/studio/images/preview/android-studio-cloud/android-studio.png)    |

*** ** * ** ***

## Workflows to try

You can access many of the same services in Android Studio Cloud as on the desktop version. Try these common workflows:

- Deploy your app on a virtual or physical device.

  - If you deploy to the[Android emulator](https://developer.android.com/studio/run/emulator), we recommend using the**Pixel 8a API 35** (that is pre-configured) or**Small Phone API 35**. We've found that these two devices work better than other emulators, which are generally very slow---especially on first start---due to nested virtualization.

  ![Device manager UI example](https://developer.android.com/static/studio/images/preview/android-studio-cloud/android-emulator-device-manager.png)
  - Alternatively, you can deploy to a physical device by using[Android Device Streaming](https://developer.android.com/studio/run/android-device-streaming), powered by Firebase. Running the app on a real device should be faster than an emulator.
- Try[Gemini in Android Studio](https://developer.android.com/gemini-in-android). Ask questions, get AI-assisted code completion, get code suggestions, and more.

- Get your code into Android Studio Cloud from a version control system using**Get from VCS** from the welcome dialog. For more information about importing projects from Git, see[Set up a Git repository](https://www.jetbrains.com/help/idea/set-up-a-git-repository.html)in the IntelliJ documentation.

![Welcome to Android Studio UI](https://developer.android.com/static/studio/images/preview/android-studio-cloud/get-from-vcs.png)

*** ** * ** ***

## Known issues and workarounds

- To interact with Android Studio Cloud you must use a[Linux keyboard mapping](https://resources.jetbrains.com/storage/products/intellij-idea/docs/IntelliJIDEA_ReferenceCard.pdf).
- Only the latest stable version of Android Studio is available.
- If you are logging into Android Studio, accounts that require**physical** two factor authentication won't work. Consider using alternative methods, if supported, for example authenticator apps like[Google Authenticator](https://support.google.com/accounts/answer/1066447?co=GENIE.Platform%3DAndroid).
- The Android Emulator will be slow to boot up for the first time. We recommend letting it run for about 10 minutes after you first create it before deploying your app to it.
- You can't deploy to a local Android physical device.
- Sometimes the "Choose password for new keyring" popup appears. When this happens, click**Cancel**to close it.

![Choose password for new keyring UI example](https://developer.android.com/static/studio/images/preview/android-studio-cloud/choose-password-for-keyring.png)

- Ignore popups related to updates from the Linux machines for now.

![Linux software updater notification example](https://developer.android.com/static/studio/images/preview/android-studio-cloud/linux-software-updater.png)

- To download APK from Android Studio Cloud:
  1. Click**Locate**after you generated an APK.
  2. This will take you to the APK location.
  3. Upload the APK to the cloud storage services (e.g. Google Drive) of your choice using Chrome.

![CLick Locate in generated APK notification](https://developer.android.com/static/studio/images/preview/android-studio-cloud/generate-apk.png)