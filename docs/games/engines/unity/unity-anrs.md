---
title: https://developer.android.com/games/engines/unity/unity-anrs
url: https://developer.android.com/games/engines/unity/unity-anrs
source: md.txt
---

Solving[ANRs](https://developer.android.com/topic/performance/vitals/anr)in your Unity game is a systematic process:
![](https://developer.android.com/static/images/games/engines/unity/unity-anr-flowchart.jpg)**Figure 1.**Steps to solve ANRs in Unity games.

## Integrate reporting services

Reporting services such as[Android vitals](https://developer.android.com/topic/performance/vitals),[Firebase Crashlytics](https://firebase.google.com/products/crashlytics), and[Backtrace](https://backtrace.io/)(a certified Unity partner) provide error logging and analysis for your game at scale. Integrate reporting services SDKs into your game early in the development cycle. Analyze which reporting service best fits your game needs and budget.

Different reporting services have different ways of capturing ANRs. Include a second reporting service to increase the chance of obtaining valid data to support your decision in fixing ANRs.

Integrating reporting SDKs doesn't impact game performance or APK size.

## Analyze symbols

Analyze the reports from your reporting service and check whether the stack traces are in human-readable format. See[Symbolicate Android crashes and ANR for Unity games](https://developer.android.com/games/engines/unity/unity-symbolicate)for more information.
![](https://developer.android.com/static/images/games/engines/unity/unity-anr-crashlytics.png)**Figure 2.** Crashlytics showing build ID and missing`libil2cpp.so`symbols.

**How to check symbol build ID**

If the reporting system shows the missing build ID but the build symbols still exist in the build machine storage, it's possible to check the build ID of the symbols and then upload them to the reporting service. Otherwise, a new build is required to upload the symbol files.

On Windows or macOS:

1. Navigate to the symbols folder based on your[scripting backend](https://support.unity.com/hc/en-us/articles/115000292166-Symbolicate-Android-crash)(see**Resolution** :)
   1. Use the following command (on Windows, use[Cygwin](https://www.cygwin.com/)to run the`readelf`utility)
   2. Grep usage is optional to filter the text output
   3. Look for Build ID

    readelf -n libil2cpp.so | grep 'Build ID'
    Build ID: b42473fb7449e44e0182dd1f580c99bab0cd8a95

## Inspect game code

When the stack trace shows a function in the`libil2cpp.so`library, the error happened in the C# code, which is[converted to C++](https://docs.unity3d.com/Manual/overview-of-dot-net-in-unity.html). The`libil2cpp.so`library has not only your game code but also plugins and packages.

The C++ filename follows the assembly name defined in the Unity project. Otherwise, the filename has the default Assembly-C# name. For example, figure 3 shows the error on file`Game.cpp`(highlighted in blue), which is the name defined in the Assembly Definition file.`Logger`is the class name (highlighted in red) in the C# script, followed by the function name (highlighted in green). Finally is the full name that the IL2CPP converter generated (highlighted in orange).
![](https://developer.android.com/static/images/games/engines/unity/unity-anr-backtrace.png)**Figure 3.**Test project call stack from Backtrace.

Inspect your game code by doing the following:

- Examine the C# project for any suspicious code. Usually, C# unhandled exceptions don't cause an ANR or application crash. Even so, ensure the code runs properly in different situations. Check whether the code uses a third-party engine module, and analyze whether a recent release introduced the error. In addition, review whether you have recently updated Unity or whether the error only happens on specific devices.
- [Export](https://docs.unity3d.com/Manual/android-export-process.html)the game as an Android Studio project. With complete access to your game's converted C# source code, you can find the function that's causing the ANR. The C++ code looks very different from your C# code, and the code conversion rarely has an issue. If you do find something, file a support ticket to Unity.
- Review the game source code and ensure that any logic running in the[OnApplicationFocus()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnApplicationFocus.html)and[OnApplicationPause()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnApplicationPause.html)callbacks is appropriately cleaned up.
  - The Unity engine has a timeout to pause its execution; excessive workload on these callbacks can cause an ANR.
  - Add logs or breadcrumbs to parts of the code to enhance your data analysis.
- Use the[Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html)to investigate the game's performance. Profiling your app can also be a great way to help identify bottlenecks that might be causing the ANR.
- A great way to identify long I/O operations on the main thread is to use[strict mode](https://developer.android.com/topic/performance/vitals/anr#strict_mode).
- Analyze the Android Vitals or another reporting service history and check the release versions of the game for which the error is happening the most. Review your source code in your version control history and compare code changes between releases. If you find something suspicious, experiment with each change or potential fix individually.
- Examine the Google Play ANR reporting history for the devices and Android versions receiving the most ANRs. If the devices or versions are outdated, chances are you can safely ignore them if doing so doesn't impact the game's profitability. Study the data carefully since a particular group of users will no longer be able to play your game. For more information, see[Distribution dashboard](https://developer.android.com/about/dashboards).
- Review the game source code to ensure you are not calling any code that might cause an issue, for example,[finish](https://developer.android.com/reference/android/app/Activity#finish())can be destructive if not used correctly. See the[Android developer guides](https://developer.android.com/guide)to learn more about Android development.
- After reviewing the data and exporting the game build to Android Studio, you're dealing with C and C++ code, and so you can take full advantage of tools beyond Unity's standard solutions, such as[Android Memory Profiler](https://developer.android.com/studio/profile/memory-profiler),[Android CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler), and[perfetto](https://developer.android.com/tools/perfetto).

| **Warning:** Avoid custom code loading---both native and managed---with[Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery), as code loading causes hard-to-debug ANRs.

## Unity engine code

To know if an ANR is happening on the Unity engine side of things, check for`libUnity.so`or`libMain.so`in the stack traces. If you find them, take the following steps:

- First, search the community channels ([Unity Forums](https://forum.unity.com/),[Unity Discussions](https://discussions.unity.com/),[Stackoverflow](https://stackoverflow.com/questions/tagged/unity-game-engine?tab=Newest)%7B:.external%7D)).
- If you do not find anything,[file a bug](https://unity.com/releases/editor/qa/bug-reporting)to resolve the problem. Provide a symbolicated stack trace so the engine's engineers can better understand and solve the error.
- Check whether the latest[Unity LTS](https://unity.com/releases/editor/qa/lts-releases)has made improvements related to your issues. If so, upgrade your game to use that version. (This solution may be possible only for some developers.)
- If your code uses a custom[`Activity`](https://developer.android.com/reference/android/app/Activity)instead of the default, review the Java code to ensure the activity is not causing any issues.

## Third-party SDK

- Check that all third-party libraries are up to date and don't have reports of crashes or ANRs for the latest version of Android.
- Go to the[Unity Forums](https://forum.unity.com/)to see if any errors have already been resolved in a later version or if a workaround has been provided by Unity or a community member.
- Review the[Google Play ANR report](https://support.google.com/googleplay/android-developer/answer/9859174)and ensure the error has not already been identified by Google. Google is aware of some ANRs and is actively working to fix them.

| **Note:** The[Google Play SDK Console](https://play.google.com/sdk-console/about/)allows SDK providers to access usage statistics, crash and ANR (application not responding) reporting, and tools to help guide app developers in adopting SDK versions that fix quality issues and comply with Play policies. You can submit bug reports and feedback to the Google Play SDK Console to help the SDK provider improve their SDK.

## System library

System libraries usually are far from the developer's control, but they don't represent a significant percentage of ANRs. Beyond contacting the library developer or adding logs to narrow down the problem, system library ANRs are difficult to resolve.

## Exit reasons

[`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo)is an Android API for understanding ANR causes. If your game is using[Unity 6 or later](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IApplicationExitInfo.html)you can call`ApplicationExitInfo`directly. For older Unity versions, you need to implement your own plugin to enable`ApplicationExitInfo`calls from Unity.

Crashlytics also uses`ApplicationExitInfo`; however, your own implementation gives you finer control and enables you to include[more relevant information](https://developer.android.com/reference/kotlin/android/app/ActivityManager#setprocessstatesummary).