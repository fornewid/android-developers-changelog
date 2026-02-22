---
title: https://developer.android.com/games/playgames/user-acquisition
url: https://developer.android.com/games/playgames/user-acquisition
source: md.txt
---

With Google Play Games on PC, developers can run User Acquisition (UA) campaigns
similar to how they do so with mobile Android phones today using the [Google
Play Install Referrer library](https://developer.android.com/google/play/installreferrer) and linking to the
[Google Play Store
listing](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#OpeningDetails).

As a sample scenario:

1. The developer generates a Google Play URL, which includes marketing
   attribution information and links to the game's Google Play Store listing
   page, and uses it in an advertisement on the web or in an existing GPG on PC
   game. It could look something like this:

       https://play.google.com/store/apps/details?id=com.sample.package&referrer=utm_source%3Dsearch%26utm_medium%3Dcpc%26utm_campaign%3Dsummerpromo

   In this example
   `utm_source%3Dsearch%26utm_medium%3Dcpc%26utm_campaign%3Dsummerpromo`
   corresponds to the string created by the developer for marketing
   attribution, and upon game installation is passed through the *referrer*
   field to the game client.

   > [!NOTE]
   > **Note:** The referrer string must be URL encoded, 512 characters or less, and included in the referrer query parameter of the Google Play URL.

2. When a PC user clicks on an ad with this link, they are redirected to the
   game's listing page on the [Google Play web
   UI](https://play.google.com/store/games), which gives the user the option to
   *Install on Windows*.

   ![A sample store listing for a game on GPG on
   PC](https://developer.android.com/static/images/games/playgames/web-play-store-ui.png)

   Clicking *Install on Windows* prompts the user to either open or download
   the Google Play Games on PC client.

   ![Prompt asking the user to open the game listing page, or download the
   client if needed](https://developer.android.com/static/images/games/playgames/gpg-install-client-prompt.png)

   If the user already has the client installed, then clicking *Open* launches
   the game's detail page on Google Play Games on PC and automatically start
   the installation process.

   > [!NOTE]
   > **Note:** Depending on the browser, the user may need to accept a permission to allow the browser to open links within the Google Play Games on PC client

   If the user does not have Google Play Games on PC installed then clicking
   *Download* initiated the download of the platform installer, and upon a
   successful installation and setup of Google Play Games on PC, the game
   automatically starts installing.

   This is the same flow regardless if the user clicks the ad from the web
   browser, or if it's within another GPG on PC game. For the latter, the
   Google Play Games on PC client launches a browser with the game's listing
   page on the Google Play Store web UI to initiate the download flow.
3. Upon successful install and launch, the developer can retrieve referrer
   details within the game using the Google Play Install Referrer library.

   ![A sample game running on GPG on PC showing the successfully retrieved
   referrer string](https://developer.android.com/static/images/games/playgames/gpg-client-referrer-string.png)

> [!NOTE]
> **Note:** After a user initiates an install through the Google Play web UI, the GPG on PC client will retain the referrer until the game is successfully installed (up to 28 days after the install was originally initiated). After a successful game install, the referrer details will be maintained on the client for 90 days, as is [standard for the Play Referrer
> API](https://developer.android.com/google/play/installreferrer/igetinstallreferrerservice). As such, the referrer may be retained for at most 118 days.