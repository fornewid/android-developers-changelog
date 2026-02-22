---
title: https://developer.android.com/kotlin/first
url: https://developer.android.com/kotlin/first
source: md.txt
---

# Android’s Kotlin-first approach

At Google I/O 2019, we announced that Android development will be increasingly Kotlin-first, and we've stood by that commitment. Kotlin is an expressive and concise programming language that reduces common code errors and easily integrates into existing apps. If you're looking to build an Android app, we recommend starting with Kotlin to take advantage of its best-in-class features.

In an effort to support Android development using Kotlin, we co-founded the[Kotlin Foundation](https://kotlinlang.org/foundation/kotlin-foundation.html)and have ongoing investments in improving compiler performance and build speed. To learn more about Android's commitment to being Kotlin-first, see[Android's commitment to Kotlin](https://android-developers.googleblog.com/2019/12/androids-commitment-to-kotlin.html).

![Kotlin](https://developer.android.com/static/images/lockups/kotlin.svg)

## Why is Android development Kotlin-first?

We reviewed feedback that came directly from developers at conferences, our Customer Advisory Board (CAB), Google Developer Experts (GDE), and through our developer research. Many developers already enjoy using Kotlin, and the request for more Kotlin support was clear. Here's what developers appreciate about writing in Kotlin:

- **Expressive and concise:**You can do more with less. Express your ideas and reduce the amount of boilerplate code. 67% of professional developers who use Kotlin say Kotlin has increased their productivity.
- **Safer code:**Kotlin has many language features to help you avoid common programming mistakes such as null pointer exceptions. Android apps that contain Kotlin code are 20% less likely to crash.
- **Interoperable:**Call Java-based code from Kotlin, or call Kotlin from Java-based code. Kotlin is 100% interoperable with the Java programming language, so you can have as little or as much of Kotlin in your project as you want.
- **Structured Concurrency:**Kotlin coroutines make asynchronous code as easy to work with as blocking code. Coroutines dramatically simplify background task management for everything from network calls to accessing local data.

## What does Kotlin-first mean?

When building new Android development tools and content, such as Jetpack libraries, samples, documentation, and training content, we will design them with Kotlin users in mind while continuing to provide support for using our APIs from the Java programming language.

|                                                            | Java language |                                                                Kotlin                                                                |
|------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Platform SDK support                                       | Yes           | Yes                                                                                                                                  |
| Android Studio support                                     | Yes           | Yes                                                                                                                                  |
| Lint                                                       | Yes           | Yes                                                                                                                                  |
| Guided docs support                                        | Yes           | Yes                                                                                                                                  |
| API docs support                                           | Yes           | Yes                                                                                                                                  |
| AndroidX support                                           | Yes           | Yes                                                                                                                                  |
| AndroidX Kotlin-specific APIs (KTX, coroutines, and so on) | N/A           | Yes                                                                                                                                  |
| Online training                                            | Best effort   | Yes                                                                                                                                  |
| Samples                                                    | Best effort   | Yes                                                                                                                                  |
| Multi-platform projects                                    | No            | Yes                                                                                                                                  |
| Jetpack Compose                                            | No            | Yes                                                                                                                                  |
| Compiler plugin support                                    | No            | Yes - The[Kotlin Symbol Processing API](https://github.com/google/ksp)was created by Google to develop lightweight compiler plugins. |

## We use Kotlin, too!

Our engineers enjoy the language features Kotlin offers, and today over 70 of Google's apps are built using Kotlin. This includes apps like Maps, Home, Play, Drive, and Messages. One example of success comes from the[Google Home team](https://developer.android.com/stories/apps/google-home), where migrating new feature development to Kotlin resulted in a 33% reduction in codebase size and a 30% reduction in the number of NPE crashes.

To learn more about Kotlin on Android, see the[Kotlin on Android FAQ](https://developer.android.com/kotlin/faq).