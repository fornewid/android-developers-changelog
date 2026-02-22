---
title: https://developer.android.com/stories/apps/concepts
url: https://developer.android.com/stories/apps/concepts
source: md.txt
---

# TopHatch unveils Concepts&#39; immersive canvas on ChromeOS and Android

![Concepts logo](https://developer.android.com/static/images/distribute/stories/concepts-icon.png)

[Concepts](https://play.google.com/store/apps/details?id=com.tophatch.concepts), developed by the small, tight-knit team at[TopHatch](https://concepts.app/en/), is an advanced design platform that combines the flexibility of a traditional sketchbook with the speed and versatility of a digital drawing tool. Built for a natural interface using touch on mobile from the beginning, Concepts allows professional designers to work with beautiful yet highly responsive tools, flexible environments, and adjustable vectors. It's a playground for creativity. TopHatch's developers knew Concepts' users value two things: a highly responsive and accurate stylus and a big canvas to develop their ideas. With the emergence of versatile devices like the Pixelbook Pen and foldable smartphones, the team saw an opportunity to reach even more creators by building Concepts' UX for larger screens and different form factors. With a few tips and best practices from Google, TopHatch's developers went to work building the Concepts app for immersive experiences on ChromeOS and Android devices.

![Screen interaction with stylus pen](https://developer.android.com/static/images/distribute/stories/concepts-1.png)

## What they did

### High-performance graphics

The team's first priority was to ensure ChromeOS could support Concepts' sharp design and seamless performance on all devices. Concepts runs highly-optimized, low-level GPU code. Because Android has so many different devices on the market, TopHatch was concerned about ensuring fast performance on every driver. After evaluating ChromeOS' capabilities with engineers at Google, TopHatch found that the OS' graphics were consistent and compatible across devices. That meant building the app for maximum performance on every GPU driver was much easier than expected. The team ultimately ended up with five variations of its rendering engine, which allows Concepts to perform beautifully on around 2,500 devices after establishing Android 7 and OpenGL ES 3.1 as minimum requirements. After building Concepts for ChromeOS, TopHatch went a step further and adapted the app for foldable devices. Because ChromeOS already fully supports dynamic screen resizing, the team was able to complete the optimizations in just half a day.

### Low-latency stylus and keyboard support

Smooth and speedy stylus interaction is at the core of the Concepts experience. Digital designers want to feel like ink is flowing from the stylus just like a real pen. To that end, TopHatch's next goal was to make sure the delay from receiving touch input to rendering strokes on screen was as minimal as possible.

TopHatch knew that among all the layers of software between Android and Chrome OS, there was a high potential for lag and "tearing" side effects, where strokes could be partially or incorrectly drawn on screen. The team found its solution through front-buffer rendering. Enabled by the security and simplicity of Chrome OS, front-buffer rendering helped bypass layers of software in the drawing process to allow pixels to be copied the absolute minimum number of times. This significantly reduced the potential for delays when stylus input was detected, ensuring that Concepts would feel as much like drawing with a real pen and paper as possible. TopHatch also decided to implement intuitive keyboard support for Concepts' project navigation and toolbar screens. That way, designers can more easily manage, rename, view, and share their projects when they're not actively drawing in the app.

## Results

Designers' early response to Concepts on ChromeOS has been stellar. The average Concepts user is spending 12x more time on Chromebooks and 20x times more time on the Google Pixelbook and Pixel Slate compared to other devices. TopHatch has also seen Chromebook users become paying users at double the rate on Pixelbook and at 4x the rate on Slate compared to other devices. "Building the app for ChromeOS helped us reach a highly engaged audience --- and a huge Android market," said David Brittain, co-founder and CEO of TopHatch. "We knew designing for larger screens would unlock access to a growing user base, and we've already received incredible feedback as a result." TopHatch strives to support its users with monthly updates, and it most recently rolled out a highly-requested image import feature where designers can sketch over and mark up their own photos. The team looks forward to working with creators across ChromeOS and Android and enabling powerful and mobile creative lifestyles for designers of every stripe.

## Get Started

Learn how to best[optimize your apps for ChromeOS](https://developer.android.com/topic/arc/optimizing).