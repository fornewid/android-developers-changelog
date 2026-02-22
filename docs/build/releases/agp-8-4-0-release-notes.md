---
title: https://developer.android.com/build/releases/agp-8-4-0-release-notes
url: https://developer.android.com/build/releases/agp-8-4-0-release-notes
source: md.txt
---

Android Gradle plugin 8.4.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.4 supports is API level 34.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.6 | 8.6 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 34.0.0 | 34.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 26.1.10909125 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

The following are new features in Android Gradle plugin 8.4.

## Patch releases

<br />

The following is a list of the patch releases in Android Studio Jellyfish
and Android Gradle plugin 8.4.

<br />

<br />

### Android Studio Jellyfish \| 2023.3.1 Patch 2 and AGP 8.4.2 (June 2024)

<br />

<br />

> [!IMPORTANT]
> **Important:** This update fixes a critical vulnerability in the GitHub plugin that exists in Android Studio Iguana \| 2023.2.1 and higher.

<br />

<br />

**Important security update:** A
[security vulnerability](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37051)
in the
[GitHub plugin](https://plugins.jetbrains.com/plugin/13115-github)
available in Android Studio Iguana \| 2023.2.1 and higher could expose access
tokens to unauthorized parties.

<br />

<br />

**The fix:** Jetbrains has
[resolved the issue in IntelliJ platform products](https://blog.jetbrains.com/security/2024/06/updates-for-security-issue-affecting-intellij-based-ides-2023-1-and-github-plugin/),
and the fix is now available in
[Android Studio Jellyfish \| 2023.3.1 Patch 2 (2023.3.1.20)](https://developer.android.com/studio).

<br />

<br />

If you already have an Android Studio build on the
[stable channel](https://developer.android.com/studio/intro/update#channels), you can
get the update by clicking **Help \> Check for Updates** (or **Android
Studio \> Check for Updates** on macOS). Otherwise,
[download the latest stable build](https://developer.android.com/studio).

<br />

Furthermore, if you've actively used GitHub pull request functionality in
the IDE, we strongly advise that you revoke any GitHub tokens being used by
the plugin. Given that the plugin can use OAuth integration or personal
access tokens (PATs), please check both and revoke as necessary:

<br />

<br />

- To revoke access for OAuth integration, go to **[Applications](https://github.com/settings/applications)
  \> Authorized OAuth Apps** and revoke access for the **JetBrains IDE Integration** token.
- To revoke access for PATs, go to [Personal access tokens](https://github.com/settings/tokens) and delete the token issued for the GitHub plugin. The default token name is **IntelliJ IDEA GitHub integration plugin**, but you might be using a custom name.

<br />

<br />

After revoking access for the token(s), you need to set up the plugin again
get all the plugin features, including Git operations, to work again.

<br />

<br />

We apologize for any inconvenience and urge all users to update immediately
to safeguard their code and data.

<br />

<br />

This minor update also includes
[these bug fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2023.3.1#android-studio-jellyfish-|-2023.3.1-patch-2).

<br />

<br />

### Android Studio Jellyfish \| 2023.3.1 Patch 1 and AGP 8.4.1 (May 2024)

<br />

<br />

This minor update includes
[these bug fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2023.3.1#android-studio-jellyfish-|-2023.3.1-patch-1).

<br />

## Library classes are shrunk

Starting with Android Gradle Plugin 8.4, if an Android library project is
minified, shrunk program classes will be published for inter-project publishing.
This means that if an app depends on the shrunk version of the Android library
subprojects, the APK will include shrunk Android library classes. You may need
to adjust [library keep rules](https://developer.android.com/build/shrink-code#keep-code) in case there are
missing classes in the APK.

In case you are building and publishing an AAR, local jars that your library
depends on will be included unshrunk in the AAR, which means
[code shrinker](https://developer.android.com/build/shrink-code) won't run on them.

To revert to previous behavior, set
`android.disableMinifyLocalDependenciesForLibraries` in the `gradle.properties`
file and
[file a bug](https://issuetracker.google.com/issues/new?component=192708&template=840533&pli=1).
Future versions of AGP will remove this flag remove this flag.

## Fixed issues

### Android Gradle plugin 8.4.2

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #339670469](https://issuetracker.google.com/issues/339670469) AGP 8.4 seems to break GMD downloads on CI | |

### Android Gradle plugin 8.4.1

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #332788833](https://issuetracker.google.com/issues/332788833) Allow suppressing a warning about JDK 21 deprecating support for targeting java 8 | |
| **Dexer (D8)** | |---| | [Issue #334275655](https://issuetracker.google.com/issues/334275655) java.lang.VerifyError: Verifier rejected class | | [Issue #335663479](https://issuetracker.google.com/issues/335663479) New version R8 format conversion error after obfuscation | | [Issue #335803299](https://issuetracker.google.com/issues/335803299) Intermediate builds may not have complete global synthetic content for stubs | |

### Android Gradle plugin 8.4.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #278800528](https://issuetracker.google.com/issues/278800528) Improve error message for why \`--release\` option can't be used for JavaCompile | | [Issue #194804421](https://issuetracker.google.com/issues/194804421) Disable caching of MergeSourceSetFolders using @DoNotCacheByDefault | | [Issue #298703884](https://issuetracker.google.com/issues/298703884) Unable to set JaCoCo version in AGP 8.2.0 | | [Issue #300096187](https://issuetracker.google.com/issues/300096187) DynamicFeatureBuildType is missing isDebuggable | | [Issue #263197720](https://issuetracker.google.com/issues/263197720) Minified library classes are not published correctly for inter-project consumption | | [Issue #266681484](https://issuetracker.google.com/issues/266681484) Provide Variant#sources API that excludes generated files | | [Issue #248059128](https://issuetracker.google.com/issues/248059128) AGP models do not contain java-platform project dependencies | | [Issue #315336689](https://issuetracker.google.com/issues/315336689) ExtractAarTransform creates non-reproducible classes.jar for aars that have no classes.jar | | [Issue #318384658](https://issuetracker.google.com/issues/318384658) Allow to configure sourceInformation from ComposeOptions | | [Issue #318732733](https://issuetracker.google.com/issues/318732733) Cannot find field: sdk_runtime in message android.bundle.DeviceSpec | | [Issue #168640703](https://issuetracker.google.com/issues/168640703) Support for compileOnlyApi | | [Issue #319132114](https://issuetracker.google.com/issues/319132114) R8 fails on a library module when resource processing is disabled | | [Issue #241581686](https://issuetracker.google.com/issues/241581686) Add ability to change artifact name during transformation | | [Issue #320711864](https://issuetracker.google.com/issues/320711864) Adding task output to as srcDir of sourceSets.androidMain.resources does not create a task dependencies | | [Issue #319053159](https://issuetracker.google.com/issues/319053159) AndroidPluginVersion.toString() is missing leading 0s | | [Issue #302717381](https://issuetracker.google.com/issues/302717381) Artifacts.add(FileSystemLocation) should be more restrictive. | | [Issue #307987906](https://issuetracker.google.com/issues/307987906) AGP 8.3.0-alpha11 produces release APK that crashes on startup with android.content.res.Resources$NotFoundException | | [Issue #314731501](https://issuetracker.google.com/issues/314731501) Android Gradle Plugin 8.2.0 install task fails in project that uses dynamic features | | [Issue #317262738](https://issuetracker.google.com/issues/317262738) AIDL compile fails with IndexOutOfBoundsException: Index 0 out of bounds for length 0 | | [Issue #284003132](https://issuetracker.google.com/issues/284003132) MergeJavaResourcesTask incremental inputs handling issue | | [Issue #299134781](https://issuetracker.google.com/issues/299134781) AGP 8.3.0-alpha02 depends on libraries with known security vunelaribilities | | [Issue #297226571](https://issuetracker.google.com/issues/297226571) Selected activity template requires project with androidx.\* dependencies | | [Issue #281118582](https://issuetracker.google.com/issues/281118582) AGP Upgrade Assistent errouneously removes consumerProguardFiles from module | | [Issue #324445638](https://issuetracker.google.com/issues/324445638) AGP Upgrade Assistant Loads Infinitely | | [Issue #328852035](https://issuetracker.google.com/issues/328852035) SourceDirectories#static shouldn't depend on GenerateBuildConfig task | | [Issue #319822816](https://issuetracker.google.com/issues/319822816) Compose preview unable to resolve classes from transitive dependency | | [Issue #330593433](https://issuetracker.google.com/issues/330593433) AGP 8.3 breaks zipApksFor Task | | [Issue #328687152](https://issuetracker.google.com/issues/328687152) AndroidX Desktop artifacts packaged in Android APK | |
| **Lint** | |---| | [Issue #321771651](https://issuetracker.google.com/issues/321771651) Lint testing framework's GradleModelMocker does not allow setting library version | | [Issue #325107804](https://issuetracker.google.com/issues/325107804) Lint K2 UAST: UCallableReferenceExpression reports wrong qualifierType | | [Issue #324087645](https://issuetracker.google.com/issues/324087645) Lint false positive with useK2Uast=true with overloaded functions | | [Issue #251722662](https://issuetracker.google.com/issues/251722662) \[BuildTool/Lint\] ChecksSdkIntAtLeast constructor property | |
| **Lint Integration** | |---| | [Issue #330911660](https://issuetracker.google.com/issues/330911660) Lint unable to disambiguate a KMP dependency | |

<br />