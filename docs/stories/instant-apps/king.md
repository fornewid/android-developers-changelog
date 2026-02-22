---
title: https://developer.android.com/stories/instant-apps/king
url: https://developer.android.com/stories/instant-apps/king
source: md.txt
---

# King improves player acquisition with Google Play Instant

![](https://developer.android.com/static/images/distribute/stories/bubble-witch-3-saga-icon.png)

[King](https://king.com/)is a leading interactive entertainment company, with popular mobile games such as Candy Crush Saga, Farm Heroes Saga and Bubble Witch 3 Saga. In March 2018, King implemented Google Play Instant and was excited to see the potential impact on removing user acquisition friction, targeting audiences more efficiently, and increasing the effectiveness of game cross-promotion.

They launched an instant version of Bubble Witch 3 Saga (BW3S), which is easily accessible to play by clicking the "Try Now" button on its Play Store listing.

### What they did

![](https://developer.android.com/static/images/distribute/stories/bubble-witch-3-saga.png)

King was able to reduce the \~79MB installed version of BW3S to under \~20MB in a couple of weeks, and eventually reduced it to 15MB by stripping out all but the first five levels, removing cut scenes, eliminating unused code with better ProGuard rules, optimizing their LLVM compiler flags, and reducing the number of supported languages.

Finally, the team managed to reduce BW3S under Google Play Instant's 10MB limit by splitting their game into a 7MB base APK, and programmatically downloading the remaining 8MB of gameplay assets after the main menu assets are loaded.

### Results

Since launching their Google Play Instant version of Bubble Witch 3 Saga, click-throughs from the Play Store details page has increased.

Encouraged by these results, King is planning to bring instant app technology to more games, and enabling cross promotions to directly launch instant experiences.

David Fernandez Remesal, Executive Producer, commented:

*"Instant Games will definitely remove friction in user acquisition through organic, cross-promotion and paid media, making King more efficient and effective in targeting audiences for our broad games portfolio.*

*Most of future and current King franchises (Candy Crush, Bubble Witch, Farm Heroes, Pet Rescue) could benefit from this initiative."*

### Get started

Instant apps will be broadly available for games in the coming months.[Sign up here](https://docs.google.com/forms/d/e/1FAIpQLSeUodw6iqSKppOtm22vYwCgAnngES9lXV6821UBlF2bM3r-wg/viewform)to apply for the beta and more information as it is available.