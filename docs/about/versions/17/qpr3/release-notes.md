---
title: https://developer.android.com/about/versions/17/qpr3/release-notes
url: https://developer.android.com/about/versions/17/qpr3/release-notes
source: md.txt
---

### Beta 3

|---|---|
| **Release date** | October 29, 2026 |
| **Builds** | DP11.261016.003 DP11.261016.004 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-10-05 |
| **Google Play services** | 26.36.33 |

### Beta 2

|---|---|
| **Release date** | October 20, 2026 |
| **Builds** | DP11.261002.005 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-10-05 |
| **Google Play services** | 26.36.33 |

### Beta 1

|---|---|
| **Release date** | October 2, 2026 |
| **Builds** | DP11.260918.005 DP11.260918.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.32.34 |

### Android 17 QPR 3 Beta 3 (October 2026)

Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

### Top Issues fixed in Beta 3 (October 2026)

Top issues fixed include:

- *Images render with incorrect transparency when using the Multiply blend mode. ([**Issue #73186237**](https://issuetracker.google.com/issues/73186237))*
- *Recents overview flickers when performing a home gesture immediately after quick-switching apps. ([**Issue #237526296**](https://issuetracker.google.com/issues/237526296), [**Issue #341680318**](https://issuetracker.google.com/issues/341680318))*
- *Inner display remains black when unfolding the device. ([**Issue #311469796**](https://issuetracker.google.com/issues/311469796), [**Issue #311583772**](https://issuetracker.google.com/issues/311583772))*
- *Twitter app crashes when viewing post thread mentions. ([**Issue #282904709**](https://issuetracker.google.com/issues/282904709), [**Issue #293383813**](https://issuetracker.google.com/issues/293383813))*
- *Display randomly turns off and on during device usage. ([**Issue #325555461**](https://issuetracker.google.com/issues/325555461))*
- *Poor video quality when using the device as a webcam. ([**Issue #313062628**](https://issuetracker.google.com/issues/313062628))*
- *Toast notifications intermittently fail to display under high memory pressure. ([**Issue #321628126**](https://issuetracker.google.com/issues/321628126))*
- *Home screen wallpaper incorrectly displays on the lock screen when waking the device from an open app. ([**Issue #343002680**](https://issuetracker.google.com/issues/343002680))*
- *Equalizer frequency adjustment bars are cut off at the top of the screen. ([**Issue #342124654**](https://issuetracker.google.com/issues/342124654), [**Issue #358742436**](https://issuetracker.google.com/issues/358742436))*
- *Force stop button in app settings fails to terminate running applications. ([**Issue #337240745**](https://issuetracker.google.com/issues/337240745))*
- *Colored icons flicker when navigating back to the Accessibility settings page. ([**Issue #354424795**](https://issuetracker.google.com/issues/354424795))*
- *Apps fail to launch new activities when opened with an active Picture-in-Picture window. ([**Issue #479561839**](https://issuetracker.google.com/issues/479561839))*
- *Inconsistent spacing between status bar icons. ([**Issue #450097709**](https://issuetracker.google.com/issues/450097709))*
- *Screen recording callback incorrectly reports active recording state after stopping screen share from floating controls. ([**Issue #442801639**](https://issuetracker.google.com/issues/442801639))*
- *UI buttons render as blank white squares without icons in dark mode. ([**Issue #470561031**](https://issuetracker.google.com/issues/470561031))*
- *Grouped notification icons and titles appear grayed out. ([**Issue #489219424**](https://issuetracker.google.com/issues/489219424), [**Issue #516800663**](https://issuetracker.google.com/issues/516800663), [**Issue #548675068**](https://issuetracker.google.com/issues/548675068), [**Issue #568096206**](https://issuetracker.google.com/issues/568096206))*
- *Persistent UI message cannot be dismissed. ([**Issue #497831984**](https://issuetracker.google.com/issues/497831984), [**Issue #517093542**](https://issuetracker.google.com/issues/517093542))*
- *Bubbles get stuck in a miniaturized state at the bottom of the screen when swiped to dismiss. ([**Issue #504704002**](https://issuetracker.google.com/issues/504704002), [**Issue #517621552**](https://issuetracker.google.com/issues/517621552))*
- *Navigation bar animation glitches when swiping up to the recent apps screen. ([**Issue #552037549**](https://issuetracker.google.com/issues/552037549))*
- *Mobile Data Quick Settings icon renders at an incorrect size with persistent visual artifacts. ([**Issue #508083737**](https://issuetracker.google.com/issues/508083737), [**Issue #508904751**](https://issuetracker.google.com/issues/508904751), [**Issue #504868272**](https://issuetracker.google.com/issues/504868272), [**Issue #527517148**](https://issuetracker.google.com/issues/527517148), [**Issue #544886523**](https://issuetracker.google.com/issues/544886523), [**Issue #550178753**](https://issuetracker.google.com/issues/550178753), [**Issue #567904796**](https://issuetracker.google.com/issues/567904796), [**Issue #571714475**](https://issuetracker.google.com/issues/571714475))*
- *Display rendering issue when adjusting the font size slider in Settings. ([**Issue #554687371**](https://issuetracker.google.com/issues/554687371))*
- *Image action icons missing from the Recent Apps screen. ([**Issue #570996132**](https://issuetracker.google.com/issues/570996132))*
- *SettingsDumpService persists and consumes excessive memory after opening SIM settings. ([**Issue #567819031**](https://issuetracker.google.com/issues/567819031))*
- *Device crashes intermittently on the lock screen or shortly after startup. ([**Issue #569613685**](https://issuetracker.google.com/issues/569613685))*
- *Apps crash when BluetoothLeScanner.stopScan() is called with a null callback. ([**Issue #571626896**](https://issuetracker.google.com/issues/571626896))*
- *WPA-Enterprise Wi-Fi connections fail when authenticating with PEAP. ([**Issue #572438311**](https://issuetracker.google.com/issues/572438311), [**Issue #569431116**](https://issuetracker.google.com/issues/569431116), [**Issue #565959472**](https://issuetracker.google.com/issues/565959472))*

### Top Issues fixed in Beta 2 (October 2026)

Top issues fixed include:

- *Devices intermittently crash and reboot during normal use. ([**Issue #570031572**](https://issuetracker.google.com/issues/570031572), [**Issue #570031155**](https://issuetracker.google.com/issues/570031155), [**Issue #569529428**](https://issuetracker.google.com/issues/569529428), [**Issue #569222433**](https://issuetracker.google.com/issues/569222433), [**Issue #570414567**](https://issuetracker.google.com/issues/570414567), [**Issue #570725957**](https://issuetracker.google.com/issues/570725957), [**Issue #569237164**](https://issuetracker.google.com/issues/569237164), [**Issue #572493638**](https://issuetracker.google.com/issues/572493638))*
- *Internet Quick Settings tile displays persistent text when mobile data is active without Wi-Fi. ([**Issue #354469154**](https://issuetracker.google.com/issues/354469154), [**Issue #367059437**](https://issuetracker.google.com/issues/367059437))*
- *Media output dialog ignores the monochrome system theme when external audio devices are connected. ([**Issue #476304142**](https://issuetracker.google.com/issues/476304142))*
- *Pin icon glitches position next to pinned apps in the share sheet. ([**Issue #476234992**](https://issuetracker.google.com/issues/476234992))*
- *Internal PublishedApi declarations trigger unexpected API lint and source compatibility check errors. ([**Issue #562178518**](https://issuetracker.google.com/issues/562178518))*
- *Device unexpectedly shuts down during WhatsApp video calls. ([**Issue #554451749**](https://issuetracker.google.com/issues/554451749), [**Issue #559966303**](https://issuetracker.google.com/issues/559966303))*
- *Lock screen in-progress notifications overlap with other UI elements and cause stuttering panel animations. ([**Issue #547371609**](https://issuetracker.google.com/issues/547371609), [**Issue #548539836**](https://issuetracker.google.com/issues/548539836), [**Issue #562186670**](https://issuetracker.google.com/issues/562186670))*
- *Cellular data, MMS, and hotspot services fail to connect on Dish Network. ([**Issue #537736046**](https://issuetracker.google.com/issues/537736046))*
- *Screen recording freezes and stops capturing frames after screen rotation. ([**Issue #541325203**](https://issuetracker.google.com/issues/541325203))*
- *System UI, fonts, and apps render at an abnormally small scale regardless of configured display size settings. ([**Issue #563321433**](https://issuetracker.google.com/issues/563321433))*
- *Display turns black and becomes unresponsive after ending a phone call. ([**Issue #564953545**](https://issuetracker.google.com/issues/564953545))*
- *Terminal app fails to launch the Linux development environment virtual machine after installation. ([**Issue #551657934**](https://issuetracker.google.com/issues/551657934))*
- *Wi-Fi Aware fails to establish subsequent data paths with a no interfaces available error after releasing an accept-any responder network request during connection confirmation. ([**Issue #550726291**](https://issuetracker.google.com/issues/550726291))*
- *Paired watch continues to ring after an incoming call is answered on the phone. ([**Issue #564594780**](https://issuetracker.google.com/issues/564594780))*
- *Airbnb app fails to connect when attempting to send messages. ([**Issue #563024453**](https://issuetracker.google.com/issues/563024453))*
- *Quick Settings Bluetooth subtitle is misaligned to the right. ([**Issue #559417120**](https://issuetracker.google.com/issues/559417120))*
- *App drawer unexpectedly closes when switching keyboard language. ([**Issue #558774933**](https://issuetracker.google.com/issues/558774933), [**Issue #540389222**](https://issuetracker.google.com/issues/540389222), [**Issue #533125590**](https://issuetracker.google.com/issues/533125590))*
- *Bluetooth pairing fails due to a connection timeout when attempting to pair with a device. ([**Issue #563675080**](https://issuetracker.google.com/issues/563675080))*
- *VoLTE, VoNR, and Wi-Fi calling are unavailable on the IT\&E network. ([**Issue #556432987**](https://issuetracker.google.com/issues/556432987))*
- *High idle battery drain caused by motion sensors remaining active after using Face Unlock or the camera. ([**Issue #568078965**](https://issuetracker.google.com/issues/568078965))*
- *Wi-Fi Calling unavailable on the OXIO network. ([**Issue #563089593**](https://issuetracker.google.com/issues/563089593))*

### Top Issues fixed in Beta 1 (October 2026)

Top issues fixed include:

- *Audio output device cannot be switched while playing audio from apps without active media controls. ([**Issue #259180936**](https://issuetracker.google.com/issues/259180936))*
- *Apps crash when attempting to start a foreground service from a Quick Settings tile. ([**Issue #299506164**](https://issuetracker.google.com/issues/299506164))*
- *Application icons in the app menu display with excessive spacing. ([**Issue #316288379**](https://issuetracker.google.com/issues/316288379), [**Issue #300758716**](https://issuetracker.google.com/issues/300758716))*
- *App previews fail to display in the recent apps screen. ([**Issue #515091621**](https://issuetracker.google.com/issues/515091621))*
- *NFC service crashes with DeadObjectException and stops detecting tags after the initial scan on Android 16. ([**Issue #456078994**](https://issuetracker.google.com/issues/456078994))*
- *Device freezes and becomes unresponsive when unlocking with the fingerprint sensor. ([**Issue #490719716**](https://issuetracker.google.com/issues/490719716), [**Issue #514867650**](https://issuetracker.google.com/issues/514867650), [**Issue #523022829**](https://issuetracker.google.com/issues/523022829))*
- *Device crashes when selecting the require eyes to be open option in Face Unlock settings. ([**Issue #466618368**](https://issuetracker.google.com/issues/466618368), [**Issue #522677686**](https://issuetracker.google.com/issues/522677686))*
- *MediaPlayer crashes when handling non-ASCII audio attribute tags. ([**Issue #552043106**](https://issuetracker.google.com/issues/552043106))*
- *Applications freeze and trigger an Application Not Responding (ANR) error when launched. ([**Issue #484969809**](https://issuetracker.google.com/issues/484969809), [**Issue #475406236**](https://issuetracker.google.com/issues/475406236))*
- *Camera feed is rotated 90 degrees when using video calling apps on an external display in desktop mode. ([**Issue #432390710**](https://issuetracker.google.com/issues/432390710))*
- *User interface issues when navigating back to the home screen from an app. ([**Issue #566639975**](https://issuetracker.google.com/issues/566639975))*
- *Unexpected dot displayed on the Mobile Data icon in Quick Settings. ([**Issue #551150806**](https://issuetracker.google.com/issues/551150806))*
- *Front camera fails to function while screen recording is active. ([**Issue #523313834**](https://issuetracker.google.com/issues/523313834))*
- *Calling apps crash with ForegroundServiceStartNotAllowedException when handling calls immediately after device reboot. ([**Issue #409069722**](https://issuetracker.google.com/issues/409069722))*
- *eSIM profile cannot be enabled and silently reverts to off in Settings. ([**Issue #541436675**](https://issuetracker.google.com/issues/541436675))*
- *Excessive battery drain during idle when Flip to Shh is enabled. ([**Issue #560036427**](https://issuetracker.google.com/issues/560036427))*
- *Settings app crashes when opening battery settings. ([**Issue #554603197**](https://issuetracker.google.com/issues/554603197))*
- *Audio playback stops on active LHDC v5 Bluetooth devices when a second connected device disconnects. ([**Issue #554992287**](https://issuetracker.google.com/issues/554992287))*
- *com.android.phone crash loop and complete loss of cellular service when the modem reports unexpected SIM slot indices. ([**Issue #554049220**](https://issuetracker.google.com/issues/554049220))*
- *Wi-Fi fails to automatically reconnect during background wakes when hardware PNO scans fail or are unsupported. ([**Issue #551970385**](https://issuetracker.google.com/issues/551970385))*