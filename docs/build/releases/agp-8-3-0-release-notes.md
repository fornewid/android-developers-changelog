---
title: https://developer.android.com/build/releases/agp-8-3-0-release-notes
url: https://developer.android.com/build/releases/agp-8-3-0-release-notes
source: md.txt
---

Android Gradle plugin 8.3.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.3 supports is API level 34.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.4 | 8.4 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 34.0.0 | 34.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 25.1.8937393 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

The following are new features in Android Gradle plugin 8.3.

## Patch releases

<br />

The following is a list of the patch releases in Android Studio Iguana
and Android Gradle plugin 8.3.

<br />

<br />

### Android Studio Iguana \| 2023.2.1 Patch 2 and AGP 8.3.2 (April 2024)

<br />

<br />

This minor update includes
[these bug fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2023.2.1#android-studio-iguana-|-2023.2.1-patch-2).

<br />

<br />

### Android Studio Iguana \| 2023.2.1 Patch 1 and AGP 8.3.1 (March 2024)

<br />

<br />

This minor update includes
[these bug fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2023.2.1#android-studio-iguana-|-2023.2.1-patch-1).

<br />

## Support for Gradle Version Catalogs

Android Studio supports TOML-based
[Gradle Version Catalogs](https://docs.gradle.org/current/userguide/platforms.html),
a feature that lets you manage dependencies in one central location and share
dependencies across modules or projects. Android Studio now makes it easier to
configure version catalogs through editor suggestions and integration with the
**Project Structure** dialog. Learn how to
[set up and configure Gradle Version Catalogs](https://developer.android.com/build/dependencies)
or how to
[migrate your build to version catalogs](https://developer.android.com/studio/build/migrate-to-catalogs).

> [!NOTE]
> **Note:** Starting with Android Studio Giraffe Canary 10, new projects use Gradle Version Catalogs by default. If an existing project uses a catalog in `gradle/libs.versions.toml`, new modules that are added to that project also use the catalog.

### Code completion and navigation

Android Studio offers code completion when you're editing a version catalog in
the TOML file format or adding a dependency from a version catalog to a build
file. To use code completion, press <kbd>Ctrl+Space</kbd>
(<kbd>Command+Space</kbd> on macOS). In addition, you can quickly navigate from
a dependency reference in your app's `build.gradle` file to where it's declared
in the version catalog by pressing <kbd>Ctrl+b</kbd>
(<kbd>Command+b</kbd> on macOS).

![Code completion when adding a dependency](https://developer.android.com/static/studio/images/gradle-version-catalogs-code-completion.png)

### Integration with the Project Structure dialog

If your project uses a version catalog defined in the TOML file format, you can
edit variables you've defined there through the **Project Structure** dialog
**Variables** view (**File \> Project Structure \> Variables**) in Android Studio.
For each version catalog, there is a drop-down that lists the variables from
that catalog. To edit a variable, click its value and overwrite it. When you
save these changes, the TOML file is updated accordingly.

![Variables from a version catalog in the Project Structure dialog](https://developer.android.com/static/studio/images/gradle-version-catalogs-variables.png)

You can also update dependencies in the **Project Structure** dialog
**Dependencies** view (**File \> Project Structure \> Dependencies** ). To update
versions using the **Project Structure** dialog, navigate to the module and
dependency you want to edit, and then update the **Requested Version** field.
When you save these changes, the TOML file is updated accordingly. Note that if
the dependency version was defined using a variable, updating the version
directly this way replaces the variable with a hardcoded value. Also be aware
that removing a dependency from a build file, whether you use the **Project
Structure** dialog or not, doesn't remove the dependency from the version
catalog.

![Dependencies from a version catalog in the Project Structure dialog](https://developer.android.com/static/studio/images/gradle-version-catalogs-dependencies.png)

### Known issues and limitations

The following are known issues or limitations with Gradle Version Catalogs
support in Android Studio.

- Error highlighting plugin alias declarations in Kotlin script files: when you
  add a plugin declaration of the form `alias(libs.plugins.example)`, the editor
  adds a red underline under the `libs` part. This is a known issue in Gradle
  versions 8.0 and lower and will be resolved in a future release of Gradle.

- Android Studio support only for version catalogs in TOML format: currently the
  Android Studio code completion, navigation, and Project Structure dialog
  support is only available for version catalogs defined in the TOML file
  format. However, you can still add a version catalog directly in the
  `settings.gradle` file and use its dependencies in your project.

- Navigation for KTS build files not supported: navigating to a dependency
  definition in a version catalog by using <kbd>Control</kbd>+click
  (<kbd>Command</kbd>+click on macOS) isn't yet supported for build files
  written using Kotlin script.

- Firebase Assistant adds dependencies directly in build scripts: the
  [Firebase Assistant](https://firebase.google.com/docs/android/learn-more#firebase-assistant)
  adds dependencies directly to your build scripts instead of through version
  catalogs.

- "Find usages" functionality not supported: finding usages of a version catalog
  variable in other build files isn't yet supported, whether the build file is
  in KTS or Groovy. That is, using <kbd>Control</kbd>+click
  (<kbd>Command</kbd>+click on macOS) on a variable definition in a version
  catalog doesn't lead to the build files where the variable is used.

- The Project Structure dialog in Android Studio shows multiple catalog
  files if they're in the root `gradle` folder, but doesn't show catalogs for
  a [composite build](https://docs.gradle.org/current/userguide/composite_builds.html).
  For example, if you have two catalog files---one for your app and one for a
  composite build---the Project Structure dialog only shows the app catalog file.
  You can use a composite build, but you have to edit its TOML file directly.

## Additional SDK insights: policy issues

Android Studio displays lint warnings in `build.gradle.kts` and `build.gradle`
files and in the
**Project Structure Dialog** for public SDKs that have Play policy violations
in the [Google Play SDK Index](https://developer.android.com/distribute/sdk-index). You should update any
dependencies that violate Play policies because these violations could prevent
you from publishing to the Google Play Console in the future. The policy
violation warnings supplement
the [outdated version warnings](https://developer.android.com/build/dependencies#sdk-insights)
displayed by Android Studio.

## Android Studio compileSdk version support

Android Studio displays a warning if your project uses a `compileSdk` that isn't
supported by the current version of Android Studio. If available, it also
suggests moving to a version of Android Studio that supports the `compileSdk`
used by your project. Keep in mind that
[upgrading Android Studio might also require you upgrade AGP](https://developer.android.com/studio/releases#android_gradle_plugin_and_android_studio_compatibility).
AGP also displays a warning in the **Build** tool window if the `compileSdk`
used by your project isn't supported by the current version of AGP.

## Lint behavior changes

Starting with Android Gradle plugin 8.3.0-alpha02, when running lint on a
module, separate lint analysis tasks are run for the main and test
components of the module. The reason for this change is to improve performance.
To revert to the earlier behavior, set
`android.experimental.lint.analysisPerComponent=false` in your
`gradle.properties` file.

## Precise resource shrinking on by default

Precise resource shrinking, which removes unused entries from the
`resources.arsc` file and eliminates unused resource files, is on by default.
When this shrinking is enabled, your resource table is reduced and only
referenced `res` folder entries are included in the APK.

To turn off precise resource shrinking, set
`android.enableNewResourceShrinker.preciseShrinking` to `false` in your
project's `gradle.properties` file.

## Fixed issues

### Android Gradle plugin 8.3.2

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #329346760](https://issuetracker.google.com/issues/329346760) AGP 8.3 with desugaring enabled deadlock can happen | | [Issue #330593433](https://issuetracker.google.com/issues/330593433) AGP 8.3 breaks zipApksFor Task | |
| **Lint Integration** | |---| | [Issue #330911660](https://issuetracker.google.com/issues/330911660) Lint unable to disambiguate a KMP dependency | |

### Android Gradle plugin 8.3.1

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #284003132](https://issuetracker.google.com/issues/284003132) MergeJavaResourcesTask incremental inputs handling issue | |
| **Lint Integration** | |---| | [Issue #325650375](https://issuetracker.google.com/issues/325650375) Lint cannot resolve sibling source sets' types in AGP 8.3.0-rc02 | |

### Android Gradle plugin 8.3.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #292114808](https://issuetracker.google.com/issues/292114808) Build cache is redundant for PackageForUnitTest task | | [Issue #293547829](https://issuetracker.google.com/issues/293547829) \[AGP 8.1.0\] ./gradlew test fails with "Unable to find manifest output" if both splits.abi.isEnable and testOptions.unitTests.isIncludeAndroidResources are true | | [Issue #278096743](https://issuetracker.google.com/issues/278096743) AGP model building fails with nested gradle composite builds | | [Issue #296250243](https://issuetracker.google.com/issues/296250243) Resource shrinker mangles resource IDs, leading to runtime crashes | | [Issue #265296706](https://issuetracker.google.com/issues/265296706) Minimum Gradle version check does not run on the second build and after | | [Issue #295205663](https://issuetracker.google.com/issues/295205663) Execution failed for task ':app:mergeReleaseClasses' after Updating AGP from 8.0.2 to 8.1.0 | | [Issue #298008231](https://issuetracker.google.com/issues/298008231) \[Gradle 8.4\]\[upgrade\] Integration test failure after upgrade due to use of deprecated feature in kotlin gradle plugin | | [Issue #289098893](https://issuetracker.google.com/issues/289098893) Don't check for the existence of manifest overlay files during configuration phase | | [Issue #299314630](https://issuetracker.google.com/issues/299314630) Broken link to Gradle doc on MergeJavaResWorkAction error | | [Issue #278767328](https://issuetracker.google.com/issues/278767328) Gradle 8.1 breaks configuration caching due to .gradle/.android/analytics.settings | | [Issue #196226533](https://issuetracker.google.com/issues/196226533) AGP should not use ProjectComponentIdentifier.projectPath without ProjectComponentIdentifier.build | | [Issue #300502151](https://issuetracker.google.com/issues/300502151) Please reduce/remove info-level logging for AGP "Analytics other plugin to proto: ..." | | [Issue #298011288](https://issuetracker.google.com/issues/298011288) \[Gradle 8.4\]\[upgrade\] File operation during configuration in ProcessJavaResTask breaks config caching | | [Issue #118668005](https://issuetracker.google.com/issues/118668005) Variant API to get symbol table (R.txt) | | [Issue #198453608](https://issuetracker.google.com/issues/198453608) lint standalone plugin doesn't handle gradleApi() dependency properly | | [Issue #197121903](https://issuetracker.google.com/issues/197121903) Poor kDocs on AGP classes/properties. \`VariantOutput.enable\` suggests it should be replaced with \`VariantOutput.enable\` | | [Issue #299506174](https://issuetracker.google.com/issues/299506174) AGP 8.3.0-alpha02 cannot install release profiles on Windows hosts | | [Issue #225900051](https://issuetracker.google.com/issues/225900051) Enforce \`android.enableDexingArtifactTransform=true\` | | [Issue #298011938](https://issuetracker.google.com/issues/298011938) \[Gradle 8.4\]\[upgrade\] Integration test failure after upgrade due to file handling in configuration phase | | [Issue #299602350](https://issuetracker.google.com/issues/299602350) AGP 8.3.0-alpha-02 - \`Error: Failed to deserialize cached resource repository.\` | | [Issue #298012643](https://issuetracker.google.com/issues/298012643) \[Gradle 8.4\]\[upgrade\] Integration test failure after upgrade due file handling in configuration phase of TestLabBuildService | | [Issue #295039976](https://issuetracker.google.com/issues/295039976) AGP 8.1.0 uninstalls app after running instrumented tests - 7.4.2 does not | | [Issue #303641463](https://issuetracker.google.com/issues/303641463) Tranforming an APK leads to a error with ListingFileRedirectTask | | [Issue #303497756](https://issuetracker.google.com/issues/303497756) Transforming the ASSETS artifact give broken input/output locations | | [Issue #303900539](https://issuetracker.google.com/issues/303900539) Promote android.experimental.r8.dex-startup-optimization=true to be default | | [Issue #172671706](https://issuetracker.google.com/issues/172671706) Migrate to new Gradle configuration alignment API | | [Issue #269585156](https://issuetracker.google.com/issues/269585156) Resource compilation fails when Kotlin compiler tries to update to IDEA 21.3 | | [Issue #232323922](https://issuetracker.google.com/issues/232323922) Reactive get() with artifacts API | | [Issue #303926255](https://issuetracker.google.com/issues/303926255) Graduate "android.lint.printStackTrace" AGP property to stable | | [Issue #295666695](https://issuetracker.google.com/issues/295666695) AGP 8.1.0: dynamic feature: Implicit dependency between exportReleaseConsumerProguardFiles and extractProguardFiles cause compilation errors | | [Issue #306420288](https://issuetracker.google.com/issues/306420288) \`variant.unitTest.jniLibs.addGeneratedSourceDirectory\` does not seem to do anything | | [Issue #306301014](https://issuetracker.google.com/issues/306301014) Update XML parser used in AGP for Gradle 8.4 compatibility | | [Issue #283015405](https://issuetracker.google.com/issues/283015405) AGP 8.0.1 release package jacoco instrument does not take effect | | [Issue #303737186](https://issuetracker.google.com/issues/303737186) HEDGEHOG REGRESSION: Run button is delayed by a few seconds (Creating spec) | | [Issue #307987906](https://issuetracker.google.com/issues/307987906) AGP 8.3.0-alpha11 produces release APK that crashes on startup with android.content.res.Resources$NotFoundException | | [Issue #303926255](https://issuetracker.google.com/issues/303926255) Graduate "android.lint.printStackTrace" AGP property to stable | | [Issue #297440098](https://issuetracker.google.com/issues/297440098) Feature Request: Promote com.android.build.api.extension.impl.CURRENT_AGP_VERSION to a public API | | [Issue #227511002](https://issuetracker.google.com/issues/227511002) SDK Manager should stop spamming log info to stdout | | [Issue #308401803](https://issuetracker.google.com/issues/308401803) DexArchiveBuilderTaskDelegate was failed with resource only library module | | [Issue #260925077](https://issuetracker.google.com/issues/260925077) AGP7.4 custom plugin variant toTransform for all throw duplicate entry: META-INF/MANIFEST.MF exception | | [Issue #309685910](https://issuetracker.google.com/issues/309685910) Support new Manifest tags, | | [Issue #310112606](https://issuetracker.google.com/issues/310112606) The link for "decoupled Projects" in studio settings goes to the wrong place. | | [Issue #214428179](https://issuetracker.google.com/issues/214428179) Please provide options to include generated sources on Javadoc and SourceJar | | [Issue #308175247](https://issuetracker.google.com/issues/308175247) Need quick fix for discrepancy between compileSdk and dependency with minCompileSdkVersion | | [Issue #37045148](https://issuetracker.google.com/issues/37045148) \[Gradle\] tools:overrideLibrary should support asterisk (\*) | | [Issue #309843401](https://issuetracker.google.com/issues/309843401) UI Freeze when editing manifest | | [Issue #298703884](https://issuetracker.google.com/issues/298703884) Unable to set JaCoCo version in AGP 8.2.0 | | [Issue #314731501](https://issuetracker.google.com/issues/314731501) Android Gradle Plugin 8.2.0 install task fails in project that uses dynamic features | | [Issue #314731501](https://issuetracker.google.com/issues/314731501) Android Gradle Plugin 8.2.0 install task fails in project that uses dynamic features | |
| **Dexer (D8)** | |---| | [Issue #319604744](https://issuetracker.google.com/issues/319604744) \[desugared library\] Desugared library version 2.1 is not compatible with previous versions of R8 | | [Issue #316744331](https://issuetracker.google.com/issues/316744331) Optimizations running even just with D8? | |
| **Lint** | |---| | [Issue #291319992](https://issuetracker.google.com/issues/291319992) \[Lint\] TranslucentViewDetector crashes in filterIncident function and causes lint to produce wrong result | | [Issue #292114818](https://issuetracker.google.com/issues/292114818) TranslucentViewDetector should accept "behind" value | | [Issue #293900782](https://issuetracker.google.com/issues/293900782) Android Lint fails on a KMP library with \`property 'variantInputs.name' doesn't have a configured value.\` | | [Issue #292069881](https://issuetracker.google.com/issues/292069881) TranslucentViewDetector report wrong line in manifest | | [Issue #290794202](https://issuetracker.google.com/issues/290794202) lintDebug falsely reports UseTomlInstead warnings when using project dependencies | | [Issue #294279964](https://issuetracker.google.com/issues/294279964) Unexpected issues from another project flagged by Android Lint | | [Issue #284997735](https://issuetracker.google.com/issues/284997735) LINT check Unused Resource false positive detection inside of binding and click listener | | [Issue #300090636](https://issuetracker.google.com/issues/300090636) Could not load custom lint check jar file: Node cannot be cast to TreeNode | | [Issue #228961124](https://issuetracker.google.com/issues/228961124) Lint visitAnnotationUsage not called for usages of annotated classes in variable declarations | | [Issue #289695599](https://issuetracker.google.com/issues/289695599) Lint 31.0.2 fails with java.util.NoSuchElementException: Array is empty. | | [Issue #266116266](https://issuetracker.google.com/issues/266116266) No Lint warning about kotlin.text.MatchNamedGroupCollection#get(String) requiring API 26 | | [Issue #293397291](https://issuetracker.google.com/issues/293397291) lint:TypographyQuotes false negatives: more than one escaped apostrophe are ignored | | [Issue #291130217](https://issuetracker.google.com/issues/291130217) AGP 8.0.2 lint InvalidId detector false positive | | [Issue #297095583](https://issuetracker.google.com/issues/297095583) LintError issues added to lint baselines | | [Issue #300392968](https://issuetracker.google.com/issues/300392968) Quickfix Lint doesn't work and results in an IDE error | | [Issue #188814760](https://issuetracker.google.com/issues/188814760) Inconsistent test failure due to partial analysis | | [Issue #301833844](https://issuetracker.google.com/issues/301833844) Invalid highlight of an warning which is false positive | | [Issue #228961124](https://issuetracker.google.com/issues/228961124) Lint visitAnnotationUsage not called for usages of annotated classes in variable declarations | | [Issue #308400860](https://issuetracker.google.com/issues/308400860) Unused Resources Processor might delete Gradle build file | | [Issue #303549797](https://issuetracker.google.com/issues/303549797) NewApi lint check does not undertand "isAtleastU() \&\& otherCondition()" final field | | [Issue #299673844](https://issuetracker.google.com/issues/299673844) StackOverflow from \`LintClient.getSdkHome\` | | [Issue #313937481](https://issuetracker.google.com/issues/313937481) Android Studio / Lint doesn't tell you when "platform" dependencies are out of date | | [Issue #190076622](https://issuetracker.google.com/issues/190076622) Bug: no suggestion to update Firebase-bom dependency | | [Issue #192383335](https://issuetracker.google.com/issues/192383335) Project Structure (and Gradle (?)) does not discover Firebase BOM dependencies to be upgraded to a newer version. | |
| **Lint Integration** | |---| | [Issue #294385251](https://issuetracker.google.com/issues/294385251) DuplicatePlatformClasses lint error from testImplementation dependency | |
| **Shrinker (R8)** | |---| | [Issue #293820078](https://issuetracker.google.com/issues/293820078) R8 doesn't work after upgrade from AGP 8.0.2 to 8.1.0 | | [Issue #311837855](https://issuetracker.google.com/issues/311837855) isShrinkResources overoptimizes in 8.3.0-alpha11 to alpha14 | | [Issue #315877832](https://issuetracker.google.com/issues/315877832) R8 Flurry SDK crash with AGP 8.2.0 | | [Issue #314984596](https://issuetracker.google.com/issues/314984596) Android - R8 causes subclass of LinearLayoutManager to crash | | [Issue #315186101](https://issuetracker.google.com/issues/315186101) R8 v8.2.33, "java.lang.VerifyError: Bad type on operand stack" runtime crash after upgrade | | [Issue #316100042](https://issuetracker.google.com/issues/316100042) \[R8 8.3.21\] R8 8.3.21 is 1.57MB larger than R8 8.1.56 | | [Issue #316100042](https://issuetracker.google.com/issues/316100042) \[R8 8.3.21\] R8 8.3.21 is 1.57MB larger than R8 8.1.56 | | [Issue #318787479](https://issuetracker.google.com/issues/318787479) class.getInterfaces() return empty | | [Issue #323512667](https://issuetracker.google.com/issues/323512667) Test SimpleKotlinEnumUnboxingTest fails on kotlin_dev bot | |

<br />