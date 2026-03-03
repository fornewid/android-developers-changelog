---
title: https://developer.android.com/design/ui/mobile/guides/home-screen/live-updates
url: https://developer.android.com/design/ui/mobile/guides/home-screen/live-updates
source: md.txt
---

Live updates provide a summary of important updates so users can track progress
without opening the app. Users can temporarily dismiss or demote a live update
notification to a standard notification. Live update notifications should follow
notification principles for delivering brief, timely, and relevant information.
![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-update.png) **Figure 1:** Live Updates template ![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-do.webp)

### Do

Use live updates for finite or trackable experiences initiated by the user. ![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-dont.webp)

### Don't

Use live updates if there is not a clear end time for the notification.

Live updates don't work well in the following situations:

- If information in the notification is bundled from multiple applications.
- If the notification is meant to provide recommendations to users.
- If it requires bespoke visuals, animations, or unique data structures to communicate.

The following sections are recommendations to assist with consistency, clarity,
and prevent user frustration.

## Alert behavior

In order to eliminate phantom alerts and reduce notification fatigue, alert only
for critical status changes. Don't alert for minor variable adjustments. For
example, alert for driver arrived, but don't alert for a shift in ETA.

If you do alert, the UI should provide immediate visual evidence of why.

<br />

![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-critical-do.webp)

### Do

Alert for critical changes. ![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-critical-dont.webp)

### Don't

Alert for minor adjustments.

<br />

## Progress bar semantics

Show the status at a glance. If using discrete steps, clearly label the distinct
phases to show progress. If using a standard progress bar, make sure the fill
matches the remaining time or distance.
![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-progress-semantics.webp) **Figure 2:** Glanceable progress state.

## Timestamp consistency

When transitioning between views, use the same timestamp or duration format in
the collapsed Status Bar view as the expanded card view. Mismatch here can
cause unnecessary friction.
![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-contexts.webp) **Figure 3:** A matching format timestamp on both a card and a status chip.

## Template specialization

For key templates such as Rideshare, Delivery or Maps, data should be displayed
predictably. Apps within the same vertical should use similar fields for similar
data points. For example, the content title includes the most critical
information to help users scan quickly.
![](https://developer.android.com/static/images/design/ui/mobile/notifications-live-progress-usecases.webp) **Figure 4:** Three different key templates.

Explore use case templates in more detail and create your own with the
[Android UI Kit](https://www.figma.com/community/file/1478523627015571873/android-ui-kit).