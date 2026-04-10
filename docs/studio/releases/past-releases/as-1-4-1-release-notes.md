---
title: https://developer.android.com/studio/releases/past-releases/as-1-4-1-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-1-4-1-release-notes
source: md.txt
---

<br />

# Android Studio v1.4.1 (October 2015)

Fixes and enhancements:

- Fixed a Gradle model caching issue that could lead to excessive Gradle syncing when the IDE was restarted.
- Fixed a native debugging deadlock issue.
- Fixed an issue blocking users of the Subversion 1.9 version control system.
- Fixed a *Device Chooser* dialog problem where after connecting a device that was unauthorized you could no longer select the emulator. [Issue: 189658](http://b.android.com/189658)
- Fixed incorrect translation error reporting for locales that have a region qualifier and a translation in the region (but not in the base locale). [Issue: 188577](http://b.android.com/188577)
- Fixed a deadlock issue in the Theme Editor related to its interaction with the Layout Editor. [Issue: 188070](http://b.android.com/188070)
- Fixed a Theme Editor reload and edit conflict causing attributes to not properly update. [Issue: 187726](http://b.android.com/187726)
- Improved Theme Editor performance.
- Fixed an issue where the `android:required` attribute was ignored in the manifest. [Issue: 187665](http://b.android.com/187665)

<br />