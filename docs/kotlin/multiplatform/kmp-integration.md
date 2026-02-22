---
title: https://developer.android.com/kotlin/multiplatform/kmp-integration
url: https://developer.android.com/kotlin/multiplatform/kmp-integration
source: md.txt
---

This document provides a guide for plugin authors on how to correctly detect, interact with, and configure the Kotlin Multiplatform (KMP) setup, with a specific focus on integrating with the Android targets within a KMP project. As KMP continues to evolve, understanding the proper hooks and APIs---such as `KotlinMultiplatformExtension`, `KotlinTarget` types, and the Android-specific integration interfaces---is essential for building robust and future-proof tooling that works seamlessly across all platforms defined in a multiplatform project.

## Check if a project uses the Kotlin Multiplatform plugin

To avoid errors and to make sure that your plugin only runs when KMP is present,
you must check if the project uses the KMP plugin. It's best practice to use
`plugins.withId()` to react to the KMP plugin being applied, rather than
checking for it immediately. This reactive approach prevents your plugin from
being brittle to the order in which plugins are applied in the user's build
scripts.

    import org.gradle.api.Plugin
    import org.gradle.api.Project

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("org.jetbrains.kotlin.multiplatform") {
                // The KMP plugin is applied, you can now configure your KMP integration.
            }
        }
    }

## Access the model

The entry point for all Kotlin Multiplatform configurations is the
`KotlinMultiplatformExtension` extension.

    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("org.jetbrains.kotlin.multiplatform") {
                val kmpExtension = project.extensions.getByType(KotlinMultiplatformExtension::class.java)
            }
        }
    }

## React to Kotlin Multiplatform targets

Use the `targets` container to reactively configure your plugin for each target
the user adds.
| **Important:** Use `targets.configureEach { }` to apply configuration lazily. Iterating with `forEach` might cause errors if the targets are not yet fully registered or configured by Gradle.

    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("org.jetbrains.kotlin.multiplatform") {
                val kmpExtension = project.extensions.getByType(KotlinMultiplatformExtension::class.java)
                kmpExtension.targets.configureEach { target ->
                    // 'target' is an instance of KotlinTarget
                    val targetName = target.name // for example, "android", "iosX64", "jvm"
                    val platformType = target.platformType // for example, androidJvm, jvm, native, js
                }
            }
        }
    }

## Apply target-specific logic

If your plugin needs to apply logic only to certain types of platforms, a common
approach is to check the `platformType` property. This is an enum that broadly
categorizes the target.

For example, use this if your plugin only needs to differentiate broadly (for example,
run only on JVM-like targets):

    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension
    import org.jetbrains.kotlin.gradle.plugin.KotlinPlatformType

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("org.jetbrains.kotlin.multiplatform") {
                val kmpExtension = project.extensions.getByType(KotlinMultiplatformExtension::class.java)
                kmpExtension.targets.configureEach { target ->
                    when (target.platformType) {
                        KotlinPlatformType.jvm -> { /* Standard JVM or Android */ }
                        KotlinPlatformType.androidJvm -> { /* Android */ }
                        KotlinPlatformType.js -> { /* JavaScript */ }
                        KotlinPlatformType.native -> { /* Any Native (iOS, Linux, Windows, etc.) */ }
                        KotlinPlatformType.wasm -> { /* WebAssembly */ }
                        KotlinPlatformType.common -> { /* Metadata target (rarely needs direct plugin interaction) */ }
                    }
                }
            }
        }
    }

### Android-specific details

While all Android targets have the `platformType.androidJvm` indicator, KMP has
two distinct integration points depending on the Android Gradle plugin used:
`KotlinAndroidTarget` for projects using `com.android.library` or
`com.android.application`, and `KotlinMultiplatformAndroidLibraryTarget` for
projects using `com.android.kotlin.multiplatform.library`.
| **Note:** The new KMP Android plugin, `com.android.kotlin.multiplatform.library`, is not part of the `com.android.base` plugin, which other Android plugins (like `com.android.application` and `com.android.library`) are part of. This is an important distinction if your plugin logic relies on detecting `com.android.base`.

