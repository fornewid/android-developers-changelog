---
title: https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows
url: https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows
source: md.txt
---

# Plan task flows

Help drivers focus on the road by minimizing the amount of time they need to interact with their screen. You can do this by choosing the templates best suited for each task and keeping task flows short.

While the templates in the app library are designed for usability while driving (except those that are parked only), keeping task flows to 5 steps or fewer helps to minimize distraction.

As you design your flows, make sure you understand how to:

- **Count steps** ([Step counts and refreshes](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#steps-refreshes))
- **Sequence templates appropriately** ([Template order in task flows](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#order))
- **Gain flexibility in task length** through[Adaptive task limits](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#task-limits), a feature that allows task flows greater than 5 steps under certain circumstances
- **Use template features that promote task efficiency** , such as[interactive maps](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#maps)(features are detailed in the[Templates](https://developer.android.com/design/ui/cars/guides/templates/overview)section)

## Keeping task flows short

To minimize driver distraction, keep task flows as short as possible.
![Mock-up of sample task flow](https://developer.android.com/static/images/design/ui/cars/foundations/plan-task-flow-sample.png)Sample task flow with a subflow

A new task starts when the user performs any of the following actions:

- Lands on (or returns to) the app's landing template
- Chooses an action that opens another app
- Lands on the[Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template)(in navigation apps)

To minimize required driver attention, keep task flows to 3 steps or fewer when possible (4 steps or fewer for[flows involving purchases](https://developer.android.com/design/ui/cars/guides/flows/purchase)). When flows are longer than 3 or 4 steps, consider providing shortcuts back to earlier steps.

Except as noted in[Step counts and refreshes](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#steps-refreshes), the limit is 5 steps, including the starting and ending steps.
| **Note:** Exceeding 5 steps for a task is possible only if the[Adaptive task limits](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#task-limits)feature is enabled.

## Template order in task flows

When creating task flows, keep the following template ordering considerations in mind:

- **Avoid List and Grid templates for step 5.** If the flow involves 5 steps, the final step must not be a list- or grid-based template (examples of acceptable templates include[Navigation](https://developer.android.com/design/ui/cars/guides/templates/navigation-template),[Message](https://developer.android.com/design/ui/cars/guides/templates/message-template), and[Pane](https://developer.android.com/design/ui/cars/guides/templates/pane-template)).
- **Don't put 5 Lists or Grids in a row.**Apps should not create flows with 5 list-based or grid-based templates in a row, even if one of those templates is in a subflow.

## Step counts and refreshes

To design task flows that don't exceed the 5-step limit, it's important to understand how steps are counted for each flow.

The step count**increases by 1**whenever one of the following occurs:

- A new template is shown
- The same template is shown with new content -- unless the new content is a refresh of existing content, as defined in[What is a refresh?](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#refresh)

The step count**decreases by 1**if the task returns to the previous view with the same content.
![Wireframe of sample task flow with new template](https://developer.android.com/static/images/design/ui/cars/foundations/step-count-new-template.png)In both of these examples, a step is added as the user browses and selects a place from the Place List.

For more examples of how step counts would be incremented in specific task flows, see[Sample flows](https://developer.android.com/design/ui/cars/guides/flows/overview).

### What is a refresh?

Refreshes are updates to a template's content that don't increment the step count. Refreshes are almost always app-initiated. The only exception is when a user[refreshes a list with the refresh button](https://developers.google.com/cars/design/create-apps/sample-flows/refresh-with-button)on the Place List template.

What qualifies as a refresh depends on the template and whether the[Adaptive task limits](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#task-limits)feature is enabled. If this feature is enabled, the definition of what qualifies as a refresh is widened for some templates (see the following table), because the refreshes are throttled during drives to minimize distraction.

For example, with the feature enabled, updates that change the number of rows on list- or grid-based templates can be considered a refresh, as long as the title and any section names stay the same. If the feature is not enabled, changing the number of rows is a step count.

For examples of refreshes, see[Refresh versus step count example](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#example)and[Sample flows](https://developer.android.com/design/ui/cars/guides/flows/overview).

|                                        Template type                                         |           What qualifies as a refresh           |                                  What qualifies as a refresh when Adaptive task limits feature is enabled                                   |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Navigation, Sign-in\*, Long Message\*                                                        | Any content update                              | Any content update                                                                                                                          |
| List, Grid, Map, Pane, Place List (map), Place List (navigation), Route Preview, Search, Tab | See the template restrictions for each template | All updates where the layout stays the same, meaning: - Same title or tabs at the top And (on List template): <!-- --> - Same section names |
| Message                                                                                      | Only updates that don't change the title and message (for example, adding a button)                                                                                                          ||

| **Note:** \*For parked-only templates, the term refresh is typically not used, but steps are not limited, since the car is parked.

### Refresh versus step count example

In this example, the[Adaptive task limits](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#task-limits)feature is enabled, so any update with the same title qualifies as a refresh.
![Three screenshots; one update is counted as a refresh, while the other is considered a step](https://developer.android.com/static/images/design/ui/cars/foundations/plan-task-flows-3.png)

Because only the rows updated on one path, this would be considered a refresh. If Adaptive task limits isn't enabled, this will count as a step. On the other path, the title changed, which increments the step count.

### Adaptive task limits

**Adaptive task limits**is a feature that lets apps have task flows with more than 5 steps under certain controlled circumstances, such as when parked or when refreshes are being throttled while driving. Availability depends on location and discretion of vehicle OEMs (see note at right).

When this feature is**enabled**:

- **Task flows \> 5 steps are allowed while parked**(if driving, they will be paused after the 5th step and can be resumed when parked)
- **Refreshes are throttled** during drives to be less distracting, so the definition of refresh is expanded to include more types of updates (see[What is a refresh?](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#refresh)).

When the feature is**not enabled**:

- **Task flows must not exceed 5 steps**, or the app will crash
- **Refreshes are not throttled during drives**so the definition of refresh is not expanded

| **Note:** Keep in mind that this feature is not available for Japanese Automobile Manufacturers Association (JAMA)-affiliated Android Auto vehicles. Also, for AAOS, vehicle OEMs can selectively enable or disable this feature by app category. Before running any tasks that are longer than 5 steps, be sure to have your code check that this feature is enabled for the OEM and vehicle in question. To check if the feature is enabled, use the`IsAppRefreshEnabled`API.

#### How refresh throttling works

With throttled refreshes, apps can refresh the template as often as they want, but the time between the refreshes is spaced out to minimize distraction. If multiple refreshes are sent during the throttle period, the latest one is shown at the end of the period.

## Interactive maps

Design your app to include zooming and panning for navigation apps. Users can interact with maps through features (such as zooming and panning) in templates specific to navigation apps: Navigation, Route Preview, Map, and Place List (navigation).
**Note:** The Place List (map) template does not have an interactive map but does allow refresh of the list next to the map.  
Users can interact with maps using:

- **Touchscreen gestures**, such as swiping to pan
- **Taps**on specific areas of the map, such as points of interest
- **[Buttons](https://developer.android.com/design/ui/cars/guides/components/button)** on the[map action strip](https://developer.android.com/design/ui/cars/guides/components/map-action-strip)
- **A refresh button** that refreshes the information adjacent to the map (currently available only on the[Place List (map) template](https://developer.android.com/design/ui/cars/guides/templates/place-list-map-template)and the[Place List (navigation) template](https://developers.google.com/cars/design/create-apps/apps-for-drivers/templates/place-list-navigation-template))
![Mock-up of interactive map](https://developer.android.com/static/images/design/ui/cars/foundations/plan-task-flows-4.png)Users zoom and pan to locate places on the map.

Refreshing the content next to the map does not add to the[step count](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#steps-refreshes)for a task flow.