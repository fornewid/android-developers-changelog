---
title: layoutopt  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/tools/help/layoutopt
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Studio](https://developer.android.com/studio)

# layoutopt Stay organized with collections Save and categorize content based on your preferences.



**Note:** The Android `layoutopt` tool has been replaced
by the `lint` tool beginning in SDK Tools revision 16. The `lint` tool reports UI
layout performance issues in a similar way as `layoutopt` and detects additional problems.

For more information about using `lint`, see
[Improve your code with lint checks](/tools/debugging/improving-w-lint).

`layoutopt` is a command-line tool that helps you optimize the
layouts and layout hierarchies of your applications. This document is a reference for the available command line options.

### Usage

To run `layoutopt` against a given list of layout resources:

```
layoutopt <file_or_directory> ...
```

For example:

```
$ layoutopt res/layout-land
```

```
$ layoutopt res/layout/main.xml res/layout-land/main.xml
```