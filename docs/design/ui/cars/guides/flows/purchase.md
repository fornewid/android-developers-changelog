---
title: Purchase using existing payment methods  |  Cars  |  Android Developers
url: https://developer.android.com/design/ui/cars/guides/flows/purchase
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Cars](https://developer.android.com/design/ui/cars)
* [Guides](https://developer.android.com/design/ui/cars/guides/foundations/design-principles)

# Purchase using existing payment methods Stay organized with collections Save and categorize content based on your preferences.




Flows that involve purchases should be as simple and short as possible so you
can minimize distraction for drivers.

Be sure to follow the [guidelines for purchase flows](/design/ui/cars/guides/ux-requirements/overview#purchase).

## Sample flow

| User action | Where action is performed | Step count after action |
| --- | --- | --- |
| The user is using your app. They decide to make a purchase. | Landing template (not shown) | 1 |
| The user selects a parking location from a curated list of nearby or recently booked locations. | List template List template with list of locations | 2 |
| The user views parking location details and reserves the spot; the purchase takes place in the background. | Pane template Pane template with more details about selected location | 3 |
| The user sees confirmation and selects **Navigate**. | Message template Message template with one primary button and another button | 4 |
| A separate navigation app opens and routing begins. | Switch to navigation app Navigation app opens | 1 (new task) |