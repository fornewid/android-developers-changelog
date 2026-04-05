---
title: Set up continuous integration  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/projects/continuous-integration
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Set up continuous integration Stay organized with collections Save and categorize content based on your preferences.




Continuous integration systems let you automatically build and test your app
every time you check in updates to your source control system. You can use any
continuous integration tool that can initiate a Gradle build to build your
Android Studio projects.

To run tests as part of the build, you need to either configure
your continuous integration server to use the
[Android Emulator](/studio/run/emulator-commandline) or use
[Firebase Test Lab](https://firebase.google.com/docs/test-lab/)
to run your tests.

For specific information about configuring continuous integration for your
Android project using Jenkins and Firebase Test Lab, see
[Start testing with continuous integration (CI)
systems](https://firebase.google.com/docs/test-lab/continuous).

**Note:** You must accept the license agreements for any packages your app requires
on each machine where you build your app. If you have not installed Android
Studio on your continuous integration server, you can [accept licenses from the
command line using
`sdkmanager`](/studio/command-line/sdkmanager#accept-licenses).