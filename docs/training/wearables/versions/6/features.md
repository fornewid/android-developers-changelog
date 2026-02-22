---
title: https://developer.android.com/training/wearables/versions/6/features
url: https://developer.android.com/training/wearables/versions/6/features
source: md.txt
---

# Explore features

Wear OS 6 introduces several features to help enhance your Wear OS app experience. Before you add these features to your app,[prepare your app](https://developer.android.com/training/wearables/versions/6/changes)for compatibility with Wear OS 6.

## Support for Material 3 Expressive

Wear OS 6 includes a design refresh that's based on Material 3 Expressive, which is available in the latest release of the[Compose for Wear OS](https://developer.android.com/jetpack/androidx/releases/wear-compose)and[Wear OS ProtoLayout](https://developer.android.com/jetpack/androidx/releases/wear-protolayout)libraries in Jetpack.

Material 3 Expressive, supported on Wear OS 3 and higher, helps you transform the expressiveness and creativity of your app's layouts and tiles, making the most of the round form factor. Explore different shape and typography combinations, including the latest system font support, and experiment with dynamic color theming.

Material 3 Expressive also offers the following layout improvements:

- An edge-hugging button shape that invites users to take action or learn more.
- Expressive motion and more prominent scroll indicators within collections such as lists, offering more fluidity and control when selecting from a series of options.
- A multi-slot tile layout, supporting up to three columns, that creates consistency while offering customizable expressiveness of key information.

Learn more about how to migrate to Material 3 Expressive and how to follow design principles using this latest design system:

- Migrate to Material 3 Expressive in your[apps](https://developer.android.com/training/wearables/compose/migrate-to-material3)and[tiles](https://developer.android.com/training/wearables/tiles/get_started).
- Follow design principles for your[apps and tiles](https://developer.android.com/design/ui/wear/guides/foundations/common-layouts).

Try out Material 3 Expressive designs using the latest[Figma design kits](https://developer.android.com/design/ui/wear/guides/foundations/download).

## Enhancements to watch faces

Watch Face Format version 4 is supported for devices that run Wear OS 6 or higher. This version includes several enhancements:

- Support for showing photos, including user-curated collections of photos.
- Animated state transitions between ambient and interactive modes.
- A new API, Watch Face Push, for supporting a marketplace that features your watch faces.

Learn more about the[Watch Face Format](https://developer.android.com/training/wearables/wff). In the[XML reference](https://developer.android.com/training/wearables/wff/watch-face), look for items that have changed or been added in version 4.

## Continued support for features introduced in previous versions

Wear OS 6 maintains support for several key features introduced in previous versions, including the following:

- Expanded media controls---including rewind, fast-forward, and playlist shuffling---starting in Wear OS 5.1.
- [Enhanced, streamlined authentication](https://developer.android.com/training/wearables/apps/auth-wear)that supports a user's preferred authentication method, such as passkeys. They're available through the Credential Manager API, which was introduced in Wear OS 5.1.