---
title: Voice input indicator in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/voice-input-indicator
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Voice input indicator in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Display Glasses

[Learn about XR device types →](/develop/xr/devices)

The [`VoiceInputIndicator`](/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable) is a [Jetpack Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) component that
displays sound activity to the user. You can use this component to accept voice
input or other audio and provide visual feedback to show that your app is
capturing audio.

This component is strictly a visual element. It doesn't record audio or process
microphone data on its own. Instead, it responds to an audio `level` provided
by your app, which shows a visual representation of the audio intensity.
![](/static/images/design/ui/glasses/guides/glasses_components_voiceindicator.png)


**Figure 1.** An example of the VoiceInputIndicator.

## Request projected permissions

To capture audio data to drive the indicator, your app needs the
[`Manifest.permission.RECORD_AUDIO`](/reference/kotlin/android/Manifest.permission#record_audio) permission.

When you build augmented experiences for display glasses, ensure that you
request permissions correctly across both the device and the glasses. Use
[`ProjectedPermissionsResultContract`](/reference/kotlin/androidx/xr/projected/ProjectedActivityCompat) and
[`ProjectedPermissionsRequestParams`](/reference/kotlin/androidx/xr/projected/permissions/ProjectedPermissionsRequestParams) to prompt the user.

For more information about requesting permissions in projected environments,
see [Request hardware permissions](/develop/xr/jetpack-xr-sdk/request-hardware-permissions).

## Capture and normalize audio

The [`VoiceInputIndicator`](/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable) requires a `Float` between `0.0f` and `1.0f` to
visually reflect audio intensity. Because it operates purely as a visual
component and doesn't capture audio, your app must actively monitor the
microphone and stream the volume to the indicator's `level` parameter.

While there are multiple ways to capture audio data, one approach is to
use the [`SpeechRecognizer`](/reference/kotlin/android/speech/SpeechRecognizer) API. When using [`SpeechRecognizer`](/reference/kotlin/android/speech/SpeechRecognizer), you
can capture real-time volume updates using the
[`RecognitionListener.onRmsChanged`](/reference/kotlin/android/speech/RecognitionListener#onRmsChanged(kotlin.Float)) callback, which provides the audio
level in decibels, `rmsdB`.

Because this raw value typically falls between 0 and 10, you must normalize the
output to the required `0.0f` to `1.0f` range. You can hold this normalized
level in a state variable to continuously update the indicator.

**Note:** It's not strictly required to map the full 0 to 10 dB range to the `0.0f`
to `1.0f` scale. You can set custom minimums and maximums for your dB
range, mapping whatever minimum and maximum threshold you choose to the `0.0f`
to `1.0f` scale.

Here's an example using a [`RecognitionListener`](/reference/kotlin/android/speech/RecognitionListener) to update a state
variable:

```
// Example state variables to hold the normalized level
val audioLevel = MutableStateFlow(0f)
val speechRecognizer = SpeechRecognizer.createSpeechRecognizer(context)

val listener = object : RecognitionListener {
    override fun onRmsChanged(rmsdB: Float) {
        // Normalize raw dB (~0–10) to 0.0-1.0 for the indicator
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

// Attach the listener and start recognizing speech
speechRecognizer.setRecognitionListener(listener)

val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
    putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
}
speechRecognizer.startListening(intent)

VoiceInputIndicatorSample.kt
```

## Integrate the voice input indicator

Once your audio stream is properly normalized and exposed as state, you can pass
it directly into the [`VoiceInputIndicator`](/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable).

```
@Composable
fun VoiceInputExample() {
    // Collect the flow as Compose State so the UI reacts to changes
    val currentLevel by audioLevel.collectAsState()

    VoiceInputIndicator(
        // The component responds to the level provided, showing a visual representation of the audio intensity
        level = { currentLevel },
        modifier = Modifier.size(64.dp)
    )
}

VoiceInputIndicatorSample.kt
```

### Customization parameters

The [`VoiceInputIndicator`](/reference/kotlin/androidx/xr/glimmer/VoiceInputIndicator.composable) provides a few parameters to customize its
behavior and appearance:

* `level`: A function returning a `Float` that represents the level of the voice
  input, ranging from `0.0` for silence to `1.0` for the loudest sound.
* `indicatorColor`: The color of the indicator bars. By default, this uses
  the primary color from the Glimmer theme; see
  [`GlimmerTheme.colors.primary`](/reference/kotlin/androidx/xr/glimmer/Colors#primary()).
* `modifier`: The standard Compose [`modifier`](/reference/kotlin/androidx/compose/ui/Modifier) to be applied to the
  indicator.

### Related components

If your UI requires the indicator to sit within a visible background container,
use the [`ContainedVoiceInputIndicator`](/reference/kotlin/androidx/xr/glimmer/ContainedVoiceInputIndicator.composable). This alternative ensures that the
indicator bars are transparent, allowing the background container to show
through.