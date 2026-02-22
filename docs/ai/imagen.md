---
title: https://developer.android.com/ai/imagen
url: https://developer.android.com/ai/imagen
source: md.txt
---

Imagen is an image generation model. It can be used to generate
custom avatars for user profiles or to integrate personalized visual assets into
existing screen flows to increase user engagement.

You can access [Imagen models](https://firebase.google.com/docs/vertex-ai/models) from your Android app using the
[Firebase AI Logic SDK.](https://firebase.google.com/docs/vertex-ai/generate-images-imagen?platform=android) Imagen models are available using both
Firebase AI Logic [API providers](https://developer.android.com/ai/gemini#api-providers): Gemini Developer API (recommended for most
developers) and Vertex AI.
![A diagram illustrating a Firebase AI Logic integration architecture
to access the Gemini Developer API. An Android App utilizes the Firebase
Android SDK to connect to Firebase. Firebase then interacts with the
Gemini Developer API, which accesses Gemini Pro & Flash within the
cloud.](https://developer.android.com/static/ai/assets/images/firebase-ai-logic-imagen.svg) **Figure 1.** Access Imagen models using Firebase AI Logic.

> [!NOTE]
> **Note:** Firebase AI Logic doesn't yet support all the features available for the server-side integrations of Imagen models. Learn more about the supported capabilities in the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/generate-images-imagen?platform=android#capabilities-features).

> [!NOTE]
> **Note:** To build with Gemini 2.5 Flash Nano Banana, read the [Generate images on Android with Nano Banana](https://developer.android.com/ai/gemini/developer-api#generate-images) section of the Gemini Developer API documentation.

## Experiment with prompts

Creating the ideal prompts often takes multiple attempts. You can experiment
with image prompts in [Google AI Studio](https://aistudio.google.com/gen-media), an IDE for prompt
design and prototyping. For tips on how to improve your prompts, review the
[prompt and image attribute guide](https://cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide).
![A screenshot of the Google AI Studio interface,
displaying four generated images of a T-Rex with a blue backpack in a
prehistoric forest.](https://developer.android.com/static/ai/assets/images/t-rex-imagen.png) **Figure 2.** Google AI Studio can help you refine your image generation prompts.

## Set up a Firebase project and connect your app

Follow the steps in the Firebase documentation to
[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

## Add the Gradle dependency

Add the following dependencies to your `build.gradle` file:

    dependencies {
      // Import the BoM for the Firebase platform
      implementation(platform("com.google.firebase:firebase-bom:34.9.0"))

      // Add the dependency for the Firebase AI Logic library. When using the BoM,
      // you don't specify versions in Firebase library dependencies
      implementation("com.google.firebase:firebase-ai")
    }

## Generate an image

To generate an image in your Android app, start by instantiating an
`ImagenModel` with an optional configuration.

You can use the [`generationConfig`](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=android) parameter to define a negative prompt,
the number of images, the output image aspect ratio, the image format and add a
watermark. You can use the [`safetySettings`](https://firebase.google.com/docs/vertex-ai/safety-settings?platform=android) parameter to configure the
safety and person filters.

> [!NOTE]
> **Note:** Refer to the Firebase documentation for up-to-date information about [available Imagen models](https://firebase.google.com/docs/vertex-ai/models).


### Kotlin

```kotlin
val config = ImagenGenerationConfig(
    numberOfImages = 2,
    aspectRatio = ImagenAspectRatio.LANDSCAPE_16x9,
    imageFormat = ImagenImageFormat.jpeg(compressionQuality = 100),
    addWatermark = false,
)

// Initialize the Gemini Developer API backend service
// For Vertex AI use Firebase.ai(backend = GenerativeBackend.vertexAI())
val model = Firebase.ai(backend = GenerativeBackend.googleAI()).imagenModel(
    modelName = "imagen-4.0-generate-001",
    generationConfig = config,
    safetySettings = ImagenSafetySettings(
        safetyFilterLevel = ImagenSafetyFilterLevel.BLOCK_LOW_AND_ABOVE,
        personFilterLevel = ImagenPersonFilterLevel.BLOCK_ALL
    ),
)
```

### Java

```java
ImagenGenerationConfig config = new ImagenGenerationConfig.Builder()
        .setNumberOfImages(2)
        .setAspectRatio(ImagenAspectRatio.LANDSCAPE_16x9)
        .setImageFormat(ImagenImageFormat.jpeg(100))
        .setAddWatermark(false)
        .build();

// For Vertex AI use Firebase.ai(backend = GenerativeBackend.vertexAI())
ImagenModelFutures model = ImagenModelFutures.from(
        FirebaseAI.getInstance(GenerativeBackend.googleAI()).imagenModel(
                "imagen-4.0-generate-001",
                config,
                new ImagenSafetySettings(
                        ImagenSafetyFilterLevel.BLOCK_LOW_AND_ABOVE,
                        ImagenPersonFilterLevel.BLOCK_ALL))
);
```

<br />

Once your `ImagenModel` is instantiated, you can generate images by calling
`generateImages`:


### Kotlin

```kotlin
val imageResponse = model.generateImages(
    prompt = "A hyper realistic picture of a t-rex with a blue bagpack in a prehistoric forest",
)
val image = imageResponse.images.first()
val bitmapImage = image.asBitmap()
```

### Java

```java
ListenableFuture<ImagenGenerationResponse<ImagenInlineImage>> futureResponse =
        model.generateImages(
                "A hyper realistic picture of a t-rex with a blue bagpack in a prehistoric forest");

try {
    ImagenGenerationResponse<ImagenInlineImage> imageResponse = futureResponse.get();
    List<ImagenInlineImage> images = null;
    if (imageResponse != null) {
        images = imageResponse.getImages();
    }
    if (images != null && !images.isEmpty()) {
        ImagenInlineImage image = images.get(0);
        Bitmap bitmapImage = image.asBitmap();
        // Use bitmapImage
    }
} catch (ExecutionException | InterruptedException e) {
    e.printStackTrace();
}
```

<br />

## Edit images with Imagen

The Firebase AI Logic SDKs offer advanced image editing capabilities through the
Imagen model, allowing you to:

- [**Edit images based on masks**](https://developer.android.com/ai/imagen#mask-based-editing), which includes actions such as inserting or removing objects, extending image content beyond its original boundaries, and changing backgrounds.
- [**Customize images**](https://developer.android.com/ai/imagen#customization) through the application of specific styles (patterns, textures, or artist styles), by focusing on various subjects (such as products, people, or animals), or by adhering to different controls (such as hand-drawn sketch, a canny edge image, or a face mesh).

> [!NOTE]
> **Note:** The use of Imagen for image generation using a text prompt is generally available, but the Imagen editing features are in **developer preview**. Imagen editing features are exclusively available through Vertex AI.

### Model initialization

To use the Imagen editing features, specify an Imagen model that supports image
editing, such as `imagen-3.0-capability-001`:


```kotlin
val imagenModel = Firebase.ai(backend = GenerativeBackend.vertexAI())
    .imagenModel("imagen-3.0-capability-001")
```

<br />

### Mask-based editing

Imagen's mask-based editing allows for modifications to images by defining
specific areas for the model to manipulate. This capability enables a range of
actions, including creating and applying masks, inserting or removing objects,
and expanding image content beyond the original boundaries.

#### Create a mask

To perform mask-based editing such as inserting or removing objects you need to
define the area that needs to be edited by the model, the *mask*.

To create a mask, you can have the model auto-generate it by using
`ImagenBackgroundMask()` or `ImagenSemanticMask()`, passing a [class
ID](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-customization#segment-ids).

You can also manually draw the mask on screen, by generating a mask bitmap and
converting it into a `ImagenRawMask`. Using `detectDragGestures` and `Canvas`,
you can implement a mask-drawing user interface with Jetpack Compose in your app
as follows:


```kotlin
//import androidx.compose.ui.graphics.Color as ComposeColor

@Composable
fun ImagenEditingMaskEditor(
    sourceBitmap: Bitmap,
    onMaskFinalized: (Bitmap) -> Unit,
) {

    val paths = remember { mutableStateListOf<Path>() }
    var currentPath by remember { mutableStateOf<Path?>(null) }
    var scale by remember { mutableFloatStateOf(1f) }
    var offsetX by remember { mutableFloatStateOf(0f) }
    var offsetY by remember { mutableFloatStateOf(0f) }

    Column(
        modifier = Modifier.fillMaxSize(),
    ) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .pointerInput(Unit) {
                    detectDragGestures(
                        onDragStart = { startOffset ->
                            val transformedStart = Offset(
                                (startOffset.x - offsetX) / scale,
                                (startOffset.y - offsetY) / scale,
                            )
                            currentPath = Path().apply { moveTo(transformedStart.x, transformedStart.y) }
                        },
                        onDrag = { change, _ ->
                            currentPath?.let {
                                val transformedChange = Offset(
                                    (change.position.x - offsetX) / scale,
                                    (change.position.y - offsetY) / scale,
                                )
                                it.lineTo(transformedChange.x, transformedChange.y)
                                currentPath = Path().apply { addPath(it) }
                            }
                            change.consume()
                        },
                        onDragEnd = {
                            currentPath?.let { paths.add(it) }
                            currentPath = null
                        },
                    )
                },
        ) {
            Image(
                bitmap = sourceBitmap.asImageBitmap(),
                contentDescription = null,
                modifier = Modifier.fillMaxSize(),
                contentScale = ContentScale.Fit,
            )
            Canvas(modifier = Modifier.fillMaxSize()) {
                val canvasWidth = size.width
                val canvasHeight = size.height
                val bitmapWidth = sourceBitmap.width.toFloat()
                val bitmapHeight = sourceBitmap.height.toFloat()
                scale = min(canvasWidth / bitmapWidth, canvasHeight / bitmapHeight)
                offsetX = (canvasWidth - bitmapWidth * scale) / 2
                offsetY = (canvasHeight - bitmapHeight * scale) / 2
                withTransform(
                    {
                        translate(left = offsetX, top = offsetY)
                        scale(scale, scale, pivot = Offset.Zero)
                    },
                ) {
                    val strokeWidth = 70f / scale
                    val stroke = Stroke(width = strokeWidth, cap = StrokeCap.Round, join = StrokeJoin.Round)
                    val pathColor = ComposeColor.White.copy(alpha = 0.5f)
                    paths.forEach { path ->
                        drawPath(path = path, color = pathColor, style = stroke)
                    }
                    currentPath?.let { path ->
                        drawPath(path = path, color = pathColor, style = stroke)
                    }
                }
            }
        }
        Button(
            onClick = {
                val maskBitmap = createMaskBitmap(sourceBitmap, paths)
                onMaskFinalized(maskBitmap)
            },
        ) {
            Text("Save mask")
        }
    }
}
```

<br />

You can then create the mask bitmap by drawing the paths on the canvas:


```kotlin
// import android.graphics.Color as AndroidColor
// import android.graphics.Paint

private fun createMaskBitmap(
    sourceBitmap: Bitmap,
    paths: SnapshotStateList<Path>,
): Bitmap {
    val maskBitmap = Bitmap.createBitmap(sourceBitmap.width, sourceBitmap.height, Bitmap.Config.ARGB_8888)
    val canvas = android.graphics.Canvas(maskBitmap)
    val paint = Paint().apply {
        color = AndroidColor.RED
        strokeWidth = 70f
        style = Paint.Style.STROKE
        strokeCap = Paint.Cap.ROUND
        strokeJoin = Paint.Join.ROUND
        isAntiAlias = true
    }
    paths.forEach { path -> canvas.drawPath(path.asAndroidPath(), paint) }

    return maskBitmap
}
```

<br />

Make sure the mask is the same size as the source image. See the [Imagen AI
Catalog Samples](https://github.com/android/ai-samples/tree/main/samples/imagen-editing) for more details.

> [!NOTE]
> **Note:** When performing mask-based edits, we recommend dilating the mask by 1-2% to create smoother, more convincing borders. This can be achieved by adjusting the `strokeWidth` property of the `paint` object.

#### Insert objects

You can insert a new object or content into an existing image, also called
*inpainting*. The model will generate and insert the new content into the
specified masked area.

To achieve this, use the `editImage()` function. You'll need to provide the
original image, a [mask](https://developer.android.com/ai/imagen?tab=t.gaj0xg8c26y0#heading=h.u6pnz49k9z58), and a text prompt
describing the content you want to insert. Additionally, pass an
`ImagenEditingConfig` object, ensuring its `editMode` property is set to
`ImagenEditMode.INPAINT_INSERTION`.


```kotlin
suspend fun insertFlowersIntoImage(
    model: ImagenModel,
    originalImage: Bitmap,
    mask: ImagenMaskReference
): ImagenGenerationResponse<ImagenInlineImage> {
    val prompt = "a vase of flowers"

    // Pass the original image, a mask, the prompt, and an editing configuration.
    val editedImage = model.editImage(
        referenceImages = listOf(
            ImagenRawImage(originalImage.toImagenInlineImage()),
            mask,
        ),
        prompt = prompt,
        // Define the editing configuration for inpainting and insertion.
        config = ImagenEditingConfig(ImagenEditMode.INPAINT_INSERTION)
    )
    return editedImage
}
```

<br />

#### Remove objects

Inpainting lets you remove unwanted objects from an image. To do this, use
the `editImage` function. You'll need to provide the original image and a
[mask](https://developer.android.com/ai/imagen?tab=t.gaj0xg8c26y0#heading=h.u6pnz49k9z58) that highlights the object you want to
remove. Optionally, you can include a text prompt to describe the object, which
can assist the model in accurate identification. Additionally, you must set the
`editMode` within the `ImagenEditingConfig` to `ImagenEditMode.INPAINT_REMOVAL`.


```kotlin
suspend fun removeBallFromImage(
    model: ImagenModel,
    originalImage: Bitmap,
    mask: ImagenMaskReference
): ImagenGenerationResponse<ImagenInlineImage> {

    // Optional: provide the prompt describing the content to be removed.
    val prompt = "a ball"

    // Pass the original image, a mask, the prompt, and an editing configuration.
    val editedImage = model.editImage(
        referenceImages = listOf(
            ImagenRawImage(originalImage.toImagenInlineImage()),
            mask
        ),
        prompt = prompt,
        // Define the editing configuration for inpainting and removal.
        config = ImagenEditingConfig(ImagenEditMode.INPAINT_REMOVAL)
    )

    return editedImage
}
```

<br />

#### Expand image content

You can expand an image beyond its original boundaries, known as *outpainting* ,
by using the `outpaintImage()` function. This function requires the original
image and the necessary [`Dimensions`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Dimensions) of the expanded image.
Optionally, you can include a descriptive prompt for the expansion and specify
the [`ImagenImagePlacement`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenImagePlacement) of the original image within the
new generated image:


```kotlin
suspend fun expandImage(originalImage: Bitmap, imagenModel: ImagenModel): ImagenGenerationResponse<ImagenInlineImage> {

    // Optionally describe what should appear in the expanded area.
    val prompt = "a sprawling sandy beach next to the ocean"

    val editedImage = imagenModel.outpaintImage(
        originalImage.toImagenInlineImage(),
        Dimensions(1024, 1024),
        prompt = prompt,
        newPosition = ImagenImagePlacement.LEFT_CENTER
    )


    return editedImage
}
```

<br />

#### Replace the background

You can replace the background of an image while preserving the foreground
subject. To do this, use the `editImage` function. Pass the original image, an
`ImagenBackgroundMask` object (containing a text prompt for the new background),
and an `ImagenEditingConfig` with its `editMode` property set to
`ImagenEditMode.INPAINT_INSERTION`.


```kotlin
suspend fun replaceBackground(model: ImagenModel, originalImage: Bitmap): ImagenGenerationResponse<ImagenInlineImage> {
    // Provide the prompt describing the new background.
    val prompt = "space background"

    // Pass the original image, a mask, the prompt, and an editing configuration.
    val editedImage = model.editImage(
        referenceImages = listOf(
            ImagenRawImage(originalImage.toImagenInlineImage()),
            ImagenBackgroundMask(),
        ),
        prompt = prompt,
        config = ImagenEditingConfig(ImagenEditMode.INPAINT_INSERTION)
    )

    return editedImage
}
```

<br />

### Customization

You can use the **customization capability** from Imagen to generate or edit
images based on reference images that specify a subject, control, or style. This
is accomplished by providing a text prompt along with one or more reference
images to guide the model.

#### Customize based on a subject

You can generate new images of a specific subject from a reference image (for
example, a product, person, or animal). Simply provide a text prompt and at
least one reference image of the subject. For instance, you could upload a
picture of your pet and generate a new image of it in an entirely different
environment.

To do this, define the subject reference using `ImagenSubjectReference` and then
pass it to `editImage` along with your prompt. Additionally, include an
`ImagenEditingConfig` that specifies the number of `editSteps`; a higher
`editSteps` value generally leads to better quality results:


```kotlin
suspend fun customizeCatImage(model: ImagenModel, referenceCatImage: Bitmap): ImagenGenerationResponse<ImagenInlineImage> {

    // Define the subject reference using the reference image.
    val subjectReference = ImagenSubjectReference(
        image = referenceCatImage.toImagenInlineImage(),
        referenceId = 1,
        description = "cat",
        subjectType = ImagenSubjectReferenceType.ANIMAL
    )

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the subject reference with ID 1.
    val prompt = "A cat[1] flying through outer space"

    // Use the editImage API to perform the subject customization.
    val editedImage = model.editImage(
        referenceImages = listOf(subjectReference),
        prompt = prompt,
        config = ImagenEditingConfig(
            editSteps = 50 // Number of editing steps, a higher value can improve quality
        )
    )

    return editedImage
}
```

<br />

#### Customize based on a control

This technique generates a new image based on a **control reference image** ,
such as a hand-drawn sketch ("scribble"), a [Canny edge image](https://en.wikipedia.org/wiki/Canny_edge_detector),
or a face mesh. The model uses the control image as a structural guide for the
new image's layout and composition, while the text prompt provides details like
color and texture.

Define a control reference with `ImagenControlReference` and provide it to
`editImage` along with a prompt and `ImagenEditingConfig` with the number of
`editSteps` (a higher value can improve quality):


```kotlin
suspend fun customizeCatImageByControl(model: ImagenModel, referenceImage: Bitmap): ImagenGenerationResponse<ImagenInlineImage> {

    // Define the subject reference using the reference image.
    val controlReference = ImagenControlReference(
        image = referenceImage.toImagenInlineImage(),
        referenceId = 1,
        type = ImagenControlType.SCRIBBLE,
    )

    val prompt = "A cat flying through outer space arranged like the scribble map[1]"

    val editedImage = model.editImage(
        referenceImages = listOf(controlReference),
        prompt = prompt,
        config = ImagenEditingConfig(
            editSteps = 50
        ),
    )

    return editedImage
}
```

<br />

#### Customize based on a style

You can generate or edit an image to match a specific **style** from a reference
image, like its pattern, texture, or design. The model uses the reference image
to understand the required aesthetic and applies it to the new image described
in the text prompt. For example, you could generate an image of a cat in the
style of a famous painting by providing an image of that painting.

Define a style reference with `ImagenStyleReference` and provide it to
`editImage` along with a prompt and `ImagenEditingConfig` with the number of
`editSteps` (a higher value can improve quality):


```kotlin
suspend fun customizeImageByStyle(model: ImagenModel, referenceVanGoghImage: Bitmap): ImagenGenerationResponse<ImagenInlineImage> {

    // Define the style reference using the reference image.
    val styleReference = ImagenStyleReference(
        image = referenceVanGoghImage.toImagenInlineImage(),
        referenceId = 1,
        description = "Van Gogh style"
    )

    // Provide a prompt that describes the final image.
    // The "1" links the prompt to the style reference with ID 1.
    val prompt = "A cat flying through outer space, in the Van Gogh style[1]"

    // Use the editImage API to perform the style customization.
    val editedImage = model.editImage(
        referenceImages = listOf(styleReference),
        prompt = prompt,
        config = ImagenEditingConfig(
            editSteps = 50 // Number of editing steps, a higher value can improve quality
        ),
    )

    return editedImage
}
```

<br />

## Next steps

- Learn more about Firebase AI Logic in the [Firebase
  documentation](https://firebase.google.com/docs/vertex-ai/).
- Explore the [Android AI Sample Catalog](https://github.com/android/ai-samples).