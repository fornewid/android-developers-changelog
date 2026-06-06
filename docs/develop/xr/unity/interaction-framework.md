---
title: https://developer.android.com/develop/xr/unity/interaction-framework
url: https://developer.android.com/develop/xr/unity/interaction-framework
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The [Android XR Interaction Framework](https://developer.android.com/develop/xr/interaction-framework) (AXRIF) provides familiar, high-level,
opinionated interactions for OpenXR applications on Android XR. AXRIF bridges
the gap between system-level interactions and in-app interactions, offering an
intuitive and cohesive way to handle user input.

Follow this guide to set up and get started using AXRIF with Unity.

## Prerequisites

Before beginning, ensure your development environment meets the following
requirements:

- **Unity version** : Unity 6 [version 6000.3.12f1](https://unity.com/releases/editor/whats-new/6000.3.12f1) or higher.
- **Project setup** : Complete all steps in the [Unity project setup](https://developer.android.com/develop/xr/unity/setup) guide.

## Set up and configure Unity

Before you can try out the sample scene, you need to set up and configure Unity
for AXRIF. Follow the steps in the following sections to complete this process.

### Import the AXRIF package

First, install the AXRIF package and its dependencies:

1. Navigate to **Window \> Package Manager**.
2. Open the add menu in the **Package Manager** toolbar.
3. In the options for adding packages, click **+** (plus).
4. From the drop-down menu, select **Install package from git URL**.

   ![Import the AXRIF package using its git URL.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/import-package-git-url.png)
5. Enter the following URL:

   `https://github.com/android-xr/android-xr-interaction-framework-unity-package.git`
6. Click **Install**.

   ![The AXRIF package details in Unity's Package Manager.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/import-axrif.png)

#### Check the XR Interaction Toolkit version

The AXRIF package works alongside the Unity XR Interaction Toolkit (XRIT) and
doesn't replace it. Because the AXRIF package defines a dependency to XRIT,
Unity should have installed XRIT when you installed the AXRIF package in the
previous steps. However, you should check that version 3.3.1 or higher is
installed by navigating to **Window \> Package Manager \> Unity Registry \> XR
Interaction Toolkit** in the Unity Editor.
![](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/xrit-package.png) **Figure 1.** Check the installed version of the XR Interaction Toolkit in the Unity Editor.

### Select the Android XR build profile

Select the Android XR build profile to enable appropriate OpenXR Extensions and
build settings for Android XR:

1. Navigate to **File \> Build Profiles**.
2. Click **Android XR** , and then click **Switch Platform**.

   > [!NOTE]
   > **Note:** Depending on your version of Unity, you might also have to click **Enable Platform** for the Android XR build profile.

   ![Select the Android XR build profile in Unity's settings.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/android-xr-build-profile.png)

### Configure OpenXR settings

Configure Unity's OpenXR settings so Unity can access the necessary OpenXR
data:

1. Navigate to **Edit \> Project Settings \> XR Plug-in Management \> OpenXR**.
2. In the **Android tab** , click **+** (plus) for the **Enabled Interaction
   Profiles** section.
3. Add any of the following profiles, depending on your app's needs:

   - Eye Gaze Interaction Profile
   - Hand Interaction Profile
   - Oculus Touch Controller Profile
   - Android XR Mouse Interaction Profile
4. In the features list in **XR Plug-in Management \> OpenXR**, enable the
   following features:

   - Android XR (Extensions): Passthrough Composition Layer
   - Android XR (Extensions): Session Management
   - Android XR Support
   - Android XR: AR Camera
   - Android XR: AR Session
   - Android XR: AR Hand Mesh Data
   - Composition Layers Support
   - Hand Tracking Subsystem

#### Perform project validation

Perform project validation to fix any OpenXR errors in your project's
configuration:

1. Navigate to **Edit** \> **Project Settings** \> **XR Plug-in Management** \> **Project Validation**.
2. Fix any outstanding alerts or warnings to ensure runtime errors don't affect
   compilation.

   ![Resolve any outstanding OpenXR issues by performing project validation.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/openxr-project-validation.png)

## Use the sample scene

Now that you've finished the preliminary setup and configuration, you can use
the AXRIF sample scene. Follow the steps in the following sections to get the
sample scene and try it out.

### Import XRIT sample packages and the AXRIF sample

The AXRIF sample scene depends on Unity's XR Interaction Toolkit (XRIT) Starter
Assets and Hands Interaction Demo sample packages.

#### Import XRIT sample packages

Import the XRIT sample packages that the AXRIF sample depends on:

1. Navigate to **Window \> Package Manager**.
2. Select **XR Interaction Toolkit** from the package list.
3. In the **Samples** tab, click **Import** next to both **Starter Assets** and
   **Hands Interaction Demo**.

   ![Import the required XRIT sample packages before you import the AXRIF sample package.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/xrit-sample-packages.png)

#### Import the AXRIF sample

Import the AXRIF sample to get the sample scene:

1. Navigate to **Window \> Package Manager**.
2. Select **Android XR Interaction Framework** from the package list.
3. In the **Samples** tab, click **Import** next to **Axrif Sample**.

   ![Import the AXRIF sample in Unity's package manager.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/axrif-sample-package.png)

### Open the Scene

After you've imported the required sample packages, you can open the scene:

1. Navigate to **Assets \> Samples \> Android XR Interaction Framework \> \[AXRIF
   Version Number\] \> Axrif Sample**.
2. Open **AxrifDemoScene**.

   ![Import the AXRIF sample package in Unity's package manager.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/open-scene.png)

### Explore the prefabs

The scene comes pre-configured using modular prefabs located under **Packages \>
Android XR Interaction Framework \> Prefabs**.

#### Interactor prefabs

The Axrif Interactor prefabs drive Unity XRIT interactor mechanics using the
corresponding input modalities from the following list:

- **Hand/Controller Ray** :
  - Axrif Left Interactor - Uses left hand raycast or controller.
  - Axrif Right Interactor - Uses right hand raycast or controller.
- **Gaze Pinch** :
  - Axrif Left GazePinch Interactor - Uses eye gaze and left-hand motion when pinching.
  - Axrif Right GazePinch Interactor - Uses eye gaze and right-hand motion when pinching.
  - Axrif Gaze Interactor - Uses eye gaze to point only.
- **Hand Poke** :
  - Axrif Left Poke Interactor - Uses left index finger when touching interactables.
  - Axrif Right Poke Interactor - Uses right index finger when touching interactables.
- **Mouse** :
  - Axrif Mouse Interactor - Uses Android XR spatial mouse.

#### Axrif Interaction Manager and Origin prefabs

- **Axrif Interaction Manager**: This prefab is the central hub for AXRIF in
  the scene. The prefab houses the Axrif Interaction Manager component, which
  is designed to work in conjunction with the XRIT XR Interaction Manager.
  This prefab is responsible for:

  - Initializing and managing the core AXRIF subsystems at runtime.
  - Processing and routing input data from OpenXR using the Interaction Framework Input Adapter.
  - Observing UI and collider states using the Interaction Framework Scene Integrator.
- **Axrif XR Origin**: Serves as the main character and camera driver and
  manages hand-mesh visualizers.

  > [!NOTE]
  > **Note:** The Main Camera on this prefab dictates passthrough rendering behaviors by default. If you prefer virtual environments, update the camera background or clear flags to a Skybox or Solid Color.

### Configure input actions

To bridge the OpenXR runtime data with Unity's Input Actions, register
project-wide map bindings:

1. Navigate to **Packages \> Android XR Interaction Framework \> InputActions**.
2. Locate **AndroidXRInteractionFramework Input Actions**.
3. Click **Assign as the Project-wide Input Actions**.

   ![Configure input actions for Unity to bridge runtime data with Unity's Input Actions.](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/input-actions.png)

### Modify interactions

Using the Axrif Interaction Manager prefab, you can enable or disable different
input modalities. AXRIF supports the following input modalities:

- Controller Raycasting
- Pinch and Gaze
- Hand Raycasting
- Direct Hand
- Mouse Interactions.

You can configure input modalities directly inside the Inspector in the
**Configurations** section of the **Interaction Framework Manager** component.
![](https://developer.android.com/static/images/develop/xr/unity/interaction-framework/modify-interactions.png) **Figure 2.** Configure input modalities inside the Inspector.

### Build the sample

When you want to build the sample, click **Build** or **Build and Run** in the
Unity Editor.

> [!NOTE]
> **Note:** Compiling the sample triggers AXRIF build scripts that package internal native library plugins and make temporary injections to the `AndroidManifest.xml` file, which are required for context permissions.