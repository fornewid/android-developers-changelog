---
title: https://developer.android.com/develop/devices/assistant/in-app-promo-sdk
url: https://developer.android.com/develop/devices/assistant/in-app-promo-sdk
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

To promote features of your app and make it easier to use, you can suggest
Assistant shortcuts to your users. Assistant shortcuts are concise phrases that
a user can utter to trigger functionality within your app.

Though Assistant shortcuts can be created manually by your users, the
In-App Promo SDK enables you to proactively suggest and implement Assistant
shortcuts. By suggesting shortcuts, you give your users clear, simple
paths back to their favorite activities in your app without the added effort
of setting up the shortcuts.

For example, if a user performs a search for "heavy metal workout" in your music
app, you might suggest an Assistant shortcut directly to those search results
in the future. When you suggest a shortcut, a prompt appears in your app that
displays the proposed phrase for the shortcut and asks the user if the shortcut
can be created.

In this example, you suggest the phrase, "start my heavy metal
workout." The user accepts the suggestion and can then launch the shortcut by
saying, *"Hey Google, start my heavy metal workout."*

For more information about ways to grow your app's audience, see
[Grow your app with app actions](https://developer.android.com/develop/devices/assistant/grow-overview).

The In-App Promo SDK provides the following methods:

- **`lookupShortcut`:** checks whether the shortcut you want to suggest already
  exists. The method also checks for any issues that prevent the shortcut
  from being created. If the shortcut can't be created, `lookupShortcut`
  returns the reasons why.

- **`createShortcutSuggestionIntent`:** returns an intent you can use to
  prompt the user to create the suggested shortcut.

- **`createShortcutSettingsIntent`:** returns an intent you can use to move
  the user to the Assistant Shortcut settings for your app.

> [!NOTE]
> **Note:** The In-App Promo SDK doesn't support shortcuts bound to [custom intents](https://developer.android.com/guide/app-actions/custom-intents).

## Prerequisites and limitations

This section describes prerequisites and requirements for using suggestions
as well as limitations you might encounter.

### Development prerequisites

To use suggestions, your development environment must meet the following
prerequisites.

- Extend your Android app to
  [use App Actions](https://developer.android.com/guide/app-actions/get-started).

- Include `com.google.android.googlequicksearchbox` within the `<queries>`
  tag in your manifest. For example:

      <manifest ...>
        <queries>
          <package android:name="com.google.android.googlequicksearchbox" />
        </queries>
        ...
      </manifest>

- Use [Android App Bundles](https://developer.android.com/guide/app-bundle) to publish your apps.

### Device requirements

To test your suggestions on a device, your device must have the following
installed.

- The latest version of the
  [Google app](https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox)

- Android 6.0 (API level 23) or higher

### Known limitations

Suggestions are supported only in English. For users to see your suggestions,
they must set the Assistant language on their device to English.

## Implement suggestions

To implement suggestions, you need to update your `build.gradle`
file, set up the suggestions client, and then define the suggestions that you
want to give users.

1. Add the library dependency to your `build.gradle` file.

       dependencies {
         ...
         implementation "com.google.assistant.appactions:suggestions:1.0.0"
       }

2. Define an instance of `AssistantShortcutSuggestionsClient`.

   ### Kotlin

   ```kotlin
   val shortcutsClient =
     AssistantShortcutSuggestionsClient.builder()
       .setContext(CONTEXT: Context)
       .setVerifyIntents(VERIFY_INTENTS: Boolean)
       .setCustomExecutor(CUSTOM_EXECUTOR: Object)
       .build()
   ```

   ### Java

   ```java
   AssistantShortcutSuggestionsClient shortcutsClient =
     AssistantShortcutSuggestionsClient.builder()
       .setContext(CONTEXT: Context)
       .setVerifyIntents(VERIFY_INTENTS: Boolean)
       .setCustomExecutor(CUSTOM_EXECUTOR: Object)
       .build();
   ```

   In this example:
   - `CONTEXT` (required) is the application context.

   - `VERIFY_INTENTS` (required) determines whether to verify every intent
     created when suggesting shortcuts to users. When `true`, the intents
     created by `AssistantShortcutSuggestionsClient` are verified. If
     an intent is invalid, an exception is returned.

   - `CUSTOM_EXECUTOR` (optional) is a custom executor for running
     asynchronous tasks. If not provided, the SDK uses a
     single-threaded executor for the task.

3. Use the `lookupShortcut` method to determine whether the shortcut you want to
   suggest is valid and, optionally, whether the shortcut already exists.

   1. Create an app shortcut intent. The shortcut intent represents the
      shortcut that you want to suggest to a user. The following example
      creates an intent for a shortcut to start an exercise.

      ### Kotlin

      ```kotlin
      val exercise = mapOf(
          "@type" to "Exercise",
          "@context" to "http://schema.googleapis.com",
          "name" to "Running",
      )

      val appShortcutIntent = AppShortcutIntent.builder()
          .setIntentName("actions.intent.START_EXERCISE")
          .setPackageName("my.app.package")
          .setIntentParamName("exercise")
          .setIntentParamValue(exercise)
          .build()
       
      ```

      ### Java

      ```java
        Map<String, Object> exercise = new HashMap<>();
        exercise.put("@type", "Exercise");
        menuItem.put("@context", "http://schema.googleapis.com");
        menuItem.put("name", "Running");

        AppShortcutIntent appShortcutIntent =
            AppShortcutIntent.builder()
                .setIntentName("actions.intent.START_EXERCISE")
                .setPackageName("my.app.package")
                .setIntentParamName("exercise")
                .setIntentParamValue(exercise)
                .build();
       
      ```
   2. Pass the shortcut intent to the `lookupShortcut` method.

      ### Kotlin

      ```kotlin
      val result = shortcutsClient.lookupShortcut(appShortcutIntent).await()
      if (!result.isShortcutPresent) {
          // App can suggest creating a shortcut
      } else {
          // App can remind the user that they have a shortcut for this app action
      }
      ```

      ### Java

      ```java
      shortcutsClient.lookupShortcut(appShortcutIntent)
        .addOnSuccessListener(shortcutLookupResult -> {
          if (!shortcutLookupResult.isShortcutPresent()) {
            // App can suggest creating a shortcut
          } else {
            // App can remind the user that they have a shortcut for this app action
          }
        })
        .addOnFailureListener(e -> Log.e(TAG, "Shortcut lookup failed", e));
      ```
4. Create the suggestion using the shortcut intent. There are two methods you
   can use to create a suggestion:

   - **`createShortcutSuggestionIntent`:** returns an Android intent that you
     use to start the shortcut suggestion activity in the context of your
     app.

     ### Kotlin

     ```kotlin
     val exerciseShortcut = AppShortcutSuggestion.builder()
         .setAppShortcutIntent(appShortcutIntent)
         .setCommand(PHRASE: String)
         .build()

     val intent = shortcutsClient.createShortcutSuggestionIntent(exerciseShortcut).await()
     application.startActivity(intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
     ```

     ### Java

     ```java
       AppShortcutSuggestion exerciseShortcut =
           AppShortcutSuggestion.builder()
               .setAppShortcutIntent(appShortcutIntent)
               .setCommand(PHRASE: String)
               .build();

       shortcutsClient.createShortcutSuggestionIntent(exerciseShortcut)
           .addOnSuccessListener(intent ->
               getApplication().startActivity(
                   intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK));
           )
           .addOnFailureListener(e ->
               Log.e(TAG, "Failed to get shortcut suggestion intent", e);
           );
     ```

     In this example, <var translate="no">PHRASE</var> is the utterance that you want to
     suggest to the user as a shortcut. For example, if you wanted the user
     to say *"Hey Google, start a run"* as a shortcut, replace
     <var translate="no">PHRASE</var> with `"start a run"`.

     > [!NOTE]
     > **Note:** Do not include `Hey Google` in your suggestion.

     ### Kotlin

     ```kotlin
     val exerciseShortcut = AppShortcutSuggestion.builder()
         .setAppShortcutIntent(appShortcutIntent)
         .setCommand("start a run")
         .build()
     ```

     ### Java

     ```java
     AppShortcutSuggestion exerciseShortcut =
         AppShortcutSuggestion.builder()
             .setAppShortcutIntent(appShortcutIntent)
             .setCommand("start a run")
             .build();
     ```
   - **`createShortcutSettingsIntent`:** returns an Android intent that moves
     the user to the shortcut settings interface in the Assistant app.

     ### Kotlin

     ```kotlin
     val intent = shortcutsClient.createShortcutSettingsIntent().await()
     application.startActivity(intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
     ```

     ### Java

     ```java
       shortcutsClient.createShortcutSettingsIntent()
         .addOnSuccessListener(intent ->
             getApplication().startActivity(
                 intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK));
         )
         .addOnFailureListener(e ->
             Log.e(TAG, "Failed to get shortcut settings intent", e);
         );
     ```
5. Call [`startActivity`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent))
   using the Android intent returned during the previous step.

   > [!NOTE]
   > **Note:** If the shortcut you suggest conflicts with an existing shortcut, the user remains in the context of your app and is prompted to set a new utterance for the shortcut.

## Troubleshoot suggestions

This section lists issues and exceptions that you might encounter when suggesting shortcuts.

### "GoogleInstallationUnsupportedException: Cannot bind to service"

Due to
[package visibility filtering](https://developer.android.com/training/package-visibility#declare-other-apps),
"`GoogleInstallationUnsupportedException`: Cannot bind to service" may happen on
Android 11 and later. Make sure that `com.google.android.googlequicksearchbox`
is included within the `<queries>` tag in your manifest:

    <manifest ...>
      <queries>
        <package android:name="com.google.android.googlequicksearchbox" />
      </queries>
      ...
    </manifest>

### "Failed to verify the APK signature"

The following error can occur if you do not submit your production app as
an app bundle:

    Failed to verify the APK signature. If this is a development build, please
    make sure to update the preview of your app in App Actions Test Tool.

Ensure that you
[submit your app as an Android App Bundle](https://developer.android.com/guide/app-bundle).

### "Failed to get user shortcuts"

The "Failed to get user shortcuts" error message can happen if you recently
added an account to the device and the new account's shortcut data isn't
cached on the device yet.

To sync the shortcut data on the device, add or delete an Assistant shortcut
using the Assistant app's interface.

### Shortcut creation activity immediately closes without showing any content

The shortcut creation activity can close without displaying any content if you
don't create a preview using the App Actions Test Tool or if the preview
expires. Update your preview and try again.