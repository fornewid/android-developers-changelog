---
title: https://developer.android.com/build/releases/agp-8-10-0-release-notes
url: https://developer.android.com/build/releases/agp-8-10-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.10.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle Plugin 8.10 supports is API level 36.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.11.1 | 8.11.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 35.0.0 | 35.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## API changes

Android Gradle plugin 8.10.0 contains the following notable API changes:

- [Source level breaking change: `finalizeDsl` now requires use of parameterized types.](https://developer.android.com/build/releases/gradle-plugin-api-updates#api-finalizeDsl)

## Fixed issues


### Android Gradle plugin 8.10.1

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #390602110](https://issuetracker.google.com/issues/390602110) Explicitly enabling device tests in a non-default build type using AGP does not work | |
| **Shrinker (R8)** | |---| | [Issue #406300397](https://issuetracker.google.com/issues/406300397) NullPointerException when compiling instant app after updating Kotlin to 2.1.20 | | [Issue #406525499](https://issuetracker.google.com/issues/406525499) \[AGP\]: ERROR: R8: java.lang.OutOfMemoryError: Required array length 2147483638 + 196 is too large | |

### Android Gradle plugin 8.10.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #344016691](https://issuetracker.google.com/issues/344016691) AGP should claim that it supports API 35 that is about to ship | | [Issue #393189008](https://issuetracker.google.com/issues/393189008) AndroidComponentsExtension.addSourceSetConfigurations broken when stats are enabled | | [Issue #389951197](https://issuetracker.google.com/issues/389951197) Project ':app' cannot access 'Project.group' and 'Project.version' with isolated project setup in AGP 8.8.0 | | [Issue #394384907](https://issuetracker.google.com/issues/394384907) Initialization script 'C:\\Users\\mypc\\AppData\\Local\\Temp\\ijresolvers2.gradle' line: 162 | | [Issue #394384907](https://issuetracker.google.com/issues/394384907) Initialization script 'C:\\Users\\mypc\\AppData\\Local\\Temp\\ijresolvers2.gradle' line: 162 | | [Issue #353554169](https://issuetracker.google.com/issues/353554169) Unable to strip the following libraries, packaging them as they are | | [Issue #319065197](https://issuetracker.google.com/issues/319065197) Add support for passing "isolated splits" info to R8 | | [Issue #390736538](https://issuetracker.google.com/issues/390736538) App crashes with NoClassDefFoundError and ClassNotFoundException when running app from Android Studio | | [Issue #395798193](https://issuetracker.google.com/issues/395798193) Android Gradle Plugin: Avoid overriding Sync.getDestinationDir() in PackageRenderscriptTask and ProcessJavaResTask | | [Issue #118690729](https://issuetracker.google.com/issues/118690729) Use merged java resources for unit tests | | [Issue #400492927](https://issuetracker.google.com/issues/400492927) Isolated project: DeclarativeSchemaModel serialization error | |
| **Dexer (D8)** | |---| | [Issue #401489623](https://issuetracker.google.com/issues/401489623) Backporting of android.os.Build.VERSION_CODES_FULL incorrect for Baklava | | [Issue #401147877](https://issuetracker.google.com/issues/401147877) AutoClosable desugaring no longer reports ExecutorService.close as supported | |
| **Lint** | |---| | [Issue #389023409](https://issuetracker.google.com/issues/389023409) Wrong lint warning for \`@Parcelize\` annotation on sealed interfaces | | [Issue #382396705](https://issuetracker.google.com/issues/382396705) AS 2024.3.1.4 hang intermittently when editing kotlin texts. | | [Issue #385394934](https://issuetracker.google.com/issues/385394934) False positive lint error for CredentialManagerSignInWithGoogle | | [Issue #395836302](https://issuetracker.google.com/issues/395836302) ConcurrentModificationException in Aligned16KB lint check | | [Issue #396584142](https://issuetracker.google.com/issues/396584142) Lint: AGP 8.10.0-alpha05 triggers lots of false positive SyntheticAccessor | | [Issue #398807363](https://issuetracker.google.com/issues/398807363) Make it possible to enable NewApi on test sources | | [Issue #396647876](https://issuetracker.google.com/issues/396647876) What is the effect of pressing button "LintIdeFix" after code inspection in Android Studio | | [Issue #399692455](https://issuetracker.google.com/issues/399692455) Error in the text of the warning message: "Unnecessary; \`Build.VERSION.SDK_INT \>= Build.VERSION_CODES.O\` is \*never\* true here (\`SDK_INT\` ≥ 26 and \< 31)" | |
| **Shrinker (R8)** | |---| | [Issue #401546693](https://issuetracker.google.com/issues/401546693) Unable to Generate Signed APK after updating to AGP 8.9.0 | | [Issue #397737234](https://issuetracker.google.com/issues/397737234) Analyze written-before-read property at allocation sites encounters error when generating classfile | | [Issue #389737060](https://issuetracker.google.com/issues/389737060) Problem regarding Java SPI in R8 shrinker of versions 8.6.\*, 8.7.\*, 8.8.0 | | [Issue #401515589](https://issuetracker.google.com/issues/401515589) ClassCastException from a safe cast in class init | | [Issue #404745556](https://issuetracker.google.com/issues/404745556) Resource Shrinking Issue in AGP 8.9 Causing Missing Resources in Dynamic Feature Modules | | [Issue #400746842](https://issuetracker.google.com/issues/400746842) Cannot invoke com.android.tools.r8.internal.H5.x() | |

<br />