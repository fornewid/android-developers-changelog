---
title: https://developer.android.com/design/ui/wear/guides/patterns/media/use-cases
url: https://developer.android.com/design/ui/wear/guides/patterns/media/use-cases
source: md.txt
---

# Explore common use cases

![](https://developer.android.com/static/wear/images/design/media-use-cases-hero.png)

When designing media apps, prioritize the following use cases. Allow users to do
the following:

- Listen to downloaded media
- Stream media from the watch

## Listen to downloaded media

The following examples show how to help users listen to downloaded media.

### Download media

Users can manually download media items from an entity page. Show the user the
download location, progress, and size.  
![](https://developer.android.com/static/wear/images/design/media-use-cases-entity.png)

<br />

Entity page

![](https://developer.android.com/static/wear/images/design/media-download-prompt.png)

<br />

Size of download (Dialog)

![](https://developer.android.com/static/wear/images/design/media-download-progress.png)

<br />

Download progress

<br />

### Browse downloaded media

When the user browses media, display recently downloaded media.  
![](https://developer.android.com/static/wear/images/design/media-recent-downloads.png)

<br />

Downloads

![](https://developer.android.com/static/wear/images/design/media-downloads-browse.png)

<br />

Browse

![](https://developer.android.com/static/wear/images/design/media-downloaded-entity.png)

<br />

Entity page

<br />

### Remove downloaded media

If content is already downloaded, show an action to remove the downloaded media
from the device.  
![](https://developer.android.com/static/wear/images/design/media-downloaded-entity.png)

<br />

Downloaded

![](https://developer.android.com/static/wear/images/design/media-remove-download-prompt.png)

<br />

Remove download (Dialog)

![](https://developer.android.com/static/wear/images/design/media-option-to-download-again.png)

<br />

Entity page

<br />

### Select output device

If the source device is the watch, prompt users to [select audio output](https://developer.android.com/training/wearables/apps/audio#prompt-the-user-to-connect-a-headset)
before they start listening to music. After the user selects an output device,
play the media and display the output device icon---such as a headset or buds---on
the media controls.  
![](https://developer.android.com/static/wear/images/design/media-player-without-output.png)

<br />

Media Player **without** output

![](https://developer.android.com/static/wear/images/design/media-output-switcher.png)

<br />

System output switcher (Dialog)

![](https://developer.android.com/static/wear/images/design/media-player-with-output.png)

<br />

Media Player **with** output

<br />

## Stream media

Streaming from the watch drains the battery. Prioritize downloaded content
when users choose to listen on the watch by displaying recently used downloads
on the browse list. Add a button that takes users to a full list of downloads,
as shown in the following images.  
![](https://developer.android.com/static/wear/images/design/media-recent-downloads.png)

<br />

Prioritize downloaded content

![](https://developer.android.com/static/wear/images/design/media-downloads-button.png)

<br />

Downloads button

![](https://developer.android.com/static/wear/images/design/media-downloads-list.png)

<br />

Downloads list

<br />

For more information, see the [Media Toolkit](https://github.com/google/horologist/tree/main/media) on GitHub.