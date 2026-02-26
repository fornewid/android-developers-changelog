---
title: https://developer.android.com/develop/ui/views/layout/webapps/jsengine
url: https://developer.android.com/develop/ui/views/layout/webapps/jsengine
source: md.txt
---

## JavaScript Evaluation

Jetpack library [JavaScriptEngine](https://developer.android.com/jetpack/androidx/releases/javascriptengine) provides a way for an application to
evaluate JavaScript code without creating a WebView instance.

For applications requiring non-interactive JavaScript evaluation, using the
JavaScriptEngine library has the following advantages:

- Lower resource consumption, since there is no need to allocate a WebView
  instance.

- Can be done in a Service (WorkManager task).

- Multiple isolated environments with low overhead, enabling the application to
  run several JavaScript snippets simultaneously.

- Ability to pass large amounts of data by using an API call.

## Basic Usage

To begin, create an instance of [`JavaScriptSandbox`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox). This represents a
connection to the out-of-process JavaScript engine.

> [!NOTE]
> **Note:** Applications must check `JavaScriptSandbox` availability by calling [`JavaScriptSandbox.isSupported()`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#isSupported()) API. Make sure that the application verifies that the sandbox is supported on the device before calling any other `JavaScriptSandbox` methods. If JavaScriptEngine is unsupported, attempting to create a [`JavaScriptSandbox`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox) instance throws a [`SandboxUnsupportedException`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/SandboxUnsupportedException). The sandbox is supported on API 26 and above if the WebView implementation supports it.

    ListenableFuture<JavaScriptSandbox> jsSandboxFuture =
                   JavaScriptSandbox.createConnectedInstanceAsync(context);

It's recommended to align the lifecycle of the sandbox with the lifecycle of the
component which needs JavaScript evaluation.

For example, a component hosting the sandbox may be an `Activity` or a
`Service`. A single `Service` might be used to encapsulate JavaScript evaluation
for all application components.

Maintain the `JavaScriptSandbox` instance because its allocation is fairly
expensive. Only one `JavaScriptSandbox` instance per application is allowed. An
`IllegalStateException` is thrown when an application attempts to allocate a
second `JavaScriptSandbox` instance. However, if multiple execution environments
are required, several `JavaScriptIsolate` instances can be allocated.

When it is no longer used, close the sandbox instance to free up resources. The
`JavaScriptSandbox` instance implements an `AutoCloseable` interface, which
allows try-with-resources usage for simple blocking use cases.
Alternatively, make sure `JavaScriptSandbox` instance lifecycle is managed by
the hosting component, closing it in the `onStop()` callback for an Activity or
during `onDestroy()` for a Service:

    jsSandbox.close();

A [`JavaScriptIsolate`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate) instance represents a context for executing
JavaScript code. They can be allocated when necessary, providing weak security
boundaries for scripts of different origin or enabling concurrent JavaScript
execution since JavaScript is single-threaded by nature. Subsequent calls to
the same instance share the same state, hence it is possible to create some data
first and then process it later in the same instance of `JavaScriptIsolate`.

    JavaScriptIsolate jsIsolate = jsSandbox.createIsolate();

Release `JavaScriptIsolate` explicitly by calling its [`close()`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#close()) method.
Closing an isolate instance running JavaScript code
(having an incomplete `Future`) results in an `IsolateTerminatedException`. The
isolate is cleaned up subsequently in the background if the implementation
supports [`JS_FEATURE_ISOLATE_TERMINATION`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#JS_FEATURE_ISOLATE_TERMINATION()), as described in the
[handling sandbox crashes](https://developer.android.com/develop/ui/views/layout/webapps/jsengine##handling-sandbox-crashes) section later on this
page. Otherwise, the cleanup is postponed until all pending evaluations are
completed or the sandbox is closed.

An application can create and access a [`JavaScriptIsolate`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate) instance from
any thread.

Now, the application is ready to execute some JavaScript code:

    final String code = "function sum(a, b) { let r = a + b; return r.toString(); }; sum(3, 4)";
    ListenableFuture<String> resultFuture = jsIsolate.evaluateJavaScriptAsync(code);
    String result = resultFuture.get(5, TimeUnit.SECONDS);

The same JavaScript snippet formatted nicely:

    function sum(a, b) {
        let r = a + b;
        return r.toString(); // make sure we return String instance
    };

    // Calculate and evaluate the expression
    // NOTE: We are not in a function scope and the `return` keyword
    // should not be used. The result of the evaluation is the value
    // the last expression evaluates to.
    sum(3, 4);

The code snippet is passed as a `String` and the result delivered as a `String`.
Note that calling [`evaluateJavaScriptAsync()`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#evaluateJavaScriptAsync(java.lang.String)) returns the evaluated
result of the last expression in the JavaScript code. This must be
of JavaScript `String` type; otherwise, the library API returns an empty value.
The JavaScript code shouldn't use a `return` keyword. If the sandbox
supports certain features, additional return types (for example, a `Promise`
that resolves to a `String`) might be possible.

The library also supports evaluation of scripts that are in the form of an
`AssetFileDescriptor` or a `ParcelFileDescriptor`. See
[`evaluateJavaScriptAsync(AssetFileDescriptor)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#evaluateJavaScriptAsync(android.content.res.AssetFileDescriptor)) and
[`evaluateJavaScriptAsync(ParcelFileDescriptor)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#evaluateJavaScriptAsync(android.os.ParcelFileDescriptor)) for more details.
These APIs are better suited for evaluating from a file on disk or in app
directories.

> [!WARNING]
> **Warning:** Passing improperly escaped data to scripts using [`evaluateJavaScriptAsync(...)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#evaluateJavaScriptAsync(java.lang.String)) can lead to code injection vulnerabilities. Use [`provideNamedData(...)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#provideNamedData(java.lang.String,byte%5B%5D)) to pass data to scripts.

The library also supports console logging which can be used for debugging
purposes. This can be set up using [`setConsoleCallback()`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#setConsoleCallback(androidx.javascriptengine.JavaScriptConsoleCallback)).

Since the context persists, you can upload code and execute it several times
during the lifetime of the `JavaScriptIsolate`:

> [!NOTE]
> **Note:** This example does not include exception handling.

    String jsFunction = "function sum(a, b) { let r = a + b; return r.toString(); }";
    ListenableFuture<String> func = js.evaluateJavaScriptAsync(jsFunction);
    String twoPlusThreeCode = "let five = sum(2, 3); five";
    ListenableFuture<String> r1 = Futures.transformAsync(func,
           input -> js.evaluateJavaScriptAsync(twoPlusThreeCode)
           , executor);
    String twoPlusThree = r1.get(5, TimeUnit.SECONDS);

    String fourPlusFiveCode = "sum(4, parseInt(five))";
    ListenableFuture<String> r2 = Futures.transformAsync(func,
           input -> js.evaluateJavaScriptAsync(fourPlusFiveCode)
           , executor);
    String fourPlusFive = r2.get(5, TimeUnit.SECONDS);

Of course, variables are persistent as well, so you can continue the previous
snippet with:

    String defineResult = "let result = sum(11, 22);";
    ListenableFuture<String> r3 = Futures.transformAsync(func,
           input -> js.evaluateJavaScriptAsync(defineResult)
           , executor);
    String unused = r3.get(5, TimeUnit.SECONDS);

    String obtainValue = "result";
    ListenableFuture<String> r4 = Futures.transformAsync(func,
           input -> js.evaluateJavaScriptAsync(obtainValue)
           , executor);
    String value = r4.get(5, TimeUnit.SECONDS);

For example, the complete snippet for allocating all necessary objects and
executing a JavaScript code might look like the following:

    final ListenableFuture<JavaScriptSandbox> sandbox
           = JavaScriptSandbox.createConnectedInstanceAsync(this);
    final ListenableFuture<JavaScriptIsolate> isolate
           = Futures.transform(sandbox,
                   input -> (jsSandBox = input).createIsolate(),
                   executor);
    final ListenableFuture<String> js
           = Futures.transformAsync(isolate,
                   isolate -> (jsIsolate = isolate).evaluateJavaScriptAsync("'PASS OK'"),
                   executor);
    Futures.addCallback(js,
           new FutureCallback<String>() {
               @Override
               public void onSuccess(String result) {
                   text.append(result);
               }
               @Override
               public void onFailure(Throwable t) {
                   text.append(t.getMessage());
               }
           },
           mainThreadExecutor);

It's recommended that you use try-with-resources to make sure all allocated
resources are released and are no longer used. Closing the sandbox results
in all pending evaluations in all [`JavaScriptIsolate`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate) instances failing
with a [`SandboxDeadException`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/SandboxDeadException). When the JavaScript evaluation encounters
an error, a [`JavaScriptException`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptException) is created. Refer to its subclasses
for more specific exceptions.

## Handling Sandbox Crashes

All JavaScript is executed in a separate sandboxed process away from your
application's main process. If the JavaScript code causes this sandboxed process
to crash, for example, by exhausting a memory limit, the application's main
process will be unaffected.

A sandbox crash will cause all isolates in that sandbox to terminate. The most
obvious symptom of this is that all evaluations will start failing with
[`IsolateTerminatedException`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/IsolateTerminatedException). Depending on the circumstances, more
specific exceptions such as [`SandboxDeadException`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/SandboxDeadException) or
[`MemoryLimitExceededException`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/MemoryLimitExceededException) may be thrown.

Handling crashes for each individual evaluation is not always practical.
Furthermore, an isolate may terminate outside of an explicitly requested
evaluation due to background tasks or evaluations in other isolates. The crash
handling logic can be centralized by attaching a callback using
[`JavaScriptIsolate.addOnTerminatedCallback()`](https://developer.android.com/reference/androidx/javascriptengine/JavaScriptIsolate#addOnTerminatedCallback(androidx.core.util.Consumer%3Candroidx.javascriptengine.TerminationInfo%3E)).

    final ListenableFuture<JavaScriptSandbox> sandboxFuture =
        JavaScriptSandbox.createConnectedInstanceAsync(this);
    final ListenableFuture<JavaScriptIsolate> isolateFuture =
        Futures.transform(sandboxFuture, sandbox -> {
          final IsolateStartupParameters startupParams = new IsolateStartupParameters();
          if (sandbox.isFeatureSupported(JavaScriptSandbox.JS_FEATURE_ISOLATE_MAX_HEAP_SIZE)) {
            startupParams.setMaxHeapSizeBytes(100_000_000);
          }
          return sandbox.createIsolate(startupParams);
        }, executor);
    Futures.transform(isolateFuture,
        isolate -> {
          // Add a crash handler
          isolate.addOnTerminatedCallback(executor, terminationInfo -> {
            Log.e(TAG, "The isolate crashed: " + terminationInfo);
          });
          // Cause a crash (eventually)
          isolate.evaluateJavaScriptAsync("Array(1_000_000_000).fill(1)");
          return null;
        }, executor);

> [!NOTE]
> **Note:** The callback added through [`addOnTerminatedCallback()`](https://developer.android.com/reference/androidx/javascriptengine/JavaScriptIsolate#addOnTerminatedCallback(androidx.core.util.Consumer%3Candroidx.javascriptengine.TerminationInfo%3E)) does not trigger when closing the isolate using [`JavaScriptIsolate.close()`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#close()).

## Optional Sandbox Features

Depending on the underlying WebView version, a sandbox implementation might have
different sets of features available. So, it's necessary to query each required
feature using [`JavaScriptSandbox.isFeatureSupported(...)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#isFeatureSupported(java.lang.String)). It is important
to check feature status before calling methods relying on these features.

[`JavaScriptIsolate`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate) methods that might not be available everywhere are
annotated with [`RequiresFeature`](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresFeature) annotation, making it easier to spot these
calls in the code.

## Passing Parameters

> [!NOTE]
> **Note:** To help us gauge developer community interest in additional data I/O APIs, provide your feedback using our [bug tracker](https://issuetracker.google.com/issues/new?component=1225213&template=1720664).

If [`JavaScriptSandbox.JS_FEATURE_EVALUATE_WITHOUT_TRANSACTION_LIMIT`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#JS_FEATURE_EVALUATE_WITHOUT_TRANSACTION_LIMIT()) is
supported, the evaluation requests sent to the JavaScript engine are not bound
by the binder transaction limits. If the feature is not supported, all data to
the JavaScriptEngine occurs through a Binder transaction. The [general
transaction size limit](https://developer.android.com/reference/android/os/TransactionTooLargeException) is applicable to every call that passes in data or
returns data.

The response is always [returned as a String](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#evaluateJavaScriptAsync(java.lang.String)) and is subject to the Binder
transaction maximum size limit if
[`JavaScriptSandbox.JS_FEATURE_EVALUATE_WITHOUT_TRANSACTION_LIMIT`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#JS_FEATURE_EVALUATE_WITHOUT_TRANSACTION_LIMIT()) is not
supported. Non-string values must be explicitly converted to a JavaScript String
otherwise an empty string is returned. If [`JS_FEATURE_PROMISE_RETURN`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#JS_FEATURE_PROMISE_RETURN())
feature is supported, JavaScript code may alternatively return a Promise
resolving to a `String`.

For passing large byte arrays to the [`JavaScriptIsolate`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate) instance, you
can use the [`provideNamedData(...)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#provideNamedData(java.lang.String,byte%5B%5D)) API. Usage of this API is not bound by
the Binder transaction limits. Each byte array must be passed using a unique
identifier which cannot be re-used.

> [!NOTE]
> **Note:** The application must check the [`JS_FEATURE_PROVIDE_CONSUME_ARRAY_BUFFER`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#JS_FEATURE_PROVIDE_CONSUME_ARRAY_BUFFER()) feature before using this method.

    if (sandbox.isFeatureSupported(JavaScriptSandbox.JS_FEATURE_PROVIDE_CONSUME_ARRAY_BUFFER)) {
        js.provideNamedData("data-1", "Hello Android!".getBytes(StandardCharsets.US_ASCII));
        final String jsCode = "android.consumeNamedDataAsArrayBuffer('data-1').then((value) => { return String.fromCharCode.apply(null, new Uint8Array(value)); });";
        ListenableFuture<String> msg = js.evaluateJavaScriptAsync(jsCode);
        String response = msg.get(5, TimeUnit.SECONDS);
    }

## Running Wasm Code

WebAssembly (Wasm) code can be passed using the [`provideNamedData(...)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate#provideNamedData(java.lang.String,byte%5B%5D))
API, then compiled and executed in the usual manner, as demonstrated below.

    final byte[] hello_world_wasm = {
       0x00 ,0x61 ,0x73 ,0x6d ,0x01 ,0x00 ,0x00 ,0x00 ,0x01 ,0x0a ,0x02 ,0x60 ,0x02 ,0x7f ,0x7f ,0x01,
       0x7f ,0x60 ,0x00 ,0x00 ,0x03 ,0x03 ,0x02 ,0x00 ,0x01 ,0x04 ,0x04 ,0x01 ,0x70 ,0x00 ,0x01 ,0x05,
       0x03 ,0x01 ,0x00 ,0x00 ,0x06 ,0x06 ,0x01 ,0x7f ,0x00 ,0x41 ,0x08 ,0x0b ,0x07 ,0x18 ,0x03 ,0x06,
       0x6d ,0x65 ,0x6d ,0x6f ,0x72 ,0x79 ,0x02 ,0x00 ,0x05 ,0x74 ,0x61 ,0x62 ,0x6c ,0x65 ,0x01 ,0x00,
       0x03 ,0x61 ,0x64 ,0x64 ,0x00 ,0x00 ,0x09 ,0x07 ,0x01 ,0x00 ,0x41 ,0x00 ,0x0b ,0x01 ,0x01 ,0x0a,
       0x0c ,0x02 ,0x07 ,0x00 ,0x20 ,0x00 ,0x20 ,0x01 ,0x6a ,0x0b ,0x02 ,0x00 ,0x0b,
    };
    final String jsCode = "(async ()=>{" +
           "const wasm = await android.consumeNamedDataAsArrayBuffer('wasm-1');" +
           "const module = await WebAssembly.compile(wasm);" +
           "const instance = WebAssembly.instance(module);" +
           "return instance.exports.add(20, 22).toString();" +
           "})()";
    // Ensure that the name has not been used before.
    js.provideNamedData("wasm-1", hello_world_wasm);
    FluentFuture.from(js.evaluateJavaScriptAsync(jsCode))
               .transform(this::println, mainThreadExecutor)
               .catching(Throwable.class, e -> println(e.getMessage()), mainThreadExecutor);
    }

## JavaScriptIsolate Separation

All [`JavaScriptIsolate`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptIsolate) instances are independent of each other and do not
share anything. The following snippet results in

`Hi from AAA!5`

and

`Uncaught Reference Error: a is not defined`

because the "`jsTwo`" instance has no visibility of the objects created in
"`jsOne`".

    JavaScriptIsolate jsOne = engine.obtainJavaScriptIsolate();
    String jsCodeOne = "let x = 5; function a() { return 'Hi from AAA!'; } a() + x";
    JavaScriptIsolate jsTwo = engine.obtainJavaScriptIsolate();
    String jsCodeTwo = "a() + x";
    FluentFuture.from(jsOne.evaluateJavaScriptAsync(jsCodeOne))
           .transform(this::println, mainThreadExecutor)
           .catching(Throwable.class, e -> println(e.getMessage()), mainThreadExecutor);

    FluentFuture.from(jsTwo.evaluateJavaScriptAsync(jsCodeTwo))
           .transform(this::println, mainThreadExecutor)
           .catching(Throwable.class, e -> println(e.getMessage()), mainThreadExecutor);

## Kotlin Support

To use this Jetpack library with Kotlin coroutines, add a dependency to
[`kotlinx-coroutines-guava`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-guava/). This allows integration with
`ListenableFuture`.

    dependencies {
        implementation "org.jetbrains.kotlinx:kotlinx-coroutines-guava:1.6.0"
    }

The Jetpack library APIs can now be called from a coroutine scope, as
demonstrated below:

    // Launch a coroutine
    lifecycleScope.launch {
        val jsSandbox = JavaScriptSandbox
                .createConnectedInstanceAsync(applicationContext)
                .await()
        val jsIsolate = jsSandbox.createIsolate()
        val resultFuture = jsIsolate.evaluateJavaScriptAsync("PASS")

        // Await the result
        textBox.text = resultFuture.await()
        // Or add a callback
        Futures.addCallback<String>(
            resultFuture, object : FutureCallback<String?> {
                override fun onSuccess(result: String?) {
                    textBox.text = result
                }
                override fun onFailure(t: Throwable) {
                    // Handle errors
                }
            },
            mainExecutor
        )
    }

## Configuration Parameters

When requesting an isolated environment instance, you can tweak its
configuration. To tweak the configuration, pass the
[IsolateStartupParameters](https://developer.android.com/reference/kotlin/androidx/javascriptengine/IsolateStartupParameters) instance to
[`JavaScriptSandbox.createIsolate(...)`](https://developer.android.com/reference/kotlin/androidx/javascriptengine/JavaScriptSandbox#createIsolate()).

Currently parameters allow specifying the maximum heap size and the maximum size
for evaluation return values and errors.