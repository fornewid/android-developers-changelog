---
title: https://developer.android.com/games/pgs/play-games-sidekick-sdk
url: https://developer.android.com/games/pgs/play-games-sidekick-sdk
source: md.txt
---

The Sidekick SDK is available to developers who:

- Publish releases as an APK, rather than an Android App Bundle (AAB).
- Need access to Sidekick, but use an incompatible anti-tampering solution. If you have other questions, [request support](https://docs.google.com/forms/d/1NPmZ04tyT97tb8q-NbElU_HJ3YuPWOkXvhwJB3mTmB8/viewform).

To add Sidekick SDK, add the `com.google.android.play:sidekick`
to your dependencies. Make sure that you include Google's Maven
repository ([`maven.google.com`](https://maven.google.com)) as one of your listed
repositories.

For example, in your module's `build.gradle.kts` file, add the following:

    dependencyResolutionManagement {
      repositories {
        google()
        // Other repositories
      }
    }

    dependencies {
      // Other dependencies
      implementation("com.google.android.play:sidekick:*")
    }

### Games using multiple processes

If your game activities run in a separate process (use the `android:process`
attribute in your `AndroidManifest.xml`'s `<application>` tags), you must update
the manifest by adding the following content providers. No other code changes
are needed.

```xml
<application>
  [...]
  <provider
      android:name="com.google.android.play.deku.DekuContentProvider$Process1"
      android:authorities="insert.your.package.name.here.deku.contentprovider1"
      android:exported="false"
      android:process=":insert_name_of_process1_here" />

  <provider
      android:name="com.google.android.play.deku.DekuContentProvider$Process2"
      android:authorities="insert.your.package.name.here.deku.contentprovider2"
      android:exported="false"
      android:process=":insert_name_of_process2_here" />

  [...] <!-- Up to 5 processes ($Process1, $Process2, ..., $Process5) -->
</application>
```