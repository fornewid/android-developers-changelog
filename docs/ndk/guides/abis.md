---
title: https://developer.android.com/ndk/guides/abis
url: https://developer.android.com/ndk/guides/abis
source: md.txt
---

Different Android devices use different CPUs, which in turn support different
instruction sets. Each combination of CPU and instruction set has its own
Application Binary Interface (ABI). An ABI includes the following information:

- The CPU instruction set (and extensions) that can be used.
- The endianness of memory stores and loads at runtime. Android is always little-endian.
- Conventions for passing data between applications and the system, including alignment constraints, and how the system uses the stack and registers when it calls functions.
- The format of executable binaries, such as programs and shared libraries, and the types of content they support. Android always uses ELF. For more information, see [ELF System V Application Binary Interface](https://refspecs.linuxfoundation.org/elf/gabi4+/contents.html).
- How C++ names are mangled. For more information, see [Generic/Itanium C++ ABI](http://itanium-cxx-abi.github.io/cxx-abi/).

This page enumerates the ABIs that the NDK supports, and provides information
about how each ABI works.

ABI can also refer to the native API supported by the platform. For a
list of those kinds of ABI issues affecting 32-bit systems, see
[32-bit ABI bugs](https://android.googlesource.com/platform/bionic/+/master/docs/32-bit-abi.md).

## Supported ABIs


**Table 1.** ABIs and supported instruction sets.

| ABI | Supported Instruction Sets | Notes |
|---|---|---|
| [`armeabi-v7a`](https://developer.android.com/ndk/guides/abis#v7a) | - armeabi - Thumb-2 - Neon | Incompatible with ARMv5/v6 devices. |
| [`arm64-v8a`](https://developer.android.com/ndk/guides/abis#arm64-v8a) | - AArch64 | Armv8.0 only. |
| [`x86`](https://developer.android.com/ndk/guides/abis#x86) | - x86 (IA-32) - MMX - SSE/2/3 - SSSE3 | No support for MOVBE or SSE4. |
| [`x86_64`](https://developer.android.com/ndk/guides/abis#86-64) | - x86-64 - MMX - SSE/2/3 - SSSE3 - SSE4.1, 4.2 - POPCNT - CMPXCHG16B - LAHF-SAHF | Full [x86-64-v2](https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels). |

**Note:** Historically the NDK supported ARMv5
(armeabi), and 32-bit and 64-bit MIPS, but support for these ABIs was removed in
NDK r17.

### armeabi-v7a

This ABI is for 32-bit ARM CPUs. It includes Thumb-2 and Neon.

For information about the parts of the ABI that aren't Android-specific, see
[Application Binary Interface (ABI) for the ARM Architecture](https://developer.arm.com/architectures/system-architectures/software-standards/abi)

The NDK's build systems generate Thumb-2 code by default unless you use
`LOCAL_ARM_MODE` in your [`Android.mk`](https://developer.android.com/ndk/guides/android_mk) for
ndk-build or `ANDROID_ARM_MODE` when configuring [CMake](https://developer.android.com/ndk/guides/cmake).

For more information on the history of Neon, see [Neon Support](https://developer.android.com/ndk/guides/cpu-arm-neon).

For historical reasons, this ABI uses `-mfloat-abi=softfp` causing all `float`
values to be passed in integer registers and all `double` values to be passed
in integer register pairs when making function calls. Despite the name, this
only affects the floating point *calling convention*: the compiler will still
use hardware floating point instructions for arithmetic.

This ABI uses a 64-bit `long double` ([IEEE binary64](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) the same as `double`).

### arm64-v8a

This ABI is for 64-bit ARM CPUs.

See Arm's
[Learn the Architecture](https://developer.arm.com/architectures/learn-the-architecture)
for complete details of the parts of the ABI that aren't Android-specific. Arm
also offers some porting advice in
[64-bit Android Development](https://developer.arm.com/64bit).

You can use [Neon intrinsics](https://developer.arm.com/architectures/instruction-sets/simd-isas/neon/intrinsics)
in C and C++ code to take advantage of the Advanced SIMD extension. The
[Neon Programmer's Guide for Armv8-A](https://developer.arm.com/architectures/instruction-sets/simd-isas/neon/neon-programmers-guide-for-armv8-a)
provides more information about Neon intrinsics and Neon programming in general.

On Android, the platform-specific x18 register is reserved for
[ShadowCallStack](https://source.android.com/devices/tech/debug/shadow-call-stack)
and should not be touched by your code. Current versions of Clang default to
using the `-ffixed-x18` option on Android, so unless you have hand-written
assembler (or a very old compiler) you shouldn't need to worry about this.

This ABI uses a 128-bit `long double` ([IEEE binary128](https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format)).

### x86

This ABI is for CPUs supporting the instruction set commonly known as "x86",
"i386", or "IA-32".

Android's ABI includes the base instruction set plus
the [MMX](https://en.wikipedia.org/wiki/MMX_%28instruction_set%29),
[SSE](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions),
[SSE2](https://en.wikipedia.org/wiki/SSE2),
[SSE3](https://en.wikipedia.org/wiki/SSE3), and
[SSSE3](https://en.wikipedia.org/wiki/SSSE3) extensions.

The ABI does not include any other optional IA-32 instruction set
extensions such as MOVBE or any variant of SSE4.
You can still use these extensions, as long as you use runtime feature-probing to
enable them, and provide fallbacks for devices that do not support them.

The NDK toolchain assumes 16-byte stack alignment before a function call. The default tools and
options enforce this rule. If you are writing assembly code, you must make sure to maintain stack
alignment, and ensure that other compilers also obey this rule.

Refer to the following documents for more details:

- [Calling
  conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf)
- [Intel IA-32 Intel Architecture Software Developer's Manual, Volume 2:
  Instruction Set Reference](http://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-instruction-set-reference-manual-325383.pdf)
- [Intel
  IA-32 Intel Architecture Software Developer's Manual, Volume 3: System
  Programming Guide](http://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-system-programming-manual-325384.pdf)
- [System V Application Binary
  Interface: Intel386 Processor Architecture Supplement](http://www.sco.com/developers/devspecs/abi386-4.pdf)

This ABI uses a 64-bit `long double` ([IEEE binary64](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) the same as `double`, and not the more
common 80-bit Intel-only `long double`).

### x86_64

This ABI is for CPUs supporting the instruction set commonly referred to as
"x86-64".

Android's ABI includes the base instruction set plus
[MMX](https://en.wikipedia.org/wiki/MMX_%28instruction_set%29),
[SSE](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions),
[SSE2](https://en.wikipedia.org/wiki/SSE2),
[SSE3](https://en.wikipedia.org/wiki/SSE3),
[SSSE3](https://en.wikipedia.org/wiki/SSSE3),
[SSE4.1](https://en.wikipedia.org/wiki/SSE4#SSE4.1),
[SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2), and
the POPCNT instruction.

The ABI does not include any other optional x86-64 instruction set
extensions such as MOVBE, SHA, or any variant of AVX.
You can still use these extensions, as long as you use runtime feature probing to
enable them, and provide fallbacks for devices that do not support them.

Refer to the following documents for more details:

- [Calling conventions for
  different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf)
- [Intel64 and IA-32 Architectures Software Developer's Manual, Volume 2: Instruction Set
  Reference](http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html?iid=tech_vt_tech+64-32_manuals)
- [Intel64 and IA-32 Intel Architecture Software Developer's Manual Volume 3: System Programming](http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html?iid=tech_vt_tech+64-32_manuals)

This ABI uses a 128-bit `long double` ([IEEE binary128](https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format)).

## Generate code for a specific ABI

### Gradle

Gradle (whether used via Android Studio or from the command line) builds for
all non-deprecated ABIs by default. To restrict the set of ABIs that your
application supports, use `abiFilters`. For example, to build for only
64-bit ABIs, set the following configuration in your `build.gradle`:

    android {
        defaultConfig {
            ndk {
                abiFilters 'arm64-v8a', 'x86_64'
            }
        }
    }

### ndk-build

ndk-build builds for all non-deprecated ABIs by default. You can target a
specific ABIs by setting `APP_ABI` in your [Application.mk](https://developer.android.com/ndk/guides/application_mk) file. The
following snippet shows a few examples of using `APP_ABI`:

    APP_ABI := arm64-v8a  # Target only arm64-v8a
    APP_ABI := all  # Target all ABIs, including those that are deprecated.
    APP_ABI := armeabi-v7a x86_64  # Target only armeabi-v7a and x86_64.

For more information on the values you can specify for `APP_ABI`, see
[Application.mk](https://developer.android.com/ndk/guides/application_mk).

### CMake

With CMake, you build for a single ABI at a time and must specify your ABI
explicitly. You do this with the `ANDROID_ABI` variable, which must be
specified on the command line (cannot be set in your CMakeLists.txt). For
example:

    $ cmake -DANDROID_ABI=arm64-v8a ...
    $ cmake -DANDROID_ABI=armeabi-v7a ...
    $ cmake -DANDROID_ABI=x86 ...
    $ cmake -DANDROID_ABI=x86_64 ...

For the other flags that must be passed to CMake to build with the NDK, see
the [CMake guide](https://developer.android.com/ndk/guides/cmake).

The default behavior of the build system is to include the binaries for each ABI
in a single APK, also known as a [fat APK](https://en.wikipedia.org/wiki/Fat_binary). A fat APK is significantly larger
than one containing only the binaries for a single ABI; the tradeoff is gaining
wider compatibility, but at the expense of a larger APK. It is strongly
recommended that you take advantage of either [App Bundles](https://developer.android.com/guide/app-bundle) or [APK Splits](https://developer.android.com/studio/build/configure-apk-splits) to
reduce the size of your APKs while still maintaining maximum device
compatibility.

At installation time, the package manager unpacks only the most appropriate
machine code for the target device. For details, see [Automatic extraction of
native code at install time](https://developer.android.com/ndk/guides/abis#aen).

## ABI management on the Android platform

This section provides details about how the Android platform manages native
code in APKs.

### Native code in app packages

Both the Play Store and Package Manager expect to find NDK-generated
libraries on filepaths inside the APK matching the following pattern:

```
/lib/<abi>/lib<name>.so
```

Here, `<abi>` is one of the ABI names listed under [Supported ABIs](https://developer.android.com/ndk/guides/abis#sa),
and `<name>` is the name of the library as you defined it for the `LOCAL_MODULE`
variable in the [`Android.mk`](https://developer.android.com/ndk/guides/android_mk) file. Since
APK files are just zip files, it is trivial to open them and confirm that the shared native
libraries are where they belong.

If the system does not find the native shared libraries where it expects them, it cannot use
them. In such a case, the app itself has to copy the libraries over, and then
perform `dlopen()`.

In a fat APK, each library resides under a directory whose name matches a corresponding ABI.
For example, a fat APK may contain:

```
/lib/armeabi/libfoo.so
/lib/armeabi-v7a/libfoo.so
/lib/arm64-v8a/libfoo.so
/lib/x86/libfoo.so
/lib/x86_64/libfoo.so
```

**Note:** ARMv7-based Android devices running 4.0.3 or earlier
install native libraries from the `armeabi` directory instead of the `armeabi-v7a`
directory if both directories exist. This is because `/lib/armeabi/` comes after
`/lib/armeabi-v7a/` in the APK. This issue is fixed from 4.0.4.

### Android platform ABI support

The Android system knows at runtime which ABI(s) it supports, because build-specific system
properties indicate:

- The primary ABI for the device, corresponding to the machine code used in the system image itself.
- Optionally, secondary ABIs, corresponding to other ABI that the system image also supports.

This mechanism ensures that the system extracts the best machine code from
the package at installation time.

For best performance, you should compile directly for the primary ABI. For example, a
typical ARMv5TE-based device would only define the primary ABI: `armeabi`. By contrast, a
typical, ARMv7-based device would define the primary ABI as `armeabi-v7a` and the secondary
one as `armeabi`, since it can run application native binaries generated for each of them.

64-bit devices also support their 32-bit variants. Using arm64-v8a devices
as an example, the device can also run armeabi and armeabi-v7a code. Note,
however, that your application will perform much better on 64-bit devices if it
targets arm64-v8a rather than relying on the device running the armeabi-v7a
version of your application.

Many x86-based devices can also run `armeabi-v7a` and `armeabi` NDK binaries. For
such devices, the primary ABI would be `x86`, and the second one, `armeabi-v7a`.

You can force install an apk for a specific [ABI](https://developer.android.com/ndk/guides/abis#sa).
This is useful for testing. Use the following command:

```
adb install --abi abi-identifier path_to_apk
```

<br />

### Automatic extraction of native code at install time

When installing an application, the package manager service scans the APK, and looks for any
shared libraries of the form:

```
lib/<primary-abi>/lib<name>.so
```

If none is found, and you have defined a secondary ABI, the service scans for shared libraries of
the form:

```
lib/<secondary-abi>/lib<name>.so
```

When it finds the libraries that it's looking for, the package manager copies
them to `/lib/lib<name>.so`, under the application's native library directory
(`<nativeLibraryDir>/`). The following snippets retrieve the `nativeLibraryDir`:

### Kotlin

```kotlin
import android.content.pm.PackageInfo
import android.content.pm.ApplicationInfo
import android.content.pm.PackageManager
...
val ainfo = this.applicationContext.packageManager.getApplicationInfo(
        "com.domain.app",
        PackageManager.GET_SHARED_LIBRARY_FILES
)
Log.v(TAG, "native library dir ${ainfo.nativeLibraryDir}")
```

### Java

```java
import android.content.pm.PackageInfo;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
...
ApplicationInfo ainfo = this.getApplicationContext().getPackageManager().getApplicationInfo
(
    "com.domain.app",
    PackageManager.GET_SHARED_LIBRARY_FILES
);
Log.v( TAG, "native library dir " + ainfo.nativeLibraryDir );
```

If there is no shared-object file at all, the application builds and installs, but crashes at
runtime.

## ARMv9: Enabling PAC and BTI for C/C++

| **Important:** PAC and BTI are two of many tools available for memory debugging and mitigation. See [Memory error debugging and mitigation](https://developer.android.com/ndk/guides/memory-debug) for an overview of all the tools.

Enabling PAC/BTI will provide protection against some attack vectors.
PAC protects return addresses by cryptographically signing them in a function's
prolog and checking that the return address is still correctly signed in the
epilog. BTI prevents jumping to arbitrary locations in your code by requiring
that each branch target is a special instruction that does nothing but tell
the processor that it's okay to land there.

Android uses PAC/BTI instructions that do nothing on older processors that
don't support the new instructions. Only ARMv9 devices will have the PAC/BTI
protection, but you can run the same code on ARMv8 devices too: no need for
multiple variants of your library. Even on ARMv9 devices, PAC/BTI only applies
to 64-bit code.

Enabling PAC/BTI will cause a slight increase in code size, typically 1%.

See Arm's [Learn the architecture - Providing protection for
complex software](https://developer.arm.com/documentation/102433/0100/Overview)
([PDF](https://documentation-service.arm.com/static/62bdb1d031ea212bb66257c5?token))
for a detailed explanation of the attack vectors PAC/BTI target, and how
the protection works.

### Build changes

| **Note:** When considering the code to be a target for attackers, we recommend also building with CFI. CFI and PAC/BTI are similar but complementary.

### ndk-build

Set `LOCAL_BRANCH_PROTECTION := standard` in each module of your Android.mk.

### CMake

Use `target_compile_options($TARGET PRIVATE -mbranch-protection=standard)`
for each target in your CMakeLists.txt.

### Other build systems

Compile your code using `-mbranch-protection=standard`. This flag only works
when compiling for the arm64-v8a ABI. You don't need to use this flag when
linking.

### Troubleshooting

We are not aware of any issues with the compiler support for PAC/BTI, but:

- Take care not to mix BTI and non-BTI code when linking, because that results in a library that doesn't have BTI protection enabled. You can use llvm-readelf to check whether your resulting library has the BTI note or not.

```
$ llvm-readelf --notes LIBRARY.so
[...]
Displaying notes found in: .note.gnu.property
  Owner                Data size    Description
  GNU                  0x00000010   NT_GNU_PROPERTY_TYPE_0 (property note)
    Properties:    aarch64 feature: BTI, PAC
[...]
$
```

- Old versions of OpenSSL (prior to 1.1.1i) have a bug in hand-written assembler
  that causes PAC failures. Upgrade to the current OpenSSL.

- Old versions of some app DRM systems generate code that violates PAC/BTI
  requirements. If you're using app DRM and see issues when enabling PAC/BTI,
  contact your DRM vendor for a fixed version.