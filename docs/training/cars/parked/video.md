---
title: https://developer.android.com/training/cars/parked/video
url: https://developer.android.com/training/cars/parked/video
source: md.txt
---

In addition to the guidelines described in [Build parked apps for Android
Automotive OS](https://developer.android.com/training/cars/parked/automotive-os), there are some requirements specific to video apps.
| **Design guidelines:** Refer to [Adapt video apps](https://developers.google.com/cars/design/create-apps/parked-passenger-apps/overview) for UX guidance specific to video apps.
| **Important:** Google takes driver distraction very seriously. Your app must meet specific criteria before it can be listed on Google Play for Android Automotive OS. By adhering to these requirements, you can make it easier to build and test your app. For more information, see [Android app quality for cars](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=video).

## Mark your app as a video app

To indicate that your app is a video app, add the
[`android:appCategory="video"`](https://developer.android.com/guide/topics/manifest/application-element#appCategory) attribute to the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element
of your manifest.  

    <manifest ...>
        ...
        <application
          ...
          android:appCategory="video">
            ...
        </application>
    </manifest>

## Support audio while driving

Audio while driving is a beta feature  
Publishing apps that support audio while driving is limited to early access partners. While this feature is in beta, you can prepare your app for support by following the guidance in this section.  
[Nominate yourself to be an early access partner →](https://goo.gle/440dHqw)  
![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

In general, all video apps must pause playback when user experience restrictions
are active, as described in [Meet driver distraction requirements](https://developer.android.com/training/cars/parked/automotive-os#driver-distraction).

However, some vehicles have the ability to display driving-optimized playback
controls while user experience restrictions are active, making it possible to
continue playing audio.
![Driving optimized playback controls for an app that supports audio while driving.](https://developer.android.com/static/training/cars/images/media-blocking-activity.png) **Figure 1**: Driving optimized playback controls for an app that supports audio while driving.  
[![](https://developer.android.com/static/images/picto-icons/code.svg)
Codelab
Follow a step-by-step guide to implement support for audio while driving
arrow_forward](https://developer.android.com/codelabs/audio-while-driving)

### Declare that your app supports audio while driving

To indicate that your app supports audio while driving, add the following
[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) element in your manifest:  

    <manifest ...>
        ...
        <uses-feature
            android:name="com.android.car.background_audio_while_driving"
            android:required="false" />
        ...
    </manifest>

| **Important:** Setting the `android:required` attribute to `false` ensures that your app can still be distributed to devices that don't support audio while driving.

### Support background playback

Because your app's activities are hidden by the system UX restrictions, your app
must support background playback to continue playing audio while driving. See
[Background playback with a MediaSessionService](https://developer.android.com/media/media3/session/background-playback) for details on how to
accomplish this using the Media3 library.

Your app must post a [`MediaStyle`](https://developer.android.com/reference/androidx/media/app/NotificationCompat.MediaStyle) notification that includes your app's
`MediaSession`. If you're using `MediaSessionService`, this is [handled for you
by default](https://developer.android.com/media/media3/session/background-playback#notification).
| **Caution:** If you don't use a service for background playback, playback may continue for a short period of time, but your app will eventually be [cached](https://developer.android.com/guide/components/activities/process-lifecycle) by the system, causing playback to end.

### Determine support

To determine if a device supports audio while driving, you can use the
[`CarFeatures`](https://developer.android.com/reference/androidx/car/app/features/CarFeatures#summary) class from the [`androidx.car.app:app`](https://developer.android.com/jetpack/androidx/releases/car-app) library.  

    CarFeatures.isFeatureEnabled(context, CarFeatures.FEATURE_BACKGROUND_AUDIO_WHILE_DRIVING)

Use this information to modify your app's behavior depending on the capabilities
of the device it's running on. On devices that don't support audio while
driving, your app must still meet the [`DD-2`](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=video#DD-2) guideline.

### Test audio while driving

To test your implementation, you can [simulate driving](https://developer.android.com/training/cars/testing/emulator#simulate-driving) can using an
[emulator image that supports audio while driving](https://developer.android.com/training/cars/testing/emulator?filter=audio-while-driving#generic-images).
| **Caution:** Be sure to test that your app still meets the [`DD-2`](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=video#DD-2) guideline on devices that don't support audio while driving.

## Frequently asked questions

### Is Widevine DRM supported?

Yes, Widevine DRM L3 is supported on Android Automotive OS.