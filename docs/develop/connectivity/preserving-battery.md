---
title: https://developer.android.com/develop/connectivity/preserving-battery
url: https://developer.android.com/develop/connectivity/preserving-battery
source: md.txt
---

> Documentation index: https://developer.android.com/develop/connectivity/llms.txt

Users rely on their mobile devices for virtually everything these days, from
sending emails and managing finances, to streaming videos and streaming and
playing video games. In order to be useful, most apps require data, images, and
other media from remote services. It's important to remember that your app is
just one of many apps on the user's device, all competing for network resources.
Managed poorly, this can have a dramatic and detrimental impact on battery
performance and unnecessarily use the user's limited network bandwidth.

In [Android 8.0 (API level 26)](https://developer.android.com/about/versions/oreo/android-8.0-changes.md.txt) and higher, several OS updates help preserve
battery, user experience, and system health. However, there are additional
considerations, strategies, and patterns that you can employ as well. Requests
that your app makes to the network can be a major cause of battery drain because
they rely on power-consuming cellular and Wi-Fi radios.

In this guide, you'll learn about the following:

- How your app's connectivity model interacts with the wireless radio state machine.
- How to employ techniques for minimizing the impact of your data connection.
- How to troubleshoot slow connections.
- How to run background work only under specific conditions such as when the device is charging or on Wi-Fi.
- How to track your app's battery usage over time.

Finally, you'll learn about three broad categories of updates:
[User-initiated](https://developer.android.com/develop/connectivity/minimize-effect-regular-updates.md.txt#user-initiated), [App-initiated](https://developer.android.com/develop/connectivity/minimize-effect-regular-updates.md.txt#app-initiated), and [Server-initiated](https://developer.android.com/develop/connectivity/minimize-effect-regular-updates.md.txt#server-initiated), with tools
and techniques for maximizing the efficiency of each category.

Ultimately, optimize your app's network usage to provide the best experience
for your users.

## Additional material

[Video](https://www.youtube.com/watch?v=fEEulSk1kNY)