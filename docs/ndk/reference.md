---
title: Android NDK API Reference  |  Android Developers
url: https://developer.android.com/ndk/reference
source: html-scrape
---

* [Home](https://developer.android.com/)
* [NDK](https://developer.android.com/ndk)
* [Develop](https://developer.android.com/develop)
* [Reference](https://developer.android.com/ndk/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# Android NDK API Reference

| Modules | |
| --- | --- |
| [API Levels](/ndk/reference/group/apilevels) | Defines functions for working with Android API levels. |
| [Android Image Decoder](/ndk/reference/group/image-decoder) | Functions for converting encoded images into RGBA pixels. |
| [Asset](/ndk/reference/group/asset) |  |
| [Audio](/ndk/reference/group/audio) |  |
| [Bitmap](/ndk/reference/group/bitmap) |  |
| [Camera](/ndk/reference/group/camera) |  |
| [Choreographer](/ndk/reference/group/choreographer) | Choreographer coordinates the timing of frame rendering. |
| [Configuration](/ndk/reference/group/configuration) |  |
| [Data Space](/ndk/reference/group/a-data-space) | ADataSpace describes how to interpret colors. |
| [Dynamic Linker](/ndk/reference/group/libdl) |  |
| [File Descriptor](/ndk/reference/group/file-descriptor) |  |
| [Font](/ndk/reference/group/font) |  |
| [ICU4C](/ndk/reference/group/icu4c) |  |
| [Input](/ndk/reference/group/input) |  |
| [Logging](/ndk/reference/group/logging) |  |
| [Looper](/ndk/reference/group/looper) |  |
| [Media](/ndk/reference/group/media) |  |
| [Memory](/ndk/reference/group/memory) |  |
| [Midi](/ndk/reference/group/midi) |  |
| [Native Activity](/ndk/reference/group/native-activity) |  |
| [Native Hardware Buffer](/ndk/reference/group/a-hardware-buffer) | AHardwareBuffer objects represent chunks of memory that can be accessed by various hardware components in the system. |
| [Native Window](/ndk/reference/group/a-native-window) | ANativeWindow represents the producer end of an image queue. |
| [NdkBinder](/ndk/reference/group/ndk-binder) |  |
| [Networking](/ndk/reference/group/networking) |  |
| [NeuralNetworks](/ndk/reference/group/neural-networks) |  |
| [Performance Hint Manager](/ndk/reference/group/a-performance-hint) | APerformanceHint allows apps to create performance hint sessions for groups of threads, and provide hints to the system about the workload of those threads, to help the system more accurately allocate resources for them. |
| [Permission](/ndk/reference/group/permission) | Structures and functions related to permission checks in native code. |
| [Sensor](/ndk/reference/group/sensor) | Structures and functions to receive and process sensor events in native code. |
| [Storage](/ndk/reference/group/storage) |  |
| [SurfaceTexture](/ndk/reference/group/surface-texture) |  |
| [Sync](/ndk/reference/group/sync) |  |
| [SystemHealth](/ndk/reference/group/system-health) | SystemHealth provides access to data about how various system resources are used by applications. |
| [Thermal](/ndk/reference/group/thermal) |  |
| [Tracing](/ndk/reference/group/tracing) |  |

| Structs | |
| --- | --- |
| [AAdditionalInfoEvent](/ndk/reference/struct/a-additional-info-event) |  |
| [AAudioPlaybackParameters](/ndk/reference/struct/a-audio-playback-parameters) | Structure for common playback params. |
| [ACameraCaptureFailure](/ndk/reference/struct/a-camera-capture-failure) | Struct to describe a capture failure. |
| [ACameraCaptureSession\_captureCallbacks](/ndk/reference/struct/a-camera-capture-session-capture-callbacks) | ACaptureCaptureSession\_captureCallbacks structure used in [ACameraCaptureSession\_capture](/ndk/reference/group/camera#group___camera_1ga6099baf4316e44db1d5f133cdf02c838) and [ACameraCaptureSession\_setRepeatingRequest](/ndk/reference/group/camera#group___camera_1ga07aa2f8bb53c7c0d88c59c33848bb2d6). |
| [ACameraCaptureSession\_captureCallbacksV2](/ndk/reference/struct/a-camera-capture-session-capture-callbacks-v2) | This has the same functionality as [ACameraCaptureSession\_captureCallbacks](/ndk/reference/struct/a-camera-capture-session-capture-callbacks#struct_a_camera_capture_session__capture_callbacks), with the exception that captureCallback\_startV2 callback is used, instead of captureCallback\_start, to support retrieving the frame number. |
| [ACameraCaptureSession\_logicalCamera\_captureCallbacks](/ndk/reference/struct/a-camera-capture-session-logical-camera-capture-callbacks) | This has the same functionality as [ACameraCaptureSession\_captureCallbacks](/ndk/reference/struct/a-camera-capture-session-capture-callbacks#struct_a_camera_capture_session__capture_callbacks), with the exception that an onLogicalCameraCaptureCompleted callback is used, instead of onCaptureCompleted, to support logical multi-camera. |
| [ACameraCaptureSession\_logicalCamera\_captureCallbacksV2](/ndk/reference/struct/a-camera-capture-session-logical-camera-capture-callbacks-v2) | This has the same functionality as [ACameraCaptureSession\_logicalCamera\_captureCallbacks](/ndk/reference/struct/a-camera-capture-session-logical-camera-capture-callbacks#struct_a_camera_capture_session__logical_camera__capture_callbacks), with the exception that an captureCallback\_startV2 callback is used, instead of captureCallback\_start, to support retrieving frame number. |
| [ACameraCaptureSession\_stateCallbacks](/ndk/reference/struct/a-camera-capture-session-state-callbacks) | Capture session state callbacks used in [ACameraDevice\_createCaptureSession](/ndk/reference/group/camera#group___camera_1ga2d2cc252a4c3cb60ca0a85cb9d408191) and [ACameraDevice\_createCaptureSessionWithSessionParameters](/ndk/reference/group/camera#group___camera_1ga622c05d72ab1fcee2c5d9de91e4f0730). |
| [ACameraDevice\_StateCallbacks](/ndk/reference/struct/a-camera-device-state-callbacks) | Applications' callbacks for camera device state changes, register with [ACameraManager\_openCamera](/ndk/reference/group/camera#group___camera_1ga56ec3decad6c0734be7cc504b03acc41). |
| [ACameraIdList](/ndk/reference/struct/a-camera-id-list) | Struct to hold list of camera device Ids. |
| [ACameraManager\_AvailabilityListener](/ndk/reference/struct/a-camera-manager-availability-listener) | A listener for camera devices becoming available or unavailable to open. |
| [ACameraManager\_ExtendedAvailabilityListener](/ndk/reference/struct/a-camera-manager-extended-availability-listener) | A listener for camera devices becoming available/unavailable to open or when the camera access permissions change. |
| [ACameraMetadata\_const\_entry](/ndk/reference/struct/a-camera-metadata-const-entry) | A single read-only camera metadata entry. |
| [ACameraMetadata\_entry](/ndk/reference/struct/a-camera-metadata-entry) | A single camera metadata entry. |
| [ACameraMetadata\_rational](/ndk/reference/struct/a-camera-metadata-rational) | Definition of rational data type in [ACameraMetadata](/ndk/reference/group/camera#group___camera_1gabd236e2a05c30cf024d0a2b69dbed9f2). |
| [AColor\_xy](/ndk/reference/struct/a-color-xy) | Color is defined in CIE XYZ coordinates. |
| [ADoubleRange](/ndk/reference/struct/a-double-range) | A uitlity structure describing the range of two double values. |
| [ADynamicSensorEvent](/ndk/reference/struct/a-dynamic-sensor-event) |  |
| [AHardwareBuffer\_Desc](/ndk/reference/struct/a-hardware-buffer-desc) | Buffer description. |
| [AHardwareBuffer\_Plane](/ndk/reference/struct/a-hardware-buffer-plane) | Holds data for a single image plane. |
| [AHardwareBuffer\_Planes](/ndk/reference/struct/a-hardware-buffer-planes) | Holds all image planes that contain the pixel data. |
| [AHdrMetadata\_cta861\_3](/ndk/reference/struct/a-hdr-metadata-cta861-3) | CTA 861.3 "HDR Static Metadata Extension" static metadata. |
| [AHdrMetadata\_smpte2086](/ndk/reference/struct/a-hdr-metadata-smpte2086) | SMPTE ST 2086 "Mastering Display Color Volume" static metadata. |
| [AHeadTrackerEvent](/ndk/reference/struct/a-head-tracker-event) |  |
| [AHeadingEvent](/ndk/reference/struct/a-heading-event) |  |
| [AHeartRateEvent](/ndk/reference/struct/a-heart-rate-event) |  |
| [AImageCropRect](/ndk/reference/struct/a-image-crop-rect) | Data type describing an cropped rectangle returned by [AImage\_getCropRect](/ndk/reference/group/media#group___media_1gaa5aa50f209be212051f9b33be185cee9). |
| [AImageReader\_BufferRemovedListener](/ndk/reference/struct/a-image-reader-buffer-removed-listener) | A listener to the AHardwareBuffer removal event, use [AImageReader\_setBufferRemovedListener](/ndk/reference/group/media#group___media_1ga067af6087a020665eaf4eb6c4f756977) to register the listener object to AImageReader. |
| [AImageReader\_ImageListener](/ndk/reference/struct/a-image-reader-image-listener) |  |
| [AIntRange](/ndk/reference/struct/a-int-range) | A uitlity structure describing the range of two integer values. |
| [ALimitedAxesImuEvent](/ndk/reference/struct/a-limited-axes-imu-event) |  |
| [ALimitedAxesImuUncalibratedEvent](/ndk/reference/struct/a-limited-axes-imu-uncalibrated-event) |  |
| [ALogicalCameraCaptureFailure](/ndk/reference/struct/a-logical-camera-capture-failure) | Struct to describe a logical camera capture failure. |
| [AMediaCodecBufferInfo](/ndk/reference/struct/a-media-codec-buffer-info) |  |
| [AMediaCodecOnAsyncNotifyCallback](/ndk/reference/struct/a-media-codec-on-async-notify-callback) |  |
| [AMediaCodecSupportedMediaType](/ndk/reference/struct/a-media-codec-supported-media-type) | The media type definition with bitfeids indicating if it is supported by decoders/ encoders/ both. |
| [AMediaDrmByteArray](/ndk/reference/struct/a-media-drm-byte-array) |  |
| [AMediaDrmKeyStatus](/ndk/reference/struct/a-media-drm-key-status) |  |
| [AMediaDrmKeyValuePair](/ndk/reference/struct/a-media-drm-key-value-pair) | Data type containing {key, value} pair. |
| [AMetaDataEvent](/ndk/reference/struct/a-meta-data-event) |  |
| [ANativeActivity](/ndk/reference/struct/a-native-activity) | This structure defines the native side of an android.app.NativeActivity. |
| [ANativeActivityCallbacks](/ndk/reference/struct/a-native-activity-callbacks) | These are the callbacks the framework makes into a native application. |
| [ANativeWindow\_Buffer](/ndk/reference/struct/a-native-window-buffer) | Struct that represents a windows buffer. |
| [ANeuralNetworksOperandType](/ndk/reference/struct/a-neural-networks-operand-type) | [ANeuralNetworksOperandType](/ndk/reference/struct/a-neural-networks-operand-type#struct_a_neural_networks_operand_type) describes the type of an operand. |
| [ANeuralNetworksSymmPerChannelQuantParams](/ndk/reference/struct/a-neural-networks-symm-per-channel-quant-params) | Parameters for ANEURALNETWORKS\_TENSOR\_QUANT8\_SYMM\_PER\_CHANNEL operand. |
| [ARect](/ndk/reference/struct/a-rect) | Rectangular window area. |
| [ASensorEvent](/ndk/reference/struct/a-sensor-event) | Information that describes a sensor event, refer to [SensorEvent](/reference/android/hardware/SensorEvent) for additional documentation. |
| [ASensorVector](/ndk/reference/struct/a-sensor-vector) | A sensor event. |
| [AThermalHeadroomThreshold](/ndk/reference/struct/a-thermal-headroom-threshold) | This struct defines an instance of headroom threshold value and its status. |
| [AUncalibratedEvent](/ndk/reference/struct/a-uncalibrated-event) |  |
| [AndroidBitmapInfo](/ndk/reference/struct/android-bitmap-info) | Bitmap info, see [AndroidBitmap\_getInfo()](/ndk/reference/group/bitmap#group___bitmap_1ga80292ee39d8a675928e38849742b54bf). |
| [PsshEntry](/ndk/reference/struct/pssh-entry) | mapping of crypto scheme uuid to the scheme specific data for that scheme |
| [PsshInfo](/ndk/reference/struct/pssh-info) | list of crypto schemes and their data |
| [UParseError](/ndk/reference/struct/u-parse-error) | A [UParseError](/ndk/reference/struct/u-parse-error#struct_u_parse_error) struct is used to returned detailed information about parsing errors. |
| [UReplaceableCallbacks](/ndk/reference/struct/u-replaceable-callbacks) | A set of function pointers that transliterators use to manipulate a UReplaceable. |
| [UTransPosition](/ndk/reference/struct/u-trans-position) | Position structure for [utrans\_transIncremental()](/ndk/reference/group/icu4c#group__icu4c_1ga67160f7c04dc1af49d1f1aad2bcb0d49) incremental transliteration. |
| [\_\_android\_log\_message](/ndk/reference/struct/android-log-message) | Logger data struct used for writing log messages to liblog via \_\_android\_log\_write\_logger\_data() and sending log messages to user defined loggers specified in [\_\_android\_log\_set\_logger()](/ndk/reference/group/logging#group___logging_1ga0e29961fa7bd5904bfc142d795af1fd6). |
| [android\_dlextinfo](/ndk/reference/structandroid/dlextinfo) | Used to pass Android-specific arguments to [android\_dlopen\_ext()](/ndk/reference/group/libdl#group__libdl_1ga30dee587d0ce38e881572a1e5a99f17c). |
| [cryptoinfo\_pattern\_t](/ndk/reference/structcryptoinfo/pattern-t) |  |