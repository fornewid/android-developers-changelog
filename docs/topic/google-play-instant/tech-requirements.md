---
title: https://developer.android.com/topic/google-play-instant/tech-requirements
url: https://developer.android.com/topic/google-play-instant/tech-requirements
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

The quality of your instant experience can influence the long-term success of your app or game in terms of installs, pre-registrations, growth, and user retention. Before making your instant experience available, it's important to make sure that the instant experience meets users' basic expectations.

This document helps you understand the quality level, feature set, and UX that your instant experience should attain to be successful. Each focus area presents a checklist of minimum requirements, best practices, and good-to-have enhancements. In the interest of delivering the best possible experience to your users, follow each checklist requirement, and follow the checklist recommendations to the greatest extent possible.  
**Note:**To help prioritize your development efforts, take note of the level of importance indicated for each checklist item:

- **Required.**Minimum requirements that must be implemented for your instant experience to be considered compatible with Google Play Instant.
- **Best practice.**Strongly recommended implementation guidelines.
- **Good to have.**Suggested guidelines to help you create a distinctive user experience.

## Instant app total download size

| ID  |  Importance   |                                                                                                                                                                         Description                                                                                                                                                                          |
|-----|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1 | Required      | Your instant app's total download size to individual devices (ex: arm64) must be less than or equal to 15 MB. This is enforced during upload of your App Bundle. You can estimate your app download size by using the bundle tool to generate a device specific APK and then brotli compress it using the highest compression level (e.g. \`--quality 11\`). |
| 1.2 | Required      | The instant app must not consume more than 150 MB of storage space on the device.                                                                                                                                                                                                                                                                            |
| 1.3 | Best practice | When uncached, users should be able to engage with your instant experience in less than 15 seconds over an LTE or 4G connection.                                                                                                                                                                                                                             |

## App installation or pre-registration

Note that in-game installation buttons are not allowed for the[Instant play experience in the Play Games app](https://developer.android.com/topic/google-play-instant/instant-play-games).

| ID  |  Importance   |                                                                                                                                                                                                     Description                                                                                                                                                                                                     |
|-----|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.1 | Required      | When offering installation or pre-registration, you must display a clearly marked installation or pre-registration button that initiates installation and pre-registration, respectively, in at least one of the following ways: - Display a persistent button throughout your instant experience. - Display a persistent button on the main screen. - Display a button between actions in your instant experience. |
| 2.2 | Best practice | Your instant app call-to-action (CTA) button should use the label**Install** or**Pre-register**. Users might not understand standalone icons that represent installation or pre-registration if these icons are unaccompanied by clear labels.                                                                                                                                                                      |

## In-app navigation

| ID  |  Importance  |                                                                                                                                         Description                                                                                                                                         |
|-----|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.1 | Required     | Don't disable support for the Android back button. Users must be able to move backward through the history of screens that they've previously visited.                                                                                                                                      |
| 3.2 | Required     | Users must be able to exit the instant experience in 2 clicks or fewer.                                                                                                                                                                                                                     |
| 3.3 | Good to have | Provide a confirmation prompt to the user when they click the back button with clear**Cancel** and**Exit** options. The**Cancel** option can return users to the instant experience, and the**Exit**option can return users to screen they visited before entering your instant experience. |

## Ads display

| ID  | Importance |                                                                                 Description                                                                                  |
|-----|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4.1 | Required   | During your instant experience, use only unobtrusive banner ads. Don't use any other type of ad, especially full-page interstitial ads, that would interrupt the experience. |
| 4.2 | Required   | Ads must not be disguised as in-app components or elements of menu/app navigation.                                                                                           |

## In-app purchases

| ID  | Importance |                                                                                                                                                                                                                Description                                                                                                                                                                                                                |
|-----|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5.1 | Required   | If your instant app offers in-app purchases, your instant experience must support the transfer of in-app items to the installed app. Example: 1. Player buys a pack of 1000 coins. 2. Player uses 500 coins to unlock an in-game item, such as a power-up. 3. Player clicks the**Install**button to upgrade to the full, installed version of the game. 4. The balance of 500 coins must be transferred over to the full, installed game. |
| 5.2 | Required   | Users must not be required to make an in-app purchase before being able to engage with your instant experience. This requirement also applies to the full, installed version of your app or game.                                                                                                                                                                                                                                         |