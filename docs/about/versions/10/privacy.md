---
title: Privacy in Android 10  |  Platform  |  Android Developers
url: https://developer.android.com/about/versions/10/privacy
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Platform](https://developer.android.com/about)
* [Releases](https://developer.android.com/about/versions)

Stay organized with collections

Save and categorize content based on your preferences.




### Privacy in Android 10

Android 10 includes extensive changes to protect privacy and give users control
— from improved system UI to stricter
permissions and restrictions on what data apps can use.

All developers should review the privacy features and test their apps. Impacts
can vary based on each app's core functionality, targeting, and other factors.

[Read all](/about/versions/10/privacy/changes)

## Top privacy changes

|  | Privacy change | Apps affected | Mitigation strategy |
| --- | --- | --- | --- |
|  | **Scoped storage** Filtered view into external storage, giving access to app-specific files and media collections | Apps that access and share files in external storage | Work in app-specific directory and media collection directories  [Learn more](/about/versions/10/privacy/changes#scoped-storage) |
|  | **More user control over location permissions** Foreground-only permission that gives users more control over app access to device location | Apps that request the user's location while in the background | Ensure graceful degradation in the absence of background location updates Use permission introduced in Android 10 to access location in the background  [Learn more](/about/versions/10/privacy/changes#app-access-device-location) |
|  | **Background activity starts** Restrictions on launching activities from the background | Apps that launch activities without user interaction | Use notification-triggered activities  [Learn more](/about/versions/10/privacy/changes#background-activity-starts) |
|  | **Non-resettable hardware identifiers** Restrictions on accessing device serial and IMEI | Apps that access device serial or IMEI | Use an identifier that the user can reset  [Learn more](/about/versions/10/privacy/changes#non-resettable-device-ids) |
|  | **Permission for wireless scanning** Access to some Wi-Fi, Wi-Fi Aware, and Bluetooth scanning methods requires fine location permission | Apps using Wi-Fi and Bluetooth APIs | Request `ACCESS_FINE_LOCATION` permission for related use cases  [Learn more](/about/versions/10/privacy/changes#location-telephony-bluetooth-wifi) |

## More privacy changes

### Identifiers and data

New restrictions on hardware identifiers such as IMEI,
serial number, MAC, and similar data.

* [**Removal of contacts affinity**](/about/versions/10/privacy/changes#contacts-affinity)
* [**MAC address randomization**](/about/versions/10/privacy/changes#randomized-mac-addresses)
* [**Restriction on access to /proc/net file system**](/about/versions/10/privacy/changes#proc-net-filesystem)
* [**Restriction on non-resettable device identifiers**](/about/versions/10/privacy/changes#non-resettable-device-ids)
* [**Limited access to clipboard data**](/about/versions/10/privacy/changes#clipboard-data)
* [**Protection of USB device serial number**](/about/versions/10/privacy/changes#usb-serial)

### Camera and connectivity

Stronger protections for camera metadata, connectivity APIs.

* [**Restriction on access to camera details and metadata**](/about/versions/10/privacy/changes#camera-info)
* [**Restriction on enabling and disabling Wi-Fi**](/about/versions/10/privacy/changes#enable-disable-wifi)
* [**Restriction on direct access to configured Wi-Fi networks**](/about/versions/10/privacy/changes#configure-wifi)
* [**Some telephony, Bluetooth, Wi-Fi APIs require FINE location permission**](/about/versions/10/privacy/changes#location-telephony-wifi-bluetooth)

### Permissions

Changes to the permissions model and requirements.

* [**Restricted access to screen contents**](/about/versions/10/privacy/changes#screen-contents)  
  * [**User-facing permission check on legacy apps**](/about/versions/10/privacy/changes#user-permission-legacy-apps)  
    * [**Physical activity recognition**](/about/versions/10/privacy/changes#physical-activity-recognition)  
      * [**Permission groups removed from UI**](/about/versions/10/privacy/changes#permission-groups-removed)

## Get started with privacy updates

1. **Review the privacy features** — Learn about [what's changing](/about/versions/10/privacy/changes)
   and assess your app.
2. **Test your app on Android 10** —
   [Get Android 10](/about/versions/10/get)
   as soon as possible, test, migrate as needed.
3. **Update your app** — Targeting 29 if possible, test
   with users via beta channels or other groups.

## Latest news and videos