---
title: https://developer.android.com/training/wearables/principles
url: https://developer.android.com/training/wearables/principles
source: md.txt
---

# Principles of Wear OS development

Wear OS is based on Android, so many of the best practices for Android also apply to Wear OS. However, Wear OS is optimized for the wrist, so there are some differences between the two.

To optimize your development time, review the following principles before you start building your Wear OS app.

## Design for critical tasks

If you already have a mobile app, don't migrate the entire codebase. Instead, identify the core tasks that are best suited for the wrist and streamline that experience. A successful wearable app delivers meaningful, glanceable experiences that help people stay present and productive while on the go.
![Wear OS app interfaces showing focused tasks.](https://developer.android.com/static/wear/images/principles_1.png)**Figure 1:**Wear OS app examples.

## Optimize for the wrist

Help people complete tasks on the watch within seconds to avoid ergonomic discomfort or arm fatigue.

Review the[Wear OS design guidelines](https://developer.android.com/training/wearables/design)to learn more about optimizing for the wrist.
![A maps app and timer app running on Wear OS.](https://developer.android.com/static/wear/images/principles_4.png)**Figure 2:**Wear OS app optimized for quick interaction.

## Respect the user's privacy

Your app must earn a user's trust before they grant permission for your app to access potentially sensitive information. The system provides several ways to help users maintain their privacy.

### Privacy dashboard

Starting in Wear OS 5, the system supports the[privacy dashboard](https://support.google.com/android/answer/13530434). This dashboard offers users a centralized view of each app's data usage, including the following details:

- The data types being accessed---for example, location and microphone.
- How recently those data types were accessed.

With access to this information, users can make more informed decisions about which apps should still have access to their personal data. To maintain user trust, use data responsibly and be transparent when collecting and using user data.

### Screenshot detection

On devices that run Wear OS 5 or higher, apps can use a privacy-preserving[screenshot detection API](https://developer.android.com/about/versions/14).

## Use the appropriate surface for the task

Wear OS has more surfaces than mobile to engage users. Apps should tailor their content for these surfaces.

Each surface has its own use case. If more action is required, direct users into a fuller app experience.

Read and understand how your content scales across each surface based on user needs. The following table provides an example of priorities for a weather app.

| ![Wear OS watch face showing a weather complication.](https://developer.android.com/static/wear/images/principles_9.png) | ![Wear OS watch face showing a weather notification.](https://developer.android.com/static/wear/images/principles_updated_2.png) | ![Wear OS watch face showing a weather tile.](https://developer.android.com/static/wear/images/principles_updated_6.png) | ![Wear OS watch face showing a full weather app.](https://developer.android.com/static/wear/images/principles_updated_5.png) |
|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Complication P1: What's the weather right now?                                                                           | Notification P1 Tell me about a severe weather advisory                                                                          | Tile P1: What's the weather right now? P2: What's the weather today?                                                     | App P1: What's the weather right now? P2: What's the weather today? P3: What's the hourly breakdown? P3: Preferences         |

To learn more, read the[User Interface Guide](https://developer.android.com/training/wearables/user-interfaces).

## Add notifications to additional surfaces

In Wear OS API level 30 and higher, pair any ongoing notification with an`OngoingActivity`to add that notification to additional surfaces within the Wear OS user interface. This increases engagement with[long-running activities](https://developer.android.com/training/wearables/notifications/ongoing-activity).

## Support offline scenarios

While a Wear OS device generally supports Bluetooth and Wi-Fi, it might not support LTE. Design for spotty connections and offline use cases, for example, exercising and commuting, when a user might leave their mobile device at home.
![Wear OS music and workout apps that work offline.](https://developer.android.com/static/wear/images/principles_3.png)**Figure 3:**Examples of offline Wear OS app usage.

## Provide relevant content

The watch is almost always with the user. Keep your app content updated with the user's context, for example, their time, place, and activity.
![Wear OS calendar and weather apps with fresh content.](https://developer.android.com/static/wear/images/principles_6.png)**Figure 4:**Wear OS apps with fresh content.

## Help users complete a task from another device

People increasingly own multiple devices. The watch can help users complete a task across a distributed ecosystem of devices. Review use cases where this makes sense for your app.

## Improve user experience during an app cold start

To improve user experience during an app cold start, create a splash activity with a separate theme. Then, set its`windowBackground`to your custom splash drawable in the manifest file. The splash screen consists of a layer-list with two elements: the background color and the custom drawable, which is typically your app icon. Use a 48x48 dp drawable.

For more information, see[Add a splash screen](https://developer.android.com/training/wearables/apps/splash-screen).

## Considerations for media apps

### Enable playback controls for music from the phone

If your app is installed on both the phone and watch, users expect remote controls from their watch. For example, users expect the ability to pause, play, or skip songs from their watch.

### Downloaded content

As noted earlier, it is important to support offline scenarios. This is especially important for media apps. For media apps, it's easier to support offline downloads first, and then add streaming if you see the demand.

When designing, make it clear to the user what content is available offline. For any long-running immediate or periodic tasks, use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager). Defer downloads until the watch is charging and connected to Wi-Fi.

### Streaming on LTE

Consider offering streaming support on devices that have LTE connectivity, a common use case for media playback. Streaming lets users leave their other devices at home and still listen to music. Visually communicate to the user when they are streaming music, and cache streamed audio. Avoid using LTE for any jobs that could be deferred, for example, sending logging and analytics data, to optimize power usage while streaming.

### Support Bluetooth headphones

Users might take only their watch and headphones out for a run or walk. Let them have a true standalone experience by supporting pairing with headphones. If headphones are not connected when playing or resuming music, launch[**Bluetooth settings**](https://developer.android.com/reference/android/provider/Settings#ACTION_BLUETOOTH_SETTINGS)to let the user connect to their Bluetooth headphones directly from the app.

### Indicate music source

Clearly indicate whether the sound is coming from the watch or the phone. Use a source icon to indicate where the music is playing. Set the default source to where the user starts the music.

### Use the speaker

Some Wear OS devices include a built-in speaker that you can use for things like reminders and alarms. Avoid using the built-in speaker for playing media and music, because users expect these experiences to be tied to using headphones. For more information, see[Detecting audio devices](https://developer.android.com/training/wearables/apps/audio#detecting-audio-devices).

## Considerations for fitness apps

When creating fitness apps for Android 10 (API level 29) and higher, request the[Physical activity recognition](https://developer.android.com/about/versions/10/privacy/changes#physical-activity-recognition)permission.

### Complement the mobile app

As outlined earlier, a Wear OS fitness app should handle only critical tasks for the wrist. This means a fitness Wear OS app focuses mostly on data gathering.

While you can include some post-workout summary screens, leave detailed post-workout analysis and any other features that require more screen space to the mobile app.

### Support long-lived activities

Like many apps that subscribe to location and sensor data, design your app to handle running*while-in-use*. This means your app functions in the foreground.

If the workout starts in an activity, bind that activity to a service that performs the work. When the user navigates away from your app, the service unbinds and can promote itself to an ongoing notification.

In Wear OS, you can expose your Ongoing Notifications to new surfaces with the[Ongoing Activity API](https://developer.android.com/training/wearables/notifications/ongoing-activity)by using a minimal amount of code.

Review the[Ongoing Activity code lab](https://developer.android.com/codelabs/ongoing-activity)on GitHub to see a simplified app with this architecture.

### Use always-on sparingly

If a user stops using their watch during a session with your app, the device enters system ambient mode to save battery.

Wear OS brings that app back to an active state if the user interacts with the device again within a specified amount of time.

For most use cases, this is enough for users to have a good experience and save battery life.

In some cases, you might need your app to be visible for longer, for example, during an entire workout. For these cases, use[`AmbientLifecycleObserver`](https://developer.android.com/reference/androidx/wear/ambient/AmbientLifecycleObserver). For more information, see[Keep your app visible on Wear](https://developer.android.com/training/wearables/apps/always-on).

### Don't hold a wake lock

Use APIs, for example,[Health Services](https://developer.android.com/health-and-fitness/guides/health-services), to obtain sensor data while letting the CPU sleep between readings or delivery.

### Optimize location and sensor management

Sensor management is important and can negatively affect battery life if not done properly.

Follow these recommendations when implementing your sensor strategy:

- Always use sensors in batch mode where possible.
- Flush sensors when the screen or app becomes active again.
- Change the length of batching when the screen goes off to conserve power.
- Unregister sensor listeners when they are no longer needed.
- For location sensors, follow the best practices in[Detect location on Wear OS](https://developer.android.com/training/articles/wear-location-detection).

To simplify sensor management and optimize for power, consider using[Health Services](https://developer.android.com/health-and-fitness/guides/health-services).

### Use haptics to confirm actions

Use[haptic feedback](https://developer.android.com/develop/ui/views/haptics/haptic-feedback)to confirm actions, for example, start, stop, auto-pause, or auto-lap.

### Use touch lock

In some cases, disabling the touch experience improves the app experience. For example, it makes sense to disable touch when tracking a workout, because accidental touch is likely in this case.

## Considerations for messaging apps

### Start with notifications

Support[`MessagingStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.MessagingStyle)to improve the user's app experience.

### Support voice input

Support[speech-to-text](https://developer.android.com/training/wearables/user-input/voice), because it's much faster on a watch. You might also want to support recorded audio.