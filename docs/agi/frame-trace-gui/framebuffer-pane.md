---
title: Framebuffer pane  |  Android Developers
url: https://developer.android.com/agi/frame-trace-gui/framebuffer-pane
source: html-scrape
---

Join us for ⁠the [Google for Games Developer Summit](https://gamedevsummit.withgoogle.com/) on March 15!

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Guides](https://developer.android.com/games/guides)

# Framebuffer pane Stay organized with collections Save and categorize content based on your preferences.



The **Framebuffer** pane shows the contents of the currently-bound framebuffer.
Depending on the item you select in the **Commands** pane, the **Framebuffer**
pane can show onscreen or offscreen framebuffers.

![](/static/images/agi/framebuffer-pane-images/framebuffer-pane.png)

When you select a command in the **Commands** pane, the **Framebuffer** pane displays the contents of the framebuffer after that call finishes. If you select a command group, it displays the framebuffer that best represents the group. Typically, this is the framebuffer after the last call in the group finishes.

Start by selecting the first call within a frame, then click each successive
call to watch the framebuffer components draw one-by-one until the end of the
frame. These framebuffer displays, for both onscreen and offscreen graphics, help you to locate the source of any rendering errors.

Move the cursor over the image to display a zoomed-in preview of the surrounding pixels in the bottom-left hand corner of the view as in the image above. The pane also shows the image width and height
as well as the *x* and *y* coordinates, normalized image coordinates (U and V
values), and RBGA hex value for that point on the image.

## Select different attachments

A framebuffer can contain multiple attachments. You can select which
attachment to display and click **Show Attachments** or **Hide Attachments** as
needed. Attachment thumbnails are labeled with the type of the attachment
(for example, COLOR, DEPTH, and INPUT) as well as its index.

Once you select an attachment, the main view displays in the upper left corner.

## Operations

You can perform operations on the framebuffer image using the following buttons:

| Button | Description | Example Result |
| --- | --- | --- |
| Render shaded geometry | Renders the shaded geometry of the image. |  |
| Render wireframe geometry | Shows the wireframe of the image. |  |
| Zoom to Fit | Adjusts the image to fit completely within the pane. You can also right-click the image to adjust the zoom to fit the image. |  |
| Zoom to Actual Size | Displays the image at no scale, where one device pixel is equivalent to one screen pixel. |  |
| Zoom In | Zooms in on the image. You can also use your mouse wheel, or two-finger swipes on a touchpad, to zoom in and out. You can drag the image with your cursor. |  |
| Zoom Out | Zooms out on the image. You can also use your mouse wheel, or two-finger swipes on a touchpad, to zoom in and out. |  |
| Color Histogram | Displays the color histogram for the image. You can select the control handles on either side to limit the color values displayed. |  |
| Color Channels | Select the color channels to render. The options are **Red**, **Green**, **Blue**, and **Alpha** (transparency). |  |
| Background | Select a checkerboard pattern or a solid color for the image background. |  |
| Flip Vertically | Flips the image vertically. |  |
| Save To File | Saves the image to a file. |  |