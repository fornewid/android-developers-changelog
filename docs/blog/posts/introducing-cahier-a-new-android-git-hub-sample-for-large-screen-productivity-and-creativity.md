---
title: https://developer.android.com/blog/posts/introducing-cahier-a-new-android-git-hub-sample-for-large-screen-productivity-and-creativity
url: https://developer.android.com/blog/posts/introducing-cahier-a-new-android-git-hub-sample-for-large-screen-productivity-and-creativity
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Introducing Cahier: A new Android GitHub sample for large screen productivity and creativity

###### 11-min read

![](https://developer.android.com/static/blog/assets/introducing_Cahier_792458c981_Z15HUkw.webp) 29 Oct 2025 [![](https://developer.android.com/static/blog/assets/Chris_Assigbe_2_a72a1e1687_sAjN.webp)](https://developer.android.com/blog/authors/chris-assigbe) [##### Chris Assigbe](https://developer.android.com/blog/authors/chris-assigbe)

###### Developer Relations Engineer

[Ink API](https://developer.android.com/jetpack/androidx/releases/ink) is now in [beta](https://developer.android.com/jetpack/androidx/releases/ink#1.0.0-beta01) and is ready to be integrated in your app. This milestone was made possible by valuable developer feedback, leading to continuous improvements in the API's performance, stability, and visual quality.

Google apps, such as [Google Docs](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.docs), [Pixel Studio](https://play.google.com/store/apps/details?id=com.google.android.apps.pixel.creativeassistant), [Google Photos](https://play.google.com/store/apps/details?id=com.google.android.apps.photos), [Chrome PDF](https://www.google.com/chrome/?brand=FHFK&ds_kid=10484928882&gclsrc=aw.ds&gad_source=1&gad_campaignid=22668273831&gbraid=0AAAAAoY3CA6P2Qnecu3wa4SGbiQesRxPr&gclid=CjwKCAjwx-zHBhBhEiwA7Kjq65_0B9_-VnywwemCbmR19p7LrWt-Zg8Ych8WNzYj_aF60bs5Xi2PlBoCtWQQAvD_BwE), [Youtube Effect Maker,](https://effects.youtube.com/) and unique features on Android such as [Circle to Search](https://search.google/ways-to-search/circle-to-search/) all use the latest APIs.

To mark this milestone, we're excited to announce the launch of [Cahier](https://github.com/android/cahier), a comprehensive note-taking app sample optimized for Android devices of all sizes particularly tablets and foldable phones.

## What is Cahier?

[Cahier](https://github.com/android/cahier) ("notebook" in French) is a sample app designed to demonstrate how you can build an application that enables users to capture and organize their thoughts by combining text, drawings, and images.

The sample can serve as the go-to reference for enhancing user productivity and creativity on large screens. It showcases best practices for building such experiences, accelerating developer understanding and adoption of related powerful APIs and techniques. This post walks you through the core features of Cahier, key APIs, and the architectural decisions that make the sample a great reference for your own apps.

Key features demonstrated in the sample include:

- **Versatile note creation:** Shows how to implement a flexible content creation system that supports multiple formats within a single note, including text, freeform drawings, and image attachments.
- **Creative inking tools** : Implements a high performance, low latency drawing experience using the [Ink API](https://developer.android.com/jetpack/androidx/releases/ink). The sample provides a practical example of integrating various brushes, a color picker, undo/redo functionality, and an eraser tool.
- **Fluid content integration with drag and drop**: Demonstrates how to handle both incoming and outgoing content using drag and drop. This includes accepting images dropped from other apps and enabling users to drag content out of your app for seamless sharing.
- **Note organization**: Mark notes as favorites for quick access. Filter the view to stay organized.
- **Offline first architecture:** Built with an offline first architecture using [Room](https://developer.android.com/jetpack/androidx/releases/room), ensuring all data is saved locally and the app remains fully functional without an internet connection.
- **Powerful multi-window and multi-instance support**: Showcases how to support multi-instance, allowing your app to be launched in multiple windows so users can work on different notes side by side, enhancing productivity and creativity on large screens.
- **Adaptive UI for all screens** : The user interface seamlessly adapts to different screen sizes and orientations using [ListDetailPaneScaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) and [NavigationSuiteScaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuiteScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteColors,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0)) to provide an optimized user experience on phones, tablets, and foldables.
- **Deep system integration**: Provides a guide on how to make your app the default note-taking app on Android 14 and higher by responding to system wide Notes intents, enabling quick content capture from various system entry points.

## Built for productivity and creativity on large screens

For the initial launch, we're centering the announcement on a few core features that make **Cahie**r a key learning resource for both productivity and creativity use cases.

#### A foundation of adaptivity

**Cahier** is built to be adaptive from the ground up. The sample utilizes the [material3-adaptive](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) library specifically [ListDetailPaneScaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldValue,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) and [NavigationSuiteScaffold](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuiteScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteColors,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0)) to seamlessly adapt the app layout to various screen sizes and orientations. This is a crucial element for a modern Android app, and **Cahier** provides a clear example of how to implement it effectively.
![Cahier adaptive UI built with Material 3 Adaptive library..gif](https://developer.android.com/static/blog/assets/Cahier_adaptive_UI_built_with_Material_3_Adaptive_library_9bc6538d7c_gy0Dn.webp)

*Cahier adaptive UI built with Material 3 Adaptive library*

### Showcasing key APIs and integrations

The sample is focused on showcasing powerful productivity APIs that you can leverage in your own applications, including:

- [Ink API](https://developer.android.com/jetpack/androidx/releases/ink)
- [Notes role](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/create-a-note-taking-app#notes_role)
- [Multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance), [Multi-window](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance), and [Desktop windowing](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-desktop-windowing)
- [Drag and drop](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop)

## A Closer look at key APIs

Let's dive deeper into two of the cornerstone APIs that Cahier integrates to deliver a first class note-taking experience.

### Creating natural inking experiences with the Ink API

Stylus input transforms large screen devices into digital notebooks and sketchbooks. To help you build fluid and natural inking experiences, we've made the Ink API a cornerstone of the sample. Ink API makes it easy to create, render, and manipulate beautiful ink strokes with best in class low latency.

Ink API offers a modular architecture, so you can tailor it to your app's specific stack and needs. The API modules include:

- **Authoring modules (** [**Compose**](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary)**-** [**views**](https://developer.android.com/reference/kotlin/androidx/ink/authoring/package-summary)**):** Handle realtime inking input to create smooth strokes with the lowest latency a device can provide.
  - In [DrawingSurface](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/DrawingSurface.kt), Cahier uses the newly introduced [InProgressStrokes](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary#InProgressStrokes(androidx.ink.brush.Brush,kotlin.Function0,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Path,androidx.ink.brush.TextureBitmapStore,kotlin.Function1)) composable to handle realtime stylus or touch input. This module is responsible for capturing pointer events and rendering wet ink strokes with the lowest possible latency.
- [**Strokes**](https://developer.android.com/reference/kotlin/androidx/ink/strokes/package-summary)**module:** Represents the ink input and its visual representation. a user finishes drawing a line, the [onStrokesFinished](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:ink/ink-authoring/src/androidMain/kotlin/androidx/ink/authoring/InProgressStrokesFinishedListener.kt;l=54;bpv=0;bpt=1) callback provides a finalized/dry [Stroke](https://developer.android.com/reference/kotlin/androidx/ink/strokes/Stroke) object to the app. This immutable object, representing the completed ink stroke, is then managed in [DrawingCanvasViewModel](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/viewmodels/DrawingCanvasViewModel.kt).
- **Rendering module:** Efficiently displays ink strokes, allowing them to be combined with Jetpack [Compose](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/package-summary) or [Android views](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/view/package-summary).
  - To display both existing and newly dried strokes, Cahier uses [CanvasStrokeRenderer](https://developer.android.com/reference/kotlin/androidx/ink/rendering/android/canvas/CanvasStrokeRenderer) in [DrawingSurface](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/DrawingSurface.kt) for active drawing and in [DrawingDetailPanePreview](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/DrawingDetailPanePreview.kt) for showing a static preview of the note. This module efficiently draws the [Stroke](https://developer.android.com/reference/kotlin/androidx/ink/strokes/Stroke) objects onto a [Canvas](https://developer.android.com/reference/android/graphics/Canvas).
- **Brush modules (** [**Compose**](https://developer.android.com/reference/kotlin/androidx/ink/brush/compose/package-summary)**-** [**views**](https://developer.android.com/reference/kotlin/androidx/ink/brush/package-summary)**):** Provide a declarative way to define the visual style of strokes. Recent updates (since the alpha03 release) include a new *dashed line brush*, particularly useful for features like lasso selection. [DrawingCanvasViewModel](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/viewmodels/DrawingCanvasViewModel.kt) holds the state for the currentBrush. A toolbox in [DrawingCanvas](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/DrawingCanvas.kt) allows users to select different brush families (like [StockBrushes.pressurePen()](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:ink/ink-brush/src/jvmAndroidMain/kotlin/androidx/ink/brush/StockBrushes.kt;l=182;bpv=0;bpt=0#:~:text=public%20fun%20pressurePen,%7D) or [StockBrushes.highlighter()](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:ink/ink-brush/src/jvmAndroidMain/kotlin/androidx/ink/brush/StockBrushes.kt;l=182;bpv=0;bpt=0#:~:text=%40JvmOverloads-,public%20fun%20highlighter(,%7D,-private%20val%20dashedLineV1)) and change colors. The [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) updates the [Brush](https://developer.android.com/reference/kotlin/androidx/ink/brush/Brush) object, which is then used by the [InProgressStrokes](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary#InProgressStrokes(androidx.ink.brush.Brush,kotlin.Function0,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Path,androidx.ink.brush.TextureBitmapStore,kotlin.Function1)) composable for new strokes.
- **Geometry modules (** [**Compose**](https://developer.android.com/reference/kotlin/androidx/ink/geometry/compose/package-summary)**-** [**views**](https://developer.android.com/reference/kotlin/androidx/ink/geometry/package-summary)**):** Support manipulating and analyzing strokes for features like erasing and selecting.
  - The eraser tool within the toolbox and functionality in [DrawingCanvasViewModel](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/viewmodels/DrawingCanvasViewModel.kt) rely on the geometry module. When the eraser is active, it creates a [MutableParallelogram](https://developer.android.com/reference/androidx/ink/geometry/MutableParallelogram) around the path of the user's gesture. The eraser then checks for intersections between the shape and bounding boxes of existing strokes to determine which strokes to erase, making the eraser feel intuitive and precise.
- [**Storage**](https://developer.android.com/reference/kotlin/androidx/ink/storage/package-summary)**module:** Provides efficient serialization and deserialization capabilities for ink data, leading to significant disk and network size savings. To save drawings, Cahier persists the [Stroke](https://developer.android.com/reference/kotlin/androidx/ink/strokes/Stroke) objects in its Room database. In [Converters](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/data/Converters.kt), the sample uses the storage module's [encode](https://developer.android.com/reference/kotlin/androidx/ink/storage/package-summary#(androidx.ink.brush.BrushFamily).encode(java.io.OutputStream)) function to serialize the [StrokeInputBatch](https://developer.android.com/reference/kotlin/androidx/ink/strokes/StrokeInputBatch) (the raw point data) into a [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/#). The byte array, along with brush properties, is saved as a JSON string. The [decode](https://developer.android.com/reference/kotlin/androidx/ink/storage/package-summary#(androidx.ink.strokes.StrokeInputBatch.Companion).decode(java.io.InputStream)) function is used to reconstruct the strokes when a note is loaded.

![orion.png](https://developer.android.com/static/blog/assets/orion_df400b782b_Z10OIzg.webp)

Beyond these core modules, recent updates have expanded the Ink API's capabilities:

- New experimental APIs for custom `BrushFamily` objects empower developers to create creative and unique brush types, providing the possibilities for tools like **Pencil** and **Laser Pointer** brushes.

Cahier leverages custom brushes, including the unique music brush showcased below, to illustrate advanced creative possibilities.
![Rainbow laser created with Ink API's custom brushes..gif](https://developer.android.com/static/blog/assets/Rainbow_laser_created_with_Ink_API_s_custom_brushes_1242177640_1NFmpG.webp)

*Rainbow laser created with Ink API's custom brushes*
![notes.png](https://developer.android.com/static/blog/assets/notes_d782283635_Z1FtRzW.webp)

*Music brush created with Ink API's custom brushes*

- Native Jetpack Compose interoperability modules streamline the integration of inking functionalities directly within your Compose UIs for a more idiomatic and efficient development experience.

Ink API offers several advantages that make it the ideal choice for productivity and creativity apps over a custom implementation:

- **Ease of use:** Ink API abstracts away the complexities of graphics and geometry, allowing you to focus on Cahier's core features.
- **Performance:** Built-in low latency support and optimized rendering ensure a smooth and responsive inking experience.
- **Flexibility:** The modular design allows you to pick and choose the components needed, which enables seamless integration of the Ink API into Cahier's architecture.

Ink API has already been adopted across many Google apps, including for markup in Docs and for Circle to Search as well as partner apps like [Orion Notes](https://play.google.com/store/apps/details?id=com.orion.notes.us), and [PDF Scanner](https://play.google.com/store/apps/details?id=com.rvappstudios.pdf.editor.scanner.maker.reader.merge.converter).

*"Ink API was our first choice for Circle-to-Search (CtS). Utilizing their extensive documentation, integrating the Ink API was a breeze, allowing us to reach our first working prototype w/in just one week. Ink's custom brush texture and animation support allowed us to quickly iterate on the stroke design." *- Jordan Komoda, Software Engineer - Google

### Becoming the default notes app with notes role

Note-taking is a core capability that enhances user productivity on large screen devices. With the [notes role feature](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/create-a-note-taking-app#notes_role), users can access your compatible apps from the lock screen or while other apps are running. This feature identifies and sets system wide default note-taking apps and grants them permission to be launched for capturing content.

#### Implementation in Cahier

Implementing the notes role involves a few key steps, all demonstrated in the sample:

1. **Manifest declaration** : First, the app must declare its capability to handle note-taking intents. In [AndroidManifest.xml](https://github.com/android/cahier/blob/main/app/src/main/AndroidManifest.xml), Cahier includes an `<intent-filter>` for the [android.intent.action.CREATE_NOTE](https://developer.android.com/reference/android/content/Intent#ACTION_CREATE_NOTE) action. This signals to the system that the app is a potential candidate for the notes role.
2. **Checking role status** : [SettingsViewModel](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/viewmodels/SettingsViewModel.kt) uses Android's [RoleManager](https://developer.android.com/reference/kotlin/android/app/role/RoleManager) to determine the current status. SettingsViewModel checks whether the notes role is available on the device ([isRoleAvailable](https://developer.android.com/reference/kotlin/android/app/role/RoleManager#isroleavailable)) and whether Cahier currently holds that role ([isRoleHeld](https://developer.android.com/reference/kotlin/android/app/role/RoleManager#isroleheld)). This state is exposed to the UI using Kotlin flows.
3. **Requesting the role** : In the [Settings.kt](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/Settings.kt) file, a [Button](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) is displayed to the user if the role is available but not held. When clicked, the button calls the `requestNotesRole` function in the ViewModel. The function creates an intent to open the default app settings screen where the user can select Cahier. The process is managed using the [rememberLauncherForActivityResult](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#rememberLauncherForActivityResult(androidx.activity.result.contract.ActivityResultContract,kotlin.Function1)) API, which handles launching the intent and receiving the result.
4. **Updating the UI** : After the user returns from the settings screen, the [ActivityResultLauncher](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultLauncher) callback triggers a function in the ViewModel to update the role status, ensuring the UI accurately reflects whether the app is now the default.

Learn how to integrate the notes role in your app in our [create a note-taking app guide](https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/create-a-note-taking-app).
![helloworld.png](https://developer.android.com/static/blog/assets/helloworld_757f054326_k0u1v.webp)

*Cahier launched in a floating window as the default note-taking app on a Lenovo tablet*

#### A major step forward: Lenovo enables notes role

We're thrilled to announce a major step forward for large screen Android productivity: **Lenovo has enabled support for Notes Role on tablets running Android 15 and higher!** With this update, you can now update your note-taking apps to allow users with compatible Lenovo devices to set them as default, granting seamless access from the lock screen and unlocking system level content capture features.

This commitment from a leading OEM demonstrates the growing importance of the notes role in delivering a truly integrated and productive user experience on Android.

### Multi-instance, multi-windowing, and desktop windowing

Productivity on a large screen is all about managing information and workflows efficiently. That's why Cahier is built to fully embrace Android's advanced windowing capabilities, providing a flexible workspace that adapts to user needs. The app supports:

- **Multi-windowing**: The fundamental ability to run alongside another app in split-screen or free-form mode. This is essential for tasks like referencing a web page while taking notes in Cahier.
- **Multi-instance** : This is where true multitasking shines. Cahier allows users to open *multiple, independent windows of the app simultaneously*. Imagine comparing two different notes side by side or referencing a text note in one window while working on a drawing in another. Cahier demonstrates how to manage these separate instances, each with its own state, turning your app into a powerful, multifaceted tool.
- **Desktop windowing**: When connected to an external display, Android desktop mode transforms a tablet or foldable into a workstation. Because Cahier is built with an adaptive UI and supports multi-instance, the app performs beautifully in this environment. Users can open, resize, and position multiple Cahier windows just like on a traditional desktop, enabling complex workflows that were previously out of reach on mobile devices.

![cahier-desktop-windowing.webp](https://developer.android.com/static/blog/assets/cahier_desktop_windowing_c7fb0bcc05_1rmEal.webp)

*Cahier running in desktop window mode on Pixel Tablet*

Here's how we implemented these features in Cahier:

To enable multi-instance, we first needed to signal to the system that the app supports being launched multiple times by adding the `PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI` property to `MainActivity`'s declaration in `AndroidManifest`:

```
<activity

    android:name="com.example.cahier.MainActivity"

    android:exported="true"

    android:label="@string/app_name"

    android:theme="@style/Theme.MyApplication"

    android:showWhenLocked="true"

    android:turnScreenOn="true"

    android:resizeableActivity="true"

    android:launchMode="singleInstancePerTask">


    <property

        android:name="android.window.PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI"

        android:value="true"/>

    ...

</activity>
```

Next, we implemented the logic to launch a new instance of the app. In [CahierHomeScreen.kt](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/CahierHomeScreen.kt), when a user opts to open a note in a new window, we create a new Intent with specific flags that instruct the system on how to handle the new activity launch. The combination of `FLAG_ACTIVITY_NEW_TASK`, `FLAG_ACTIVITY_MULTIPLE_TASK`, and `FLAG_ACTIVITY_LAUNCH_ADJACENT` ensures the note opens in a new, separate window alongside the existing one.

```
fun openNewWindow(activity: Activity?, note: Note) {

    val intent = Intent(activity, MainActivity::class.java)

    intent.putExtra(AppArgs.NOTE_TYPE_KEY, note.type)

    intent.putExtra(AppArgs.NOTE_ID_KEY, note.id)

    intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_MULTIPLE_TASK or

        Intent.FLAG_ACTIVITY_LAUNCH_ADJACENT


    activity?.startActivity(intent)

}
```

To support multi-window mode, we needed to signal to the system that the app supports resizability by setting the Manifest's `<activity>` or `<application>` element.

```
<activity

    android:name="com.example.cahier.MainActivity"

    android:resizeableActivity="true"

    ...>

</activity>
```

The UI itself being built with the Material 3 adaptive library enables it to adapt seamlessly in multi-window scenarios like Android's split screen mode.

To enhance user experience, we added support for drag and drop. See below how we implemented this in Cahier.

### Drag and drop

A truly productive or creative app doesn't function in isolation; it interacts seamlessly with the rest of the device's ecosystem. Drag and drop is a cornerstone of this interaction, especially on large screens where users are often working across multiple app windows. Cahier fully embraces this by implementing intuitive drag and drop functionality for both adding and sharing content.

- **Effortless Importing** : Users can drag images from other applications---like a web browser, photo gallery, or file manager---and drop them directly onto a note canvas. For this, Cahier uses the [dragAndDropTarget](https://developer.android.com/reference/kotlin/androidx/compose/foundation/draganddrop/package-summary#(androidx.compose.ui.Modifier).dragAndDropTarget(kotlin.Function1,androidx.compose.ui.draganddrop.DragAndDropTarget)) modifier to define a drop zone, check for compatible content (like `image/*`), and process the incoming URI.
- **Simple sharing**: Content inside Cahier is just as easy to share as content from other apps. Users can long-press an image within a text note, or long-press the entire canvas of a drawing note and image composite, and drag it out to another application.

#### Technical deep dive: Dragging from the drawing canvas

Implementing the drag gesture on the drawing canvas presents a unique challenge. In our [DrawingSurface](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/DrawingSurface.kt), the composables that handle live drawing input (the Ink API's [InProgressStrokes](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary#InProgressStrokes(androidx.ink.brush.Brush,kotlin.Function0,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Path,androidx.ink.brush.TextureBitmapStore,kotlin.Function1))) and the `Box` that detects the long-press gesture to initiate a drag are *sibling composables*.

By default, the Jetpack Compose pointer input system is designed so that just one sibling composable ---the first one in declaration order that overlaps the touch location---receives the event. In Cahier's case, we want our drag-and-drop input handling logic to have a chance to run and potentially consume inputs before the [InProgressStrokes](https://developer.android.com/reference/kotlin/androidx/ink/authoring/compose/package-summary#InProgressStrokes(androidx.ink.brush.Brush,kotlin.Function0,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Matrix,androidx.compose.ui.graphics.Path,androidx.ink.brush.TextureBitmapStore,kotlin.Function1)) composable uses all unconsumed input for drawing and then consumes that input. If we don't arrange things in the right order, our Box won't detect the long-press gesture to start a drag, or `InProgressStrokes` won't receive the input to draw.

To solve this, we created a custom `pointerInputWithSiblingFallthrough` modifier, and we put our `Box` using that modifier before `InProgressStrokes` in the composable code. This utility is a thin wrapper around the standard [pointerInput](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary#(androidx.compose.ui.Modifier).pointerInput(kotlin.Array,androidx.compose.ui.input.pointer.PointerInputEventHandler) system but with one critical change: it overrides the [sharePointerInputWithSiblings()](https://developer.android.com/reference/kotlin/androidx/compose/ui/node/PointerInputModifierNode#sharePointerInputWithSiblings()) function to return `true`. This tells the Compose framework to allow pointer events to pass through to sibling composables, even after being consumed.

```
internal fun Modifier.pointerInputWithSiblingFallthrough(

    pointerInputEventHandler: PointerInputEventHandler

) = this then PointerInputSiblingFallthroughElement(pointerInputEventHandler)


private class PointerInputSiblingFallthroughModifierNode(

    pointerInputEventHandler: PointerInputEventHandler

) : PointerInputModifierNode, DelegatingNode() {


    var pointerInputEventHandler: PointerInputEventHandler

        get() = delegateNode.pointerInputEventHandler

        set(value) {

            delegateNode.pointerInputEventHandler = value

        }


    val delegateNode = delegate(

        SuspendingPointerInputModifierNode(pointerInputEventHandler)

    )


    override fun onPointerEvent(

        pointerEvent: PointerEvent,

        pass: PointerEventPass,

        bounds: IntSize

    ) {

        delegateNode.onPointerEvent(pointerEvent, pass, bounds)

    }


    override fun onCancelPointerInput() {

        delegateNode.onCancelPointerInput()

    }


    override fun sharePointerInputWithSiblings() = true

}


private data class PointerInputSiblingFallthroughElement(

    val pointerInputEventHandler: PointerInputEventHandler

) : ModifierNodeElement<PointerInputSiblingFallthroughModifierNode>() {


    override fun create() = PointerInputSiblingFallthroughModifierNode(pointerInputEventHandler)


    override fun update(node: PointerInputSiblingFallthroughModifierNode) {

        node.pointerInputEventHandler = pointerInputEventHandler

    }


    override fun InspectorInfo.inspectableProperties() {

        name = "pointerInputWithSiblingFallthrough"

        properties["pointerInputEventHandler"] = pointerInputEventHandler

    }

}
```

Here's how it's used in [`DrawingSurface`](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/ui/DrawingSurface.kt):

```
Box(

    modifier = Modifier

        .fillMaxSize()

        // Our custom modifier enables this gesture to coexist with the drawing input.

        .pointerInputWithSiblingFallthrough {

            detectDragGesturesAfterLongPress(

                onDragStart = { onStartDrag() },

                onDrag = { _, _ -> /* consume drag events */ },

                onDragEnd = { /* No action needed */ }

            )

        }

) 

// The Ink API's composable for live drawing sits here as a sibling.

InProgressStrokes(...)
```

With this in place, the system correctly detects both the drawing strokes and the long-press drag gesture simultaneously. Once the drag is initiated, we create a shareable `content://` URI with [FileProvider](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/utils/FileHelper.kt) and pass the URI to the system's drag and drop framework using [view.startDragAndDrop()](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:core/core/src/main/java/androidx/core/view/ViewCompat.java;l=4347;bpv=1;bpt=1?q=public+final+boolean+startDragAndDrop&ss=androidx/platform/frameworks/support). This solution ensures a robust and intuitive user experience, showcasing how to overcome complex gesture conflicts in layered UIs.

## Built with modern architecture

Beyond specific APIs, Cahier demonstrates crucial architectural patterns for building high-quality, adaptive applications.

### The presentation layer: Jetpack Compose and adaptability

The presentation layer is built entirely with Jetpack Compose. As mentioned, Cahier adopts the [material3-adaptive library](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) for UI adaptability. State management follows a strict Unidirectional Data Flow (UDF) pattern, with ViewModel instances used as data containers that hold note information and UI state.

### The data layer: Repositories and Room

For the data layer, Cahier uses a [NoteRepository](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/data/NotesRepository.kt) interface to abstract all data operations. This design choice cleanly allows the app to swap between a local data source (Room) and a potential future remote backend. The data flow for an action like editing a note is straightforward:

1. The Jetpack Compose UI triggers a method in the ViewModel.
2. The ViewModel fetches the note from [NoteRepository](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/data/NotesRepository.kt), handles the logic, and passes the updated note back to the repository.
3. [NoteRepository](https://github.com/android/cahier/blob/main/app/src/main/java/com/example/cahier/data/NotesRepository.kt) saves the update to a Room database.

### Comprehensive input support

To be a true productivity powerhouse, an app must handle a variety of input methods flawlessly. Cahier is built to be compliant with [large screen input guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) and supports:

- **Stylus:** Integration with the Ink API, palm rejection, registration for the notes role, stylus input in text fields, and immersive mode.
- **Keyboard:** Support for most common keyboard shortcuts and combinations (like ctrl+click, meta+click) and clear indication for keyboard focus.
- **Mouse and trackpad:** Support for right-click and hover states.

Support for advanced keyboard, mouse, and trackpad interactions is a key focus for further improvements.

## Get started today

We hope [Cahier](https://github.com/android/cahier) serves as a launchpad for your next great app. We built it to be a comprehensive, open source resource that demonstrates how to combine an adaptive UI, powerful APIs like Ink and notes role, and a modern, adaptive architecture.

Ready to dive in?

- **Explore the code** : Head over to our [GitHub repository](https://github.com/android/cahier) to explore the Cahier codebase and see the design principles in action.
- **Build your own**: Use Cahier as a foundation for your own note-taking, document markup, or creative application.
- **Contribute**: We welcome your contributions! Help us make Cahier an even better resource for the Android developer community.

Check out the [official developer guides](https://developer.android.com/develop/ui/compose/touch-input/stylus-input) and start building your next generation productivity and creativity app today. We can't wait to see what you create!

###### Written by:

-

  ## [Chris Assigbe](https://developer.android.com/blog/authors/chris-assigbe)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/chris-assigbe) ![](https://developer.android.com/static/blog/assets/Chris_Assigbe_2_a72a1e1687_sAjN.webp) ![](https://developer.android.com/static/blog/assets/Chris_Assigbe_2_a72a1e1687_sAjN.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](https://developer.android.com/blog/authors/ivy-knight) 02 Dec 2025 02 Dec 2025 ![](https://developer.android.com/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow_forward](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app) We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 20 Nov 2025 20 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow_forward](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey) The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  9 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)