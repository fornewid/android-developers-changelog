---
title: Handle audio output for AI glasses using Text to Speech  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/tts
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Handle audio output for AI glasses using Text to Speech Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

One of the ways that you can communicate with your users is by using Text to
Speech (TTS) technology. TTS is built into Android (requiring no additional
libraries) and works even when offline. These characteristics makes TTS ideal
for handling error conditions in displayless mode. You can reference TTS
features using the [`TextToSpeech`](/reference/kotlin/android/speech/tts/TextToSpeech) class.

### Instantiate TextToSpeech

We recommend instantiating the `TextToSpeech` class on your AI glasses
activity's [`onCreate()`](/reference/kotlin/android/app/Activity#onCreate(android.os.Bundle)) method so that it's available for the lifetime of
the [`Activity`](/reference/kotlin/android/app/Activity):

```
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    tts = TextToSpeech(this) { status ->
        if(status == TextToSpeech.SUCCESS) {
        // Initialization successful
        }else {
            // Initialization failed
        }
    }
    ...
}
```

## Notify the user when TTS starts

For displayless (audio-only) experiences, let the user know that your app
successfully launched by notifying them in the [`onStart()`](/reference/kotlin/android/app/Activity#onStart()) method:

```
override fun onStart() {
  super.onStart()

  tts?.speak("Welcome to Android XR Glasses!",
  TextToSpeech.QUEUE_FLUSH,
  null,
  "welcome_utterance")
  ...
}
```

## Key points about the code

* [`TextToSpeech.QUEUE_FLUSH`](/reference/kotlin/android/speech/tts/TextToSpeech#queue_flush) indicates that the text should be spoken
  immediately and any other TTS utterance should be interrupted.
* The `utteranceId`, in this case `"welcome_utterance"`, is used to identify
  when this text is finished being spoken. For more information, see the
  [`UtteranceProgressListener`](/reference/kotlin/android/speech/tts/UtteranceProgressListener).

## Interrupt TTS

If your app ever needs to interrupt TTS, call the [stop()](/reference/kotlin/android/speech/tts/TextToSpeech#stop) method:

```
// This interrupts the current utterance and discards other utterances in the queue.
tts?.stop()
...
```

### Clean up TTS resources

You should clean up resources when your activity is destroyed by calling the
[shutdown()](/reference/kotlin/android/speech/tts/TextToSpeech#shutdown) method within the activity's [`onDestroy()`](/reference/kotlin/android/app/Activity#onDestroy()) method:

```
override fun onDestroy() {
    super.onDestroy()

    tts?.shutdown()
}
```

[Previous

arrow\_back

Overview](/develop/xr/jetpack-xr-sdk/audio-interactions)

[Next

Integrate with the Gemini Live API

arrow\_forward](/develop/xr/jetpack-xr-sdk/gemini-live)