---
title: https://developer.android.com/ndk/guides/ndk-build
url: https://developer.android.com/ndk/guides/ndk-build
source: md.txt
---

# The ndk-build script

The`ndk-build`script builds projects that use the NDK's Make-based build system. There is more specific documentation for the[Android.mk](https://developer.android.com/ndk/guides/android_mk)and[Application.mk](https://developer.android.com/ndk/guides/application_mk)configuration used by`ndk-build`.

## Internals

Running the`ndk-build`script is equivalent to running the following command:  

```
$GNUMAKE -f <ndk>/build/core/build-local.mk
<parameters>
```

`$GNUMAKE`points to GNU Make 3.81 or later, and`<ndk>`points to your NDK installation directory. You can use this information to invoke ndk-build from other shell scripts, or even your own make files.

## Invoke from the command line

The`ndk-build`script lives in the top level NDK installation directory. To run it from the command line, invoke it while in or under your application project directory. For example:  

```
$ cd <project>
$ <ndk>/ndk-build
```

In this example,`<project>`points to your project's root directory, and`<ndk>`is the directory where you installed the NDK.

### Options

All parameters to ndk-build are passed directly to the underlying GNU`make`command that runs the NDK build scripts. Combine`ndk-build`and options in the form`ndk-build <option>`. For example:  

```
$ ndk-build clean
```

The following options are available:

`clean`

:   Remove any previously generated binaries.**Note:** On Mac OS X, running`ndk-build clean`with a high number of[parallel executions](https://www.gnu.org/software/make/manual/html_node/Parallel.html)may result in a build error that includes the following message:

    ```
    rm: fts_read: No such file or directory
    ```

    To avoid this issue, consider not using the`-j`<var translate="no">N</var>modifier or selecting a smaller value for<var translate="no">N</var>, such as 2.

`V=1`
:   Launch build, and display build commands.

`-B`
:   Force a complete rebuild.

`-B V=1`
:   Force a complete rebuild, and display build commands.

`NDK_LOG=1`
:   Display internal NDK log messages (used for debugging the NDK itself).

`NDK_DEBUG=1`
:   Force a debuggable build (see[table 1](https://developer.android.com/ndk/guides/ndk-build#dvr)).

`NDK_DEBUG=0`
:   Force a release build (see[table 1](https://developer.android.com/ndk/guides/ndk-build#dvr)).

`NDK_HOST_32BIT=1`
:   Always use the toolchain in 32-bit mode.

`NDK_APPLICATION_MK=<file>`
:   Build, using a specific`Application.mk`file pointed to by the`NDK_APPLICATION_MK`variable.

`-C <project>`
:   Build the native code for the project path located at`<project>`. Useful if you don't want to`cd`to it in your terminal.

### Debuggable versus release builds

Use the`NDK_DEBUG`option and, in certain cases,`AndroidManifest.xml`to specify debug or release build, optimization-related behavior, and inclusion of symbols. Table 1 shows the results of each possible combination of settings.

**Table 1.** Results of`NDK_DEBUG`(command line) and`android:debuggable`(manifest) combinations.

|      Manifest Setting      |         NDK_DEBUG=0          |           NDK_DEBUG=1            |      NDK_DEBUG not specified      |
|----------------------------|------------------------------|----------------------------------|-----------------------------------|
| android:debuggable="true"  | Debug; Symbols; Optimized\*1 | Debug; Symbols; Not optimized\*2 | (same as NDK_DEBUG=1)             |
| android:debuggable="false" | Release; Symbols; Optimized  | Release; Symbols; Not optimized  | Release; No symbols; Optimized\*3 |

\*1: Useful for profiling.  
\*2: Default for running[`ndk-gdb`](https://developer.android.com/ndk/guides/ndk-gdb).  
\*3: Default mode.  

**Note:** \`NDK_DEBUG=0\` is the equivalent of \`APP_OPTIM=release\`, and compiles with \`-O2\`. \`NDK_DEBUG=1\` is the equivalent of \`APP_OPTIM=debug\` in \`Application.mk\`, and compiles with \`-O0\`. For more information about \`APP_OPTIM\`, see[Application.mk](https://developer.android.com/ndk/guides/application_mk).

The syntax on the command line is, for example:  

```
$ ndk-build NDK_DEBUG=1
```

## Requirements

You need GNU Make 4 to use ndk-build or the NDK in general. The NDK includes its own copy of GNU Make and will use that unless you've set the`$GNUMAKE`environment variable to point to an unsuitable make.

## JSON compilation databases

In NDK r18 and newer, ndk-build can generate a[JSON compilation database](https://clang.llvm.org/docs/JSONCompilationDatabase.html).

You can either use`ndk-build compile_commands.json`to generate the database without building your code, or`ndk-build GEN_COMPILE_COMMANDS_DB=true`if you want to build and generate the database as a side-effect.