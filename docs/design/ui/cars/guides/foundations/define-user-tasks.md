---
title: https://developer.android.com/design/ui/cars/guides/foundations/define-user-tasks
url: https://developer.android.com/design/ui/cars/guides/foundations/define-user-tasks
source: md.txt
---

# Define user tasks

To create the Android for Cars version of your app, first identify vehicle-appropriate tasks -- and keep in mind the need to limit driver distraction.

## Limiting driver distraction

To help drivers focus on the road, keep these strategies in mind when designing your car app.

- **Limit information on each screen** : The templates in the app library limit the amount of information that can appear on each screen while driving. Allowable numbers of actions, images, and other elements (such as amount of text, in some cases) are described for each template. For templates with list and grid items, the maximum allowed number of items varies by vehicle and can be retrieved using the[ConstraintManager API](https://developer.android.com/training/cars/apps#constraint-manager).

- **Present only essential app content**: For the car version of your app, focus on essential, driving-related content such as frequently-used locations, rather than the full content of your app.

- **Minimize attention needed for tasks** : Simplify processes for drivers by[keeping task flows short](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#short).

- **Provide shortcuts**: Present saved user content early in task flows for quick access (for example, favorites or recently visited locations).

- **Minimize user input** : When possible, present pre-selected options and defaults, so users can easily make choices while driving. Consider enabling[voice input](https://developer.android.com/design/ui/cars/guides/components/plan-communications)while driving.

**Update template content cautiously** : Because updates to template content may take the driver's attention away from the road, some types of updates are limited. (That is, they increase the step count of the task, and steps are limited while driving.) Updates that are refreshes are less disruptive and can be throttled to minimize distraction. For details, see[What is a refresh?](https://developer.android.com/design/ui/cars/guides/ux-requirements/plan-task-flows#refresh)