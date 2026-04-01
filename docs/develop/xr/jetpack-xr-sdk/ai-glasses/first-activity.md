---
title: Create your first activity for AI glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/first-activity
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Create your first activity for AI glasses Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

The AI glasses experience is built on the existing Android [`Activity` framework
API](/guide/components/activities/intro-activities) and [includes additional concepts](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types#activity-lifecycle) to support the unique aspects of
AI glasses. Unlike XR headsets that run a full APK on the device, AI glasses use
a dedicated activity that runs within your phone's existing app. This activity
is projected from the host device to the AI glasses.

To create your app's AI glasses experience, you extend your existing phone app
by creating a new projected [`Activity`](/reference/kotlin/android/app/Activity) for AI glasses. This activity serves
as the main launch entry point for your app on AI glasses. This approach
simplifies development because you can share and reuse business logic between
your phone and AI glasses experiences.

## Version compatibility

Check the [Android SDK compatibility requirements](/develop/xr/jetpack-xr-sdk/set-up-sdk#compatibility) for the Jetpack XR SDK.

### Dependencies

Add the following [library dependencies for AI glasses](/develop/xr/jetpack-xr-sdk/set-up-sdk#augmented):

### Groovy

```
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-alpha12"
    implementation "androidx.xr.glimmer:glimmer:1.0.0-alpha08"
    implementation "androidx.xr.projected:projected:1.0.0-alpha05"
    implementation "androidx.xr.arcore:arcore:1.0.0-alpha11"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-alpha12")
    implementation("androidx.xr.glimmer:glimmer:1.0.0-alpha08")
    implementation("androidx.xr.projected:projected:1.0.0-alpha05")
    implementation("androidx.xr.arcore:arcore:1.0.0-alpha11")
}
```

## Declare your activity in your app's manifest

Just like other types of activities, you need to declare your activity in your
app's manifest file for the system to see and run it.

```
<application>
  <activity
      android:name="com.example.xr.projected.GlassesMainActivity"
      android:exported="true"
      android:requiredDisplayCategory="xr_projected"
      android:label="Example AI Glasses activity">
      <intent-filter>
          <action android:name="android.intent.action.MAIN" />
      </intent-filter>
  </activity>
</application>
```

### Key points about the code

* Specifies `xr_projected` for the `android:requiredDisplayCategory` attribute
  to tell the system that this activity should use a [projected context](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types#projected-context) to
  access hardware from a connected device.

## Create your activity

Next, you'll create a small activity that can display something on the AI
glasses whenever the display is turned on.

```
@OptIn(ExperimentalProjectedApi::class)
class GlassesMainActivity : ComponentActivity() {

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
            val projectedDeviceController = ProjectedDeviceController.create(this@GlassesMainActivity)
            isVisualUiSupported = projectedDeviceController.capabilities.contains(CAPABILITY_VISUAL_UI)

            val controller = ProjectedDisplayController.create(this@GlassesMainActivity)
            displayController = controller
            val observer = GlassesLifecycleObserver(
                context = this@GlassesMainActivity,
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

GlassesMainActivity.kt
```

### Key points about the code

* Opts in to using [opt-in APIs](/reference/kotlin/androidx/annotation/RequiresOptIn) from the [Jetpack Projected](/jetpack/androidx/releases/xr-projected)
  library.
* `GlassesMainActivity` extends [`ComponentActivity`](/reference/kotlin/androidx/activity/ComponentActivity), just as you would
  expect in mobile development.
* Because not all AI glasses have a display, checks whether the device has a
  display using [`ProjectedDeviceController`](/reference/kotlin/androidx/xr/projected/ProjectedDeviceController).
* The `setContent` block within the `onCreate` function defines the root of
  the Composable UI tree for the activity. You'll implement the `HomeScreen`
  composable using [Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer).
* Initializes the UI during the activity's [`onCreate`](/reference/kotlin/android/app/Activity#onCreate(android.os.Bundle)) method (see
  [projected activity lifecycle](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types#activity-lifecycle)).
* To prepare for camera-related features that
  [access the glasses hardware](/develop/xr/jetpack-xr-sdk/access-hardware-projected-context), [requests hardware permissions](/develop/xr/jetpack-xr-sdk/request-hardware-permissions) by
  registering a permissions launcher, defining the `hasCameraPermission` and
  `requestHardwarePermissions` functions, and checking whether permissions
  have been granted before calling `initializeGlassesFeatures`.

## Implement the composable

The activity that you created references a `HomeScreen` composable function that
you need to implement. The following code uses [Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) to
define a composable that can display some text on the AI glasses' display:

```
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
            .surface(focusable = false)
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

GlassesMainActivity.kt
```

### Key points about the code

* As you defined in your activity earlier, the `HomeScreen` function includes
  the composable content that the user sees when the AI glasses' display is
  on.
* The Jetpack Compose Glimmer [`Text`](/reference/kotlin/androidx/xr/glimmer/package-summary#Text(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Function1,androidx.compose.foundation.text.TextAutoSize,androidx.compose.ui.text.TextStyle)) component displays the text "Hello,
  AI Glasses!" to the glasses' display.
* The Jetpack Compose Glimmer `Button` closes the activity by calling
  `finish()` through `onClose` in the AI glasses activity.

**Note:** For an example of developing for a displayless experience, see [Handle
audio input using Automatic Speech Recognition](/develop/xr/jetpack-xr-sdk/asr) and [Handle audio input
using Text to Speech](/develop/xr/jetpack-xr-sdk/tts).

## Check whether AI glasses are connected

To determine whether a user's AI glasses are connected to their phone before
launching your activity, use the
[`ProjectedContext.isProjectedDeviceConnected`](/reference/kotlin/androidx/xr/projected/ProjectedContext#isProjectedDeviceConnected(android.content.Context,kotlin.coroutines.CoroutineContext)) method. This method
returns a `Flow<Boolean>` that your app can observe to get real-time updates on
the connection status.

## Start your activity

**Preview:** There is a known rendering issue that causes the AI glasses' display to
briefly flash white when a projected activity starts.

Now that you've created a basic activity, you can launch it onto your glasses.
To access the glasses' hardware, your app must start your activity with specific
options that tell the system to use a [projected context](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types#projected-context), as shown in the
following code:

```
val options = ProjectedContext.createProjectedActivityOptions(context)
val intent = Intent(context, GlassesMainActivity::class.java)
context.startActivity(intent, options.toBundle())

PhoneMainActivity.kt
```

The [`createProjectedActivityOptions`](/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedActivityOptions(android.content.Context)) method in [`ProjectedContext`](/reference/kotlin/androidx/xr/projected/ProjectedContext)
generates the necessary options to start your activity in a projected context.
The `context` parameter can be a context from the phone or the glasses device.

**Preview:** When your app launches a projected activity, it doesn't automatically
turn on the AI glasses' display. We're planning to add this capability in the
future.

## Next steps

Now that you've created your first activity for AI glasses, explore other ways
that you can extend its functionality:

* [Handle audio output using Text to Speech](/develop/xr/jetpack-xr-sdk/tts)
* [Handle audio input using Automatic Speech Recognition](/develop/xr/jetpack-xr-sdk/asr)
* [Build UI with Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer)
* [Access AI glasses' hardware](/develop/xr/jetpack-xr-sdk/access-hardware)

[Previous

arrow\_back

Overview](/develop/xr/jetpack-xr-sdk/ai-glasses/build)

[Next

Plan to support different types of AI glasses

arrow\_forward](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types)