---
title: https://developer.android.com/games/docs/release-notes
url: https://developer.android.com/games/docs/release-notes
source: md.txt
---

This page contains release notes for features and updates to Android games.
To get the latest product updates delivered to you, add the URL of this page to your
[feed
reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the feed URL directly: `https://developer.android.com/feeds/androidgames-release-notes.xml`.

## September 23, 2025

Announcement Google Play Games Level Up is a program to recognize and reward great gaming experiences across Google Play, providing you with powerful tools and promotional opportunities to drive business growth for your game.

Learn more: [Google Play Games \| Level Up](https://play.google.com/console/about/levelup/)

Google Play Games Level Up+ is a program where you receive all the benefits outlined on the [Google Play Games Level Up](https://play.google.com/console/about/levelup/) page and in addition you get exclusive premium benefits.

Learn more: [Google Play Games \| Level Up+](https://support.google.com/googleplay/android-developer/answer/16501431)

## September 17, 2025

Deprecated The [Google Play Games (v1) plugin for Unity, version 0.10.15](https://github.com/playgameservices/play-games-plugin-for-unity/releases/tag/v10.15) update includes the following changes:

Following the deprecation of [Google Sign-in](https://developer.android.com/identity/legacy/gsi) API, we are deprecating the Games v1 SDK and APIs.

> [!IMPORTANT]
> **Important:** Starting in May 2026, the deprecated APIs will be removed from the SDK. Then, as early as July 2028, calls to these APIs will fail, even if you're using older versions of the SDK.

## September 12, 2025

Deprecated The [play-services-games (v24.0.0)](https://mvnrepository.com/artifact/com.google.android.gms/play-services-games) update includes the following changes:

Following the deprecation of [Google Sign-in](https://developer.android.com/identity/legacy/gsi) API, we are deprecating Games v1 SDK and APIs.

> [!IMPORTANT]
> **Important:** Starting in May 2026, the deprecated APIs will be removed from the SDK. Then, as early as July 2028, calls to these APIs will fail, even if you're using older versions of the SDK.

## July 08, 2025

Feature The [Google Play Games plugin for Unity, version 2.1.0](https://github.com/playgameservices/play-games-plugin-for-unity/releases/tag/v2.1.0) update includes the following changes:

- Added support for additional auth scopes using [requestServerSideAccess](https://developer.android.com/games/pgs/unity/unity-start#retrieve-auth-codes).

- Published the [Play Games Services Unity Plugin (v2) Reference](https://developer.android.com/games/services/unity/v2/api) documentation.

Deprecated The [Google Play Games plugin for Unity, version 2.1.0](https://github.com/playgameservices/play-games-plugin-for-unity/releases/tag/v2.1.0) update includes the following changes:

- Removed the deprecated [Google Sign-In](https://developer.android.com/identity/legacy/gsi) dependency.

- Removed the deprecated [Google Drive](https://developers.google.com/android/reference/com/google/android/gms/drive/Drive) dependency.

## June 23, 2025

Feature The `play-services-games-v2 (v21.0.0)` update includes the following changes:

- Added support for additional auth scopes using [requestServerSideAccess](https://developers.google.com/android/reference/com/google/android/gms/games/GamesSignInClient#public-abstract-taskauthresponse-requestserversideaccess-string-serverclientid,-boolean-forcerefreshtoken,-listauthscope-scopes).

- Removed the deprecated [Google Sign-In](https://developer.android.com/identity/legacy/gsi) dependency.

- Removed the deprecated [Google Drive](https://developers.google.com/android/reference/com/google/android/gms/drive/Drive) dependency.

Feature The user can now request three basic OAuth 2.0 identity scopes with `GamesSignInClient` when requesting server-side access to Play Games Services web APIs.

For details, see:

- [Server-side access to Play Games Services](https://developer.android.com/games/pgs/android/server-access)

## May 05, 2025

Feature You can now import definitions and other metadata for multiple achievements together in a single step.

For details, see:
[Achievements](https://developer.android.com/games/pgs/achievements#import-achievements)

## November 20, 2024

Feature Google Play Games plugin for Unity, version 2.0.0 supports [recall API](https://developer.android.com/games/pgs/recall/recall-setup#unity-sdk).

For details, see:

- [Set up Google Play Games for Unity and sign-in](https://developer.android.com/games/pgs/unity/unity-start)