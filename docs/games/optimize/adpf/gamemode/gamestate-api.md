---
title: Game State API  |  Android game development  |  Android Developers
url: https://developer.android.com/games/optimize/adpf/gamemode/gamestate-api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Game State API Stay organized with collections Save and categorize content based on your preferences.



**Released**:

Android 13 (API Level 33) - [Java](/reference/android/app/GameState)

With Game State API, you can let the system know what the game is currently
doing (for example: loading levels, intense networked gameplay, rendering
in-game menu, showing ads, etc). With this valuable information, the system is
be able to optimize resources and power accordingly.

### Java

```
if ( Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ) {
  // Get GameManager from SystemService
  GameManager gameManager =
  Context.getSystemService(GameManager.class);
  GameState gameState = new GameState(false,
  GameState.MODE_GAMEPLAY_UNINTERRUPTIBLE);
  gameManager.setGameState(gameState);
}
```

Check out the modes you can notify the system in the documentation
[Summary](/reference/android/app/GameState#summary).
It is possible that the list will grow when different resource consumption
patterns is discovered in the future.




Send feedback