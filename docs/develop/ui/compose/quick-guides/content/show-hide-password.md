---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/show-hide-password
url: https://developer.android.com/develop/ui/compose/quick-guides/content/show-hide-password
source: md.txt
---

<br />

You can create an icon to hide or show a password based on a user toggle to
improve security and enhance the user experience.

## Results

<br />

**Figure 1.** Toggling the show-and-hide password icon.

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/show-hide-password_199fce1cf843ea3721f0f0f028137b0d60d4f71fa63b09730be7ae764b094fa8.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Show or hide a password based on user toggle

To show or hide a password based on a user toggle, create an input field for
entering information and use a clickable icon for the toggle:


```kotlin
@Composable
fun PasswordTextField() {
    val state = remember { TextFieldState() }
    var showPassword by remember { mutableStateOf(false) }
    BasicSecureTextField(
        state = state,
        textObfuscationMode =
        if (showPassword) {
            TextObfuscationMode.Visible
        } else {
            TextObfuscationMode.RevealLastTyped
        },
        modifier = Modifier
            .fillMaxWidth()
            .padding(6.dp)
            .border(1.dp, Color.LightGray, RoundedCornerShape(6.dp))
            .padding(6.dp),
        decorator = { innerTextField ->
            Box(modifier = Modifier.fillMaxWidth()) {
                Box(
                    modifier = Modifier
                        .align(Alignment.CenterStart)
                        .padding(start = 16.dp, end = 48.dp)
                ) {
                    innerTextField()
                }
                Icon(
                    if (showPassword) {
                        Icons.Filled.Visibility
                    } else {
                        Icons.Filled.VisibilityOff
                    },
                    contentDescription = "Toggle password visibility",
                    modifier = Modifier
                        .align(Alignment.CenterEnd)
                        .requiredSize(48.dp).padding(16.dp)
                        .clickable { showPassword = !showPassword }
                )
            }
       https://github.com/android/snippets/blob/df2de96bc6313883ec381bd33c9df6b614bd9325/compose/snippets/src/main/java/com/example/compose/snippets/text/TextSnippets.kt#L868-L909nippets.kt
```

<br />

### Key points about the code

- Maintains the password visibility state in`showPassword`.
- Uses a [`BasicSecureTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/package-summary#BasicSecureTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,kotlin.Function2,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,androidx.compose.foundation.text.input.TextFieldDecorator,androidx.compose.foundation.text.input.TextObfuscationMode,kotlin.Char)) composable for password entry.
- Has a clickable trailing icon, which toggles the value of `showPassword`.
- Defines the [`textObfuscationMode`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextObfuscationMode) attribute and the visible/not-visible state of the trailing icon by the state of `showPassword`.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways you can present text in your app to provide a delightful user experience. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-text) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Request user input

Learn how to implement ways for users to interact with your app by entering text and using other means of input. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/request-user-input) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)