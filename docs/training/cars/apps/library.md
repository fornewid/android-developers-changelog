---
title: Use the Android for Cars App Library  |  Android Developers
url: https://developer.android.com/training/cars/apps/library
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Use the Android for Cars App Library Stay organized with collections Save and categorize content based on your preferences.




Use the Android for Cars App Library, [androidx.car.app](/jetpack/androidx/releases/car-app), to bring your
[navigation](/training/cars/apps/navigation), [point of interest (POI)](/training/cars/apps/poi), [Internet of Things (IoT)](/training/cars/apps/iot),
and [weather](/training/cars/apps/weather) apps to the car. The library provides a set of templates
designed to meet driver distraction standards and to address details such as the
variety of car screen factors and input modalities.

This guide provides an overview of the library's key features and concepts and
walks you through the process of setting up a basic app.

[![](/static/images/picto-icons/code.svg)

Codelab

Learn Car App Library fundamentals

arrow\_forward](https://developer.android.com/codelabs/car-app-library-fundamentals)

**Important:** Google takes driver distraction very seriously. Your app must belong
to one of the supported categories and meet specific design requirements before
it can be listed on Google Play for Android Auto and Android Automotive OS. By
adhering to these requirements, you can make it easier to build and test your
app. For more information, see [Android app quality for cars](/docs/quality-guidelines/car-app-quality).

## Before you begin

1. Review the [Design for Driving](https://developers.google.com/cars/design) pages specific to the Car App Library:

   * [Navigation apps](https://developers.google.com/cars/design/create-apps/app-types/navigation) and [other driving-related apps](https://developers.google.com/cars/design/create-apps/app-types/other) category overviews
   * [Build apps with templates](https://developers.google.com/cars/design/create-apps/apps-for-drivers/build-with-templates) overview
   * [Building blocks](https://developers.google.com/cars/design/create-apps/apps-for-drivers/overview) specific to [Templates](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/overview) and
     [Template components](https://developers.google.com/cars/design/create-apps/apps-for-drivers/components/overview)
   * [Sample flows](https://developers.google.com/cars/design/create-apps/sample-flows/overview) that demonstrate common user experience (UX) patterns
   * [Templated app requirements](https://developers.google.com/cars/design/create-apps/ux-requirements/templated-apps)
2. Review the [Terms and concepts](/training/cars/apps/library/terms-concepts).
3. Become familiar with the [Android Auto System UI](https://developers.google.com/cars/design/android-auto/product-experience/system-ui/overview) and
   [Android Automotive OS design](https://developers.google.com/cars/design/automotive-os).
4. See the [Release Notes](/jetpack/androidx/releases/car-app).
5. See the [Code samples](https://github.com/android/car-samples/tree/main/car_app_library).