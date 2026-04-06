---
title: https://developer.android.com/media/camera/lowlight/choose-option
url: https://developer.android.com/media/camera/lowlight/choose-option
source: md.txt
---

# Choose the best low light option

We offer several different ways to capture moments in low light. This document helps you choose the right one for your app's needs.

### Low light options

There are several different options for low light capture. It's important to pick the right one for your app's needs.

- To capture high-quality still images in low-light conditions, use the[night mode camera extension](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT). This extension produces the highest quality results, but it can't stream images in real time. That's because night mode takes a burst capture, combines all of the photos together, and processes the result to capture more details. If you've ever taken a photo in a dim scene, and your phone asks you to hold still for a few seconds, this is what's happening.
- For real-time use cases, like a camera preview in low light, use*low light boost* . This mode produces a lower-quality capture than night mode; for example, you may see more artifacts and more motion blur than you would with night mode. There are two low light boost options available:
  - Some devices support[*Low Light Boost AE Mode*](https://developer.android.com/media/camera/lowlight/low-light-boost-ae). This mode fine-tunes the exposure control and applies additional processing in the ISP pipeline.
  - Google Play services provides the software-based[*Google Low Light Boost*](https://developer.android.com/media/camera/lowlight/low-light-boost-gp)library, which can run on many devices that don't support Low Light Boost AE Mode. Google Low Light Boost applies post-processing to the stream produced by the camera hardware. The results aren't quite as good as Low Light Boost AE Mode, so you should use Low Light Boost AE Mode if the device supports it.