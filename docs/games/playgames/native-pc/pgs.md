---
title: https://developer.android.com/games/playgames/native-pc/pgs
url: https://developer.android.com/games/playgames/native-pc/pgs
source: md.txt
---

Seamlessly sign users into your game while continuing to use your own account
system. With Play Games Services Recall APIs you can link in-game accounts with
a Google Play Games Services account, then when a user plays your game across
different devices (or the same device after re-installing your game) you query
the linked in-game account and streamline the sign-in flow.

If you have integrated with the [Android Recall APIs](https://developer.android.com/games/pgs/recall/recall-setup), these
Recall APIs should look familiar. Any server-side integrations with Play Games
Services Recall can be reused by PC titles as they are the same across both
Android \& PC.

## Prerequisites

- Complete the [SDK setup](https://developer.android.com/games/playgames/native-pc/setup).

- Read the overview of [Play Games Services Recall API](https://developer.android.com/games/pgs/recall).

- Complete [Google Play Games Services setup](https://developer.android.com/games/pgs/console/setup) in the Play Console.

## **Step 1**: Add your Play Games Services project ID in the manifest

After completing the Play Games Services setup in the Play Console, your game
now has an associated Play Games Services' project ID. Using this project ID,
which can be found inside Play Games Service's
[Configuration page](https://play.google.com/console/u/0/developers/app/games/configuration-summary) in the Play Console, update
your game's `manifest.xml`.

Example `manifest.xml` contents:

    <?xml version="1.0" encoding="utf-8"?>
    <Manifest version="1">
        <Application>
            <PackageName>com.example.package</PackageName>
            \<PlayGamesServices\>
    \<ProjectId\>123456789\</ProjectId\>
    \</PlayGamesServices\>
        </Application>
    </Manifest>

## **Step 2**: Request Recall access when signing-in

> [!TIP]
> **Tip:** We recommend using the Recall API to query for linked in-game accounts each time your game is launched. For new installs a linked in-game account can be used to seamlessly sign-in a user and restore their progress. For existing installs, when the linked in-game account changes it signals that the user switched accounts on a different device and you can save them time by switching to that account.

When your game is handling a sign-in flow, for example adding an in-game
account, request Recall access using
[`GamesRecallClient::RequestRecallAccess()`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/games/recall/games-recall-client#requestrecallaccess).

This call returns a session ID which is used by your backend to make server-side
calls to Google for linking \& unlinking your in-game accounts with a Play Games
Services user.

    auto promise = std::make_shared<std::promise<RecallAccessResult>>();
    games_recall_client.RequestRecallAccess(params, [promise](RecallAccessResult result) {
       promise->set_value(std::move(result));
    });

    auto recall_access_result = promise->get_future().get();
    if (recall_access_result.ok()) {
       auto recall_session_id = recall_access_result.value().recall_session_id;
       // Pass the recall session ID to your backend game server so it can query
       // for an existing linked in-game account.
       // - If you discover an existing linked in-game account, continue to sign-in
       //   the in-game account. This provides a seamless cross-device sign-in
       //   experience.
       // - If there is not an existing linked in-game account, when the user
       //   completes the sign-in using your in-game account system record the
       //   account linking with Play Games Services Recall. This helps to provide
       //   a seamless cross-device sign-in experience when the user returns on a
       //   different device or after re-installing your game on the same device.
    } else {
       // Handle the error
    }

## **Step 3**: Process the Recall session ID

Once your game has the Recall session ID and has passed it to you backend game
server, use the [Play Games server-side REST APIs](https://developer.android.com/games/services/web/api/rest/v1/recall) to:

- Querying for existing linked in-game accounts using [`recall.retrieveTokens`](https://developer.android.com/games/services/web/api/rest/v1/recall/retrieveTokens)
- Add or update linked in-game accounts using [`recall.linkPersona`](https://developer.android.com/games/services/web/api/rest/v1/recall/linkPersona)
- Delete linked in-game accounts using [`recall.unlinkPersona`](https://developer.android.com/games/services/web/api/rest/v1/recall/unlinkPersona)

For a more detailed guide covering the server-side integration see the
documentation covering how to
[use the Recall API within your game server](https://developer.android.com/games/pgs/recall/recall-setup#using-recall).