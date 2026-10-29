---
title: https://developer.android.com/tools/agents/lightbuild/release-notes
url: https://developer.android.com/tools/agents/lightbuild/release-notes
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

This page lists the new features and known issues in each Lightbuild release. To
get started with Lightbuild, see [Get started with Lightbuild](https://developer.android.com/tools/agents/lightbuild/setup). To report
a bug, [file an issue](https://goo.gle/lightbuild-feedback).

## Lightbuild 0.0.30 (October 2026)

Lightbuild 0.0.30 is the first public preview release of Lightbuild.

### Supported

Lightbuild 0.0.30 supports the following:

- Declarative YAML build configuration for app and library modules, including local and instrumented tests
- Kotlin and Jetpack Compose support by default
- Creating, building, running, testing, and debugging projects in Android Studio Canary
- Building, testing, and querying projects, and resolving dependencies, with the Lightbuild CLI
- KSP code generators, such as Moshi and Room
- Protocol Buffers code generation for Java and Kotlin
- Libraries that support Kotlin Multiplatform (KMP), such as Koin and Ktor
- Password-protected Maven repositories
- Resolved dependencies in `resolved.deps` files that you check in to version control

### Not supported

Lightbuild 0.0.30 doesn't support the following:

- Version catalogs and convention plugins
- Custom plugins
- Product flavors ([use separate app modules](https://developer.android.com/tools/agents/lightbuild/structure#multiple-apps) instead)
- Kotlin Multiplatform (KMP) modules
- Proxy servers for downloading dependencies
- Kotlin DSL and Lightbuild modules in the same project