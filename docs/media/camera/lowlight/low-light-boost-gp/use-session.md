---
title: https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session
url: https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session
source: md.txt
---

Use a low light boost session to turn Google Low Light Boost on and off.  

### Kotlin

    dependencies {
      val low_light_boost_version = "16.0.1-beta04"
      implementation("org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.10.2")
      implementation("com.google.android.gms:play-services-base:18.7.0")
      implementation("com.google.android.gms:play-services-camera-low-light-boost:${low_light_boost_version}")
      implementation("com.google.android.gms:play-services-tasks:18.3.0")
    }

### Groovy

    dependencies {
      def low_light_boost_version = "16.0.1-beta04"
      implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.10.2'
      implementation 'com.google.android.gms:play-services-base:18.7.0'
      implementation 'com.google.android.gms:play-services-camera-low-light-boost:${low_light_boost_version}'
      implementation 'com.google.android.gms:play-services-tasks:18.3.0'
    }

`LowLightBoostSession` is provided by the Google Play services
[`com.google.android.gms.cameralowlight`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/package-summary) package. See the Google
Play services documentation for information on [accessing Google Play services
APIs](https://developers.google.com/android/guides/api-client).

## Create a callback object

When you [create the low light boost session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#create-session), you'll need to pass it an
object that implements the [`LowLightBoostCallback`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostCallback) interface.
This object's functions are called when the session is disconnected or
destroyed. The following code shows how to create a callback:  

### Kotlin

    private fun createLowLightBoostCallback(): LowLightBoostCallback =
      object : LowLightBoostCallback() {
        override fun onSessionDestroyed() {
          Log.d(TAG, "onSessionDestroyed")
          lowLightBoostSession = null
        }

        override fun onSessionDisconnected(statusCode: Int) {
          Log.d(TAG, "onSessionDisconnected: error=$statusCode")
          lowLightBoostSession = null
        }
      }

### Java

    private LowLightBoostCallback createLowLightBoostCallback() {
      LowLightBoostCallback lowLightBoostCallback = new LowLightBoostCallback() {
        @Override
        public void onSessionDestroyed() {
          Log.d(TAG, "onSessionDestroyed");
          lowLightBoostSession = null;
        }

        @Override
        public void onSessionDisconnected(int statusCode) {
          Log.d(TAG, "onSessionCreationFailed: error=" + statusCode);
          lowLightBoostSession = null;
        }
      }
      return lowLightBoostCallback;
    }

### Key points about this code

- This code defines a private method, `createLowLightBoostCallback()`, which creates the callback object. You'll call that method when you actually create the low light boost session, as described in [Create a session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#create-session).
- The callback is called when the session is disconnected or destroyed. It is *not* called when the session is created. To check whether the session was successfully created, examine the [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object returned by [`LowLightBoostClient.createSession`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#createSession(com.google.android.gms.cameralowlight.LowLightBoostOptions,com.google.android.gms.cameralowlight.LowLightBoostCallback)).

## Create a session

To create a low light session, call the method
[`LowLightBoostClient.createSession`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#createSession(com.google.android.gms.cameralowlight.LowLightBoostOptions,com.google.android.gms.cameralowlight.LowLightBoostCallback)).  

### Kotlin

    val options = LowLightBoostOptions(
      previewSurface,
      cameraId,
      previewWidth,
      previewHeight,
      enableLowLightBoost
    )

    launch {
      try {
        val lowLightBoostSession = lowLightBoostClient
          .createSession(options, createLowLightBoostCallback()).await()

        Log.d(TAG, "Session created successfully")

        // Get the surface from the LLB session;
        // give it to camera so camera can write frames to it
      } catch (e: CancellationException) {
        Log.w(TAG, "Session creation was canceled", e)
        lowLightBoostSession = null
      } catch (e: ApiException) {
        Log.e(TAG, "Session creation failed with ApiException:", e)
        lowLightBoostSession = null
      } catch (e: Exception) {
        Log.e(TAG, "Session creation failed with Exception", e)
        lowLightBoostSession = null
      }
    }

### Java

    LowLightBoostOptions options = new LowLightBoostOptions(
      previewSurface,
      cameraId,
      previewWidth,
      previewHeight,
      enableLowLightBoost);

    lowLightBoostClient
      .createSession(options, createLowLightBoostCallback())
      .addOnSuccessListener(
        lowLightBoostExecutor,
        (session) -> {
          Log.d(TAG, "Session created successfully");

          // Get the surface from the LLB session;
          // give it to camera so camera can write frames to it

        })
      .addOnFailureListener(
        lowLightBoostExecutor,
        (e) -> {
          ApiException apiException = (ApiException) e;
          Log.d(TAG, "Session creation failed: " + e);
          lowLightBoostSession = null;
        })
      .addOnCompleteListener(
        lowLightBoostExecutor,
        (task) -> Log.d(TAG, "Session creation complete"))
      .addOnCanceledListener(
        lowLightBoostExecutor,
        () -> {
          throw new RuntimeException("Session creation canceled");
        });

### Key points about this code

- You pass a [`LowLightBoostOptions`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostOptions) object to `createSession()` to configure the session. This object specifies such things as the [target
  surface](https://developer.android.com/reference/android/view/Surface), the ID of the camera to use, and the dimensions of the preview.
- This code assumes you have already opened a connection to a Camera2 camera, and used that information to set the values of `cameraId, previewWidth,
  previewHeight`. For more information, see the [Camera2 documentation](https://developer.android.com/media/camera/camera2).
- `enableLowLightBoost` is a boolean value specifying whether low light boost should start on or off.
- `createLowLightBoostCallback` is a method you write to create the callback object. This object is called when the session is disconnected or destroyed.
- The method `LowLightBoostClient.createSession()` returns a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object. You use this object to set up success and failure listeners. [Capture the video inside the success listener.](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#preview)
- You can specify an [`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor) to run the listeners. If you don't specify an `Executor`, the listeners run on the main thread. In this code, we assume `lowLightBoostExecutor` is a suitable `Executor`.

## Pass in the capture results

Google Low Light Boost needs certain camera metadata to know the correct amount
of brightening to apply. You must pass in the [`TotalCaptureResult`](https://developer.android.com/reference/android/hardware/camera2/TotalCaptureResult) to the
[`processCaptureResult()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostSession#processCaptureResult(android.hardware.camera2.TotalCaptureResult)) method. You can get the `TotalCaptureResult` in
the [`onCaptureCompleted()`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession.CaptureCallback#onCaptureCompleted(android.hardware.camera2.CameraCaptureSession,%20android.hardware.camera2.CaptureRequest,%20android.hardware.camera2.TotalCaptureResult)) callback method.  

### Kotlin

      val captureCallback = CameraCaptureSession.CaptureCallback() {
        override fun onCaptureCompleted(
          session: CameraCaptureSession,
          request: CaptureRequest,
          result: TotalCaptureResult
        ) {
          super.onCaptureCompleted(session, request, result)
          lowLightBoostSession?.processCaptureResult(result)
        }
      }

### Java

      CameraCaptureSession.CaptureCallback captureCallback =
        new CameraCaptureSession.CaptureCallback() {
          @Override
          public void onCaptureCompleted(
            @NonNull CameraCaptureSession session,
            @NonNull CaptureRequest request,
            @NonNull TotalCaptureResult result) {
              super.onCaptureCompleted(session, request, result)
              if (lowLightBoostSession != null) {
                lowLightBoostSession.processCaptureResult(result);
              }
            }
          };

### Key points about this code

- This code is only showing the `CaptureCallback` code relevant to Google LLB. You will likely have other code in these callbacks.
- Passing in the `TotalCaptureResult` allows Google LLB to analyze the auto exposure data and other metadata which is necessary for low light boost to process scene detection and determine how much boost to apply to the frame.
- You should pass the `captureCallback` object when creating the camera session, for example with \`[setSingleRepeatingRequest()](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession#setSingleRepeatingRequest(android.hardware.camera2.CaptureRequest,%20java.util.concurrent.Executor,%20android.hardware.camera2.CameraCaptureSession.CaptureCallback)).

| **Note:** For CameraX apps, you'll need to use the [`Camera2Interop.Extender.setSessionCaptureCallback()`](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2Interop.Extender#setSessionCaptureCallback(android.hardware.camera2.CameraCaptureSession.CaptureCallback)) method to set the `captureCallback` object defined in the previous code snippet. See the [CameraX interoperability with Camera2](https://developer.android.com/media/camera/camerax/architecture#camerax-interoperability) guide for information on this approach.

## Start camera preview

Once you have created a low light session, you can start the camera preview
stream. You should do
this inside the `onSuccess()` callback you pass to the low light session, as
described in [Create a session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#create-session). The following code shows how to capture
video:  

### Kotlin

    MainActivity.this.lowLightBoostSession =
      lowLightBoostSession
    MainActivity.this.lowLightBoostSession
      .setSceneDetectorCallback(
        (lowLightBoostSession, boostStrength) -> {
          Log.d(TAG, "onSceneBrightnessChanged: " +
            "boostStrength=$boostStrength")
          // boostStrength > 0.5 indicates a low light scene.
          // Update UI accordingly.
        },
        lowLightBoostExecutor
      )
    try {
      startCaptureSession(
        lowLightBoostSession.getCameraSurface())
        // Start a Camera2 session here. Pass the LLB surface
        // to the camera so the camera can write frames to it.
    } catch (e: CameraAccessException) {
      Log.e(TAG, "Failed to start capture session", e)
      // Must try again or start the capture session without LLB.
    }

### Java

    MainActivity.this.lowLightBoostSession =
      lowLightBoostSession;
    MainActivity.this.lowLightBoostSession
      .setSceneDetectorCallback(
        (lowLightBoostSession, boostStrength) -> {
          Log.d(TAG, "onSceneBrightnessChanged: " +
            "boostStrength=" + boostStrength);
          // boostStrength > 0.5 indicates a low light scene.
          // Update UI accordingly.
        },
        lowLightBoostExecutor
      );
    try {
      startCaptureSession(
        lowLightBoostSession.getCameraSurface());
        // Start a Camera2 session here. Pass the LLB surface
        // to the camera so the camera can write frames to it.
    } catch (CameraAccessException e) {
      Log.e(TAG, "Failed to start capture session", e);
      // Must try again or start the capture session without LLB.
    }

### Key points about this code

- `lowLightBoostSession` is the session you created in [Create a session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session#create-session).
- [`setSceneDetectorCallback()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostSession#setSceneDetectorCallback(com.google.android.gms.cameralowlight.SceneDetectorCallback,java.util.concurrent.Executor)) defines a callback object implementing the [`SceneDetectorCallback`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/SceneDetectorCallback) interface. The session calls that object's [`onSceneBrightnessChanged()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/SceneDetectorCallback#onSceneBrightnessChanged(com.google.android.gms.cameralowlight.LowLightBoostSession,kotlin.Float)) method when the scene brightness changes. Your implementation should adjust the camera's UI appropriately.
- You can specify an [`Executor`](https://developer.android.com/reference/java/util/concurrent/Executor) to run the callback. If you don't specify an `Executor`, the callback runs on the main thread. In this code, we assume `lowLightBoostExecutor` is a suitable `Executor`.
- [`lowLightBoostSession.getCameraSurface()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostSession#getCameraSurface()) returns the [`Surface`](https://developer.android.com/reference/android/view/Surface) with the captured video.

| **Note:** For CameraX apps, you can provide the Google LLB camera surface to CameraX by setting it with [`SurfaceRequest.provideSurface()`](https://developer.android.com/reference/androidx/camera/core/SurfaceRequest#provideSurface(android.view.Surface,java.util.concurrent.Executor,androidx.core.util.Consumer%3Candroidx.camera.core.SurfaceRequest.Result%3E)).

## Release the session

When the camera is no longer active, release the low light boost session by
calling `LowLightBoostSession.release()`. In particular, you should make sure to
release the session when your activity is destroyed. You can do this by calling
the method in your activity's `onDestroy()` method:  

### Kotlin

    override protected void onDestroy() {
      super.onDestroy()
      if (lowLightBoostSession != null) {
        lowLightBoostSession.release()
        lowLightBoostSession = null
      }
    }

### Java

    @Override
    protected void onDestroy() {
      super.onDestroy();
      if (lowLightBoostSession != null) {
        lowLightBoostSession.release();
        lowLightBoostSession = null;
      }
    }

### Key points about this code

- After the session is released, you shouldn't call any of its methods. You should clear any variables pointing to the session, as this code does.