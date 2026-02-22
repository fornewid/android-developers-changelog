---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/cards
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/cards
source: md.txt
---

# Cards

![](https://developer.android.com/static/wear/images/cards/cards-hero.png)

The [Card](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#Card(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.painter.Painter,androidx.compose.ui.graphics.Color,kotlin.Boolean,androidx.compose.foundation.layout.PaddingValues,androidx.compose.ui.graphics.Shape,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.semantics.Role,kotlin.Function1)) component contains content and actions about a single subject.

## Anatomy

![](https://developer.android.com/static/wear/images/cards/cards-anatomy.png)  
A card component only has a single slot. Cards can contain icons, images or labels, are customizable.

By default, cards are rectangular with rounded corners and a gradient background. Set the maximum height of your card to 60% to ensure that it's fully displayed on the screen because circular displays can clip up to 20% of the top and bottom of the screen.

<br />

<br />

![](https://developer.android.com/static/wear/images/cards/cards-related-components-title-card.png) ![](https://developer.android.com/static/wear/images/cards/cards-related-components-app-card.png)  
**Title Card**

Use [Title cards](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#TitleCard(kotlin.Function0,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.graphics.painter.Painter,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) to show information within an application, such as a message. Title cards have a three-slot layout which includes a title, an optional time field, and the relevant content, which is either an image or text.  
**App Card**

Use [App cards](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#AppCard(kotlin.Function0,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.graphics.painter.Painter,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) to show interactive elements from multiple applications. App cards have a five-slot layout that includes an application icon, the application name, the time that the activity occurred, a title of some sort and the relevant content, which is either an image or text.

<br />

<br />

## Cards gradient

![](https://developer.android.com/static/wear/images/cards/Colour_Gradient_1.png)  
**Card Gradient**

Top/Left + 68dp padding from Left = 100% Surface  

Bottom/Right = 0% Surface

<br />

<br />

![](https://developer.android.com/static/wear/images/cards/Colour_Gradient_2.png)  
**Image Card Overlay**

Top/Left + 56 dp padding from T/L = 100% Surface   

Bottom/Right + 24 dp padding from B/R = 0% Surface  

(Gradient overlays on a image background)

<br />

<br />

## Sizes

![](https://developer.android.com/static/wear/images/cards/cards-sizes.png)  
**Card width**

Cards default to the maximum width of the container.

<br />

**Card height**

<br />

Card height is flexible. It is determined by the components' content.

On round watch faces, cards that are taller than 60% of the height of the screens are clipped.

<br />

<br />

## Usage

![](https://developer.android.com/static/wear/images/cards/cards-usage-cards.png)

## Adaptive layouts

![](https://developer.android.com/static/wear/images/cards/cards-large-screen-usage.png)

**TitleCard**

On larger screens we allow an extra line of text for body copy. And in order to display more of the image, add an enlarged 24 dp padding at the bottom.

![](https://developer.android.com/static/wear/images/cards/cards-adaptive-layout-title-card-layout.png)

**TitleCard with in-line image (replacing the body copy slot)**

On larger screens, the image doesn't change its aspect ratio and has the padding on the right in order to not make the height of the card too big.

![](https://developer.android.com/static/wear/images/cards/cards-adaptive-layouts-title-card-image.png)

### Cards with additional customization

**Card with an image background**  
![](https://developer.android.com/static/wear/images/cards/cards-additional-customisation-image-card.png)  
In order to achieve this layout you will need customization.  


Image cards display content relating to a single topic with a background image. Image cards can also display standalone images.  


It is recommended that the bottom padding is increased to 24 dp in order to display more of the background image without text over it.

<br />

<br />

![](https://developer.android.com/static/wear/images/cards/cards-adaptive-layout-image-cards.png)