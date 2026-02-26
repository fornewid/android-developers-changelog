---
title: https://developer.android.com/develop/devices/assistant/overview
url: https://developer.android.com/develop/devices/assistant/overview
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

Google Assistant enables voice-forward control of Android apps. Using
Assistant, users can launch apps, perform tasks, access content, and more by
using their voice to say things like, *"Hey Google, start a run on
Example App."*

As an Android developer, you can use Assistant's development framework and
testing tools to easily enable deep voice control of your apps on
Android-powered surfaces, such as mobile devices, cars, and wearables.
[Video](https://www.youtube.com/watch?v=DozT--NclbM)

## App Actions

Assistant's App Actions let users launch and control Android apps with
their voice.

<br />


<br />


<br />


<br />

> [!TIP]
> **Try it out:** Have an app published to the Play Store on your device? Launch it by telling Assistant, *"Hey Google, open AppName."* Assistant can open your app with no integration work required from you.

App Actions enable deeper voice control, enabling users to launch your apps and
perform tasks like:

- **Launching features from Assistant**: Connect your app's capabilities to user queries that match predefined semantic patterns or built-in intents.
- **Displaying app information on Google surfaces** : Provide [Android widgets](https://developer.android.com/guide/app-actions/widgets) for Assistant to display, offering inline answers, simple confirmations, and brief interactions to users without changing context.
- **Suggesting voice shortcuts from Assistant**: Use Assistant to proactively suggest tasks in the right context for users to discover or replay.

App Actions use [built-in intents](https://developer.android.com/reference/app-actions/built-in-intents) (BIIs) to enable these and dozens more use
cases across popular task categories. See the [App Actions](https://developer.android.com/develop/devices/assistant/overview#app_actions)
overview on this page for details on supporting BIIs in your apps.

### Multidevice development

You can use App Actions to provide voice-forward control on device surfaces
beyond mobile. For example, with BIIs optimized for Auto use cases, drivers
can perform the following tasks using their voice:

- [Navigate to the nearest restaurant on their driving route](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-local-business)
- [Find the closest parking garage](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-parking-facility)
- [Locate nearby EV charging stations](https://developer.android.com/reference/app-actions/built-in-intents/travel/get-charging-station)

## App Actions overview

You use App Actions to offer deeper voice control of your apps to users by
enabling them to use their voice to perform specific tasks in your app. If a
user has your app installed, they can simply state their intent using a phrase
that includes your app name, such as *"Hey Google, start an exercise on
Example App."* App Actions supports BIIs that model the common ways users
express tasks they want to accomplish or information they seek, such as:

- Start an exercise, send messages, and other category specific actions.
- Opening a feature of your app.
- Querying for products or content using in-app search.

With App Actions, Assistant can proactively suggest your voice capabilities as
shortcuts to users, based on the user's context. This functionality enables
users to easily discover and replay your App Actions. You may also suggest these
shortcuts in your app with the App Actions [in-app promo SDK](https://developer.android.com/guide/app-actions/in-app-promo-sdk).

You enable support for App Actions by declaring `<capability>` tags in
`shortcuts.xml`. Capabilities tell Google how your in-app functionality can be
semantically accessed using BII and enable voice support for your features.
Assistant fulfills user intents by launching your app to
the specified content or action. For some use cases, you can specify an Android
widget to display within Assistant to fulfill the user query.

App Actions are supported on Android 5 (API level 21) and higher. Users can only
access App Actions on Android phones. Assistant on Android Go does not
support App Actions.


> [!NOTE]
> **Note:** App Actions, like all Actions that support built-in intents, trigger on a number of factors, including quality and relevancy to the user's request. Based on those factors, Google may exercise discretion in surfacing your Action in response to user requests.

<br />

## How App Actions work

App Actions extend your in-app functionality to Assistant, enabling users to
access your app's features by voice. When a user invokes an App Action,
Assistant matches the query to a BII declared in your `shortcuts.xml` resource,
launching your app at the requested screen or displaying an Android widget.

You declare BIIs in your app using Android [capability elements](https://developer.android.com/guide/topics/ui/shortcuts/adding-capabilities). When you
upload your app using the [Google Play console](https://play.google.com/console), Google registers the
capabilities declared in your app and makes them available for users to access
from Assistant.

> [!NOTE]
> **Note:** The [Built-in intents reference](https://developer.android.com/reference/app-actions/built-in-intents) offers BIIs across several functional categories, or "verticals," making it simple for developers to enable voice control of their app by matching their app shortcuts to supported voice intents.

For example, you might provide a capability for starting exercise in your app.
When a user says, *"Hey Google, start a run on Example App,"* the following
steps occur:

- Assistant performs natural language analysis on the query, matching the semantics of the request to the predefined pattern of a BII. In this case, the [`actions.intent.START_EXERCISE`](https://developer.android.com/reference/app-actions/built-in-intents/health-and-fitness/start-exercise) BII matches the query.
- Assistant checks whether the BII was previously registered for your app and uses that configuration to determine how to launch it.
- Assistant generates an Android intent to launch the in-app destination of the request, using information you provide in the `<capability>`. Assistant extracts the parameters of the query and passes them as extras in a generated Android intent.
- Assistant fulfills the user request by launching the generated Android intent. You configure the `intent` to launch a screen in your app or to display a widget within Assistant.

![When a user provides a query to Google Assistant, Assistant responds
by launching an app destination for the user.](https://developer.android.com/static/guide/app-actions/images/assistant-flow.png) **Figure 1.** Example App Actions user query flow.

> [!NOTE]
> **Note:** App Actions generate intents that are used to launch in-app destinations to fulfill user requests. An intent can specify either an explicit Android `Activity` or an Android [deep link](https://developer.android.com/training/app-links/deep-linking) that launches an `Activity`. Apps with navigation built around Android deep links may prefer to use these links to fulfill an action. For more information, see [Create Shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema).

After a user completes a task, you use the
[Google Shortcuts Integration Library](https://developer.android.com/guide/app-actions/dynamic-shortcuts) to push a dynamic shortcut of the
action and its parameters to Google, enabling Assistant to suggest the
shortcut to the user at contextually relevant times.

Using this library makes your shortcuts eligible for discovery and replay on
Google surfaces, like Assistant. For instance, you might push a shortcut to
Google for each destination a user requests in your ride sharing app for
quick replay later as a shortcut suggestion.

## Build App Actions

App Actions build on top of existing functionality in your Android app. The
process is similar for each App Action you implement. App Actions take users
directly to specific content or features in your app using `capability` elements
you specify in `shortcuts.xml`.

When you build an App Action, the first step is to identify the activity you
want to allow users to access from Assistant. Then, using that information,
find the closest matching BII from the
[App Actions BII reference](https://developer.android.com/reference/app-actions/built-in-intents).

BIIs model some of the common ways that users express tasks they
want to do using an app or information they seek. For example, BIIs exist for
actions like starting an exercise, sending a message, and searching within an
App. BIIs are the best way to start with App Actions, as they model common
variations of user queries in multiple languages, making it easy for you to
quickly voice enable your app.

Once you identify the in-app functionality and BII to implement, you add or
update the `shortcuts.xml` resource file in your Android app that maps the BII
to your app functionality. App Actions defined as `capability` elements in
`shortcuts.xml` describe how each BII resolves its fulfillment, as well as
which parameters are extracted and provided to your app.

> [!NOTE]
> **Note:** For cases where there isn't a BII for your app functionality, you can use a [custom intent](https://developer.android.com/guide/app-actions/custom-intents) to extend your app with App Actions.

A significant portion of developing App Actions is mapping BII parameters into
your defined fulfillment. This process commonly takes the form of mapping the
expected inputs of your in-app functionality to a BII's semantic parameters.

> [!NOTE]
> **Note:** If your app [exports its activities](https://developer.android.com/guide/topics/manifest/activity-element#exported) by allowing other on-device apps to invoke the exported activity, Assistant may automatically use these intents to bootstrap your app's support for Assistant queries. You can override this behavior by implementing your own App Actions as covered in this section or opt out using the [App Actions support form](https://developer.android.com/guide/app-actions/app-actions-support).

## Test App Actions

During development and testing, you use the [Google Assistant plugin](https://developer.android.com/guide/app-actions/test-tool) for
Android Studio to create a preview of your App Actions in Assistant for your
Google Account. This plugin helps you test how your App Action handles various
parameters prior to submitting it for deployment. Once you generate a preview of
your App Action in the test tool, you can trigger an App Action on your test
device directly from the test tool window.

## Media apps

Assistant also offers built-in capabilities to understand media app commands, like
*"Hey Google, play something by Beyonce,"* and supports media controls like
*pause* , *skip* , *fast forward* , and *thumbs up*.

## Next steps

Follow the [App Actions pathway](https://developers.google.com/learn/pathways/app-actions) to build an App Action using our sample
Android app. Then, continue on to our guide to
[build App Actions for your own app](https://developer.android.com/guide/app-actions/get-started). You can also explore
these additional resources for building App Actions:

- Download and explore our [sample fitness Android app on GitHub](https://github.com/actions-on-google/appactions-fitness-kotlin).
- [r/GoogleAssistantDev](https://www.reddit.com/r/GoogleAssistantDev): The official Reddit community for developers working with Google Assistant.
- If you have a programming question about App Actions, submit a post to [Stack Overflow](https://stackoverflow.com/questions/tagged/app-actions) using the "android" and "app-actions" tags. Before posting, ensure your question is [on topic](https://stackoverflow.com/help/on-topic) and that you've read the guidance for [how to ask a good question](https://stackoverflow.com/help/how-to-ask).
- Report bugs and general issues with App Actions features in our [public issue tracker](https://issuetracker.google.com/issues/new?component=617864&template=1257475).

*** ** * ** ***