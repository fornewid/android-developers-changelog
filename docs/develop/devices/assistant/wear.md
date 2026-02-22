---
title: https://developer.android.com/develop/devices/assistant/wear
url: https://developer.android.com/develop/devices/assistant/wear
source: md.txt
---

[Video](https://www.youtube.com/watch?v=gVIEbeqQQW8)

Watch voice assistants enable quick and efficient on-the-go scenarios. Voice
interactions on wearables are dynamic, meaning that the user may speak to their
wrist without necessarily looking at the device while waiting for a response.

With Assistant App Actions, Android developers can extend [Wear OS apps](https://developer.android.com/wear) to
Google Assistant, fast forwarding users into their apps with voice commands like
*"Hey Google, start my run on ExampleApp."*

#### Limitations

Assistant on Wear supports media and workout tracking activity interactions. For
guidance on integrating media apps with Assistant, see [Google Assistant
and media apps](https://developer.android.com/media/implement/assistant). The following Health and Fitness BIIs are supported for
Wear OS apps:

- [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise)
- [`STOP_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/stop-exercise)
- [`PAUSE_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/pause-exercise)
- [`RESUME_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/resume-exercise)

## How it works

App Actions extend app functionality to Assistant, enabling users to access app
features quickly, using their voice. When a user indicates to Assistant that
they want to use your app, Assistant looks for App Actions registered to your
app in the app's `shortcuts.xml` resource.

App Actions are described in `shortcuts.xml` with Android [capability](https://developer.android.com/develop/ui/views/launch/shortcuts/adding-capabilities#define_capabilities_in_shortcutsxml) elements.
Capability elements pair [built-in intents](https://developer.android.com/guide/app-actions/intents) (BII), which are semantic
descriptions of an app capability, with fulfillment instructions, such as a deep
link template. When you upload your app using the Google Play console, Google
registers the capabilities declared in `shortcuts.xml`, making them available
for users to trigger from Assistant.

![App Actions flow](https://developer.android.com/static/develop/devices/assistant/images/app-actions-wear-flow.png)

The preceding diagram demonstrates a user pausing their exercise in a standalone
app. The following steps occur:

1. The user makes a voice request to Assistant for the specific wearable app.
2. Assistant matches the request to a pre-trained model (BII), and extracts any parameters found in the query that are supported by the BII.
3. In the example, Assistant matches the query to the [`PAUSE_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/pause-exercise) BII, and extracts the exercise name parameter, "hike."
4. The app is triggered via its `shortcuts.xml` capability fulfillment definition for this BII.
5. The app processes the fulfillment, pausing the exercise.

#### Connectivity

App Actions development varies depending on the functionality of your app within
the Android-powered device ecosystem.

- **Tethered**: When a wearable app is dependent on the mobile app for full
  functionality, user queries made to Assistant through the watch are fulfilled
  on the mobile device. App Actions fulfillment logic must be built into the
  mobile app for this scenario to function properly.

- **Untethered**: When a wearable app is independent from a mobile app for
  functionality, Assistant fulfills user queries locally on the watch. App
  Actions capabilities must be built into the wearable app for these requests to
  fulfill properly.

| **Note:** This only applies to App Actions functionality on wearables. [General queries to the Assistant](https://assistant.google.com/platforms/wearables/) such as getting things done, home control, and helpful info for the day are handled automatically through the Google Assistant app.

## Add voice capabilities to Wear

Integrate App Actions with your Wear OS app by following these steps:

1. Match the in-app functionality you want to voice enable to a [corresponding BII](https://developer.android.com/guide/app-actions/get-started#identify_app_functionality).
2. Declare support for Android shortcuts in your main activity
   `AndroidManifest.xml` resource.

       <!-- AndroidManifest.xml -->
       <meta-data
           android:name="android.app.shortcuts"
           android:resource="@xml/shortcuts" />

3. Add an [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) element to AndroidManifest.xml. This enables
   Assistant to use deep links to connect to your app's content.

4. [Create shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema#overview) to provide fulfillment details for your BIIs. You use
   `capability` shortcut elements to declare to Assistant the BIIs your app
   supports. For more information, see [Add capabilities](https://developer.android.com/develop/ui/views/launch/shortcuts/adding-capabilities).

5. In `shortcuts.xml`, implement a [capability](https://developer.android.com/develop/ui/views/launch/shortcuts/adding-capabilities#define_capabilities_in_shortcutsxml) for your chosen BII. The
   following sample demonstrates a capability for the [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII:

       <?xml version="1.0" encoding="utf-8"?>
       <!-- This is a sample shortcuts.xml -->
       <shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
         <capability android:name="actions.intent.START_EXERCISE">
           <intent
             android:action="android.intent.action.VIEW"
             android:targetPackage="YOUR_UNIQUE_APPLICATION_ID"
             android:targetClass="YOUR_TARGET_CLASS">
             <!-- Eg. name = "Running" -->
             <parameter
               android:name="exercise.name"
               android:key="name"/>
             <!-- Eg. duration = "PT1H" -->
             <parameter
               android:name="exercise.duration"
               android:key="duration"/>
           </intent>
         </capability>
       </shortcuts>

6. If applicable, expand support for user speech variations using an
   [inline inventory](https://developer.android.com/guide/app-actions/inline-inventory), which represents features and content in your app.

       <capability android:name="actions.intent.START_EXERCISE">
         <intent
           android:targetPackage="com.example.myapp"
           android:targetClass="com.example.myapp.ExerciseActivity">
           <parameter android:name="exercise.name" android:key="exercise" />
         </intent>
       </capability>

       <shortcut android:shortcutId="CARDIO_RUN">
         <capability-binding android:key="actions.intent.START_EXERCISE">
           <parameter-binding
             android:key="exercise.name"
             android:value="@array/run_names" />
           </capability-bindig>
       </shortcut>

7. Update your app's logic to handle the incoming App Actions fulfillment.

       //FitMainActivity.kt

       private fun handleIntent(data: Uri?) {
           var actionHandled = true
           val startExercise = intent?.extras?.getString(START_EXERCISE)

           if (startExercise != null){
               val type = FitActivity.Type.find(startExercise)
               val arguments = Bundle().apply {
                   putSerializable(FitTrackingFragment.PARAM_TYPE, type)
               }
               updateView(FitTrackingFragment::class.java, arguments)
           }
           else{
               showDefaultView()
               actionHandled = false
           }
           notifyActionSuccess(actionHandled)
       }

## Preview, test, and publish your app

App Actions provide tools to review and test your app. For more detailed
information, see [Google Assistant plugin for Android Studio](https://developer.android.com/guide/app-actions/test-tool). Once you have
tested your app and created a test release, you can request an
[App Actions review](https://developer.android.com/guide/app-actions/get-started#request-review) and deploy. Review the following best practices for
guidance on handling common errors.
| **Note:** The App Actions review is separate from the [Google Play review](https://play.google.com/console/about/guides/releasewithconfidence/#review-guidance-for-your-first-app-launch) and does not affect your status in Google Play. While your app may pass the Google Play review and be published, App Actions will not function for your app's users until the App Actions review is completed.

**Best practices**

Create a positive user experience when integrating your app with Assistant by
following these recommended best practices.

Show a corresponding or relevant confirmation screen, along with haptics and
audio feedback, to respond to a user request - either when successfully
fulfilling a request, or to alert to an error.

| Basic quality | Better quality | Best quality |
|---|---|---|
| - Create an intent to start `ConfirmationActivity` from an activity. | - Create an intent to start `ConfirmationActivity` from an activity. - Play a chime AND haptic feedback to indicate current state. | - Create an intent to start `ConfirmationActivity` from an activity. - Text-To-Speech (TTS) and haptic feedback to indicate error or success. |

| **Note:** Custom TTS prompts are not available through App Actions.

**Common errors and resolutions**

For the following error cases, use the following recommended app
[`ConfirmationActivity`](https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity) messaging.

| Error case | Example user interaction | App response |
|---|---|---|
| Activity already ongoing | "Start my *ExerciseName* " "Resume my *ExerciseName*" | Display error: Already ongoing activity." |
| No Activity started | "Pause/Stop my *ExerciseName*" | Display error: "No activity started." |
| Mismatch of Activity types | "Pause/Stop my *ExerciseName*," which is a different exercise type from the ongoing activity. | Display error: "Activity type mismatch." |
| Login error | "Start my *ExerciseName*," when the user is not logged into the app. | Play haptic to alert user and redirect to login screen. |
| Permissions error | The user does not have permission to start their requested activity. | Play haptic to alert user and redirect to permission request screen. |
| Sensor issue | The user has location services turned off in their device settings. | Play haptic to alert users and show sensor error screen. Optional next steps: - Start activity without sensor tracking and notify user. - Request user acknowledgement to start activity without sensor tracking. |

*** ** * ** ***