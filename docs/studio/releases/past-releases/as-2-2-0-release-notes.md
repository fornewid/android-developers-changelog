---
title: https://developer.android.com/studio/releases/past-releases/as-2-2-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-2-2-0-release-notes
source: md.txt
---

    <h1 id="2-2-0" class="showalways">Android Studio 2.2 (September 2016)</h1>

<br />


**2.2.3 (December 2016)**

<br />

    <p>
      This is a minor update to Android Studio 2.2. It includes a bug fixes
      focused around gradle, the core IDE, and lint.
    </p>

    <p>
      Highlighted build changes:
    </p>

    <ul>
      <li>ProGuard version rollback. Due to a <a href=
      "https://sourceforge.net/p/proguard/bugs/625/">correctness issue</a>
      discovered in ProGuard 5.3.1, we have rolled back to ProGuard 5.2.1. We
      have worked with the ProGuard team on getting a fix quickly, and we expect
      to roll forward to ProGuard 5.3.2 in Android Studio 2.3 Canary 3.
      </li>
      <li>Bug fix for <code>aaptOptions</code> <code>IgnoreAssetsPattern</code>
      not working properly (<a href="http://b.android.com/224167">issue
      224167</a>)
      </li>
      <li>Bug fix for Gradle autodownload for Constraint Layout library
        (<a href="https://code.google.com/p/android/issues/detail?id=212128">issue
        212128</a>)
      </li>
      <li>Bug fix for a JDK8/Kotlin compiler + dx issue (<a href=
      "http://b.android.com/227729">issue 227729</a>)
      </li>
    </ul>

    <p>
      <a href=
      "https://code.google.com/p/android/issues/list?can=1&amp;q=target%3D2.2.3+status%3AReleased+&amp;colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&amp;cells=tiles">
      See all bug fixes in 2.2.3</a>.
    </p>

<br />

<br />

<br />


**2.2.2 (October 2016)**

<br />

    <p>
      This is a minor update to Android Studio 2.2. It includes a number of small
      changes and bug fixes, including:
    </p>

    <ul>
      <li>When reporting Instant Run issues through the IDE, the report now also
      includes logcat output for <code>InstantRun</code> events. To help us
      improve Instant Run, please <a href=
      "/studio/run/index.html#submit-feedback">enable extra logging and report
      any issues</a>.
      </li>
      <li>A number of small bug fixes for Gradle.
      </li>
      <li>A fix for problems with generating multiple APKs.
      </li>
    </ul>

<br />

<br />

<br />


**2.2.1 (October 2016)**

<br />

    <p>
      This is a minor update to Android Studio 2.2. It includes several bug fixes
      and a new feature to enable extra logging to help us troubleshoot Instant
      Run issues---to help us improve Instant Run, please <a href=
      "/studio/run/index.html#submit-feedback">enable extra logging and report
      any issues</a>.
    </p>

<br />

<br />

<br />

# New

<br />

<br />

<br />

<br />

