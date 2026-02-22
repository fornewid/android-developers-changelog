---
title: https://developer.android.com/ndk/guides/using-newer-apis
url: https://developer.android.com/ndk/guides/using-newer-apis
source: md.txt
---

This page explains how your app can use new OS functionality when running on new
OS versions while preserving compatibility with older devices.
| **Key Point:** Most developers should enable this feature. It is not the default for the reasons explained in [Why isn't this the default](https://developer.android.com/ndk/guides/using-newer-apis#why_isnt_this_the_default), but if you're writing code for Android, rather than porting non-Android code, this will make it easier.

By default, references to NDK APIs in your application are strong references.
Android's dynamic loader will eagerly try to resolve them when your library is
loaded. If the symbols are not found, the app will abort. This is contrary to
how Java behaves, where an exception won't be thrown until the missing API is
called.

For this reason, the NDK will prevent you from creating strong references to
APIs that are newer than your app's `minSdkVersion`. This protects you from
accidentally shipping code that worked during your testing but will fail to load
(`UnsatisfiedLinkError` will be thrown from `System.loadLibrary()`) on older
devices. On the other hand, it is more difficult to write code that uses APIs
newer than your app's `minSdkVersion`, because you must call the APIs using
`dlopen()` and `dlsym()` rather than a normal function call.

The alternative to using strong references is using weak references. If a weak
reference is not found when a library is loaded, the address of that symbol will
be set to `nullptr` instead of causing the library to fail to load. They still
cannot be safely called, but as long as callsites are guarded to prevent calling
the API when it is not available, the rest of your code can be run, and you can
call the API normally without needing to use `dlopen()` and `dlsym()`.
| **Note:** If you're familiar with lazy binding on other systems (which you get by calling `dlopen()` with the `RTLD_LAZY` flag, or linking with `-z lazy`), weak symbols offer similar behavior but have some important differences that are beneficial for hardening and debugging. With lazy loading the symbol is not looked up until reaching the callsite. Failure to find the symbol at that point is still fatal, and the deferred lookup makes performance less predictable. Weak symbols are still eagerly resolved during library load, but failure to find a symbol results in the function's address being `nullptr` rather than an error. The downside to weak symbols over lazy loading is that if you do incorrectly call an unavailable API the app will segfault without a clear error message, whereas a lazily bound reference would emit a clear error to the log. Fortunately, Clang can diagnose this mistake at build time, so when built with the correct flags (see below), this downside is easily avoided in practice. Android's dynamic linker does not support lazy loading because lazy binding inhibits hardening features like RELRO.

Weak API references don't require additional support from the dynamic linker,
so they can be used with any version of Android.

## Enabling weak API references in your build

| **Warning:** Using this feature circumvents build-time checks that you've linked the appropriate libraries for the affected APIs. If, for example, your `minSdkVersion` is 21 and you call `ANativeWindow_getBuffersDefaultDataSpace()` but forget to link against libnativewindow, your app will build successfully, `__builtin_available()` will return true, but your app will crash when `ANativeWindow_getBuffersDefaultDataSpace()` is called. **The only defense
| against this problem is testing.**

### CMake

Pass `-DANDROID_WEAK_API_DEFS=ON` when running CMake. If you're using CMake via
`externalNativeBuild`, add the following to your `build.gradle.kts` (or the
Groovy equivalent if you're still using `build.gradle`):

    android {
        // Other config...

        defaultConfig {
            // Other config...

            externalNativeBuild {
                cmake {
                    arguments.add("-DANDROID_WEAK_API_DEFS=ON")
                    // Other config...
                }
            }
        }
    }

### ndk-build

Add the following to your `Application.mk` file:

    APP_WEAK_API_DEFS := true

If you do not already have an `Application.mk` file, create it in the same
directory as your `Android.mk` file. Additional changes to your
`build.gradle.kts` (or `build.gradle`) file are not necessary for ndk-build.

### Other build systems

If you're not using CMake or ndk-build, consult the documentation for your build
system to see if there's a recommended way to enable this feature. If your build
system doesn't support this option natively, you can enable the feature by
passing the following flags when compiling:

    -D__ANDROID_UNAVAILABLE_SYMBOLS_ARE_WEAK__ -Werror=unguarded-availability

The first configures the NDK headers to allow weak references. The second turns
the warning for unsafe API calls into an error.

See the [Build System Maintainers Guide](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md) for more information.

## Guarded API calls

This feature does not magically make calls to new APIs safe. The only thing it
does is defer a load-time error to a call-time error. The benefit is that you
can guard that call at runtime and fall back gracefully, whether by using an
alternative implementation or notifying the user that that feature of the app is
not available on their device, or avoiding that code path entirely.

Clang can emit a warning (`unguarded-availability`) when you make an unguarded
call to an API that isn't available for your app's `minSdkVersion`. If you're
using ndk-build or our CMake toolchain file, that warning will be automatically
enabled and promoted to an error when enabling this feature.
| **Caution:** Be careful when enabling this feature for code which was not written with Android in mind. In particular [configure](https://en.wikipedia.org/wiki/Configure_script)-style checks for APIs will most likely detect APIs as available when this feature is enabled (it depends on how the specific system determines availability), but that code almost certainly does not include the necessary runtime check to make the call safe. Be sure that `-Werror=unguarded-availability` is used and not suppressed: make sure no flags which would disable that error (`-Wno-unguarded-availability`, `-Wno-error=unguarded-availability`, `-Wno-error`, and `-w` would all do it, but may not be a complete list) appear after the initial `-Werror=unguarded-availability`.

Here is an example of some code that makes conditional use of an API without
this feature enabled, using `dlopen()` and `dlsym()`:

    void LogImageDecoderResult(int result) {
        void* lib = dlopen("libjnigraphics.so", RTLD_LOCAL);
        CHECK_NE(lib, nullptr) << "Failed to open libjnigraphics.so: " << dlerror();
        auto func = reinterpret_cast<decltype(&AImageDecoder_resultToString)>(
            dlsym(lib, "AImageDecoder_resultToString")
        );
        if (func == nullptr) {
            LOG(INFO) << "cannot stringify result: " << result;
        } else {
            LOG(INFO) << func(result);
        }
    }

It's a bit messy to read, there's some duplication of function names (and if
you're writing C, the signatures as well), it'll build successfully but always
take the fallback at runtime if you accidentally typo the function name passed
to `dlsym`, and you have to use this pattern for every API.

With weak API references, the function above can be rewritten as:

    void LogImageDecoderResult(int result) {
        if (__builtin_available(android 31, *)) {
            LOG(INFO) << AImageDecoder_resultToString(result);
        } else {
            LOG(INFO) << "cannot stringify result: " << result;
        }
    }

Under the hood, `__builtin_available(android 31, *)` calls
`android_get_device_api_level()`, caches the result, and compares it with `31`
(which is the API level that introduced `AImageDecoder_resultToString()`).
| **Note:** The `*` argument signifies that the API is unconditionally available for non-Android targets. In rare cases where the API in question is portable across a variety of platforms (obviously iOS will not have Android-specific APIs and vice-versa, but some libraries like libc will have considerable overlap), you can list multiple platforms in a single `__builtin_available()` (for example, `__builtin_available(android 31, iOS 10.0, *)`). In practice, you're unlikely to ever have a need to do that.

The simplest way to determine which value to use for `__builtin_available` is to
attempt to build without the guard (or a guard of
`__builtin_available(android 1, *)`) and do what the error message tells you.
For example, an unguarded call to `AImageDecoder_createFromAAsset()` with
`minSdkVersion 24` will produce:

    error: 'AImageDecoder_createFromAAsset' is only available on Android 30 or newer [-Werror,-Wunguarded-availability]

In this case the call should be guarded by `__builtin_available(android 30, *)`.
If there is no build error, either the API is always available for your
`minSdkVersion` and no guard is needed, or your build is misconfigured and the
`unguarded-availability` warning is disabled.

Alternatively, the NDK API reference will say something along the lines of
"Introduced in API 30" for each API. If that text is not present, it means that
the API is available for all supported API levels.

## Avoiding repetition of API guards

If you're using this, you will probably have sections of code in your app that
are only usable on new enough devices. Rather than repeating the
`__builtin_available()` check in each of your functions, you can annotate your
own code as requiring a certain API level. For example, the ImageDecoder APIs
themselves were added in API 30, so for functions that make heavy use of those
APIs you can do something like:

    #define REQUIRES_API(x) __attribute__((__availability__(android,introduced=x)))
    #define API_AT_LEAST(x) __builtin_available(android x, *)

    void DecodeImageWithImageDecoder() REQUIRES_API(30) {
        // Call any APIs that were introduced in API 30 or newer without guards.
    }

    void DecodeImageFallback() {
        // Pay the overhead to call the Java APIs via JNI, or use third-party image
        // decoding libraries.
    }

    void DecodeImage() {
        if (API_AT_LEAST(30)) {
            DecodeImageWithImageDecoder();
        } else {
            DecodeImageFallback();
        }
    }

## Quirks of API guards

Clang is very particular about how `__builtin_available` is used. Only a literal
(though possibly macro-replaced) `if (__builtin_available(...))` works. Even
trivial operations like `if (!__builtin_available(...))` will not work (Clang
will emit the `unsupported-availability-guard` warning, as well as
`unguarded-availability`). This may improve in a future version of Clang. See
[LLVM Issue 33161](https://github.com/llvm/llvm-project/issues/33161) for more information.

Checks for `unguarded-availability` only apply to the function scope where they
are used. Clang will emit the warning even if the function with the API call is
only ever called from within a guarded scope. To avoid repetition of guards in
your own code, see [Avoiding repetition of API guards](https://developer.android.com/ndk/guides/using-newer-apis#avoiding_repetition_of_api_guards).

## Why isn't this the default?

Unless used correctly, the difference between strong API references and weak API
references is that the former will fail quickly and obviously, whereas the
latter will not fail until the user takes an action that causes the missing API
to be called. When this happens, the error message will not be a clear
compile- time "AFoo_bar() is not available" error, it will be a segfault. With
strong references, the error message is much clearer, and failing-fast is a
safer default.

Because this is a new feature, very little existing code is written to handle
this behavior safely. Third-party code that was not written with Android in mind
will likely always have this problem, so there are currently no plans for the
default behavior to ever change.

We **do** recommend that you use this, but as it will make problems more
difficult to detect and debug, you should accept those risks knowingly rather
than the behavior changing without your knowledge.

## Caveats

This feature works for most APIs, but there are a few cases where it does not
work.

Prior to NDK r28, this did not work for libc or libm APIs.

The case that more developers are likely to encounter is when the *library* that
contains the new API is newer than your `minSdkVersion`. This feature only
enables weak symbol references; there is no such thing as a weak library
reference. For example, if your `minSdkVersion` is 24, you can link
`libvulkan.so` and make a guarded call to `vkBindBufferMemory2`, because
`libvulkan.so` is available on devices starting with API 24. On the other hand,
if your `minSdkVersion` were 23, you must fall back to `dlopen` and `dlsym`
because the library will not exist on the device on devices that only support
API 23. We don't know of a good solution for fixing this case, but in the long
term it will resolve itself because we (whenever possible) no longer allow new
APIs to create new libraries.

## For library authors

If you are developing a library to be used in Android applications, you should
avoid using this feature in your public headers. It can be safely used in
out-of-line code, but if you rely on `__builtin_available` in any code in your
headers, such as inline functions or template definitions, you force all your
consumers to enable this feature. For the same reasons we do not enable this
feature by default in the NDK, you should avoid making that choice on the behalf
of your consumers.

If you do require this behavior in your public headers, make sure to document
that so your users both know that they will need to enable the feature and are
aware of the risks of doing so.