---
title: https://developer.android.com/develop/xr/web
url: https://developer.android.com/develop/xr/web
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Chrome on Android XR supports [WebXR](https://www.w3.org/TR/webxr/). WebXR is an open standard
by [W3C](https://www.w3.org/) that brings high-performance XR APIs to
[supported browsers](https://immersiveweb.dev/#supporttable). If you're building for the web, you can
enhance existing sites with 3D models or build new immersive experiences.

The following WebXR features are supported by Chrome for Android XR:

- [Device API](https://www.w3.org/TR/webxr/)
- [AR Module](https://www.w3.org/TR/webxr-ar-module-1/)
- [Gamepads Module](https://www.w3.org/TR/webxr-gamepads-module-1/)
- [Hit Test Module](https://immersive-web.github.io/hit-test/)
- [Hand Input](https://www.w3.org/TR/webxr-hand-input-1/)
- [Anchors](https://immersive-web.github.io/anchors/)
- [Depth Sensing](https://immersive-web.github.io/depth-sensing/)
- [Light Estimation](https://immersive-web.github.io/lighting-estimation/)

To see WebXR in action, launch Chrome on an Android XR device or the [Android XR
Emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/studio-tools#emulator) and browse the official [WebXR samples](https://immersive-web.github.io/webxr-samples/).

## Prerequisite: Choose a WebXR framework

Before you begin developing, it's important to choose the right WebXR framework.
This significantly enhances your own productivity and improves the quality of
the experiences you create.

- For full control over 3D scenes and creation of custom or complex interactions, we recommend [three.js](https://threejs.org/) and [babylon.js](https://www.babylonjs.com/).
- For rapid prototyping or using HTML-like syntax to define 3D scenes, we recommend [A-Frame](https://aframe.io/docs/1.6.0/components/webxr.html) and [model-viewer](https://modelviewer.dev/examples/augmentedreality/).
- You can also review more [frameworks and sample code](https://immersiveweb.dev/#a-frame).

If you prefer using native JavaScript and WebGL, refer to [WebXR on
GitHub](https://github.com/immersive-web/webxr-samples/tree/main) to create your first WebXR experiment.

## Adapt for Android XR

If you have existing WebXR experiences running on other devices, you may need to
update your code to properly support WebXR on Android XR. For example, WebXR
experiences focused on mobile devices will have to adapt from one screen to two
stereo screens in Android XR. WebXR experiences targeting mobile devices or
existing headsets may need to adapt input code to be hand-first.

When working with WebXR on Android XR, you may need to update your code to
compensate for the fact that there are two screens---one for each eye.

## About ensuring a sense of depth in WebXR

When a user places a virtual object in their physical space, its scale should be
accurate so that it appears as if it truly belongs there. For example, in a
furniture shopping app, users need to trust that a virtual armchair will fit
perfectly in their living room.

Chrome for Android XR supports the [Depth Sensing Module in
WebXR](https://www.w3.org/TR/webxr-depth-sensing-1/), which enhances a device's ability to perceive the
dimensions and contours of their real-world environment. This depth information
allows you to create more immersive and realistic interactions, helping users
make informed decisions.

Unlike depth sensing on mobile phones, depth sensing in Android XR is
stereoscopic, streaming two depth maps in real-time for binocular vision. You
may need to update your WebXR code to properly support stereo depth frames.

The following example renders depth information stereoscopically:

    // Called every time a XRSession requests that a new frame be drawn.
    function onXRFrame(t, frame) {
      const session = frame.session;
      session.requestAnimationFrame(onXRFrame);
      const baseLayer = session.renderState.baseLayer;
      const pose = frame.getViewerPose(xrRefSpace);

      if (pose) {
        gl.bindFramebuffer(gl.FRAMEBUFFER, session.renderState.baseLayer.framebuffer);

        // Clears the framebuffer.
        gl.clearColor(0, 0, 0, 0);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        // Note: Two views will be returned from pose.views.
        for (const view of pose.views) {
          const viewport = baseLayer.getViewport(view);
          gl.viewport(viewport.x, viewport.y, viewport.width, viewport.height);

          const depthData = frame.getDepthInformation(view);
          if (depthData) {
            renderDepthInformationGPU(depthData, view, viewport);
          }
        }
      } else {
        console.error('Pose unavailable in the current frame!');  }
    }

**Key points about the code**

- A valid pose must be returned to access depth data.
- `pose.views` returns a view for each eye and its corresponding for loop runs twice.

Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/videos/design/ui/xr/depth_01.mp4) and watch it with a video player.
Real-time depth visualization using WebXR depth sensing API. Red indicates closer pixels while blue indicates farther pixels.

## Add hand interaction in WebXR

Adding hand interaction to your WebXR app enhances user engagement by enabling
more intuitive and immersive experiences.

Hand input is the primary interaction mechanism in Android XR. Chrome for
Android XR supports the [Hand Input API](https://github.com/immersive-web/webxr-hand-input/blob/master/explainer.md) as the default input.
This API lets users interact with virtual objects naturally, using gestures and
hand movements to grab, push, or manipulate elements in the scene.

Devices such as mobile phones or controller-centric XR devices may not yet
support hand input. You may need to update your WebXR code to properly support
hand input. The [Immersive VR Session with Hands](https://immersive-web.github.io/webxr-samples/immersive-hands.html) demonstrates
how to integrate hand tracking into your WebXR project.

The following animation shows an example of combining pinching with the WebXR
API to show a user "wiping out" the surface of a virtual space to reveal a
pass-through window into the real world.
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/videos/design/ui/xr/xrlabs_screenwiper_20241209_v2.mp4) and watch it with a video player.
WebXR demo of using hand pinch to wipe out screens to see-through the physical reality.

## Permissions in WebXR

When you use WebXR APIs that require permission, Chrome prompts the user to
grant the permission to the site. All WebXR APIs require the 3d mapping and
camera tracking permission. Access tracked face, eye, and hand data are also
protected by permissions. If all needed permissions are
granted, calling `navigator.xr.requestSession('immersive-ar', options)` returns
a valid WebXR session.

The permissions preference chosen by the user persists for each domain.
Accessing a WebXR experience in a different domain causes Chrome to prompt for
permissions again. If the WebXR experience requires multiple permissions, Chrome
prompts for each permission one at a time.

As with all permissions on the web, you should properly handle situations where
the permission is denied.