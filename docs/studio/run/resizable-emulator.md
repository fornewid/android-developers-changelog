---
title: https://developer.android.com/studio/run/resizable-emulator
url: https://developer.android.com/studio/run/resizable-emulator
source: md.txt
---

# Test on multiple screen sizes with the resizable emulator

| **Note:** The resizable emulator is no longer experimental starting in Android Studio Narwhal Feature Drop.

Test your app on multiple screen sizes with a single resizable emulator. Testing on a single resizable emulator not only allows you to rapidly test changes across different interfaces, but also promotes a smoother development experience by saving the compute resources and memory that would be required to maintain separate virtual devices.

To create a resizable Android Virtual Device (AVD) follow these steps:

1. In the[create device flow](https://developer.android.com/studio/run/managing-avds#createavd), select the**Resizable (Experimental)**phone hardware profile.
2. Download the system image for API level 34 or higher.
3. Follow the prompts to create the AVD.

When you deploy your app to the resizable emulator, use the**Display Mode**dropdown in the emulator toolbar to quickly toggle between a set of common device types. The emulator screen resizes so you can easily test your app across a range of screen sizes and densities.

![Resizable emulator Display Mode dropdown menu](https://developer.android.com/static/studio/images/resizable-emulator.png)