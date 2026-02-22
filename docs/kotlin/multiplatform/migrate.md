---
title: https://developer.android.com/kotlin/multiplatform/migrate
url: https://developer.android.com/kotlin/multiplatform/migrate
source: md.txt
---

# Add Kotlin Multiplatform to an existing project

To create a Kotlin Multiplatform (KMP) module within your Android project, use the**Kotlin Multiplatform Shared Module** template, available in Android Studio Meerkat and Android Gradle Plugin[version 8.8.0](https://maven.google.com/web/index.html?q=build#com.android.tools.build:gradle)and higher.

The module template automates the creation of a new module with the minimum configuration targeting Android and iOS platforms.
| **Note:** If you want to build an iOS app, you need a macOS machine with[Xcode installed](https://developer.apple.com/documentation/safari-developer-tools/installing-xcode-and-simulators). You also need to install an iOS simulator, or have an iPhone[prepared for developing](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device#Connect-real-devices-to-your-Mac), to run the app.

## Set up the shared KMP module

To create a shared KMP module, follow these steps:

1. Select**File \> New \> New Module**
2. Select the**Kotlin Multiplatform Shared Module** template in the**Templates**panel:

![Creating a new KMP Module](https://developer.android.com/static/kotlin/images/kmp_new_module.png)**Figure 1.**Creating a new KMP Module

The fields in the template are the following:

- **Module name**-- defines the Gradle module name, as well as the iOS framework name (can be changed later)
- **Package name** -- defines the package name for files in this module
  1. Click**Finish**and allow Gradle to sync with the project. You might also be prompted to add the newly created module files to source control.

| **Note:** The generated module includes some basic placeholder functions and tests. These placeholder functions ensure that the module compiles and runs successfully..

Once complete, the Android Studio**Project View**shows the new shared module along with a sourceset for each platform.
![Project view showing new shared modules](https://developer.android.com/static/kotlin/images/kmp_project_structure.png)**Figure 2.**Project view showing new shared modules

<br />

## Link the shared module to the Android app

The module wizard doesn't add the newly created module as a dependency to any existing module. As a next step, you need to link the shared module to one of your existing Gradle modules similarly to other Android dependencies  

    dependencies {
        ...
        implementation(project(":shared"))
    }

| **Note:** If your project enabled Gradle's[Type-safe project accessors](https://docs.gradle.org/current/userguide/declaring_dependencies_basics.html#sec:type-safe-project-accessors)feature, you can access the shared module with projects.shared.

Once enabled, you can access code as usual. From the Android app, you're able to access code that is available either in androidMain or in commonMain.

For more information on Kotlin Multiplatform project structure, see the[basics of Kotlin Multiplatform project structure](https://kotlinlang.org/docs/multiplatform-discover-project.html)

## Set up the shared module to the iOS app

Swift can't use Kotlin modules directly and requires a compiled binary framework to be produced.
| **Note:** Kotlin Gradle Plugin also supports[Swift Package Manager integration](https://kotlinlang.org/docs/native-spm.html)or[Cocoapods integration](https://kotlinlang.org/docs/native-cocoapods.html)to share and consume the common code built for Kotlin \& Native (iOS).

The new module template in Android Studio configures the shared module to produce a framework for each of the iOS architectures. You can find the following code in the shared module's`build.gradle.kts`file:  

    val xcfName = "sharedKit"

    iosX64 {
      binaries.framework {
        baseName = xcfName
      }
    }

    iosArm64 {
      binaries.framework {
        baseName = xcfName
      }
    }

    iosSimulatorArm64 {
      binaries.framework {
        baseName = xcfName
      }
    }

See[Hierarchical project structure](https://kotlinlang.org/docs/multiplatform-hierarchy.html)for information on defining other architecture types.
| **Note:** The output framework is called sharedKit by default, as defined in the shared module's`build.gradle.kts`file. In your own project, you can rename it as needed controlling the`xcfName`variable.

## Link the shared library in the iOS project

To enable access to the shared code from the iOS project, add a script phase to generate the Kotlin framework before compiling the Swift sources:
| **Note:** You can also open the Xcode project by double-clicking the**xcodeproj**file in Finder.

1. Right-click the file in the Android Studio and select**Open In** and**Open in Associated Application**. This will open the iOS app in Xcode.

![Open in Associated Application](https://developer.android.com/static/kotlin/images/kmp_open_in.png)**Figure 3.**Open in Associated Application

1. Open the project settings by double-clicking the project name in the project navigator

![Xcode project settings dialog](https://developer.android.com/static/kotlin/images/kmp_xcode_1.png)**Figure 4.**Xcode project settings dialog

1. Change the default**Run Script** name to***Compile Kotlin Framework*** to better identify what this phase does. Double-click the*Run Script*title to edit it.
2. Expand the build phase, and in the**Shell**text field, enter the following script code:

![Adding a new run script build phase](https://developer.android.com/static/kotlin/images/kmp_xcode_runscript.png)**Figure 5.**Run script build phase**Note:** `cd "$SRCROOT/.."`navigates the script to the root folder of the KMP Gradle project, which in this case is a parent folder. If in your case the iOS project is on a different path, you need to tweak that here.

1. Drag the**Run Script** phase before the**Compile Sources**phase.

   ![Run script build phase before compile sources](https://developer.android.com/static/kotlin/images/kmp_xcode_runscript2.png)**Figure 6.**Run script build phase before compile sources

   <br />

2. Build the project in Xcode by clicking**⌘B** or navigating to the**Product** menu and selecting**Build**.

When the build succeeds, you'll see the following icon.
![Build successful shown in Xcode](https://developer.android.com/static/kotlin/images/kmp_xcode_success.png)**Figure 7.**Build successful

## Access the shared code in the iOS app

To verify that the iOS app can successfully access code from the shared module, do the following:

1. In the iOS project, open the`ContentView.swift`file at:`Sources/View/ContentView.swift`
2. Add import`sharedKit`at the top of the file.
3. Modify the Text view to include the`Platform_iosKt.platform()`information in the displayed string as follows:

| **Note:** The string interpolation in Swift uses (code) syntax.

This update checks whether the app can call the`platform()`function from the shared module, which should return "iOS" when running on the iOS platform.
![Xcode simulator running the iOS app](https://developer.android.com/static/kotlin/images/kmp_xcode_simulator.png)**Figure 8.**Xcode simulator running the iOS app

## Additional Resources

- If you're new to KMP development, see the[official KMP documentation](https://kotlinlang.org/docs/multiplatform.html)for more guides.
- If you're new to iOS development, see[Swift Basics documentation](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/).
- For common KMP setup issues, see[Possible issues and solutions](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-setup.html#possible-issues-and-solutions).
- For sample apps, see[Android Kotlin Multiplatform Samples](https://github.com/android/kotlin-multiplatform-samples).