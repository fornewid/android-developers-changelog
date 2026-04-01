---
title: https://developer.android.com/games/playgames/ad-guidance
url: https://developer.android.com/games/playgames/ad-guidance
source: md.txt
---

Google Play Games on PC allows users to experience Android games on Windows PC
environments. Many popular Android games are supported by in-app advertising.
Google Play Games on PC aims to continue supporting in-game advertising without
app changes and offers additional functionality for ad buyers and sellers to
identify and separate Google Play Games on PC from physical Android devices so
that these requests may be handled with any wanted changes.

## Differences to consider with Google Play Games on PC

While Google Play Games on PC runs standard Android games, users experience
these games differently due to the PC hardware they use to play them. Examples
of these differences include:

- Games are played on a much larger screen than any mobile device.
- Keyboards and mice are the common input devices.
- For ads that promote mobile apps, users may not be able to install these apps on their PC.

## Ad providers

As an ad provider with an Android SDK, you may see incoming ad requests from
Android apps published on Google Play Games on PC. As documented in the
[Developer's Guide](https://developer.android.com/games/playgames/overview), Google Play Games on PC
emulator Android environments. Existing SDKs that function in Android today
should continue to function in Google Play Games on PC without changes.
However, because users will be experiencing your ads on a desktop PC, you may
want to consider changes to how ads display or what happens when a user clicks
on an ad.

> [!NOTE]
> **Note:** Google Play recommends you think carefully through the user experiences your SDK facilitates and how these should best be optimized for your users. Alternatively, you can choose to simply refrain from serving ads to requests from games on Google Play Games on PC. To do so, see the following section on how to identify requests from Google Play Games on PC.

### Identifying requests from games running on Google Play Games on PC

Use the [Play Integrity API](https://developer.android.com/google/play/integrity/setup#sdks) to
see whether a requests is coming from a verified instance of
Google Play Games on PC. Note that they Play Integrity API can also
be used to verify that the runtime environment is trusted.

## Ad buyers

As an ad buyer considering purchasing Android game inventory, you may want to
target, exclude or alter your bidding strategies for inventory that is
experiences on Google Play Games on PC, which runs on Windows PCs.

### Identifying inventory from apps running on Google Play Games on PC

Devices running in Google Play Games on PC will exhibit specific
characteristics in their User Agent such as
"`Mozilla/5.0 (Linux; Android 12; HPE device Build/SKR1.230204.001.A4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 (Mobile; afma-sdk-a-v230914118.230914118.0),gzip(gfe),gzip(gfe)`". The Platform
will be reported as 'Windows'.

### Preparing ad campaigns for Google Play Games on PC

Review the developer's guide for [graphics on Google Play Games on PC](https://developer.android.com/games/playgames/graphics#large-screen-optimization) and consider whether to
add or adjust assets that will bid on this inventory.

## Frequently Asked Questions

- **Question: Which ad providers and/or buyers are supported for
  Google Play Games on PC?**
  - Google Play Games on PC should be considered a limited extension of the Android platform. Any ad buyer/seller that can support Android platforms can work with Google Play Games on PC. Note that buyers and sellers may wish to consider different behavior for requests from apps running Google Play Games on PC, and this can be accommodated by the means provided above to identify and separate this inventory from standard Android platforms.
- **Question: Can app-install ads be shown to users in Google Play Games on PC?
  How does the user install the app?**
  - Each ad provider should decide on their own which types of advertising they want to facilitate for requests from Google Play Games on PC. In some cases, users may be able to install apps to their devices from an app store page on the open web.