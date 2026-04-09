---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input
source: md.txt
---

# Stylus

### Stylus

![](http://developer.android.com/static/images/jetpack/compose/touchinput/stylus/hero.png)  
On phones and large screen devices that include stylus support, users expect a consistent stylus experience across all their apps.

Support stylus to provide improved navigation, drawing and handwriting capabilities, and advanced brushes with tilt and pressure detection.

## Manage stylus input

Guide

### [Add inking to your app with the Ink API](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/about-ink-api)

Use the Ink API to add stylus support and capabilities to your app.  
Guide

### [Stylus input in text fields](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/stylus-input-in-text-fields)

Let users handwrite input in text fields using a stylus.  
Guide

### [Custom text editors](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/custom-text-editors)

Enable stylus handwriting in views that are not`EditText`components or`WebView`text widgets.  
Guide

### [Advanced stylus features](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/advanced-stylus-features)

Support stylus pressure, orientation, tilt, hover, and palm detection. Enhance stylus input rendering with low-latency graphics and motion prediction libraries.  
Guide

### [Note-taking apps](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/create-a-note-taking-app)

Take note---support stylus input in note-taking apps so users can write, sketch, and annotate screen content with fluid efficiency.

## Set your experience apart with advanced libraries

Use the advanced stylus libraries to reduce latency, detect pressure and tilt, ignore accidental marks, and recognize handwriting.

## Low latency libraries

[![](http://developer.android.com/static/images/picto-icons/reduce.svg)](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#low-latency_graphics)  

### [Reduce latency in the graphics rendering pipeline](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#low-latency_graphics)

Improve latency by reducing the processing time between stylus input and screen rendering.  
[![](http://developer.android.com/static/images/picto-icons/lightning.svg)](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#motion_prediction)  

### [Reduce perceived latency](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#motion_prediction)

Further reduce latency using prediction of future motion events, made easy with our Motion Prediction Jetpack library.

## Advanced libraries

[![](http://developer.android.com/static/images/picto-icons/pencils.svg)](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#pressure)  

### [Build advanced brushes with pressure and tilt](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#pressure)

Use information about the pressure and tilt of the stylus to render the stroke from the`MotionEvent`object.  
[![](http://developer.android.com/static/images/picto-icons/prohibited.svg)](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#palm_rejection)  

### [Reject accidental stray marks](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#palm_rejection)

Avoid stray marks when the user accidentally touches the screen while drawing or writing with a stylus.  
[![](http://developer.android.com/static/images/spot-icons/engagement-2.svg)](https://developers.google.com/ml-kit/vision/digital-ink-recognition)  

### [Recognize handwriting](https://developers.google.com/ml-kit/vision/digital-ink-recognition)

Recognize handwritten text and classify gestures on a digital surface with ML Kit Recognize handwritten text and classify gestures on a digital surface with ML Kit Digital Ink Recognition.  
[![](http://developer.android.com/static/images/picto-icons/hardware.svg)](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#full_screen_and_navigation_gestures)  

### [Build immersive experiences](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#full_screen_and_navigation_gestures)

Empower users to work in full screen and use gesture navigation without stray marks.![](http://developer.android.com/static/images/picto-icons/spanner.svg)  

## Build for all types of input

Empower your users to navigate your app with their stylus, just as they would with a keyboard or trackpad. Stylus optimizations also improve the experience for other types of input, like Empower your users to navigate your app with their stylus, just as they would with a keyboard or trackpad. Stylus optimizations also improve the experience for other types of input, like keyboard and mouse.  
Guide

### [Show focus when hovering](http://developer.android.com/develop/ui/views/touch-and-input/stylus-input/support-advanced-stylus-features#hover)

Help users easily identify where the focus is on the screen for precise input. For example, add a focus indicator like a thicker border when a user hovers over it.  
Guide

### [Customize your cursors](http://developer.android.com/about/versions/nougat/android-7.0#custom_pointer_api)

While hovering, update the cursor to show a preview of the brush type or current action.  
Guide

### [Drag and drop content](http://developer.android.com/develop/ui/views/touch-and-input/drag-drop)

Drag and drop images, text, and other content so users can quickly share from your app Drag and drop images, text, and other content so users can quickly share from your app to another app.  
Guide

### [Make text selectable](http://developer.android.com/jetpack/compose/text#select-text)

Make the text in your app selectable so that users can quickly select text and share Make the text in your app selectable so that users can quickly select text and share with other apps with their stylus.

## Other resources

[![](http://developer.android.com/static/images/cards/distribute/engage/ls-gallery.png)](http://developer.android.com/large-screens/gallery)  
Gallery

### [Large screen gallery](http://developer.android.com/large-screens/gallery)

[![](http://developer.android.com/static/images/cards/distribute/engage/training-codelab.png)](http://developer.android.com/codelabs/large-screens/advanced-stylus-support#0)  
CodeLab

### [Enhance stylus support in an Android app](http://developer.android.com/codelabs/large-screens/advanced-stylus-support#0)

[![](http://developer.android.com/static/images/cards/distribute/engage/low-latency.png)](https://medium.com/androiddevelopers/stylus-low-latency-d4a140a9c982)  
Blog post

### [Stylus Low Latency](https://medium.com/androiddevelopers/stylus-low-latency-d4a140a9c982)

[![](http://developer.android.com/static/images/cards/distribute/engage/concept-70.png)](https://android-developers.googleblog.com/2023/03/concepts-users-spend-more-time-using-app-on-tablets-than-phones.html)  
case study

### [Concepts users spend 70% more time using the app on tablets than on phones](https://android-developers.googleblog.com/2023/03/concepts-users-spend-more-time-using-app-on-tablets-than-phones.html)

[![](http://developer.android.com/static/images/cards/distribute/engage/stylus-youtube.png)](https://www.youtube.com/watch?v=F8boaQsioH8)  
YOUTUBE video

### [Adding Stylus support to your Android app](https://www.youtube.com/watch?v=F8boaQsioH8)

[![](http://developer.android.com/images/cards/distribute/engage/optimizing-youtube.png?7)](https://www.youtube.com/watch?v=ucaSqyfpPas)  
YOUTUBE video

### [The key to keyboard and mouse support across tablets and ChromeOS](https://www.youtube.com/watch?v=ucaSqyfpPas)