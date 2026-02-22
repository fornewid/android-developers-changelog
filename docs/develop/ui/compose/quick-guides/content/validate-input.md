---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/validate-input
url: https://developer.android.com/develop/ui/compose/quick-guides/content/validate-input
source: md.txt
---

<br />

You can validate input as the user types in a text field, such as entering a
name, email, address, or other contact information. This validation reduces
errors and saves your users time.

## Results

![A valid text input](https://developer.android.com/static/develop/ui/compose/quick-guides/content/email_validation.png) **Figure 1.** A text input field with email validators displaying no error messages for a valid email address. ![An invalid text input with errors](https://developer.android.com/static/develop/ui/compose/quick-guides/content/invalid_email_format_example.png) **Figure 2.** A text input field displaying an error message when an invalid email address is entered.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/validate-input_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Validate input as the user types

Use the following code to display the field input and validate the text while
the user types. If the information is not validated, an error message helps the
user correct the input.


```kotlin
class EmailViewModel : ViewModel() {
    var email by mutableStateOf("")
        private set

    val emailHasErrors by derivedStateOf {
        if (email.isNotEmpty()) {
            // Email is considered erroneous until it completely matches EMAIL_ADDRESS.
            !android.util.Patterns.EMAIL_ADDRESS.matcher(email).matches()
        } else {
            false
        }
    }

    fun updateEmail(input: String) {
        email = input
    }
}

@Composable
fun ValidatingInputTextField(
    email: String,
    updateState: (String) -> Unit,
    validatorHasErrors: Boolean
) {
    OutlinedTextField(
        modifier = Modifier
            .fillMaxWidth()
            .padding(10.dp),
        value = email,
        onValueChange = updateState,
        label = { Text("Email") },
        isError = validatorHasErrors,
        supportingText = {
            if (validatorHasErrors) {
                Text("Incorrect email format.")
            }
        }
    )
}

@Preview
@Composable
fun ValidateInput() {
    val emailViewModel: EmailViewModel = viewModel<EmailViewModel>()
    ValidatingInputTextField(
        email = emailViewModel.email,
        updateState = { input -> emailViewModel.updateEmail(input) },
        validatorHasErrors = emailViewModel.emailHasErrors
    )
}
```

<br />

### Key points about the code

- Defines a composable that reuses the [`OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TextField(kotlin.String,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors)) component, adding the required parameters to display validator error messages as user types.
- `EmailViewModel` is used to maintain state and provide the email validation logic.
- if `isError` is true, the UI provides a visual indicator of a validation error state.
- The component will display "Incorrect email format." until a complete, correct email is input.

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