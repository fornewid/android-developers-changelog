---
title: https://developer.android.com/develop/ui/views/launch/shortcuts/adding-capabilities
url: https://developer.android.com/develop/ui/views/launch/shortcuts/adding-capabilities
source: md.txt
---

Capabilities in `shortcuts.xml` let you declare the types of actions users can
take to launch your app and directly perform a specific task.

For example, Google Assistant App Actions use capabilities to let developers
extend in-app features to [built-in intents](https://developers.google.com/assistant/app/intents) (BIIs), letting users activate
and control those features using spoken commands. A capability consists of the
name of the action and an `intent` targeting the destination in your app that
resolves the user intent.

## Define capabilities in shortcuts.xml

You define `capability` elements in a `shortcuts.xml` resource file in your
Android app development project. To define a `capability` element, do the
following:

1. Create a `shortcuts.xml` resource by following the instructions in [Create
   static shortcuts](https://develop/ui/views/launch/shortcuts/creating-shortcuts#static).
2. Include the following required information in your capability:

   - **Capability name:** the action you want your app to support. Refer to
     the component documentation for the feature that requires capability
     definitions. App Actions voice-enabled commands use the BII `Action ID`
     for capability names, which you can find in [BII reference](https://developers.google.com/assistant/app/reference/built-in-intents). For example,
     the [`GET_THING`](https://developers.google.com/assistant/app/reference/built-in-intents/common/get-thing) BII lists its `Action ID` as `actions.intent.GET_THING`.

   - **App destination:** the destination in your app the action launches to
     fulfill the user request. Define app destinations using `intent` elements
     nested within the `capability`.

   - **Parameter mappings:** each `intent` might contain parameters to be
     passed as `extra` data of the intent. For example, each App Actions BII
     includes fields representing information users often provide in queries that
     trigger the BII.

The following example demonstrates a capability definition in `shortcuts.xml`
for [`actions.intent.START_EXERCISE`](https://developers.google.com/assistant/app/reference/built-in-intents/health-and-fitness/start-exercise), a BII that lets users use spoken
commands with Assistant to begin a workout in a fitness app:  

    <shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
      <capability android:name="actions.intent.START_EXERCISE">
        <intent
          android:action="android.intent.action.VIEW"
          android:targetPackage="com.example.sampleApp"
          android:targetClass="com.example.sampleApp.ExerciseActivity">
          <parameter
            android:name="exercise.name"
            android:key="exerciseType"/>
        </intent>
      </capability>
    </shortcuts>

In the preceding example, the `<capability>` `android:name` attribute refers to
the `START_EXERCISE` BII. If a user invokes this BII by asking Assistant, *"Hey
Google, start a run in ExampleApp,"* Assistant fulfills the user request using
information provided in the nested `intent` element. The `intent` in this sample
defines the following details:

- The `android:targetPackage` sets the target application package for this intent.
- The `android:targetClass` field specifies the destination activity: `com.example.sampleApp.ExerciseActivity`.
- The intent `parameter` declares support for a BII parameter [`exercise.name`](https://developers.google.com/assistant/app/reference/built-in-intents/health-and-fitness/start-exercise#recommended-fields) and how to pass the parameter value---collected from the user---as extra data in the `intent`.

## Associate shortcuts with a capability

Once you define a capability, you can extend its functionality by associating
static or dynamic shortcuts with it. How shortcuts are linked to a `capability`
depends on the feature being implemented and the actual words included in a
user's request. For example, when a user begins a run in your fitness tracking
app by asking Assistant, *"Hey Google, start a run in ExampleApp."* Assistant
can use a shortcut to launch an instance of a `capability` that defines a valid
exercise entity of "run" for the `exercise.name` parameter.

For more information about associating shortcuts to App Actions, see [App
Actions overview](https://developers.google.com/assistant/app).