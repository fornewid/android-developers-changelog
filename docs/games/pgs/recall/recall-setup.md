---
title: https://developer.android.com/games/pgs/recall/recall-setup
url: https://developer.android.com/games/pgs/recall/recall-setup
source: md.txt
---

This page explains how to implement the [Recall API](https://developer.android.com/games/pgs/recall) within your game. It
first covers setting up your game server and client to support the API, and then
explains how to store and retrieve tokens.

## Game server setup

Set up your game server to make Recall API calls to Google servers.

### 1. Set up your Play Games Services project

If you haven't already done so, follow the instructions in [Set up Google Play
Games Services](https://developer.android.com/games/pgs/console/setup).

> [!NOTE]
> **Note:** Recall tokens and personas are available on a per-PGS project basis. For separate PGS projects, there are separate collections of links between PGS profiles and personas. For more information, see the documentation on [setting
> up your PGS projects](https://developer.android.com/games/pgs/console/setup#add_your_game_to_the).

### 2. Set up a service account for the game

Follow the instructions on [creating a service account](https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount). At the end you
should have a JSON file with service account credentials.

> [!NOTE]
> **Note:** The Recall API is a server-to-server API. Because of this, the Recall API uses service accounts to authenticate the game server, not regular 3-legged OAuth, which is used by other Games APIs to authenticate both game servers and end users.

### 3. Download server-side Java library for PlayGamesServices

Download the [google-api-services-games library](https://github.com/googleapis/google-api-java-client-services/tree/main/clients/google-api-services-games) and upload it to your
server.

### 4. Prepare credentials for Recall API calls

See [Preparing to make an authorized API call](https://developers.google.com/identity/protocols/oauth2/service-account#authorizingrequests) for more context.

    import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
    import com.google.api.services.games.Games;
    import com.google.api.services.games.GamesScopes;

    // ...

    GoogleCredential credential =
      GoogleCredential.fromStream(new FileInputStream("<credentials>.json"))
        .createScoped(Collections.singleton(GamesScopes.ANDROIDPUBLISHER));

    Games gamesApi =
        new Games.Builder(httpTransport, JSON_FACTORY, credential).build();

## Game client setup

Set up your game client to retrieve the recall session IDs used by our server to
communicate with Google servers.

### Java SDK

[Set up the Java SDK within your client](https://developer.android.com/games/pgs/android/android-start), and make sure to include
`com.google.android.gms:play-services-games-v2:19.0.0`
and `com.google.android.gms:play-services-tasks:18.0.2` or later in your
Gradle file.

To communicate with Google's servers with the correct information, you need to
request a Recall session ID from the client SDK, which you send to your game's
server.

### Kotlin

    PlayGames.getRecallClient(getActivity())
                    .requestRecallAccess()
                    .addOnSuccessListener { recallAccess -> val recallSessionId: String = recallAccess.getSessionId() }
                    // Send the recallSessionId to your game server

### Java

    PlayGames.getRecallClient(getActivity())
      .requestRecallAccess()
      .addOnSuccessListener(
        recallAccess -> {
          String recallSessionId = recallAccess.getSessionId();
          // Send the recallSessionId to your game server
        });

### Unity SDK

If you haven't already done so, [set up the Unity SDK within your client](https://developer.android.com/games/pgs/unity/unity-start).

To communicate with Google's servers with the correct information, you need to
request a Recall session ID from the client SDK, and send it to your game's
server.

    PlayGamesPlatform.Instance.RequestRecallAccess(
        recallAccess => {
            string recallSessionId = recallAccess.sessionId;
            // Send the recallSessionId to your game server
        });

### v2 Native SDK (beta)

If you haven't already done so,
[get started with Play Games Services for C and C++](https://developer.android.com/games/pgs/cpp/cpp-start).

    // Include the following headers

    #include "play_games.h"
    #include "recall_client.h"
    #include "pgs_status_code.h"

    // Request Recall Access
    // Initializes the Play Games Services v2 Native SDK (beta).
    Pgs_initialize(javaVM, activity);

    //Creating Recall Client
    PgsRecallClient* pgs_recall_client =
          PgsRecallClient_create(activity);

    // RequestRecallAccess Function
    PgsRecallClient_requestRecallAccess(
        pgs_recall_client,

        // This is your callback function defined as an inline lambda
        [](PgsStatusCode status_code, char* session_id, user_data) {

            if (status_code == PGS_STATUS_SUCCESS) {
                // Recall Session Id Fetched Successfully
            } else {
                // Fetching Recall Session Id Failed
                // Handle error based on status_code.
                // Examples:
                // PGS_STATUS_NETWORK_ERROR: Check internet connection.
                // PGS_STATUS_INTERNAL_ERROR: An unexpected error occurred.
            }

            // Clean up the client instance passed as user_data
            PgsRecallClient* client = static_cast<PgsRecallClient*>(user_data);
            if (client != nullptr) {
                PgsRecallClient_destroy(client);
            }
        },

        user_data // Data to pass to the callback
    );

    // Shuts down the Play Games Services v2 Native SDK (beta).
    Pgs_destroy()

## Use the Recall API within your game server

After configuring your server and client, you can send the `recallSessionID`
from your game client to your game server and follow the following guidance to
start using the Java API to store, retrieve, or delete the Recall tokens
server-side.

### Store tokens

A player account in the Google Play Games Recall API consists of two pieces
of information:

- a **Persona** serving as a stable identifier for an in-game account
- a **Token** serving as the key to securely sign a player into the account

You can store a user's persona and token by using the `LinkPersonaRequest`
object. Use the `GoogleCredential` to call Google APIs (See [Calling Google
APIs](https://developers.google.com/identity/protocols/oauth2/service-account#callinganapi) for context). A persona has a **1:1 cardinality constraint** : a PGS
profile can contain only one persona, and a persona can belong to only one PGS
profile. Set the [conflicting links resolution policy](https://developer.android.com/games/services/web/api/rest/v1/recall/linkPersona#conflictinglinksresolutionpolicy) to define
how violations of the 1:1 cardinality constraint should resolve.

Optionally set the expiration time of the token. Use [`SetTtl()`](https://googleapis.dev/java/google-api-services-games/latest/com/google/api/services/games/model/LinkPersonaRequest.html#setTtl-java.lang.String-) with a
[`Durations`](https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/util/Durations) object to set a Time to Live or provide an exact expiration
time with [`setExpireTime()`](https://googleapis.dev/java/google-api-services-games/latest/com/google/api/services/games/model/LinkPersonaRequest.html#setExpireTime-java.lang.String-).

You must encrypt the persona and game token, and they cannot contain personally
identifiable information. Persona and token strings can be at most 256
characters long.

> [!NOTE]
> **Note:** The encryption key used for encrypting tokens should be unique for each application. If the game is transferred to another developer, the encryption key must be passed to the new owner. The recall tokens can't be decrypted without the original encryption key.

> [!NOTE]
> **Note:** Tokens created for [profileless users](https://developer.android.com/games/pgs/recall#profileless) have a default TTL of 30 days. Otherwise, for users with PGS profiles, tokens don't have a default TTL.

    import com.google.api.services.games.Games.Recall.LinkPersona;
    import com.google.api.services.games.model.LinkPersonaRequest;
    import com.google.api.services.games.model.LinkPersonaResponse;
    import com.google.protobuf.util.Durations;

    // ...

    Games gamesApi =
        new Games.Builder(httpTransport, JSON_FACTORY, credential).build();

    String recallSessionId = ... // recallSessionID from game client
    String persona = ... // encrypted opaque string, stable for in-game account
    String token = ... // encrypted opaque string encoding the progress line

    LinkPersonaRequest linkPersonaRequest =
      LinkPersonaRequest.newBuilder()
        .setSessionId(recallSessionId)
        .setPersona(persona)
        .setToken(token)
        .setCardinalityConstraint(ONE_PERSONA_TO_ONE_PLAYER)
        .setConflictingLinksResolutionPolicy(CREATE_NEW_LINK)
        .setTtl(Durations.fromDays(7)) // Optionally set TTL for token
        .build();

    LinkPersonaResponse linkPersonaResponse =
      gamesApi.recall().linkPersona(linkPersonaRequest).execute();

    if (linkPersonaResponse.getState() == LINK_CREATED) {
      // success
    }

### Retrieve tokens

There are three options to retrieve a token, based on your games' needs. You can
request the following:

- The tokens associated with the current game, including game-scoped recall tokens.
- The last token stored across all games owned by the developer account.
- Given a list of games owned by the developer account, all the recall tokens associated with each game.

> [!NOTE]
> **Note:** When you request recall tokens, the API doesn't return strings that represent the persona.

#### Game-scoped recall tokens

To retrieve the recall tokens from the current game, get the `recallSessionId`
from the client and pass it into the `retrieveTokens` API:

    import com.google.api.services.games.Games;
    import com.google.api.services.games.model.RetrievePlayerTokensResponse;
    import com.google.api.services.games.model.RecallToken;

    // ...

    String recallSessionId = ... // recallSessionID from game client

    RetrievePlayerTokensResponse retrievePlayerTokensResponse =
      gamesApi.recall().retrieveTokens(recallSessionId).execute();

    for (RecallToken recallToken : retrievePlayerTokensResponse.getTokens()) {
      String token recallToken.getToken();
      // Same string as was written in LinkPersona call
      // decrypt and recover in-game account
    }

#### Latest recall token across all games owned by developer account

To retrieve the most recent token stored across all games owned by the developer
account in the Google Play Console, you need to get the `recallSessionId` from
the client and pass it into the `lastTokenFromAllDeveloperGames` API, as shown
in the following code snippet. As part of the response, you can inspect the
[Application ID](https://developer.android.com/build/configure-app-module#set-application-id) associated with this token.

    import com.google.api.services.games.Games;
    import com.google.api.services.games.model.RetrieveDeveloperGamesLastPlayerTokenResponse;
    import com.google.api.services.games.model.GamePlayerToken;
    import com.google.api.services.games.model.RecallToken;

    // ...

    String recallSessionId = ... // recallSessionID from game client

    RetrieveDeveloperGamesLastPlayerTokenResponse response =
            gamesApi.recall().lastTokenFromAllDeveloperGames(recallSessionId)
            .execute();

    if (response.hasGamePlayerToken()) {
        GamePlayerToken gamePlayerToken = response.getGamePlayerToken();

        // The ID of the application that the token is associated with.
        String applicationId = gamePlayerToken.getApplicationId();

        // Same string as was written in LinkPersona call.
        RecallToken recallToken = gamePlayerToken.getRecallToken();

        // Decrypt and recover in-game account.
    }

#### All recall tokens across a given list of games owned by the developer account

To retrieve all the tokens associated with a list of games which are owned by
your developer account in the Google Play Console, get the `recallSessionId`
from the client and pass it into the `gamesPlayerTokens` API. Supply a list of
[Application IDs](https://developer.android.com/build/configure-app-module#set-application-id).

    import com.google.api.services.games.Games;
    import com.google.api.services.games.model.RetrieveGamesPlayerTokensResponse;
    import com.google.api.services.games.model.GamePlayerToken;
    import com.google.api.services.games.model.RecallToken;

    // ...

    String recallSessionId = ... // recallSessionID from game client

    // Application IDs for which you would like to retrieve the recall tokens.
    List<String> applicationIds = ...

    RetrieveGamesPlayerTokensResponse response =
    gamesApiClient
            .recall()
            .gamesPlayerTokens(recallSessionId)
            .setApplicationIds(applicationIds)
            .execute();

    for (GamePlayerToken gamePlayerToken : response.getGamePlayerTokens()) {
        // The ID of the application that the token is associated with.
        String applicationId  = gamePlayerToken.getApplicationId();

        // Same string as was written in LinkPersona call.
        RecallToken recallToken = gamePlayerToken.getRecallToken();

        // Decrypt and recover in-game account.
    }

### Delete recall token

If needed, you can also delete the recall token with the following call:

    import com.google.api.services.games.Games;
    import com.google.api.services.games.model.UnlinkPersonaRequest;
    import com.google.api.services.games.model.UnlinkPersonaResponse;

    // ...

    String recallSessionId = ...
    String persona = ...
    String token = ...

    Games gamesApi =
        new Games.Builder(httpTransport, JSON_FACTORY, credential).build();

    UnlinkPersonaRequest unlinkPersonaRequest =
      UnlinkPersonaRequest.newBuilder()
        .setSessionId(recallSessionId)
        .setPersona(persona)
        // .setToken(token) - alternatively set token, but not both
        .build();

    UnlinkPersonaResponse unlinkPersonaResponse =
      gamesApi.recall().unlinkPersona(unlinkPersonaRequest).execute();

    boolean unlinked = unlinkPersonaResponse.isUnlinked();

## Enable profileless mode

You can enable [limited Recall API functionality](https://developer.android.com/games/pgs/recall#profileless) for users that don't have
PGS profiles by following these steps:

1. Enable profileless recall for your PGS game project in the Play Developer Console. ![Select the option labeled "Turn on
   storage".](https://developer.android.com/static/images/games/pgs/play-console-recall.png)
2. Review the [additional terms](https://developer.android.com/games/pgs/recall/recall-setup#terms) described later in this section.
3. Add the following metadata tag into your [app manifest](https://developer.android.com/guide/topics/manifest/manifest-intro):

    <meta-data
      android:name="com.google.android.gms.games.PROFILELESS_RECALL_ENABLED"
      android:value="true" />

### Additional terms

You must also comply with the [Play Games Services Terms of Service](https://developers.google.com/games/services/terms). If you
use the Recall API for users without a PGS profile, which involves sharing
end-user data with Google, you must, before sharing this data with Google,
provide end users with an appropriate notice that describes the following:

- How you share data with Google to enable the Play Games account linking feature.
- The availability of settings to manage this sharing, for example, through Play Games settings.
- The processing of this data under the [Google Privacy Policy](https://policies.google.com/privacy), and the requirement to obtain appropriate end-user consent for this sharing that meets all applicable legal requirements.