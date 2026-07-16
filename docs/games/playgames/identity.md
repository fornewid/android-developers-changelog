---
title: https://developer.android.com/games/playgames/identity
url: https://developer.android.com/games/playgames/identity
source: md.txt
---

Google Play Games on PC aligns with Google Play Games Level Up's
[cloud save](https://developer.android.com/games/guidelines#cloud-save) guidance for cross-device play.

In addition, your cloud save solution must work across platforms. This way a
player can freely switch between PC, Android, and iOS without losing or
resetting progress.

We also recommend providing a seamless restore experience using
[Google Play Games Services (PGS) v2](https://developer.android.com/games/pgs/overview), leveraging the platform
identity provided by
[Play Games Services's platform authentication](https://developer.android.com/games/pgs/android/android-signin)
to identify a returning player across Play enabled devices. The
[Recall API](https://developer.android.com/games/pgs/recall) lets you associate an account with a **Player ID**
without restructuring your login system.

To learn more about implementing these requirements, see:

- [Google Play Games \| Level Up guidelines](https://developer.android.com/games/guidelines#cloud-save) for cloud save and player continuity requirements
- [Developer documentation](https://developer.android.com/games/pgs/overview) for integrating Play Games Services v2 within your game
- [Seamless restore documentation](https://developer.android.com/games/pgs/seamless-restore) for automatic sign-in and account linking