---
title: https://developer.android.com/develop/xr/unity
url: https://developer.android.com/develop/xr/unity
source: md.txt
---

# Develop with Unity for Android XR

This guide provides an overview of developing with Unity for Android XR. Android XR works with the familiar tools and features you've come to expect from Unity, and since Unity's Android XR support is built on top of OpenXR, many of the features described in the[OpenXR Overview](https://developer.android.com/develop/xr/openxr)are also supported in Unity.

Follow this guide to learn about:

- Unity Support for Android XR
  - Unity XR basics
  - Developing and publishing apps for Android XR
  - Unity Packages for Android XR
    - Unity OpenXR: Android XR package
    - Android XR Extensions for Unity
    - Features and Compatibility Considerations
- Input and interaction

## Unity Support for Android XR

When you build Unity apps for Android XR, you can take advantage of the mixed reality tools and capabilities in the[latest versions of Unity 6](https://unity.com/releases/editor/archive). This includes mixed reality templates that use the[XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@latest),[AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest), and[OpenXR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest), to help you get started quickly. When building apps with Unity for Android XR, we recommend the Universal Render Pipeline (URP) as your render pipeline and Vulkan as your Graphics API. These features allow you to take advantage of some of the[graphics features](https://unity.com/srp/universal-render-pipeline)of Unity, which are only supported with Vulkan. Review the[project setup guide](https://developer.android.com/develop/xr/unity/setup)for more information on how to configure these settings.

### Unity XR Basics

If you are new to Unity or XR development, you can refer to[Unity's XR Manual](https://docs.unity3d.com/Manual/XR.html)to understand basic XR concepts and workflows. The XR Manual contains information about:

- [XR provider plug-ins](https://docs.unity3d.com/Manual/xr-support-packages.html#plug-ins), including[Unity OpenXR: Android XR](https://developer.android.com/develop/xr/unity#unity-openxr)and the Android XR Extensions for Unity
- [XR support packages](https://docs.unity3d.com/Manual/xr-support-packages.html#support-packages)to add additional application-level features
- An[XR architecture guide](https://docs.unity3d.com/Manual/XRPluginArchitecture.html)that describes the Unity XR tech stack and XR subsystems
- [XR project set up](https://docs.unity3d.com/Manual/configuring-project-for-xr.html)
- [Building and running XR apps](https://docs.unity3d.com/Manual/xr-run.html)
- [XR graphics guidance](https://docs.unity3d.com/Manual/xr-graphics.html), including Universal Render Pipeline, stereo rendering, foveated rendering, multiview render regions, and VR frame timing
- [XR audio guidance](https://docs.unity3d.com/Manual/xr-audio.html), including support for[audio spatializers](https://docs.unity3d.com/Manual/VRAudioSpatializer.html)

### Develop and publish apps for Android

Unity provides in-depth documentation for developing, building, and publishing for Android, covering topics including[Android permissions in Unity](https://docs.unity3d.com/Manual/android-permissions-in-unity.html),[Android Build Settings](https://docs.unity3d.com/Manual/android-build-settings.html),[Building your app for Android](https://docs.unity3d.com/Manual/android-BuildProcess.html), and[Delivering to Google Play](https://docs.unity3d.com/Manual/android-distribution-google-play.html).

### Unity Packages for Android XR

There are two packages that provide support for building Unity apps for Android XR. Both of these packages are XR provider plug-ins, which can be enabled through Unity's XR Plug-in Management[package](https://docs.unity3d.com/Manual/com.unity.xr.management.html). The XR plug-in manager adds Project Settings for managing and offering help with loading, initialization, settings, and build support for XR plug-ins. To allow your app to execute OpenXR features at runtime, the project must have these features enabled through the plug-in manager.

This image shows an example of where you can enable these feature groups through Unity's editor.

![Example of the unity xr plugin management screen](https://developer.android.com/static/images/develop/xr/unity/index/xr-plugin-management.png)

#### Unity OpenXR Android XR

The[Unity OpenXR Android XR package](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@latest/)is an XR Plug-in to add Android XR support to Unity. This XR Plug-in provides the majority of the Android XR support for Unity, and it enables Android XR device support for[AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest)projects. AR Foundation is designed for developers who want to create AR or mixed reality experiences. It provides the interface for AR features, but doesn't implement any features itself. The Unity OpenXR Android XR package provides the implementation. To get started with this package view the package manual, which contains a Getting Started guide.

#### Android XR Extensions for Unity

The[Android XR Extensions for Unity](https://github.com/android/android-xr-unity-package)supplements the Unity OpenXR Android XR package, and it includes additional features to help you build immersive experiences. It can be used alone or together with the Unity OpenXR Android XR package.

To get started with this package, follow our[project setup guide](https://developer.android.com/develop/xr/unity/setup)or[quickstart for importing Android XR Extensions for Unity](https://developer.android.com/develop/xr/unity/xr-extensions-quickstart).

#### Features and Compatibility Considerations

The following table describes the features supported by the Unity OpenXR: Android XR package and the Android XR Extensions for Unity package, and it can be used to determine which package contains the features you need and any compatibility considerations.

|                                                                        Feature                                                                         |                                                                             Unity OpenXR: Android XR feature string                                                                             |                                     Android XR Extensions for Unity feature string                                     |                                                                                                                                                                                                                                                                                                                                   Use cases and expected behavior                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AR Session](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/session.html)                                             | Android XR: AR Session - Feature settings include Optimize Buffer Discards (Vulkan)                                                                                                             | Android XR (Extensions): Session Management - Feature settings include Subsampling (Vulkan) and URP SpaceWarp (Vulkan) | To use features from either package, you must enable the AR Session feature for that package. You can enable both feature sets at the same time; individual features will handle conflicts accordingly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Device tracking](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/device-tracking.html)                                | N/A                                                                                                                                                                                             | N/A                                                                                                                    | Device tracking is used to track the device's position and rotation in physical space. The XR Origin[GameObject](https://docs.unity3d.com/6000.2/Documentation/Manual/class-GameObject.html)automatically handles device tracking and transforming trackables into Unity's coordinate system using its[XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-reference.html)component and GameObject hierarchy with a Camera and[TrackedPoseDriver](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/api/UnityEngine.InputSystem.XR.TrackedPoseDriver.html).                                                                                         |
| [Camera](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/camera.html)                                                  | Android XR: AR Camera                                                                                                                                                                           | N/A                                                                                                                    | This feature provides support for light estimation and full screen passthrough.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Plane detection](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/plane-detection.html)                                | Android XR: AR Plane                                                                                                                                                                            | Android XR (Extensions): Plane                                                                                         | These two features are identical; use one or the other. Android XR (Extensions): Plane is included so that developers can use the Android XR (Extensions): Object Tracking and persistent anchors features without having to have a dependency on the Unity OpenXR Android XR package. In the future, Android XR (Extensions): Plane will be removed in favor of Android XR: AR Anchor.                                                                                                                                                                                                                                                                                                             |
| [Object tracking](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/object-tracking.html)                                | N/A                                                                                                                                                                                             | Android XR (Extensions): Object Tracking                                                                               | This feature provides support for detecting and tracking objects in the physical environment, used in combination with a reference object library.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Face tracking](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/face-tracking.html)                                    | Android XR: AR Face - XR_ANDROID_eye_tracking only - No face tracking                                                                                                                           | Android XR: Face Tracking - XR_ANDROID_face_tracking                                                                   | Avatar eyes support is provided through the Android XR: AR Face feature. Access a user's facial expressions through the Android XR: Face Tracking feature. These two features can be used together.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Ray casts](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/raycasts.html)                                             | Android XR: AR Raycast - Plane Anchor - Depth Anchor                                                                                                                                            | N/A                                                                                                                    | This feature lets you cast a ray and calculate the intersection between that ray and plane trackables or depth trackables that are detected in the physical environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Anchors](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/anchors.html)                                                | Android XR: AR Anchor                                                                                                                                                                           | Android XR (Extensions): Anchor - Feature settings include persistence.                                                | Both features include support for spatial anchors and plane anchors; use one feature or the other. For persistent anchors, use Android XR (Extensions): Anchor. In the future, Android XR (Extensions): Anchor will be removed and all Anchor features will be in Android XR: AR Anchor.                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Occlusion](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/features/occlusion.html)                                            | Android XR: AR Occlusion - Environment Depth                                                                                                                                                    | N/A                                                                                                                    | Occlusion allows mixed reality content in your app to appear hidden or partially obscured behind objects in the physical environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Performance Metrics                                                                                                                                    | Android XR Performance Metrics                                                                                                                                                                  | N/A                                                                                                                    | Use this feature to access performance metrics for Android XR devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Composition Layers](https://docs.unity3d.com/Packages/com.unity.xr.compositionlayers@2.1/manual/usage-guide.html)                                     | Composition Layer Support (OpenXR Plugin and XR Composition Layer are required)                                                                                                                 | Android XR: Passthrough Composition Layer - XR_ANDROID_composition_layer_passthrough_mesh                              | Use Unity's Composition Layer Support to create basic[composition layers](https://registry.khronos.org/OpenXR/specs/1.0-khr/html/xrspec.html#composition-layer-types)(e.g. quad, cylinder, projection). Android XR: Passthrough Composition Layer can be used to create a passthrough layer with a custom mesh, reading from Unity's[GameObject](https://docs.unity3d.com/6000.2/Documentation/Manual/class-GameObject.html).                                                                                                                                                                                                                                                                       |
| [Foveated Rendering](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/features/foveatedrendering.html)                                | Foveated Rendering (OpenXR Plugin is required) - Supports eye-tracked foveated rendering: the higher resolution area is centered where the user is looking, making it less apparent to the user | Foveation (Legacy)                                                                                                     | Foveated rendering allows for speeding up rendering by lowering the resolution of areas in the user's peripheral vision. Unity's[foveated rendering feature](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/features/foveatedrendering.html)is only supported for apps using URP and Vulkan. The Foveation (Legacy) feature in the Android XR Extensions for Unity also supports Built-in Render Pipeline and OpenGL ES. We recommend using Unity's[foveated rendering feature](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/features/foveatedrendering.html)when possible, and note that both URP and Vulkan are recommended when building for Android XR. |
| [Unbounded Reference Space](https://docs.unity3d.com/ScriptReference/XR.TrackingOriginModeFlags.html)                                                  | N/A                                                                                                                                                                                             | Android XR: Unbounded Reference Space                                                                                  | This feature sets the[XRInputSubsystem](https://docs.unity3d.com/ScriptReference/XR.XRInputSubsystem.html)tracking origin mode to[Unbounded](https://docs.unity3d.com/ScriptReference/XR.TrackingOriginModeFlags.Unbounded.html). Unbounded indicates that the XRInputSubsystem tracks all InputDevices in relation to a world anchor, which can change.                                                                                                                                                                                                                                                                                                                                            |
| [Environment Blend Mode](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/api/UnityEngine.XR.OpenXR.NativeTypes.XrEnvironmentBlendMode.html) | N/A                                                                                                                                                                                             | Environment Blend Mode                                                                                                 | This feature lets you set the[XR Environment Blend Mode](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/api/UnityEngine.XR.OpenXR.Features.OpenXRFeature.html#UnityEngine_XR_OpenXR_Features_OpenXRFeature_SetEnvironmentBlendMode_UnityEngine_XR_OpenXR_NativeTypes_XrEnvironmentBlendMode_), which controls how virtual imagery blends with the real-world environment when passthrough is enabled.                                                                                                                                                                                                                                                                                   |

## Input and interaction

Android XR supports multi-modal natural input.
| **Note:** Hand input is the default.

In addition to hand and eye tracking, peripherals such as 6DoF controllers, mouse, and physical keyboard are also supported. This means that apps for Android XR are expected to support hand interaction, and it cannot be assumed that all devices will come with controllers.

### Interaction Profiles

Unity uses[interaction profile](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/project-configuration.html#interaction-profile)to manage how your XR application communicates with various XR devices and platforms. These profiles establish the expected inputs and outputs for different hardware configurations, promoting compatibility and consistent functionality across a range of platforms. By enabling interaction profiles, you can help ensure that your XR application functions correctly with different devices, maintains consistent input mapping, and has access to specific XR features. To set an interaction profile:

1. Open the**Project Settings** window (menu:**Edit \> Project Settings**).
2. Click**XR Plug-in Management**to expand the plug-in section (if necessary).
3. Select**OpenXR**in the list of XR plug-ins.
4. In the**Interaction Profiles** section, select the**+**button to add a profile.
5. Select the profile to add from the list.

### Hand Interaction

Hand interaction ([`XR_EXT_hand_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_interaction)) is provided by the[OpenXR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest), and you can expose the`<HandInteraction>`device layout in the[Unity Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/index.html)by enabling the[Hand Interaction Profile](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/features/handinteractionprofile.html). Use this interaction profile for hand input supported by the four action poses defined by OpenXR: "pinch", "poke", "aim", and "grip". If you need additional hand interaction or hand tracking functionality, refer to[XR Hands](https://developer.android.com/develop/xr/unity#xr-hands)on this page.
| **Note:** Because this feature doesn't surface sensitive data, using the Hand Interaction profile doesn't require requesting any permissions.

### Eye Gaze Interaction

Eye gaze interaction ([`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction)) is provided by the OpenXR Plugin, and you can use this layout to retrieve the eye pose data (position and rotation) that the extension returns.[Read more about eye gaze interaction in the OpenXR Input guide](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/features/eyegazeinteraction.html).
| **Note:** Using the Eye Gaze Interaction profile requires the[`android.permission.EYE_TRACKING_FINE`](https://developer.android.com/develop/xr/get-started#permissions-xr)permission.

### Controller Interaction

Android XR supports the[Oculus Touch Controller Profile](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/features/oculustouchcontrollerprofile.html)for 6DoF controllers. Both of these profiles are provided by the OpenXR Plugin.

### Mouse Interaction

The[Android XR Mouse Interaction Profile (`XR_ANDROID_mouse_interaction`)](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRMouseInteractionProfile)is provided by the Android XR Extensions for Unity. It exposes an`<AndroidXRMouse>`device layout in the[Unity Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/index.html).

### Palm Pose Interaction

The OpenXR Plugin provides support for the[Palm Pose Interaction](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/features/palmposeinteraction.html)([`XR_EXT_palm_pose`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_palm_pose)), which exposes the`<PalmPose>`layout within the[Unity Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/index.html). Palm pose is not meant to be an alternative to extensions or packages that perform hand tracking for more complex use cases; instead it can be used to place app-specific visual content such as avatar visuals. The palm pose consists of both palm position and orientation.

### XR Hands

The[XR Hands package](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.6/manual/index.html)lets you access hand tracking data---using[`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking)and[`XR_FB_hand_tracking_aim`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_aim)---and provides a wrapper to convert hand joint data from hand tracking to input poses. To use the features provided by the XR Hands package, enable the**Hand Tracking Subsystem** and**Meta Hand Tracking Aim OpenXR**features.

![Example showing how to enable hand tracking](https://developer.android.com/static/images/develop/xr/unity/index/enable-hand-tracking.png)

The XR hands package can be useful if you need more granular hand pose or hand joint data or when you need to work with custom gestures.

For more details, see Unity's[documentation for setting up XR Hands in your project](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.6/manual/project-setup/project-setup.html)
| **Note:** Using the XR Hands package requires the[`android.permission.HAND_TRACKING`permission](https://developer.android.com/develop/xr/get-started#permissions-xr).

### Face Tracking Confidence Regions

The`XR_ANDROID_face_tracking`extension provides confidence values for three facial regions: upper left, upper right, and lower face. These values, ranging from 0 (no confidence) to 1 (highest confidence), indicate the accuracy of the face tracking for each region.

You can use these confidence values to progressively disable blendshapes or apply visual filters (like blurring) to the corresponding face region. For a basic deactivate blendshapes in the corresponding face region.

The "lower face" area represents everything under the eyes, including the mouth, chin, cheek, and nose. The two upper regions include the eyes and brow area on the left and right sides of the face.

The following C# code snippet demonstrates how to access and use the confidence data in a Unity script:  

    using UnityEngine;
    using Google.XR.Extensions;

    public class FaceTrackingConfidence : MonoBehaviour
    {
        void Update()
        {
          if (!XRFaceTrackingFeature.IsFaceTrackingExtensionEnabled.HasValue)
          {
            DebugTextTopCenter.text = "XrInstance hasn't been initialized.";
            return;
          }
          else if (!XRFaceTrackingFeature.IsFaceTrackingExtensionEnabled.Value)
          {
            DebugTextTopCenter.text = "XR_ANDROID_face_tracking is not enabled.";
            return;
          }

          for (int x = 0; x < _faceManager.Face.ConfidenceRegions.Length; x++)
          {
            switch (x)
            {
              case (int)XRFaceConfidenceRegion.Lower:
                regionText = "Bottom";
                break;
              case (int)XRFaceConfidenceRegion.LeftUpper:
                regionText = DebugTextConfidenceLeft;
                break;
              case (int)XRFaceConfidenceRegion.RightUpper:
                regionText = DebugTextConfidenceRight;
                break;
            }
        }
    }

For more information, see the[Android XR Extensions for Unity documentation](https://github.com/android/android-xr-unity-package).

### Choose a way to render hands

Android XR supports two ways of rendering hands: a hand mesh and a prefab visualizer.

#### Hand mesh

The[Android XR Unity package](https://developer.android.com/develop/xr/unity#android-xr-extensions-unity)contains a Hand Mesh feature that provides access to the[`XR_ANDROID_hand_mesh extension`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRHandMeshFeature). The Hand Mesh feature provides meshes for the user's hands. The hand mesh contains vertices of triangles that represent the geometry of a hand. This feature is intended to be used to provide a personalized mesh representing the real geometry of the user's hands for visualization.

#### XR Hands prefab

The[XR Hands package](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.6/manual/index.html)contains a sample called[Hands visualizer](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.1/manual/index.html), which contains fully rigged left and right hands for rendering context-appropriate representation of the user's hands.

### System gestures

Android XR includes a system gesture to open a menu for users to go back, open the launcher or get an overview of running apps. The user can activate this system menu by using a dominant-hand pinch.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/develop/xr/unity/index/pinch-gesture.mp4)and watch it with a video player.

When the user is interacting with the system navigation menu, the application will only respond to head tracking events. The XR Hands package can detect when a user performs specific actions such as interacting with this system navigation menu. Checking for`AimFlags`,`SystemGesture`, and`DominantHand`lets you know when this system action is performed. For more information on`AimFlags`, refer to Unity's[Enum MetaAimFlags documentation](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.1/api/UnityEngine.XR.Hands.MetaAimFlags.html).

### XR Interaction Toolkit

The[XR Interaction Toolkit package](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@latest)is a high-level, component-based, interaction system for creating VR and AR experiences. It provides a framework that makes 3D and UI interactions available from Unity input events. It supports interaction tasks including haptic feedback, visual feedback, and locomotion.

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.