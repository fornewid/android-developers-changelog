---
title: https://developer.android.com/design/ui/cars/guides/flows/purchase
url: https://developer.android.com/design/ui/cars/guides/flows/purchase
source: md.txt
---

# Purchase using existing payment methods

Flows that involve purchases should be as simple and short as possible so you can minimize distraction for drivers.

Be sure to follow the[guidelines for purchase flows](https://developer.android.com/design/ui/cars/guides/ux-requirements/overview#purchase).

## Sample flow

|                                                User action                                                 |                                                                    Where action is performed                                                                     | Step count after action |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| The user is using your app. They decide to make a purchase.                                                | Landing template (not shown)                                                                                                                                     | 1                       |
| The user selects a parking location from a curated list of nearby or recently booked locations.            | List template ![List template with list of locations](https://developer.android.com/static/images/design/ui/cars/flows/purchase-1.png)                           | 2                       |
| The user views parking location details and reserves the spot; the purchase takes place in the background. | Pane template ![Pane template with more details about selected location](https://developer.android.com/static/images/design/ui/cars/flows/purchase-2.png)        | 3                       |
| The user sees confirmation and selects**Navigate**.                                                        | Message template ![Message template with one primary button and another button](https://developer.android.com/static/images/design/ui/cars/flows/purchase-3.png) | 4                       |
| A separate navigation app opens and routing begins.                                                        | Switch to navigation app ![Navigation app opens](https://developer.android.com/static/images/design/ui/cars/flows/purchase-4.png)                                | 1 (new task)            |