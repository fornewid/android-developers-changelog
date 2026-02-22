---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/asr
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/asr
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg)AI Glasses[](https://developer.android.com/develop/xr/devices#ai-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

You can use Automatic Speech Recognition (ASR) to recognize specific utterances from your user using[`SpeechRecognizer`](https://developer.android.com/reference/kotlin/android/speech/SpeechRecognizer)and turn them into text.`SpeechRecognizer`is built into Android (requiring no additional libraries) and works even when offline.

For`SpeechRecognizer`to convert your user's speech into text, the user needs to grant your app the[`RECORD_AUDIO`](https://developer.android.com/reference/kotlin/android/Manifest.permission#record_audio)permission. To learn how to request this permission for your app, see[Request hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions).

## Instantiate SpeechRecognizer

Instantiate the`SpeechRecognizer`in your AI glasses activity's[`onCreate()`](https://developer.android.com/reference/kotlin/android/app/Activity#onCreate(android.os.Bundle))method so that it's available for the lifetime of the activity:  

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        //The RECORD_AUDIO permission must be granted to your app before instantiation

        speechRecognizer = SpeechRecognizer.createOnDeviceSpeechRecognizer(this)
        speechRecognizer?.setRecognitionListener(recognitionListener)
        ...
    }

## Configure your RecognitionListener

The[`setRecognitionListener()`](https://developer.android.com/reference/kotlin/android/speech/SpeechRecognizer#setRecognitionListener(android.speech.RecognitionListener))method lets you specify the object where important callbacks are made, such as in[`RecognitionListener.onResults()`](https://developer.android.com/reference/kotlin/android/speech/RecognitionListener#onResults(android.os.Bundle)), which the system calls after it recognizes spoken language.  

    val recognitionListener = object : RecognitionListener {

        override fun onResults(results: Bundle?) {

            val matches = results?.getStringArrayList(RESULTS_RECOGNITION)
            val confidences = results?.getFloatArray(CONFIDENCE_SCORES)

            val mostConfidentIndex = confidences!!.indices.maxByOrNull { confidences[it] }

            if (mostConfidentIndex != null){
                val spokenText = matches[mostConfidentIndex]

                if (spokenText.equals("Start my Run", ignoreCase = true)){
                    // User indicated they want to start a run
                }
            }

        }
        ...
    }

### Key points about the code

- The bundle is queried for two arrays. The first array includes all of the matches and the second is the speech recognizer's confidence in what was heard. The indices of these arrays correspond to each other. The match with the highest confidence value (`mostConfidentIndex`) is used.

- A case-insensitive string match is performed to determine what action the user wants to take.

### Alternative approaches when matching

In the preceding example, the match with the highest confidence value is used. This choice means that the system must be pretty confident in what it understood from the user or it won't flag a match. When using this approach, you might get false negatives.

Another approach could be to look through all of the matches regardless of confidence and find any match that fits the input you are looking for. In contrast, this kind of approach could lead to more false positives. The approach you should take is largely dependent on your usecase.

## Start listening

To start listening to the user, specify the[`ACTION_RECOGNIZE_SPEECH`](https://developer.android.com/reference/kotlin/android/speech/RecognizerIntent#ACTION_RECOGNIZE_SPEECH:kotlin.String)intent when calling[`startListening()`](https://developer.android.com/reference/kotlin/android/speech/SpeechRecognizer#startListening(android.content.Intent)).  

    override fun onStart() {
        super.onStart()

        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
        }

        speechRecognizer?.startListening(intent)

    }

### Key points about the code

- When using[`ACTION_RECOGNIZE_SPEECH`](https://developer.android.com/reference/kotlin/android/speech/RecognizerIntent#ACTION_RECOGNIZE_SPEECH:kotlin.String), you must also specify the[`EXTRA_LANGUAGE_MODEL`](https://developer.android.com/reference/kotlin/android/speech/RecognizerIntent#extra_language_model)extra.
- [`LANGUAGE_MODEL_FREE_FORM`](https://developer.android.com/reference/kotlin/android/speech/RecognizerIntent#language_model_free_form)is intended for conversational speech.