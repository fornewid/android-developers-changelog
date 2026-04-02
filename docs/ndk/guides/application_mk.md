---
title: Application.mk  |  Android NDK  |  Android Developers
url: https://developer.android.com/ndk/guides/application_mk
source: html-scrape
---

* [Home](https://developer.android.com/)
* [NDK](https://developer.android.com/ndk)
* [Develop](https://developer.android.com/develop)
* [Guides](https://developer.android.com/ndk/guides)

# Application.mk Stay organized with collections Save and categorize content based on your preferences.




This document explains the `Application.mk` build file used by `ndk-build`.

We recommend that you read the [Concepts](/ndk/guides/concepts) page before this
one.

## Overview

The `Application.mk` specifies project-wide settings for ndk-build. By default,
it is located at `jni/Application.mk`, in your application's project directory.

**Note:** Many of these parameters also have a per-module equivalent. For example,
`APP_CFLAGS` corresponds to `LOCAL_CFLAGS`. In every case, the module-specific
option will take precedence over the application-wide option. For flags, both
are used but the module-specific flags will appear later in the command line so
they may override project-wide settings.

## Variables

### APP\_ABI

By default, the NDK build system generates code for all non-deprecated ABIs. You
can use the `APP_ABI` setting to generate code for specific ABIs. Table 1 shows
the `APP_ABI` settings for different instruction sets.

**Table 1.** `APP_ABI` settings for different instruction sets.

| Instruction set | Value |
| --- | --- |
| 32-bit ARMv7 | `APP_ABI := armeabi-v7a` |
| 64-bit ARMv8 (AArch64) | `APP_ABI := arm64-v8a` |
| x86 | `APP_ABI := x86` |
| x86-64 | `APP_ABI := x86_64` |
| All supported ABIs (default) | `APP_ABI := all` |

You can also specify multiple values by placing them on the same line, delimited
by spaces. For example:

```
APP_ABI := armeabi-v7a arm64-v8a x86
```

**Note:** `APP_ABI` is ignored by Gradle's `externalNativeBuild`. Instead, use an
`abiFilters` block or (if you are using "Multiple APKs") an `abi` block inside a
`splits` block.

For the list of all supported ABIs and details about their usage and
limitations, refer to [Android ABIs](/ndk/guides/abis).

### APP\_ASFLAGS

Flags to be passed to the assembler for every assembly source file (`.s` and
`.S` files) in the project.

**Note:** `ASFLAGS` are distinct from `ASMFLAGS`. The latter applies specifically to
YASM source files (see the section on [APP\_ASMFLAGS](#app_asmflags)).

### APP\_ASMFLAGS

Flags to be passed to YASM when for all YASM source files (`.asm`, x86/x86\_64
only).

### APP\_BUILD\_SCRIPT

By default, ndk-build assumes that the [Android.mk](/ndk/guides/android_mk) file is located at
`jni/Android.mk` relative to the project root.

To load an [Android.mk](/ndk/guides/android_mk) file from a different location, set `APP_BUILD_SCRIPT`
to the absolute path of the Android.mk file.

**Note:** Gradle's `externalNativeBuild` will configure this automatically based on
the `externalNativeBuild.ndkBuild.path` variable.

### APP\_CFLAGS

Flags to be passed for all C/C++ compiles in the project.

**Note:** Include paths should use `LOCAL_C_INCLUDES` rather than explicit `-I`
flags.

See also: [APP\_CONLYFLAGS](#app_conlyflags), [APP\_CPPFLAGS](#app_cppflags).

### APP\_CLANG\_TIDY

Set to true to enable clang-tidy for all modules in the project. Disabled by
default.

### APP\_CLANG\_TIDY\_FLAGS

Flags to pass for all clang-tidy executions in the project.

### APP\_CONLYFLAGS

Flags to be passed for all C compiles in the project. These flags will not be
used for C++ code.

See also: [APP\_CFLAGS](#app_cflags), [APP\_CPPFLAGS](#app_cppflags).

### APP\_CPPFLAGS

Flags to be passed for all C++ compiles in the project. These flags will not be
used for C code.

See also: [APP\_CFLAGS](#app_cflags), [APP\_CONLYFLAGS](#app_conlyflags).

### APP\_CXXFLAGS

**Note:** [APP\_CPPFLAGS](#app_cppflags) should be preferred to `APP_CXXFLAGS`.

Identical to `APP_CPPFLAGS`, but will appear after `APP_CPPFLAGS` in the compile
command. For example:

```
APP_CPPFLAGS := -DFOO
APP_CXXFLAGS := -DBAR
```

The above configuration will result in a compilation command similar to `clang++
-DFOO -DBAR` rather than `clang++ -DBAR -DFOO`.

### APP\_DEBUG

Set to true to build a debuggable application.

### APP\_LDFLAGS

Flags to be passed when linking executables and shared libraries.

**Note:** These flags have no effect on static libraries. Static libraries are not
linked.

### APP\_MANIFEST

Absolute path to an AndroidManifest.xml file.

By default, `$(APP_PROJECT_PATH)/AndroidManifest.xml)` will be used if it
exists.

**Note:** When using `externalNativeBuild` this value will not be set by Gradle.

### APP\_MODULES

An explicit list of modules to build. The elements of this list are the names of
the modules as they appear in `LOCAL_MODULE` within the [Android.mk](/ndk/guides/android_mk) file.

By default, ndk-build will build all shared libraries, executables, and their
dependencies. Static libraries will be built only if they are used by the
project, the project contains *only* static libraries, or if they are named in
`APP_MODULES`.

**Note:** Imported modules (those defined in build scripts imported with `$(call
import-module)` will not be built unless depended on by a module to be built or
listed in `APP_MODULES`.

### APP\_OPTIM

Define this optional variable as either `release` or `debug`. Release binaries
will be built by default.

Release mode enables optimizations and may produce binaries that are not usable
with a debugger. Debug mode disables optimizations so that debuggers may be
used.

Note that you can debug either release or debug binaries. Release binaries,
however, provide less information during debugging. For example, variables may
be optimized out, preventing inspection. Also, code re-ordering can make it more
difficult to step through the code; stack traces may not be reliable.

Declaring `android:debuggable` in your application manifest's `<application>`
tag will cause this variable to default to `debug` instead of `release`.
Override this default value by setting `APP_OPTIM` to `release`.

**Note:** When building with `externalNativeBuild`, Android Studio will set this
flag appropriately based on your build flavor.

### APP\_PLATFORM

`APP_PLATFORM` declares the Android API level this application is built against
and corresponds to the application's `minSdkVersion`.

If not specified, ndk-build will target the minimum API level supported by the
NDK. The minimum API level supported by the latest NDK will always be low enough
to support nearly all active devices.

**Warning:** Setting `APP_PLATFORM` higher than an application's `minSdkVersion`
will likely produce an application that will not run on older devices. In most
cases the libraries will fail to load because they refer to symbols that are not
available on older devices.

For example, a value of `android-16` specifies that your library uses APIs that
are not available below Android 4.1 (API level 16) and can't be used on devices
running a lower platform version. For a complete list of platform names and
corresponding Android system images, see [Android NDK native
APIs](/ndk/guides/stable_apis).

When using Gradle and `externalNativeBuild`, this parameter should not be set
directly. Instead, set the `minSdkVersion` property in the `defaultConfig` or
`productFlavors` blocks of your
[module-level](/studio/build#module-level) `build.gradle` file. This
makes sure your library is used only by apps installed on devices running an
adequate version of Android.

Note that the NDK does not contain libraries for every API level of Android.
Versions that did not include new native APIs are omitted to save space in the
NDK. ndk-build uses, in descending order of preference:

1. The platform version matching `APP_PLATFORM`.
2. The next available API level below `APP_PLATFORM`. For example, `android-19`
   will be used when `APP_PLATFORM` is `android-20`, since there were no new
   native APIs in android-20.
3. The minimum API level supported by the NDK.

### APP\_PROJECT\_PATH

The absolute path of the project's root directory.

### APP\_SHORT\_COMMANDS

The project-wide equivalent of `LOCAL_SHORT_COMMANDS`. For more information, see
the documentation for `LOCAL_SHORT_COMMANDS` in [Android.mk](/ndk/guides/android_mk).

### APP\_STL

The C++ standard library to use for this application.

The `system` STL is used by default. Other choices are `c++_shared`,
`c++_static`, and `none`. See [NDK C++ Runtimes and
Features](/ndk/guides/cpp-support#c_runtime_libraries).

### APP\_STRIP\_MODE

The argument to be passed to `strip` for modules in this application. Defaults
to `--strip-unneeded`. To avoid stripping all binaries in the module, set to
`none`. For other strip modes, see the [strip
documentation](https://sourceware.org/binutils/docs/binutils/strip.html).

### APP\_THIN\_ARCHIVE

Set to true to use thin archives for all static libraries in the project. For
more information, see the documentation for `LOCAL_THIN_ARCHIVE` in
[Android.mk](/ndk/guides/android_mk).

### APP\_WRAP\_SH

Path to the [wrap.sh](/ndk/guides/wrap-script) file to be included with this application.

A variant of this variable exists for each ABI, as does an ABI-generic variant:

* `APP_WRAP_SH`
* `APP_WRAP_SH_armeabi-v7a`
* `APP_WRAP_SH_arm64-v8a`
* `APP_WRAP_SH_x86`
* `APP_WRAP_SH_x86_64`

**Note:** `APP_WRAP_SH_<abi>` may not be combined with `APP_WRAP_SH`. If any ABI
uses an ABI-specific wrap.sh, all ABIs must.