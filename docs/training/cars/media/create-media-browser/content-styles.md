---
title: https://developer.android.com/training/cars/media/create-media-browser/content-styles
url: https://developer.android.com/training/cars/media/create-media-browser/content-styles
source: md.txt
---

# Apply content styles

After using browsable or playable items to[build your content hierarchy](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy), apply content styles to determine how those items display in the car. Use these content styles:
![List items](https://developer.android.com/static/training/cars/images/list-items-01.png)

**Figure 1.**List items prioritize titles and metadata over images.
![Grid items](https://developer.android.com/static/training/cars/images/grid-items-02.png)

**Figure 2.**Grid items prioritize images over titles and metadata.

<br />

## Set default content styles

You can set global defaults for how your media items are displayed. To do so, include specific constants in the`BrowserRoot`extras bundle returned by your service's[`onGetRoot`](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy)implementation and look for these constants to determine the appropriate style.

These extras can be used as keys in the bundle:

- [`DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE()): A presentation hint for all*browsable*items within the browse tree.

- [`DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE()): A presentation hint for all*playable*items within the browse tree.

These keys can map to the these integer constant values to influence the presentation of those items:

- [`DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_LIST_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_LIST_ITEM()): Corresponding items presented as list items.

- [`DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_GRID_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_GRID_ITEM()): Corresponding items presented as grid items.

- [`DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_CATEGORY_LIST_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_CATEGORY_LIST_ITEM()): Corresponding items presented as "category" list items, similar to ordinary list items, but margins are applied around the items' icons. This improves the appearance of small icons. Icons must be tintable vector drawables. This hint is expected to be provided only for browsable items.

- [`DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_CATEGORY_GRID_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_CATEGORY_GRID_ITEM()): Corresponding items presented as "category" grid items and are similar to ordinary grid items, but margins are applied around the items' icons. This improves the appearance of small icons. The icons must be tintable vector drawables. This hint is expected to be provided only for browsable items.

This code snippet shows how to set the default content style for browsable items to grids and playable items to lists:  

### Kotlin

    import androidx.media.utils.MediaConstants

    @Nullable
    override fun onGetRoot(
        @NonNull clientPackageName: String,
        clientUid: Int,
        @Nullable rootHints: Bundle
    ): BrowserRoot {
        val extras = Bundle()
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_GRID_ITEM)
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_LIST_ITEM)
        return BrowserRoot(ROOT_ID, extras)
    }

### Java

    import androidx.media.utils.MediaConstants;

    @Nullable
    @Override
    public BrowserRoot onGetRoot(
        @NonNull String clientPackageName,
        int clientUid,
        @Nullable Bundle rootHints) {
        Bundle extras = new Bundle();
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_GRID_ITEM);
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_LIST_ITEM);
        return new BrowserRoot(ROOT_ID, extras);
    }

## Set per-item content styles

You can override the default content style for any browsable media item's descendants, as well as for any media item. To override the default for a browsable media item's descendants, create an extras bundle in the`MediaDescription`of the media item and add the same previously mentioned hints:

- `DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE`applies to that item's playable descendants.

- `DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE`applies to that item's browsable descendants.

