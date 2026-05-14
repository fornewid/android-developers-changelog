---
title: https://developer.android.com/develop/ui/views/pip-jetpack
url: https://developer.android.com/develop/ui/views/pip-jetpack
source: md.txt
---

The [Picture-in-Picture (PiP) Jetpack Library](https://developer.android.com/jetpack/androidx/releases/core#core-pip-1.0.0-alpha) offers a streamlined and
robust solution for Android app developers to implement PiP functionality,
particularly for media playback, video communication, and navigation apps. By
providing a unified API, the library helps eliminate boilerplate code, common
in-app bugs, and improve the overall quality of the PiP user experience.

The PiP Jetpack library facilitates the existing PiP APIs by addressing several
key challenges and inconsistencies across the Android ecosystem:

- **OS fragmentation** : The library automatically handles differences in PiP API calls across various Android versions, such as using [`enterPictureInPictureMode`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) before Android 12 and [`isAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams#isAutoEnterEnabled()) after, so developers don't need to manage version differences.
- **Incorrect PiP parameters** : It provides a unified solution for correctly setting PiP parameters, for example [`setSourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect)), to create smooth and high-quality animations during media playback.
- **Unified PiP state callbacks** : It consolidates [`onPictureInPictureModeChanged`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureModeChanged(boolean,%20android.content.res.Configuration)) and [`onPictureInPictureUiStateChanged`](https://developer.android.com/reference/android/app/Activity#onPictureInPictureUiStateChanged(android.app.PictureInPictureUiState)) into a single, unified callback interface (`PictureInPictureDelegate.OnPictureInPictureEventListener`) for simplified state and UI management.
- **Boilerplate code reduction** : The library reduces the amount of repetitive, boilerplate code by offering predefined sets of `RemoteActions` for common use cases, such as playback controls and video call actions.
- **Future-proofing**: Further PiP features are delivered through the Jetpack library, allowing adopters to access additional functionality with minimal to no effort.

## Migration Workflow

Identify the app's use case category and legacy PiP logic:

**Categories:**
Video Playback, Navigation, or Video Call.

**Legacy PiP Logic to Identify:**

- `onUserLeaveHint`
- `setAutoEnterEnabled`
- `onPictureInPictureModeChanged`
- `onPictureInPictureUiStateChanged`
- `setPictureInPictureParams`.

### 2. AndroidManifest Configuration

Ensure the Activity entering PiP declares support in `AndroidManifest.xml` with
the necessary `configChanges` to prevent unnecessary restarts:

    <activity
    android:name="VideoActivity" android:supportsPictureInPicture="true"
    android:configChanges="screenSize|smallestScreenSize|screenLayout|orientation">
    </activity>

### 3. Environment Setup

Add the required dependencies to `build.gradle`:

    dependencies {
    implementation("androidx.core:core:1.18.0")
    implementation("androidx.activity:activity:1.13.0")
    implementation("androidx.core:core-pip:1.0.0-alpha02") }

Use the latest AndroidX libraries for the dependencies and refer to the
[releases](https://developer.android.com/jetpack/androidx/releases/core) page for that info.

### 4. Template Selection and Initialization

Choose the implementation template that best fits the app's use case:

- **Navigation and video call** : `BasicPictureInPicture`; seamless resize isn't typically supported, and you don't need a source rect hint.
- **Video playback** : `VideoPlaybackPictureInPicture`; automatically tracks player view bounds for the source rect hint and enables seamless resize by default.

In order to adopt the Jetpack Library, replace your existing custom PiP
implementation with the Jetpack Library APIs. The complexity and cost of
adoption will vary based on the app's current implementation.

The following sections describe some of the typical use cases of PiP and the
necessary implementation steps:

### Navigation

The app informs the library of the navigation's active or inactive state and
sets the aspect ratio. The Jetpack library handles the rest.

**Key differences:**

1. No need to differentiate auto-enter and legacy-enter on app side.
2. Consolidated callback interfaces.
3. New `PictureInPictureParams` builder for backward compatibility.

### Video Call

The app informs the library of the call's active or inactive state and sets the
aspect ratio.

**Key differences:**

1. No need to differentiate auto-enter and legacy-enter on app side.
2. Consolidated callback interfaces.
3. New `PictureInPictureParams` builder for backward compatibility.
4. Standardized action icons for video call.

### 5. Code Migration

- **Entry Logic:** Replace API-specific logic such as `setAutoEnterEnabled` for Android 12 and higher, or `onUserLeaveHint` for Android 11 and lower with [`setEnabled`](https://developer.android.com/reference/androidx/core/pip/BasicPictureInPicture#setEnabled(kotlin.Boolean)). Trigger this whenever the PiP eligibility status changes.
- **Callbacks:** Consolidate `onPictureInPictureModeChanged` (layout toggling) and `onPictureInPictureUiStateChanged` (animation/states) into a unified event-based callback `onPictureInPictureEvent`.
- **Actions \& Params:** Update parameters using [`setActions`](https://developer.android.com/reference/androidx/core/app/PictureInPictureParamsCompat.Builder#setActions(kotlin.collections.List)) and [`setAspectRatio`](https://developer.android.com/reference/androidx/core/app/PictureInPictureParamsCompat.Builder#setAspectRatio(android.util.Rational)) on the template instance whenever they change.
- **Video Special Handling:** For video apps, use [`setPlayerView`](https://developer.android.com/reference/androidx/core/pip/VideoPlaybackPictureInPicture#setPlayerView(android.view.View)) to automate source rect hint updates and ensure smooth transitions. \` ### 6. Cleanup

For [`VideoPlaybackPictureInPicture`](https://developer.android.com/reference/androidx/core/pip/VideoPlaybackPictureInPicture), call [`close`](https://developer.android.com/reference/androidx/core/pip/VideoPlaybackPictureInPicture#close()) in
[`onDispose`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/DisposableEffectScope#onDispose(kotlin.Function0)) or [`onDestroy`](https://developer.android.com/reference/android/app/Activity#onDestroy()) to release resources like view trackers.

## Reference Implementation Patterns

Examples of implementations.

### Navigation and Video Call


```kotlin
class NavOrVideoCallJpipActivity : ComponentActivity(), PictureInPictureDelegate.OnPictureInPictureEventListener {
    private lateinit var pictureInPictureImpl: BasicPictureInPicture
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        pictureInPictureImpl = BasicPictureInPicture(this)
        // BasicPictureInPicture is ideal for Navigation and Video call use cases.
        pictureInPictureImpl.addOnPictureInPictureEventListener(
            ContextCompat.getMainExecutor(this),
            this
        )
        setContent {
        }
    }
    override fun onPictureInPictureEvent(
        event: PictureInPictureDelegate.Event,
        config: Configuration?
    ) {
        when (event) {
            PictureInPictureDelegate.Event.ENTERED -> { /* Toggle to PiP layout */ }
            PictureInPictureDelegate.Event.EXITED -> { /* Toggle to Full-screen layout */ }
            PictureInPictureDelegate.Event.STASHED -> { /* Optional: PiP is stashed */ }
            PictureInPictureDelegate.Event.UNSTASHED -> { /* Optional: PiP is unstashed */ }
        }
    }
}
```

<br />

### Video Playback


```kotlin
class VideoPlaybackJpipActivity : ComponentActivity(), PictureInPictureDelegate.OnPictureInPictureEventListener {
    private lateinit var pictureInPictureImpl: VideoPlaybackPictureInPicture
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        pictureInPictureImpl = VideoPlaybackPictureInPicture(this)
        pictureInPictureImpl.addOnPictureInPictureEventListener(
            ContextCompat.getMainExecutor(this),
            this
        )
        setContent {
            ContentScreen(pictureInPictureImpl)
        }
    }
    override fun onPictureInPictureEvent(
        event: PictureInPictureDelegate.Event,
        config: Configuration?
    ) {
        when (event) {
            PictureInPictureDelegate.Event.ENTER_ANIMATION_START -> { /* Hide overlays */ }
            PictureInPictureDelegate.Event.ENTER_ANIMATION_END -> { /* Animation finished */ }
            PictureInPictureDelegate.Event.ENTERED -> { /* Switch to PiP layout */ }
            PictureInPictureDelegate.Event.STASHED -> { /* PiP stashed */ }
            PictureInPictureDelegate.Event.UNSTASHED -> { /* PiP unstashed */ }
            PictureInPictureDelegate.Event.EXITED -> { /* Return to full-screen */ }
        }
    }

    @Composable
    fun ContentScreen(pipController: VideoPlaybackPictureInPicture) {
        DisposableEffect(pipController) {
            onDispose {
                pipController.close()
            }
        }
    }
}
```

<br />