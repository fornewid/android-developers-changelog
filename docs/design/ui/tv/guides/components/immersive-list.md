---
title: https://developer.android.com/design/ui/tv/guides/components/immersive-list
url: https://developer.android.com/design/ui/tv/guides/components/immersive-list
source: md.txt
---

# Immersive list is a combination of a row of content \& preview of the selected item. It features content in a larger viewport.

![Cover](https://developer.android.com/static/design/ui/tv/guides/components/images/covers/cover-immersive-list.webp)

## Resources

|      Type      |                                                                                                  Link                                                                                                   |  Status   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Design         | [Design source (Figma)](https://goo.gle/tv-desing-kit)                                                                                                                                                  | Available |
| Implementation | [Sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:tv/samples/src/main/java/androidx/tv/samples/ImmersiveListSamples.kt;drc=5920fece16ad6723107098f24a492a25937cd51a) | N/A       |

## Highlights

- Dynamic content preview. When a user navigates through the row of content, the preview area automatically update to display the current focused item.
- The Immersive list component features a larger viewport for displaying content, making it easier for users to view and appreciate the visual details of the focused item.
- Immersive lists provide relevant and contextual information about the focused item, helping users make informed decisions without leaving the browsing experience.
- The Immersive list component uses progressive disclosure to reveal more details about the content as users navigate, reducing cognitive load and maintaining user engagement.
- The Immersive list component ensures consistent interactions across the app, providing users with a familiar and predictable experience.

## Anatomy

![Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-anatomy.webp)

1. Image background
2. Content block
3. Card on focus
4. Content grid

![Image anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-image-anatomy.webp)

1. Cinematic scrim
2. Poster
3. Background color

## Specs

![Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-specs.webp)

## Behavior

When navigating between cards in the Immersive list, the details of the selected card are progressively revealed in the background.  

When the immersive list is in focus, its height increases to reveal additional information, such as the background title and description, as shown in the following video.

## Usage

Use immersive carousels when you want to draw attention to featured or promoted content, such as new releases, popular shows, or exclusive titles. The larger viewport and dynamic preview provide a compelling way to showcase these high-priority items.

### Image display

![Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-image-display.webp)

1. **Card focus**: As the user navigates through the carousel, the focused card is visually emphasized, scaling the card by 1.1, using a border, and other visual cues as elevation to indicate its selection. Ensure content titles inside the thumbnail of the focused card are clearly visible and easier to read.
2. **Background image**: When a card is in focus, a corresponding background image is displayed in the larger viewport. We recommend this background image is high-quality and visually appealing, as it provides an immersive and engaging backdrop for the content.

### Composition

![](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-image-composition-do.webp)  
check_circle

### Do

Scale and align the subject to the top right corner creating a cinematic experience.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-image-composition-dont.webp)  
cancel

### Don't

Avoid using full screen crop that will make crop the subject under the content.

To ensure the images used as backgrounds in the Immersive list component look good, make sure to scale them appropriately so they are not blurry or distorted.

### Aspect ratio

Use a 16:9 ratio for background images whenever possible to ensure a visually appealing and consistent layout.

![Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/immersive-list/immersive-list-ratio.webp)