---
title: https://developer.android.com/training/cars/apps/library/car-microphone
url: https://developer.android.com/training/cars/apps/library/car-microphone
source: md.txt
---

You can use your car's [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService) and [`CarAudioRecord`](https://developer.android.com/reference/androidx/car/app/media/CarAudioRecord) API
to grant your app access to the user's car microphone. Users must grant
permission to your app to access the car microphone. Your app can record and
process user input in your app.

## Declare permission to record

Before recording any audio, you must first declare the permission to record in
your `AndroidManifest.xml` and request that the user grant it.  

    <manifest ...>
       ...
       <uses-permission android:name="android.permission.RECORD_AUDIO" />
       ...
    </manifest>

You must request the permission to record at runtime. To learn more about how
to request permissions in your car, see [Request permissions](https://developer.android.com/training/cars/apps/library/request-permissions).

## Record audio

After the user gives permission to record, you can record the audio and process
the recording.  

### Kotlin

    val carAudioRecord = CarAudioRecord.create(carContext)
            carAudioRecord.startRecording()

            val data = ByteArray(CarAudioRecord.AUDIO_CONTENT_BUFFER_SIZE)
            while(carAudioRecord.read(data, 0, CarAudioRecord.AUDIO_CONTENT_BUFFER_SIZE) >= 0) {
                // Use data array
                // Potentially call carAudioRecord.stopRecording() if your processing finds end of speech
            }
            carAudioRecord.stopRecording()

### Java

    CarAudioRecord carAudioRecord = CarAudioRecord.create(getCarContext());
            carAudioRecord.startRecording();

            byte[] data = new byte[CarAudioRecord.AUDIO_CONTENT_BUFFER_SIZE];
            while (carAudioRecord.read(data, 0, CarAudioRecord.AUDIO_CONTENT_BUFFER_SIZE) >= 0) {
                // Use data array
                // Potentially call carAudioRecord.stopRecording() if your processing finds end of speech
            }
            carAudioRecord.stopRecording();

## Acquire audio focus

When recording from the car microphone, you must acquire [audio focus](https://developer.android.com/reference/android/media/AudioFocusRequest#what-is-audio-focus) first.
This stops any ongoing media. If you lose audio focus, stop recording. For
example, to acquire audio focus:  

### Kotlin

    val carAudioRecord = CarAudioRecord.create(carContext)

            // Take audio focus so that user's media is not recorded
            val audioAttributes = AudioAttributes.Builder()
                .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                // Use the most appropriate usage type for your use case
                .setUsage(AudioAttributes.USAGE_ASSISTANCE_NAVIGATION_GUIDANCE)
                .build()

            val audioFocusRequest =
                AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_EXCLUSIVE)
                    .setAudioAttributes(audioAttributes)
                    .setOnAudioFocusChangeListener { state: Int ->
                        if (state == AudioManager.AUDIOFOCUS_LOSS) {
                            // Stop recording if audio focus is lost
                            carAudioRecord.stopRecording()
                        }
                    }
                    .build()

            if (carContext.getSystemService(AudioManager::class.java)
                    .requestAudioFocus(audioFocusRequest)
                != AudioManager.AUDIOFOCUS_REQUEST_GRANTED
            ) {
                // Don't record if the focus isn't granted
                return
            }

            carAudioRecord.startRecording()
            // Process the audio and abandon the AudioFocusRequest when done

### Java

    CarAudioRecord carAudioRecord = CarAudioRecord.create(getCarContext());
            // Take audio focus so that user's media is not recorded
            AudioAttributes audioAttributes =
                    new AudioAttributes.Builder()
                            .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                            // Use the most appropriate usage type for your use case
                            .setUsage(AudioAttributes.USAGE_ASSISTANCE_NAVIGATION_GUIDANCE)
                            .build();

            AudioFocusRequest audioFocusRequest =
                    new AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_EXCLUSIVE)
                            .setAudioAttributes(audioAttributes)
                            .setOnAudioFocusChangeListener(state -> {
                                if (state == AudioManager.AUDIOFOCUS_LOSS) {
                                    // Stop recording if audio focus is lost
                                    carAudioRecord.stopRecording();
                                }
                            })
                            .build();

            if (getCarContext().getSystemService(AudioManager.class).requestAudioFocus(audioFocusRequest)
                    != AUDIOFOCUS_REQUEST_GRANTED) {
                // Don't record if the focus isn't granted
                return;
            }

            carAudioRecord.startRecording();
            // Process the audio and abandon the AudioFocusRequest when done