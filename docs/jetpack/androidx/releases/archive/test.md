---
title: https://developer.android.com/jetpack/androidx/releases/archive/test
url: https://developer.android.com/jetpack/androidx/releases/archive/test
source: md.txt
---

# Test Release Note Archive

| **Note:** These are the original release notes for Test components that shipped in the support library. For the current release notes see the[Androidx release notes](https://developer.android.com/jetpack/androidx/releases/test).

## AndroidX Test Espresso 3.1.1, Runner 1.1.1, Rules 1.1.1, Monitor 1.1.1 AndroidTestOrchestrator 1.1.1, Core 1.1.0, Truth 1.1.0, JUnit 1.1.0 (2018-12-13)

This is the stable release of AndroidX Test 1.1.0

- *Core*
  - Make ActivityScenario support activities which start another activity

## AndroidX Test Espresso 3.1.1-beta01, Runner 1.1.1-beta01, Rules 1.1.1-beta01, Monitor 1.1.1-beta01 AndroidTestOrchestrator 1.1.1-beta01, Core 1.1.0-beta01 Truth 1.1.0-beta01, JUnit 1.1.0-beta01 (2018-12-06)

- *Core*
  - New core-ktx kotlin extension artifact! Includes a kotlin-friendly ActivityScenario.launchActivity API
  - New ActivityScenario API for launching activities with custom intents
  - New ActivityScenario API for receiving an Activity result
  - Make ActivityScenario closeable
- *Espresso*
  - Modify withResourceNameMatcher and HumanReadables to be API 28 compatible.
  - Update ReplaceTextAction's description to include the stringToBeSet
  - Support Espresso in Robolectric paused looper mode.
- *JUnit*
  - New ActivityScenarioRule API, for auto-launching and closing an Activity on test setup and teardown
  - New junit-ktx kotlin extension artifact! Includes a kotlin-friendly ActivityScenarioRule API
- *Runner*
  - Make -e package and -e testFile consistent in behavior when receiving packages
- *Truth*
  - Add bool, parcelable, and parcelableAsType BundleSubject APIs

## AndroidX Test Espresso 3.1.0, Runner 1.1.0, Rules 1.1.0, Monitor 1.1.0 AndroidTestOrchestrator 1.1.0, Core 1.0.0 Truth 1.0.0, JUnit 1.0.0 (2018-10-24)

- *All*
  - Set minSdkVersion to 14 and targetSdkVersion to 28
- *Espresso*
  - Fix withContentDescription to work with non-string types
  - Add support for using Espresso on Robolectric
  - Issue[72798625](https://issuetracker.google.com/issues/72798625): Espresso ViewMatchers.withText doesn't work when textAllCaps is enabled
  - Add support for injecting a sequence of motion events
- *Intents*
  - Add beta API for retrieving list of intents. Intended for use with new truth assertions
- *Runner*
  - Add support for instant apps
  - Deprecate androidx.test.runner.AndroidJUnit4 and replace with androidx.test.ext.junit.runners.AndroidJUnit4
- *Monitor*
  - Deprecate androidx.test.InstrumentationRegistry and replace with androidx.test.platform.app.InstrumentationRegistry and androidx.test.core.app.ApplicationProvider
- *AndroidTestOrchestrator*
  - Only enable orchestrator coverage handling if both 'coverage' and 'coverageFilePath' arguments are passed.
  - Only wait for debugger when the -debug is set but not for listing ATO test cases. A new orchestratorDebug flag was added for debugging orchestrator itself
- *Core*
  - New artifact! Includes new APIs that support both local and on-device tests for:
    - Retrieving context: ApplicationProvider
    - Controlling activity lifecycles: ActivityScenario(beta)
    - Builders for MotionEvent, PackageInfo
    - Parceables utility class
- *Truth*
  - New artifact! Includes custom truth subjects for Notification, Intent, Bundle, Parcelable, and MotionEvent
- *JUnit*
  - New artifact! Includes JUnit runner class androidx.test.ext.junit.runners.AndroidJUnit4 that supports both local and on-device tests.

## Espresso 3.0.2-beta1, Runner 1.0.2-beta1, Rules 1.0.2-beta1, Monitor 1.0.2-beta1, AndroidTestOrchestrator 1.0.2-beta1 (2018-04-16)

- *Espresso*
  - Breaking API Change:
    - It was brought up to our attention in Issue[64062890](https://issuetracker.google.com/issues/64062890)that we were using Guava Optional in our public API. This was terrible oversight on our part . As a result, there is a breaking public API change in this release to address this issue. We introduced an ugly wrapper around Guava Optional class, named EspressoOptional which lives under "android.support.test.espresso.util" namespace. Developers that were using the leaked Guava Optional API need to change their imports and references to use EspressoOptional during the update to this new version. Sorry for the inconvenience this may cause.
  - onView() and onData() APIs are now marked @CheckReturnValue to prevent errors
  - Fixed espresso-core POM file to not pull in "rules" dependency, instead have espresso-intents POM pull it. This should be a NoOp change for developers since espresso-intents cannot be used without espresso-core.
  - Issue[65486414](https://issuetracker.google.com/issues/65486414): Espresso missing guava dependency
  - Issue[65576174](https://issuetracker.google.com/issues/65576174): Espresso IdlingResourceRegistry.sync causes second test fail
  - Issue[65568629](https://issuetracker.google.com/issues/65568629): Espresso.onIdle not using IdlingRegistry
  - Issue[69333598](https://issuetracker.google.com/issues/69333598): espresso 3.0.1 incompatible with play-services-auth:11.6.0 in android library module.
  - Issue[64062890](https://issuetracker.google.com/issues/64062890): Internal Optional type exposed by AdapterViewProtocol interface
  - Issue[64091847](https://issuetracker.google.com/issues/64091847): Espresso 3.0.0 should NOT depend on test runner
  - Issue[73722050](https://issuetracker.google.com/issues/73722050): espresso-contrib 3.0.2-alpha1 packages android.arch.{lifecycle/core} classes
- *Espresso-remote*
  - This is a brand new artifact. We decoupled all of Espresso's multi process functionality outside of espresso-core artifact. This is cleaner and should significantly reduce espresso-core's overall size and method count.
- *Runner*
  - Truncate stack trace if too large for a binder transaction. Since AJUR needs to report failures back to AM via a binder IPC, we need to make sure that we don't exceed the Binder transaction limit - which is 1MB per process.
  - Issue[65828576](https://issuetracker.google.com/issues/65828576): TestRequestBuilder crash when running test in class with @Ignore
  - Issue[37057596](https://issuetracker.google.com/issues/37057596): We don't handle failures in @BeforeClass
- *Rules*
  - Ensure to release a reference on the activity under test after lifecycle changes. During the duration of the test one is now able to manipulate the Activity directly using the reference obtained from #getActivity() If the Activity is finished and relaunched, the reference returned by #getActivity() now always points to the current instance of the Activity.
  - Issue[64389280](https://issuetracker.google.com/issues/64389280):[GrantPermissionRule](https://developer.android.com/reference/android/support/test/rule/GrantPermissionRule.html)doesn't provide WRITE_EXTERNAL_STORAGE
  - Issue[37065965](https://issuetracker.google.com/issues/37065965):[ActivityTestRule](https://developer.android.com/reference/android/support/test/rule/ActivityTestRule.html)leaks activity after orientation change
  - Issue[75254050](https://issuetracker.google.com/issues/75254050):[ActivityTestRule](https://developer.android.com/reference/android/support/test/rule/ActivityTestRule.html)doesn't update Activity instance during configuration changes
  - Issue[64464625](https://issuetracker.google.com/issues/64464625): Cannot do UI work in method finish() of Activity
- *AndroidTestOrchestrator*
  - Pass`-e coverage true -e coverageFilePath /sdcard/foo/`flags to generate coverage files in the given location (The app must have permission to write to the given location). The coverage file naming convention now looks like this`com.foo.Class#method1.ec`. Note, this is only supported when running in isolated mode. Also, it cannot be used together with AndroidJUnitRunner's`coverageFile`flag. Since the generated coverage files overwrite each other.
  - Pass`-e clearPackageData`flag if you wish the orchestrator to run`pm clear context.getPackageName()`and`pm clear targetContext.getPackageName()`commands in between test invocations. Note, the context in the clear command is the App under test context.
  - Fixed - When running an empty test, aka. no @Test inside the target, the test result is different than legacy mode.
  - Issue[72758547](https://issuetracker.google.com/issues/72758547): Test Orchestrator causes Jacoco Coverage Data to be incomplete, only has last test run data
  - Issue[67916042](https://issuetracker.google.com/issues/67916042): Android Test Orchestrator : Execution stopped on Process crash due to OutOfMemory
  - Issue[77752735](https://issuetracker.google.com/issues/77752735): Orchestrator crashes for TransactionTooLargeException
  - Issue[77549481](https://issuetracker.google.com/issues/77549481): Test Orchestrator Should Run "pm clear" After Each Test

## Espresso 3.0.2-alpha1, Runner 1.0.2-alpha1, Rules 1.0.2-alpha1, AndroidTestOrchestrator 1.0.2-alpha1 (2017-12-05)

- *Espresso*

  - `Intents`now has a callable response, allowing tests to execute after capturing a fired intent but before returning an[Instrumentation.ActivityResult](https://developer.android.com/reference/android/app/Instrumentation.ActivityResult)object.
- *Runner*

  - Split out monitor maven artifact`com.android.support.test:monitor:<version>`, for users who need[`MonitoringInstrumentation`](https://developer.android.com/reference/android/support/test/runner/MonitoringInstrumentation)without test running and JUnit features.

    If you use`com.android.support.test:runner:<version>`, everything works as expected, because Gradle automatically pulls in the`monitor`module as a dependency of the`runner`module.
  - Added flag`newRunListenerOrderMode`. When`true`, user-defined listeners run before default listeners. (We expect this behavior to eventually become the default.)

  - Issue[65828576](https://issuetracker.google.com/issues/65828576):`TestRequestBuilder`crashes when running tests in a class annotated with`@Ignore`(standalone without test running or JUnit features).

- *AndroidTestOrchestrator*

  - Now handles empty tests in the same way as non-orchestrated[`AndroidJUnitRunner`](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner).
  - Orchestrator can now handle very large standard output from`AndroidJUnitRunner`.

## Espresso 3.0.1, Runner 1.0.1, Rules 1.0.1, AndroidTestOrchestrator 1.0.1 (2017-08-28)

- *Espresso*

  - Added a[`IdlingPolicy`](https://developer.android.com/reference/android/support/test/espresso/IdlingPolicy)option to suppress`onTimeout()`when a step debugger is attached to the VM.
  - Issues[64024656](https://issuetracker.google.com/issues/64024656),[64247586](https://issuetracker.google.com/issues/64247586), and[64525881](https://issuetracker.google.com/issues/64525881): Don't report failures for unsuccessful class loading unless a user is loading specific classes by including the`-e`class runner argument.
  - Issue[64877246](https://issuetracker.google.com/issues/64877246): Add missing classes to sources JAR file.
- *Runner*

  - Simplified`ShardingFilter`logic.
  - Issue[65025743](https://issuetracker.google.com/issues/65025743):`@RequiresDevice`filter now supports FTL emulators.
- *AndroidTestOrchestrator*

  - Don't duplicate report failures. When a test process crashes after failing, now only one failure is reported for the test.
  - Fixed Javadoc for Orchestrator.
  - Tests now indicated as missed if the remote process crashes.
  - Now handles ignored test cases.
  - Now excludes ignored test cases from footer to match legacy results.
  - Fixed runtime permission issues. Test reports are now written to SD card on Android 7.0 (API level 24) and higher.

## Espresso 3.0.0, Runner 1.0.0, Rules 1.0.0, AndroidTestOrchestrator 1.0.0 (2017-07-25,[Announcement](https://android-developers.googleblog.com/2017/07/android-testing-support-library-10-is.html))

### Breaking changes

- *All artifacts*
  - Dropping support for API levels lower than 15 -- however, the min SDK still points to API level 9 to give users time to upgrade
- *Espresso*
  - The deprecated`android.support.test.espresso.contrib.CountingIdlingResource`class has been deleted and moved to[`android.support.test.espresso.idling.CountingIdlingResource`](https://developer.android.com/reference/android/support/test/espresso/idling/CountingIdlingResource)
    - Use[`getInstance().register()`](https://developer.android.com/reference/android/support/test/espresso/IdlingRegistry#register(android.support.test.espresso.IdlingResource...))instead of[`registerIdlingResources()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#registerIdlingResources(android.support.test.espresso.IdlingResource...))
  - [Guava](https://github.com/google/guava)is now jarjar'd away to a different "internal" namespace -- if you're accidentally using Guava API through Espresso namespaces, you might see breakages
    - Remove any references to shaded Guava (`.core.deps.guava.`)
    - Upgrade your Support Library version to 25.4.0 or higher

### Known issues

- *AndroidTestOrchestrator*
  - `-e numShards`and`-e shardIndex`runner arguments aren't currently supported
  - [Parameterized tests](https://github.com/junit-team/junit4/wiki/parameterized-tests)aren't currently supported

### New features

- *Espresso*
  - New[Multiprocess Espresso](https://developer.android.com/training/testing/espresso/multiprocess)Support on API 26 for`espresso-core`and`espresso-web`, but**not** `espresso-contrib`
  - New lightweight[`IdlingRegistry`](https://developer.android.com/reference/android/support/test/espresso/IdlingRegistry)API
    - Published as part of`com.android.support.test.espresso:espresso-idling-resource:3.0.0`
    - Deprecated methods:
      - [`registerIdlingResources()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#registerIdlingResources(android.support.test.espresso.IdlingResource...))
      - [`unregisterIdlingResources()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#unregisterIdlingResources(android.support.test.espresso.IdlingResource...))
      - [`getIdlingResources()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#getIdlingResources())
      - [`registerLooperAsIdlingResource(Looper)`](https://developer.android.com/reference/android/support/test/espresso/Espresso#registerLooperAsIdlingResource(android.os.Looper))
      - [`registerLooperAsIdlingResource(Looper, boolean)`](https://developer.android.com/reference/android/support/test/espresso/Espresso#registerLooperAsIdlingResource(android.os.Looper,%20boolean))
  - New API to help synchronize against[Executors](https://developer.android.com/reference/java/util/concurrent/Executors)
    - New maven artifact:`com.android.support.test.espresso.idling:idling-concurrent:3.0.0`
    - Contains[`IdlingScheduledThreadPoolExecutor`](https://developer.android.com/reference/android/support/test/espresso/idling/concurrent/IdlingScheduledThreadPoolExecutor)and[`IdlingThreadPoolExecutor`](https://developer.android.com/reference/android/support/test/espresso/idling/concurrent/IdlingThreadPoolExecutor)classes
  - New API to help synchronize against network requests and responses.
    - New maven artifact:`com.android.support.test.espresso.idling:idling-net:3.0.0`
    - Contains[`UriIdlingResource`](https://developer.android.com/reference/android/support/test/espresso/idling/net/UriIdlingResource)class
  - New`espresso-core`view matchers:
    - [`hasBackground()`](https://developer.android.com/reference/android/support/test/espresso/matcher/ViewMatchers#hasBackground(int))matches against a[View](https://developer.android.com/reference/android/view/View)object's background drawable resource
    - [`hasTextColor()`](https://developer.android.com/reference/android/support/test/espresso/matcher/ViewMatchers#hasTextColor(int))matches against a[TextView](https://developer.android.com/reference/android/widget/TextView)object's color
  - New view action methods:
    - Enhanced[`scrollTo()`](https://developer.android.com/reference/android/support/test/espresso/action/ViewActions#scrollTo())view action to work with descendants of[ListView](https://developer.android.com/reference/android/widget/ListView)
    - [`repeatedlyUntil()`](https://developer.android.com/reference/android/support/test/espresso/action/ViewActions#repeatedlyUntil(android.support.test.espresso.ViewAction,%20org.hamcrest.Matcher%3Candroid.view.View%3E,%20int))-- Performs the given[`ViewAction`](https://developer.android.com/reference/android/support/test/espresso/ViewAction)on a view until the view matches the desired[`ViewMatchers`](https://developer.android.com/reference/android/support/test/espresso/matcher/ViewMatchers)
  - New Espresso methods:
    - [`pressBackUnconditionally()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#pressBackUnconditionally())-- Similar to[`pressBack()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#pressBack())but doesn't throw an exception when Espresso navigates
    - [`noActivity()`](https://developer.android.com/reference/android/support/test/espresso/ViewInteraction#noActivity())-- Removes the need of waiting for an activity before performing a[`ViewAction`](https://developer.android.com/reference/android/support/test/espresso/ViewAction)or[`ViewAssertion`](https://developer.android.com/reference/android/support/test/espresso/ViewAssertion)
    - [`onIdle()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#onIdle())-- Loops the main thread until the app goes idle
    - [`onIdle(Callable<T>)`](https://developer.android.com/reference/android/support/test/espresso/Espresso#onIdle(java.util.concurrent.Callable%3CT%3E))-- Same as[`onIdle()`](https://developer.android.com/reference/android/support/test/espresso/Espresso#onIdle()), but takes an additional[Callable](https://developer.android.com/reference/java/util/concurrent/Callable)as a parameter, which is executed after the app goes idle
  - [`webScrollIntoView()`](https://developer.android.com/reference/android/support/test/espresso/web/webdriver/DriverAtoms)-- New`espresso-web`atom that allows you to scroll inside a[WebView](https://developer.android.com/reference/android/webkit/WebView)

<!-- -->

- *Runner*
  - [`InterceptingActivityFactory`](https://developer.android.com/reference/android/support/test/runner/intercepting/InterceptingActivityFactory)and[`SingleActivityFactory`](https://developer.android.com/reference/android/support/test/runner/intercepting/SingleActivityFactory)-- Provides a facility of testing an activity in isolation from the outer world by overriding methods like[startService()](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent))and[sendBroadcast()](https://developer.android.com/reference/android/content/Context#sendBroadcast(android.content.Intent, java.lang.String))
  - Add support for using[JUnitParams](https://github.com/Pragmatists/junitparams/wiki/Quickstart)with[`AndroidJUnitRunner`](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner)
  - Start handling[`@UiThreadTest`](https://developer.android.com/reference/android/support/test/annotation/UiThreadTest)on the core test runner level and deprecate[`@UiThreadTestRule`](https://developer.android.com/reference/android/support/test/rule/UiThreadTestRule)-- This enables the use of[`@UiThreadTest`](https://developer.android.com/reference/android/support/test/annotation/UiThreadTest)annotation directly on methods annotated with[`@Before`](http://junit.sourceforge.net/javadoc/org/junit/Before.html)and[`@After`](http://junit.sourceforge.net/javadoc/org/junit/After.html)
  - [`@SdkSupress`](https://developer.android.com/reference/android/support/test/filters/SdkSuppress)annotation now supports[`maxSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element)value (Issue[37067792](https://issuetracker.google.com/issues/37067792))
  - `-e classLoader`-- Provide the ability to pass class loaders using runner args
  - `-e filter`-- Add support for custom JUnit filters to be specified using runner args
  - `-e runnerBuilder`-- Allows developers to provide their own implementations of[`RunnerBuilder`](http://junit.org/junit4/javadoc/4.12/org/junit/runners/model/RunnerBuilder.html)that can determine whether and how they can run against a specific class

<!-- -->

- *Rules*
  - [`ProviderTestRule`](https://developer.android.com/reference/android/support/test/rule/provider/ProviderTestRule)-- New API to test[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)objects
  - [`getActivityResult()`](https://developer.android.com/reference/android/support/test/rule/ActivityTestRule#getActivityResult())and[`ActivityResultMatchers`](https://developer.android.com/reference/android/support/test/espresso/contrib/ActivityResultMatchers)-- New API to retrieve the activity result of an activity that has called[setResult()](https://developer.android.com/reference/android/app/Activity#setResult(int))
- *AndroidTestOrchestrator*
  - [Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator)provides a new way of collecting and running tests, with an emphasis on correctness and isolation. Orchestrator is an independent instrumentation process, spawning one instrumentation runner process for each test and collecting the results.
    - Application crashes take down the runner instrumentation but not the orchestrator, allowing your test suite to continue
    - Requires installation of the orchestrator APK --`'com.android.support.test:orchestrator:1.0.0'`
    - Version 1.0 has a command-line interface only; integration with Android Studio and Firebase Test Labs is planned

### Bug fixes

- *Espresso*
  - Improved root view synchronization to significantly reduce flakiness
  - Fix corruption of`IdlingResourceRegistry`
  - Better synchronization against[`IdlingResource`](https://developer.android.com/reference/android/support/test/espresso/IdlingResource)objects
  - Issue[37132680](https://issuetracker.google.com/issues/37132680): Espresso doesn't wait for dialog creation to complete before performing the next action
  - Issue[37103280](https://issuetracker.google.com/issues/37103280): Espresso should ship ProGuard consumer rules so consumers aren't required to add them
  - Issue[37094726](https://issuetracker.google.com/issues/37094726): Espresso Intents contains unnecessary application label
  - Issue[37093953](https://issuetracker.google.com/issues/37093953): Espresso: No available check for null/empty error text
  - Issue[37071776](https://issuetracker.google.com/issues/37071776):`espresso-core`embeds Guava's`.pom`files
  - Issue[37062612](https://issuetracker.google.com/issues/37062612): NPE in[`release()`](https://developer.android.com/reference/android/support/test/espresso/intent/Intents#release())
  - Issue[37063389](https://issuetracker.google.com/issues/37063389): Having Guava and`espresso-web`as`androidTest`dependencies doesn't compile
  - Issue[37070533](https://issuetracker.google.com/issues/37070533): Add support for[NavigationView](https://developer.android.com/reference/android/support/design/widget/NavigationView)in[Android Design Support Library](https://developer.android.com/training/material/design-library)

<!-- -->

- *Runner*
  - Fix the ability to use[`@UiThreadTest`](https://developer.android.com/reference/android/support/test/annotation/UiThreadTest)in combination with[`@Test(timeout = 123)`](http://junit.org/junit4/javadoc/4.12/org/junit/Test.html#timeout())
  - Fixed`-e notClass`runner arg
  - Fixed`-e log`to support JUnit3 and JUnit4 test suites, as well as[`Parameterized`](http://junit.org/junit4/javadoc/4.12/org/junit/runners/Parameterized.html)and[`Enclosed`](http://junit.org/junit4/javadoc/4.12/org/junit/experimental/runners/Enclosed.html)runners
  - Issue[37663530](https://issuetracker.google.com/issues/37663530): Wait for all activities to finish before and after each test method
  - Issue[37132680](https://issuetracker.google.com/issues/37132680): Espresso doesn't wait for dialog creation to complete before performing the next action
  - Issue[37123213](https://issuetracker.google.com/issues/37123213):[`@RequiresDevice`](https://developer.android.com/reference/android/support/test/filters/RequiresDevice)ignored on x86_64 ABI
  - Issue[37101485](https://issuetracker.google.com/issues/37101485): Some manifest-provided arguments for[`AndroidJUnitRunner`](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner)---such as test size, annotation and debug---are ignored
  - Issue[37082857](https://issuetracker.google.com/issues/37082857): Espresso semi-parallel test execution fails on static objects
  - Issue[37063396](https://issuetracker.google.com/issues/37063396): Context not initialized with[ProviderTestCase2](https://developer.android.com/reference/android/test/ProviderTestCase2)(causes[NullPointerException](https://developer.android.com/reference/java/lang/NullPointerException))

<!-- -->

- *Rules*
  - Fixed[`ActivityTestRule`](https://developer.android.com/reference/android/support/test/rule/ActivityTestRule)lifecycle to unify behavior across regular and lazy`ActivityTestRule`initialization
  - Issue[37079943](https://issuetracker.google.com/issues/37079943): Fix[`ServiceTestRule`](https://developer.android.com/reference/android/support/test/rule/ServiceTestRule)to allow re-binding
  - Issue[37109342](https://issuetracker.google.com/issues/37109342): Add[`getActivityResult()`](https://developer.android.com/reference/android/support/test/rule/ActivityTestRule#getActivityResult())and[`ActivityResultMatchers`](https://developer.android.com/reference/android/support/test/espresso/contrib/ActivityResultMatchers)
- *UiAutomator*
  - [`setUiAutomationFlags()`](https://developer.android.com/reference/android/support/test/uiautomator/Configurator#setUiAutomationFlags(int))for use with`UiAutomation.FLAG_DONT_SUPPRESS_ACCESSIBILITY_SERVICES`-- this allows`UiAutomator`to be used while other accessibility services are running
  - Issue[37082813](https://issuetracker.google.com/issues/37082813):[`setText()`](https://developer.android.com/reference/android/support/test/uiautomator/UiObject2#setText(java.lang.String))on empty[EditText](https://developer.android.com/reference/android/widget/EditText)objects throws[NullPointerException](https://developer.android.com/reference/java/lang/NullPointerException)if API level is 19 or lower

### Other notable changes

- Binaries are now published via Google Maven
- Reduced size of`espresso-core`and`espresso-web`JAR files -- embedded dependencies now have ProGuard applied
- All`.aar`files now include ProGuard rules
- Add`proguard_library.cfg`files to released artifacts
- [`Tapper`](https://developer.android.com/reference/android/support/test/espresso/action/Tapper)interface has a new version of[`sendTap()`](https://developer.android.com/reference/android/support/test/espresso/action/Tapper#sendTap(android.support.test.espresso.UiController,%20float%5B%5D,%20float%5B%5D,%20int,%20int))to implement

### External contributions

- *Espresso*
  - [Change 221522](https://android-review.googlesource.com/#/c/221522)
  - [Change 221452](https://android-review.googlesource.com/#/c/221452)
  - [Change 235980](https://android-review.googlesource.com/#/c/235980)
  - [Change 256438](https://android-review.googlesource.com/#/c/256438)
  - [Change 236730](https://android-review.googlesource.com/#/c/236730)
  - [Change 233160](https://android-review.googlesource.com/#/c/233160)
  - [Change 219761](https://android-review.googlesource.com/#/c/219761)
  - [Change 216916](https://android-review.googlesource.com/#/c/216916)
- *Runner*
  - [Change 220630](https://android-review.googlesource.com/#/c/220630)
- *Rules*
  - [Change 246570](https://android-review.googlesource.com/#/c/246570)

## Espresso 2.2.2, Runner/Rules 0.5 (2016-02-22, silent release)

### New features

- *espresso*
  - Issue[194253](https://issuetracker.google.com/issues/194253): Add support for NavigationView in android support design library
  - Added checks for enabled animations and transitions
  - New`ViewMatcher`API:`withResourceName()`

### Bug fixes

- *espresso*
  - Issue[195331](https://issuetracker.google.com/issues/195331): espresso-core embeds guava's pom files
  - Moved counting idling resource out of espresso-contrib
- *rules*
  - Issue[187249](https://issuetracker.google.com/issues/187249): NPE in`Intents.release()`
- *runner*
  - Issue 196066: The`-e log true`argument in`AndroidJUnitRunner`does not bypass actual test
  - Wait for debugger in`onCreate()`of the runner
  - Moved all supported test annotation out of platform and into ATSL
  - Removed the stack trace dump about no JSBridge
  - Fixed`AndroidAnnotatedBuilder`

### Other notable changes

- `ActivityTestRule`,`UiThreadTestRule`,`IntentsTestRule`and`ServiceTestRule`are out of beta
- Add code style settings file for uniform code formatting

## Espresso 2.2.1, Runner/Rules 0.4 (2015-09-15)

### New features

- *rules*
  - Added new`IntentsTestRule`constructor to be fully compatible with`ActivityTestRule`
- *runner*
  - Added special case multidex installation for API levels 15 and lower
  - Added exclude filters to class and package:
    - Running all tests except those in a particular class:`adb shell am instrument -w -e notClass com.android.foo.FooTest`
    - Running all but a single test:`adb shell am instrument -w -e notClass com.android.foo.FooTest#testFoo`
    - Running all tests except a particular package:`adb shell am instrument -w -e notPackage com.android.foo.bar`

### External contributions

- *espresso*
  - [157911](https://issuetracker.google.com/issues/157911): Add view matcher for input type on an`EditText`object
  - [157912](https://issuetracker.google.com/issues/157912): Add view matcher for matching error text on an`EditText`object
  - [150674](https://issuetracker.google.com/issues/150674): Add`DrawerActions`support for drawers with arbitrary gravity
  - [150744](https://issuetracker.google.com/issues/150744):`DrawerActions`no longer leak`parentListener`
  - [153303](https://issuetracker.google.com/issues/153303): Gravity specified on the "is the drawer open or closed" checks
  - [157910](https://issuetracker.google.com/issues/157910): Add`DrawerLayout`open and close action factories

### Bug fixes

- *espresso*
  - `ViewActions.closeSoftKeyboard()`now ensures that soft keyboard is completely gone
  - Fixed synchronization issue with Espresso's`Espresso.pressBack()`method on API level 21 and higher
  - Fixed synchronization for keyboard closure animations on API level 23
- *rules*
  - Fixed`ServiceTestRule`on API level 23,`startService()`must always be called with an explicit`Intent`
- *runner*
  - Fixed broken gradle`JaCoCo`support
  - Fixed broken test sharding support
  - Fixed inconsistent state in test runner after`JUnit3`style test timeouts

### Other notable changes

- Javadoc fixes and error message improvements
- Ignore`suite()`methods and don't ignore init errors when using method filters

## Espresso 2.2 / ATSL 0.3 (2015-06-09)

### New features

- *espresso-web 2.2*
  - New`WebView`support
- *espresso-core 2.2*
  - Migrated to use dagger v2
  - Migrated to use hamcrest v1.3
- *espresso-contrib 2.2*
  - Accessibility checks
  - `DrawerActions`gravity support
- *rules 0.3*
  - `DisableOnAndroidDebug`rule
- *runner 0.3*
  - Upgrade from JUnit v4.10 to JUnit v4.12
  - Migrated to use Hamcrest v1.3

### Bug fixes

- Fixed`DrawerActions`leaking`ParentListener`
- Assumption failure is now treated as an ignore test rather than a failing test
- Fixed`MonitoringInstrumentation`leaking activity instances through`ExecutorService`
- Fixed for orphan activities being stuck in stopped stage
- Update`Until.scrollFinished()`to return true if no scroll events were generated. Guard against potential NPE in`UiObject2#setText()`.

## Espresso 2.1, Test Runner/Rules 0.2 and UIAutomator 2.1.0 (2015-04-21)

### Breaking changes

- Test runner artifact split into two and the name changed from`com.android.support.test:testing-support-lib:0.1`to`com.android.support.test:runner:0.2`and`com.android.support.test:rules:0.2`.

### New features

- *espresso-intents* : A Mockito-like API that enables hermetic inter-activity testing by allowing test authors to verify and stub outgoing intents
  - `IntentsTestRule`: extends`ActivityTestRule`, initialized and releases Espresso-Intents in functional UI tests
- *espresso-core*
  - `ViewActions`: Added ability to run global assertions prior to running actions. This is useful for other frameworks that build on top of Espresso to validate state of the view hierarchy while existing Espresso test suite is executed
  - `ViewMatchers.withContentDescription()``resId`overload
- *rules*
  - `ActivityTestRule`: This rule provides functional testing of a single activity
  - `UiThreadRule`and`UiThreadTest`annotations: This rule allows the test method annotated with`UiThreadTest`to execute on the application's main thread (or UI thread)
  - `ServiceTestRule`: This rule provides functional testing of a service
- *runner*
  - `ApplicationLifecycleCallback`: Callback for monitoring application lifecycle events
  - All runner arguments can now be also specified in the Android manifest file using a`<meta-data>`tag
- *UIAutomator*
  - `UiDevice.dumpWindowHierarchy()`can now accept a`File`or an`OutputStream`

### Bug fixes

- *espresso*
  - Cursor matcher now returns`false`if the column wasn't found so Hamcrest can proceed to the next cursor
  - `NullPointerException`with`PreferenceMatchers``withTitle`no longer occurs
  - Unregistering idling resource no longer causes Espresso to think we have busy idling resources
  - Updated Support Annotations version used by Espresso Contrib
- *runner*
  - `AndroidJUnit4`now skips tests with failing assumptions
- *UIAutomator*
  - Run watchers to prevent`StaleObjectException`

### Other notable changes

- Add better error message when we can't typeText with a non-Latin string

## UIAutomator 2.0 (2015-03-12)

UI Automator is now based on Android Instrumentation, and you can build and run tests using the`./gradlew connectedCheck`command.

## Espresso Version 2.0, Test Runner 0.1 (Released on: 2014-12-19)

### Breaking changes

- Espresso has moved to a new namespace, from`android.support.test.espresso`to`android.support.test.espresso`
- Espresso artifacts have been renamed
  - `espresso-1.1.jar`is now`espresso-core-release-2.0.jar`
  - `IdlingResource`interface has been moved into a separate library:`espresso-idling-resource-release-2.0.jar`
  - `CountingIdlingResource`now resides in`espresso-contrib-release-2.0.jar`(as it always should have)
- Optional (a guava dependency) has been removed from the public API in order to support repackaging the guava dependency and avoid DEX collision (a major source of development pain). Affected methods include the following:
  - `ViewAssertion.check()`
  - `HumanReadables.getViewHierarchyErrorMessage()`

### New features

- Actions
  - `ViewActions`
    - `replaceText()`
    - `openLink()`
    - Swipe up and down
  - *espresso-contrib*
    - `RecyclerViewActions`: Handles interactions with`RecyclerViews`
    - `PickerActions`: Handles interactions with`Date`and`Time`pickers
- Matchers
  - `RootMatchers`
    - `isPlatformPopup()`
  - `ViewMatchers`
    - `isJavascriptEnabled()`
    - `withSpinnerText()`
    - `withHint()`
    - `isSelected()`
    - `hasLinks()`
  - `LayoutMatchers`: Matchers for i18n-related layout testing
  - `CursorMatchers`: A collection of matchers for`Cursor`objects
- Assertions
  - `PositionAssertions`, including`isLeftOf()`and`isAbove()`: Colleciton of`ViewAssertions`for checking relative position of elements on the screen
  - `LayoutAssertions`: Assertions for i18n-related layout testing
- Test app: Many new sample activities/tests
- Other
  - `Espresso.unregisterIdlingResources()`and`Espresso.getIdlingResources()`: Provides additional flexibility for working with`IdlingResources`
  - `ViewInteraction.withFailureHandler()`: Allows overriding the failure handler from`onView()`
  - `onData()`support for`AdapterViews`backed by`CursorAdapters`

### Bug fixes

- `ViewMatchers.isDisplayed()`matches views that take up the entire screen, but are no longer less than 90% displayed
- Performing swipe action call to`DrawerActions.openDrawer()`no longer results in`IdlingResourceTimeoutException`

### Other notable changes

- Switched from building with Maven to Gradle
- Moved Espresso dependencies (Guava, Dagger, Hamcrest) out of the way to avoid DEX collisions
- Changed to return success or failure when registering and unregistering idling resources
- Lollipop support: Place`message.recycle()`behind an interface to account for version-related changes
- Switched target SDK level to 21 -- mostly affects the test app

## Version 1.1 (Released on: 2014-01-08)

### Espresso

- New`swipeLeft`and`swipeRight``ViewActions`
- Multi-window support: An advanced feature that enables picking the target window on which Espresso should run the operation
- Improvements to`TypeTextAction`: Allows typing text into a pre-focused view, which makes it easier to append text
- Numerous bug fixes

### Espresso Contrib Library

- This new library contains features that supplement Espresso, but aren't part of the core library
- New`DrawerActions`for operating on`DrawerLayout`: Has a dependency on Android Support Library, hence we are keeping it outside of the core Espresso library

### Sample Tests

- These tests have been relocated to live in the same package as the test app
- Maven POMs have been fixed to remove duplicate guava deps, so`mvn install`should work now