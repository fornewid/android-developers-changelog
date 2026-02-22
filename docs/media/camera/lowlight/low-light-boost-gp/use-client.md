---
title: https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client
url: https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client
source: md.txt
---

To use Google Low Light Boost, you'll need a [*low light boost client*](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient).
You can use
the client to check if the low light boost module is installed, and to check
whether Google Low Light Boost is supported by the device and camera your app is
running on. You'll also use the client to create a [`LowLightBoostSession`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostSession).
([You'll use the session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session) to turn low light boost on and off.) You can also
set up a listener to receive callbacks when low light boost is active.
| **Note:** The Google Low Light Boost APIs are provided by Google Play services. See the [Google Play services documentation](https://developers.google.com/android) for information on how to set up and call its APIs.

`LowLightBoostClient` methods don't signal success or failure directly. Instead,
they return a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object. You use a `Task` to set up success and failure
listeners. This lets the methods signal success or failure asynchronously, which
is necessary since the methods need to communicate with Google Play services.

## Dependencies

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

`LowLightBoostClient` is provided by the Google Play services
[`com.google.android.gms.cameralowlight`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/package-summary) package. See the Google
Play services documentation for information on [accessing Google Play services
APIs](https://developers.google.com/android/guides/api-client).

## Create a client

You need a low light boost client to do anything else. The following code
creates a client:  

### Kotlin

    val lowLightBoostClient = LowLightBoost.getClient(context)

### Java

    LowLightBoostClient lowLightBoostClient = LowLightBoost.getClient(context);

### Key points about this code

- The [`LowLightBoost`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoost) class provides the static method [`getClient`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoost#getClient(android.content.Context))%7B:.external%7D(), which returns an instance of `LowLightBoostClient`.

## Check if low light boost is supported

Once you have a client, you can check if low light boost is supported by the
device the app is running on. The following code checks if low light boost is
supported:  

### Kotlin

    launch {
      try {
        // Await the result of the Task in a non-blocking way
        val isSupported: Boolean = lowLightBoostClient
          .isCameraSupported(cameraId).await()
        Log.d(TAG, "isCameraSupported: $isSupported")
        if (isSupported) {
          // Create the low light boost session here
        }
      } catch (e: Exception) {
        Log.e(TAG, "isCameraSupported failed", e)
      }
    }

### Java

    lowLightBoostClient
      .isCameraSupported(cameraId)
      .addOnSuccessListener(
        lowLightBoostExecutor,
        (isSupported) -> {
          Log.d(TAG, "isCameraSupported: " + isSupported);
          if (isSupported) {
            // Create the low light boost session here
          }
        )

### Key points about this code

- `cameraId` is assumed to be [the ID of a Camera2
  camera](https://developer.android.com/media/camera/camera2), created elsewhere.
- [`LowLightBoostClient.isCameraSupported()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#isCameraSupported(kotlin.String)) checks whether the Camera2 camera supports low light boost. In some cases, a device might support low light boost but one of its cameras might not, so you need to check both.
- The method `LowLightBoostClient.isCameraSupported()` returns a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object. You use this object to set up success and failure listeners. [Create
  the low light boost session](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-session) inside the success listener.

## Check if the low light boost module is installed

Once you have a client, you can confirm whether the low light boost module is
installed on your device. The following code checks if the module is installed:  

### Kotlin

    // Handle the Google Play services Task API with Kotlin coroutines
    // (kotlinx-coroutines-play-services)
    launch {
      try {
        val isInstalled: Boolean = lowLightBoostClient
          .isModuleInstalled(context).await()

        if (isInstalled) {
          Log.d(TAG, "Module is installed")
          try {
            openCamera(cameraId)
          } catch (e: CameraAccessException) {
            Log.e(TAG, "Failed to open camera", e)
          }
        } else {
          Log.d(TAG, "Module is not installed")
          launchInstallRequest()
        }
      } catch (e: Exception) {
        Log.e(TAG, "Failed to check module availability", e)
      }
    }

### Java

    lowLightBoostClient
      .isModuleInstalled(context)
      .addOnSuccessListener(
        (isInstalled) -> {
          if (isInstalled) {
            Log.d(TAG, "Module is installed");
            try {
              openCamera(cameraId);
            } catch (CameraAccessException e) {
              Log.e(TAG, "Failed to open camera", e);
            }
          } else {
            Log.d(TAG, "Module is not installed");
            launchInstallRequest();
          }
        })
      .addOnFailureListener(
        (e) -> {
          Log.e(TAG, "Failed to check module availability", e);
        });

### Key points about this code

- This code opens a camera session connecting to the camera identified by `cameraId`. For more information, see the [Camera2
  documentation](https://developer.android.com/media/camera/camera2).
- The method [`LowLightBoostClient.isModuleInstalled()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#isModuleInstalled(android.content.Context)) returns a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object. You use this object to set up success and failure listeners.
- Use `Task.addOnSuccessListener()` to set up a listener that's called if the call to `isModuleInstalled()` succeeds. Importantly, if the success listener is called, that just tells you that the client succeeded in finding out **whether** the module is installed on the device. In the body of your listener, you need to check whether the module is actually installed or not.
- If the module isn't already installed, this snippet installs it by calling the method `launchInstallRequest()`. That method is defined in the snippet in [Install the low light boost
  module](https://developer.android.com/media/camera/lowlight/low-light-boost-gp/use-client#install).

## Install the low light boost module

If the low light boost module isn't already installed on the device, you'll need
to download and install it from Google Play services. This code shows how to do
that:  

### Kotlin

    private suspend fun launchInstallRequest() {
      Log.v(TAG, "Launching install request")

      try {
        // Check if this device can support Google LLB.
        val isDeviceSupported: Boolean = lowLightBoostClient
          .isDeviceSupported(context).await()

        if (isDeviceSupported) {
          Log.d(TAG, "Device is supported")
          // Show download indicator, if needed.

          try {
            val isInstallSuccessful: Boolean = lowLightBoostClient
              .installModule(context,
                            createInstallStatusCallback()
              ).await()

            if (isInstallSuccessful) {
              Log.d(TAG, "Module installed")
              // Hide download indicator, if needed.
              try {
                openCamera()
              } catch (e: CameraAccessException) {
                Log.e(TAG, "Failed to open camera", e)
              }
            } else {
              Log.d(TAG, "Module install failed")
            }
          } catch (e: Exception) {
            Log.e(TAG, "An error occurred installing the module:", e)
          }
        } else {
          Log.d(TAG, "Device is not supported")
        }
      } catch (e: Exception) {
        Log.e(TAG, "An error occurred checking device support:", e)
      }
    }

### Java

    private void launchInstallRequest() {
      Log.v(TAG, "Launching install request");
      // Check if this device can support Google LLB.
      lowLightBoostClient
        .isDeviceSupported(context)
        .addOnSuccessListener(
          (isDeviceSupported) -> {
            if (isDeviceSupported) {
              Log.d(TAG, "Device is supported");
              // Show download indicator, if needed.
              lowLightBoostClient
                .installModule(
                  this,
                  createInstallStatusCallback()
                )
                .addOnSuccessListener(
                  (result) -> {
                    if (result) {
                      Log.d(TAG, "Module installed");
                      // Hide download indicator, if needed.
                      try {
                        openCamera();
                      } catch (CameraAccessException e) {
                        Log.e(TAG, "Failed to open camera", e);
                      }
                    } else {
                      Log.d(TAG, "Module install failed");
                    }
                  }
                );
            } else {
              Log.d(TAG, "Device is not supported");
            }
          })
        .addOnFailureListener(
          (e) -> {
            Log.e(TAG, "Failed to check device support", e);
          });
    }

### Key points about this code

- When you call [`LowLightBoostClient.installModule()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#installModule(android.content.Context,com.google.android.gms.cameralowlight.LowLightBoostClient.InstallStatusCallback)) you pass a callback object, which implements [`LowLightBoostClient.InstallStatusCallback`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient.InstallStatusCallback). `installModule()` calls methods in that callback to indicate the status of the download. For example, if the download is paused, `installModule()` calls the callback object's [`onDownloadPause()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient.InstallStatusCallback#onDownloadPaused()) method.
- In this code snippet, the callback object is created by the `createInstallStatusCallback()` method. You'd need to write that method yourself, along these lines:

### Kotlin

    private fun createInstallStatusCallback(): LowLightBoostClient.InstallStatusCallback =
            object : LowLightBoostClient.InstallStatusCallback() {
        override fun onDownloadPending() {
          Log.d(TAG, "onDownloadPending")
          // Code here...
        }

        override fun onDownloadStart() {
          Log.d(TAG, "onDownloadStart")
          // Code here...
        }

        // other overrides here...
      }

### Java

    private InstallStatusCallback createInstallStatusCallback() {
      new LowLightBoostClient.InstallStatusCallback() {
        @Override
        public void onDownloadPending() {
          Log.d(TAG, "onDownloadPending");
          // Code here...
        }

        @Override
        public void onDownloadStart() {
          Log.d(TAG, "onDownloadStart");
          // Code here...
        }

      // other overrides here...
    }

- [`LowLightBoostClient.isDeviceSupported()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#isDeviceSupported(android.content.Context))
  checks whether the Android-powered device and operating system support Google
  Low Light Boost. If not, don't download the module.

- The method
  [`LowLightBoostClient.installModule()`](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/LowLightBoostClient#installModule(android.content.Context,com.google.android.gms.cameralowlight.LowLightBoostClient.InstallStatusCallback))
  returns a
  [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task)
  object. You use this object to set up success and failure listeners.

- When the install finishes, the success listener verifies the install by
  opening the camera. In the snippet, this is done with a call to
  `openCamera()`. You'll need to write that method yourself.