---
title: Tone mapping - Supporting HDR and SDR content  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/transformer/tone-mapping
source: html-scrape
---

Media3 Transformer is actively under development and we are looking to hear from you! We welcome your feedback, feature requests and bug reports in the [issue tracker](https://github.com/androidx/media/issues). Follow the [ExoPlayer blog](https://medium.com/google-exoplayer) for the latest updates.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Tone mapping - Supporting HDR and SDR content Stay organized with collections Save and categorize content based on your preferences.



When working with Transformer, it is important to consider the compatibility
between HDR and SDR content. HDR displays content with greater color detail,
color and contrast, giving users a better visual experience. However, due to the
difference in color ranges between HDR and SDR, combining the two types of
content could lead to compatibility issues.

As you are building a
[`Composition`](/reference/androidx/media3/transformer/Composition.Builder),
you have the option to [`setHdrMode`](/reference/androidx/media3/transformer/Composition.Builder#setHdrMode(int))
for HDR video inputs. By default, Transformer sets this value to
[`HDR_MODE_KEEP_HDR`](/reference/androidx/media3/transformer/Composition#HDR_MODE_KEEP_HDR()),
which ensures the output is kept in the HDR format. If the device does not
support the HDR format, Transformer automatically attempts to use
[`HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL`](/reference/androidx/media3/transformer/Composition#HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL()) instead.

In some cases, you may be combining both HDR and SDR assets. For example, you
might have SDR overlays on top of HDR videos and images, or you might have a mix
of HDR and SDR videos. In this case, you have the following options:

|  | Advantages | Disadvantages |
| --- | --- | --- |
| [Tone map with MediaCodec](/reference/androidx/media3/transformer/Composition#HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_MEDIACODEC()) | Best visual quality output if supported on device and API combination. | Only supported on API 31+ on certain devices and on API 33+ for devices with HDR capture support. If not supported, `Transformer` throws an `ExportException`. |
| [Tone map with OpenGL](/reference/androidx/media3/transformer/Composition#HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_OPEN_GL()) | Supported on API 29+, with generally wider support across devices. Produces more consistent results. | May produce mild differences compared to output from using `HDR_MODE_TONE_MAP_HDR_TO_SDR_USING_MEDIACODEC`. |
| [Interpret HDR as SDR](/reference/androidx/media3/transformer/Composition#HDR_MODE_EXPERIMENTAL_FORCE_INTERPRET_HDR_AS_SDR()) | Most widely supported option. | Contents will likely have a washed out look and may be displayed incorrectly. |

## Current limitations

The following are unsupported for multi-asset compositions:

* SDR to HDR tone mapping
* SDR and HDR content sequences that start with an HDR asset