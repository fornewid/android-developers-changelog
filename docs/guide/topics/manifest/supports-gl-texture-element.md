---
title: https://developer.android.com/guide/topics/manifest/supports-gl-texture-element
url: https://developer.android.com/guide/topics/manifest/supports-gl-texture-element
source: md.txt
---

# &lt;supports-gl-texture>

**Note:**Google Play filters applications according to the texture compression formats that they support so that they install only on devices that can handle their textures properly. You can use texture compression filtering as a way of targeting specific device types based on the GPU platform.

For important information about how Google Play uses`<supports-gl-texture>`elements as the basis for filtering, read the[Google Play and texture compression filtering](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element#market-texture-filtering)section.

syntax:
:

    ```xml
    <supports-gl-texture
      android:name="string" />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Declares a single GL texture compression format that the app supports.An application "supports" a GL texture compression format if it can provide texture assets compressed in that format when the application installs on a device.

    The application provides the compressed assets locally, from inside the APK, or it can download them from a server at runtime.

    Each`<supports-gl-texture>`element declares exactly one supported texture compression format, specified as the value of a`android:name`attribute. If your application supports multiple texture compression formats, you can declare multiple`<supports-gl-texture>`elements:  

    ```xml
    <supports-gl-texture android:name="GL_OES_compressed_ETC1_RGB8_texture" />
    <supports-gl-texture android:name="GL_OES_compressed_paletted_texture" />
    ```

    `<supports-gl-texture>`elements are informational, meaning that the Android system itself does not examine the elements at install time to ensure matching support on the device.

    However, other services, such as Google Play, or applications can check your application's`<supports-gl-texture>`declarations as part of handling or interacting with your application. For this reason, it's very important that you declare all the texture compression formats from the following list that your application supports.

    Applications and devices typically declare their supported GL texture compression formats using the following set of well-known strings. The set of format strings might grow over time, as needed. Since the values are strings, applications are free to declare other formats as needed.

    Assuming that the application is built with SDK Platform Tools r3 or higher, filtering based on the`<supports-gl-texture>`element is activated for all API levels.

attributes:
:

    `android:name`
    :   Specifies a single GL texture compression format supported by the application as a descriptor string. Common descriptor values are listed in the following table.

        | Texture compression format descriptor |                                                                                                                                     Comments                                                                                                                                      |
        |---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | `GL_OES_compressed_ETC1_RGB8_texture` | Ericsson texture compression. Specified in OpenGL ES 2.0 and available in all Android-powered devices that support OpenGL ES 2.0.                                                                                                                                                 |
        | `GL_OES_compressed_paletted_texture`  | Generic paletted texture compression.                                                                                                                                                                                                                                             |
        | `GL_AMD_compressed_3DC_texture`       | ATI 3Dc texture compression.                                                                                                                                                                                                                                                      |
        | `GL_AMD_compressed_ATC_texture`       | ATI texture compression. Available on devices running Adreno GPU, including HTC Nexus One, Droid Incredible, EVO, and others. For widest compatibility, devices may also declare a`<supports-gl-texture>`element with the descriptor`GL_ATI_texture_compression_atitc`.           |
        | `GL_EXT_texture_compression_latc`     | Luminance alpha texture compression.                                                                                                                                                                                                                                              |
        | `GL_EXT_texture_compression_dxt1`     | S3 DXT1 texture compression. Supported on devices running the Nvidia Tegra2 platform, including Motorala Xoom, Motorola Atrix, Droid Bionic, and others.                                                                                                                          |
        | `GL_EXT_texture_compression_s3tc`     | S3 texture compression, nonspecific to DXT variant. Supported on devices running the Nvidia Tegra2 platform, including Motorala Xoom, Motorola Atrix, Droid Bionic, and others. If your application requires a specific DXT variant, declare that descriptor instead of this one. |
        | `GL_IMG_texture_compression_pvrtc`    | PowerVR texture compression. Available on devices running the PowerVR SGX530/540 GPU, such as Motorola DROID series; Samsung Galaxy S, Nexus S, and Galaxy Tab; and others.                                                                                                       |

see also:
:
    - [Filters on Google Play](https://developer.android.com/google/play/filters)