---
title: https://developer.android.com/design/ui/ai-glasses/guides/styles/color
url: https://developer.android.com/design/ui/ai-glasses/guides/styles/color
source: md.txt
---

Color considers display, environment, and cognition. Color on glasses uses a highly-refined palette to support the behavior of additive displays and to optimize for visual comfort. The use of color on glasses should be used judiciously to harmonize with the real world, to indicate important actions, display imagery or provide semantic meaning.

Black is transparent on optical-see-through display. Keep this in mind when designing as darker color will appear dull or transparent, but this can also be used to create depth.

## Color scheme

The glasses color scheme (collection of color tokens or roles to theme the color of your app) consists of 3 accent roles, 4 surface (or neutral roles) and their on-color counterparts. The color roles are similar to their mobile scheme roles and should be used in the same manner.

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_colorscheme.png)

**Accent colors can be used for on color as limited emphasis.**  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_customize.png)  
check_circle

### Do

Use white text for most of your text content. Font color can be used for emphasized text.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_font_dont.png)  
cancel

### Don't

Use color text for all content.

## Customize color

When customizing colors for glasses, it's crucial to ensure minimal visual obstruction and harmonization with the real world, prioritizing legibility across varying lighting conditions. This involves carefully calibrating colors to balance brightness against saturation, ensuring prominence for clear legibility while retaining enough saturation to be instantly discernible. Primary color can be customized to use your brand or primary interaction color. Consider the contrast, saturation, and power usage of the chosen color.

<br />

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_customize.png)  

#### Optimized brand and semantic colors

Colors that represent brand, actions, or system alerts must be:

- Bright enough to be legible
- Saturated enough to be discernible as a color

<br />

<br />

### Power usage

Some colors use more power and generate more heat than others. Green is the least power hungry, blue is the most, when comparing colors of equal tone as seen on the right. Minimize the number of pixels you light up. The brighter the screen, the hotter the display gets. Don't fill the screen with all white, as this can cause thermal mitigation.  
![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_power.png)

<br />

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_screen_do.png)  
check_circle

### Do

Take into account contrast between all backgrounds your users will encounter.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_screen_dont.png)  
cancel

### Don't

Have too little contrast for UI elements on various backgrounds, this can create eyestrain and illegibility.
In order to have enough contrast over every background you need to have a contrast difference of 70 (7:1) in the tone of the foreground and background colors. You can test this out by setting your designs to screen blend mode.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_saturated_do.png)  
check_circle

### Do

Use desaturated colors.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_saturated_dont.png)  
cancel

### Don't

Use overly saturated colors. They may not display properly and disrupt legibility.

**Customized surfaces should be avoided.**

<br />

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_container.png)  

#### Dark container colors

Containers generally must focus on displaying content that is within them, without being distracting:

- Surfaces must be black for highest contrast
- Outlines should be visible but subtle

<br />

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_surface_do.png)  
check_circle

### Do

Use dark surfaces and bright content.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_surface_dont.png)  
cancel

### Don't

Use bright or filled surfaces.

**Outline customization is possible to add branding or expressive UI.**  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_outline_do.png)  
check_circle

### Do

Use the default colors. These have been highly optimized for glasses display.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_outline_dont.png)  
cancel

### Don't

Use multiple outline colors.

<br />

![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_outline_warning.png)  
cancel

### Warning

Be careful and harmonize custom colors between focus and default state outlines.

<br />

![Design elements should be anchored to the bottom of the frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_outline_focus.png)Customizing the outline focus with blue: the focus state highlight is made of 2 outlines, color is applied to layer 2 to tine the focus state.