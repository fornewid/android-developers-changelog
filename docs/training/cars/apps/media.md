---
title: https://developer.android.com/training/cars/apps/media
url: https://developer.android.com/training/cars/apps/media
source: md.txt
---

Templated media apps are in beta  
At this time, anyone can publish templated media apps to internal testing and closed testing tracks on the Play Store. Publishing to open tracks and production tracks will be permitted at a later date.  
[Nominate yourself to be an early access partner →](https://goo.gle/Media-Comms-EAP)  
![](https://developer.android.com/static/images/picto-icons/test-tube-2.svg)

Media apps using the Car App Library templates can customize their media
browsing and playback experience while ensuring the experience is
optimized for car screens and minimizes distractions while driving.
| **Note:** Media apps built with the Car App Library templates are currently only available on Android Auto.
| **Design guidelines:** Refer to [Media Apps](https://developers.google.com/cars/design/create-apps/app-types/media) for UX guidance specific to media apps.

This guide assumes that you already have a media app that plays audio on a phone
and that your media app conforms to the [Android media app architecture](https://developer.android.com/media/legacy). The
Car App Library gives you the ability to replace the in-app experience with
templates instead of those built using the [Build media apps for cars](https://developer.android.com/training/cars/media)
`MediaBrowser` data structure. You still must provide a `MediaSession`
for playback controls, and a `MediaBrowserService`, which is used for
recommendations and other smart experiences.
| **Note:** Both a `MediaBrowserService` and Car App Library implementation can be supported by the same app. In the case that a user has an older version of Android Auto installed or cannot use the Car App Library version, the host will fall back to the `MediaBrowserService` implementation.

## Configure your app's manifest

In addition to the steps described in
[Using the Android for Cars App Library](https://developer.android.com/training/cars/apps#configure-manifest-files), the following are
required of templated media apps:

### Declare category support in your manifest

Your app needs to declare the `androidx.car.app.category.MEDIA`
[car app category](https://developer.android.com/training/cars/apps#supported-app-categories) in the intent
filter of its [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService).  

    <application>
        ...
       <service
           ...
            android:name=".MyCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.MEDIA"/>
          </intent-filter>
        </service>
        ...
    <application>

To get access to the [`MediaPlaybackTemplate`](https://developer.android.com/reference/kotlin/androidx/car/app/media/model/MediaPlaybackTemplate), your app also
needs to declare the `androidx.car.app.MEDIA_TEMPLATES` permission in its
manifest file:  

    <manifest ...>
      ...
      <uses-permission android:name="androidx.car.app.MEDIA_TEMPLATES"/>
      ...
    </manifest>

### Set the minimum car app API level

Media apps using the `MediaPlaybackTemplate` are only supported in CAL API 8,
be sure your minimum [`Car App API level`](https://developer.android.com/training/cars/apps#api-level) is set to 8.  

    <application ...>
      ...
      <meta-data
        android:name="androidx.car.app.minCarApiLevel"
        android:value="8"/>
      ...
    </application>

### Declare Android Auto support

Ensure the following is included in your app's manifest:  

    <application>
      ...
      <meta-data android:name="com.google.android.gms.car.application"
          android:resource="@xml/automotive_app_desc"/>
      ...
    </application>

Then, add the *template* declaration to `automotive_app_desc.xml` in your xml
resources. It should look as follows:  

    <automotiveApp xmlns:android="http://schemas.android.com/apk/res/android">
     <uses name="media"/>
     <uses name="template"/>
    </automotiveApp>

### Provide an attribution icon

Be sure to add an [attribution icon](https://developer.android.com/training/cars/media#attribution_icon) for media apps built using the Car
App Library.

## Support voice actions

Voice-enable your app to allow users to complete common actions hands-free.
See [support voice actions for media](https://developer.android.com/training/cars/media#support_voice) for more detailed implementation
instructions. With a templated media app if you receive a voice command, you
don't need to update your `MediaBrowserService` with search results. Instead,
consider adding an action in your media playback template to allow the user to
find more content based on that play or search query. Supporting voice commands
is required to meet the [`VC-1`](https://developer.android.com/docs/quality-guidelines/car-app-quality#car-optimized-tier) quality guideline.

## Create your Playback Template

The [`MediaPlaybackTemplate`](https://developer.android.com/reference/kotlin/androidx/car/app/media/model/MediaPlaybackTemplate) displays media playback
information in your Car App Library media app. This template allows setting a
header with a title and customizable actions while the media information and
playback controls are populated by the host based off of the state of your app's
`MediaSession`.

![A music player shows Sounds of Spring by Summer Fielding with an
square portrait of a woman playing guitar.](https://developer.android.com/static/training/cars/images/now-playing.png)

**Figure 1:**
`MediaPlaybackTemplate` with a header action to open the queue
along the top.

<br />

This code example shows how to build an example playback template that sets a
header action which allows the user to navigate to a screen with the queue
of songs.  

    val playbackTemplate = MediaPlaybackTemplate.Builder()
          .setHeader(
            Header.Builder()
              .setStartHeaderAction(Action.BACK)
              .addEndHeaderAction(
                    Action.Builder()
                      .setTitle(model.context.getString(R.string.queue_button_title))
                      .setIcon(
                        CarIcon.Builder(
                            IconCompat.createWithResource(
                              model.context,
                              R.drawable.gs_queue_music_vd_theme_24,
                            ))
                          .build())
                      .setOnClickListener(showQueueScreen())
                      .build())
              .setTitle(model.context.getString(R.string.media_playback_view_title))
              .build())
          .build()

When you use [`MediaPlaybackTemplate`](https://developer.android.com/reference/kotlin/androidx/car/app/media/model/MediaPlaybackTemplate), register a
`MediaSession` token using the [`MediaPlaybackManager`](https://developer.android.com/reference/androidx/car/app/media/MediaPlaybackManager) in your
`CarAppService`. Failing to do so causes an error to be displayed when a
`MediaPlaybackTemplate` is sent to the host.  

    import androidx.car.app.media.MediaPlaybackManager
    ...

    override fun onCreateSession(sessionInfo: SessionInfo): Session {
        return object : Session() {
            ...

            init {
              lifecycle.addObserver(
                LifecycleEventObserver { _, event ->
                  if (event == ON_CREATE) {
                    val token = ... // MediaSessionCompat.Token
                    (carContext.getCarService(CarContext.MEDIA_PLAYBACK_SERVICE) as MediaPlaybackManager)
                      .registerMediaPlaybackToken(token)
                  }
                  ...
                }
              )
            }
        }
    }

`.registerMediaPlaybackToken` is necessary for exposing media playback
information and controls to Android Auto. This is also important for the host to
create media specific notifications.

## Organize media using templates

To organize media for browsing such as songs or albums, we recommend using the
[`SectionedItemTemplate`](https://developer.android.com/reference/androidx/car/app/model/SectionedItemTemplate),
which lets you use the [`GridSection`](https://developer.android.com/reference/androidx/car/app/model/GridSection) and
[`RowSection`](https://developer.android.com/reference/androidx/car/app/model/RowSection) together to create layouts that mix lists of images
and text items.
| **Caution:** The screen stack can have a maximum depth of five screens. See [Template restrictions](https://developer.android.com/training/cars/apps#template-restrictions).

![A music app interface displays recently played songs and albums,
including two vertical rows and three horizontal album art portraits.](https://developer.android.com/static/training/cars/images/sectioned-item.png)

**Figure 2:** A
`SectionedItemTemplate` containing a `RowSection`
followed by a `GridSection`

<br />

### Using SectionedItemTemplate inside a TabTemplate

One convenient way to categorize media within your app, is using the
[`SectionedItemTemplate`](https://developer.android.com/reference/androidx/car/app/model/SectionedItemTemplate) inside a
[`TabTemplate`](https://developer.android.com/reference/androidx/car/app/model/TabTemplate).  

    val template =
          SectionedItemTemplate.Builder()...build();
    val tabTemplate = 
          TabTemplate.Builder(tabCallback)
              .setTabContents(TabContents.Builder(template).build)
              .setHeaderAction(Action.APP_ICON)
              ...
              .build();

For more details about how to design your media app's user interface using these
templates, see [Media apps](https://developers.google.com/cars/design/create-apps/app-types/media).

## Navigating to the playback controls

When browsing through media it is important that the user is able to quickly
navigate to the `MediaPlaybackTemplate` with minimal distraction. To meet the
[`MFT-1`](https://developer.android.com/docs/quality-guidelines/car-app-quality#car-optimized-tier) quality requirement, your app must have a way to access
the `MediaPlaybackTemplate` from all media browsing screens.

If you are using `SectionedItemTemplate` you can achieve this by adding a
floating action button that [navigates you](https://developer.android.com/training/cars/apps#implement-screen-navigation) to the media playback screen. For
other templates, a header action is another way to achieve this.