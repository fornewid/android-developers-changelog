---
title: https://developer.android.com/about/versions/nougat/android-7.1
url: https://developer.android.com/about/versions/nougat/android-7.1
source: md.txt
---

# Android 7.1 for Developers

The Android 7.1 update introduces a variety of new features and capabilities for users and developers. This document highlights what's new for developers.

## App Shortcuts

You can use the new*shortcuts*feature to bring users from the launcher directly to key actions within your app. Users simply long-press your app's launcher icon to reveal the app's shortcuts, then tap on a shortcut to jump to the associated action. These shortcuts are a great way to engage users, and they let you surface the functionality of your app even before users launch your app.

Each shortcut references an[intent](https://developer.android.com/guide/components/intents-filters), each of which launches a specific action or task, and you can create a shortcut for any action that you can express as an intent. For example, you can create intents for sending a new text message, making a reservation, playing a video, continuing a game, loading a map location, and much more.

You can create shortcuts for your app statically by adding them to a resource file in the APK, or you can add them dynamically at runtime. Static shortcuts are ideal for common actions, and dynamic shortcuts let you highlight actions based on users' preferences, behavior, location, and so on. You can offer up to five shortcuts in each of your apps. Note, however, that some launcher apps don't show every shortcut you've registered for your app.

After your app adds shortcuts, they're available on any launcher that supports them, such as the Pixel launcher (the default launcher on Pixel devices), the Now launcher (the default launcher on Nexus devices), and other launchers that provide support.

Any app can create shortcuts, and any launcher app can add support for shortcuts. Android 7.1 provides an API for apps to register shortcuts and launchers to read the registered shortcuts. For details, see the[App Shortcuts developer documentation](https://developer.android.com/guide/topics/ui/shortcuts).  
![Image keyboard support on Nexus 6P](https://developer.android.com/static/images/guide/topics/text/image-keyboard-sample.png)

*Image keyboard support:*Lets users input images and other content directly from a keyboard.  
![App shortcuts on Nexus 6P](https://developer.android.com/static/images/guide/topics/ui/shortcuts.png)

*App shortcuts:*Surface key actions and take users deep into your app instantly.

## Image Keyboard Support

Users often want to communicate with emojis, stickers, and other kinds of rich content. In previous versions of Android, soft keyboards (also known as[input method editors](https://developer.android.com/guide/topics/text/creating-input-method)or IMEs) could send only unicode emojis to apps. For rich content, apps had to either build app-specific emojis that couldn't be used in other apps, or use workarounds like sending images through an[Easy Share Action](https://developer.android.com/training/sharing/shareaction)or the clipboard.

Now in Android 7.1, the Android SDK includes the Commit Content API, which provides a universal way for IMEs to send images and other rich content directly to a text editor in an app. The API is also available in v13 Support Library as of revision 25.0.0.

With this API, you can build messaging apps that accept rich content from any keyboard, as well as, keyboards that can send rich content to any app. For details, see the[Image Keyboard Support developer documentation](https://developer.android.com/guide/topics/text/image-keyboard).

## New Professional Emoji

With Android 7.1, we're adding new emoji that represent a wider range of professions for women as well as men. The new emoji bring parity between our existing male emoji and female emoji and are available in a variety of skin tones.

If you're a keyboard or messaging app developer, you should start incorporating these emoji into your apps. You can dynamically check for the new emoji characters by calling[Paint.hasGlyph()](https://developer.android.com/reference/android/graphics/Paint#hasGlyph(java.lang.String)).
![Collection of new professional female emoji in a variety of skin tones](https://developer.android.com/static/images/about/versions/nougat/new-emoji-7.1.png)

## Enhanced Live Wallpaper Metadata

You can now provide metadata about your live wallpapers to any component that's displaying a preview of the wallpaper, such as a wallpaper picker app. You can show existing metadata attributes such as label, description, and author, as well as new attributes for a context URL and title to link users to more information about the wallpaper.

For more information, see the[Android Developers blog](https://android-developers.blogspot.com/2016/10/android-71-developer-preview.html).

## Round Icon Resources

![Screen displaying the Image Asset tool](https://developer.android.com/static/images/about/versions/nougat/round-icon.png)

You can use the Image Asset tool to quickly create circular icon assets.

Apps can now define circular launcher icons, which are used on devices that support them. When a launcher requests an app icon, the framework returns either`android:icon`or`android:roundIcon`, depending on the device build configuration. Because of this, apps should make sure to define both`android:icon`and`android:roundIcon`resources when responding to launcher intents. You can use[Image Asset Studio](https://developer.android.com/studio/write/image-asset-studio#access)to design round icons.

You should make sure to test your app on devices that support the new circular icons, to see how your circular app icons look and how they are displayed. One way to test your resources is to run the[Android emulator](https://developer.android.com/studio/run/emulator)and use a Google APIs Emulator System targeting API level 25. You can also test your icons by installing your app on a Google Pixel device.

For more information about designing app launcher icons, see the[Material Design guidelines](https://material.google.com/style/icons.html#icons-product-icons).

## Storage Manager Intent

Apps can now fire an`ACTION_MANAGE_STORAGE`intent, taking the user to the system's**Free up space**screen. For example, if an app requires more space than is currently available, it can use this intent to let the user delete unneeded apps and content to free up sufficient space.

## Improved VR Thread Scheduling

Android 7.1 provides new features to improve VR thread scheduling. This is useful since virtual reality apps are very latency sensitive.

Apps can now designate one thread as a VR thread. While the app is in[VR mode](https://developer.android.com/about/versions/nougat/android-7.0#vr), the system will schedule that thread more aggressively to minimize latency. A process may only have one VR thread at a time, and the system may subject that thread to restrictions on the amount of time it can run. The setting has no effect when the app is not in VR mode.

To designate a thread as a VR thread, call the new`ActivityManager.setVrThread()`method.

## Demo User Hint

Apps can now check to see if the device is running as the demo user.

Apps can call the new`UserManager.isDemoUser()`method to see if the app is running in a demo user sandbox. This allows apps to customize the starting experience to a potential customer. For example, when running as a demo user, an app might provide more assistance to the user, or explain its features in more detail.

## APIs for Carriers and Calling Apps

The system now provides new telephony features for carriers and telephone apps, including:

- Multi-endpoint calling
- CDMA voice privacy property
- Source type support for Visual Voicemail
- Carrier configuration options for managing video telephony

## New Screen Densities for Wear Devices

Android now supports several new screen densities for Wear devices, which more closely match some devices' physical specifications. This lets you fine-tune the graphics in your Wear apps to the screens they'll be displayed on, if necessary.

The new device densities are:

- `DENSITY_260`
- `DENSITY_300`
- `DENSITY_340`