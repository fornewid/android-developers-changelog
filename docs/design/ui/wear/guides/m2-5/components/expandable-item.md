---
title: Expandable items  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/expandable-item
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Expandable items Stay organized with collections Save and categorize content based on your preferences.




![](/static/wear/images/expandable-item/expandable-item-hero-hero.png)

An expandable item is a custom chip that displays additional content inline.

![](/static/wear/images/expandable-item/expandable-item-chip.png)

**Expandable item chip**

Expandable items let apps include high-density content in less space on the screen. Use this component when you want to keep an app compact while allowing users quick access to additional content.
Use this component to let users perform the following tasks:

* Show more list items (chips, cards)
* Show more text

## Anatomy

![](/static/wear/images/expandable-item/expandable-item-anatomy-list.png)

**Expanding list**  
The chip must be center-aligned.
**A. Label**  
The label text can be customized. Default is "Show more".
**B. Container**  
The button must include a container border.
**C. Expand icon**  
The default icon is the down-facing chevron, which can be customized or removed. The icon is right-aligned for a LTR language locale, and left-aligned for an RTL language locale.

![](/static/wear/images/expandable-item/expandable-item-anatomy-text.png)

**Expanding text**  
The chip must be center-aligned.
**A. Label**  
The label text can be customized. Default is "More".
**B. Container**  
The button has two variants: outlined and non-outlined.
**C. Expand icon**  
The default icon is the down-facing chevron, which can be customized or removed. The icon is right-aligned for a LTR language locale, and left-aligned for an RTL language locale.

## Behavior

![](/static/wear/images/expandable-item/expandable-item-behavior-list.png)

**Expanding list**

Tap the chip to expand and display more items in a list. The expansion action animates, hiding the **Show more** text and revealing the other items in one smooth motion. You can customize the number of items displayed in the collapsed state. The recommended number of items is three.

![](/static/wear/images/expandable-item/expandable-item-behavior-text.png)

**Expanding text**

Tap the chip to expand and display more text. The expansion action animates, hiding the **More** text and revealing the other items in one smooth motion. You can customize the number of lines of text displayed in the collapsed state. The recommended number of lines is eight.

The tap target consists of the entire text area, not just the button.

## Chip styles

![](/static/wear/images/expandable-item/expandable-item-style-list-list.png)
![](/static/wear/images/expandable-item/expandable-item-style-text-text.png)

**Expanding list**

Icon size: 20 dp x 20 dp  
Icon color: On Surface  
Height: 32 dp  
Width: Varies based on text and language  
Stroke: 1 dp  
Label style: Caption 1  
Label color: On Surface

**Expanding text**

Icon size: 20 dp x 20 dp  
Icon color: On Surface  
Height: 32 dp  
Width: Varies based on text & language  
Stroke: 0 or 1 dp  
Fill: None  
Label style: Caption 1  
Label color: On Surface

## Padding

![](/static/wear/images/expandable-item/expandable-item-padding.png)

For both the list variant and the text variant of the expandable item component, the chip should have the following padding values:

* Top padding: 8 dp
* Bottom padding: 16 dp

## **Usage**

Examples of using expandable items:

![](/static/wear/images/expandable-item/expandable-item-usage.png)