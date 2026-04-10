---
title: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/permission
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/permission
source: md.txt
---

# Permissions

Make permission requests simple, transparent, and understandable. When requesting access, apps should make it clear why a permission is needed. For more information about best practices with permissions, see[Request permissions on Wear OS](https://developer.android.com/training/wearables/data/wear-permissions).

## Watch permissions

When Wear OS needs to grant permission to a watch app, it displays a dialog asking the user to accept or reject that permission. Apps should request permissions when and where it is clear why the permission is needed. For example, apps may request permissions after providing information about a specific permission.

![](https://developer.android.com/static/wear/images/design/behaviors_permissions_1.png)

**Figure 1.**Examples of permissions for a fitness app.
| **Note:** If an app or watch face requires more than one permission at a time, the permission requests appear sequentially, one after the other.