The `KotlinMultiplatformAndroidLibraryTarget` API was added in AGP 8.8.0 so if
the consumers of your plugin are running on lower version of AGP, checking
`target is KotlinMultiplatformAndroidLibraryTarget` might result in a
`ClassNotFoundException`. To make this safe, check
`AndroidPluginVersion.getCurrent()` before checking the target type.
Note that `AndroidPluginVersion.getCurrent()` requires AGP 7.1 or higher.

    import com.android.build.api.AndroidPluginVersion
    import com.android.build.api.dsl.KotlinMultiplatformAndroidLibraryTarget
    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension
    import org.jetbrains.kotlin.gradle.plugin.mpp.KotlinAndroidTarget

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("com.android.kotlin.multiplatform.library") {
                val kmpExtension = project.extensions.getByType(KotlinMultiplatformExtension::class.java)
                kmpExtension.targets.configureEach { target ->
                    if (target is KotlinAndroidTarget) {
                        // Old kmp android integration using com.android.library or com.android.application
                    }
                    if (AndroidPluginVersion.getCurrent() >= AndroidPluginVersion(8, 8) &&
                        target is KotlinMultiplatformAndroidLibraryTarget
                    ) {
                        // New kmp android integration using com.android.kotlin.multiplatform.library
                    }
                }
            }
        }
    }

## Access the Android KMP extension and its properties

Your plugin will primarily interact with the Kotlin extension provided
by the Kotlin Multiplatform plugin and the Android extension provided by AGP
for the KMP Android target. The `android {}` block within the Kotlin extension
in a KMP project is represented by the `KotlinMultiplatformAndroidLibraryTarget`
interface, which also extends `KotlinMultiplatformAndroidLibraryExtension`.
This means you can access both target-specific and Android-specific DSL
properties through this single object.

    import com.android.build.api.dsl.KotlinMultiplatformAndroidLibraryTarget
    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension
    import org.jetbrains.kotlin.gradle.plugin.KotlinMultiplatformPluginWrapper

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("com.android.kotlin.multiplatform.library") {
                val kmpExtension = project.extensions.getByType(KotlinMultiplatformExtension::class.java)

                // Access the Android target, which also serves as the Android-specific DSL extension
                kmpExtension.targets.withType(KotlinMultiplatformAndroidLibraryTarget::class.java).configureEach { androidTarget ->

                    // You can now access properties and methods from both
                    // KotlinMultiplatformAndroidLibraryTarget and KotlinMultiplatformAndroidLibraryExtension
                    androidTarget.compileSdk = 34
                    androidTarget.namespace = "com.example.myplugin.library"
                    androidTarget.withJava() // enable Java sources
                }
            }
        }
    }

Unlike other Android plugins (such as `com.android.library` or
`com.android.application`), the KMP Android plugin does not register its main
DSL extension at the project level. It lives within the KMP target hierarchy
to make sure it only applies to the specific Android target defined in your
multiplatform setup.

## Handle compilations and source sets

Often, plugins need to work at a more granular level than just the
target---specifically, they need to work at the *compilation* level. The `KotlinMultiplatformAndroidLibraryTarget`
contains `KotlinMultiplatformAndroidCompilation` instances (for example, `main`,
`hostTest`, `deviceTest`). Each compilation is associated with Kotlin source
sets. Plugins can interact with these to add sources, dependencies, or configure
compilation tasks.

    import com.android.build.api.dsl.KotlinMultiplatformAndroidCompilation
    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("com.android.kotlin.multiplatform.library") {
                val kmpExtension = project.extensions.getByType(KotlinMultiplatformExtension::class.java)
                kmpExtension.targets.configureEach { target ->
                    target.compilations.configureEach { compilation ->
                        // standard compilations are usually 'main' and 'test'
                        // android target has 'main', 'hostTest', 'deviceTest'
                        val compilationName = compilation.name

                        // Access the default source set for this compilation
                        val defaultSourceSet = compilation.defaultSourceSet

                        // Access the Android-specific compilation DSL
                        if (compilation is KotlinMultiplatformAndroidCompilation) {

                        }

                        // Access and configure the Kotlin compilation task
                        compilation.compileTaskProvider.configure { compileTask ->

                        }
                    }
                }
            }
        }
    }

