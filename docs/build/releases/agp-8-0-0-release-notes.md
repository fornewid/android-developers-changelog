---
title: https://developer.android.com/build/releases/agp-8-0-0-release-notes
url: https://developer.android.com/build/releases/agp-8-0-0-release-notes
source: md.txt
---

Android Gradle plugin 8.0.0 is a major release that includes a variety of new
features and improvements.

## Compatibility


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.0 | 8.0 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.3 | 30.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 25.1.8937393 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Patch releases

<br />

The following is a list of the patch releases for Android Gradle Plugin
8.0.

<br />

<br />

### Android Gradle Plugin 8.0.2 (May 2023)

<br />

For a list of bugs fixed in AGP 8.0.2, see the
[Android Studio 2022.2.1 closed issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2022.2.1#android-studio-flamingo-patch-2-2022.2.1.20).

<br />

### Android Gradle Plugin 8.0.1 (May 2023)

<br />

<br />

This minor update includes the following bug fixes:

<br />

<br />

| Fixed issues ||
|---|---|
| [Issue #267334465](https://issuetracker.google.com/issues/267334465) Error: "No VersionRequirement with the given id in the table" after upgrading AGP 7.2.2 -\> 7.4.0 |
| [Issue #274337639](https://issuetracker.google.com/issues/274337639) R8 NullPointerException at markTypeAsLive AGP 7.4.1 |
| [Issue #272725341](https://issuetracker.google.com/issues/272725341) \[R8 4.0.53\] Hard class verification failure on Android 11 |

<br />

## Breaking change: namespace required in module-level build script

You must set the namespace in the module-level `build.gradle.kts` file, rather
than the manifest file. You can start using the `namespace` DSL property
starting with AGP 7.3. To learn more, see
[Set a namespace](https://developer.android.com/studio/build/configure-app-module#set-namespace).

When migrating to the namespace DSL, be aware of the following issues:

- Previous versions of AGP infer the test namespace from the main namespace, or application ID, incorrectly in some cases. The AGP Upgrade Assistant blocks the upgrade if it finds that your project's main namespace and test namespace are the same. If the upgrade is blocked, you need to manually change `testNamespace` and modify your source code accordingly.
- After you change the test namespace, it's possible that your code compiles but your instrumented tests fail at runtime. This can happen if your instrumented test source code references a resource defined in both your `androidTest` and app sources.

For more information, see
[issue #191813691 comment #19](https://issuetracker.google.com/issues/191813691#comment19).

## Breaking changes: build option default values

Starting with AGP 8.0, the default values for these flags have changed to
improve build performance. To get help adjusting your code to support some of
these changes, use the AGP Upgrade Assistant
(**Tools \> AGP Upgrade Assistant**). The Upgrade Assistant guides you through
updating your code to accommodate the new behavior or setting flags to preserve
the previous behavior.

| Flag | New default value | Previous default value | Notes |
|---|---|---|---|
| `android.defaults.buildfeatures.buildconfig` | `false` | `true` | AGP 8.0 doesn't generate `BuildConfig` by default. You need to specify this option using the DSL in the projects where you need it. |
| `android.defaults.buildfeatures.aidl` | `false` | `true` | AGP 8.0 doesn't enable AIDL support by default. You need to specify this option using the DSL in the projects where you need it. This flag is planned to be removed in AGP 9.0. |
| `android.defaults.buildfeatures.renderscript` | `false` | `true` | AGP 8.0 doesn't enable RenderScript support by default. You need to specify this option using the DSL in the projects where you need it. This flag is planned to be removed in AGP 9.0. |
| `android.nonFinalResIds` | `true` | `false` | AGP 8.0 generates `R` classes with non-final fields by default. |
| `android.nonTransitiveRClass` | `true` | `false` | AGP 8.0 generates `R` classes for resources defined in the current module only. |
| `android.enableR8.fullMode` | `true` | `false` | AGP 8.0 enables R8 full mode by default. For more details, see [R8 full mode](https://r8.googlesource.com/r8/+/refs/heads/master/compatibility-faq.md#r8-full-mode). |

## Breaking changes: enforced build option values

Starting with AGP 8.0, you can no longer change the values for these flags. If
you specify them in the `gradle.properties` file, the value is ignored and AGP
prints warnings.

| Flag | Enforced value | Notes |
|---|---|---|
| `android.dependencyResolutionAtConfigurationTime.warn` | `true` | AGP 8.0 emits a warning if it detects configuration resolution during the configuration phase because it negatively impacts Gradle configuration times. |
| `android.r8.failOnMissingClasses` | `true` | AGP 8.0 fails builds that use R8 if there are missing classes to ensure better DEX optimization. To address this, you need to add the missing libraries or `-dontwarn` keep rules. For more details, see [Missing class warnings in R8 shrinker](https://developer.android.com/build/releases/past-releases/agp-7-0-0-release-notes#r8-missing-class-warning). |
| `android.testConfig.useRelativePath` | `true` | When support for using Android resources, assets, and manifests in unit tests is enabled, AGP 8.0 generates a `test_config.properties` file that contains only relative paths. This ensures that Android unit tests can always use the Gradle build cache. |
| `android.useNewJarCreator` | `true` | AGP uses the Zipflinger library when creating JAR files to improve build performance. |
| `android.bundletool.includeRepositoriesInDependencyReport` | `true` | When adding SDK dependency information in AABs and APKs is enabled, AGP 8.0 also adds a list of project repositories to this information. To learn more, see [Dependency information for Play Console](https://developer.android.com/build/dependencies#dependency-info-play). |
| `android.enableArtProfiles` | `true` | Baseline profiles are now always generated. See [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview) for details. |
| `android.enableNewResourceShrinker` | `true` | Use the new resource shinker implementation by default. The new resource shrinker includes support for dynamic features. |
| `android.enableSourceSetPathsMap` | `true` | Used for computing relative resource path mappings, so Gradle builds are up-to-date more often. |
| `android.cacheCompileLibResources` | `true` | Compiled library resources can now be cached by default because Gradle tracks resources files relative to the project location. Requires `android.enableSourceSetPathsMap` to be enabled. |
| `android.disableAutomaticComponentCreation` | `true` | AGP 8.0 creates no SoftwareComponent by default. Instead AGP creates SoftwareComponents only for variants that are configured to be published using the publishing DSL. |

## New stable flag for execution profile

AGP includes the new flag `android.settings.executionProfile`. Use this flag to
override the default execution profile from the
[`SettingsExtension`](https://developer.android.com/reference/tools/gradle-api/8.0/com/android/build/api/dsl/SettingsExtension).
To learn more, see the [settings plugin documentation](https://developer.android.com/build/releases/agp-8-0-0-release-notes#settings-plugin).

To preview experimental flags, see the
[preview release notes](https://developer.android.com/studio/preview/features#experimental-build-flags).

## Kotlin lazy property assignment not supported

If you're using Gradle's Kotlin DSL for your build scripts, note that Android
Studio and AGP 8.0 don't support the experimental property assignment using the
`=` operator. For more information about this feature, see the
[release notes](https://docs.gradle.org/8.1-rc-1/release-notes.html#kotlin-dsl-improvements)
and
[documentation](https://docs.gradle.org/8.1-rc-1/userguide/kotlin_dsl.html#kotdsl:assignment).

## Build Analyzer task categories

Starting with Android Studio Flamingo, Build Analyzer has a new default view for
tasks that impact build duration. If your project uses AGP 8.0 or higher,
instead of displaying tasks individually, Build Analyzer groups them by
category. For example, tasks specific to Android Resources, Kotlin, or Dexing
are grouped together and then sorted by build duration. This makes it easy to
know what category has the most impact on build time. Expanding each category
displays a list of the corresponding tasks. To display tasks individually,
without grouping, use the **Group by** drop-down.

![Build Analyzer task categories.](https://developer.android.com/static/studio/images/ba-task-categories.png)

## New settings plugin

AGP 8.0.0-alpha09 introduces the new settings plugin. The settings plugin lets
you centralize global configurations---configurations that apply to all modules---in
one place so you don't need to copy and paste the configurations in multiple
modules. In addition, you can use the settings plugin to create tool
*execution profiles*, or different instructions for how to run a tool, and
switch among them.

> [!NOTE]
> **Note:** To use the settings plugin with Kotlin script, use least AGP 8.7.0

To use the settings plugin, apply the plugin in the `settings.gradle` file:

    apply plugin 'com.android.settings'

### Centralize global configurations

To configure global configurations, use the new `android` block in the
`settings.gradle` file. Here's an example:

    android {
      compileSdk 31
      minSdk 28
      ...
    }

### Tool execution profiles

The settings plugin also lets you create execution profiles for some tools. An
execution profile determines how a tool is run; you can select different
execution profiles depending on the environment. In an execution profile, you
can set JVM arguments for a tool and configure it to run in a separate process.
Currently, only the
[R8 tool](https://developer.android.com/studio/build/shrink-code) is supported.

Create execution profiles and set the default execution profile in the
`settings.gradle` file, as shown in the following example:

    android {
      execution {
        profiles {
          high {
            r8 {
              jvmOptions += ["-Xms2048m", "-Xmx8192m", "-XX:+HeapDumpOnOutOfMemoryError"]
              runInSeparateProcess true
            }
          }
          low {
            r8 {
              jvmOptions += ["-Xms256m", "-Xmx2048m", "-XX:+HeapDumpOnOutOfMemoryError"]
              runInSeparateProcess true
            }
          }
          ci {
            r8.runInSeparateProcess false
          }
        }
        defaultProfile "low"
      }
    }

To override the default profile, select a different profile using the
`android.experimental.settings.executionProfile` property in the
`gradle.properties` file:

    android.experimental.settings.executionProfile=high

You can also set this property using the command line, which lets you set up
different workflows. For example if you have a continuous integration workflow
you can use the command line to change the execution profile without having to
change the `settings.gradle` file:

    ./gradlew assembleRelease \
      -Pandroid.experimental.settings.executionProfile=ci

## JDK 17 required to run AGP 8.0

When using Android Gradle Plugin 8.0 to build your app, JDK 17 is now required
to run Gradle. Android Studio Flamingo bundles JDK 17 and configures Gradle to
use it by default, which means that most Android Studio users don't need to make
any configuration changes to their projects.

If you need to manually [set the JDK version](https://developer.android.com/studio/intro/studio-config#jdk)
used by AGP inside of Android Studio, you need to use JDK 17 or higher.

When using AGP independent of Android Studio, upgrade the JDK version by
setting the `JAVA_HOME`
[environment variable](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_environment_variables)
or the `-Dorg.gradle.java.home`
[command-line option](https://docs.gradle.org/current/userguide/command_line_interface.html#environment_options)
to your installation directory of JDK 17.

## Fixed issues

### Android Gradle plugin 8.0.2

| Fixed Issues ||
|---|---|
| **Shrinker (R8)** | |---| | [Issue #280904554](https://issuetracker.google.com/issues/280904554) R8 fails during Compose build with ArrayIndexOutOfBoundsException | | [Issue #278573402](https://issuetracker.google.com/issues/278573402) VerifyError: Verifier rejected class when using R8 with Kotlin 1.8.20 | | [Issue #280659987](https://issuetracker.google.com/issues/280659987) R8 on AGP 8 breaks Google Fit service | | [Issue #279702361](https://issuetracker.google.com/issues/279702361) Including source file information with residual names that overlap input names is not correctly represented | |

### Android Gradle plugin 8.0.1

| Fixed Issues ||
|---|---|
| **Shrinker (R8)** | |---| | [Issue #267334465](https://issuetracker.google.com/issues/267334465) Error: "No VersionRequirement with the given id in the table" after upgrading AGP 7.2.2 -\> 7.4.0 | | [Issue #274337639](https://issuetracker.google.com/issues/274337639) R8 NullPointerException at markTypeAsLive AGP 7.4.1 | | [Issue #272725341](https://issuetracker.google.com/issues/272725341) \[R8 4.0.53\] Hard class verification failure on Android 11 | |

### Android Gradle plugin 8.0.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #206674992](https://issuetracker.google.com/issues/206674992) Flaky build failure in MergeResources task | | [Issue #241354494](https://issuetracker.google.com/issues/241354494) JavaPluginConvention and HasConvention is deprecated | | [Issue #174678813](https://issuetracker.google.com/issues/174678813) Wrong and inconsistent file location for new transform API | | [Issue #245405989](https://issuetracker.google.com/issues/245405989) Android Gradle Plugin should not use the deprecated GUtil.toWords(string) function | | [Issue #245405994](https://issuetracker.google.com/issues/245405994) Android Gradle Plugin should not use the deprecated ConfigureUtil.configure(closure, target) function | | [Issue #241886012](https://issuetracker.google.com/issues/241886012) Update AGP tests to use KGP 1.7.20-Beta | | [Issue #226095015](https://issuetracker.google.com/issues/226095015) Gradle 7.4 fails (could not create instance of AnalyticsService) | | [Issue #241287611](https://issuetracker.google.com/issues/241287611) New "unknown enum constant" from javac on AGP 7.4.0-alpha09 | | [Issue #237813820](https://issuetracker.google.com/issues/237813820) MergeGeneratedProguardFilesCreationAction configuration is slow even with configuration caching on | | [Issue #232805583](https://issuetracker.google.com/issues/232805583) \[AGP\] Add generated source directory to IDE model (Variant API) | | [Issue #241354494](https://issuetracker.google.com/issues/241354494) JavaPluginConvention and HasConvention is deprecated | | [Issue #243342123](https://issuetracker.google.com/issues/243342123) Don't add ignorewarnings to R8 by default | | [Issue #245716309](https://issuetracker.google.com/issues/245716309) Warn when proguard files do not exist | | [Issue #247066500](https://issuetracker.google.com/issues/247066500) AGP 7.3.0 breaks gradle sync for gradle platform projects | | [Issue #173422058](https://issuetracker.google.com/issues/173422058) apksig library: ApkVerifier$Result.getV4SchemeSigners() is marked private | | [Issue #236896287](https://issuetracker.google.com/issues/236896287) Stop creating androidJacocoAnt configuration if coverage is not enabled | | [Issue #228751486](https://issuetracker.google.com/issues/228751486) Using @IntDef in a library component doesn't generate annotations.zip in the aar | | [Issue #231997058](https://issuetracker.google.com/issues/231997058) Unable to find common super type for and | | [Issue #237820036](https://issuetracker.google.com/issues/237820036) Add a gradle property version of LINT_PRINT_STACKTRACE=true | | [Issue #191068821](https://issuetracker.google.com/issues/191068821) Stale prefab artifacts being packaged into AAR | | [Issue #242831042](https://issuetracker.google.com/issues/242831042) Migrate from destination property to outputLocation property to address deprecation warning and prepare for Gradle 9.0 | | [Issue #188389628](https://issuetracker.google.com/issues/188389628) Take \`--release\` flag into account when setting up JavaCompile task | | [Issue #235863809](https://issuetracker.google.com/issues/235863809) \[AGP-7.3.0-beta03\] ShrinkResourcesNewShrinkerTask is failed when there is an empty line after xml declaration | | [Issue #227811110](https://issuetracker.google.com/issues/227811110) lintVital target run by default in a debug variant | | [Issue #245716309](https://issuetracker.google.com/issues/245716309) Warn when proguard files do not exist | | [Issue #247544167](https://issuetracker.google.com/issues/247544167) AGP tries to add kotlinOptions.freeCompilerArgs on task execution phase | | [Issue #247211509](https://issuetracker.google.com/issues/247211509) Gradle sync failed: Sync failed: reason unknown | | [Issue #235457021](https://issuetracker.google.com/issues/235457021) DependencyReportTask is incompatible with the configuration cache | | [Issue #37005589](https://issuetracker.google.com/issues/37005589) Overriding resources with resValue in build.gradle leads to Error: Duplicate resources | | [Issue #111118208](https://issuetracker.google.com/issues/111118208) 'debug' build type has default signing key, others do not | | [Issue #243399322](https://issuetracker.google.com/issues/243399322) Using dynamic features and resource shrinking cause runtime crash | | [Issue #111118208](https://issuetracker.google.com/issues/111118208) 'debug' build type has default signing key, others do not | | [Issue #252821904](https://issuetracker.google.com/issues/252821904) generated source directory listed as Java directory in lint model's main source provider | | [Issue #252848749](https://issuetracker.google.com/issues/252848749) Gradle 8.0-milestone-2 causes exception in AGP | | [Issue #234170605](https://issuetracker.google.com/issues/234170605) Optimize manifest merging for apps and library | | [Issue #232428943](https://issuetracker.google.com/issues/232428943) Add gradle-settings-api to the javadoc generation | | [Issue #241287611](https://issuetracker.google.com/issues/241287611) New "unknown enum constant" from javac on AGP 7.4.0-alpha09 | | [Issue #241469653](https://issuetracker.google.com/issues/241469653) AGP 7.4.0-alpha09 generates builds that won't upload into Firebase App Distribution | | [Issue #211012777](https://issuetracker.google.com/issues/211012777) lint.xml in modules is not considered for UP-TO-DATE check of lint tasks | | [Issue #197342475](https://issuetracker.google.com/issues/197342475) Android Gradle Plugin 7.0+ and Android Tests issue: Cannot find resource: id | | [Issue #255788407](https://issuetracker.google.com/issues/255788407) configureCMakeDebug flakily crashing with null pointer exception | | [Issue #254292369](https://issuetracker.google.com/issues/254292369) IllegalAccessError upgrading project to AS2022.2.1.5, FireBasePerfPlugin | | [Issue #255584199](https://issuetracker.google.com/issues/255584199) Sync fails with cryptic error "Collection contains no element matching the predicate." | | [Issue #259130486](https://issuetracker.google.com/issues/259130486) Instrumentation API does not transform local file dependencies | | [Issue #247906487](https://issuetracker.google.com/issues/247906487) \`AnnotationProcessorOptions.arguments are queried\` error when updating to 7.4 Beta 1 | | [Issue #227795139](https://issuetracker.google.com/issues/227795139) Move Gradle public plugins to gradle-api and remove BasePlugin.getExtension | | [Issue #258704137](https://issuetracker.google.com/issues/258704137) r8.jvmArgs don't get used | | [Issue #241546506](https://issuetracker.google.com/issues/241546506) JDK17 as min version required for AGP | | [Issue #259556213](https://issuetracker.google.com/issues/259556213) AGP 8.0.0 A8 breaks baseline profiles | | [Issue #199900566](https://issuetracker.google.com/issues/199900566) Change 'compileSdkVersion' to 'compileSdk' in CheckAarMetadataTask message in AGP 8.0 | | [Issue #261329823](https://issuetracker.google.com/issues/261329823) AGP 7.4.0-rc01 breaks Variant API with "Querying the mapped value of map(provider(java.util.Set)) before task '...' has completed is not supported" | | [Issue #263576736](https://issuetracker.google.com/issues/263576736) \`com.android.build.gradle.tasks.ShaderCompile\` issues with configuration cache | | [Issue #263469991](https://issuetracker.google.com/issues/263469991) Adding to Java resources using AGP APIs breaks configuration cache | | [Issue #263881233](https://issuetracker.google.com/issues/263881233) Lint plugin is not part of gradle-api | | [Issue #266780231](https://issuetracker.google.com/issues/266780231) DexingFileDependenciesTask.outputKeepRules is a directory but is marked as an OutputFile | | [Issue #265385297](https://issuetracker.google.com/issues/265385297) Upgrading to AGP 7.4 results in a StackOverflowError | | [Issue #266967487](https://issuetracker.google.com/issues/266967487) processDebugUnitTestManifest is failing with manifest placeholders for test variants | | [Issue #253219347](https://issuetracker.google.com/issues/253219347) Lint accesses source sets information without dependencies | | [Issue #269598545](https://issuetracker.google.com/issues/269598545) Build error refers to API level 34, which does not exist | | [Issue #227796082](https://issuetracker.google.com/issues/227796082) "We recommend using a newer Android Gradle plugin" when there isn't a newer one | | [Issue #271424910](https://issuetracker.google.com/issues/271424910) android.injected.testOnly=false does not work | |
| **Dexer (D8)** | |---| | [Issue #257488927](https://issuetracker.google.com/issues/257488927) Dex merging error related to global synthetics after upgrading AS Canary 6 to 7 | | [Issue #265108171](https://issuetracker.google.com/issues/265108171) Update Kotlin metadata library to version 0.6.0 | | [Issue #271408544](https://issuetracker.google.com/issues/271408544) Workaround for JDK-8272564 seems to be required on API level 28-30 | |
| **Lint** | |---| | [Issue #247025215](https://issuetracker.google.com/issues/247025215) ResourceType lint check is not working for kotlin sources | | [Issue #247146231](https://issuetracker.google.com/issues/247146231) VersionChecks doesn't handle Kotlin range checks | | [Issue #244824912](https://issuetracker.google.com/issues/244824912) False positive for InlinedApi when wrapped | | [Issue #248675800](https://issuetracker.google.com/issues/248675800) Lint false positive Recycle regarding openInputStream | | [Issue #251722662](https://issuetracker.google.com/issues/251722662) \[BuildTool/Lint\] ChecksSdkIntAtLeast constructor property | | [Issue #239337003](https://issuetracker.google.com/issues/239337003) Lint: PartialResults merging works incorrectly | | [Issue #257726238](https://issuetracker.google.com/issues/257726238) Android Studio improperly marks specified version as out-of-date. | | [Issue #256418226](https://issuetracker.google.com/issues/256418226) AndroidDeprecationInspection.DeprecationFilter EP is never registered in android-plugin.xml file | | [Issue #255708236](https://issuetracker.google.com/issues/255708236) AccessibilityDetector lint check explanation is outdated | | [Issue #262376528](https://issuetracker.google.com/issues/262376528) Lint SDK_INT checks should understand temporary local variables | | [Issue #259130471](https://issuetracker.google.com/issues/259130471) Error when TestMode.TYPE_ALIAS replace Function type with typealias | | [Issue #254222461](https://issuetracker.google.com/issues/254222461) Bug: when ObjectAnimator is created outside of current code block, there are false-positive warnings of not starting it #38 | | [Issue #259140252](https://issuetracker.google.com/issues/259140252) Lint: NPE due to querying Application instance in mergeOnly mode | | [Issue #260752253](https://issuetracker.google.com/issues/260752253) NonConstantResourceId lint rule cannot detect to assign constant values from resource id | | [Issue #258954161](https://issuetracker.google.com/issues/258954161) not showing error on view id | | [Issue #259363262](https://issuetracker.google.com/issues/259363262) Failure to deserialize lint resources cache results in a lint error (but should be a warning) | | [Issue #260755411](https://issuetracker.google.com/issues/260755411) AGP Flamingo Alpha 8 Lint NewApi Desugar Regression | | [Issue #262851206](https://issuetracker.google.com/issues/262851206) TypedArray#close (API 31) not desugared but AS does not display warning when used in try-with-resources | | [Issue #263526227](https://issuetracker.google.com/issues/263526227) Lint doesn't check valid casts for call receivers | | [Issue #263526184](https://issuetracker.google.com/issues/263526184) Lint only checks safe casts for directly implemented interfaces, not inherited ones | |
| **Lint Integration** | |---| | [Issue #193244776](https://issuetracker.google.com/issues/193244776) Baseline file is currently an Input and an Output of the Lint tasks | |
| **Shrinker (R8)** | |---| | [Issue #261967650](https://issuetracker.google.com/issues/261967650) NPE / assertion error in CF frame verifier | | [Issue #265148324](https://issuetracker.google.com/issues/265148324) Regression after removal of field lookup cache | | [Issue #250634405](https://issuetracker.google.com/issues/250634405) \`:app:minifyVariantWithR8\` throws a NullPointerException in AGP 7.4.0-beta02 | | [Issue #263934503](https://issuetracker.google.com/issues/263934503) R8: ClassNotFoundException when -allowaccessmodification | | [Issue #266396725](https://issuetracker.google.com/issues/266396725) Add support for context receivers in metadata | | [Issue #267463817](https://issuetracker.google.com/issues/267463817) java.lang.VerifyError: Verifier rejected class androidx.compose.ui.graphics.colorspace.o: void androidx.compose.ui.graphics.colorspace.o.(java.lang.Object) failed to verify: void androidx.compose.ui.graphics.colorspace.o.(java.lang.Object): \[0x0\] cannot access instance field java.lang.Object androidx.compose.ui.graphics.colorspace.n.a from object of type Precise Reference: androidx.compose.ui.graphics.colorspace.o | | [Issue #265905174](https://issuetracker.google.com/issues/265905174) AGP 7.4.0/7.3.1 - Attempt to enqueue an action in a non pushable enqueuer work list | | [Issue #267990059](https://issuetracker.google.com/issues/267990059) Minifying Renderscript code: huge performance drop when upgrading AGP from 7.3.1 to 7.4.0 | |

<br />