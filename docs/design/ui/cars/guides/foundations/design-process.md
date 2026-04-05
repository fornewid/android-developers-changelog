---
title: Design process  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/foundations/design-process
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Design process Stay organized with collections Save and categorize content based on your preferences.




The type of app and its use case — whether it's for use while driving or parked
— determines the design process for *Android for Cars* apps.

Some apps are built on templates that work for both driving and parked
scenarios. Others apps, like media apps, need to have app content and actions
that are optimized for a driving UI.

If the car has Google built-in, you can adapt an existing app for the car
screen to deliver parked and passenger experiences.

## In-car app experience

Users can experience Android apps in cars through two ways:
Android Auto (projected from phones) or Android Automotive OS with
Google built-in.

![Diagram showing phones connected to cars via USB cable and wireless](/static/images/design/ui/cars/foundations/experience-projected.png)

![Diagram showing apps being downloaded to a car's system from the Play store](/static/images/design/ui/cars/foundations/experience-embedded.png)

**Projected from phones (Android Auto)**
  
  
Android Auto users can access compatible applications on their in-car
screen,right from their phones. The app's interface is projected from the
user's mobile phone to the in-car screen, either through a wireless or USB
connection.
  
  
The visual presentation of the app, including color schemes and styling,
remain consistent across all compatible cars.

**Downloaded into cars (Google built-in)**
  
  
Cars with AAOS provide users with the capability to install apps
directly from the Google Play Store within the car's infotainment system,
without the need to connect a mobile phone.
  
Car makers (OEMs) can modify color palettes and styling of installed
apps to align to their brand's visual identity.
  
  
When your app is downloaded into cars, vehicle OEMs can adjust colors and
[customize styling](/design/ui/cars/guides/foundations/customize-app) to fit specific vehicle models.

As you design your app, keep in mind that the experience of using it can
depend partly on whether users are running the app on *Android Auto* or on
*Google built-in*
(which is customizable by car makers). The processes described in this section
work for both Android for Cars systems
([Android Auto](https://developers.google.com/cars/design/android-auto) and
[AAOS](https://developers.google.com/cars/design/automotive-os)) except where otherwise noted - for example,
for cars with Google built-in.

## Partner roles for apps

Multiple partners contribute to the app experience in Android for Cars: app
developers, Google, and car makers.

App developers, Google, and car makers collaborate to create the app experience
in Android for Cars. Each partner's design responsibilities depend on the type
of app they are developing. While apps created using Android for
Cars App Library (CAL) templates follow a specific partnership model,
those with less flexible UIs or those designed for parked and passenger
use follow a different model.

For more details about some of these partnership models, refer to
the following table.

| Type of app | Discussions of partner roles in app design |
| --- | --- |
| Apps created with the Android for Cars App Library | * [Who handles what](/design/ui/cars/guides/foundations/overview#who-handles-what) * [Visual design customization](/design/ui/cars/guides/foundations/customize-app) |
| Media apps | * [Partner roles for media](https://developers.google.com/cars/design/create-apps/media-apps/overview#roles) |

![](/static/images/design/ui/cars/foundations/template-apps-ov.png)
[## Build apps with templates](/design/ui/cars/guides/foundations/overview)

Use the templates in the Android for Cars App Library to create apps in
these categories: navigation, point-of-interest, Internet of Things (IoT), and
weather


![](/static/images/design/ui/cars/foundations/media-apps-ov.png)
[## Create media apps](/design/ui/cars/guides/app-types/create-media-apps)

Create a version of your audio-content app for the Android for Cars UI

![](/static/images/design/ui/cars/foundations/video-apps-ov.png)
[## Adapt parked apps](/design/ui/cars/guides/app-types/parked-passenger-apps)

Download guidelines for adapting existing parked apps to work in cars with
Google built-in