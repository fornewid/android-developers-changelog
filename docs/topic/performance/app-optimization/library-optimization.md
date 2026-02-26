---
title: https://developer.android.com/topic/performance/app-optimization/library-optimization
url: https://developer.android.com/topic/performance/app-optimization/library-optimization
source: md.txt
---

As a library author, you must ensure that app developers can easily incorporate
your library into their app while maintaining a high-quality end-user
experience. This means your library must be compatible with Android optimization
(R8) without requiring additional setup from the developer---or document that the
library might be inappropriate for usage on Android. It is crucial that
libraries intended for use on Android must not prevent important app
optimizations and [adhere to additional optimization requirements](https://developer.android.com/topic/performance/app-optimization/library-optimization#requirements).

This documentation is targeted at developers of published libraries, but might
also be useful for developers of internal library modules in a large,
modularized app.

If you're an app developer and want to learn about optimizing your Android app,
see [Enable app optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization). To learn about which libraries are appropriate
to use, see [Choose libraries wisely](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely).

## Understand keep rule types

There are two distinct types of keep rules that you can have in libraries:

- **Consumer keep rules** must specify rules that keep whatever the library reflects on. If a library uses reflection or JNI to call into its code, or code defined by a client app, these rules need to describe what code needs to be kept. Libraries should package consumer keep rules, which use the same format as app keep rules. These rules are bundled into library artifacts (AARs or JARs) and get consumed automatically during Android app optimization when the library is used. These rules are maintained in the file specified with the `consumerProguardFiles` property in your `build.gradle.kts` (or `build.gradle`) file. To learn more, see [Write
  consumer keep rules](https://developer.android.com/topic/performance/app-optimization/library-optimization#write-consumer-rules).
- **Library build keep rules** are applied when your library is built. They are only needed if you decide to partially optimize your library at build time. They must keep the library's public API from being removed, otherwise the public API won't be present in the library distribution, meaning app developers can't use the library. These rules are maintained in the file specified with the `proguardFiles` property in your `build.gradle.kts` (or `build.gradle`) file. To learn more, see [Optimize AAR library build](https://developer.android.com/topic/performance/app-optimization/library-optimization#optimize-aar).

## Optimization requirements and guidelines

The R8 configuration in libraries has a global impact on the consuming app's
final binary size and performance. Apart from the general [keep rule best
practices](https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices), library authors must adhere to specific requirements, and
consider additional guidelines.

### Adhere to optimization requirements

Inefficiency in libraries is a major contributor to app bloat, wasted memory,
slow startups, and ANRs (Application Not Responding errors). Libraries must
avoid violating the following requirements to avoid significantly reducing app
quality, and user experience.

- **No broad or package-wide keep rules:** Your library must not include broad
  keep rules that keep most of the code in your library, or in another
  library. Broad keep rules might solve crashes in the short-term, but they
  bloat the app size of all apps that consume your library.

  Don't include package-wide keep rules (such as `-keep class com.mylibrary.**
  {*; }`) for packages in your library or other referenced libraries. Such
  rules limit optimization for these packages across all the apps that consume
  your library.
- **No inappropriate global rules:** Never use [global options](https://developer.android.com/topic/performance/app-optimization/global-options) like
  `-dontobfuscate` or `-allowaccessmodification`.

- **Use of codegen over reflection whenever possible:** When possible, use
  [code generation (*codegen*)](https://en.wikipedia.org/wiki/Code_generation_(compiler)) over reflection. Codegen and
  reflection are both common approaches to avoid boilerplate code when
  programming, but codegen is more compatible with an app optimizer like R8.

  With codegen, code is analyzed and modified during the build process.
  Because there aren't any major modifications after compile time, the
  optimizer knows what code is ultimately needed and what can be safely
  removed.

  With reflection, code is analyzed and manipulated at runtime. Because the
  code isn't really finalized until it executes, the optimizer doesn't know
  what code can be safely removed. It'll likely remove code that is used
  dynamically through reflection during runtime, which causes app crashes for
  users.

  Many modern libraries use codegen instead of reflection. See [KSP](https://github.com/google/ksp)
  for a common entrypoint, used by [Room](https://developer.android.com/topic/performance/app-optimization/library-optimization#write-consumer-rules), [Dagger2](https://dagger.dev/), and
  many others.

  > [!NOTE]
  > **Note:** There are instances when it might be appropriate to use reflection. For more information, see [When reflection is okay](https://developer.android.com/topic/performance/app-optimization/library-optimization#when-reflection).

- **Support R8 full mode:** Your library shouldn't crash when
  [R8 full mode](https://developer.android.com/topic/performance/app-optimization/full-mode) is enabled. R8's full mode is the recommended mode to use
  R8, and is the default since AGP 8.0, which was made stable in 2023. If your
  library crashes under R8, the solution is to identify the specific
  reflection or JNI entry point and add a targeted rule, not to keep the
  entire package.

### Additional recommendations

Apart from the optimization requirements, the following are additional
recommendations.

- Don't use `-repackageclasses` in your library's consumer keep rules file. However, to optimize your library build, you can use `-repackageclasses` with an internal package name, such as `<your.library.package>.internal`, in your library's build keep rules file. This can improve your library's efficiency in unoptimized apps. However, it is generally not necessary, because apps should also be optimized.
- Declare any attributes you need for your library to function in your library's keep rules files, even if there might be an overlap with the attributes defined in `proguard-android-optimize.txt`.
- If you require the following attributes in your library distribution, maintain them in your library's build keep rules file, and *not* in your library's consumer keep rules file:
  - `AnnotationDefault`
  - `EnclosingMethod`
  - `Exceptions`
  - `InnerClasses`
  - `RuntimeInvisibleAnnotations`
  - `RuntimeInvisibleParameterAnnotations`
  - `RuntimeInvisibleTypeAnnotations`
  - `RuntimeVisibleAnnotations`
  - `RuntimeVisibleParameterAnnotations`
  - `RuntimeVisibleTypeAnnotations`
  - `Signature`
- Library authors should keep the `RuntimeVisibleAnnotations` attribute in their consumer keep rules if annotations are used at runtime.
- Library authors shouldn't use the following global options in their consumer keep rules:
  - `-include`
  - `-basedirectory`
  - `-injars`
  - `-outjars`
  - `-libraryjars`
  - `-repackageclasses`
  - `-flattenpackagehierarchy`
  - `-allowaccessmodification`
  - `-renamesourcefileattribute`
  - `-ignorewarnings`
  - `-addconfigurationdebugging`
  - `-printconfiguration`
  - `-printmapping`
  - `-printusage`
  - `-printseeds`
  - `-applymapping`
  - `-obfuscationdictionary`
  - `-classobfuscationdictionary`
  - `-packageobfuscationdictionary`

### When reflection is okay

If you must use reflection, you should only reflect into either of the
following:

- Specific targeted types (specific interface implementers or subclasses)
- Code using a specific runtime annotation

Using reflection in this way limits the runtime cost, and enables writing
[targeted consumer keep rules](https://developer.android.com/topic/performance/app-optimization/library-optimization#write-consumer-rules).

This specific and targeted form of reflection is a pattern you can see across
both the Android framework (for example, when inflating activities, views, and
drawables) and AndroidX libraries (for example when constructing `WorkManager
ListenableWorkers`, or `RoomDatabases`). By contrast, the open ended reflection
of [Gson isn't appropriate for usage in Android apps](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely#gson-issues).

### Common misconceptions

A few common misconceptions might lead you to configure R8 incorrectly. These
include the following:

- **Incorrect understanding of R8's optimizations** : Contrary to popular
  understanding, R8's optimizations are not limited to just obfuscation, but
  also include code shrinking and logical optimizations with method inlining
  and class merging techniques. For more information, see [R8 optimization
  overview](https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices).

- **Bypassing optimization of obfuscated librariess** : A common error is to
  omit a library from optimization, because the library was optimized or
  obfuscated when it was compiled to an AAR (Android Archive) or JAR (Java
  Archive). The optimizations during library build time are limited, and your
  app shouldn't disable the optimization of the library by including it in a
  keep rule. For more information, see [Optimize AAR library build](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#overview).

- **Incorrect understanding of the `-keep` option** The `-keep` rule prevents
  R8 from running any of its [optimization passes](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#overview). For more information,
  see [Choose the right keep option](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#choose-keep).

## Configure rule packaging

To ensure your consumer keep rules are applied correctly, you must package them
appropriately depending on your library format.

### AAR libraries

To add consumer rules for an AAR library, use the `consumerProguardFiles` option
in the Android library module's build script. For more information, see our
[guidance on creating library modules](https://developer.android.com/studio/projects/android-library#Considerations).

### Kotlin

    android {
        defaultConfig {
            consumerProguardFiles("consumer-proguard-rules.pro")
        }
        ...
    }

### Groovy

    android {
        defaultConfig {
            consumerProguardFiles 'consumer-proguard-rules.pro'
        }
        ...
    }

### JAR libraries

To bundle rules with your Kotlin or Java library that ships as a JAR, put your
rules file in the final JAR's `META-INF/proguard/` directory, with any filename.
For example if your code in `<libraryroot>/src/main/kotlin`, put a consumer
rules file at
`<libraryroot>/src/main/resources/META-INF/proguard/consumer-proguard-rules.pro`
and the rules will be bundled in the correct location in your output JAR.

Verify that the final JAR bundles rules correctly by checking that the rules are
in the `META-INF/proguard` directory.

## Optimize AAR library build (advanced)

> [!NOTE]
> **Note:** A common misconception in Android development is that optimizing your AAR (Android Archive) or JAR (Java Archive) makes it acceptable to prevent optimization by keeping your library package during the app-level build. However, whole-program optimization (at the app level) is significantly more effective than optimization done at the library level. It's only during an app build, when a library is included as part of an app, that R8 can know how all the methods of the library are used, and which parameters are passed.

Generally, you shouldn't need to optimize a library build directly because the
possible optimizations at library build time are very limited. As a library
developer, you need to reason about multiple stages of optimization and keep
behavior, both at library and app build time, before you optimize that library.

If you still want to optimize your library at build time this is supported by
the Android Gradle Plugin.

### Kotlin

    android {
        buildTypes {
            release {
                isMinifyEnabled = true
                proguardFiles(
                    getDefaultProguardFile("proguard-android-optimize.txt"),
                    "proguard-rules.pro"
                )
            }
            configureEach {
                consumerProguardFiles("consumer-rules.pro")
            }
        }
    }

### Groovy

    android {
        buildTypes {
            release {
                minifyEnabled true
                proguardFiles
                    getDefaultProguardFile('proguard-android-optimize.txt'),
                    'proguard-rules.pro'
            }
            configureEach {
                consumerProguardFiles "consumer-rules.pro"
            }
        }
    }

Note that the behavior of `proguardFiles` is very different from
`consumerProguardFiles`:

- `proguardFiles` are used at build time, often together with `getDefaultProguardFile("proguard-android-optimize.txt")`, to define which part of your library should be kept during the library build. At a minimum, this is your public API.
- `consumerProguardFiles` by contrast are packaged into the library to affect what optimizations happen later, during the build of an app that consumes your library.

For example, if your library uses reflection to construct internal classes, you
might need to define the keep rules both in `proguardFiles` and
`consumerProguardFiles`.

If you use `-repackageclasses` in your library's build, repackage classes to a
sub-package *inside* your library's package. For example, use `-repackageclasses
'com.example.mylibrary.internal'` instead of `-repackageclasses 'internal'`.

## Support different R8 versions (advanced)

You can tailor rules to target specific versions of R8. This enables your
library to work optimally in projects that use newer R8 versions, while allowing
existing rules to continue to be used in projects with older R8 versions.

To specify targeted R8 rules, you need to include them in the
`META-INF/com.android.tools` directory inside `classes.jar` of an AAR or in the
`META-INF/com.android.tools` directory of a JAR.

    In an AAR library:
        proguard.txt (legacy location, the file name must be "proguard.txt")
        classes.jar
        └── META-INF
            └── com.android.tools (location of targeted R8 rules)
                ├── r8-from-<X>-upto-<Y>/<R8-rule-files>
                └── ... (more directories with the same name format)

    In a JAR library:
        META-INF
        ├── proguard/<ProGuard-rule-files> (legacy location)
        └── com.android.tools (location of targeted R8 rules)
            ├── r8-from-<X>-upto-<Y>/<R8-rule-files>
            └── ... (more directories with the same name format)

In the `META-INF/com.android.tools` directory, there can be multiple
subdirectories with names in the form of `r8-from-<X>-upto-<Y>` to indicate
which R8 versions the rules are written for. Each subdirectory can have one or
more files containing the R8 rules, with any file names and extensions.

Note that the `-from-<X>` and `-upto-<Y>` parts are optional, the `<Y>` version
is *exclusive*, and the version ranges are usually continuous but can also
overlap.

For example, `r8`, `r8-upto-8.0.0`, `r8-from-8.0.0-upto-8.2.0`, and
`r8-from-8.2.0` are directory names representing a set of targeted R8 rules. The
rules under the `r8` directory can be used by any R8 versions. The rules under
the `r8-from-8.0.0-upto-8.2.0` directory can be used by R8 from version
8.0.0 up to but *not including* version 8.2.0.

The Android Gradle plugin uses that information to select all the rules that can
be used by the current R8 version. If a library does not specify targeted R8
rules, the Android Gradle plugin will select the rules from the legacy locations
(`proguard.txt` for an AAR or `META-INF/proguard/<ProGuard-rule-files>` for a
JAR).