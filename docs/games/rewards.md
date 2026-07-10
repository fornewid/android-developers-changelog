---
title: https://developer.android.com/games/rewards
url: https://developer.android.com/games/rewards
source: md.txt
---

Play Games Rewards are in-game items that can be distributed to your players as
incentives and rewards to drive increased engagement from the Google Play Games
platform through experiences like [Quests](https://support.google.com/googleplay/answer/11534416) and Social Challenges.

There are two types of Play Games Rewards:

- **Single Use Rewards**: These are high-value, unique rewards that are
  restricted to a single-use quantity per player. These types of rewards will
  be used for single-use experiences like Quests.

  Examples:
  - Cosmetic items like skins, avatars or profile badges.
  - Exclusive items like characters or weapons.
- **Repeatable Rewards**: These are lower-value, repeatable rewards that
  are issued in a larger volume and players can redeem more than once.

  Examples:
  - In-game currency like coins, gems or event tokens.
  - Performance boosters like temporary XP boosts, multipliers.
  - Energy refills or consumable resources.

## Play Games Rewards requirements

> [!NOTE]
> **Note:** The Google Play Billing Library is used to process the Play Games Reward. However, developers are not required to use the Google Play Billing system for processing payments. Developers using alternative billing solutions will need to create SKUs in Play Console and integrate with PBL in order to grant Play Games Rewards.

The following are requirements for Play Games Rewards:

- Rewards need to be available for every player in the published regions for your game.
- Rewards need to be meaningful or desirable for players.
- Developers need to create or nominate SKUs in Play Console to be used as Play Games Rewards.
- Developers need to integrate with the [out of app purchase flow](https://developer.android.com/google/play/billing/integrate#process) using the Play Billing Library to give users in the game rewards that have been granted. Developers are responsible for ensuring the rewards are granted to the right in-game identity.

## Integrate Play Games Rewards

Add, manage, and deliver Play Games Rewards one-time product offers used by
Google Play as incentives to drive engagement for your game.

### Add a Play Game Reward (available from September 01, 2026)

Play Games Rewards (for both single use and repeatable rewards) are one-time
product offers that have been created with the purpose of being distributed by
Google Play. Once created, Google Play will use these offers as incentives and
rewards to drive increased engagement for your game.

To create a one-time product offer for Play Games Rewards, complete these
steps:

1. In the [Google Play Console](https://play.google.com/console/u/0/developers), select a game.
2. Navigate to **Monetize with Play** \> **Products** \> **One-time products**.
3. Select one or more available one-time products from the list that represents the entitlement you want to associate and create a new offer that represents the Play Games Rewards for your game.
   1. If you don't have any one-time products showing in this list, then you must first create some by navigating to **Monetise with Play** \> **Products** \> **One time products** and [follow these instructions](https://support.google.com/googleplay/android-developer/answer/16430488).

### Remove a Play Games Reward (available from September 01, 2026)

If you no longer want a SKU to be available to be used as a reward:

1. Go to **Monetise with Play** \> **Products \> One-time products**.
2. Select the specific SKU and associated "Play Game Reward" offer and make that offer inactive.

### Ensure a Play Games Reward is delivered in game (available from September 01, 2026)

Play will grant a player a Play Games Reward after they have successfully
completed an engagement mechanism, such as a Quest, for your game. At that point
your game needs to acknowledge the one-time product once the player has claimed
their Play Games Reward. This should be done using the
[out of app purchase flow](https://developer.android.com/google/play/billing/integrate#process) for both single use and repeatable rewards.

You can integrate with the out of app purchase flow in advance of September 1,
2026. However, you can only test the flow fully on or after September 1, 2026,
once Play Game Rewards have been created.

1. Ensure you have integrated with the [out of app purchase flow](https://developer.android.com/google/play/billing/integrate#process) in your game.
2. When your game starts, or is foregrounded, it should check if the player has any unacknowledged Play Games Rewards. For more information, follow instructions to call [`queryPurchasesAsync`](https://developer.android.com/google/play/billing/integrate#process). Games should check and grant rewards immediately.
3. Follow the rest of the [out of app purchase flow](https://developer.android.com/google/play/billing/integrate#process) instructions to [verify the purchase](https://developer.android.com/google/play/billing/integrate#verifying-purchase), [grant the entitlement to the user](https://developer.android.com/google/play/billing/integrate#granting-entitlement), [notify the user](https://developer.android.com/google/play/billing/integrate#notifying-user), and notify Google that the [purchase was processed](https://developer.android.com/google/play/billing/integrate#notifying-google).
4. Users have up to 3 days to open the game and claim the reward. After 3 days the reward will no longer be available.

**Important**: If you support multiple in-game identities, you must ensure that
your game also prompts the user to decide which in-game identity such reward
should be delivered to. Users will only be shown these rewards if their PGS ID
and Play Billing account match.

## Test Play Games Rewards

For more information on how to test the Play Games Rewards flow, see
[Google Play Billing Library Testing and troubleshooting guide](https://developer.android.com/google/play/billing/test).