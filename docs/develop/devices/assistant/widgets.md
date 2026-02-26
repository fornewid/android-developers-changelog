---
title: https://developer.android.com/develop/devices/assistant/widgets
url: https://developer.android.com/develop/devices/assistant/widgets
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml
![](https://developer.android.com/static/guide/app-actions/images/Fitness4-widget.png) **Figure 1.** Launching a widget for `GET_EXERCISE_OBSERVATION`.

For many intents, the best response is to deliver a simple answer, brief
confirmation, or quick interactive experience to the user. You can display an
[Android app widget](https://developer.android.com/guide/topics/appwidgets/overview) in Google Assistant to fulfill these kinds of intents.

This guide covers how to fulfill Assistant user queries using widgets and how to
enhance your widget experience for Assistant with the App Actions
[Widgets Extension library](https://developer.android.com/develop/devices/assistant/widgets#library).

## Benefits

Widgets are miniature application views that can be embedded on Android
surfaces, such as the launcher or lock screen. With App Actions, you increase
the impact of your widgets by making them eligible for display in Assistant:

1. **Discovery:** Proactively display widgets in response to users' natural language queries.
2. **Engagement:** Display widgets in hands-free contexts, such as when Assistant provides [personal results](https://support.google.com/assistant/answer/7684543) on the lock screen, and on [Android Auto](https://developer.android.com/cars).
3. **Retention:** Let users pin the widgets displayed in Assistant to their launcher. Pinning functionality requires the [Widgets Extension library](https://developer.android.com/develop/devices/assistant/widgets#library).

## How Assistant displays widgets

There are two ways users can invoke widgets on Assistant:

- Explicitly requesting a widget by name.
- Speaking a query to Assistant that triggers a [built-in intent](https://developer.android.com/reference/app-actions/built-in-intents) (BII) or [custom intent](https://developer.android.com/guide/app-actions/custom-intents) configured for widget fulfillment.

#### Explicit invocation

To explicitly invoke widgets for any installed app, users can ask Assistant
things like:

- *"Hey Google, show ExampleApp widget."*
- *"Widgets from ExampleApp."*

Assistant displays these widgets with the generic introduction: *"ExampleApp
says, here's a widget."* While Assistant natively returns widgets requested in
this manner with no work required by the app developer, this invocation method
requires the user to have explicit knowledge of the widget to request it. To
simplify widget discovery, use the intent fulfillment method detailed in the
following section.

#### Intent fulfillment

Make your widgets easier to find by using them to fulfill the natural
language queries users perform on Assistant. For example, you can return a
widget whenever a user triggers the [`GET_EXERCISE_OBSERVATION`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/get-exercise-observation) BII in your
fitness app by asking, *"Hey Google, how many miles have I run this week on
ExampleApp?"* In addition to simplifying discovery, integrating widgets with
App Actions offers these advantages:

- **Parameter access:** Assistant provides the [intent parameters](https://developer.android.com/guide/app-actions/intents#implement_biis_and_handle_intent_parameters) extracted from the user query to your widget, enabling [tailored responses](https://developer.android.com/develop/devices/assistant/widgets#extract_parameters).
- **Custom TTS introductions:** You can provide a text-to-speech (TTS) string for Assistant to announce when displaying your widget.
- **Widget pinning:** Assistant displays an **Add this widget** button near your widget, letting users easily pin your widgets to their launcher.

> [!NOTE]
> **Note:** Not all BIIs support widget fulfillment. Refer to the [BII reference](https://developer.android.com/reference/app-actions/built-in-intents) for the BII you plan to use.

## Implement widget fulfillment

To implement widget fulfillment for your intents, follow these steps:

1. Implement an Android widget by following the steps described in [Create a simple widget](https://developer.android.com/guide/topics/appwidgets).
2. In your app's `shortcuts.xml` resource file, add an [`<app-widget>`](https://developer.android.com/develop/devices/assistant/widgets#app-widget) element to your capability containing fulfillment details and BII [`<parameter>`](https://developer.android.com/develop/devices/assistant/widgets#parameter) tags. Update your widget to handle the parameters.
3. Add the required [Widgets Extension library](https://developer.android.com/develop/devices/assistant/widgets#library), which lets Assistant pass BII names and parameters to your widgets. It also enables [custom TTS introductions](https://developer.android.com/develop/devices/assistant/widgets#tts) and widget [pinning](https://developer.android.com/develop/devices/assistant/widgets#pinning) functionality.

The following section describes the `<app-widget>` schema for `shortcuts.xml`.

### Widget schema

[`<app-widget>`](https://developer.android.com/develop/devices/assistant/widgets#app-widget) elements are defined as fulfillments within
[`<capability>`](https://developer.android.com/guide/app-actions/action-schema#capability) elements in `shortcuts.xml`. They require the following
attributes, unless noted as optional:

| \`shortcuts.xml\` tag | Contained in | Attributes |
|---|---|---|
| [`<app-widget>`](https://developer.android.com/develop/devices/assistant/widgets#app-widget) | [`<capability>`](https://developer.android.com/guide/app-actions/action-schema#capability) | - `android:identifier` - `android:targetClass` |
| [`<parameter>`](https://developer.android.com/develop/devices/assistant/widgets#parameter) | [`<app-widget>`](https://developer.android.com/develop/devices/assistant/widgets#app-widget) | - See [App Actions schema](https://developer.android.com/guide/app-actions/action-schema#parameter) for attributes. |
| [`<extra>`](https://developer.android.com/develop/devices/assistant/widgets#extra) | [`<app-widget>`](https://developer.android.com/develop/devices/assistant/widgets#app-widget) | - `android:name` (only applicable for TTS) - `android:value` (optional) |

### Widget schema description

#### \<app-widget\>

Top-level widget fulfillment element.

Attributes:

- `android:identifier`: the identifier for this fulfillment. This value must be unique across the `<app-widget>` and `<intent>` fulfillment elements defined within a `<capability>`.
- `android:targetClass`: the full class name of the [`AppWidgetProvider`](https://developer.android.com/reference/android/appwidget/AppWidgetProvider) to handle the intent.

#### \<parameter\>

Maps a BII parameter to an intent `<parameter>` value. You can define zero or
more parameters for each `<app-widget>` element. During fulfillment, Assistant
passes parameters by updating the extras for the widget instance as key-value pairs,
with the following format:

- Key: the `android:key` defined for the parameter.
- Value: the value the BII extracts from a user's voice input.

You access these extras by calling [`getAppWidgetOptions()`](https://developer.android.com/reference/android/appwidget/AppWidgetManager#getAppWidgetOptions(int)) on the associated
`AppWidgetManager` object, which returns a [`Bundle`](https://developer.android.com/reference/android/os/Bundle) containing the name of
the triggering BII and its parameters. See
[Extract parameter values](https://developer.android.com/develop/devices/assistant/widgets#extract_parameters) for details.

For more information on BII parameter matching, see
[Parameter data and matching](https://developer.android.com/guide/app-actions/action-schema#url-templates-in-fulfillment).

#### \<extra\>

Optional tag declaring that a [custom TTS introduction](https://developer.android.com/develop/devices/assistant/widgets#tts) is used for
this widget. This tag requires the following attribute values:

- `android:name`: `"hasTts"`
- `android:value`: `"true"`

### Sample code

The following example from a `shortcuts.xml` file demonstrates a widget
fulfillment configuration for a
[`GET_EXERCISE_OBSERVATION`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/get-exercise-observation) BII capability:

    <capability android:name="actions.intent.GET_EXERCISE_OBSERVATION">
      <app-widget
        android:identifier="GET_EXERCISE_OBSERVATION_1"
        android:targetClass="com.exampleapp.providers.exampleAppWidgetProvider"
        android:targetPackage="com.exampleapp">
        <parameter
          android:name="exerciseObservation.aboutExercise.name"
          android:key="exercisename">
        </parameter>
        <extra android:name="hasTts" android:value="true"/>
      </app-widget>
    </capability>

You can specify multiple `<app-widget>` elements or use a combination of
`<app-widget>` and `<intent>` elements per capability. This approach lets you
provide a customized experience based on different combinations of parameters
provided by users. For example, if the user does not specify a drop-off location
in their query, you can direct them to the activity in your app that shows
options for setting the pick-up and drop-off locations. See the
[Fallback intents](https://developer.android.com/develop/devices/assistant/widgets#guideline_fallback) section for more information
about defining fallback intents.

> [!NOTE]
> **Note:** Assistant fulfills App Actions for capabilities containing multiple fulfillment options by evaluating each fulfillment element in the order it was defined. Assistant fulfills the action by selecting the first fulfillment whose required `<parameter>` values are fully provided in the user query.

#### Extract parameter values

In the following sample `AppWidgetProvider` class, the private function
`updateAppWidget()` is used to extract the BII name and parameters from the
widget options `Bundle`:

### Kotlin

```kotlin
package com.example.exampleapp

//... Other module imports
import com.google.assistant.appactions.widgets.AppActionsWidgetExtension

/**
 * Implementation of App Widget functionality.
 */
class MyAppWidget : AppWidgetProvider() {
    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray
    ) {
        // There might be multiple widgets active, so update all of them
        for (appWidgetId in appWidgetIds) {
            updateAppWidget(context, appWidgetManager, appWidgetId)
        }
    }

    private fun updateAppWidget(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetId: Int
    ) {
        val widgetText: CharSequence = context.getString(R.string.appwidget_text)

        // Construct the RemoteViews object
        val views = RemoteViews(context.packageName, R.layout.my_app_widget)
        views.setTextViewText(R.id.appwidget_text, widgetText)

        // Extract the name and parameters of the BII from the widget options
        val optionsBundle = appWidgetManager.getAppWidgetOptions(appWidgetId)
        val bii = optionsBundle.getString(AppActionsWidgetExtension.EXTRA_APP_ACTIONS_BII) // "actions.intent.CREATE_TAXI_RESERVATION"
        val params = optionsBundle.getBundle(AppActionsWidgetExtension.EXTRA_APP_ACTIONS_PARAMS)
        if (params != null && params.containsKey("dropoff")) {
            val dropoffLocation = params.getString("dropoff")
            // Build your RemoteViews with the extracted BII parameter
            // ...
        }
        appWidgetManager.updateAppWidget(appWidgetId, views)
    }
}
```

### Java

```java
package com.example.exampleapp;

//... Other module imports
import com.google.assistant.appactions.widgets.AppActionsWidgetExtension;

/**
 * Implementation of App Widget functionality.
 */
public class MyAppWidget extends AppWidgetProvider {

    @Override
    public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
        // There might be multiple widgets active, so update all of them
        for (int appWidgetId : appWidgetIds) {
            updateAppWidget(context, appWidgetManager, appWidgetId);
        }
    }

    private static void updateAppWidget(Context context, AppWidgetManager appWidgetManager, int appWidgetId) {

        CharSequence widgetText = context.getString(R.string.appwidget_text);

        // Construct the RemoteViews object
        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.my_app_widget);
        views.setTextViewText(R.id.appwidget_text, widgetText);

        // Extract the name and parameters of the BII from the widget options
        Bundle optionsBundle = appWidgetManager.getAppWidgetOptions(appWidgetId);
        String bii =
                optionsBundle.getString(AppActionsWidgetExtension.EXTRA_APP_ACTIONS_BII); // "actions.intent.CREATE_TAXI_RESERVATION"
        Bundle params =
                optionsBundle.getBundle(AppActionsWidgetExtension.EXTRA_APP_ACTIONS_PARAMS);

        if (params != null && params.containsKey(("dropoff"))){
            String dropoffLocation = params.getString("dropoff");
            // Build your RemoteViews with the extracted BII parameter
            // ...
        }

        appWidgetManager.updateAppWidget(appWidgetId, views);
    }
}
```

## Widgets Extension library

The App Actions Widgets Extension library enhances your widgets for
voice-forward Assistant experiences. This library lets your widgets receive
important fulfillment information from the triggering BII, including the BII
name and any intent parameters extracted from the user query.

This Maven library lets you provide a custom text-to-speech (TTS) introduction
for each widget, enabling Assistant to announce a summary of the content being
visually rendered to users. It also enables [launcher pinning](https://developer.android.com/develop/devices/assistant/widgets#pinning), making
it easy for users to save the widgets displayed in Assistant to their launcher
screens.

Get started by adding the library to the dependencies section of the
`build.gradle` file for your app module:

    dependencies {
        //...
        implementation "com.google.assistant.appactions:widgets:0.0.1"
    }

### Custom introductions

After importing the Widgets Extension library, you can provide custom TTS
introductions for your widgets. To add your definition to the widget's
`AppWidgetProvider`, open the class in your IDE and import the Widgets Extension
library:

### Kotlin

```kotlin
import com.google.assistant.appactions.widgets.AppActionsWidgetExtension
```

### Java

```java
import com.google.assistant.appactions.widgets.AppActionsWidgetExtension;
```
Next, use the library to define your introduction strings and update the widget, as shown in this \`ExampleAppWidget\`:

### Kotlin

```kotlin
package com.example.exampleapp

//... Other module imports
import com.google.assistant.appactions.widgets.AppActionsWidgetExtension

/**
 * Implementation of App Widget functionality.
 */
object MyAppWidget : AppWidgetProvider() {
    fun updateAppWidget(
        context: Context?,
        appWidgetManager: AppWidgetManager,
        appWidgetId: Int
    ) {
        val appActionsWidgetExtension = AppActionsWidgetExtension.newBuilder(appWidgetManager)
            .setResponseSpeech("Hello world") // TTS to be played back to the user
            .setResponseText("Hello world!") // Response text to be displayed in Assistant
            .build()

        // Update widget with TTS
        appActionsWidgetExtension.updateWidget(appWidgetId)

        // Update widget UI
        appWidgetManager.updateAppWidget(appWidgetId, views)
    }
}
```

### Java

```java
package com.example.exampleapp;

//... Other module imports
import com.google.assistant.appactions.widgets.AppActionsWidgetExtension;

/**
 * Implementation of App Widget functionality.
 */
public class MyAppWidget extends AppWidgetProvider {

  static void updateAppWidget(Context context, AppWidgetManager appWidgetManager,
    int appWidgetId) {

    AppActionsWidgetExtension appActionsWidgetExtension = AppActionsWidgetExtension.newBuilder(appWidgetManager)
      .setResponseSpeech("Hello world")  // TTS to be played back to the user
      .setResponseText("Hello world!")  // Response text to be displayed in Assistant
      .build();

      // Update widget with TTS
      appActionsWidgetExtension.updateWidget(appWidgetId);

      // Update widget UI
      appWidgetManager.updateAppWidget(appWidgetId, views);
    }

}
```

### TTS style recommendations

Use the following style recommendations to optimize your custom widget
introductions for TTS and displayed prompts.

| Recommendation | Recommended | Not recommended |
|---|---|---|
| ##### Contractions Use contractions in TTS prompts. Messages without contractions sound stilted and robotic rather than natural and conversational. Speaking words like "cannot" and "do not" can sound punishing and harsh. | **`ResponseSpeech`** (TTS) Sorry, I can't find a reservation. **`ResponseText`** Sorry, I can't find a reservation. | **`ResponseSpeech`** (TTS) Sorry, I cannot find a reservation. **`ResponseText`** Sorry, I cannot find a reservation. |
| ##### Commas Add clarity by using serial commas in lists of three or more items. Without the serial comma, individual items in your list might be incorrectly heard, or read as groups. For example, in "daffodils, daisies and sunflowers," "daisies and sunflowers" sound like they come together. In "daffodils, daisies, and sunflowers," all three are clearly separate. | **`ResponseSpeech`** (TTS) Our most popular ones include yellow roses, daffodils, daisies, and sunflowers. **`ResponseText`** Our most popular ones include yellow roses, daffodils, daisies, and sunflowers. | **`ResponseSpeech`** (TTS) Our most popular ones include yellow roses, daffodils, daisies and sunflowers. **`ResponseText`** Our most popular ones include yellow roses, daffodils, daisies and sunflowers. |
| ##### Numerals Use numerals instead of text to make visual content more glanceable. | **`ResponseSpeech`** (TTS) Your blood pressure is 100 over 80. **`ResponseText`** Your blood pressure is 100/80. | **`ResponseSpeech`** (TTS) Your blood pressure is 100/80. **`ResponseText`** Your blood pressure is one hundred over eighty. |
| ##### Symbols Use specialized symbols instead of text to make visual content more glanceable. | **`ResponseSpeech`** (TTS) Your last purchase was for $24.65. **`ResponseText`** Your last purchase was for $24.65. | **`ResponseSpeech`** (TTS) Your last purchase was for twenty-four dollars and sixty-five cents. **`ResponseText`** Your last purchase was for twenty-four dollars and sixty-five cents. |
| ##### Avoid niceties Niceties make responses feel distant and formal. Ditch them and keep the conversation friendly and informal. | **`ResponseSpeech`** (TTS) Your order has been delivered. **`ResponseText`** Your order has been delivered. | **`ResponseSpeech`** (TTS) Sure, I can tell you that. Your order has been delivered. **`ResponseText`** Sure, I can tell you that. Your order has been delivered. |
| ##### Avoid exclamation points They can be perceived as shouting. | **`ResponseSpeech`** (TTS) You ran 1.5 miles today. **`ResponseText`** You ran 1.5 miles today. | **`ResponseSpeech`** (TTS) You ran 1.5 miles today! **`ResponseText`** You ran 1.5 miles today! |
| ##### Time Use numerals: "5:15," instead of "five-fifteen" or "quarter after five." For the 12-hour clock, use AM or PM. | **`ResponseSpeech`** (TTS) Your delivery should arrive by 8:15 AM. **`ResponseText`** Your delivery should arrive by 8:15 AM. | **`ResponseSpeech`** (TTS) Your delivery should arrive by 15 mins past 8 in the morning today. **`ResponseText`** Your delivery should arrive by 15 mins past 8 in the morning today. |
| ##### Don't launch into monologues Be informative, but keep responses concise. Don't go into heavy-handed details without a clear user benefit. | **`ResponseSpeech`** (TTS) Last month you used 159 hours of energy. **`ResponseText`** Last month you used 159 hours of energy. | **`ResponseSpeech`** (TTS) Saving energy is very important to the planet and environment. Last month you used 159 hours of energy. For this month you've used 58 hours of energy. **`ResponseText`** Saving energy is very important to the planet and environment. Last month you used 159 hours of energy. For this month you've used 58 hours of energy. |
| ##### Use short, simple words Plain and simple language has the broadest appeal, making it accessible to people of all backgrounds. | **`ResponseSpeech`** (TTS) Your last blood sugar reading was 126. **`ResponseText`** Your last blood sugar reading was 126 mg/dL. | **`ResponseSpeech`** (TTS) The penultimate blood glucose level was 126. **`ResponseText`** The penultimate blood glucose level was 126. |

### Launcher pinning

The Widgets Extension library lets the **Add this widget** button be displayed
with your widget in Assistant. To enable pinning, add the following receiver
definition to `AndroidManifest.xml`:

    <application>
      <receiver android:name="com.google.assistant.appactions.widgets.pinappwidget.PinAppWidgetBroadcastReceiver"
        android:exported="false">
        <intent-filter>
          <action android:name="com.google.assistant.appactions.widgets.COMPLETE_PIN_APP_WIDGET" />
        </intent-filter>
      </receiver>
      <service
        android:name=
        "com.google.assistant.appactions.widgets.pinappwidget.PinAppWidgetService"
        android:enabled="true"
        android:exported="true">
        <intent-filter>
          <action
            android:name="com.google.assistant.appactions.widgets.PIN_APP_WIDGET" />
        </intent-filter>
      </service>
    </application>

## Inventory availability

BIIs supporting [inline inventory](https://developer.android.com/guide/app-actions/inline-inventory) or [web inventory](https://developer.android.com/guide/app-actions/web-inventory) can extend these
inventories to your widget fulfillments.

#### Inline inventory

The following code from a sample `shortcuts.xml` file demonstrates a
[`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII capability
configured for inline inventory and widget fulfillment:

    <capability
      android:name="actions.intent.START_EXERCISE">
      <app-widget
        android:identifier="START_EXERCISE_1"
        android:targetClass="com.example.exampleapp.StartExerciseAppWidgetProvider">
        <parameter
          android:name="exercise.name"
          android:key="exerciseName"
          app:shortcutMatchRequired="true">
        </parameter>
      </app-widget>
    </capability>

    <shortcut android:shortcutId="RunningShortcut">
      <intent
        android:action="android.intent.action.VIEW"
        android:targetClass="com.example.exampleapp.StartExcerciseActivity" />
      <capability-binding
        android:capability="actions.intent.START_EXERCISE"
        android:parameter="exercise.name"
        android:value="running;runs" />
    </shortcut>

In the preceding sample, when a user triggers this capability by asking
Assistant, *"Start running with ExampleApp,"* the option bundle for the
`<app-widget>` fulfillment contains the following key-value pair:

- Key = `"exerciseName"`
- Value = `"RunningShortcut"`

#### Web inventory

The following code from a sample `shortcuts.xml` file shows a capability
enabled for web inventory and widget fulfillment:

    <shortcuts>
      <capability
        android:name="actions.intent.START_EXERCISE">
        <app-widget
          android:identifier="START_EXERCISE_1"
          android:targetClass="com.example.exampleapp.CreateTaxiAppWidgetProvider">
          <parameter
            android:name="exercise.name"
            android:key="exerciseName"
            android:mimeType="text/*">
            <data android:pathPattern="https://exampleapp.com/exercise/.*" />
          </parameter>
        </app-widget>
      </capability>
    </shortcuts>

## Test App Actions

Use the App Actions Test Tool, a feature of the [Google Assistant plugin for
Android Studio](https://developer.android.com/guide/app-actions/test-tool), to test widgets on a physical or virtual device. To use
the test tool, follow these steps:

1. Connect your test device with your app running.
2. In Android Studio, go to **Tools** \> **App Actions** \> **App Actions Test
   Tool**.
3. Click **Create preview**.
4. Using Android Studio, run your app on your test device.
5. Use the Assistant app on your test device to test your App Action. For example, you can say something like *"Hey Google, how many miles have I run
   this week on ExampleApp?"*
6. Observe the behavior of your app, or use the [Android Studio debugger](https://developer.android.com/studio/debug), to verify the desired action result.

## Quality guidelines

This section highlights key requirements and best practices when
you integrate App Actions with widgets.

#### Content in widgets

- (**Required**) Do not show ads in your widgets.
- Focus widget content completely on fulfilling the intent. Don't try to fulfill multiple intents with one widget or add irrelevant content.

#### Handle authentication

- (**Required**) Where user authentication is needed to complete a user flow, return a widget that explains that the user needs to continue in the app. Inline user authentication in Google Assistant is not supported for App Actions.
- If users permit your app to show data using widgets, you can return an error widget at runtime for unauthorized users.

#### Fallback intents

- (**Required** ) In your `shortcuts.xml`, always provide a fallback
  `<intent>` in addition to your widget fulfillment for a
  given capability. A fallback intent is an `<intent>` element with no required
  `<parameter>` values.

  This enables Assistant to fulfill an action when
  the user query does not contain parameters required by the other fulfillment
  elements defined in the capability. The exception to this is when there are no
  required parameters for that capability, in which case only the widget
  fulfillment is needed.
- Use the fallback intent to open your app to the relevant screen,
  not the home screen.

The following code from a sample `shortcuts.xml` file demonstrates a
`<capability>` with a fallback `<intent>` supporting a primary
`<app-widget>` fulfillment:

    <shortcuts>
      <capability
        android:name="actions.intent.CREATE_TAXI_RESERVATION">
        <!-- Widget with required parameter, specified using the "android:required" attribute. -->
        <app-widget
          android:identifier="CREATE_TAXI_RESERVATION_1"
          android:targetClass="com.example.myapplication.CreateTaxiAppWidgetProvider">
          <parameter
            android:name="taxiReservation.dropoffLocation.name"
            android:key="dropoff"
            android:required="true">
          </parameter>
        </app-widget>
        <!-- Fallback intent with no parameters required to successfully execute. -->
        <intent
          android:identifier="CREATE_TAXI_RESERVATION_3"
          android:action="myapplication.intent.CREATE_TAXI_RESERVATION_1"
          android:targetClass="com.example.myapplication.TaxiReservationActivity">
        </intent>
      </capability>
    </shortcuts>

## Google Play data disclosure

This section lists the end-user data collected by the latest version of the
Widgets Extension library.

This SDK sends developer-provided text-to-speech (TTS) responses that are
announced to the user by Google Assistant using Assistant's speech
technology. This information is not stored by Google.

[App actions](https://developer.android.com/guide/app-actions/overview) might also
collect client app metadata for the following purposes:

- To monitor adoption rates of different SDK versions.
- To quantify SDK feature usage across apps.

*** ** * ** ***