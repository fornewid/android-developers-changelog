---
title: https://developer.android.com/build/publish-library/upload-library
url: https://developer.android.com/build/publish-library/upload-library
source: md.txt
---

To grant access to your library, you need to choose a repository.
This page guides you through the considerations related to choosing a
repository type and shows how to create a publication using the
[Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html).

Before uploading your library, make sure you have [prepared your library for
release](https://developer.android.com/studio/publish-library/prep-lib-release) and configured any necessary
[publication variants](https://developer.android.com/studio/publish-library/configure-pub-variants) or
[test fixtures](https://developer.android.com/studio/publish-library/configure-test-fixtures).

## Choose a repository type

Libraries are published as AAR files. These files contain compiled code as
bytecode and native libraries, an Android manifest, and resources. The package
itself does not declare any identity, version, or dependencies on other
libraries.

Providing AARs through a repository is generally the best practice, rather
than distributing the AAR directly. It
helps users have a better understanding of where the library is coming from
rather than having to deal with a `name.aar` file without important details,
like version. When upgrading to a newer version of a library, use a
repository to ensure that only the required dependencies of the newer version
are added, so that users don't have to manually update dependencies.

There are multiple benefits to using a repository to publish your library:

- Gradle can automatically add your library's dependencies to the [dependency
  graph](https://docs.gradle.org/current/userguide/viewing_debugging_dependencies.html).
- Gradle can ensure that a single version of your library is in the dependency graph, resolving conflicts if your library is transitively included more than once with different versions.
- The Android Gradle Plugin (AGP) can do more efficient desugaring if your library uses Java 8 or higher language features, reducing build times for your users.
- Your library can use variant publishing and include features like test fixtures.

Distributing the AAR directly doesn't provide your user with any information
regarding the identity, version, or dependencies of your library. When
publishing to a repository, distribution is handled by a separate file that is
part of the repository mechanism. For Maven repositories, this is the
[POM file](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html). Therefore, it is strongly recommended to publish libraries using
repositories rather than manually distributing AAR files.

### Types of repositories

There are three types of repositories:

- Free online repositories, like Maven Central, let anyone upload and download libraries.
- Private repositories, with access via login, allow controlled distribution of private libraries.
- Local, folder-based repositories allow distribution of libraries through manual download.

Using local, folder-based repositories is very similar to providing your users
with a manual download link to the AAR or sending the AAR by email. The main
difference is that you are not sending just the AAR but also the additional
information about identity, version, and dependencies.

You distribute a zip file of the folder-based repository containing your AAR
plus the metadata. Your users can then extract the file's contents, add the
contents to their project, and point Gradle to it. From then on, the users can
declare a dependency on the library using Maven coordinates, as if the library
were in an online repository, and benefit from all the advantages mentioned
earlier.

## Create the publication

Publish using the [Gradle Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html). The Maven Publish Plugin lets you declare publications and
repositories and creates tasks to publish these publications to the
repositories. These publications consume a `SoftwareComponent` instance that
the plugin that drives the build creates, which could be AGP or the
`java-library` plugin.

Note that when running the Maven Publish Plugin with AGP, the software
components are not created directly when the plugin is applied. They are instead
created during the
[`afterEvaluate()`](https://docs.gradle.org/current/userguide/build_lifecycle.html)
callback step. Therefore, the publication that selects the software component
must also be configured during the `afterEvaluate()` step.

The following code snippet of the module-level `build.gradle` file creates a
publication for a given variant created with `singleVariant()` or
`multipleVariants()`:

### Groovy

```groovy
publishing {
  publications {
    release(MavenPublication) {
      groupId = 'com.my-company'
      artifactId = 'my-library'
      version = '1.0'

      afterEvaluate {
        from components.release
      }
    }
  }
}
```

### Kotlin

```kotlin
publishing {
  publications {
    register<MavenPublication>("release") {
      groupId = "com.my-company"
      artifactId = "my-library"
      version = "1.0"

      afterEvaluate {
        from(components["release"])
      }
    }
  }
}
```

In the preceding example, the name of the component (`components.release`) is
based on the name that was given to either `singleVariant()`
or `multipleVariants()`.

Once you declare a publication, you must create a target repository.

### Publish to a local repository

Publishing to a local repository is very similar to publishing to a remote
repository, except for the repository declaration. Read the preceding section to
learn how to [publish to a remote repository](https://developer.android.com/build/publish-library/upload-library#create-pub) to create a
publication that publishes the desired variant or variants. Then create a local
repository:

### Groovy

```groovy
publishing {
  publications {
    release(MavenPublication) {
      ...
    }
  }
  repositories {
    maven {
      name = 'myrepo'
      url = layout.buildDirectory.dir("repo")
    }
  }
}
```

### Kotlin

```kotlin
publishing {
  publications {
    register<MavenPublication>("release") {
      ...
    }
  }
  repositories {
    maven {
      name = "myrepo"
      url = uri(layout.buildDirectory.dir("repo"))
    }
  }
}
```

This creates a task called
`publishReleaseToMyRepoRepository` that consists of
the name of the publication and the name of the repository. Run this task
to generate the repository to the location provided. In this example, the
repository is generated inside the build
folder of the project, under a `repo` directory.

If you want to automatically generate a zip file of the repository, do
so using the following code:

### Groovy

```groovy
tasks.register('generateRepo', Zip) {
  def publishTask = tasks.named('publishReleasePublicationToMyrepoRepository')
  from publishTask.map { it.getRepository().getUrl() }
  into 'mylibrary'
  archiveFileName.set('mylibrary.zip')
}
```

### Kotlin

```kotlin
tasks.register<Zip>("generateRepo") {
  val publishTask = tasks.named(
    "publishReleasePublicationToMyrepoRepository",
    PublishToMavenRepository::class.java)
  from(publishTask.map { it.repository.url })
  into("mylibrary")
  archiveFileName.set("mylibrary.zip")
}
```

This code creates a `Zip` task called `generateRepo` that consumes the content
of the publishing task and compresses it while ensuring that the zip entries are in a
top-level folder called `mylibrary`. The output is located under
`build/distributions`.