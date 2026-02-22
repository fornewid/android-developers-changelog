---
title: https://developer.android.com/games/playgames/native-pc/unity/unity_start
url: https://developer.android.com/games/playgames/native-pc/unity/unity_start
source: md.txt
---

This guide provides step-by-step instructions for integrating the
Google Play Games PC SDK into your Unity project.

## Step 1: Download the SDK

Download the latest version of the Unity Package using the download link.

Download: [Play Games PC Unity SDK](https://dl.google.com/play/games/native/sdk/unity/play_pc_sdk_unity_26.2.121.0.tgz)

## Step 2: Import the package

The SDK is distributed as a tar file compatible with the Unity Package
Manager (UPM). For more information,
see [Install a UPM package from a local tar file](https://docs.unity3d.com/6000.3/Documentation/Manual/upm-ui-tarball.html)

## Step 3: Configure Build Settings

To verify the native libraries load correctly, you must configure your project
to use the `IL2CPP` scripting backend and target the correct architecture.

1. [Create a build profile](https://docs.unity3d.com/6000.3/Documentation/Manual/create-build-profile.html)
   with **Windows** as the platform.

2. Select the [platform settings](https://docs.unity3d.com/6000.3/Documentation/Manual/build-profiles-reference.html#platform-settings)
   as Windows. For the [architecture](https://docs.unity3d.com/6000.3/Documentation/Manual/WindowsStandaloneBinaries.html), use the options:

   - **Intel 64-bit** (Recommended)
   - **Intel 32-bit**

   **Note:** The Google Play Games on PC platform runs on a 64-bit environment.
   You can build your game as 32-bit (x86) or 64-bit (x64).
3. Set **Scripting Backend** to **IL2CPP** .
   For more information, see [Building a project with IL2CPP](https://docs.unity3d.com/6000.3/Documentation/Manual/il2cpp-introduction.html).

   - Set **Api Compatibility Level** to **.NET Standard 2.0** (or .NET Framework).

## Step 4: Create the application manifest

Before you can use the SDK in your game, you must associate your game executable
with the Play package name that you claimed in the **Play Console** . You do this
by adding a `manifest.xml` file in the same directory as your game's executable.

**Note:** This is a manual step that must be performed.

1. To build your game executable file, select **File \> Build and
   Run** or click `Ctrl+B`.
2. Open a text editor and create a new file named `manifest.xml`.
3. Copy and paste the following XML code into the file:


   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <?Manifest version="1">
      <?Application>
        <?PackageName>com.example.package<?/PackageName>
      <?/Application>
   <?/Manifest>
   ```

   <br />

4. Save the file as `manifest.xml`.

5. Move this file into the same folder as your built game executable file.

   Example: If your game is at `Builds/MyGame.exe`, the manifest must be at
   `Builds/manifest.xml`.

## Step 5: Initialize the SDK

You must initialize the SDK before accessing any features, such as Billing or
Integrity. Use the `PlayPcSdkFactory` to create the initialization handler and
start the connection.

Create a new C# script, for example, `SdkInitialization.cs`, and add the
following code:

```c#
using UnityEngine;
using System;
using System.Threading.Tasks;
// Import the SDK namespaces
using PlayPcSdkManaged.Initialization;
using PlayPcSdkManaged.Unity;

public class GooglePlayPCSDKInit : MonoBehaviour
{
    // Prevent double-initialization if this script is reloaded
    private static bool _isInitialized = false;

    private void Start()
    {
        // Use the "Safe Runner" pattern to fire the async method
        _ = InitializeSdkAsync();
    }

    private async Task InitializeSdkAsync()
    {
        if (_isInitialized)
        {
            Debug.LogWarning("Google Play PC SDK is already initialized. Skipping.");
            return;
        }

        try
        {
            Debug.Log("Initializing Google Play PC SDK...");

            // 1. Get the Unity-specific initialization handler from the factory
            var initHandler = PlayPcSdkFactory.InitializationHandler;

            // 2. Call InitializeAsync to start the connection
            var result = await GooglePlayInitialization.InitializeAsync(initHandler);

            // 3. Check the result
            if (result.IsOk)
            {
                _isInitialized = true;
                Debug.Log("<color=green>Google Play PC SDK Initialized Successfully!</color>");
                // You can now create BillingClient or IntegrityClient instances
            }
            else
            {
                Debug.LogError($"<color=red>Initialization Failed!</color>");
                Debug.LogError($"Error Code: {result.Code}");
                Debug.LogError($"Message: {result.ErrorMessage}");
            }
        }
        catch (Exception ex)
        {
            // Catch unexpected crashes or task failures
            Debug.LogError($"Exception during initialization: {ex.Message}");
            Debug.LogException(ex);
        }
    }
}
```

Attach this script to a **GameObject** in your first scene. When you run the
game, check the Console for the "SDK Initialized Successfully!" message.