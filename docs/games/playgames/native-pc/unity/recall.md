---
title: Play Games Services Recall  |  Play for Native PC  |  Android Developers
url: https://developer.android.com/games/playgames/native-pc/unity/recall
source: html-scrape
---

* [Home](https://developer.android.com/)
* [Play for Native PC](https://developer.android.com/games/playgames/native-pc)
* [Guides](https://developer.android.com/games/playgames/native-pc/setup)

# Play Games Services Recall Stay organized with collections Save and categorize content based on your preferences.




Seamlessly sign users into your game while continuing to use your own account
system. With Play Games Services Recall APIs you can link in-game accounts with
a Google Play Games Services account. Then when a user plays your game across
different devices (or the same device after reinstalling your game), you query
the linked in-game account and streamline the sign-in flow.

If you have integrated with the [Android Recall APIs](/games/pgs/recall/recall-setup), these
Recall APIs should look familiar. Any server-side integrations with Play Games
Services Recall can be reused by PC titles as they are the same across both
Android and PC.

**Namespace:** `PlayPcSdkManaged.Recall`

**Client Class:** `RecallClient`

## Prerequisites

* Read the overview of [Play Games Services Recall API](/games/pgs/recall).
* Complete [Google Play Games Services setup](/games/pgs/console/setup) in the Play Console.

## Add your Play Games Services project ID in the manifest

After completing the Play Games Services setup in the Play Console, your game
now has an associated Play Games Services project ID. Using this project ID,
which can be found inside the Play Games Services
[Configuration page](https://play.google.com/console/u/0/developers/app/games/configuration-summary) in the Play Console,
update your game's `manifest.xml`.

Example `manifest.xml` contents:

```
<?xml version="1.0" encoding="utf-8"?>
<?Manifest version="1">
   <?Application>
     <?PackageName>com.example.package<?/PackageName>
     <?PlayGamesServices>
          <?ProjectId>123456789<?/ProjectId>
     <?/PlayGamesServices>
   <?/Application>
<?/Manifest>
```

**Note:** If you want to use the PC SDK while developing in the Unity Editor
without needing to digitally sign your game executable or launch it from Google
Play Games. For additional manifest configuration steps, see
[developer mode setup guide](/games/playgames/native-pc/setup/developer_mode).

## Create the client

Always use the factory to create a `RecallClient`. This ensures that
Unity-safe callbacks are automatically registered.

```
using UnityEngine;
using System;
using System.Threading.Tasks;
// Required SDK Namespaces
using PlayPcSdkManaged.Recall;
using PlayPcSdkManaged.Unity;

public class RecallManager : MonoBehaviour
{
    private RecallClient _recallClient;

    public void SetupRecall()
    {
        try
        {
            // Creates the client with the required UnityRecallCallbacksHandler
            _recallClient = PlayPcSdkFactory.CreateRecallClient();
            Debug.Log("Recall Client created successfully.");
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to create Recall Client: {ex.Message}");
        }
    }

    private void OnDestroy()
    {
        // Always dispose of the client to clean up native C++ resources
        _recallClient?.Dispose();
    }
}
```

## Request Recall access

**Tip:** We recommend using the Recall API to query for linked in-game accounts
each time your game is launched. For new installs a linked in-game account can
be used to seamlessly sign in a user and restore their progress. For existing
installs, when the linked in-game account changes it signals that the user
switched accounts on a different device and you can save them time by switching
to that account.

When your game is handling a sign-in flow, for example adding an in-game
account, request Recall access using
[`RequestRecallAccessAsync`](/games/playgames/native-pc/unity/api_reference#playpcsdkmanaged-recall).

This call returns a **session ID** that is used by your backend to make
server-side calls to Google for linking and unlinking your in-game accounts
with a Play Games Services user.

```
public async Task RequestRecallAccessAsync()
{
    try
    {
        Debug.Log("Requesting Recall access...");

        // Async call to retrieve the session ID
        var result = await _recallClient.RequestRecallAccessAsync();

        if (result.IsOk)
        {
            // On success, access the RecallSessionId
            var sessionId = result.Value.RecallSessionId;
            Debug.Log($"Recall Access Granted! Session ID: {sessionId}");

            // Pass 'sessionId' to your backend server to process account linking
        }
        else
        {
            // Handle expected API errors (e.g., Error)
            Debug.LogError($"Request Failed: {result.Code} - {result.ErrorMessage}");
        }
    }
    catch (Exception ex)
    {
        Debug.LogException(ex);
    }
}
```

## Process the Recall session ID

Once your game has the Recall session ID and has passed it to your backend game
server, use the [Play Games server-side REST APIs](/games/services/web/api/rest/v1/recall) to:

* Query for existing linked in-game accounts using
  [`recall.retrieveTokens`](/games/services/web/api/rest/v1/recall/retrieveTokens)
* Add or update linked in-game accounts using
  [`recall.linkPersona`](/games/services/web/api/rest/v1/recall/linkPersona)
* Delete linked in-game accounts using
  [`recall.unlinkPersona`](/games/services/web/api/rest/v1/recall/unlinkPersona)

For a more detailed guide covering the server-side integration, see the
documentation covering how to
[use the Recall API within your game server](/games/pgs/recall/recall-setup#using-recall).