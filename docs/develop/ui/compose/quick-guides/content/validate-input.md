---
title: Validate input as the user types  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/validate-input
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Validate input as the user types Stay organized with collections Save and categorize content based on your preferences.




You can validate input as the user types in a text field, such as entering a
name, email, address, or other contact information. This validation reduces
errors and saves your users time.

## Results

![A valid text input](/static/develop/ui/compose/quick-guides/content/email_validation.png)


**Figure 1.** A text input field with email validators displaying no error messages for a valid email address.


![An invalid text input with errors](/static/develop/ui/compose/quick-guides/content/invalid_email_format_example.png)


**Figure 2.** A text input field displaying an error message when an invalid email address is entered.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Validate input as the user types

Use the following code to display the field input and validate the text while
the user types. If the information is not validated, an error message helps the
user correct the input.

```
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

TextSnippets.kt
```

### Key points about the code

* Defines a composable that reuses the [`OutlinedTextField`](/reference/kotlin/androidx/compose/material/TextField.composable) component, adding the
  required parameters to display validator error messages as user types.
* `EmailViewModel` is used to maintain state and provide the email validation logic.
* if `isError` is true, the UI provides a visual indicator of a validation
  error state.
* The component will display "Incorrect email format." until a complete, correct email is input.

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