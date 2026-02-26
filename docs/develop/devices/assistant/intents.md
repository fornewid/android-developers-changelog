---
title: https://developer.android.com/develop/devices/assistant/intents
url: https://developer.android.com/develop/devices/assistant/intents
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

Built-in intents (BIIs) allow your app to express its fulfillment capabilities
to Google. By declaring capabilities in your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file and
mapping intent parameters to the fulfillment, you make it possible for
Google Assistant to launch your app to a specific screen in response to a
query, so the user can complete a task.
[Video](https://www.youtube.com/watch?v=UsipIqcw3y4)

Built-in intents are grouped according to app categories. Each category
represents a set of common tasks that users frequently want to perform on their
apps. The full list of available BIIs, their parameters, and example
queries usable for testing is in the [built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents).

Many BIIs have specific deployment requirements and
recommendations. These requirements and recommendations help your app deliver
the best possible experience to your users.
![](https://developer.android.com/static/guide/app-actions/images/Fitness1.png) **Figure 1.** Invoke the `START_EXERCISE` BII with a voice query to Assistant. ![](https://developer.android.com/static/guide/app-actions/images/Fitness3.png) **Figure 2.** Launch the app to a specific screen to begin the `START_EXERCISE` task. ![](https://developer.android.com/static/guide/app-actions/images/Fitness4-widget.png) **Figure 3.** Display a [widget](https://developer.android.com/guide/app-actions/widgets) in response to a query.

## ​

## Implement BIIs and handle intent parameters

For App Actions, you declare capabilities and handle BII parameters
in your [shortcuts.xml](https://developer.android.com/guide/app-actions/action-schema) file. To implement a BII and handle its
parameters, follow these steps:

1. Declare the `capability` with the chosen BII.
2. Add nested `parameter` elements for each BII field you want to add.
   1. If you use `targetClass` or `targetPackage`, map them to the Android intent `extras` using a name you choose.
   2. If you use a deep link URL, use the named parameters in the query string of the URL template.

To handle a BII parameter, map the BII parameter to the
corresponding parameter of an explicit Android intent in your `capability`.
Then, you can use its value in your app. Your app is not required to handle
BII parameters. However, do attempt to handle data fields marked as "Recommended"
in the [built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents).

You can define multiple intent fulfillments, each with its own set of
recommended parameters. Google selects the appropriate fulfillment based on the
capability parameters it identifies from the user's query and the ones declared
in an intent.

For example, the [`actions.intent.START_EXERCISE`](https://developer.android.com/reference/app-actions%20built-in-intents/health-and-fitness/start-exercise)
intent recommends that your app handle the `exercise.name` BII parameter, but you
can implement the BII in your app with no parameters.
You might do this if you want to handle user queries without the specific
exercise name, like *"Ask Example App to start tracking exercise."*

The
following snippet has a fallback to a fulfillment with no required parameters
if the parameters are not included in the user's query:

    <?xml version="1.0" encoding="utf-8"?>
    <shortcuts xmlns:android="http://schemas.android.com/apk/res/android">

        <capability android:name="actions.intent.START_EXERCISE">
            <intent
                android:action="android.intent.action.VIEW"
                android:targetClass="com.example.myapplication.Activity1"
                android:targetPackage="com.example.myapplication">
                <parameter
                    android:name="exercise.name"
                    android:key="exerciseType"
                    android:required="true"
                    />
            </intent>
            <intent
                android:action="android.intent.action.VIEW"
                android:targetClass="com.example.myapplication.Activity2">
            </intent>
        </capability>
    </shortcuts>

Google Assistant does its best to provide the most relevant information to
the user when returning parameter values to your app. For example, user queries
for ordering pizza from Example Restaurant's mobile app don't always include a
location. To better serve the user, Assistant might provide the latitude
and longitude values of the nearest Example Restaurant to that app.

As an additional requirement, you don't want your app to directly perform an
action that modifies a user's real-world state (for example, transferring
money, placing an order, or sending a message) without first confirming the
action with the user.


> [!NOTE]
> **Note:** App Actions, like all Actions that support built-in intents, trigger on a number of factors, including quality and relevancy to the user's request. Based on those factors, Google may exercise discretion in surfacing your Action in response to user requests.

<br />

## Disambiguation

Arguments passed to your app via `<url-parameter>` or intent extras might not
uniquely identify the item that you want to show to the user. In this case,
use the argument value as a search argument and take the user to the search
page of the app. They can disambiguate and choose the right item.

For example, if a user's query is *"Order from Example Restaurant"* for the
BII `ORDER_MENU_ITEM`, you can present to the user a list of
restaurants whose names match the term `"Example Restaurant"`.

## Language and locale support

The locales supported for development and testing by each App Action BII
are listed in the [built-in intent reference](https://developer.android.com/reference/app-actions/built-in-intents). Some BIIs have different
locale support for developer testing and for user triggering from Assistant.