To override the default for a specific media item (not its descendants), create an extras bundle in the`MediaDescription`of the media item. Then, add a hint with the key[`DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_SINGLE_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_SINGLE_ITEM()). Use the same values described previously to specify that item's presentation.
| **Tip:** Not all versions of AAOS support the`SINGLE_ITEM`hint. Prefer other hints if they fulfill your requirements.

This code snippet shows how to create a browsable`MediaItem`that overrides the default content style for itself and its descendants. It styles itself as a category list item, its browsable descendants as list items, and its playable descendants as grid items.  

### Kotlin

    import androidx.media.utils.MediaConstants

    private fun createBrowsableMediaItem(
        mediaId: String,
        folderName: String,
        iconUri: Uri
    ): MediaBrowser.MediaItem {
        val mediaDescriptionBuilder = MediaDescription.Builder()
        mediaDescriptionBuilder.setMediaId(mediaId)
        mediaDescriptionBuilder.setTitle(folderName)
        mediaDescriptionBuilder.setIconUri(iconUri)
        val extras = Bundle()
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_SINGLE_ITEM,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_CATEGORY_LIST_ITEM)
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_LIST_ITEM)
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_GRID_ITEM)
        mediaDescriptionBuilder.setExtras(extras)
        return MediaBrowser.MediaItem(
            mediaDescriptionBuilder.build(), MediaBrowser.MediaItem.FLAG_BROWSABLE)
    }

### Java

    import androidx.media.utils.MediaConstants;

    private MediaBrowser.MediaItem createBrowsableMediaItem(
        String mediaId,
        String folderName,
        Uri iconUri) {
        MediaDescription.Builder mediaDescriptionBuilder = new MediaDescription.Builder();
        mediaDescriptionBuilder.setMediaId(mediaId);
        mediaDescriptionBuilder.setTitle(folderName);
        mediaDescriptionBuilder.setIconUri(iconUri);
        Bundle extras = new Bundle();
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_SINGLE_ITEM,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_CATEGORY_LIST_ITEM);
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_BROWSABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_LIST_ITEM);
        extras.putInt(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_PLAYABLE,
            MediaConstants.DESCRIPTION_EXTRAS_VALUE_CONTENT_STYLE_GRID_ITEM);
        mediaDescriptionBuilder.setExtras(extras);
        return new MediaBrowser.MediaItem(
            mediaDescriptionBuilder.build(), MediaBrowser.MediaItem.FLAG_BROWSABLE);
    }

| **Note:** Per-item content styles apply only to specific items (in the case of`SINGLE_ITEM`) or their immediate descendants (in the case of`BROWSABLE`or`PLAYABLE`). Other items use the default styles passed in`BrowserRoot`extras. The`SINGLE_ITEM`hint takes precedence over all other hints. This means that even if an item's parent uses the`BROWSABLE`or`PLAYABLE`override, the`SINGLE_ITEM`hint is used instead.

## Group items using title hints

To group related media items, use a per-item hint. Every media item in a group must declare an extras bundle in its`MediaDescription`. This bundle must include a mapping with the key[`DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE())and an identical string value. Localize this string, as it is used for the group's title.

This code snippet shows how to create a`MediaItem`with a subgroup heading of`Songs`:  

### Kotlin

    import androidx.media.utils.MediaConstants

    private fun createMediaItem(
        mediaId: String,
        folderName: String,
        iconUri: Uri
    ): MediaBrowser.MediaItem {
        val mediaDescriptionBuilder = MediaDescription.Builder()
        mediaDescriptionBuilder.setMediaId(mediaId)
        mediaDescriptionBuilder.setTitle(folderName)
        mediaDescriptionBuilder.setIconUri(iconUri)
        val extras = Bundle()
        extras.putString(
            MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE,
            "Songs")
        mediaDescriptionBuilder.setExtras(extras)
        return MediaBrowser.MediaItem(
            mediaDescriptionBuilder.build(), /* playable or browsable flag*/)
    }

### Java

    import androidx.media.utils.MediaConstants;

    private MediaBrowser.MediaItem createMediaItem(String mediaId, String folderName, Uri iconUri) {
       MediaDescription.Builder mediaDescriptionBuilder = new MediaDescription.Builder();
       mediaDescriptionBuilder.setMediaId(mediaId);
       mediaDescriptionBuilder.setTitle(folderName);
       mediaDescriptionBuilder.setIconUri(iconUri);
       Bundle extras = new Bundle();
       extras.putString(
           MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE,
           "Songs");
       mediaDescriptionBuilder.setExtras(extras);
       return new MediaBrowser.MediaItem(
           mediaDescriptionBuilder.build(), /* playable or browsable flag*/);
    }

Your app must pass all media items that you want to group together as a contiguous block. For example, consider displaying two groups of media items, "Songs" and "Albums", in that order. If your app passes five media items in this order, Android Auto and AAOS interpret them as four separate groups:

