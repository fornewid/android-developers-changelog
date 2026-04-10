---
title: https://developer.android.com/courses/quizzes/kotlin-multiplatform
url: https://developer.android.com/courses/quizzes/kotlin-multiplatform
source: md.txt
---

# Basics of Kotlin Multiplatform Pathway

# Basics of Kotlin Multiplatform Pathway

<br />

Return to pathway  
1.

   ## What are the key benefits of adopting Kotlin Multiplatform (KMP)?

   Choose as many answers as you see fit.  
   It completely eliminates the need for any platform-specific code.  
   Native performance on each platform.  
   Flexible multiplatform development, allowing choice of what to share and what to write natively.  
   Gradual adoption, starting with small components and incrementally sharing more logic.  
   Reduced code duplication and development time.  
2.

   ## Which statements correctly describe the common approaches for code sharing in KMP?

   Choose as many answers as you see fit.  
   You can share diverse parts of a codebase such as business logic, presentation logic, or even UI logic (with Compose Multiplatform).  
   KMP dictates exactly which parts of your codebase must be shared for optimal performance.  
   Mobile teams commonly start by sharing a discrete set of business logic like data models, database access, network layers, and associated tests.  
3.

   ## What is true about targets and source sets?

   Choose as many answers as you see fit.  
   Targets define the platforms to which Kotlin compiles the common code.  
   A Kotlin source set is a set of source files with its own targets, dependencies, and compiler options. It's the main way to share code in multiplatform projects.  
   The commonMain source set contains code shared among all declared target platforms.  
   Source sets primarily define UI components for each platform.  
4.

   ## Which of the following statements correctly describe how to add and manage dependencies?

   Choose as many answers as you see fit.  
   Add multiplatform dependencies by updating the build.gradle(.kts) file in the shared module with library coordinates.  
   Add multiplatform libraries used across all source sets only to commonMain.  
   The standard library (stdlib) must be manually added to each source set.  
   Platform-specific library dependencies cannot be set directly in commonMain.  
5.

   ## To which Kotlin declarations can the expect and actual mechanism be applied?

   Functions and properties only.  
   Classes and interfaces only.  
   Enumerations and annotations only.  
   Functions, classes, interfaces, enumerations, properties, and annotations.  
6.

   ## Which Gradle task is designed specifically for the Xcode environment to embed and sign the Kotlin framework during direct integration?

   exportKotlinBinaryForXcode  
   embedAndSignAppleFrameworkForXcode  
   buildIosFramework  
   syncKotlinFrameworkForXcode  
7.

   ## Where are you explicitly prevented from setting dependencies on platform-specific libraries in a project targeting Android, iOS, and Desktop?

   androidMain source set  
   iosMain source set  
   jvmMain source set  
   commonMain source set  
8.

   ## When compiling for a target like JVM, which source sets are included?

   Only the platform-specific source set (for example, jvmMain).  
   Only the commonMain source set.  
   All source sets labeled with that target, including commonMain and relevant intermediate source sets.  
   Only source sets that contain platform-specific APIs.  
9.

   ## What is the primary purpose of the commonMain source set?

   To contain Kotlin code that is shared among all declared target platforms.  
   To define platform-specific APIs for Android or iOS.  
   To manage test dependencies for all platforms.  
10.

    ## How are tests organized and executed in a Kotlin Multiplatform project?

    Choose as many answers as you see fit.  
    Each Main source set has a corresponding Test source set for its tests, for example, commonTest and commonMain.  
    The connection between Main and Test source sets is automatically established, allowing tests to use the API of the production code without additional configuration.  
    For platform-specific tests, you can use frameworks like JUnit for Android and JVM, and XCTest for iOS within their respective platform-specific test source sets.  
    All tests, including platform-specific ones, must be written in the commonTest source set to ensure multiplatform compatibility.  

Submit answers

*error_outline*An error occurred when grading the quiz. Please try again.