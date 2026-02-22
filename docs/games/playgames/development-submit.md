---
title: https://developer.android.com/games/playgames/development-submit
url: https://developer.android.com/games/playgames/development-submit
source: md.txt
---

This guide describes how to submit your game for distribution on
Google Play Games on PC.

As you complete the tasks, ensure that you [opt in](https://developer.android.com/games/playgames/development-submit#distribution-opt-in) to the
**Google Play Games on PC** distribution; otherwise, your submission will fail.

## Verify that you meet the Google Play Games on PC requirements

To help ensure a smooth submission process, review the [Playability
requirements](https://developer.android.com/games/playgames/start#playability-requirements) and verify that you've met the
Google Play Games on PC playability requirements.

For games seeking full certification for Google Play Games on PC, review the
[Requirements Checklist](https://developer.android.com/games/playgames/start#requirements-checklist).

## Add the Google Play Games on PC form factor

To enable the *Google Play Games on PC* form factor:

1. Go to advanced distribution settings at **Release \> Advanced settings** ([direct link](https://play.google.com/console/u/0/developers/app/advanced-distribution))
2. Go to the **Form factors** tab and add *Google Play Games on PC* from the **+ Add form factor** dropdown.

You have two options: **Use the same release track and
artifacts as your mobile app** and **Use a dedicated release track for Google
Play Games on PC**.

![A screenshot of choice of whether use dedicated track for Google Play Games on
PC](https://developer.android.com/static/images/games/playgames/choice_of_using_dedicated_track.png)

**Use the same release track and artifacts as your mobile app** Use this option
to continue using the mobile release track to serve Google Play Games on PC
with the same artifact. This shared track simplifies maintaining the release
process and QA testing, because the same artifact can contain assets and
features for different form factors. You can achieve this by using [Android app
bundles](https://developer.android.com/guide/app-bundle) without affecting the game's download size.

**Use a dedicated release track for Google Play Games on PC** Use this option if
your game requires different release artifacts for Google Play Games on PC.
A dedicated track allows you to:

- Create and manage separate tracks specifically for Google Play Games on PC.

- Publish different artifacts on each platform (mobile and PC).

- Manage your Google Play Games on PC releases and users independently from
  your mobile app.

For more information, see [Create and configure your Play multiplatform users
track](https://developer.android.com/games/playgames/development-submit#users-tracks).

If your game is already using the dedicated track, it will continue to function
as before. To migrate your game to the shared track:

- Select **Use the same release track and artifacts as your mobile app**.
- Complete all new requirements as prompted (for example, store listing assets).
- Submit the changes for review.

There is no service interruption. The existing dedicated track remains active
and serves users until the shared track submission is approved and published. The
transition then occurs automatically.

> [!NOTE]
> **Note:** You can switch between a shared or dedicated track at any time.

### Opt in to Google Play Games on PC distribution

1. Go to [advanced distribution](https://play.google.com/console/u/0/developers/app/advanced-distribution) settings at **Release \> Advanced settings**.
2. Go to the **Form factors** tab and open the settings for Google Play Games on PC via the **Manage** button.
3. Select **Opt-in to Google Play Games on PC** and save the settings.

> [!NOTE]
> **Note:** Remember to [Publish your
> changes](https://support.google.com/googleplay/android-developer/answer/9859654) to finish activating the PC formfactor.

## Set up game cards to make your game stand out on PC (optional)

A game card is an app icon for desktop games on Google Play Games. It has
expressive qualities, including interactive behavior and videos on hover. These
can be found on Home, Library, Continue Playing and All Games pages.

Game cards are composed of two elements, a background and a logo. Both of
these need to be set at the same time, otherwise you will receive an error in
the console.

To set up game cards, visit the **Grow \> Store Presence \> Main store listing**
or **Custom store listings** menus.

1. To set up the game card backgound, select **"Google Play Games on PC feature
   graphic"**.

   1. The image must be a PNG or JPG, 16:9 aspect ratio, up to 15 MB, with each side between 720 and 7680 px.
   2. The image should represent the game *cover* and not contain any text.

   3. To set up the game card logo, select **Google Play Games on PC logo**.

   4. The image must be a PNG, 600px by 400px, up to 8mb.

   5. The image should represent your game name and will be overlaid on top of
      the feature graphic. It should have a transparent background.

Setting these elements helps promote your game in different places in Google
Play.

## Create and configure your Play multiplatform users track

To distribute a PC optimized build, create a track:

1. Go to the closed testing page at **Release \> Test \> Closed testing** ([direct
   link](https://play.google.com/console/u/0/developers/app/closed-testing)).
2. If you have a dedicated track for Google Play Games on PC: Select **Google
   Play Games on PC only** from the **form factors** selector. If you are using your mobile artifacts, you don't need to select a new form factor.
3. Create a new closed testing track:
   1. Click **Create track** in the top right corner.
   2. Name the track *Play multiplatform users*. On successful creation, the site directs you to the track page for your new track. This track is also located on the closed testing page for the release type.
4. Click the **Manage track** button for the track.
5. On the **Countries / regions** tab, select the countries that should be
   targeted by the track. These are the countries and regions where releases on
   this track will be available. We recommend you select all available
   countries.

   1. You must include the United States and the United Kingdom for testing purposes if you opt to only allow certain regions.

   > [!NOTE]
   > **Note:** Including "United States" and "United Kingdom" is required for test tracks, but optional for production tracks.

6. On the **Testers** tab:

   1. Select **Google Groups**.
   2. In the **Email addresses** field, add the email `play-multiplatform-test-track@googlegroups.com`.

   > [!NOTE]
   > **Note:** Make a note of the opt-in URL provided for the test track to speed up the review process.

### Roll out a release on the dedicated track

Create a new Google Play Games on PC release on the closed
*Play multiplatform users* track and upload your game.

1. Go back to the track page for your new track. See [Create and configure your
   Play multiplatform users track](https://developer.android.com/games/playgames/development-submit#users-tracks) to manage the track.
2. Click **Create release** , which opens the **Prepare release** page for the new release.
3. Follow the on-screen instructions to prepare your release:
   - Add your app bundles or APKs.
   - Name your release.
   - Enter release notes for the version of your release.
4. Click **Save** to save your changes.
5. Click **Review release** to proceed to the review page.
6. On the review page, ensure that all the information you have entered is correct.
   - Validation errors and warnings will appear at the top of the screen. You must resolve any errors before you can proceed.
   - Review the information on the page to ensure that you have uploaded correct artifacts and entered your release details.
7. Click **Start roll-out** at the bottom of the page to complete rolling out your release.

For more information, see the [Prepare and roll out a
release](https://support.google.com/googleplay/android-developer/answer/9859348)
help center article.

> [!NOTE]
> **Note:** Your Google Play Games on PC release must align with your Android mobile update. Failure to do so will cause your game to warn users of game updates that are not available to them.

### Remove the Google Play Games on PC only form factor

To remove your game from Google Play Games on PC, remove the form factor as follows:

1. Go to [advanced distribution](https://play.google.com/console/u/0/developers/app/advanced-distribution) settings at **Release \> Advanced settings**.
2. Go to the **Form factors** tab
3. Find the **Google Play Games on PC** section
4. Select **Remove** on the right (next to **Manage**)
5. Read and confirm the dialog box that appears

After you remove the form factor, users who have already downloaded your game can still play
it. However, the game is no longer available from the Google Play Games on PC
storefront, and updates are no longer published to Google Play Games on PC.