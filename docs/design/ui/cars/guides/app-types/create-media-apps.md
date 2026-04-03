---
title: https://developer.android.com/design/ui/cars/guides/app-types/create-media-apps
url: https://developer.android.com/design/ui/cars/guides/app-types/create-media-apps
source: md.txt
---

# Create media apps

Media apps designed with Android for Cars help drivers find and control their favorite media while keeping their eyes on the road.

There are two ways to create media apps with Android for Cars. For greater control over the user interface, flow, and branding of your app, use the Car App Library templates as guardrails to help you bring the best of your media app to the car.

If you'd prefer a more straightforward approach with less customization, use the[Media Browser Service](https://developer.android.com/design/ui/cars/guides/app-types/create-media-apps#mediabrowserservice).

## Do more with Car App Library templates

[Car App Library (CAL)](https://developer.android.com/training/cars/apps)templates allow for more in-app customization and flexibility to bring more features to your media app.
| **Important:** Templated media apps are in beta testing. You can publish templated media apps to both internal and closed testing tracks on the Play Store. Publishing to open tracks and production tracks is not permitted. You can[nominate yourself to become an early access partner](https://docs.google.com/forms/d/e/1FAIpQLSf0z4Nfw8wrloVhlgHDpLgdkg4WXsFj9ni5c1pw0qTvJ3Q4fQ/viewform).

The following templates in particular will help you create a great media experience:

- **Sectioned Item template:** The[Sectioned Item template](https://developer.android.com/design/ui/cars/guides/templates/sectioned-item-template)lets you mix and match lists and grids to create a customized browsing structure. To get the latest updates and features, move any existing instances of the list or grid templates into the sectioned item template.
- **Media Playback template:** With the[Media Playback template](https://developer.android.com/design/ui/cars/guides/templates/media-playback-template), you can decide which actions can be performed from the playback screen. You can choose which buttons to show in the search results section and which playback buttons and images to show (provided through media session).
- **Sign-in template:** The[Sign-in template](https://developer.android.com/design/ui/cars/guides/templates/sign-in-template)presents options for signing in to the app while parked.
- **Tab template:** The[Tab template](https://developer.android.com/design/ui/cars/guides/templates/tab-template)acts as a container for other templates, providing tabs across the top.

![Media playback example](https://developer.android.com/static/images/design/ui/cars/app-cuj/create-media-apps-1.png)Sample showing a list and a grid in a media app.![Example of Media playback](https://developer.android.com/static/images/design/ui/cars/app-cuj/create-media-apps-2.png)Sample showing the now playing view of a media app.

<br />

## Media Browser Service

If you'd prefer to create a more basic media app with limited branding and customization, use`MediaBrowserService`(MBS).

Because the basic visual design and interaction model for much of the Android for Cars media experience is determined by Google and car makers, your role in design is mostly focused on:

- **Creating a browsing structure**for the content
- **Supplying branding elements and icons**for navigational tabs and custom controls (if needed)
- Depending on your app, you may need to create additional flows, such as a[sign-in flow](https://developer.android.com/design/ui/cars/guides/flows/create-sign-in-flow)or[settings](https://developer.android.com/design/ui/cars/guides/flows/create-settings)for the car screen (for AAOS) using the templates in the Car App Library (CAL).

**Optional step for Android Auto**:

- [Provide recommendations](https://developer.android.com/design/ui/cars/guides/app-types/provide-recommendations): Choose 10 items of media content to showcase as recommendations.

## Media app UX requirements

To learn more about media app requirements, review these resources:

- [Create your media app](https://developer.android.com/design/ui/cars/guides/app-types/media-apps)
- [Division of roles](https://developer.android.com/design/ui/cars/guides/app-types/media-apps#roles)
- [Branding elements requirements](https://developer.android.com/design/ui/cars/guides/app-types/branding-elements#requirements)
- [Browsing views elements](https://developer.android.com/design/ui/cars/guides/app-types/plan-browsing-views#browsing-view-req)
- [Playback controls requirements](https://developer.android.com/design/ui/cars/guides/app-types/customize-playback-controls#playback-control-requirements)
- [Queue requirements](https://developer.android.com/design/ui/cars/guides/app-types/customize-playback-controls#queue-requirements)
- [Settings requirements](https://developer.android.com/design/ui/cars/guides/flows/create-settings)
- [Navigation requirements](https://developer.android.com/design/ui/cars/guides/app-types/navigation-tabs)
- [Recommendation requirements](https://developer.android.com/design/ui/cars/guides/app-types/provide-recommendations#requirements)
- [Sign-in flow requirements](https://developer.android.com/design/ui/cars/guides/flows/create-sign-in-flow#requirements)
- [Voice action requirements](https://developer.android.com/design/ui/cars/guides/ux-requirements/voice-actions#voice-action-req)