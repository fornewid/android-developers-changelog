---
title: https://developer.android.com/games/pgs/quota
url: https://developer.android.com/games/pgs/quota
source: md.txt
---

This topic describes how to detect and manage Play Games Services API usage in
your game.

## Detect rate limiting

If you are using the Play Games Services SDK, your callback handlers or listeners
return errors when your game exceeds its rate limit.

In Android, calls that return
[`PendingResult`](https://developers.google.com/android/reference/com/google/android/gms/common/api/PendingResult)
objects, such as
[`incrementImmediate`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient#public-abstract-taskboolean-incrementimmediate-string-id,-int-numsteps),
return a
[`NETWORK_ERROR_OPERATION_FAILED`](https://developers.google.com/android/reference/com/google/android/gms/games/GamesClientStatusCodes#constant-summary)
status code in the result object. This status code indicates that the library
will automatically attempt to make the call again later when your game is no
longer rate limited.

To request additional quota for your games, see the
[quota increase](https://developer.android.com/games/pgs/quota#quota-increase) section.

## Manage your daily quota

You can review your application's daily quota for Google Cloud Platform by
visiting your project in the
[Google Cloud Platform](https://console.developers.google.com/).

To view or change usage limits for your project, or to request an increase to
your quota, do the following:

1. If you don't already have a [billing account](https://cloud.google.com/billing/docs/how-to/manage-billing-account) for your project, then create one.
2. [Visit the Enabled APIs page of the
   API library](https://console.cloud.google.com/apis/enabled) in the API Console, and select an API from the list.
3. To view and change quota-related settings, select **Quotas** . To view usage statistics, select **Usage**.

You can set the maximum number of calls a user can make per second, to
help ensure that an abusive player doesn't use up all of your application's
quota. To learn more about capping usage, see the
Google Cloud Platform
[documentation](https://developers.google.com/console/help/capping-usage).

To request additional quota for your games, see the
[quota increase](https://developer.android.com/games/pgs/quota#quota-increase) section.

## Request a quota increase

To request a game quota increase, click the *Request more* link next to
your app's quota entry in the
[Google Cloud Platform](https://console.developers.google.com/).

Requests to increase the games quota usually aren't accepted unless your game is
experiencing exceptional usage and is obeying the best practices in the
[quality checklist](https://developers.google.com/games/services/bestpractices#9_quota_and_rate_limiting).