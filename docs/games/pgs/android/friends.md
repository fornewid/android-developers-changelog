---
title: https://developer.android.com/games/pgs/android/friends
url: https://developer.android.com/games/pgs/android/friends
source: md.txt
---

> [!NOTE]
> **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
> documentation](https://developer.android.com/games/pgs/v1/android/friends).

This guide describes how to use the [Friends](https://developer.android.com/games/pgs/friends) APIs in
Android Studio projects.

## Load friends

You can retrieve and display (in the game) a list of players who are friends
with the current user. As a user, it is possible to control which games have
access to the friends list. When you retrieve the friends list, you must handle
the case where permission is required. This is all encapsulated in the API to
make requesting access and subsequently using the friends list a straightforward
task. To load the friends list, follow these steps:

1. Call the [`PlayersClient.loadFriends()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient#loadFriends(int,%20boolean)) method, which is an asynchronous call returning a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object.
2. If the call is successful (the user already granted access to the friends list), Google Play Games Services returns an annotated [`PlayerBuffer`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayerBuffer) that represents the user's friends.
3. If the player needs to grant access to the friends list, the call fails with
   a
   [`FriendsResolutionRequiredException`](https://developers.google.com/android/reference/com/google/android/gms/games/FriendsResolutionRequiredException).
   No dialogs are shown yet.

   1. This exception contains an `Intent` that triggers a dialog to ask the player for consent. You can launch this `Intent` immediately to open a consent dialog. You can only use this `Intent` once.
   2. If the result of the `Intent`'s activity is `Activity.RESULT_OK`, then
      consent was granted. Call `loadFriends()` again to return the friends
      list. If the result is `Activity.RESULT_CANCELLED`, the user did
      not consent and `loadFriends()` will continue to return
      `FriendsResolutionRequiredException`.

      > [!NOTE]
      > **Note:** If you call `loadFriends()` from your server and determine that you need to request consent, you need to call `loadFriends()` again from your game client. This second call won't succeed, but it will provide you the `Intent` required to show the consent dialog.

The following code shows how to load the friends list:

    // Attempt loading friends.
    // Register a success listener to handle the successfully loaded friends list.
    // Register a failure listener to handle asking for permission to access the list.
    PlayGames.getPlayersClient(this)
        .loadFriends(PAGE_SIZE, /* forceReload= */ false)
        .addOnSuccessListener(
            new OnSuccessListener<AnnotatedData<PlayerBuffer>>() {
                @Override
                public void onSuccess(AnnotatedData<PlayerBuffer>  data) {
              PlayerBuffer playerBuffer = data.get();
              // ...
            })

        .addOnFailureListener(
            exception -> {
          if (exception instanceof FriendsResolutionRequiredException) {
            PendingIntent pendingIntent =
                ((FriendsResolutionRequiredException) task.getException())
                .getResolution();
            parentActivity.startIntentSenderForResult(
                pendingIntent.getIntentSender(),
                /* requestCode */ SHOW_SHARING_FRIENDS_CONSENT,
                /* fillInIntent */ null,
                /* flagsMask */ 0,
                /* flagsValues */ 0,
                /* extraFlags */ 0,
                /* options */ null);
         }
       });
     return;
    }

The following code shows how to handle the result from the request for consent:

    /** Handle the activity result from the request for consent. */
    @Override
    public void onActivityResult(int requestCode, int result, Intent data) {
      if (requestCode == SHOW_SHARING_FRIENDS_CONSENT) {
        if (result == Activity.RESULT_OK) {
          // We got consent from the user to access their friends. Retry loading the friends
          callLoadFriends();
        } else {
          // User did not grant consent.
        }
      }
    }

## View another player's profile

You can display a view of another player's Play Games profile from
within your game. This view allows players to send and accept friend invitations
for the player being viewed. This view does not require access to the friends
list. Additionally, if your game has its own concept of player names separate
from Play Games Gamer IDs, you can pass these along to the profile view
so that they can be included in any friend invitations for additional context.

To show another player's profile, follow these steps:

1. Call the [`PlayersClient.getCompareProfileIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient) method, which is an asynchronous call returning a [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) object.
2. If the call is successful, Google Play Games Services returns an Intent that will display a screen where the user can compare themselves against another player's profile.
3. Use the `Intent` from the previous step to start an activity.

    // Retrieve and launch an Intent to show a player profile within the game.
    PlayGames.getPlayersClient(this)
        .getCompareProfileIntent(otherPlayerId)
        .addOnSuccessListener(new OnSuccessListener<Intent>() {
            @Override
            public void onSuccess(Intent  intent) {
              startActivityForResult(intent, RC_SHOW_PROFILE);
              // ...
            }});

If the game has its own name for players, these can be added to the API call.
This enables Play Games to set the nickname of players who send friend
invitations from within your game to "\<game-specific-name\> from
\<your-game-name\>" Play Games automatically appends "from
\<your-game-name\>"):

    // Show a player profile within the game, with additional hints containing the
    // game-specific names for both players.
    // - otherPlayerId is the Play Games playerId of the player to view.
    // - otherPlayerInGameName is the game-specific name of the player being viewed.
    // - currentPlayerInGameName is the game-specific name of the player who is authenticated.
    //   Hence if the player sends an invitation to the profile they are viewing,
    //   their game-specific name can be included.
    PlayGames.PlayersClient(this)
        .getCompareProfileIntentWithAlternativeNameHints(otherPlayerId, otherPlayerInGameName, currentPlayerInGameName)
        .addOnSuccessListener(new OnSuccessListener<Intent>() {
            @Override
            public void onSuccess(Intent  intent) {
              startActivityForResult(intent, RC_SHOW_PROFILE);
              // ...
            }});