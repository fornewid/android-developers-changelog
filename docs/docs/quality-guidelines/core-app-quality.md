---
title: https://developer.android.com/docs/quality-guidelines/core-app-quality
url: https://developer.android.com/docs/quality-guidelines/core-app-quality
source: md.txt
---

To provide a solid foundation for a quality app, follow the core app quality
guidelines.

The guidelines define the minimum quality that all apps should meet.
Adaptive app quality

Android apps run on a wide variety of devices---everything from compact phones to tablets, foldables, desktops, connected displays, car infotainment systems, TV, and XR. Windowing modes like split‑screen and desktop windowing enable apps to run in resizable portions of a screen.

Follow the [adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) guidelines---in conjunction with the core app quality guidelines---to:

- Create apps optimized for all form factors and display sizes
- Get your apps ranked higher in Google Play listings and search
- Acquire more users and increase user retention

## Guidelines

The following core guidelines help you build a basic, high‑quality app.

### User experience

Standard Android visual design and interaction patterns provide a consistent and
intuitive user experience.

Use [Material design components](https://m3.material.io/components) to create your app's user interface in place
of Android platform components where possible. Material Design provides a modern
Android look and feel along with UI consistency across Android versions.

#### Usability

| ID | Tests | Description |
|---|---|---|
| Consistent_UX | [T-Consistent_UX](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Consistent_UX), [T-SD_Card](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-SD_Card) | App provides a consistent user experience for all app use cases on all form factors. |
| App_Switcher | [T-App_Switcher](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-App_Switcher), [T-SD_Card](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-SD_Card) | App goes into the background when focus switches to another app. App returns to the foreground when reactivated from the **Recents** app switcher. |
| Sleep_Resume | [T-Sleep_Resume](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Sleep_Resume), [T-SD_Card](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-SD_Card) | When the app is the foreground app, it pauses when the device goes to sleep and resumes when the device wakes up. |
| Lock_Resume | [T-Lock_Resume](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Lock_Resume), [T-SD_Card](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-SD_Card) | When the app is the foreground app, it pauses when the device is locked and resumes when the device is unlocked. |

#### User interface

| ID | Tests | Description |
|---|---|---|
| Display_State_Parity | [T-Orientation_Transitions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Orientation_Transitions) | Display orientations and fold states expose essentially the same features and actions and preserve functional parity. |
| Fullscreen_Display | [T-Orientation_Transitions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Orientation_Transitions) | App fills the app window in both orientations and is not letterboxed because of configuration changes, including device folding and unfolding. Minor letterboxing to compensate for small variations in screen geometry is acceptable. |
| Orientation_Transitions | [T-Orientation_Transitions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Orientation_Transitions) | App handles rapid transitions between display orientations and device folding and unfolding with no display rendering problems and without losing state. |

#### Visual quality

| ID | Tests | Description |
|---|---|---|
| Graphic_Quality | [T-Graphic_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Graphic_Quality) | App displays graphics, text, images, and other UI elements without noticeable distortion, blurring, or pixelation. - App uses [vector drawables](https://developer.android.com/guide/topics/graphics/vector-drawable-resources) where possible - App uses high-quality graphics for all targeted screen sizes and form factors - No aliasing at the edges of menus, buttons, and other UI elements |
| Line_Length | [T-Line_Length](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Line_Length) | App ensures readability of text and text blocks by limiting line length to 45-75 characters (including spaces) for each of the app's supported languages. |
| Theme_Support | [T-Theme_Support](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Theme_Support) | The app's content, and all web content accessed by the app, support both light and [dark themes](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme). |

#### Navigation

| ID | Tests | Description |
|---|---|---|
| Back_Button_Nav | [T-Back_Nav](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Back_Nav) | App supports standard [back button navigation](https://developer.android.com/design/patterns/navigation) and does not make use of any custom, onscreen back button prompts. |
| Back_Gesture_Nav | [T-Back_Nav](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Back_Nav) | App supports [gesture navigation](https://developer.android.com/training/gestures/gesturenav) for going back and going to the home screen. |
| State_Preservation | [T-State_Preservation](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-State_Preservation), [T-Back_Nav](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Back_Nav) | The app preserves user or app state when leaving the foreground and prevents accidental data loss due to back navigation and other state changes. When returning to the foreground, the app restores the preserved state and any pending stateful transactions. Examples include changes to editable fields, game progress, menus, videos, and other sections of the app. - When the app is resumed from the **Recents** app switcher, the app returns the user to the exact state in which the app was last used. - When the app is resumed after the device wakes from the sleep (locked) state, the app returns the user to the exact state in which the app was last used. - When the app is relaunched from **Home** or **All Apps**, it should do one of the following, depending on how much time has passed since the app was last used: - If the app was last used a short time ago (minutes), restore the app state as closely as possible to its previous state. - If more time has passed since the app was last used, try to restore the app as closely as possible to its previous state or start the app from its home screen or some other default state. |

#### Notifications

| ID | Tests | Description |
|---|---|---|
| Notification_Quality | [T-Notification_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Notification_Quality) | [Notifications](https://developer.android.com/design/ui/mobile/guides/home-screen/notifications) provide relevant information related to your app. - Don't use notifications for cross-promotion or advertising of another product, as this is strictly prohibited by the Play Store. - [Notification channels](https://developer.android.com/training/notify-user/channels) are defined according to best practices, rather than serving all notifications from one channel. - Select [the correct notification priority](https://android-developers.googleblog.com/2018/12/notifications-from-twitter-app.html). - Stack multiple notifications into [a single notification group](https://developer.android.com/training/notify-user/group) when possible. - Set [timeouts](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.Builder#setTimeoutAfter(long)) for notifications where appropriate. - Notifications are persistent only if related to ongoing events, such as music playback or a phone call. For more information, see the [Functionality section](https://developer.android.com/docs/quality-guidelines/core-app-quality#fn). |
| Conversation_Quality | [T-Notification_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Notification_Quality) | For messaging apps, social apps and conversations: - Use the [`MessagingStyle`](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.MessagingStyle) notifications for conversations. - Support the [direct reply action](https://developer.android.com/training/notify-user/build-notification#reply-action). - Support [conversation shortcuts](https://developer.android.com/guide/topics/ui/conversations#shortcuts), and implement best practices for getting the [best direct share ranking](https://developer.android.com/training/sharing/direct-share-targets#get-best-ranking). - Support [bubbles](https://developer.android.com/guide/topics/ui/bubbles). |

#### Accessibility

| ID | Tests | Description |
|---|---|---|
| Touch_Target_Size | [T-Touch_Target_Size](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Touch_Target_Size) | Touch targets are least 48 dp. See the Material Design [Layout and typography](https://material.io/design/usability/accessibility.html#layout-and-typography) guidelines. |
| Visual_Contrast | [T-Visual_Contrast](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Visual_Contrast) | App text and foreground content maintain the following contrast ratios with the app background: - 3:1 for large text and graphics - 4.5:1 for small text (less than 18 pt or less than 14 pt if text is bold) Learn more about [color and contrast](https://material.io/design/usability/accessibility.html#color-and-contrast). |
| Content_Description | [T-Content_Description](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Content_Description) | [Describe each UI element](https://developer.android.com/guide/topics/ui/accessibility/apps#describe-ui-element), except for `TextView`, using `contentDescription`. |

### Functionality

Your app should implement the following functional behavior.

#### Audio

| ID | Tests | Description |
|---|---|---|
| Audio_Playback_Start | [T-Audio_Playback_Start](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Audio_Playback_Start) | When the user initiates audio playback, the app should do one of the following within one second: - Start playing the audio - Provide a visual indicator that the audio data is being prepared |
| Audio_Focus_Request | [T-Audio_Focus_Request](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Audio_Focus_Request) | App should request [audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus) when audio starts playing and abandon audio focus when playback stops. |
| Audio_Focus_Change | [T-Audio_Focus_Change](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Audio_Focus_Change) | App should [handle other apps' requests for audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus#audio-focus-change). For example, an app might reduce playback volume when another app plays speech. |
| Audio_Playback_Background | [T-Audio_Playback_Background](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Audio_Playback_Background) | App should support [background playback](https://developer.android.com/media/platform/mediaplayer/background). App must use a foreground service to prevent the system from killing the app process once the app is no longer visible. The app must also display a persistent, non‑dismissible notification in the status bar or on the lock screen to inform the user that the app is running. Users should be able to control playback using the notification or lock screen controls or the controls on a connected accessory. |
| Audio_Notification_Style | [T-Audio_Notification_Style](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Audio_Notification_Style) | When the app plays audio in the background, app must create a [notification styled with `MediaStyle`](https://android-developers.googleblog.com/2020/08/playing-nicely-with-media-controls.html). |
| Audio_Playback_Resume | [T-Audio_Playback_Resume](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Audio_Playback_Resume) | If the app is in the background and audio is paused, audio resumes when the app returns to the foreground, or the app must indicate to the user that playback is in a paused state. |

#### Video

| ID | Tests | Description |
|---|---|---|
| Video_PiP | [T-Video_PiP](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Video_PiP) | If the app plays video, app should support [picture-in-picture](https://developer.android.com/guide/topics/ui/picture-in-picture) playback. |
| Video_Encoding | [T-Video_Encoding](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Video_Encoding) | If the app encodes video, app should do so using the [HEVC video compression standard](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding). |
| Video_Playback_Background | [T-Video_Playback_Background](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Video_Playback_Background) | App supports background playback of video when the app is not the topmost app, including when the app window is: - Minimized - Behind other windows or system UI (for example, notification shade or home/lock screen) - Off the visible desktop screen |

#### Sharing

| ID | Tests | Description |
|---|---|---|
| System_Sharesheet | [T-System_Sharesheet](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-System_Sharesheet) | App should use the [Android Sharesheet](https://developer.android.com/training/sharing/send) when sharing content. App can suggest targets that are unavailable to custom solutions. |

#### Background services

| ID | Tests | Description |
|---|---|---|
| Background_Service_Optimization | [T-Background_Service_Optimization](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Background_Service_Optimization) | App avoids running unnecessarily long services in the background to ensure the smooth running of the user's device. **Note:** The system applies various [restrictions on background services](https://developer.android.com/about/versions/oreo/background#services). The following are poor uses of background services: - Maintaining a network connection for notifications - Maintaining a Bluetooth connection - Keeping the GPS powered on For more information, see [Background tasks overview](https://developer.android.com/guide/background#categories_of_background_tasks). |

### Performance and stability

Your app should provide optimal performance, stability, compatibility, and responsiveness.

#### Performance

| ID | Tests | Description |
|---|---|---|
| App_Startup_Time | [T-App_Startup_Time](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-App_Startup_Time) | [App loads quickly](https://medium.com/androiddevelopers/testing-app-startup-performance-36169c27ee55) or provides onscreen feedback to the user (a progress indicator or similar cue) if the app takes longer than two seconds to load. |
| Rendering_Performance | [T-Rendering_Performance](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Rendering_Performance) | App renders frames every 16 (or fewer) milliseconds to display at least 60 frames per second. For help with rendering issues, see [Slow rendering](https://developer.android.com/topic/performance/vitals/render). |
| StrictMode_Compliance | [T-StrictMode_Compliance](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-StrictMode_Compliance) | With [`StrictMode`](https://developer.android.com/reference/kotlin/android/os/StrictMode) enabled (see the [StrictMode](https://developer.android.com/docs/quality-guidelines/core-app-quality#strictmode) testing section), no red flashes (performance warnings from `StrictMode`) are visible when testing the app. |

#### Stability

| ID | Tests | Description |
|---|---|---|
| Stability_ANR | [T-Stability_ANR](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Stability_ANR) | App does not [crash](https://developer.android.com/topic/performance/vitals/crash) or block the UI thread causing[ANR (Android Not Responding)](https://developer.android.com/topic/performance/vitals/anr) errors. Use the Google Play [pre-launch report](https://support.google.com/googleplay/android-developer/answer/9842757) to identify potential stability issues. After deployment, monitor the [Android Vitals](https://developer.android.com/topic/performance/vitals) page in the Google Play console. |

#### SDK

| ID | Tests | Description |
|---|---|---|
| Android_Platform_Compatibility | [T-Android_Platform_Compatibility](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Android_Platform_Compatibility) | App runs on the latest public version of the Android platform without crashing or severely impacting core functionality. |
| Target_SDK_Version | [T-Target_SDK_Version](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Target_SDK_Version) | App targets the [latest Android SDK](https://developer.android.com/distribute/best-practices/develop/target-sdk) needed to align with Google Play requirements by setting the `targetSdk` value in the app's module `build.gradle` file. |
| Compile_SDK_Version | [T-Target_SDK_Version](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Target_SDK_Version) | App is built with the latest Android SDK by setting the `compileSdk` value in the app's module `build.gradle` file. |
| SDK_Maintenance | [T-SDK_Maintenance](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-SDK_Maintenance), [T-Non_SDK_Interfaces](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Non_SDK_Interfaces) | Any Google or third-party SDKs used are up to date. Any improvements to these SDKs related to stability, compatibility, or security should be available to users in a timely manner. For Google SDKs, use SDKs powered by [Google Play services](https://developers.google.com/android) when available. These SDKs are backward compatible, receive automatic updates, reduce your app package size, and make efficient use of on-device resources. > [!NOTE] > You are accountable for the entire app codebase, inclusive of any third-party SDKs used. |
| Non_SDK_Interfaces | [T-Non_SDK_Interfaces](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Non_SDK_Interfaces) | App does not use [non-SDK interfaces](https://developer.android.com/distribute/best-practices/develop/restrictions-non-sdk-interfaces). |
| Production_Build_Quality | [T-Production_Build_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Production_Build_Quality) | No debug libraries are included in the production app. Debug libraries included in the app can cause performance as well as security issues. |

#### Battery

| ID | Tests | Description |
|---|---|---|
| Power_Management | [T-Power_Management](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Power_Management) | App properly supports power management features [Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby). Apps can request a power maintenance exemption. See [Support for other use cases](https://developer.android.com/training/monitoring-device-state/doze-standby#support_for_other_use_cases) in *Optimize for Doze and App Standby*. |

### Privacy and security

App handles user data and personal information safely and provides appropriate levels of permission.

Applications published on the Google Play Store must also follow the Google Play
[User Data](https://play.google.com/about/privacy-security/user-data) policies to protect user privacy.

#### Permissions

| ID | Tests | Description |
|---|---|---|
| Minimize_Permissions | [T-Minimize_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Minimize_Permissions) | App requests only the absolute minimum permissions needed to support the current use case. For some permissions, such as location, app uses a *coarse* specification in place of *fine* if possible. See [Minimize your permission requests](https://developer.android.com/training/permissions/evaluating). |
| Sensitive_Permissions | [T-Sensitive_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Sensitive_Permissions) | App requests permission to access sensitive data (such as [SMS or Call Log permission groups](https://support.google.com/googleplay/android-developer/answer/10208820) or [location](https://developer.android.com/training/permissions/requesting#location)) or services that cost money (such as Dialer or SMS) only when directly related to the app's core use cases. Implications related to these permissions must be prominently disclosed to the user. Depending on how your app uses the permissions, an [alternative way](https://developer.android.com/training/permissions/evaluating) of fulfilling your app's use case might be possible without relying on access to sensitive information. For example, instead of requesting permissions related to a user's contacts, use an [implicit intent](https://developer.android.com/guide/components/intents-common#Contacts) to request access. |
| Runtime_Permissions | [T-Runtime_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Runtime_Permissions) | App requests runtime permissions when the functionality is requested, rather than during app startup. |
| Permission_Rationale | [T-Permission_Rationale](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Permission_Rationale) | App clearly explains [why permissions are needed](https://developer.android.com/training/permissions/requesting#explain). |
| Graceful_Degradation | [T-Graceful_Degradation](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Graceful_Degradation) | App [gracefully degrades](https://developer.android.com/training/permissions/requesting#handle-denial) when users deny or revoke a permission. App shouldn't prevent user access altogether. |

#### Data and files

| ID | Tests | Description |
|---|---|---|
| Sensitive_Data_Storage | [T-Sensitive_Data_Storage](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Sensitive_Data_Storage), [T-Sensitive_Data_Handling](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Sensitive_Data_Handling) | All sensitive data is [stored in the app's internal storage](https://developer.android.com/topic/security/best-practices#internal-storage). |
| Sensitive_Data_Logging | [T-Sensitive_Data_Logging](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Sensitive_Data_Logging) | [No personal or sensitive user data](https://developer.android.com/privacy-and-security/security-tips#user-data) is logged to the system log or an app-specific log. |
| Hardware_IDs | [T-Hardware_IDs](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Hardware_IDs) | App does not use any [non-resettable hardware IDs](https://developer.android.com/training/articles/user-data-ids), such as the IMEI, for identification purposes. |

#### Identity

| ID | Tests | Description |
|---|---|---|
| Autofill_Hints | [T-Autofill_Hints](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Autofill_Hints) | App provides [hints to autofill](https://developer.android.com/guide/topics/text/autofill-optimize#hints) account credentials and other sensitive information, such as credit card info, physical address, and phone number. |
| Credential_Manager | [T-Credential_Manager](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Credential_Manager) | App integrates [Credential Manager for Android](https://developer.android.com/training/sign-in/passkeys) for a seamless sign-in experience that unifies support for passkeys, federated identity, and passwords. |
| Biometric_Authentication | [T-Biometric_Authentication](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Biometric_Authentication) | App supports [biometric authentication](https://developer.android.com/training/sign-in/biometric-auth) to protect financial transactions or sensitive information, such as important user documents. |

#### App components

| ID | Tests | Description |
|---|---|---|
| Component_Export | [T-Component_Export](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Component_Export) | App sets the `android:exported` attribute explicitly for all [activities](https://developer.android.com/guide/topics/manifest/activity-element#exported), [services](https://developer.android.com/guide/topics/manifest/service-element#exported), [broadcast receivers,](https://developer.android.com/guide/topics/manifest/receiver-element#exported) and especially [content providers](https://developer.android.com/guide/topics/manifest/provider-element#exported). Only application components that *share data with other apps* , or components that *should be invoked by other apps* , are [exported](https://developer.android.com/guide/topics/manifest/service-element#exported). |
| Component_Permissions | [T-Component_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Component_Permissions) | All intents and broadcasts follow best practices: - [Use explicit intents](https://developer.android.com/guide/components/intents-filters#Types) if the destination application is well defined. - [Use intents to defer permissions to a different app that already has the permission.](https://developer.android.com/topic/security/best-practices#permissions-intents) - [Share data securely across apps](https://developer.android.com/topic/security/best-practices#permissions-share-data). - Intents that contain a payload are [verified before use](https://developer.android.com/privacy-and-security/security-tips#input-validation). - If you need to pass an intent to another app, so that the receiving app can invoke and expect a callback in the calling app, don't include a nested intent in the extras. Use a [`PendingIntent`](https://developer.android.com/reference/kotlin/android/app/PendingIntent). - When setting up pending intents, explicitly set the [immutable flag](https://developer.android.com/reference/kotlin/android/app/PendingIntent#flag_immutable), where applicable. |
| Component_Protection | [T-Component_Protection](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Component_Protection) | All components that *share content between apps* use [`android:protectionLevel="signature"`](https://developer.android.com/guide/topics/manifest/permission-element#plevel) for [custom permissions](https://developer.android.com/guide/topics/permissions/defining). This includes [activities](https://developer.android.com/guide/topics/manifest/activity-element#prmsn), [services](https://developer.android.com/guide/topics/manifest/service-element#prmsn), [broadcast receivers](https://developer.android.com/guide/topics/manifest/receiver-element#prmsn), and especially [content providers](https://developer.android.com/guide/topics/manifest/provider-element#prmsn). Apps shouldn't rely on accessing a list of installed packages. |

#### Networking

| ID | Tests | Description |
|---|---|---|
| Network_Security_Traffic | [T-Network_Security_Traffic](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Network_Security_Traffic) | All network traffic is sent over [SSL](https://developer.android.com/training/articles/security-ssl). |
| Network_Security_Configuration | [T-Network_Security_Configuration](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Network_Security_Configuration) | App declares a [network security configuration](https://developer.android.com/training/articles/security-config). |
| Security_Provider_Initialization | [T-Security_Provider_Initialization](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Security_Provider_Initialization) | If the app uses Google Play services, the [security provider is initialized at application startup](https://developer.android.com/training/articles/security-gms-provider). |

#### WebViews

| ID | Tests | Description |
|---|---|---|
| WebView_Asset_Loader | [T-WebView_Asset_Loader](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-WebView_Asset_Loader), [T-WebView_Navigation](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-WebView_Navigation) | Don't use [`setAllowUniversalAccessFromFileURLs()`](https://developer.android.com/reference/kotlin/android/webkit/WebSettings#setallowuniversalaccessfromfileurls)for accessing local content. Instead, use [`WebViewAssetLoader`](https://developer.android.com/reference/kotlin/androidx/webkit/WebViewAssetLoader). |
| WebView_JavaScript | [T-WebView_JavaScript](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-WebView_JavaScript), [T-WebView_Navigation](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-WebView_Navigation) | [Web views](https://developer.android.com/privacy-and-security/security-tips#webview) don't use [`addJavaScriptInterface()`](https://developer.android.com/reference/kotlin/android/webkit/WebView#addjavascriptinterface) with untrusted content. On Android 6.0 (API level 23 and higher), use [HTML message channels](https://developer.android.com/privacy-and-security/security-best-practices#message-channels) instead. |

#### Execution

| ID | Tests | Description |
|---|---|---|
| App_Bundles | [T-App_Bundles](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-App_Bundles) | App does not [dynamically load](https://developer.android.com/privacy-and-security/security-tips#dynamic-code) code from outside the app's APK. Use [Android App Bundles](https://developer.android.com/guide/app-bundle), which include [Play Feature Delivery](https://developer.android.com/guide/app-bundle/play-feature-delivery) and [Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery). As of August 2021, the use of Android App Bundles is mandatory for all new apps in the Google Play Store. |

#### Cryptography

| ID | Tests | Description |
|---|---|---|
| Cryptographic_Algorithms | [T-Cryptographic_Algorithms](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Cryptographic_Algorithms) | App uses strong, platform-provided [cryptographic algorithms and a random number generator](https://developer.android.com/privacy-and-security/security-tips#cryptography). Also, the app does not implement custom algorithms. |

### Google Play

Enable your app to be published on Google Play.

#### Policies

| ID | Tests | Description |
|---|---|---|
| Play_Content_Policies | [T-Play_Content_Policies](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Content_Policies) | App strictly adheres to the terms of the [Google Play Developer Content Policy](https://play.google.com/about/developer-content-policy.html), does not offer inappropriate content, and does not use the intellectual property or brand of others. |
| Play_Content_Rating | [T-Play_Content_Policies](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Content_Policies) | App maturity level is set appropriately based on the [Content Rating Guidelines](https://support.google.com/googleplay/android-developer/bin/answer.py&answer=188189). |

#### App details page

| ID | Tests | Description |
|---|---|---|
| Play_Feature_Graphic | [T-Play_Feature_Graphic](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Feature_Graphic), [T-Play_Graphic_Assets](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Graphic_Assets) | App feature graphic follows the guidelines outlined in this [support article](https://support.google.com/googleplay/android-developer/answer/9866151?visit_id=637408759199927231-2278064029&rd=1#feature_graphic_requirements). Make sure that: - App listing includes a high-quality feature graphic - The feature graphic does not contain device images, screenshots, or small text that's illegible when scaled down and displayed on the smallest screen size that your app is targeting - The feature graphic does not resemble an advertisement |
| Play_Device_References | [T-Play_Graphic_Assets](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Graphic_Assets) | App screenshots and videos don't show or reference non-Android devices. |
| Play_Misleading_Content | [T-Play_Graphic_Assets](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Graphic_Assets) | App screenshots or videos don't represent the content and experience of your app in a misleading way. |

#### User support

| ID | Tests | Description |
|---|---|---|
| Play_User_Reviews | [T-Play_Content_Policies](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Play_Content_Policies) | Common user-reported bugs in the **Reviews** tab of the Google Play page are addressed if the bugs are reproducible and occur on many different devices. If a bug occurs on only a few devices, you should still address it if those devices are particularly popular or new. |

## Test environment

Set up a test environment as follows:

- **Emulator testing:** Android Emulator is a great way to test your app under
  different Android versions and screen resolutions. Set up [emulated devices](https://developer.android.com/tools/devices) (AVDs) to represent the most common form factors and
  hardware/software combinations for your target user base. Test a variety of
  form factors using the following emulators (at a minimum):

  - Foldables: 7.6" fold-in with outer display (this is listed under phones in the AVD Manager)
  - Tablet: Pixel C 9.94" (2,560px x 1,800px)
  - Mobile app notification testing: Pair a mobile device / emulator with Wear OS emulator: Wear OS Round 1.84"
- **Hardware devices:** Your test environment should include a small number of
  actual hardware devices that represent the key form factors and hardware/software combinations that are available to consumers. You don't
  need to test on *every* device that's on the market. Focus on a small number
  of representative devices, even using one or two devices per form factor.

- **Device test labs:** ; You can also use third party services, such as
  [Firebase Test Lab](https://firebase.google.com/docs/test-lab/android/overview), to test your app on a wide variety of devices.

- **Test with the latest Android version:** In addition to testing
  representative Android versions for your target user base, you should
  always test against the latest version of Android to ensure the
  [latest behavior changes](https://developer.android.com/about/versions/14/behavior-changes-14) don't negatively impact your app's user
  experience.

For further guidance on testing, including unit testing, integration testing,
and UI testing, see [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals).

### StrictMode

For performance testing, enable [`StrictMode`](https://developer.android.com/reference/kotlin/android/os/StrictMode) in your app. Use `StrictMode` to catch operations that could affect performance, network accesses, and file
reads and writes. Look for potentially problematic operations both on the main thread and on other threads.

Set up a per-thread monitoring policy using [`StrictMode.ThreadPolicy.Builder`](https://developer.android.com/reference/kotlin/android/os/StrictMode.ThreadPolicy.Builder) and enable all supported monitoring in the
`ThreadPolicy` using [`detectAll()`](https://developer.android.com/reference/kotlin/android/os/StrictMode.ThreadPolicy.Builder#detectall).

Enable **visual notification** of policy violations for the `ThreadPolicy` using
[`penaltyFlashScreen()`](https://developer.android.com/reference/kotlin/android/os/StrictMode.ThreadPolicy.Builder#penaltyflashscreen).

## Tests

The core app quality tests help you assess the fundamental quality of your app.
You can combine the tests or integrate groups of tests together in your test plan.

### User experience

Test for a consistent and intuitive user experience.

#### Usability

| ID | Feature | Description |
|---|---|---|
| T-Consistent_UX | [Consistent_UX](https://developer.android.com/docs/quality-guidelines/core-app-quality#Consistent_UX) | Navigate to all parts of the app---all screens, dialogs, settings, and all user flows. Do the following: - If the application allows for editing or content creation, game play, or media playback, make sure to test those flows. - While testing the app, introduce interruptions from other apps, such as receiving a notification or a phone call; and apply transient changes to device attributes, such as network connectivity, battery function, GPS availability, and system load. - Enter and test all in-app purchase flows |
| T-App_Switcher | [App_Switcher](https://developer.android.com/docs/quality-guidelines/core-app-quality#App_Switcher) | From each app screen, switch to another running app, and then return to the app under test using the **Recents** app switcher. |
| T-Sleep_Resume | [Sleep_Resume](https://developer.android.com/docs/quality-guidelines/core-app-quality#Sleep_Resume) | Press the power button to put the device to sleep, then press the power button again to wake the screen. |
| T-Lock_Resume | [Lock_Resume](https://developer.android.com/docs/quality-guidelines/core-app-quality#Lock_Resume) | Set up a screen lock on the device. Press the power button to put the device to sleep (which locks the device). Then, press the power button again to wake the screen and unlock the device. |

#### SD card

| ID | Feature | Description |
|---|---|---|
| T-SD_Card | [Consistent_UX](https://developer.android.com/docs/quality-guidelines/core-app-quality#Consistent_UX) | Perform [core functionality](https://developer.android.com/docs/quality-guidelines/core-app-quality#T-Consistent_UX) tests with the app installed on a [device's SD card](https://developer.android.com/guide/topics/data/install-location) (if the app supports this installation method). To move the app to an SD card, see the app **Settings**. |

#### User interface

| ID | Feature | Description |
|---|---|---|
| T-Orientation_Transitions | [Display_State_Parity](https://developer.android.com/docs/quality-guidelines/core-app-quality#Display_State_Parity), [Fullscreen_Display](https://developer.android.com/docs/quality-guidelines/core-app-quality#Fullscreen_Display), [Orientation_Transitions](https://developer.android.com/docs/quality-guidelines/core-app-quality#Orientation_Transitions) | From each app screen, rotate the device between landscape and portrait orientations and folded and unfolded states at least three times. Verify the app does the following: - Provides function parity in all display orientations and fold states - Fills the app window in all display orientations and fold states and is not letterboxed - Maintains state and has no rendering problems during rapid transitions between orientations and device folding and unfolding |

#### Visual quality

| ID | Feature | Description |
|---|---|---|
| T-Graphic_Quality | [Graphic_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#Graphic_Quality) | Use all features of your app. Verify that all visuals, including graphics, text, images, and other UI elements are free of distortion, blurring, or pixelation. |
| T-Line_Length | [Line_Length](https://developer.android.com/docs/quality-guidelines/core-app-quality#Line_Length) | Review all text blocks in the app. Verify that text and text block line length is limited to 45-75 characters (including spaces) for readability. Verify the following: - Composition is acceptable in all supported form factors - No cut-off letters or words - No improper word wraps within buttons or icons - Sufficient spacing between text and surrounding elements |
| T-Theme_Support | [Theme_Support](https://developer.android.com/docs/quality-guidelines/core-app-quality#Theme_Support) | Verify that all text is readable in light and dark themes. Verify that all visuals are clearly discernible and aesthetic in light and dark themes. |

#### Navigation

| ID | Feature | Description |
|---|---|---|
| T-Back_Nav | [Back_Button_Nav](https://developer.android.com/docs/quality-guidelines/core-app-quality#Back_Button_Nav), [Back_Gesture_Nav](https://developer.android.com/docs/quality-guidelines/core-app-quality#Back_Gesture_Nav) | Navigate to all parts of the app---all screens, dialogs, settings, and all user flows. From each app screen, press the **Back** button or use the back swipe gesture. The app should navigate to the previous or home screen. |
| T-State_Preservation | [State_Preservation](https://developer.android.com/docs/quality-guidelines/core-app-quality#State_Preservation) | From each app screen, press the device's **Home** key or swipe up in gesture navigation, then relaunch the app from the **All Apps** screen. |

#### Notifications

| ID | Feature | Description |
|---|---|---|
| T-Notification_Quality | [Notification_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#Notification_Quality), [Conversation_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#Conversation_Quality) | Trigger and observe in the notifications drawer all types of notifications that the app can display. Expand notifications where applicable (Android 4.1 and higher), and tap on all available actions. |

#### Accessibility

| ID | Feature | Description |
|---|---|---|
| T-Touch_Target_Size | [Touch_Target_Size](https://developer.android.com/docs/quality-guidelines/core-app-quality#Touch_Target_Size) | Verify that touch targets maintain a consistent, accessible size and position for all display sizes and configurations. For information on accessibility, see the [Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor). |
| T-Visual_Contrast | [Visual_Contrast](https://developer.android.com/docs/quality-guidelines/core-app-quality#Visual_Contrast) | Verify the contrast of all visual elements. |
| T-Content_Description | [Content_Description](https://developer.android.com/docs/quality-guidelines/core-app-quality#Content_Description) | Verify that all UI elements other than `TextView` have content descriptions. |

### Functionality

Verify that your app implements the following functional behavior.

#### Audio

| ID | Feature | Description |
|---|---|---|
| T-Audio_Playback_Start | [Audio_Playback_Start](https://developer.android.com/docs/quality-guidelines/core-app-quality#Audio_Playback_Start) | Initiate audio playback. Verify that within one second the app starts playing the audio or provides a visual indicator that the audio data is being prepared for playback. |
| T-Audio_Focus_Request | [Audio_Focus_Request](https://developer.android.com/docs/quality-guidelines/core-app-quality#Audio_Focus_Request) | Initiate audio playback. App should [request audio focus](https://developer.android.com/reference/kotlin/android/media/AudioManager#requestaudiofocus). When audio playback stops, the app should relinquish audio focus (which happens automatically for apps that target [Android 12 (API level 31) and higher](https://developer.android.com/media/optimize/audio-focus#audio-focus-12)). |
| T-Audio_Focus_Change | [Audio_Focus_Change](https://developer.android.com/docs/quality-guidelines/core-app-quality#Audio_Focus_Change) | Initiate audio playback. Initiate audio playback in another app. Your app should respond to the [change in audio focus](https://developer.android.com/media/optimize/audio-focus#audio-focus-change) and stop audio playback or reduce playback volume. |
| T-Audio_Playback_Background | [Audio_Playback_Background](https://developer.android.com/docs/quality-guidelines/core-app-quality#Audio_Playback_Background) | Initiate audio playback. Interact with another *non-audio* app as the foreground app. The app should continue playing audio in the background and should display a notification in the status bar. Verify that you can manage playback using controls displayed in the notification. Lock the device screen. The app should continue playing audio in the background and should display a notification on the lock screen. Verify that you can manage playback using controls displayed in the notification. |
| T-Audio_Notification_Style | [Audio_Notification_Style](https://developer.android.com/docs/quality-guidelines/core-app-quality#Audio_Notification_Style) | Initiate audio playback. Interact with another *non-audio* app as the foreground app. Verify that your app continues to play audio in the background and has created a notification styled with `MediaStyle`. See [Playing nicely with media controls](https://android-developers.googleblog.com/2020/08/playing-nicely-with-media-controls.html). |
| T-Audio_Playback_Resume | [Audio_Playback_Resume](https://developer.android.com/docs/quality-guidelines/core-app-quality#Audio_Playback_Resume) | Initiate audio playback. Interact with another non-audio app as the foreground app. Interact with your app to make it the top app. Audio should resume or volume should be restored. Otherwise, the app should indicate to the user that playback is paused. |

#### Video

| ID | Feature | Description |
|---|---|---|
| T-Video_PiP | [Video_PiP](https://developer.android.com/docs/quality-guidelines/core-app-quality#Video_PiP) | Activate app [video playback in picture-in-picture mode](https://developer.android.com/guide/topics/ui/picture-in-picture#pip_button). |
| T-Video_Encoding | [Video_Encoding](https://developer.android.com/docs/quality-guidelines/core-app-quality#Video_Encoding) | Verify that the app encodes video using the HEVC video compression standard. |
| T-Video_Playback_Background | [Video_Playback_Background](https://developer.android.com/docs/quality-guidelines/core-app-quality#Video_Playback_Background) | Start video playback. Minimize the app window, open another app to move the app window to the background. On desktop‑capable devices, move the app window off the visible desktop. Verify that video playback continues without interruption in all cases. |

#### Sharing

| ID | Feature | Description |
|---|---|---|
| T-System_Sharesheet | [System_Sharesheet](https://developer.android.com/docs/quality-guidelines/core-app-quality#System_Sharesheet) | Create an intent and start an activity by calling [`startActivity()`](https://developer.android.com/reference/kotlin/android/app/Activity#startactivity) with the intent as an argument. See [Use the Android Sharesheet](https://developer.android.com/training/sharing/send#using-android-system-sharesheet). Your app should display the Android Sharesheet. |

#### Background services

| ID | Feature | Description |
|---|---|---|
| T-Background_Service_Optimization | [Background_Service_Optimization](https://developer.android.com/docs/quality-guidelines/core-app-quality#Background_Service_Optimization) | Use all major features of your app. Verify that no long-running background services are started. Switch to another app to send your app to the background. Go to **Settings** and check whether your app has any services running while in the background. On Android 4.0 and higher, go to the **Apps** screen and find the app in the **Running** tab. |

### Performance and stability

Verify performance, stability, and pixel-perfect visuals.

#### Performance

| ID | Feature | Description |
|---|---|---|
| T-App_Startup_Time | [App_Startup_Time](https://developer.android.com/docs/quality-guidelines/core-app-quality#App_Startup_Time) | Start your app. Verify that the app loads quickly or provides a progress indicator or similar cue if the app takes longer than two seconds to load. |
| T-Rendering_Performance | [Rendering_Performance](https://developer.android.com/docs/quality-guidelines/core-app-quality#Rendering_Performance) | Use all major features of your app. Verify that the app renders at least 60 frames per second. Use the [Profile HWUI rendering](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering) option to help test your app. |
| T-StrictMode_Compliance | [StrictMode_Compliance](https://developer.android.com/docs/quality-guidelines/core-app-quality#StrictMode_Compliance) | Enable `StrictMode` in your app. Use all major features. Verify that the app doesn't produce any `StrictMode` performance warnings; that is no red flashes are visible when testing the app. Red flashes indicate bad behavior regarding storage, network access, or memory management (such as memory leaks). Pay close attention to garbage collection and its impact on the user experience. |

#### Stability

| ID | Feature | Description |
|---|---|---|
| T-Stability_ANR | [Stability_ANR](https://developer.android.com/docs/quality-guidelines/core-app-quality#Stability_ANR) | Use all major features of your app. Verify that the app does not crash or block the UI thread causing ANR (Android Not Responding) errors. Review the Google Play [pre-launch report](https://support.google.com/googleplay/android-developer/answer/9842757) to identify potential stability issues. |

#### SDK

| ID | Feature | Description |
|---|---|---|
| T-Android_Platform_Compatibility | [Android_Platform_Compatibility](https://developer.android.com/docs/quality-guidelines/core-app-quality#Android_Platform_Compatibility) | Run your app on the latest public version of the Android platform. Use all major features. Verify that the app doesn't crash and runs without any loss of core functionality. |
| T-Target_SDK_Version | [Target_SDK_Version](https://developer.android.com/docs/quality-guidelines/core-app-quality#Target_SDK_Version), [Compile_SDK_Version](https://developer.android.com/docs/quality-guidelines/core-app-quality#Compile_SDK_Version) | Review the Android manifest file and build configuration to ensure the application is built against the [latest available SDK](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels) (`targetSdk` and `compileSdk`). |
| T-SDK_Maintenance | [SDK_Maintenance](https://developer.android.com/docs/quality-guidelines/core-app-quality#SDK_Maintenance) | Review your app's `build.gradle` file for any outdated dependencies. |
| T-Non_SDK_Interfaces | [Non_SDK_Interfaces](https://developer.android.com/docs/quality-guidelines/core-app-quality#Non_SDK_Interfaces) | Use the [Android Studio lint tool](https://developer.android.com/distribute/best-practices/develop/restrictions-non-sdk-interfaces#studio-lint) to detect non-SDK interface usage. See [Restrictions on non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk) for alternative testing methods. |
| T-Production_Build_Quality | [Production_Build_Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality#Production_Build_Quality) | Review your app's `build.gradle` file for any included debug libraries. |

#### Battery

| ID | Feature | Description |
|---|---|---|
| T-Power_Management | [Power_Management](https://developer.android.com/docs/quality-guidelines/core-app-quality#Power_Management) | Use all major app features in Doze and App Standby modes. Verify that alarms, timers, notifications, and syncs function properly in the Doze *maintenance window* and when the app exits App Standby mode. Test Doze and App Standby behavior using ADB commands (see [Test with Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby#testing_doze_and_app_standby) for requirements and guidelines). To diagnose unexpected battery drain, use the [Android Studio Power Profiler](https://developer.android.com/studio/profile/power-profiler) or the [Battery Historian](https://developer.android.com/topic/performance/power/battery-historian) tool combined with planned background work. |

### Privacy and security

Test for privacy and security protections expected by users.

#### Permissions

| ID | Feature | Description |
|---|---|---|
| T-Minimize_Permissions | [Minimize_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#Minimize_Permissions) | Review all permissions that your app requires, in the manifest file, at runtime, and in app settings on the device (**Settings \> App Info**). |
| T-Sensitive_Permissions | [Sensitive_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#Sensitive_Permissions) | Use any features of your app that request permissions. Verify that the app requests permission to access sensitive data or services only for core app use cases. Verify that the implications of granting permission to sensitive data and services are clearly communicated to the user. |
| T-Runtime_Permissions | [Runtime_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#Runtime_Permissions) | Use all features of your app that require permissions. Verify that the permissions are requested *lazily*, that is, only when the features are accessed, rather than during app startup. |
| T-Permission_Rationale | [Permission_Rationale](https://developer.android.com/docs/quality-guidelines/core-app-quality#Permission_Rationale) | Use all features of your app that require permissions. Verify that the app explains to the user why the permissions are needed. |
| T-Graceful_Degradation | [Graceful_Degradation](https://developer.android.com/docs/quality-guidelines/core-app-quality#Graceful_Degradation) | Use all features of your app that require permissions. Deny or revoke the permissions. Verify that the app provides an alternative use case and continues to function. |

#### Data and files

| ID | Feature | Description |
|---|---|---|
| T-Sensitive_Data_Storage | [Sensitive_Data_Storage](https://developer.android.com/docs/quality-guidelines/core-app-quality#Sensitive_Data_Storage) | Review all data stored in internal storage. Verify that data stored externally is not sensitive data. |
| T-Sensitive_Data_Handling | [Sensitive_Data_Storage](https://developer.android.com/docs/quality-guidelines/core-app-quality#Sensitive_Data_Storage) | Review how the data that's loaded from external storage is handled and processed. |
| T-Sensitive_Data_Logging | [Sensitive_Data_Logging](https://developer.android.com/docs/quality-guidelines/core-app-quality#Sensitive_Data_Logging) | Use all major app features while monitoring the device log. Verify that no private user information is logged. |
| T-Hardware_IDs | [Hardware_IDs](https://developer.android.com/docs/quality-guidelines/core-app-quality#Hardware_IDs) | Use all major app features. Verify that the app does not use any hardware IDs such as the IMEI for identification purposes. |

#### Identity

| ID | Feature | Description |
|---|---|---|
| T-Autofill_Hints | [Autofill_Hints](https://developer.android.com/docs/quality-guidelines/core-app-quality#Autofill_Hints) | Use all app features that require user input. Verify that the app provides hints to autofill input fields for data such as account credentials and other sensitive information. |
| T-Credential_Manager | [Credential_Manager](https://developer.android.com/docs/quality-guidelines/core-app-quality#Credential_Manager) | Sign in to your app. Verify that the app integrates [Credential Manager for Android](https://developer.android.com/training/sign-in/passkeys) for a sign-in experience that unifies support for passkeys, federated identity, and passwords. |
| T-Biometric_Authentication | [Biometric_Authentication](https://developer.android.com/docs/quality-guidelines/core-app-quality#Biometric_Authentication) | Use all app features that require authentication. Verify that the app protects financial transactions or sensitive information, such as important user documents, with [biometric authentication](https://developer.android.com/training/sign-in/biometric-auth). |

#### App components

| ID | Feature | Description |
|---|---|---|
| T-Component_Export | [Component_Export](https://developer.android.com/docs/quality-guidelines/core-app-quality#Component_Export) | Review all [application components](https://developer.android.com/guide/topics/manifest/application-element) defined in the Android manifest file for the appropriate export state. The exported property must be set explicitly for all components. |
| T-Component_Permissions | [Component_Permissions](https://developer.android.com/docs/quality-guidelines/core-app-quality#Component_Permissions) | Review all permissions that your app requires, in the manifest file, at runtime, and in the app settings on the device (**Settings \> App Info**). |
| T-Component_Protection | [Component_Protection](https://developer.android.com/docs/quality-guidelines/core-app-quality#Component_Protection) | Review all content providers defined in the Android manifest file. Make sure each provider has an appropriate `protectionLevel`. |

#### Networking

| ID | Feature | Description |
|---|---|---|
| T-Network_Security_Traffic | [Network_Security_Traffic](https://developer.android.com/docs/quality-guidelines/core-app-quality#Network_Security_Traffic) | Declare a network security configuration that [disables cleartext traffic](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted), then test the app. |
| T-Network_Security_Configuration | [Network_Security_Configuration](https://developer.android.com/docs/quality-guidelines/core-app-quality#Network_Security_Configuration) | Review the app's [network security configuration](https://developer.android.com/training/articles/security-config). Verify that no lint checks on the configuration fail. |
| T-Security_Provider_Initialization | [Security_Provider_Initialization](https://developer.android.com/docs/quality-guidelines/core-app-quality#Security_Provider_Initialization) | Verify that the security provider is initialized at application startup for Google Play services. |

#### WebViews

| ID | Feature | Description |
|---|---|---|
| T-WebView_Asset_Loader | [WebView_Asset_Loader](https://developer.android.com/docs/quality-guidelines/core-app-quality#WebView_Asset_Loader) | Review the app's [network security configuration](https://developer.android.com/training/articles/security-config). Verify that no lint checks on the configuration fail. |
| T-WebView_JavaScript | [WebView_JavaScript](https://developer.android.com/docs/quality-guidelines/core-app-quality#WebView_JavaScript) | For each `WebView`, navigate to a page that requires JavaScript. |
| T-WebView_Navigation | [WebView_Asset_Loader](https://developer.android.com/docs/quality-guidelines/core-app-quality#WebView_Asset_Loader), [WebView_JavaScript](https://developer.android.com/docs/quality-guidelines/core-app-quality#WebView_JavaScript) | In each WebView, attempt to navigate to sites and content that aren't loaded directly by your app. |

#### Execution

| ID | Feature | Description |
|---|---|---|
| T-App_Bundles | [App_Bundles](https://developer.android.com/docs/quality-guidelines/core-app-quality#App_Bundles) | Verify that the app uses [Android App Bundles](https://developer.android.com/guide/app-bundle) and does not dynamically load code from outside the app's APK. |

#### Cryptography

| ID | Feature | Description |
|---|---|---|
| T-Cryptographic_Algorithms | [Cryptographic_Algorithms](https://developer.android.com/docs/quality-guidelines/core-app-quality#Cryptographic_Algorithms) | Verify that the app uses strong, platform-provided [cryptographic algorithms and a random number generator](https://developer.android.com/privacy-and-security/security-tips#cryptography). Also verify that the app doesn't implement custom algorithms. |

### Google Play

Verify that your app is ready for Google Play.

#### Policies

| ID | Feature | Description |
|---|---|---|
| T-Play_Content_Policies | [Play_Content_Policies](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_Content_Policies), [Play_Content_Rating](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_Content_Rating), [Play_User_Reviews](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_User_Reviews) | Sign into the [Google Play Developer Console](https://play.google.com/apps/publish/) to review your developer profile, app description, screenshots, feature graphic, content rating and user feedback. |

#### App details page

| ID | Feature | Description |
|---|---|---|
| T-Play_Feature_Graphic | [Play_Feature_Graphic](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_Feature_Graphic) | Download your feature graphic and screenshots, and scale them down to match the display sizes on the devices and form factors that you are targeting. |
| T-Play_Graphic_Assets | [Play_Feature_Graphic](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_Feature_Graphic), [Play_Device_References](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_Device_References), [Play_Misleading_Content](https://developer.android.com/docs/quality-guidelines/core-app-quality#Play_Misleading_Content) | Review all graphical assets, media, text, code libraries, and other content that's packaged in the app or expansion file download. |

## Archive

Previous versions of the core app quality guidelines:

- [2026-03-20](https://developer.android.com/docs/quality-guidelines/archive/core/core-app-quality-2026-03-20)
- [2021-05-17](https://developer.android.com/docs/quality-guidelines/archive/core/core-app-quality-2021-05-17)
- [2021-02-10](https://developer.android.com/docs/quality-guidelines/archive/core/core-app-quality-2021-02-10)