---
title: https://developer.android.com/games/pgs/recall
url: https://developer.android.com/games/pgs/recall
source: md.txt
---

The Recall API lets games manage links between Google Play Games Services (PGS) users and
their in-game accounts by storing *recall tokens* with Google servers. Here's a
sample scenario of how the Recall API might be used.

1. A user is playing a game where the developer has an identity system to track
   user progress, and uses PGS in parallel with other authentication methods to
   log users into their game. In this example, a user is logged into their PGS
   account *Laura* , and creates an in-game account with the developer's
   identity system called *Racer94*. As the user plays the game, the
   developer's game server syncs their progress.

   ![User is logged in with PGS and an in-game
   account](https://developer.android.com/static/images/games/pgs/recall-overview-user-creates-account.png)
2. Separately, the developer saves a recall token with Google, which
   corresponds with the user's in-game account. Google automatically stores
   that recall token against the user's PGS profile.

   ![Game server stores recall token with Google
   servers](https://developer.android.com/static/images/games/pgs/recall-overview-game-server-stores-token.png)
3. The user now decides to play the game on [GPG on
   PC](https://developer.android.com/games/playgames/overview) for the first time. The user is automatically
   authenticated with their PGS account, and the game client checks to see if
   there is any progress available for this PGS user. The game server then
   queries Google to see if there are any tokens for this PGS account. Since
   there are, Google sends back the recall token, and the game server uses that
   token to find the user's associated account Racer94, and restore their
   progress. Since authenticating with PGS is a frictionless experience, the
   user's progress is restored by the app without the user needing to enter a
   username or password. Furthermore, the developer can use PGS
   authentication with their existing identity system, and rely on
   Google to store the link between player progress and their PGS account.

   ![Game server restores progress with recall
   token](https://developer.android.com/static/images/games/pgs/recall-overview-game-server-resores-progress.png)

As seen in the example earlier, there are two main actions which are performed
by the Recall API:

- **Storing** the token with Google when a user logs in with one of the in-game
  accounts.

- **Retrieving** the token for a user in order to restore their in-game
  accounts.

In addition to recall tokens, the Recall API also requires a stable identifier
corresponding to the in-game account, known as *persona* . You might think of a
persona as the label which represents the user's in-game account within the
developer's identity system, and the recall token as a key which is used to
restore the user's in-game account to the game. Persona and token values must
not be reused across different [PGS projects](https://developer.android.com/games/pgs/console/setup#add_your_game_to_the). Also, while recall tokens may
be changed over time, a persona should be stable according to the user's in-game
account.
| **Note:** Strings used for recall tokens and personas must be opaque and not contain any sensitive or personally-identifiable information (including but not limited to name, email address, and demographics). Games must use robust encryption algorithms for generating recall tokens.

## Technical flows for storing and retrieving the recall tokens

This section covers the technical flow between the game client and servers with
Google servers when storing and retrieving recall tokens.

### Step 1: Authenticate the PGS User and retrieve the session ID

The game initializes the PGS SDK and attempts to authenticate the user with PGS.

![User authentication with PGS](https://developer.android.com/static/images/games/pgs/recall-flow-user-pgs-signin.png)

Assuming the user is authenticated, request a session ID from the Games SDK on the
game client, and request an OAuth 2.0 token from Google's OAuth backend. The
session ID and OAuth 2.0 tokens are used to communicate with the Google Games
backend.

![Developer requests a session
ID](https://developer.android.com/static/images/games/pgs/recall-flow-request-session-id-without-login.png)

### Step 2: Retrieve any available recall token

Request for any associated recall token with the PGS user's account. If a token
is present, [proceed to Step 3a and restore progress](https://developer.android.com/games/pgs/recall#restore-progress).
Otherwise, if this is a new user and they have no token present, [proceed to
Step 3b and store a new token](https://developer.android.com/games/pgs/recall#store-tokens).

![Developer retrieves recall
token](https://developer.android.com/static/images/games/pgs/recall-flow-retrieve-token.png)

### Step 3a: If token is present, restore progress

If a token is present, retrieve and decrypt the token, and restore user data.

![Developer restores data from recall
token](https://developer.android.com/static/images/games/pgs/recall-flow-restore-data.png)

### Step 3b: If no token is present, store a token

Since no token is present, no progress is restored. The user proceeds to platform authentication
with the developer's identity system, or creates a new account if one does not
exist. Note - this isn't authenticating in with PGS (which has been done already), but
with a developer's identity system outside of PGS.

![User authenticates with their in-game
account](https://developer.android.com/static/images/games/pgs/recall-flow-user-game-signin.png)

Create an encrypted recall token which encodes the user's in-game account, and
send it to Google along with the session ID and OAuth 2.0 token. At this point,
Google creates an association between the recall token which was sent, and the
player's PGS account.

![Developer stores recall token](https://developer.android.com/static/images/games/pgs/recall-flow-store-token.png)

## Flows for users without a PGS profile

You can store recall tokens for a user who hasn't created a PGS profile yet by
using profileless mode. However, there are two important caveats:

- You can't retrieve tokens for a user who doesn't have a PGS profile. Profile creation is automatically prompted when the user tries to log into your game with Play Games Services on a second device.
- You must follow [additional guidelines](https://developer.android.com/games/pgs/recall/recall-setup#terms) to ensure you have an appropriate notice describing the following items and obtaining the appropriate end-user consent:
  - Your sharing of the data with Google to enable the Play Games account linking feature.
  - The availability of settings to manage this sharing, such as Play Games settings.
  - The processing of such data under the [Google Privacy
    Policy](https://policies.google.com/privacy).

### Store a token and persona pair

![User without PGS profile opens a game](https://developer.android.com/static/images/games/pgs/recall-profileless-flow.png)

1. A user without a PGS profile opens a game that has profileless recall enabled.
2. The Games SDK triggers an automatic platform authentication, which fails because the user has no PGS profile.
3. The Games SDK shows a snackbar that informs the user that the game has integration with Google. This snackbar is actionable---the user can disable recall until a profile is created.
4. The game requests recall access. Note that PGS rejects recall access requests when there are PGS profiles on the device or when there are no Google Accounts on the device. In that case, the game should proceed without using PGS.
5. After the user logs in with an in-game account, the game creates a token and persona pair for the user that corresponds to their in-game account. The game stores this pair with Google. The game might store more tokens later if the user logs into other in-game accounts.

### Launch a game on a new device

1. A user without a PGS profile opens a game that has profileless recall enabled on a device.
2. The game records a profileless recall token as described in [Store a token
   and persona pair](https://developer.android.com/games/pgs/recall#profileless-store).
3. The user opens the same game on a different device that has the same account setup.
4. The Games SDK triggers profile creation. The user can review and reject previously stored recall tokens. The user creates a PGS profile at this time.
5. The automatic platform authentication into PGS completes, and the game receives the authenticated status.
6. The game retrieves recall tokens for the user as usual.

## Next steps

In order to integrate the Recall API with your client and game server, [follow
this guidance](https://developer.android.com/games/pgs/recall/recall-setup).