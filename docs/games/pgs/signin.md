---
title: https://developer.android.com/games/pgs/signin
url: https://developer.android.com/games/pgs/signin
source: md.txt
---

| **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
| documentation](https://developer.android.com/games/pgs/v1/signin).

To integrate your game with Google Play Games Services, first implement platform
authentication. This is required to access all other features, such as
achievements, leaderboards, and events.

To meet the Google Play Games Level Up [user experience guidelines](https://developer.android.com/games/guidelines),
your game needs to be compliant with the [recommended authentication flow](https://developer.android.com/games/pgs/signin#sign-in-flow).

## Initialization and authentication

This is a required step to initialize and authenticate your game:

- Implement platform authentication by initializing the Play Games Services v2 SDK on startup. For more information, see [platform authentication for Android games](https://developer.android.com/games/pgs/android/android-signin). This is a required step for accessing Play Games Services features like achievements and leaderboards.
- Authentication runs as a silent background process during game launch.
- Existing Play Games Services users will see a welcome message upon successful
  authentication.

  ![Automatic sign-in prompt](https://developer.android.com/static/images/games/pgs/automatic-sign-in.gif)

## Profile creation

Players need a Play Games Services profile to engage with the platform. Some
players might not have a Play Games Services profile when they start your game.
These players will be asked to create one.

Auto-triggered profile creation prompts appear automatically by default when you
launch a game without a Play Games Services profile.
[![Profile creation prompt when you launch a game.](https://developer.android.com/static/images/games/pgs/profileprompt.png)](https://developer.android.com/static/images/games/pgs/profileprompt.png) Profile creation prompt when you launch a game (click to enlarge).

## Recommended authentication flow

To meet the Google Play Games Level Up user experience guidelines, verify that you are
compliant with the [player continuity](https://developer.android.com/games/guidelines#gameplay-continuity)
requirements. In order to successfully sign players into your game, use the
following authentication flow:

1. During the startup sequence of your game, implement the auto-triggered [profile creation](https://developer.android.com/games/pgs/signin#automatic-sign-in).
2. If automatic authentication fails or you decline, show a manual sign-in button so you can authenticate later.

## Player ID

A player ID is an identifier for a Play Games Services player account. Your
game can retrieve a player ID for any player that signs into your game using
Play Games Services authentication. Your
[game client integration](https://developer.android.com/games/pgs/signin#client-integration),
[game server integration](https://developer.android.com/games/pgs/signin#secure-access), and
[cloud-save service](https://developer.android.com/games/pgs/savedgames) can use the ID to securely access
player data from Play Games Services.

A player ID is consistent for a user when they play your game on multiple
devices. However, it is not always consistent between games.
For more information, see [next generation Player IDs](https://developer.android.com/games/pgs/next-gen-player-ids).

## OAuth Scopes

Play Games Services relies on the
[OAuth system](https://developers.google.com/identity/protocols/OAuth2)
to allow players to give your game access to their account. Play Games Services
has a unique scope for games (`games-lite`) and relies on another scope
(`drive.appdata`) if your game uses the saved games feature. The saved games
feature gives access to the user's Google Drive account, which is where the game
data is stored.

When using the Play Games Services v2 SDK, you can request extra
[OAuth scopes](https://developers.google.com/identity/protocols/googlescopes).
If you need extra OAuth scopes, we recommend calling `requestServerSideAccess`.
For more information, see
[get the server auth code](https://developer.android.com/games/pgs/android/server-access#get-auth-code) or [retrieve server authentication codes](https://developer.android.com/games/pgs/unity/unity-start#retrieve-auth-codes).

## Multiple authentication services

Play Games Services provides a gaming identity for Android players, but it
doesn't need to be the only identity connected to your users. You can authenticate
players using Play Games Services, a social network ID, and your own in-game ID
system all at the same time.

## Recall API

The [Recall API](https://developer.android.com/games/pgs/recall) lets games manage links between PGS users
and their in-game accounts by storing recall tokens with Google servers. To
learn more about enabling this feature, see [Integrate the PGS Recall API
within your game](https://developer.android.com/games/pgs/recall/recall-setup).

## Game client integration

When integrating authentication into your game project, we recommend the following
user flow:

1. During the startup sequence of your game,
   [Profile creation](https://developer.android.com/games/pgs/signin#automatic-sign-in) launches and attempts to authenticate the
   user or create a new account.

2. If automatic authentication fails or you decline, show a manual sign-in
   button so you can authenticate later.

For information about integrating authentication in your game project, see the
documentation for your project type:

- [C and C++ games](https://developer.android.com/games/pgs/cpp/cpp-start)

- [Unity games](https://developer.android.com/games/pgs/unity/unity-start)

- [Java games](https://developer.android.com/games/pgs/android/android-signin)

## Game server integration

You can obtain a server authorization code by calling `requestServerSideAccess`
once you have verified that the player is authenticated. Pass this server
authorization code to your backend game server to communicate directly with
Play Games Services servers. This communication
allows your server to access player data, including:

- Player ID
- Profile
- Friends list
- Game progress
- Achievements

Your server then uses this authorization code with
the [REST API](https://developer.android.com/games/services/web/api/rest) to interact securely with
Play Games Services servers.
For more information, see
[Server-side access to Play Games Services](https://developer.android.com/games/pgs/android/server-access).

## Login request quota

There is a daily quota for login requests with Play Games Services. For more
information, see [Managing your daily quota](https://developer.android.com/games/pgs/quota#manage-daily-quota).