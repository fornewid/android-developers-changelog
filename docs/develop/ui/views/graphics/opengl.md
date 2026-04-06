---
title: Displaying graphics with OpenGL ES  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/graphics/opengl
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Displaying graphics with OpenGL ES Stay organized with collections Save and categorize content based on your preferences.



The Android framework provides plenty of standard tools for creating attractive, functional
graphical user interfaces. However, if you want more control of what your application draws on
screen, or are venturing into three dimensional graphics, you need to use a different tool. The
OpenGL ES APIs provided by the Android framework offers a set of tools for displaying high-end,
animated graphics that are limited only by your imagination and can also benefit from the
acceleration of graphics processing units (GPUs) provided on many Android devices.

This class walks you through the basics of developing applications that use OpenGL, including
setup, drawing objects, moving drawn elements and responding to touch input.

The example code in this class uses the OpenGL ES 2.0 APIs, which is the recommended API version
to use with current Android devices. For more information about versions of OpenGL ES, see the
[OpenGL developer
guide](/develop/ui/views/graphics/opengl/about-opengl#choosing-version).

**Note:** Be careful not to mix OpenGL ES 1.x API calls with OpenGL
ES 2.0 methods! The two APIs are not interchangeable and trying to use them together only results in
frustration and sadness.

## Lessons

**[Build an OpenGL ES environment](/develop/ui/views/graphics/opengl/environment)**
:   Learn how to set up an Android application to be able to draw OpenGL graphics.

**[Define shapes](/develop/ui/views/graphics/opengl/shapes)**
:   Learn how to define shapes and why you need to know about faces and winding.

**[Draw shapes](/develop/ui/views/graphics/opengl/draw)**
:   Learn how to draw OpenGL shapes in your application.

**[Apply projection and camera views](/develop/ui/views/graphics/opengl/projection)**
:   Learn how to use projection and camera views to get a new perspective on your drawn
    objects.

**[Add motion](/develop/ui/views/graphics/opengl/motion)**
:   Learn how to do basic movement and animation of drawn objects with OpenGL.

**[Respond to touch events](/develop/ui/views/graphics/opengl/touch)**
:   Learn how to do basic interaction with OpenGL graphics.

## Additional sample code

To download NDK samples, see
[NDK Samples](https://github.com/googlesamples/android-ndk/).