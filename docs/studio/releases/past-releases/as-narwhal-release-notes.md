---
title: https://developer.android.com/studio/releases/past-releases/as-narwhal-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-narwhal-release-notes
source: md.txt
---

# Android Studio Narwhal | 2025.1.1 (June 2025)

The following are new features in Android Studio Narwhal.

## Introducing Gemini in Android Studio for businesses

Android Studio Narwhal introduces Gemini in Android Studio for businesses. Gemini in Android Studio for businesses includes the core Gemini in Android Studio features, enterprise-grade security and privacy features, and more. To unlock the power of AI for your team or business,[learn more](https://developer.android.com/gemini-for-businesses).

## Studio Labs

Android Studio Narwhal introduces*Studio Labs* , a way to discover and try out experimental AI features in stable channels. To see the available features and enable the ones you would like to use, select**Studio Labs**from the Settings menu.

See[AI features in Studio Labs](https://developer.android.com/studio/preview/gemini/labs)for descriptions of the experimental features that are currently available.

## Embedded Layout Inspector component tree enhancement

Interacting with the component tree in the Embedded Layout Inspector is now more intuitive and efficient thanks to several key improvements. These updates are designed to streamline your workflow and provide clearer insights into your Compose UI structures.

1. **Horizontal Scrolling**: You can now scroll horizontally within the component tree, making it easier to navigate and inspect wide or deeply nested layouts without losing context.
2. **Automatic Scrolling on Selection**: Selecting an item in the component tree will now automatically scroll the view, both horizontally and vertically, to bring the selected item neatly into focus. This ensures the element you're interested in is always front and center.
3. **Improved Relationship Visualization**: We've refined the support lines within the component tree to offer more explicit visual cues for understanding node relationships. Dotted lines now clearly indicate a call stack relationship between a parent and its child node, helping you trace programmatic connections more effectively. Solid lines continue to represent all other standard parent-child relationships within the tree.

These enhancements aim to provide a smoother, more efficient debugging experience, allowing you to quickly understand and refine your UI.
![The component tree in the Embedded Layout Inspector now supports horizontal scrolling and automatic scrolling on selection.](https://developer.android.com/static/studio/images/design/li-ct-enhancement.png)Embedded Layout Inspector Component Tree Enhancement