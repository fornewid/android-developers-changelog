---
title: https://developer.android.com/games/playgames/development-update
url: https://developer.android.com/games/playgames/development-update
source: md.txt
---

This guide describes how to update your game after it has been approved to
upload to the production track. It lists items to verify before updating your
game and publishing tasks to perform on new versions.

## Keep the Google Play Games on PC version available

Google Play Games on PC requires you to maintain the availability of Google Play Games on PC
versions along with mobile versions. This requirement includes the following
scenarios:

- Verify Google Play Games on PC version after you update the mobile
  version or related configurations on the server side.

  A common mistake in this scenario is that developers forget to verify
  their Google Play Games on PC version after they update the mobile version
  and/or server's configurations, which causes the server to reject requests for
  the outdated Google Play Games on PC version.
- Use the [link to Google Play](https://developer.android.com/distribute/marketing-tools/linking-to-google-play#OpeningDetails)
  for downloading a new update.

  The link on Google Play Games on PC is the same as on mobile. A common
  mistake in this scenario is that developers use a different link for
  mobile when they detect the game is running in an emulator. You can
  [detect Google Play Games on PC](https://developer.android.com/games/playgames/%22pc-compatibility#detect-hpe) and then use
  the correct link.

## Pre-submit checklist

This section describes a checklist that you need to verify before you submit each
update.

### Mobile checklist

- [Evaluate your game against the continuity requirements](https://developer.android.com/games/playgames/continuity-expected-behaviors).

### Google Play Games on PC checklist

- New features are shipped simultaneously with the mobile version.
- Verify the [Google Play Games on PC requirements checklist](https://developer.android.com/games/playgames/start#requirements-checklist).

## Publishing flows

We highly recommend that you always put a release candidate build on the test
track for game updates as soon as it's available. Contact **google-play-games-support@google.com**
with your package name and version code to request a review.

![upload_to_test_track_earlier](https://developer.android.com/static/images/games/playgames/update-flow-test-track-earlier.png)
**Figure 1.** Recommended publishing flow for review requests on the test track.

In figure 1, there are 4 phases:

1. Development phase. This includes coding, debugging, and testing.

2. Checklist phase. This includes verifying mobile and Google Play Games on PC
   checklists.

3. Publishing phase. Uploads versions to the test track before the production
   track, and then requests a review for the test track.

4. Review phase. This is performed in parallel with production publishing.

The other option is to request a review for the production track directly if
you are in an emergency situation, such as your game experiencing a crash that
must be fixed as soon as possible.

![upload_to_production_track_directly](https://developer.android.com/static/images/games/playgames/update-flow-production-track-directly.png)
**Figure 2.** Recommended publishing flow for making review requests directly
on the production track.

In figure 2, there are also 4 phases. The development and checklist phases are
the same as figure 1. In the publishing phase, you are able to upload to the
production track directly and the requested review is performed after
publishing.

For both publishing flows, we will contact you if we find violations of the
Google Play Games on PC requirements.