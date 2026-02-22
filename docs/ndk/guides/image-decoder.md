---
title: https://developer.android.com/ndk/guides/image-decoder
url: https://developer.android.com/ndk/guides/image-decoder
source: md.txt
---

The NDK [`ImageDecoder`](https://developer.android.com/ndk/reference/group/image-decoder) API provides a
standard API for Android C/C++ apps to decode images directly. App developers no
longer need to use the Java APIs (via JNI) or third-party image decoding
libraries. This API, along with encoding functions in the
[Bitmap](https://developer.android.com/ndk/reference/group/bitmap) module, enables the following:

- Native apps and libraries can be smaller because they no longer have to link their own decoding libraries.
- Apps and libraries automatically benefit from platform security updates to decoding libraries.
- Apps can decode images directly into memory they provide. Apps can then post-process the image data (if desired) and pass it to OpenGL or their drawing code.

This page describes how to use the API to decode an image.

## Availability and capability

The `ImageDecoder` API is available on apps that target Android 11 (API level 30)
or higher. The implementation is inside the following files:

- `imagedecoder.h` for the decoder
- `bitmap.h` for the encoder
- `libjnigraphics.so`

The API supports the following image formats:

- JPEG
- PNG
- GIF
- WebP
- BMP

- ICO

- WBMP

- HEIF

- Digital negatives (via the DNG SDK)

In order to cover all usages of the decoded raw images, this API does not
provide higher level objects like those built on top of decoded images inside
the Java framework, such as:

- [`Drawable` objects](https://developer.android.com/reference/android/graphics/drawable/Drawable).
- [`NinePatch`](https://developer.android.com/reference/android/graphics/NinePatch): If present in an encoded image, NinePatch chunks are ignored.
- [Bitmap density](https://developer.android.com/reference/android/graphics/Bitmap#getDensity()): `AImageDecoder` does not do any automatic size adjustment based on the screen's density, but it does allow decoding to a different size via [`AImageDecoder_setTargetSize()`](https://developer.android.com/ndk/reference/group/image-decoder#aimagedecoder_settargetsize).
- Animations: Only decodes the first frame of an animated GIF or WebP file.

## Decode an image

Decoding starts with some form of input representing the encoded image.
`AImageDecoder` accepts multiple types of input:

- [`AAsset`](https://developer.android.com/ndk/reference/group/asset) (shown below)
- File descriptor
- Buffer

The following code shows how to open an image `Asset` from a file, decode it,
and then properly dispose of the decoder and asset. To see an example of
rendering the decoded image, see the
[teapot sample](https://github.com/android/ndk-samples/tree/develop/teapots/image-decoder/src/main/cpp/Texture.cpp#30).  

    AAssetManager* nativeManager = AAssetManager_fromJava(env, jAssets);
    const char* file = // Filename
    AAsset* asset = AAssetManager_open(nativeManager, file, AASSET_MODE_STREAMING);
    AImageDecoder* decoder;
    int result = AImageDecoder_createFromAAsset(asset, &decoder);
    if (result != ANDROID_IMAGE_DECODER_SUCCESS) {
      // An error occurred, and the file could not be decoded.
    }

    const AImageDecoderHeaderInfo* info = AImageDecoder_getHeaderInfo(decoder);
    int32_t width = AImageDecoderHeaderInfo_getWidth(info);
    int32_t height = AImageDecoderHeaderInfo_getHeight(info);
    AndroidBitmapFormat format =
           (AndroidBitmapFormat) AImageDecoderHeaderInfo_getAndroidBitmapFormat(info);
    size_t stride = AImageDecoder_getMinimumStride(decoder);  // Image decoder does not
                                                              // use padding by default
    size_t size = height * stride;
    void* pixels = malloc(size);

    result = AImageDecoder_decodeImage(decoder, pixels, stride, size);
    if (result != ANDROID_IMAGE_DECODER_SUCCESS) {
      // An error occurred, and the file could not be decoded.
    }

    // We're done with the decoder, so now it's safe to delete it.
    AImageDecoder_delete(decoder);

    // The decoder is no longer accessing the AAsset, so it is safe to
    // close it.
    AAsset_close(asset);

    // Draw the pixels somewhere

    // Free the pixels when done drawing with them
    free(pixels);