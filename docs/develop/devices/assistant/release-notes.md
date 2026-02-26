---
title: https://developer.android.com/develop/devices/assistant/release-notes
url: https://developer.android.com/develop/devices/assistant/release-notes
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

This page provides a changelog that lists new plugin and SDK releases, and
describes updates to App Actions features. To learn about specific releases,
click the links in the changelog below.

## Latest plugin versions

You can see all release notes for a given plugin version using the following
links.

| Plugin version ||
|---|---|
| **[Google Assistant plugin](https://developer.android.com/guide/app-actions/test-tool) (Recommended)** | 2.0.0 • [Release notes](https://plugins.jetbrains.com/plugin/16739-google-assistant/versions) |
| [App Actions Test Tool](https://developer.android.com/guide/app-actions/legacy/test-tool) (Legacy plugin) | 3.5.5 • [Release notes](https://plugins.jetbrains.com/plugin/12322-app-actions-test-tool/versions) |

## Latest SDK versions

You can see all App Actions release notes for a given SDK by scrolling down this
page.

| SDK Version ||
|---|---|
| [In-App Promo](https://developer.android.com/guide/app-actions/in-app-promo-sdk) | 1.0.0 |
| [App Actions Widgets Extension](https://developer.android.com/guide/app-actions/widgets#library) | 0.0.1 |

## February 26, 2024 - Streamlined BIIs

The following BIIs were deprecated in favor of more helpful BIIs. Invoking
Google Assistant using the following won't trigger an app response.

- Cancel taxi reservation
- Create contact point
- Create digital document
- Create flight reservation
- Create lodging reservation
- Create media object
- Create money transfer
- Create offer
- Create order
- Create photograph
- Create review
- Create social media connection
- Create social media posting
- Create taxi reservation
- Create thing
- Create trade order
- Get account
- Get barcode
- Get call history
- Get cart
- Get digital document
- Get financial position
- Get game observation
- Get image object
- Get invoice
- Get local business
- Get news article
- Get offer
- Get order
- Get product
- Get reservation
- Get review
- Get service observation
- Get social media posting
- Get social media profile
- Get stock quotes
- Get taxi reservation
- Order menu item
- Pay invoice
- Start game event
- Update account
- Update cart
- Update digital document
- Update order
- Update reservation
- Update software application

Also, Web inventory and Foreground App Actions are no longer supported.

## February 4, 2022

### SDK Releases

- **In-App Promo 1.0.0**

  This release removes the requirement to specify an app's Agent ID when
  defining an instance of `AssistantShortcutSuggestionsClient`.