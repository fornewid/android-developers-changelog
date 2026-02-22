---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-connected-displays
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-connected-displays
source: md.txt
---

Connected displays extend the [desktop windowing](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-desktop-windowing) experience to standard phones, giving users access to large screens from their mobile devices. This capability opens up new possibilities for app interaction and user productivity.

All the unique features of desktop windowing apply to connected displays. When you connect a phone to a display, the phone's state remains unchanged, and a blank desktop session starts on the connected display. The device and the display act as two individual systems, with apps specific to each display.
Your browser doesn't support the video tag. **Figure 1.** Phone connected to an external display, with a desktop session on the display while the phone maintains its own state.

If you connect a desktop windowing--enabled device, such as a tablet, to an external monitor, the desktop session extends across both displays. The two displays then function as one continuous system. This setup allows windows, content, and the cursor to move freely between the two displays.
Your browser doesn't support the video tag. **Figure 2.** Tablet connected to an external monitor, extending the desktop session across both displays.

Supporting connected displays effectively requires attention to several aspects of your app's design and implementation. The following best practices ensure a smooth and productive user experience.

## Handle dynamic display changes

Many apps are built with the assumption that the [`Display`](https://developer.android.com/reference/kotlin/android/view/Display) object and its characteristics won't change during the app's lifecycle. However, when a user connects or disconnects an external monitor, or even moves an app window between displays, the underlying `Display` object associated with your app's context or window can change. The display's properties, such as size, resolution, refresh rate, HDR support, and density, can all be different. If you hardcode values based on the phone's screen, for example, your layouts will likely break on an external display.

External displays can also have vastly different pixel densities. You need to make sure your app responds correctly to [density changes](https://developer.android.com/guide/topics/manifest/activity-element#config). This involves using density-independent pixels (dp) for layouts, providing density-specific resources, and ensuring your UI scales appropriately.

### Use the right context

Using the right context is crucial in multi-display environments. When accessing resources, the activity context (which is displayed) is different from the application context (which is not displayed).

The activity context contains information about the display and is always adjusted for the display area in which the activity appears. This enables you to get the correct information about the display density or window metrics of your app. Always use the activity context (or another UI-based context) to get information about the current window or display. This also affects some system APIs that use information from the context.

### Get display information

You can use the [`Display`](https://developer.android.com/reference/kotlin/android/view/Display) class to get information about a particular display, such as its size or flags that indicate whether a display is secure. To get the available displays, use the [`DisplayManager`](https://developer.android.com/reference/kotlin/android/hardware/display/DisplayManager) system service:

    val displayManager = getSystemService(Context.DISPLAY_SERVICE) as DisplayManager
    val displays = displayManager.getDisplays()

## Manage activity launch and configuration

With connected displays, apps can specify which display an app should run on when it launches or when it creates another activity. This behavior depends on the activity launch mode defined in the manifest file and on the intent flags and options set by the entity launching the activity.

When an activity moves to a secondary display, your app can experience a context update, window resizing, and configuration and resource changes. If the activity handles the configuration change, it is notified in [`onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/app/Activity#onconfigurationchanged). Otherwise, the activity is relaunched.

If the selected launch mode for an activity allows multiple instances, launching on a secondary screen can create a new instance of the activity. Both activities are resumed at the same time, which can be beneficial for certain multitasking scenarios.

You can launch an activity on a particular display using [`ActivityOptions`](https://developer.android.com/reference/kotlin/android/app/ActivityOptions):

    val options = ActivityOptions.makeBasic()
    options.setLaunchDisplayId(targetDisplay.displayId)
    startActivity(intent, options.toBundle())

## Avoid device allowlists

Apps sometimes restrict large screen UI and features to select devices through an allowlist or by checking the built-in display size. With connected displays, this approach is no longer effective, as virtually any new device can be connected to a large screen. Design your app to be responsive and adaptable to various screen sizes and densities.

## Support external peripherals

When users connect to an external display, they often create a more desktop-like environment. This frequently involves using external keyboards, mice, trackpads, webcams, microphones, and speakers. You need to ensure your app works seamlessly with these peripherals. This includes handling keyboard shortcuts, managing mouse pointer interactions, correctly supporting external cameras or microphones, and respecting audio output routing. For more details, see [Input compatibility on large screens](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens).

## Enhance user productivity

Connected displays provide a significant opportunity to improve [user productivity](https://developer.android.com/large-screens/gallery/productivity). You now have the tools to build mobile apps that can offer experiences comparable to desktop applications. Consider implementing the following features to [boost user productivity](https://www.youtube.com/watch?v=MmeJSLAnB-M):

- Allow users to open multiple instances of the same app. This is invaluable for tasks like comparing documents, managing different conversations, or viewing multiple files simultaneously.
- Enable users to share rich data in and out of your app with [drag and drop](https://developer.android.com/guide/topics/large-screens/drag-and-drop).
- Help users maintain their workflow across configuration changes by implementing a robust [state management system](https://developer.android.com/guide/topics/large-screens/configuration-and-continuity).

By following these guidelines and utilizing the provided code examples, you can create apps that seamlessly adapt to connected displays, offering users a richer and more productive experience.