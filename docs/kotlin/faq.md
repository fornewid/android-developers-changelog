---
title: https://developer.android.com/kotlin/faq
url: https://developer.android.com/kotlin/faq
source: md.txt
---

> Documentation index: https://developer.android.com/kotlin/llms.txt

This page answers common questions about using Kotlin to build Android apps.

## Why did Google make Kotlin an officially supported language for Android?

Kotlin is an Android-compatible language that is concise, expressive, and
designed to be type- and null-safe. It interoperates with the Java programming
language, so developers who use Java can keep using it while incrementally
adding Kotlin code and libraries. For more information, see
[Android's Kotlin-first approach](https://developer.android.com/kotlin/first.md.txt).

## How do I use Kotlin with Android Studio?

Kotlin is fully supported in [Android Studio](https://developer.android.com/studio). You can create new projects
with Kotlin files, convert Java language code to Kotlin, and debug Kotlin code.

## How do I debug Kotlin in Android Studio?

Debugging Kotlin works like debugging Java code. You don't need to do
anything differently.

## What other IDE support is there for Kotlin, such as lint, autocomplete, and refactoring?

[Android Studio](https://developer.android.com/studio) has full tooling support for Kotlin.

## What's the future of Kotlin?

Google partners with JetBrains across the Kotlin language, libraries, and build
tools. JetBrains and Google are founding members of the
[Kotlin Foundation](https://kotlinfoundation.org/), a not-for-profit organization that protects
and advances the language.

## Is Kotlin open source?

The preferred license for Kotlin is the
[Apache Software License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
(Apache 2.0), and the majority of the Kotlin software is licensed under
it. Although the project strives to adhere to the preferred license,
there can be exceptions, which are handled on a case-by-case basis. For
example, certain third-party dependencies used by Kotlin are licensed under
different open-source licenses that are still compatible with the Apache 2.0
license.

## How do I choose between the Java and Kotlin languages?

Kotlin is the preferred way to build Android apps, and you can also use both
languages in the same project. To get started, visit [Kotlin and Android](https://developer.android.com/kotlin.md.txt) or
[Learn the Kotlin programming language](https://developer.android.com/kotlin/learn.md.txt).

## Can I call Android or other Java language library APIs from Kotlin?

Yes. Kotlin provides Java language interoperability. This design lets
Kotlin code transparently call Java language methods, coupled with
annotations that let you expose Kotlin-only functionality to Java code.
Kotlin files that don't use any Kotlin-specific semantics can be directly
referenced from Java code without any annotations at all. Combined, this
interoperability lets you granularly mix Java code with Kotlin code. For more
information, see [Kotlin's interop documentation](https://kotlinlang.org/docs/java-interop.html).

## Are there Kotlin reference docs for Android APIs?

Yes. Android API documentation includes idiomatic Kotlin references on the
[Android reference overview](https://developer.android.com/reference/kotlin) page. For the core Kotlin language APIs, see the
[Kotlin standard library reference](https://kotlinlang.org/api/latest/jvm/stdlib/index.html).

## Can I use both Java files and Kotlin files in the same project?

Yes. You can adopt as much or as little Kotlin as you like and mix it with Java
code using [Kotlin's interoperability with Java](https://kotlinlang.org/docs/java-interop.html).

## Can I use Kotlin with C++?

Yes, the Java Native Interface (JNI) is fully supported with Kotlin. Mark JNI
methods with [the `external` modifier](https://kotlinlang.org/docs/java-interop.html#using-jni-with-kotlin).

## How do I add Kotlin to my new projects?

When creating new projects, Kotlin is the default language choice in
Android Studio. For more information, see [Create a project](https://developer.android.com/studio/projects/create-project.md.txt).

## How do I add Kotlin to my existing projects?

Select your module in the **Project** window, and then select **File \> New** .
Select any Android template, and then choose **Kotlin** as the
**Source language** . For more information, see
[Add Kotlin to an existing app](https://developer.android.com/kotlin/add-kotlin.md.txt).

## How do I convert Java language code to Kotlin?

Open a Java file and select **Code \> Convert Java File to Kotlin File** .
Alternatively, select **File \> New \> Kotlin File/Class** to create a new Kotlin
file, and then paste your Java code into that file. When prompted, click
**Yes** to convert the code to Kotlin.

> [!NOTE]
> **Note:** Review converted code and run your tests to verify behavior.

## Are docs, samples, codelabs, and templates available in both Java and Kotlin?

Android documentation and samples are Kotlin-first: new content uses Kotlin,
and Android Studio creates new projects in Kotlin by default. API reference
pages and many guides also show the Java programming language, and samples and
training support Java on a best-effort basis. If you have existing Java code,
Android Studio can [convert it to Kotlin](https://developer.android.com/kotlin/faq.md.txt#convert).

## Do Kotlin coroutines work on Android? How about async/await?

Kotlin coroutines are stable in Kotlin version 1.3 and higher and work as
intended on Android. For more information about using coroutines on Android, see
[Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines.md.txt).

## Does using Kotlin have any performance impact?

Kotlin doesn't have a direct performance impact, but just as with the Java
language, you should be thoughtful about how you use it. For example, repeated
copying between new collection instances can affect garbage collection
performance, and calling a method that accepts non-null types adds a method
call for the null check. You can disable runtime null checks in the compiler
with `-Xno-param-assertions`.

## Which versions of Android does Kotlin support?

Kotlin supports all Android versions supported by your project's Android Gradle
plugin. Kotlin compiles to bytecode that Android's D8 and R8 compilers process
for your app's `minSdk`.

## Where can I learn more about using Kotlin?

Start with the interactive [Kotlin tour](https://kotlinlang.org/docs/kotlin-tour-welcome.html), read
[Learn the Kotlin programming language](https://developer.android.com/kotlin/learn.md.txt), or take the
[Android Basics with Compose course](https://developer.android.com/courses/android-basics-compose/course) to build Android apps.