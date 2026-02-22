---
title: https://developer.android.com/topic/performance/tracing/custom-events-native
url: https://developer.android.com/topic/performance/tracing/custom-events-native
source: md.txt
---

# Custom trace events in native code

Android 6.0 (API level 23) and higher support a native tracing API,`trace.h`, to write trace events to the system buffer that you can then analyze using Perfetto or systrace. Common use cases for this API include observing the time that a particular block of code takes to execute and associating a block of code with undesirable system behavior.

**Note:** On devices and emulators running API level 27 and lower, if there isn't enough memory available or the memory is too fragmented, you'll get the following message:`Atrace could not allocate enough memory to record a trace`. If this happens and your capture does not have a complete set of data, then you should close background processes or restart the device or emulator.

To define custom events that occur in the native code within your app or game, complete the following steps:

1. Define function pointers for the ATrace functions that you use to capture custom events within your app or game, as shown in the following code snippet:

   ```c++
   #include <android/trace.h>
   #include <dlfcn.h>

   void *(*ATrace_beginSection) (const char* sectionName);
   void *(*ATrace_endSection) (void);

   typedef void *(*fp_ATrace_beginSection) (const char* sectionName);
   typedef void *(*fp_ATrace_endSection) (void);
   ```
2. Load the ATrace symbols at runtime, as shown in the following code snippet. Usually, you perform this process in an object constructor.

   ```c++
   // Retrieve a handle to libandroid.
   void *lib = dlopen("libandroid.so", RTLD_NOW | RTLD_LOCAL);

   // Access the native tracing functions.
   if (lib != NULL) {
       // Use dlsym() to prevent crashes on devices running Android 5.1
       // (API level 22) or lower.
       ATrace_beginSection = reinterpret_cast<fp_ATrace_beginSection>(
           dlsym(lib, "ATrace_beginSection"));
       ATrace_endSection = reinterpret_cast<fp_ATrace_endSection>(
           dlsym(lib, "ATrace_endSection"));
   }
   ```

   **Caution:** For security reasons, include calls to`dlopen()`only in the debug version of your app or game.

   **Note:** To provide tracing support further back to Android 4.3 (API level 18), you can use JNI to call the methods in[managed code](https://developer.android.com/topic/performance/tracing/custom-events-native#managed-code)around the code shown in the preceding snippet.
3. Call`ATrace_beginSection()`and`ATrace_endSection()`at the beginning and end, respectively, of your custom event:

   ```c++
   #include <android/trace.h>

   char *customEventName = new char[32];
   sprintf(customEventName, "User tapped %s button", buttonName);

   ATrace_beginSection(customEventName);
   // Your app or game's response to the button being pressed.
   ATrace_endSection();
   ```  
   **Note:** When you call`ATrace_beginSection()`multiple times, calling`ATrace_endSection()`ends only the most recently called`ATrace_beginSection()`method. So, for nested calls, make sure that you properly match each call to`ATrace_beginSection()`with a call to`ATrace_endSection()`.

   Additionally, you cannot call`ATrace_beginSection()`on one thread and end it from another. You must call both functions from the same thread.

# Convenience tips

The following tips are optional but might make it easier to analyze your native code.

## Trace an entire function

When instrumenting your call stack or function timing, you might find it useful to trace entire functions. You can use the`ATRACE_CALL()`macro to make this type of tracing easier to set up. Furthermore, such a macro allows you to skip creating`try`and`catch`blocks for cases where the traced function might throw an exception or call`return`early.

To create a macro for tracing an entire function, complete the following steps:

1. Define the macro:

   ```c++
   #define ATRACE_NAME(name) ScopedTrace ___tracer(name)

   // ATRACE_CALL is an ATRACE_NAME that uses the current function name.
   #define ATRACE_CALL() ATRACE_NAME(__FUNCTION__)

   class ScopedTrace {
     public:
       inline ScopedTrace(const char *name) {
         ATrace_beginSection(name);
       }

       inline ~ScopedTrace() {
         ATrace_endSection();
       }
   };
   ```
2. Call the macro within the function that you want to trace:

   ```c++
   void myExpensiveFunction() {
     ATRACE_CALL();
     // Code that you want to trace.
   }
   ```

## Name your threads

You can give a name to each thread in which your events occur, as demonstrated in the following code snippet. This step makes it easier to identify the threads that belong to specific actions within your game.  

```c++
#include <pthread.h>

static void *render_scene(void *parm) {
    // Code for preparing your app or game's visual components.
}

static void *load_main_menu(void *parm) {
    // Code that executes your app or game's main logic.
}

void init_threads() {
    pthread_t render_thread, main_thread;

    pthread_create(&render_thread, NULL, render_scene, NULL);
    pthread_create(&main_thread, NULL, load_main_menu, NULL);

    pthread_setname_np(render_thread, "MyRenderer");
    pthread_setname_np(main_thread, "MyMainMenu");
}
```

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Best practices for SQLite performance](https://developer.android.com/topic/performance/sqlite-performance-best-practices)
- [Create and measure Baseline Profiles without Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/manually-create-measure)