---
title: Type scale  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/styles/typography/type-scale-tokens
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Type scale Stay organized with collections Save and categorize content based on your preferences.



The Material 3 Expressive type scale features a combination of 21 styles, each
with an intended application and meaning. They're assigned based on use (such as
display or label), and grouped more broadly into categories based on scale (such
as large or small). The default type scale for Material 3 Expressive is Roboto
Flex, which creates a cohesive typography experience.

## Display

Display is utilized for large, short strings of text used to display highly
glanceable hero information, significant metrics, confidence or expressive brand
moments.

![](/static/wear/images/design/font-type-display.png)

**Scaling:** None of the Display type styles can scale with user-configurable
font size preferences. Scaling on fonts 20sp and up isn't allowed because of the
limited screen space on Wear OS devices.

## Title

Title is hierarchical text used as a mechanism for way-finding, like a page,
section title, or sub-section title (in the case of TitleSmall).

![](/static/wear/images/design/font-type-title.png)

**Scaling:** All Title type styles scale with user-configurable font size
preferences. Scaling on fonts 20sp and up isn't allowed because of the limited
screen space on Wear OS devices.

## Label

Label is used for component level text that describes an action that would
happen if interacted with. The most common and widely used application for label
is for text nested within a button.

![](/static/wear/images/design/font-type-label.png)

**Scaling:** LabelMedium and Small can scale with user-configurable font size
preferences, but not LabelLarge. Scaling on fonts 20sp and up isn't allowed
because of the limited screen space on Wear OS devices.

## Body

Body is reserved for content text like paragraphs of body copy, text used in
complex data visualization, time stamps, and metadata.

![](/static/wear/images/design/font-type-body.png)

**Scaling:** All Arc type styles scale with user-configurable font size
preferences. Scaling on fonts 20sp and up isn't allowed because of the limited
screen space on Wear OS devices.

## Numeral

Numeral text styles are used for numerical digits, usually limited to a few
characters. Can take on more expressive properties at the larger display sizes.
Gives flexibility to expand width axis with minimal localization and font
scaling concerns.

![](/static/wear/images/design/font-type-numeral.png)

**Scaling:** None of the Numeral type styles can scale with user-configurable
font size preferences. Scaling on fonts 20sp and up isn't allowed because of the
limited screen space on Wear OS devices.

**Tabular/Mono:** In certain cases, add tabular and mono spacing to numerals,
especially when the numbers scroll or change using motion, and you want to avoid
the numbers jumping around due to them having different widths. This spacing
helps all characters have the same width. An example of this would be on the
Picker which has number in a scrolling list.

## Arc

Arc header text is used for curved text making up the signposting on the UI such
as time text and a curved labels. Tailored font axis that specifically optimize
type along a curve and in order to accommodate the different spacing that
appears between characters when they're positioned on the top, instead of the
bottom, of a curved screen.

![](/static/wear/images/design/font-type-arc.png)

**Scaling:** All Body type styles scale with user-configurable font size
preferences. Scaling on fonts 20sp and up isn't allowed because of the limited
screen space on Wear OS devices.

**Tabular/Mono:** Add tabular and mono spacing to curved text. Tabular and mono
spacing helps all characters have the same width.