---
title: Play Age Signals overview  |  Android Developers
url: https://developer.android.com/google/play/age-signals/overview
source: html-scrape
---

On March 17, 2026, the Play Age Signals API starts rolling out responses for users in Brazil in [preparation for requirements under Digital ECA](https://support.google.com/googleplay/android-developer/answer/6223646#digital_eca_requirements). Ongoing updates will be provided in advance of [age verification bills](http://support.google.com/googleplay/android-developer/answer/16569691) in US states, which are slated to go into effect in Utah and Louisiana in May and July 2026 respectively. API responses for users in Texas not live due to a Federal District Court preliminary injunction.

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Play Age Signals](https://developer.android.com/google/play/age-signals)

# Play Age Signals overview Stay organized with collections Save and categorize content based on your preferences.



This guide explains how to use the Play Age Signals API (beta) to retrieve
age-related signals for users, how to notify Google Play of significant changes
to your app that require parental approval, and how to be notified about revoked
app approvals. These tools are designed to help you meet compliance obligations
under certain age verification laws in jurisdictions like Texas, Utah, and
Louisiana in the United States. Developers are responsible for ensuring their
use of the API is compliant with all applicable regulations and Google Play
policies.

See [this help center article](https://support.google.com/googleplay/android-developer/answer/16569691) to learn more about the age verification
laws, their requirements for developers, and timelines for each jurisdiction.

## How to use Play Age Signals API (beta)

The following steps describe how the Play Age Signals API (beta) can be used:

1. Your app calls the client-side Play Age Signals API.
2. Your app receives a response from the Play Age Signals API.
3. Your app may use the information provided in the response in accordance with
   the terms and guidelines provided in this documentation.

For more information, see [Use Play Age Signals API (beta)](/google/play/age-signals/use-age-signals-api).

## Terms and data safety

### Terms of service

Last modified: October 2025

1. By using the Play Age Signals API, you agree to these terms in addition to
   the [Google APIs Terms of Service](https://developers.google.com/terms) ("API ToS").
2. You may only use information from the Play Age Signals API to provide
   age-appropriate content and experiences in compliance with laws. You may not
   use the Play Age Signals API for any other purpose including, but not
   limited to, advertising, marketing, user profiling, or analytics.
3. Use of the Play Age Signals API is limited to apps that are updated by
   Google Play and the information returned by the API can be used only
   by the requesting app.
4. Use of the Play Age Signals API for a prohibited purpose may result in
   termination of your API access and suspension or takedown of your
   apps from Google Play.
5. Google may make changes to these terms at any time with notice and will
   post notice of modifications to the terms at
   <https://developer.android.com/google/play/age-signals/overview#terms-service>. Changes will not be retroactive.

As a Google Play developer, you must adhere to the
[Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html) and you are responsible for ensuring
that your app complies with all [Google Play developer policies](https://play.google/developer-content-policy/) including
the [Age Signals API and User Data policy](https://support.google.com/googleplay/android-developer/answer/16585319#age_signals).

### Data safety

Google Play has a [data safety section](https://support.google.com/googleplay/answer/11416267) for developers to disclose their
apps' data collection, sharing, and security practices. To help you complete the
data safety section requirements, you can use the following information on how
the Play Age Signals API handles data.

The Play Age Signals API is a runtime interface with the Google Play Store. As
such, when you use Play Age Signals in your app, the Play Store runs its own
processes, which include handling data as governed by the [Google Play Terms of
Service](https://play.google.com/intl/en-US_us/about/play-terms/index.html).

|  |  |
| --- | --- |
| Data collected on usage | No data is collected by the Play Age Signals client library. |
| Purpose of data collection | Not applicable. |
| Data encryption | Not applicable. |
| Data sharing | Not applicable. |
| Data deletion | Not applicable. |

You are solely responsible for deciding how to respond to [Google Play's data
safety section form](https://support.google.com/googleplay/android-developer/answer/10787469) regarding your app's user data collection, sharing, and
security practices.

[Next

Use age signals

arrow\_forward](/google/play/age-signals/use-age-signals-api)