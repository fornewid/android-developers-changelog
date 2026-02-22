---
title: https://developer.android.com/games/playgames/identity
url: https://developer.android.com/games/playgames/identity
source: md.txt
---

With Google Play Games on PC, your users transition seamlessly between playing your game on their mobile device, and playing on their PC. If you also support other device types, such as Chromebooks or Android tablets, your user may be playing across even more surfaces. This topic introduces the continuity requirements for Google Play Games on PC.

Resetting game progress each time they play on a new device is a poor experience for your users; typically their intention is to continue playing your game, regardless of which surface they are on.
Additionally, having to login separately on each new surface creates a significant pain point which can lead users to abandon your game; users want to be immersed into the game experience as soon as possible with minimal roadblocks.

By implementing the [continuity requirements](https://developer.android.com/games/playgames/continuity-requirements) for Google Play Games on PC, powered by [Google Play Games Services Sign In](https://developer.android.com/games/pgs/android/android-signin), you give your users the best experience possible by assuring them that they can restore their credentials on a new Play surface and continue with their game - all without needing to enter a username or password, so that they can jump into the experience quickly and seamlessly as possible.

At a high level, there are 2 components that make up this requirement, so that we can ensure seamless continuity across surfaces for the user:

- **Saving game data and progress in the cloud** - Your game must be able to restore the user's game state between their mobile device and PC, at a minimum. This optionally spans across any surface your game supports.
- **Providing a zero-touch login experience across surfaces** - Leverage [Google Play Games Services (PGS) v2](https://developer.android.com/games/pgs/overview) to create a zero-touch experience, using the user's Google Account to bring their game credentials from their mobile device to PC. With our new Google Play Games Services v2 SDK, which is a requirement for Google Play Games on PC, integration is easier than before and users have a seamless experience when signing in with your game.

These topics describe how to implement the requirements:

- [Detailed guidance for fulfilling our continuity requirements](https://developer.android.com/games/playgames/continuity-requirements) for Google Play Games on PC users
- [Test cases](https://developer.android.com/games/playgames/continuity-expected-behaviors) you can use to evaluate your own integration against our requirements
- [Our recommendations](https://developer.android.com/games/playgames/integrating-pgs-existing-id-solutions) for integrating Play Games Services with your own existing identity system.
- [Developer documentation](https://developer.android.com/games/pgs/overview) for integrating Play Games Services v2 within your game