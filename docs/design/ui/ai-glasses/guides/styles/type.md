---
title: https://developer.android.com/design/ui/ai-glasses/guides/styles/type
url: https://developer.android.com/design/ui/ai-glasses/guides/styles/type
source: md.txt
---

Type is optimized for comfort and glanceability for AI glasses this includes an optimized typescale and font family characteristics.

Jetpack Compose Glimmer has an optimized default typescale, composed of two roles with 3 sizes each.

![Typescale for glasses.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_type_scale.png)
| **Note:** Google Sans Flex is now available at[fonts.google.com](https://fonts.google.com/specimen/Google+Sans+Flex?query=google+sans)!

## Measured in degrees

Interfaces, including text, on glasses are measured in angular degrees, not pixels or points. This unit of measurement corresponds to how much space UI takes up in the user's field of view.**The size of type changes based on how far away it appears.**

<br />

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_type_size.png)

<br />

#### The minimum size for text is 0.6°

Most text should be between 0.7° - 0.9° Based on legibility research, the minimum size for readable body text is around 0.6° at any given depth. To meet the minimum legibility metric, text must be at least 18px in size. 30 PPD × 0.6° minimum = 18px text size.

<br />

## Customize fonts

Fonts like Google Sans Flex can be optimized for glasses display. If using Google Sans Flex, you can optimize your font through variable font axes to make adjustments that create a more comfortable reading experience:

- Optical size, optimizes letterforms for each point size
- Roundness axis to adjust formality
- Wide range of weights and widths

Halation and chromatic aberration in glasses displays spreads light in all directions, causing the boundaries of the letters to disappear. Rounded letterforms can mitigate halation and chromatic aberration in glasses displays due their simplified letterforms geometry. Consider letter spacing, letterform shape and glanceable sizing improves readability and comfort.

![A customized hiking app.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_surfaces_app_customize_hike.png)Here Google Sans Flex has been replaced with Nunito, a rounded font at an increased weight axes.

These principles are based on optical science for this specific display form-factor, and adhering to them is key to creating a comfortable and legible user experience.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_type_rounded_do.png)  
check_circle

### Do

Use rounded fonts with increased weight and letter-spacing.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_type_rounded_dont.png)  
cancel

### Don't

Use condensed thin typefaces.