---
title: https://developer.android.com/health-and-fitness/health-connect/test/test-cases
url: https://developer.android.com/health-and-fitness/health-connect/test/test-cases
source: md.txt
---

| **Caution:** Test cases are continuously evolving. Make sure you're checking them for any updates before running your test cycles.

You are responsible for testing your applications and verifying users have a
positive and consistent experience. Health Connect recommends a list of test
cases that are designed to conform with best practices and user experience
guidelines.

If you're using a tracker to monitor your progress in your test cycles, you can
add them in your list and customize them depending on your app's requirements.

## 01: Request permissions through an onboarding flow


| Details ||
|---|---|
| **Description** | Every time a user installs a health and fitness app for the first time, they must go through an onboarding process to integrate the app with Health Connect. |
| **Requirements** | The Health Connect app must be installed on the phone. |
| **Notes** | If your app can display the integration status with Health Connect, you can check it from there. |
| **Reference** | [New Health Connect users](https://developer.android.com/guide/health-and-fitness/health-connect/design/permissions-and-data#new-health-connect-users) |

<br />

### Steps

1. Open your app.
2. Go to the promo card, modal, **Settings** screen, or similar screens that allow users to integrate with Health Connect for the first time.
3. Open the onboarding screen by following the steps indicated in your app.
4. On the onboarding screen, tap **Get started**.
5. On the rational screen, toggle **Allow all** to enable permissions listed for your app.
6. Tap **Allow** to grant permissions.

### Expected results

![Onboarding flow](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-01.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- Users is taken to the rationale screen with all required read and write permissions.
- Granted permissions is reflected properly in the Health Connect app.


FAIL for *any* of the following reasons:

- The user is not taken to the rationale page with all required read and write permissions.
- Granted permissions isn't reflected properly in the Health Connect app.

## 02-01: Attempt to integrate with Health Connect while uninstalled


| Details ||
|---|---|
| **Description** | When a user decides to sync data to Health Connect, but the Health Connect app is uninstalled, the app must have a way to inform users how to install the Health Connect app. Preferably, have the app directly load the Health Connect page in the Google Play store to install it. |
| **Requirements** | The Health Connect app must not be installed on the phone. |

<br />

### Steps

1. Open your app.
2. Navigate to the app's **Settings** screen (or similar screens) where it has the option to integrate with Health Connect.
3. Choose to install Health Connect.

### Expected results

![Attempt to integrate with Health Connect while uninstalled](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-02-01.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The app's **Settings** screen (or similar screens) must have a feature to integrate with Health Connect.
- Users must be taken to the Health Connect page in the Google Play store.


FAIL for *any* of the following reasons:

- There's no way to integrate with Health Connect in the app's **Settings** screen or any similar screens.
- Users are not taken to the Health Connect page in the Google Play store.

## 02-02: Integrate with Health Connect through your app


| Details ||
|---|---|
| **Description** | When a user decides to sync data to Health Connect, and the Health Connect app is installed, the app must have a way to inform users how to integrate with Health Connect. It must direct users into the Health Connect app. |
| **Requirements** | The Health Connect app must be installed on the phone. |

<br />

### Steps

1. Open your app.
2. Navigate to the app's **Settings** screen (or similar screens) where it has the option to integrate with Health Connect.
3. Choose to integrate with Health Connect.

### Expected results

![Integrate with Health Connect through your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-02-02.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The app's **Settings** screen (or similar screens) must have a feature to integrate with Health Connect.
- Tapping the option to integrate with Health Connect must lead you to the Health Connect app.


FAIL for *any* of the following reasons:

- There's no feature to integrate with Health Connect in the app's **Settings** screen or any similar screens.
- Tapping the option to integrate with Health Connect doesn't lead you to the Health Connect app.

## 02-03: Unlink from Health Connect through your app


| Details ||
|---|---|
| **Description** | When a user decides to stop using Health Connect, an app must have a way to unlink from Health Connect. <br /> It must revoke all permissions through the app, effectively removing integration from Health Connect. |
| **Requirements** | The Health Connect app must be installed on the phone. |
| **Reference** | [`PermissionController.revokeAllPermissions`](https://developer.android.com/reference/androidx/health/connect/client/PermissionController#revokeAllPermissions()) |

<br />

### Steps

1. Open your app.
2. Navigate to the app's **Settings** screen (or similar screens) where it has the option to unlink from Health Connect.
3. Choose to unlink from Health Connect.

### Expected results

![Unlink from Health Connect through your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-02-03.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The app's **Settings** screen (or similar screens) must have a feature to unlink from Health Connect.
- All permissions listed under your app must be revoked.


FAIL for *any* of the following reasons:

- There's no way to unlink from Health Connect in the app's **Settings** screen or any similar screens.
- At least one permission listed under your app isn't revoked.

## 03: Access Health Connect app through your app settings


| Details ||
|---|---|
| **Description** | When a user decides to manage Health Connect, the app must have a way to direct users to the Health Connect app. |
| **Requirements** | <br /> - The Health Connect app must be installed on the phone. - Your app must be integrated with Health Connect. |
| **Notes** | This is an optional user interface feature, as users can also directly access Health Connect through the phone's **Settings** , the **Quick Settings** when configured, or through the Google Play store. |
| **Reference** | [Option within your settings menu](https://developer.android.com/guide/health-and-fitness/health-connect/design/permissions-and-data#option_within_your_settings_menu) |

<br />

### Steps

1. Open your app.
2. Navigate to the app's **Settings** screen (or similar screens) where it has the option to access the Health Connect app.
3. Choose to access or manage Health Connect.

### Expected results

![Access Health Connect from your app's settings](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-03.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The app's **Settings** screen (or similar screens) must have a way to access the Health Connect app.


FAIL for *any* of the following reasons:

- There's no way to access the Health Connect app in the app's **Settings** screen or any similar screens.

## 04-01: Deny permissions


| Details ||
|---|---|
| **Description** | The app must not read or write specific records to Health Connect when a user revokes permission. |
| **Requirements** | <br /> - The Health Connect app must be installed on the phone. - All permissions must be granted prior to testing. |
| **Notes** | <br /> - If your app has a way to reflect denied permissions, check it from there as well. - If your app can still read data from Health Connect, the app must be using a `dataOriginFilter` when calling a `ReadRecordsRequest`. |

<br />

### Steps

1. Open the Health Connect app.
2. Go to **App permissions**.
3. Choose your app.
4. Toggle the **Allow all** switch to deny permissions.
5. When the dialog appears, choose **Remove all**.

### Expected results

![Deny permissions through the Health Connect app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-04-01.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- Under **App permissions** , your app must appear under **Not allowed access**.
- No permissions are granted.
- Those permission changes take effect in your app.
- Your app doesn't crash.


FAIL for *any* of the following reasons:

- Under **App permissions** , your app didn't appear under **Not allowed access** and is still under **Allowed access**.
- At least one permission is still left granted.
- Those permission changes didn't take effect in your app.
- Your app crashed.

## 04-02: Allow permissions


| Details ||
|---|---|
| **Description** | The app must read or write specific records to Health Connect when a user grants permission. |
| **Requirements** | <br /> - The Health Connect app must be installed on the phone. - All permissions must be revoked prior to testing. |
| **Notes** | If your app has a way to reflect allowed permissions, check it from there as well. |

<br />

### Steps

1. Open the Health Connect app.
2. Go to **App permissions**.
3. Choose your app.
4. Toggle the **Allow all** switch to allow permissions.

### Expected results

![Allow permissions through the Health Connect app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-04-02.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- Under **App permissions** , your app must appear under **Allowed access**.
- All permissions are granted.
- Those permission changes take effect in your app.
- Your app doesn't crash.


FAIL for *any* of the following reasons:

- Under **App permissions** , your app didn't appear under **Allowed access** and is still under **Not allowed access**.
- At least one permission is still left revoked.
- Those permission changes didn't take effect in your app.
- Your app crashed.

## 05: Write data to Health Connect


| Details ||
|---|---|
| **Description** | Part of the common workflow is to write data to the Health Connect datastore. |
| **Requirements** | The **Write permission** of the required data type must be granted for your app. |
| **Reference** | [Write data](https://developer.android.com/health-and-fitness/health-connect/write-data) |

<br />

### Steps

1. Log a value for the required data type using your app.
2. Open the Health Connect app.
3. Choose **Data and access**.
4. Choose the category where your required data type belongs.
5. Select the required data type.
6. Under **Manage data** , choose **See all entries**.

### Expected results

![Write data through your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-05.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The new data is reflected in the Health Connect app.


FAIL for *any* of the following reasons:

- The new data isn't reflected in the Health Connect app.

## 06: Read data from Health Connect


| Details ||
|---|---|
| **Description** | Part of the common workflow is to read data from the Health Connect datastore. |
| **Requirements** | <br /> - You have installed the [Health Connect Toolbox app](https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox). - The **Write permission** of the required data type must be granted for the Health Connect Toolbox app. - The **Read permission** of the required data type must be granted for your app unless you're using your app's package name for your `dataOriginFilter`. |
| **Reference** | [Read raw data](https://developer.android.com/health-and-fitness/health-connect/read-data) |

<br />

### Steps

1. Log a value for the required data type using the Health Connect Toolbox app.
2. Check the Health Connect app to see if it is reflected.
   1. Open the Health Connect app.
   2. Choose **Data and access**.
   3. Choose the category where the required data type belongs.
   4. Select the required data type.
   5. Under **Manage data** , choose **See all entries**.
3. Read the data using your app.

### Expected results

![Read data from your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-06.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The new data must reflect in both the Health Connect app and your app.


FAIL for *any* of the following reasons:

- The new data didn't reflect in either the Health Connect app or your app.

## 07: Read aggregated data from Health Connect


| Details ||
|---|---|
| **Description** | Part of the common workflow is to read data from the Health Connect datastore. <br /> In most apps, the data is aggregated for purposes such as displaying statistics or charts. |
| **Requirements** | <br /> - You have installed the [Health Connect Toolbox app](https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox). - The **Write permission** of the required data type must be granted for the Health Connect Toolbox app. - The **Read permission** of the required data type must be granted for your app unless you're using your app's package name for your `dataOriginFilter`. |
| **Notes** | Aggregated data may vary depending on the values used in the `timeRangeFilter` and `dataOriginFilter`. |
| **Reference** | [Read aggregated data](https://developer.android.com/health-and-fitness/health-connect/aggregate-data) |

<br />

### Steps

1. Log multiple values for the required data type in the Health Connect Toolbox app.
2. Check the Health Connect app to see if they are reflected.
   1. Open the Health Connect app.
   2. Choose **Data and access**.
   3. Choose the category where the required data type belongs.
   4. Select the required data type.
   5. Under **Manage data** , choose **See all entries**.
3. Read and aggregate the data using your app.

### Expected results

![Read aggregated data from your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-07.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The new values are reflected in the Health Connect app.
- The aggregated values are reflected in your app.


FAIL for *any* of the following reasons:

- The new values aren't reflected in the Health Connect app.
- The aggregated values aren't reflected in your app.

## 08: Update data from Health Connect


| Details ||
|---|---|
| **Description** | Part of the common workflow is to update data from the Health Connect datastore. <br /> Updates are necessary in scenarios such as syncing and importing data. |
| **Requirements** | The **Write permission** of the required data type must be granted for your app. |
| **Reference** | [Update data](https://developer.android.com/health-and-fitness/health-connect/write-data#update-data) |

<br />

### Steps

1. Update the values of the required data type using your app.
2. Open the Health Connect app.
3. Choose **Data and access**.
4. Choose the category where the required data type belongs.
5. Select the required data type.
6. Under **Manage data** , choose **See all entries**.

### Expected results

![Update data through your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-08.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The updated values are reflected in the Health Connect app.


FAIL for *any* of the following reasons:

- The updated values aren't reflected in the Health Connect app.

## 09: Display updated data from Health Connect


| Details ||
|---|---|
| **Description** | Part of the common workflow is to update data from the Health Connect datastore. <br /> There are viewing apps that can display data coming from other source apps. The source apps store data in Health Connect, while the viewing apps pull data from there. |
| **Requirements** | <br /> - You have installed the [Health Connect Toolbox app](https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox). - The **Write permission** of the required data type must be granted for the Health Connect Toolbox app. - The **Read permission** of the required data type must be granted for your app unless you're using your app's package name for your `dataOriginFilter`. |

<br />

### Steps

1. Update the values of your chosen data type using the Health Connect Toolbox app.
2. Check the Health Connect app to see if they are reflected.
   1. Open the Health Connect app.
   2. Choose **Data and access**.
   3. Choose the category where the required data type belongs.
   4. Select the required data type.
   5. Under **Manage data** , choose **See all entries**.
3. Read the data using your app.

### Expected results

![Display updated data from your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-09.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The updated values are reflected in both the Health Connect app and your app.


FAIL for *any* of the following reasons:

- The updated values aren't reflected in either the Health Connect app or your app.

## 10: Delete data from Health Connect


| Details ||
|---|---|
| **Description** | Part of the common workflow is to delete data from the Health Connect datastore. |
| **Requirements** | The **Write permission** of the required data type must be granted for your app. |
| **Reference** | [Delete data](https://developer.android.com/health-and-fitness/health-connect/delete-data) |

<br />

### Steps

1. Delete the values of the required data type using your app.
2. Open the Health Connect app.
3. Choose **Data and access**.
4. Choose the category where the required data type belongs.
5. Select the required data type.
6. Under **Manage data** , choose **See all entries**.

### Expected results

![Delete data through your app](https://developer.android.com/static/health-and-fitness/health-connect/test/images/hc-10.png)

### Pass and fail conditions


PASS if *all* of the following conditions are met:

- The deleted values aren't reflected in the Health Connect app.


FAIL for *any* of the following reasons:

- The deleted values are still reflected in the Health Connect app.