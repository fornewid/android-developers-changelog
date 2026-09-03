---
title: https://developer.android.com/about/versions/17/qpr2/release-notes
url: https://developer.android.com/about/versions/17/qpr2/release-notes
source: md.txt
---

### Beta 4

|---|---|
| **Release date** | August 28, 2026 |
| **Builds** | CP41.260814.003.A2 CP41.260814.003.B1 CP41.260814.003.C2 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.28.33 |

### Beta 3

|---|---|
| **Release date** | August 14, 2026 |
| **Builds** | CP41.260731.005.A2 CP41.260731.005.B1 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-08-05 |
| **Google Play services** | 26.26.34 |

### Beta 2

|---|---|
| **Release date** | August 3, 2026 |
| **Builds** | CP41.260717.006 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-07-05 |
| **Google Play services** | 26.24.35 |

### Beta 1

|---|---|
| **Release date** | July 20, 2026 |
| **Builds** | CP41.260701.005 |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-07-05 |
| **Google Play services** | 26.23.34 |

### Android 17 QPR 2 Beta 4 (August 2026)

Building on the [initial release of Android 17](https://developer.android.com/about/versions/17), we continue to
update the platform with fixes and improvements that are then rolled out to
supported devices. These releases happen on a quarterly cadence through
*Quarterly Platform Releases* (QPRs), which are delivered both to AOSP and to
Google Pixel devices as part of *Feature Drops*.

Although these updates don't include app-impacting API changes, we provide
images of the latest QPR beta builds so you can test your app with these builds
as needed (for example, if there are upcoming features that might impact the
user experience of your app).

Android 17 QPR2 includes a minor SDK release. This incremental update has no
planned behavior changes, minimizing the need for compatibility testing.
You can the current SDK changes in the
[API diff report](https://developer.android.com/sdk/api_diff/37.2/changes).

#### Hardening against call forwarding fraud

Android 17 QPR2 introduces new security restrictions on programmatic call
forwarding to protect users from fraud. The system now parses and selectively
restricts call-forwarding USSD codes (such as `*21#`) executed using the
[`TelephonyManager.sendUssdRequest()` API](https://developer.android.com/reference/android/telephony/TelephonyManager#sendUssdRequest(java.lang.String,%20android.telephony.TelephonyManager.UssdResponseCallback,%20android.os.Handler)).

- **API Restriction:** The `sendUssdRequest()` API is no longer accessible for call-forwarding codes using only the `CALL_PHONE` permission. Standard apps attempting to execute these codes in the background will be blocked and receive a `USSD_ERROR_NOT_ALLOWED` callback.
- **System Confirmation:** To combat social engineering scams, users manually dialing call-forwarding codes in the system dialer will now see a new OS-level confirmation dialog before the command is executed.
- **Non-Call Forwarding USSD:** Non-call forwarding enabling USSD requests (such as mobile money transfers and account checks) are unaffected by this change.
- **Mitigation:** If your app is affected, verify that it handles the `USSD_ERROR_NOT_ALLOWED` failure callback gracefully. For apps requiring call-forwarding setup that don't qualify for an exempted role, migrate your flow to use the `ACTION_DIAL` intent to pre-fill the dialer, allowing the user to manually confirm the action.

### Top Issues fixed in Beta 4 (August 2026)

- *Enabling the "render apps below the cutout area" developer setting caused a transparent status bar on the launcher after exiting fullscreen video playback. ([**Issue #295747911**](https://issuetracker.google.com/issues/295747911))*
- *A thermal management issue that caused devices to overheat and unexpectedly reboot during use. ([**Issue #437116407**](https://issuetracker.google.com/issues/437116407))*
- *An issue preventing screen mirroring to external USB-C XR glasses. ([**Issue #439269938**](https://issuetracker.google.com/issues/439269938))*
- *Gesture navigation became unresponsive when rendering apps below the display cutout. ([**Issue #441378954**](https://issuetracker.google.com/issues/441378954))*
- *The 80% battery limit optimization caused excessive charge times during the final 2% threshold. ([**Issue #477009501**](https://issuetracker.google.com/issues/477009501), [**Issue #476803337**](https://issuetracker.google.com/issues/476803337))*
- *A launcher UI issue where searching for apps in the app drawer failed to process text input. ([**Issue #505157934**](https://issuetracker.google.com/issues/505157934), [**Issue #527921034**](https://issuetracker.google.com/issues/527921034), [**Issue #530531588**](https://issuetracker.google.com/issues/530531588), [**Issue #537704656**](https://issuetracker.google.com/issues/537704656))*
- *Invoking the power menu via hardware buttons caused a missing background blur effect behind the navigation bar. ([**Issue #537202501**](https://issuetracker.google.com/issues/537202501))*
- *An issue where phone call audio defaulted to the phone speaker instead of connected Bluetooth devices. ([**Issue #537908014**](https://issuetracker.google.com/issues/537908014), [**Issue #541501134**](https://issuetracker.google.com/issues/541501134), [**Issue #541772860**](https://issuetracker.google.com/issues/541772860), [**Issue #545047074**](https://issuetracker.google.com/issues/545047074))*
- *A Recents app switcher rendering bug where the first task card could intermittently freeze and visually clip behind other apps during horizontal scrolling. ([**Issue #530484511**](https://issuetracker.google.com/issues/530484511), [**Issue #505564040**](https://issuetracker.google.com/issues/505564040), [**Issue #545574713**](https://issuetracker.google.com/issues/545574713), [**Issue #551022006**](https://issuetracker.google.com/issues/551022006))*
- *An audio service resource lock triggered during screen recording that prevented microphone usage across apps and input methods like Gboard and Gemini until a device restart. ([**Issue #538229807**](https://issuetracker.google.com/issues/538229807))*
- *A System UI visual inconsistency where turning off the screen from the home screen triggered a plain fade instead of the power-button screen-off animation. ([**Issue #541261786**](https://issuetracker.google.com/issues/541261786))*
- *A low-contrast rendering issue in dark mode where the connected Wi-Fi settings cog icon was barely visible. ([**Issue #536320341**](https://issuetracker.google.com/issues/536320341))*
- *Enabling 3D mode on connected smart glasses resulted in a blank screen. ([**Issue #536628506**](https://issuetracker.google.com/issues/536628506))*
- *A User Interface issue that prevented the notification bar from being pulled all the way down. ([**Issue #539244095**](https://issuetracker.google.com/issues/539244095), [**Issue #547801203**](https://issuetracker.google.com/issues/547801203), [**Issue #547017781**](https://issuetracker.google.com/issues/547017781), [**Issue #546896889**](https://issuetracker.google.com/issues/546896889), [**Issue #547163658**](https://issuetracker.google.com/issues/547163658), [**Issue #547281675**](https://issuetracker.google.com/issues/547281675))*
- *An issue where WebGL applications could freeze or crash the browser process when combining shadow maps with vertex color attributes by resolving an invalid memory read in the PowerVR GPU driver's texture state processing. ([**Issue #541322087**](https://issuetracker.google.com/issues/541322087))*
- *Low-light Face Unlock failures bypassed Fingerprint Unlock and forced PIN entry. ([**Issue #547597971**](https://issuetracker.google.com/issues/547597971), [**Issue #545329611**](https://issuetracker.google.com/issues/545329611), [**Issue #541723970**](https://issuetracker.google.com/issues/541723970))*

### Top Issues fixed in Beta 3 (August 2026)

- *Opening the notification shade and Quick Settings menu caused visual corruption and an unexpected device restart. ([**Issue #535249652**](https://issuetracker.google.com/issues/535249652), [**Issue #543124160**](https://issuetracker.google.com/issues/543124160))*
- *The Device Health and Support tool erroneously displayed false battery capacity degradation warnings to users. ([**Issue #535421490**](https://issuetracker.google.com/issues/535421490), [**Issue #538943170**](https://issuetracker.google.com/issues/538943170), [**Issue #535504630**](https://issuetracker.google.com/issues/535504630))*

### Top Issues fixed in Beta 1 (July 2026)

- *Bluetooth re-pairing fails silently following a remote bond loss. ([**Issue #412524057**](https://issuetracker.google.com/issues/412524057))*
- *Media player controls briefly flashed on the lock screen upon waking the device despite the app's notifications being disabled. ([**Issue #484607701**](https://issuetracker.google.com/issues/484607701))*
- *A system crash causing Pixel devices to unexpectedly reboot when invoking Gemini. ([**Issue #505750489**](https://issuetracker.google.com/issues/505750489))*
- *Initiating a drag-and-drop gesture with multiple fingers caused the source application to stop receiving subsequent touch events. ([**Issue #516836306**](https://issuetracker.google.com/issues/516836306))*
- *Notifications randomly became invisible in the notification shade until a system restart. ([**Issue #526139207**](https://issuetracker.google.com/issues/526139207), [**Issue #522657034**](https://issuetracker.google.com/issues/522657034))*
- *ML-DSA key generation fails with an exception when using the "NONE" string digest instead of the class constant. ([**Issue #525612735**](https://issuetracker.google.com/issues/525612735))*
- *An issue in AccessibilityNodeInfo.toString() where window bounds were incorrectly logged using screen bounds, which caused misleading accessibility debugging data. ([**Issue #520428442**](https://issuetracker.google.com/issues/520428442))*
- *Window-level UI blur effects failed to render and the "Allow window-level blurs" developer toggle reset after rebooting. ([**Issue #527376569**](https://issuetracker.google.com/issues/527376569))*