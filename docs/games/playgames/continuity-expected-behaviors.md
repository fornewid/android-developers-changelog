---
title: https://developer.android.com/games/playgames/continuity-expected-behaviors
url: https://developer.android.com/games/playgames/continuity-expected-behaviors
source: md.txt
---

You can use the test cases below to see if your game satisfies our [continuity requirements](https://developer.android.com/games/playgames/continuity-requirements) with different scenarios. Please note that this is not an exhaustive list of all scenarios, and this document may be updated in the future.

As a prerequisite to these scenarios, Play Games Services v2 must be
integrated into the Android and Google Play Games on PC versions of your game.
You need to migrate your game to v2, even if you currently use v1. You cannot use Play Games Services v1 and v2 together.

Each scenario below displays the steps to replicate the scenario and the
expected results for the given step.

> [!NOTE]
> **Note:** Throughout these scenarios, at no point should the player have to opt-in to cloud save. This means that once you auto login with Play Games Services, the game should seamlessly save your game against your Play Games Services ID without needing to click any extra buttons. One exception to this situation is if the game asks to resolve a conflict (e.g. asks "You have an existing game with X account. Would you like to continue with this or start a new game?")

> [!NOTE]
> **Note:** Test cases 1-3 apply even if the user is not logged into your existing identity system (e.g. they are playing as a guest user). If a user is logged in with Google Play Games Services, then their progress should be automatically backed up and restored. The only exception is when the user explicitly understands that progress is explicitly tied to a single device. More details in our [requirement page here](https://developer.android.com/games/playgames/continuity-requirements).

## 1. Restore progress from a new mobile user to Google Play Games on PC

In this scenario, a new player initially opens your game, and then their progress
is automatically restored using their Play Games Services ID on both
mobile and Google Play Games on PC.

**Goal**: New players can seamlessly transfer their progress from mobile to PC.

| **Steps** | **Expected Result** |
|---|---|
| 1. Open the game on mobile. <br /> 2. Accumulate enough progress until the game cloud saves and progress is linked to the Player ID. <br /> <br /> 3. Redownload the game on a second mobile device, and choose the same Play Games Services profile from step 1 if the Play Games Services account selector pops up. <br /> 4. On your Google Play Games on PC client, log in with your profile from Step 1 and open the game. | 1. Play Games Services setup begins or the profile is automatically logged in (depending on if the player already has a Play Games Services profile configured, and if they enabled auto sign-in). <br /> 3. Progress from step 2 should be automatically restored. <br /> 4. Progress from step 2 should be automatically restored. |

## 2. Restore progress from an existing mobile user to Google Play Games on PC

In this scenario an existing player (i.e. a player who already has the game
downloaded to their device and will update to the new version with
Play Games Services v2
integrated) will automatically have their progress restored by their
Play Games Services ID on
both mobile and Google Play Games on PC.

**Goal**: Existing players can seamlessly transfer their progress on mobile to PC.

| **Steps** | **Expected Result** |
|---|---|
| 1. Download and open a prior version of the game on mobile which does not yet integrate Play Games Services v2. <br /> 2. Make some progress in the game. <br /> <br /> 3. Close the game, upgrade to the new version of the game on mobile with Play Games Services v2 integrated, open the game, and sign in or create a new account. Accumulate enough progress until the game cloud saves and progress is linked to the Player ID. <br /> 4. Delete the game on the mobile device. <br /> 5. Redownload the game on mobile, and choose the same profile from step 3. <br /> 6. On your Google Play Games on PC client, log in with your profile from Step 3 and open the game. | 3. Play Games Services setup begins OR profile is automatically logged in (depending on if the player already has a Play Games Services profile configured, and if they enabled auto sign-in). <br /> 5. Progress from step 4 should be automatically restored. <br /> 6. Progress from step 4 should be automatically restored. |

## 3. Restore progress from a Google Play Games on PC user to mobile

This is similar to the previous 2 cases, but instead the player starts on
Google Play Games on PC and moves to mobile. Your Android on PC build and
mobile builds should act the same as far as Google Play Games Services and cloud save
is concerned.

**Goal**: Players who initially download your game on Google Play Games on PC,
can seamlessly transfer their progress to mobile.

| **Steps** | **Expected Result** |
|---|---|
| 1. Open the game on Google Play Games on PC. <br /> 2. Accumulate enough progress until the game cloud saves and progress is linked to the Player ID. <br /> 3. On your mobile device, log in with your profile from Step 1 and open the game. | 3. Progress from step 2 should be automatically restored. |

## 4. Restore progress from a user that initially declines Google Play Games Services mobile sign-in

This step confirms that if the player initially declines creating/signing in with
their Play Games Services profile on mobile, they can still opt-in to
cloud save in the future.

**Goal**: Players who defer signing up for Play Games Services, can sign
up in the future and expect the same behavior as those who sign up at first
prompt.

| **Steps** | **Expected Result** |
|---|---|
| 1. Make sure there is no profile signed into the game in the Play Games Services settings. <br /> 2. Open the game on mobile (making sure not to login to any Play Games Services profile). <br /> 3. Make some progress in the game. <br /> 4. Close and reopen the game, on Play Games Services account selector pop up, select a Play Games Services profile on device. <br /> 5. Accumulate enough progress until the game cloud saves and progress is linked to the Player ID. <br /> 6. Delete the game on the mobile device. <br /> 7. Redownload the game on mobile, and choose the same profile from step 4. | 7. Account progress is restored. |

## 5. Link a new Google Play Games Services profile with an existing identity system

This case covers the requirement that player progress is tracked by a
Play Games Services ID, even
when logged into multiple identity systems. This also confirms that if your game
uses other identity solutions, the Play Games Services ID is linked to
these solutions so that players don't have to restore their credentials manually
when using a new device. For more information about this requirement, see
[continuity requirements](https://developer.android.com/games/playgames/continuity-requirements).

**Goal**: Players who are signed into a game's existing identity system can
seamlessly transfer their progress and account between mobile and
Google Play Games on PC, without the need to sign in on each platform.

| **Steps** | **Expected Result** |
|---|---|
| 1. Make sure there is no profile signed into the game in the Play Games Services settings. <br /> 2. Open the game on mobile (making sure not to login to any Play Games Services profile). <br /> 3. Make some progress in the game. <br /> 4. Link the current game progress to a non-Play Games Services account which is part of the existing identity system. <br /> 5. Close and reopen the game. <br /> 6. Log into Play Games Services at game re-open with a Play Games Services profile which hasn't been linked with any account in this game. <br /> 7. Accumulate enough progress until the game cloud saves and progress is linked to the the Player ID. <br /> 8. Delete the game on the mobile device. <br /> 9. Redownload the game on mobile, open the game and choose the same Play Games Services profile from step 6. | 9. Account progress is restored from step 7, and the identity system logged in at step 4 should be automatically logged into. |

## 6. Resolve account conflicts on mobile

We have the requirement that when there are conflicts on progress (a player
signs in with Play Games Services and another identity platform), you
should resolve it in a way
your players can expect and understand. This could be asking the player which
account they want to play with, preferring the local progress, or merging the
progress.
This happens when a player signs in with
Play Games Services, then logs into with another identity system which
is linked to another Play Games Services profile. Given that each
developer may choose to implement this in a unique way, we do not have
steps/expected behavior listed below, however we did want to call out the
requirement here when planning for your implementation. For more information
about this requirement, see
[continuity requirements](https://developer.android.com/games/playgames/continuity-requirements).

**Goal**: Players who start off with one Play Games Services profile, then
login with an in-game
account that is linked to another Play Games Services profile, can
expect to have their account
management resolved in a predictable way, where the player gives clear direction
on which account they would like to persist or link with their
Play Games Services account.