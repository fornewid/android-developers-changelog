---
title: https://developer.android.com/docs/quality-guidelines/android-xr/augmented
url: https://developer.android.com/docs/quality-guidelines/android-xr/augmented
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The app quality guidelines for intelligent eyewear extend the foundational [core
app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) mobile standards.

These app quality guidelines and policies focus on crucial, multimodal
interactions that are unique to the Android XR platform on intelligent eyewear,
as outlined in the [compatibility tier definitions](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#tier-definitions), the [checklists](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#checklist), and
the [policies for audio-only experiences](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#policies-audio). Review these sections to verify
that your app provides a great user experience on audio and display glasses.

## Augmented experiences: mobile app compatibility tier definitions

Review the following compatibility tier definitions to understand the level of
support that your app provides for augmented experiences on glasses.

### Compatible

A compatible mobile app provides an augmented experience on glasses with zero
additional developer effort. This represents an existing Android mobile app
including Bluetooth connectivity that has not been modified for glasses. The
Android XR platform automatically supports this type of app, provided it does
not rely on unsupported hardware features.

To achieve this capability, the platform seamlessly extends standard Android
system surfaces onto the glasses. For example, [notifications](https://developer.android.com/develop/ui/compose/notifications) are
automatically surfaced in the user's line of sight or read aloud (for audio
glasses), ensuring the user can complete critical, glanceable tasks without
needing to pull out their phone.

### Differentiated

A differentiated augmented experience is **specifically designed** for glasses,
leveraging the full capabilities of the Jetpack XR SDK and the unique hardware
of the form factor.

To build these transformative augmented experiences, use the following
libraries:

- [**Jetpack Compose Glimmer**](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer): A Compose UI Toolkit for creating minimal and legible interfaces optimized for optical see-through displays.
- [**Jetpack Projected**](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware): Manage resources and seamlessly bridge functionality between the companion phone (host) and the glasses (projected device).
- [**ARCore for Jetpack XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore): Access advanced perception capabilities like Device Tracking and the Geospatial API, which enable localization and context-aware features such as walking navigation.

## Augmented experiences: mobile app quality checklist

To ensure your app provides a great user experience for augmented experiences,
review the following compatibility checklists and tests.

These checklists and tests define a comprehensive set of quality requirements
for most types of Android apps.

### Compatible

Compatible apps are existing Android mobile apps that work automatically on
glasses by leveraging standard Android surfaces (for example, standard and Live
Update notifications). No glasses-specific code is required for this
compatibility tier.

Your app must fulfill the following core requirements:

- **Notifications** : Ensure all actionable and time-sensitive notifications use standard Android [`NotificationManager`](https://developer.android.com/reference/kotlin/android/app/NotificationManager) APIs so they can be correctly converted by the platform into audio read-outs (audio devices) or minimalist visual overlays (display devices).
- **Live Updates** : If the app has an ongoing activity (such as [progress-related tasks](https://developer.android.com/develop/ui/compose/notifications/live-update)), it must use the standard Live Update notifications framework so the platform can surface this information in a glanceable, hands-free manner.
- **Google Play**: The app must adhere to all applicable Android and Google Play policies. Compatibility is automatically determined based on manifest declarations and feature requirements.

### Differentiated

Differentiated apps are specifically built using the Jetpack XR SDK (with
libraries such as Jetpack Compose Glimmer, Jetpack Projected, and ARCore for
Jetpack XR) to deliver a world-aware, highly-optimized user experience or use
unique augmented capabilities. See the requirements that are appropriate for
your app.

| Category | Area | Guidance |
|---|---|---|
| Core Functionality | Start glasses activity | Experiences should be launchable and controllable directly from the mobile app, especially for initial setup or navigating dense information before handing off to audio and display glasses that have a smaller set of UX capabilities. |
| Core Functionality | Open App command | Experiences should be configured with a zero-launch state on glasses with Gemini so that when a user prompts with an "Open \[App\]" [command](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/first-activity#declare-activity), the app bypasses traditional menus and immediately transitions into a ready-to-act audio experience, such as an audio-only background mode, a live listening state, or an immediate audio cue. |
| Core Functionality | Camera initiation | Camera access can be initiated either from a mobile entry point or activity, or from direct input using the [camera action gesture](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#camera-action-gesture) on the device. If camera access is initiated from the mobile surface, the user should hear a countdown before starting camera streaming. |
| Core Functionality | Clarity and Consistency (Gestures) | Gestures (such as voice, taps, or swipes) should be implemented in a clear and consistent manner, aligning with user expectations for common interactions. Core gesture policies are outlined in the [subsequent, corresponding sections](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#policies-audio). |
| Performance \& Stability | Battery | Optimize background processes following Android [background task](https://developer.android.com/develop/background-work/background-tasks) restrictions and minimize the use of high-drain sensors (such as the camera feed) when not actively in use. |
| Performance \& Stability | Camera frame rate \& resolution | Camera feed access should be configured to use the most-efficient configuration (lowest frame rate and resolution) for a given use-case. For more information on recommended configurations per use-case, refer to the [developer guidance](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context#capture-video). |
| Safety | Safety | Experiences should be designed around user-initiated actions and strictly minimize distracting the user from their immediate surroundings, especially during movement or in public spaces. |
| Privacy \& Security | Permissions | The app must [request glasses-specific permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions) for hardware access (such as the camera or microphone) using the projected request permissions API and handling the redirection to the host device for user consent. |
| General Policy | Accessibility | Consider users with diverse needs and ensure alternative input methods are available (for example, using voice commands as a fallback for touchpad gestures) where appropriate. |
| General Policy | Testing | Thoroughly test all gesture and visual implementations across various user scenarios, lighting, and busy environmental conditions, using the [Android XR Emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/glasses) and [composable previews](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/preview). |
| Google Play | Policies | Adhere to all Google Play policies, including [glasses-specific policies outlined in the subsequent sections](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#policies-audio) that help protect a user's privacy and well-being. |
| Audio Experience | Voice alerts | Voice alerts must be concise and provide only the most relevant, actionable information. Voice alerts for error conditions should work regardless of internet connectivity. Follow-ups and deeper conversations should be explicitly expected using an in-app agent or Gemini. |
| Audio Experience | Audio focus | Audio focus is tightly correlated to input focus. Apps should request and give up audio focus as appropriate and aligned with [Android guidelines](https://developer.android.com/media/optimize/audio-focus). |
| Audio Experience | Audio Policies | Gestures and LED behaviors should comply with all of the [policies for audio-only experiences](https://developer.android.com/docs/quality-guidelines/android-xr/augmented#policies-audio). |

## Policies for audio-only experiences

All apps must comply with the requirements in the following policies to promote
safe and respectful audio-only experiences on intelligent eyewear.

### App safety

As a reminder, all apps distributed through Google Play must comply with all
[Google Play Developer Policies](https://play.google/developer-content-policy/).

The following activities are strictly prohibited, and apps must not facilitate
or promote these activities:

- Doxxing
- Facial recognition or biometric identification
- Surveillance
- Creation or dissemination of Non-Consensual Intimate Imagery (NCII)

The following bystander protections are required for all apps:

#### Camera safety

Apps that access wearable camera sensors must respect bystander privacy and must
comply with the following:

##### Video and photo restriction

| Allowed interactions | Description |
|---|---|
| Video calls | Apps are allowed to use wearable camera sensors for video call purposes. |
| Scene understanding \& ambient sensing | Apps are allowed to use wearable camera sensors for ambient camera sensing or scene understanding. |

| Prohibited interactions | Description |
|---|---|
| Video social live streaming \& public broadcasting | Apps must not use wearable camera sensors for Video Social Live Streaming which includes any real-time, one-to-many live streaming, public broadcasting, or casting to public feeds and open channels. |
| Real-time facial identification \& doxxing | Apps must not use camera sensors to run facial identification to surface bystander Personally Identifiable Information (PII). For example: names, home addresses, phone numbers, or their employer. |
| Non-consensual intimate imagery (NCII) or illegal content generation | Apps must not use camera sensors to facilitate the creation of non-consensual intimate imagery (NCII) or any illegal content generation (for example, CSAM). |

#### Audio safety

Apps utilizing the microphone array should respect bystander privacy and must
comply with the following:

| Prohibited interactions | Description |
|---|---|
| Persistent eavesdropping | Apps must not maintain persistent, background audio recording or transcription when the wearer is not actively engaged with the app on a user-initiated task. |
| Speech identification | Apps must not use the microphone array to identify non-wearer voices or bystanders. |
| Programmatic suppression or modification | Apps must not change or disable system-enforced audio denoisers. Apps must also not encourage or direct users to change or disable audio denoisers. |

### Gestures and input

These policies outline the requirements for implementing gesture events on
glasses during audio-only experiences. Adhere to these guidelines to provide a
consistent and intuitive user experience across different apps and Android XR
devices. All input is expected to work if your app has audio focus, regardless
of its foreground state.

#### 1. Tap gesture

The *tap gesture* is a quick, single touch on the touchpad input area. A tap is
how a user takes action on glasses. This can initiate audio playback, like to
provide information based on a user's state or to repeat the last audible
message. If audio is playing, a tap could pause or stop audio output.

##### Examples

| Allowed interactions | Description |
|---|---|
| Play a relevant prompt | Provide the user with relevant information such as: - Prompting user permissions. - Information based on the user's current state. For example, saying "To your right is the Golden Gate Bridge". - Repeating the last audible message that was provided to the user. Tapping while audio is playing back would stop the audio. |
| Mute or unmute the microphone | Allow users to mute or unmute their microphone with a tap gesture when in an experience that is taking microphone input. Audio feedback should be provided when the microphone is muted or unmuted. |

| Prohibited interactions | Description |
|---|---|
| Irrelevant information or ads | Do not use the tap gesture to serve advertisements or provide information that is irrelevant to the user's current physical state or context. |
| Gaming inputs and rapid continuous actions | The tap gesture is designed for quick, single-touch actions. It must not be repurposed as a continuous controller for interactive games or high-frequency input tasks that disrupt standard system controls. |
| Enabling crime, violence, or self-harm | The tap gesture must never trigger actionable instructions that facilitate illegal or harmful acts, such as extremist scouting, weapons creation, or self-harm. |

#### 2. Camera action gesture

The *camera action gesture* involves pressing the camera button twice in quick
succession. Apps that access the camera must treat this event as a camera action
that provides sensor data directly to the app.

##### Examples

| Allowed interactions | Description |
|---|---|
| Activate camera to the app | Start the camera stream into the app. This includes activating the camera stream to capture photos, videos, or allow for ambient camera processing using the camera feed. <br /> Camera stream usage must conform to all Android policies related to camera and microphone captures, and the [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) policy in the Play [Developer Policy Center](https://play.google/developer-content-policy/). Additionally, the [Bullying and Harassment](https://support.google.com/googleplay/android-developer/answer/9878810) policy disallows apps that dox or exploit others publicly. |

| Prohibited interactions | Description |
|---|---|
| Custom inputs and remapping | The camera double press gesture must be exclusively used to activate the camera stream and provide sensor data directly to the app. You must not remap this hardware gesture to non-camera functions, custom shortcuts, or alternative app experiences. |
| Decoupled or dummy sensor usage | Apps that intercept the camera double press gesture must treat it as a genuine request for visual sensor data. You can't register the double press event to hijack the hardware button while intentionally ignoring, discarding, or suppressing the camera feed. |
| Lack of disclosure or deceptive usage | When the camera double press gesture is used to activate the camera, you must explicitly educate the user on exactly what the camera usage is beforehand in a mobile app flow during initial permission granting or app setup. For example, some valid use cases might be live streaming, taking a photo, or AI processing. The camera stream must never be used for a function that was not explicitly agreed to by the user. |

#### 3. Single finger back swipe gesture

The *single finger back swipe gesture* involves a continuous backward movement
across the touchpad input area. The system supports this gesture even during
audio-only experiences by calling `onBack()`. Your app should handle this event
by either exiting the current experience or returning the user to a previous app
state.

| Prohibited interactions | Description |
|---|---|
| Hijacking the exit command | The back swipe gesture must always call `onBack()` to either exit the experience or return the user to a previous app state. It must never be mapped to custom actions, new media launches, or advertisements. |
| Fake exits (covert listening) | Apps must truly exit or suspend their primary sensor usage when this gesture is invoked. Do not simulate an exit while secretly maintaining active sensors in the background for surveillance. |

### LED behaviors

Your app must not change LED system behavior based on microphone and camera
access.

| Prohibited interactions | Description |
|---|---|
| Programmatic suppression or modification | Apps must not change, dim, or disable the system-enforced world-facing LED and user-facing LED behavior based on microphone and camera access. Apps must also not encourage or direct users to change, dim, or disable the LEDs' behavior. |
| Bypassing thwart and tamper detection | Apps must not bypass or interfere with, or encourage or direct users to do so, the device's thwart detection algorithms, which are designed to programmatically stop recording if the world-facing LED is physically covered or damaged. |