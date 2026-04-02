---
title: Explore common use cases  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/patterns/media/use-cases
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Explore common use cases Stay organized with collections Save and categorize content based on your preferences.



![](/static/wear/images/design/media-use-cases-hero.png)

When designing media apps, prioritize the following use cases. Allow users to do
the following:

* Listen to downloaded media
* Stream media from the watch

## Listen to downloaded media

The following examples show how to help users listen to downloaded media.

### Download media

Users can manually download media items from an entity page. Show the user the
download location, progress, and size.

![](/static/wear/images/design/media-use-cases-entity.png)

Entity page

![](/static/wear/images/design/media-download-prompt.png)

Size of download (Dialog)

![](/static/wear/images/design/media-download-progress.png)

Download progress

### Browse downloaded media

When the user browses media, display recently downloaded media.

![](/static/wear/images/design/media-recent-downloads.png)

Downloads

![](/static/wear/images/design/media-downloads-browse.png)

Browse

![](/static/wear/images/design/media-downloaded-entity.png)

Entity page

### Remove downloaded media

If content is already downloaded, show an action to remove the downloaded media
from the device.

![](/static/wear/images/design/media-downloaded-entity.png)

Downloaded

![](/static/wear/images/design/media-remove-download-prompt.png)

Remove download (Dialog)

![](/static/wear/images/design/media-option-to-download-again.png)

Entity page

### Select output device

If the source device is the watch, prompt users to [select audio output](/training/wearables/apps/audio#prompt-the-user-to-connect-a-headset)
before they start listening to music. After the user selects an output device,
play the media and display the output device icon—such as a headset or buds—on
the media controls.

![](/static/wear/images/design/media-player-without-output.png)

Media Player **without** output

![](/static/wear/images/design/media-output-switcher.png)

System output switcher (Dialog)

![](/static/wear/images/design/media-player-with-output.png)

Media Player **with** output

## Stream media

Streaming from the watch drains the battery. Prioritize downloaded content
when users choose to listen on the watch by displaying recently used downloads
on the browse list. Add a button that takes users to a full list of downloads,
as shown in the following images.

![](/static/wear/images/design/media-recent-downloads.png)

Prioritize downloaded content

![](/static/wear/images/design/media-downloads-button.png)

Downloads button

![](/static/wear/images/design/media-downloads-list.png)

Downloads list

For more information, see the [Media Toolkit](https://github.com/google/horologist/tree/main/media) on GitHub.