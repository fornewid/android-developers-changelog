---
title: https://developer.android.com/health-and-fitness/health-connect/medical-records
url: https://developer.android.com/health-and-fitness/health-connect/medical-records
source: md.txt
---

The Health Connect platform provides a [range of data types](https://developer.android.com/health-and-fitness/guides/health-connect/plan/data-types),
mostly covering wellness and fitness use cases, enabling apps in the Android
ecosystem to share data without the need for high-cost one-to-one
API integrations.

Medical Records extends this capability to include basic medical
data in [Fast Healthcare Interoperability Resources (FHIR®)](https://www.hl7.org/fhir/overview.html)
format. FHIR is an open-source global specification describing schema and
semantics for medical data published by HL7 (Health Level Seven International).

Medical Records on Health Connect features:

- An API for applications writing medical data.
- A user-facing browser experience for medical data stored in Health Connect as new medical data types, along with fine-grained permissions for allowing downstream reads.
- An API for applications reading medical data based on user-granted permissions.

![An overview of how Medical Records work with Health Connect.](https://developer.android.com/static/health-and-fitness/guides/medical-records/images/overview.png) **Figure 1.** How Medical Records work with Health Connect.

## Limitations

As these APIs are still under development, there are still some limitations and
some components aren't fully available.

The Medical Records APIs are marked with an annotation of
`ExperimentalPersonalHealthRecordApi`, which indicates that these APIs are still
under development and subject to change.

There are still some limitations and some components aren't fully available:

- The Play Policy for Medical Records access is still being developed, and apps may need to meet additional requirements before they can be released on the Play Store.
- Some features, such as changelogs-based APIs, have not been developed for Medical Records APIs yet.

## Get Started

Because Medical Records is a set of new record types in Health Connect, the
same process for getting started with Health Connect applies to Medical Records.
See [Get started with Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started) for more information.

If you have been experimenting with the Medical Records Framework APIs that
were initially available, we strongly recommend you transition to Jetpack for
an improved developer experience for the following reasons:

- All guides and sample code are written for Jetpack
- Ecosystem tools use the Jetpack APIs
- The API surface is Kotlin native
- Jetpack has improved compatibility support (such as the [Feature
  Availability API](https://developer.android.com/health-and-fitness/guides/health-connect/develop/feature-availability))

Medical Records APIs are made available through Health Connect version
[1.1.0-beta02](https://developer.android.com/jetpack/androidx/releases/health-connect#1.1.0-beta02) in Jetpack. Updating your Jetpack dependency to
this version requires that apps be compiled against the [Android 16
SDK](https://developer.android.com/about/versions/16/setup-sdk).

Once you're set up and ready to write and read Medical Records data in your app,
see [Write medical data](https://developer.android.com/health-and-fitness/guides/medical-records/write-data) and [Read medical data](https://developer.android.com/health-and-fitness/guides/medical-records/read-data).

## User experience

General information about the user experience is provided in this section.

### Permissions

Requesting read or write medical record permissions behaves similarly to the
existing Health Connect permissions screens, but a separate
health records screen is shown:
![Permissions screen for medical records](https://developer.android.com/static/health-and-fitness/guides/medical-records/images/permissions.png) **Figure 2**: Medical Records permissions screen

### Data browsing

Health Connect also provides basic visualization and browsing of Medical Records
data stored, similar to existing Health Connect data types.
![Data browsing screen for medical records](https://developer.android.com/static/health-and-fitness/guides/medical-records/images/browsing.png) **Figure 3**: Medical Records data browsing screen