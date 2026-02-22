---
title: https://developer.android.com/topic/google-play-instant/guides/multiple-entry-points
url: https://developer.android.com/topic/google-play-instant/guides/multiple-entry-points
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Each instant experience has at least one*entry point* , which is a single activity within your app or game. If you want your app or game to have multiple entry points, each starting activity needs to be*addressable*; that is, it needs to correspond to a unique URL.
| **Note:** You cannot associate fragments with URLs. Additionally, you cannot launch these fragments independently of an activity.

If the URLs for the entry points in an instant app or game share a domain, each entry point needs to correspond to a different path within that domain. For example, say you're creating a navigation app that should have three separate entry points: find current location, search for nearby restaurants, and share location. Each of these features corresponds to resources within a web domain, "example.com". To provide a unique URL for each entry point, specify different paths within the domain, as shown in the following table.
| **Caution:** To help the system launch the correct activity for each entry point, make sure that your paths don't share a common prefix. For example, if you provided entry points containing the URLs "http://example.com/check" and "http://example.com/checkout", the system's behavior might be undefined.

|      Feature       |              URL               |
|--------------------|--------------------------------|
| Location finder    | http://example.com/finder      |
| Nearby restaurants | http://example.com/restaurants |
| Share location     | http://example.com/share       |

## Declare URL path prefixes

It's possible for the URL of one entry point to share a prefix with the URLs of other entry points into the same app or game. In this case, specify the full path for one entry point and the path prefix for the other entry points, as shown in the following code snippet:

AndroidManifest.xml  

```xml
<manifest>
  <activity android:name=".CatalogActivity" >
    <intent-filter>
      <!-- List of items in the catalog. -->
      <data android:path="/items" />
    </intent-filter>
  </activity>
  <activity android:name=".ItemActivity" >
    <intent-filter>
      <!-- Information about a specific item in the catalog. -->
      <data android:pathPrefix="/items/" />
    </intent-filter>
</manifest>
```
| **Note:** To match a`pathPrefix`filter, URLs must contain the path prefix in addition to at least one character following the prefix. Therefore, by following the logic in the preceding code snippet, the URL "/items/" would bring users to`CatalogActivity`.