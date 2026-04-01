---
title: https://developer.android.com/games/pgs/unity/friends
url: https://developer.android.com/games/pgs/unity/friends
source: md.txt
---

Play Games Friends allows players to create and maintain a cross-games friends
list. You can request access to this friends list to help your players play your
game with their friends. See the
[Friends concept page](https://developers.google.com/games/services/common/concepts/friends)
for more details on the friends system.

## Before you start

- Set up your project and the Google Play Games plugin for Unity. For details, see
  the [Get started guide](https://developer.android.com/games/pgs/unity/unity-start).

- See the [best practices guidelines](https://developer.android.com/games/pgs/quality#friends) for
  instructions on the best way to implement these APIs.

See the
[best practices guidelines](https://developer.android.com/games/pgs/quality#friends) for instructions on the
best way to implement these APIs.

## Enable friends

To enable friends, use the following functions:

- [View friends](https://github.com/playgameservices/play-games-plugin-for-unity#view-friends):
  Request access to a player's friends list, so you can add their play games
  friends to your in-game friends list.

- [View a player profile](https://github.com/playgameservices/play-games-plugin-for-unity#view-a-player-profile):
  Let a player view the Play Games profile of another player. This is
  essential so a player knows who their friends are, and can connect to other
  Play Games players in your game. This will need to be tied to a UI element to
  trigger the popup. See the
  [friends guidelines](https://developers.google.com/games/services/checklist#friends)
  for details.

## View friends

There are two ways to load friends, either using the `ISocial` framework or
directly with [PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform).

### Load friends with the ISocial framework

    Social.localUser.LoadFriends((success) =>  {
        Debug.Log("Friends loaded OK: " + ok));
        foreach(IUserProfile p in Social.localUser.friends) {
             Debug.Log(p.userName + " is a friend");
        }

However, this call will fail if the current player has not yet granted
permission to the game to access this information. Use
`GetLastLoadFriendsStatus` to check if `LoadFriends` failed due to missing
consent.

     PlayGamesPlatform.Instance.GetLastLoadFriendsStatus((status) => {
        // Check for consent
        if (status == LoadFriendsStatus.ResolutionRequired) {
            // Ask for resolution.
        }
    });

A game can ask the current player to share the friends list by calling
`AskForLoadFriendsResolution`.

    PlayGamesPlatform.Instance.AskForLoadFriendsResolution((result) => {
        if (result == UIStatus.Valid) {
            // User agreed to share friends with the game. Reload friends.
        } else {
            // User doesn't agree to share the friends list.
        }
    });

This function will show the appropriate platform-specific friends sharing UI.
This UI asks the player if they want to share their friends with the game.

### Load friends with PlayGamesPlatform

Another way of loading friends is to use `LoadFriends` and `LoadMoreFriends`:

    PlayGamesPlatform.Instance.LoadFriends(pageSize, forceReload, (status) => {
        // Check if the call is successful and if there are more friends to load.
    });

    PlayGamesPlatform.Instance.LoadMoreFriends(pageSize, (status) => {
        // Check if there are more friends to load.
    });

The `pageSize` param represents the number of entries to request for this page.
Note that if cached data already exists, the returned buffer may contain more
than this size. The buffer is guaranteed to contain at least this many entries
if the collection contains enough records. If `forceReload` is set to `true`,
this call will clear any locally-cached data and attempt to fetch the latest
data from the server. This would commonly be used for actions like a user-
initiated refresh. Normally, this should be set to `false` to gain the
advantages of data caching.

If the callback returns `LoadFriendsStatus.LoadMore`, then there are more
friends to load. `LoadFriendsStatus.ResolutionRequired` signals that the user
has not shared the friends list and you can directly call
`PlayGamesPlatform.Instance.AskForLoadFriendsResolution`.

### Determine friends list visibility

Use `PlayGamesPlatform.Instance.GetFriendsListVisibility` to check if the user
has shared the friends list with the game. Possible return statuses are:

- `FriendsListVisibilityStatus.RequestRequired` indicates you must ask for
  consent.

- `FriendsListVisibilityStatus.Visible` indicates that loading the friends list
  should succeed.

- `FriendsListVisibilityStatus.Unknown` generally shouldn't happen. You can set
  `forceReload` to true to refresh the data.

    PlayGamesPlatform.Instance.GetFriendsListVisibility(forceReload, (friendsListVisibilityStatus) => {});

## View a player profile

To add or remove a player as a friend, use the show and compare profile
function. This function triggers a bottom sheet dialog showing the Play Games
profile of the user; call the function with the player Id of the requested
player. If the player and friend have in-game nicknames, use them in the call to
add more context to the profile UI:

    PlayGamesPlatform.Instance.ShowCompareProfileWithAlternativeNameHintsUI(
        mFirstFriendId, /* otherPlayerInGameName= */ null, /* currentPlayerInGameName= */ null,
        (result) => {
            // Profile comparison view has closed.
    });