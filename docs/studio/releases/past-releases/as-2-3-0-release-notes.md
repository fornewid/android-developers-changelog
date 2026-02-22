---
title: https://developer.android.com/studio/releases/past-releases/as-2-3-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-2-3-0-release-notes
source: md.txt
---

<br />

# Android Studio 2.3 (March 2017)

Android Studio 2.3.0 is primarily a bug fix and stability release, but it
also includes a number of new features.  

**2.3.3 (June 2017)**


This is a minor update to add support for Android O (API level 26).  

**2.3.2 (April 2017)**


This is a minor update to Android Studio 2.3 for the following changes:

- AVD Manager updates to support Google Play in system images.
- Bug fixes for NDK builds when using R14+ of the NDK.


Also see corresponding updates for [Android Emulator 26.0.3](https://developer.android.com/studio/releases/emulator).  

**2.3.1 (April 2017)**


This is a minor update to Android Studio 2.3 that fixes an issue where some
physical Android devices did not work properly with [Instant Run](https://developer.android.com/studio/run#instant-run) (see [Issue
#235879](https://code.google.com/p/android/issues/detail?id=235879)).

<br />

    <h1 class="hide-from-toc">
      New
    </h1>

    <div class="video-wrapper-left">
      <iframe class="devsite-embedded-youtube-video" data-video-id="VFyKclKBGf0"
              data-autohide="1" data-showinfo="0" frameborder="0" allowfullscreen>
      </iframe>
    </div>

    <ul>
      <li>Android Studio can now convert PNG, BMP, JPG, and static GIF files to
      WebP format. WebP is an image file format from Google that provides lossy
      compression (like JPEG) as well as transparency (like PNG) but can provide
      better compression than either JPEG or PNG. For more information, see
        <a href="/studio/write/convert-webp.html">Convert images to WebP in Android
        Studio</a>.
      </li>

      <li>The new <a href="/studio/write/app-link-indexing.html">App Links
      Assistant</a> simplifies the process of adding Android App Links to your app
      into a step-by-step wizard. Android App Links are HTTP URLs that bring users
      directly to specific content in your Android app.
      </li>

      <li>The Layout Editor now includes support for two new ConstraintLayout
      features:
        <ul>
          <li>Define a view size based on an aspect ratio.
          </li>
          <li>Create packed, spread, and weighted linear groups with constraint
          chains.
          </li>
        </ul>
        For more information, see <a href=
        "/training/constraint-layout/index.html">Build a Responsive UI with
        ConstraintLayout</a>.
      </li>

      <li>The Layout Editor also now lets you create a list of <a href=
      "/studio/write/layout-editor.html#edit-properties">favorite attributes</a> so
      you don't have to click <b>View all attributes</b> to access the attributes
      you use most.
      </li>

      <li>When adding a material icon using the Vector Import Dialog (<b>File &gt;
      New &gt; Vector Asset</b>), you can now filter the list of available icons by
      category or by icon name. For more information, see <a href=
      "/studio/write/vector-asset-studio.html#materialicon">Adding a material
      icon</a>.
      </li>

      <li>
        <a href="/studio/write/annotations.html#accessibility">New and updated
        annotations</a>. The new <code>@RestrictTo</code> annotation for methods,
        classes, and packages lets you restrict an API. The updated
        <code>@VisibleForTesting</code> annotation now has an optional
        <code>otherwise</code> argument that lets you designate what the visibility
        of a method should be if not for the need to make it visible for testing.
        Lint uses the <code>otherwise</code> option to enforce the intended
        visibility of the method.
      </li>

      <li>New <a href="/studio/write/lint.html#snapshot">lint baseline support</a>
      allows you to use a snapshot of your project's current set of warnings as a
      baseline for future inspection runs so only new issues are reported. The
      baseline snapshot lets you start using lint to fail the build for new issues
      without having to go back and address all existing issues first.
      </li>

      <li>New lint checks, including the following:
        <ul>
          <li>Obsolete <code>SDK_INT</code> Checks: Android Studio removes obsolete
          code that checks for SDK versions.
          </li>
          <li>Object Animator Validation: Lint analyzes your code to make sure that
          your <code>ObjectAnimator</code> calls reference valid methods with the
          right signatures and checks that those methods are annotated with <code>
            @Keep</code> to prevent ProGuard from renaming or removing them during
            release builds.
          </li>
          <li>Unnecessary Item Decorator Copy: Older versions of the
          <code>RecyclerView</code> library did not include a divider decorator
          class, but one was provided as a sample in the support demos. Recent
          versions of the library have a divider decorator class. Lint looks for
          the old sample and suggests replacing it with the new one.
          </li>
          <li>WifiManager Leak: Prior to Android 7.0 (API level 24), initializing
          the <code>WifiManager</code> with <code><a href="/reference/android/content/Context.html#getSystemService(java.lang.Class&lt;T&gt;)">Context.getSystemService()</a></code>
          can cause a memory leak if the context is not the application context.
          Lint looks for these initializations, and if it <em>cannot</em> determine
          that the context is the application context, it suggests you use <code><a href="/reference/android/content/Context.html#getApplicationContext()">Context.getApplicationContext()</a></code> to get the proper context for the
          initialization.
          </li>
          <li>Improved Resource Prefix: The existing <code>resourcePrefix</code>
          lint check had many limitations. You can now configure your project with
          a prefix, such as <code>android { resourcePrefix '<var>my_lib</var>'
          }</code>, and lint makes sure that all of your resources are using this
          prefix. You can use variations of the name for styles and themes. For
          example for the <var>my_lib</var> prefix, you can have themes named
          <code>MyLibTheme</code>, <code>myLibAttr</code>,
          <code>my_lib_layout</code>, and so on.
          </li>
          <li>Switch to WebP: This check identifies images in your project that can
          be converted to WebP format based on your project's
          <code>minSdkVersion</code> setting. An associated quickfix can
          automatically convert the images, or you can <a href=
          "/studio/write/convert-webp.html">convert images to WebP</a> manually.
          </li>
          <li>Unsafe WebP: If your project already includes WebP images, this check
          analyzes your project to ensure that your <code>minSdkVersion</code>
          setting is high enough to support the included images. For more
          information about WebP support in Android and Android Studio, see
          <a class="external" href=
          "https://developers.google.com/speed/webp/faq#which_web_browsers_natively_support_webp">
            Which browsers natively support WebP?</a> and <a href=
            "/studio/write/convert-webp.html">Create WebP Images Using Android
            Studio</a>.
          </li>
        </ul>
      </li>
    </ul>

    <h1 class="hide-from-toc">
      Changes
    </h1>

    <ul>
      <li>A separate button to push changes with Instant Run: After deploying your
      app, you now click <b>Apply Changes</b> <img src=
      "/studio/images/buttons/toolbar-apply-changes.svg" alt="" class=
      "inline-icon"> to quickly push incremental changes to your running app using
      Instant Run. The <b>Run</b> <img src="/studio/images/buttons/toolbar-run.png"
        alt="" class="inline-icon"> and <b>Debug</b> <img src=
        "/studio/images/buttons/toolbar-debug.png" alt="" class="inline-icon">
        buttons are always available to you when you want to reliably push your
        changes and force an app restart.
        <ul>
          <li>Instant Run is supported only when deploying your app to a target
          device running Android 5.0 (API level 21) or higher.
          </li>
          <li>Instant Run is no longer disabled for projects that <a href=
          "/studio/projects/add-native-code.html">link to external native
          projects</a> using CMake or ndk-build. However, you can only use Instant
          Run to push incremental changes to your Java code, not your native code.
          </li>
          <li>Cold swaps (which you can force for a running app by clicking
          <strong>Run</strong> <img src="/studio/images/buttons/toolbar-run.png"
          alt="" class="inline-icon">) are now more reliable. Forcing a cold swap
          also fixes the issue where changes to notification and widget UIs were
          not updated on the target device.
          </li>
          <li>Includes optimizations that make app startup much faster. These
          optimizations may affect profiling, so you should temporarily <a href=
          "/studio/run/index.html#disable-ir">disable Instant Run</a> whenever
          profiling your app.
          </li>
        </ul>
      </li>

      <li>
        <p>
          The <b>AVD Manager</b> <img src=
          "/studio/images/buttons/toolbar-avd-manager.png" alt="" class=
          "inline-icon"> and <b>SDK Manager</b> <img src=
          "/studio/images/buttons/toolbar-sdk-manager.png" alt="" class=
          "inline-icon"> buttons are now included in the lean Navigation Bar as
          well as the full Toolbar. To use the lean Navigation Bar, click
          <b>View</b> to open the View menu, then ensure that <b>Navigation Bar</b>
          is selected and <b>Toolbar</b> is <em>not</em> selected.
        </p>
        <img src="/studio/images/releases/navigationbar_sdkavd_2x.png" width="757">
      </li>

      <li>The "Hybrid" debugger has been renamed to "Dual" debugger.
      </li>

      <li>In the <a href="/studio/run/rundebugconfig.html">Run/Debug
      Configurations</a> dialog, under Defaults in the left pane, the following run
      configuration names have changed with no behavior changes:
        <ul>
          <li>The JUnit name has changed to Android JUnit. If you have a project
          that uses JUnit run configurations, those configurations are transformed
          to Android JUnit run configurations the first time you open the project
          with Android Studio. A dialog appears to inform you of the name change.
          </li>
          <li>The Android Tests name has changed to Android Instrumented Tests.
          </li>
        </ul>
      </li>

      <li>The <a href="/studio/debug/am-gpu-debugger.html">GPU Debugger</a> has
      been removed from Android Studio as of version 2.3. An open-source,
      standalone version of the tool is now available on <a href=
      "https://github.com/google/gapid" class="external-link">GitHub</a>.
      </li>

      <li>The Run/Debug option is no longer available when you right-click a <code>
        *.gradle build</code> script.
      </li>

      <li>All templates now use <code>ConstraintLayout</code> as the default
      layout.
      </li>

      <li>The Widgets palette in the Layout Editor has been redesigned.
      </li>
    </ul>

    <p>
      This release also includes a number of bug fixes. <a href=
      "https://code.google.com/p/android/issues/list?can=1&amp;q=target%3D2.3+status%3DReleased&amp;colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&amp;cells=tiles">
      See all bug fixes in 2.3.0.</a>
    </p>

    <p class="note">
      <b>Known issue:</b> Some device manufacturers block apps from automatically
      launching after being installed on the device. When deploying your app to a
      physical device using Android Studio 2.3, this restriction breaks the
      intended behavior of Instant Run and causes the following error output:
      <code>Error: Not found; no service started</code>. To avoid this issue,
      either <a href="/studio/run/emulator.html">use the emulator</a> or enable
      automatic launching for your app in your device's settings. The procedure
      for doing this is different for each device, so check the instructions
      provided by the manufacturer. To learn more about this issue, see
      <a href="https://code.google.com/p/android/issues/detail?id=235879">Issue
        #235879</a>.
    </p>