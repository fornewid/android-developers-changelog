---
title: https://developer.android.com/ndk/guides/simpleperf
url: https://developer.android.com/ndk/guides/simpleperf
source: md.txt
---

# Simpleperf

Android Studio includes a graphical front end to Simpleperf, documented in[Inspect CPU activity with CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler). Most users will prefer to use that instead of using Simpleperf directly.

If you prefer to use the command line, Simpleperf is a versatile command-line CPU profiling tool included in the NDK for Mac, Linux, and Windows.

For full documentation, start with the Simpleperf[README](https://android.googlesource.com/platform/system/extras/+/master/simpleperf/doc/README.md).

## Simpleperf tips and recipes

If you are just starting out with Simpleperf, here are some commands that you may find particularly useful. For more commands and options, see[Simpleperf command and options reference](https://developer.android.com/ndk/guides/simpleperf-commands).

### Find which shared libraries take the longest to execute

You can run this command to see which`.so`files take up the largest percentage of execution time (based on the number of CPU cycles). This is a good first command to run when starting your performance analysis session.  

```
$ simpleperf report --sort dso
```

### Find which functions take the longest to execute

Once you have identified which shared library takes most of the execution time, you can run this command to see the percentage of time spent executing the functions of that`.so`file.  

```
$ simpleperf report --dsos library.so --sort symbol
```

### Find percentage of time spent in threads

Execution time in a`.so`file can be split across multiple threads. You can run this command to see the percentage of time spent in each thread.  

```
$ simpleperf report --sort tid,comm
```

### Find the percentage of time spent in object modules

After finding the threads where most of the execution time is spent, you can use this command to isolate the object modules taking the longest execution time on those threads.  

```
$ simpleperf report --tids threadID --sort dso
```

### See how function calls are related

A*call graph*provides a visual representation of a stack trace that Simpleperf records during the profiling session.

You can use the`report -g`command to print a call graph to see what functions are called by other functions. This is useful to determine if a function is slow by itself, or if it's because one or more of the functions it calls are slow.  

```
$ simpleperf report -g
```

You can also use the Python script`report.py -g`to start an interactive tool that displays functions. You can click on each function to see how much time is spent in its children.

### Profiling apps built with Unity

If you are profiling an app built with Unity, make sure to build the app with debug symbols by following these steps:

1. Open your Android project in the Unity Editor.
2. In the**Build Settings** window for the Android platform, make sure the**Development Build**option is checked.
3. Click on**Player Settings** and set the**Stripping Level** property to**Disabled**.