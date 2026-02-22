---
title: https://developer.android.com/games/playgames/integrating-pgs-existing-id-solutions
url: https://developer.android.com/games/playgames/integrating-pgs-existing-id-solutions
source: md.txt
---

This page explains how to integrate
Play Games Services Sign In with your existing identity or cloud save
solution. Even though these recommendations are optional, they can help you
complete the
[cloud save requirements](https://developer.android.com/games/playgames/continuity-requirements) for
Google Play Games on PC. Use the [continuity requirements](https://developer.android.com/games/playgames/continuity-requirements) and
[expected behaviors](https://developer.android.com/games/playgames/continuity-expected-behaviors) pages to verify that your
implementation satisfies these requirements.

## Restore player state

In your game's backend, game accounts are likely represented by some identifier
that lets you fetch and update their progress within your game. We will call
this your account ID for short. When a player signs in to Play Games Services, you
can use that authentication to get a new identifier, the Play Games Services
Player ID, which is used to power the [cloud save
requirement](https://developer.android.com/games/playgames/continuity-requirements).

![Play Game Services Multi Idenitifier Workflow](https://developer.android.com/static/images/games/playgames/pgs-multi-identifier-workflow.png)

When a player logs in with Play Games Services, you should continue as follows:

1. Retrieve the OAuth code from the client, and send it to your server.
2. Exchange the authentication token and get a verified Play Games Services ID from the Play Games Server. This ensures that the id is trusted and not someone pretending to be another player by using a compromised device.
3. Attempt to resolve a game account based on the conditions of the device and any linked identifiers.

Two main new scenarios need to be introduced into your game:

- Storing Play Games Services IDs on your backend and assigning them to existing account IDs in some way, such as the following:
  - For new players, the progress should be automatically linked to Play Games Services at some point. (e.g. at game launch, after the tutorial or some number of levels, etc.).
  - For existing players, the current progress should be automatically linked to Play Games Services after the player updates to a version of your game with Play Games Services V2 integrated.
  - The Play Games Services ID can be linked with one or more accounts, and Play Games Services can be de-linked from those accounts, but it should be linked to at least one valid account.
- Automatically restoring game progress on a signed out/new device based on the Play Games Services Player ID.

How you store and assign Play Games Services IDs to existing accounts is
flexible, as outlined in the examples below. The main requirements to keep in
mind are that the player should not have to manually sign in or create a link with
another identity system in order to create a link between their
Play Games Services ID and game progress, and that player progress should
be seamlessly restored across surfaces.

When designing your solution, start by looking at your existing system
and how it incorporates different identity providers. Some systems use a single identifier per account, while others use multiple identifiers per account.

If you can only associate each account ID with a single identifier, you'll need
to add support to associate Play Games Services with it. The following solutions demonstrate how to do this.

## Example Solutions

The example solutions include **binding** and **recall** solutions.

Binding is the process of permanently or semi permanently linking the
Play Games Services ID to an account state. In the case of binding, the
underlying account that is restored through Play Games Services doesn't
change for the player without their action, even if they log out and log in with
another account within your game. We cover this here with
[account binding](https://developer.android.com/games/playgames/integrating-pgs-existing-id-solutions#account_binding).

![Strong Binding Flow](https://developer.android.com/static/images/games/playgames/pgs-strong-binding-flow.png)

With recall, you as the game developer store a loose mapping of
Play Games Services ID and last seen account(s) for the player to restore
when they sign in with Play Games Services on another device. Each time
the player logs in to another game account with the same
Play Games Services ID, this binding changes. Here's an example
flowchart, which we cover more in the [recall recent
accounts](https://developer.android.com/games/playgames/integrating-pgs-existing-id-solutions#recall_recent_accounts) example below:

![Recall Flow](https://developer.android.com/static/images/games/playgames/pgs-recall-flow.png)
![Recall Flowchart](https://developer.android.com/static/images/games/playgames/pgs-recall-flowchart.png)

More user flow examples are attached to the solutions below.

### Account binding

If your game doesn't have a lot of multi-account players, or if you like to
encourage gamers to have a single account within your game, then binding is
likely the best solution for your game. In this example, you bind the first
account seen while signed in with Play Games Services (whether a
guest account or one bound with another identity platform as well) with the
Play Games Services Player ID.
After this binding, that bound account is restored on new devices automatically.
Since we're doing a strong binding, the player can also switch
Play Games Services profiles to change accounts within the game, and you
can prompt the player to confirm in this scenario.

![Play Game Services Account Resolution Workflow](https://developer.android.com/static/images/games/playgames/pgs-account-resolution-workflow.png)

If there are conflicting accounts, we recommend that you ask
the player to choose an account. These conflicting cases should only happen to players that have multiple
accounts in your game, and so they likely have the knowledge and desire to play
with a specific account.

Once the account has been resolved, your game should remember the player's choice
unless there is a change in sign in identifiers. If the Play Games Services
profile is changed, or the player logs in to a different identifier within the
game, then the above steps should be repeated as the player
has given a strong signal that they desire a change in accounts.

#### Unbinding

If you'd like to offer the player the ability to completely control their
bindings, you can offer the player the ability to unbind their
Play Games Services Player ID with a game account. This could be important to
some multi-account players, if they accidentally bound their
Play Games Services Player ID with an account that isn't their main account.

#### Additional account binding examples

![Strong Binding Flow](https://developer.android.com/static/images/games/playgames/pgs-strong-binding-flow.png)

This main example shows that a given Play Games Services Player ID (1) is
bound to the first in-game account that is seen (A) and not rebound when the
player logs out of their game progress to play on another account.

You can optionally allow players to rebind their account, but it is not required.

##### Switching accounts on device

![Strong Binding Switch Accounts Flow](https://developer.android.com/static/images/games/playgames/pgs-strong-binding-switch-accounts-flow.png)

Here, the player has switched Play Games Services accounts manually, and
so has given the game a strong signal that they want to change their in-game
account to another account. Reacting to this change is what the player desires; taking this signal into consideration leads to a better player experience.

##### Existing bound account with another identifier

![Strong Binding Existing Account Flow](https://developer.android.com/static/images/games/playgames/pgs-strong-binding-existing-account-flow.png)

This example shows that even accounts bound to non Play Games Services
identifiers should be bound to Play Games Services and then restored on
new devices. Most existing players of your game with accounts will fall into this
category.

### Recall recent accounts

When thinking about solutions, one thing that will often come up is the
multi-account experience. If your game incentivises power users to create many
accounts (such as gacha games or choose your own adventure games), then binding
the Play Games Services Player ID to a single account might not provide the
best player experience when moving across devices.

In the recall solution, you store a loose mapping of a
Play Games Services Player ID and in-game account, and the player simply sees the
last accounts you've stored when switching devices or when logged out.

![Recall Flowchart](https://developer.android.com/static/images/games/playgames/pgs-recall-flowchart.png)

In this example, a player owns three accounts for a game, and then moves to a
new device:

![Recall Flow 2](https://developer.android.com/static/images/games/playgames/pgs-recall-flow-2.png)

When you prompt the player to restore, you can also offer a "cancel" or
"create new" button for players to select to create a new account.

For simplicity, your game could choose to only recall the last
seen account. This may be more difficult for the multi-account switching use case, but still
meets the continuity requirement.

#### Additional recall examples

The following section includes additional examples using recall.

##### Non-Android phones

![Recall Non-Android Flow](https://developer.android.com/static/images/games/playgames/pgs-recall-non-android-flow.png)

Here we illustrate both recalling accounts that already exist (3rd party account linked),
or that were created from another non Play Games Services signed in
device.

A more common flow may be starting from a non Android phone and moving to
Google Play Games on PC.

![Recall Non-Android Flow 2](https://developer.android.com/static/images/games/playgames/pgs-recall-non-android-flow-2.png)

Since the non Android phone does not have Play Games Services, there is no
recall active, and the player has to manually type in their credentials from
within Google Play Games on PC.

##### Multiple Play Games Services profiles for one account

Occasionally there might be multiple Play Games Services profiles active
that have previously "recalled" a given account. For this case, there are two
main solutions that would work equally well:

**Save it anyways**
![Recall Multiple Profiles Save Anyways Flow](https://developer.android.com/static/images/games/playgames/pgs-recall-multiple-profiles-save-anyway-flow.png)
We disregard duplicate pointers to a given account in the "Save it anyways" model.

**Override it**
![Recall Multiple Profiles Override Flow](https://developer.android.com/static/images/games/playgames/pgs-recall-multiple-profiles-override-flow.png)
In the "Override it" model, the developer needs to remember Play Games Services to
Account mappings and clear old mappings in their tables in the "Override it" model. By doing so, they can
keep a clean 1:1 mapping of recalled accounts and Play Games Services
accounts.

**Same Device Recall**
![Recall Same Device Flow](https://developer.android.com/static/images/games/playgames/pgs-recall-same-device-flow.png)
A multi-account player can use your recall implementation to quickly switch
between their game accounts too.