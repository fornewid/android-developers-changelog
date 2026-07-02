---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/first-activity
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/first-activity
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Augmented experiences for audio glasses and display glasses are built on the
existing Android [`Activity` framework API](https://developer.android.com/guide/components/activities/intro-activities) and [include additional
concepts](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/support-different-types#activity-lifecycle) to support the unique aspects of these glasses. Unlike XR headsets
that run a full APK on the device, audio glasses and display glasses use a
dedicated activity that runs within your phone's existing app. This activity is
projected from the host device to the glasses.

To create your app's experience for audio glasses and display glasses, you
extend your existing phone app by creating a new projected [`Activity`](https://developer.android.com/reference/kotlin/android/app/Activity). This
activity serves as the main launch entry point for your app on the glasses. This
approach simplifies development because you can share and reuse business logic
between your phone and glasses experiences.

## Version compatibility

Check the [Android SDK compatibility requirements](https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk#compatibility) for the Jetpack XR SDK.

### Dependencies

Add the following [library dependencies for audio glasses and display
glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk#augmented):

### Groovy

    dependencies {
        implementation "androidx.xr.runtime:runtime:1.0.0-alpha15"
        implementation "androidx.xr.glimmer:glimmer:1.0.0-alpha13"
        implementation "androidx.xr.glimmer:glimmer-google-fonts:1.0.0-alpha13"
        implementation "androidx.xr.projected:projected:1.0.0-alpha08"
        implementation "androidx.xr.arcore:arcore:1.0.0-alpha14"
    }

### Kotlin

    dependencies {
        implementation("androidx.xr.runtime:runtime:1.0.0-alpha15")
        implementation("androidx.xr.glimmer:glimmer:1.0.0-alpha13")
        implementation("androidx.xr.glimmer:glimmer-google-fonts:1.0.0-alpha13")
        implementation("androidx.xr.projected:projected:1.0.0-alpha08")
        implementation("androidx.xr.arcore:arcore:1.0.0-alpha14")
    }

## Declare your activity in your app's manifest

Just like other types of activities, you need to declare your activity in your
app's manifest file for the system to see and run it.

    <application>
      <activity
          android:name="com.example.xr.projected.ProjectedMainActivity"
          android:exported="true"
          android:requiredDisplayCategory="android.hardware.display.category.XR_PROJECTED"
          android:label="Example activity for audio glasses and display glasses">
          <intent-filter>
              <action android:name="android.intent.action.MAIN" />
              <category android:name="android.intent.category.XR_PROJECTED_LAUNCHER"/>
          </intent-filter>
      </activity>
    </application>

### Key points about the code

- Specifies `android.hardware.display.category.XR_PROJECTED` for the `android:requiredDisplayCategory` attribute to tell the system that this is a projected activity and can be projected onto audio and display glasses.
- `android.intent.action.MAIN` sets this activity as the default launch activity.
- `android.intent.category.XR_PROJECTED_LAUNCHER` is a specialized category
  that makes your projected activity discoverable by Gemini voice commands.

  When a user issues a voice command using the app's name (for example, "Open
  the AI catalog sample", "Launch the AI catalog sample", or "Start the AI
  catalog sample"), the system uses this category to locate and start the
  designated activity on the audio or display glasses.

> [!NOTE]
> **Note:** If multiple projected activities are defined with this category, Gemini selects the first one found in the manifest file.

## Create your activity

Next, you'll create a small activity that can display something on the AI
glasses whenever the display is turned on.


```kotlin
@OptIn(ExperimentalProjectedApi::class)
class ProjectedMainActivity : ComponentActivity() {

    private var displayController: ProjectedDisplayController? = null
    private var isVisualUiSupported by mutableStateOf(false)
    private var areVisualsOn by mutableStateOf(true)
    private var isPermissionDenied by mutableStateOf(false)

    // Register the permissions launcher using the ProjectedPermissionsResultContract.
    private val requestPermissionLauncher: ActivityResultLauncher<List<ProjectedPermissionsRequestParams>> =
        registerForActivityResult(ProjectedPermissionsResultContract()) { results ->
            if (results[Manifest.permission.CAMERA] == true) {
                isPermissionDenied = false
                initializeGlassesFeatures()
            } else {
                // Handle permission denial.
                isPermissionDenied = true
            }
        }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        lifecycle.addObserver(object : DefaultLifecycleObserver {
            override fun onDestroy(owner: LifecycleOwner) {
                displayController?.close()
                displayController = null
            }
        })

        if (hasCameraPermission()) {
            initializeGlassesFeatures()
        } else {
            requestHardwarePermissions()
        }

        setContent {
            GlimmerTheme {
                HomeScreen(
                    areVisualsOn = areVisualsOn,
                    isVisualUiSupported = isVisualUiSupported,
                    isPermissionDenied = isPermissionDenied,
                    onRetryPermission = { requestHardwarePermissions() },
                    onClose = { finish() }
                )
            }
        }
    }

    private fun initializeGlassesFeatures() {
        lifecycleScope.launch {
            // Check device capabilities
            val projectedDeviceController = ProjectedDeviceController.create(this@ProjectedMainActivity)
            isVisualUiSupported = projectedDeviceController.capabilities.contains(CAPABILITY_VISUAL_UI)

            val controller = ProjectedDisplayController.create(this@ProjectedMainActivity)
            displayController = controller
            val observer = GlassesLifecycleObserver(
                context = this@ProjectedMainActivity,
                controller = controller,
                onVisualsChanged = { visualsOn -> areVisualsOn = visualsOn }
            )
            lifecycle.addObserver(observer)
        }
    }

    private fun hasCameraPermission(): Boolean {
        return ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) ==
                PackageManager.PERMISSION_GRANTED
    }

    private fun requestHardwarePermissions() {
        val params = ProjectedPermissionsRequestParams(
            permissions = listOf(Manifest.permission.CAMERA),
            rationale = "Camera access is required to overlay digital content on your physical environment."
        )
        requestPermissionLauncher.launch(listOf(params))
    }
}
```

<br />

### Key points about the code

- Opts in to using [opt-in APIs](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresOptIn) from the [Jetpack Projected](https://developer.android.com/jetpack/androidx/releases/xr-projected) library.
- `ProjectedMainActivity` extends [`ComponentActivity`](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity), just as you would expect in mobile development.
- Because not all glasses have a display, checks whether the device has a display using [`ProjectedDeviceController`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedDeviceController).
- The `setContent` block within the `onCreate` function defines the root of the Composable UI tree for the activity. You'll implement the `HomeScreen` composable using [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer).
- Initializes the UI during the activity's [`onCreate`](https://developer.android.com/reference/kotlin/android/app/Activity#onCreate(android.os.Bundle)) method (see [projected activity lifecycle](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/support-different-types#activity-lifecycle)).
- To prepare for camera-related features that [access the glasses hardware](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context), [requests hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions) by registering a permissions launcher, defining the `hasCameraPermission` and `requestHardwarePermissions` functions, and checking whether permissions have been granted before calling `initializeGlassesFeatures`.

## Implement the composable

The activity that you created references a `HomeScreen` composable function that
you need to implement. The following code uses [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) to
define a composable that can display some text on the glasses' display:


```kotlin
@Composable
fun HomeScreen(
    areVisualsOn: Boolean,
    isVisualUiSupported: Boolean,
    isPermissionDenied: Boolean,
    onRetryPermission: () -> Unit,
    onClose: () -> Unit,
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier
            .surface()
            .focusable(false)
            .fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        if (isPermissionDenied) {
            Card(
                title = { Text("Permission Required") },
                action = { Button(onClick = onClose) { Text("Exit") } }
            ) {
                Text("Camera access is needed to use AI glasses features.")
                Button(onClick = onRetryPermission) { Text("Retry") }
            }
        } else if (isVisualUiSupported) {
            Card(
                title = { Text("Android XR") },
                action = {
                    Button(onClick = onClose) {
                        Text("Close")
                    }
                }
            ) {
                if (areVisualsOn) {
                    Text("Hello, AI Glasses!")
                } else {
                    Text("Display is off. Audio guidance active.")
                }
            }
        } else {
            Text("Audio Guidance Mode Active")
        }
    }
}
```

<br />

### Key points about the code

- As you defined in your activity earlier, the `HomeScreen` function includes the composable content that the user sees when the glasses' display is on.
- The Jetpack Compose Glimmer [`Text`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#Text(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Function1,androidx.compose.foundation.text.TextAutoSize,androidx.compose.ui.text.TextStyle)) component displays the text "Hello, AI Glasses!" to the glasses' display.
- The Jetpack Compose Glimmer `Button` closes the activity by calling `finish()` through `onClose` in the projected activity.

> [!NOTE]
> **Note:** For an example of developing for a displayless experience, see [Handle
> audio input using Automatic Speech Recognition](https://developer.android.com/develop/xr/jetpack-xr-sdk/asr) and [Handle audio input
> using Text to Speech](https://developer.android.com/develop/xr/jetpack-xr-sdk/tts).

## Check whether audio or display glasses are connected

To determine whether a user's audio or display glasses are connected to their
phone before launching your activity, use the
[`ProjectedContext.isProjectedDeviceConnected`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedContext#isProjectedDeviceConnected(android.content.Context,kotlin.coroutines.CoroutineContext)) method. This method
returns a `Flow<Boolean>` that your app can observe to get real-time updates on
the connection status.

## Start your activity

> [!WARNING]
> **Preview:** There is a known rendering issue that causes the glasses' display to briefly flash white when a projected activity starts.

Now that you've created a basic activity, you can launch it onto your glasses.
To access the glasses' hardware, your app must start your activity with specific
options that tell the system to use a [projected context](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/support-different-types#projected-context), as shown in the
following code:


```kotlin
val options = ProjectedContext.createProjectedActivityOptions(context)
val intent = Intent(context, ProjectedMainActivity::class.java)
context.startActivity(intent, options.toBundle())
```

<br />

The [`createProjectedActivityOptions`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedActivityOptions(android.content.Context)) method in [`ProjectedContext`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedContext)
generates the necessary options to start your activity in a projected context.
The `context` parameter can be a context from the phone or the glasses device.

> [!WARNING]
> **Preview:** When your app launches a projected activity, it doesn't automatically turn on the glasses' display. We're planning to add this capability in the future.

## Next steps

Now that you've created your first activity for audio glasses and display
glasses, explore other ways that you can extend its functionality:

- [Handle audio output using Text to Speech](https://developer.android.com/develop/xr/jetpack-xr-sdk/tts)
- [Handle audio input using Automatic Speech Recognition](https://developer.android.com/develop/xr/jetpack-xr-sdk/asr)
- [Build UI with Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer)
- [Access hardware on audio glasses and display glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware)