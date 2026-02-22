---
title: https://developer.android.com/games/pgs/account-linking
url: https://developer.android.com/games/pgs/account-linking
source: md.txt
---

Seamless Restore is a Google Play Games Services feature designed to immediately
reconnect returning players to their game progress when they install a game on a
new device or reinstall it, effectively removing the friction of a login screen.

Seamless Restore is a recommended guideline for the [Level Up](https://play.google.com/console/about/levelup/) program.

Use Google Play Games Services [authentication](https://developer.android.com/games/pgs/signin) to streamline the user platform
authentication experience for your game. Initialize the Play Games Services
SDK to trigger authentication, which removes the need for a separate platform
authentication flow.

## Link user accounts to enable continuity and cross-device Play

Players engage with their favorite games across a variety of devices and
platforms, including mobile, tablets, and PCs. A core expectation for these
players is the ability to seamlessly resume their gameplay exactly where they
left off, regardless of the device they choose.

A significant barrier that often leads to user abandonment is the
requirement to sign in separately on each new device. Users need immediate
immersion into the game experience, free from unnecessary interruptions.

To facilitate seamless continuity and cross-device play, you must implement two
key features:

- [Account linking](https://developer.android.com/games/pgs/account-linking#account-linking-recall-api)
- [Cloud Save](https://developer.android.com/games/pgs/savedgames)

The Play Games Services authentication process provides flexible
options for player identifiers. These options allow you to integrate
Play Games Services with your own existing identity solution.

## New Play Games Services integration

For games without existing Play Games Services integration, the [Recall API](https://developer.android.com/games/pgs/recall)
simplifies backend setup by managing account associations and storing the
connection between a user's game account and their
Play Games Services account.

### Account linking using Recall API

The Recall API is the recommended solution for linking user
accounts in cross-platform games. This API is particularly useful for games
without existing Play Games Services integration or those that use additional
platform authentication solutions beyond Play Games Services.

The Recall API simplifies your game's backend setup by managing account
associations.

- **Simplified backend:** The API streamlines your game's backend setup for account linking.
- **Play-Managed associations:** Play stores the association between users' game accounts (including third-party accounts) and their Play Games Services accounts.
- **Progress restoration:** Developers generate and send Recall tokens to Play, which can then be retrieved to restore a user's game progress.

When implementing the Recall API, developers must verify that Recall tokens are
opaque strings. These tokens must be free of any sensitive or
personally-identifiable information (such as name, email address, or
demographics) about gamers.

Games must use robust encryption algorithms when generating
Recall tokens to protect user data and maintain security.

To learn more about how Recall works, see [Recall API](https://developer.android.com/games/pgs/recall).

To implement the Recall API feature, see
[Integrate the Play Games Services Recall API within your game](https://developer.android.com/games/pgs/recall/recall-setup).

## Existing Play Games Services integration

This section explains how to integrate your game with Play Games Services by
binding player accounts. Learn how to use player IDs to identify authenticated
players and manage multiple game accounts for a single Play Games Services
user.

### Bind with a `Player_id`

A player ID is an identifier for a Play Games Services player account. Your
game can retrieve a player ID for any player who is authenticated into your game
using Play Games Services.

The games that have the backend set up with Play Games Services `Player_Id` or
the games that require support for child users, should use `Player_Id` and bind
their game and 3P accounts with `Player_Id`.

Understand how player IDs behave:

- **Consistent within a game:** A player ID remains consistent for a user across multiple devices when they play the same game.
- **Inconsistent between games:** Player IDs are not always consistent when a user plays different games.

For more information, see [next generation Player IDs](https://developer.android.com/games/pgs/next-gen-player-ids).

### Manage multiple accounts per user with binding

To link multiple user accounts to a single Play Games Services account, create
a one-to-many mapping in your table.
| **Note:** When restoring progress using the Play Games Services identifier, you must display account identifiers clearly to the user. Then, prompt the user to select which account to restore.

## Cross-platform Google identity using Sign in with Google

[Sign in with Google](https://developers.google.com/identity/siwg) (SiwG) is Google's primary identity solution that
lets game developers to securely receive their player's profile information:
their name, email address, and profile picture.

A key benefit of Sign in with Google is its broad availability across platforms,
including [web](https://developers.google.com/identity/gsi/web/guides/overview), [Android](https://developer.android.com/identity/sign-in/credential-manager-siwg), and [iOS](https://developers.google.com/identity/sign-in/ios/start-integrating). It provides a fast, secure, and
familiar sign-in experience that players already know and trust.
| **Important:** Sign in with Google solution is not the same as Google Play Games Services authentication. Instead, Sign in with Google is designed to complement, not replace, your identity solution or Play Games Services integration.

### Bind with Google ID token's `sub` field

To create a seamless cross-platform experience, you can implement an
authentication strategy that links your game's account system to a unique
Google Account identifier. This approach leverages the streamlined
Play Games Services authentication on Android while using the standard
Sign in with Google SDK on other platforms like iOS and Web.

The `sub` field from the Google [ID token](https://developers.google.com/identity/openid-connect/openid-connect#an-id-tokens-payload) is a unique and persistent
identifier for a Google user's account. This `sub` field is identical across all
platforms for the same user. Use this `sub` value as the unique key in your
backend to bind and restore player progress across devices. This key links all
of a player's sessions to a single game account in your backend.

Here is the high-level flow:

- **On Android:** Your game initializes the Play Games Services SDK to trigger platform authentication automatically on Android devices. When you [sign in with Google on Android](https://play.google.com/console/about/levelup/), request the three [sign-in scopes](https://developers.google.com/identity/protocols/oauth2/scopes#oauth2): `email`, `profile`, and `openid`. Don't use Play Games Services v2 integration. These are the same scopes that a standard SiwG SDK requests. This lets you retrieve an [ID token](https://developers.google.com/identity/openid-connect/openid-connect#an-id-tokens-payload) that contains the player's `sub` field.
- **On Web and iOS:** Your game uses the standard [Sign in with Google for web](https://developers.google.com/identity/gsi/web/guides/overview), [Google Sign in for iOS and macOS](https://developers.google.com/identity/sign-in/ios/start-integrating) SDKs. When the user signs in, the SiwG SDK provides an ID token that also contains the user's `sub` field.
- **Account Binding:** Because the user is signing in with the same Google Account on both platforms, the `sub` field you receive will be identical. You can then confidently bind this `sub` value to your internal user ID in your identity solution, creating a unified user experience.

### Integration on Android

On Android, initialize the Play Games Services SDK to trigger platform
authentication automatically on Android devices. Then, when you [sign in with
Google on Android](https://play.google.com/console/about/levelup/), request the three [sign-in scopes](https://developers.google.com/identity/protocols/oauth2/scopes#oauth2): `email`,
`profile`, and `openid`. This lets you retrieve a server-side auth code, which
your backend can exchange for an ID token containing the user's information
including the unique `sub` field.

At a high level, the implementation involves:

1. **Set Up Client IDs in a Unified Project:** Before you integrate, you must
   [set up Play Games Services in the Google Play Console](https://developer.android.com/games/pgs/console/setup) to obtain your
   OAuth 2.0 Client IDs.

   | **Important:** For cross-platform linking, this Google Cloud project must be used for all platforms. Any Client IDs you create later for other platforms (like Web and iOS) must be added to this exact same project.
2. **Configure Play Games Services:** First, add your game in the [Google Play
   Console](https://play.google.com/apps/publish/) and integrate [Play Games Services platform authentication](https://developer.android.com/games/pgs/signin)
   with your game.

3. **Add a Sign in with Google Button:** On your game's sign-in page or user
   settings screen, add a [Sign in with Google](https://play.google.com/console/about/levelup/) button. This button will
   trigger the sign in or up flow. When you create this button, it is
   recommended that you follow the
   [Sign in with Google branding guidelines](https://developers.google.com/identity/branding-guidelines). At a minimum, the button
   should clearly display "Google" or "Sign in with Google". The guidelines
   link also provides downloadable UX assets that are compliant and can be
   used in your game.

4. **Request the Server Auth Code with Sign-in Scopes:** When the player clicks
   the button, your game requests a one-time server auth code. The most
   important step is to configure this request to include the following
   [sign-in scopes](https://developers.google.com/identity/protocols/oauth2/scopes#oauth2): `EMAIL`, `PROFILE`, and `OPEN_ID`.

   How you configure this depends on your development environment:
   - **For Java/Kotlin:** See the guide to [get the server auth code](https://developer.android.com/games/pgs/android/server-access#get-auth-code)
     using `requestServerSideAccess`.

   - **For Unity:** See the guide to [retrieve auth codes in Unity](https://developer.android.com/games/pgs/unity/unity-start#retrieve-auth-codes).

5. **Exchange Auth Code and Verify ID Token on Backend:** Send the auth code
   from the previous step to your backend server. On the server, follow the
   standard [OAuth 2.0 code exchange flow](https://developer.android.com/games/pgs/android/server-access#send-auth-code) guide to swap the code for an
   ID token, access token, and refresh token. As described in the guide, you
   must verify the ID token on your server.

6. **Bind the `sub` Field:** Once the ID token is successfully verified,
   extract the `sub` field from its payload. Use this `sub` value as the
   unique key for Google identity in your identity solution.

   - **If this `sub` value already exists** in your database, the user has
     linked before. Sign them into their corresponding game account.

   - **If this `sub` value doesn't exist** , you can either create a new
     user account in your game's account system associated with this
     `sub`, or link to an existing user account in your account system by
     matching user information (like the email address) provided in the
     ID Token.

### Integration in iOS, Web, and other platforms

On platforms other than Android, iOS, Web, or PC, you will use the
standard Sign in with Google SDKs. The goal is the same as the Android flow: to
securely get a Google ID token, send it to your backend, and use the `sub`
field to link the account.

At a high level, the implementation involves:

1. **Client-Side Integration:** Follow the official documentation to integrate
   the Sign in with Google SDK for your platform. These guides cover the
   complete client-side flow, from rendering a Sign in with Google button to
   retrieving the ID token.

   - **For Web:** [Sign in with Google for Web](https://developers.google.com/identity/gsi/web/guides/overview)

   - **For iOS:** [Google Sign-In for iOS and macOS](https://developers.google.com/identity/sign-in/ios/start-integrating)

   - For platforms without a dedicated SDK (like a custom game engine or
     PC build), you can manually implement the [OAuth 2.0 web server flow](https://developers.google.com/identity/protocols/oauth2/web-server)
     to get the necessary tokens.

2. **Backend Logic:** Send the ID token (or auth code) to your backend. Your
   server then performs the exact same verification and `sub` field binding
   logic as described in steps 4 and 5 of the "Integration on Android" section.

Because the `sub` field from all these Sign in with Google flows is identical
to the one retrieved from the Google Play Games Services flow on Android (for the same
Google account), this process successfully links the user's account across all
platforms.