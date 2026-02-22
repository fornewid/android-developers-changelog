---
title: https://developer.android.com/ndk/guides/symbol-visibility
url: https://developer.android.com/ndk/guides/symbol-visibility
source: md.txt
---

Controlling symbol visibility can reduce APK size, improve load times, and help
other developers avoid accidental dependencies on implementation details. The
most robust way to do this is with version scripts.

[Version scripts](https://www.gnu.org/software/gnulib/manual/html_node/LD-Version-Scripts.html) are a feature of ELF linkers that can be used as a more robust
form of `-fvisibility=hidden`. See [Benefits](https://developer.android.com/ndk/guides/symbol-visibility#benefits) below for a more
detailed explanation, or read on to learn how to use version scripts in your
project.

In the [GNU documentation](https://www.gnu.org/software/gnulib/manual/html_node/LD-Version-Scripts.html) linked above and in a few other
places on this page, you'll see references to "symbol versions". That's because
the original intent for these files was to allow multiple versions of a symbol
(usually a function) to exist in a single library for bug-compatibility
preservation in libraries. Android supports that use as well, but it's generally
only of use to OS library vendors, and even we don't use them in Android because
`targetSdkVersion` offers the same benefits with a more deliberate opt-in
process. For the topic of this doc, don't worry about terms like "symbol
version". If you're not defining multiple versions of the same symbol, "symbol
version" is just an arbitrary named grouping of symbols in the file.
| **Important:** In this document "linker" without additional qualifications refers to the [static linker](https://en.wikipedia.org/wiki/Linker_(computing)), `ld.lld`, which is run as part of the build process. The [dynamic linker](https://en.wikipedia.org/wiki/Dynamic_linker), `/system/bin/linker64`, which is the part of the Android OS that loads those libraries at run-time, will be explicitly named as such.

If you're a library author (whether your interface is C/C++, or if it's
Java/Kotlin and your native code is merely an implementation detail) rather than
an app developer, be sure to also read [Advice for middleware vendors](https://developer.android.com/ndk/guides/middleware-vendors).

## Write a version script

In the ideal case, an app (or AAR) that includes native code will contain
exactly one shared library, with all its dependencies statically linked into
that one library, and the complete public interface of that library is
`JNI_OnLoad`. This allows the [benefits](https://developer.android.com/ndk/guides/symbol-visibility#benefits) described on this page to be
applied as broadly as possible. In that case, assuming that library is named
`libapp.so`, create a `libapp.map.txt` file (the name doesn't need to match, and
the `.map.txt` suffix is just a convention) with the following contents (you can
omit the comments):

    # The name used here also doesn't matter. This is the name of the "version"
    # which matters when the version script is actually used to create multiple
    # versions of the same symbol, but that's not what we're doing.
    LIBAPP {
      global:
        # Every symbol named in this section will have "default" (that is, public)
        # visibility. See below for how to refer to C++ symbols without mangling.
        JNI_OnLoad;
      local:
        # Every symbol in this section will have "local" (that is, hidden)
        # visibility. The wildcard * is used to indicate that all symbols not listed
        # in the global section should be hidden.
        *;
    };

| **Note:** Version scripts do not apply when creating static libraries. They can be applied to the code in a static library, but that must be done downstream where the static library is consumed. The only consequence that's likely to be relevant is that if you ship a static library and require certain symbols to be visible (such as your own JNI functions), be sure to document that for the consumers of your library, because if *they* use a version script, they'll need to include your library's public symbols in their version script.

If your app has more than one shared library, you must add one version script
per library.

For JNI libraries that are not using `JNI_OnLoad` and `RegisterNatives()`, you
can instead list each of the JNI methods with their JNI mangled names.
| **Tip:** If you're not already using `RegisterNatives()`, you probably should be! See [the
| Native Libraries section of JNI tips](https://developer.android.com/training/articles/perf-jni#native-libraries) for more information.

For non-JNI libraries (dependencies of JNI libraries, typically), you'll need to
enumerate your full API surface. If your interface is C++ rather than C, you can
use `extern "C++" { ... }` in a version script the same way you would in a
header file. For example:

    LIBAPP {
      global:
        extern "C++" {
          # A class that exposes only some methods. Note that any methods that are
          # `private` in the class will still need to be visible in the library if
          # they are called by `inline` or `template` functions.
          #
          # Non-static members do not need to be enumerated as they do not have
          # symbols associated with them, but static members must be included.
          #
          # The * exposes all overloads of the MyClass constructor, but note that it
          # will also expose methods like MyClass::MyClassNonConstructor.
          MyClass::MyClass*;
          MyClass::DoSomething;
          MyClass::static_member;

          # All members/methods of a class, including those that are `private` in
          # the class.
          MyOtherClass::*;
          #

          # If you wish to only expose some overloads, name the full signature.
          # You'll need to wrap the name in quotes, otherwise you'll get a warning
          # like "ignoring invalid character '(' in script" and the symbol will
          # remain hidden (pass -Wl,--no-undefined-version to convert that warning
          # to an error as described below).
          "MyClass::MyClass()";
          "MyClass::MyClass(const MyClass&)";
          "MyClass::~MyClass()";
        };
      local:
        *;
    };

## Use the version script when building

The version script must be passed to the linker when building. Follow the steps
appropriate to your build system below.

### CMake

    # Assuming that your app library's target is named "app":
    target_link_options(app
        PRIVATE
        -Wl,--version-script,${CMAKE_SOURCE_DIR}/libapp.map.txt
        # This causes the linker to emit an error when a version script names a
        # symbol that is not found, rather than silently ignoring that line.
        -Wl,--no-undefined-version
    )

    # Without this, changes to the version script will not cause the library to
    # relink.
    set_target_properties(app
        PROPERTIES
        LINK_DEPENDS ${CMAKE_SOURCE_DIR}/libapp.map.txt
    )

### ndk-build

    # Add to an existing `BUILD_SHARED_LIBRARY` stanza (use `+=` instead of `:=` if
    # the module already sets `LOCAL_LDFLAGS`):
    LOCAL_LDFLAGS := -Wl,--version-script,$(LOCAL_PATH)/libapp.map.txt

    # This causes the linker to emit an error when a version script names a symbol
    # that is not found, rather than silently ignoring that line.
    LOCAL_ALLOW_UNDEFINED_VERSION_SCRIPT_SYMBOLS := false

    # ndk-build doesn't have a mechanism for specifying that libapp.map.txt is a
    # dependency of the module. You may need to do a clean build or otherwise force
    # the library to rebuild (such as by changing a source file) when altering the
    # version script.

### Other

If the build system you're using has explicit support for version scripts, use
that.

Otherwise, use the following linker flags:

    -Wl,--version-script,path/to/libapp.map.txt -Wl,--no-version-undefined

How those are specified will depend on your build system, but there's typically
an option named `LDFLAGS` or something similar. `path/to/libapp.map.txt` needs
to be resolvable from the current working directory of the linker. It's often
easier to use an absolute path.

If you're not using a build system, or are a build system maintainer looking to
add version script support, those flags should be passed to `clang` (or
`clang++`) when linking but not when compiling.

## Benefits

APK size can be improved when using a version script because it minimizes the
visible set of symbols in a library. By telling the linker exactly which
functions are accessible to callers, the linker can remove all the unreachable
code from the library. This process is a type of [dead-code elimination](https://en.wikipedia.org/wiki/Dead-code_elimination). The
linker cannot remove the definition for function (or other symbol) that is not
hidden, even if the function is never called, because the linker must assume
that a visible symbol is a part of the library's public interface. Hiding
symbols allows the linker to remove functions that are not called, reducing the
size of the library.

Library load performance is improved for similar reasons: [relocations](https://en.wikipedia.org/wiki/Relocation_(computing)) are
required for visible symbols because those symbols are [interposable](https://developer.android.com/ndk/guides/that's%0Ahow%20behaviors%20like%20%60operator%20new%60%20and%20%60operator%20delete%60%20replacement%20work).
That's almost never the desired behavior, but it what's required by the ELF
specification, so it's the default. but because the linker can't know which (if
any) symbols you intend to be interposable, it must create relocations for every
visible symbol. Hiding those symbols allows the linker to omit those relocations
in favor of direct jumps, which reduces the amount of work the dynamic linker
must do when loading libraries.

Explicitly enumerating your API surface also prevents consumers of your
libraries from mistakenly depending on implementation details of your library,
as those details won't be visible.

## Comparison with alternatives

Version scripts offer similar results as alternatives such as
`-fvisibility=hidden` or per-function `__attribute__((visibility("hidden")))`.
All three approaches control which symbols of a library are visible to other
libraries and to `dlsym`.

The biggest downside to the other two approaches is that they are only able to
hide symbols defined in the library being built. They cannot hide symbols from
static library dependencies of the library. A very common case where this makes
a difference is when using `libc++_static.a`. Even if your build uses
`-fvisibility=hidden`, while the library's own symbols will be hidden, all the
symbols included from `libc++_static.a` will become public symbols of your
library. In contrast, version scripts offer explicit control of the public
interface of the library; if the symbol is not explicitly listed as visible in
the version script, it will be hidden.

The other difference can be both a pro and a con: the public interface of the
library must be explicitly defined in a version script. For JNI libraries this
is actually trivial, because the only necessary interface for a JNI library is
`JNI_OnLoad` (because JNI methods registered with `RegisterNatives()` need not
be public). For libraries with a large public interface this can be an
additional maintenance burden, but one that's usually worthwhile.