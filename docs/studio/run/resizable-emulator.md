---
title: Test on multiple screen sizes with the resizable emulator  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/run/resizable-emulator
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Test on multiple screen sizes with the resizable emulator Stay organized with collections Save and categorize content based on your preferences.



**Note:** The resizable emulator is no longer experimental starting in Android
Studio Narwhal Feature Drop.

Test your app on multiple screen sizes with a single resizable emulator. Testing
on a single resizable emulator not only allows you to rapidly test changes
across different interfaces, but also promotes a smoother development experience
by saving the compute resources and memory that would be required to maintain
separate virtual devices.

To create a resizable Android Virtual Device (AVD) follow these steps:

1. In the
   [create device flow](https://developer.android.com/studio/run/managing-avds#createavd),
   select the **Resizable (Experimental)** phone hardware profile.
2. Download the system image for API level 34 or higher.
3. Follow the prompts to create the AVD.

When you deploy your app to the resizable emulator, use the **Display Mode**
dropdown in the emulator toolbar to quickly toggle between a set of common
device types. The emulator screen resizes so you can easily test your app across
a range of screen sizes and densities.

![Resizable emulator Display Mode dropdown menu](/static/studio/images/resizable-emulator.png)