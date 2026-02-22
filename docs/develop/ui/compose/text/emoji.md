---
title: https://developer.android.com/develop/ui/compose/text/emoji
url: https://developer.android.com/develop/ui/compose/text/emoji
source: md.txt
---

The standard set of emoji is [refreshed annually by
Unicode](https://emojipedia.org/new/), as emoji usage is increasing
rapidly for all types of apps.

If your app displays internet content or provides text input, *we strongly
recommend supporting the latest emoji fonts.* Otherwise, later emoji might be
displayed as a small square box called *tofu* (☐) or other incorrectly rendered
emoji sequences.

Android versions 11 (API level 30) and lower can't update the emoji font, so
apps that display them on those versions must be updated manually.

The following are examples of modern emoji.

| Examples | Version |
|---|---|
| 🫩 🪉 🇨🇶 | [16.0](https://emojipedia.org/emoji-16.0/) (September 2024) |
| 🐦‍🔥 🧑‍🧑‍🧒‍🧒 👩🏽‍🦽‍➡️ 🇲🇶 | [15.1](https://emojipedia.org/emoji-15.1/) (September 2023) |
| 🩷 🫸🏼 🐦‍⬛ | [15.0](https://emojipedia.org/emoji-15.0/) (September 2022) |
| 🫠 🫱🏼‍🫲🏿 🫰🏽 | [14.0](https://emojipedia.org/emoji-14.0/) (September 2021) |
| 😶‍🌫️ 🧔🏻‍♀️ 🧑🏿‍❤️‍🧑🏾 | [13.1](https://emojipedia.org/emoji-13.1/) (September 2020) |
| 🥲 🥷🏿 🐻‍❄️ | [13.0](https://emojipedia.org/unicode-13.0/) (March 2020) |
| 🧑🏻‍🦰 🧑🏿‍🦯 👩🏻‍🤝‍👩🏼 | [12.1](https://emojipedia.org/emoji-12.1/) (October 2019) |
| 🦩 🦻🏿 👩🏼‍🤝‍👩🏻 | [12.0](https://emojipedia.org/emoji-12.0/) (February 2019) |

[BOM March 2023](https://developer.android.com/develop/ui/compose/bom/bom) ([Compose UI 1.4](https://developer.android.com/jetpack/androidx/releases/compose-ui#version_14_2))) brings support for the [latest emoji
version](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2), including backwards compatibility with older Android versions down
to API 21.

*This support requires no changes to your app* --- if you use `Text` and
`TextField` (Material 2 or Material 3) or [`BasicText`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/package-summary#BasicText(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.text.TextStyle,kotlin.Function1,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,androidx.compose.ui.graphics.ColorProducer)) and
[`BasicTextField`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/package-summary#BasicTextField(androidx.compose.ui.text.input.TextFieldValue,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.text.TextStyle,androidx.compose.foundation.text.KeyboardOptions,androidx.compose.foundation.text.KeyboardActions,kotlin.Boolean,kotlin.Int,kotlin.Int,androidx.compose.ui.text.input.VisualTransformation,kotlin.Function1,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Brush,kotlin.Function1)), you get modern emoji support out of the box.

The best way to test the [latest emojis](https://unicode.org/emoji/charts/emoji-versions.html) in your app is by using
a real device on API 30 or below.

If you're using a custom emoji solution, or need to disable the default emoji
resolution in Compose for any other reason, you can use
[`PlatformTextStyle(emojiSupportMatch)`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/ui/ui-text/src/androidMain/kotlin/androidx/compose/ui/text/AndroidTextStyle.android.kt;l=85?q=emojisupportmatch):


```kotlin
Text(
    text = "Hello $EMOJI_TEXT",
    style = TextStyle(
        platformStyle = PlatformTextStyle(
            emojiSupportMatch = EmojiSupportMatch.None
        )/* ... */
    )
)
```

<br />

## Interoperatibility

If your app uses both Views and Compose in the same `Activity`, make sure you
are using the appropriate APIs to configure emojis correctly. The following
sections describe when to use each API.

### Extending from `ComponentActivity`

If your `Activity` extends from Compose [`ComponentActivity`](https://developer.android.com/reference/androidx/activity/ComponentActivity) instead of
[`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity), follow the [Support emoji without AppCompat](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2#support-without-appcompat)
instructions.

Because you are not extending [`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity), add the [Emoji2
library](https://developer.android.com/jetpack/androidx/releases/emoji2) to your dependencies and use [`EmojiTextView`](https://developer.android.com/reference/androidx/emoji/widget/EmojiTextView) in your views
instead of the [`TextView`](https://developer.android.com/reference/android/widget/TextView) widget, as shown in the following snippet:


```kotlin
class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val emojiTextView: EmojiTextView = findViewById(R.id.emoji_text_view)
        emojiTextView.text = getString(R.string.emoji_text_view, EMOJI_TEXT)

        val composeView: ComposeView = findViewById(R.id.compose_view)

        composeView.apply {
            setContent {
                // compose code
            }
        }
    }
}
```

<br />

Then, in your XML file:

```xml
<androidx.emoji2.widget.EmojiTextView
    android:id="@+id/emoji_text_view"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    />
```

### Extending from `AppCompatActivity`

If your `Activity` extends from `AppCompatActivity`, you can use
[`ComposeView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView) to call composable functions. Emojis render correctly across
Android versions when you use Text composables.

If you are extending from `AppCompatActivity`, inflate [`TextView`](https://developer.android.com/reference/android/widget/TextView) from XML
to have emojis rendered correctly.

This applies if you are inflating the XML:

- outside `ComposeView`, in the `Activity`. Notice the usage of `AppCompatActivity` and `TextView` in the following snippet:


```kotlin
class MyActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val emojiTextView: TextView = findViewById(R.id.emoji_text_view)
        emojiTextView.text = getString(R.string.emoji_text_view, EMOJI_TEXT)

        val composeView: ComposeView = findViewById(R.id.compose_view)

        composeView.apply {
            setContent {
                // compose code
            }
        }
    }
}
```

<br />

- inside `ComposeView`, via [view binding](https://developer.android.com/topic/libraries/view-binding) using [`AndroidViewBinding`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidViewBinding(kotlin.Function3,androidx.compose.ui.Modifier,kotlin.Function1)), like in the following snippet:


```kotlin
class MyActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(
            ComposeView(this).apply {
                setContent {
                    Column {
                        Text(EMOJI_TEXT)

                        AndroidViewBinding(ExampleViewBinding::inflate) {
                            emojiTextView.text = EMOJI_TEXT
                        }
                    }
                }
            }
        )
    }
}
```

<br />

To inflate a text with [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/package-summary#AndroidView(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function1,kotlin.Function1)) inside `ComposeView`, use
[`AppCompatTextView`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatTextView) to render emojis properly:


```kotlin
class MyActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(
            ComposeView(this).apply {
                setContent {
                    Column {
                        Text(EMOJI_TEXT)

                        AndroidView(
                            factory = { context -> AppCompatTextView(context) },
                            update = { it.text = EMOJI_TEXT }
                        )
                    }
                }
            }
        )
    }
}
```

<br />

See the [Interoperability APIs](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis) documentation for details.

## Troubleshooting

If you're seeing *tofu* (☐) instead of the emoji, first check if the problem is
your specific test device. There are few main things you can check:

- You might be using a [recently flashed device or a new emulator](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2#appcompat-displays-tofu-new-or-flashed-device). If possible, try another real test device you use often that is signed into your Google Account. Remember that API should be 30 or below to ensure emojis work in the correct versions.
- The test phone [doesn't support downloadable fonts](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2#appcompat-displays-tofu-no-downloadable-font-support).
- Check the [correct Google Play services version](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2#appcompat-displays-tofu-earlier-emulator-has-early-google-play-services).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Other considerations](https://developer.android.com/develop/ui/compose/migrate/other-considerations)
- [Text in Compose](https://developer.android.com/develop/ui/compose/text)
- [Scroll](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/scroll)