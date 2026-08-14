---
title: https://developer.android.com/topic/google-play-instant/getting-started/support-play-games-services
url: https://developer.android.com/topic/google-play-instant/getting-started/support-play-games-services
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025,
Instant Apps cannot be published through Google Play, and all
[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)
will no longer work. Users will no longer be served Instant Apps by Play using any
mechanism.

We're making this change based on developer feedback and our continuous investments
to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to
their regular app or game, using [deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)
to redirect them to specific journeys or features when relevant.

All Instant play games must support automatic
[sign-in using Google Play Games Services](https://developers.google.com/games/services/common/concepts/sign-in). Use
Google Play Games Services to
provide a consistent player ID that you can use to restore saved progress
from the cloud.

## Size impact of the library

The size impact of the Google Play Games Services library depends on whether the
game engine runs on Unity, Java, or Native.

### Java

The size impact is minimal because ProGuard is informed about
which classes are used.

### Unity

You can integrate the game save feature into your Unity game using the
[official Google Play Game Services plugin](https://github.com/playgameservices/play-games-plugin-for-unity/tree/master/current-build).
The size impact is around 200 KB if you use the ProGuard recommendations.

### Native

You can integrate the game save feature with a game built on the Android NDK using the
[Native Play Games Services SDK](https://developers.google.com/games/services/cpp/GettingStartedNativeClient).

Use the general ProGuard configuration below to strip out most of the Java code
included by the library. You can implement Play Games Services
sign-in and game save with this configuration, while only adding about
250 KB to the APK.

    # The native PGS library wraps the Java PGS SDK using reflection.
    -dontobfuscate
    -keeppackagenames

    # Needed for callbacks.
    -keepclasseswithmembernames,includedescriptorclasses class * {
        native <methods>;
    }

    # Needed for helper libraries.
    -keep class com.google.example.games.juihelper.** {
      public protected *;
    }
    -keep class com.sample.helper.** {
      public protected *;
    }

    # Needed for GoogleApiClient and auth stuff.
    -keep class com.google.android.gms.common.api.** {
      public protected *;
    }

    # Keep all of the "nearby" library, which is needed by the native PGS library
    # at runtime (though deprecated).
    -keep class com.google.android.gms.nearby.** {
      public protected *;
    }

    # Keep all of the public PGS APIs.
    -keep class com.google.android.gms.games.** {
      public protected *;
    }