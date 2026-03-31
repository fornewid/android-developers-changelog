---
title: Geometry pane  |  Android Developers
url: https://developer.android.com/agi/frame-trace-gui/geometry-pane
source: html-scrape
---

Join us for ⁠the [Google for Games Developer Summit](https://gamedevsummit.withgoogle.com/) on March 15!

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Guides](https://developer.android.com/games/guides)

# Geometry pane Stay organized with collections Save and categorize content based on your preferences.




![Geometry pane overview](/static/images/agi/geometry-images/geometry.png)

The geometry pane renders the pre-transformed mesh of the selected draw call.
You can use your mouse or touchpad to rotate the model, and zoom in and out.

The following table describes the operations you can perform with the toolbar
buttons:

| Button | Description | Example |
| --- | --- | --- |
| Y-up Z-up | Click the button to toggle between y axis up and z axis up. In OpenGL ES, the default is the y axis pointing up, the x axis horizontal, and the z axis as depth. |  |
| Winding CW Winding CCW | Toggle between counterclockwise and clockwise triangle winding to view front- versus back-facing triangles. |  |
| Shaded | Show the geometry rendered as shaded polygons. |  |
| Wireframe | Show the geometry rendered as a wireframe. |  |
| Point Cloud | Show the geometry rendered as vertex data points. |  |
| Authored Normals | Select this button to display smooth normals as specified in your code. The button is unavailable if you haven't authored normals in your mesh. |  |
| Faceted Normals | Select this button to see the lit geometry without using smooth normals. It renders the geometry as if each polygon were flat instead of smoothed, using computed face normals. |  |
| Backface Culling Disabled Backface Culling Enabled | Click this button to toggle backface culling, which when enabled hides polygons facing away from the camera. |  |
| Lit | Select this button to render the mesh with a simple directional light. |  |
| Flat | Select this button to render the mesh with just ambient light. |  |
| Normals | Select this button to view normals. Red indicates a positive x axis value, green a positive y axis value, and blue a positive z axis value. |  |