- All new **[Layout
Editor](https://developer.android.com/studio/write/layout-editor)** with tools custom-built to support [ConstraintLayout](https://developer.android.com/training/constraint-layout).  

    <li>New <strong><a href=
    "http://tools.android.com/tech-docs/layout-inspector">Layout
    Inspector</a></strong> lets you examine snapshots of your layout hierarchy
    while your app is running on the emulator or a device.
    </li>

    <li>New <strong><a href="/studio/write/firebase.html">Assistant</a></strong>
    window to help you integrate Firebase services into your app.
    </li>

    <li>New <strong><a href="/studio/debug/apk-analyzer.html">APK
    Analyzer</a></strong> tool so you can inspect the contents of your packaged
    app.
    </li>

    <li>New <strong><a href=
    "http://tools.android.com/tech-docs/test-recorder">Espresso Test
    Recorder</a></strong> tool (currently in beta) to help you create UI tests by
    recording your own interactions.
    </li>

    <li>New <strong><a href=
    "http://tools.android.com/tech-docs/build-cache">build cache</a></strong>
    (currently experimental) to speed up build performance.
    </li>

    <li>New <strong>C/C++ build integration with CMake and ndk-build</strong>.
    Compile and build new or existing native code into libraries packaged into
    your APK, and debug using lldb. For new projects, Android Studio uses CMake
    by default, but also supports ndk-build for existing projects. To learn how
    to include native code in your Android application, read <a href=
    "/studio/projects/add-native-code.html">Add C and C++ Code to Your
    Project</a>. To learn how to debug native code with lldb, see <a href=
    "/studio/debug/index.html#debug-native">Debug Native Code</a>.
    </li>

    <li>New <strong><a href="/studio/intro/index.html#sample-code">Samples
    Browser</a></strong> so you can easily look up Google Android sample code
    from within Android Studio to jump start app development.
    </li>

    <li>New <strong>Merged Manifest Viewer</strong> to help you diagnose how your
    manifest file merges with your app dependencies across project build
    variants.
    </li>

    <li>The <strong>Run</strong> window now contains log messages for the current
    running app. Note that you can configure the <a href=
    "/studio/debug/am-logcat.html">logcat Monitor</a> display, but not the
    <strong>Run</strong> window.
    </li>

    <li>New <strong><a href="/studio/run/emulator.html">Android
    Emulator</a></strong> features:
      <ul>
        <li>Added new <strong>Virtual</strong> <strong>Sensors</strong> and
        <strong>Cellular</strong> &gt; <strong>Signal Strength</strong> controls.
        </li>
        <li>Added an <strong>LTE</strong> option to the <strong>Cellular</strong>
        &gt; <strong>Network type</strong> control.
        </li>
        <li>Added simulated vertical swipes for scrolling through vertical menus
        with a mouse wheel.
        </li>
      </ul>
    </li>

    <li>New <strong><a href="/studio/run/rundebugconfig.html">Run/Debug
    Configuration</a></strong> features:
      <ul>
        <li>The <strong>Debugger</strong> tab of the Android App and Android
        Tests templates now contain several new options for debugging with LLDB.
        </li>
        <li>The <strong>Profiling</strong> tab of the Android App and Android
        Tests templates now contain a <strong>Capture GPU Commands</strong>
        option for enabling GPU tracing. You can display GPU traces in the GPU
        Debugger (a beta feature).
        </li>
        <li>The Android Tests template now has a <strong>Firebase Test Lab Device
        Matrix</strong> option for the <strong>Deployment Target</strong>.
        </li>
        <li>The Native Application template has been deprecated. If you use this
        template in a project, Android Studio automatically converts it to the
        Android App template.
        </li>
        <li>The Android Application template has been renamed to Android App.
        </li>
      </ul>
    </li>

    <li>Improved installation, configuration, performance, and UI features in the
    <strong><a href="/studio/debug/am-gpu-debugger.html">GPU
    Debugger</a></strong> (currently in beta).
    </li>

    <li>Android Studio now comes bundled with <strong>OpenJDK 8</strong>.
    Existing projects still use the JDK specified in <strong>File &gt; Project
    Structure &gt; SDK Location</strong>. You can switch to use the new bundled
    JDK by clicking <strong>File &gt; Project Structure &gt; SDK
    Location</strong> and checking the <strong>Use embedded JDK</strong>
    checkbox.
    </li>

    <li>Added new <strong>help menus and buttons</strong> in the UI so you can
    more easily find the online documentation.
    </li>

<br />

<br />

# Changes

<br />

<br />

- Updated the IDE codebase from IntelliJ 15 to **IntelliJ
  2016.1**
- Instant Run now requires the platform SDK corresponding to the target device API level to be installed.
- Instant Run will automatically disabled if user is running the app under a work profile or as a secondary user.
- Fixed many reliability issues for **[Instant Run](https://developer.android.com/studio/run#instant-run)** where changes were not getting deployed or the app would crash:
  - Some app assets were not deployed to your running app. ( [Bug: #213454](http://b.android.com/213454))
  - App crashes when user transitions between Instant Run and non Instant Run sessions where a Serializable class does not have serialVersionUID defined. ([Bug: #209006](http://b.android.com/209006))
  - Style changes aren't reflected with Instant Run. ([Bug: #210851](http://b.android.com/210851))
  - Instant Run session is unreliable and causes FileNotFoundException. ([Bug: #213083](http://b.android.com/213083))
  - Changes to drawables not reflected until full rebuild is performed for KitKat. ([Bug: #21530](http://b.android.com/215360))
  - Resource changes aren't reflected with Instant Run when custom sourceSets contain nested paths. ([Bug: #219145](http://b.android.com/219145))
  - Hot and warm swap don't work if changed class contains annotation with enum value. ([Bug: #209047](http://b.android.com/209047))
  - Changes to annotation data not reflected with Instant Run. ([Bug: #210089](http://b.android.com/210089))
  - Instant Run doesn't pick up code changes if you make changes outside the IDE. ([Bug: #213205](http://b.android.com/213205))
  - Instant Run session is unreliable due to mismatch security token. ([Bug: #211989](http://b.android.com/211989)
  - Cold swap fails for devices that doesn't properly support run-as. ([Bug: #210875](http://b.android.com/210875))
  - App crash after instant run restart. ([Bug: #219744](http://b.android.com/219744))
- ClassNotFoundException observed when switching from Instant Run to Instant Debug. ([Bug: #215805](http://b.android.com/215805))  

    <li>Improved performance for <strong>Gradle sync</strong> within the IDE,
    especially for large projects.
    </li>

    <li>Improved build times for both full and incremental builds with new app
    packaging code.
    </li>

    <li>Improved <strong>Jack compiler performance and features</strong>,
    including support for annotation processors and dexing in process. To learn
    more, read the <a href=
    "/studio/releases/gradle-plugin.html#revisions">Android plugin for Gradle
    2.2.0 release notes</a>.
    </li>

    <li>Removed the <strong>Scale</strong> AVD property from the AVD Manager.
    </li>

    <li>The Android Emulator <strong>-port</strong> and <strong>-ports</strong>
    command-line options now report which ports and serial number the emulator
    instance is using, and warn if there are any issues with the values you
    provided.
    </li>

    <li>Improved the <strong><a href=
    "/studio/write/create-java-class.html">Create New Class dialog</a></strong>
    and the corresponding file templates. <strong>Note:</strong> If you've
    previously customized the <strong>AnnotationType</strong>,
    <strong>Class</strong>, <strong>Enum</strong>, <strong>Interface</strong>, or
    <strong>Singleton</strong> file templates, you need to modify your templates
    to comply with the new templates or you won't be able to use the new fields
    in the <strong>Create New Class</strong> dialog.
    </li>

    <li>Improved the <strong><a href=
    "/studio/write/vector-asset-studio.html">Vector Asset Studio</a></strong>
    user interface and added support for Adobe Photoshop Document (PSD) files.
    </li>

    <li>Improved the <strong><a href=
    "/studio/write/image-asset-studio.html">Image Asset Studio</a></strong> user
    interface.
    </li>

    <li>Improved the <strong>Theme Editor</strong>'s Resource Picker.
    </li>

    <li>Fixed memory leaks and reduced overall memory usage in Android Studio.
    </li>

    <li>Added a <strong>Background</strong> button in the <strong><a href=
    "/studio/intro/update.html#sdk-manager">SDK Manager</a></strong> so you can
    get back to work and install your packages in the background.
    </li>

    <li>Improved <strong><a href="/studio/intro/accessibility.html">Accessibility
    features</a></strong>, including support for screen readers and keyboard
    navigation.
    </li>

    <li>Enhanced <strong>Code Analysis</strong> includes code quality checks for
    Java 8 language usage and more cross-file analysis.
    </li>

    <li>Several toolbar icons have changed.
    </li>

<br />