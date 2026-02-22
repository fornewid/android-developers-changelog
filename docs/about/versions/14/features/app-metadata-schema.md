---
title: https://developer.android.com/about/versions/14/features/app-metadata-schema
url: https://developer.android.com/about/versions/14/features/app-metadata-schema
source: md.txt
---

# Schema for app metadata bundles

Starting in Android 14, the Android package installer can ingest metadata about
an app, such as data safety practices, for use in Android platform features such
as the updated Location permission prompt.

There are two ways to provide this metadata:

- For an app preloaded on the system image, **device manufacturers** can
  provide metadata about the app by adding an XML file to the system image
  with the persistable bundle described below.

- For apps being installed or updated, To specify this metadata, **app
  installers** should pass a [`PersistableBundle`](https://developer.android.com/reference/android/os/PersistableBundle) object into the
  [`setAppMetadata()`](https://developer.android.com/reference/android/content/pm/PackageInstaller.Session#setAppMetadata(android.os.PersistableBundle)) method.

| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `setAppMetadata()`. In these cases, it is assumed that no app metadata is available.

The top-level persistable bundle consists of the following key/values pairs.
Unless specified otherwise, each key is optional.
| **Important:** All keys should be lowercase.

`version` (required)
:   The version number of the app metadata format. Use `2` as the value for this
    current version and `long` as the type. If expected keys or content types of
    `AppMetadata` change, Android will change the version number.

`safety_labels`
:   A `PersistableBundle` object that specifies the app's [safety-labels](https://developer.android.com/about/versions/14/features/app-metadata-schema#safety-labels).

`system_app_safety_label`
:   A `PersistableBundle` object that specifies the app's
    [system-app-safety-label](https://developer.android.com/about/versions/14/features/app-metadata-schema#system-app-safety-label). For apps acting as a [system service](https://docs.partner.android.com/partners/guides/system-services), the
    `system_app_safety_label` bundle is used instead of the `safety_labels` bundle.

`transparency_info`
:   A `PersistableBundle` object that specifies the app's [transparency
    information](https://developer.android.com/about/versions/14/features/app-metadata-schema#transparency-info).

## Safety labels format

The `safety_labels` bundle contains the following key/values pairs:
| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `safety_labels`. In these cases, it is assumed that no information is available.

`version` (required)
:   The version number of the safety labels format. Use `1` as the value for this
    current version and `long` as the type.

`data_labels`
:   A `PersistableBundle` object that specifies the [data that the app collects
    and shares](https://developer.android.com/about/versions/14/features/app-metadata-schema#data-collect-share).

`security_labels`
:   A `PersistableBundle` object that specifies the app's [data deletion and
    encryption practices](https://developer.android.com/about/versions/14/features/app-metadata-schema#data-delete-encrypt).

`third_party_verification`
:   A `PersistableBundle` object that specifies how the app's data safety
    practices are [verified by a third party](https://developer.android.com/about/versions/14/features/app-metadata-schema#third-party-verification).

### Data collected and shared

The `data_labels` bundle contains the following key/value pairs:
| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `data_labels`. In these cases, it is assumed that no information is available.

`data_collected`
:   A `PersistableBundle` object that specifies the types of data that the app
    collects.

`data_shared`
:   A `PersistableBundle` object that specifies the types of data that the app
    shares.

#### Data categories

Both the `data_collected` and `data_shared` keys use the `data_category` bundle
format, which contains the key/value pairs shown in the following list. Each key
maps to a `PersistableBundle` object that specifies the [data types](https://developer.android.com/about/versions/14/features/app-metadata-schema#data-types) for a
particular category.
| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `data_collected` and `data_shared`. In these cases, it is assumed that the data category is not collected or shared.

- `personal`
- `financial`
- `location`
- `email_text_message`
- `photo_video`
- `audio`
- `storage`
- `health_fitness`
- `contacts`
- `calendar`
- `identifiers`
- `app_performance`
- `actions_in_app`
- `search_and_browsing`

#### Data types

Each key in the `data_category` bundle maps to a different bundle that uses the
`data_type` format. The keys that you specify in the `data_type` format depend
on what you choose for a `data_category`.

The possible `data_type` key/value pairs appear in the following lists. The
value for each of these keys is a `PersistableBundle` object that describes the
app's [data usage practices](https://developer.android.com/about/versions/14/features/app-metadata-schema#data-delete-encrypt) for that particular data type. Some data types
use only one key.

**Personal**

- `name`
- `email_address`
- `physical_address`
- `phone_number`
- `race_ethnicity`
- `political_or_religious_beliefs`
- `sexual_orientation_or_gender_identity`
- `personal_identifiers`
- `other`

**Financial**

- `card_bank_account`
- `purchase_history`
- `credit_score`
- `other`

**Location**

- `approx_location`
- `precise_location`

**Email and text messages**

- `emails`
- `text_messages`
- `other`

**Photos and videos**

- `photos`
- `videos`

**Audio**

- `sound_recordings`
- `music_files`
- `other`

**Storage**

`files_docs`

**Health fitness**

- `health`
- `fitness`

**Contacts**

`contacts`

**Calendar**

`calendar`

**Identifiers**

`other`

**App performance**

- `crash_logs`
- `performance_diagnostics`
- `other`

**Actions in app**

- `user_interaction`
- `in_app_search_history`
- `installed_apps`
- `user_generated_content`
- `other`

**Search and browsing**

`web_browsing_history`

#### Data usage

The `data_usage` bundle contains the following key/value pairs:

`purposes`(required)

:   An array of integers that represents specific reasons for collecting or
    sharing data and uses `PersistableBundle`
    [`putIntArray`](https://developer.android.com/reference/android/os/BaseBundle#putIntArray(java.lang.String,%20int[]))
    method. At least one of the purposes defined below are required for each
    bundle.

    - `1`: PURPOSE_APP_FUNCTIONALITY
    - `2`: PURPOSE_ANALYTICS
    - `3`: PURPOSE_DEVELOPER_COMMUNICATIONS
    - `4`: PURPOSE_FRAUD_PREVENTION_SECURITY
    - `5`: PURPOSE_ADVERTISING
    - `6`: PURPOSE_PERSONALIZATION
    - `7`: PURPOSE_ACCOUNT_MANAGEMENT

`is_collection_optional`

:   Boolean value. Specifies whether users can opt in to, or opt out of,
    data collection.

    **Note:** Set this value only for
    `data_category` bundles that represent data collection; don't set
    it for data sharing.

`ephemeral`

:   Boolean value. Specifies whether the app processes the data
    server-side only in memory, not on disk, and that the app retains the data
    no longer than necessary to service the specific data processing
    request.

    **Note:** Set this value only for
    `data_category` bundles that represent data collection; don't set
    it for data sharing.

### Data deletion and encryption practices

The `security_labels` bundle contains key/value pairs that represent the app's
data deletion and encryption practices:
| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `security_labels`. In these cases, it is assumed that no information is available.

`is_data_deletable`
:   Boolean value. Specifies whether or not the app allows the user to request
    the app to delete their user data.

`is_data_encrypted`
:   Boolean value. Specifies whether or not all user data collected by the app is
    encrypted in transit.

### Third-party verification

The `third_party_verification` bundle consists of a single key, `url`. This URL,
represented as a string value, specifies the third-party website used for
verifying the app's data safety information.

## System service safety labels format

For apps acting as a [system service](https://docs.partner.android.com/partners/guides/system-services), the `system_app_safety_label` bundle
is used instead of the `safety_labels` bundle and contains the following
key/values pairs:
| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `system_app_safety_label`. In these cases, it is assumed that no information is available.

`url` (**required**)

- URL that points to a page containing safety information for the app that is acting as a system service.
- Use `string` as the type.
- If it has not been supplied then the privacy policy URL should be used as a fallback.
- Note: The Google Play store uses `privacy_policy` as a fallback.

## Transparency info format

| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `transparency_info`. In these cases, it is assumed that no information is available.

The `transparency_info` bundle contains the following key/values pairs:

`developer_info`
:   A `PersistableBundle` object that specifies [information about the app
    developer](https://developer.android.com/about/versions/14/features/app-metadata-schema#developer-info).

`app_info`
:   A `PersistableBundle` object that specifies [information about the app](https://developer.android.com/about/versions/14/features/app-metadata-schema#app-info).

### Developer info

| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `developer_info`. In these cases, it is assumed that no information is available.

The `developer_info` bundle contains the following key/value pairs:

`developer_`<var translate="no">#</var>
:   A `PersistableBundle` object that identifies the developer. The
    `developer_info` contains one or more `developer_`<var translate="no">#</var>,
    where <var translate="no">#</var> is an integer. For example `developer_0`,
    `developer_1`, `developer_2`, and so on.

#### Developer

| **Note:** You can also pass in either `null` or `PersistableBundle.EMPTY` into `developer_`<var translate="no">#</var>. In these cases, it is assumed that no information is available.

The `developer_`<var translate="no">#</var> bundle contains the following key/value
pairs:

`name` (**required**)
:   A string that states the name of the developer.

`email` (**required**)
:   A string that states the email address of the developer.

`address` (**required**)
:   A string that states the mailing address of the developer.

`country_region` (**required**)
:   A string that states the country or region of the developer.

`website`
:   A string that states the website of the developer.

`app_registry`

- A string that states the store or registry of the developer.
- If the developer is also registered on a store or other registry, the value should be the Android package name of the store or the URL of the registry.
- Multiple entries for multiple stores are permitted.
- For Google Play, use `com.android.vending`.
- If the developer is an SDK listed in the Google Play SDK Index, omit this attribute.
- If a developer isn't registered on any app store or registry, omit this attribute.

`app_registry_id`

- A string that states the ID of the developer for the stated `app_registry`.
- If the developer is also registered on a store or other registry, the value should be their store or registry identity.
- Multiple entries for multiple stores are permitted.
- For developers registered with Google Play, this value **must** be the URL of the developer page (for example, <https://play.google.com/store/apps/dev?id=5700313618786177705> is the URL for developer Google LLC).
- If the developer is a SDK developer listed in the Google Play SDK Index, use the Google Play SDK Index URL of the SDK (for example, <https://play.google.com/sdks/details/com-google-android-gms-play-services-ads> is the Google Play SDK Index URL of Google Mobile Ads (GMA) SDK).
- If the developer is registered on another store or registry, an app store URL or other identifier can be provided.
- If a developer isn't registered on any app store, this attribute can be omitted.

### App info

The `app_info` bundle contains the following key/value pairs:

`title` (**required**)
:   A string that states the title of the app.

`description` (**required**)
:   A string that states the purpose of the app in a human-readable blob of text
    in English.

`contains_ads` (**required**)
:   A boolean that declares whether the app displays any ads.

`privacy_policy` (**required**)

- A string that contains a URL attribute linking to the privacy policy detailing how user data is handled.
- Required for apps that transmit user data.
- If the app doesn't contain this link, it is assumed that the app does not handle user data.

`category` (**required**)

:   A string that contains one of the following app categories that best
    describes the app's primary purpose:

- Android (only for an AOSP component)\*
- Art and design
- Cars and vehicles
- Beauty
- Books and reference
- Business
- Comics
- Communications
- Dating
- Education
- Entertainment
- Events
- Finance
- Food and drink
- Game
- Health and fitness
- House and home
- Installer (only for an app store or other installer)\*
- Libraries and demo
- Lifestyle
- Maps and navigation
- Medical
- Music and audio
- News and magazines
- Parenting
- Personalisation
- Photography
- Productivity
- Security\*
- Shopping
- Social
- Sports
- Tools
- Travel and local
- Updater (only for a device's default over-the-air (OTA) update app)\*
- Video players and editors
- Weather

| **Note:** Categories marked with an asterisk\* are not available in the Google Play store and are intended for preloaded apps only.

`contact_info`
:   A `PersistableBundle` object that includes [contact information](https://developer.android.com/about/versions/14/features/app-metadata-schema#contact-info) for the
    app (below).

#### Contact info

The `contact_info` bundle contains the following key/value pairs:

`email` (**required**)
:   A string that states the email address for the app.

`website`
:   A string that states the website for the app.