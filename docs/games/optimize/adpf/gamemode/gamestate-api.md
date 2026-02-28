---
title: https://developer.android.com/games/optimize/adpf/gamemode/gamestate-api
url: https://developer.android.com/games/optimize/adpf/gamemode/gamestate-api
source: md.txt
---

**Released**:

Android 13 (API Level 33) - [Java](https://developer.android.com/reference/android/app/GameState)

With Game State API, you can let the system know what the game is currently
doing (for example: loading levels, intense networked gameplay, rendering
in-game menu, showing ads, etc). With this valuable information, the system is
be able to optimize resources and power accordingly.

### Java

    if ( Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ) {
      // Get GameManager from SystemService
      GameManager gameManager =
      Context.getSystemService(GameManager.class);
      GameState gameState = new GameState(false,
      GameState.MODE_GAMEPLAY_UNINTERRUPTIBLE);
      gameManager.setGameState(gameState);
    }

Check out the modes you can notify the system in the documentation
[Summary](https://developer.android.com/reference/android/app/GameState#summary).
It is possible that the list will grow when different resource consumption
patterns is discovered in the future.