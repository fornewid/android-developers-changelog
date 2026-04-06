---
title: https://developer.android.com/productivity/guides/basic-better-best
url: https://developer.android.com/productivity/guides/basic-better-best
source: md.txt
---

# Take your productivity app to the next level — basic, better, and best

This guide charts the optimal progression of a productivity app from a likely starting place to best-in-class. It's designed to help you think about improving your app over time, deciding what features to implement when. While every productivity app is different, consider these recommendations to achieve a best-in-class app.

## Basic

A basic productivity app must support a subset of Android software and hardware features so it doesn't get in the way of user productivity.

- **Accessibility**   
  Follow[Material Design guidelines to design and develop your app for accessibility.](https://developer.android.com/guide/topics/ui/accessibility)
- **Spellcheck**   
  Implement[spell checking](https://developer.android.com/develop/ui/views/touch-and-input/spell-checker-framework#SpellCheckClient)in your app.
- **Sharing and app interoperability**   
  Use[photo picker](https://developer.android.com/training/data-storage/shared/photopicker)to access existing photos and videos  
  Support copy and paste[with views](https://developer.android.com/develop/ui/views/touch-and-input/copy-paste)or[with Compose.](https://developer.android.com/develop/ui/compose/touch-input/copy-and-paste)
- **Hardware input**   
  Support keyboard navigation[with views](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/navigation)or[with Compose.](https://developer.android.com/develop/ui/compose/touch-input/focus)  
  Support alternative pointing devices such as mouse, trackpad, and stylus[with views](https://developer.android.com/develop/ui/views/touch-and-input/input-events)or[with Compose.](https://developer.android.com/develop/ui/compose/touch-input/pointer-input))
- **Large screens**   
  Support devices with[large screens](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes), such as laptop and tablet devices.  
  Support folding devices with[app continuity](https://developer.android.com/guide/topics/large-screens/learn-about-foldables#app_continuity)when transitioning between folded and unfolded states.
- **Expressive text**   
  Support emoji[with views](https://developer.android.com/guide/topics/large-screens/learn-about-foldables#app_continuity)or[with Compose.](https://developer.android.com/develop/ui/compose/text/emoji))

## Better

- **Large screens**   
  Support fully[adaptive layout,](https://developer.android.com/guide/topics/large-screens/multi-window-support)including window resizing.
- **Home screen integration**   
  Have an[app widget.](https://developer.android.com/develop/ui/compose/glance/create-app-widget)
- **Hardware input**   
  Support keyboard[shortcuts](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper), either[with views](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/commands)or[with Compose.](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/commands)  
  Support hover events for mouse/trackpad/stylus[with views](https://developer.android.com/reference/android/view/View.OnHoverListener)or[with Compose.](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/handling-interactions#producing-modifier))
- **Sharing and app interoperability**   
  Support drag and drop[with views](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop)or[with Compose.](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop)  
  Support image[keyboards](https://developer.android.com/develop/ui/views/receive-rich-content)and other rich content.  
  Use the[Storage Access Framework](https://developer.android.com/training/data-storage/shared/documents-files)to create and open documents that can be shared.
- **Printing and exporting to PDF**   
  Support[printers](https://developer.android.com/training/printing/custom-docs)and other output devices.

## Best

- **Leverage AI**   
  Use[on-device](https://developer.android.com/ai/aicore)or[cloud-based](https://developer.android.com/ai/vertex-ai-firebase)generative AI to improve user productivity.
- **Hardware**   
  Leverage[foldable postures.](https://developer.android.com/guide/topics/large-screens/make-apps-fold-aware)  
  Directly support[external displays.](https://developer.android.com/reference/android/app/Presentation)  
  Support drawing[using a stylus](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/about-ink-api), minimizing latency.  
  Support[advanced stylus features](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features)such as tilt and pressure.
- **Multi-window**   
  Support multiple[app windows with concurrent documents](https://medium.com/google-developers/dominating-the-overview-screen-eef18d2195d)for full desktop functionality.