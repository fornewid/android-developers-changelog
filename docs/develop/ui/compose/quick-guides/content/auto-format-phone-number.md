---
title: Auto-format a phone number in a text field  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/auto-format-phone-number
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Auto-format a phone number in a text field Stay organized with collections Save and categorize content based on your preferences.




You can auto format a phone number in a text field in your app, saving users
time by formatting the phone number as they input digits. Follow this guidance
to auto format a phone number:

* Create the text field.
* Auto-format a number in the text field.

## Results

![An auto-formatted phone number in the text field](/static/develop/ui/compose/quick-guides/content/nanp_formatter.gif)


**Figure 1.** An auto-formatted phone number in the text field.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create the text field

First, configure the [`TextField`](/reference/kotlin/androidx/compose/material/TextField.composable#TextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)). This example shows a phone number
formatted per the North American Numbering Plan
(NANP).`NanpVisualTransformation` formats a raw string of numbers to NANP, eg.
1234567890 to (123) 456-7890.

```
@Composable
fun PhoneNumber() {
    var phoneNumber by rememberSaveable { mutableStateOf("") }
    val numericRegex = Regex("[^0-9]")
    TextField(
        value = phoneNumber,
        onValueChange = {
            // Remove non-numeric characters.
            val stripped = numericRegex.replace(it, "")
            phoneNumber = if (stripped.length >= 10) {
                stripped.substring(0..9)
            } else {
                stripped
            }
        },
        label = { Text("Enter Phone Number") },
        visualTransformation = NanpVisualTransformation(),
        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)
    )
}

TextSnippets.kt
```

### Key points about the code

* A `TextField` composable where the `onValueChange` uses a regular expression
  to remove all non-numeric characters and limits the length to a maximum of
  10 characters before updating the `phoneNumber` state.
* The `TextField` has a custom [`VisualTransformation`](/reference/kotlin/androidx/compose/ui/text/input/VisualTransformation) instance set on the
  `visualTransformation` attribute. `NanpVisualTransformation`, the custom
  class instantiated here, is defined in the following section.

## Auto-format a number in the text field

To format a raw string of numbers, use the implementation of the custom
`NanpVisualTransformation` class:

```
class NanpVisualTransformation : VisualTransformation {

    override fun filter(text: AnnotatedString): TransformedText {
        val trimmed = if (text.text.length >= 10) text.text.substring(0..9) else text.text

        var out = if (trimmed.isNotEmpty()) "(" else ""

        for (i in trimmed.indices) {
            if (i == 3) out += ") "
            if (i == 6) out += "-"
            out += trimmed[i]
        }
        return TransformedText(AnnotatedString(out), phoneNumberOffsetTranslator)
    }

    private val phoneNumberOffsetTranslator = object : OffsetMapping {

        override fun originalToTransformed(offset: Int): Int =
            when (offset) {
                0 -> offset
                // Add 1 for opening parenthesis.
                in 1..3 -> offset + 1
                // Add 3 for both parentheses and a space.
                in 4..6 -> offset + 3
                // Add 4 for both parentheses, space, and hyphen.
                else -> offset + 4
            }

        override fun transformedToOriginal(offset: Int): Int =
            when (offset) {
                0 -> offset
                // Subtract 1 for opening parenthesis.
                in 1..5 -> offset - 1
                // Subtract 3 for both parentheses and a space.
                in 6..10 -> offset - 3
                // Subtract 4 for both parentheses, space, and hyphen.
                else -> offset - 4
            }
    }
}

TextSnippets.kt
```

### Key points about the code

* The `filter()` function inserts the non-numeric formatting characters at the
  appropriate places.
* The `phoneNumberOffsetTranslator` object contains two methods. One maps the
  offsets between the original string and the formatted one, and the other
  does the reverse mapping. These mappings enable the skipping of the
  formatting characters when the user changes the cursor location in the text
  field.
* The formatted string and `phoneNumberOffsetTranslator` are used as arguments
  for a `TransformedText` instance that is returned and used by the
  `TextField` to perform the formatting.

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