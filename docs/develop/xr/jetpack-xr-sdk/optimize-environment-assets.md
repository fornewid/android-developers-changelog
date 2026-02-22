---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/optimize-environment-assets
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/optimize-environment-assets
source: md.txt
---

<br />


Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Beginning with the alpha04 release of the Jetpack XR libraries, there are
important updates to how you should provide spatial environment assets for
optimal performance and visual quality. These changes are a compatibility impact
and require updating existing apps that set spatial environments.

To provide spatial environments, you need two main components:

- A .glb or .gltf file for the environment's geometry (for example, the ground plane, nearby objects) and the primary visual skybox texture that users see.
- A separate ZIP file containing Image Based Lighting (IBL) information generated from a high dynamic range EXR image using the cmgen tool. The ZIP file is used for lighting calculations, such as reflections on objects, and not for the visual skybox texture itself.

## Why this approach?

This updated asset structure provides these advantages:

- **Smaller file sizes:** Compared to previous methods, such as using a single high-resolution HDR skybox file for both visual display and lighting information, this approach reduces file sizes.
- **Improved performance:** Separating the visual skybox texture (built into the glb) from the IBL data (in the ZIP file) lets you optimize each component independently. This results in lower texture memory read bandwidth and lower power consumption.
- **Optimized lighting:** Using a lower resolution skybox resource specifically for the lighting map is beneficial for performance without significantly impacting the visual results of the lighting on objects.

To learn more about adding a spatial Environment in your app, see our guide on
[adding environments to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environment).
| **Note:** It's important to provide an IBL asset if your app sets a custom environment, especially if your app has any 3D objects. This is because, if your app provides a glb/glTF but no IBL ZIP file, the 3D objects in the user's environment appear with incorrect lighting (for example, too bright or dim, reflecting objects that the user can't otherwise see).

## Optimize your glb

![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/optimize-environment-assets/environment-gltf.png "A 3D model of an environment.")

Your glb represents the geometry around the user, and you include the visual
texture of your skybox. For your geometry, you should try to maintain file sizes
at or smaller than 80MB.

To do this, there are a number of opportunities to make your environment more
efficient while maintaining high quality. For example, the density of your mesh
should be the most dense near the user, and you can decrease the density for
meshes that are farther from the user.

- **View distance:** The view distance for environments in Android XR is 200m from the point of the user, and your skybox texture should adhere to this constraint. This provides an optimal experience because parallax becomes indiscernible at that distance.
- **User height:** Geography can vary, but position the user on a mound at
  around 1.5 meters of height to avoid clipping with larger UI elements in
  apps.

- **Polycount:** Be sensitive to the polycount in your glb files, as a high
  polycount can lead to unnecessary power consumption. Each patch of geometry
  shouldn't exceed 10,000 vertices.

- **KTX compression:** Optimize the GPU performance of your glb file by
  ensuring that your glb uses mipmaps and ktx2 textures.

## What you'll need to optimize your IBL

Download the cmgen command line utility:

- You can find the latest release in [the Filament repository](https://github.com/google/filament/releases/).
- Find the .tgz containing the prebuilt version of cmgen for your platform and extract it.
- The prebuilt tool is under the /bin directory of the extracted .tgz file.

Assets to prepare to generate the .zip file for IBL:

- A low-resolution EXR that matches your skybox texture
  - Your skybox texture input should be an EXR file. Although cmgen supports other formats, EXRs are recommended because they provide the high dynamic range information that's critical to provide high quality IBL. Using other formats like PNG results in less precise lighting.
  - The source image (EXR) needs to have a 2:1 ratio and dimensions that are a power of 2. Use an EXR that's 1024 x 512 pixels. Note: It may seem that 1024 x 512 is too low of a resolution, but this is beneficial for performance. For IBL, the visual results for the user are very similar to much higher IBL resolution assets.
- A solid black png
  - This asset must also be a 2:1 ratio. Use a size of 100 x 50 pixels.
  - This serves as an optimized texture to accompany the IBL. Users won't look at this, so we focus the asset on optimizing for performance.

![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/optimize-environment-assets/environment_skybox.png "A 3D model of a skybox.")

The following shows an example of using cmgen to create the .zip file for IBL.
In this example we use input files named my_360_skybox_1024_x_512.exr and
black_skybox.png, and we create a .zip file named my_ibl.zip  

    # Produce black cubemaps for the texture of the IBL asset.
    ./cmgen --format=rgb32f --size=128 --extract=./skybox_ibl ./black_skybox.png

    # Produce lighting cubemaps and a Spherical Harmonics from EXR
    ./cmgen --format=rgb32f --size=128 --deploy=./skybox_ibl --ibl-ld=. --ibl-samples=1024 --extract-blur=0.0 --sh-irradiance --sh-shader --sh-output=./skybox_ibl/sh.txt ./my_360_skybox_1024_x_512.exr

    # Copy all of the black cubemaps into the other folder.
    cp -rf ./skybox_ibl/black_skybox/* ./skybox_ibl/my_360_skybox_1024_x_512

    # Rename the directory to reflect that these are old assets.
    mv ./skybox_ibl/black_skybox ./skybox_ibl/black_skybox_old

    # Rename the directory to reflect that these are your cubemap assets.
    mv ./skybox_ibl/my_360_skybox_1024_x_512 ./skybox_ibl/black_skybox

    # Change into the child directory.
    cd ./skybox_ibl

    # Zip all of the cubemap and the Spherical Harmonics assets together.
    zip -q my_ibl.zip black_skybox/*

    # Return to the directory you started in.
    cd ..