---
title: https://developer.android.com/tools/jetifier
url: https://developer.android.com/tools/jetifier
source: md.txt
---

# Jetifier

The standalone Jetifier tool migrates support-library-dependent libraries to instead rely on the equivalent AndroidX packages. The tool lets you migrate an individual library directly instead of using the Android Gradle plugin bundled with Android Studio.
| **Note:** Before you begin the migration, update your library to use version 28.0.0 of the Support Library.

## Install Jetifier

To install Jetifier,[download the zip file](https://dl.google.com/dl/android/studio/jetifier-zips/1.0.0-beta10/jetifier-standalone.zip)and extract it. Your device must have Java version 1.8 or higher installed.

## Usage

To process a library, pass the path to the current library and the path to the output file that the tool should create. Jetifier supports JAR, AAR, and ZIP files, including nested archives.  

```
./jetifier-standalone -i <source-library> -o <output-library>
```

### Options

The following table lists the available options for the Jetifier tool commands:

|                         Option                         | Required? |                                                                                    Description                                                                                     |
|--------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-i`,`--input`<var translate="no">&lt;path&gt;</var>   | yes       | Path to input library (JAR, AAR, or ZIP).                                                                                                                                          |
| `-o`,`--output`<var translate="no">&lt;path&gt;</var>  | yes       | Path to the output file. If the file already exists, Jetifier overwrites it.                                                                                                       |
| `-c`,`--config`<var translate="no">&lt;path&gt;</var>  | no        | Path to optional custom config file.                                                                                                                                               |
| `-l`,`--log`<var translate="no">&lt;level&gt;</var>    | no        | Logging level. Allowed values are: - error - warning - info - verbose If not specified, defaults to "warning".                                                                     |
| `-r`                                                   | no        | Operate in reverse mode ("de-jetification").                                                                                                                                       |
| `-rebuildTopOfTree`, `--rebuildTopOfTree`              | no        | Rebuild the ZIP of Maven distribution according to the generated POM file. If set, all rewritten libraries are assumed to be part of Support Library. Not needed for jetification. |
| `-s`,`--strict`                                        | no        | Don't fallback when rules are missing; throw errors instead.                                                                                                                       |
| `-stripSignatures`, `--stripSignatures`                | no        | Don't throw an error when jetifying a signed library; strip the signature files instead.                                                                                           |
| `-t`,`-timestamp`<var translate="no">&lt;arg&gt;</var> | no        | Timestamps policy to use for the archived entries as their modified time. Values: keepPrevious (default) epoch or now.                                                             |

#### Example

The following example runs the utility on the library`libraryToProcess.aar`in the current directory and writes the output to`result.aar`in the same directory:  

```
./jetifier-standalone -i libraryToProcess.aar -o result.aar
```

### Usage notes

Jetifier migrates Java, XML, POM, and ProGuard references that point to`android.support.*`packages, changing them so they point to the corresponding`androidx.*`packages.

Since ProGuard wildcards for`android.support.*`don't always map directly to`androidx.*`packages, Jetifier produces all eligible substitutions.

If there is a type in an`android.support.*`package that does not come from any Support Library artifact, Jetifier still migrates the type as long as there is a mapping for it. However, this migration is not guaranteed to work, as there might not be mapping rules general enough to cover all the custom types.

## Advanced usage

The Jetifier utility supports some advanced use cases.

### Reverse mode

If you pass the`-r`flag, the utility runs in*reverse mode*. In this mode, the utility converts AndroidX APIs to the Support Library equivalents. Reverse mode is useful if you are developing libraries that use AndroidX APIs but also need to distribute versions that use the Support Library.

#### Example

The following example runs the utility in reverse mode on the library`myAndroidXLib.aar`in the current directory and writes the output to`supportLibVersion.aar`in the same directory:  

```
./jetifier-standalone -r -i myAndroidXLib.aar -o supportLibVersion.aar
```

### Custom config file

The Jetifier tool uses a config file to map Support Library classes to their AndroidX equivalents. If necessary, you can make a custom config file that alters this mapping. You can even add new classes to the mapping that are not actually members of the Support Library. For example, you might modify the mapping to replace one of your own classes with a successor class written to use AndroidX.

To use a custom config file:

1. Extract the file`default.generated.config`from the utility's`jetifier-core-*.jar`file and save it.
2. Make any necessary edits to your copy of the config file.
3. Pass your file to the utility with the`-c`flag.

For example:  

```
./jetifier-standalone -i libraryToProcess.aar -o result.aar -c myCustomMapping.config
```