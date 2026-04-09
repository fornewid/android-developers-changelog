---
title: https://developer.android.com/agi/frame-trace-gui/texture-pane
url: https://developer.android.com/agi/frame-trace-gui/texture-pane
source: md.txt
---

The **Texture** pane shows the content of the texture that has been selected in [textures view](https://gpuinspector.dev/docs/).

If the texture has a mip-map chain, you can change the displayed mip-map level with the slider at the bottom (not pictured). By default, the highest resolution level, level 0, will be displayed.

Move the cursor over the texture image to display a zoomed-in preview of the surrounding pixels in the bottom-left hand corner of the view as in the image above. The pane will also show the texture width and height as well as the x and y coordinates, normalized texture coordinates (U and V values), and RBGA hex value for that point on the image.

## Operations

You can perform operations on the image using the following buttons:
\| BUTTON \| Description \| Example Result \|
\|:---:\|:---:\| :---:\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/zoom_fit%402x.png "Fit View")\| Adjusts the image to fit completely within the pane. You can also right-click the image to adjust the zoom to fit the image.\|![alt text](https://gapid.dev/images/textures-pane/zoom-to-fit.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/zoom_actual%402x.png "1:1")\| Displays the image at no scale, where one device pixel is equivalent to one screen pixel.\|![alt text](https://gapid.dev/images/textures-pane/original-size.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/zoom_in%402x.png "Zoom in")\| Zooms in on the image. You can also use your mouse wheel, or two-finger swipes on a touchpad, to zoom in and out. You can drag the image with your cursor.\|![alt text](https://gapid.dev/images/textures-pane/zoom-in.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/zoom_out%402x.png "Zoom out")\| Zooms out on the image. You can also use your mouse wheel, or two-finger swipes on a touchpad, to zoom in and out.\|![alt text](https://gapid.dev/images/textures-pane/zoom-out.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/histogram%402x.png "Histogram")\|Displays the color histogram for the image. You can select the control handles on either side to limit the color values displayed.\|![alt text](https://gapid.dev/images/textures-pane/histogram.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/color_channels_15%402x.png "Channels")\|Select the color channels to render. The options are Red, Green, Blue, and Alpha (transparency).\|![alt text](https://gapid.dev/images/textures-pane/color-channel.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/transparency%402x.png "Alpha Background")\|Select a checkerboard pattern or a solid color for the image background.\|![alt text](https://gapid.dev/images/textures-pane/image-background.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/flip_vertically%402x.png "Flip Image")\|Flips the image vertically.\|![alt text](https://gapid.dev/images/textures-pane/flip-vertical.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/save%402x.png "Download Image")\|Saves the image to a file.\|![alt text](https://gapid.dev/images/textures-pane/save.png "Fit View")\|
\|![alt text](https://raw.githubusercontent.com/google/gapid/master/gapic/res/icons/jump%402x.png "Commands")\|Displays the list of all calls that updated the texture to this point. Select a call to view the image after the call completes; the selected frame thumbnail and the pane will update accordingly. \|![alt text](https://gapid.dev/images/textures-pane/jump-to-reference.png "Fit View")\|