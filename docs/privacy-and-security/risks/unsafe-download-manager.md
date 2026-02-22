---
title: https://developer.android.com/privacy-and-security/risks/unsafe-download-manager
url: https://developer.android.com/privacy-and-security/risks/unsafe-download-manager
source: md.txt
---

# Unsafe Download Manager

<br />

**OWASP category:** [MASVS-NETWORK: Network Communication](https://mas.owasp.org/MASVS/08-MASVS-NETWORK)

## Overview

DownloadManager is a system service introduced in API level 9. It handles long-running HTTP downloads and allows applications to download files as a background task. Its API handles HTTP interactions and retries downloads after failures or across connectivity changes and system reboots.

DownloadManager has security relevant weaknesses that make it an insecure choice for managing downloads in Android applications.

**(1) CVEs in Download Provider**

In 2018, three[CVEs](https://ioactive.com/multiple-vulnerabilities-in-androids-download-provider-cve-2018-9468-cve-2018-9493-cve-2018-9546/)were found and patched in Download Provider. A summary of each follows (see[technical details](https://ioactive.com/multiple-vulnerabilities-in-androids-download-provider-cve-2018-9468-cve-2018-9493-cve-2018-9546/)).

- **Download Provider Permission Bypass**-- With no granted permissions, a malicious app could retrieve all entries from the Download Provider, which could include potentially sensitive information such as file names, descriptions, titles, paths, URLs, as well as full READ/WRITE permissions to all downloaded files. A malicious app could run in the background, monitoring all downloads and leaking their contents remotely, or modifying the files on-the-fly before they are accessed by the legitimate requester. This could cause a denial-of-service for the user for core applications, including the inability to download updates.
- **Download Provider SQL Injection** -- Through a SQL injection vulnerability, a malicious application with no permissions could retrieve all entries from the Download Provider. Also, applications with limited permissions, such as[`android.permission.INTERNET`](http://go/android-dev/reference/android/Manifest.permission#INTERNET), could also access all database contents from a different URI. Potentially sensitive information such as file names, descriptions, titles, paths, URLs could be retrieved, and, depending on permissions, access to downloaded contents may be possible as well.
- **Download Provider Request Headers Information Disclosure** -- A malicious application with the[`android.permission.INTERNET`](http://go/android-dev/reference/android/Manifest.permission#INTERNET)permission granted could retrieve all entries from the Download Provider request headers table. These headers may include sensitive information, such as session cookies or authentication headers, for any download started from the Android Browser or Google Chrome, among other applications. This could allow an attacker to impersonate the user on any platform from which sensitive user data was obtained.

**(2) Dangerous Permissions**

DownloadManager in API levels lower than 29 requires dangerous permissions --[`android.permission.WRITE_EXTERNAL_STORAGE`](http://go/android-dev/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE). For API level 29 and higher,[`android.permission.WRITE_EXTERNAL_STORAGE`](http://go/android-dev/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)permissions are not required, but the URI must refer to a path within the directories owned by the application or a path within the top-level "Downloads" directory.

**(3) Reliance on** `Uri.parse()`

DownloadManager relies on the`Uri.parse()`method to parse the location of the requested download. In the interest of performance, the`Uri`class applies little to no validation on untrusted input.

## Impact

Using DownloadManager may lead to vulnerabilities through the exploitation of WRITE permissions to external storage. Since android.permission.WRITE_EXTERNAL_STORAGE permissions allow broad access to external storage, it is possible for an attacker to silently modify files and downloads, install potentially malicious apps, deny service to core apps, or cause apps to crash. Malicious actors could also manipulate what is sent to Uri.parse() to cause the user to download a harmful file.

## Mitigations

Instead of using DownloadManager, set up downloads directly in your app using an HTTP client (such as Cronet), a process scheduler/manager, and a way to ensure retries if there is network loss. The[documentation of the library](https://developer.android.com/develop/connectivity/cronet)includes a link to a[sample](https://github.com/GoogleChromeLabs/cronet-sample)app as well as[instructions](https://developer.android.com/develop/connectivity/cronet/start)on how to implement it.

If your application requires the ability to manage process scheduling, run downloads in the background, or retry establishing the download after network loss, then consider including[`WorkManager`](https://developer.android.com/reference/androidx/work/WorkManager)and[`ForegroundServices`](https://developer.android.com/develop/background-work/services/foreground-services).

Example code for setting up a download using Cronet is as follows, taken from the Cronet[codelab](https://developer.android.com/codelabs/cronet#8).  

### Kotlin

    override suspend fun downloadImage(url: String): ImageDownloaderResult {
       val startNanoTime = System.nanoTime()
       return suspendCoroutine {
           cont ->
           val request = engine.newUrlRequestBuilder(url, object: ReadToMemoryCronetCallback() {
           override fun onSucceeded(
               request: UrlRequest,
               info: UrlResponseInfo,
               bodyBytes: ByteArray) {
               cont.resume(ImageDownloaderResult(
                   successful = true,
                   blob = bodyBytes,
                   latency = Duration.ofNanos(System.nanoTime() - startNanoTime),
                   wasCached = info.wasCached(),
                   downloaderRef = this@CronetImageDownloader))
           }
           override fun onFailed(
               request: UrlRequest,
               info: UrlResponseInfo,
               error: CronetException
           ) {
               Log.w(LOGGER_TAG, "Cronet download failed!", error)
               cont.resume(ImageDownloaderResult(
                   successful = false,
                   blob = ByteArray(0),
                   latency = Duration.ZERO,
                   wasCached = info.wasCached(),
                   downloaderRef = this@CronetImageDownloader))
           }
       }, executor)
           request.build().start()
       }
    }

### Java

    @Override
    public CompletableFuture<ImageDownloaderResult> downloadImage(String url) {
        long startNanoTime = System.nanoTime();
        return CompletableFuture.supplyAsync(() -> {
            UrlRequest.Builder requestBuilder = engine.newUrlRequestBuilder(url, new ReadToMemoryCronetCallback() {
                @Override
                public void onSucceeded(UrlRequest request, UrlResponseInfo info, byte[] bodyBytes) {
                    return ImageDownloaderResult.builder()
                            .successful(true)
                            .blob(bodyBytes)
                            .latency(Duration.ofNanos(System.nanoTime() - startNanoTime))
                            .wasCached(info.wasCached())
                            .downloaderRef(CronetImageDownloader.this)
                            .build();
                }
                @Override
                public void onFailed(UrlRequest request, UrlResponseInfo info, CronetException error) {
                    Log.w(LOGGER_TAG, "Cronet download failed!", error);
                    return ImageDownloaderResult.builder()
                            .successful(false)
                            .blob(new byte[0])
                            .latency(Duration.ZERO)
                            .wasCached(info.wasCached())
                            .downloaderRef(CronetImageDownloader.this)
                            .build();
                }
            }, executor);
            UrlRequest urlRequest = requestBuilder.build();
            urlRequest.start();
            return urlRequest.getResult();
        });
    }

## Resources

- [Main documentation page for DownloadManager](https://developer.android.com/reference/android/app/DownloadManager)
- [Report for DownloadManager CVEs](https://ioactive.com/multiple-vulnerabilities-in-androids-download-provider-cve-2018-9468-cve-2018-9493-cve-2018-9546/)
- [Android Permission Bypass CVE 2018-9468](https://ioactive.com/wp-content/uploads/2019/04/IOActive-Security-Advisory-Androids-Download-Provider-Permission-Bypass-CVE-2018-9468.pdf)
- [Android Download Provider SQL Injection CVE-2018- 9493](https://act-on.ioactive.com/acton/attachment/34793/f-722b41b4-7aff-4b35-9925-c221a217744d/1/-/-/-/-/cve-2018-9493.pdf)
- [Android Download Provider Permission Bypass CVE2018-9468](https://act-on.ioactive.com/acton/attachment/34793/f-3b8bb46b-d105-4efd-97a1-9970bfa6928b/1/-/-/-/-/cve-2018-9546.pdf)
- [Main documentation page for Cronet](https://developer.android.com/develop/connectivity/cronet)
- [Instructions for using Cronet in an application](https://developer.android.com/develop/connectivity/cronet/start#java)
- [Sample Cronet implementation](https://github.com/GoogleChromeLabs/cronet-sample)
- [Documentation for Uri](https://developer.android.com/reference/android/net/Uri)
- [Documentation for ForegroundService](https://developer.android.com/develop/background-work/services/foreground-services)
- [Documentation for WorkManager](https://developer.android.com/reference/androidx/work/WorkManager)