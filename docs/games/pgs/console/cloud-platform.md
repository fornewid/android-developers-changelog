---
title: https://developer.android.com/games/pgs/console/cloud-platform
url: https://developer.android.com/games/pgs/console/cloud-platform
source: md.txt
---

There may be instances where you will want to view and edit your
Play Games Services project directly in Google Cloud Platform.

Typical scenarios include:

- Enabling additional APIs for your project (such as Google Drive).
- Editing the branding information for your game in the OAuth 2.0 dialog.
- Viewing your API quota and requesting more (if necessary).
- Editing authorized URIs or JavaScript origins in Client IDs that you've created in the past.

### View your project

To view your project in Google Cloud Platform:

1. Select a credential for your game on the **Configuration** page (**Grow users \> Play Games
   Services \> Setup and
   management \> Configuration**).
2. Scroll to the bottom of the **Authentication** section and click **View in
   Google Cloud Platform**.

### Adjust API usage quotas

In Google Cloud Platform, you can view the API usage limits currently set up for
your game and the amount of quota that has been used. You can also set per-user
limits to prevent an abusive user (or a buggy game client) from depleting your
quota.

To view or change usage limits for your project, or to request an increase to
your quota, do the following:

1. If you don't already have a [billing account](https://cloud.google.com/billing/docs/how-to/manage-billing-account) for your project, then create one.
2. [Visit the Enabled APIs page of the
   API library](https://console.cloud.google.com/apis/enabled) in the API Console, and select an API from the list.
3. To view and change quota-related settings, select **Quotas** . To view usage statistics, select **Usage**.

Be aware that "users" are determined based on the IP address of the
client making the quota request. For instance, if all of your requests came from
a single server, that server might be erroneously tagged as a single spammy user.
To prevent this, you can attach a `userIp=x.x.x.x` argument to your API endpoint
requests.

To learn more about setting per-user quotas, see
Google Cloud [documentation](https://cloud.google.com/apis/docs/capping-api-usage).

In addition to a per-user limit, there is an application-wide
per-day limit for the Google Play Games Services API. Typically, you
will not need to change the pre-allocated limit. However, if you anticipate a
large spike in volume (for example, for an upcoming launch event), you can
request for additional quota by clicking the **Request more** link.

### Activate other APIs

When you create your client ID in Play Console, the
Google Play Games Services API is automatically turned on for your project. You
can activate other Google APIs from Google Cloud Platform.

To enable an API for your project, do the following:

1. [Open the API Library](https://console.developers.google.com/apis/library)
   in Google API Console. If prompted, select a project or create a new one.
   API Library lists all available APIs, grouped by product family and
   popularity.

2. If the API you want to enable isn't visible in the list, use search to
   find it.

3. Select the API you want to enable, then click the **Enable** button.

4. If prompted, enable billing.

5. If prompted, accept the API's terms of service.

### Modify branding information

To modify the branding information (title, logo, etc.) for your game that
appears in the OAuth 2.0 dialog, set the attributes in the consent screen of
Google Cloud.

To set up your project's consent screen, do the following:

1. Open the [Consent Screen page](https://console.developers.google.com/apis/credentials/consent) in Play Console. If prompted, select a project or create a new one.
2. Fill out the form and click **Save**.

### Modify the OAuth user type

If you are testing in the [Production](https://play.google.com/console/u/0/developers/app/tracks/production)
**(Test and release \> Production)** testing track using a [personal testing
account](https://support.google.com/googleplay/android-developer/answer/14151465),
you must have also configured your OAuth audience setting in Google Cloud as
**External** . For more information, see
[Manage App audience](https://support.google.com/cloud/answer/15549945).

### Modify client ID related attributes

| **Important:** If you change the launch URL of your web app, you must follow the instructions below to make the corresponding change in Play Console to avoid getting `origin_mismatch` errors. If you change the package name of your Android app, you must create a new linked app entry and remove the existing linked app entry that has the old package name.

To modify attributes related to your OAuth 2.0 client ID (web
origins and redirect urls for a web app, etc.):

1. Open Play Console and navigate to your game.
2. Select a credential for your game on the **Configuration** page (**Grow users \> Play Games
   Services \> Setup and
   management \> Configuration**).
3. Scroll to the bottom of the **Authentication** section and click **View in
   Google Cloud Platform**.
4. In Google Cloud, select your project.
5. In the sidebar on the left, select **APIs \& auth** . Make sure that the Google Play Games Services API status is **ON** in the displayed list of APIs.
6. In the sidebar on the left, select **Registered apps**.
7. Expand the OAuth 2.0 Client ID section and find the attribute to edit.