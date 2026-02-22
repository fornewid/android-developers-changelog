---
title: https://developer.android.com/games/playgames/publish-deploy
url: https://developer.android.com/games/playgames/publish-deploy
source: md.txt
---

This guide should tell you everything you need to know about development for PC,
including references to our ChromeOS developer documentation for areas in
common, such as supporting keyboard and mouse input. While our [Android on
ChromeOS documentation](https://developer.android.com/chrome-os/intro) has lots of helpful information, note
that this guide should be treated as the source of truth for the requirements to
optimize your game on PC.

## Testing

During the first phase of development, you can test the changes you make to your
game on a physical Chromebook. [Any Chromebook that supports
Android](https://www.chromium.org/chromium-os/chrome-os-systems-supporting-android-apps) will work.

Alternatively, our team can ship you a loaner Chromebook device to use during
this process. For information on receiving a test device, notify your Google
Play point of contact, and they will follow up with instructions.

## APK and app bundle management

Google Play Games on PC will allow you to upload an APK or app bundle to the
Google Play Console to be used on PC. We strongly recommend you use the same
APK as your mobile game to reduce additional maintenance cost and complexity. In
changes specific to PC and Chromebook. All requirements described in this
document are only required for the PC version of your game, so we recommend
using this conditional check for any new changes you make to your game.

Once you begin developing for PC, we will provide a way to detect whether your
user is on a PC. While initially developing for a Chromebook, you can use the
following code for detection:

    fun isArc() : Boolean {
        return packageManager.hasSystemFeature("org.chromium.arc")
    }

Alternatively, you can [check for the presence of a physical
keyboard](https://developer.android.com/games/develop/all-screens#handle-interaction-models) as outlined in
the documentation.

## Build submission process

Once your game has successfully met the requirements in the PC optimization
checklist and is ready for review, the next step is to submit the build through
a test track in the Google Play Console for review. The following are steps
for uploading your build to the console.

In order to complete a Google Play Games on PC release and view the *Google
Play Games on PC only* form factor, your Google Play point of contact must
enable the feature on your Google Play Developer account. Contact them to enable
the feature if you haven't already done so.

### Ensure your app meets the required size limits

In order to upload your game to the console and to eventually publish on the
platform, your game must be within the size limits allowed by Google Play
policy. Play policy sets the following size limits:

- Legacy APK submissions:
  - [100 MB](https://support.google.com/googleplay/android-developer/answer/2481797) maximum APK size.
  - Up to 2 GB for assets for each [APK expansion file](https://developer.android.com/google/play/expansion-files) (OBB).
- App Bundle submissions:
  - [200 MB](https://developer.android.com/guide/app-bundle#size_restrictions) maximum base module size.
  - Up to 1.5 GB for each asset pack through [Play Asset Delivery](https://developer.android.com/guide/app-bundle/asset-delivery). For games with a cumulative total larger than 4 GB, contact your Google Play point of contact for additional space.

Here are a few things to double-check before proceeding with your console
submission:

1. It is recommended that you use App Bundles and Play Asset Delivery to publish your game. Note that in the second half of 2021, [OBBs will be
   deprecated](https://android-developers.googleblog.com/2020/08/recent-android-app-bundle-improvements.html) and new games will be required to switch over to Play Asset Delivery.
2. If you are using OBBs to deliver assets, additional high resolution assets might cause the total size to exceed the OBB limit (2 GB main + 2 GB patch). In this case, it is recommended that you switch over to Play Asset Delivery.
3. If you are submitting a debug build, ensure that the APK fits within the size constraints. If your APK exceeds the limit, you may instead need to share a non-development build.

### Add the Google Play Games on PC only release type

This step assumes you have already worked with your Google Play point of contact
to enable your account for the *Google Play Games on PC only* form factor, as
this feature is only available for early access. If you don't see the form
factor *Google Play Games on PC only*, then make sure you first work with your
point of contact to enable the feature in your Google Play Developer account.

While this project is in its pre-launch phase, the form factor will be labeled
*Google Play Games on PC only* . To release to the *Google Play Games on PC only*
test track, you first need to add the form factor for the app by following the
steps.

1. Go to advanced distribution settings at **Release \> Advanced settings** ([direct
   link](https://play.google.com/console/u/0/developers/app/advanced-distribution))
2. Go to the **Form factors** tab and add *Google Play Games on PC only* from the **+ Add form factor** drop-down.

This will also create the release tracks that you will use to roll out releases.
These are separate from the tracks you will use to release to phones and
tablets.

### Create and configure your Play multi platform users track

To distribute your PC-optimized build, create a users track:

1. Go to the closed testing page at **Release \> Test \> Closed testing** ([direct
   link](https://play.google.com/console/u/0/developers/app/closed-testing))
2. Select *Google Play Games on PC only* from the form factors selector in the top right corner.
3. Create a new closed testing track:
   1. Click **Create track** in the top right corner.
   2. Name the track *Play multi platform users*. On successful creation, the site directs you to the track page for your new track. This is also located on the closed testing page for the release type.
4. Click the **Manage track** button for the track.
5. On the **Countries / regions** tab select the countries which should be
   targeted by the track. These are the countries and regions where releases on
   this track will be available. We recommend you select all available countries
   unless you have specific requirements otherwise.

   > [!NOTE]
   > **Note:** You must add "United States" and "United Kingdom" for testing purposes if you opt to only allow certain regions.

6. On the **Testers** tab:

   1. Select **Google Groups**.
   2. In the **Email addresses** field, add the email `play-multiplatform-test-track@googlegroups.com`. ![screenshot_of_plat_multiplatform_user_test_group](https://developer.android.com/static/images/games/playgames/test_group_configuration.png) Note: Make a note of the opt-in URL provided for the test track. You'll need to provide this URL to your Google Play point of contact to make sure your build is properly reviewed.

### Roll out a release

Create your new Google Play Games on PC release on the closed
*Play multi platform users* track. You can upload either your existing APKs and
app bundles or a Google Play Games on PC-optimized version of the same.

1. Go back to the track page for your new track. See steps 1, 2, and 4 from [Create and configure your Play multi platform users track](https://developer.android.com/games/playgames/publish-deploy#users-tracks) to manage the track.
2. Click **Create release** in the top right corner. You will be navigated to the **Prepare release** page for the new release.
3. Follow the on-screen instructions to prepare your release:
   - Add your app bundles or APKs.
   - Name your release.
   - Enter release notes for the version of your release.
4. Click **Save** at the bottom of the screen to save any changes that you made to your release.
5. When you've finished preparing your release, click **Review release** to proceed to the review page.
6. On the review page, ensure that all the information you have entered is correct.
   - Validation errors and warnings will appear at the top of the screen. Errors need to be resolved before you can proceed.
   - Review the information on the page to ensure that you have uploaded correct artifacts and entered your release details.
7. Click **Start roll-out** at the bottom of the page to complete rolling out your release.

For more information on the **Prepare and review** release flow you can refer to
this [help center article](https://support.google.com/googleplay/android-developer/answer/9859348).

### Opt in to Google Play Games on PC only distribution

At this point you should be ready to distribute your new
Google Play Games on PC releases. You need to go back to the form factor
settings and opt in to distribution.

1. Go to advanced distribution settings at **Release \> Advanced settings** ([direct
   link](https://play.google.com/console/u/0/developers/app/advanced-distribution))
2. Go to the **Form factors** tab and open the settings for Google Play Games on PC using the **Manage** button.
3. Select *Opt-in to Google Play Games on PC only* and save the settings.

Once you are opted in and all of your recent changes are reviewed and approved,
your app will be successfully available for review by our team.

### Notify your Google Play POC that a new release is available

Once you've successfully uploaded a release to your *Play multi platform
testers* track, and opted in to Google Play Games on PC only distribution,
notify your Google Play point of contact over email that your build is now ready
for review. Your uploaded build will be shared with members of the review teams,
and your point of contact will follow up directly with further instructions.