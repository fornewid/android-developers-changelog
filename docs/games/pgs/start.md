---
title: https://developer.android.com/games/pgs/start
url: https://developer.android.com/games/pgs/start
source: md.txt
---

This page outlines how to set up [Google Play Games Services](https://developer.android.com/games/pgs/overview) and then
add features to an Android game. The tasks include setting up the service in
Google Play Console and adding features to your game, such as
authentication and achievements.

To go straight to the guides for each programming language, use these links:

[C and CPP](https://developer.android.com/games/pgs/cpp/cpp-start)
[Unity](https://developer.android.com/games/pgs/unity/unity-start)
[Java](https://developer.android.com/games/pgs/android/android-start)

The Play Games Services setup tasks are common for C and Java games. However,
the tasks that set up your game project and add Play Games Services features
are specific to the main programming language used in the game project. The get
started tasks for Unity games have additional difference because they use a
[plugin](https://developer.android.com/games/pgs/unity/overview) for Play Games Services instead of having
an additional set of C# APIs.

Here are the basic steps to set up Play Games Services for a game and add
features:

1. [Set up](https://developer.android.com/games/pgs/start#setup-pgs) Play Games Services.

2. [Set up your game project](https://developer.android.com/games/pgs/start#setup-project) and integrate the authentication
   service.

3. Set up and [add features](https://developer.android.com/games/pgs/start#add-features) to your game project.

4. [Test and Publish](https://developer.android.com/games/pgs/start#test-publish) any changes you make to your
   Play Games Services features.

## Before you start

You must have a Google Play Developer account set up in
Play Console. For more information, see the
[Register for a Google Play Developer account](https://support.google.com/googleplay/android-developer/answer/6112435).

## Set up Play Games Services

- To set up Play Games Services in Google Play Console, see the
  [set up](https://developer.android.com/games/pgs/console/setup) guide.

- For Unity games: If you are developing your game in Unity, after you
  complete these, you must perform additional steps to configure the
  [Google Play Games plugin for Unity](https://developer.android.com/games/pgs/unity/overview). See the
  [plugin set up](https://developer.android.com/games/pgs/unity/unity-start) guide for details.

## Set up your game project

You must set up a Play Games Services in your game project and integrate the
[platform authentication](https://developer.android.com/games/pgs/signin) before adding other
Play Games Services features. See the following guides for details. These tasks
are specific to the main programming language used by your game project:

- [C and C++ games](https://developer.android.com/games/pgs/cpp/cpp-start)

- [Unity games](https://developer.android.com/games/pgs/unity/unity-start)

- [Java games](https://developer.android.com/games/pgs/android/android-signin)

## Add additional features

After you integrate authentication, you can add additional Play Games Services
features to your game. This involves setting up the feature in
Play Console and then integrating the API in your game project.
See the following guides for details:

- [Achievements](https://developer.android.com/games/pgs/achievements)

- [Leaderboards](https://developer.android.com/games/pgs/leaderboards)

- [Events](https://developer.android.com/games/pgs/events)

- [Friends](https://developer.android.com/games/pgs/friends)

- [Saved games](https://developer.android.com/games/pgs/savedgames)

## Test and publish Play Games Services updates

After you add Play Games Services features to your game project, you should
test any updates you make to your Play Games Services project using the
[test accounts](https://developer.android.com/games/pgs/console/setup#start) that you setup when you
configure Play Games Services. When you're satisfied with the changes, you can
use Play Console to [publish](https://developer.android.com/games/pgs/console/publish) them.
This does not involve publishing your game, and only updates the
Play Games Services project and services hosted by Google.

## What's next

After you set up Play Games Services and add features to your game, you can use
the Play Games Services REST APIs for
[publishing](https://developer.android.com/games/pgs/publishing/publishing) and
[management](https://developer.android.com/games/pgs/management/management) tasks.