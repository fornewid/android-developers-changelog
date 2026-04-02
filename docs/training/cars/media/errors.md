---
title: Handle errors  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/media/errors
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Handle errors Stay organized with collections Save and categorize content based on your preferences.




Android Auto and Android Automotive (AAOS) set the playback state to
`STATE_ERROR` and provide a user-facing, localized error message. The apps can
then display the message to the user.

To address an error, you provide an error message with [`setErrorMessage`](/reference/android/support/v4/media/session/PlaybackStateCompat.Builder#setErrorMessage(int,%20java.lang.CharSequence)).

See [`PlaybackStateCompat`](/reference/android/support/v4/media/session/PlaybackStateCompat) for a list of the error codes you can use when
designing the error message to indicate the nature of the error. If a user
must interact with their phone to resolve an issue, include this instruction
in the error message.

Error messages must be user-facing and targeted to the user's locale. For
example, if content is not available in the user's locale, use
[`ERROR_CODE_NOT_AVAILABLE_IN_REGION`](/reference/android/support/v4/media/session/PlaybackStateCompat#ERROR_CODE_NOT_AVAILABLE_IN_REGION()).

### Kotlin

```
mediaSession.setPlaybackState(
    PlaybackStateCompat.Builder()
        .setState(PlaybackStateCompat.STATE_ERROR)
        .setErrorMessage(PlaybackStateCompat.ERROR_CODE_NOT_AVAILABLE_IN_REGION, getString(R.string.error_unsupported_region))
        // ...and any other setters.
        .build())
```

### Java

```
mediaSession.setPlaybackState(
    new PlaybackStateCompat.Builder()
        .setState(PlaybackStateCompat.STATE_ERROR)
        .setErrorMessage(PlaybackStateCompat.ERROR_CODE_NOT_AVAILABLE_IN_REGION, getString(R.string.error_unsupported_region))
        // ...and any other setters.
        .build())
```

To learn more about error states, see
[Using a media session: States and errors](/guide/topics/media-apps/working-with-a-media-session#errors).