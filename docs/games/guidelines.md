---
title: https://developer.android.com/games/guidelines
url: https://developer.android.com/games/guidelines
source: md.txt
---

Google Play Games Level Up is a program to recognize and reward great gaming experiences,
providing you with powerful tools and promotional opportunities to drive
business growth for your game.

Our mission is to connect players with the best gaming experiences---ones that
offer player continuity, rewarding player journeys, and cross device gameplay.
Level Up is open to most games and includes access to program
benefits.
Games can remain in the program and maximize [benefits](https://play.google.com/console/about/levelup)
by meeting the user experience guidelines by each program milestone.

Player expectations and developer needs are always evolving, and the program is
designed to evolve with them. User experience guidelines and benefits may be
updated over time.

This page describes the user experience guidelines. To know more about the
program and benefits, visit the [Google Play Games \| Level Up](https://play.google.com/console/about/levelup/) program page.

## User experience guidelines

To gain access to the benefits offered by the Level Up program, your game needs
to adhere to all the *required* user experience guidelines defined in the
program by the [timelines](https://developer.android.com/games/guidelines#timelines) and milestones.

Adhering to *recommended* user experience guidelines is not mandatory to
access the program benefits, but these guidelines might evolve into required
guidelines in the future.

The following sections outline the user experience guidelines with three main
themes:

- [Rewarding player journeys](https://developer.android.com/games/guidelines#rewarding-player-journeys)
- [Player continuity](https://developer.android.com/games/guidelines#gameplay-continuity)
- [Cross device gameplay](https://developer.android.com/games/guidelines#cross-device-gameplay)

## Rewarding player journeys

Players love seeing the time and effort they invest in games to be recognized
and rewarded. By designing achievements that span the lifetime of the
game---celebrating everything from leveling up and story progression to
discovering hidden surprises or even acknowledging failed attempts,you can make
a player's entire experience feel more engaging and valuable. By implementing
high-quality achievements, you'll become eligible for Play Points promotions
like [Quests](https://support.google.com/googleplay/answer/11534416) that reward players for completing achievements and increase
retention for your game.

Refer to: [Achievements](https://developer.android.com/games/pgs/achievements)

### Achievements

#### Required

- A minimum of ten achievements spread across the lifetime of the game.
- All achievements should have unique names and descriptions. These should make clear to users what they need to do to get the achievement.
- Only new achievements should have unique icons.
- Required for Quests eligibility only:
  - At least four achievements are reasonably and reliably achievable within an hour of gameplay by everyone who plays. You can create a maximum of 400 achievements across the lifetime of the game.

#### Recommended

- Use [incremental
  achievements](https://developer.android.com/games/pgs/achievements#incremental-achievements) to show progress.
- At least forty or more achievements spread across the lifetime of the game including ones that surprise and delight, recognise milestones, and capture player progress.
- Use [hidden achievements](https://developer.android.com/games/pgs/achievements#state) for element of surprise and delight.
- Add new achievements when new levels or episodes are added to the game.

## Player continuity

Players want to switch devices and continue their game without missing a beat.
Cloud save and seamless restore makes this possible, seamlessly syncing progress
and rewards to their gamer profile so they can pick up right where they left
off.

We're making this experience even better with Play Games Sidekick. The new
in-game overlay gives players instant access to their rewards, offers, and
achievements, driving higher engagement for your game. With AI-driven tips and
advice, Sidekick helps players stay immersed in the games they love.

Refer to:

[Play Games Sidekick (beta)](https://developer.android.com/games/pgs/play-games-sidekick)

[Cloud save](https://developer.android.com/games/pgs/savedgames)

[Seamless restore](https://developer.android.com/games/pgs/account-linking)

### Cloud save and seamless restore

#### Required

- Implement cloud save to backup and retrieve the latest state of the player's game on the cloud. See [Cloud save](https://developer.android.com/games/pgs/savedgames).

#### Recommended

- Link Play Games Services account, with third-party or in-game identity solutions. See [Seamless restore](https://developer.android.com/games/pgs/account-linking).

### Play Games Sidekick

#### Required

- Access the Play Games Sidekick while playing your game. See [Play Games Sidekick (beta)](https://developer.android.com/games/pgs/play-games-sidekick).
- From December 2025, you can enable this experience for internal testing by using a toggle in Play Console with a streamlined testing process.

> [!WARNING]
> **Beta:** The Play Games Sidekick feature is now available to early access partners, as we work to enhance its performance and stability.

## Cross device gameplay

Players want the flexibility to enjoy their favourite games across their
devices. We have seen games optimized for multiple device types---from mobile to
tablet to PC---drive higher player engagement and spend. To make these games even
easier for players to find, we are launching new in-store discovery features
to showcase titles with great cross device and input support. Google Play
Games on PC makes it easier to bring your mobile game to a new audience on PC
with streamlined distribution using Play Console.

You can give your players the flexibility to play how they want by adding
keyboard and mouse support, as well as controller support---which also unlocks
better gaming with attachable mobile controllers and Android XR.

Refer to:

[Keyboard](https://developer.android.com/games/playgames/input)

[Mouse](https://developer.android.com/games/playgames/input-mouse)

[Controller support](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers)

[Google Play Games on PC](https://developer.android.com/games/playgames/overview)

### Controller, mouse, and keyboard support

#### Recommended

- You can play your favorite games with a controller, keyboard, and mouse on your preferred device.
  - The game should be fully playable with a controller, keyboard, and mouse across all devices the game supports through Play. Fully playable implies that the game can be played from the start, inclusive of gameplay and settings menus, without the need for touch. For best practices, you can refer to the following: [keyboard](https://developer.android.com/games/playgames/input), [mouse](https://developer.android.com/games/playgames/input-mouse), and [controller support](https://developer.android.com/develop/ui/views/touch-and-input/game-controllers).

### Play on PC

#### Recommended

- Support multi-platform either with PC native or through emulation of the mobile version on PC. See [Google Play Games on PC](https://developer.android.com/games/playgames/overview).

## Timelines

The Level Up program started in September 2025.
For more details, visit the [Google Play Games \| Level Up](https://play.google.com/console/about/levelup/) program page.

The key dates dates are as follows:

|---|---|
| **Deadline** | **Milestone** |
| **July 31, 2026** | Games released before July 31, 2026 will be automatically enrolled in the program and can enjoy the program [benefits](https://play.google.com/console/about/levelup) upon release. After July 31, 2026, games will have to meet the required user experience guidelines for the following features: - **[Achievements](https://developer.android.com/games/guidelines#achievements)** You must have integrated your game to use [Play Games Services](https://developer.android.com/games/pgs/overview) v2 SDK. - **[Play Games Sidekick](https://developer.android.com/games/guidelines#play-games-sidekick)** From early 2026, you can enable this experience for internal testing by using a toggle in Play Console with a streamlined testing process. > [!WARNING] > **Beta:** The Play Games Sidekick feature is now available to early access partners, as we work to enhance its performance and stability. |
| **November 30, 2026** | After November 30, 2026, games will have to meet the required user experience guidelines for the following features: - **[Cloud save](https://developer.android.com/games/guidelines#cloud-save)** |

## Frequently asked questions

#### Where can I find the benefits of the program?

The benefits are described in the [Google Play Games \| Level Up](https://play.google.com/console/about/levelup/) program page.

#### Where can I find the timelines to comply with the user experience guidelines?

The timelines are available in the [Google Play Games \| Level Up](https://play.google.com/console/about/levelup/) program page and also
the [timelines](https://developer.android.com/games/guidelines#timelines) section.

#### What is the difference between
a **required** and a **recommended** guideline?

**Required guidelines:**

- **Established Timelines:** Deadlines will be defined.
- **Validation:** Compliance with guidelines will be subject to validation methods such as self-certification, manual validation, automated validation, or structured reviews.
- **Benefit Eligibility:** Eligibility for Level Up benefits will be determined by being compliant with the guideline.
- **Editorial Contribution:** Compliance with guidelines will contribute to editorial decision-making.

**Recommended guidelines:**

- **Timelines:** Deadlines are not defined.
- **Benefit Eligibility:** Non-compliance with guidelines won't impact eligibility for Level Up benefits.
- **Editorial Contribution:** These guidelines will contribute to editorial decision-making.
- **Level Up direction:** These guidelines will serve as a mechanism to communicate the long-term strategic direction of Level Up. The intent is for recommended guidelines to potentially evolve into required guidelines in the future.