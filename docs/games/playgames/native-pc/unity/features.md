---
title: https://developer.android.com/games/playgames/native-pc/unity/features
url: https://developer.android.com/games/playgames/native-pc/unity/features
source: md.txt
---

This section provides detailed implementation guides for the core modules
supported by Google Play Games PC SDK for Unity:

## Initialization

The SDK must be initialized before you attempt to use any other features. This
process establishes the connection between your Unity game and the
Google Play Games on PC runtime.

**Namespace:** `PlayPcSdkManaged.Initialization`

**Entry Point:** `GooglePlayInitialization`

**Implementation**

You must retrieve the Unity-specific callback handler from the
`PlayPcSdkFactory` and pass it to the initialization method. To ensure
stability, we recommend wrapping the initialization logic in a safe async runner
to handle potential exceptions and prevent double-initialization.

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
            Debug.LogWarning("SDK is already initialized. Skipping.");
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
                Debug.Log("SDK Initialized Successfully!");
                // You can now create BillingClient or IntegrityClient instances
            }
            else
            {
                Debug.LogError($"Initialization Failed!");
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

## Error handling reference

The SDK uses a `Result` object for all expected API outcomes. You should check
`Result.Code` to handle scenarios like network errors or user cancellations.

**Note:** While the SDK APIs themselves don't throw exceptions for logic errors,
we still recommend wrapping your top-level `async` methods in a `try-catch`
block. This ensures that unexpected runtime errors (such as null references in
your own code or task scheduling failures) are logged correctly in the Unity
console.