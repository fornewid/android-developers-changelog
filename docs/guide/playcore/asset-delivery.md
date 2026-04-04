---
title: https://developer.android.com/guide/playcore/asset-delivery
url: https://developer.android.com/guide/playcore/asset-delivery
source: md.txt
---

### Play Asset Delivery

*Play Asset Delivery (PAD)*brings the benefits of app bundles to games. It allows games larger than 200MB to replace legacy expansion files (OBBs) by publishing a single artifact to Play containing all the resources the game needs. PAD offers flexible delivery modes, auto-updates, compression, and delta patching, and is free to use. Using PAD, all asset packs are hosted and served on Google Play removing the need to use a content delivery network (CDN) to get your game resources to players.

Play Asset Delivery uses asset packs, which are composed of assets (such as textures, shaders, and sounds), but no executable code. Through Dynamic Delivery, you can customize how and when each asset pack is downloaded onto a device according to three delivery modes: install-time, fast-follow, and on-demand.

If you want to jump directly to implementing PAD in your game, see[Next step](https://developer.android.com/guide/playcore/asset-delivery#next-step-instructions).
![](http://developer.android.com/static/images/picto-icons/distribution.svg)  

#### Single publishing artifact

Publish a single artifact to Play including all your game's resources  
![](http://developer.android.com/static/images/picto-icons/pathway.svg)  

#### Flexible delivery modes

Control when and how Play delivers your game assets  
![](http://developer.android.com/static/images/picto-icons/frame.svg)  

#### Texture compression format targeting

Start making efficient use of the available hardware while not sacrificing reach  
![](http://developer.android.com/static/images/spot-icons/tools-update.svg)  

#### Automatic updates

Let Play auto-update your game assets with advanced compression and delta patching

## Answers to commonly-asked questions

## Delivery modes

**`install-time`**asset packs are delivered when the app is installed. These packs are served as split APKs (part of the APK set). These packs are also known as "upfront" asset packs; you can use these packs immediately at app launch. These packs contribute to the app size listed on the Google Play Store. These packs can't be modified or deleted by the user.

**`fast-follow`** asset packs are downloaded automatically as soon as the app is installed; the user does not have to open the app for`fast-follow`downloads to begin. These downloads do not prevent the user from entering the app. These packs do not contribute to the app size listed on the Google Play Store.

**`on-demand`**asset packs are downloaded while the app is running.

Asset packs configured as`fast-follow`and`on-demand`are served as archive files by the Google Play Store (and not as split APKs). These packs are then expanded in the app's internal storage. You can query the location of asset packs served this way using the[Play Asset Delivery Library](https://developer.android.com/guide/playcore#java-kotlin-asset-delivery). The app can't assume the existence of these files or their locations because these files may be deleted by the user or moved by the Play Asset Delivery Library across play sessions. Even though these files are writable by the app, you should treat them as read-only since asset pack patches depend on the integrity of these files. These packs do not contribute to the app size listed on the Google Play Store.

When using Play Asset Delivery in an[instant app](https://developer.android.com/gtopic/google-play-instant/overview), on-demand is the only supported mode.
| **Note:** To successfully install or update an app, Android requires a certain amount of free disk space on the device.`install-time`asset packs have the same requirements as the base APK, which**require at least two times the size of all the asset packs** . On the other hand,`fast-follow`and`on-demand`asset packs require only a few hundred extra MBs.
|
| Minimize the size of your`install-time`asset packs to avoid the situation where users have to free up space to install or update your apps.

## Asset updates

When the app is updated,`install-time`asset packs are updated as part of the base app update (with no action needed from the developer).

App updates for`fast-follow`and`on-demand`asset packs follow these steps:

1. The patch for the app, including all assets, is downloaded to a secure location on the device.
2. The app binary is updated; this includes any`install-time`asset packs.
3. All previously-downloaded asset packs are invalidated.
4. The patch for the assets is copied and applied to assets stored in the app's internal storage.

In most cases when the user opens the game, the entire update has already completed and the user can start playing the updated version immediately. In rare cases, when the app is opened, the app binary may have already been updated while the process of applying the patch for the assets has not yet completed and thus assets are not ready to be accessed. You need to accommodate this scenario by providing an appropriate "Update in progress" user interface element around these assets, or build in logic to deal with invalidated assets that are not ready to be accessed. Since the app binary update takes place only after all asset pack types have been downloaded, applying the patch is a local, offline action that should complete quickly.

## Texture compression format targeting

Texture Compression is a form of lossy image compression that allows the GPU to render directly from the compressed texture with dedicated hardware, reducing the amount of texture memory and memory bandwidth required.[Texture Compression Format Targeting](https://developer.android.com/guide/app-bundle/asset-delivery/texture-compression)lets you include textures compressed with multiple texture compression formats in your Android App Bundle and rely on Google Play to automatically deliver the assets with the best supported texture compression format for each device.

## App version updates

After a new version of an app is uploaded to Google Play, it is possible for the user to open the previous version of the app before it's updated on the device. If required, in such cases, the app can choose to force an update or recommend an update by calling the[In-App Updates API](https://developer.android.com/guide/app-bundle/in-app-updates). This API allows you to trigger an update from within the app rather than the user triggering the update from the Google Play Store.

## Download size limits

Asset packs are ideal for large games due to their increased size limits. Higher size limits are also possible for developers who are part of[Google Play Partner Program for Games](https://play.google.com/console/about/programs/partnerprogram/). You can find more information on the maximum sizes at[Google Play maximum size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits).

If you use[Texture Compression Format Targeting](https://developer.android.com/guide/app-bundle/asset-delivery/texture-compression), these download limits apply separately to each unique texture format.

## Next step

Build Play Asset Delivery into your game or app using one of the following:  
[Get started for Java](https://developer.android.com/guide/app-bundle/asset-delivery/build-native-java)[Get started for Native](https://developer.android.com/guide/app-bundle/asset-delivery/build-native-java)[Get started for Unity](https://developer.android.com/guide/app-bundle/asset-delivery/build-unity)

<br />

## Terms of service and data safety

By accessing or using the Play Asset Delivery Library, you agree to the[Play Core Software Development Kit Terms of Service](https://developer.android.com/guide/playcore#license). Please read and understand all applicable terms and policies before accessing the library.

The Play Core libraries are your app's runtime interface with the Google Play Store. As such, when you use Play Core in your app, the Play Store runs its own processes, which include handling data as governed by the[Google Play Terms of Service](https://play.google.com/about/play-terms/index.html). The information below describes how the Play Core libraries handle data to process specific requests from your app.

#### Play Asset Delivery

|----------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Data collected on usage    | Device metadata Application version                                                                                           |
| Purpose of data collection | The data collected is used to serve the right asset pack to the device and to preserve installed asset packs after an update. |
| Data encryption            | Data is encrypted.                                                                                                            |
| Data sharing               | Data is not transferred to any third parties.                                                                                 |
| Data deletion              | Data is deleted following a fixed retention period.                                                                           |

While we aim to be as transparent as possible, you are solely responsible for deciding how to respond to Google Play's data safety section form regarding your app's user data collection, sharing, and security practices.

## More resources

[![](http://developer.android.com/static/images/distribute/stories/Devsisters_PAD_thumbnail.png)](http://developer.android.com/stories/games/devsisters)  
Case Study  

#### Cookie Run: OvenBreak saves over $200K CDN cost with Play Asset Delivery

Devsisters is a mobile game developer and publisher, producing casual games based on the Cookie Run IP. Learn how they decreased their game's unnecessary resources with Play Asset Delivery.  
[Learn more](http://developer.android.com/stories/games/devsisters)  
[![](http://developer.android.com/static/images/cards/distribute/stories/cat-daddy-games-logo.png)](http://developer.android.com/stories/games/cat-daddy)  
Case Study  

#### 2K delivers higher quality graphics with Play Asset Delivery

Cat Daddy Games is a wholly-owned 2K studio based in Kirkland, Washington. The teams behind the NBA 2K Mobile, NBA SuperCard, and WWE SuperCard series were looking for a solution to improve the overall quality of their games for users,  
[Learn more](http://developer.android.com/stories/games/cat-daddy)  
[![](http://developer.android.com/static/images/cards/distribute/stories/cdpr-thumbnail.png)](http://developer.android.com/stories/games/cdpr)  
Case Study  

#### CD Projekt RED reduces update size by 90% and increases update rates by 10% with Play Asset Delivery

Based in Warsaw, Poland, game developer CD Projekt RED (CDPR) reimagined their mini-game in The Witcher 3, GWENT: The Witcher Card Game, to launch as a standalone free-to-play title on Google Play in March of 2020.  
[Learn more](http://developer.android.com/stories/games/cdpr)  
[![](http://developer.android.com/static/images/cards/distribute/stories/puzzle-kids-framed.png)](http://developer.android.com/stories/games/rv-appstudios-pad)  
Case study  

#### RV AppStudios improves user retention with Google Play Asset Delivery

US-based developer RV AppStudios has over 200 million downloads to date across their portfolio of casual games, educational kids apps, and utility apps.  
[Learn more](http://developer.android.com/stories/games/rv-appstudios-pad)  
[![](http://developer.android.com/static/images/cards/distribute/stories/gameloft-asphalt8.jpg)](http://developer.android.com/stories/games/gameloft-pad)  
Case study  

#### Gameloft acquires 10% more new users with Google Play Asset Delivery

In 2000, Gameloft was created with a passion for games and a desire to bring them to players around the world.  
[Learn more](http://developer.android.com/stories/games/gameloft-pad)  
Video  

#### Google Play Asset Delivery for games

Optimize your game delivery with the new App Bundle for games, which enables free, customizable delivery of large game assets.  
[Watch on YouTube](https://www.youtube.com/watch?v=WW9GevpEo1s)