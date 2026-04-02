---
title: https://developer.android.com/guide/topics/resources/pseudolocales
url: https://developer.android.com/guide/topics/resources/pseudolocales
source: md.txt
---

# Test your app with pseudolocales

A pseudolocale is a locale that is designed to simulate characteristics of languages that cause UI, layout, and other translation-related problems when an app is translated. Pseudolocales are created by instant and automatic translations that are readable in English for all*localizable*messages. Un-pseudolocalized text points to untranslatable messages in your source code.

Pseudolocales save time and money because you can make adjustments to the UI text and its layout before you commit your messages to the source repository to be sent for translation later. For a list of potential translation problems, see the[Spot localization issues](https://developer.android.com/guide/topics/resources/pseudolocales#spot_localization_issues)section.  
![](https://developer.android.com/static/images/develop/pseudo-locale-example-app_2x.png)

**Figure 1.**English (XA) pseudolocale.

The Android pseudolocale names follow standard locale naming conventions, and their locale IDs can be parsed by any BCP 47 compliant programming language. In this sense, pseudolocales are just like any other locales, such as French, Chinese, or Russian.

The Android platform provides the following two pseudolocales to represent left-to-right (LTR) and right-to-left (RTL) languages:  
![](https://developer.android.com/static/images/develop/pseudo-locale-example-app-rtl_2x.png)

**Figure 2.**AR (XB) pseudolocale.

**English (XA):**adds Latin accents to the base English UI text, expands the original text by adding non-accented text, and brackets each message unit to expose potential issues from expanded text. Potential issues can be layout breakage and badly formed message syntax, such as a sentence split into multiple parts displaying as multiple bracketed messages. The English (XA) pseudolocale is shown in figure 1.

**AR (XB):**sets the text direction of the original left-to-right messages to the right-to-left direction, which reverses the order of the characters in the original message. The AR (XB) pseudolocale is shown in figure 2.

Pseudolocales can help you make an RTL version of your app, even if you don't write or speak any RTL languages.

## Enable pseudolocales

Pseudolocales are usually added to developer-oriented builds. When you choose a pseudolocale on your device, all the apps that support pseudolocales take on the characteristics of the selected pseudolocale, including all the system apps such as the Settings app and Quick Settings panel.

<br />

To use the Android pseudolocales, you must be running Android 4.3 (API level 18) or higher and have[developer options](https://developer.android.com/studio/debug/dev-options)enabled on your device. You must also reboot your device after enabling developer options.

The following procedure explains how to enable pseudolocales:

1. In Android Studio, enable pseudolocales for a specific app by adding the following configuration to your`build.gradle`file:

   ### Groovy

   ```groovy
   android {
      ...
      buildTypes {
          debug {
              pseudoLocalesEnabled true
          }
      }
   }
   ```

   ### Kotlin

   ```kotlin
   android {
      ...
      buildTypes.getByName("debug") {
          isPseudoLocalesEnabled = true
      }
   }
   ```
2. [Build and run your app](https://developer.android.com/studio/run).

   ![](https://developer.android.com/static/images/develop/pseudo-locale-select_2x.png)

   **Figure 3.**Select a pseudolocale.
3. Use the Settings app to select a pseudolocale. This step varies based on your Android version, as follows:

   **Android 5.0 (API level 21) or higher**
   1. On the device, open the Settings app and tap**Languages and input \> Language preferences**.
   2. In the**Language preferences**list, drag the tab to move a pseudolocale to the top of the list and make it the active language. See figure 3.

   **Android 4.4.4 (API level 19) or lower**
   1. On the device, open the Settings app and tap**Languages and input \> Language preferences \> Add a language**.
   2. Tap a pseudolocale to add it to the**Language preferences**list.
   3. In the**Language preferences**list, drag the tab to move a pseudolocale to the top of the list and make it the active language See figure 3.

## Spot localization issues

Pseudolocales provide a time-saving and effective way to spot potential localizability issues in the UI by helping you identify problems in the following areas:

- Hardcoded strings, which can't be sent to translation, display as unaccented text in the pseudolocale to make them noticeable.
- UI layout issues caused by text expansion, showing where the UI can break due to text length.
- String concatenation, which displays as one message split across two or more brackets. This can make correct translation difficult, because translators have to translate each part independently without knowing that the parts are related. String concatenation can also make correct translation impossible, because different languages might require a different order of parts or a completely different sentence structure. For example, languages such as Japanese, Korean, and Tamil place the verb at the end of a sentence. When a sentence is concatenated, translators can't change the word order as needed.

- Bidirectional (BIDI) text problems, such as when content in one text direction includes an inline phrase in the opposite text direction, making the string difficult to read.

- Right-to-left (RTL) problems, such as elements not being mirrored. Some examples are a UI element not moving to the left, text not reversing and moving to the left, or misplaced punctuation, such as "pseudolocales rule!" changing to "elur selacoloduesp!" instead of "!elur selacoloduesp".