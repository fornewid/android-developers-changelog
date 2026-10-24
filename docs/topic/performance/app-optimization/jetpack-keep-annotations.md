---
title: https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations
url: https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations
source: md.txt
---

Jetpack Keep lets you declare reflection and Java Native Interface (JNI) usage
with annotations directly in your Kotlin or Java source code, instead of in
separate keep rules files. The Jetpack Keep Gradle plugin reads these
annotations at build time and generates the keep rules that R8 needs.

Jetpack Keep helps R8 optimization stay effective as your codebase changes:

- **Keep rules stay next to the code that needs them.** When you rename or
  delete code that uses reflection, you update the annotation in the same
  place. There's no separate rules file to keep in sync.

- **Generated rules are conditional.** R8 keeps the target of a reflective
  call only if it also keeps the code that makes the call. If the calling
  code is unused and R8 removes it (often the case in optional library
  features), R8 can also remove the target, so rules from unused features
  don't add bloat.

- **Lint finds reflection for you.** The library includes lint checks that
  flag reflective calls that aren't annotated, and that can add many of the
  annotations automatically.

> [!CAUTION]
> **Caution:** Jetpack Keep is in alpha. The API and the generated rules might change before a stable release. If a new version generates rules that keep less code than before, your app can throw exceptions such as `ClassNotFoundException` in release builds, even though the build succeeds. When you upgrade, [compare the generated rules](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#verify) from the old and new versions, and test your release build.

## How Jetpack Keep works

Consider a function that instantiates a class by name. If R8 can't tell that
your code uses the class, it removes the class's constructor, and the app
crashes at runtime. To prevent the crash, you can add a rule like the following
to your keep rules file:

    # Unconditional: R8 keeps this constructor even if it removes the reflection that invokes it.
    -keep class com.example.ResourceLocatorImpl {
        <init>();
    }

With Jetpack Keep, you annotate the function that performs the reflection
instead:

    // ResourceLocatorImpl isn't on this module's compile classpath, so both the
    // annotation and the code refer to it by name.
    @UsesReflectionToConstruct(
        className = "com.example.ResourceLocatorImpl",
        // Omitting parameterTypes keeps every constructor. An empty array keeps
        // only the no-argument constructor, which the code calls.
        parameterTypes = [],
    )
    fun loadResourceLocator(): ResourceLocator {
        val implClass = Class.forName("com.example.ResourceLocatorImpl")
        return implClass.getDeclaredConstructor().newInstance() as ResourceLocator
    }

At build time, the Gradle plugin generates a keep rule for the constructor.
Unlike the preceding manually written rule, the generated rule is conditional:
R8 keeps the constructor only if `loadResourceLocator` remains in the
optimized app.

## Requirements

To use Jetpack Keep, your project needs Android Gradle Plugin (AGP) 8.7 or
higher.

The Gradle plugin supports the following module types:

| Module type | Plugin that the module applies | Additional setup |
|---|---|---|
| Android app | `com.android.application` | None |
| Android library | `com.android.library` | None |
| Kotlin Multiplatform library with an Android target | `com.android.kotlin.multiplatform.library` | None |
| JVM library (Java or Kotlin) | `java-library` or `org.jetbrains.kotlin.jvm` | [Register a JAR transform](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#jvm-libraries) |

## Set up Jetpack Keep

To use Jetpack Keep, add both the library and the Gradle plugin to each
module that uses reflection or JNI. The library provides the annotations and
lint checks, and the plugin turns the annotations into keep rules.

1. In your `libs.versions.toml` file, add the library and the plugin. The
   library and the plugin share the same version:

       [versions]
       # The library and the plugin ship together. Use one version for both so
       # that they stay in sync when you upgrade.
       annotationKeep = "1.0.0-alpha01"

       [libraries]
       androidx-annotation-keep = { group = "androidx.annotation.keep", name = "keep", version.ref = "annotationKeep" }

       [plugins]
       androidx-annotation-keep = { id = "androidx.annotation.keep", version.ref = "annotationKeep" }

   Gradle downloads the plugin from Google's Maven repository, so make sure
   that the `pluginManagement` repositories in your `settings.gradle.kts` file
   include `google()`.
2. In your root `build.gradle.kts` file, declare the plugin alongside AGP
   without applying it:

       plugins {
           alias(libs.plugins.android.application) apply false
           // Other plugins.

           // The plugin relies on AGP classes that it doesn't bundle, so declare
           // it next to AGP. Declaring it here also gives every module the same
           // plugin version.
           alias(libs.plugins.androidx.annotation.keep) apply false
       }

3. In the `build.gradle.kts` file of each module that uses reflection or JNI,
   apply the plugin and add the library dependency:

       plugins {
           alias(libs.plugins.android.application)
           // The plugin reads annotations only from this module's own code, so
           // apply it in every module that uses Jetpack Keep.
           alias(libs.plugins.androidx.annotation.keep)
       }

       dependencies {
           implementation(libs.androidx.annotation.keep)
       }

4. Sync your project with Gradle files.

For each build variant of an Android app module, the plugin registers a
`<variant>ExtractKeepRules` task, such as `releaseExtractKeepRules`, and passes
the generated rules to R8 for that variant. For library modules, the plugin
packages the generated rules as consumer keep rules in the library's output.
JVM library modules need [additional setup](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#jvm-libraries).

## Find reflection with lint

Jetpack Keep includes the following lint checks:

`ReflectionWithoutKeepAnnotations`
:   Flags reflective calls, such as `Class.forName`, `getDeclaredConstructor`,
    `getDeclaredMethod`, and `getDeclaredField`, that don't have a matching keep
    annotation.

`MissingKeepAnnotationPlugin`
:   Flags modules that depend on `androidx.annotation.keep:keep` but don't
    apply the `androidx.annotation.keep` Gradle plugin. Without the plugin, your
    build doesn't generate keep rules from the annotations.

To use lint to annotate an Android module, follow these steps:

1. Run lint on the module to find reflective calls that need annotations:

       ./gradlew :app:lint

2. Apply the fixes that lint can make automatically:

       ./gradlew :app:lintFix

   Lint can add an annotation automatically when it can determine which class
   and members the code reflects on.
3. Review each added annotation to confirm that it matches what your code
   does. For example, check that the parameter types match the constructor or
   method that your code calls.

4. Resolve the remaining findings in Android Studio. When lint can't determine
   the target class, the quick fix inserts the annotation with a `TODO`
   placeholder for you to complete. You can also [add the annotation
   manually](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#annotate).

   For example, the following function receives the class name as a
   parameter, so lint can't determine which class it constructs. The quick fix
   adds an annotation with a placeholder:

       @UsesReflectionToConstruct(
           className = TODO(),
           parameterTypes = []
       )
       fun createInstance(className: String): Any =
           Class.forName(className).getDeclaredConstructor().newInstance()

   Replace the placeholder with the class that your code constructs. If the
   class is available at compile time, use `classConstant` instead of
   `className`. In Kotlin, your code doesn't compile until you replace
   `TODO()`.
5. Check which keep rules the plugin generates from your annotations before
   you remove any existing rules. For an app module, run the extraction task
   for the release variant:

       ./gradlew :app:releaseExtractKeepRules

   The plugin writes the rules to
   `app/build/generated/release/androidx.annotation.keep.rules.pro`. For
   library modules, see [Verify the generated rules](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#verify).
6. Remove the keep rules that the new annotations replace from your keep rules
   files. A rule might also cover reflection that lint didn't flag, such as
   reflection in another module or in a library, so check each rule before you
   remove it:

   - For a package-wide rule, such as `-keep class com.example.** { *; }`, make sure that annotations or other rules cover all reflection on the package's classes.
   - For a rule that keeps specific classes or members, make sure that it closely matches one of the generated rules, or that no other reflection depends on it.
7. Test your release build.

## Annotate your code

Add a Jetpack Keep annotation to the code that performs the reflection: the
function, constructor, field, or class that contains the reflective call. The
annotation describes the target of the reflection, and the generated rule keeps
that target only if R8 keeps the annotated code.

Choose an annotation based on what your code does:

| Annotation | Use when your code |
|---|---|
| `@UsesReflectionToConstruct` | Calls a constructor through reflection, for example with `getDeclaredConstructor().newInstance()`. |
| `@UsesReflectionToAccessMethod` | Calls a method through reflection, for example with `getMethod` or `getDeclaredMethod`. |
| `@UsesReflectionToAccessField` | Reads or writes a field through reflection, for example with `getField` or `getDeclaredField`. |
| `@UnconditionallyKeep` | Is called from outside your app's Kotlin or Java code, for example from native code through JNI. Use this annotation only when you can't use the `@UsesReflection*` annotations, which generate conditional rules. |

All of the `@UsesReflection*` annotations follow these conventions:

- **Identify the target class with `classConstant` or `className`.** If the class is available at compile time, use `classConstant`. The compiler checks the reference, and IDE refactorings such as renaming update it. Use `className` only when the class isn't available at compile time, such as a class in an optional dependency. These two parameters are mutually exclusive.
- **Target the most specific class.** The generated rules keep matching members in the class that you specify and in its subclasses or interface implementations. The more general the class, the more code R8 keeps.
- **Specify parameter types to keep a single overload.** If you don't set `parameterTypes` or `parameterTypeNames`, the rules keep all constructors or all overloads of the method. To keep only the no-argument constructor or method, pass an empty array.
- **Repeat the annotation for multiple targets.** If one function reflects on more than one class or member, add one annotation for each target.

### Construct objects with reflection

Use `@UsesReflectionToConstruct` when your code instantiates a class through
reflection. In the following example, a task runner instantiates
implementations of a `StartupTask` interface by name. Because the annotation
specifies the interface, the generated rules keep the no-argument constructor
of every `StartupTask` implementation, as long as R8 keeps `execute`:

    interface StartupTask {
        fun run()
    }

    object TaskRunner {
        // The task class is known only at runtime, so target the interface that
        // every task implements.
        @UsesReflectionToConstruct(classConstant = StartupTask::class, parameterTypes = [])
        fun execute(className: String) {
            val task = Class.forName(className)
                .getDeclaredConstructor()
                .newInstance() as StartupTask
            task.run()
        }
    }

### Call methods with reflection

Use `@UsesReflectionToAccessMethod` when your code calls a method through
reflection. Set `methodName` to the name of the method. In the following
example, the code calls a static method in an optional dependency. The class
isn't available at compile time, so the annotation uses `className` instead of
`classConstant`:

    object CrashReporting {
        @UsesReflectionToAccessMethod(
            className = "com.example.crashlib.CrashReporter",
            methodName = "log",
            // Omitting parameterTypes keeps every log overload. Keep only the one
            // that the code calls.
            parameterTypes = [String::class],
        )
        fun log(message: String) {
            val reporterClass = try {
                Class.forName("com.example.crashlib.CrashReporter")
            } catch (e: ClassNotFoundException) {
                // Crash reporting is optional, so skip it instead of failing.
                return
            }
            reporterClass.getMethod("log", String::class.java).invoke(null, message)
        }
    }

### Access fields with reflection

Use `@UsesReflectionToAccessField` when your code reads or writes a field
through reflection. Set `fieldName` to the name of the field:

    class UserProfileFetcher {
        // User doesn't expose internalId, so reading it requires reflection.
        @UsesReflectionToAccessField(classConstant = User::class, fieldName = "internalId")
        fun readInternalId(user: User): Any? {
            val field = User::class.java.getDeclaredField("internalId")
            field.isAccessible = true
            return field.get(user)
        }
    }

### Keep code called from outside your app

Use `@UnconditionallyKeep` for code that's called from outside your app's Kotlin
or Java code, such as a method that native code calls through JNI. Annotate the
element that's called, not the code that calls it:

    class NativeBridge {
        // Only native code calls this method, through a JNI lookup by name that
        // R8 can't see. Keep the method and its name unconditionally.
        @UnconditionallyKeep
        fun onNativeEvent(message: String) {
            Log.d("NativeBridge", "Received from native code: $message")
        }

        // The default proguard-android-optimize.txt file already keeps native
        // method names, so this method doesn't need an annotation.
        external fun startNativeProcess()
    }

The generated rule keeps the annotated method and its containing class, with
their original names. It doesn't keep other classes that the method's signature
references. If native code depends on those classes, annotate them too, or add
keep rules for them. For more information about JNI and R8, see [Interaction
with native code through JNI](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples#interaction-with-native-code-through-the-java-native-interface-jni).

By default, `@UnconditionallyKeep` preserves the element's name. If the
external caller doesn't depend on the name, set `shouldPreserveName = false` so
that R8 can rename the element.

> [!WARNING]
> **Warning:** `@UnconditionallyKeep` keeps the annotated code even if your app never uses it, which limits optimization. If your own Kotlin or Java code performs the reflection, use the `@UsesReflection*` annotations instead, because they generate conditional rules.

## Verify the generated rules

This section explains how to check the generated rules for each type of module.
For an app module, the plugin passes the rules directly to R8. For a library
module, the plugin packages the rules as consumer keep rules in the library's
output. Apps that depend on your library apply these rules automatically when
they run R8, even if the apps don't use Jetpack Keep. For more information
about consumer keep rules, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization).

### Android apps

To check which keep rules the plugin generates for an app module, run the
extraction task for a build variant:

    ./gradlew :app:releaseExtractKeepRules

The plugin writes the rules for each variant to
`app/build/generated/<variant>/androidx.annotation.keep.rules.pro`. A
`# context:` comment before each rule identifies the annotated code that
produced it.

To check how the generated rules affect optimization together with your other
keep rules, use the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer).

### Android libraries

Android library modules don't need any additional setup. When you build the
AAR, the plugin adds the generated rules to the AAR's `proguard.txt` file, after
any consumer keep rules that the AAR already contains. The plugin registers a
`<variant>KeepRulesTransformAar` task for each build variant to do this.

To verify the rules, build the AAR, for example with `./gradlew
:mylibrary:assembleRelease`, and open `proguard.txt` in the generated AAR. The
generated rules appear in a section with the following header:

    #################################################################
    #   Rules generated from androidx.annotation.keep annotations   #
    #################################################################

On macOS and Linux, you can also print the rules from the command line:

    unzip -p mylibrary/build/intermediates/aar/release/releaseKeepRulesTransformAar/mylibrary-release.aar proguard.txt

### Kotlin Multiplatform libraries

Kotlin Multiplatform library modules with an Android target don't need any
additional setup either. When you build the AAR for the Android target, the
plugin adds the generated rules to the AAR's `proguard.txt` file in the same
way as for [Android libraries](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#verify-aar). The plugin registers an
`androidMainKeepRulesTransformAar` task to do this.

To verify the rules, run that task and open `proguard.txt` in the AAR that it
creates. On macOS and Linux, you can print the rules from the command line:

    ./gradlew :mylibrary:androidMainKeepRulesTransformAar
    unzip -p mylibrary/build/intermediates/aar/androidMain/androidMainKeepRulesTransformAar/mylibrary.aar proguard.txt

### JVM libraries

Before you can verify the rules for a JVM library module, [configure the
module](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#jvm-libraries) so that the plugin adds the generated rules to a copy
of its JAR. Then run the transform task that you registered and check the rules
files in the JAR that it creates. For example, if you named the task
`keepRulesJar`, you can print the rules on macOS and Linux with the following
commands:

    ./gradlew :mylibrary:keepRulesJar
    unzip -p mylibrary/build/intermediates/annotation-keep/keepRulesJar/mylibrary-keep-rules.jar \
        "META-INF/com.android.tools/*" "META-INF/proguard/*"

## Configure JVM libraries

For JVM library modules that produce a JAR, the plugin doesn't modify the JAR
automatically. Instead, use the `annotationKeep.registerJavaArchiveTransform`
function to register a task that creates a copy of the JAR with the generated
rules, and then publish that JAR. Add the following to the library module's
`build.gradle.kts` file:

    plugins {
        id("java-library")
        alias(libs.plugins.jetbrains.kotlin.jvm)
        alias(libs.plugins.androidx.annotation.keep)
    }

    val jarTask = tasks.named<Jar>("jar")

    // Apps run R8 on this library's code, so the generated rules must be inside
    // the JAR. The plugin handles this automatically only for Android modules.
    val keepRulesJarTask = annotationKeep.registerJavaArchiveTransform(
        taskName = "keepRulesJar",
        input = jarTask.flatMap { it.archiveFile },
        fileName = jarTask.flatMap { it.archiveFileName }.map { it.replace(".jar", "-keep-rules.jar") },
    )

    // Consumers of this library resolve apiElements and runtimeElements, so add
    // the JAR that contains the generated rules to them.
    configurations.configureEach {
        if (name == "apiElements" || name == "runtimeElements") {
            outgoing.artifact(keepRulesJarTask.flatMap { it.outputJar })
        }
    }

    dependencies {
        implementation(libs.androidx.annotation.keep)
    }

The transform adds the generated rules to the JAR's targeted R8 rules location,
`META-INF/com.android.tools/r8/proguard.txt`. If the JAR already contains rules
in `META-INF/com.android.tools/` or `META-INF/proguard/`, the transform appends
the generated rules to the existing rules file instead. For more information
about these locations, see [Support different R8 versions](https://developer.android.com/topic/performance/app-optimization/library-optimization#support-different).

After you register the transform, [verify the rules in the JAR](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#verify-jar).

## Example: Load an optional add-on library

Libraries often use reflection to load optional add-ons. For example, an
analytics SDK might ship a core library and a video add-on. The add-on depends
on the core library, so the core library can't refer to the add-on's classes
directly. Instead, the core library looks up the add-on's class by name at
runtime and turns on video analytics only if it finds the class.

Because the core library uses the add-on's class only through reflection, R8
might remove the class or its constructor from an app's release build, which
makes the lookup fail. The failure happens only in release builds of apps that
include the add-on, so it's hard to catch in testing.

Without Jetpack Keep, the add-on ships a consumer keep rule for its class,
as shown in [Reflection to support optional dependencies](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples#reflection-to-support-optional-dependencies):

    # In the add-on's consumer keep rules file.
    -keep class com.example.analytics.video.VideoEventTracker {
        <init>();
    }

This rule is in a different library from the lookup that needs it, so the two
can get out of sync. With Jetpack Keep, you annotate the lookup in the core
library instead:

    // In the core library.
    interface AnalyticsPlugin {
        fun start()
    }

    object AnalyticsManager {
        // The annotation and the lookup share this constant so that they can't
        // refer to different classes.
        private const val VIDEO_TRACKER_CLASS =
            "com.example.analytics.video.VideoEventTracker"

        @UsesReflectionToConstruct(
            className = VIDEO_TRACKER_CLASS,
            parameterTypes = [],
        )
        fun initialize() {
            val tracker = try {
                Class.forName(VIDEO_TRACKER_CLASS)
                    .getDeclaredConstructor()
                    .newInstance() as AnalyticsPlugin
            } catch (e: ClassNotFoundException) {
                // Apps that don't play video leave out the add-on, so a missing
                // class isn't an error.
                return
            }
            // This is an ordinary interface call, not a reflective one, so R8
            // keeps start() without an annotation.
            tracker.start()
        }
    }

The annotation follows these guidelines:

- **Annotate the code that performs the reflection.** The annotation is on `initialize`, which calls `Class.forName`, not on the add-on's class.
- **Choose the annotation based on what the code does.** The lookup creates an instance of the class, so the code uses `@UsesReflectionToConstruct`.
- **Use `className` for a class that you can't reference.** The add-on's class isn't on the core library's compile classpath, so the annotation can't use `classConstant`.
- **Keep only the constructor that the code calls.** The lookup calls the no-argument constructor, so `parameterTypes` is an empty array.

When you build the core library's AAR, the plugin adds a rule that keeps
`VideoEventTracker` and its no-argument constructor whenever R8 keeps
`initialize`. Apps that use the SDK apply this rule automatically, even if they
don't use Jetpack Keep, so the add-on doesn't need a rule of its own.
Compared with the add-on's rule, this approach has the following advantages:

- **The rule stays next to the lookup.** The core library owns both the lookup and the rule, so you update them together instead of coordinating a change across two libraries.
- **R8 can still remove unused code.** If an app includes the add-on but never calls `initialize`, the generated rule doesn't apply, and R8 can remove `VideoEventTracker`. The add-on's rule keeps it in every app that includes the add-on.
- **Lint catches unannotated lookups.** If the core library later adds another reflective lookup without an annotation, lint flags it, so you can fix it before you release the library.

To confirm the result, check that the generated rule appears in the AAR's
`proguard.txt` file, as described in [Android libraries](https://developer.android.com/topic/performance/app-optimization/jetpack-keep-annotations#verify-aar). Then
test a release build of an app that includes the add-on, because that's where a
missing rule would break video analytics.

## Limitations

Jetpack Keep doesn't yet detect reflection that finds classes and members by
their annotations, or generate keep rules for it. This feature is planned.

Until then, use [keep rules](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples) for this kind of reflection. For example, the
following rule keeps every member that's annotated with `@SomeAnnotation` in the
classes that R8 keeps:

    -keepclassmembers class * {
        @com.example.annotation.SomeAnnotation <methods>;
        @com.example.annotation.SomeAnnotation <fields>;
    }

If Jetpack Keep doesn't work for your use case, or if you have other feedback,
[file an issue](https://issuetracker.google.com/issues/new?component=2295349&template=2425184).

<br />

## Additional resources

- [Jetpack Keep sample](https://github.com/android/performance-samples/tree/main/KeepAnnotationsSample): An Android Studio project that uses Jetpack Keep in an app, an Android library, a Kotlin Multiplatform library, and a JVM library.
- [Keep rule use cases and examples](https://developer.android.com/topic/performance/app-optimization/keep-rule-examples): Keep rules for common reflection and JNI scenarios.
- [Follow best practices](https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices): Guidance on writing narrowly scoped keep rules.

<br />