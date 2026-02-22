---
title: https://developer.android.com/training/tv/get-started/onscreen-keyboard
url: https://developer.android.com/training/tv/get-started/onscreen-keyboard
source: md.txt
---

# On-screen keyboard

Android TV comes with an on-screen software keyboard named Gboard. The keyboard supports a wide range of features, including speech-to-text (STT), which lets users speak and have the speech automatically translated into text for input. This feature works through Gboard, so you don't need to request the audio permission or do any special handling in your app.

## Input methods

You can[specify the input method type](https://developer.android.com/training/keyboard-input/style)for Android TV in exactly the same way as you do for mobile, except that Gboard for Android TV supports a more limited set of input types, shown in the following figures:

|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![Email input](https://developer.android.com/static/training/tv/images/atv-keyboard-email.png)**Figure 1.**Email input type. | ![Password input](https://developer.android.com/static/training/tv/images/atv-keyboard-password.png)**Figure 2.**Password input type. |
| ![Text input](https://developer.android.com/static/training/tv/images/atv-keyboard-text.png)**Figure 3.**Text input type.    | ![Numeric input](https://developer.android.com/static/training/tv/images/atv-keyboard-numeric.png)**Figure 4.**Numeric input type.    |

You can specify one or more input types based on your use case. Gboard automatically determines the best layout based on the input types you specify and the layouts it supports.

## Placement

One major difference with Gboard for Android TV is the ability to specify where the keyboard should be placed. Previously, the keyboard covered the bottom portion of the screen from edge to edge, but an update to Gboard lets it float. You can specify where the keyboard should go: left, right, or center. The default position is in the center.
![Alignment of Gboard](https://developer.android.com/static/training/tv/images/atv-keyboard-placement.png)**Figure 5.**Gboard alignment options.

To control the alignment, set the value within`privateImeOptions`for`horizontalAlignment`. The options for`horizontalAlignment`are the default`center`,`left`, and`right`. This is shown in the following example:  

```xml
<EditText
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:imeOptions="actionNext"
    android:privateImeOptions="horizontalAlignment=right">
```

This example results in the keyboard being placed at the bottom right, which works well when you have input fields aligned to the right:
![Gboard aligned to the right](https://developer.android.com/static/training/tv/images/atv-keyboard-placement-example.png)**Figure 6.**Gboard aligned to the right.

## Supported languages

Gboard for Android TV supports many different languages. The list of languages includes the following:

- English---US
- English---Australia
- English---Canada
- English---UK
- Afrikaans
- Albanian
- Arabic
- Bengali
- Bulgarian
- Burmese
- Chinese---Hong Kong
- Chinese---Simplified
- Chinese---Traditional
- Croatian
- Czech
- Danish
- Dutch---Belgium
- Dutch---Nederlands
- Estonian
- Farsi
- Filipino
- Finnish
- French
- French---Belgium
- French---Canada
- French---Switzerland
- German
- German---Austria
- German---Belgium
- German---Switzerland
- Greek
- Hebrew
- Hindi
- Hindi---transliteration
- Hungarian
- Indonesian
- Irish
- Italian
- Italian---Switzerland
- Japanese---Japan
- Korean
- Lithuanian
- Macedonian
- Malay
- Norwegian---Bokmål
- O'zbek
- Polish
- Portuguese
- Punjabi
- Romanian
- Russian
- Serbian
- Slovakian
- Slovenian
- Spanish---Mexico
- Spanish---Spain
- Swedish
- Thai
- Turkish
- Ukrainian
- Urdu
- Vietnamese