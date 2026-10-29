---
title: https://developer.android.com/wear/gallery/media
url: https://developer.android.com/wear/gallery/media
source: md.txt
---

# Media

![](http://developer.android.com/static/images/wear/gallery/icons/media.svg)  

### Media

Take your music, leave your phone. The watch is the ultimate on-body controller that gives people quick access to media.

## Apps to keep you connected to everywhere

![](http://developer.android.com/static/images/wear/gallery/media/working-out.png)  

### Working out

Media is commonly used when people are working out. The watch is faster to access than the phone.  
![](http://developer.android.com/static/images/wear/gallery/media/home-devices.png)  

### Around the house

Homes are often filled with smart devices. The smartwatch can become the ultimate on-body controller for people around their home.  
![](http://developer.android.com/static/images/wear/gallery/media/common-on-the-go.png)  

### On the go

People usually control media from the watch while on the go. Common scenarios include commuting, gym, walking.

*** ** * ** ***

## Help people listen to media without their phone.

![](http://developer.android.com/static/images/wear/gallery/media/media-watches-callout.png)Smartwatches are a great way for people to quickly control the media in their lives. Research shows that smartwatch interactions tend to be short, but frequent, so the glanceability of a media experience matters  
[Media design guidelines](http://developer.android.com/training/wearables/design/media-apps)![](http://developer.android.com/static/images/wear/gallery/media/browse-watch.png)  

### Browse

Help people find media on their smartwatch. Prioritize content so that the most likely media choice is at the top of the app.

Help people quickly start or resume a media session by leaning into highly engaging surfaces such as tiles and complications.  
[Create lists on Wear OS](http://developer.android.com/training/wearables/compose/lists)[Golden Tile Developer Implementation](https://github.com/android/wear-os-samples/pull/450)![](http://developer.android.com/static/images/wear/gallery/media/download-watch.png)  

### Download

Be sure to indicate download progress using the Ongoing Activity API. This gives the user assurance and understanding of what is happening on their watch.  
[Media download service](https://google.github.io/horologist/media-data/)[Creating ongoing activities on Wear](http://developer.android.com/training/wearables/notifications/ongoing-activity)![](http://developer.android.com/static/images/wear/gallery/media/starting-media-watch.png)  

### Starting media

People expect their Wear OS app to be fast. Use a placeholder UI to mask latency on your watch.

Playing media from the watch speaker doesn't provide a great experience. Instead, when people initiate a media session, prompt them to select a more suitable output device, such as headphones.  
[Handling latency on Wear OS](http://developer.android.com/training/wearables/design/launch)[Detect audio devices](http://developer.android.com/training/wearables/apps/audio)[Horologist PlaceholderChip](https://github.com/google/horologist/blob/f24c424766ae78da8cd069080e325e045855879c/composables/src/main/java/com/google/android/horologist/composables/PlaceholderChip.kt)![](http://developer.android.com/static/images/wear/gallery/media/media-controls-watch.png)  

### Media controls

Because most people have more than one media app, Wear OS provides an adaptable media control layout, so you can make media controls consistent from app to app.  
[Media controller](https://google.github.io/horologist/simple-media-app-guide/#display-a-playerscreen)[Horologist Player Screen](https://github.com/google/horologist/blob/main/media/ui/src/main/java/com/google/android/horologist/media/ui/screens/player/PlayerScreen.kt)[Volume control on Wear](https://github.com/google/horologist/blob/main/media/audio-ui/src/main/java/com/google/android/horologist/audio/ui/VolumeScreen.kt)

## Proven Design Patterns

[![](http://developer.android.com/static/images/wear/gallery/media/media-controls-frame.png)](https://google.github.io/horologist/simple-media-app-guide/#display-a-playerscreen)  

### [Media Controls](https://google.github.io/horologist/simple-media-app-guide/#display-a-playerscreen)

Adapt and build using our media controller layout so people do not have to re-learn basics from app to app.  
[Media controller](https://google.github.io/horologist/simple-media-app-guide/#display-a-playerscreen)  
[![](http://developer.android.com/static/images/wear/gallery/media/volume-controls-frame.png)](https://github.com/google/horologist/blob/main/media/audio-ui/src/main/java/com/google/android/horologist/audio/ui/VolumeScreen.kt)  

### [Volume Control](https://github.com/google/horologist/blob/main/media/audio-ui/src/main/java/com/google/android/horologist/audio/ui/VolumeScreen.kt)

Enable people to quickly and easily control volume using rotary input on the smartwatch.  
[Volume control on Wear OS](https://github.com/google/horologist/blob/main/media/audio-ui/src/main/java/com/google/android/horologist/audio/ui/VolumeScreen.kt)  
[![](http://developer.android.com/static/images/wear/gallery/media/output-devices-frame.png)](http://developer.android.com/training/wearables/apps/audio)  

### [Output devices](http://developer.android.com/training/wearables/apps/audio)

Launch the settings fragment so people can choose their output device before the media starts. Playing media from the watch speaker doesn't provide a great experience.  
[Detect audio devices](http://developer.android.com/training/wearables/apps/audio)  
[![](http://developer.android.com/static/images/wear/gallery/media/tiles-frame.png)](https://github.com/android/wear-os-samples/tree/main/WearTilesKotlin)  

### [Tiles](https://github.com/android/wear-os-samples/tree/main/WearTilesKotlin)

The Wear OS golden tile layouts and complication templates can help people quickly initiate media sessions. Prioritize access to downloaded content to preserve users' battery life.  
[Golden Tile samples](https://github.com/android/wear-os-samples/tree/main/WearTilesKotlin)

## What customers are saying

![](https://developer.android.com/static/images/wear/gallery/icons/wear-spotify.png)  
Spotify believes that Wearables will be more and more important in the future, and they see their investment in Wear OS as absolutely essential.  
[Explore on Google Play](https://play.google.com/store/search?q=spotify&c=apps)

## Build better withAndroid

[![](http://developer.android.com/static/images/wear/gallery/nav/messaging.png)](http://developer.android.com/wear/gallery/messaging)  
[![](http://developer.android.com/static/images/wear/gallery/icons/messaging.svg)](http://developer.android.com/wear/gallery/messaging)  

### [Messaging](http://developer.android.com/wear/gallery/messaging)

People want to stay connected. A messaging experience enables reliable, helpful and safe communication from your smartwatch.  
[Learn more](http://developer.android.com/wear/gallery/messaging)  
[![](http://developer.android.com/static/images/wear/gallery/nav/fitness-health.png)](http://developer.android.com/wear/gallery/health-fitness)  
[![](http://developer.android.com/static/images/wear/gallery/icons/fitness-health.svg)](http://developer.android.com/wear/gallery/health-fitness)  

### [Health \& Fitness](http://developer.android.com/wear/gallery/health-fitness)

Help people live healthier lives by tracking workouts and setting fitness goals.  
[Learn more](http://developer.android.com/wear/gallery/health-fitness)