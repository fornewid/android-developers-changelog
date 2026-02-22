---
title: https://developer.android.com/studio/intro/migrate
url: https://developer.android.com/studio/intro/migrate
source: md.txt
---

Migrating your projects to Android Studio requires adapting to a new project
structure, build system, and IDE functionality.

If you are migrating from IntelliJ and your project already uses Gradle,
you can open your existing project from Android Studio. If you are using
IntelliJ but your project doesn't already use Gradle, you need to
manually prepare your project before you can import it into Android
Studio. For more information, see the [Migrate from IntelliJ](https://developer.android.com/studio/intro/migrate#migrate-intellij)
section.

## Android Studio basics

Here are some of the key differences to be aware of as you prepare to
migrate to Android Studio.

### Project and module organization

Android Studio is based on the [IntelliJ
IDEA](https://www.jetbrains.com/idea/) IDE. To familiarize yourself
with the IDE basics, such as navigation, code completion, and keyboard
shortcuts, see [Meet Android Studio](https://developer.android.com/studio/intro).

Android Studio organizes code into projects, which contain everything that defines
your Android app, from app source code to build configurations and test code.
Projects open in separate Android Studio windows. Each project
contains one or more modules, which let you divide your project into
discrete units of functionality. Modules can be independently built, tested, and
debugged.

For more information about Android Studio
projects and modules, see the [Projects overview](https://developer.android.com/tools/projects).

### Gradle-based build system

Android Studio's build system is based on
[Gradle](http://gradle.org) and uses build configuration files
written in either Groovy or Kotlin script for ease of extensibility and
customization.

Gradle-based projects offer significant features for Android development,
including the following:

- Support for binary libraries (AARs). You no longer need to copy library sources into your own projects; you can [declare a dependency](https://developer.android.com/studio/build/build-variants#dependencies) and the library is automatically downloaded and merged into your project. This includes automatically merging in resources, manifest entries, Proguard exclusion rules, custom lint rules, and so on at build time.
- Support for [build variants](https://developer.android.com/studio/build/build-variants), which let you build different versions of your app (such as a free version and a pro version) from the same project.
- Easy [build configuration](https://developer.android.com/studio/build) and customization. For example, you can pull version names and version codes from Git tags as part of the build.
- Gradle can be used from the IDE, from the [command line](https://developer.android.com/studio/build/building-cmdline), and from continuous integration servers like Jenkins, providing the same build everywhere, every time.

For more information about using and configuring Gradle, see
[Configure your build](https://developer.android.com/tools/building/plugin-for-gradle).

### Dependencies

Library dependencies in Android Studio use Gradle dependency declarations and
Maven dependencies for well-known local source and binary libraries with Maven
coordinates. For more information, see
[Declare dependencies](https://developer.android.com/tools/building/configuring-gradle#dependencies).

## Migrate from IntelliJ

If your IntelliJ project uses the Gradle build system, you can
import your project directly into Android Studio. If your IntelliJ project uses
Maven or another build system, you need to set it up to work with Gradle
before you can migrate to Android Studio.

### Import a Gradle-based IntelliJ project

If you are already using Gradle with your IntelliJ project, open it in
Android Studio using the following steps:

1. Click **File \> New \> Import Project**.
2. Select your IntelliJ project directory and click **OK**. Your project opens in Android Studio.

### Import a non-Gradle IntelliJ project

If your IntelliJ project doesn't already use the Gradle build system, you have
two options for importing your project into Android Studio, which are described
in the sections that follow:

- Create a new empty Android Studio project and copy your existing source code into the directories associated with the new project. For more information, see the section about [migrating by creating a new empty
  project](https://developer.android.com/studio/intro/migrate#empty-project).
- Create a new Gradle build file for your project and then import the project and new build file into Android Studio. For more information, see the section about [migrating by creating a custom Gradle build file](https://developer.android.com/studio/intro/migrate#custom-gradle).

<br />

#### Migrate by creating a new empty project

To migrate your project into Android Studio by creating a new empty project and
copying your source files into the new directories, proceed as follows:

1. Open Android Studio and click **File \> New \> New Project**.
2. Enter a name for your app project and specify the location where it should be created, then click **Next**.
3. Select the form factors your app runs on, then click **Next**.
4. Click **Add No Activity** , then click **Finish**.
5. In the **Project** tool window, click the arrow to open the view menu and select the **Project** view to see and explore the organization of your new Android Studio project. To read more about changing views and how Android Studio structures projects, see [Project files](https://developer.android.com/studio/projects#ProjectFiles).
6. Navigate to the location you selected for your new project and move the code, unit tests, instrumentation tests, and resources from your old project directories into the correct locations in your new project structure.
7. In Android Studio, click **File \> Project Structure** to open the Project Structure dialog. Ensure that your app's module is selected in the left pane.
8. Make any necessary modifications in the **Properties** tab for your project (for example, modifying the `minSdk` or `targetSdk`).
9. Click **Dependencies** and add any libraries your project depends on as Gradle dependencies. To add a new dependency, click **Add** ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png), then select the type of dependency you would like to add and follow the prompts.
10. Click **OK** to save your modifications.
11. Click **Build \> Make Project** to test building your project, and if necessary resolve any outstanding errors.

#### Migrate by creating a custom Gradle build file

To migrate your project into Android Studio by creating a new Gradle build file
to point to your existing source files, proceed as follows:

1. Before you begin, back up your project files in a separate location, as the migration process modifies the contents of your project in place.
2. Create a file in your project directory called `build.gradle`, if you're using Groovy, or `build.gradle.kts`, if you're using Kotlin script. This file contains all the information required for Gradle to run your build.

   By default, Android Studio expects your project to be organized as
   shown in figure 1.
   ![](https://developer.android.com/static/images/tools/studio/project-structure_2x.png) **Figure 1.** The default project structure for an Android app module.

   In `settings.gradle`, for Groovy, or
   `settings.gradle.kts`, for Kotlin script, you set the repositories
   that are used to find plugins and dependencies in the
   `pluginManagement` and `dependencyResolutionManagement`
   blocks, respectively:

   ### Groovy

   ```groovy
     pluginManagement {
         repositories {
             google()
             mavenCentral()
             gradlePluginPortal()
         }
     }
     dependencyResolutionManagement {
         repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
         repositories {
             google()
             mavenCentral()
         }
     }
     rootProject.name = "Test App"
     include ':app'
     
   ```

   ### Kotlin

   ```kotlin
     pluginManagement {
         repositories {
             google()
             mavenCentral()
             gradlePluginPortal()
         }
     }
     dependencyResolutionManagement {
         repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
         repositories {
             google()
             mavenCentral()
         }
     }
     rootProject.name = "Test App"
     include(":app")
     
   ```


   **Warning:** The JCenter repository became read-only on March 31, 2021.
   For more information, see
   [JCenter service update](https://developer.android.com/studio/build/jcenter-migration).

   The Android Gradle plugin applies some default
   [source sets](https://developer.android.com/studio/build#sourcesets) to the project. These
   source sets define the directories used to store
   [various types of source files](https://developer.android.com/studio/projects#ProjectView).
   Gradle uses these source sets to determine the locations of specific file
   types. If your existing project doesn't conform to the defaults, then you can
   either move files to where they should be or
   [change the default
   source sets](https://developer.android.com/studio/build/build-variants#configure-sourcesets) so Gradle knows where to find them.

   For more information about setting up and customizing a Gradle build file, read
   [Configure your build.](https://developer.android.com/studio/build)
3. Next, identify which library projects you are using.

   With Gradle, you no
   longer need to add these libraries as source code projects. You can instead
   refer to them in the `dependencies{}` block of your build file. The
   build system then handles these libraries for you, including downloading
   libraries, merging in resources, and merging manifest entries. The following
   example adds the declaration statements for a number of AndroidX libraries to
   the `dependencies{}` block of a build file.

   ### Groovy

   ```groovy
   ...
   dependencies {
       implementation fileTree(dir: 'libs', include: ['*.jar'])

       // AndroidX libraries
       implementation 'androidx.core:core-ktx:1.17.0'
       implementation 'androidx.appcompat:appcompat:1.7.1'
       implementation 'androidx.cardview:cardview:1.0.0'
       implementation 'com.google.android.material:material:1.7.0'
       implementation 'androidx.gridlayout:gridlayout:1.1.0'
       implementation 'androidx.leanback:leanback:'
       implementation 'androidx.mediarouter:mediarouter:1.8.1'
       implementation 'androidx.palette:palette-ktx:1.0.0'
       implementation 'androidx.recyclerview:recyclerview:1.4.0'
       implementation 'androidx.annotation:annotation:1.9.1'

       // Note: these libraries require that the Google repository has been declared
       // in the pluginManagement section of the top-level build.gradle file.
   }
   ```

   ### Kotlin

   ```kotlin
   ...
   dependencies {
       implementation(fileTree(mapOf("dir" to "libs", "include" to listOf("*.jar"))))

       // AndroidX libraries
       implementation("androidx.core:core-ktx:1.17.0")
       implementation("androidx.appcompat:appcompat:1.7.1")
       implementation("androidx.cardview:cardview:1.0.0")
       implementation("com.google.android.material:material:1.7.0")
       implementation("androidx.gridlayout:gridlayout:1.1.0")
       implementation("androidx.leanback:leanback:")
       implementation("androidx.mediarouter:mediarouter:1.8.1")
       implementation("androidx.palette:palette-ktx:1.0.0")
       implementation("androidx.recyclerview:recyclerview:1.4.0")
       implementation("androidx.annotation:annotation:1.9.1")

       // Note: these libraries require that the Google repository has been declared
       // in the pluginManagement section of the top-level build.gradle.kts file.
   }
   ```
   For help determining the correct declaration statements for your libraries, search [the Google Maven
   repository](https://maven.google.com/) or [Maven
   Central](https://search.maven.org/).
4. Save your `build.gradle` file, then close the project in IntelliJ. Navigate to your project directory and delete the `.idea` directory and any IML files in your project.
5. Launch Android Studio and click **File \> New \> Import
   Project**.
6. Locate your project directory, select the `build.gradle` or `build.gradle.kts` file you created, and then click **OK** to import your project.
7. Click **Build \> Make Project** to test your build file by building your project, and address any errors you find.

## Next steps

Once you have migrated your project to Android Studio, learn more about building
with Gradle and running your app in Android Studio by reading
[Build and run your app](https://developer.android.com/studio/run).

Depending on your project and workflow, you may also want to learn more about
version control, managing dependencies, and configuring Android Studio. To get
started using Android Studio, read
[Meet Android Studio](https://developer.android.com/studio/intro).

### Configure version control

Android Studio supports a variety of version control systems, including Git,
Mercurial, and Subversion. Other version control systems can be added through
plugins.

If your app is already under source control, you might need to enable it in
Android Studio. From the VCS menu, click **Enable Version Control Integration**
and select the appropriate version control system.

If your app is not under source control, you can configure it after importing
your app into Android Studio. Use the Android Studio VCS menu options to enable
VCS support for the desired version control system, create a repository, import
the new files into version control, and perform other version control
operations:

1. From the Android Studio VCS menu, click **Enable Version Control
   Integration**.
2. Select a version control system to associate with the project root from the menu, then click **OK**. The VCS menu now displays a number of version control options based on the system you selected.

**Note:** You can also use the **File \>
Settings \> Version Control** menu option to set up and modify the version
control.

For more information about working with version control, see
[IntelliJ's Version control reference](https://www.jetbrains.com/help/idea/2025.3/version-control-integration.html).

### App signing

If a debug certificate was used previously, it might be detected during
the import process. In this case, Android Studio continues to reference that
certificate. Otherwise, the debug configuration uses the Android Studio-generated
debug keystore, using a known password and a default key with a known
password located in `$HOME/.android/debug.keystore`. The debug build type is set
to use this debug configuration automatically when you run or debug your project
from Android Studio.

Similarly, the import process might detect an existing release certificate.
If no release certificate was defined previously, add the release signing
configuration to the `build.gradle` or `build.gradle.kts` file or use the
**Build \> Generate Signed APK** menu option to open the *Generate Signed APK
Wizard* . For more information about signing your app, see
[Sign your app](https://developer.android.com/studio/publish/app-signing).

### Adjust Android Studio's maximum heap size

By default, Android Studio has a maximum heap size of 1280MB. If you are
working on a large project, or your system has a lot of RAM, you can improve
performance by [increasing the maximum heap
size](https://developer.android.com/studio/intro/studio-config#adjusting_heap_size).

### Software updates

Android Studio updates separately from the Gradle plugin, the build tools, and
the SDK tools. You can specify which versions you would like to use with Android
Studio.

By default, Android Studio provides automatic updates whenever a new stable
version is released, but you can choose to update more frequently and
receive canary or RC versions.

For more information about updating Android Studio and using canary and RC
versions, read about [updates](https://developer.android.com/studio/intro/update).