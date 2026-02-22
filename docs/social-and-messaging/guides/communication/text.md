---
title: https://developer.android.com/social-and-messaging/guides/communication/text
url: https://developer.android.com/social-and-messaging/guides/communication/text
source: md.txt
---

# Text in social and messaging apps

Text is at the heart of social applications, where users share thoughts, express emotions, and tell stories. This document explores how to work with text effectively, focusing on emoji, styling, and rich content integration.

## Working with emoji

Emoji have become an integral part of modern communication, particularly in social and messaging apps. They transcend language barriers, allowing users to express emotions and ideas quickly and effectively.

### Emoji support in Compose

Jetpack Compose, Android's modern declarative UI toolkit, simplifies emoji handling:

- **Input** : The[`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.ui.text.input.VisualTransformation,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.material.TextFieldColors))component natively supports emoji input.
- **Display** : Compose's[`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle))component renders emoji correctly, ensuring their consistent appearance across devices and platforms that offer an emoji2-compatible downloadable fonts provider, such as devices powered by[Google Play services](https://developers.google.com/android).

[Display emoji](https://developer.android.com/develop/ui/compose/text/emoji)covers displaying emoji in Jetpack Compose, including how to ensure that your app displays the latest emoji fonts, how to make sure emoji work correctly if your app uses[both Views and Compose in the same Activity](https://developer.android.com/develop/ui/compose/text/emoji#interoperatibility), and how to troubleshoot when emoji aren't showing up as expected.

### Emoji support in Views

If you're using Android Views, the[AppCompat](https://developer.android.com/jetpack/androidx/releases/appcompat)library 1.4 or higher provides emoji support for platform subclasses of[`TextView`](https://developer.android.com/reference/android/widget/TextView):

- **Input** : The AppCompat version of[`EditText`](https://developer.android.com/reference/android/widget/EditText)natively supports emoji input.
- **Display** : The AppCompat versions of[`TextView`](https://developer.android.com/reference/android/widget/TextView),[`ToggleButton`](https://developer.android.com/reference/android/widget/ToggleButton),[`Switch`](https://developer.android.com/design/building-blocks/switches),[`Button`](https://developer.android.com/reference/android/widget/Button),[`CheckedTextView`](https://developer.android.com/reference/android/widget/CheckedTextView),[`RadioButton`](https://developer.android.com/reference/android/widget/RadioButton),[`CheckBox`](https://developer.android.com/reference/android/widget/CheckBox),[`AutoCompleteTextView`](https://developer.android.com/reference/android/widget/AutoCompleteTextView), and[`MultiAutoCompleteTextView`](https://developer.android.com/reference/android/widget/MultiAutoCompleteTextView)all support emoji display, ensuring consistent appearance across devices and platforms that provide an emoji2-compatible downloadable fonts provider, such as devices powered by[Google Play services](https://developers.google.com/android).

If you are[creating a custom view](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2#custom-views)that is a direct or indirect subclass of`TextView`, extend the AppCompat implementation (rather than the platform implementation) to get built-in emoji support.[Support modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2)shows how to test and troubleshoot your emoji integration, support emoji without AppCompat, support emoji in custom views, support alternate fonts or font providers, and more.

### Using the Emoji Picker

The[Jetpack Emoji Picker](https://developer.android.com/develop/ui/views/text-and-emoji/emoji-picker)is an Android[View](https://developer.android.com/reference/android/view/View)that provides a categorized list of emoji, sticky variants, and support for recently used emoji --- compatible across multiple Android versions and devices. It's an easy way to uplevel your app's emoji integration.

Begin by importing the library in`build.gradle`.  

    dependencies {
       implementation("androidx.emoji2:emojipicker:$version")
    }

### Using the Emoji Picker with Compose

You construct the Emoji Picker in Compose using the[`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1))composable. This snippet includes a listener that lets you know when an emoji is selected:  

    AndroidView(
        modifier = Modifier.fillMaxSize(),
        factory = { context ->
            val emojiPickerView = EmojiPickerView(context)
            emojiPickerView.setOnEmojiPickedListener(this::updateTextField)
            emojiPickerView
        },
    )

Compose 1.7 adds lots of new functionality to[`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/package-summary#BasicTextField(androidx.compose.foundation.text.input.TextFieldState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.text.input.InputTransformation,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.input.KeyboardActionHandler,androidx.compose.foundation.text.input.TextFieldLineLimits,kotlin.Function2,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,androidx.compose.foundation.text.input.OutputTransformation,androidx.compose.foundation.text.input.TextFieldDecorator,androidx.compose.foundation.ScrollState)), including support for[`TextFieldState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState), which can sit in your[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel#viewmodel-benefits):  

    private val emojiTextFieldState = TextFieldState()

    @Composable fun EmojiTextField() {
        BasicTextField(
            state = emojiTextFieldState,
        )
    }

You can use[`TextFieldState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState)to insert text at the cursor position or replace the selected text, as if you were typing in the IME:  

    private fun insertStringAsIfTyping(textFieldState: TextFieldState, string: String) {
        textFieldState.edit {
            replace(selection.start, selection.end, string)
            // clear selection on replace if necessary
            if (hasSelection) selection = TextRange(selection.end)
        }
    }

The callback can update the`BasicTextField`using the helper function:  

    private fun updateTextField(emojiViewItem: EmojiViewItem) {
        insertStringAsIfTyping(emojiTextFieldState, emojiViewItem.emoji)
    }

### Using the Emoji Picker with Views

The Emoji Picker also works well with Views.

Inflate the[EmojiPickerView](https://developer.android.com/reference/androidx/emoji2/emojipicker/EmojiPickerView). Optionally set emojiGridColumns and emojiGridRows based on the desired size of each emoji cell.  

    <androidx.emoji2.emojipicker.EmojiPickerView
        ...
        app:emojiGridColumns="9" />

Insert a character at the cursor position or replace the selected text:  

    // Consider unregistering/reregistering anyTextWatcher that you might have as part of this
    private fun insertStringAsIfTyping(editText: EditText, string: String) {
        val stringBuffer = StringBuffer(editText.text.toString())
        val index = editText.selectionStart
        if ( !editText.hasSelection() ) {
            stringBuffer.insert(index, string)
        } else {
            stringBuffer.replace(index, editText.selectionEnd, string)
        }
        editText.setText(stringBuffer.toString())
        editText.setSelection(index + string.length)
    }

Provide a listener to the picked emoji, and use it to append characters to the`EditText`.  

    // a listener example
    emojiPickerView.setOnEmojiPickedListener {
       val editText = findViewById<EditText>(R.id.edit_text)
       insertStringAsIfTyping(editText, it.emoji)
    }

## Style text

By applying visual distinctions to text, such as font styles, sizes, weights, and colors, you can enhance the readability, hierarchy, and overall aesthetic appeal of the user interface of your social or messaging app. Text styles help users quickly parse information, distinguish between different types of messages, and identify important elements.

### Style text in Compose

The[`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle))composable offers a wealth of styling options, including:

- **Text Color** : Set[`Color`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Color)to make text stand out.
- **Font Size** : Control[`FontSize`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle#fontSize())for appropriate scale.
- **Font Style** : Use[`FontStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontStyle)to italicize text.
- **Font Weight** : Adjust[`FontWeight`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight)for bold, light, etc. text variations.
- **Font Family** : Use[`FontFamily`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontFamily)to choose a suitable font.

    Text(
        text = "Hello 👋",
        color = Color.Blue
        fontSize = 18.sp,
        fontWeight = FontWeight.Bold,
        fontFamily = FontFamily.SansSerif
    )

You can set these styling options consistently across your application using*themes*.  

    MaterialTheme(
        // This theme would include Color.Blue (as appropriate for dark and light themes)
        colorScheme = colorScheme,
        content = content,
        typography = Typography(
            titleLarge = TextStyle(
                fontSize = 18.sp,
                fontFamily = titleFont,
                fontWeight = FontWeight.Bold
            ),
        ),
    )

#### Add multiple styles in text

You can set different styles within the same`Text`composable using an[`AnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/AnnotatedString).

`AnnotatedString`has a[type-safe builder](https://kotlinlang.org/docs/reference/type-safe-builders.html),[`buildAnnotatedString`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/package-summary#buildAnnotatedString(kotlin.Function1)), to make it easier to create.  

    @Composable
    fun MultipleStylesInText() {
        Text(
            buildAnnotatedString {
                withStyle(style = SpanStyle(color = Color.Blue)) {
                    append("M")
                }
                append("y ")

                withStyle(style = SpanStyle(fontWeight = FontWeight.Bold, color = Color.Red)) {
                    append("S")
                }
                append("tyle")
            }
        )
    }

See[Style text](https://developer.android.com/develop/ui/compose/text/style-text)for lots more information about text styling in Compose, including[adding a shadow](https://developer.android.com/develop/ui/compose/text/style-text#shadow),[advanced styling with a Brush](https://developer.android.com/develop/ui/compose/text/style-text#brush), and[opacity](https://developer.android.com/develop/ui/compose/text/style-text#text-opacity).

### Style text in Views

With Views, rely on styles and themes for consistent typography. See[Styles and themes](https://developer.android.com/develop/ui/views/theming/themes)for more information on how to apply custom theming for the views in your app. If you want to set different styles within a single text view, see[Spans](https://developer.android.com/develop/ui/views/text-and-emoji/spans)for more information on how to change text in a variety of ways, including adding[color](https://developer.android.com/reference/android/text/style/ForegroundColorSpan), making the text[clickable](https://developer.android.com/reference/android/text/style/ClickableSpan), scaling the[text size](https://developer.android.com/reference/android/text/style/AbsoluteSizeSpan), and drawing text in a[customized way](https://developer.android.com/develop/ui/views/text-and-emoji/spans#custom-spans).

## Support image keyboards and other rich content

Users often want to communicate using stickers, animations, and other kinds of rich content. To make it simpler for apps to receive rich content, Android 12 (API level 31) introduced a unified API that lets your app accept content from any source: clipboard, keyboard, or dragging and dropping. For backward compatibility with previous Android versions (currently back to API level 14), we recommend you use the Android Jetpack (AndroidX) version of this API.

You attach an[`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener)to UI components and get a callback when content is inserted through any mechanism. The callback becomes the single place for your code to handle receiving all content, from plain and styled text to markup, images, videos, audio files, and others.

See[Receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content)to learn more about how to implement support in your app. Jetpack Compose now has[`dragAndDropSource`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/draganddrop/package-summary#(androidx.compose.ui.Modifier).dragAndDropSource(kotlin.Function1,kotlin.coroutines.SuspendFunction1))and[`dragAndDropTarget`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/draganddrop/package-summary#(androidx.compose.ui.Modifier).dragAndDropTarget(kotlin.Function1,androidx.compose.ui.draganddrop.DragAndDropTarget))modifiers to simplify implementing drag-and-drop within your app and between other apps.