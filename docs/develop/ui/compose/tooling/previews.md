---
title: https://developer.android.com/develop/ui/compose/tooling/previews
url: https://developer.android.com/develop/ui/compose/tooling/previews
source: md.txt
---

A composable is defined by a function and annotated with `@Composable`:


```kotlin
@Composable
fun SimpleComposable() {
    Text("Hello World")
}
```

<br />

![A simple text element containing the words "Hello
World"](https://developer.android.com/static/develop/ui/compose/images/tooling-hello-world.png)

To enable a preview of this composable, create another composable, annotated
with `@Composable` and `@Preview`. This new, annotated composable now contains
the composable you created initially, `SimpleComposable`:


```kotlin
@Preview
@Composable
fun SimpleComposablePreview() {
    SimpleComposable()
}
```

<br />

The [`@Preview`](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/Preview) annotation tells Android Studio that this
composable should be shown in the design view of this file. You can see live
updates to your composable preview as you make your edits.

> [!NOTE]
> **Note:** Android Wear uses different annotations for previews (`@WearPreviewDevices` and `@WearPreviewFontScales`); for more information see [Test combinations of screen and font sizes using
> previews](https://developer.android.com/training/wearables/compose/screen-size#previews).

![A gif showing real time updates using Compose
Preview](https://developer.android.com/static/develop/ui/compose/images/tooling-preview-live-edit.gif)

You can add parameters manually in your code to customize the way Android Studio
renders `@Preview`. You can even add the `@Preview` annotation to the same
function multiple times to preview a composable with different properties.

> [!NOTE]
> **Note:** If you have multiple composable previews but want to focus on one preview at a time, we recommend using Focus mode to save rendering resources. Switch to Grid or List mode when you need to see all the UI variants at once. You can toggle between modes by using the menu at the top of the **Design** tab.

One of the primary benefits of using `@Preview` composables is to avoid reliance
on the emulator in Android Studio. You can save the memory-heavy startup of the
emulator for more final look-and-feel changes, and `@Preview`'s ability to make
and test small code changes with ease.

To leverage `@Preview` annotation most effectively, make sure to define your
screens in terms of the state it receives as input and the events that it
outputs.

## Define your `@Preview`

Android Studio offers some features to extend composable previews. You can
change their container design, interact with them, or deploy them directly to an
emulator or device.

### Dimensions

By default, `@Preview` dimensions are chosen automatically to wrap its content.
To set the dimensions manually, add `heightDp` and `widthDp` parameters. Those
values are already interpreted as [`dp`](https://developer.android.com/reference/kotlin/androidx/compose/ui/unit/Dp), so you don't need to add `.dp`
to them:


```kotlin
@Preview(widthDp = 50, heightDp = 50)
@Composable
fun SquareComposablePreview() {
    Box(Modifier.background(Color.Yellow)) {
        Text("Hello World")
    }
}
```

<br />

![A yellow square with the words "Hello
World"](https://developer.android.com/static/develop/ui/compose/images/tooling-square-preview.png)

### Dynamic color preview

If you've enabled [dynamic
color](https://m3.material.io/styles/color/dynamic-color/overview) in your app,
use the `wallpaper` attribute to switch wallpapers and see how your UI reacts to
different users' chosen wallpaper. Select from the different wallpaper themes
offered by the
[`Wallpaper`](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/Wallpapers)
class. This feature requires Compose 1.4.0 or higher.

### Use with different devices

In Android Studio Flamingo, you can edit the `device` parameter of the Preview
annotation to define configurations for your composables in different devices.

![Sample Composable
function](https://developer.android.com/static/develop/ui/compose/images/preview-devicespec-sample-function.png)

When the device parameter has an empty string (`@Preview(device = "")`), you can
invoke autocomplete by pressing `Ctrl` + `Space`. Then, you can set the values
of each parameter.

![Editing the sample
function](https://developer.android.com/static/develop/ui/compose/images/preview-devicespec-edit-sample-function.png)

From autocomplete, you can select any device option from the list--for example,
`@Preview(device = "id:pixel_4")`. Alternatively, you can enter a custom device
by choosing `spec:width=px,height=px,dpi=int...` to set the individual values of
each parameter.

![Spec
list](https://developer.android.com/static/develop/ui/compose/images/preview-devicespec-spec-list.png)

To apply, press `Enter`, or cancel with `Esc`.

If you set an invalid value, the declaration is underlined in red and a fix may
be available (`Alt` + `Enter` (⌥ + ⏎ for macOS) \> **Replace with ...**. The
Inspection attempts to provide a fix that is closest to resembling your input.

![Example of invalid
value](https://developer.android.com/static/develop/ui/compose/images/preview-devicespec-gibberish.png)

### Locale

To test different user locales, add the `locale` parameter:


```kotlin
@Preview(locale = "fr-rFR")
@Composable
fun DifferentLocaleComposablePreview() {
    Text(text = stringResource(R.string.greeting))
}
```

<br />

![A simple text element containing the word "Bonjour" with a French
flag](https://developer.android.com/static/develop/ui/compose/images/tooling-locale-preview.png)

### Set background color

By default, your composable is displayed with a transparent background. To add a
background, add the `showBackground` and `backgroundColor` parameters. Keep in
mind that `backgroundColor` is an ARGB [`Long`](https://developer.android.com/reference/android/graphics/Color#color-longs), not a `Color`
value:


```kotlin
@Preview(showBackground = true, backgroundColor = 0xFF00FF00)
@Composable
fun WithGreenBackground() {
    Text("Hello World")
}
```

<br />

![A green rectangle with the words "Hello
World"](https://developer.android.com/static/develop/ui/compose/images/tooling-background-preview.png)

### System UI

If you need to display the status and action bars inside a preview, add the
`showSystemUi` parameter:


```kotlin
@Preview(showSystemUi = true)
@Composable
fun DecoratedComposablePreview() {
    Text("Hello World")
}
```

<br />

![A preview window showing an activity with the status and action bars.](https://developer.android.com/static/develop/ui/compose/images/tooling-decorated-preview.png)

### UI mode

The parameter `uiMode` can take any of the [`Configuration.UI_*`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_NIGHT_MASK)
constants and allows you to change the behavior of the preview accordingly. For
example, you can set the preview to Night Mode to see how the theme reacts.

![Compose preview UI](https://developer.android.com/static/studio/images/profile/compose-preview-ui.png)

### `LocalInspectionMode`

You can read from the [`LocalInspectionMode`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#LocalInspectionMode())
`CompositionLocal` to see if the composable is rendered in a preview (inside an
[inspectable component](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/InspectableValue)). If the composition is rendered
in a preview, `LocalInspectionMode.current` evaluates to `true`. This
information lets you customize your preview; for example, you can show a
placeholder image in the preview window instead of showing real data.

This way, you can also work around the [limitations](https://developer.android.com/develop/ui/compose/tooling/previews#preview-limitations). For
example, showing sample data instead of calling network request.


```kotlin
@Composable
fun GreetingScreen(name: String) {
    if (LocalInspectionMode.current) {
        // Show this text in a preview window:
        Text("Hello preview user!")
    } else {
        // Show this text in the app:
        Text("Hello $name!")
    }
}
```

<br />

## Interact with your `@Preview`

Android Studio provides features that allow you to interact with your defined
previews. This interaction helps you understand your previews' runtime behavior
and allows you to better navigate your UI with previews.

### Interactive mode

The interactive mode lets you interact with a preview similarly to how you would
on a device running your program, like a phone or tablet. The interactive mode
is isolated in a sandbox environment (meaning, isolated from other previews),
where you can click elements and enter user input in the preview. It's a quick
way to test different states, gestures, and even animations of your composable.

![The user clicking the preview's "interactive"
button](https://developer.android.com/static/develop/ui/compose/images/tooling-start-interactive.png)

![A video of the user interacting with a
preview](https://developer.android.com/static/develop/ui/compose/images/tooling-interactive-preview-demo.gif)

### Code navigation and composable outlines

You can hover over a preview to see the outlines of the composables contained
within. Clicking on a composable outline triggers your editor view to navigate
to its definition.

![The user hovering over a preview, causing Studio to display the outlines of
its
composables](https://developer.android.com/static/develop/ui/compose/images/tooling-preview-code-nav.png)

### Run preview

You can run a specific `@Preview` on an emulator or a physical device. The
preview is deployed within the same project app as a new `Activity`, so it
shares the same context and permissions. It does not require you to write
boilerplate code asking for a permission if it has already been granted.

> [!NOTE]
> **Note:** The arguments applied to the `@Preview` annotation (for example, `widthDp`, `locale`, etc.) aren't applied to the preview that is run and deployed.

Click the **Run Preview** icon ![Run Preview
icon](https://developer.android.com/static/studio/images/buttons/deploy-to-device-icon.png)
next to the `@Preview` annotation or at the top of the preview, and Android
Studio deploys that `@Preview` to your connected device or emulator.

![The user clicking the preview's "run preview"
button](https://developer.android.com/static/develop/ui/compose/images/tooling/run_preview.png)

![Video of the user deploying a preview to the
device](https://developer.android.com/static/develop/ui/compose/images/tooling-deploy-preview-demo.gif)

### Copy `@Preview` render

Every rendered preview can be copied as an image by right clicking on it.

![The user clicking on a preview to copy it as an
image.](https://developer.android.com/static/develop/ui/compose/images/tooling-copy-render.png)

## Multiple previews of the same `@Preview` annotation

You can showcase multiple versions of the same `@Preview` composable with
different specifications, or different parameters passed to the composable. This
way, you can reduce the boilerplate code that you would need to write otherwise.

### Multipreview templates

`androidx.compose.ui:ui-tooling-preview` 1.6.0-alpha01+ introduces Multipreview
API templates: `@PreviewScreenSizes`, `@PreviewFontScales`, `@PreviewLightDark`,
and `@PreviewDynamicColors`, so that with one single annotation, you can
preview your Compose UI in common scenarios.

![Previewing different fonts and screen sizes using templates](https://developer.android.com/static/studio/images/design/multipreview-template.png)

### Create custom multipreview annotations

With multipreview, you can define an annotation class that itself has multiple
`@Preview` annotations with different configurations. Adding this annotation to
a composable function automatically renders all of the different previews at
once. For example, you can use this annotation to preview multiple devices, font
sizes, or themes at the same time without repeating those definitions for every
single composable.

Start by creating your own custom annotation class:


```kotlin
@Preview(
    name = "small font",
    group = "font scales",
    fontScale = 0.5f
)
@Preview(
    name = "large font",
    group = "font scales",
    fontScale = 1.5f
)
annotation class FontScalePreviewshttps://github.com/android/snippets/blob/fbed24d5695413cfd86b4b2c6b6faf0a3a2eadb8/compose/snippets/src/main/java/com/example/compose/snippets/tooling/AndroidStudioComposeSnippets.kt#L63-L73
```

<br />

You can use this custom annotation for your preview composables:


```kotlin
@FontScalePreviews
@Composable
fun HelloWorldPreview() {
    Text("Hello World")
}
```

<br />

![Android Studio design tab showing the composable with small and large font](https://developer.android.com/static/develop/ui/compose/images/tooling/preview-multipreview-1.png)

You can combine multiple multipreview annotations and normal preview annotations
to create a more complete set of previews. Combining multipreview annotations
doesn't mean all the different combinations are shown. Instead, each
multipreview annotation acts independently and renders only its own variants.


```kotlin
@Preview(
    name = "Spanish",
    group = "locale",
    locale = "es"
)
@FontScalePreviews
annotation class CombinedPreviews

@CombinedPreviews
@Composable
fun HelloWorldPreview2() {
    MaterialTheme { Surface { Text(stringResource(R.string.hello_world)) } }
}
```

<br />

![Android Studio design tab showing the composable in all configurations](https://developer.android.com/static/develop/ui/compose/images/tooling/preview-multipreview-2.png)

The mix-and-match nature of multipreview-- and normal preview!-- lets you more
comprehensively test many properties of larger scale projects.

### `@Preview` and large data sets

Very often, a need arises where you must pass a large dataset to your composable
preview. To do this, simply pass sample data to a Composable Preview function by
adding a parameter with the [`@PreviewParameter`](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/PreviewParameter)
annotation.


```kotlin
@Preview
@Composable
fun UserProfilePreview(
    @PreviewParameter(UserPreviewParameterProvider::class) user: User
) {
    UserProfile(user)
}
```

<br />

To provide the sample data, create a class that implements
[`PreviewParameterProvider`](https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/PreviewParameterProvider) and returns the
sample data as a sequence.


```kotlin
class UserPreviewParameterProvider : PreviewParameterProvider<User> {
    override val values = sequenceOf(
        User("Elise"),
        User("Frank"),
        User("Julia")
    )
}
```

<br />

This renders one preview per data element in the sequence:

![Previews showing Elise, Frank and Julia
composables](https://developer.android.com/static/develop/ui/compose/images/tooling/preview-sequence.png)

You can use the same provider class for multiple previews. If necessary, limit
the number of previews by setting the limit parameter.


```kotlin
@Preview
@Composable
fun UserProfilePreview2(
    @PreviewParameter(UserPreviewParameterProvider::class, limit = 2) user: User
) {
    UserProfile(user)
}
```

<br />

Previews using `@PreviewParameter` are named by default using the parameter
index and property name (user 0, user 1, user 2, and so on), which can make
it difficult to tell them apart. To improve preview clarity, you can provide
custom display names for each preview by overriding `getDisplayName()` in your
`PreviewParameterProvider`. This helps distinguish between different data
variations or UI states. For example, you can label previews based on the input
data:


```kotlin
class UserAgePreviewParameterProvider : PreviewParameterProvider<User> {
    // Using a List internally for efficient index-based access
    private val userList = listOf(
        User(name = "Elise", age = 30),
        User(name = "Frank", age = 31),
        User(name = "Julia", age = 40)
    )

    override val values = userList.asSequence()

    override fun getDisplayName(index: Int): String? {
        // Return null or an empty string to use the default index-based name
        val user = userList.getOrNull(index) ?: return null
        return "${user.name} - ${user.age}"
    }
}
```

<br />

![Previews with custom display names showing Elise - 30, Frank - 31 and Julia - 40
composables](https://developer.android.com/static/develop/ui/compose/images/tooling/preview-custom-display-name.png)

> [!TIP]
> **Tip:** For better performance, back your `Sequence` with a `List` in the `PreviewParameterProvider`. This provides efficient, index-based access in `getDisplayName()` and avoids slow lookups in large sequences.

## AI-assisted preview generation

The AI agent in Android Studio can automatically generate Compose previews for your
composables. Right-click on a Composable function and select
**AI \> Generate Preview for \[Composable name\]** . The agent analyzes your composable to
generate the necessary `@Preview` boilerplate with correct parameters,
helping you quickly verify that your UI renders as expected.
![](https://developer.android.com/static/studio/preview/features/images/generate-compose-preview.png) Generate a Compose Preview using AI.

## Annotation class `@Preview`

You can always 'ctrl or ⌘ + click' the `@Preview` annotation in Android
Studio for a full list of parameters that can be adjusted when customizing your
preview.


```kotlin
annotation class Preview(
    val name: String = "",
    val group: String = "",
    @IntRange(from = 1) val apiLevel: Int = -1,
    val widthDp: Int = -1,
    val heightDp: Int = -1,
    val locale: String = "",
    @FloatRange(from = 0.01) val fontScale: Float = 1f,
    val showSystemUi: Boolean = false,
    val showBackground: Boolean = false,
    val backgroundColor: Long = 0,
    @UiMode val uiMode: Int = 0,
    @Device val device: String = Devices.DEFAULT,
    @Wallpaper val wallpaper: Int = Wallpapers.NONE,
)
```

<br />

## Limitations and best practices

Android Studio executes previews code directly in the preview area. It doesn't
require running an emulator or physical device because it leverages a ported
part of the Android framework called `Layoutlib`. `Layoutlib` is a custom
version of the Android framework designed to run outside of Android devices. The
goal of the library is to provide a preview of a layout in Android Studio that
is very close to its rendering on devices.

### Previews limitations

Because of the way previews are rendered within Android Studio, they are
lightweight and don't require the whole Android framework to render them.
However, this comes with the following limitations:

- No network access
- No file access
- Some `Context` APIs may not be fully available

### Previews and `ViewModels`

Previews are limited when using [`ViewModel`](https://developer.android.com/viewmodel) within a
composable. The previews system is not capable of constructing all of the
parameters passed to a `ViewModel`, such as repositories, use cases, managers,
or similar. Also, if your `ViewModel` participates in dependency injection (such
as with [Hilt](https://developer.android.com/training/dependency-injection/hilt-android)), the previews system can't build the whole dependency
graph to construct the `ViewModel`.

When you try to preview a composable with `ViewModel`, Android Studio shows an
error when rendering the particular composable:

![Android studio problem pane with Failed to instantiate a `ViewModel`
message](https://developer.android.com/static/develop/ui/compose/images/tooling/viewmodel_failed.png)

> [!WARNING]
> **Warning:** You shouldn't pass the `ViewModel` instances down to other composable functions. When you do this, you're coupling the composables with the `ViewModel` type, which makes them less reusable, harder to test, and unable to preview.

If you want to preview a composable that uses a `ViewModel`, you should create
another composable with the parameters from `ViewModel` passed as arguments of
the composable. This way, you don't need to preview the composable that uses the
`ViewModel`.

    @Composable
    fun AuthorScreen(viewModel: AuthorViewModel = viewModel()) {
      AuthorScreen(
        name = viewModel.authorName,
        // ViewModel sends the network requests and makes posts available as a state
        posts = viewModel.posts
      )
    }

    @Composable
    fun AuthorScreen(
      name: NameLabel,
      posts: PostsList
    ) {
      // ...
    }

    @Preview
    @Composable
    fun AuthorScreenPreview(
      // You can use some sample data to preview your composable without the need to construct the ViewModel
      name: String = sampleAuthor.name,
      posts: List<Post> = samplePosts[sampleAuthor]
    ) {
      AuthorScreen(
          name = NameLabel(name),
          posts = PostsList(posts)
      )
    }

## Additional resources

To read more about how Android Studio promotes `@Preview` ease of use, and learn
more Tooling tips, check out the blog [Compose
Tooling](https://medium.com/androiddevelopers/compose-tooling-42621bd8719b).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
- [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material)
- [Using Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose)