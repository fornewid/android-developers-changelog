---
title: https://developer.android.com/build/gradle-dependency-resolution
url: https://developer.android.com/build/gradle-dependency-resolution
source: md.txt
---

Your build files specify your *direct* dependencies, but each of those
dependencies can require others. These *transitive* dependencies quickly grow
your overall dependency graph, often with conflicting versions.

> [!NOTE]
> **Note:** This page uses [semantic versioning](https://semver.org/) throughout and follows a `major.minor.patch` format. For example, in the version number 4.8.3, 4 is the `major` version, 8 is the `minor` version and 3 is the `patch` number. When the `major` part changes, the library might have breaking changes in API or behavior. This can impact your build or application behavior, so you should test your build and app thoroughly to ensure compatibility.

When the `minor` (new features) or `patch` (bug fixes) parts change, the library
is still likely to be compatible and less likely to impact your application.

For example, suppose your application depends on library A and library B, which
in turn depend on different versions of library C.
![Your app depends on library A and library B, which in turn depend on different versions of library C. Gradle chooses the newest version of library C.](https://developer.android.com/static/images/build/conflict-1.svg) **Figure 1.** A transitive version conflict. Gradle resolves to the newest version (by default).

In this case, Gradle chooses the newest version of library C by default, which
may cause compilation or runtime issues. In this example, library C is resolved
to 2.1.1, but note that library A requested library C 1.0.3. The major part of
the version number has changed, indicating incompatible changes, such as removed
functions or types. This could cause calls made from library A to crash.

Your app can have direct dependencies that are also transitive dependencies.
![Your app depends on library A and library C. Library A depends on a newer version of library C. Gradle chooses the newest version of library C.](https://developer.android.com/static/images/build/conflict-2.svg) **Figure 2.** Another transitive version conflict. Here, Gradle resolves to the transitive version, and your application sees that newer version.

In a case like this, newer transitive dependencies can override the version you
directly request in your app.

Gradle looks at all candidate versions for all dependencies in the graph to
determine the newest version of each dependency. You can use [basic Gradle
tasks](https://docs.gradle.org/current/userguide/viewing_debugging_dependencies.html) and third-party plugins to determine which versions
of each dependency Gradle has resolved. Comparing the changes in this resolution
is key to understanding and mitigating the risks of your upgrade.

For example, you can use the Gradle `dependencies` task by running `./gradlew
app:dependencies` to display a tree of all dependencies used by your app
module. Running this against an application that uses the libraries as shown in
figure 2, we see

    1: releaseRuntimeClasspath - Runtime classpath of /release.
    2: +--- org.jetbrains.kotlin:kotlin-stdlib:2.0.0
    3: |    +--- ... (omitted for brevity) ...
    4: +--- com.sample:library.a:1.2.3
    5: |    +--- com.sample:library.c:2.1.1
    6: |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:2.0.0 (*)
    7: |    \--- org.jetbrains.kotlin:kotlin-stdlib:2.0.0 (*)
    8: +--- com.sample:library.c:1.4.1 -> 2.1.1 (*)

This part of the report shows some of the dependencies resolved for the
`releaseRuntimeClasspath` configuration.

Whenever you see `->` in your dependencies report, a requestor (your application
or another library) uses a version of that dependency that it isn't
expecting. In many cases, this doesn't cause any issues, as most libraries are
written for backward compatibility. However, some libraries may make
incompatible changes, and this report can help you determine where new issues
with your application's behavior are coming from.

More details on using Gradle's dependency reporting can be found at [View and
Debug Dependencies](https://docs.gradle.org/current/userguide/viewing_debugging_dependencies.html).

> [!NOTE]
> **Note:** You can [customize dependency resolution](https://docs.gradle.org/current/userguide/resolution_rules.html) in Gradle if needed, but most often the "newest version wins" strategy works well.

You can specify requested versions directly, in a version catalog, or in a Bill
of Materials (BOM).

### Direct version specification resolution

The versions of dependencies you specify become candidates for version
resolution.

For example, to request version 1.7.3 of the `androidx.compose.ui:ui` library as
a dependency in your `app/build.gradle.kts`:

    dependencies {
        implementation("androidx.compose.ui:ui:1.7.3")
    }

Version 1.7.3 becomes a candidate version. Gradle resolves to the latest
version among 1.7.3 and other versions of the same library requested by
transitive dependencies.

### Version catalog resolution

Version catalogs define variables to track the version of dependencies used
throughout your application. If you use a variable from the version catalog,
then that variable's specified dependencies are added to the candidates for
version resolution. Unused variables in the version catalog are ignored.

For example, to specify version 1.7.3 of the `androidx.compose.ui:ui` as a
dependency in your `gradle/libs.versions.toml` file:

    [versions]
    ui = "1.7.3"

    [libraries]
    androidx-compose-ui = { group = "androidx.compose.ui", name = "ui", version.ref = "ui" }

This defines a variable named `libs.androidx.compose.ui` to represent the
library. This version is *not* considered a candidate unless you use that
variable to specify a dependency.

To request the library and its version in your `app/build.gradle.kts`:

    dependencies {
        implementation(libs.androidx.compose.ui)
    }

Gradle resolves the same way it did for a direct specification.

### Bill of Materials (BOM) resolution

Versions for *all* libraries appearing in the BOM become candidates for version
resolution. Note that libraries are used as dependencies only if specified as
direct or indirect. Other libraries in the BOM are ignored.

BOM versions affect your direct dependencies as well as all transitive
dependencies that appear in the BOM.

For example, specify a BOM as a *platform* dependency in your
`app/build.gradle.kts`:

    dependencies {
        implementation(platform("androidx.compose:compose-bom:2024.10.00"))
        implementation("androidx.compose.ui:ui")
    }

Any libraries you want to use as dependencies don't require a version
specification; the requested version comes from the BOM.

Note that you can also use a version catalog to create variables for the BOM and
libraries. Omit the version numbers in the version catalog for libraries that
appear in a BOM dependency.

For example, your version catalog contains the BOM and its version number, but
doesn't specify a version for the libraries that you reference from the BOM:

    [versions]
    composeBom = "2024.10.00"

    [libraries]
    androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "composeBom" }
    androidx-compose-ui = { group = "androidx.compose.ui", name = "ui" }

Your `app/build.gradle.kts` references the BOM and libraries using the variables
defined in the version catalog:

    dependencies {
        implementation(platform(libs.androidx.compose.bom))
        implementation(libs.androidx.compose.ui)
    }

The version of that library specified in the BOM becomes a candidate for
Gradle's resolution. Further, all other library versions specified in the BOM
become candidate versions, whether or not you directly use them as dependencies.

For example, suppose a BOM specifies versions for libraries A, B, and C. Your
application wants to directly use library A as a dependency, as well as library
D. Library D uses library B as a dependency. Nothing uses library C.
![A BOM includes versions for libraries A, B, and C. Your application uses libraries A and D as dependencies. Library D uses library B as a dependency. Library C isn't used directly or indirectly in this application.](https://developer.android.com/static/images/build/bom-resolution.svg) **Figure 3.** BOM scenario.

Libraries A, B and D are dependencies in the application; library C is ignored.
Gradle uses the versions of A and B specified in the BOM as candidates, even
though you don't directly specify library B as a dependency.

If library D requested a version of library B lower than 2.0.1, Gradle
resolves to 2.0.1. If library D requested a higher version of library B, Gradle
resolves to that version.