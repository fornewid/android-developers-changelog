---
title: https://developer.android.com/games/playgames/continuity-requirements
url: https://developer.android.com/games/playgames/continuity-requirements
source: md.txt
---

To provide the best experience to players for Google Play Games on PC,
[your Google Play Games on PC and mobile (Android) versions of your game
must](https://developer.android.com/games/playgames/identity) provide a seamless cross-device experience
using the [Google Play Games Services v2](https://developer.android.com/games/pgs/overview) SDK to be
considered [optimized for
Google Play Games on PC](https://developer.android.com/games/playgames/checklist#optimized-requirements).

Here's a summary of the requirements:

- Players on mobile (Android) and Google Play Games on PC (on PC) are [automatically signed in to Google Play Games Services](https://developer.android.com/games/pgs/signin) within your game when possible, and their non-tutorial progress is linked to their Google Play Games Services Player ID. On other devices, the game automatically restores this progress when there are no conflicts with the local state.
  - Users might be automatically signed in to your game with Google Play Games Services, but not sign in with your existing identity system (for example, guest accounts). In these cases, given the user is signed in with Google Play Games Services and has the expectation that their progress is being saved, you still must back up and restore the user's progress. **The only exception is when the user specifically
    understands that the guest mode is tied to a single device.**
  - [Google Play Games Services v2 Sign-in](https://developer.android.com/games/pgs/signin) must be used to satisfy this requirement. If you are using v1 Sign-in, we have guidance for migrating [Java](https://developer.android.com/games/pgs/android/migrate-to-v2) and [Unity](https://developer.android.com/games/pgs/unity/unity-start) integrations.
- If your game has other identity solutions, link the Google Play Games Services Player ID to these solutions so that players don't have to restore their credentials manually when using a new device.
- When there are conflicts on progress (a player signs in with Google Play Games Services and another identity platform), you should resolve it in a way your players can expect and understand. This could be asking the player which account they want to play with, preferring the local progress, or merging the progress.

We acknowledge that your existing identity solutions have their own
complexities, and we are flexible on edge cases that arise from identity
collisions and resolution. In the end, the requirement is that players will
automatically have their progress or state restored when switching between
Android (including phones and tablets) and Google Play Games on PC.

See [these recommendations](https://developer.android.com/games/playgames/integrating-pgs-existing-id-solutions) on how to integrate Google Play Games Services
with your existing identity system. You can choose between two primary
integration methods based on your game's needs.

- **Binding solution:** Create a one-to-one connection between Google Play Games Services and your existing identity system.
- **Recall solution:** Associate a Google Play Games Services account with multiple user-associated accounts to restore state.

Each method offers different benefits for managing player progress across
devices.

You can use the [test cases](https://developer.android.com/games/playgames/continuity-expected-behaviors) to evaluate your own solution
against the requirements.

> [!NOTE]
> **Note:** We strongly recommend enabling [next generation IDs](https://developer.android.com/games/pgs/next-gen-player-ids) as you configure your PGS project. This will [become the default for all PGS
> projects](https://android-developers.googleblog.com/2023/02/enable-next-generation-ids-for-better-play-games-services-support-for-all-google-accounts.html), and enables better support for all accounts, including [those
> under supervision](https://support.google.com/families/answer/9499456).

Here's a checklist of our required and encouraged behaviors related to
Google Play Games Services sign-in on Google Play Games on PC.

| **ID** | **Importance** | **Description** |
|---|---|---|
| 1.1 | Required for [optimized](https://developer.android.com/games/playgames/checklist#optimized-requirements) builds | Sign players in with [Google Play Games Services v2](https://developer.android.com/games/pgs/signin) on Android devices and Google Play Games on PC. <br /> Integrate the new [Google Play Games Services v2 SDK](https://developer.android.com/games/pgs/overview) with your Android and Google Play Games on PC builds, and enable the [Sign-in functionality](https://developer.android.com/games/pgs/signin) within your game. Use the credentials from signed in players to power requirement 1.2. <br /> Note that v1 Sign-in does not meet the requirement. If you use Google Play Games Services v1 in your game, you need to upgrade to [v2](https://developer.android.com/games/pgs/signin). For more information about migrating your game, see the [Java](https://developer.android.com/games/pgs/android/migrate-to-v2) and [Unity](https://developer.android.com/games/pgs/unity/unity-start) guides. |
| 1.2 | Required for [optimized](https://developer.android.com/games/playgames/checklist#optimized-requirements) builds | Back up and restore player progress by the Play Games Services Player ID. <br /> This is not required when the player understands that the progress is tied to the local device and would be lost when going to another device or the progress is only within the tutorial. <br /> To ensure players don't lose their progress when switching or resetting devices, or if they play on multiple devices, ensure their progress is backed up to a cloud save solution, and use the Play Games Services Player ID as a key, [securely](https://developer.android.com/games/pgs/signin#secure-access) if using your own backend game server. When players sign in with Play Games Services, check whether progress exists for that account and if it does, allow the player to pick up where they left off. You can use your own cloud save solution or Play Games Services [Saved Games](https://developer.android.com/games/pgs/savedgames) <br /> If the player is not signed in with Play Games Services, try to maintain the player's progress locally, then sync that progress when the player eventually signs in to Play Games Services. This helps to prevent losing any of the player's progress if the player postpones signing in to your game. |
| 1.3 | Best Practice | Provide a sign-in button for signed-out players. <br /> Players might opt out of using Play Games Services and therefore not automatically sign in to your game. By adding a sign-in button for signed-out players, you allow players to change their mind and sign in to Play Games Services as they get more invested in your game. <br /> The sign-in button should be findable by players; for example, it should be accessible from your main screen or located in the Settings screen. This button shouldn't be buried multiple levels deep in your game menu. |
| 1.4 | Good-to-have | Follow Google branding guidelines. <br /> To provide players with an end-to-end experience that is attractive and consistent, implement the [Play Games Services branding guidelines](https://developer.android.com/games/pgs/branding). |