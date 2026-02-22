---
title: https://developer.android.com/games/pgs/overview
url: https://developer.android.com/games/pgs/overview
source: md.txt
---

[Video](https://www.youtube.com/watch?v=v-6b_wWF96U)

### Google Play Games Services overview


The Google Play Games platform is a unified gaming ecosystem
encompassing Android, ChromeOS, and [Windows
PC](https://developer.android.com/games/playgames/overview). Developers use the Google Play Games platform to integrate
Play Games Services social features into their gaming applications.
Play Games Services is the primary interface between the game
application and the Play Games platform. Play Games Services also
provides a centralized [Gamer Profile](https://play.google.com/games/profile)
account that provides consistent player identification across different devices
and form factors.
[Get Started](https://developer.android.com/games/pgs/start)

## Key capabilities of the Play Games platform

Integrating Play Games Services unlocks platform capabilities that improve user
retention and cross-platform continuity.

- **Cross-device continuity:** Consistent Gamer Profiles across phones, tablets, and PCs, which lets players resume gameplay seamlessly.
- **Social and Engagement Features:**
  - **Achievements and leaderboards:** Recognize accomplishments and foster competition outside the game.
  - **Play Points:** Drives monetization by allowing players to earn and redeem points for in-game purchases.
  - **Social Graph:** Allows players to follow their friends, their activities and build a social gaming community of their own.
- **Play Games Sidekick (Beta):** Provides an overlay with utilities, real-time Gemini tips, and engagement tools.

## Game benefits and program advantages

The Google Play Games platform provides an extensive array of compelling and
rewarding and engaging mechanics, including leagues, quests, achievements,
and streaks. These impactful capabilities are restricted to titles enrolled in
the [LevelUp program](https://developer.android.com/games/pgs/%5Bhttps:/play.google.com/console/about/levelup), a cornerstone of the Google Play Games ecosystem.

Developers can obtain instant access to these powerful tools by integrating
their games with Play Games Services. As the primary method for platform
authentication, Play Games Services serves as the link to the full range of
rewarding features, provided that program guidelines are followed.

These mechanics are proven to drive significant improvements in acquisition,
retention, engagement, and monetization.

By using the vast Android player
base and participating in the LevelUp program, titles gain increased
discoverability and visibility across multiple Play Games surfaces through these
diverse engagement systems.

## What is the difference between platform identity and game identity?

Because Play Games Services has implemented version 2, you must distinguish
between the **platform identity** and the proprietary **in-game Account (IGA)**
architecture.

- **Play Games Platform Identity (Managed by Play Games Services):**
  This is the player's universal gaming persona on Android. It tracks Play
  Social Progress, such as Player XP, Levels, Streaks, and
  Achievements. Because it is built into the device, it automatically
  recognizes the player when the game starts.

- **In-game account identity (Managed by the Developer):** It is important to
  note that Play Games Services does **not** serve as a primary system for
  inventory management or game-state preservation. Developers are expected to
  utilize independent "In-Game Identity" solutions---such as Sign in with Google,
  Facebook, or custom backend---to manage game progress data.

**Importance of Play Games Services to the Platform:** Play Games Services v2
operates as a platform connector. It maintains persistent authentication with
the Play Games platform regardless of the specific login method used by the
player. Consequently, this architecture enables the platform to aggregate
gameplay statistics and distribute achievements without disrupting the
developer's internal logic for saving and restoring game progress.

**Impact on Games:** Play Games Services v2 SDK is a high-level integration
layer for games. Developers don't need to modify existing login flows or systems
to implement it.