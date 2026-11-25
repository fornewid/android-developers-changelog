---
title: https://developer.android.com/develop/ui/compose/animation/introduction
url: https://developer.android.com/develop/ui/compose/animation/introduction
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/llms.txt

[Video](https://www.youtube.com/watch?v=7yY2OocGiQU)

### [Animations in Compose](http://developer.android.com/develop/ui/compose/animation/quick-guide.md.txt)

Animations are essential in a modern mobile app in order to realize a smooth and understandable user experience. [Quick guide](http://developer.android.com/develop/ui/compose/animation/quick-guide.md.txt)

## Animation modifiers and composables

[![](http://developer.android.com/static/develop/ui/compose/images/animations/animated_visibility_column.gif)](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedvisibility)

### [Animate appearance and disappearance](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedvisibility)

The `AnimatedVisibility` composable allows you to hide or show content easily. [Learn more](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedvisibility) [![](http://developer.android.com/static/develop/ui/compose/images/animations/animated_content_size.gif)](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animateContentSize)

### [Animate content size changes](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animateContentSize)

Use `animateContentSize()` to achieve automatic size change animations. [Learn more](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animateContentSize) [![](http://developer.android.com/static/develop/ui/compose/images/animations/animated_content_slower.gif)](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedcontent)

### [Animate between different composables](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedcontent)

Use `AnimatedContent` to animate between composables that have different content. [Learn more](http://developer.android.com/develop/ui/compose/animation/composables-modifiers.md.txt#animatedcontent)

## Value-based animations

[![](http://developer.android.com/static/develop/ui/compose/images/animations/animated_padding.gif)](http://developer.android.com/develop/ui/compose/animation/value-based.md.txt#animate-as-state)

### [Animate a single value](http://developer.android.com/develop/ui/compose/animation/value-based.md.txt#animate-as-state)

Use `animate*AsState` functions to animate an individual property, such as opacity. [Learn more](http://developer.android.com/develop/ui/compose/animation/value-based.md.txt#animate-as-state) [![](http://developer.android.com/static/develop/ui/compose/images/animations/multiple_properties.gif)](http://developer.android.com/develop/ui/compose/animation/quick-guide.md.txt#concurrent-animations)

### [Animate multiple values together](http://developer.android.com/develop/ui/compose/animation/quick-guide.md.txt#concurrent-animations)

Use `Transition` to animate multiple values at once. [Learn more](http://developer.android.com/develop/ui/compose/animation/quick-guide.md.txt#concurrent-animations) [![](http://developer.android.com/static/develop/ui/compose/images/animations/animated_forever.gif)](http://developer.android.com/develop/ui/compose/animation/value-based.md.txt#rememberinfinitetransition)

### [Animate properties indefinitely](http://developer.android.com/develop/ui/compose/animation/value-based.md.txt#rememberinfinitetransition)

Use `InfiniteTransition` to animate properties continuously. [Learn more](http://developer.android.com/develop/ui/compose/animation/value-based.md.txt#rememberinfinitetransition) [![](http://developer.android.com/static/images/picto-icons/responsive-layout.svg)](http://developer.android.com/develop/ui/compose/animation/shared-elements.md.txt)

### [Shared element transitions](http://developer.android.com/develop/ui/compose/animation/shared-elements.md.txt)

Learn how to transition shared content between screens and composables with the `sharedElement` and `sharedBounds` modifiers. [Shared elements](http://developer.android.com/develop/ui/compose/animation/shared-elements.md.txt) [![](http://developer.android.com/static/images/picto-icons/interoperable.svg)](http://developer.android.com/develop/ui/compose/animation/customize.md.txt)

### [Customize your animations](http://developer.android.com/develop/ui/compose/animation/customize.md.txt)

Learn how to customize your animations duration, easing curve and spring configuration. [Customize](http://developer.android.com/develop/ui/compose/animation/customize.md.txt) [![](http://developer.android.com/static/images/picto-icons/bug-2.svg)](http://developer.android.com/develop/ui/compose/animation/testing.md.txt)

### [Test animations](http://developer.android.com/develop/ui/compose/animation/testing.md.txt)

Learn how to write tests for your animations. [Testing](http://developer.android.com/develop/ui/compose/animation/testing.md.txt) [![](http://developer.android.com/static/images/picto-icons/spanner.svg)](http://developer.android.com/develop/ui/compose/animation/tooling.md.txt)

### [Android Studio Tooling](http://developer.android.com/develop/ui/compose/animation/tooling.md.txt)

Learn all about how to preview your animations in Android Studio. [Tooling](http://developer.android.com/develop/ui/compose/animation/tooling.md.txt)