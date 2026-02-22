---
title: https://developer.android.com/design/ui/tv/guides/components/featured-carousel
url: https://developer.android.com/design/ui/tv/guides/components/featured-carousel
source: md.txt
---

# Featured carousels showcase a selection of content relevant to the user.

![Cover](https://developer.android.com/static/design/ui/tv/guides/components/images/covers/cover-featured-carousel.webp)

## Resources

|      Type      |                                                                                                                                                                Link                                                                                                                                                                 |  Status   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Design         | [Design source (Figma)](https://goo.gle/tv-desing-kit)                                                                                                                                                                                                                                                                              | Available |
| Implementation | [Jetpack Compose](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary#Carousel(kotlin.Int,androidx.compose.ui.Modifier,androidx.tv.material3.CarouselState,kotlin.Long,androidx.compose.animation.ContentTransform,androidx.compose.animation.ContentTransform,kotlin.Function1,kotlin.Function2)) | Available |

## Highlights

- Use featured carousels to highlight specific content.
- Featured carousels can include UI elements such as images, headlines, content details, videos, actions, and pagination controls.
- Carousels are usually located on the app's homepage or landing page, which makes them readily accessible.
- Featured carousels are visually appealing to help engage the user, and create an immersive experience.
- The content displayed can be personalized based on the user's viewing history, preferences, or current trends.

## Variants

There are two different ways of integrating featured carousels:

1. Immersive
2. Card

![Immersive Featured Carousel](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/immersive-fc.webp)

![Card Featured Carousel](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/card-fc.webp)

## Content block

### Anatomy

![Content Block Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/content-block-anatomy.webp)

1. Overline text
2. Title
3. Description
4. Button

### Specs

![Content Block Immersive Spec](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/content-block-immersive-spec.webp)

## Pagination

### Anatomy

![Paginaton](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/pagination-anatomy.webp)

1. Background
2. Active element
3. Inactive elements
4. Total elements

### Specs

![Pagination Spec](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/pagination-spec.webp)

## Immersive

### Anatomy

![Immersive Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/immersive-fc-anatomy.webp)

![Immersive Background Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/immersive-fc-bg-anatomy.webp)

1. Image background
   1. Cinematic scrim
   2. Poster
   3. Background color
2. Content block
3. Pagination
4. Content grid

### Specs

![Immersive Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/immersive-fc-bg-spec.webp)

## Card

### Anatomy

![Card Featured Carousel Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/card-fc-anatomy.webp)

![Card Featured Carousel Image Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/card-fc-image-anatomy.webp)

1. Image background
   1. Cinematic scrim
   2. Poster
   3. Card background
2. Content block
3. Pagination
4. Content grid

### Specs

![Card Featured Carousel Spec](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/card-fc-spec.webp)

## Usage

Use featured carousels to showcase and promote a curated selection of content in an engaging, visually appealing, and simple to navigate format.

### Images in backgrounds

Images in backgrounds play a crucial role in enhancing user engagement in a streaming app featured carousel.

### High quality imagery

Use high-resolution images that are visually appealing and relevant to the content of the focused card.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/card-fc-text-do.webp)  
check_circle

### Do

Keep images clean, visually appealing, and relevant to the content block.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/card-fc-text-dont.webp)  
cancel

### Don't

Avoid using images with text in the background.

### Obvious visual hierarchy

Ensure that the background does not distract from the focused card's content by using a scrim over the image; this helps the user maintain focus on the card's title, description, and call-to-action button.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/visual-hierarchy-do.webp)  
check_circle

### Do

Use a scrim to improve readability and content digestion.  
![](https://developer.android.com/static/design/ui/tv/guides/components/images/carousel/visual-hierarchy-dont.webp)  
cancel

### Don't

Make sure the background doesn't affect readability and visibility of the rest of the content on the screen.