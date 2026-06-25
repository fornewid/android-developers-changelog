---
title: https://developer.android.com/develop/connectivity/avoid-unoptimized-downloads
url: https://developer.android.com/develop/connectivity/avoid-unoptimized-downloads
source: md.txt
---

Some of your app's users have intermittent access to the internet or have limits
on the amount of information they can download onto their devices. You can
encourage users to interact with your app more often by reducing the amount of
data that your app needs to download.

The most fundamental way to reduce your downloads is to download only what you
need. In terms of data, that means implementing REST APIs that allow you to
specify query criteria that limit the returned data by using parameters such as
the time of your last update.

Similarly, when downloading images, it's good practice to reduce the size of
images server-side, rather than downloading full-sized images that are reduced
on the client.

## Cache HTTP responses

Another important technique is to avoid downloading duplicate data. You can
reduce the likelihood of downloading the same piece of data repeatedly by using
caching. By caching your app's data and resources, you create a local copy of
the information that your app needs to reference. If your app needs to access
the same piece of information multiple times over a short time period, you need
to download it into the cache only once.

It's important to cache as aggressively as possible in order to reduce the total
amount of data that you download. Always cache static resources, including
on-demand downloads such as full-size images, for as long as reasonably
possible. On-demand resources should be stored separately to enable you to
regularly flush your on-demand cache to manage its size.

To ensure that your caching doesn't result in your app displaying stale data,
use the appropriate [HTTP status codes and
headers](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#validating_cached_responses_with_etags),
such as the
[`ETag`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.3.2)
and
[`Last-Modified`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.3.1)
headers. This allows you to determine when the associated content should be
refreshed. For example:

### Kotlin

```kotlin
// url represents the website containing the content to place into the cache.
val conn: HttpsURLConnection = url.openConnection() as HttpsURLConnection
val currentTime: Long = System.currentTimeMillis()
val lastModified: Long = conn.getHeaderFieldDate("Last-Modified", currentTime)

// lastUpdateTime represents when the cache was last updated.
if (lastModified < lastUpdateTime) {
    // Skip update
} else {
    // Parse update
    lastUpdateTime = lastModified
}
```

### Java

```java
// url represents the website containing the content to place into the cache.
HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
long currentTime = System.currentTimeMillis();
long lastModified = conn.getHeaderFieldDate("Last-Modified", currentTime);

// lastUpdateTime represents when the cache was last updated.
if (lastModified < lastUpdateTime) {
    // Skip update
} else {
    // Parse update
    lastUpdateTime = lastModified;
}
```

You can configure some networking libraries to respect these status codes and
headers automatically. When using
[OkHttp](https://square.github.io/okhttp/), for example, configuring
a cache directory and cache size for the client will enable the library to use
HTTP caching, as shown in the following code sample:

### Kotlin

```kotlin
val cacheDir = Context.getCacheDir()
val cacheSize = 10L * 1024L * 1024L // 10 MiB
val client: OkHttpClient = OkHttpClient.Builder()
    .cache(Cache(cacheDir, cacheSize))
    .build()
```

### Java

```java
File cacheDir = Context.getCacheDir();
long cacheSize = 10L * 1024L * 1024L; // 10 MiB
OkHttpClient client = new OkHttpClient.Builder()
    .cache(new Cache(cacheDir, cacheSize))
    .build();
```

With the cache configured, you can serve fully-cached HTTP requests directly
from local storage, eliminating the need to open a network connection.
Conditionally-cached responses can validate their freshness from the server,
eliminating the bandwidth cost associated with the download. Uncached responses
get stored in the response cache for future requests.

You can cache non-sensitive data in the unmanaged external cache directory by
using
[`Context.getExternalCacheDir()`](https://developer.android.com/reference/android/content/Context#getExternalCacheDir()).
Alternatively, you can cache data in the managed, secure application cache by
using
[`Context.getCacheDir()`](https://developer.android.com/reference/android/content/Context#getCacheDir()).
Note that this internal cache may be flushed when the system is running low on
available storage.

> [!NOTE]
> **Note:** Files stored in either cache location are erased when the app is uninstalled.

## Use a repository

For a more sophisticated approach to caching, consider the Repository design
pattern. This involves creating a custom class, known as a Repository, which
provides an API abstraction over some specific data or resource. The repository
may initially fetch its data from various sources, such as a remote web service,
but provides callers with a cached version of the data in subsequent calls. This
layer of indirection allows you to provide a robust caching strategy that's
specific to your app. For more information about using the Repository pattern
within your app, see the [Guide to app
architecture](https://developer.android.com/jetpack/guide).