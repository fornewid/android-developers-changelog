---
title: https://developer.android.com/develop/ui/compose/tooling/stacktraces
url: https://developer.android.com/develop/ui/compose/tooling/stacktraces
source: md.txt
---

Jetpack Compose executes your code in multiple different phases, which causes
some parts of the `@Composable` function to be executed separately from each
other. Crashes in these phases can result in stack traces that are hard to
decipher, making it difficult to pinpoint the exact function or line of code
that caused the crash.

## Add source info to stack traces

To improve stack trace readability, an opt-in API provides richer crash location
details, including composable names and locations, enabling you to:

- Efficiently identify and resolve crash sources
- Isolate crashes for reproducible samples
- Investigate crashes that previously only showed internal stack frames

The Compose runtime can detect the crash location in composition and reconstruct
a stack trace based on your `@Composable` hierarchy. The stack trace is appended
for crashes in:

- Composition
- `DisposableEffect` and `LaunchedEffect` (except for `onDispose` or cancellation)
- Coroutines launched in `rememberCoroutineScope`
- Measure, layout and draw passes

To enable this feature, add the following lines to the application entry point:

> [!WARNING]
> **Warning:** Verify that you are using Kotlin 2.3.0+ and have R8 enabled when using `Auto` or `GroupKeys` option in production builds.


```kotlin
// Enable stack traces at application level: onCreate
class SampleStackTracesEnabledApp : Application() {

    override fun onCreate() {
        super.onCreate()
        // Enable Compose stack traces for minified builds only.
        Composer.setDiagnosticStackTraceMode(ComposeStackTraceMode.Auto)

        // Alternatively:
        // Enable verbose Compose stack traces for local debugging
        Composer.setDiagnosticStackTraceMode(ComposeStackTraceMode.SourceInformation)
    }
}
```

<br />

Ideally, perform this configuration before creating any compositions to verify
that the stack trace information is collected correctly.

There are four options for the [`ComposeStackTraceMode`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/tooling/ComposeStackTraceMode):

- [`Auto`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/tooling/ComposeStackTraceMode#Auto()): Recommended option, as it uses `GroupKeys` if the app is minified and `None` otherwise.
- [`GroupKeys`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/tooling/ComposeStackTraceMode#GroupKeys()): Stack traces are created for minified apps. The group key information is retained even after minification and is used together with the proguard mapping file emitted by Compose compiler and R8 to reconstruct a rough location of `@Composable` functions. These stack traces are less precise, and optimized to avoid doing additional work at runtime. Compose compiler supports emission of additional R8 mappings starting from Kotlin 2.3.0.
- [`SourceInformation`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/tooling/ComposeStackTraceMode#SourceInformation()): Useful for non-minified builds, collects source information and adds it to the stack trace. The results are more accurate, but incur significant performance cost that is similar to attaching the Layout inspector. They are created to be used in debug versions of the apps to get accurate readings on a crash that requires more information about its location. The source information is removed from minified apps to optimize the binary size and performance.
- [`None`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/tooling/ComposeStackTraceMode#None()): No extra stack trace details added.

When using the `SourceInformation` option, the stack trace then appears as a
`DiagnosticComposeException` in the suppressed exception list:

    java.lang.IllegalStateException: Test layout error
        at <original trace>
    Suppressed: androidx.compose.runtime.DiagnosticComposeException:
    Composition stack when thrown:
        at ReusableComposeNode(Composables.kt:<unknown line>)
        at Layout(Layout.kt:79)
        at <lambda>(TempErrorsTest.kt:164)
        at <lambda>(BoxWithConstraints.kt:66)
        at ReusableContentHost(Composables.kt:164)
        at <lambda>(SubcomposeLayout.kt:514)
        at SubcomposeLayout(SubcomposeLayout.kt:114)
        at SubcomposeLayout(SubcomposeLayout.kt:80)
        at BoxWithConstraints(BoxWithConstraints.kt:64)
        at SubcomposeLayoutErrorComposable(TempErrorsTest.kt:164)
        at <lambda>(TempErrorsTest.kt:86)
        at Content(ComposeView.android.kt:430)
        at <lambda>(ComposeView.android.kt:249)
        at CompositionLocalProvider(CompositionLocal.kt:364)
        at ProvideCommonCompositionLocals(CompositionLocals.kt:193)
        at <lambda>(AndroidCompositionLocals.android.kt:113)
        at CompositionLocalProvider(CompositionLocal.kt:364)
        at ProvideAndroidCompositionLocals(AndroidCompositionLocals.android.kt:102)
        at <lambda>(Wrapper.android.kt:141)
        at CompositionLocalProvider(CompositionLocal.kt:384)
        at <lambda>(Wrapper.android.kt:140)

## Known limitations

There are a few known issues with stack trace frames:

### Source information stack traces

Missing line numbers (`<unknown line>`) in the first stack frame for crashes in
composition. Since source information introspection is happening after a crash,
the slot table data can be incomplete and drop line number.
`ReusableComposeNode` and `remember` don't produce source information, so you
will see `<unknown line>` in the stack frames for those functions.

### Group keys stack traces

`GroupKeys` based stack traces can only point to the first line of the
`@Composable` function by design. They also don't contain any data for any
functions that don't produce a group (such as inline or non-Unit returning
functions)

## Stack trace collection crashes

If the stack trace collection crashes for any reason, that exception is appended
as a suppressed exception instead of `DiagnosticComposeException`.

Report any suppressed crashes or stack trace inconsistencies to the [Compose
Runtime component](https://issuetracker.google.com/issues/new?component=610764&template=1424126).