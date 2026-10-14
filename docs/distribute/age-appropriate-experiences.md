---
title: Build age-appropriate experiences on Google Play  |  Android Developers
url: https://developer.android.com/distribute/age-appropriate-experiences
source: html-scrape
---

Stay organized with collections

Save and categorize content based on your preferences.



![](https://developer.android.com/static/distribute/age-appropriate-experiences/images/hero.svg)

### Build age-appropriate experiences on Google Play

**Deliver safe, age-appropriate experiences in your apps and games**

Google Play gives you a suite of tools to help you simplify building age-appropriate experiences. By combining Google Play Console controls and our API, you can dynamically tailor your in-app content and features to the right age groups—without the complexity of collecting sensitive user data like exact birthdate or age yourself.

## Core developer controls and protections

![](https://developer.android.com/static/distribute/age-appropriate-experiences/images/content-restrictions.svg)

### Content restrictions

Google Play may restrict downloads by users identified as minors based on the age rating assigned by IARC through parental controls and, in some regions, apply restrictions at the Google Play store level.

**Google Play level restrictions**

[Complete](https://play.google.com/console/developers/app/app-content/content-rating-overview)
the mandatory International Age Rating Coalition (IARC) questionnaire in Play
Console, to automatically receive ratings across regional rating authorities such as PEGI,
ESRB, ClassInd and more. In some regions, Google Play restricts users identified as
minors from downloading or purchasing mature content, such as apps rated 18+.

**[Learn more about content ratings](https://support.google.com/googleplay/android-developer/answer/9859655#How_content_ratings_are_used)**   
  
 **Parental controls**

Parents can use [Google Family Link](https://families.google/familylink/) to
set content filters based on maturity rating level.
On supervised devices, Google Play uses your app's rating to limit what supervised users
can discover and download.

**[Learn more about parental controls](https://support.google.com/googleplay/answer/1075738)**

![](https://developer.android.com/static/distribute/age-appropriate-experiences/images/restrict-minor-access.svg)

### Restrict minor access

Limit app discovery and distribution to your age appropriate audience, directly from
Google Play Console. When you enable Restrict Minor Access, users who are identified as
minors can't discover, download, or purchase your app. This setting applies globally to
protect younger audiences.

While Restrict Minor Access is required for apps in designated
[age-restricted content and functionality policy](https://support.google.com/googleplay/android-developer/answer/16302250) categories, any developer can
proactively opt in by using Play Console to help direct their content only to adults.

[Learn more](https://support.google.com/googleplay/android-developer/answer/9867159#age-groups-18-and-over)

![](https://developer.android.com/static/images/cluster-illustrations/personal-16-9.svg)

### Play Age Signals API

Dynamically adapt your app experiences based on user age ranges. The Play Age Signals
API lets your app request a user's age range. By default, the API returns age ranges
of 0–12, 13–15, 16–17, and 18+. You can also set
[custom age ranges](https://play.google.com/console/developers/app/age-signals)
in Play Console to get age ranges that suit your app content.

[Explore more](https://developer.android.com/google/play/age-signals/overview)

![](https://developer.android.com/static/images/picto-icons/pathway.svg)

## How to get started

Follow these steps to help implement the right age-based protections for your app.

Step 1

### [Keep IARC content ratings up to date [Required]](https://support.google.com/googleplay/android-developer/answer/9859655)

Ensure your responses to the International Age Rating Coalition (IARC) questionnaire matches every new version of your app in the Play Console. This keeps your regional ratings accurate and facilitates Family Link appropriately restricting minors' access to your app.

Step 2

### [Check regional protections on Play](https://developer.android.com/distribute/age-appropriate-experiences/regional-protections)

Review the age-related Google Play tools and features that apply in the countries and regions where you distribute your app.

Step 3

### [Determine if Restrict Minor Access is mandatory for your app [Required]](https://support.google.com/googleplay/android-developer/answer/9867159#age-groups-18-and-over)

Depending on your app category, you may need to enable Restrict Minor Access to comply with [Google Play policy](https://support.google.com/googleplay/android-developer/answer/16302250). You can easily configure this setting in the Play Console to restrict discovery, downloads, and in-app purchases and new subscriptions by users identified as minors.

Step 4

### [Integrate the Play Age Signals API](https://developer.android.com/google/play/age-signals/overview)

Add the client library to request runtime age signals from within your app, handle returned age bands, and adapt your in-app features dynamically.

## Resources for developers

Technical guides, API references, and Play Console tools that you use to build age-appropriate experiences into your app.

![](https://developer.android.com/static/distribute/age-appropriate-experiences/images/age-signals.svg)

### Play Age Signals API overview

Understand API architecture, request signals, handle responses, and more.

[Read API overview](https://developer.android.com/google/play/age-signals/overview)

![](https://developer.android.com/static/images/picto-icons/prohibited.svg)

### Restrict minor access

Learn how to configure this setting in Play Console to prevent minors from discovering and downloading your app.

[Learn more about Restrict Minor Access](https://support.google.com/googleplay/android-developer/answer/9867159#age-groups-18-and-over)

![](https://developer.android.com/static/images/picto-icons/playground.svg)

### Families policies

Review Families Policies if your app's target audience includes children, as these policies specify additional requirements for distributing your app on Google Play.

[Review Families policies](https://support.google.com/googleplay/android-developer/answer/9893335)

## Resources for parents and families

Understand the Google Play experiences that parents and users control, so you know how they affect your app's discovery, installs, and the age signals your app receives.

![](https://developer.android.com/static/images/picto-icons/family.svg)

### Parental controls and Family Link

Parents can restrict Play Store content by maturity level and approve downloads and purchases on supervised devices. Your IARC rating determines how these controls apply to your app.

[Learn about parental controls](https://support.google.com/googleplay/answer/1075738)
[Explore Family Link](https://families.google/familylink/)

![](https://developer.android.com/static/images/picto-icons/toggle.svg)

### Age range sharing settings

Users decide whether Google Play shares their age range with apps. Learn what users see when your app requests age signals through the Play Age Signals API.

[About age range sharing](https://support.google.com/googleplay/answer/17232873)