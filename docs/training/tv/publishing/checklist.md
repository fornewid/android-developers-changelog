---
title: https://developer.android.com/training/tv/publishing/checklist
url: https://developer.android.com/training/tv/publishing/checklist
source: md.txt
---

# TV apps checklists

Users enjoy the TV app experience when it is consistent, logical, and predictable. They should be able to navigate within your app and throughout Android TV without getting lost or having to "reset" the UI and start over. Users appreciate clear, colorful, and functional interfaces that make the experience magical. With these ideas in mind, you can create an app that fits nicely in Android TV and performs as users expect.

These checklists cover the main aspects of development for both apps and games to help ensure that your app provides the best possible experience. Additional considerations for games only are covered in the[Games](https://developer.android.com/training/tv/publishing/checklist#games)section.

For the criteria that qualify an Android TV app to be distributed through Google Play, see[TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality).

## TV form factor support

These checklist items apply to games and apps.

- Identify the[main TV activity](https://developer.android.com/training/tv/get-started/create#tv-activity)with the[CATEGORY_LEANBACK_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER)filter in the manifest.
- Provide a[home screen banner](https://developer.android.com/training/tv/get-started/create#banner)for each language supported by your app, with the following characteristics:
  - Banner measures 320x180 px.
  - Banner resource is in the`drawables/xhdpi`directory.
  - Banner image includes localized text to identify the app.
- Consider whether your app needs to prevent the device from entering[Ambient Mode](https://developer.android.com/training/tv/playback/ambient-mode). This is particularly relevant for media[playback apps](https://developer.android.com/training/tv/publishing/checklist#playback-apps).
- Don't[declare a requirement](https://developer.android.com/training/tv/get-started/hardware#declare-hardware-requirements)for hardware that might be unsupported.
- Make sure your[permissions](https://developer.android.com/training/tv/get-started/hardware#hardware-permissions)don't imply hardware requirements.

## User interface design

These checklist items apply to games and apps.

- Specify activities with landscape orientation by setting`android:`[screenOrientation](https://developer.android.com/guide/topics/manifest/activity-element#screen)`="landscape"`.
- Provide appropriate[layout resources](https://developer.android.com/training/tv/playback/leanback/layouts#structure)for landscape mode.
- Make sure that[text and controls](https://developer.android.com/training/tv/playback/leanback/layouts#visibility)are large enough to be visible from a distance.
- Provide[high-resolution bitmaps and icons](https://developer.android.com/training/tv/playback/leanback/layouts#density-resources)for HDTV screens.
- Make sure your icons and logo conform to Android TV specifications.
- Allow for[overscan](https://developer.android.com/training/tv/playback/leanback/layouts#overscan)in your layout.
- When actively playing user-initiated media playback, prevent the device from entering[Ambient Mode](https://developer.android.com/training/tv/playback/ambient-mode).
- Make sure every UI element works with both D-pad and game controllers. See[TV navigation](https://developer.android.com/training/tv/get-started/navigation)and[Handle TV hardware](https://developer.android.com/training/tv/get-started/hardware#controllers).
- Change the[background image](https://developer.android.com/training/tv/playback/leanback/browse#background)as users browse through content.
- Customize the[background color](https://developer.android.com/training/tv/playback/leanback/card)to match your branding in Leanback fragments.
- Make sure that your UI does not require a touchscreen. See[Touchscreen](https://developer.android.com/training/tv/get-started/hardware#no-touchscreen)and[Declare touchscreen not required](https://developer.android.com/training/tv/get-started/create#no-touchscreen).
- Follow the[guidelines for effective advertising](https://developer.android.com/training/tv/playback/leanback/layouts#advertising).
- To guide the user through a series of decisions, use the Leanback library's[guided step API](https://developer.android.com/training/tv/playback/leanback/guided-step).

## Search and content discovery

These checklist items apply to games and apps.

- Provide[search results](https://developer.android.com/training/tv/discovery/searchable#provide)from your app in the Android TV global search box.
- Provide TV-specific[data fields](https://developer.android.com/training/tv/discovery/searchable#columns)for search.
- Make sure your app presents discovered content in a[details screen](https://developer.android.com/training/tv/discovery/searchable#details)that lets the user start watching the content immediately.

## TV home screen

These checklist items apply to the layout and content of the[home screen](https://developer.android.com/training/tv/discovery/recommendations-channel).

### Channels

- Provide a meaningful name that represents the channel's content. Don't use your app's name as a channel name.
- Don't change the channel name unless there is some interaction with the user.
- Include an associated icon for each channel. The icon doesn't need to be your app's exact icon; it can be a branded representation of the content in the channel.
- Make each channel unique, and don't mimic the functionality of the Play Next row. For example, letting users continue watching where they left off in a video is not a valid use for a channel.

### Content in channels

- Limit each program in a channel to a single piece of content. A program must not contain a collection of videos.
- Don't use programs for promotional messages or ads.
- Include a suitable description for each program, and map its metadata correctly. For example, the content rating must not appear where the title is expected.
- Don't crop or stretch preview images representing program content. They must fit one of the available[aspect ratios](https://developer.android.com/training/tv/discovery/preview-videos).
- Start playing a program as soon as the user selects it.

### Play Next

- Don't add content to the Play Next row unless the user has been interacting with it some way. For example, you can add the next episode in a series that the user is currently watching, but don't add a related but different series when the user completes the current series.
- Limit Play Next content to traditional TV shows, movies, or events. Don't add clips to the Play Next row.

## Playback apps

These checklist items apply to apps that perform media playback.

- [Register a media session](https://developer.android.com/guide/topics/media-apps/working-with-a-media-session)to inform the platform of media playback state and to let playback controls be delegated to the app.
- Set the[`FLAG_KEEP_SCREEN_ON`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON)flag while video is playing on the screen to[prevent the device from entering standby or Ambient Mode during playback](https://developer.android.com/training/tv/playback/ambient-mode#preventing-ambient-mode).
- Validate that media commands accurately expose metadata and control playback using[Media Controller Test](https://github.com/googlesamples/android-media-controller)and the[Media Session Validator](https://developers.google.com/cast/docs/android_tv_receiver/mediasession_validator).
- Comply with the[Ambient mode-related quality guidelines.](https://developer.android.com/docs/quality-guidelines/tv-app-quality#ambient-mode)Ambient Mode keeps users quietly entertained between watch sessions and prevents screen burn in.
- Profile your app's memory and make sure to check[`ActivityManager.isLowRamDevice()`](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice())for discovering low-RAM devices. For those devices, you must follow the requirements in the[Optimize memory usage guidelines](https://developer.android.com/training/tv/playback/memory).

## Games

These checklist items apply to games.

- Set the`isGame`flag in the manifest so that your game appears in the games section of the[home screen](https://developer.android.com/training/tv/games#Launcher).
- Make sure[game controller support](https://developer.android.com/training/tv/games#control)doesn't depend on the Start, Select, or Menu buttons. Not all controllers have these buttons.
- Use a generic gamepad graphic, without specific controller branding, to show[game button mappings](https://developer.android.com/training/tv/games#control).
- Check for both ethernet and Wi-Fi[connectivity](https://developer.android.com/training/basics/network-ops/reading-network-state).
- Provide users with a clean way to[exit](https://developer.android.com/training/tv/games#exit)your app.

## Distribute to Android TV

To learn how to distribute to Android TV, see the[detailed guide for publishing TV apps on Google Play](https://developer.android.com/training/tv/publishing/distribute).