## Configure test compilations in convention plugins

When configuring default values for test compilations (such as `targetSdk` for
instrumented tests) in a convention plugin, you should avoid using enabler
methods like `withDeviceTest { }` or `withHostTest { }`. Calling these methods
eagerly triggers the creation of the corresponding Android test variants and
compilations for every module that applies the convention plugin, which might
not be suitable. Furthermore, these methods cannot be called a second time in
a specific module to refine settings, because doing so will throw an error
stating the compilation has already been created.

Instead, we recommend using a reactive `configureEach` block
on the compilations container. This lets you provide default configurations
that only apply if and when a module explicitly enables the test compilation:

    import com.android.build.api.dsl.KotlinMultiplatformAndroidDeviceTestCompilation
    import com.android.build.api.dsl.KotlinMultiplatformAndroidLibraryTarget
    import org.gradle.api.Plugin
    import org.gradle.api.Project
    import org.jetbrains.kotlin.gradle.dsl.KotlinMultiplatformExtension

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("com.android.kotlin.multiplatform.library") {
                val kmpExtension =
                    project.extensions.getByType(KotlinMultiplatformExtension::class.java)
                kmpExtension.targets.withType(KotlinMultiplatformAndroidLibraryTarget::class.java)
                    .configureEach { androidTarget ->
                        androidTarget.compilations.withType(
                            KotlinMultiplatformAndroidDeviceTestCompilation::class.java
                        ).configureEach {
                            targetSdk { version = release(34) }
                        }
                    }
            }
        }
    }

This pattern makes sure that your convention plugin remains lazy and allows
individual modules to call `withDeviceTest { }` to enable and further customize
their tests without conflicting with the defaults.

## Interact with the Variant API

For tasks that require late-stage configuration, artifact access (like
manifests or byte-code), or the ability to enable or disable specific
components, you must use the Android Variant API. In KMP projects, the
extension is of type `KotlinMultiplatformAndroidComponentsExtension`.

The extension is registered at the project level when the KMP Android plugin is
applied.

Use `beforeVariants` to control the creation of variants or their nested test
components (`hostTests` and `deviceTests`). This is the correct place to
programmatically disable tests or change DSL properties' values.

    import com.android.build.api.variant.KotlinMultiplatformAndroidComponentsExtension
    import org.gradle.api.Plugin
    import org.gradle.api.Project

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("com.android.kotlin.multiplatform.library") {
                val androidComponents = project.extensions.findByType(KotlinMultiplatformAndroidComponentsExtension::class.java)
                androidComponents?.beforeVariants { variantBuilder ->
                    // Disable all tests for this module
                    variantBuilder.hostTests.values.forEach { it.enable = false }
                    variantBuilder.deviceTests.values.forEach { it.enable = false }
                }
            }
        }
    }

Use `onVariants` to access the final variant object
(`KotlinMultiplatformAndroidVariant`). This is where you can inspect resolved
properties or register transformations on artifacts like the merged manifest
or library classes.

    import com.android.build.api.variant.KotlinMultiplatformAndroidComponentsExtension
    import org.gradle.api.Plugin
    import org.gradle.api.Project

    class MyPlugin : Plugin<Project> {
        override fun apply(project: Project) {
            project.plugins.withId("com.android.kotlin.multiplatform.library") {
                val androidComponents = project.extensions.findByType(KotlinMultiplatformAndroidComponentsExtension::class.java)
                androidComponents?.onVariants { variant ->
                    // 'variant' is a KotlinMultiplatformAndroidVariant
                    val variantName = variant.name

                    // Access the artifacts API
                    val manifest = variant.artifacts.get(com.android.build.api.variant.SingleArtifact.MERGED_MANIFEST)
                }
            }
        }
    }

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Set up your environment](https://developer.android.com/kotlin/multiplatform/setup)
- [Add KMP module to a project](https://developer.android.com/kotlin/multiplatform/migrate)
- [Set up the Android Gradle Library Plugin for KMP](https://developer.android.com/kotlin/multiplatform/plugin)