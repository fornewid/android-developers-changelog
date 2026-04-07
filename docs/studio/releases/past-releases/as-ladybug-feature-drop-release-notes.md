---
title: Android Studio Ladybug Feature Drop | 2024.2.2 (January 2025)  |  Android Developers
url: https://developer.android.com/studio/releases/past-releases/as-ladybug-feature-drop-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [IDE guides](https://developer.android.com/studio/releases/past-releases)

# Android Studio Ladybug Feature Drop | 2024.2.2 (January 2025) Stay organized with collections Save and categorize content based on your preferences.




The following are new features in Android Studio Ladybug Feature Drop.

## Wear Tiles Animation Preview

[Android Studio Ladybug Canary 2+](/studio/preview)
now supports Wear Tile Animation Previews, making it easier than ever to inspect
and debug your [tile animations](/training/wearables/tiles/animations)
directly within the IDE. This feature builds upon the
[Wear Tiles Preview](/training/wearables/tiles/preview)
support introduced in Android Studio Koala.

[

](/static/studio/images/videos/wear-tiles-anim-preview.mp4)

To get started:

1. Update to Android Studio Ladybug Canary 2 or higher.
2. Add tiles and tooling libraries:

1. Add the dependencies to your app-level `build.gradle.kts` file:

   ```
         # Required for the previews
         debugImplementation(libs.androidx.tiles.tooling)
         implementation(libs.androidx.tiles.tooling.preview)
         # Dependencies needed to build the tiles
         implementation(libs.androidx.tiles)
         implementation(libs.androidx.protolayout)
         implementation(libs.androidx.protolayout.material)
   ```
2. `libs.versions.toml` file:

   ```
       [versions]
       tiles = "1.5.0-alpha01"
       protolayout = "1.3.0-alpha01"
       [libraries]
       androidx-tiles-tooling = { group = "androidx.wear.tiles", name = "tiles-tooling", version.ref = "tiles" }
       androidx-tiles-tooling-preview = { group = "androidx.wear.tiles", name = "tiles-tooling-preview", version.ref = "tiles" }
       androidx-tiles = { group = "androidx.wear.tiles", name = "tiles", version.ref = "tiles" }
       androidx-protolayout = { group = "androidx.wear.protolayout", name = "protolayout-proto", version.ref = "protolayout" }
       androidx-protolayout-material= { group = "androidx.wear.protolayout", name = "protolayout-material", version.ref = "protolayout" }
       androidx-protolayout-expression= { group = "androidx.wear.protolayout", name = "protolayout-expression", version.ref = "protolayout" }
   ```

3. Set up Previews for your Tiles Services. Refer to the
   [tiles preview guide](/training/wearables/tiles/preview) for
   detailed instructions. If your tiles include animations, the
   [Animation
   Preview](/develop/ui/compose/tooling/animation-preview) will automatically appear, allowing you to inspect and
   debug them.

This enhancement streamlines your Wear Tile development workflow by providing
a visual and interactive way to fine-tune your tile animations within
Android Studio.

## Motion Editor deprecation

In the upcoming release, we will be deprecating the
[Motion Editor](/studio/write/motion-editor) as part of our ongoing transition
from XML to [Jetpack Compose](/compose). Compose offers a more modern and
efficient approach to building animations, and we encourage developers to start
using [Compose Animation Preview](/develop/ui/compose/tooling/animation-preview)
for new projects.

## New Gemini in Android Studio features

Android Studio Ladybug Feature Drop introduces a number of new Code Editor
features that use Gemini to help you be more productive. To use these
features, enable sharing code context with Gemini in your current
project.

Use the following links to learn more about these features:

* [Gemini code
  transforms](/studio/preview/gemini/ai-code-completion#gemini-code-transforms)
* [Generate documentation](/studio/preview/gemini/organize#gen-doc)
* [Rename with Gemini](/studio/preview/gemini/organize#rename)
* [Rethink variable names](/studio/preview/gemini/organize#rethink-vars)
* [Commit message generation](/studio/preview/gemini/organize#suggest-commits)

## Google Play SDK Index integration

The Android Studio [Google Play SDK Index
integration](/build/dependencies#sdk-insights) now includes warnings from
the [Google Play SDK Console](https://android-developers.googleblog.com/2024/05/build-better-safer-sdks-google-play-sdk-console.html).
This gives you a complete view of any potential version or policy issues in your
dependencies before submitting your app to the Google Play Console.

Android Studio now also displays notes from SDK authors directly in the editor
to save you time. When a recommended version or version range is available,
Android Studio will also include a quick fix:

![The SDK Insights panel showing a note from an SDK author.](/static/studio/images/sdk-author-note.png)

Android Studio also displays warnings when a specific SDK version has
known security vulnerabilities. This information helps you discover and address
these issues during app development so you can
follow [best practices](/guide/practices/sdk-best-practices).

## Mock sensor capabilities and values

Android Studio now includes a new sensor panel, which lets you simulate a device
having or not having specific sensor capabilities, such as a heart rate sensor,
as well as set specific test values for these sensors. Use this panel to test
how your app handles devices that have different sensor capabilities. This panel
is useful for testing [health and fitness apps](/health-and-fitness), especially
on Wear OS devices.

![Button is near the middle of the panel row](/static/studio/images/run/emulator-health-services.png)


The **Wear Health Services** panel,
available in the emulator.

To open and use the panel, do the following:

1. Create or open an [Android Virtual Device (AVD)](/studio/run/managing-avds)
   and [run your app on the emulator](/studio/run/emulator#avd).
2. In the emulator panel, select **Wear Health Services**.
   ![Open Wear Health Services panel](/static/images/tools/e-health-services.png) The **Wear Health Services** panel
   opens, showing a list of sensors that are available on different
   Android-powered devices.

After the panel opens, you can do the following:

* Toggle among **Standard capabilities**,
  **All capabilities** (default), or **Custom**. Select **Apply** to send the
  current list of capabilities to the emulated device, and select **Reset** to
  restore the list of capabilities to their default on-off values.
* Trigger different user events after you select the **Trigger events**
  drop-down button. From here, you can **Trigger auto pause/resume** of fitness
  activities, **Trigger sleep events** by the user, and **Trigger golf shots**
  that the user takes on a golf course or mini-golf course.
* Override sensor values, after you begin an exercise in an app that's installed
  on the emulator. After you enter new values for different exercise metrics,
  select **Apply** to sync these values with the emulator. This is useful for
  testing how your app handles different exercise conditions and users' fitness
  tendencies.

## App Links Assistant: JSON generation and web issue fixes

To implement App Links, developers need to publish a Digital Asset Links JSON
file on their websites to verify ownership of the domain. When the App Links
Assistant identifies failed web checks, it now creates a JSON file which can fix
those failures. This JSON file can be downloaded by the user and subsequently
uploaded to the respective website to resolve the web check failures.

In cases where a JSON file already exists, users have the ability to compare the
existing and newly-generated JSON files to identify differences.

![](/static/studio/images/app-links-assistant-json.png)

To open the App Links Assistant navigate to **Tools > App Link Assistant** from
the main menu bar.

## Notification when run configuration is missing build step

Android Studio Ladybug Feature Drop Patch 1 and higher informs you if the
active run configuration is missing a "Gradle-aware Make" step. If the run
configuration is missing that step, you were probably impacted by a
[known issue](/studio/known-issues#run-config-missing-gradle) that was
introduced in Ladybug Feature Drop Canary 9. To fix this, you can manually
add the "Gradle-aware Make" step in the "Before launch" section of the
run configuration settings. You can get there by clicking on
**Run/Debug Configurations > Edit Configurations**.