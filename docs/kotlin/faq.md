---
title: https://developer.android.com/kotlin/faq
url: https://developer.android.com/kotlin/faq
source: md.txt
---

# Kotlin on Android FAQ

#### Why did Android make Kotlin a first-class supported language?

Kotlin is an Android-compatible language that is concise, expressive, and designed to be type- and null-safe. It works with the Java programming language seamlessly, so it makes it easy for developers who love Java to keep using it while incrementally adding Kotlin code and leveraging Kotlin libraries. Meanwhile, many Android developers have found that Kotlin makes development faster and more fun, so Google wants to better support these Kotlin users. Read more about[Android's Kotlin-first approach](https://developer.android.com/kotlin/first).

#### How do I use Kotlin with Android Studio?

Kotlin is fully supported in[Android Studio](https://developer.android.com/studio). All new releases of Android Studio ship with support for creating new projects with Kotlin files, converting Java language code to Kotlin, debugging Kotlin code, and more.

#### How do I debug Kotlin in Android Studio?

Debugging Kotlin works just like debugging Java code. You don't need to do anything differently.

#### What kind of other IDE support is provided for Kotlin (like lint,

autocomplete, and refactoring)?

[Android Studio](https://developer.android.com/studio)has full tooling support for Kotlin.

#### What's the future of Kotlin?

JetBrains' thoughtful work on Kotlin's design is one of the reasons to embrace the language. Google is partnering with JetBrains to ensure a wonderful overall developer story---from language to framework to tools. We're excited to be working together to move the Kotlin language into a not-for-profit foundation.

#### Is Kotlin open source?

The preferred license for Kotlin is the[Apache Software License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)("Apache 2.0"), and the majority of the Kotlin software is licensed under it. While the project strives to adhere to the preferred license, there can be exceptions, which are handled on a case-by-case basis. For example, certain third-party dependencies used by Kotlin are licensed under different open-source licenses that are still compatible with the Apache 2.0 license.

#### How do I choose between the Java and Kotlin languages?

You don't have to pick! You can use both. If you need help discovering whether Kotlin is a good fit for you, you can[try it on Android](https://developer.android.com/kotlin)or learn more about the language with[these Kotlin resources](https://developer.android.com/kotlin/getting-started-resources).

#### Can I call Android or other Java language library APIs from Kotlin?

Yes. Kotlin provides Java language interoperability. This design lets Kotlin code transparently call Java language methods, coupled with annotations that make it easy to expose Kotlin-only functionality to Java code. Kotlin files that don't use any Kotlin-specific semantics can be directly referenced from Java code without any annotations at all. Combined, this lets you granularly mix Java code with Kotlin code. To learn more, see[Kotlin's interop documentation](https://kotlinlang.org/docs/reference/java-interop.html).

#### Do you have Kotlin reference docs for Android APIs?

Yep! Google is working to make all Android API documentation available with idiomatic Kotlin references. You can find links to the available Kotlin reference docs on the[Android reference overview page](https://developer.android.com/reference/kotlin). If you're looking for a core Kotlin language reference, see the[Kotlin standard library reference](https://kotlinlang.org/api/latest/jvm/stdlib/index.html).

#### Can I use both Java files and Kotlin files in the same project?

Yes. You can adopt as much or as little Kotlin as you like and mix it with Java code using[Kotlin's interoperability with Java](https://kotlinlang.org/docs/reference/java-interop.html).

#### Can I use Kotlin with C++?

Yes, JNI is fully supported with Kotlin. Mark JNI methods with[the external modifier](https://kotlinlang.org/docs/reference/java-interop.html#using-jni-with-kotlin).

#### How do I add Kotlin to my new projects?

When creating new projects, Kotlin is now the default language choice in Android Studio. For more information, see[Create a project](https://developer.android.com/studio/projects/create-project).

#### How do I add Kotlin to my existing projects?

Select your module in the**Project** window, and then select**File \> New** . Select any Android template, and then choose**Kotlin** as the**Source language** . For more information, see[Add Kotlin to an existing app](https://developer.android.com/kotlin/add-kotlin).

#### How do I convert Java language code to Kotlin?

Open a Java file and select**Code \> Convert Java File to Kotlin File** . Or, create a new Kotlin file (**File \> New \> Kotlin File/Class** ), and then paste your Java code into that file. When prompted, click**Yes**to convert the code to Kotlin.
| **Note:** Be sure to review any converted code and ensure that your tests continue to pass.

#### Will there be parallel docs, samples, codelabs, and templates in Kotlin?

We're working to make our documentation and educational materials as useful as possible to both Java and Kotlin language users. In the meantime, developers can rely on Kotlin's excellent interoperability with the Java language and the ability to automatically translate Java language code to Kotlin in Android Studio.

#### Do Kotlin coroutines work on Android? How about async/await?

Kotlin coroutines are stable as of Kotlin version 1.3 and work as intended on Android. For more information on using coroutines with Android, see[Improve app performance with Kotlin coroutines](https://developer.android.com/kotlin/coroutines).

#### Does using Kotlin have any performance impact?

Kotlin doesn't have a direct performance impact, but just as with the Java language, you should be thoughtful about how you use it. For example, repeated copying between new collection instances can impact GC performance, and calling a method that accepts non-null types adds a method call for the null check (though you can disable runtime null checks in the compiler with`-Xno-param-assertions`).

#### Which versions of Android does Kotlin support?

All of them! Kotlin is compatible with JDK 6, so apps with Kotlin safely run on older Android versions.

#### Where can I learn more about using Kotlin?

Check out[Additional resources for getting started with Kotlin](https://developer.android.com/kotlin/getting-started-resources).