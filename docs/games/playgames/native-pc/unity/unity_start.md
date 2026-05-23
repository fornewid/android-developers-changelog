---
title: https://developer.android.com/games/playgames/native-pc/unity/unity_start
url: https://developer.android.com/games/playgames/native-pc/unity/unity_start
source: md.txt
---

project, covering steps from SDK download to initialization and build
configuration.
keywords_public: Google Play Games PC, Unity, SDK integration, native PC,
game development, IL2CPP, manifest, Play Games PC Unity SDK

This guide provides step-by-step instructions for integrating the
Google Play Games PC SDK into your Unity project.

## Step 1: Download the SDK

Download the latest version of the Unity Package using the download link.

Download: [Play Games PC Unity SDK](https://developer.android.com/games/playgames/native-pc/downloads/unity)

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

Before you can use the SDK in your game, you must associate your game
executable with the Play package name that you claimed in the
**Play Console** . You do this by adding a `manifest.xml` file in the same
directory as your game's executable.

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

**Note:** If you want to use the PC SDK while developing in the Unity Editor
without needing to digitally sign your game executable or launch it from Google
Play Games. For additional manifest configuration steps, see
[developer mode setup guide](https://developer.android.com/games/playgames/native-pc/setup/developer_mode).

## Step 5: Initialize the SDK

You must initialize the SDK before accessing any features, such as Billing or
Integrity. Use the `PlayPcSdkFactory` to create the initialization handler
and start the connection.

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

## **Step 6**: Enabling Auto-Play upon installation of your PC Native Games

Google Play Games on PC (GPG) allows developers to enable an "auto-play"
feature, which automatically launches your game immediately after the
installation process completes. This feature allows for a seamless user
experience by transitioning the player directly into the game, fully
authenticated within the GPG ecosystem.

### How it works

When you enable the feature, GPG will pass a GPG session token to your
third-party (3P) installer process via command-line arguments. Your installer
is then responsible for extracting this token and using it to launch the game
executable in an authenticated context.

#### Prerequisites

To use this feature, your 3P installer must be capable of handling
command-line arguments.

### Implementation Steps

1. Enable Auto-Play in Publishing Config

   To opt-in to this feature, add the `acceptsCommandLineArguments` attribute
   to the `<installer>` element in your `play_publishing_config.xml`.

   Example `manifest.xml` contents:

       <installer requiresElevation="true" acceptsCommandLineArguments="true">
         <path>path/to/installer.exe</path>
         <installation-path-registry-location>
           <key-name>SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\key</key-name>
           <value-name>InstallPath</value-name>
         </installation-path-registry-location>
       </installer>

   - Attribute: `acceptsCommandLineArguments`
   - Type: `Boolean`
   - Default: `false`
   - Behavior: When you set it to true, GPG will append the session token to the command-line arguments when executing your installer.
2. Handle the Session Token in Your Installer

   When your installer is launched by the GPG client, it will receive the
   session token as a command-line argument.
   - Argument Format: `--g_session_token=<TOKEN>`

   What you must do:
   - Extraction: Your installer must parse the command-line arguments to retrieve the token string.
   - Propagation: If your installation flow involves launching a secondary launcher or game process, your installer is responsible for securely passing the session token to the final game process that uses the SDK.
   - Launch: Use the provided session token to start the game executable. This ensures the game runs within an authenticated GPG context. Otherwise, [InitializeSDK](https://developer.android.com/games/playgames/native-pc/unity/unity_start#create-app-manifest) will fail and your player will need to restart your game.
3. Error Handling and Fallbacks

- Token Retrieval: If, for any reason, GPG cannot generate or pass a session token (e.g., token generation failure), the installation process will still proceed. However, your installer will be launched without the --g_session_token argument.
- Robustness: Your installer should be designed to handle scenarios where the session token is absent. In such cases, the installer should proceed with a standard installation; you should not trigger automatic game launch as [InitializeSDK](https://developer.android.com/games/playgames/native-pc/unity/unity_start#create-app-manifest) will fail anyway.
- Installer Errors: You are responsible for the robustness and error handling of your installer and the game launch sequence it initiates. GPG does not have control over processes that occur within the installer after it has been launched.