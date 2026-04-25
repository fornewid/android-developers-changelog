---
title: https://developer.android.com/games/playgames/native-pc/unity/install_referrer
url: https://developer.android.com/games/playgames/native-pc/unity/install_referrer
source: md.txt
---

Make informed marketing decisions by identifying your most valuable user
acquisition channels for your game. Use the Google Play Install Referrer API for
a reliable way to track your apps' referral information.

By tracking referral data, you can understand which traffic sources send the
most users to download your app from the Google Play store. These insights can
help you make the most of your advertising spend and maximize ROI.

**Namespace:** `PlayPcSdkManaged.InstallReferrer`

**Client Class:** `InstallReferrerClient`

## Link to your store listing page

Start by linking your users to your application's Google Play store page. In the
URL, include query parameters for:

- `id`: The Play package name of your game
- `referrer`: A string representing the referral source. This string can be queried once your application is installed and running.

    https://play.google.com/store/apps/details?id=com.example.package&referrer=example_referrer_source

## Create the client

Always use the factory to create an `InstallReferrerClient`. This ensures that
Unity-safe callbacks are automatically registered.

```c#
using UnityEngine;
using System;
using System.Threading.Tasks;
// Required SDK Namespaces
using PlayPcSdkManaged.InstallReferrer;
using PlayPcSdkManaged.Unity;

public class InstallReferrerManager : MonoBehaviour
{
    private InstallReferrerClient _installReferrerClient;

    public void SetupInstallReferrer()
    {
        try
        {
            // Creates the client with the required UnityInstallReferrerCallbacksHandler
            _installReferrerClient = PlayPcSdkFactory.CreateInstallReferrerClient();
            Debug.Log("Install Referrer Client created successfully.");
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to create Install Referrer Client: {ex.Message}");
        }
    }

    private void OnDestroy()
    {
        // Always dispose of the client to clean up native C++ resources
        _installReferrerClient?.Dispose();
    }
}
```

## Query the install referrer

> [!NOTE]
> **Note:** The referrer is available for 90 days after the installation of your game.

After the user installs and launches the game, your app can determine the
traffic source that led to the installation using the Install Referrer API.

Query the referrer details using
[`GetInstallReferrerAsync`](https://developer.android.com/games/playgames/native-pc/unity/api_reference#playpcsdkmanaged-installreferrer). The response contains the
same string passed into the `referrer` query parameter of your store listing
page.

```c#
public async Task GetInstallReferrerAsync()
{
    try
    {
        Debug.Log("Querying Install Referrer...");

        // Async call to retrieve referral information
        var result = await _installReferrerClient.GetInstallReferrerAsync();

        if (result.IsOk)
        {
            // On success, access the InstallReferrer and InstallTimeEpochSeconds
            var referrer = result.Value.InstallReferrer;
            var installTime = result.Value.InstallTimeEpochSeconds;

            Debug.Log($"Install Referrer: {referrer}");
            Debug.Log($"Install Time: {installTime}");

            // Attribute your game's installation to an acquisition channel
        }
        else
        {
            // Handle expected API errors (e.g., Error)
            Debug.LogError($"Query Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}
```