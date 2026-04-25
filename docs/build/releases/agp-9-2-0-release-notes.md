---
title: https://developer.android.com/build/releases/agp-9-2-0-release-notes
url: https://developer.android.com/build/releases/agp-9-2-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.2 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.2 supports is API level 36.1.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.4.1 | 9.4.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Unified coverage and test reports

> [!WARNING]
> **Experimental:** This is an experimental feature. To enable this feature, set `android.experimental.reportAggregationSupport=true` in your `gradle.properties` file.

AGP 9.2.0-alpha07 introduces tasks to generate HTML dashboards that consolidate
test results and coverage from various test types (unit and instrumentation),
modules, and build variants, providing a comprehensive overview in a single
dashboard. For more information, see [Generate unified code coverage reports](https://developer.android.com/studio/test/coverage-report#unified)
and [View unified test reports](https://developer.android.com/studio/test/command-line#view-test-reports).

## R8 changes

The following R8 changes are included in AGP 9.2.0.

### Stricter `-keepattributes` semantics for keeping runtime invisible annotations

Runtime invisible annotations cannot be read at runtime. D8 therefore
unconditionally removes runtime invisible annotations, with no option to change
this.

For compatibility with ProGuard, R8 supports outputting runtime invisible
annotations. But when compiling to DEX, runtime invisible annotations should
generally never be retained. However, it's common practice to include the
convenient rule `-keepattributes *Annotation*` (either directly or indirectly
from consumer keep rules) for R8 to keep runtime visible annotations.
Unfortunately this also ends up keeping runtime invisible annotations.

To mitigate this problem and better match D8 behavior, `-keepattributes`
patterns with wildcards no longer match `RuntimeInvisibleAnnotations`,
`RuntimeInvisibleParameterAnnotations`, and `RuntimeInvisibleTypeAnnotations`.
As a result, runtime invisible annotations will only be kept if the attribute
name is mentioned explicitly without wildcards.

None of the following rules will now keep runtime invisible annotations:

    -keepattributes *
    -keepattributes *Annotation*
    -keepattributes *Invisible*

To keep runtime invisible annotations, use the following rule:

    -keepattributes RuntimeInvisibleAnnotations,
                    RuntimeInvisibleParameterAnnotations,
                    RuntimeInvisibleTypeAnnotations

### Support for negated names in member rules

The configuration language has been extended so that you can now match on
negated member name patterns.

For example, to match all methods that don't end in "ForTesting" use the
following rule:

    -keepclassmembers class com.example.MyClass {
      *** !*ForTesting(...);
    }

Member name patterns can also be negated in the precondition of `-if`
rules. If a negated member name pattern contains wildcards, such
wildcards cannot be back-referenced in the `-if` consequent rule.

## Fixed issues


### Android Gradle plugin 9.2.0-alpha04

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #480062612](https://issuetracker.google.com/issues/480062612) Renaming APK using new AGP DSL | | [Issue #461382865](https://issuetracker.google.com/issues/461382865) Error when accessing (but not evaluating) bootClasspath IllegalStateException: targetCompatibility is not yet finalized | |

### Android Gradle plugin 9.2.0-alpha03

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #486844145](https://issuetracker.google.com/issues/486844145) JdkImageTransform failure with JDK 26 | | [Issue #474084303](https://issuetracker.google.com/issues/474084303) Automatically encode minAgpVersion in the AAR metadata in AGP 10.0 | |
| **Lint** | |---| | [Issue #488736407](https://issuetracker.google.com/issues/488736407) Truncated context window in Lint SARIF reports due to stuck offset pointer in \`SarifReporter.kt\` | | [Issue #484887319](https://issuetracker.google.com/issues/484887319) Lint Gradle client is missing a critical feature making it unreliable at best | |
| **Lint Integration** | |---| | [Issue #468928427](https://issuetracker.google.com/issues/468928427) Lint Gradle tasks ignore --quiet flag | |

### Android Gradle plugin 9.2.0-alpha02

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #477562205](https://issuetracker.google.com/issues/477562205) AGP 9.0 No androidComponents.onVariant equivalent for applicationVariants.all.mergeAssetsProvider | | [Issue #398173037](https://issuetracker.google.com/issues/398173037) \`\*.xml.flat\` files contain absolute file paths | | [Issue #437828055](https://issuetracker.google.com/issues/437828055) R8D8ThreadPoolBuildService not registered | |
| **Lint Integration** | |---| | [Issue #314101896](https://issuetracker.google.com/issues/314101896) Android Lint fails with custom lint checks compiled to Java 21 bytecode | |

### Android Gradle plugin 9.2.0-alpha01

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #459878951](https://issuetracker.google.com/issues/459878951) Warn users if they have commonTest but forget withHostTestBuilder | | [Issue #482839660](https://issuetracker.google.com/issues/482839660) \[fused lib - public\] OkHttp includes sources | | [Issue #482293927](https://issuetracker.google.com/issues/482293927) Cannot run androidDeviceTest with manifest placeholders in library (AGP 9.0.0 with com.android.kotlin.multiplatform.library plugin) | | [Issue #460469730](https://issuetracker.google.com/issues/460469730) AGP should warn if user has src/androidDeviceTest/java with java disabled | |
| **Lint** | |---| | [Issue #483413438](https://issuetracker.google.com/issues/483413438) Lint typo in message | |

<br />