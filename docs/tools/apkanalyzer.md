---
title: apkanalyzer  |  Android Studio  |  Android Developers
url: https://developer.android.com/tools/apkanalyzer
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [SDK tools guides](https://developer.android.com/tools)

# apkanalyzer Stay organized with collections Save and categorize content based on your preferences.



The command-line version of APK Analyzer provides immediate insight into the
composition of your APK after the build process completes and lets you
compare differences between two APKs. Using APK Analyzer reduces the
time you spend debugging issues with DEX files and resources within your app and
reduces the size of your APK.

`apkanalyzer` is included in the
[Android SDK Command-Line Tools](/studio/command-line#tools-sdk) package at
`android_sdk/cmdline-tools/version/bin/apkanalyzer`.
Alternatively, you can access the APK Analyzer tool within
Android Studio as described in
[Analyze your build with APK Analyzer](/studio/debug/apk-analyzer).

## Syntax

The syntax for `apkanalyzer` is:

```
apkanalyzer [global-options] subject verb [options] apk-file [apk-file2]
```

The `subject` is what you want to query and can be the entire APK
or a part of the APK. A subject can be any of the following:

* `apk`: Analyze APK file attributes such as application ID, version code,
  and version name.
* `files`: Analyze the files inside the APK file.
* `manifest`: Analyze the contents of the manifest inside the APK file.
* `dex`: Analyze the DEX files inside the APK file.
* `resources`: View text, image, and string resources.

The `verb` is what you want to know about the subject. The subjects,
verbs, and their options are described in the following section about [commands](#commands).

Every command requires that you specify an APK file. Only the
`apk compare` command requires that you specify a second APK.

You can shorten every option as long as the option is unambiguous. For example,
the `--human-readable` global option can be shortened to
`-h`.

The following example analyzes the `apk` (subject)
to get its `file-size` (verb), and then prints the file size in a
human-readable format (`-h` option):

```
apkanalyzer -h apk file-size myapk.apk
```

## Commands

The following command descriptions are organized by subject and list the
available verb and option combinations for each subject:

| View APK file attributes | Description |
| --- | --- |
| `apk summary apk-file` | Prints the application ID, version code, and version name. |

Example output:

```
com.myapp 5 1.1-beta
```

| `apk file-size apk-file` | Prints the total file size of the APK. |
| `apk download-size apk-file` | Prints an estimate of the download size of the APK. |
| `apk features [--not-required] apk-file` | Prints features used by the APK that trigger [Play Store filtering](/google/play/filters#manifest-filters). Add the `--not-required` option to include features marked as not required in the output. |

Example output:

```
android.hardware.type.watch
android.hardware.microphone implied:
    requested android.permission.RECORD_AUDIO permission
```

| `apk compare [options] apk-file apk-file2` | Compares the sizes of `apk-file` and `apk-file2`. You can include the following options:  * `--different-only`: Prints directories and files with   differences. * `--files-only`: Does not print directory entries. * `--patch-size`: Shows an estimate of the file-by-file patch   instead of a raw difference. |

Example output (old size / new size / size difference / path):

```
39086736 48855615 9768879 /
10678448 11039232 360784 /classes.dex
18968956 18968956 0 /lib/
110576 110100 -476 /AndroidManifest.xml
...
```

| View the APK file system | Description |
| `files list apk-file` | Lists all files in the APK. |

Example output:

```
/
/classes2.dex
/classes.dex
/assets/
/assets/asset.data
/AndroidManifest.xml
/resources.arsc
/res/
...
```

| `files cat --file path apk-file` | Prints out the file contents. You must specify a path inside the APK using the `--file path` option, such as `--file /AndroidManifest.xml` |
| View information in the manifest | Description |
| `manifest print apk-file` | Prints the APK manifest in XML format. |
| `manifest application-id apk-file` | Prints the application ID value. |
| `manifest version-name apk-file` | Prints the version name value. |
| `manifest version-code apk-file` | Prints the version code value. |
| `manifest min-sdk apk-file` Prints the minimum SDK version. | |
| `manifest target-sdk apk-file` | Prints the target SDK version. |
| `manifest permissions apk-file` | Prints the list of permissions. |
| `manifest debuggable apk-file` | Prints whether the app is debuggable. |
| Access DEX file information | Description |
| `dex list apk-file` | Prints a list of the DEX files in the APK. |
| `dex references [--files path] [--files path2] apk-file` | Prints the number of method references in the specified DEX files. The default is all DEX files. Add the `--files` option to indicate specific files that you want to include. |

Example output:

```
classes.dex 59598
classes2.dex 8042
```

| `dex packages [option1 option2 ...] apk-file` | Prints the class tree from DEX. In the output, `P`, `C`, `M`, and `F` indicate packages, classes, methods, and fields, respectively. And `x`, `k`, `r`, and `d` indicate removed, kept, referenced and defined nodes, respectively. |

Add the following options to refine the output:

* `--defined-only`: Includes only classes defined in the APK in the output.
* `--files`: Specifies the DEX file names to include. Default: all DEX files.
* `--proguard-folder file`: Specifies the Proguard output folder to search for mappings.
* `--proguard-mappings file`: Specifies the Proguard mappings file.
* `--proguard-seeds file`: Specifies the Proguard seeds file.
* `--proguard-usages file`: Specifies the Proguard usages file.
* `--show-removed`: Shows classes and members that were removed by Proguard.

Example output (type/state/defined methods/referenced methods
/byte size/name):

```
P d 1 1 85 g
P d 1 1 85 g.a
C d 1 1 85 g.a.a
M d 1 1 45 g.a.a java.lang.Object get()
C r 0 1 40 byte[]
M r 0 1 40 byte[] java.lang.Object clone()
```

| `dex code --class class [--method method]` | Prints the bytecode of a class or method in smali format. The class name is required and prints the fully qualified class name to decompile. Add the `--method` option to specify the method to decompile. |

The format
for the method decompile is `name(params)returnType`, for example,
`someMethod(Ljava/lang/String;I)V`.| View resources stored in res/ and resources.arsc | Description |
| `resources packages` | Prints a list of the packages that are defined in the resources table. |
| `resources configs --type type [--package package] apk-file` | Prints a list of configurations for the specified `type`. The `type` is a resource type such as `string`. Include the `--package` option if you want to specify the resource table package name, otherwise the first defined package will be used. |
 `resources value --config config --name name --type type [--package package] apk-file` | Prints the value of the resource specified by `config`, `name`, and `type`. The `type` option is the type of the resource, such as `string`. |

Include the `--package`
option if you want to specify the resource table package name, otherwise
the first defined package will be used.| `resources names --config config --type type [--package package] apk-file` | Prints a list of resource names for a configuration and type. The `type` option is the type of the resource, such as `string`. Include the `--package` option if you want to specify the resource table package name, otherwise the first defined package will be used. |
| `resources xml --file path apk-file` | Prints the human-readable form of a binary XML file. Include the `file` option to specify the path to the file. |