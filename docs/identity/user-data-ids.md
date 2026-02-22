---
title: https://developer.android.com/identity/user-data-ids
url: https://developer.android.com/identity/user-data-ids
source: md.txt
---

This document provides guidance for selecting appropriate identifiers for your
app based on your use case.

For a general look at Android permissions, see [Permissions
overview](https://developer.android.com/training/articles/user-data-overview). For specific best
practices for working with Android permissions, see [App permissions best
practices](https://developer.android.com/training/permissions/usage-notes).

## Best practices for working with Android identifiers

To protect the privacy of your users, use the most restrictive identifier that
satisfies your app's use case. In particular, follow these best practices:

1. ***Choose user-resettable identifiers whenever possible.*** Your app can achieve most of its use cases even when it uses identifiers other than non-resettable hardware IDs.
2. ***Avoid using hardware identifiers.*** In most use cases, you can avoid
   using hardware identifiers, such as International Mobile Equipment Identity
   (IMEI), without limiting required functionality.

   Android 10 (API level 29) adds restrictions for non-resettable identifiers,
   which include both IMEI and serial number. Your app must be a [device or
   profile owner
   app](https://source.android.com/devices/tech/admin/managed-profiles#device_administration),
   have [special carrier
   permissions](https://source.android.com/devices/tech/config/uicc), or have
   the `READ_PRIVILEGED_PHONE_STATE` privileged permission in order to access
   these identifiers.
3. ***Only use an Advertising ID for user profiling or ads use cases.*** When
   using an [Advertising ID](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient), always [respect users' selections regarding
   ad tracking](https://play.google.com/about/monetization-ads/ads/ad-id/). If
   you must connect the advertising identifier to personally-identifiable
   information, do so only with the [explicit consent of the
   user](https://support.google.com/googleplay/android-developer/answer/11150561).

4. ***Don't bridge Advertising ID resets.***

5. ***Use a Firebase installation ID (FID) or a privately stored GUID whenever
   possible for all other use cases, except for payment fraud prevention and
   telephony.*** For the vast majority of non-ads use cases, an FID or GUID
   should be sufficient.

6. ***Use APIs that are appropriate for your use case to minimize privacy
   risk.*** Use the [DRM API](https://source.android.com/devices/drm) for
   high-value content protection and the
   [Play Integrity APIs](https://developer.android.com/google/play/integrity/overview) for abuse protection.
   The Play Integrity APIs are the easiest way to determine whether a device is
   genuine without incurring privacy risk.

The remaining sections of this guide elaborate on these rules in the context of
developing Android apps.

## Work with advertising IDs

The Advertising ID is a user-resettable identifier and is appropriate for ads
use cases. There are some key points to bear in mind, however, when you use this
ID:

***Always respect the user's intention in resetting the advertising ID.***
Don't bridge user resets by using another identifier or fingerprint to link
subsequent Advertising IDs together without
the user's consent. The [Google Play Developer Content
Policy](https://play.google.com/about/developer-content-policy) states the
following:
> *"...if reset, a new advertising identifier must not be connected to a
> previous advertising identifier or data derived from a previous advertising
> identifier without the explicit consent of the user."*

***Always respect the associated Personalized Ads flag.*** Advertising IDs are
configurable in that users can limit the amount of tracking associated with the
ID. Always use the [`AdvertisingIdClient.Info.isLimitAdTrackingEnabled()`](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.Info.html#isLimitAdTrackingEnabled())
method to ensure that you aren't circumventing your users' wishes. The [Google
Play Developer Content
Policy](https://play.google.com/about/developer-content-policy) states the
following:
> *"...you must abide by a user's 'Opt out of interest-based advertising' or
> 'Opt out of Ads Personalization' setting. If a user has enabled this setting,
> you may not use the advertising identifier for creating user profiles for
> advertising purposes or for targeting users with personalized advertising.
> Allowed activities include contextual advertising, frequency capping, conversion
> tracking, reporting and security and fraud detection."*
| **Note:** As part of Google Play services update in late 2021, the advertising ID will be removed when a user opts out of personalization using advertising ID in Android Settings. Any attempts to access the identifier will receive a string of zeros instead of the identifier. See [Play Console Help to learn more](https://support.google.com/googleplay/android-developer/answer/6048248?ref_topic=2364761).

***Be aware of any privacy or security policies associated with SDKs you use that are related to Advertising ID use.***
For example, if you pass `true` into the
[`enableAdvertisingIdCollection()`](https://developers.google.com/android/reference/com/google/android/gms/analytics/Tracker.html#enableAdvertisingIdCollection(boolean))
method from the Google Analytics SDK, make sure to review and adhere to all
applicable [Analytics SDK
policies](https://developers.google.com/analytics/devguides/collection/android/v4/policy).

Also, be aware that the [Google Play Developer Content
Policy](https://play.google.com/about/developer-content-policy.html) requires
that the Advertising ID "must not be connected to personally-identifiable
information or associated with any persistent device identifier (for example:
SSAID, MAC address, IMEI, etc.,)."

As an example, suppose you want to collect information to populate database
tables with the following columns:

|---|---|---|---|
| TABLE-01 ||||
| `timestamp` | `ad_id` | **account_id** | `clickid` |
| TABLE-02 ||||
| **account_id** | `name` | `dob` | `country` |

In this example, the `ad_id` column could be joined to PII via the `account_id`
column in both tables, which would be a violation of the [Google Play Developer
Content Policy](https://play.google.com/about/developer-content-policy), if you
didn't get explicit permission from your users.

Keep in mind that links between Advertiser ID and PII aren't always this
explicit. It's possible to have "quasi-identifiers" that appear in both PII and
Ad ID keyed tables, which also cause problems. For example, assume we change
TABLE-01 and TABLE-02 as follows:

|---|---|---|---|---|
| TABLE-01 |||||
| **timestamp** | `ad_id` | `clickid` | **dev_model** ||
| TABLE-02 |||||
| **timestamp** | `demo` | `account_id` | **dev_model** | `name` |

In this case, with sufficiently rare click events, it's still possible to join
between the Advertiser ID TABLE-01 and the PII contained in TABLE-02 using the
timestamp of the event and the device model.

Although it's often difficult to guarantee that no such quasi-identifiers exist
in a dataset, you can prevent the most obvious join risks by generalizing
unique data where possible. In the preceding example, this would mean reducing
the accuracy of the timestamp so that multiple devices with the same model
appear for every timestamp.

Other solutions include the following:

- ***Not designing tables that explicitly link PII with Advertising IDs*** . In
  the first example above, this would mean not including the `account_id` column
  in TABLE-01.

- ***Segregating and monitoring access control lists for users or roles that have access to both the Advertising ID keyed data and PII***.
  By tightly controlling and auditing the ability to access both sources
  simultaneously (for example, by performing a join between tables), you reduce
  the risk of association between the Advertising ID and PII. Generally speaking,
  controlling access means doing the following:

  1. Keep access control lists (ACLs) for Advertiser ID keyed data and PII disjoint to minimize the number of individuals or roles that are in both ACLs.
  2. Implement access logging and auditing to detect and manage any exceptions to this rule.

For more information on working responsibly with Advertising IDs, see the
[`AdvertisingIdClient`](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient) API reference.

## Work with FIDs and GUIDs

The most straightforward solution to identifying an app instance running on a
device is to use a Firebase installation ID (FID), and this is the recommended
solution in the majority of non-ads use cases. Only the app instance for which
it was provisioned can access this identifier, and it's (relatively) easily
resettable because it only persists as long as the app is installed.

As a result, FIDs provide better privacy properties compared to
non-resettable, device-scoped hardware IDs. For more information, see the
[`firebase.installations`](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/package-summary)
API reference.

In cases where an FID isn't practical, you can also use custom
globally-unique IDs (GUIDs) to uniquely identify an app instance. The simplest
way to do so is by generating your own GUID using the following code:  

### Kotlin

```kotlin
var uniqueID = UUID.randomUUID().toString()
```

### Java

```java
String uniqueID = UUID.randomUUID().toString();
```

Because the identifier is globally unique, it can be used to identify a specific
app instance. To avoid concerns related to linking the identifier across apps,
store GUIDs in internal storage instead of external (shared) storage. For more
information, see the [Data and file storage
overview](https://developer.android.com/guide/topics/data/data-storage) page.


## Don't work with MAC addresses

MAC addresses are globally unique, not user-resettable, and survive factory
resets. For these reasons, to protect user privacy, on Android versions 6 and
higher, access to MAC addresses is restricted to system apps. Third-party apps
can't access them.

### MAC address availability changes in Android 11

On apps targeting Android 11 and higher, MAC randomization for Passpoint
networks is per Passpoint profile, generating a unique MAC address based on the
following fields:

- Fully-qualified domain name (FQDN)
- Realm
- Credential, based on the credential used in the Passpoint profile:
  - User credential: user name
  - Certificate credential: cert and cert type
  - SIM credential: EAP type and IMSI

In addition, non-privileged apps can't access the device's MAC address; only
network interfaces with an IP address are visible. This impacts the
[`getifaddrs()`](https://android.googlesource.com/platform/bionic/+/master/libc/include/ifaddrs.h#83)
and
[`NetworkInterface.getHardwareAddress()`](https://developer.android.com/reference/java/net/NetworkInterface#getHardwareAddress())
methods, as well as sending `RTM_GETLINK` Netlink messages.

The following is a list of the ways that apps are affected by this change:

- `NetworkInterface.getHardwareAddress()` returns null for every interface.
- Apps cannot use the `bind()` function on `NETLINK_ROUTE` sockets.
- The `ip` command does not return information about interfaces.
- Apps cannot send `RTM_GETLINK` messages.

Note that most developers should use the higher-level APIs of
[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) rather than
lower-level APIs like
[`NetworkInterface`](https://developer.android.com/reference/java/net/NetworkInterface),
[`getifaddrs()`](https://android.googlesource.com/platform/bionic/+/master/libc/include/ifaddrs.h#83),
or Netlink sockets. For example, an app that needs up-to-date information on the
current routes can get this information by listening for network changes using [`ConnectivityManager.registerNetworkCallback()`](https://developer.android.com/reference/android/net/ConnectivityManager#registerNetworkCallback(android.net.NetworkRequest,%20android.net.ConnectivityManager.NetworkCallback))
and calling the network's associated
[`LinkProperties.getRoutes()`](https://developer.android.com/reference/android/net/LinkProperties#getRoutes()).

## Identifier characteristics

The Android OS offers a number of IDs with different behavior characteristics.
Which ID you should use depends on how the following characteristics work with
your use case. These characteristics also come with privacy implications,
however, so it's important to understand how these characteristics interact with
each other.

### Scope

Identifier scope explains which systems can access the identifier. Android
identifier scope generally comes in three flavors:

- *Single app*: The ID is internal to the app and not accessible to other apps.
- *Group of apps*: The ID is accessible to a pre-defined group of related apps.
- *Device*: The ID is accessible to all apps installed on the device.

The wider the scope granted to an identifier, the greater the risk of it being
used for tracking purposes. Conversely, if an identifier can only be accessed by
a single app instance, it cannot be used to track a device across transactions
in different apps.

### Resettability and persistence

Resettability and persistence define the lifespan of the identifier and explain
how it can be reset. Common reset triggers include: in-app resets, resets via
System Settings, resets on launch, and resets on installation. Android
identifiers can have varying lifespans, but the lifespan is usually related
to how the ID is reset:

- *Session-only*: A new ID is used every time the user restarts the app.
- *Install-reset*: A new ID is used every time user uninstalls and reinstalls the app.
- *FDR-reset*: A new ID is used every time the user factory-resets the device.
- *FDR-persistent*: The ID survives factory reset.

Resettability gives users the ability to create a new ID that is disassociated
from any existing profile information. The longer, and more reliably, an
identifier persists, such as one that persists across factory resets, the
greater the risk that the user may be subjected to long-term tracking. If the
identifier is reset upon app reinstall, this reduces the persistence and
provides a means for the ID to be reset, even if there is no explicit user
control to reset it from within the app or System Settings.

### Uniqueness

Uniqueness establishes the likelihood of collisions; that is, that identical
identifiers exist within the associated scope. At the highest level, a globally
unique identifier never has a collision, even on other devices or apps.
Otherwise, the level of uniqueness depends on the entropy of the identifier and
the source of randomness used to create it. For example, the chance of a
collision is much higher for random identifiers seeded with the calendar date of
installation (such as `2019-03-01`) than for identifiers seeded with the Unix
timestamp of installation (such as `1551414181`).

In general, user account identifiers can be considered unique. That is, each
device/account combination has a unique ID. On the other hand, the less unique
an identifier is within a population, the greater the privacy protection because
it's less useful for tracking an individual user.

### Integrity protection and non-repudiability

You can use an identifier that is difficult to spoof or replay to prove that the
associated device or account has certain properties. For example, you could
prove that the device isn't a virtual device used by a spammer.
Difficult-to-spoof identifiers also provide *non-repudiability*. If the device
signs a message with a secret key, it's difficult to claim that someone else's
device sent the message. Non-repudiability could be something a user wants, such
as when authenticating a payment, or it could be an undesirable property, such
as when they send a message they regret.

## Common use cases and the appropriate identifier to use

This section provides alternatives to using hardware IDs, such as IMEI. Using
hardware IDs is discouraged because the user cannot reset them, and they're
scoped to the device. In many cases, an app-scoped identifier would suffice.

### Accounts


#### Carrier status

*In this case, your app interacts with the device's phone and texting
functionality using a carrier account.*

**Recommended identifier to use:** IMEI, IMSI, and Line1

**Why this recommendation?**

Leveraging hardware identifiers is acceptable if it's required for
carrier-related functionality. For example, you could use these identifiers to
switch between cellular carriers or SIM slots, or to deliver SMS messages over
IP (for Line1) - SIM-based user accounts. For unprivileged apps, however, we
recommend using an account sign-in to retrieve user device information
server-side. One reason for this is that, in Android 6.0 (API level 23) and
higher, these identifiers can only be used via a runtime permission. Users might
toggle off this permission, so your app should handle these exceptions
gracefully.

#### Mobile subscription status

*In this case, you need to associate app functionality with certain mobile
service subscriptions on the device. For example, you may have a requirement to
verify access to certain premium app features based on the device's mobile
subscriptions via SIM.*

**Recommended identifier to use:** [Subscription ID
API](https://developer.android.com/reference/android/telephony/SubscriptionInfo#getSubscriptionId()) to
identify SIMs that are used on the device.

The Subscription ID provides an index value (starting at 1) for uniquely
identifying installed SIMs (including physical and electronic) used on the
device. Through this ID, your app can associate its functionality with various
subscription information for a given SIM. This value is stable for a given SIM
unless the device is factory reset. However, there may be cases where the same
SIM has a different Subscription ID on different devices or different SIMs have
the same ID on different devices.
| **Note:** Access to this ID requires the [`READ_PHONE_STATE`](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE) permission.

**Why this recommendation?**

Some apps may be currently using the [ICC
ID](https://developer.android.com/reference/android/telephony/SubscriptionInfo#getIccId%28%29) for this
purpose. Because the ICC ID is globally unique and non-resettable, the access
has been restricted to apps with the `READ_PRIVILEGED_PHONE_STATE`
permission since Android 10. Beginning with Android 11, Android further
restricted access to the ICCID through the
[`getIccId()`](https://developer.android.com/reference/android/telephony/SubscriptionInfo#getIccId%28%29)
API, regardless of the app's target API level. Affected apps should migrate to
use the Subscription ID instead.

#### Single sign-on

*In this case, your app offers a single sign-on experience, allowing users to
associate an existing account with your organization.*

**Recommended identifier to use:** Account manager-compatible accounts, such as
[Google Account Linking](https://developers.google.com/identity/account-linking)

**Why this recommendation?**

Google Account Linking allows users to associate a user's existing Google
account with your app, providing seamless and more secure access to your
organization's products and services. Additionally, you can
[define custom OAuth scopes](https://developers.google.com/identity/protocols/oauth2/native-app#identify-access-scopes)
to share only necessary data, increasing user trust by clearly defining how
their data is used.

### Ads

#### Targeting

*In this case, your app builds a profile of a user's interests, to show them
more relevant ads.*

**Recommended identifier to use:** If your app uses an ID for ads and uploads or
publishes to Google Play, that ID must be the Advertising ID.

**Why this recommendation?**

This is an ads-related use case which might require an ID that is available
across your organization's different apps, so using an Advertising ID is the
most appropriate solution. Use of the Advertising ID is mandatory for
advertising use cases, per the
[Google Play Developer Content Policy](https://play.google.com/about/developer-content-policy),
because the user can reset it.

Regardless of whether you share user data in your app, if you collect and use it
for ads purposes, you need to declare the ads purposes in the
[Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469)
of the **App content** page in the Play Console.

#### Measurement

*In this case, your app creates a profile of a user based on their behavior
across your organization's apps on the same device.*

**Recommended identifier to use:** Advertising ID or Play install referrer APIs

**Why this recommendation?**

This is an ads-related use case which might require an ID that is available
across your organization's different apps, so using an Advertising ID is the
most appropriate solution. If you use an ID for advertising use cases, that ID
must be the Advertising ID because the user can reset it. Learn more in the
[Google Play Developer Content Policy](https://play.google.com/about/developer-content-policy).


#### Conversions

*In this case, you're tracking conversions to detect if your marketing strategy
is successful.*

**Recommended identifier to use:** Advertising ID or Play install referrer APIs

**Why this recommendation?**

This is an ads-related use case which might require an ID that is available
across your organization's different apps, so using an Advertising ID is the
most appropriate solution. Use of the Advertising ID is mandatory for
advertising use cases, per the
[Google Play Developer Content Policy](https://play.google.com/about/developer-content-policy),
because the user can reset it.

#### Remarketing

*In this case, your app shows ads based on a user's previous interests.*

**Recommended identifier to use:** Advertising ID

**Why this recommendation?**

This is an ads-related use case which might require an ID that is available
across your organization's different apps, so using an Advertising ID is the
most appropriate solution. Use of the Advertising ID is mandatory for
advertising use cases, per the
[Google Play Developer Content Policy](https://play.google.com/about/developer-content-policy),
because the user can reset it.

### App analytics

*In this case, your app evaluates a user's behavior to help you determine the
following:*

- *Which of your organization's other products or apps might be suitable for the
  user.*
- *How to keep users interested in using your app.*
- *Measure usage statistics and analytics for signed-out or anonymous users.*

Possible solutions include:

- **App set ID:** An App Set ID allows you to analyze a user's behavior across multiple apps that your organization owns, as long as you don't use user data for advertising purposes. If you're targeting devices powered by Google Play services, we recommend that you use App Set ID.
- **Firebase ID (FID):** An FID is scoped to the app that creates it, which prevents the identifier from being used to track users across apps. It is also easily resettable, as the user can clear app data or reinstall the app. The process of creating a FID is straightforward; see the Firebase installations guide.

### App development

#### Crash reporting

*In this case, your app collects data regarding when and why it crashes on a
user's devices.*

**Recommended identifier to use:** FID or App set ID

**Why this recommendation?**

An FID is scoped to the app that creates it, which prevents the identifier from
being used to track users across apps. It is also easily resettable, as the user
can clear app data or reinstall the app. The process of creating a FID is
straightforward; see the
[Firebase installations guide](https://firebase.google.com/docs/projects/manage-installations).
An App Set ID allows you to analyze a user's behavior across multiple apps that
your organization owns, as long as you don't use user data for advertising
purposes.

#### Performance reporting

In this case, your app collects performance metrics, such as load times and
battery usage, to help improve your app's quality.

**Recommended identifier to use:**
[Firebase Performance Monitoring](https://firebase.google.com/products/performance)

**Why this recommendation?**

Firebase Performance Monitoring helps you focus on the metrics that matter most
to you, and to test the impact of a recent change in your app.

### App testing

In this case, your app evaluates a user's experience with your app for testing
or debugging purposes.

**Recommended identifier to use:** FID or App set ID

**Why this recommendation?**

An FID is scoped to the app that creates it, which prevents the identifier from
being used to track users across apps. It is also easily resettable, as the user
can clear app data or reinstall the app. The process of creating a FID is
straightforward; see the
[Firebase installations guide](https://firebase.google.com/docs/projects/manage-installations).
An App Set ID allows you to analyze a user's behavior across multiple apps that
your organization owns, as long as you don't use user data for advertising
purposes.

### Cross-device installation

*In this case, your app needs to identify the correct instance of the app when
it's installed on multiple devices for the same user.*

**Recommended identifier to use:** FID or GUID

**Why this recommendation?**

An FID is designed explicitly for this purpose; its scope is limited to the
app so that it cannot be used to track users across different apps, and it's
reset upon app reinstall. In the rare cases where an FID is
insufficient, you can also use a GUID.

### Security

#### Abuse detection

*In this case, you are trying to detect multiple fake devices attacking your
backend services.*

**Recommended identifier to use:** The Google Play Integrity API integrity token

**Why this recommendation?**

To verify that a request comes from a genuine Android device---rather than an
emulator or other code spoofing another device---use the
[Google Play Integrity API](https://developer.android.com/google/play/integrity/overview).

#### Ad fraud

*In this case, your app checks that a user's impressions and actions in your app
are genuine and verifiable.*

**Recommended identifier to use:** Advertising ID

**Why this recommendation?**

Use of the Advertising ID is mandatory for advertising use cases, per the
[Google Play Developer Content Policy](https://play.google.com/about/developer-content-policy),
because the user can reset it.


#### Digital rights management (DRM)

*In this case, your app wants to protect fraudulent access to intellectual
property or paid content.*

**Recommended identifier to use:** Using an FID or GUID forces the user to
reinstall the app in order to circumvent the content limits, which is a
sufficient burden to deter most people. If this isn't sufficient protection,
Android provides a [DRM API](https://source.android.com/devices/drm), which can
be used to limit access to content, includes a per-APK identifier, the
Widevine ID.


### User preferences

*In this case, your app saves per-device user state on your app's, particularly
for users who aren't signed in. You might transfer this state to another app
that's signed with the same key on the same device.*

**Recommended identifier to use:** FID or GUID

**Why this recommendation?**

Persisting information through reinstalls isn't recommended because users may
want to reset their preferences by reinstalling the app.