---
title: https://developer.android.com/games/pgs/friends
url: https://developer.android.com/games/pgs/friends
source: md.txt
---

Use the Friends APIs to complement and enhance your existing in-game friends system
and other social systems your game may access. This lets you enable players to:

- Find their friends in your game.

- Compare scores with their friends on leaderboards.

- Combine the list of their Play Games friends with existing in-game lists of
  friends.

- Identify another player with an in-game profile popup. This popup shows a
  nickname that the current player has given to their friend, so they know who
  they are playing with.

![Import friends](https://developer.android.com/static/images/games/pgs/friends-import.gif)

## Basics

These APIs allow you to perform the following actions:

- **Load friends**: You can check if the player has allowed the game to access Friends list information. If access is granted, you can get a list of Player objects corresponding to the friends of the authenticated player.
- **Launch a view of another player's Play Games profile**: You can open up this view to show the name given to the other player by the authenticated player. This view also offers friendship management controls and won't take the player out of your game.
- **Provide user controls**: The user has controls to manage how their Play Games profile is visible to friends and how their friends list is visible to games. For friends list access, the user can choose to automatically grant access for all games or they can choose to individually approve access for each game. Consequently, when loading the friends list, the result may be a callback to display a request for access.

## Import a Play Games friends list

You can use the Friends APIs to get a list of your players' Play Games
friends and add them to your in-game friends list.

New users will have a starting list of friends to play with, and existing users
can import their Play Games friends into any in-game lists of friends.
As a result, your users will have the largest possible set of players to play
with or compete against.

> [!NOTE]
> **Note:** If you store any relationships from Play Games, you must regularly check the friends list to ensure that the relationships, and consent to use them, are still valid.

### Add Play Games friends to your game

Add Play Games friends to any existing in-game friends list by
associating their Play Games ID with corresponding player information in
your internal database. Make sure you have a button with the Play Games
icon next to these friends, which shows the other player's profile when pressed,
so your users can know who the friends are.

When using the friends list from a backend server,
[load it securely](https://developer.android.com/games/pgs/signin#secure-access)
using the REST API rather than passing the result of the Android API. Make sure
to use the player ID returned by
[`players.get(me)`](https://developer.android.com/games/services/web/api/rest/v1/players/get)
in the REST API for the currently authenticated player, as this will be consistent
with the ID seen by other players.

If the augmented friends list is not stored (but just used at the time of
viewing), then no additional work is needed.

### Grant Play Games access

If your game doesn't already have Play Games access, a good time to
prompt users for their consent is when they view your in-game friends list. For
example, you might add a button called **Import Play Games friends**, which
prompts the user for consent when tapped. (Make sure to use the
Play Games logo on any button that mentions the service.)

## View another player's profile

You can allow your authenticated player to view another player's
Play Games profile. This allows the authenticated player to see the name they
have given the other player and whether or not they are already friends, giving
them added context about the relationship. If the players are not yet friends,
the authenticated player will see friendship management controls on the profile
view. When friendships are created from within the game, the default names for
the two players are their in-game names (if provided). The name of the
game where the friendship was initiated is also shown.

![View another player's profile](https://developer.android.com/static/images/games/pgs/friends-show-profile.png)

## Social leaderboards

The Friends APIs can also be used for leaderboards. Use this feature to show the
ranking of the current player among their Play Games friends. Note that
this only applies to users who have chosen to share this information with your
application, and if the users are friends in Play Games. To support this
feature, the game exposes a control to the user. This control uses the
`collection` argument to select the social view of the leaderboard. To learn
more, see the section on
[public and social leaderboards](https://developer.android.com/games/pgs/leaderboards#public_and_social_leaderboards).

If you implement the social leaderboards collection, the call to load the
leaderboard scores may return a consent-required resolution exception similar to
that from
[`loadFriends()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient#loadFriends(int,%20boolean)).
If you implement the default Play Games-provided UI (for example,
[`getLeaderboardIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient.html#getLeaderboardIntent(java.lang.String))),
then this is handled for you automatically.

## Next steps

Before you start to use the Friends APIs, do the following:

- Download and review a code sample:
  - [Java](https://github.com/playgameservices/android-basic-samples)
  - [Unity sample app](https://github.com/playgameservices/play-games-plugin-for-unity/tree/master/Samples/SmokeTest) using the [Unity plugin](https://github.com/playgameservices/play-games-plugin-for-unity)
- Familiarize yourself with the recommendations described in the [Quality Checklist](https://developer.android.com/games/pgs/quality#friends).
- Implement the [Friends APIs in a Java client](https://developer.android.com/games/pgs/android/friends).