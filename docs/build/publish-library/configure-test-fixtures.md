---
title: https://developer.android.com/build/publish-library/configure-test-fixtures
url: https://developer.android.com/build/publish-library/configure-test-fixtures
source: md.txt
---

# Configure test fixtures for publication

While publishing test fixtures doesn't require any particular configuration of the publication, the[capability mechanism](https://docs.gradle.org/current/userguide/component_capabilities.html)used to handle fixtures does require an additional configuration.

For a given artifact with coordinates`groupId:artifactId:version`, Gradle expects that the test fixtures artifact declares a capability with coordinates`groupId:artifactId-test-fixtures:version`. This is not currently done automatically by either the test fixture support or the Maven Publish Plugin, and therefore must be done manually.

Gradle creates the capability from the project's name, group, and version. All three must be set up to match the`artifactId`,`groupId`, and`version`set in the publication.

The project's name is the last segment of its path by default, so the default name of a project with the path`:path:to:mylibrary`is`mylibrary`. If this is not what you want to use for`artifactId`, then you need to change your project name.

There are two options for renaming your project:

- Rename the folder of the project. This changes the project name, or the Gradle path of the project, so all dependencies on the project need to be updated. While keeping the project name and folder the same might create more reorganization work initially, it reduces confusion.
- Rename the project in Gradle without renaming the folder of the project. This avoids the impact on source versioning, but it splits the project location and name.

To rename the project in Gradle, insert the following code in the`settings.gradle`file:  

### Groovy

```groovy
include ':path:to:mylibrary'
project(':path:to:mylibrary').name = 'my-library'
```

### Kotlin

```kotlin
include(":path:to:mylibrary")
project(":path:to:mylibrary").name = "my-library"
```

This code assigns the new path of the project to`:path:to:my-library`.

The value`groupId`defaults to the build name, which is generally the name of the root folder, and the value`version`is by default unspecified. To change the values of the group ID or version, set the`group`and`version`properties, respectively, in your project-level`build.gradle`file (for Groovy) or`build.gradle.kts`(for Kotlin script):  

### Groovy

```groovy
group = 'com.my-company'
version = '1.0'
```

### Kotlin

```kotlin
group = "com.my-company"
version = "1.0"
```