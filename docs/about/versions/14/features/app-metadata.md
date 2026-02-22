---
title: https://developer.android.com/about/versions/14/features/app-metadata
url: https://developer.android.com/about/versions/14/features/app-metadata
source: md.txt
---

# App metadata bundles for data safety

App metadata bundles provide developers with a transparent way to include information about them (the developer), the app, and if and how they collect, share, and protect user data. The Google Play Store requires developers to provide this information for apps it distributes, and manufacturers of Android devices with Google Play services require the same from developers of apps that the manufacturer preloads, with limited exceptions for system services.

Other app stores and installers can choose to require an app metadata bundle for apps that they distribute. The method of app distribution determines how developers can create and integrate an app metadata bundle. Android displays data safety information from the app metadata bundle to users; for example, if an app declares that it shares location with a third party, that information is displayed in the location permission prompt on devices running Android 14 or higher.

## Overview

An app metadata bundle lets you share information about you (the developer) and your app, including what user data your app collects or shares, and to showcase your app's key privacy and security practices. This information helps users make more-informed choices when, for example, granting access to permissions.

App metadata bundles are separate from and an addition to any legal transparency and disclosure obligations that you as a developer might be subject to in countries where you operate.

All developers are encouraged to declare how they collect and handle user data for their apps, and provide details about the app purpose, developer information, and how the app protects user data through security practices like encryption. This includes data collected and handled through any third-party libraries or SDKs used in apps. Developers might want to refer to SDK providers' published data safety information for details. Developers can check the[Google Play SDK Index](https://play.google.com/sdks)to see if a provider has provided a link to their guidance.

App metadata bundles reach the device differently, depending on how the app is distributed:

- **Apps preloaded on the system image**: The device manufacturer is responsible for including the app metadata bundle in a data safety XML file in the system image.
- **Apps distributed by installers** : The installer is responsible for sending the app metadata bundle to the device. If you develop an app that's distributed through Google Play, refer to[the instructions in the Play Console Help](https://support.google.com/googleplay/android-developer/answer/10787469). Installers can refer to the[schema for app metadata bundles](https://developer.android.com/about/versions/14/features/app-metadata-schema).

Developers of preloaded apps can create a data safety XML file by using one of the following methods:

