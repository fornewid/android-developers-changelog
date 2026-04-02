---
title: https://developer.android.com/games/pgs/unity/achievements
url: https://developer.android.com/games/pgs/unity/achievements
source: md.txt
---

This topic describes how to use Play Games Services achievements in Unity
games. It assumes that you've set up your project and the
Google Play Games plugin for Unity, as discussed in the
[Get started guide](https://developer.android.com/games/pgs/unity/unity-start).

## Create an achievement

When you set up your project and plugin, create the achievements in
Google Play Console and then update the plugin with the Android resources
for your achievements. For details about creating achievements in
Play Console, see the
[achievements guide](https://developer.android.com/games/pgs/achievements#create_an_achievement).

## Reveal and unlock an achievement

To unlock an achievement, use the **Social.ReportProgress** method with a
progress value of 100.0f:

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // unlock achievement (achievement ID "Cfjewijawiu_QA")
        Social.ReportProgress("Cfjewijawiu_QA", 100.0f, (bool success) => {
          // handle success or failure
        });

According to the expected behavior of
[Social.ReportProgress](http://docs.unity3d.com/Documentation/ScriptReference/Social.ReportProgress.html),
a value of 0.0f means the achievement is revealed and a progress of 100.0f
means the achievement is unlocked.

To reveal an achievement that was
previously hidden without unlocking it, call **Social.ReportProgress** with
a value of 0.0f.

## Increment an achievement

If the achievement is incremental, the Play Games implementation of
**Social.ReportProgress** will try to adhere to the
expected behavior according to Unity's social API. The behavior might not be
identical, though, so we recommend that you don't use **Social.ReportProgress**
for incremental achievements. Instead, use the
[PlayGamesPlatform.IncrementAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#incrementachievement) method, which is a
Play Games extension.

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // increment achievement (achievement ID "Cfjewijawiu_QA") by 5 steps
        PlayGamesPlatform.Instance.IncrementAchievement(
            "Cfjewijawiu_QA", 5, (bool success) => {
                // handle success or failure
        });

## Show the achievements UI

To show the built-in UI for all achievements, call
**Social.ShowAchievementsUI**.

        using GooglePlayGames;
        using UnityEngine.SocialPlatforms;
        ...
        // show achievements UI
        Social.ShowAchievementsUI();