---
title: https://developer.android.com/work/dpc/dedicated-devices
url: https://developer.android.com/work/dpc/dedicated-devices
source: md.txt
---

# Dedicated devices overview

Android includes APIs to manage devices that are dedicated to a specific purpose.
This developer's guide introduces these APIs. If you're an enterprise mobility
management (EMM) developer or solution integrator, read this guide to get
started.

## Where are dedicated devices used?

*Dedicated devices* (formerly called corporate-owned single-use, or COSU) are
fully managed devices that serve a specific purpose. Android provides APIs that
can help you create devices that cater to employee- and customer-specific needs:

- **Employee-facing:** Inventory management, field service management, transport and logistics
- **Customer-facing:** Kiosks, digital signage, hospitality check-in

## Dedicated device features

Android includes APIs to help people using dedicated devices focus
on their tasks. You typically call these APIs from a custom home app that you
develop. Your custom home app can use some, or all, of the following APIs:

- Run the system in an immersive, kiosk-like fashion where devices are locked to an allowlisted set of apps using [lock task
  mode](https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode).
- Share a device between multiple users (such as shift workers or public-kiosk users) by [managing ephemeral and secondary
  users](https://developer.android.com/work/dpc/dedicated-devices/multiple-users).
- Avoid devices downloading the same app again for each temporary user by [caching app packages](https://developer.android.com/work/dpc/dedicated-devices/cookbook#cache-apps).
- Suspend over-the-air (OTA) system updates over critical periods by [freezing
  the operating system version](https://developer.android.com/work/dpc/system-updates#freeze-periods).

To call these APIs, apps need to be the admin of a fully managed
device---explained in the following section.

## Managed devices

Because dedicated devices might be left unattended or used in critical tasks,
you need to secure the device. To prevent misuse, dedicated devices are *fully
managed* and owned by an [admin component](https://developer.android.com/reference/android/app/admin/DeviceAdminReceiver) (the admin component typically
manages the users too). Fully managed deployments are for company-owned devices
that are used exclusively for work purposes. To learn more about Android device
management, read the Android Enterprise [Overview](https://developers.google.com/android/work/overview) guide.

Depending on your solution's needs and your business goals, you can manage the
device in one of the following ways:

- [Develop your own device policy controller (DPC)](https://developer.android.com/work/dpc/build-dpc), combining it with a [custom home app](https://developer.android.com/work/dpc/dedicated-devices#features).
- Use the [Android Management
  API](https://developers.google.com/android/management/) to manage the device and any custom apps.
- Use a [third-party EMM
  solution](https://androidenterprisepartners.withgoogle.com/emm/) that supports lock task mode and other dedicated device features.

## Testing

If you're planning to support a third-party EMM, develop an end-to-end testing
plan using the EMM's solution.

We also provide the following resources, which you can
use to create your own development or test environment:

- [Test DPC](https://play.google.com/store/search?q=testdpc) app on Google Play
- [Dedicated device source
  code](https://github.com/googlesamples/android-testdpc/tree/master/src/main/java/com/afwsamples/testdpc/cosu) (Test DPC) on GitHub

While you're still developing, you can [set your app as the
admin](https://developer.android.com/work/dpc/dedicated-devices/cookbook#dev-setup) of a fully managed device
using the Android Debug Bridge (ADB).

## Provision dedicated devices

When you've finished developing your solution, you're ready to *provision*
Android devices, or set up the devices for management. To provision a device,
complete the following steps:

1. Factory reset the device.
2. Enroll the device. We recommend [using a QR
   code](https://developers.google.com/android/work/prov-devices#qr_code_method)
   that contains a provisioning config for device. An IT admin can then scan the
   code to provision the device.

   If you cannot use a QR code, you can enroll devices through [other
   methods](https://developers.google.com/android/work/overview#device_and_work_profile_provisioning),
   such as NFC bumping or by entering an identifier.

## Documentation

## Additional resources

To learn more about getting started with dedicated devices, read the following
documents:

- [Android Enterprise
  overview](https://developers.google.com/android/work/overview) that introduces device management.
- [Build a device policy controller](https://developer.android.com/work/dpc/build-dpc) explains how to develop a DPC.
- [Dedicated devices cookbook](https://developer.android.com/work/dpc/dedicated-devices/cookbook) gives examples for features typical of dedicated devices.