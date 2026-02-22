---
title: https://developer.android.com/training/tv/playback/memory
url: https://developer.android.com/training/tv/playback/memory
source: md.txt
---

# Optimize memory usage

Memory optimization is crucial for ensuring smooth performance, preventing app crashes, and maintaining system stability and platform health. While memory usage should be monitored and optimized in every app,**content apps for TV**devices have specific challenges that differ from typical Android apps for handheld devices.

High memory consumption can lead to problems with app and system behaviors including:

- **The app itself**can become slow or laggy, or in the worst case, get killed.
- **User-visible system services**(Volume Control, Picture Settings dashboard, Voice Assistant, etc.) become very laggy or may not work at all.
- **The[low memory killer (LMK) daemon process](https://developer.android.com/topic/performance/memory-management#low-memory_killer)**may react to high memory pressure by killing the least essential processes; then these components may restart shortly after, triggering spikes of further resource contention which can directly impact the foreground app.
- **Transition to the Launcher**can be significantly delayed, and leave the foreground app appearing unresponsive until the transition finishes.
- **The system may begin using[direct reclaim](https://developer.android.com/training/tv/playback/memory#direct-reclaim)**, temporarily pausing a threads execution whilst waiting for memory allocation. This can happen to any thread such as the main thread or codec related threads potentially causing audio and video frame drops, and UI glitches.

## Memory considerations on TV Devices

TV devices typically have considerably less memory than phones or tablets.**For example, a configuration we can see on TV is 1 GB of RAM and 1080p video resolution**. At the same time, most TV apps have similar features; therefore similar implementation and common challenges. These two situations present problems not seen in other device types and apps:

- Media TV apps are usually composed of both**gridded image views** and**fullscreen background images**which require loading a lot of images into memory in a short period of time
- TV apps**play multimedia streams**which require to allocate a certain amount of memory to play video and audio and need considerable media buffers to ensure smooth playback.
- Additional media features (seeking, episode change, audio track change, etc.) can take additional memory pressure if not implemented properly.

## Understand TV devices

This guide primarily focuses on app memory usage and memory targets for low-RAM devices.

On TV devices, consider these characteristics:

- **Device memory**: The amount of Random Access Memory (RAM) the device has installed.
- **Device UI resolution**: The resolution the device uses to render the OS and Applications UI; this is typically lower than the device video resolution.
- **Video resolution**: The maximum resolution the device can play videos at.

This leads to categorizing different device types and how memory should be used by them.

#### TV devices summary

| **Device memory** | **Device video resolution** | **Device UI resolution** | **isLowRAMDevice()** |
|-------------------|-----------------------------|--------------------------|----------------------|
| 1 GB              | 1080p                       | 720p                     | Yes                  |
| 1.5 GB            | 2160p                       | 1080p                    | Yes                  |
| ≥1.5 GB           | 1080p                       | 720p or 1080p            | No\*                 |
| ≥2 GB             | 2160p                       | 1080p                    | No\*                 |

| **Note:** Additional situations may let OEMs to define[`ActivityManager.isLowRAMDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())if the device is memory constrained. Always use the`islowRAMDevice()`flag to check this situation, rather than manually checking memory or device resolution.

### Low-RAM TV devices

These devices are in a**memory constrained situation** and will report[`ActivityManager.isLowRAMDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())to true. Applications which are running on low-RAM TV devices need to implement**additional memory control measures**.

We consider devices with the following characteristics to fall into this category:

- **1 GB devices**: 1 GB of RAM, 720p/HD (1280x720) UI resolution, 1080p/FullHD (1920x1080) Video resolution
- **1.5 GB devices**: 1.5 GB of RAM, 1080p/FullHD (1920x1080) UI resolution, 2160p/UltraHD/4K (3840x2160) Video resolution
- Other situations in which the OEM defined the[`ActivityManager.isLowRAMDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())flag due to additional memory constraints.

| **Note:** We will use**720p, 1080p and 2160p**in this document to refer to resolutions of the UI and video layers.

### Regular TV devices

These devices don't suffer such a significant memory pressure situation. We consider these devices to have the following characteristics:

- ≥1.5 GB of RAM, 720p or 1080p UI and 1080p video resolution
- ≥2 GB of RAM, 1080p UI and 1080p or 2160p video resolution

This doesn't mean apps shouldn't care about memory usage on these devices, as some specific memory misuse**can still exhaust available memory**and perform poorly.

## Memory targets on low-RAM TV devices

When measuring memory on these devices, we**strongly recommend** monitoring every section of the memory using the[Android Studio memory profiler](https://developer.android.com/studio/profile/memory-profiler). TV apps should profile their memory usage and work to put their categories below the thresholds we define in this section.

![memory profiler](https://developer.android.com/studio/images/profile/memory-profiler-allocations-jvmti_2x.png)

In the[How memory is counted](https://developer.android.com/studio/profile/memory-profiler#how-counted)section you'll find a detailed explanation of the reported memory figures.**For the definition of thresholds for TV apps**, we will focus on three memory categories:

- **Anonymous + Swap**: Composed of Java + Native + Stack allocation memory in Android Studio.
- **Graphics**: Directly reported on the profiler tool. Generally composed of graphics textures.
- **File**: Reported as "Code" + "Others" categories in Android Studio.

| **Note:** The*Anonymous + Swap* terminology refers to the kernel categories reported in`/proc/PID/status`.

With these definitions, the following table indicates the maximum value each type of memory group should use:

|             **Memory type**              |                                    **Purpose**                                    | **Usage targets (1 GB)** |
|------------------------------------------|-----------------------------------------------------------------------------------|--------------------------|
| Anonymous + Swap (Java + Native + Stack) | Used for allocations, media buffers, variables, and other memory-intensive tasks. | **\< 160 MB**            |
| Graphics                                 | Used by the GPU for textures and display related buffers                          | **30-40 MB**             |
| File                                     | Used for code pages and files in memory.                                          | **60-80 MB**             |

| **Note:** These values are to be maintained on average values and recommended on peak values. You may reach the limit in one category as long as you then keep it down on other. Make sure the total memory doesn't go higher than the limit provided in this guide.

The**maximum total memory** (Anon+Swap + Graphics + File)**must not**exceed the following:

- **280 MB** of total memory usage (**Anon+Swap + Graphics + File**) for 1 GB low-RAM devices.

It is**strongly recommended**not to exceed:

- **200 MB** of memory usage on (**Anon+Swap + Graphics**).

| **Note:** These values for peak memory usage assumes the app has no active bindings (except to processes which were already present and classified as**Perceptible** ,**Foreground** ,**Persistent** or**System** in the[low memory killer](https://developer.android.com/topic/performance/memory-management#low-memory_killer)categorization). They also assume a single video stream. Decoding multiple streams can increase system memory usage, which will decrease the acceptable memory usage for the app.

#### File memory

As**general guidance**for file backed memory be aware that:

- In general file memory is handled well by OS memory management.
- We have not found it to be a major cause of memory pressure at this moment.

However, when dealing with File memory in general:

- **Don't include unused libraries**into your build, and use small subsets of libraries rather than the complete ones when possible.
- **Don't keep large files opened**into memory and release them as soon as you are done with them.
- **Minimize your compiled code size** for Java and Kotlin classes, see the[Shrink, obfuscate, and optimize your app](https://developer.android.com/build/shrink-code)guide.

## Specific TV recommendations

This section provides specific recommendations for optimizing memory usage on TV devices.

### Graphics memory

| **Note:** Some devices, specially the older ones, won't properly report graphics memory. If you don't see the graphic counters in Android Studio memory profiler, they could be not reported at all on the total memory count. If you encounter this situation, you must use another device which has complete graphics reporting capability to profile your app.

Use appropriate image formats and resolutions.

- **Do not load images with higher resolution than the device UI resolution.**For example, 1080p images should be downsized to 720p on a 720p UI device.
- **Use hardware-backed bitmaps** when possible.
  - On libraries like Glide, enable the[`Downsampler.ALLOW_HARDWARE_CONFIG`](https://bumptech.github.io/glide/doc/hardwarebitmaps.html#how-do-we-enable-hardware-bitmaps)feature which is disabled by default. Enabling this avoids duplicating bitmaps which otherwise would be in both graphics memory and anonymous memory.
- **Avoid intermediate renders** and re-renders
  - These can be identified with[Android GPU Inspector](https://developer.android.com/agi):
  - Look on the "Textures" section for images that are steps towards the final render rather than being only the elements forming them, this is commonly a so called*"intermediate render".*
  - For Android SDK applications you can often remove these by using the layout flag[`forceHasOverlappedRendering:false`](https://developer.android.com/reference/android/view/View#attr_android:forceHasOverlappingRendering)to disable intermediate renders for this layout.
  - See[Avoid Overlapping Renders](https://www.youtube.com/watch?v=wIy8g8yNhNk)on overlapping renders as a great resource.
- **Avoid loading placeholder images** when possible, use[`@android:color/`](https://developer.android.com/reference/android/graphics/Color)or[`@color`](https://developer.android.com/reference/android/graphics/Color)for placeholder textures.
- **Avoid compositing multiple images**on the device when the composition could be performed offline. Prefer to load standalone images rather than doing image composition from downloaded images
- Follow the[Handling bitmaps](https://developer.android.com/develop/ui/views/graphics)guide to better deal with Bitmaps.

### Anon+Swap memory

**Anon+Swap** is composed of Native + Java + Stack allocations in Android Studio memory profiler. Use[`ActivityManager.isLowMemoryDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())to check if the device is memory constrained, and adapt to this situation following these guidelines.

- **Media:**
  - **Specify a variable size for media buffers** depending on the device RAM and**video playback resolution** . This should account for 1 minute of video playback:
    1. **40-60 MB**for 1 GB / 1080p
    2. **60-80 MB**for 1.5 GB / 1080p
    3. **80-100 MB**for 1.5 GB / 2160p
    4. **100-120 MB**for 2 GB / 2160p
  - **Free media memory allocations when changing an episode**to prevent increases in the total amount of Anonymous memory.
  - **Release and stop media resources immediately** when you app gets stopped: Use the activity[lifecycle callbacks](https://developer.android.com/guide/components/activities/activity-lifecycle)to handle audio and video resources. If you are not an audio app,**stop your playback** when[`onStop()`](https://developer.android.com/guide/components/activities/activity-lifecycle#onstop)happens on your activities, save all the work you are performing and set your resources to be released. To schedule work you may need later. See the[Jobs and Alarms](https://developer.android.com/training/tv/playback/memory#jobs-and-alarms)section.
    - You can use[lifecycle aware components](https://developer.android.com/topic/libraries/architecture/lifecycle)like[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)and[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)to help you deal with Activity lifecycle calls.
    - To make your work Lifecycle aware, you can also use[Kotlin coroutines](https://developer.android.com/topic/libraries/architecture/coroutines)and[Kotlin flows](https://developer.android.com/kotlin/flow).
  - **Pay attention to the buffer's memory when video seeking** : Developers often allocate additional 15-60s of future content when seeking to have video ready for the user, but this creates additional memory overhead. In general, don't take more than 5s of future buffer until the user has selected the new video position. If you strictly need to pre-buffer additional time while seeking, make sure to:
    - Allocate the seeking buffer ahead of time and reuse it.
    - The buffer size should be no bigger than**15-25 MB**(depending on the device memory).
- **Allocations:**
  - Use the[graphics memory guidance](https://developer.android.com/training/tv/playback/memory#graphics-memory)to ensure you**don't duplicate images in Anonymous memory**
    - Images are often the biggest user of memory so duplication of them can put a lot of pressure on the device. This is especially true during heavy navigation of image gridviews.
  - **Release allocations by dropping their references when moving screens**: Ensure there are no references to bitmaps and objects left behind.
- **Libraries:**
  - **Profile memory allocations from libraries** when adding new ones, as they may load additional libraries as well, which may also make allocations and create[Bindings](https://developer.android.com/training/tv/playback/memory#bindings).
- **Networking:**
  - **Do not perform blocking network calls during app startup**, they slow down the application startup time and create additional memory overhead at launch, where memory is particularly constrained by the app load. Show a loading or splash screen first and do network requests once the UI is in place.

### Bindings

[Bindings](https://developer.android.com/develop/background-work/services/bound-services)**introduce additional memory overhead** as they**bring other applications into memory** or**increase the memory consumption of the bound app** (if it is in memory already) to facilitate the API call. This, as a result,**reduces the available memory** for the foreground app. When binding a service, be mindful of when and how long you are using the binding. Make sure to**release the binding**as soon as it's not needed.

**Typical bindings**and best practices:

- [Play integrity API](https://developer.android.com/google/play/integrity): Used to check for device integrity
  - Check for device integrity after the loading screen and before media playback
  - Release references to PlayIntegrity[`StandardIntegrityManager`](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager)before playing content.
- [Play Billing Library](https://developer.android.com/distribute/play-billing): Used for managing subscriptions and purchases using Google Play
  - Initialize the library after the loading screen, and handle all the billing work before playing any media.
  - Use[`BillingClient.endConnection()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#endConnection())when done using the library and always before playing video or media.
  - Use[`BillingClient.isReady()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isReady())and[`BillingClient.getConnectionState()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#getConnectionState())to check if the service was disconnected in case any billing work needs to be done again, and then do[`BillingClient.endConnection()`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient#endConnection())again after finishing.
- [GMS FontsProvider](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts)
  - Prefer to use standalone fonts on low-RAM devices rather than using fonts provider, as downloading the fonts is costly and FontsProvider will bind services to do it.
- [Google Assistant](https://developer.android.com/develop/devices/assistant/overview)library: Sometimes used for search and in-app search, if possible, replace this library.
  - **For leanback apps** : Use Gboard text to speech or[androidx.leanback](https://developer.android.com/training/tv/get-started/create#tv-libraries)library.
    - Follow[Search guidelines](https://developer.android.com/training/tv/discovery/in-app-search#kotlin)for implementing search.
    - Note:**leanback is deprecated**and apps should move to TV Compose.
  - **For Compose apps** :
    - Use Gboard text to speech to implement voice search.
  - Implement[Watch Next](https://developer.android.com/training/tv/discovery/watch-next-add-programs)to make media content in your app discoverable.

### Foreground Services

[Foreground Services](https://developer.android.com/develop/background-work/services/foreground-services)are a special type of service which is tied to a notification. This notification is displayed on the notification tray on phones and tablets, but TV devices don't have a notification tray in the same sense as those devices. Even if[Foreground Services](https://developer.android.com/develop/background-work/services/foreground-services)are useful because they can be kept running while the application is in the background, TV apps must follow these guidelines:

In Android TV and Google TV, Foreground Services are**only allowed**to keep running once the user leaves the app:

- **For[audio apps](https://developer.android.com/develop/background-work/services/fg-service-types#media):** Foreground Services are**only allowed**to keep running once the user leaves the app to keep playing the audio track. The service must be stopped immediately after audio playback ends.
- **For any other app:** **[all Foreground Services must be stopped](https://developer.android.com/develop/background-work/services/foreground-services#remove-from-foreground)** .**once the user leaves your app**, as there is no notification to notify the user that the app is still running and consuming resources.
- **For background jobs** such as updating recommendations or[Watch Next](https://developer.android.com/training/tv/discovery/watch-next-add-programs), use[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started).

### Jobs and Alarms

[`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started)is the state-of-the-art Android API for scheduling background recurring jobs. WorkManager will use the new[`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler)when available (SDK 23+) and the old[`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager)when it's not. For best practices performing scheduled jobs on TV follow these recommendations:

- **Avoid** using the[`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager)APIs, on SDK 23+, especially[`AlarmManager.set()`](https://developer.android.com/reference/android/app/AlarmManager#set(int,%20long,%20android.app.PendingIntent)),[`AlarmManager.setExact()`](https://developer.android.com/reference/android/app/AlarmManager#setExact(int,%20long,%20android.app.PendingIntent))and similar methods, as they don't allow the system to decide the proper time to run the jobs (as an example, when the device is idling).
- On low-RAM devices, avoid running jobs unless strictly necessary. If needed, use WorkManager[`WorkRequest`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work)**only for updating recommendations after playback**, and try to do so while the app is still open.
- Define WorkManager[`Constraints`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#work-constraints)to let the system run your jobs when the time is appropriate:

### Kotlin

    Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .setRequiresStorageNotLow(true)
        .setRequiresDeviceIdle(true)
        .build()

### Java

    Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .setRequiresStorageNotLow(true)
        .setRequiresDeviceIdle(true)
        .build()

| **Note:** It's particularly important to call`setRequiresDeviceIdle(true)`for low-RAM devices.

- If you must run jobs regularly (for example, to update[Watch Next](https://developer.android.com/training/tv/discovery/watch-next-add-programs)based on a user's content watching activity in your app on another device), then keep memory use down keeping the job's memory consumption**below 30 MB**.

## General memory considerations

Following guidelines provide general information on Android App development:

- Minimize object allocations, optimize object re-use and de-allocate any unused objects promptly.
  - **Do not hold references**to objects, especially bitmaps.
  - Avoid using[`System.gc()`](https://developer.android.com/reference/java/lang/System#gc())and direct release memory calls as they interfere with the system's memory handling process: As an example, in devices using zRAM, a forced call to`gc()`can temporarily increase memory usage due to the compression and decompression of the memory.
  - Use[`LazyList`](https://developer.android.com/develop/ui/compose/lists#lazy)such as demonstrated in a[catalog browser](https://developer.android.com/training/tv/playback/compose/browse)in Compose or[`RecyclerView`](https://developer.android.com/develop/ui/views/layout/recyclerview)in the now deprecated Leanback UI toolkit to reutilize views and not re-create list elements.
  - Cache locally elements read from external content providers which are unlikely to change and define updating intervals that prevent allocating additional external memory.
- Check for possible memory leaks.
  - **Watch out** for typical**memory leak**cases such as references inside anonymous threads, reallocation of video buffers which never get released, and other similar situations.
  - Use[heap dump](https://developer.android.com/studio/profile/memory-profiler#capture-heap-dump)to debug memory leaks.
- Generate[baseline profiles](https://developer.android.com/topic/performance/baselineprofiles/overview)to minimize the amount of just-in-time compilation is needed when executing your app on a cold start.

## Understanding direct memory reclaim

When an Android TV application requests memory and the system is under pressure, the Linux kernel, which underpins Android, may have to use**direct memory reclaim**.

The process involves**pausing any allocating thread entirely**to wait for freed up memory pages. This occurs when background reclaim is not able to maintain a sufficient pool of memory proactively.

This can lead to**noticeable pauses or jank** in the user experience as the system pauses allocating threads until sufficient memory is made available. In this sense, allocating threads are not limited to application code calls like`malloc()`; memory needs to be allocated to page in code pages, for example.
| **Note:** While necessary to prevent out-of-memory errors, frequent direct memory reclaim indicates that the system is consistently running with insufficient free memory, suggesting that applications may be using too much memory.

## Tools summary

- Use[Android Studio memory profiler](https://developer.android.com/studio/profile/memory-profiler)tool to check for your memory consumption during usage.
  - Use[heapdump](https://developer.android.com/studio/profile/memory-profiler#capture-heap-dump)to check specific object and bitmap allocations.
  - Use[native memory profiler](https://developer.android.com/studio/profile/memory-profiler#native-memory-profiler)to check non Java or Kotlin allocations.
- Use[Android GPU Inspector](https://developer.android.com/agi)to check graphics allocations.