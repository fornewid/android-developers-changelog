---
title: https://developer.android.com/ndk/guides/common-problems
url: https://developer.android.com/ndk/guides/common-problems
source: md.txt
---

# Common problems and solutions

This document is a partial list of the most commonly encountered non-bugs you might encounter when using the NDK, and their solutions (if available).

## Using`_FILE_OFFSET_BITS=64`with older API levels

Prior to[unified headers](https://android.googlesource.com/platform/ndk/+/master/docs/UnifiedHeaders.md), the NDK did not support`_FILE_OFFSET_BITS=64`. If you defined it when building your app, it was silently ignored. The`_FILE_OFFSET_BITS=64`option is now supported with unified headers, but on old versions of Android very few of the`off_t`APIs were available as an`off64_t`variant. Therefore, using this feature with old API levels results in fewer functions being available.

This problem is explained in detail in the[r16 blog post](https://android-developers.googleblog.com/2017/09/introducing-android-native-development.html)and in the[bionic documentation](https://android.googlesource.com/platform/bionic/+/master/docs/32-bit-abi.md).

**Problem** : Your build is asking for APIs that do not exist in your`minSdkVersion`.

**Solution** : Disable`_FILE_OFFSET_BITS=64`or raise your`minSdkVersion`.

### Undeclared or implicit definition of`mmap`

You may see the following error in C++:
> error: use of undeclared identifier 'mmap'

or the following error in C:
> warning: implicit declaration of function 'mmap' is invalid in C99

Using`_FILE_OFFSET_BITS=64`instructs the C library to use`mmap64`instead of`mmap`.`mmap64`was not available until`android-21`. If your`minSdkVersion`value is lower than 21, the C library does not contain an`mmap`that is compatible with`_FILE_OFFSET_BITS=64`, so the function is unavailable.
| **Note:** `mmap`is only the most common manifestation of this problem. The same is true of any function in the C library that has an`off_t`parameter.
| **Note:** Since r16 beta 2, the C library exposes`mmap64`as an inline function to mitigate this instance of this issue.

## `minSdkVersion`set higher than device API level

The API level you build against with the NDK has a very different meaning than`compileSdkVersion`does for Java. The NDK API level is your app's**minimum** supported API level. In ndk-build, this is your`APP_PLATFORM`setting. With CMake, this is`-DANDROID_PLATFORM`.
| **Note:** If you're using[externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/current/com/android/build/api/dsl/ExternalNativeBuild), it automatically uses your`minSdkVersion`.

Since references to functions are typically resolved when libraries are loaded rather than when they are first called, you cannot reference APIs that are not always present and guard their use with API level checks. If they are referred to at all, they must be present.

**Problem**: Your NDK API level is higher than the API supported by your device.

**Solution** : Set your NDK API level (`APP_PLATFORM`) to the minimum version of Android your app supports.

|                                                             Build System                                                              |         Setting         |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| [ndk-build](https://developer.android.com/ndk/guides/application_mk)                                                                  | `APP_PLATFORM`          |
| [CMake](https://developer.android.com/ndk/guides/cmake)                                                                               | `ANDROID_PLATFORM`      |
| [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/current/com/android/build/api/dsl/ExternalNativeBuild) | `android.minSdkVersion` |

For other build systems, see[Use the NDK with other build systems](https://developer.android.com/ndk/guides/other_build_systems).

### Cannot locate`__aeabi`Symbols

The following message:
> UnsatisfiedLinkError: dlopen failed: cannot locate symbol "`__aeabi_memcpy`"

is one example of possible*runtime* errors. These errors appear in the log when you attempt to load your native libraries. The symbol might be any of`__aeabi_*`;`__aeabi_memcpy`and`__aeabi_memclr`seem to be the most common.

This problem is documented in[Issue 126](https://github.com/android-ndk/ndk/issues/126)

### Cannot locate symbol`rand`

For the following error log message:
> UnsatisfiedLinkError: dlopen failed: cannot locate symbol "`rand`"

See this detailed[Stack Overflow answer](http://stackoverflow.com/a/27338365/632035).

## Undefined reference to`__atomic_*`

**Problem** : Some ABIs need`libatomic`to provide some implementations for atomic operations.

**Solution** : Add`-latomic`when linking.

For the following error message:
> error: undefined reference to '`__atomic_exchange_4`'

the actual symbol here might be anything prefixed with`__atomic_`.
| **Note:** ndk-build and CMake handle this for you. For other build systems, you may need to do this manually.

## RTTI/exceptions not working across library boundaries

**Problem** : Exceptions are not being caught when thrown across shared library boundaries, or`dynamic_cast`is failing.

**Solution** : Add a[key function](https://itanium-cxx-abi.github.io/cxx-abi/abi.html#vague-vtable)to your types. A key function is the first non-pure, out-of-line virtual function for a type. For an example, see the discussion on[Issue 533](https://github.com/android-ndk/ndk/issues/533#issuecomment-335977747).

The[C++ ABI](https://itanium-cxx-abi.github.io/cxx-abi/abi.html#rtti)states that two objects have the same type if and only if their`type_info`pointers are identical. Exceptions may only be caught if the`type_info`for the catch matches the thrown exception. The same rule applies for`dynamic_cast`.

When a type does not have a key function, its`typeinfo`is emitted as a weak symbol and matching type infos are merged when libraries are loaded. When loading libraries dynamically after the executable has been loaded (in other words, via`dlopen`or`System.loadLibrary`), it may not be possible for the loader to merge type infos for the loaded libraries. When this happens, the two types are not considered equal.
| **Note:** For non-polymorphic types, the type cannot have a key function. For non-polymorphic types, RTTI is unnecessary, since`std::is_same`can be used to determine type equality at compile time.

## Using mismatched prebuilt libraries

Using prebuilt libraries---these are typically third-party libraries---in your application requires a bit of extra care. In general, be aware of the following rules:

- The resulting app's minimum API level is the maximum of the`minSdkVersion`s of all the app's libraries.

  If your`minSdkVersion`is 16, but you're using a prebuilt library that was built against 21, the resulting app's minimum API level is 21. Failure to adhere to this will be visible at build time if the prebuilt library is static, but may not appear until run time for prebuilt shared libraries.
- All libraries should be generated with the same NDK version.

  This rule is a bit more flexible than most since breakages are rare, but compatibility between libraries that were built with different major versions of the NDK is not guaranteed. The C++ ABI is not stable and has changed in the past.
- Apps with multiple shared libraries must use a[shared STL](https://developer.android.com/ndk/guides/cpp-support#sr).

  As with mismatched STLs, the problems caused by this can be avoided if great care is taken, but it's better to just avoid the problem. The best way to avoid this problem is to avoid having multiple shared libraries in your app.