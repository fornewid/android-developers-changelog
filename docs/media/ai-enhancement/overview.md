---
title: https://developer.android.com/media/ai-enhancement/overview
url: https://developer.android.com/media/ai-enhancement/overview
source: md.txt
---

Modern mobile applications rely heavily on user-generated media to drive
engagement and retention. Apps observe natural variability in content quality
due to the wide spectrum of device capabilities, lighting conditions, and user
experience. For apps managing large volumes of photos and videos that come from
a variety of sources, there is an opportunity to elevate the baseline quality
of this user-generated content. Maintaining optimal quality requires a careful
balance between the compression needed for operations like editing, uploading,
and downloading, while retaining enough detail for high-fidelity consumption.

## Media enhancement API overview

The Media Enhancement API in Google Play services provides a comprehensive,
on-device AI solution to bridge this gap. It uses on-device Graphics
Processing Unit (GPU) acceleration to provide high quality, low latency
improvements for images and videos. It achieves these enhancements through
features such as automatic tone mapping, deblurring, denoising, and upscaling.

Delivered natively through Google Play services, this API offloads
computationally intensive image and video restoration tasks directly to the host
device's native GPU and Neural Processing Unit (NPU). The API provides a
low-latency, privacy-preserving pipeline with zero APK bloat, downloading models
on-demand only when needed to respect device disk space.

## Core capabilities and use cases

The framework targets specific media failure points through three core machine
learning capabilities, which you can configure independently or in tandem:

| Capability | Algorithmic functionality | Optimal application use case |
|---|---|---|
| Tonemap | [An SDR-to-SDR local tone mapping algorithm](https://groups.csail.mit.edu/graphics/hdrnet/) that enhances standard dynamic range (SDR) images to mimic HDR-like qualities---such as improved local contrast and brightened shadows---while remaining within the displayable SDR range. This realtime, power-efficient algorithm is optimized for mobile performance. | Rescuing flat, overcast landscape photos or severely backlit indoor portraits. |
| Deblur | Reconstructs sharp edges by estimating the mathematical blur kernel caused by subject motion or camera shake. Applies spatial filtering to smooth chromatic grain, and acts as a deblocking filter to mitigate compression artifacts near sharp edges. | Reclaiming shaky or blurred photos, enhancing grainy low-light images, and removing blocky artifacts from compressed JPEG images and video streams. |
| Upscale | Uses a super-resolution generative model to multiply pixel count and reconstruct missing high-frequency details. | Scaling small thumbnails or standard-definition video files for full-screen display. |

## Hardware requirements

Running inference on-device with machine learning or deep learning models takes
time, and performance largely depends on which hardware accelerators the device
uses. The Media Enhancement API is optimized for premium-tier devices equipped
with dedicated tensor cores and high-bandwidth memory (for example, the Pixel 10
Pro or Samsung Galaxy S26 Ultra).

If a device's hardware does not meet minimum performance thresholds, the
initialization process stops and reports an unsupported status to prevent frame
drops or thermal throttling.