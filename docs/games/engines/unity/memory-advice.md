---
title: https://developer.android.com/games/engines/unity/memory-advice
url: https://developer.android.com/games/engines/unity/memory-advice
source: md.txt
---

# Get started with the Memory Advice API for Unity games

| **Note:** The Memory Advice API Beta is now over and the library is deprecated.[learn more about alternative memory management approaches](https://developer.android.com/games/optimize/memory-allocation).

This guide describes how to use the Memory Advice plugin for Unity to integrate the[Memory Advice API](https://developer.android.com/games/sdk/memory-advice/overview)into your Unity game.

## Requirements

The plugin is supported on:

- Unity 2019 with Android NDK r19

- Unity 2020 with Android NDK r19

- Unity 2021 with Android NDK r21

- Unity 2022 with Android NDK r23

You may face unexpected issues if you are using other versions of Unity and the Android NDK. To find the NDK version used by your Unity installation, see the[Android environment setup guide](https://docs.unity3d.com/Manual/android-sdksetup.html)for Unity.

## Download the plugin

Download[the plugin](https://dl.google.com/developers/android/games/memory_advice/memory-advice-1.0.0-beta01.unitypackage).

## Import the plugin

The plugin is a Unity Package that you can import into your project. To import the plugin, click**Assets \> Import Package \> Custom Package** and select the`.unitypackage`file you downloaded. You can also double-click the`.unitypackage`file after opening your Unity project.

## Use the library

This section describes how to use the library.

### Initialize the library

You need to initialize the library once when the app starts. To do so, add this code to your project:  

    void Start()
    {
        MemoryAdviceErrorCode errorCode = MemoryAdvice.Init();
        if(errorCode == MemoryAdviceErrorCode.Ok)
        {
            Debug.Log("Memory advice init successfully");
        }
    }

### Poll for memory state

You can retrieve the memory state of your app by polling the library at the interval of your choosing. Use the[MemoryAdvice_getMemoryState](https://developer.android.com/reference/games/memory-advice/group/memory-advice#memoryadvice_getmemorystate)function whenever you need to poll the library:  

    MemoryState memoryState = MemoryAdvice.GetMemoryState();
    switch (memoryState)
    {
        case MemoryState.Ok:
            //The application can safely allocate memory.
            break;
        case MemoryState.ApproachingLimit:
            // The application should minimize memory allocation.
            break;
        case  MemoryState.Critical:
            // The application should free memory as soon as possible
            // until the memory state changes.
            break;
    }

### Set up a watcher

You can also set up[a watcher](https://developer.android.com/reference/games/memory-advice/group/memory-advice#memoryadvice_registerwatcher)and register the Memory Advice API, and your watcher function will get called when the state is either approaching the limit or the critical[memory state](https://developer.android.com/reference/games/memory-advice/group/memory-advice#memoryadvice_memorystate)(but not for the ok state). For example, the following code creates a watcher and requests a Memory Advice API notification every 2 seconds:  

    MemoryAdviceErrorCode errorCode = MemoryAdvice.RegisterWatcher(2000,
            new MemoryWatcherDelegateListener((MemoryState state) =>
        {
            switch (memoryState)
            {
                case MemoryState.ApproachingLimit:
                    // The application should minimize memory allocation.
                    break;
                case  MemoryState.Critical:
                    // The application should free memory as soon as possible
                    // until the memory state changes.
                    break;
            }
        })
    );

    if(errorCode == MemoryAdviceErrorCode.Ok)
    {
        Debug.Log("Memory Advice watcher registered successfully");
    }

## What's next

You can download our[Unity sample project](https://dl.google.com/developers/android/games/memory_advice/sample.zip)that provides a simple UI for allocating and freeing memory, and uses Memory Advice API to monitor the memory state.

See the[overview](https://developer.android.com/games/sdk/memory-advice/overview)for[additional resources](https://developer.android.com/games/sdk/memory-advice/overview#additional_resources)and[reporting issues](https://developer.android.com/games/sdk/memory-advice/overview#issues_and_feedback).