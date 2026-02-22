---
title: https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy
url: https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy
source: md.txt
---

# Build your content hierarchy

Android Auto and Android Automotive OS (AAOS) call your app's media browser service to discover which content is available. To support this, you implement these two methods in your media browser service.

## Implement onGetRoot

Your service's[`onGetRoot`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onGetRoot(java.lang.String,%20int,%20android.os.Bundle))method returns information about the root node of your content hierarchy. Android Auto and AAOS use this root node to request the rest of your content using the[`onLoadChildren`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadChildren(java.lang.String,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E,android.os.Bundle))method. This code snippet shows an implementation of the`onGetRoot`method:  

### Kotlin

    override fun onGetRoot(
        clientPackageName: String,
        clientUid: Int,
        rootHints: Bundle?
    ): BrowserRoot? =
        // Verify that the specified package is allowed to access your
        // content. You'll need to write your own logic to do this.
        if (!isValid(clientPackageName, clientUid)) {
            // If the request comes from an untrusted package, return null.
            // No further calls will be made to other media browsing methods.

            null
        } else MediaBrowserServiceCompat.BrowserRoot(MY_MEDIA_ROOT_ID, null)

### Java

    @Override
    public BrowserRoot onGetRoot(String clientPackageName, int clientUid,
        Bundle rootHints) {

        // Verify that the specified package is allowed to access your
        // content. You'll need to write your own logic to do this.
        if (!isValid(clientPackageName, clientUid)) {
            // If the request comes from an untrusted package, return null.
            // No further calls will be made to other media browsing methods.

            return null;
        }

        return new MediaBrowserServiceCompat.BrowserRoot(MY_MEDIA_ROOT_ID, null);
    }

