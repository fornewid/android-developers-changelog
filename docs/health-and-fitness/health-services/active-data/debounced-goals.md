---
title: https://developer.android.com/health-and-fitness/health-services/active-data/debounced-goals
url: https://developer.android.com/health-and-fitness/health-services/active-data/debounced-goals
source: md.txt
---

Health Services now supports *debounced goals* for instantaneous metrics, such
as heart rate, distance, and speed. Debounced goals improve the user experience
for people who want to maintain a specific threshold or range---such as heart
rate---throughout their workout.

Debounced goals prevent the same event from being emitted multiple times---every
time the condition is true---over a short time period. Instead, events are emitted
only if the threshold has been continuously exceeded for a configurable period
of time, usually some number of seconds. **Duration at threshold** is the amount
of uninterrupted time the user needs to cross the specified threshold before
Health Services sends an alert event.

You can also prevent events from being emitted immediately after goal
registration. **Initial delay** is the amount of time that must pass, since goal
registration, before your app is notified.

When combined, "duration at threshold" and "initial delay" reduce the number of
false positives and repeated alerts surfaced to users if your app lets users set
fitness goals or targets.

## Case study: heart rate

A common use case for debounced goals involves heart rate zones. Heart rate
continuously fluctuates throughout an exercise, especially during
cardio-intensive activities. Without support for debouncing, an app might get
many alerts in a short period of time, such as each time the user's heart rate
exceeds or falls below the target range.

By introducing an "initial delay," you can inform Health Services to send a goal
alert only after a specified time period has passed--you can think of this as an
adjustment period. By introducing a "duration at threshold," you can take this
customization further, by specifying the amount of time that must elapse while
the user is in or out of the specified threshold for their goal to be activated.

In practice, this might involve waiting for the user to be out of their target
heart rate range for 15 seconds before your app lets them know to increase or
decrease their exercise intensity.