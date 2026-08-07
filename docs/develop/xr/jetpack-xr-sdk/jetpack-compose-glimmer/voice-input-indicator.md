---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/voice-input-indicator
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/voice-input-indicator
source: md.txt
---

<br />

<br />

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The [`VoiceInputIndicator`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable) is a [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) component that displays sound activity to the user. You can use this component to accept voice input or other audio and provide visual feedback to show that your app is capturing audio.

This component is strictly a visual element. It doesn't record audio or process microphone data on its own. Instead, it responds to an audio `level` provided by your app, which shows a visual representation of the audio intensity.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_voiceindicator.png) **Figure 1.** An example of the VoiceInputIndicator.

<br />

## Request projected permissions

To capture audio data to drive the indicator, your app needs the [`Manifest.permission.RECORD_AUDIO`](https://developer.android.com/reference/kotlin/android/Manifest.permission#record_audio) permission.

When you build augmented experiences for display glasses, ensure that you request permissions correctly across both the device and the glasses. Use [`ProjectedPermissionsResultContract`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedActivityCompat) and [`ProjectedPermissionsRequestParams`](https://developer.android.com/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsRequestParams) to prompt the user.

For more information about requesting permissions in projected environments, see [Request hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions).

## Capture and normalize audio

The [`VoiceInputIndicator`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable) requires a `Float` between `0.0f` and `1.0f` to visually reflect audio intensity. Because it operates purely as a visual component and doesn't capture audio, your app must actively monitor the microphone and stream the volume to the indicator's `level` parameter.

While there are multiple ways to capture audio data, one approach is to use the [`SpeechRecognizer`](https://developer.android.com/reference/kotlin/android/speech/SpeechRecognizer) API. When using [`SpeechRecognizer`](https://developer.android.com/reference/kotlin/android/speech/SpeechRecognizer), you can capture real-time volume updates using the [`RecognitionListener.onRmsChanged`](https://developer.android.com/reference/kotlin/android/speech/RecognitionListener#onRmsChanged(kotlin.Float)) callback, which provides the audio level in decibels, `rmsdB`.

Because this raw value typically falls between 0 and 10, you must normalize the output to the required `0.0f` to `1.0f` range. You can hold this normalized level in a state variable to continuously update the indicator.

> [!NOTE]
> **Note:** It's not strictly required to map the full 0 to 10 dB range to the `0.0f` to `1.0f` scale. You can set custom minimums and maximums for your dB range, mapping whatever minimum and maximum threshold you choose to the `0.0f` to `1.0f` scale.

Here's an example using a [`RecognitionListener`](https://developer.android.com/reference/kotlin/android/speech/RecognitionListener) to update a state variable:

<br />

```kotlin
// Example state variable to hold the normalized level (0.0 to 1.0)
// that the VoiceInputIndicator component expects.
val audioLevel = MutableStateFlow(0f)

// Initialize the Android SpeechRecognizer
val speechRecognizer = SpeechRecognizer.createSpeechRecognizer(context)

// Listener to capture speech events and audio level changes
val listener = object : RecognitionListener {
    override fun onRmsChanged(rmsdB: Float) {
        // Normalize raw dB level to a 0.0-1.0 range.
        // Android SpeechRecognizer's rmsdB typically ranges from 0 to ~10.
        audioLevel.value = ((rmsdB - 1f) / 9f).coerceIn(0f, 1f)
    }

    // ... Implement other required RecognitionListener methods ...
    override fun onReadyForSpeech(params: Bundle?) {}
    override fun onBeginningOfSpeech() {}
    override fun onEndOfSpeech() {}
    override fun onError(error: Int) {}
    override fun onResults(results: Bundle?) {}
    override fun onPartialResults(partialResults: Bundle?) {}
    override fun onEvent(eventType: Int, params: Bundle?) {}
    override fun onBufferReceived(buffer: ByteArray?) {}
}

// Attach the listener to the recognizer
speechRecognizer.setRecognitionListener(listener)

// Create an intent to specify the recognition model and behavior
val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
    putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
}
// Begin listening for audio input
speechRecognizer.startListening(intent)
   
```

<br />

## Integrate the voice input indicator

Once your audio stream is properly normalized and exposed as state, you can pass it directly into the [`VoiceInputIndicator`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable).

<br />

```kotlin
@Composable
fun VoiceInputExample(modifier: Modifier) {
    // Collect the flow as Compose State so the UI reacts to changes in real-time.
    val currentLevel by audioLevel.collectAsState()

    VoiceInputIndicator(
        // The VoiceInputIndicator component provides a visual "pulse" or indicator
        // that changes based on the 'level' lambda, which returns a Float between 0.0 and 1.0.
        level = { currentLevel },
        modifier = modifier
    )
}
   
```

<br />

### Customization parameters

The [`VoiceInputIndicator`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable) provides a few parameters to customize its behavior and appearance:

- `level`: A function returning a `Float` that represents the level of the voice input, ranging from `0.0` for silence to `1.0` for the loudest sound.
- `indicatorColor`: The color of the indicator bars. By default, this uses the primary color from the Glimmer theme; see [`GlimmerTheme.colors.primary`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#primary()).
- `modifier`: The standard Compose [`modifier`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier) to be applied to the indicator.

### Related components

If your UI requires the indicator to sit within a visible background container, use the [`ContainedVoiceInputIndicator`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/ContainedVoiceInputIndicator.composable). This alternative ensures that the indicator bars are transparent, allowing the background container to show through.