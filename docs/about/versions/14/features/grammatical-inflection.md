---
title: https://developer.android.com/about/versions/14/features/grammatical-inflection
url: https://developer.android.com/about/versions/14/features/grammatical-inflection
source: md.txt
---

3 billion people speak *gendered languages* : languages where grammatical
categories---such as nouns, verbs, adjectives, and prepositions---inflect according
to the gender of people and objects you talk to or about. Traditionally, many
gendered languages use masculine grammatical gender as the default or *generic*
gender.

Addressing users in the wrong grammatical gender, such as addressing women in
masculine grammatical gender, can [negatively impact](https://www.nature.com/articles/s41539-021-00087-7)
their performance and attitude. In contrast, a UI with language that correctly
reflects the user's grammatical gender can improve user engagement and provide
a more personalized and natural-sounding user experience.

To help you build a user-centric UI for gendered languages, Android 14
introduces the Grammatical Inflection API, which lets you add support for
grammatical gender without refactoring your app.

## Example of inflection for grammatical gender

In gendered languages, grammatical gender can't be worked around the same way as
it can in English. For example, in English to write a message telling the user
that they are subscribed to your app's service, you could use a single phrase:
"You are subscribed to...".

To provide a similar phrase in French, there are a few options:

- Masculine-inflected form: "Vous êtes abonné à..." (English: "You are subscribed to...")
- Feminine-inflected form: "Vous êtes abonnée à..." (English: "You are subscribed to...")
- Neutral phrasing that avoids inflection: "Abonnement à...activé" (English: "Subscription to ... enabled")

Similar to English, the first two options address the user directly. However,
without any mechanism to accommodate this grammatical feature of French, you
would only have the third option, which changes the tone of the message and
might not be what you want to display in your user interface.

In these cases, the Grammatical Inflection API lowers the effort to display
strings relative to the viewer's grammatical gender---that is, the person who's
viewing the UI, not who's being talked about. To show users personalized
translations in your app, [add translations that are inflected for each
grammatical gender](https://developer.android.com/about/versions/14/features/grammatical-inflection#add-translations) for affected languages and then use the
[`GrammaticalInflectionManager`](https://developer.android.com/reference/android/app/GrammaticalInflectionManager) API to adjust which translations are shown
to each user.
| **Note:** Support for these resource qualifiers is only available in [Android
| Studio Giraffe Canary 7](https://developer.android.com/studio/preview/features#grammatical-inflection-api) or higher.

In many languages, grammatical gender also applies to regular nouns in addition
to people. For example, in French the word chaise (chair) is feminine, whereas
oiseau (bird) is masculine. For situations other than addressing the user, you
can use the existing [ICU SelectFormat](https://developer.android.com/reference/android/icu/text/SelectFormat) API.

## Implement the API

After the user has indicated their grammatical gender (for example, either
through a settings section of your app or a user setup workflow), you can use
the [`setRequestedApplicationGrammaticalGender(int)`](https://developer.android.com/reference/android/app/GrammaticalInflectionManager#setRequestedApplicationGrammaticalGender(int)) method to store the
value in your app's resources configuration.

For example, if you want to set a user's preferred grammatical gender to
feminine, you would ask the user to select which grammatical gender they prefer
and then call the API:  

### Kotlin

```kotlin
// Set app's grammatical gender to feminine
val gIM = mContext.getSystemService(GrammaticalInflectionManager::class.java)
gIM.setRequestedApplicationGrammaticalGender(
    Configuration.GRAMMATICAL_GENDER_FEMININE)
```

### Java

```java
// Set app's grammatical gender to feminine
GrammaticalInflectionManager gIM =
    mContext.getSystemService(GrammaticalInflectionManager.class);
gIM.setRequestedApplicationGrammaticalGender(
    Configuration.GRAMMATICAL_GENDER_FEMININE);
```
| **Caution:** Calling `setRequestedApplicationGrammaticalGender()` recreates your `Activity`, unless your app handles `grammaticalGender` configuration changes by itself.

Here is example of how to declare [configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes) in your app's
manifest file if you want to handle them yourself:  

    <activity android:name=".TestActivity"
                  android:configChanges="grammaticalGender"
                  android:exported="true">
    </activity>

If your app needs to check the grammatical gender in the current resource
configuration, you can use the [`getApplicationGrammaticalGender()`](https://developer.android.com/reference/android/app/GrammaticalInflectionManager#getApplicationGrammaticalGender()) method
to retrieve it:  

### Kotlin

```kotlin
val gIM = mContext.getSystemService(GrammaticalInflectionManager::class.java)
val grammaticalGender = gIM.getApplicationGrammaticalGender()
```

### Java

```java
GrammaticalInflectionManager gIM =
    mContext.getSystemService(GrammaticalInflectionManager.class);
int grammaticalGender = gIM.getApplicationGrammaticalGender();
```

## Add translations for languages with grammatical gender

To provide localized text for languages with grammatical gender, [create an
alternative resources file](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources) and append the grammatical gender qualifier
immediately after the locale name for those languages. The following table
outlines the possible values:

| Qualifier | String value | Example (French `fr`) |
|---|---|---|
| Feminine | `feminine` | `res/values-fr-feminine/strings.xml` |
| Masculine | `masculine` | `res/values-fr-masculine/strings.xml` |
| Neuter | `neuter` | `res/values-fr-neuter/strings.xml` |

You should only include strings that support grammatical gender inflections in
these resources files. All strings must have a value in the [default resource
file that contains other localized strings](https://developer.android.com/guide/topics/resources/localization#creating-alternatives). This default translation is
shown whenever a gender-inflected translation is not available.

In the [example provided for French earlier](https://developer.android.com/about/versions/14/features/grammatical-inflection#inflection), the neutral phrasing would be
the value of the string in the default resources `res/values-fr/strings.xml`
file. The following code snippets show how each resource file would be formatted
to accommodate all the grammatical variations from the example in French:  

### Feminine


Include the feminine-inflected string in the `res/values-fr-feminine/strings.xml` resources file:  

```xml
<resources>
    ...
    <string name="example_string">Vous êtes abonnée à...</string>
</resources>
```

### Masculine


Include the masculine-inflected string in the `res/values-fr-masculine/strings.xml` resources file:  

```xml
<resources>
    ...
    <string name="example_string">Vous êtes abonné à...</string>
</resources>
```

### Neuter


Include the default string in the `res/values-fr/strings.xml` resources file:  

```xml
<resources>
    ...
    <string name="example_string">Abonnement à...activé</string>
</resources>
```