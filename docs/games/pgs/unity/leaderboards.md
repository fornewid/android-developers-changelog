---
title: https://developer.android.com/games/pgs/unity/leaderboards
url: https://developer.android.com/games/pgs/unity/leaderboards
source: md.txt
---

This topics describes how to use Play Games Services leaderboards in Unity
games.

## Before you get started

Set up your Unity project and the Google Play Games plugin for Unity. For
details, see the [Get started guide](https://developer.android.com/games/pgs/unity/unity-start).

## Create events

You create leaderboards in Google Play Console. For details, see the
[leaderboards guide](https://developer.android.com/games/pgs/leaderboards#create_a_leaderboard) for
Play Games Services. After you create a leaderboard, add its Android resource
to the plugin as described in the
[get started guide](https://developer.android.com/games/pgs/unity/unity-start).

## Post a Score to a Leaderboard

To post a score to a leaderboard, call **Social.ReportScore**.

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // Post score 12345 to leaderboard ID "Cfji293fjsie_QA")
        Social.ReportScore(12345, "Cfji293fjsie_QA", (bool success) => {
            // Handle success or failure
        });

To post a score and include a metadata tag, use a [PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform)
instance directly:

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // Post score 12345 to leaderboard ID "Cfji293fjsie_QA" and tag "FirstDaily")
        PlayGamesPlatform.Instance.ReportScore(12345, "Cfji293fjsie_QA", "FirstDaily", (bool success) => {
            // Handle success or failure
        });

Note that the platform and the server will automatically discard scores that are
lower than the player's existing high score, so you can submit scores freely
without any checks to test whether or not the score is greater than the player's
existing score.

## Show the Leaderboard UI

To show the built-in UI for all leaderboards, call **Social.ShowLeaderboardUI**.

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // Show leaderboard UI
        Social.ShowLeaderboardUI();

If you wish to show a particular leaderboard instead of all leaderboards, you
can pass a leaderboard ID to the method. This, however, is a Play Games
extension, so the Social.Active object needs to be cast to a
[PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform) object first:

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // Show leaderboard UI
        PlayGamesPlatform.Instance.ShowLeaderboardUI("Cfji293fjsie_QA");

## Access Leaderboard data

There are 2 methods to retrieving the leaderboard score data.

### Use Social.ILeaderboard

This method uses the ILeaderboard interface to define the scope and filters
for getting the data. This approach allows you to configure:
1. The leaderboard Id
2. The collection (social or public)
3. The timeframe (daily, weekly, all-time)
4. The rank position to start retrieving scores.
5. The number of scores (the default is 25).
6. Filter by user id.

If the from parameter is non-positive, then the results returned are
player-centered, meaning the scores around the current player's score are
returned.

        ILeaderboard lb = PlayGamesPlatform.Instance.CreateLeaderboard();
        lb.id = "MY_LEADERBOARD_ID";
        lb.LoadScores(ok =>
            {
                if (ok) {
                    LoadUsersAndDisplay(lb);
                }
                else {
                    Debug.Log("Error retrieving leaderboardi");
                }
            });

### Use PlayGamesPlatform.LoadScores()

This method uses [PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform) directly, which provides additional
flexibility and information when accessing the leaderboard data.

        PlayGamesPlatform.Instance.LoadScores(
                GPGSIds.leaderboard_leaders_in_smoketesting,
                LeaderboardStart.PlayerCentered,
                100,
                LeaderboardCollection.Public,
                LeaderboardTimeSpan.AllTime,
                (data) =>
                {
                    mStatus = "Leaderboard data valid: " + data.Valid;
                    mStatus += "\n approx:" +data.ApproximateCount + " have " + data.Scores.Length;
                });

The parameters for LoadScores() are:

1. leaderboardId
2. start position (top scores or player centered)
3. row count
4. leaderboard collection (social or public)
5. time span (daily, weekly, all-time)
6. callback accepting a LeaderboardScoreData object.

The [LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data)
class is used to return information back to the
caller when loading scores. The members are:

    1. Id - the leaderboard id
    2. Valid - true if the returned data is valid (the call was successful)
    3. Status - the ResponseStatus of the call
    4. ApproximateCount - the approximate number of scores in the leaderboard
    5. Title - the title of the leaderboard
    6. PlayerScore - the score of the current player
    7. Scores - the list of scores
    8. PrevPageToken - a token that can be used to call `LoadMoreScores()` to
        get the previous page of scores.
    9. NextPageToken - a token that can be used to call `LoadMoreScores()` to
        get the next page of scores.

        void GetNextPage(LeaderboardScoreData data)
        {
            PlayGamesPlatform.Instance.LoadMoreScores(data.NextPageToken, 10,
                (results) =>
                {
                    mStatus = "Leaderboard data valid: " + data.Valid;
                    mStatus += "\n approx:" +data.ApproximateCount + " have " + data.Scores.Length;
                });
        }

This call may fail when trying to load friends with
`ResponseCode.ResolutionRequired` if the user has not shared their friends list
with the game. In this case, use `AskForLoadFriendsResolution` to request
access.

### Get player names

Each score has the userId of the player that made the score. You can use
`Social.LoadUsers()` to load the player profile. Remember that the contents
of the player profile are subject to privacy settings of the players.

        internal void LoadUsersAndDisplay(ILeaderboard lb)
        {
            // Get the user ids
            List<string> userIds = new List<string>();

            foreach(IScore score in lb.scores) {
                userIds.Add(score.userID);
            }
            // Load the profiles and display (or in this case, log)
            Social.LoadUsers(userIds.ToArray(), (users) =>
                {
                    string status = "Leaderboard loading: " + lb.title + " count = " +
                        lb.scores.Length;
                    foreach(IScore score in lb.scores) {
                        IUserProfile user = FindUser(users, score.userID);
                        status += "\n" + score.formattedValue + " by " +
                            (string)(
                                (user != null) ? user.userName : "**unk_" + score.userID + "**");
                    }
                    Debug.log(status);
                });
        }