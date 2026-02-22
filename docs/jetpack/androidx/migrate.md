---
title: https://developer.android.com/jetpack/androidx/migrate
url: https://developer.android.com/jetpack/androidx/migrate
source: md.txt
---

# Migrate to AndroidX

AndroidX replaces the original support library APIs with packages in the`androidx`namespace. Only the package and Maven artifact names changed; class, method, and field names did not change.
| **Caution:** As of late 2021, most of the library ecosystem already supports AndroidX natively. This means that your project is most likely already using AndroidX libraries directly and there is no need to follow the steps in this migration guide. Additionally, the[`enableJetifier`](https://developer.android.com/jetpack/androidx/migrate#migrate_an_existing_project_using_android_studio)flag mentioned in this guide can lead to slower build times and should not be used unless it's necessary.
|
| If your project already has the`enableJetifier`flag and it's turned on, you can run Build Analyzer's Jetifier check to confirm if it's actually needed. The Build Analyzer check is available starting in[Android Studio Chipmunk](https://developer.android.com/studio/preview/features#jetifier-build-analyzer).

## Prerequisites

Before you migrate, bring your app up to date. We recommend updating your project to use the final version of the support library:[version 28.0.0](https://developer.android.com/topic/libraries/support-library/revisions#28-0-0). This is because AndroidX artifacts with version 1.0.0 are binary equivalent to the Support Library 28.0.0 artifacts.
| **Note:** We recommend working in a separate branch when migrating. Also try to avoid refactoring your code while performing the migration.

## Mappings

If you run into issues because your project hasn't fully migrated to AndroidX, refer to these tables to determine the proper mappings from the support library to the corresponding AndroidX artifacts and classes:

- [Maven artifact mappings](https://developer.android.com/jetpack/androidx/migrate/artifact-mappings)
- [Class mappings](https://developer.android.com/jetpack/androidx/migrate/class-mappings)

For the latest versions of the Jetpack libraries, see the[versions page](https://developer.android.com/jetpack/androidx/versions).

## Additional resources

To learn more about migrating your code to AndroidX, see the following additional resources:

### Blog posts

- [Cross-stitching Plaid and AndroidX](https://medium.com/androiddevelopers/cross-stitching-plaid-and-androidx-7603a192348e)
- [Migrating to AndroidX: Tip, Tricks, and Guidance](https://medium.com/androiddevelopers/migrating-to-androidx-tip-tricks-and-guidance-88d5de238876)

### Videos

- [Migrating to AndroidX: the time is right](https://www.youtube.com/watch?v=Hyt7LR5mXLc)