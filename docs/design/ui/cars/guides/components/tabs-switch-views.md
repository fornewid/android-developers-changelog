---
title: Use tabs to switch views  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/components/tabs-switch-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Use tabs to switch views Stay organized with collections Save and categorize content based on your preferences.



Tabs help drivers quickly switch between views in your app.

You can use them to place common tasks a few taps away, minimizing distraction
so drivers can focus on the road. Implement tabs using the [Tab template](/design/ui/cars/guides/templates/tab-template).

**Note:** Remember to [keep task flows short](/design/ui/cars/guides/ux-requirements/plan-task-flows), sticking to 5 steps or fewer.

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user taps the **Home devices** tab. | Tab template with embedded List template Tab template with embedded List template with 4 items and 4 tabs at           the top | 1 |
| The user taps the desk light icon to turn off the desk light. | Tab template with embedded Grid template Tab template with 4 tabs and embedded grid of items | 1 |
| A toast appears to confirm that the desk light was turned off. | Tab template with embedded Grid template Tab template with embedded Grid template with 4 tabs and confirmation       toast **Note:** Because the content of the navigation template does not change, this is considered a refresh and does not add to the step count. | 1 |