- Media item A with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Songs")`
- Media item B with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Albums")`
- Media item C with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Songs")`
- Media item D with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Songs")`
- Media item E with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Albums")`

This results in these four groups:

- Group 1, called "Songs", containing media item A
- Group 2, called "Albums", containing media item B
- Group 3, called "Songs", containing media items C and D
- Group 4, called "Albums", containing media item E

To display these items in two groups, your app must instead pass the media items in this order:

- Media item A with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Songs")`
- Media item C with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Songs")`
- Media item D with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Songs")`
- Media item B with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Albums")`
- Media item E with`extras.putString(MediaConstants.DESCRIPTION_EXTRAS_KEY_CONTENT_STYLE_GROUP_TITLE, "Albums")`

## Display additional metadata indicators

You can include additional metadata indicators to provide at-a-glance information for content in the media browser tree and during playback.

In the browse tree, Android Auto and AAOS read the extras associated with an item and display the indicators. During media playback, Android Auto and AAOS read the metadata for the media session and look for specific constants to determine which indicators to display.
![Playback view with metadata](https://developer.android.com/static/images/training/cars/metadata_indicators.png)

**Figure 3.**Playback view with metadata.
![Browse view for unplayed content.](https://developer.android.com/static/images/training/cars/progress_indicators.png)

**Figure 4.**Browse view for unplayed content.

<br />

These constants can be used in*both* `MediaItem`description extras and`MediaMetadata`extras:

- [`EXTRA_DOWNLOAD_STATUS`](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat#EXTRA_DOWNLOAD_STATUS()): Indicates the download status of an item. Use this constant as the key. These long constants are possible values:

  - [`STATUS_DOWNLOADED`](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat#STATUS_DOWNLOADED()): Item is fully downloaded.
  - [`STATUS_DOWNLOADING`](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat#STATUS_DOWNLOADING()): Item is in the process of being downloaded.
  - [`STATUS_NOT_DOWNLOADED`](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat#STATUS_NOT_DOWNLOADED()): Item isn't downloaded.
- [`METADATA_KEY_IS_EXPLICIT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#METADATA_KEY_IS_EXPLICIT()): Indicates the item contains explicit content. To indicate an item is explicit, use this constant as the key and the long[`METADATA_VALUE_ATTRIBUTE_PRESENT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#METADATA_VALUE_ATTRIBUTE_PRESENT())as the value.

These constants can*only* be used in`MediaItem`description extras:

- [`DESCRIPTION_EXTRAS_KEY_COMPLETION_STATUS`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_COMPLETION_STATUS()): Indicates the completion state of long-form content, such as podcast episodes and audiobooks. Use this constant as the key. These integer constants are possible values:

  - [`DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_NOT_PLAYED`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_NOT_PLAYED()): Item hasn't been played.

  - [`DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_PARTIALLY_PLAYED`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_PARTIALLY_PLAYED()): Item is partially played, and the current position is somewhere in the middle.

  - [`DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_FULLY_PLAYED`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_FULLY_PLAYED()): Item is completed.

- [`DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE()): Indicates completion progress on long-form content as a double between 0.0 and 1.0, inclusive. This provides more information about the`PARTIALLY_PLAYING`state, allowing Android Auto or AAOS to display a more meaningful progress indicator, such as a progress bar. If you use this extra, see[Update the progress bar in browse view while content plays](https://developer.android.com/training/cars/media/create-media-browser/content-styles#browse-progress-bar)to learn how to keep this indicator up to date after the initial impression.

To display indicators that appear while the user is browsing the media browse tree, create an extras bundle that includes one or more of these constants. Then, pass that bundle to the`MediaDescription.Builder.setExtras`method.
| **Caution:** Not all versions of AAOS support the`COMPLETION_PERCENTAGE`extra. Consider also including the`COMPLETION_STATUS`extra with`PARTIALLY_PLAYED`for compatibility with these versions.

This snippet shows how to display indicators for an explicit media item that is 70% complete:  

### Kotlin

    import androidx.media.utils.MediaConstants

    val extras = Bundle()
    extras.putLong(
        MediaConstants.METADATA_KEY_IS_EXPLICIT,
        MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT)
    extras.putInt(
        MediaConstants.DESCRIPTION_EXTRAS_KEY_COMPLETION_STATUS,
        MediaConstants.DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_PARTIALLY_PLAYED)
    extras.putDouble(
        MediaConstants.DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE, 0.7)
    val description =
        MediaDescriptionCompat.Builder()
            .setMediaId(/*...*/)
            .setTitle(resources.getString(/*...*/))
            .setExtras(extras)
            .build()
    return MediaBrowserCompat.MediaItem(description, /* flags */)

### Java

    import androidx.media.utils.MediaConstants;

    Bundle extras = new Bundle();
    extras.putLong(
        MediaConstants.METADATA_KEY_IS_EXPLICIT,
        MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT);
    extras.putInt(
        MediaConstants.DESCRIPTION_EXTRAS_KEY_COMPLETION_STATUS,
        MediaConstants.DESCRIPTION_EXTRAS_VALUE_COMPLETION_STATUS_PARTIALLY_PLAYED);
    extras.putDouble(
        MediaConstants.DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE, 0.7);
    MediaDescriptionCompat description =
        new MediaDescriptionCompat.Builder()
            .setMediaId(/*...*/)
            .setTitle(resources.getString(/*...*/))
            .setExtras(extras)
            .build();
    return new MediaBrowserCompat.MediaItem(description, /* flags */);

To display indicators for a media item that is currently playing, declare values for`METADATA_KEY_IS_EXPLICIT`or`EXTRA_DOWNLOAD_STATUS`in your`mediaSession`'s`MediaMetadataCompat`.
| **Note:** You can't display the`DESCRIPTION_EXTRAS_KEY_COMPLETION_STATUS`or`DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE`indicators on the playback view.

This code snippet shows how to indicate that the song in the playback view is explicit and downloaded:  

### Kotlin

    import androidx.media.utils.MediaConstants

    mediaSession.setMetadata(
        MediaMetadataCompat.Builder()
            .putString(
                MediaMetadataCompat.METADATA_KEY_DISPLAY_TITLE, "Song Name")
            .putString(
                MediaMetadataCompat.METADATA_KEY_DISPLAY_SUBTITLE, "Artist name")
            .putString(
                MediaMetadataCompat.METADATA_KEY_ALBUM_ART_URI,
                albumArtUri.toString())
            .putLong(
                MediaConstants.METADATA_KEY_IS_EXPLICIT,
                MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT)
            .putLong(
                MediaDescriptionCompat.EXTRA_DOWNLOAD_STATUS,
                MediaDescriptionCompat.STATUS_DOWNLOADED)
            .build())

### Java

    import androidx.media.utils.MediaConstants;

    mediaSession.setMetadata(
        new MediaMetadataCompat.Builder()
            .putString(
                MediaMetadataCompat.METADATA_KEY_DISPLAY_TITLE, "Song Name")
            .putString(
                MediaMetadataCompat.METADATA_KEY_DISPLAY_SUBTITLE, "Artist name")
            .putString(
                MediaMetadataCompat.METADATA_KEY_ALBUM_ART_URI,
                albumArtUri.toString())
            .putLong(
                MediaConstants.METADATA_KEY_IS_EXPLICIT,
                MediaConstants.METADATA_VALUE_ATTRIBUTE_PRESENT)
            .putLong(
                MediaDescriptionCompat.EXTRA_DOWNLOAD_STATUS,
                MediaDescriptionCompat.STATUS_DOWNLOADED)
            .build());

## Update the progress bar in browse view while content plays

As previously mentioned, you can use the[`DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE())extra to show a progress bar for partially played content in the browse view. However, if a user continues playing the partially played content, that indicator becomes inaccurate over time.

So that Android Auto and AAOS keep the progress bar up to date, supply additional information in`MediaMetadataCompat`and`PlaybackStateCompat`to link ongoing content to media items in the browse view.

For a media item to have an automatically updating progress bar, these requirements must be met:

- When created, the`MediaItem`must send[`DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE())in its extras with a value between`0.0`and`1.0`, inclusive.

- The`MediaMetadataCompat`must send[`METADATA_KEY_MEDIA_ID`](https://developer.android.com/reference/android/support/v4/media/MediaMetadataCompat#METADATA_KEY_MEDIA_ID())with a string value equal to the[media ID](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat.Builder#setMediaId(java.lang.String))passed to the`MediaItem`.

- The`PlaybackStateCompat`must include an extra with the key[`PLAYBACK_STATE_EXTRAS_KEY_MEDIA_ID`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#PLAYBACK_STATE_EXTRAS_KEY_MEDIA_ID())that maps to a string value equal to the[media ID](https://developer.android.com/reference/android/support/v4/media/MediaDescriptionCompat.Builder#setMediaId(java.lang.String))passed to the`MediaItem`.

This code snippet shows how to indicate that the playing item is linked to an item in the browse view:  

### Kotlin

    import androidx.media.utils.MediaConstants

    // When the MediaItem is constructed to show in the browse view.
    // Suppose the item was 25% complete when the user launched the browse view.
    val mediaItemExtras = Bundle()
    mediaItemExtras.putDouble(
        MediaConstants.DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE, 0.25)
    val description =
        MediaDescriptionCompat.Builder()
            .setMediaId("my-media-id")
            .setExtras(mediaItemExtras)
            // ...and any other setters.
            .build()
    return MediaBrowserCompat.MediaItem(description, /* flags */)

    // Elsewhere, when the user has selected MediaItem for playback.
    mediaSession.setMetadata(
        MediaMetadataCompat.Builder()
            .putString(MediaMetadata.METADATA_KEY_MEDIA_ID, "my-media-id")
            // ...and any other setters.
            .build())

    val playbackStateExtras = Bundle()
    playbackStateExtras.putString(
        MediaConstants.PLAYBACK_STATE_EXTRAS_KEY_MEDIA_ID, "my-media-id")
    mediaSession.setPlaybackState(
        PlaybackStateCompat.Builder()
            .setExtras(playbackStateExtras)
            // ...and any other setters.
            .build())

### Java

    import androidx.media.utils.MediaConstants;

    // When the MediaItem is constructed to show in the browse view.
    // Suppose the item was 25% complete when the user launched the browse view.
    Bundle mediaItemExtras = new Bundle();
    mediaItemExtras.putDouble(
        MediaConstants.DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE, 0.25);
    MediaDescriptionCompat description =
        new MediaDescriptionCompat.Builder()
            .setMediaId("my-media-id")
            .setExtras(mediaItemExtras)
            // ...and any other setters.
            .build();
    return new MediaBrowserCompat.MediaItem(description, /* flags */);

    // Elsewhere, when the user has selected MediaItem for playback.
    mediaSession.setMetadata(
        new MediaMetadataCompat.Builder()
            .putString(MediaMetadata.METADATA_KEY_MEDIA_ID, "my-media-id")
            // ...and any other setters.
            .build());

    Bundle playbackStateExtras = new Bundle();
    playbackStateExtras.putString(
        MediaConstants.PLAYBACK_STATE_EXTRAS_KEY_MEDIA_ID, "my-media-id");
    mediaSession.setPlaybackState(
        new PlaybackStateCompat.Builder()
            .setExtras(playbackStateExtras)
            // ...and any other setters.
            .build());

P Even unplayed or fully played content can display an automatically updating progress bar. This occurs if the corresponding media items include the`DESCRIPTION_EXTRAS_KEY_COMPLETION_PERCENTAGE`extra with a value of`0.0`(for unplayed) or`1.0`(for fully played). After the user selects these media items, Android Auto and AAOS display the progress bar over other progress indicators.