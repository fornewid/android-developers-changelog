---
title: https://developer.android.com/docs/quality-guidelines/build-for-billions/connectivity
url: https://developer.android.com/docs/quality-guidelines/build-for-billions/connectivity
source: md.txt
---

# Connectivity for billions

Over half of all users worldwide will experience your app over a 2G connection. To improve their experience, optimize for low-speed connections and offline working by storing data, queuing requests, and handling images for optimal performance.

Here you can find some tips on how to accomplish these things.

## Optimize images

There are a number of ways to make images easier to download. These include serving WebP images, dynamically sizing images, and using image-loading libraries.

### Serve WebP images

- Serve[WebP](https://developers.google.com/speed/webp/)files over the network to reduce image load times and save network bandwidth. A WebP file is often smaller in size than its PNG and JPG counterparts, with at least the same image quality. Even using lossy settings, WebP can produce a nearly identical image to the original. Android has included lossy[WebP support](https://developer.android.com/guide/topics/media/media-formats#image-formats)since Android 4.0 (API level 14: Ice Cream Sandwich) and support for lossless, transparent WebP since Android 4.2 (API level 17: Jelly Bean).

### Dynamically size images

- Have your apps request images at the target rendering size, based on the device specification, and your server provide appropriately sized images. Doing this minimizes the data sent over the network and reduces the amount of memory needed to hold each image, resulting in improved performance and user satisfaction.
- User experience degrades when users have to wait for images to download. Using appropriate image sizes helps to address these issues. Consider making image size requests based on network type or network quality; this size could be smaller than the target rendering size.
- Dynamic placeholders such as[pre-computed palette values](https://developer.android.com/reference/androidx/palette/graphics/Palette)or low-resolution thumbnails can improve the user experience while the image is being fetched.

### Use image loading libraries

- Your app should not fetch any image more than once. Image loading libraries such as[Glide](https://github.com/bumptech/glide)and[Picasso](http://square.github.io/picasso/)fetch the image, cache it, and provide hooks into your Views to show placeholder images until the actual images are ready. Because images are cached, these libraries return the local copy the next time an image is requested.
- Image-loading libraries manage their cache, holding onto the most recent images so that your app storage doesn't grow indefinitely.

## Optimize networking

You can enhance the user experience by providing an optimal network experience. For example, you can make your app usable offline, use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)and[Room](https://developer.android.com/topic/libraries/architecture/room), and deduplicate network requests.

### Make your app usable offline

- In rural location and less affluent areas, it's common for devices to lose network connectivity. Creating a useful offline state means users can interact with your app at all times. Do this by storing data locally, caching data, and queuing outbound requests to action when connectivity is restored.
- Where possible, apps shouldn't notify users that connectivity has been lost. It's only when the user performs an operation where connectivity is essential that the user needs to be notified.
- When a device lacks connectivity, your app should batch up network requests---on behalf of the user---that can be executed when connectivity is restored. An example of this is an email client that allows users to compose, send, read, move, and delete existing mails even when the device is offline. These operations can be cached and executed when connectivity is restored. In doing so, the app is able to provide a similar user experience whether the device is online or offline.

### Use Room to fetch and cache data

- Ensure that your app stores all data on disk using a database or similar structure so that it performs optimally regardless of network conditions. Use the[Room persistence library](https://developer.android.com/topic/libraries/architecture/room)to cache data in a local database, and use[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)to update that cache when the device has a network connection.
- Apps should cache content that is fetched from the network. Before making subsequent requests, apps should display locally cached data. This ensures that the app is functional regardless of whether the device is offline or on a slow or unreliable network.

### Deduplicate network requests

- An offline-first architecture initially tries to fetch data from local storage and, failing that, requests the data from the network. After being retrieved from the network, the data is cached locally for future retrieval. This helps to ensure that network requests for the same piece of data only occur once---with subsequent requests satisfied locally. To achieve this, use a local database for long-lived data (usually[android.database.sqlite](https://developer.android.com/reference/android/database/sqlite/package-summary)or[SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)).
- This architecture also simplifies an app's flow between offline and online states as one side fetches from the network to the cache, while the other retrieves data from the cache to present to the user.
- For transitory data, use a bounded disk cache such as a[`DiskLruCache`](https://github.com/JakeWharton/DiskLruCache). Data that doesn't typically change should only be requested once over the network and cached for future use. Examples of such data are images and non-temporal documents like news articles or social posts.

## Fine-tune data transfer

There are several ways in which your app can adapt to network conditions to provide a better user experience. For example, it can prioritize network requests to minimize the user's waiting time for information. It can also detect and adapt to slower network speeds and changes that may take place in the network connection.

### Prioritize bandwidth

- You shouldn't assume that any network that the device is connected to is long-lasting or reliable. For this reason, apps should prioritize network requests to display the most useful information to the user as soon as possible.
- Presenting users with visible and relevant information immediately is a better user experience than making them wait for information that might not be necessary. This reduces the time that the user has to wait and increases the usefulness of the app on slow networks.
- To achieve this, sequence your network requests such that text is fetched before rich media. Text requests tend to be smaller, compress better, and hence transfer faster, meaning that your app can display useful content quickly. For more information on managing network requests, visit the Android training on[Managing Network Usage](https://developer.android.com/training/basics/network-ops/managing).

### Use less bandwidth on slower connections

- The ability for your app to transfer data in a timely fashion is dependent on the network connection. Detecting the quality of the network and adjusting the way your app uses it can help provide an excellent user experience.
- You can use the following methods to detect the underlying network quality. Using the data from these methods, your app should tailor its use of the network to continue to provide a timely response to user actions:
  - [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)\>[isActiveNetworkMetered()](https://developer.android.com/reference/android/net/ConnectivityManager#isActiveNetworkMetered())
  - [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)\>[getActiveNetworkInfo()](https://developer.android.com/reference/android/net/ConnectivityManager#getActiveNetworkInfo())
  - [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)\>[getNetworkCapabilities(Network)](https://developer.android.com/reference/android/net/ConnectivityManager#getNetworkCapabilities(android.net.Network))
  - [TelephonyManager](https://developer.android.com/reference/android/telephony/TelephonyManager)\>[getNetworkType()](https://developer.android.com/reference/android/telephony/TelephonyManager#getNetworkType())
- On slower connections, consider downloading only lower-resolution media or perhaps none at all. This ensures that your users can use the app on slow connections. Where you don't have an image or the image is still loading, you should always show a placeholder. You can create a dynamic placeholder by using the[Palette library](https://developer.android.com/training/material/palette-colors)to generate placeholder colors that match the target image.
- On devices powered by Android 7.0 (API level 24) and higher, users can turn on the**Data Saver** setting, which helps minimize data use. Android 7.0 extends[ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)to detect**Data Saver** settings. For more information about this feature, see[Data Saver.](https://developer.android.com/training/basics/network-ops/data-saver)

### Detect network changes, then change app behavior

- Network quality is not static; it changes based on location, network traffic, and local population density. Apps should detect changes in network and adjust bandwidth accordingly. By doing so, your app can tailor the user experience to the network quality. Detect network state using these methods:
  - [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)\>[getActiveNetworkInfo()](https://developer.android.com/reference/android/net/ConnectivityManager#getActiveNetworkInfo())
  - [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)\>[getNetworkCapabilities(Network)](https://developer.android.com/reference/android/net/ConnectivityManager#getNetworkCapabilities(android.net.Network))
  - [TelephonyManager](https://developer.android.com/reference/android/telephony/TelephonyManager)\>[getDataState()](https://developer.android.com/reference/android/telephony/TelephonyManager#getDataState())
- As the network quality degrades, scale down the number and size of requests. As the connection quality improves, you can scale up your requests to optimal levels.
- On higher quality, unmetered networks, consider[prefetching data](https://developer.android.com/training/efficient-downloads/efficient-network-access#PrefetchData)to make it available ahead of time. From a user experience standpoint, this might mean that news reader apps fetch three articles at a time on 2G but fetch twenty articles at a time on Wi-Fi. For more information on adjusting app behavior based on network changes, visit the Android training on[Monitoring the Connectivity Status](https://developer.android.com/training/monitoring-device-state/connectivity-monitoring).
- The broadcast[`CONNECTIVITY_CHANGE`](https://developer.android.com/reference/android/net/ConnectivityManager#CONNECTIVITY_ACTION)is sent when a change in network connectivity occurs. When your app is in the foreground, you can call[`registerReceiver`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter))to receive this broadcast. After receiving the broadcast, you should reevaluate the current network state and adjust your UI and network use appropriately. You shouldn't declare this receiver in your manifest, as it's unavailable in Android 7.0 (API level 24) and higher. For more information about this and other changes in Android 7.0, see[Android 7.0 Changes](https://developer.android.com/about/versions/nougat/android-7.0-changes).

## Related

## Additional resources

To learn more about supporting a variety of connection speeds, view the following resource:

### Blog post

- [Connect, No Matter the Speed](https://medium.com/google-design/connect-no-matter-the-speed-3b81cfd3355a)