---
title: https://developer.android.com/studio/gemini/aiexclude
url: https://developer.android.com/studio/gemini/aiexclude
source: md.txt
---

# Configure context sharing with .aiexclude files

When you opt in to sharing your project context with Gemini in Android Studio, you can control which files specifically from the codebase are shared using`.aiexclude`files. AI features in Android Studio cannot access files outside of the current project and the Version Control System (VCS) roots attached to it. With this in mind, you can place`.aiexclude`files anywhere within the project and its VCS roots to control which files AI features are allowed to access.

Much like a`.gitignore`file, an`.aiexclude`file tracks files that shouldn't be shared with Gemini in Android Studio. This includes the chat experience as well as AI features that operate in the editor, like[code completion](https://developer.android.com/studio/gemini/code-completion). An`.aiexclude`file operates on files at or below the directory that contains it.
![An example `.aiexclude` file in Android Studio.](https://developer.android.com/static/studio/images/gemini-aiexclude.png)An example of an \`.aiexclude\` file in Android Studio.

## How to write`.aiexclude`files

An`.aiexclude`file follows the same syntax as a[`.gitignore`file](https://git-scm.com/docs/gitignore).

## Examples

Here are example`.aiexclude`file configurations:

- The pattern`KEYS`blocks all files called "KEYS" with no file extension in the directory containing the`.aiexclude`file, or in its subdirectories.

    KEYS

- The pattern`KEYS.*`blocks all files called "KEYS" with any file extension in the directory containing the`.aiexclude`file, or in its subdirectories.

    KEYS.*

- The pattern`*.kt`blocks all Kotlin files in the directory containing the`.aiexclude`file, or in its subdirectories.

    *.kt

- The pattern`/*.kt`blocks all Kotlin files in the`.aiexclude`directory, but not in its subdirectories.

    /*.kt

- The pattern`my/sensitive/dir/`blocks all files in the`my/sensitive/dir`directory and its subdirectories. The path is relative to the directory that contains the`.aiexclude`file.

    my/sensitive/dir/

- The pattern`my/sensitive/dir/**/.txt`blocks all TXT files in the`my/sensitive/dir/`directory or its subdirectories.

    my/sensitive/dir/**/.txt

- The pattern`my/sensitive/dir/*.txt`blocks all TXT files in the directory`my/sensitive/dir`, but not in sub-directories.

    my/sensitive/dir/*.txt