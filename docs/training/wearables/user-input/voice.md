---
title: https://developer.android.com/training/wearables/user-input/voice
url: https://developer.android.com/training/wearables/user-input/voice
source: md.txt
---

Every Wear OS device comes with a microphone, so users can use their voice to interact with the
device. You can divide these into three types of interactions:

- Record audio
- Get free-form speech input
- Voice actions

## Record audio


Recording audio on a Wear OS device works the same way as it would on a phone. Refer to the
[MediaRecorder documentation](https://developer.android.com/guide/topics/media/mediarecorder) to learn more about
recording audio on Android. You can also look at a sample implementation in the
[Wear Speaker sample](https://github.com/android/wear-os-samples/tree/main/WearSpeakerSample)
on Github.

## Get free-form speech input


Call the system's built-in Speech Recognizer activity to get speech input from users. Use speech
input to send messages or perform searches.


In your app, call `https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)`
using the `https://developer.android.com/reference/android/speech/RecognizerIntent#ACTION_RECOGNIZE_SPEECH`
action. This starts the speech recognition activity, and you can then handle the result in
`https://developer.android.com/reference/android/app/Activity#onActivityResult(int, int, android.content.Intent)`.


The following code sample shows how to start and handle a speech recognition activity.

```kotlin
var textForVoiceInput by remember { mutableStateOf("") }

val voiceLauncher =
    rememberLauncherForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { activityResult ->
        // This is where you process the intent and extract the speech text from the intent.
        activityResult.data?.let { data ->
            val results = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS)
            textForVoiceInput = results?.get(0) ?: "None"
        }
    }

val scrollState = rememberScrollState()

ScreenScaffold(scrollState = scrollState) {
    // rest of implementation here
    // ...
    Column(
        // rest of implementation here
        // ...

        // Create an intent that can start the Speech Recognizer activity
        val voiceIntent: Intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )

            putExtra(
                RecognizerIntent.EXTRA_PROMPT,
                stringResource(R.string.voice_text_entry_label)
            )
        }
        // Invoke the process from a chip
        Chip(
            onClick = {
                voiceLauncher.launch(voiceIntent)
            },
            label = stringResource(R.string.voice_input_label),
            secondaryLabel = textForVoiceInput
        )
    }
}
```

## Voice Actions

Voice Actions and Assistant App Actions aren't supported at this time except for Wear OS apps in
China. Read more about
[Voice Actions support
for China](https://developer.android.com/training/wearables/apps/creating-app-china#voice-actions-support).