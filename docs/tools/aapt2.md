---
title: https://developer.android.com/tools/aapt2
url: https://developer.android.com/tools/aapt2
source: md.txt
---

# AAPT2 (Android Asset Packaging Tool) is a build tool that Android Studio and Android Gradle Plugin use to compile and package your app's[resources](https://developer.android.com/guide/topics/resources/providing-resources). AAPT2 parses, indexes, and compiles the resources into a binary format that is optimized for the Android platform.

Android Gradle Plugin 3.0.0 and higher enables AAPT2 by default. You typically don't need to invoke`aapt2`yourself. However, if you prefer to use your terminal and your own build system instead of Android Studio, you can use AAPT2 from the command line. You can also debug build errors related to AAPT2 from the command line. To do so, find AAPT2 as a standalone tool in[Android SDK Build Tools](https://developer.android.com/studio/releases/build-tools)26.0.2 and higher.

To download Android SDK Build Tools from the command line, use[`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager)and run the following command:  

```
sdkmanager "build-tools;build-tools-version"
```

Once you have downloaded the SDK Build Tools, find AAPT2 in<var translate="no">android_sdk</var>`/build-tools/`<var translate="no">version</var>`/`.

Because revisions of the Android SDK Build Tools aren't released often, the version of AAPT2 included in your SDK Build Tools might not be the latest. To get the latest version of AAPT2,[download AAPT2 from Google Maven](https://developer.android.com/tools/aapt2#download_aapt2).

To use AAPT2 from the command line on Linux or Mac, run the`aapt2`command. On Windows, run the`aapt2.exe`command.

AAPT2 supports faster compilation of resources by enabling incremental compilation. To accomplish incremental compilation, resource processing is separated into two steps:

- [Compile](https://developer.android.com/tools/aapt2#compile): compiles resource files into binary formats.
- [Link](https://developer.android.com/tools/aapt2#link): merges all compiled files and packages them to a single package.

This separation helps improve performance for incremental builds. For example, if there are changes in a single file, you need to recompile only that file.

## Download AAPT2 from Google Maven

To get the newest version of AAPT2 that's not bundled in the build tools, download AAPT2 from Google's Maven repository as follows:

1. In the[repository index](https://maven.google.com/), navigate to**com.android.tools.build \> aapt2**.
2. Copy the name of the latest version of AAPT2.
3. Insert the version name you copied into the following URL and specify your target operating system: https://dl.google.com/dl/android/maven2/com/android/tools/build/aapt2/<var translate="no">aapt2-version</var>/aapt2-<var translate="no">aapt2-version</var>-<var translate="no">[windows | linux | osx]</var>.jar

   For example, to download version 3.2.0-alpha18-4804415 for Windows, use: https://dl.google.com/dl/android/maven2/com/android/tools/build/aapt2/**3.2.0-alpha18-4804415** /aapt2-**3.2.0-alpha18-4804415** -**windows**.jar
4. Navigate to the URL in a browser. AAPT2 will begin downloading shortly.

5. Unpackage the JAR file you just downloaded.

   The JAR file should contain an`aapt2`executable and some libraries that the executable depends on.

## Compile

AAPT2 supports compilation of all[Android resource types](https://developer.android.com/guide/topics/resources/available-resources), such as drawables and XML files. When you invoke AAPT2 for compilation, pass a single resource file as an input per invocation. AAPT2 then parses the file and generates an intermediate binary file with a`.flat`extension.

When passing whole directories, AAPT2 recompiles all files in the directory even when only one resource has changed. Although you can pass resource directories containing more than one resource file to AAPT2 using the`--dir`flag, you don't gain the benefits of incremental resource compilation this way.

The output file types can differ based on the input you provide for compilation, as shown in the following table:

**Table 1.**The input and output file types for compilation

|                                                                                                             Input                                                                                                              |                                                                                                                                                Output                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XML resource files, such as[String](https://developer.android.com/guide/topics/resources/string-resource)and[Style](https://developer.android.com/guide/topics/resources/style-resource), located in the`res/values/`directory | Resource table with`*.arsc.flat`as its extension.                                                                                                                                                                                                                                                    |
| All other resource files.                                                                                                                                                                                                      | All files other than the files under`res/values/`directory are converted to binary XML files with`*.flat`extensions. Additionally all PNG files are crunched by default and adopt`*.png.flat `extensions. If you choose not to compress PNGs, you can use the`--no-crunch`option during compilation. |

The files AAPT2 outputs are not executables, and you must later include these binary files as input in the link phase to generate an APK. However, the generated APK file is not an executable that you can deploy on an Android device right away, because it does not contain DEX files and is not signed.

### Compile syntax

The general syntax for using`compile`is as follows:  

```
aapt2 compile path-to-input-files [options] -o output-directory/
```

<br />

| **Note:** For resource files, the path to input files must match the following structure:<var translate="no">path</var>/<var translate="no">resource-type[-config]</var>/<var translate="no">file</var>

In the following example, AAPT2 compiles resource files named`values.xml`and`myImage.png`individually:  

```
aapt2 compile project_root/module_root/src/main/res/values-en/strings.xml -o compiled/
aapt2 compile project_root/module_root/src/main/res/drawable/myImage.png -o compiled/
```

As shown in table 1, the name of the output file depends on the input filename and the name of its parent directory.

For the preceding example with`strings.xml`file as the input,`aapt2`automatically names the output file as`values-en_strings.arsc.flat`. However, the compiled drawable file stored in the drawable directory is named`drawable_img.png.flat`.

### Compile options

There are several options that you can use with the`compile`command, as shown in table 2:

**Table 2.**Compile command options

|                                                           Option                                                            |                                                                                                                                                           Description                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-o `<var translate="no">path</var>                                                                                         | Specifies the output path for the compiled resource(s). This is a**required**flag, because you must specify a path to a directory where AAPT2 can output and store the compiled resources.                                                                                                                                      |
| `--dir `<var translate="no">directory</var>                                                                                 | Specifies the directory to scan for resources. Although you can use this flag to compile multiple resource files with one command, it disables the benefits of incremental compilation. Therefore, this flag shouldn't be used for large projects.                                                                              |
| `--pseudo-localize`                                                                                                         | Generates[pseudolocalized](https://developer.android.com/guide/topics/resources/pseudolocales)versions of default strings, such as`en-XA`and`en-XB`.                                                                                                                                                                            |
| `--no-crunch`                                                                                                               | Disables PNG processing. <br /> Use this option if you have already processed the PNG files or if you are creating debug builds that don't require file size reduction. Enabling this option results in faster execution but increases the output file size.                                                                    |
| `--legacy`                                                                                                                  | Treats errors that are permissible when using earlier versions of AAPT as warnings. <br /> This flag should be used for unexpected compile-time errors. To resolve known behavior changes that might occur while using AAPT2, read[Behavior changes when using AAPT2](https://developer.android.com/tools/aapt2#aapt2_changes). |
| `-zip `<var translate="no">file</var>                                                                                       | <var translate="no">file</var>is a ZIP file containing the`res`directory to scan for resources.                                                                                                                                                                                                                                 |
| `-output-text-symbols `<var translate="no">file</var>                                                                       | Generates a text file containing the resource symbols in the specifiedfile.                                                                                                                                                                                                                                                     |
| `-preserve-visibility-of-styleables`                                                                                        | If specified, applies the same visibility rules for styleables that are used for all other resources. Otherwise, all styleables are made public.                                                                                                                                                                                |
| `-visibility [`<var translate="no">public</var>`|`<var translate="no">private</var>`|`<var translate="no">default</var>`|]` | Sets the visibility of the compiled resources to the specified level.                                                                                                                                                                                                                                                           |
| `-trace-folder `<var translate="no">folder</var>                                                                            | Generates a`systrace`JSON trace fragment to the specifiedfolder.                                                                                                                                                                                                                                                                |
| `-source-path `<var translate="no">path</var>                                                                               | Sets the compiled resource file's source file path topath.                                                                                                                                                                                                                                                                      |
| `-h`                                                                                                                        | Displays the tools help.                                                                                                                                                                                                                                                                                                        |
| `-v`                                                                                                                        | Enables verbose logging.                                                                                                                                                                                                                                                                                                        |

## Link

In the link phase, AAPT2 merges all the intermediate files that the compilation phase generates, such as resource tables, binary XML files, and processed PNG files, and then packages the files into a single APK. Additionally, other auxiliary files, such as`R.java`and ProGuard rules files, can be generated during this phase. However, the generated APK does not contain DEX bytecode and is unsigned. You can't deploy this APK to a device.

If you're not using the Android Gradle plugin to[build your app from the command line](https://developer.android.com/studio/build/building-cmdline), you can use other command-line tools, such as[d8](https://developer.android.com/studio/command-line/d8)to compile Java bytecode into DEX bytecode and[apksigner](https://developer.android.com/studio/command-line/apksigner)to sign your APK.

### Link syntax

The general syntax for using`link`is as follows:  

```
aapt2 link path-to-input-files [options] -o
outputdirectory/outputfilename.apk --manifest AndroidManifest.xml
```

In the following example, AAPT2 merges two intermediate files,`drawable_Image.flat`and`values_values.arsc.flat`, and the`AndroidManifest.xml`file. AAPT2 links the result against the`android.jar`file, which holds the resources defined in the`android`package:  

```
 aapt2 link -o output.apk
 -I android_sdk/platforms/android_version/android.jar
    compiled/res/values_values.arsc.flat
    compiled/res/drawable_Image.flat --manifest /path/to/AndroidManifest.xml -v
```

### Link options

You can use the following options with the`link`command:

**Table 3.**Link command options

|                                               Option                                                |                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-o `<var translate="no">path</var>                                                                 | Specifies the output path for the linked resource APK. This is a**required**flag, because you must specify the path for the output APK that can hold the linked resources.                                                                                                                                                                                                                                                                                                      |
| `--manifest `<var translate="no">file</var>                                                         | Specifies the path to the Android manifest file to build. This is a**required**flag, because the manifest file encloses essential information about your app, like package name and application ID.                                                                                                                                                                                                                                                                             |
| `-I`                                                                                                | Provides the path to the platform's`android.jar`or other APKs, like`framework-res.apk`, which might be useful while building features. This flag is**required** if you are using attributes with the`android`namespace in your resource files.                                                                                                                                                                                                                                  |
| `-A `<var translate="no">directory</var>                                                            | Specifies an assets directory to be included in the APK. <br /> You can use this directory to store original, unprocessed files. To learn more, read[Accessing original files](https://developer.android.com/guide/topics/resources/providing-resources#OriginalFiles).                                                                                                                                                                                                         |
| `-R `<var translate="no">file</var>` `                                                              | Passes an individual`.flat`file to`link`, using`overlay`semantics without using the`<add-resource>`tag. <br /> When you a provide a resource file that overlays an existing file, the last conflicting resource given is used.                                                                                                                                                                                                                                                  |
| `--package-id `<var translate="no">package-id</var>                                                 | Specifies the package ID to use for your app. <br /> The package ID you specify must be greater than or equal to 0x7f unless used in combination with`--allow-reserved-package-id`.                                                                                                                                                                                                                                                                                             |
| `--allow-reserved-package-id`                                                                       | Allows the use of a reserved package ID. Reserved package IDs are IDs that are normally assigned to shared libraries and in the range from 0x02 to 0x7e, inclusive. By using`--allow-reserved-package-id`, you can assign IDs that fall in the range of reserved package IDs. This option should only be used for packages with a`min-sdk`version of 26 or lower.                                                                                                               |
| `--java `<var translate="no">directory</var>                                                        | Specifies the directory to generate`R.java`in.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--proguard `<var translate="no">proguard_options</var>                                             | Generates the output file for ProGuard rules.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--proguard-conditional-keep-rules`                                                                 | Generates the output file for ProGuard rules for the main DEX.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--no-auto-version`                                                                                 | Disables automatic style and layout SDK versioning.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--no-version-vectors`                                                                              | Disables automatic versioning of vector drawables. Use this flag only when building your APK with the Vector Drawable Library.                                                                                                                                                                                                                                                                                                                                                  |
| `--no-version-transitions`                                                                          | Disables automatic versioning of transition resources. Use this flag only when building your APK with the Transition Support library.                                                                                                                                                                                                                                                                                                                                           |
| `--no-resource-deduping`                                                                            | Disables automatic de-duplication of resources with identical values across compatible configurations.                                                                                                                                                                                                                                                                                                                                                                          |
| `--enable-sparse-encoding`                                                                          | Enables sparse encoding of resource entries. This leads to a reduction in APK size, memory usage, and startup latency, and a small increase in individual resource lookup time after startup.                                                                                                                                                                                                                                                                                   |
| `-z`                                                                                                | Requires localization of strings marked 'suggested'.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `-c `<var translate="no">config</var>                                                               | Provides a comma-separated list of configurations. <br /> For example, if you have dependencies on the support library, which contains translations for multiple languages, you can filter resources just for the given language configuration, like English or Spanish. You must define the language configuration by a two-letter ISO 639-1 language code, optionally followed by a two letter ISO 3166-1-alpha-2 region code preceded by lowercase 'r'. For example, en-rUS. |
| `--preferred-density `<var translate="no">density</var>                                             | Allows AAPT2 to select the closest matching density and strip out all others. <br /> There are several pixel density qualifiers available to use in your app, such as ldpi, hdpi, and xhdpi. When you specify a preferred density, AAPT2 selects and stores the closest matching density in the resource table and removes all others.                                                                                                                                          |
| `--output-to-dir`                                                                                   | Outputs the APK contents to a directory specified by`-o`. <br /> If you get any errors using this flag, you can resolve them by upgrading to[Android SDK Build Tools 28.0.0 or higher](https://developer.android.com/studio/releases/build-tools).                                                                                                                                                                                                                              |
| `--min-sdk-version `<var translate="no">min-sdk-version</var>                                       | Sets the default minimum SDK version to use for`AndroidManifest.xml`.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `--target-sdk-version `<var translate="no">target-sdk-version</var>                                 | Sets the default target SDK version to use for`AndroidManifest.xml`.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--version-code `<var translate="no">version-code</var>                                             | Specifies the version code to inject into`AndroidManifest.xml`if none is present.                                                                                                                                                                                                                                                                                                                                                                                               |
| `--version-name `<var translate="no">version-name</var>                                             | Specifies the version name to inject into`AndroidManifest.xml`if none is present.                                                                                                                                                                                                                                                                                                                                                                                               |
| `--revision-code `<var translate="no">revision-code</var>                                           | Specifies the revision code to inject into`AndroidManifest.xml`file if none is present.                                                                                                                                                                                                                                                                                                                                                                                         |
| `--replace-version`                                                                                 | If`--version-code`,`--version-name`, or`--revision-code`are specified, these values replace any value already in the manifest. By default, nothing changes if the manifest already defines these attributes.                                                                                                                                                                                                                                                                    |
| ` --compile-sdk-version-nacodeme `<var translate="no">compile-sdk-version-name</var>` `             | Specifies the version code to inject into`AndroidManifest.xml`file if none is present.                                                                                                                                                                                                                                                                                                                                                                                          |
| ` --compile-sdk-version-name `<var translate="no">compile-sdk-version-name</var>` `                 | Specifies the version name to inject into`AndroidManifest.xml`file if none is present.                                                                                                                                                                                                                                                                                                                                                                                          |
| `--proto-format`                                                                                    | Generates compiled resources in Protobuf format. Suitable as input to the[`bundletool`](https://developer.android.com/studio/build/building-cmdline#bundletool-build)for generating an Android App Bundle.                                                                                                                                                                                                                                                                      |
| `--non-final-ids`                                                                                   | Generates`R.java`with non-final resource IDs. References to the IDs from app's code aren't inlined during`kotlinc`or`javac`compilation.                                                                                                                                                                                                                                                                                                                                         |
| `--emit-ids `<var translate="no">path</var>                                                         | Emits a file at the given path with a list of names of resource types and their ID mappings. This is suitable to use with`--stable-ids`.                                                                                                                                                                                                                                                                                                                                        |
| `--stable-ids `<var translate="no">outputfilename.ext</var>                                         | Consumes the file generated with`--emit-ids`containing the list of names of resource types and their assigned IDs. <br /> This option allows assigned IDs to remain stable even when you delete or add new resources while linking.                                                                                                                                                                                                                                             |
| `--custom-package `<var translate="no">package_name</var>                                           | Specifies the custom Java package to generate`R.java`under.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ` --extra-packages `<var translate="no">package_name</var>                                          | Generates the same`R.java`file, but with different package names.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `--add-javadoc-annotation `<var translate="no">annotation</var>                                     | Adds a JavaDoc annotation to all generated Java classes.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `--output-text-symbols `<var translate="no">path</var>                                              | Generates a text file containing the resource symbols of the`R`class in the specified file. <br /> You must specify the path to the output file.                                                                                                                                                                                                                                                                                                                                |
| `--auto-add-overlay`                                                                                | Allows the addition of new resources in overlays without using the`<add-resource>`tag.                                                                                                                                                                                                                                                                                                                                                                                          |
| `--rename-manifest-package `<var translate="no">manifest-package</var>                              | Renames the package in`AndroidManifest.xml`file.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--rename-instrumentation-target-package `<var translate="no">instrumentation- target-package</var> | Changes the name of the target package for[`instrumentation`](https://developer.android.com/reference/android/app/Instrumentation). <br /> This option should be used in conjunction with`--rename-manifest-package`.                                                                                                                                                                                                                                                           |
| `-0 `<var translate="no">extension</var>                                                            | Specifies the extensions of files that you don't want to compress.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `--split `<var translate="no">path:config[,config[..]]</var>` `                                     | Splits resources based on a set of configurations to generate a different version of the APK. <br /> You must specify the path to the output APK along with the set of configurations.                                                                                                                                                                                                                                                                                          |
| `--proguard-main-dex `<var translate="no">file</var>                                                | Output file for generated ProGuard rules for the main DEX.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `--proguard-minimal-keep-rules`                                                                     | Generates a minimal set of ProGuard keep rules.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `--no-resource-removal`                                                                             | Disables automatic removal of resources without defaults. Use this option only when building runtime resource overlay packages.                                                                                                                                                                                                                                                                                                                                                 |
| `-x`                                                                                                | Legacy flag that specifies the use of the package identifier 0x01.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `--product `<var translate="no">products-list</var>                                                 | Specifies a comma-separated list of product names to keep.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `--no-xml-namespaces`                                                                               | Removes XML namespace prefix and URI information from`AndroidManifest.xml`file and XML binaries in`res/*`.                                                                                                                                                                                                                                                                                                                                                                      |
| `--shared-lib`                                                                                      | Generates a shared Android runtime library.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--static-lib`                                                                                      | Generates a static Android library.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--no-static-lib-packages`                                                                          | Merges all library resources under the app's package.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `--no-proguard-location-reference`                                                                  | Keeps ProGuard rules files from having a reference to the source file.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `--private-symbols `<var translate="no">package-name</var>                                          | <var translate="no">package-name</var>specifies the package name to use when generating`R.java`for private symbols. If not specified, public and private symbols use the app's package name.                                                                                                                                                                                                                                                                                    |
| `--override-styles-instead-of-overlaying`                                                           | Causes styles defined in`-R`resources to replace previous definitions instead of merging them.                                                                                                                                                                                                                                                                                                                                                                                  |
| `--rename-resources-package `<var translate="no">package-name</var>                                 | Renames the package in the resources table to<var translate="no">package-name</var>.                                                                                                                                                                                                                                                                                                                                                                                            |
| `--no-compress`                                                                                     | Doesn't compress any resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `--keep-raw-values`                                                                                 | Preserves raw attribute values in XML files.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `--no-compress-regex `<var translate="no">regular-expression</var>                                  | Doesn't compress extensions matching<var translate="no">regular-expression</var>. Use the`$`symbol for end of line. Uses a case-sensitive ECMAScript regular expression grammar.                                                                                                                                                                                                                                                                                                |
| `--warn-manifest-validation`                                                                        | Treats manifest validation errors as warnings.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--exclude-configs `<var translate="no">qualifier[,qualifier[..]]</var>                             | Excludes values of resources whose configs contain the specified qualifiers.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `--debug-mode`                                                                                      | Inserts`android:debuggable="true"`in to the application node of the manifest, making the application debuggable even on production devices.                                                                                                                                                                                                                                                                                                                                     |
| `--strict-visibility`                                                                               | Doesn't allow overlays with different visibility levels.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `--exclude-sources`                                                                                 | Doesn't serialize source file information when generating resources in Protobuf format.                                                                                                                                                                                                                                                                                                                                                                                         |
| `--trace-folder `<var translate="no">folder</var>                                                   | Generates`systrace`JSON trace fragment to specified<var translate="no">folder</var>.                                                                                                                                                                                                                                                                                                                                                                                            |
| `--merge-only`                                                                                      | Only merges the resources without verifying resource references. This flag should only be used with the`--static-lib`flag.                                                                                                                                                                                                                                                                                                                                                      |
| `-h`                                                                                                | Displays the help menu.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `-v`                                                                                                | Enables increased verbosity of the output.                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Dump

`dump`is used for printing information about the APK you generated using the`link`command.

### Dump syntax

The general syntax for using`dump`is as follows:  

```
aapt2 dump sub-command filename.apk [options]
```

The following example prints content from the resource table of the specified APK:  

```
aapt2 dump resources output.apk
```

### Dump sub-commands

Specify one of the following sub-commands with the`dump`command:

**Table 4.**Dump sub-commands

|   Sub-command    |                                  Description                                   |
|------------------|--------------------------------------------------------------------------------|
| `apc`            | Prints the contents of the AAPT2 Container (APC) generated during compilation. |
| `badging`        | Prints information extracted from the APK's manifest.                          |
| `configurations` | Prints every configuration used by a resource in the APK.                      |
| `overlayable`    | Prints the overlayable resources of the APK.                                   |
| `packagename`    | Prints the APK's package name.                                                 |
| `permissions`    | Prints the permissions extracted from the APK's manifest.                      |
| `strings`        | Prints the contents of the APK's resource table string pool.                   |
| `styleparents`   | Prints the parents of styles used in the APK.                                  |
| `resources`      | Prints the contents of the APK's resource table.                               |
| `xmlstrings`     | Prints strings from the APK's compiled XML.                                    |
| `xmltree`        | Prints a tree of the APK's compiled XML.                                       |

### Dump options

Use the following options with`dump`:

**Table 5.**Dump options

|                 Option                  |                        Description                         |
|-----------------------------------------|------------------------------------------------------------|
| `--no-values`                           | Suppresses the output of values when displaying resource.  |
| `--file `<var translate="no">file</var> | Specifies a file as an argument to be dumped from the APK. |
| `-v`                                    | Increases verbosity of the output.                         |

## Diff

Use`diff`to compare two APKs and identify any differences between them.

### Diff syntax

The general syntax for using`diff`is as follows:  

```
aapt2 diff first.apk second.apk
```

There are no options for the`diff`command.

## Optimize

`optimize`is used to run optimizations on the merged resources and`resources.arsc`before they are packaged into the APK. This optimization can reduce APK size by around 1-3%, depending on the size and number of resources that are being used.

### Optimize syntax

The general syntax for using`optimize`is as follows:  

```
aapt2 optimize options file[,file[..]]
```

The following example optimizes the resources in`input.apk`and creates a new, optimized APK in`output.apk`. It replaces the usual flat table representation with a more compact representation, leading to a reduction in APK size, memory usage, and startup latency, and a small increase in individual resource lookup time after startup.  

```
aapt2 optimize -o output.apk --enable-sparse-encoding input.apk
```

### Optimize options

You can use the following options with`optimize`:

**Table 6.**Optimize options

|                                 Option                                  |                                                                                          Description                                                                                          |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-o `<var translate="no">path</var>                                     | Specifies the output path for the linked resource APK. <br /> This is a**required**flag, because you must specify the path for the output APK that can hold the linked resources.             |
| `-d `<var translate="no">directory</var>                                | Specifies the path to the output directory for splits.                                                                                                                                        |
| `-x `<var translate="no">path</var>                                     | Specifies the path to the XML configuration file.                                                                                                                                             |
| `-p`                                                                    | Prints the multi-APK artifacts and exit.                                                                                                                                                      |
| `--target-densities `<var translate="no">density[,density[..]]</var>    | Specifies a comma-separated list of the screen densities that the APK is optimized for. All resources that would be unused on devices of the given densities are removed from the APK.        |
| `--resources-config-path `<var translate="no">path</var>                | Specifies the path to the`resources.cfg`file containing the list of resources and directives to each resource. Format:<var translate="no">type/resource_name#[directive][,directive]</var>    |
| `-c `<var translate="no">config[,config[..]]</var>                      | Specifies a comma-separated list of configurations to include. The default is all configurations.                                                                                             |
| `--split `<var translate="no">path:config[,config[..]]</var>` `         | Splits resources based on a set of configurations to generate a different version of the APK. <br /> You must specify the path to the output APK along with the set of configurations.        |
| `--keep-artifacts `<var translate="no">artifact[,artifact[..]]</var>` ` | Specifies a comma-separated list of artifacts to keep. If none are specified, all artifacts are kept.                                                                                         |
| `--enable-sparse-encoding`                                              | Enables sparse encoding of resource entries. This leads to a reduction in APK size, memory usage, and startup latency, and a small increase in individual resource lookup time after startup. |
| `--collapse-resource-names`                                             | Collapses resource names to a single value in the key string pool. Resources are exempted using the`no_collapse`directive in a file specified by`--resources-config-path`.                    |
| `--shorten-resource-paths`                                              | Shortens the paths of resources inside the APK.                                                                                                                                               |
| `--resource-path-shortening-map `<var translate="no">path</var>         | Specifies the path to output the map of old resource paths to shortened paths.                                                                                                                |
| `-v`                                                                    | Increases verbosity of the output.                                                                                                                                                            |
| `-h`                                                                    | Displays the tool help.                                                                                                                                                                       |

## Convert

By default, the AAPT`compile`command compiles resources in to a binary format that is suitable for APKs. It is possible to also specify protobuf format that is suitable for AABs by specifying`--proto-format`. The`convert`command converts APKs between the two formats.

### Convert syntax

The general syntax for`convert`is as follows:  

```
aapt2 convert -o output-file options file[,file[..]]
```

The following example converts the resources in`input.apk`and creates a new, APK in`output.apk`containing protobuf format resources. It replaces the usual flat table representation with a more compact representation, leading to a reduction in APK size, memory usage, and startup latency, and a small increase  

```
aapt2 convert -o output.apk --output-format proto --enable-sparse-encoding input.apk
```

### Convert Options

Use the following options with`convert`:

**Table 7.**Convert options

|                           Option                           |                                                                                          Description                                                                                          |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-o `<var translate="no">path</var>                        | Specifies the output path for the linked resource APK. This is a**required**flag, because you must specify the path for the output APK that can hold the linked resources.                    |
| `--output-format `<var translate="no">[proto|binary]</var> | Format of the output. Accepted values are`proto`and`binary`. When not set, defaults to`binary`.                                                                                               |
| `--enable-sparse-encoding`                                 | Enables sparse encoding of resource entries. This leads to a reduction in APK size, memory usage, and startup latency, and a small increase in individual resource lookup time after startup. |
| `--keep-raw-values`                                        | Preserves raw attribute values in XML files.                                                                                                                                                  |
| `-v`                                                       | Increases verbosity of the output.                                                                                                                                                            |
| `-h`                                                       | Displays the tool help.                                                                                                                                                                       |

## Daemon mode

AAPT version 2.19 introduced daemon mode for issuing commands. Daemon mode lets you enter multiple commands in a single AAPT session.

### Daemon syntax

Start daemon mode with the following command:  

```
aapt2 daemon
```

Once daemon mode is running, you can enter commands. Each argument of the command must be on a separate line, with a blank line at the end of the command. Exit daemon mode by typing Control+D.

Consider the following individual`compile`commands:  

```
aapt2 compile project_root/module_root/src/main/res/values-en/strings.xml -o compiled/
aapt2 compile project_root/module_root/src/main/res/drawable/myImage.png -o compiled/
```

These commands can be entered in daemon mode as:  

```
aapt2 daemon
Ready
compile
project_root/module_root/src/main/res/values-en/strings.xml
-o
compiled/

Done
compile
project_root/module_root/src/main/res/drawable/myImage.png
-o
compiled/

Done
^D
Exiting daemon
```

### Daemon mode options

The single option for daemon mode is`--trace-folder `<var translate="no">folder</var>, which generates a`systrace`JSON trace fragment to specified<var translate="no">folder</var>.

## Version

Determine the version of AAPT2 you are using with the`version`command:  

```
aapt2 version
Android Asset Packaging Tool (aapt) 2.19-8678579
```

## Behavior changes when using AAPT2

Prior to AAPT2, AAPT was the default version of the Android Asset Packaging Tool, which is now deprecated. Although AAPT2 should immediately work with older projects, this section describes some behavior changes you should be aware of.

### Element hierarchies in the Android manifest

In previous versions of AAPT, elements nested in incorrect nodes in the`AndroidManifest.xml`file were either ignored or resulted in a warning. For example, consider the following example:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
   package="com.example.myname.myapplication">
   <application
       ...
       <activity android:name=".MainActivity">
           <intent-filter>
               <action android:name="android.intent.action.MAIN" />
               <category android:name="android.intent.category.LAUNCHER" />
           </intent-filter>
           <action android:name="android.intent.action.CUSTOM" />
       </activity>
   </application>
</manifest>
```

Previous versions of AAPT would simply ignore the misplaced`<action>`tag.

With AAPT2, you receive the following error:  

```
AndroidManifest.xml:15: error: unknown element <action> found.
```

To resolve the issue, make sure your manifest elements are nested correctly. For more information, read the[App Manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro).

### Declaration of resources

You can no longer indicate the type of a resource from the`name`attribute. The following example incorrectly declares an`attr`resource item:  

```xml
<style name="childStyle" parent="parentStyle">
    <item name="attr/my_attr">@color/pink</item>
</style>
```

Declaring a resource type this way results in the following build error:  

```
Error: style attribute 'attr/attr/my_attr (aka my.package:attr/attr/my_attr)'
not found.
```

To resolve this error, explicitly declare the type using`type="attr"`:  

```xml
<style name="childStyle" parent="parentStyle">
  <item type="attr" name="my_attr">@color/pink</item>
</style>
```

Additionally, when declaring a`<style>`element, its parent must also be a style resource type. Otherwise, you get an error similar to the following:  

```
Error: (...) invalid resource type 'attr' for parent of style
```

### Incorrect use of @ resource reference symbols

AAPT2 throws build errors when you omit or incorrectly place resource reference symbols (`@`). For example, if you omit the symbol when specifying a style attribute:  

```xml
<style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">
  ...
  <!-- Note the missing '@' symbol when specifying the resource type. -->
  <item name="colorPrimary">color/colorPrimary</item>
</style>
```

When building the module, AAPT2 throws the following build error:  

```
ERROR: expected color but got (raw string) color/colorPrimary
```

Additionally, if you incorrectly include the symbol when accessing a resource from the`android`namespace:  

```xml
...
<!-- When referencing resources from the 'android' namespace, omit the '@' symbol. -->
<item name="@android:windowEnterAnimation"/>
```

When building the module, AAPT2 throws the following build error:  

```
Error: style attribute '@android:attr/windowEnterAnimation' not found
```

### Incorrect configuration of libraries

If your app has a dependency on a third-party library that was built using older versions of the[Android SDK Build Tools](https://developer.android.com/studio/releases/build-tools), your app might crash at runtime without displaying any errors or warnings. This crash might occur because during the library's creation, the`R.java`fields are declared`final`. As a result, all the resource IDs are inlined in the library's classes.

AAPT2 relies on being able to re-assign IDs to library resources when building your app. If the library assumes the IDs are`final`and inlines them in the library DEX, there is a runtime mismatch.

To resolve this error, contact the library author to rebuild the library using the latest version of the Android SDK Build Tools, and republish the library.