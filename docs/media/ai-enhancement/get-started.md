---
title: https://developer.android.com/media/ai-enhancement/get-started
url: https://developer.android.com/media/ai-enhancement/get-started
source: md.txt
---

The Media Enhancement API is a powerful tool that uses on-device GPU
acceleration to perform high-quality, low-latency image enhancements. This
includes features like automatic tone mapping, de-blurring, de-noising, and
upscaling.

Before initializing the API, you must configure your project dependencies and
declare hardware acceleration requirements in your manifest. Skipping these
configurations is the primary cause of `GLOBAL_INIT_FAILED` runtime errors.

## Gradle dependencies

Add the following dependencies to your `app/build.gradle.kts` file. To
facilitate asynchronous, non-blocking execution, include Kotlin coroutines and
Jetpack Media3 for hardware surface handling.

    dependencies {
        // Google Play services Media Enhancement Library (Beta)
        implementation("com.google.android.gms:play-services-media-effect-enhancement:16.0.0-beta04")
    }

See package details for [`play-services-media-effect-enhancement`](https://maven.google.com/web/index.html?q=com.google.android.gms#com.google.android.gms:play-services-media-effect-enhancement) in
Google's Maven repository.

We also recommend using Kotlin coroutines for managing the enhancement sessions
async.

    // Kotlin coroutines for asynchronous API handling
      implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")
      implementation("org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.7.3")

## Android manifest requirements

Add the following elements inside the `<application>` tag of your
`AndroidManifest.xml` file:

    <manifest xmlns:android="http://schemas.android.com/apk/res/android">
        <application>
            <!-- 1. Google Play services version for runtime compatibility checks -->
            <meta-data
                android:name="com.google.android.gms.version"
                android:value="@integer/google_play_services_version" />
            <!-- 2. Declare OpenCL compute libraries for NPU/GPU neural acceleration -->
            <uses-native-library android:name="libOpenCL.so" android:required="false" />
            <uses-native-library android:name="libOpenCL-car.so" android:required="false" />
            <uses-native-library android:name="libOpenCL-pixel.so" android:required="false" />
            <!-- 3. Declare OpenGL ES for high-performance graphics rendering -->
            <uses-native-library android:name="libGLESv2.so" android:required="false" />
            <uses-native-library android:name="libGLESv3.so" android:required="false" />
        </application>
    </manifest>

OpenCL provides the native compute libraries required to enable NPU and GPU
neural acceleration for Media Enhancement tasks. Declaring these libraries in
your manifest is a prerequisite for the API to leverage hardware acceleration,
which is essential for performing high-quality, low-latency enhancements. For
more information about OpenCL, see [OpenCL implementations](https://www.khronos.org/opencl/#ocl-implementations).

OpenGL ES provides the native graphics libraries required for high-performance
rendering of media enhancement outputs. Declaring these libraries in your
manifest is essential to ensure that the rendering pipeline can effectively
display processed media on hardware-accelerated surfaces. For information about
OpenGL, see [OpenGL API documentation overview](https://www.opengl.org/Documentation/Documentation.html).

The Android rendering pipeline must be hardware-accelerated to prevent
bottlenecks. While enabled by default for apps targeting API 14+, explicitly set
`android:hardwareAccelerated="true"` within your `<activity>` tags.

## Device compatibility and module setup

Google Play services delivers machine learning models dynamically to conserve
your initial APK storage space. Before performing enhancements, the application
must use the `EnhancementClient` to verify hardware support and ensure the
necessary model weights are downloaded and cached locally. This is a one-time
process per device.

Using `suspendCancellableCoroutine`, you can wrap the task-based client
callbacks in standard Kotlin suspending functions for cleaner, sequential
execution:

    // Verifies if host hardware supports NPU/GPU acceleration
    suspend fun EnhancementClient.isDeviceSupportedAsync(): Boolean = suspendCancellableCoroutine { continuation ->
        this.isDeviceSupported()
            .addOnSuccessListener { result -> continuation.resume(result) }
            .addOnFailureListener { exception -> continuation.resumeWithException(exception) }
    }
    // Verifies the presence of required neural network models
    suspend fun EnhancementClient.isModuleInstalledAsync(): Boolean = suspendCancellableCoroutine { continuation ->
        this.isModuleInstalled()
            .addOnSuccessListener { result -> continuation.resume(result) }
            .addOnFailureListener { exception -> continuation.resumeWithException(exception) }
    }