---
title: Show or hide password based on a user toggle  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/show-hide-password
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Show or hide password based on a user toggle Stay organized with collections Save and categorize content based on your preferences.




You can create an icon to hide or show a password based on a user toggle to
improve security and enhance the user experience.

## Results

[

](/static/quick-guides/content/show_hide_password.mp4)


**Figure 1.** Toggling the show-and-hide password icon.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Show or hide a password based on user toggle

To show or hide a password based on a user toggle, create an input field for
entering information and use a clickable icon for the toggle:

```
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
        }
    )
}

TextSnippets.kt
```

### Key points about the code

* Maintains the password visibility state in`showPassword`.
* Uses a [`BasicSecureTextField`](/reference/kotlin/androidx/compose/foundation/text/BasicSecureTextField.composable) composable for password entry.
* Has a clickable trailing icon, which toggles the value of `showPassword`.
* Defines the [`textObfuscationMode`](/reference/kotlin/androidx/compose/foundation/text/input/TextObfuscationMode) attribute and the visible/not-visible
  state of the trailing icon by the state of `showPassword`.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display text

Text is a central piece of any UI. Find out different ways
you can present text in your app to provide a delightful user experience.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-text)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Request user input

Learn how to implement ways for users to interact
with your app by entering text and using other means of input.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/request-user-input)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)