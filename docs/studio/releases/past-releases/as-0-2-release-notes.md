---
title: https://developer.android.com/studio/releases/past-releases/as-0-2-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-0-2-release-notes
source: md.txt
---

<br />

# Android Studio v0.2.x (July 2013)

- Merged in the latest IntelliJ codebase changes. Includes fixes for issues reported by Studio users such as tweaks to Linux font sizes and font rendering.
- Android Gradle plug-in updated to 0.5.0. **Caution:** This new version is not backwards compatible.
  When opening a project that uses an older version of the plug-in, Studio will show an error
  stating **Gradle \<project_name\> project refresh failed.**

  The updated Gradle plug-in includes the following changes:
  - Fixed IDE model to contain the output file even if it's customized through the DSL. Also fixed the DSL to get/set the output file on the variant object so that it's not necessary to use `variant.packageApplication or variant.zipAlign`
  - Fixed dependency resolution so that we resolved the combination of (default config, build types, flavor(s)) together instead of separately.
  - Fixed dependency for tests of library project to properly include all the dependencies of the library itself.
  - Fixed case where two dependencies have the same leaf name.
  - Fixed issue where Proguard rules file cannot be applied on flavors.

  All Gradle plugin release notes are available are here: <http://tools.android.com/tech-docs/new-build-system>.
- Gradle errors from aapt no longer point to merged output files in the build/ folder, they point back to the real source locations.
- Parallel Builds. It's now possible to use Gradle's parallel builds. Please be aware that parallel builds are in "incubation" (see [Gradle's
  documentation](http://www.gradle.org/docs/current/userguide/gradle_command_line.html).) This feature is off by default. To enable it, go to **Preferences** \> **Compiler** and check the box *Compile
  independent modules in parallel*.
- Further work on the new resource repository used for layout rendering, resource folding in the editor, and more:
  - Basic support for .aar library dependencies (e.g. using a library without a local copy of the sources). Still not working for resource XML validation and navigation in source editors.
  - Cycle detection in resource references.
  - Quick Documentation (F1), which can show all translations of the string under the caret, will now also show all resource overlays from the various Gradle flavors and build types, as well as libraries. They are listed in reverse resource overlay order, with strikethrough on the versions of the string that are masked.
  - Fixes to handle updating the merged resources when the set of module dependencies change.
  - XML rendering fixes to properly handle character entity declarations and XML and unicode escapes.
- Save screenshot support for the layout preview and layout editor windows.
- Template bug fixes.
- Lint bug fixes.
- Various fixes for crash reports. Thank you, and keep filing crash reports!

<br />