---
title: https://developer.android.com/design/ui/ai-glasses/guides/styles/overview
url: https://developer.android.com/design/ui/ai-glasses/guides/styles/overview
source: md.txt
---

Design for clarity, legibility, and minimal distraction.

<br />

Visual design principles emphasize clarity, legibility, and minimal distraction,
adapted to the unique constraints of a small, near-eye display on AI glasses.
Consider the limited display area and the user's primary focus on the real
world. Visual elements should be designed to be crisp, high-contrast, and appear
only when necessary, quickly fading when no longer relevant.

![Design elements should be anchored to the bottom of the
frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_visualdesign.png)

<br />

Jetpack Compose Glimmer's design language features a simplified theme for
optimal visibility on glasses. Color and type can be customized for semantic
expression and app cohesion.
![Compose Glimmer color schematic.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_color.png) Compose Glimmer includes a color scheme. ![Compose Glimmer typescale and styles.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_type.png) Compose Glimmer includes its own typescale. ![Compose Glimmer shape
styles.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_shapes.webp) Compose Glimmer shape styles include three sizes for border radius. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_shape_do.png)

### Do

Embrace rounded corners to avoid drawing the user's attention into component corners. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_shape_dont.png)

### Don't

Overly customize shape with sharp corners, they can create visual pockets that lead the user's eye into, which on immersive and augmented experiences have greater affect.