---
title: https://developer.android.com/media/media3/exoplayer/migration-guide
url: https://developer.android.com/media/media3/exoplayer/migration-guide
source: md.txt
---

Apps that are currently using the standalone `com.google.android.exoplayer2`
library and `androidx.media` should migrate to `androidx.media3`. Use
the [migration script](https://developer.android.com/media/media3/exoplayer/migration-guide#exoplayer) to migrate gradle build files, Java and
Kotlin source files, and XML layout files from ExoPlayer
`2.19.1` to AndroidX Media3 `1.1.1`.

## Overview

Before you migrate, review the following sections to learn more about
the benefits of the new APIs, APIs to migrate, and the prerequisites
that your app's project should meet.

### Why migrate to Jetpack Media3

- It's the **new home of ExoPlayer** , whereas `com.google.android.exoplayer2` is discontinued.
- Access the **Player API across components/processes** with `MediaBrowser`/`MediaController`.
- Use the **extended capabilities of the `MediaSession` and
  `MediaController`** API.
- Advertise playback capabilities with **fine-grained access control**.
- **Simplify your app** by removing `MediaSessionConnector` and `PlayerNotificationManager`.
- **Backwards compatible** with media-compat client APIs (`MediaBrowserCompat`/`MediaControllerCompat`/`MediaMetadataCompat`)

### Media APIs to migrate to AndroidX Media3

- [**ExoPlayer and its extensions**](https://developer.android.com/media/media3/exoplayer/migration-guide#exoplayer)   
  This includes all modules of the legacy [ExoPlayer project](https://github.com/google/ExoPlayer/) except the [mediasession](https://github.com/google/ExoPlayer/tree/release-v2/extensions/mediasession) module that is discontinued. Apps or modules depending on packages in `com.google.android.exoplayer2` can be migrated with the migration script.
- [**MediaSessionConnector**](https://developer.android.com/media/media3/exoplayer/migration-guide#MediaSessionConnector) (depending on the `androidx.media.*` packages of `androidx.media:media:1.4.3+`)   
  Remove the `MediaSessionConnector` and use the `androidx.media3.session.MediaSession` instead.
- [**MediaBrowserServiceCompat**](https://developer.android.com/media/media3/exoplayer/migration-guide#MediaBrowserService) (depending on the `androidx.media.*` packages of `androidx.media:media:1.4.3+`)   
  Migrate subclasses of [`androidx.media.MediaBrowserServiceCompat`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat) to `androidx.media3.session.MediaLibraryService` and code using `MediaBrowserCompat.MediaItem` to `androidx.media3.common.MediaItem`.
- [**MediaBrowserCompat**](https://developer.android.com/media/media3/exoplayer/migration-guide#MediaBrowser) (depending on the `android.support.v4.media.*` packages of `androidx.media:media:1.4.3+`)   
  Migrate client code using the `MediaBrowserCompat` or `MediaControllerCompat` to use the `androidx.media3.session.MediaBrowser` with `androidx.media3.common.MediaItem`.

## Prerequisites

1. **Make sure your project is under source control**

   Make sure you can easily revert changes applied by scripted migration tools.
   If you don't have your project under source control yet, now is a good time
   to start with it. If for some reason you don't want to do that, make a
   backup copy of your project before starting the migration.
2. **Update your app**

   - We recommend updating your project to use the
     **[most recent version of the ExoPlayer library](https://github.com/google/ExoPlayer/blob/release-v2/RELEASENOTES.md)** and remove any
     calls to deprecated methods. If you intend to
     [use the script](https://developer.android.com/media/media3/exoplayer/migration-guide#usingscript) for the migration, you need to match the
     version you are updating to with the version handled by the script.

   - Increase the **compileSdkVersion of your app to at least 32**.

   - **Upgrade Gradle and the Android Studio Gradle plugin** to a recent
     version that works with the updated dependencies from above. For
     instance:

     - Android Gradle Plugin version: 7.1.0
     - Gradle version: 7.4
   - **Replace all wildcard import statements** that are using an asterix
     (\*) and use fully qualified import statements: Delete the wildcard
     import statements and use Android Studio to import the fully-qualified
     statements (F2 - Alt/Enter, F2 - Alt/Enter, ...).

   - **Migrate from `com.google.android.exoplayer2.PlayerView` to
     `com.google.android.exoplayer2.StyledPlayerView`** . This is necessary
     because there's no equivalent to
     `com.google.android.exoplayer2.PlayerView` in AndroidX Media3.

## Migrate ExoPlayer with script support

The script facilitates moving from `com.google.android.exoplayer2` to the new
package and module structure under [`androidx.media3`](https://developer.android.com/jetpack/androidx/releases/media3). The script applies
some validation checks on your project and prints warnings if validation fails.
Otherwise, it applies the [mappings of renamed classes and packages](https://developer.android.com/media/media3/exoplayer/mappings) in the
resources of an Android gradle project written in Java or Kotlin.

    usage: ./media3-migration.sh [-p|-c|-d|-v]|[-m|-l [-x <path>] [-f] PROJECT_ROOT]
     PROJECT_ROOT: path to your project root (location of 'gradlew')
     -p: list package mappings and then exit
     -c: list class mappings (precedence over package mappings) and then exit
     -d: list dependency mappings and then exit
     -l: list files that will be considered for rewrite and then exit
     -x: exclude the path from the list of file to be changed: 'app/src/test'
     -m: migrate packages, classes and dependencies to AndroidX Media3
     -f: force the action even when validation fails
     -v: print the exoplayer2/media3 version strings of this script
     -h, --help: show this help text

### Using the migration script

| **Warning:** The script may put gradle build files in an unusable state if your dependency declarations use variables or advanced techniques.

1. Download [the migration script](https://raw.githubusercontent.com/google/ExoPlayer/refs/heads/release-v2/media3-migration.sh) from the tag of the ExoPlayer project on
   GitHub corresponding to the version that you have updated your app to:

       curl -o media3-migration.sh \
         "https://raw.githubusercontent.com/google/ExoPlayer/r2.19.1/media3-migration.sh"

2. Make the script executable:

       chmod 744 media3-migration.sh

3. Run the script with `--help` to learn about options.

4. Run the script with `-l` to list the set of files that are selected for
   migration (use `-f` to force the listing without warnings):

       ./media3-migration.sh -l -f /path/to/gradle/project/root

5. Run the script with `-m` to map packages, classes, and modules to Media3.
   Running the script with the `-m` option will apply changes to the selected
   files.

   - Stop at validation error without making changes

       ./media3-migration.sh -m /path/to/gradle/project/root

   - Forced execution

   If the script finds a violation of the prerequisites, the migration can be
   forced with the `-f` flag:

       ./media3-migration.sh -m -f /path/to/gradle/project/root

| **Note:** You can use the `-x` parameter to exclude a path from being selected for change.

     # list files selected for migration when excluding paths
     ./media3-migration.sh -l -x "app/src/test/" -x "service/" /path/to/project/root
     # migrate the selected files
     ./media3-migration.sh -m -x "app/src/test/" -x "service/" /path/to/project/root

Complete these manual steps after running the script with the `-m` option:

1. **Check how the script changed your code** : Use a diff tool and fix potential issues (consider filing [a bug](https://github.com/androidx/media/issues/new?assignees&labels=bug,needs+triage&template=bug.yml) if you think the script has a general problem that was introduced without passing the `-f` option).
2. **Build the project** : Either use `./gradlew clean build` or in Android Studio choose **File \> Sync Project with Gradle Files** , then **Build \>
   Clean project** , and then **Build \> Rebuild project** (monitor your build in the ['Build - Build Output' tab of Android Studio](https://developer.android.com/studio/run#gradle-console)).

| **Note:** In some cases, the script is expected to leave your project in a state that doesn't build without manually migrating code. The script warns about this and requests the `-f` option to force execution. For instance, this is the case if an app is using `MediaSessionConnector` and `MediaSessionCompat`. See the next section for guidance on how you can migrate from `MediaSessionConnector` to Media3.

Recommended follow-up steps:

1. Resolve [**opt-in for errors regarding usage of unstable APIs**](https://developer.android.com/media/media3/exoplayer/migration-guide#unstableapi).
2. **Replace deprecated API calls**: Use the suggested replacement API. Hold the pointer over the warning in Android Studio, and consult the JavaDoc of the deprecated symbol to find out what to use instead of a given call.
3. **Sort the import statements** : Open the project in Android Studio, then right-click on a package folder node in the project viewer and choose **Optimize imports** on the packages that contain the changed source files.

## Replace `MediaSessionConnector` with `androidx.media3.session.MediaSession`

In the legacy `MediaSessionCompat` world, the `MediaSessionConnector` was
responsible for syncing the state of the player with the state of the session
and receiving commands from controllers that needed delegation to appropriate
player methods. With AndroidX Media3, this is done by the `MediaSession` directly
without requiring a connector.

1. **Remove all references and usage of MediaSessionConnector:** If you used
   the automated script to migrate ExoPlayer classes and packages, then the
   script likely has left your code in an uncompilable state regarding
   the`MediaSessionConnector` that can't be resolved. Android Studio will
   show you the broken code when you try to build or start the app.

2. In the `build.gradle` file where you maintain your dependencies, add **an
   implementation dependency to the AndroidX Media3 session module** and remove
   the legacy dependency:

       implementation "androidx.media3:media3-session:1.9.2"

3. Replace the `MediaSessionCompat` with
   **`androidx.media3.session.MediaSession`**.

4. At the code site where you have created the legacy `MediaSessionCompat`, use
   `androidx.media3.session.MediaSession.Builder` to **build a
   `MediaSession`** . **Pass the player** to construct the session builder.

   | **Note:** In case your app is using a different player than `ExoPlayer`, you need a custom `Player` implementation that you can pass to the `MediaSession` that is wrapping your player. We will provide more guidance around a minimal `Player` implementation that works together with the media session implementation.

       val player = ExoPlayer.Builder(context).build()
       mediaSession = MediaSession.Builder(context, player)
           .setSessionCallback(MySessionCallback())
           .build()

   | **Note:** You can intercept any playback operation on a `Player` by wrapping it in a `ForwardingSimpleBasePlayer(player)`. See [more information about
   | `ForwardingSimpleBasePlayer`](https://developer.android.com/media/media3/exoplayer/customization#player-operations).
5. Implement `MySessionCallback` as required by your app. This is optional. If
   you want to allow controllers to add media items to the player, implement
   [`MediaSession.Callback.onAddMediaItems()`](https://github.com/androidx/media/blob/1.9.2/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L184). It serves various current and
   legacy API methods that add media items to the player for playback in a
   backwards compatible way. This includes the
   `MediaController.set/addMediaItems()` methods of the Media3 controller, as
   well as the `TransportControls.prepareFrom*/playFrom*`
   methods of the legacy API. A sample implementation of `onAddMediaItems` can
   be found [in the `PlaybackService` of the session demo app](https://github.com/androidx/media/blob/1.9.2/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L184).

6. Release the media session at the code site where you destroyed your session
   before the migration:

       mediaSession?.run {
         player.release()
         release()
         mediaSession = null
       }

   | **Note:** It's important to release the media session before creating a new one with the same ID. Media3 throws an exception if an app is leaking a session instance.

### `MediaSessionConnector` functionality in Media3

The following table shows the Media3 APIs that handle functionality
previously implemented in `MediaSessionConnector`.

| MediaSessionConnector | AndroidX Media3 |
|---|---|
| `CustomActionProvider` | `MediaSession.Callback.onCustomCommand()/ MediaSession.setMediaButtonPreferences()` |
| `PlaybackPreparer` | `MediaSession.Callback.onAddMediaItems()` (`prepare()` is called internally) |
| `QueueNavigator` | `ForwardingSimpleBasePlayer` |
| `QueueEditor` | `MediaSession.Callback.onAddMediaItems()` |
| `RatingCallback` | `MediaSession.Callback.onSetRating()` |
| `PlayerNotificationManager` | `DefaultMediaNotificationProvider/ MediaNotification.Provider` |

## Migrate `MediaBrowserService` to `MediaLibraryService`

AndroidX Media3 introduces `MediaLibraryService` that replaces the
`MediaBrowserServiceCompat`. The JavaDoc of `MediaLibraryService` and its super
class `MediaSessionService` provide a good intro into the API and the
asynchronous programming model of the service.

The `MediaLibraryService` is backwards compatible with the
`MediaBrowserService`. A client app that is using `MediaBrowserCompat` or
`MediaControllerCompat`, continues to work without code changes when connecting
to a `MediaLibraryService`. For a client, it is transparent whether your app is
using a `MediaLibraryService` or a legacy `MediaBrowserServiceCompat`.
![App component diagram with service, activity and external apps.](https://developer.android.com/static/media/images/overview.png) **Figure 1**: Media app component overview

1. For backwards compatibility to work, you need to **register both service
   interfaces** with your service in the `AndroidManifest.xml`. This way a
   client finds your service by the required service interface:

       <service android:name=".MusicService" android:exported="true">
           <intent-filter>
               <action android:name="androidx.media3.session.MediaLibraryService"/>
               <action android:name="android.media.browse.MediaBrowserService" />
           </intent-filter>
       </service>

2. In the `build.gradle` file where you maintain your dependencies, add **an
   implementation dependency to the [AndroidX Media3 session module](https://github.com/androidx/media/tree/release/libraries/session)** and
   remove the legacy dependency:

       implementation "androidx.media3:media3-session:1.9.2"

3. **Change your service to inherit from a `MediaLibraryService`** instead of
   `MediaBrowserService`
   As said earlier, the `MediaLibraryService` is compatible with the legacy
   `MediaBrowserService`. Accordingly, the broader API that the service is
   offering to clients is still the same. So it's likely that an app can keep
   most of the logic that is required to implement the `MediaBrowserService`
   and adapt it for the new `MediaLibraryService`.

   The main differences compared to the legacy
   `MediaBrowserServiceCompat` are as follows:
   - **Implement the service life-cycle methods:** The methods that need to
     be overridden on the service itself are `onCreate/onDestroy`, where an
     app allocates/releases the library session, the player, and other
     resources. In addition to standard service life-cycle methods, an app
     needs to override `onGetSession(MediaSession.ControllerInfo)` to return
     the `MediaLibrarySession` that was built in `onCreate`.

   - **Implement MediaLibraryService.MediaLibrarySessionCallback:** Building
     a session requires a
     [`MediaLibraryService.MediaLibrarySessionCallback`](https://github.com/androidx/media/blob/1.9.2/libraries/session/src/main/java/androidx/media3/session/MediaLibraryService.java#L127) that implements
     the actual domain API methods. So instead of overriding API methods of
     the legacy service, you will override the methods of the
     `MediaLibrarySession.Callback` instead.

     The callback is then used to build the `MediaLibrarySession`:

         mediaLibrarySession =
               MediaLibrarySession.Builder(this, player, MySessionCallback())
                  .build()

     Find the [full API of the MediaLibrarySessionCallback](https://github.com/androidx/media/blob/1.9.2/libraries/session/src/main/java/androidx/media3/session/MediaLibraryService.java#L127) in the API
     documentation.
   - **Implement [`MediaSession.Callback.onAddMediaItems()`](https://github.com/androidx/media/blob/1.9.2/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L184)** : The callback
     `onAddMediaItems(MediaSession, ControllerInfo, List<MediaItem>)` serves
     various current and legacy API methods that add media items to the player
     for playback in a backwards compatible way. This includes the
     `MediaController.set/addMediaItems()` methods of the Media3 controller,
     as well as the `TransportControls.prepareFrom*/playFrom*`
     methods of the legacy API. A sample implementation of the callback can
     be found [in the `PlaybackService` of the session demo app](https://github.com/androidx/media/blob/1.9.2/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L184).

   - AndroidX Media3 is using **`androidx.media3.common.MediaItem`** instead
     of [MediaBrowserCompat.MediaItem](https://developer.android.com/reference/kotlin/android/support/v4/media/MediaBrowserCompat.MediaItem) and [MediaMetadataCompat](https://developer.android.com/reference/kotlin/android/support/v4/media/MediaMetadataCompat). Parts
     of your code tied to the legacy classes need to be changed accordingly
     or map to the Media3 `MediaItem` instead.

   - The general **asynchronous programming model changed to `Futures`** in
     contrast to the detachable `Result` approach of the
     `MediaBrowserServiceCompat`. Your service implementation can return an
     asynchronous [`ListenableFuture`](https://guava.dev/releases/21.0/api/docs/com/google/common/util/concurrent/ListenableFuture.html) instead of detaching a result or
     [return an immediate Future to directly return a value](https://github.com/androidx/media/blob/1.9.2/demos/session/src/main/java/androidx/media3/demo/session/PlaybackService.kt#L136).

### Remove PlayerNotificationManager

The **`MediaLibraryService` supports media notifications automatically** and the
`PlayerNotificationManager` can be removed when using a `MediaLibraryService` or
`MediaSessionService`.
| **Note:** Apps targeting API Level 28+ still need to request the [`FOREGROUND_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE) permission.

An app can **customize the notification** by setting a custom
`MediaNotification.Provider` in `onCreate()` that replaces the
`DefaultMediaNotificationProvider`. The `MediaLibraryService` then takes care of
starting the service in the foreground as required.

By overriding `MediaLibraryService.updateNotification()` an app can further take
full ownership of posting a notification and starting/stopping the service in
the foreground as required.

## Migrate client code using a MediaBrowser

With AndroidX Media3, a `MediaBrowser` implements the `MediaController/Player`
interfaces and can be used to control media playback besides browsing the media
library. If you had to create a `MediaBrowserCompat` and a
`MediaControllerCompat` in the legacy world, you can do the same by only using
the `MediaBrowser` in Media3.
| **Note:** Kotlin users can depend on [kotlin-coroutines-guava](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-guava/index.html) or [androidx.concurrent](https://developer.android.com/jetpack/androidx/releases/concurrent) in the `build.gradle` file to add the extension method `await` to the `ListenableFuture`. That makes the `MediaBrowser` API fit more naturally into a `suspend` method.

A `MediaBrowser` can be built and await for the connection to the
service being established:

    scope.launch {
        val sessionToken =
            SessionToken(context, ComponentName(context, MusicService::class.java)
        browser =
            MediaBrowser.Builder(context, sessionToken))
                .setListener(BrowserListener())
                .buildAsync()
                .await()
        // Get the library root to start browsing the library.
        root = browser.getLibraryRoot(/* params= */ null).await();
        // Add a MediaController.Listener to listen to player state events.
        browser.addListener(playerListener)
        playerView.setPlayer(browser)
    }

Take a look into
[*Control playback in the media session*](https://developer.android.com/media/media3/exoplayer/playing-in-background#controlling-playback)
to learn how to create a `MediaController` for controlling playback in the
background.

## Further steps and clean up

### Unstable API errors

After migrating to Media3, you may see lint errors about unstable API usages.
These APIs are safe to use and the lint errors are a by-product of our new
binary compatibility guarantees. If you don't require strict binary
compatibility, these errors can be safely suppressed with an `@OptIn`
annotation.

#### Background

Neither ExoPlayer v1 or v2 provided strict guarantees about binary compatibility
of the library between subsequent versions. The ExoPlayer API surface is very
large by design, in order to allow apps to customize nearly every aspect of
playback. Subsequent versions of ExoPlayer would occasionally introduce symbol
renames or other breaking changes (e.g. new required methods on interfaces). In
most cases these breakages were mitigated by introducing the new symbol
alongside deprecating the old symbol for a few versions, to allow developers
time to migrate their usages, but this wasn't always possible.

These breaking changes resulted in two problems for users of the ExoPlayer v1
and v2 libraries:

1. An upgrade from to the ExoPlayer version could cause code to stop compiling.
2. An app that depended on ExoPlayer both directly and via an intermediate library had to ensure that both dependencies were the same version, otherwise binary incompatibilities could result in runtime crashes.

#### Improvements in Media3

Media3 guarantees binary compatibility for a subset of the API surface. The
parts that **don't** guarantee binary compatibility are marked with
[`@UnstableApi`](https://developer.android.com/reference/androidx/media3/common/util/UnstableApi). In order to make this distinction clear, usages of unstable
API symbols generate a lint error unless they are annotated with `@OptIn`.

After migrating from ExoPlayer v2 to Media3, you may see a lot of unstable API
lint errors. This may make it seem like Media3 is 'less stable' than ExoPlayer
v2. This is not the case. The 'unstable' parts of the Media3 API have the same
level of stability as the **whole** of the ExoPlayer v2 API surface, and the
guarantees of the stable Media3 API surface are not available in ExoPlayer v2 at
all. The difference is simply that a lint error now alerts you to the different
levels of stability.

#### Handle unstable API lint errors

See [the troubleshooting section on these lint errors](https://developer.android.com/media/media3/exoplayer/troubleshooting#unstable-api-lint-errors) for details on how to
annotate Java and Kotlin usages of unstable APIs with `@OptIn`.

### Deprecated APIs

You may notice that calls to deprecated APIs are struck-through in Android
Studio. We recommend replacing such calls with the appropriate alternative.
Hover over the symbol to see the JavaDoc that tells which API to use instead.
![Screenshot: How to display JavaDoc with alternative of deprecated method](https://developer.android.com/static/media/media3/exoplayer/images/deprecation.png) **Figure 3**: JavaDoc tooltip in Android Studio suggests an alternative for any deprecated symbol.

## Code samples and demo apps

- [AndroidX Media3 session demo app](https://github.com/androidx/media/tree/release/demos/session) (mobile and WearOS)
  - Custom actions
  - System UI notification, MediaButton/BT
  - Google Assistant playback control
- [UAMP: Android Media Player (branch media3)](https://github.com/android/uamp/tree/media3) (mobile, AutomotiveOS)
  - System UI notification, MediaButton/BT, Playback resumption
  - Google Assistant/WearOS playback control
  - AutomotiveOS: custom command and sign-in