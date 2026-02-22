---
title: https://developer.android.com/media/media3/transformer/tone-mapping
url: https://developer.android.com/media/media3/transformer/tone-mapping
source: md.txt
---

# Tone mapping - Supporting HDR and SDR content

When working with Transformer, it is important to consider the compatibility between HDR and SDR content. HDR displays content with greater color detail, color and contrast, giving users a better visual experience. However, due to the difference in color ranges between HDR and SDR, combining the two types of content could lead to compatibility issues.

As you are building a[`Composition`](https://developer.android.com/reference/androidx/media3/transformer/Composition.Builder), you have the option to[`setHdrMode`](https://developer.android.com/reference/androidx/media3/transformer/Composition.Builder#setHdrMode(int))for HDR video inputs. By default, Transformer sets this value to[`HDR_MODE_KEEP_HDR`](https://developer.android.com/reference/androidx/media3/transformer/Composition#HDR_MODE_KEEP_HDR()), which ensures the output is kept in the HDR format. If the device does not support the HDR format, Transformer automatically attempts to use[`HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL`](https://developer.android.com/reference/androidx/media3/transformer/Composition#HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL())instead.

In some cases, you may be combining both HDR and SDR assets. For example, you might have SDR overlays on top of HDR videos and images, or you might have a mix of HDR and SDR videos. In this case, you have the following options:

|                                                                                                                                                             |                                              Advantages                                              |                                                                        Disadvantages                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tone map with MediaCodec](https://developer.android.com/reference/androidx/media3/transformer/Composition#HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_MEDIACODEC()) | Best visual quality output if supported on device and API combination.                               | Only supported on API 31+ on certain devices and on API 33+ for devices with HDR capture support. If not supported,`Transformer`throws an`ExportException`. |
| [Tone map with OpenGL](https://developer.android.com/reference/androidx/media3/transformer/Composition#HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL())        | Supported on API 29+, with generally wider support across devices. Produces more consistent results. | May produce mild differences compared to output from using`HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_MEDIACODEC`.                                                  |
| [Interpret HDR as SDR](https://developer.android.com/reference/androidx/media3/transformer/Composition#HDR_MODE_EXPERIMENTAL_FORCE_INTERPRET_HDR_AS_SDR())  | Most widely supported option.                                                                        | Contents will likely have a washed out look and may be displayed incorrectly.                                                                               |

## Current limitations

The following are unsupported for multi-asset compositions:

- SDR to HDR tone mapping
- SDR and HDR content sequences that start with an HDR asset