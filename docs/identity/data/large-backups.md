---
title: Back up large amounts of data with the Android Large Backups API Program  |  Identity  |  Android Developers
url: https://developer.android.com/identity/data/large-backups
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [Security](https://developer.android.com/security)
* [Identity](https://developer.android.com/identity)
* [Guides](https://developer.android.com/identity/credential-manager)

# Back up large amounts of data with the Android Large Backups API Program Stay organized with collections Save and categorize content based on your preferences.



The standard [Android Auto Backup](/identity/data/backup) lets apps back up a maximum of 25 MB of
user data to cloud storage. However, for apps requiring more extensive backup
capabilities—such as user-generated media and large-scale datasets—the Android
Large Backups API provides an alternative.

The Large Backups API lets developers securely back up large amounts of data,
with a per-file limit of 50 GB, but limits depending on a user's Google One
storage. Data backed up using the Android Large Backups API counts toward the
user's personal Google One storage quota. The per-user limit is based on their
remaining available Google One storage space.

## Key benefits

The Large Backups API provides several advantages for apps with large amounts of
data:

* **Seamless user experience:** Maintain the user experience by automatically
  backing up data to cloud storage.
* **Reliable data recovery:** Lets users restore their app data to a previous
  state in case of device loss, damage, or factory resets.
* **Seamless data migration:** Lets you effortlessly migrate user data to new
  devices.
* **Scalability:** Accommodates the growing data needs of your app and
  increasing user bases.
* **Abstracted backup logic:** The API abstracts settings, for example,
  backing up over mobile data and backup frequency. You can still implement
  fine-grained controls in your app.
* **Extended session duration:** Supports prolonged data transfer windows to
  safely back up large datasets. This is subject to system-defined inactivity
  timeouts.

## Compare Large Backups API with Auto Backup

The Large Backups API differs significantly in limits and capabilities compared
to the Auto Backup framework.

| Feature area | Large Backups API | Auto Backup |
| --- | --- | --- |
| **Total backup size limit** | None | 25 MB |
| **Per-file size limit** | Up to 50 GB | 25 MB |
| **Storage impact** | Counts toward user's Google One quota | Counts toward user's Google One quota |
| **Transfer method** | Cloud only | Cloud or device-to-device transfer |
| **File control** | You get granular per-file control over scheduling, prioritization, and order. For example, you can back up larger files at night and smaller files at other times. | You define which files are included for backup. |
| **Restore from settings** | Apps can initiate on-demand restore at any point in the app's lifecycle for all or part of the backup data. | Only permits user-initiated backups after the initial device setup. Availability might vary by device and the app's [`BackupAgent`][2]. |

## Program eligibility and application process

Access to the Large Backups API is **by approval only**. The program is targeted
at large-scale app developers, and apps are evaluated based on their data backup
practices to confirm that the stored data is highly valuable to users and that
the backup process is efficient.

To inquire about and request access to the API, you must [file an application
ticket](https://issuetracker.google.com/issues/new?component=1957795&template=2221282).

To confirm the Android Large Backups API is used effectively and responsibly,
the following criteria for eligibility have been established:

* **Significant user base:** Typically, this is for apps with a large-scale
  user base (for example, reaching 100 million Monthly Active Users (MAU)) or
  those demonstrating a critical technical requirement for high-volume data
  egress. Alternatively, apps with a rapidly growing user base that anticipate
  exceeding this threshold in the near future might also be considered.
* **Data volume and type:** An average of more than 1 GB of live user backup
  data per app per user. These are primarily apps that handle large volumes of
  user-generated content, such as the following:
  + Messaging app media (photos, videos, audio).
  + Note-taking apps containing user-created media, or rich text.
  + Apps with large databases containing user-created content.
* The data you back up must be essential to the user experience and not easily
  reproducible (for example, user-created text, media, or documents).
* Apps that back up large amounts of application cache or assets (for example,
  game sprites) won't be considered.
* **Backup frequency and data change rate:**
  + Apps must not have a requirement to back up data more frequently than
    once per day, nor less frequently than once per month.
  + For data that changes frequently (for example, chat databases), the app
    must implement efficient update mechanisms. This includes techniques
    such as byte-level diffing and uploading only the changes rather than
    the entire dataset. This minimizes bandwidth consumption and device
    resource usage.
* **Data security and privacy:**
  + Apps must adhere to stringent data security and privacy standards,
    including complying with all applicable data privacy regulations (for
    example, General Data Protection Regulation (GDPR) and California
    Consumer Privacy Act (CCPA)).
  + Apps that use end-to-end encryption for user data are eligible provided
    that they implement backup procedures that meet Google's standards for
    efficiency and security.

These criteria are designed to:

* Prioritize apps whose users will benefit most from the Large Backups API.
* Confirm the API is tested with a diverse range of high-volume use cases.
* Safeguard user data and maintain the integrity of the backup ecosystem.

**Important:** Google reserves the right to implement rate limiting, traffic quotas,
or transition this API to a fee-based model. Violation of the terms of service
in the application request or the technical principles outlined in this document
might result in the suspension or revocation of API access. Except in cases of
emergency or security risk, Google will try to provide reasonable notice and
engage in good-faith discussions prior to implementing restrictive measures.