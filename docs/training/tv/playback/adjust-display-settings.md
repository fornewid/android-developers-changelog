---
title: https://developer.android.com/training/tv/playback/adjust-display-settings
url: https://developer.android.com/training/tv/playback/adjust-display-settings
source: md.txt
---

Android includes APIs that allow apps to adjust display settings on supported
hardware. On Android TV OS, apps can take advantage of this to ensure that
content displays in the best possible format, by matching the framerate and
color profile for the ideal watching experience.

## Match content frame rate

When the framerate of a video doesn't match the refresh rate of the display,
users can experience unpleasant motion judder artifacts from frame rate
conversion. This is especially visible during slow panning shots. For this
reason, use the [`Surface.setFrameRate()`](https://developer.android.com/training/tv/playback/(/reference/android/view/Surface#setFrameRate(float,%20int))) API to notify the
framework about the frame rate of the content and to signal whether the video
content is eligible for a non-seamless [frame rate
switch](https://developer.android.com/guide/topics/media/frame-rate#non-seamless).

For more information, read the [frame rate guide](https://developer.android.com/guide/topics/media/frame-rate).

## Match preferred picture profiles

The MediaQuality API in Android 16 allows developers to take control over
picture profiles.

Some example scenarios include:

- For movies and TV series that are mastered with a wider dynamic range, developers might request Filmmaker mode to accurately display content as the creator intended for it to look. A cinema profile with greater color accuracy brings out subtle details in shadows in favor of increasing brightness.
- Live sporting events, which are often mastered with a narrow dynamic range and watched in the daylight, can benefit from a profile that gives preference to brightness over color accuracy.
- Game developers can request a low latency profile with minimal image processing so players can get the best performance from their display.

| **Note:** OEMs may add additional presets and provide mechanisms for users to define their own picture profiles. This implementation uses the [`createPictureProfile()`](https://developer.android.com/reference/android/media/quality/MediaQualityManager#createPictureProfile(android.media.quality.PictureProfile)) method that requires a system permission.

### Selecting a system picture profile

Before selecting a picture profile, it's important to first validate that the
device supports it.

The following snippet shows how to use
[`getAvailablePictureProfiles()`](https://developer.android.com/reference/android/media/quality/MediaQualityManager#getAvailablePictureProfiles(android.media.quality.MediaQualityManager.ProfileQueryParams)) to query all
supported picture profiles and apply a sports profile:  

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.BAKLAVA) {
        val mediaQualityManager: MediaQualityManager =
            context.getSystemService(MediaQualityManager::class.java)
        val profiles = mediaQualityManager.getAvailablePictureProfiles(null)
        for (profile in profiles) {
            // If we have a system sports profile, apply it to our media codec
            if (profile.profileType == PictureProfile.TYPE_SYSTEM
                && profile.name == NAME_SPORTS
            ) {
                val bundle = Bundle().apply { 
                    putParcelable(MediaFormat.KEY_PICTURE_PROFILE_INSTANCE, profile)
                }
                mediaCodec.setParameters(bundle)
            }
        }
    }

To obtain a specific profile by name, use [`getPictureProfile()`](https://developer.android.com/reference/android/media/quality/MediaQualityManager#getPictureProfile(int,%20java.lang.String,%20android.media.quality.MediaQualityManager.ProfileQueryParams)):  

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.BAKLAVA) {
        val profile = mediaQualityManager.getPictureProfile(
            PictureProfile.TYPE_SYSTEM, NAME_SPORTS, null)
    }

If you don't need to query whether a profile is available, profiles can be
provided directly by their ID to a MediaCodec by using
`MediaFormat.KEY_PICTURE_PROFILE_INSTANCE`.

While supported profiles may differ by device, you may consider matching against
the following known system profile IDs:  

    const val NAME_STANDARD: String = "standard"
    const val NAME_VIVID: String = "vivid"
    const val NAME_SPORTS: String = "sports"
    const val NAME_GAME: String = "game"
    const val NAME_MOVIE: String = "movie"
    const val NAME_ENERGY_SAVING: String = "energy_saving"
    const val NAME_USER: String = "user"

| **Note:** These strings are provided as recommendations to OEMs and are subject to change in future API levels.