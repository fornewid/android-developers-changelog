---
title: https://developer.android.com/build/releases/agp-8-9-0-release-notes
url: https://developer.android.com/build/releases/agp-8-9-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.9.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.9 supports is API level 35.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.11.1 | 8.11.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 35.0.0 | 35.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 8.9.2

| Fixed Issues ||
|---|---|
| **Shrinker (R8)** | |---| | [Issue #404745556](https://issuetracker.google.com/issues/404745556) Resource Shrinking Issue in AGP 8.9 Causing Missing Resources in Dynamic Feature Modules | | [Issue #401515589](https://issuetracker.google.com/issues/401515589) ClassCastException from a safe cast in class init | | [Issue #400746842](https://issuetracker.google.com/issues/400746842) Cannot invoke com.android.tools.r8.internal.H5.x() | |

### Android Gradle plugin 8.9.1

| Fixed Issues ||
|---|---|
| **Dexer (D8)** | |---| | [Issue #401489623](https://issuetracker.google.com/issues/401489623) Backporting of android.os.Build.VERSION_CODES_FULL incorrect for Baklava | |
| **Shrinker (R8)** | |---| | [Issue #401546693](https://issuetracker.google.com/issues/401546693) Unable to Generate Signed APK after updating to AGP 8.9.0 | | [Issue #397737234](https://issuetracker.google.com/issues/397737234) Analyze written-before-read property at allocation sites encounters error when generating classfile | | [Issue #389737060](https://issuetracker.google.com/issues/389737060) Problem regarding Java SPI in R8 shrinker of versions 8.6.\*, 8.7.\*, 8.8.0 | |

### Android Gradle plugin 8.9.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #331016661](https://issuetracker.google.com/issues/331016661) Provide an actionable error message when GMD setup task fails with insufficient disk space | | [Issue #317358817](https://issuetracker.google.com/issues/317358817) com.android.settings plugin doesn't recognize targetSdk | | [Issue #373478537](https://issuetracker.google.com/issues/373478537) Unhelpful error ''compileSdkVersion is not specified. Please add it to build.gradle" | | [Issue #378314205](https://issuetracker.google.com/issues/378314205) Missing "Clean build" in Build menu | | [Issue #340315591](https://issuetracker.google.com/issues/340315591) Maybe let AGP's built-in Kotlin support auto-add kotlin stdlib dependency | | [Issue #338596003](https://issuetracker.google.com/issues/338596003) Update shouldConfigureKotlinPlatformAttribute to handle built-in kotlin support | | [Issue #378724144](https://issuetracker.google.com/issues/378724144) Give kotlin gradle syntax in error message for \`checkTestedAppObfuscationRelease\` | | [Issue #383184394](https://issuetracker.google.com/issues/383184394) Fused Library error when unresolved dependency could be improved | | [Issue #380110863](https://issuetracker.google.com/issues/380110863) System Properties from gradle.properties are not passed to R8 Gradle Workers in separate processes | | [Issue #241582907](https://issuetracker.google.com/issues/241582907) Make BuiltArtifact.outputFile as File type | | [Issue #383182777](https://issuetracker.google.com/issues/383182777) Not providing namespace on fused library does not give a good error message | | [Issue #196209595](https://issuetracker.google.com/issues/196209595) lint options in AGP 7.1.0-alpha08 doesn't allow for stdout | | [Issue #317215060](https://issuetracker.google.com/issues/317215060) Android Gradle Plugin: Variants should expose source set names | | [Issue #379657438](https://issuetracker.google.com/issues/379657438) Configuration cache is brittle to the setting of the TERM environment variable | | [Issue #393189008](https://issuetracker.google.com/issues/393189008) AndroidComponentsExtension.addSourceSetConfigurations broken when stats are enabled | | [Issue #394384907](https://issuetracker.google.com/issues/394384907) Initialization script 'C:\\Users\\mypc\\AppData\\Local\\Temp\\ijresolvers2.gradle' line: 162 | | [Issue #393189008](https://issuetracker.google.com/issues/393189008) AndroidComponentsExtension.addSourceSetConfigurations broken when stats are enabled | |
| **Dexer (D8)** | |---| | [Issue #395140848](https://issuetracker.google.com/issues/395140848) java.lang.VerifyError: Verifier rejected class: \[0x430\] copy1 v2\<-v264 type=Undefined cat=3 | |
| **Lint** | |---| | [Issue #377475534](https://issuetracker.google.com/issues/377475534) Lint crashes with Lint gradle checks | | [Issue #377642757](https://issuetracker.google.com/issues/377642757) Lint fails with InstantiationException without exception message in lint stacktrace | | [Issue #375352607](https://issuetracker.google.com/issues/375352607) False positive lint check android.permission.SCHEDULE_EXACT_ALARM is only granted to system apps | | [Issue #370343337](https://issuetracker.google.com/issues/370343337) StringFormatInvalid check should be applied to Compose stringResource method | | [Issue #374896332](https://issuetracker.google.com/issues/374896332) RequiresFeature annotation does not work for Kotlin files | | [Issue #376498180](https://issuetracker.google.com/issues/376498180) kotlin android.os.Handler removeCallbacks Runnable | | [Issue #378128668](https://issuetracker.google.com/issues/378128668) WrongConstant lint on definition instead of usage of constant using shift | | [Issue #370778975](https://issuetracker.google.com/issues/370778975) WrongConstant lint appearing twice | | [Issue #381126163](https://issuetracker.google.com/issues/381126163) Runtime exception below API 26 with unsupported Java nio API (with no lint error) | | [Issue #382253664](https://issuetracker.google.com/issues/382253664) Lint prevents usage of RequiresApi even on private helper method in test | | [Issue #360354551](https://issuetracker.google.com/issues/360354551) K2 Mode throws RestrictedApi warning when using .hasRoute(Route::class) in Android Studio | | [Issue #382043552](https://issuetracker.google.com/issues/382043552) Lint suggests replacing @RequiresExtension on test with @SdkSuppress, which doesn't support SDK extensions | | [Issue #383595384](https://issuetracker.google.com/issues/383595384) Lint incorrectly reports an uncessary nested layout when a FrameLayout used with fitSystemWindows to wrap a child RelativeLayout that that requires custom padding. | | [Issue #383595395](https://issuetracker.google.com/issues/383595395) CoarseFineLocation lint rule doesn't account for a maxSdkVersion attribute | | [Issue #385875832](https://issuetracker.google.com/issues/385875832) AppLinkSplitToWebAndCustom is UnknownIssue in lint 8.7.3 | | [Issue #387281249](https://issuetracker.google.com/issues/387281249) Lint check StringEscapeDetector crash on "\\\\ " | | [Issue #389023409](https://issuetracker.google.com/issues/389023409) Wrong lint warning for \`@Parcelize\` annotation on sealed interfaces | | [Issue #382396705](https://issuetracker.google.com/issues/382396705) AS 2024.3.1.4 hang intermittently when editing kotlin texts. | |
| **Lint Integration** | |---| | [Issue #383661626](https://issuetracker.google.com/issues/383661626) lintVitalRelease doesn't run automatically when building app bundle | |
| **Shrinker (R8)** | |---| | [Issue #394185143](https://issuetracker.google.com/issues/394185143) Gson proguard is not working properly after upgrading to AGP 8.8 | | [Issue #391417819](https://issuetracker.google.com/issues/391417819) java.lang.VerifyError: Verifier rejected class | | [Issue #395489597](https://issuetracker.google.com/issues/395489597) Leanback crashes when minified with R8 included in AGP 8.10.0-alpha04 | |

<br />