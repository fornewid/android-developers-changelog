---
title: https://developer.android.com/ndk/guides/audio/opensl/getting-started
url: https://developer.android.com/ndk/guides/audio/opensl/getting-started
source: md.txt
---

# Get started

WARNING: OpenSL ES is**deprecated** . Developers should use the open source Oboe library which is available on[GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles[AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio). Oboe calls AAudio when AAudio is available, and falls back to OpenSL ES if AAudio is not available.

This section provides the information needed to get started using the OpenSL ES APIs.

## Add OpenSL ES to your app

You can call OpenSL ES from both C and C++ code. To add the core OpenSL ES feature set to your app, include the`OpenSLES.h`header file:  

```c++
#include <SLES/OpenSLES.h>
```

To add the OpenSL ES[Android extensions](https://developer.android.com/ndk/guides/audio/opensl/android-extensions), too, include the`OpenSLES_Android.h`header file:  

```c++
#include <SLES/OpenSLES_Android.h>
```

When you include the`OpenSLES_Android.h`header file, the following headers are included automatically:  

```c++
#include <SLES/OpenSLES_AndroidConfiguration.h>
#include <SLES/OpenSLES_AndroidMetadata.h>
```

**Note:**These headers are not required, but are shown as an aid in learning the API.

## Build and debug

You can incorporate OpenSL ES into your build by specifying it in the[`Android.mk`](https://developer.android.com/ndk/guides/android_mk)file that serves as one of the NDK build system's makefiles. Add the following line to[`Android.mk`](https://developer.android.com/ndk/guides/android_mk):  

```
LOCAL_LDLIBS += -lOpenSLES
```

For robust debugging, we recommend that you examine the`SLresult`value that most of the OpenSL ES APIs return. You can use[asserts](https://en.wikipedia.org/wiki/Assertion_(computing))or more advanced error-handling logic for debugging; neither offers an inherent advantage for working with OpenSL ES, although one or the other might be more suitable for a given use case.

We use asserts in our[examples](https://github.com/googlesamples/android-ndk), because they help catch unrealistic conditions that would indicate a coding error. We have used explicit error handling for other conditions more likely to occur in production.

Many API errors result in a log entry, in addition to a non-zero result code. Such log entries can provide additional detail that proves especially useful for relatively complex APIs such as[`Engine::CreateAudioPlayer`](https://www.khronos.org/registry/sles/specs/OpenSL_ES_Specification_1.1.pdf#page=243).

You can view the log either from the command line or from Android Studio. To examine the log from the command line, type the following:  

```
$ adb logcat
```

To examine the log from Android Studio, select**View \> Tool Windows \> Logcat** . For more information, see[Write and View Logs with Logcat](https://developer.android.com/studio/debug/am-logcat).

### Example code

We recommend using supported and tested example code that is usable as a model for your own code, which is located in the[audio-echo](https://github.com/android/ndk-samples/tree/main/audio-echo)and[native-audio](https://github.com/android/ndk-samples/tree/main/native-audio)folders of the[android-ndk](https://github.com/android/ndk-samples)GitHub repository.

**Caution:** The OpenSL ES 1.0.1 specification contains example code in the appendices (see[Khronos OpenSL ES Registry](https://www.khronos.org/registry/sles/)for more details). However, the examples in*Appendix B: Sample Code* and*Appendix C: Use Case Sample Code*use features that are not supported by Android. Some examples also contain typographical errors, or use APIs that are likely to change. Proceed with caution when referring to these; though the code may be helpful in understanding the full OpenSL ES standard, it should not be used as-is with Android.

### Audio content

The following are some of the many ways to package audio content for your application:

- **Resources** : By placing your audio files into the`res/raw/`folder, they can be accessed easily by the associated APIs for[`Resources`](https://developer.android.com/reference/android/content/res/Resources). However, there is no direct native access to resources, so you must write Java programming language code to copy them out before use.
- **Assets** : By placing your audio files into the`assets/`folder, they are directly accessible by the Android native asset manager APIs. See the header files`android/asset_manager.h`and`android/asset_manager_jni.h`for more information on these APIs. The example code located in the[android-ndk](https://github.com/googlesamples/android-ndk)GitHub repository uses these native asset manager APIs in conjunction with the Android file descriptor data locator.
- **Network** : You can use the URI data locator to play audio content directly from the network. However, be sure to read[Security and permissions](https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes#sandp).
- **Local file system** : The URI data locator supports the`file:`scheme for local files, provided the files are accessible by the application. Note that the Android security framework restricts file access via the Linux user ID and group ID mechanisms.
- **Recorded** : Your application can record audio data from the microphone input, store this content, and then play it back later. The example code uses this method for the*Playback*clip.
- **Compiled and linked inline** : You can link your audio content directly into the shared library, and then play it using an audio player with a buffer queue data locator. This is most suitable for short PCM format clips. The example code uses this technique for the*Hello* and*Android* clips. The PCM data was converted to hex strings using a`bin2c`tool (not supplied).
- **Real-time synthesis**: Your application can synthesize PCM data on the fly and then play it using an audio player with buffer queue data locator. This is a relatively advanced technique, and the details of audio synthesis are beyond the scope of this article.

**Note:** Finding or creating useful audio content for your application is beyond the scope of this article. You can use web search terms such as*interactive audio* ,*game audio* ,*sound design* , and*audio programming*to locate more information.

**Caution:**It is your responsibility to ensure that you are legally permitted to play or record content. There may be privacy considerations for recording content.

## Code samples

These sample apps are available on our GitHub page:

- [audio-echo](https://github.com/android/ndk-samples/tree/main/audio-echo)creates an input-to-output roundtrip loop.
- [native-audio](https://github.com/android/ndk-samples/tree/main/native-audio)is a simple audio recorder/player.

The Android NDK implementation of OpenSL ES differs from the reference specification for OpenSL ES 1.0.1 in a number of respects. These differences are an important reason why sample code that you copy directly from the OpenSL ES reference specification may not work in your Android app.

For more information on differences between the reference specification and the Android implementation, see[OpenSL ES for Android](https://developer.android.com/ndk/guides/audio/opensl/opensl-for-android).