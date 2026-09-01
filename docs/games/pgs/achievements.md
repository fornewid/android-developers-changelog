---
title: https://developer.android.com/games/pgs/achievements
url: https://developer.android.com/games/pgs/achievements
source: md.txt
---

Achievements offer engagement by rewarding players for reaching specific
milestones or completing challenges in the game. They appeal to a broader
audience, including players who might not be as interested in competitive
leaderboards but enjoy personal progression.

High-quality achievements make your game more engaging and increase discovery
across Google Play, encouraging users to start playing. They also make your
game eligible for [quests](https://support.google.com/googleplay/answer/11534416), which reward users for reaching milestones.

To meet the Google Play Games Level Up [user experience guidelines](https://developer.android.com/games/guidelines), your
game needs be compliant with the [baseline](https://developer.android.com/games/pgs/achievements#design-achievements) level of
achievements.

To bring achievements to your game:

1. Decide which achievements to award, their names, and their associated icons. Refer to the [quality checklist](https://developer.android.com/games/pgs/quality).
2. Configure your achievements in Play Console either by adding achievements individually or by using the bulk upload option. Refer to [add achievements](https://developer.android.com/games/pgs/integrate-achievements#add-achievements).
3. Integrate in your game by calling Play Games Services APIs when a user has advanced or completed an achievement using the provided IDs from your [client implementations](https://developer.android.com/games/pgs/integrate-achievements#client-implementations).
4. Verify that achievements work as planned. Refer to [testing achievements](https://developer.android.com/games/pgs/integrate-achievements#test-achievements).
5. Publish your achievements and game. Refer to [publish achievements](https://developer.android.com/games/pgs/integrate-achievements#publish-achievements).

## Design high quality achievements

#### Required and recommended achievements

**Baseline**

- A minimum of ten achievements spread across the lifetime of the game.
- All achievements should have unique names and descriptions. These should make clear to users what they need to do to get the achievement.
- New achievements should have unique icons.
- Required for Quests eligibility only:
  - At least four achievements are reasonably and reliably achievable within an hour of gameplay by everyone who plays. You can create a maximum of 400 achievements across the lifetime of the game.

**Recommended**

- Use [incremental
  achievements](https://developer.android.com/games/pgs/achievements#incremental-achievements) to show progress.
- At least forty or more achievements spread across the lifetime of the game including ones that surprise and delight, recognise milestones, and capture player progress.
- Use [hidden achievements](https://developer.android.com/games/pgs/achievements#incremental-achievements) for an element of surprise and delight.
- Add new achievements when new levels or episodes are added to the game.

#### Quality checklist

For designing high quality achievements to enhance the user experience, make
sure you follow the [quality checklist](https://developer.android.com/games/pgs/quality).

## Achievements basics

When viewing achievements in the Google Play Console, you can find the
following types, elements, and states:

##### Type of achievements

There are three types of achievements:

1. **Standard achievement** is a basic achievement that is unlocked in a single step. Create achievements with diverse goals such as reaching specific levels within the game, leveling up characters or bases, match wins, or even failed attempts. Also, add new achievements when new levels or episodes are added to the game.
2. **Incremental achievement** involves a player making gradual progress towards earning the achievement over a longer period of time. Hence they are a powerful tool for the developers to guide player behavior and reward sustained engagement. The developers should maximize the opportunities to create incremental achievements over standard achievements for a game.

   Refer to the following guidelines while designing incremental
   achievements:
   - Reward core gameplay loop engagement - Use incremental achievements to reward players for repeatedly engaging with the game's central, most common actions. *Make the player's engagement feel recognized and meaningful*.
   - Make sure that progress is measurable and made visible - The magic of an incremental achievement lies in the progress bar. Measure the progress and report to Play games services.
   - Use tiers to create milestones - A goal of 10,000 can feel very far away. Break it into tiered achievements to provide multiple moments of satisfaction. For example,

     - Tier 1: "Monster Slayer" - Defeat 1,000 enemies
     - Tier 2: "Creature Crusher" - Defeat 5,000 enemies
     - Tier 3: "War Machine" - Defeat 10,000 enemies
   - The goal should be a marathon, not a sprint - The target number should be high enough that it requires at least ten sessions to achieve.
3. **Hidden achievement** hides its details from the player. Use hidden achievements for surprise and delight, but use them sparsely. Play Games Services provides a generic placeholder description and icon for the achievement. Make an achievement hidden if it contains a spoiler you don't want to reveal about your game (for example, "Discover that you were a ghost all along!").

##### Basic elements of achievements

These basic elements are associated with every achievement:

- **Id** is a unique string that is generated by Google Play Console. You'll use this unique ID to refer to the achievement in your game clients.
- **Name** is a short name of the achievement (for example, "Pieman"). The value can be up to 100 characters.
- **Description** is a concise description about your achievement. Usually this tells your player how to earn the achievement (for example, "Bake a lemon meringue pie before sundown"). The value can be up to 500 characters.
- **Icon** is a square icon that is associated with your achievement. For best practices when creating your achievement icons, see the [Icon guidelines](https://developer.android.com/games/pgs/integrate-achievements#expandable-2) section.
- **List order** is the order in which the locked achievements appear when a player views the achievements associated with your game. This can be in any order that you like. Unlocked achievements appear at the top of the list in the order achieved.

##### State of achievements

Achievements can be in one of three different states:

- A **hidden** achievement means that details about the achievement are hidden from the player. Play Games Services provides a generic placeholder description and icon for the achievement while it's in a hidden state. We recommend making an achievement hidden if it contains a spoiler you don't want to reveal about your game too early (for example, "Discover that you were a ghost all along!").
- A **revealed** achievement means that the player knows about the achievement, but hasn't earned it yet. Most achievements start in the revealed state.
- An **unlocked** achievement means that the player has successfully earned the achievement. An achievement can be unlocked offline. When the game comes online, it syncs with Play Games Services to update the achievement's unlocked state.

## Points and experience points

Achievements in Play Games Services enabled games have a point value that
contributes to a player's experience Points (XP). These points are used to
calculate XP for each achievement.

The formula for calculating XP is as follows:

    XP for an achievement = 100 * (point value for the achievement)

As players earn achievements, Play Games Services tracks their accumulated XP.
When a player earns enough points to level up, Play Games Services sends
a notification to the Google Play Games app. Players can view their current
level and XP history directly from their **Profile** page within the
Google Play Games app.

Follow these guidelines when assigning point values to achievements:

- A game can have a maximum total of 2,000 points across all its achievements.
- Point values must be a multiple of 5.
- No single achievement can have more than 200 points.
- Assign point values based on the complexity and rarity of the achievement.
- Always reserve some balance from your total 2000-point allowance. This lets you to add new achievements for future game levels or updates.