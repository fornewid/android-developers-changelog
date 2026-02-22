---
title: https://developer.android.com/design/ui/tv/guides/components/cards
url: https://developer.android.com/design/ui/tv/guides/components/cards
source: md.txt
---

# Cards are the basic building blocks of your TV app.  
![Cover image for cards](https://developer.android.com/static/design/ui/tv/guides/components/images/covers/cover-cards.webp)

## Resources

|      Type      |                                                                                                                                                                                                              Link                                                                                                                                                                                                               |  Status   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Design         | [Design source (Figma)](https://goo.gle/tv-desing-kit)                                                                                                                                                                                                                                                                                                                                                                          | Available |
| Implementation | [Jetpack Compose](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary#Card(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,androidx.tv.material3.CardShape,androidx.tv.material3.CardColors,androidx.tv.material3.CardScale,androidx.tv.material3.CardBorder,androidx.tv.material3.CardGlow,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) | Available |

## Highlights

- Use a card to display content on a single topic.
- A card can hold anything from images to headlines, supporting text, buttons, lists, and other UI elements.
- A card cannot merge with another card or divide into multiple cards.
- There are six variations of cards: standard, classic, compact, inset, wide standard, and wide classic.

## Variants

There are five types of cards, each with a different use case:

1. Standard
2. Classic
3. Compact
4. Wide standard
5. Wide classic

![Standard Card](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/standard-card.webp)![Classic Card](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/classic-card.webp)![Compact Card](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/compact-card.webp)  
![Wide Standard Card](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-card.webp)![Wide Classic Card](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-classic.webp)

## Content blocks

A card's contents are arranged in distinct blocks. The card visual design including emphasis denotes hierarchy. The layout of the cards themselves accommodates the types of content the cards contain.

### Anatomy

![Content](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/content.webp)

1. Title
2. Subtitle
3. Description
4. Extra text

### Specs

![Content blocks spec](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/content-block-spec.webp)

## Standard card

### Anatomy

![Standard card spec](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/standard-card-anatomy.webp)

1. Image
2. Content block

### States

![Standard card states](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/standard-card-states.webp)

### Specs

![Standard card specs](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/standard-card-spec.webp)

## Classic card

### Anatomy

![Classic card spec](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/classic-card-anatomy.webp)

1. Image
2. Content block

### States

![Classic card states](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/classic-card-states.webp)

### Specs

![Classic card specs](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/classic-card-spec.webp)

## Compact card

### Anatomy

![Compact card spec](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/compact-card-anatomy.webp)

1. Image
2. Content block

### States

![Compact card states](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/compact-card-states.webp)

### Specs

![Compact card specs](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/compact-card-spec.webp)

## Wide standard card

### Anatomy

![Wide standard card spec](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-standard-card-anatomy.webp)

1. Image
2. Content block

### States

![Wide standard card states](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-standard-card-states.webp)

### Specs

![Wide standard card specs](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-standard-card-spec.webp)

## Wide classic card

### Anatomy

![Wide classic card spec](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-classic-card-anatomy.webp)

1. Image
2. Content block

### States

![Wide classic card states](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-classic-card-states.webp)

### Specs

![Wide classic card specs](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/wide-classic-card-spec.webp)

## Usage

Cards are versatile design elements that can be used to display a variety of content in a visually appealing and user-friendly way. The following sections explore design considerations for cards.

### Aspect ratio

There are three common aspect ratios for cards: 16:9, 1:1, and 2:3. Each aspect ratio has its strengths, so the best choice for you depends on your specific needs.

- 16:9 is the most common aspect ratio for cards. It is a wide aspect ratio that is well-suited for displaying images and videos.
- 1:1 is a square aspect ratio. It is a good choice for cards that need to be visually balanced, such as cast and crew, channel logos, or team logos.
- 2:3 is a taller aspect ratio. It is a good choice if you want to break up the grid and bring more emphasis.

Ultimately, the best way to choose an aspect ratio for your cards is to experiment with different options and see what looks best.

![Aspect ratios](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/aspect-ratio.webp)

Here are some examples usages of different aspect ratios  

### 1:1

Cast and crew
![Aspect ratio 1:1, cast and crew](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/aspect-ratio-1-1.webp)  

Sports teams logos
![Aspect ratio 1:1, sports logos](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/aspect-ratio-1-1-team.webp)

### 2:3

Trending books
![Aspect ratio 2:3, trending books](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/aspect-ratio-2-3.webp)

### 16:9

Movie cards
![Aspect ratio 16:9, moive cards](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/aspect-ratio-16-9.webp)

### Layout and spacing

Varying card widths based on the number of cards visible on the screen can be achieved by implementing proper peaking with a spacing of 20dp.  

### 1-card layout

Width of the card --- 844dp
![1 card layout](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/1-card.webp)

### 2-card layout

Width of the card --- 412dp
![2 card layout](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/2-card.webp)

### 3-card layout

Width of the card --- 268dp
![3 card layout](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/3-card.webp)

### 4-card layout

Width of the card --- 196dp
![4 card layout](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/4-card.webp)

### 5-card layout

Width of the card --- 124dp
![5 card layout](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/5-card.webp)

### Content block

The width of the content block in a card should be the same width as the image thumbnail. If you need to display more text in the content block, use a wide card variation.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/card-content-do.webp)  
check_circle

### Do

Use wide cards to show short descriptions, but only if absolutely necessary. The length of the description should be only a few words.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/card-content-dont.webp)  
cancel

### Don't

Avoid long descriptions on vertically stacked cards.

### Compact card

Compact cards should be concise and easier to read. The content preceding the background image should be brief and to the point. Avoid long titles, subtitles, or descriptions. This makes your cards more visually appealing and easier to scan.

To make text more readable on an image, add a semi-transparent black gradient overlay. This darkens the background without obscuring the image too much, making the text easier to see.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/compact-card-do.webp)  
check_circle

### Do

Compact card using scrim on top of image background.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/cards/compact-card-dont.webp)  
cancel

### Don't

Don't use compact cards without scrim on top of the background image.