For a detailed example of this method, see[`onGetRoot`](https://github.com/googlesamples/android-UniversalMusicPlayer/blob/47da058112cee0b70442bcd0370c1e46e830c66b/media/src/main/java/com/example/android/uamp/media/MusicService.kt#L189)in the Universal Android Music Player sample app on GitHub.

### Add package validation

When a call is made to your service's[`onGetRoot`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onGetRoot(java.lang.String,%20int,%20android.os.Bundle))method, the calling package passes identifying information to your service. Your service can use this information to decide if that package can access your content.

For example, you can restrict access to your app's content to a list of approved packages:

- Compare the`clientPackageName`to your allowlist.
- Verify the certificate used to sign the APK for the package.

If the package can't be verified, return`null`to deny access to your content.

To provide system apps, such as Android Auto and AAOS, with access to your content, your service must return a non-null`BrowserRoot`when these system apps call the`onGetRoot`method.

The signature of the AAOS system app varies according to the make and model of a car. Be sure to allow connections from all system apps to support AAOS.

This code snippet shows how your service can validate that the calling package is a system app:  

    fun isKnownCaller(
        callingPackage: String,
        callingUid: Int
    ): Boolean {
        ...
        val isCallerKnown = when {
           // If the system is making the call, allow it.
           callingUid == Process.SYSTEM_UID -> true
           // If the app was signed by the same certificate as the platform
           // itself, also allow it.
           callerSignature == platformSignature -> true
           // ... more cases
        }
        return isCallerKnown
    }

This code snippet is an excerpt from the[`PackageValidator`](https://github.com/android/uamp/blob/7080a323ae5181cc44d11b319feab81fd4e568d1/common/src/main/java/com/example/android/uamp/media/PackageValidator.kt#L50)class in the Universal Android Music Player sample app on GitHub. See that class for a more detailed example of how to implement package validation for your service's`onGetRoot`method.

In addition to allowing system apps, you must allow Google Assistant connect to your`MediaBrowserService`. Google Assistant uses[separate package names](https://developer.android.com/media/implement/assistant#signatures)for the phone, which includes Android Auto Android AAOS.
| **Caution:** Don't perform checks for user authentication or other slow processes within your service's`onGetRoot`implementation. Your service must quickly return a non-null`BrowserRoot`when`onGetRoot`is called so that the calling service doesn't timeout. Handle user authentication and other business logic for slow processes in the[`onLoadChildren`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadChildren(java.lang.String,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E,android.os.Bundle))method instead.

## Implement onLoadChildren

After receiving your root node object, Android Auto and AAOS build a top-level menu by calling[`onLoadChildren`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadChildren(java.lang.String,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E,android.os.Bundle))on the root node object to get its descendants. Client apps build submenus by calling this same method using descendant node objects.
| **Note:** Android Auto and AAOS don't support pagination. If you build your app with`MediaLibraryService`and`MediaLibrarySession`, don't rely on the`page`or`pageSize`parameters of the`onGetChildren`callback.

Each node in your content hierarchy is represented by a[`MediaBrowserCompat.MediaItem`](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat.MediaItem)object. Each of these media items is identified by a unique ID string. Client apps treat these ID strings as opaque tokens.

When a client app wants to browse to a submenu, or play a media item, it passes the token. Your app is responsible for associating the token with the appropriate media item.
| **Note:** Android Auto and AAOS have strict limits on how many media items can be displayed at each level in the menu. These limits minimize distractions for drivers and help your app to operate with voice commands. To learn more, see[Browsing content details](https://developers.google.com/cars/design/automotive-os/apps/media/interaction-model/browsing)and[Browsing views](https://developers.google.com/cars/design/android-auto/apps/browsing-views).

This code snippet shows an implementation of`onLoadChildren`  

### Kotlin

    override fun onLoadChildren(
        parentMediaId: String,
        result: Result<List<MediaBrowserCompat.MediaItem>>
    ) {
        // Assume for example that the music catalog is already loaded/cached.

        val mediaItems: MutableList&lt;MediaBrowserCompat.MediaItem> = mutableListOf()

        // Check if this is the root menu:
        if (MY_MEDIA_ROOT_ID == parentMediaId) {

            // Build the MediaItem objects for the top level
            // and put them in the mediaItems list.
        } else {

            // Examine the passed parentMediaId to see which submenu we're at
            // and put the descendants of that menu in the mediaItems list.
        }
        result.sendResult(mediaItems)
    }

### Java

    @Override
    public void onLoadChildren(final String parentMediaId,
        final Result&lt;List&lt;MediaBrowserCompat.MediaItem>> result) {

        // Assume for example that the music catalog is already loaded/cached.

        List&lt;MediaBrowserCompat.MediaItem> mediaItems = new ArrayList&lt;>();

        // Check if this is the root menu:
        if (MY_MEDIA_ROOT_ID.equals(parentMediaId)) {

            // Build the MediaItem objects for the top level
            // and put them in the mediaItems list.
        } else {

            // Examine the passed parentMediaId to see which submenu we're at
            // and put the descendants of that menu in the mediaItems list.
        }
        result.sendResult(mediaItems);
    }

To view an example of this method, see the[`onLoadChildren`](https://github.com/googlesamples/android-UniversalMusicPlayer/blob/47da058112cee0b70442bcd0370c1e46e830c66b/media/src/main/java/com/example/android/uamp/media/MusicService.kt#L215)in the Universal Android Music Player sample app on GitHub.

## Structure the root menu

Android Auto and Android Automotive OS have specific constraints about the structure of the root menu. These are communicated to the`MediaBrowserService`through root hints, which can be read through the Bundle argument passed into`onGetRoot()`. When followed, these hints let the system display the root content as navigational tabs. If you don't follow these hints, some root content might be dropped or made less discoverable by the system.

![Root content displayed as navigational tabs](https://developer.android.com/static/images/training/cars/browse_home_tabs.png)

**Figure 1.**Root content displayed as navigational tabs.

By applying these hints, the system displays the root content as navigational tabs. By not applying these hints, some root content might be dropped or made less discoverable. These hints are transmitted:

- [Limit on the number of root children](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_LIMIT()): In most cases, expect this number to be four, meaning that only four (or fewer) tabs can be shown.

- [Supported flags on the root children](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_SUPPORTED_FLAGS()): Expect this value to be[`MediaItem#FLAG_BROWSABLE`](https://developer.android.com/reference/android/support/v4/media/MediaBrowserCompat.MediaItem#FLAG_BROWSABLE()), which means only browsable items (not playable items) can be shown as tabs.

- [Limit on the number of custom browse actions](https://developer.android.com/training/cars/media/create-media-browser/custom-browse-actions#parse-actions-limit): Check how many custom browse actions are supported.

**Caution:** Not all versions of AAOS send these root hints. In the absence of these hints, assume that AAOS requires only root browsable items, and (at most) four. Consider the default values in this code snippet.  

### Kotlin

    import androidx.media.utils.MediaConstants

    override fun onGetRoot(
        clientPackageName: String,
        clientUid: Int,
        rootHints: Bundle
    ): BrowserRoot {

      val maximumRootChildLimit = rootHints.getInt(
          MediaConstants.BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_LIMIT,
          /* defaultValue= */ 4)
      val supportedRootChildFlags = rootHints.getInt(
          MediaConstants.BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_SUPPORTED_FLAGS,
          /* defaultValue= */ MediaItem.FLAG_BROWSABLE)

      // Rest of method...
    }

### Java

    import androidx.media.utils.MediaConstants;

    // Later, in your MediaBrowserServiceCompat.
    @Override
    public BrowserRoot onGetRoot(
        String clientPackageName, int clientUid, Bundle rootHints) {

        int maximumRootChildLimit = rootHints.getInt(
            MediaConstants.BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_LIMIT,
            /* defaultValue= */ 4);
        int supportedRootChildFlags = rootHints.getInt(
            MediaConstants.BROWSER_ROOT_HINTS_KEY_ROOT_CHILDREN_SUPPORTED_FLAGS,
            /* defaultValue= */ MediaItem.FLAG_BROWSABLE);

        // Rest of method...
    }

You can choose to branch the logic for the structure of your content hierarchy based on the values of these hints, particularly if your hierarchy varies among`MediaBrowser`integrations outside of Android Auto and AAOS.

For example, if you normally show a root playable item, you might want to nest it under a root browsable item instead due to the value of the supported flags hint.

Apart from root hints, use these guidelines to optimally render tabs:

- Monochrome (preferably white) icons for each tab item

- Short and meaningful labels for each tab item (short labels reduce the odds that labels might be truncated)