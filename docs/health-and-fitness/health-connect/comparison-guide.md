---
title: https://developer.android.com/health-and-fitness/health-connect/comparison-guide
url: https://developer.android.com/health-and-fitness/health-connect/comparison-guide
source: md.txt
---

# Health Connect comparison guide

With many health, fitness, and wellness apps running on Android devices, users often need to switch between platforms to manage their data. Health Connect solves this by providing a single place for Android users to manage access to their health and fitness data, offering granular control and helping developers create innovative health experiences.

This guide helps you choose which API to integrate with and when.

## Health Connect

Consider integrating with[Health Connect](https://developer.android.com/guide/health-and-fitness/health-connect)if you're an Android mobile developer.

Health Connect unifies data across Android's portfolio of devices and apps into an ecosystem, providing a common health platform for Android developers. Health Connect provides an API for reading and writing the user's health and fitness data, standardizes the data schema upon storage, and centralizes permissions control.

We**don't**recommend migrating to Health Connect if you're an existing Google Fitbit Web API developer. However, we do recommend migrating to Health Connect if you're already integrated with the Fit APIs.
| **Note:** The Google Fit APIs have been deprecated and we plan to support them until**2026** . See[Migration guide](https://developer.android.com/guide/health-and-fitness/health-connect/migrate/migration-guide)for instructions on migrating to Health Connect.

### Health Connect distinctives

The following is a summary of how Health Connect differs with the Fit Android API:

- **Intended audience:**Health Connect is intended for Android mobile developers.
- **Device-centric:**Users access and store data on their devices.
- **No account needed:**The data is not associated with a Google Account.
- **Built-in permissions:**Health and fitness data management is centralized.

### Integrate with Health Connect

The following resources help you integrate with and learn more about Health Connect:

- **Integrate:** See[Get started](https://developer.android.com/guide/health-and-fitness/health-connect/develop/get-started)to start integrating with Health Connect.
- **Learn more:** Check out the following[video](https://www.youtube.com/watch?v=d14GVcnbTeo)to learn more about Health Connect.
- **Resources:** Remember to check out the rest of the[documentation](https://developer.android.com/guide/health-and-fitness/health-connect).

## Fitbit Web API

Consider integrating with the[Fitbit Web API](https://dev.fitbit.com/build/reference/web-api/)if you want to integrate with the Fitbit ecosystem.

The Fitbit Web API is a platform-agnostic interface to integrate with the Fitbit ecosystem. It gives users the ability to store, share, and manage their data directly in the cloud. In the Fitbit Web API, the user's data is tied to their Fitbit account instead of their device. This means the Fitbit Web API is account-centric instead of device-centric.

### Fitbit Web API distinctives

The following is a summary of how the Fitbit Web API is different to Health Connect:

- **Intended audience:**The Fitbit Web API is intended for Fitbit developers, enterprise developers, and researchers.
- **Account-centric:**The data is associated with the user's Fitbit account.
- **Data ecosystem:**The Fitbit Web API can access data recorded by Fitbit watches and scales. You can manually input data using the API. Health Connect can read and write data from various apps, and is intended to be the common interface across Android apps to store and share health and fitness data.
- **Data storage:**Users store data in the cloud instead of their devices.
- **Interface:**The Fitbit Web API has a platform-agnostic interface.
- **Permissions:**Users grant access through OAuth.
- **Access to data:**Users can access data in near real-time.

### Integrate with the Fitbit Web API

The following resources help you integrate with and learn more about the Fitbit Web API:

- Integrate: See[Getting started](https://dev.fitbit.com/build/reference/web-api/developer-guide/getting-started/)to start using the Fitbit Web API.
- Resources: See[Fitbit developer guide](https://dev.fitbit.com/build/reference/web-api/developer-guide/).

## Google Fit REST API

| **Caution:** The Fit REST API will**only be supported until 2026.**We recommend integrating with Health Connect or the Fitbit Web API.

The Google Fit REST API unifies data from multiple sources, including Google Fit, allowing users to store, share, and manage their data in the cloud. Because data is tied to a user's Google Account rather than their device, the platform is account-centric rather than device-centric.

### Google Fit REST API distinctives

The following is a summary of how the Google Fit REST API is different to Health Connect.

- **Intended audience:**The Google Fit REST API is intended for non-Android mobile developers, enterprise developers and researchers.
- **Account-centric:**The data is associated with the user's Google Account.
- **Data storage:**Users store data in the cloud instead of their devices.
- **Interface:**The Google Fit REST API has a platform-agnostic interface.
- **Permissions:**Users grant access through OAuth.
- **Access to data:**Users can access data in near real-time.

### Integrate with the Google Fit REST API

The following resources help you integrate with and learn more about the Google Fit REST API:

- **Integrate:** See[Get started](https://developers.google.com/fit/rest/v1/get-started)to start using the Google Fit REST API.
- **Resources:** Check out the[Google Fit guides](https://developers.google.com/fit/overview).

## Frequently Asked Questions

The following questions provide context on our plans and what you can do in the meantime.

### Q: Will the Fit Android API eventually be turned down?

Yes, we're aiming to turn down the Google Fit Android API in**2026**. This is to give our developers enough time to successfully migrate from the Fit Android APIs to Health Connect. It also allows us to further develop Health Connect and make the platform even more comprehensive and effective for Android developers and their users.

### Q: I'm integrated with the Fit Android API. Should I migrate to Health Connect?

Yes. Health Connect is a common Android API for storing and sharing health and fitness data from multiple apps and devices on the user's mobile device. That data includes Google Fit. Health Connect is our new way of syncing data with Google Fit and Google Fit data is written to Health Connect if the user chooses to do this.

The following are some of Health Connect's components:

- API for accessing health and wellness data stored on-device.
- Single interface to read or write data across Android, including data from Google Fit, Fitbit, Samsung Health and more partners.
- Standardized data schema.
- Granular user permission controls.
- Centralized data management controls.