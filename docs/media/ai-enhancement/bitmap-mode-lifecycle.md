---
title: https://developer.android.com/media/ai-enhancement/bitmap-mode-lifecycle
url: https://developer.android.com/media/ai-enhancement/bitmap-mode-lifecycle
source: md.txt
---

The Media Enhancement API provides a low-latency, privacy-preserving, on-device
AI solution that leverages hardware acceleration to deliver high-quality media
improvements with zero APK bloat. For more information, see [Understand the
media enhancement capabilities](https://developer.android.com/media/ai-enhancement/overview).

The static Bitmap mode (`EnhancementMode.BITMAP`) is designed for static,
decoded image processing.

Operating in Bitmap mode requires the OS to serialize uncompressed pixel data
and copy it from CPU memory across the system bus to GPU memory, returning the
processed frame through a reverse copy. It is optimized for single-frame
execution and isn't compatible with real-time video streaming.

This workflow involves creating a session, processing a single bitmap with it,
and then handling the result. The code examples from the previous sections cover
this use case in detail.

1. **Configure options** : Create an `EnhancementOptions` object, ensuring the `enhancementMode` is set to `EnhancementMode.BITMAP`.
2. **Create session** : Use the `createSessionAsync` wrapper we defined earlier to create an `EnhancementSession`. This is a heavyweight object, so create it only when needed.
3. **Process image**: Call the session, your input bitmap, and the options you want.
4. **Handle result**: The suspend function returns a new, enhanced Bitmap on success or throw an exception on failure.
5. **Release session** : Crucially, call `session.release()` when you are finished to free up GPU resources.

The `EnhancementSession` is a heavyweight context object that maintains a
persistent GPU or NPU memory pipeline. It allocates dedicated video RAM (VRAM)
and native system handles. To prevent severe memory leaks and potential
`OutOfMemoryError` crashes, adhere to the following lifecycle principles:

1. **Lazy instantiation**: Don't create a session until the user initiates an enhancement action.
2. **Strategic reuse**: Maintain and reuse a single session instance when processing multiple images with identical configurations (dimensions and toggled options).
3. **Prompt teardown** : Invoke `session.release()` immediately when visual tasks terminate to free shared hardware resources.

## Initialize the enhancement engine

This method orchestrates a two-step check. It verifies if the device's hardware
supports acceleration, and then ensures the required machine learning modules
are present.

Running this as a prerequisite step prevents runtime initialization failures by
validating capabilities before your app attempts to process media.

    class MediaSetupViewModel(application: Application) : AndroidViewModel(application) {
        private val enhancementClient = Enhancement.getClient(application)
        fun initializeEnhancementEngine() {
            viewModelScope.launch {
                try {
                    // 1. Verify hardware capability
                    val isSupported = enhancementClient.isDeviceSupportedAsync()
                    if (!isSupported) {
                        notifyUiDeviceIncompatible()
                        return@launch
                    }
                    // 2. Verify and download the Google Play services ML modules
                    val isInstalled = enhancementClient.isModuleInstalledAsync()
                    if (!isInstalled) {
                        notifyUiDownloadingModels()
                        enhancementClient.installModule().await() 
                    }
                    notifyUiEngineReady()
                } catch (e: Exception) {

                    // Handle potential errors during session creation or image processing.
                    handleInitializationError(e)
                }
            }
        }
    }

## Create session and bitmap process wrappers

Use these Kotlin coroutine wrappers to convert task-based client callbacks into
standard suspending functions, enabling cleaner and sequential execution.

    // Wraps the task-based createSession callback into a suspending function.
    suspend fun EnhancementClient.createSessionAsync(
        options: EnhancementOptions,
        executor: Executor
    ): EnhancementSession = withContext(Dispatchers.Main) {
        suspendCancellableCoroutine { continuation ->

            // EnhancementSessionCallback handles session success or failure.
            val callback = object : EnhancementSessionCallback {
                override fun onSessionCreated(session: EnhancementSession) {
                    continuation.resume(session)
                }
                override fun onSessionCreationFailed(status: Status) {
                    continuation.resumeWithException(
                        Exception("Session creation failed: ${status.statusMessage} (${status.statusCode})")
                    )
                }
                override fun onSessionDestroyed() {}
                override fun onSessionDisconnected(status: Status) {}
            }

            // Handles errors during the initial request trigger.
            this.createSession(options, callback).addOnFailureListener(executor) { e ->
                if (continuation.isActive) {
                    continuation.resumeWithException(e)
                }
            }
        }
    }

    // Wraps this process in a suspending function for cleaner execution.
    suspend fun EnhancementSession.processBitmapAsync(
        bitmap: Bitmap,
        options: EnhancementOptions
    ): Bitmap = suspendCancellableCoroutine { continuation ->

        // EnhancementCallback returns the processed bitmap or an error code.
        val callback = object : EnhancementCallback {
            override fun onBitmapProcessed(enhancedBitmap: Bitmap) {
                continuation.resume(enhancedBitmap)
            }
            override fun onError(statusCode: Int) {
                continuation.resumeWithException(
                    Exception("Bitmap processing failed with status code: $statusCode")
                )
            }
            override fun onSurfaceProcessed(timestamp: Long) {}
        }
        this.process(bitmap, options, callback)
    }

## Execute the bitmap pipeline in a `ViewModel`

To integrate the enhancement pipeline into your application architecture, use a
`ViewModel` to manage the session lifecycle. This approach ensures that the
heavy GPU resources are released when the `ViewModel` is cleared.

    // Define a data class to hold image information.
    data class ImageInfo(val bitmap: Bitmap)
    // Define a UI state class to hold loading status, errors, and enhanced image.
    data class EnhancementUiState(
        val isLoading: Boolean = false,
        val enhancementError: String? = null,
        val enhancedImage: ImageInfo? = null
    )

    class EnhancementViewModel(application: Application) : AndroidViewModel(application) {

        // Backing field for UI state, initialized with default values.
        private val _uiState = MutableStateFlow(EnhancementUiState())
        // Publicly exposed UI state flow for observation.
        val uiState: StateFlow<EnhancementUiState> = _uiState.asStateFlow()

    // Initialize client to interact with the Media Enhancement service.
        private val enhancementClient: EnhancementClient = Enhancement.getClient(application)

    // Single-thread executor for processing background enhancement tasks.
        private val enhancementExecutor = Executors.newSingleThreadExecutor()

    // Track session state to enable reuse across multiple processing calls.
        private var enhancementSession: EnhancementSession? = null

    // Primary function to trigger the enhancement workflow for a provided bitmap.
        fun enhanceImage(bitmap: Bitmap) {
            viewModelScope.launch(Dispatchers.IO) {
                _uiState.update { it.copy(isLoading = true, enhancementError = null) }
                try {
                    // 1. Establish the session lazily on demand

    // Define enhancement options (for example, enable upscale, tonemapping) based
    // on bitmap dimensions.
                    if (enhancementSession == null) {
                        val options = EnhancementOptions(
                            bitmap.width,
                            bitmap.height,
                            EnhancementMode.BITMAP,
                            enableTonemap = true,
                            enableDeblurDenoise = true,
                            enableDenoiseOnly = false,
                            enableUpscale = false,
                        )
                        enhancementSession = enhancementClient.createSessionAsync(options, enhancementExecutor)
                    }
                    val session = enhancementSession ?: throw IllegalStateException("Session unavailable.")
                    // 2. Dispatch image through the neural pipeline
                    val enhancedBitmap = session.processBitmapAsync(bitmap, session.defaultOptions)
                    // 3. Render output to UI
                    _uiState.update {
                        it.copy(enhancedImage = ImageInfo(bitmap = enhancedBitmap))
                    }
                } catch (e: Exception) {
                    _uiState.update { it.copy(enhancementError = e.message) }
                } finally {

    // Ensure loading state is reset regardless of the outcome.
                    _uiState.update { it.copy(isLoading = false) }
                }
            }
        }
        override fun onCleared() {
            // 4. Critical: Release native GPU hardware resources
            enhancementSession?.release()
            enhancementSession = null
            enhancementExecutor.shutdown()
            super.onCleared()
        }
    }