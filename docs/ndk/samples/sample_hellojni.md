---
title: https://developer.android.com/ndk/samples/sample_hellojni
url: https://developer.android.com/ndk/samples/sample_hellojni
source: md.txt
---

This sample guides you through hello-jni, a minimal C/C++ application built with the NDK. This sample is in the[hello-jni](https://github.com/android/ndk-samples/tree/android-mk/hello-jni)directory of ndk-samples repo, inside[android-mk branch](https://github.com/android/ndk-samples/tree/android-mk).

## Android.mk

The following two lines provide the name of the native source file, along with the name of the shared library to build. The full name of the built library is`libhello-jni.so`, once the build system adds the`lib`prefix and the`.so`extension.  

```
LOCAL_SRC_FILES := hello-jni.c
LOCAL_MODULE    := hello-jni
```

For more information about what the`Android.mk`file does, and how to use it, see[Android.mk](https://developer.android.com/ndk/guides/android_mk).

## Application.mk

This line tells the build system the CPU and architecture against which to build. In this example, the build system builds for all supported architectures.  

```
APP_ABI := all
```

For more information about the`Application.mk`file, and how to use it, see[Application.mk](https://developer.android.com/ndk/guides/application_mk).

## Java-side Implementation

The`helloJNI.java`file is located in`hellojni/src/com/example/hellojni/`. It calls a function to retrieve a string from the native side, then displays it on the screen.

The source code contains three lines of particular interest to the NDK user. They are presented here in the order in which they are used, rather than by line order.

This function call loads the`.so`file upon application startup.  

### Kotlin

```kotlin
System.loadLibrary("hello-jni")
```

### Java

```java
System.loadLibrary("hello-jni");
```

The`native`keyword in this method declaration tells the virtual machine that the function is in the shared library (that is, implemented on the native side).  

### Kotlin

```kotlin
external fun stringFromJNI(): String
```

### Java

```java
public native String stringFromJNI();
```

The Android framework calls the function loaded and declared in the previous steps, displaying the string on the screen.  

### Kotlin

```kotlin
tv.text = stringFromJNI()
```

### Java

```java
tv.setText( stringFromJNI() );
```

## C-side Implementation

The`hello-jni.c`file is located in`hello-jni/jni/`. It contains a function that returns a string that[the Java side requested](https://developer.android.com/ndk/samples/sample_hellojni#ji)). The function declaration is as follows:  

```c++
JNIEXPORT jstring JNICALL
Java_com_example_hellojni_HelloJni_stringFromJNI( JNIEnv* env,
                                                  jobject thiz )
```

This declaration corresponds to the native function declared in the Java source code. The return type,`jstring`, is a data type defined in the[Java Native Interface Specification](http://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/jniTOC.html). It is not actually a string, but a pointer to a Java string.

After`jstring`comes the function name, which is based on the Java function name and the path to the file containing it. Construct it according to the following rules:

- Prepend`Java_`to it.
- Describe the filepath relative to the top-level source directory.
- Use underscores in place of forward slashes.
- Omit the`.java`file extension.
- After the last underscore, append the function name.

Following these rules, this example uses the function name`Java_com_example_hellojni_HelloJni_stringFromJNI`. This name refers to a Java function called`stringFromJNI()`, which resides in`hellojni/src/com/example/hellojni/HelloJni.java`.

`JNIEnv*`is the pointer to the VM, and`jobject`is a pointer to the implicit`this`object passed from the Java side.

The following line calls the VM API`(*env)`, and passes it a return value: that is, the string that the function on the Java side had requested.  

```c++
return (*env)->NewStringUTF(env, "Hello from JNI !
Compiled with ABI " ABI ".");
```