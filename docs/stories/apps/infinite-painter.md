---
title: https://developer.android.com/stories/apps/infinite-painter
url: https://developer.android.com/stories/apps/infinite-painter
source: md.txt
---

# Infinite Studio ramps up active installations after optimizing for ChromeOS

![](https://developer.android.com/static/images/distribute/stories/infinite-painter-icon.png)

With natural brushes, realistic blending, and an unparalleled toolset,[Infinite Painter](https://play.google.com/store/apps/details?id=com.brakefield.painter)is one of the most advanced painting apps available on mobile. Fueled by its mantra, "Pushing the boundaries of mobile," the developer team at Infinite Painter saw an opportunity to boost its reach and bridge the gap between its existing mobile audience and the fast-growing Chromebook user base.

Despite more users migrating from using traditional desktops and interactive tablets to mobile devices, Infinite Studio started receiving more requests to make Infinite Painter available on wider and more immersive desktop screens. The development team realized it could bring Infinite Painter into a desktop-style environment by optimizing the app for ChromeOS. Because Android apps can run on ChromeOS, and users can easily access them via Google Play, the team was able to make these updates without much heavy lifting.

## What they did

The dev team's first step was figuring out what would make Infinite Painter's UX more attractive while running on a desktop. The team decided to tap into new Chromebook features ideal for immersive, wide-screen experiences by making three key adjustments: adding keyboard shortcuts, optimizing for new input devices, and enabling resizable windows.

### Keyboard shortcuts

The first thing Infinite Studio realized was how often designers and illustrators use keyboard shortcuts to speed up their workflow. So, the developers added 30 industry-standard shortcuts and organized them in an easily accessible dropdown menu triggered by holding down the CTRL key.

![](https://developer.android.com/static/images/distribute/stories/infinitepainter-controls.png)

### Input devices

Next, Infinite Studio[optimized the app for various input devices](https://developer.android.com/topic/arc/input-compatibility), such as an external mouse, fingertips (some Chromebooks come equipped with a touch screen), a stylus, or a touchpad. For touchpads, the team added the ability to easily zoom and pan the canvas with two-finger gestures. For external mouses, they added scroll wheel zooming and tooltips that appear when users hover over interface elements with their cursor.

The developers already had support for stylus and fingertip input for mobile users, but they worked closely with the ChromeOS team to make the experience even smoother with the low-latency API. This enables the app to draw strokes directly to the screen overlay, and gives users the feeling of drawing directly on the screen with their stylus or fingers.

### Resizable windows

Finally, the team[optimized the app to support varying window sizes](https://developer.android.com/topic/arc/window-management). Users can resize the app window for an optimal experience on any form factor, whether they prefer to work in full-screen mode or to open and use another app beside it. The developers also added the ability for users to drag and drop external images into the app.

![](https://developer.android.com/static/images/distribute/stories/infinitepainter-artboards.png)

## Results

After optimizing for wider screens on ChromeOS, active installations of Infinite Painter have grown by 55%, and overall activity in the app has nearly doubled. Sean Brakefield, the creator of Infinite Painter, couldn't be happier with his team's decision: "Between users' growing demand for touch-centric experiences and the range of stylus-based Chromebooks being released, we knew it made perfect sense to optimize for ChromeOS," he concluded. "Best of all, nearly all of the migration was already done for us when Google added support for Android apps on Chromebooks."

## Get started

Learn how to best[optimize your apps for ChromeOS](https://developer.android.com/topic/arc/optimizing).