---
title: https://developer.android.com/health-and-fitness/health-connect/migration/fit/faq
url: https://developer.android.com/health-and-fitness/health-connect/migration/fit/faq
source: md.txt
---

This document provides answers to frequently asked questions about migrating
from Google Fit APIs to Android Health APIs.

## Who does this migration impact?

All developers who are using the Google Fit APIs and Google Fit REST APIs.

## What's changing?

- The Google Fit APIs, including the Google Fit REST API, will be deprecated in 2026.
- Developers cannot sign up to use these APIs as of May 1, 2024.

## How do I get started?

To provide a smooth transition for your users, review the
[Migration guide](https://developer.android.com/guide/health-and-fitness/health-connect/migrate/migration-guide).

## What can I do with my Google Fit APIs during the migration period?

If you are a developer using Google Fit APIs for Android, we recommend migrating
to Android Health APIs now to help provide uninterrupted service for your users.
Android Health APIs offer several advantages over the Fit APIs, including:

- **Recording steps** : Android Health will provide the [Recording API on mobile](https://developer.android.com/health-and-fitness/guides/recording-api), which doesn't require a Google user account or the need for you to request access to API scopes. It's also a more battery-efficient way to retrieve step count data. The Recording API on Mobile is launched with steps.
- **Health Connect** : By integrating with [Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect), your Android app can access data from a growing ecosystem of apps with just one connection. Plus, data is stored on-device, allowing the user to be in full control of their data.

## What will happen to the Google Fit APIs after the migration period?

Google Fit APIs will no longer be available for use. After the migration
period, you should have already [migrated to Health Connect](https://developer.android.com/guide/health-and-fitness/health-connect/migrate/migration-guide) or
other Android Health APIs.

## What will happen to the Google Fit REST APIs after the migration period?

There is no alternative to the Fit REST API.

We encourage Fit REST API users to migrate to the Android Health APIs. See
which one best fits your needs and users:

- **Health Connect**: Health Connect unifies data across Android's portfolio of devices and apps into an ecosystem, providing a common health platform for Android developers. Health Connect provides an API for reading and writing the user's health and fitness data, standardizes the data schema upon storage, and centralizes permissions control.
- **Fitbit Web API**: The Fitbit Web API is a platform-agnostic interface to integrate with the Fitbit ecosystem. It gives users the ability to store, share, and manage their data directly in the cloud. In the Fitbit Web API, the user's data is tied to their Fitbit account instead of their device. This means the Fitbit Web API is account-centric instead of device-centric.

Check out the [Health Connect comparison guide](https://developer.android.com/health-and-fitness/guides/health-connect/migrate/comparison-guide) for more
details.

## How do I get help?

If you find a bug or need help with the migration, submit your feedback using
our [issue tracker](https://issuetracker.google.com/issues/new?component=1676744&template=2072671).