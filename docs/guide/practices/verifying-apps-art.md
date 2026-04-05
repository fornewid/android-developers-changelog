---
title: https://developer.android.com/guide/practices/verifying-apps-art
url: https://developer.android.com/guide/practices/verifying-apps-art
source: md.txt
---

# Verifying app behavior on the Android runtime (ART)

The Android runtime (ART) is the default runtime for devices running Android 5.0 (API level 21) and higher. This runtime offers a number of features that improve performance and smoothness of the Android platform and apps. You can find more information about ART's new features in[Introducing ART](https://source.android.com/devices/tech/dalvik/art.html).

However, some techniques that work on Dalvik do not work on ART. This document lets you know about things to watch for when migrating an existing app to be compatible with ART. Most apps should just work when running with ART.

## Addressing garbage collection (GC) issues

Under Dalvik, apps frequently find it useful to explicitly call[System.gc()](https://developer.android.com/reference/java/lang/System#gc())to prompt garbage collection (GC). This should be far less necessary with ART, particularly if you're invoking garbage collection to prevent[`GC_FOR_ALLOC`](https://developer.android.com/tools/debugging/debugging-memory#LogMessages)-type occurrences or to reduce fragmentation. You can verify which runtime is in use by calling[System.getProperty("java.vm.version")](https://developer.android.com/reference/java/lang/System#getProperty(java.lang.String)). If ART is in use, the property's value is`"2.0.0"`or higher.

ART uses Concurrent Copying (CC) collector which concurrently compacts the Java heap. Because of this, you should avoid using techniques that are incompatible with compacting GC (such as saving pointers to object instance data). This is particularly important for apps that make use of the Java Native Interface (JNI). For more information, see[Preventing JNI Issues](https://developer.android.com/guide/practices/verifying-apps-art#JNI_Issues).

## Preventing JNI issues

ART's JNI is somewhat stricter than Dalvik's. It is an especially good idea to use CheckJNI mode to catch common problems. If your app makes use of C/C++ code, you should review the following article:

[Debugging Android JNI with CheckJNI](http://android-developers.blogspot.com/2011/07/debugging-android-jni-with-checkjni.html)

### Checking JNI code for garbage-collection issues

The Concurrent Copying (CC) collector may move objects in memory for compaction. If you use C/C++ code, do not perform operations that are incompatible with compacting GC. We have enhanced CheckJNI to identify some potential issues (as described in[JNI Local Reference Changes in ICS](http://android-developers.blogspot.com/2011/11/jni-local-reference-changes-in-ics.html)).

One area to watch for in particular is the use of`Get...ArrayElements()`and`Release...ArrayElements()`functions. In runtimes with non-compacting GC, the`Get...ArrayElements()`functions typically return a reference to the actual memory backing the array object. If you make a change to one of the returned array elements, the array object is itself changed (and the arguments to`Release...ArrayElements()`are usually ignored). However, if compacting GC is in use, the`Get...ArrayElements()`functions may return a copy of the memory. If you misuse the reference when compacting GC is in use, this can lead to memory corruption or other problems. For example:

- If you make any changes to the returned array elements, you must call the appropriate`Release...ArrayElements()`function when you are done, to make sure the changes you made are correctly copied back to the underlying array object.
- When you release the memory array elements, you must use the appropriate mode, depending on what changes you made:
  - If you did not make any changes to the array elements, use`JNI_ABORT`mode, which releases the memory without copying changes back to the underlying array object.
  - If you made changes to the array, and do not need the reference any more, use code`0`(which updates the array object and frees the copy of the memory).
  - If you made changes to the array that you want to commit, and you want to keep the copy of the array, use`JNI_COMMIT`(which updates the underlying array object and retains the copy).
- When you call`Release...ArrayElements()`, return the same pointer that was originally returned by`Get...ArrayElements()`. For example, it's not safe to increment the original pointer (to scan through the returned array elements) then pass the incremented pointer to`Release...ArrayElements()`. Passing this modified pointer can cause the wrong memory to be freed, resulting in memory corruption.

### Error handling

ART's JNI throws errors in a number of cases where Dalvik doesn't. (Once again, you can catch many such cases by testing with CheckJNI.)

For example, if`RegisterNatives`is called with a method that does not exist (perhaps because the method was removed by a tool such as**ProGuard** ), ART now properly throws[NoSuchMethodError](https://developer.android.com/reference/java/lang/NoSuchMethodError):  

```
08-12 17:09:41.082 13823 13823 E AndroidRuntime: FATAL EXCEPTION: main
08-12 17:09:41.082 13823 13823 E AndroidRuntime: java.lang.NoSuchMethodError:
    no static or non-static method
    "Lcom/foo/Bar;.native_frob(Ljava/lang/String;)I"
08-12 17:09:41.082 13823 13823 E AndroidRuntime:
    at java.lang.Runtime.nativeLoad(Native Method)
08-12 17:09:41.082 13823 13823 E AndroidRuntime:
    at java.lang.Runtime.doLoad(Runtime.java:421)
08-12 17:09:41.082 13823 13823 E AndroidRuntime:
    at java.lang.Runtime.loadLibrary(Runtime.java:362)
08-12 17:09:41.082 13823 13823 E AndroidRuntime:
    at java.lang.System.loadLibrary(System.java:526)
```

ART also logs an error (visible in logcat) if`RegisterNatives`is called with no methods:  

```
W/art     ( 1234): JNI RegisterNativeMethods: attempt to register 0 native
methods for <classname>
```

In addition, the JNI functions`GetFieldID()`and`GetStaticFieldID()`now properly throw[NoSuchFieldError](https://developer.android.com/reference/java/lang/NoSuchFieldError)instead of simply returning null. Similarly,`GetMethodID()`and`GetStaticMethodID()`now properly throw[NoSuchMethodError](https://developer.android.com/reference/java/lang/NoSuchMethodError). This can lead to CheckJNI failures because of the unhandled exceptions or the exceptions being thrown to Java callers of native code. This makes it particularly important to test ART-compatible apps with CheckJNI mode.

ART expects users of the JNI`CallNonvirtual...Method()`methods (such as`CallNonvirtualVoidMethod()`) to use the method's declaring class, not a subclass, as required by the JNI specification.

## Preventing stack size issues

Dalvik had separate stacks for native and Java code, with a default Java stack size of 32KB and a default native stack size of 1MB. ART has a unified stack for better locality. Ordinarily, the ART[Thread](https://developer.android.com/reference/java/lang/Thread)stack size should be approximately the same as for Dalvik. However, if you explicitly set stack sizes, you may need to revisit those values for apps running in ART.

- In Java, review calls to the[Thread](https://developer.android.com/reference/java/lang/Thread#Thread(java.lang.ThreadGroup, java.lang.Runnable, java.lang.String, long))constructor that specify an explicit stack size. For example, you will need to increase the size if[StackOverflowError](https://developer.android.com/reference/java/lang/StackOverflowError)occurs.
- In C/C++, review use of`pthread_attr_setstack()`and`pthread_attr_setstacksize()`for threads that also run Java code via JNI. Here is an example of the error logged when an app attempts to call JNI`AttachCurrentThread()`when the pthread size is too small:  

  ```
  F/art: art/runtime/thread.cc:435]
      Attempt to attach a thread with a too-small stack (16384 bytes)
  ```

## Object model changes

Dalvik incorrectly allowed subclasses to override package-private methods. ART issues a warning in such cases:  

```
Before Android 4.1, method void com.foo.Bar.quux()
would have incorrectly overridden the package-private method in
com.quux.Quux
```

If you intend to override a class's method in a different package, declare the method as`public`or`protected`.

[Object](https://developer.android.com/reference/java/lang/Object)now has private fields. Apps that reflect on fields in their class hierarchies should be careful not to attempt to look at the fields of[Object](https://developer.android.com/reference/java/lang/Object). For example, if you are iterating up a class hierarchy as part of a serialization framework, stop when  

```
Class.getSuperclass() == java.lang.Object.class
```

instead of continuing until the method returns`null`.

Proxy[InvocationHandler.invoke()](https://developer.android.com/reference/java/lang/reflect/InvocationHandler#invoke(java.lang.Object, java.lang.reflect.Method, java.lang.Object[]))now receives`null`if there are no arguments instead of an empty array. This behavior was documented previously but not correctly handled in Dalvik. Previous versions of[Mockito](https://code.google.com/p/mockito/)have difficulties with this, so use an updated Mockito version when testing with ART.

## Fixing AOT compilation issues

ART's Ahead-Of-Time (AOT) Java compilation should work for all standard Java code. Compilation is performed by ART's`dex2oat`tool; if you encounter any issues related to`dex2oat`at install time, let us know (see[Reporting Problems](https://developer.android.com/guide/practices/verifying-apps-art#Reporting_Problems)) so we can fix them as quickly as possible. A couple of issues to note:

- ART does tighter bytecode verification at install time than Dalvik does. Code produced by the Android build tools should be fine. However, some post-processing tools (especially tools that perform obfuscation) may produce invalid files that are tolerated by Dalvik but rejected by ART. We have been working with tool vendors to find and fix such issues. In many cases, getting the latest versions of your tools and regenerating the DEX files can fix these problems.
- Some typical problems that are flagged by the ART verifier include:
  - invalid control flow
  - unbalanced`monitorenter`/`monitorexit`
  - 0-length parameter type list size
- Some apps have dependencies on the installed`.odex`file format in`/system/framework`,`/data/dalvik-cache`, or in[DexClassLoader](https://developer.android.com/reference/dalvik/system/DexClassLoader)'s optimized output directory. These files are now ELF files and not an extended form of DEX files. While ART tries to follow the same naming and locking rules as Dalvik, apps should not depend on the file format; the format is subject to change without notice.

  **Note:** In Android 8.0 (API level 26) and higher, the[DexClassLoader](https://developer.android.com/reference/dalvik/system/DexClassLoader)optimized output directory has been deprecated. For more information, see the documentation for the[DexClassLoader()](https://developer.android.com/reference/dalvik/system/DexClassLoader#DexClassLoader(java.lang.String, java.lang.String, java.lang.String, java.lang.ClassLoader))constructor.

## Reporting problems

If you run into any issues that aren't due to app JNI issues, report them via the Android Open Source Project Issue Tracker at<https://code.google.com/p/android/issues/list>. Include an`"adb bugreport"`and a link to the app in the Google Play Store if available. Otherwise, if possible, attach an APK that reproduces the issue. Note that issues (including attachments) are publicly visible.