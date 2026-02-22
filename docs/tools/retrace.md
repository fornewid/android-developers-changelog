---
title: https://developer.android.com/tools/retrace
url: https://developer.android.com/tools/retrace
source: md.txt
---

# R8 retrace is a tool for obtaining the original stack trace from an obfuscated stack trace. The stack trace is reconstructed by matching class and method names in a mapping file to their original definitions.
| **Note:** R8 retrace is a standalone tool in version 4.0 of the command-line tools package, released with Android Studio 4.2.
|
| To download the command-line tools package with the SDK Manager, see[Update your tools with the SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager). The SDK Manager installs R8 retrace in`cmdline-tools/`<var translate="no">version</var>`/bin/`.
|
| To download the command-line tools package using the command line, see[`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager).

## Usage

To retrace an obfuscated stack trace, pass the mapping file to`retrace`:  

    retrace <var translate="no"> path-to-mapping-file [path-to-stack-trace-file] [options] </var>

If no stack trace file is given on the command line, R8 retrace waits for the stack trace to be entered by the user through standard input. After input, terminate the input stream:

- **Linux, macOS:**Control+D
- **Windows:**Control+Z+Enter

The retraced output is then written to standard output.

## Options

The following table describes the command-line options of R8 retrace:

|                         Option                          | Required? |                                                                                                    Description                                                                                                    |
|---------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--verbose`                                             | no        | Prints more information, such as method parameters and method return type.                                                                                                                                        |
| `--info`                                                | no        | Sets the diagnostic level to`info`. For a more in-depth look, refer to[DiagnosticsHandler](https://r8.googlesource.com/r8/+/refs/heads/main/src/main/java/com/android/tools/r8/DiagnosticsHandler.java).          |
| `--quiet`                                               | no        | Reduces the amount of information printed to increase focus.                                                                                                                                                      |
| `--regex `<var translate="no">&lt;regular_exp&gt;</var> | no        | Overwrites the default regular expression for parsing stack trace lines. For example, the following is a regex that can parse basic stack traces: `(?:.*? at %c\.%m\(%s(?::%l)?\))|(?:(?:.*?[:"] +)?%c(?::.*)?)`. |

## Usage notes

R8 retrace uses a generated mapping file for mapping obfuscated class and method names back to the original definition. For more information about shrinking your app so that it can be retraced correctly, see[Decode an obfuscated stack trace](https://developer.android.com/studio/build/shrink-code#decode-stack-trace).