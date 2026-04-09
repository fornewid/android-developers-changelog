---
title: https://developer.android.com/media/media3/transformer/demo-application
url: https://developer.android.com/media/media3/transformer/demo-application
source: md.txt
---

# Transformer demo application

The Transformer demo app lets you try out the API's capabilities and transform
your own media, including converting media between formats, trimming, and
applying video effects.

This page describes how to get, compile, and run the demo app. This guide also
describes how to use the demo app to transform your own media.

## Get the code

The source code for the main demo app can be found in the `demos/transformer`
folder of the [GitHub project](https://github.com/androidx/media). If you
haven't already done so, clone the project into a local directory:  

```
git clone https://github.com/androidx/media.git
```

Next, open the project in Android Studio. You should see the following in the
Android Project view (the relevant folders of the demo app have been expanded):
![The project in Android Studio](https://developer.android.com/static/guide/topics/media/transformer/images/demo-project.png) The project in Android Studio

## Compile and run the demo

To compile and run the demo app, select and run the `demo-transformer`
configuration in Android Studio. The demo app will install and run on a
connected Android-powered device. We recommend using a physical device if
possible, because typically an emulator's implementation of Android's media
stack has different capabilities and bugs compared to a real device.
![Demo app configuration activity](https://developer.android.com/static/guide/topics/media/transformer/images/configuration-activity.png) Demo app configuration activity

The demo app begins with the `ConfigurationActivity`, an activity where you can
set up the input media item and the transformation you want to perform. The two
buttons at the top of the screen let you choose from a list of preset media
files or pick a local file. Next, the scrollable list of options lets you
configure the output format and transformations, and you can select effects to
apply to the media. Tapping the last button transitions to
`TransformerActivity`, an activity that shows the current progress and a preview
of frames as they are passing through Transformer. Once transformation
completes, the input and output videos are shown together in two ExoPlayer
`PlayerView` instances.

## Transform your own content

The demo app supports selecting media for transformation using the buttons at
the top of the configuration screen. You can also pass a URL directly on the
command line:  

```
adb shell am start -a androidx.media3.demo.transformer.action.VIEW \
    -d https://yourdomain.com/sample.mp4
```
| **Tip:** If you see errors when selecting local media using this feature, check the [troubleshooting page](https://developer.android.com/media/media3/transformer/troubleshooting#local-files).

## MediaPipe integration

The demo app includes an example integration with
[MediaPipe](https://developers.google.com/mediapipe). You will need to build the
dependency manually, then select the `withMediaPipe` build variant to enable
building the app with the media pipe frame processor. See the
[README](https://github.com/androidx/media/tree/release/demos/transformer#mediapipe-frame-processing-demo)
for full instructions. The effects selector in the configuration activity
includes an example MediaPipe-based effect to try this out.