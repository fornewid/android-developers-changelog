---
title: https://developer.android.com/studio/releases/past-releases/as-2-0-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-2-0-0-release-notes
source: md.txt
---

<br />

# Android Studio 2.0 (April 2016)

<br />

<br />


**Note:** If you are developing for the N Developer Preview, you
should use Android Studio 2.1 Preview. Android Studio 2.0 does not support
all the features required to target the N Preview.

<br />

<br />


**Instant Run**:

<br />

<br />

- Android Studio now deploys clean builds faster than ever before. Additionally, pushing incremental code changes to the emulator or a physical device is now almost instantaneous. Review your updates without redeploying a new debug build or, in many cases, without restarting the app.  

    <li>Instant Run supports pushing the following changes to a running app:
      <ul>
        <li>Changes to the implementation of an existing instance method or
        static method
        </li>
        <li>Changes to an existing app resource
        </li>
        <li>Changes to structural code, such as a method signature or a static
        field (requires a target device running API level 21 or higher).
        </li>
      </ul>
    </li>

    <li>Read the documentation to learn more <a href=
    "/tools/building/building-studio.html#instant-run">about Instant
    Run</a>.
      <p class="note">
        <strong>Note:</strong> Instant Run is supported only when you deploy the
        debug build variant, use <a href=
        "/tools/revisions/gradle-plugin.html#revisions">Android plugin for
        Gradle version 2.0.0</a> or higher, and configure your app's module-level
        <code>build.gradle</code> file for <code>minSdkVersion 15</code> or higher.
        For the best performance, configure your app for <code>minSdkVersion
        21</code> or higher.
      </p>
    </li>

<br />

<br />

**New additions to Lint:**

- Inspection of `switch` statements using [@IntDef](https://developer.android.com/reference/androidx/annotation/IntDef) annotated integers to make sure all constants are handled. To quickly add any missing statements, use the intention action drop-down menu and select **Add Missing @IntDef
  Constants**.
- Flags for incorrect attempts to use string interpolation to insert version numbers in the `build.gradle` file.
- Flags for anonymous classes that extend the [Fragment](https://developer.android.com/reference/android/app/Fragment) class.
- Flags for native code in unsafe locations, such as the `res/` and `asset/` folders. This flag encourages storing native code in the `libs/` folder, which is then securely packaged into the application's `data/app-lib/` folder at install time. [AOSP: #169950](https://android-review.googlesource.com/#/c/169950/)
- Flags for unsafe calls to [Runtime.load()](https://developer.android.com/reference/java/lang/Runtime#load(java.lang.String)) and [System.load()](https://developer.android.com/reference/java/lang/System#load(java.lang.String)) calls. [AOSP: #179980](https://android-review.googlesource.com/#/c/179980/)
- Find and remove any unused resources by selecting **Refactor \> Remove
  Unused Resources** from the menu bar. Unused resource detection now supports resources only referenced by unused resources, references in raw files such as `.html` image references, and `tools:keep` and `tools:discard` attributes used by the Gradle resource shrinker, while considering inactive source sets (such as resources used in other build flavors) and properly handling static field imports.
- Checks that implicit API references are supported on all platforms targeted by `minSdkVersion`.
- Flags improper usage of [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView) and [Parcelable](https://developer.android.com/reference/android/os/Parcelable).
- [@IntDef](https://developer.android.com/reference/androidx/annotation/IntDef), [@IntRange](https://developer.android.com/reference/androidx/annotation/IntRange), and [@Size](https://developer.android.com/reference/androidx/annotation/Size) inspections are now also checked for `int` arrays and varargs.

<br />

<br />

**Additional Improvements**:

- Optimized for Android Emulator 2.0, which is faster than ever before, supports a wider range of virtual devices, and features a drastically improved UI. To learn more about the new emulator, read the [SDK Tools release notes](https://developer.android.com/studio/releases/sdk-tools#notes).  

    <li>Improvements to the <a href=
    "/tools/devices/managing-avds.html">Android Virtual Device
    Manager</a>:
      <ul>
        <li>System images are now categorized under the following tabs:
        <em>Recommended</em>, <em>x86</em>, and <em>Other</em>.
        </li>
        <li>Under advanced settings, you can enable multi-core support and
        specify the number of cores the emulator can use.
        </li>
        <li>Under advanced settings, you can determine how graphics are rendered
        on the emulator by selecting one of the following options:
          <ul>
            <li>
              <strong>Hardware:</strong> use you computer's graphics card for
              faster rendering.
            </li>
            <li>
              <strong>Software:</strong> use software-based rendering.
            </li>
            <li>
              <strong>Auto:</strong> let the emulator decide the best option. This
              is the default setting.
            </li>
          </ul>
        </li>
      </ul>
    </li>

    <li>Improved AAPT packaging times by specifying deploy target before the app
    is built. This allows Android Studio to efficiently package only the
    resources required by the specified device.
    </li>

    <li>Added Cloud Test Lab integration to provide on-demand app testing with
    the convenience and scalability of a cloud service. Learn more about how you
    can <a href="/training/testing/start/index.html#run-ctl">use Cloud
    Test Lab with Android Studio</a>.
    </li>

    <li>Added a preview of the new <a class="external-link" href=
    "//tools.android.com/tech-docs/gpu-profiler">GPU Debugger</a>. For graphics
    intensive applications, you can now visually step through your OpenGL ES code
    to optimize your app or game.
    </li>

    <li>Added Google App Indexing Test. Add support for URLs, app
    indexing, and search functionality to your apps to help drive more
    traffic to your app, discover which app content is used most, and attract
    new users. Test and validate URLs in your app all within Android
    Studio. See <a href=
    "/tools/help/app-link-indexing.html">Supporting URLs and App
      Indexing in Android Studio</a>.
    </li>

    <li>Upgrades from the latest IntelliJ 15 release, including improved code
    analysis and performance. See <a class="external-link" href=
    "https://www.jetbrains.com/idea/whatsnew">What's New in IntelliJ</a> for a
    complete description of the new features and enhancements.
    </li>

    <li>XML editor auto-complete now adds quotations marks when completing
    attributes. To check if this option is enabled, open the <b>Setting</b> or
    <b>Preferences</b> dialogue, navigate to <b>Editor &gt; General &gt; Smart
    Keys</b>, and check the box next to <b>Add quotes for attribute value on
    attribute completion</b>. <a class="external-link" href=
    "//b.android.com/195113">Issue: 195113</a>
    </li>

    <li>The XML editor now supports code completion for <a href=
    "/topic/libraries/data-binding/index.html#layout_details">data binding</a>
    expressions.
    </li>

<br />