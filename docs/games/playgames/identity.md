---
title: About continuity and cross-device play  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/identity
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# About continuity and cross-device play Stay organized with collections Save and categorize content based on your preferences.





Google Play Games on PC aligns with Google Play Games Level Up's
[cloud save](/games/guidelines#cloud-save) guidance for cross-device play.

In addition, your cloud save solution must work across platforms. This way a
player can freely switch between PC, Android, and iOS without losing or
resetting progress.

We also recommend providing a seamless restore experience using
[Google Play Games Services (PGS) v2](/games/pgs/overview), leveraging the platform
identity provided by
[Play Games Services's platform authentication](/games/pgs/android/android-signin)
to identify a returning player across Play enabled devices. The
[Recall API](/games/pgs/recall) lets you associate an account with a **Player ID**
without restructuring your login system.

To learn more about implementing these requirements, see:

* [Google Play Games | Level Up guidelines](/games/guidelines#cloud-save) for cloud save and
  player continuity requirements
* [Developer documentation](/games/pgs/overview) for integrating
  Play Games Services v2 within your game
* [Seamless restore documentation](/games/pgs/seamless-restore) for automatic sign-in
  and account linking






Send feedback