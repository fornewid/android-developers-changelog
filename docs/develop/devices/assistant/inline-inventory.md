---
title: https://developer.android.com/develop/devices/assistant/inline-inventory
url: https://developer.android.com/develop/devices/assistant/inline-inventory
source: md.txt
---

When you implement App Actions for your Android app, you might find yourself
having to handle requests that are variations on a theme. For example, say your
fitness app implements the [`START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) built-in intent (BII) to let
users start a wide range of workouts by asking Assistant things like,
*"Hey Google, start a run on Example App."*

Fulfilling this intent requires your request matching logic to handle each
type of workout, including variations like "jog," "sprint," or "race."
This logic quickly becomes cumbersome as supported workouts increase.

For supported BIIs, like `START_EXERCISE`, you can avoid this complex matching
logic by using an inline inventory. An inline inventory is a set of static
Android shortcuts defined in `shortcuts.xml` representing features and content
in your app.

Each shortcut contains an item identifier and a list of synonyms
representing variations in how users might refer to the item. During invocation,
the BII compares the user-provided BII parameter to the synonym list. When a
match is found, the BII parameter is updated to the matching shortcut's item
identifier.

An inline inventory lets Google Assistant simplify the BII parameter
values provided to your application during App Action invocations.

Inline inventories function like lookup tables for BII parameters,
expressing the variety of ways users refer to features or content in your app
using item identifiers that you define. They simplify your app's request matching
logic by letting your fulfillments anticipate item identifiers from BII
parameters.

<br />

![Inline inventory user flow diagram](https://developer.android.com/static/guide/app-actions/images/appactions-inline-inventory-flow.png) **Figure 1.** A flow diagram of a `START_EXERCISE` capability that uses an inline inventory to interpret user-provided workout names for supported exercise types in the app.

<br />

| **Note:** Inline inventory is supported by specific parameters of certain BIIs. For details, refer to each BII's "Inventory availability by field" section in the [BII reference](https://developer.android.com/reference/app-actions/built-in-intents).

## Limitations and alternatives

Inline inventory shortcuts have the following limitations:

- **Shortcut limit:** A maximum of 1,000 inline inventory shortcuts can be defined per app.
- **Synonym limit:** Each inline inventory shortcut can contain a maximum of 20 synonym values.
- **Static definition:** Inline inventory shortcuts are statically declared in `shortcuts.xml` and can only be updated for your users by publishing a new version of your app.

Given the requirement for static configuration, an inline inventory is best
suited to extending infrequently changing, non-personalized app information to
Assistant, such as menu items, bus routes, or drink sizes. For other types of
content, consider these alternatives:

- [**Web inventory:**](https://developer.android.com/guide/app-actions/web-inventory) lets Assistant query public web content when
  matching user queries to supported app content identifiers. Web inventory
  queries occur in real time during an invocation, letting you extend
  product catalogs, social media posts, and other frequently updating content
  to Assistant.

- [**Dynamic shortcuts:**](https://developer.android.com/guide/app-actions/dynamic-shortcuts) extend an inventory of personalized app content
  to Assistant. Dynamic shortcuts let users quickly replay common
  actions, like reordering their favorite drink from a food ordering app or
  pulling up a shopping list in a note taking app.

## Create an inline inventory

An inline inventory simplifies development by giving Assistant a handy way to
translate the different ways users request your app's content and features
into the predictable identifiers that are expected by your application. For
example, suppose your app offers different workouts that users can start using
their voice, and your app expects users to make the following requests for the
same exercise type:

- *Hey Google, start a run on Example App.*
- *Hey Google, start a jog on Example App.*

In your inline inventory shortcut, you set the `shortcutId` to `"CARDIO_RUN"`,
the exercise identifier expected by your app. You then specify "run" and
"jog" as synonyms associated to the `shortcutId`. Then, when a user triggers
your App Action with the preceding queries, Assistant uses the identifier
`"CARDIO_RUN"` for the BII parameter when generating a fulfillment intent.

The following snippet from a sample `app/res/shortcuts.xml` file implements
this case:

    <capability android:name="actions.intent.START_EXERCISE">
      <intent
        android:targetPackage="com.example.myapp"
        android:targetClass="com.example.myapp.ExerciseActivity">
        <parameter android:name="exercise.name" android:key="exercise" />
      </intent>
    </capability>

    <shortcut android:shortcutId="CARDIO_RUN">
      <capability-binding android:key="actions.intent.START_EXERCISE">
        <parameter-binding
          android:key="exercise.name"
          android:value="@array/run_names" />
        </capability-binding>
    </shortcut>

In the preceding sample, the inline inventory `shortcut` declares a
[`<parameter-binding>`](https://developer.android.com/guide/app-actions/action-schema#parameter-binding) tag within a [`<capability-binding>`](https://developer.android.com/guide/app-actions/action-schema#capability-binding) element,
binding it to the `exercise.name` BII parameter defined in the
[`<capability>`](https://developer.android.com/guide/app-actions/action-schema#capability).

The string array resource `@array/run_names` specifies a list of synonyms in
`res/values/arrays.xml` that Assistant recognizes and maps to the
`"CARDIO_RUN"` item ID:

    <!-- Synonym values for "CARDIO_RUN" inline inventory -->
    <resources>
      <string-array name="run_names">
        <item>Run</item>
        <item>Jog</item>
        <item>Sprint</item>
      </string-array>
    </resources>

When a [`<url-template>`](https://developer.android.com/guide/app-actions/action-schema#url-template) is provided for the capability, the `shortcutId` for
a matching value is inserted in the generated URL at the corresponding
placeholder for the parameter. The following code from a sample
`app/res/shortcuts.xml` file implements this case:

    <capability android:name="actions.intent.START_EXERCISE">
      <intent>
        <url-template android:value="myapp://workout{?exercise}" />
        <parameter android:name="exercise.name" android:key="exercise" />
      </intent>
    </capability>

    <shortcut android:shortcutId="CARDIO_RUN">
      <capability-binding android:key="actions.intent.START_EXERCISE">
        <parameter-binding
          android:key="exercise.name"
          android:value="@array/run_names" />
      </capability-binding>
    </shortcut>

In the preceding sample, Assistant generates the fulfillment deep link
`myapp://workout?exercise=CARDIO_RUN`.
| **Note:** Inline inventory supports a maximum of one `parameter` per fulfillment `intent` element of a `capability`.

## Fulfillment using shortcut intents

By default, a shortcut provides the `shortcutId` of a matching inline inventory
value to the `intent` of the `capability` the shortcut is bound to, as declared
in the shortcut's [`<capability-binding>`](https://developer.android.com/guide/app-actions/action-schema#capability-binding) tag. You can
alternately specify that an `intent` defined in the shortcut itself be used for
fulfillment by adding a [`<shortcut-fulfillment>`](https://developer.android.com/guide/app-actions/action-schema#shortcut-fulfillment) tag to the `capability`.

The following code from a sample `app/res/shortcuts.xml` file implements
shortcut fulfillment:

    <capability android:name="actions.intent.START_EXERCISE">
      <shortcut-fulfillment>
        <parameter android:name="exercise.name"/>
      </shortcut-fulfillment>
    </capability>

    <shortcut android:shortcutId="CARDIO_RUN">
      <capability-binding android:key="actions.intent.START_EXERCISE">
        <parameter-binding
          android:key="exercise.name"
          android:value="@array/run_names" />
      </capability-binding>
      <intent android:targetPackage="com.example.myapp"
        android:targetClass="com.example.myapp.ExerciseActivity">
        <parameter android:name="exercise.name" android:key="exercise" />
      </intent>
    </shortcut>

In the preceding sample, if the user query matches an inline inventory value
for the `exercise.name` parameter, the `<shortcut-fulfillment>` tag
specifies that the `intent` of the bound shortcut is used for fulfillment.
| **Note:** Each inline inventory `<shortcut>` intended for shortcut fulfillment must contain a fulfillment `<intent>`. To avoid fulfillment errors, don't use shortcuts that don't contain intent elements for shortcut fulfillment.

## Inline inventory for open app feature BII

While inline inventory is generally an optional capability for the BIIs that
support it, it is required for certain BIIs, like [`OPEN_APP_FEATURE`](https://developer.android.com/reference/app-actions/built-in-intents/common/open-app-feature). This
commonly used BII lets users deep-link into specific app features
using Assistant.
The open app feature BII requires an inline inventory of app feature names to
verify that a user-requested feature exists before deep-linking the user into
your app.

The following code from a sample `app/res/shortcuts.xml` file implements this
BII with a single shortcut representing the app's order status feature:

    <capability android:name="actions.intent.OPEN_APP_FEATURE">
      <intent
        android:targetPackage="com.example.myapp"
        android:targetClass="com.example.myapp.MyClass">
        <parameter
           android:name="feature"
           android:key="featureParam" />
      </intent>
      <!-- Required fallback fulfillment to handle when parameters are missing from user query. -->
      <intent
        android:targetPackage="com.example.myapp"
        android:targetClass="com.example.myapp.MyClass">
        <parameter
           android:name="HOME_SCREEN"
           android:key="featureParam" />
      </intent>
    </capability>

    <!-- Inline inventory for OPEN_APP_FEATURE. -->

    <shortcut android:shortcutId="ORDER_STATUS">
      <capability-binding android:key="actions.intent.OPEN_APP_FEATURE">
        <parameter-binding
          android:key="feature"
          android:value="@array/order_status_names" />
        </capability-binding>
    </shortcut>

The string array resources in `res/values/arrays.xml`,
`@array/order_status_names`, specifies a list of
synonyms for this feature:

    <resources>
      <string-array name="order_status_names">
        <item>Order status</item>
        <item>Orders</item>
        <item>Order history</item>
      </string-array>
    </resources>

With the preceding capability in place, Assistant can fulfill a variety of
phrases for the same feature:

- *"Hey Google, show my order status on Example App."*
- *"Hey Google, show my orders on Example App."*
- *"Hey Google, show my order history on Example App."*

## Test inline inventory

Test your inventory by inspecting the BII parameter values Assistant provides to
your application while fulfilling relevant App Action capabilities. An inline
inventory works by replacing the user-provided value of an inventory-bound BII
parameter with the `shortcutId` of a matching inline inventory shortcut.

For
example, a `START_EXERCISE` BII capability might use an inline inventory to
translate the user-provided BII parameter "run" to its corresponding exercise
ID, `"CARDIO_RUN"`.

The [Google Assistant Plugin](https://developer.android.com/guide/app-actions/test-tool) lets you preview your inline inventory App
Actions in Assistant on a test device. Test your inventory using the plugin by
following these steps:

1. [Configure](https://developer.android.com/guide/app-actions/test-tool#configure_a_built-in_intent) the inventory-bound parameters of your BII capability with synonym values associated to your inline inventory.
2. [Trigger](https://developer.android.com/guide/app-actions/test-tool#trigger_app_actions) the BII from the plugin, invoking it on your test device.
3. Inspect the resulting parameter values Assistant provides to your application during App Action fulfillment.