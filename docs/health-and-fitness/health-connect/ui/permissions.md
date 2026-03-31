---
title: Permissions and data access  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-connect/ui/permissions
source: html-scrape
---

Starting in 2026, we'll be transitioning away from Google Fit APIs. For more information on the Google Fit migration, see the [Migration Guide](/health-and-fitness/guides/health-connect/migrate/migration-guide).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Health Connect Guides](https://developer.android.com/health-and-fitness/health-connect)

# Permissions and data access Stay organized with collections Save and categorize content based on your preferences.




Your app's Settings screen should provide users with options to manage their
connection to Health Connect. This gives users control over data
synchronization and access to their data.

![Revoked and cancelled permissions](/static/health-and-fitness/health-connect/images/hc_revoked_cancelled_permissions.png)


**Figure 1**: Revoked and cancelled permissions

## Sync with Health Connect

This toggle provides a way for users to pause or resume data
synchronization between your app and Health Connect.

* **When toggled on:** Your app actively reads and writes to Health
  Connect, as per the permissions granted by the user.
* **When toggled off:** Your app should stop all data synchronization with
  Health Connect. If you programmatically revoke permissions using
  [`revokeAllPermissions()`](/reference/kotlin/androidx/health/connect/client/PermissionController#revokeAllPermissions()), explain to the user that
  the changes aren't immediately reflected in Health Connect without an app
  restart. To avoid a confusing user experience, give users the option to go
  to Health Connect settings to revoke permissions there.

## Manage access

The **Manage access** button should provide a direct link for the user to manage
your app's permissions from within the Health Connect app. This gives the user
full control and transparency.

## Insufficient access

If your app has insufficient Health Connect access, users should be presented
with the following screen across all entry points:

![App with insufficient access](/static/health-and-fitness/health-connect/images/hc_insufficient_access.png)


**Figure 2**: App with insufficient access

## Permissions cancelled twice

If the user selects **Cancel** on the permissions request screen twice in a
row, your app should present the user with a screen similar to the following:

![Permissions cancelled twice by user](/static/health-and-fitness/health-connect/images/hc_permissions_cancelled_twice.png)


**Figure 3**: Permissions cancelled twice by user

**Note:** Once this screen is displayed, users need to re-enable permissions
from within the Health Connect Settings menu.

[Previous

arrow\_back

Promote Health Connect](/health-and-fitness/health-connect/ui/promote)

[Next

Data display and attribution

arrow\_forward](/health-and-fitness/health-connect/ui/data)