- If you develop an app that's published in the Play Store, use the Play Console's data safety form on the App content page by navigating to**Policy \> App content**. If you have already completed this form, you don't need to take any additional action.
- Download and edit[the template XML file that's available on this page](https://developer.android.com/about/versions/14/features/app-metadata#manual-xml)to provide to manufacturers or installers.

| **Important:** Developers are solely responsible for making complete and accurate declarations in their app metadata bundle. While developers can work with a manufacturer or installer to add an app metadata bundle, manufacturers and installers can't make determinations on behalf of developers of how they handle user data. Only a developer possesses all the information required to create an app metadata bundle.

## Getting information ready

Before developers start creating an app metadata bundle, complete the following steps:

- Ensure that they've added a privacy policy.

- [Review how the app collects and shares user data](https://developer.android.com/guide/topics/data/collect-share)and the app's security practices. In particular, check the app's declared permissions and the APIs that the app uses.

  In addition to reviewing how the app collects and shares user data, developers should also review how any third-party code (such as third-party libraries or SDKs) in the app collects and shares such data. The app metadata bundle must reflect data collection or sharing carried out by such third-party code.

## What developers need to disclose in the app and developer information sections

This section explains what information developers need to disclose in the[app](https://developer.android.com/about/versions/14/features/app-metadata-schema#app-info)and[developer information](https://developer.android.com/about/versions/14/features/app-metadata-schema#developer-info)sections of the app metadata bundle. If the app is distributed through the Google Play store,[use the Play Console to enter this information](https://support.google.com/googleplay/android-developer/answer/10787469).

### What developers need to share about the app

When creating an app metadata bundle, developers need to disclose the app information that's described in the following sections:

#### App purpose

Describe the purpose of the app in a human-readable blob of text in English (4000 character limit).

#### App category

Select the category that best fits the purpose of the app from the following list.

The following categories are intended for preloaded apps:

- OTA - Packages responsible for receiving and installing over-the-air (OTA) updates
- AOSP - Packages available in the Android Open Source Project
- Security
- Store

The categories described in the following table are also used by Google Play:

|         Category          |                                                       Examples                                                        |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Art and Design            | Sketchbooks, painter tools, art and design tools, coloring books                                                      |
| Auto and Vehicles         | Auto shopping, auto insurance, auto price comparison, road safety, auto reviews and news                              |
| Beauty                    | Makeup tutorials, makeover tools, hair styling, beauty shopping, makeup simulators                                    |
| Books and Reference       | Book readers, reference books, textbooks, dictionaries, thesaurus, wikis                                              |
| Business                  | Document editor or reader, package tracking, remote desktop, email management, job search                             |
| Comics                    | Comic players, comic titles                                                                                           |
| Communications            | Messaging, chat or IM, dialers, address books, browsers, call management                                              |
| Dating                    | Matchmaking, courtship, relationship building, meeting new people, finding love                                       |
| Education                 | Exam preparations, study-aids, vocabulary, educational games, language learning                                       |
| Entertainment             | Streaming video, movies, TV, interactive entertainment                                                                |
| Events                    | Concert tickets, sporting event tickets, ticket resales, movie tickets                                                |
| Finance                   | Banking, payment, ATM finders, financial news, insurance, taxes, portfolio management and trading, tip calculators    |
| Food and Drink            | Recipes, restaurants, food guides, wine tasting and discovery, beverage recipes                                       |
| Health and Fitness        | Personal fitness, workout tracking, diet and nutritional tips, health and safety                                      |
| House and Home            | House and apartment search, home improvement, interior decoration, mortgages, real estate                             |
| Libraries and Demo        | Software libraries, technical demos                                                                                   |
| Lifestyle                 | Style guides, wedding and party planning, how-to guides                                                               |
| Maps and Navigation       | Navigation tools, GPS, mapping, transit tools, public transportation                                                  |
| Medical                   | Drug and clinical references, calculators, handbooks for healthcare providers, medical journals and news              |
| Music and Audio           | Music services, radios, music players                                                                                 |
| News and Magazines        | Newspapers, news aggregators, magazines, blogging                                                                     |
| Parenting                 | Pregnancy, infant care and monitoring, childcare                                                                      |
| Personalization           | Wallpapers, live wallpapers, home screen, lock screen, ringtones                                                      |
| Photography               | Cameras, photo editing tools, photo management, and sharing                                                           |
| Productivity              | Notepad, to-do list, keyboard, printing, calendar, backup, calculator, conversion                                     |
| Shopping                  | Online shopping, auctions, coupons, price comparison, grocery lists, product reviews                                  |
| Social                    | Social networking, check-in                                                                                           |
| Sports                    | Sports news and commentary, score tracking, fantasy team management, game coverage                                    |
| Tools                     | Tools for Android devices                                                                                             |
| Travel and Local          | Trip booking tools, ride-sharing, taxis, city guides, local business information, trip management tools, tour booking |
| Video Players and Editors | Video players, video editors, media storage                                                                           |
| Weather                   | Weather reports                                                                                                       |

#### App advertising and marketing

Indicate if the app contains advertising or marketing, including in-app promotions.

#### Privacy policy

Include a link to the privacy policy detailing how the user data is handled by the developer. If the app doesn't contain this link, it's assumed that the app doesn't handle user data.

### What developers need to share about themselves

When creating an app metadata bundle, developers need to disclose the developer information that's described in the following sections:

#### Developer name

Name of the developer, the person, or company that created the app. There can be multiple developer names.

#### App registry

If the app is listed on any app registry including stores and other installers, indicate in this field. Multiple entries for multiple stores are permitted.

- **For app registries that are Android installers** : The value should be the Android package name of the store. For example, use`com.android.vending`for the Google Play store.
- **For other app registries**: The value should be the URL of the registry.

Omit this field for any of the following reasons:

- The developer is an SDK listed in the Google Play SDK Index.
- The developer isn't registered on any app store or registry.

#### App registry ID

For apps listed on any app registry, including installers and stores, this value should be the developer's store, installer, or registry identity. Multiple entries for multiple stores are permitted.

- **For developers registered with Google Play** : This value**must** be the URL of the developer page (for example,`https://play.google.com/store/apps/dev?id=5700313618786177705`is the URL for developer Google LLC).
- **If the developer is an SDK developer listed in the Google Play SDK Index** : Use the URL of the SDK (for example,`https://play.google.com/sdks/details/com-google-android-gms-play-services-ads`is the URL of Google Mobile Ads (GMA) SDK).
- **If the developer is registered on another store or registry**: An app store URL or other identifier can be provided.

If a developer isn't registered on any app store, this attribute can be omitted.

#### Developer contact information

Provide the following information:

- Email
- Website
- Country or region
- Physical mailing address

## What developers need to disclose in the data safety section

This section explains what information developers need to disclose in the[data safety section](https://developer.android.com/about/versions/14/features/app-metadata-schema#safety-labels)of the app metadata bundle, and lists the user data types and purposes developers can select. If an app is distributed through the Google Play store,[use the Play Console to enter this information](https://support.google.com/googleplay/android-developer/answer/10787469).

### What developers need to declare across data types

When creating an app metadata bundle, developers need to disclose information about the types of data they collect and share, as described in the following sections:

#### Data collection

*Collect*in this case means transmitting data from an app off a user's device. Note the following guidelines:

- **Libraries and SDKs**: This includes user data transmitted off device from an app by libraries or SDKs used in an app, irrespective of whether data is transmitted to the app's developer or a third-party server.

- **Webview**: This includes user data collected from a webview that has been opened from the app, if the app is in control of the code and behavior delivered through that webview.

  Developers don't need to declare data collection from a webview in which users are navigating the open web.

- **Ephemeral processing**: User data transmitted off device that is processed ephemerally doesn't need to be included in your app metadata bundle if it meets the following standard:

  Processing data*ephemerally*means accessing and using it while the data is only stored in memory and retained for no longer than necessary to service the specific request in real time.

  For example, a weather app that transmits user location off the device to fetch the current weather at the user's location but only uses location data in memory and doesn't store that data once the request has been fulfilled, can treat its transient use of location as ephemeral. However, using data to build advertising profiles or other user profiles can't be treated as ephemeral and must be declared as collection or sharing for the relevant purposes.

- **Pseudonymous data**: User data collected pseudonymously must be disclosed. For example, data that can reasonably be re-associated with a user must be disclosed.

##### Not in scope for data collection disclosure

The following use cases don't need to be disclosed as collected:

- **On-device access or processing** : User data accessed by an app that is only processed locally on the user's device and not sent off device does**not**need to be disclosed.

- **End-to-end encryption** : User data that is sent off device, but that is unreadable by you or anyone other than the sender and recipient as a result of end-to-end encryption does**not**need to be disclosed.

  The encrypted data must not be readable by any intermediary entity, including the developer, and only the sender and recipient can have the necessary keys.

#### Data sharing

*Sharing*in this case refers to transferring user data collected from an app to a third party. This includes user data transferred in the following ways:

- **Off-device, such as server to server transfers**: For example, if a developer transfers user data collected from an app from the developer's server to a third-party server.

- **On-device transfer to another app**: Transferring user data from an app to another app directly on the device. In this case, the developer must disclose data sharing in the data safety section even if the app doesn't transmit the data off the user's device.

- **From your app libraries and SDKs**: Transferring data collected from an app off a user's device directly to a third party using libraries or SDKs that are included in the app.

- **From webview which has been opened through your app**: Transferring user data to a third party using a webview that has been opened from the app, if the app is in control of the code and behavior delivered through that webview.

  Developers don't need to declare data sharing from a webview in which users are navigating the open web.

The following types of data transfers don't need to be disclosed as*sharing*:

- **Service providers** : Transferring user data to a service provider that processes it on behalf of the developer. A*service provider*means an entity that processes user data on behalf of the developer and based on the developer's instructions.

- **Legal purposes**: Transferring user data for specific legal purposes, such as in response to a legal obligation or government requests.

- **User-initiated action or prominent disclosure and user consent**: Transferring user data to a third party based on a specific user-initiated action, where the user reasonably expects the data to be shared, or based on a prominent in-app disclosure and consent.

- **Anonymous data**. Transferring user data that has been fully anonymized so that it can no longer be associated with an individual user.

- **First and third parties** :*First party*means the developer, the primary organization responsible for processing data collected by the app. For apps distributed through stores, this is typically the organization publishing the app on the store.

  The first party has an obligation to make reasonably clear to users which organization is primarily responsible for processing data collected by the app.

  *Third party*means any organization other than the first party or its service providers.

#### Data handling

Developers can also disclose whether each data type collected by the app is*optional* or*required* .*Optional*includes the ability to opt in to or opt out of data collection. For example, developers can declare a data type as optional where a user has control over its collection and can use the app without providing it; or where a user chooses whether to manually provide that data type. If an app's primary capabilities require the data type, developers should declare that data as required.

Developers can declare that an app collects certain data optionally only if all users--regardless of device or region--can either optionally provide information, opt out, or opt in to have the data collected.

Examples of optional data collection include the following:

- A social media app that asks for a user's birthday for marketing communication, but that info is not required--the user can still sign up without providing that information.

- User data that is only collected when a user signs in where users have the ability to engage with the app without being signed in.

#### Other app and data disclosures

The data safety section is also an opportunity for developers to showcase an app's privacy and security practices. For example, developers can highlight the following information:

- **Encryption in transit**: Whether data collected or shared by an app uses encryption in transit to protect the flow of user data from the end user's device to the server.

  Some apps are designed to let users transfer data to another site or service. For example, a messaging app might give users an option to send an SMS message through their mobile services provider, which maintains different encryption practices. These apps can declare in their data safety section that data is transferred over a secure connection as long as they use best industry standards to safely encrypt data while it travels between a user's device and the app's servers.
- **Deletion request mechanism**: Whether an app provides a way for users to request deletion of their data.

#### Independent security review (available to all apps)

Developers can choose to declare in the data safety section that the app has been independently validated against a global security standard. This is an optional review undertaken and paid for by developers. For example, using a Mobile Application Security Assessment (MASA), developers can work directly with a lab to have their apps evaluated against the Open Worldwide Application Security Project's (OWASP) Mobile Application Security Verification Standard (MASVS). The third-party organizations performing the reviews are doing so on the developer's behalf.
| **Important:** This independent review might not be scoped to verify the accuracy and completeness of a developer's app metadata bundle. Even if developers use third-party tools to diagnose an app's security controls, developers remain solely responsible for making complete and accurate declarations in the app metadata bundle.

### Data types and purposes

Developers are asked to provide collection, sharing, and other practices for a range of user data types, as well as the[purposes for which the developer uses that data](https://developer.android.com/about/versions/14/features/app-metadata#data-purposes), as described in the following tables:

|         Category         |           Data type            |                                                                                              Description                                                                                              |
|--------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location                 | Approximate location           | User or device physical location to an area greater than or equal to 3 square kilometers, such as the city a user is in, or location provided by Android's`ACCESS_COARSE_LOCATION`permission.         |
|                          | Precise location               | User or device physical location within an area less than 3 square kilometers, such as location provided by Android's`ACCESS_FINE_LOCATION`permission.                                                |
| Personal info            | Name                           | How a user refers to themselves, such as their first or last name, or nickname.                                                                                                                       |
|                          | Email address                  | A user's email address.                                                                                                                                                                               |
|                          | User IDs                       | Identifiers that relate to an identifiable person. For example, an account ID, account number, or account name.                                                                                       |
|                          | Address                        | A user's address, such as a mailing or home address.                                                                                                                                                  |
|                          | Phone number                   | A user's phone number.                                                                                                                                                                                |
|                          | Race and ethnicity             | Information about a user's race or ethnicity.                                                                                                                                                         |
|                          | Political or religious beliefs | Information about a user's political or religious beliefs.                                                                                                                                            |
|                          | Sexual orientation             | Information about a user's sexual orientation.                                                                                                                                                        |
|                          | Other info                     | Any other personal information such as date of birth, gender identity, or veteran status.                                                                                                             |
| Financial info           | User payment info              | Information about a user's financial accounts such as credit card number.                                                                                                                             |
|                          | Purchase history               | Information about purchases or transactions a user has made.                                                                                                                                          |
|                          | Credit score                   | Information about a user's credit score.                                                                                                                                                              |
|                          | Other financial info           | Any other financial information such as user salary or debts.                                                                                                                                         |
| Health and fitness       | Health info                    | Information about a user's health, such as medical records or symptoms.                                                                                                                               |
|                          | Fitness info                   | Information about a user's fitness, such as exercise or other physical activity.                                                                                                                      |
| Messages                 | Emails                         | A user's emails including the email subject line, sender, recipients, and the content of the email.                                                                                                   |
|                          | SMS or MMS                     | A user's text messages including the sender, recipients, and the content of the message.                                                                                                              |
|                          | Other in-app messages          | Any other types of messages. For example, instant messages or chat content.                                                                                                                           |
| Photos and videos        | Photos                         | A user's photos.                                                                                                                                                                                      |
|                          | Videos                         | A user's videos.                                                                                                                                                                                      |
| Audio files              | Voice or sound recordings      | A user's voice such as a voicemail or a sound recording.                                                                                                                                              |
|                          | Music files                    | A user's music files.                                                                                                                                                                                 |
|                          | Other audio files              | Any other user-created or user-provided audio files.                                                                                                                                                  |
| Files and docs           | Files and docs                 | A user's files or documents, or information about their files or documents such as file names.                                                                                                        |
| Calendar                 | Calendar events                | Information from a user's calendar such as events, event notes, and attendees.                                                                                                                        |
| Contacts                 | Contacts                       | Information about the user's contacts such as contact names, message history, and social graph information like usernames, contact recency, contact frequency, interaction duration and call history. |
| App activity             | App interactions               | Information about how a user interacts with the app. For example, the number of times they visit a page or sections they tap on.                                                                      |
|                          | In-app search history          | Information about what a user has searched for in the app.                                                                                                                                            |
|                          | Installed apps                 | Information about the apps installed on a user's device.                                                                                                                                              |
|                          | Other user-generated content   | Any other user-generated content not listed here, or in any other section. For example, user bios, notes, or open-ended responses.                                                                    |
|                          | Other actions                  | Any other user activity or actions in-app not listed here such as gameplay, likes, and dialog options.                                                                                                |
| Web browsing             | Web browsing history           | Information about the websites a user has visited.                                                                                                                                                    |
| App info and performance | Crash logs                     | Crash log data from the app. For example, the number of times the app has crashed, stack traces, or other information directly related to a crash.                                                    |
|                          | Diagnostics                    | Information about the performance of the app. For example battery life, loading time, latency, framerate, or any technical diagnostics.                                                               |
|                          | Other app performance data     | Any other app performance data not listed here.                                                                                                                                                       |
| Device or other IDs      | Device or other IDs            | Identifiers that relate to an individual device, browser or app. For example, an IMEI number, MAC address, Widevine Device ID, Firebase installation ID, or advertising identifier                    |

#### Purposes

|                Data purpose                |                                      Description                                       |                                                                                        Example                                                                                        |
|--------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| App functionality                          | Used for features that are available in the app                                        | For example to enable app features, or authenticate users.                                                                                                                            |
| Analytics                                  | Used to collect data about how users use the app or how it performs                    | For example, to see how many users are using a particular feature, to monitor app health, to diagnose and fix bugs or crashes, or to make future performance improvements.            |
| Developer communications                   | Used to send news or notifications about the app or the developer.                     | For example, sending a push notification to inform users about an important security update, or informing users about new features of the app.                                        |
| Advertising or marketing                   | Used to display or target ads or marketing communications, or measuring ad performance | For example, displaying ads in the app, sending push notifications to promote other products or services, or sharing data with advertising partners.                                  |
| Fraud prevention, security, and compliance | Used for fraud prevention, security, or compliance with laws.                          | For example, monitoring failed login attempts to identify possible fraudulent activity.                                                                                               |
| Personalization                            | Used to customize the app, such as showing recommended content or suggestions.         | For example, suggesting playlists based on the user's listening habits or delivering local news based on the user's location.                                                         |
| Account management                         | Used for the setup or management of a user's account with the developer.               | For example, to enable users to create accounts or add information to an account the developer provides for use across its services, sign in to the app, or verify their credentials. |

## Create a data safety XML file manually

The following sample data safety XML file demonstrates the file structure for a preloaded app that shares data related to a user's location. Edit this structure by adding, editing, or removing elements depending on the type of information that you need to disclose for your app.

Note that the sample file is not necessarily complete. Refer to the[schema for app metadata bundles](https://developer.android.com/about/versions/14/features/app-metadata)for more information about the required XML structure for the app, developer, and data safety sections of the app metadata bundle that your app might need to include.  

    <?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
    <bundle>
    <long name="version" value="2" />

      <pbundle_as_map name="safety_labels">
        <long name="version" value="1" />

          <pbundle_as_map name="data_labels">
            <pbundle_as_map name="data_shared">
              <pbundle_as_map name="location">
                <pbundle_as_map name="approx_location">
                  <int-array name="purposes" num="4">
                      <item value="1" />
                      <item value="2" />
                      <item value="5" />
                      <item value="6" />
                  </int-array>
                </pbundle_as_map>
                <pbundle_as_map name="precise_location">
                  <int-array name="purposes" num="2">
                      <item value="1" />
                      <item value="6" />
                  </int-array>
                </pbundle_as_map>
              </pbundle_as_map>
            </pbundle_as_map>

        </pbundle_as_map>
    </pbundle_as_map>
    </bundle>

## Frequently asked questions

See the following sections for answers to common questions that developers have asked.

### General questions

The following sections have answers to general questions about app metadata bundles.

#### A developer submitted similar information for iOS. How much of that work can the developer re-use for the Android app metadata bundle?

It's great that the developer has a good handle on the app's data practices. To correctly complete an app metadata bundle, the developer might need additional information that they might not have used previously, so they should expect to do additional work. The taxonomy and framework of the Android app metadata bundle might differ materially from those used in other app stores.

#### How does Google make sure developers share accurate information? We've seen that this information is not always accurate in the industry.

Similar to a privacy policy, developers are responsible for the information disclosed in their app metadata bundle.

#### How often does a developer need to update an app metadata bundle?

Developers should update the app metadata bundle when there are relevant changes to the data practices of the app.

### Questions about completing the data safety section

The following sections have answers to questions about completing the data safety section of an app metadata bundle.

#### What if the app behaves differently in different supported Android versions?

The app's app metadata bundle should be accurate so that it is independent from usage, app version, region, and user age. The data safety section describes the sum of the app's data collection and sharing across all geographies and user types.

#### How can the developer show that they might have different practices in different regions? For example, a developer doesn't use certain libraries in Europe, but might use them in others.

The app metadata bundle reflects the global representation of data practices per app. The data safety section describes the sum of the app's data collection and sharing across all geographies and user types.

#### Are the data safety sections gated by a consent mechanism for users? Does the developer need to take any extra steps and create an in-app prominent disclosure?

No, there is no new disclosure in the user app install process, and there is no new user consent related to this feature. Developers of Google Play apps and Mobile Bundled Apps on Android devices with Google Play services that collect personal and sensitive user data must implement in-app disclosures and consent where required by policy.

#### Does the developer need to declare data if the app includes a permission but doesn't actually collect or share the data?

The developer doesn't need to declare collection or sharing unless data is actually collected or shared. Google Play apps and Mobile Bundled Apps on Android devices with Google Play services must comply with all applicable policies.

#### If one data type is collected as part of another, should the developer declare both? For example, if the developer collected Contacts which includes the user's email, does the developer declare both the "Contacts" and "Email address" data types?

If the developer is purposefully collecting a data type during the collection of another data type, the developer should disclose both. For example, if the developer collects user photos and uses them to determine users' characteristics (such as ethnicity or race) the developer should also disclose the collection of ethnicity and race.

#### Is the developer required to provide a deletion mechanism? Must it be for any and all user data?

The data safety section provides a surface for the developer to share if the developer provides a mechanism to receive data deletion requests from users. As part of completing the data safety section, the developer should indicate if they provide such a mechanism.

#### Is there a specific type of mechanism that the developer must provide to indicate that the app supports user data deletion requests?

There is no prescribed mechanism, however as best practice, the request mechanism should be discoverable and accessible by users. Common examples of mechanisms that clearly indicate a path by which users can request data deletion can include but are not limited to: in app features, contact forms, or a dedicated email alias.

#### How should a developer indicate in the data safety section that the developer provides a request for deletion mechanism for data that is automatically deleted or anonymized?

The developer can declare that users can request can delete their data if the developer provides one or more of the following options:

- A mechanism to request data deletion.
- An automatic process to initiate deletion or anonymization of collected data within 90 days of collection.

  The developer can declare that users can request can delete their data even if the developer needs to retain certain data for legitimate reasons such as legal compliance or abuse prevention.

#### What if the deletion mechanism the developer provides is not available globally to all users --- can the developer still indicate I provide a deletion request mechanism?

Only one global data safety section is available per app metadata bundle. This should cover data practices based on any usage, region, and user age. In other words, if any of the data practices are present in any version of the app, anywhere in the world, the developer must indicate these practices. Therefore, the data safety section describes the sum of the app's data collection and sharing across all users and geographies.

#### What kinds of techniques can be used to make data anonymous?

There are a variety of potential methods to anonymize data such that it can't be associated with an individual user. The developer should consult with privacy and security experts to identify the methods applicable to their use case. As an example, this page discusses some of the data anonymization methods used by Google, such as differential privacy.

#### How should the developer treat the collection and use of IP addresses?

As with other data types, the developer should disclose the collection, use, and sharing of IP addresses based on their particular usage and practices. For example, where developers use IP addresses as a means to determine location, then that data type (location) should be declared.

#### How should the developer disclose the collection and sharing of other kinds of identifiers?

As with other data types, the developer should disclose the collection, use, and sharing of different kinds of identifiers based on the developer's particular usage and practices. For example, the collection of an account name associated with an identifiable person should be declared as a "Personal identifier," and the collection of a user's Android Advertising ID should be declared as "Device or other identifiers." As another example, an identifier related to a specific in-app event, but that doesn't reasonably relate to an individual device, browser or app, wouldn't need to be disclosed as "Device or other identifiers."

As noted previously, the collection of data pseudonymously should be disclosed in the data safety section of the app metadata bundle under the relevant data type. For example, if the developer collects diagnostic information with a device identifier, the developer should still disclose the collection of "Diagnostics" in the data safety section.

#### What kinds of activities can "service providers" perform?

A service provider can only process user data on the developer's behalf. For example, an analytics provider that processes user data from the app solely on behalf of the developer, or a cloud provider hosting user data from the app for the developer's use, typically qualify as "service providers." On the other hand, if an SDK provider is building advertising profiles across multiple customers based on app data, that wouldn't be considered "service provider" activity for purposes of the data safety section, and would need to be disclosed as "sharing" in the data safety section of the app metadata bundle.

#### An app uses an external payment service to enable financial transactions. Does the app need to disclose financial information like credit card info in its app metadata bundle?

It depends on the nature of the integration with the payment service. If the app uses a payment service such as PayPal, Google Pay, Google Play's billing system, or similar services to complete payment transactions, the developer doesn't need to declare collection of the data that the payment service collects in connection with its processing of financial transactions, such as a credit card number, if all of the following conditions are met:

- The app never accesses this information.

- The payment service collects this information directly from the user, and collection is governed by that service's terms.

The developer should review the integration with the payment service closely to ensure that the data safety section of the app metadata bundle declares any relevant data collection and sharing that doesn't meet these conditions. The developer should also consider whether the app collects other financial information, like purchase history, and whether the app receives any relevant data from the payments service, for example for risk and anti-fraud purposes.

#### An app enables users to upload their data directly to Google Drive or Dropbox for backup or storage. The app doesn't access any of this data. Should that still be disclosed as "collection"?

It depends on the particular implementation. If the user chooses to upload their data directly to their own external drive or cloud storage account (such as Google Drive, Dropbox, or similar services) and this upload is governed by the external drive or cloud storage provider's terms of service and privacy policy, and the app never collects or accesses the data in question, then the app does not need to declare the collection of this data.

#### How should the developer encrypt data in transit?

The developer should follow best industry standards to safely encrypt app data in transit. Common encryption protocols include Transport Layer Security (TLS) and Hypertext Transfer Protocol Secure (HTTPS).

#### An app lets the user create an account or add information to their account, for example, birthday or gender. How should the developer declare the data that the user adds to their account?

The developer should declare the collection of this data for account management, denoting (if applicable) where collection is optional for the user.

In addition, as with any data types collected by the app, the developer should disclose this data and the purpose or purposes for which the app uses it. For example, if the app allows a user to add a birthday to their account and also uses that data to send timely push notifications, the app should also declare this purpose in addition to account management.

Account management can be used to cover general uses of account data that are not specific to the particular app. For example, if the developer uses account information for fraud prevention, advertising, marketing, or developer communications across services, and this use is not specific to the app, or activities in the app, declaring "account management" as the purpose of collecting this account data is sufficient to cover those general uses in the data safety section of the app metadata bundle. However, the app must always declare all purposes for which the app itself uses the data. As a best practice, Google recommends disclosing how the app handles user data for account services as part of account-level documentation and the account sign-up process.

#### What are System services?

*System services* are pre-installed software that support core system features. System services should include[`transparency_info`](https://developer.android.com/about/versions/14/features/app-metadata-schema#transparency-info)and[`system_app_safety_label`](https://developer.android.com/about/versions/14/features/app-metadata-schema#system-app-safety-label-bundle)bundles (the latter is provided instead of a[`safety_labels`](https://developer.android.com/about/versions/14/features/app-metadata-schema#safety-labels-bundle)bundle). System services distributed through Google Play can apply for an exemption from completing the Google Play Data safety form.

#### How does a developer declare collection of data that is used in a transient way to load pages and service other client-side requests in real time before that data is logged on the developer's servers and used for other purposes?

If this use is[ephemeral](https://developer.android.com/about/versions/14/features/app-metadata#ephemeral-processing), the developer doesn't need to include it in the data safety section of the app metadata bundle. However, the developer must declare any use of that user data beyond the ephemeral processing, including any purposes for which the developer uses the user data that is logged.