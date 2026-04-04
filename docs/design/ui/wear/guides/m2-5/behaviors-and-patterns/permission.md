---
title: Permissions  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/permission
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Permissions Stay organized with collections Save and categorize content based on your preferences.




Make permission requests simple, transparent, and understandable. When
requesting access, apps should make it clear why a permission is needed.
For more information about best practices with permissions, see
[Request permissions on Wear OS](/training/wearables/data/wear-permissions).

## Watch permissions

When Wear OS needs to grant permission to a watch app, it displays a dialog
asking the user to accept or reject that permission. Apps should request
permissions when and where it is clear why the permission is needed.
For example, apps may request permissions after providing information about a
specific permission.

![](/static/wear/images/design/behaviors_permissions_1.png)

**Figure 1.** Examples of permissions for a fitness app.

**Note:** If an app or watch face requires more than one permission at a time, the
permission requests appear sequentially, one after the other.