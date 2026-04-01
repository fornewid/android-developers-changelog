---
title: https://developer.android.com/ndk/guides/audio/sampling-audio
url: https://developer.android.com/ndk/guides/audio/sampling-audio
source: md.txt
---

# Sampling audio

As of Android 5.0 (Lollipop), the audio resamplers are now entirely based on FIR filters derived from a Kaiser windowed-sinc function. The Kaiser windowed-sinc offers the following properties:

- It is straightforward to calculate for its design parameters (stopband ripple, transition bandwidth, cutoff frequency, filter length).
- It is nearly optimal for reduction of stopband energy compared to overall energy.

See P.P. Vaidyanathan,[*Multirate Systems and Filter Banks*](https://books.google.com/books/about/Multirate_Systems_and_Filter_Banks.html?id=pAsfAQAAIAAJ), p. 50 for discussions of the Kaiser Window and its optimality and relationship to Prolate Spheroidal Windows.

The design parameters are automatically computed based on internal quality determination and the sampling ratios desired. Based on the design parameters, the windowed-sinc filter is generated. For music use, the resampler for 44.1 to 48 kHz and vice versa is generated at a higher quality than for arbitrary frequency conversion.

The audio resamplers provide increased quality, as well as speed to achieve that quality. But resamplers can introduce small amounts of passband ripple and aliasing harmonic noise, and they can cause some high frequency loss in the transition band, so avoid using them unnecessarily.  

## Best practices for sampling and resampling

This section describes some best practices to help you avoid problems with sampling rates.

#### Choose the sampling rate to fit the device

In general, it is best to choose the sampling rate to fit the device, typically 44.1 kHz or 48 kHz. Use of a sample rate greater than 48 kHz will typically result in decreased quality because a resampler must be used to play back the file.

### Use simple resampling ratios (fixed versus interpolated polyphases)

The resampler operates in one of the following modes:

- Fixed polyphase mode. The filter coefficients for each polyphase are precomputed.
- Interpolated polyphase mode. The filter coefficients for each polyphase must be interpolated from the nearest two precomputed polyphases.

The resampler is fastest in fixed polyphase mode, when the ratio of input rate over output rate L/M (taking out the greatest common divisor) has M less than 256. For example, for 44,100 to 48,000 conversion, L = 147, M = 160.

In fixed polyphase mode, the sampling rate is locked and does not change. In interpolated polyphase mode, the sampling rate is approximate. When playing on a 48-kHz device the sampling rate drift is generally one sample over a few hours. This is not usually a concern because the approximation error is much less than the frequency error contributed by internal quartz oscillators, thermal drift, or jitter (typically tens of ppm).

Choose simple-ratio sampling rates such as 24 kHz (1:2) and 32 kHz (2:3) when playing back on a 48-kHz device, even though other sampling rates and ratios may be permitted through AudioTrack.

### Use upsampling rather than downsampling to change sample rates

Sampling rates can be changed on the fly. The granularity of such change is based on the internal buffering (typically a few hundred samples), not on a sample-by-sample basis. This can be used for effects.

Do not dynamically change sampling rates when downsampling. When changing sample rates after an audio track is created, differences of around 5 to 10 percent from the original rate may trigger a filter recomputation when downsampling (to properly suppress aliasing). This can consume computing resources and may cause an audible click if the filter is replaced in real time.

### Limit downsampling to no more than 6:1

Downsampling is typically triggered by hardware device requirements. When the Sample Rate converter is used for downsampling, try to limit the downsampling ratio to no more than 6:1 for good aliasing suppression (for example, no greater downsample than 48,000 to 8,000). The filter lengths adjust to match the downsampling ratio, but you sacrifice more transition bandwidth at higher downsampling ratios to avoid excessively increasing the filter length. There are no similar aliasing concerns for upsampling. Note that some parts of the audio pipeline may prevent downsampling greater than 2:1.

### If you're concerned about latency, don't resample

Resampling prevents the track from being placed in the FastMixer path, which means that significantly higher latency occurs due to the additional, larger buffer in the ordinary Mixer path. Furthermore, there is an implicit delay from the filter length of the resampler, though this is typically on the order of one millisecond or less, which is not as large as the additional buffering for the ordinary Mixer path (typically 20 milliseconds).

## Use of floating-point audio

Using floating-point numbers to represent audio data can significantly enhance audio quality in high-performance audio applications. Floating point offers the following advantages:

- Wider dynamic range.
- Consistent accuracy across the dynamic range.
- More headroom to avoid clipping during intermediate calculations and transients.

While floating-point can enhance audio quality, it does present certain disadvantages:

- Floating-point numbers use more memory.
- Floating-point operations employ unexpected properties, for example, addition is not associative.
- Floating-point calculations can sometimes lose arithmetic precision due to rounding or numerically unstable algorithms.
- Using floating-point effectively requires greater understanding to achieve accurate and reproducible results.

Formerly, floating-point was notorious for being unavailable or slow. This is still true for low-end and embedded processors. But processors on modern mobile devices now have hardware floating-point with performance that is similar (or in some cases even faster) than integer. Modern CPUs also support[SIMD](https://en.wikipedia.org/wiki/SIMD)(Single instruction, multiple data), which can improve performance further.

### Best practices for floating-point audio

The following best practices help you avoid problems with floating-point calculations:

- Use double precision floating-point for infrequent calculations, such as computing filter coefficients.
- Pay attention to the order of operations.
- Declare explicit variables for intermediate values.
- Use parentheses liberally.
- If you get a NaN or infinity result, use binary search to discover where it was introduced.

For floating-point audio, the audio format encoding`AudioFormat.ENCODING_PCM_FLOAT`is used similarly to`ENCODING_PCM_16_BIT`or`ENCODING_PCM_8_BIT`for specifying AudioTrack data formats. The corresponding overloaded method`AudioTrack.write()`takes in a float array to deliver data.  

### Kotlin

```kotlin
fun write(
        audioData: FloatArray,
        offsetInFloats: Int,
        sizeInFloats: Int,
        writeMode: Int
): Int
```

### Java

```java
public int write(float[] audioData,
        int offsetInFloats,
        int sizeInFloats,
        int writeMode)
```

## For more information

This section lists some additional resources about sampling and floating-point.

### Sampling

Sample rates

- [Sampling (signal processing)](https://en.wikipedia.org/wiki/Sampling_%28signal_processing%29)at Wikipedia.

Resampling

- [Sample-rate conversion](https://en.wikipedia.org/wiki/Sample_rate_conversion)at Wikipedia.
- [Sample Rate Conversion](https://source.android.com/devices/audio/src.html)at source.android.com.

The high bit-depth and high kHz controversy

- [D/A and A/D \| Digital Show and Tell](https://www.youtube.com/watch?v=cIQ9IXSUzuM)video by Christopher "Monty" Montgomery of Xiph.Org.
- [The Science of Sample Rates (When Higher Is Better - And When It Isn't)](http://www.trustmeimascientist.com/2013/02/04/the-science-of-sample-rates-when-higher-is-better-and-when-it-isnt/).
- [Audio Myths \& DAW Wars](http://www.image-line.com/support/FLHelp/html/app_audio.htm)
- [192kHz/24bit vs. 96kHz/24bit "debate"- Interesting revelation](http://forums.stevehoffman.tv/threads/192khz-24bit-vs-96khz-24bit-debate-interesting-revelation.317660/)

### Floating point

The following Wikipedia pages are helpful in understanding floating-point audio:

- [Audio bit depth](https://en.wikipedia.org/wiki/Audio_bit_depth)
- [Floating-point arithmetic](https://en.wikipedia.org/wiki/Floating_point)
- [IEEE 754 floating-point](https://en.wikipedia.org/wiki/IEEE_floating_point)
- [Loss of significance](https://en.wikipedia.org/wiki/Loss_of_significance)(catastrophic cancellation)
- [Numerical stability](https://en.wikipedia.org/wiki/Numerical_stability)

The following article provides information on those aspects of floating-point that have a direct impact on designers of computer systems:

- [What every computer scientist should know about floating-point arithmetic](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)by David Goldberg, Xerox PARC (edited reprint).